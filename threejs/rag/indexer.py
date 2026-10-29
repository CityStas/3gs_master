from __future__ import annotations
import hashlib, sys, time
from dataclasses import dataclass, field
from pathlib import Path
import numpy as np
from .. import config
from .chunkers import Chunk, chunk_file
from .embedder import Embedder
from .store import IndexStore

SOURCE_BY_DIR = {
    "official_docs": config.OFFICIAL_DOCS_DIR,
    "official_source": config.OFFICIAL_SOURCE_DIR,
    "cookbook": config.COOKBOOK_DIR,
    "troubleshooting": config.TROUBLESHOOTING_DIR,
    "anti_patterns": config.ANTIPATTERNS_DIR,
    "rules": config.RULES_DIR,
}

# Extensions accepted per source. `project` keeps the wide web set; the corpora are
# narrower on purpose - we do not want stray assets or configs polluting the index.
EXTS_BY_SOURCE = {
    "project": config.PROJECT_TEXT_EXTS,
    "official_docs": {".md", ".txt", ".html", ".htm", ".json"},
    "official_source": {".js", ".mjs", ".cjs", ".ts", ".wgsl", ".glsl"},
    "cookbook": {".md", ".txt"},
    "troubleshooting": {".md", ".txt"},
    "anti_patterns": {".md", ".txt"},
    "rules": {".md", ".txt"},
}
DEFAULT_EXTS = {".md", ".txt", ".html", ".htm", ".json"}


@dataclass
class IndexReport:
    source: str = ""
    scanned: int = 0
    changed: int = 0
    skipped: int = 0
    chunks: int = 0
    vectors: int = 0
    errors: int = 0
    embed_errors: int = 0
    seconds: float = 0.0
    sources: dict = field(default_factory=dict)

    def line(self) -> str:
        base = (f"{self.source:16s} scanned={self.scanned} changed={self.changed} "
                f"skipped={self.skipped} chunks={self.chunks} vectors={self.vectors} "
                f"time={self.seconds:.1f}s")
        if self.errors or self.embed_errors:
            base += f" errors={self.errors} embed_errors={self.embed_errors}"
        return base


def _sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for b in iter(lambda: f.read(1 << 20), b""):
            h.update(b)
    return h.hexdigest()


def _iter_files(root: Path, exts):
    """Yield indexable files under `root`.

    The skip-list is matched against the path *relative to root*. Matching against the
    absolute path (the original bug) meant any ancestor directory named `build`, `data`,
    `dist` ... silently disabled the whole corpus with no warning.
    """
    root = Path(root)
    if not root.exists():
        return
    try:
        root_res = root.resolve()
    except OSError:
        return
    for p in root.rglob("*"):
        if not p.is_file() or p.suffix.lower() not in exts:
            continue
        try:
            rel_parts = p.resolve().relative_to(root_res).parts
        except (OSError, ValueError):
            continue
        if any(part in config.PROJECT_SKIP_DIRS for part in rel_parts[:-1]):
            continue
        try:
            if p.stat().st_size > config.MAX_INDEX_FILE_BYTES:
                continue
        except OSError:
            continue
        yield p


class Indexer:
    def __init__(self, store=None, embedder=None, verbose=True):
        self.store = store or IndexStore()
        self.embedder = embedder or Embedder()
        self.verbose = verbose

    def _log(self, msg):
        if self.verbose:
            print(msg, file=sys.stderr, flush=True)

    def index_file(self, path, rel_path, source, state, force=False):
        try:
            st = path.stat()
        except OSError:
            return [], False
        prev = state.get(rel_path)
        if prev and not force and abs(prev[0] - st.st_mtime) < 1e-6 and prev[1] == st.st_size:
            return [], False
        sha = _sha256(path)
        if prev and prev[2] == sha and not force:
            self.store.record_file(rel_path, source, st.st_mtime, st.st_size, sha)
            return [], False
        return chunk_file(path, rel_path, source), True

    def _flush(self, batch: list[Chunk], texts: list[str], rep: IndexReport) -> None:
        """Embed and store one batch. On embedding failure store text-only.

        Losing the vectors degrades recall for that batch but keeps the corpus intact -
        far better than aborting the whole run because the embedding server blinked.
        """
        vec = None
        try:
            vec = np.asarray(self.embedder.embed_many(texts), dtype=np.float32)
            if vec.shape[0] != len(batch):
                raise ValueError(f"embedding count mismatch: {vec.shape[0]} != {len(batch)}")
        except Exception as e:  # noqa: BLE001
            self._log(f"  ! embeddings unavailable ({type(e).__name__}: {e}); "
                      f"storing {len(batch)} chunks without vectors")
            vec = None
            rep.embed_errors += 1
        stored = self.store.upsert(batch, vec)
        rep.chunks += stored
        if vec is not None:
            rep.vectors += stored

    def index_source(self, root, source, force=False) -> IndexReport:
        rep = IndexReport(source=source)
        exts = EXTS_BY_SOURCE.get(source, DEFAULT_EXTS)
        state = self.store.file_state()
        t0 = time.time()
        batch: list[Chunk] = []
        texts: list[str] = []

        for path in _iter_files(root, exts):
            rep.scanned += 1
            try:
                rel = path.relative_to(root).as_posix()
            except ValueError:
                continue
            try:
                chunks, changed = self.index_file(path, rel, source, state, force)
            except Exception as e:  # noqa: BLE001 - one bad file must not kill the run
                rep.errors += 1
                self._log(f"  ! {rel}: {type(e).__name__}: {e}")
                continue
            if not changed:
                rep.skipped += 1
                continue

            rep.changed += 1
            # Drop the previous revision of this path. Chunk ids embed a content hash, so
            # without this the old rows survive forever and the model keeps seeing stale code.
            self.store.delete_paths([rel])

            batch.extend(chunks)
            texts.extend(c.text for c in chunks)
            rep.sources[source] = rep.sources.get(source, 0) + len(chunks)
            if len(batch) >= 256:
                self._flush(batch, texts, rep)
                batch, texts = [], []
            try:
                st = path.stat()
                self.store.record_file(rel, source, st.st_mtime, st.st_size, _sha256(path))
            except OSError:
                pass

        if batch:
            self._flush(batch, texts, rep)
        rep.seconds = time.time() - t0
        return rep

    def run(self, project_root: Path | None = None, force=False, only=None) -> list[IndexReport]:
        reports = []
        if project_root:
            reports.append(self.index_source(project_root, "project", force))
        for source, root in SOURCE_BY_DIR.items():
            if only and source not in only:
                continue
            reports.append(self.index_source(root, source, force))
        return reports
