"""Индексатор: discovery -> chunking -> embedding -> upsert.

Инкрементальный: файл с неизменившимся sha256 не трогается.
"""
from __future__ import annotations

import hashlib
import sys
import time
from dataclasses import dataclass
from pathlib import Path

import numpy as np

from .. import config
from .chunkers import Chunk, chunk_file, chunk_class_ref, chunk_plain
from .embedder import Embedder
from .store import IndexStore


@dataclass
class IndexReport:
    scanned: int = 0
    changed: int = 0
    skipped: int = 0
    chunks: int = 0
    vectors: int = 0
    seconds: float = 0.0
    sources: dict = None

    def __post_init__(self):
        if self.sources is None:
            self.sources = {}

    def line(self) -> str:
        return (f"scanned={self.scanned} changed={self.changed} skipped={self.skipped} "
                f"chunks={self.chunks} vectors={self.vectors} time={self.seconds:.1f}s")


def _sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for block in iter(lambda: f.read(1 << 20), b""):
            h.update(block)
    return h.hexdigest()


def _iter_project_files(root: Path):
    for p in root.rglob("*"):
        if not p.is_file():
            continue
        if any(part in config.PROJECT_SKIP_DIRS for part in p.parts):
            continue
        if p.suffix.lower() not in config.PROJECT_TEXT_EXTS:
            continue
        try:
            if p.stat().st_size > config.MAX_INDEX_FILE_BYTES:
                continue
        except OSError:
            continue
        yield p


def _iter_knowledge_files(root: Path):
    if not root.exists():
        return
    for p in root.rglob("*"):
        if p.is_file() and p.suffix.lower() in (".md", ".txt", ".gd", ".json"):
            try:
                if p.stat().st_size > config.MAX_INDEX_FILE_BYTES:
                    continue
            except OSError:
                continue
            yield p


class Indexer:
    def __init__(self, store: IndexStore | None = None, embedder: Embedder | None = None,
                 verbose: bool = True):
        self.store = store or IndexStore()
        self.embedder = embedder or Embedder()
        self.verbose = verbose

    def _log(self, msg: str) -> None:
        if self.verbose:
            print(msg, file=sys.stderr, flush=True)

    # ------------------------------------------------------------------
    def index_file(self, path: Path, rel_path: str, source: str,
                   state: dict, force: bool = False) -> tuple[list[Chunk], bool]:
        try:
            st = path.stat()
        except OSError:
            return [], False
        prev = state.get(rel_path)
        if prev and not force:
            if abs(prev[0] - st.st_mtime) < 1e-6 and prev[1] == st.st_size:
                return [], False
        sha = _sha256(path)
        if prev and prev[2] == sha and not force:
            self.store.record_file(rel_path, source, st.st_mtime, st.st_size, sha)
            return [], False

        if path.suffix.lower() == ".xml" and source == "official_docs":
            chunks = chunk_class_ref(path.read_text(encoding="utf-8", errors="replace"), rel_path, source)
        else:
            chunks = chunk_file(path, rel_path, source)
        return chunks, True

    # ------------------------------------------------------------------
    def index_source(self, root: Path, source: str, file_iter, force: bool = False,
                     path_prefix: str = "") -> IndexReport:
        rep = IndexReport()
        state = self.store.file_state()
        t0 = time.time()
        batch_chunks: list[Chunk] = []
        batch_texts: list[str] = []
        BATCH = 256

        def flush():
            nonlocal batch_chunks, batch_texts
            if not batch_chunks:
                return
            try:
                vecs = np.asarray(self.embedder.embed_many(batch_texts), dtype=np.float32)
            except Exception as e:  # noqa: BLE001
                self._log(f"  ! embedding недоступен, пишу без векторов: {e}")
                vecs = None
            n = self.store.upsert(batch_chunks, vecs)
            rep.chunks += n
            if vecs is not None:
                rep.vectors += len(vecs)
            batch_chunks, batch_texts = [], []

        for path in file_iter(root):
            rel = path_prefix + path.relative_to(root).as_posix()
            rep.scanned += 1
            try:
                chunks, changed = self.index_file(path, rel, source, state, force=force)
            except Exception as e:  # noqa: BLE001
                self._log(f"  ! {rel}: {e}")
                continue
            if not changed:
                rep.skipped += 1
                continue
            rep.changed += 1
            self.store.delete_paths([rel])
            if not chunks:
                continue
            batch_chunks.extend(chunks)
            batch_texts.extend(c.text for c in chunks)
            if len(batch_chunks) >= BATCH:
                flush()
            st = path.stat()
            self.store.record_file(rel, source, st.st_mtime, st.st_size, _sha256(path))
            if rep.changed % 200 == 0:
                self._log(f"  {source}: {rep.changed} изменённых, {rep.chunks} чанков...")
        flush()
        rep.seconds = time.time() - t0
        return rep

    # ------------------------------------------------------------------
    def run(self, project_root: Path | None = None, force: bool = False,
            only: list[str] | None = None) -> dict:
        only = only or ["official_docs", "project", "cookbook", "troubleshooting",
                        "anti_patterns", "external_assets"]
        reports: dict[str, IndexReport] = {}
        t0 = time.time()

        if "official_docs" in only:
            self._log("[1/5] official Godot 4.7 docs")
            reports["official_docs"] = self.index_source(
                config.GODOT_DOCS_DIR, "official_docs",
                lambda r: (p for p in r.rglob("*") if p.is_file()
                           and p.suffix.lower() in (".xml", ".md", ".rst")),
                force=force,
            )
            self._log("  " + reports["official_docs"].line())

        if "project" in only:
            root = project_root or config.godot_project_root()
            if root and root.exists():
                self._log(f"[2/5] project: {root}")
                reports["project"] = self.index_source(root, "project", _iter_project_files, force=force)
                self._log("  " + reports["project"].line())
            else:
                self._log("[2/5] project: не задан (GDM_PROJECT), пропуск")

        for name, folder in (("cookbook", config.COOKBOOK_DIR),
                             ("troubleshooting", config.TROUBLESHOOTING_DIR),
                             ("anti_patterns", config.ANTIPATTERNS_DIR),
                             ("external_assets", config.EXTERNAL_ASSETS_DIR)):
            if name not in only:
                continue
            self._log(f"[*] {name}")
            reports[name] = self.index_source(folder, name, _iter_knowledge_files, force=force)
            self._log("  " + reports[name].line())

        total = IndexReport(seconds=time.time() - t0)
        for r in reports.values():
            total.scanned += r.scanned
            total.changed += r.changed
            total.skipped += r.skipped
            total.chunks += r.chunks
            total.vectors += r.vectors
        return {
            "total": total.line(),
            "seconds": total.seconds,
            "chunks_added": total.chunks,
            "vectors_added": total.vectors,
            "files_changed": total.changed,
            "files_skipped": total.skipped,
            "per_source": {k: v.line() for k, v in reports.items()},
            "stats": self.store.stats(),
        }
