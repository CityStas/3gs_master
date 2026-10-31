"""SQLite + FTS5 store for the Roblox index.

Same shape as the Three.js / Godot / Unity stores (hybrid dense + lexical, brute-force
cosine over a numpy matrix), with Roblox-relevant columns: `class_name`, `member_kind`
and `context` (server / client / shared). The full chunk text is always kept; only the
*embedding input* is clipped (see `embedder.py`).
"""
from __future__ import annotations

import json
import re
import sqlite3
import threading
import time
from pathlib import Path

import numpy as np

from .. import config
from .chunkers import Chunk

TOKEN_RE = re.compile(r"[A-Za-z_$][A-Za-z0-9_$]{1,}")
FTS_SPECIAL = re.compile(r'["*():^\-]')


def _fts_tokens(query: str) -> list[str]:
    return TOKEN_RE.findall(query)


def _quote(tok: str) -> str:
    return '"' + FTS_SPECIAL.sub(" ", tok).strip() + '"'


SCHEMA = """
PRAGMA journal_mode=WAL;
PRAGMA synchronous=NORMAL;
CREATE TABLE IF NOT EXISTS chunks (
  id TEXT PRIMARY KEY, source TEXT NOT NULL, path TEXT NOT NULL, file_type TEXT NOT NULL,
  symbol TEXT, class_name TEXT, member_kind TEXT, context TEXT,
  section TEXT, engine_version TEXT, content_hash TEXT NOT NULL, text TEXT NOT NULL,
  meta TEXT, vec BLOB
);
CREATE INDEX IF NOT EXISTS idx_chunks_path ON chunks(path);
CREATE INDEX IF NOT EXISTS idx_chunks_source ON chunks(source);
CREATE INDEX IF NOT EXISTS idx_chunks_hash ON chunks(content_hash);
CREATE VIRTUAL TABLE IF NOT EXISTS chunks_fts USING fts5(
  id UNINDEXED, text, symbol, class_name, path,
  tokenize="unicode61 remove_diacritics 2 tokenchars '_'"
);
CREATE TABLE IF NOT EXISTS files (
  path TEXT PRIMARY KEY, source TEXT NOT NULL, mtime REAL, size INTEGER, sha256 TEXT, indexed_at REAL
);
CREATE TABLE IF NOT EXISTS meta (key TEXT PRIMARY KEY, value TEXT);
"""


def _row_to_chunk(r: sqlite3.Row) -> Chunk:
    return Chunk(
        text=r["text"], source=r["source"], path=r["path"], file_type=r["file_type"],
        symbol=r["symbol"] or "", class_name=r["class_name"] or "",
        member_kind=r["member_kind"] or "", context=r["context"] or "",
        section=r["section"] or "", engine_version=r["engine_version"] or "",
        content_hash=r["content_hash"], meta=json.loads(r["meta"] or "{}"),
    )


def _ensure_fts_alignment(conn: sqlite3.Connection) -> None:
    """Guarantee the invariant `chunks_fts.rowid == chunks.rowid`.

    `id` is UNINDEXED in FTS5, so `DELETE FROM chunks_fts WHERE id=?` scans the whole
    table. Keying both tables by rowid makes the delete an O(log n) lookup on the FTS
    primary key instead of O(chunks) per row.
    """
    row = conn.execute("SELECT value FROM meta WHERE key='fts_rowid_aligned'").fetchone()
    if row and row["value"] == "1":
        return
    conn.execute("DELETE FROM chunks_fts")
    conn.execute("INSERT INTO chunks_fts(rowid,id,text,symbol,class_name,path) "
                 "SELECT rowid,id,text,symbol,class_name,path FROM chunks")
    conn.execute("INSERT OR REPLACE INTO meta(key,value) VALUES ('fts_rowid_aligned','1')")
    conn.commit()


def _open(db_path: Path) -> sqlite3.Connection:
    """Open the DB, making sure the schema exists.

    `executescript` briefly needs the write lock, so a reader that lands inside an index
    build's commit window fails with "unable to open database file". Retry briefly
    instead of failing the search outright.
    """
    conn = sqlite3.connect(str(db_path), check_same_thread=False, timeout=30.0)
    conn.row_factory = sqlite3.Row
    last: sqlite3.OperationalError | None = None
    for attempt in range(6):
        try:
            conn.executescript(SCHEMA)
            conn.commit()
            _ensure_fts_alignment(conn)
            return conn
        except sqlite3.OperationalError as exc:
            last = exc
            time.sleep(0.25 * (attempt + 1))
    conn.close()
    assert last is not None
    raise last


class IndexStore:
    def __init__(self, db_path: Path | str | None = None):
        self.db_path = Path(db_path or config.LEXICAL_DB)
        self.db_path.parent.mkdir(parents=True, exist_ok=True)
        self._lock = threading.RLock()
        self._vec_cache = None
        self._ids_cache = None
        self._conn = _open(self.db_path)

    def close(self):
        self._conn.close()

    def invalidate_cache(self):
        self._vec_cache = None
        self._ids_cache = None

    def preload(self) -> None:
        """Pull the vector matrix into RAM now instead of on the first dense search.

        The MCP server calls this on a daemon thread at startup, so the cost lands while
        the agent is still booting instead of stalling the user's first query. Errors are
        deliberately not handled here - `dense_search` reloads lazily and degrades to
        lexical, so a failed preload costs nothing.
        """
        self._load_vectors()

    def upsert(self, chunks: list[Chunk], vectors: np.ndarray | None) -> int:
        if not chunks:
            return 0
        if vectors is not None and len(vectors) != len(chunks):
            raise ValueError("vector/chunk count mismatch")
        # Chunk.id is sha1(source|path|symbol|section|content_hash). Two byte-identical
        # chunks under the same symbol+section would collide on the primary key and abort
        # the whole batch; the rows are identical anyway, so keeping the last loses nothing.
        if len({c.id for c in chunks}) != len(chunks):
            keep: dict[str, int] = {}
            for i, c in enumerate(chunks):
                keep[c.id] = i
            order = sorted(keep.values())
            chunks = [chunks[i] for i in order]
            if vectors is not None:
                vectors = np.asarray(vectors, dtype=np.float32)[order]
        with self._lock:
            cur = self._conn.cursor()
            ids = [c.id for c in chunks]
            # Drop the previous revision by rowid, not by id: `chunks_fts.rowid` mirrors
            # `chunks.rowid` and rowid is the FTS primary key, whereas an `id` lookup scans
            # the entire FTS table per row.
            for i in range(0, len(ids), 400):
                part = ids[i:i + 400]
                old = [r["rowid"] for r in cur.execute(
                    "SELECT rowid FROM chunks WHERE id IN (%s)" % ",".join("?" * len(part)),
                    part)]
                if old:
                    cur.executemany("DELETE FROM chunks_fts WHERE rowid=?",
                                    [(r,) for r in old])
            cur.executemany("DELETE FROM chunks WHERE id=?", [(x,) for x in ids])
            base = cur.execute("SELECT COALESCE(MAX(rowid),0) FROM chunks").fetchone()[0] + 1
            rows = []
            fts_rows = []
            for i, c in enumerate(chunks):
                blob = None if vectors is None else np.asarray(vectors[i], dtype=np.float32).tobytes()
                rid = base + i
                rows.append((
                    rid, c.id, c.source, c.path, c.file_type, c.symbol, c.class_name,
                    c.member_kind, c.context, c.section, c.engine_version,
                    c.content_hash, c.text, json.dumps(c.meta, ensure_ascii=False), blob,
                ))
                fts_rows.append((rid, c.id, c.text, c.symbol, c.class_name, c.path))
            cur.executemany(
                "INSERT INTO chunks(rowid,id,source,path,file_type,symbol,class_name,"
                "member_kind,context,section,engine_version,content_hash,text,meta,vec) "
                "VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)", rows)
            cur.executemany(
                "INSERT INTO chunks_fts(rowid,id,text,symbol,class_name,path) "
                "VALUES (?,?,?,?,?,?)", fts_rows)
            self._conn.commit()
        self.invalidate_cache()
        return len(chunks)

    def delete_paths(self, paths: list[str]) -> int:
        n = 0
        with self._lock:
            cur = self._conn.cursor()
            for p in paths:
                rows = [r["rowid"] for r in
                        cur.execute("SELECT rowid FROM chunks WHERE path=?", (p,))]
                if rows:
                    cur.executemany("DELETE FROM chunks_fts WHERE rowid=?",
                                    [(r,) for r in rows])
                cur.execute("DELETE FROM chunks WHERE path=?", (p,))
                cur.execute("DELETE FROM files WHERE path=?", (p,))
                n += len(rows)
            self._conn.commit()
        self.invalidate_cache()
        return n

    def record_file(self, path, source, mtime, size, sha256):
        with self._lock:
            self._conn.execute(
                "INSERT OR REPLACE INTO files VALUES (?,?,?,?,?,?)",
                (path, source, mtime, size, sha256, time.time()))
            self._conn.commit()

    def file_state(self):
        with self._lock:
            return {r["path"]: (r["mtime"], r["size"], r["sha256"])
                    for r in self._conn.execute("SELECT path,mtime,size,sha256 FROM files")}

    def source_paths(self, source: str) -> set[str]:
        """Paths this source has recorded, for pruning what fell out of the corpus.

        `delete_paths` only drops a file's *stale revision*; nothing used to remove a file
        that disappeared from disk entirely, so a corpus cleanup left orphan chunks that
        kept winning searches forever.
        """
        with self._lock:
            return {r["path"] for r in
                    self._conn.execute("SELECT path FROM files WHERE source=?", (source,))}

    def _load_vectors(self):
        if self._vec_cache is not None:
            return self._vec_cache, self._ids_cache
        rows = list(self._conn.execute(
            "SELECT id,vec FROM chunks WHERE vec IS NOT NULL ORDER BY rowid"))
        if not rows:
            # Deliberately NOT cached: `gs roblox-index --vectors` fills the table from a
            # separate process, and a cached empty matrix would keep this one lexical-only
            # for the rest of its life.
            return np.zeros((0, config.EMBED_DIM), dtype=np.float32), []
        dim = len(rows[0]["vec"]) // 4
        mat = np.empty((len(rows), dim), dtype=np.float32)
        ids = []
        for i, r in enumerate(rows):
            mat[i] = np.frombuffer(r["vec"], dtype=np.float32)
            ids.append(r["id"])
        norms = np.linalg.norm(mat, axis=1, keepdims=True)
        np.divide(mat, norms, out=mat, where=norms > 0)
        self._vec_cache = mat
        self._ids_cache = ids
        return mat, ids

    def dense_search(self, qv, top_k: int = 20, filters: dict | None = None):
        mat, ids = self._load_vectors()
        if not len(ids):
            return []
        q = np.asarray(qv, dtype=np.float32)
        n = np.linalg.norm(q)
        q = q / n if n > 0 else q
        scores = mat @ q
        k = min(max(top_k * 4, top_k), scores.shape[0])
        idx = np.argpartition(-scores, k - 1)[:k]
        idx = idx[np.argsort(-scores[idx])]
        out = [(ids[i], float(scores[i])) for i in idx]
        if filters:
            allowed = self._filter_ids(filters)
            out = [x for x in out if x[0] in allowed]
        return out[:top_k]

    def _filter_ids(self, filters):
        where, params = _build_where(filters)
        return {r["id"] for r in self._conn.execute("SELECT id FROM chunks" + where, params)}

    def lexical_search(self, query, top_k: int = 20, filters: dict | None = None):
        toks = _fts_tokens(query)
        if not toks:
            return []
        where, params = _build_where(filters, alias="c")
        # Symbol/class/path columns are weighted hard: an exact API name
        # ("SetNetworkOwner", "Humanoid.Died", "MarketplaceService") is the whole point of
        # the lexical half.
        for expr in (" AND ".join(_quote(t) for t in toks),
                     " OR ".join(_quote(t) for t in toks)):
            sql = (f"SELECT f.id AS id, bm25(chunks_fts, 0.0,1.0,8.0,4.0,1.0) AS score "
                   f"FROM chunks_fts f JOIN chunks c ON c.rowid=f.rowid "
                   f"WHERE chunks_fts MATCH ? {where} ORDER BY score LIMIT ?")
            try:
                rows = list(self._conn.execute(sql, [expr, *params, top_k]))
            except sqlite3.OperationalError:
                rows = []
            if rows:
                return [(r["id"], -float(r["score"])) for r in rows]
        return []

    def get_chunks(self, ids):
        out = {}
        if not ids:
            return out
        with self._lock:
            for i in range(0, len(ids), 400):
                part = ids[i:i + 400]
                q = "SELECT * FROM chunks WHERE id IN (%s)" % (",".join("?" * len(part)))
                for r in self._conn.execute(q, part):
                    out[r["id"]] = _row_to_chunk(r)
        return out

    def chunks_without_vectors(self, limit: int = 0) -> list[tuple[str, str]]:
        """`(id, text)` for every chunk whose `vec` is NULL, oldest rowid first.

        These are the chunks stored while the embedding server was down. Without a repair
        pass they stay lexical-only forever, because a re-index sees an unchanged
        mtime+sha and skips the file.
        """
        sql = "SELECT id, text FROM chunks WHERE vec IS NULL ORDER BY rowid"
        if limit:
            sql += f" LIMIT {int(limit)}"
        with self._lock:
            return [(r["id"], r["text"]) for r in self._conn.execute(sql)]

    def set_vectors(self, ids: list[str], vectors: np.ndarray) -> int:
        """Fill in `vec` for existing chunks. Text and FTS rows are left untouched."""
        if not ids:
            return 0
        if len(ids) != len(vectors):
            raise ValueError("vector/id count mismatch")
        rows = [(np.asarray(vectors[i], dtype=np.float32).tobytes(), cid)
                for i, cid in enumerate(ids)]
        with self._lock:
            self._conn.executemany("UPDATE chunks SET vec=? WHERE id=?", rows)
            self._conn.commit()
        self.invalidate_cache()
        return len(rows)

    def stats(self):
        total = self._conn.execute("SELECT COUNT(*) c FROM chunks").fetchone()["c"]
        files = self._conn.execute("SELECT COUNT(*) c FROM files").fetchone()["c"]
        vecs = self._conn.execute(
            "SELECT COUNT(*) c FROM chunks WHERE vec IS NOT NULL").fetchone()["c"]
        by_source = {r["source"]: r["c"] for r in self._conn.execute(
            "SELECT source,COUNT(*) c FROM chunks GROUP BY source")}
        by_type = {r["file_type"]: r["c"] for r in self._conn.execute(
            "SELECT file_type,COUNT(*) c FROM chunks GROUP BY file_type")}
        return {"chunks": total, "files": files, "with_vectors": vecs,
                "by_source": by_source, "by_type": by_type, "db": str(self.db_path)}


def _build_where(filters, alias=""):
    if not filters:
        return "", []
    pre = alias + "." if alias else ""
    clauses = []
    params = []
    for key, val in filters.items():
        if key in {"source", "file_type", "class_name", "member_kind", "context",
                   "engine_version", "symbol"}:
            if isinstance(val, (list, tuple)):
                clauses.append(f"{pre}{key} IN ({','.join('?' * len(val))})")
                params.extend(val)
            else:
                clauses.append(f"{pre}{key}=?")
                params.append(val)
        elif key == "path_prefix":
            clauses.append(f"{pre}path LIKE ?")
            params.append(f"{val}%")
        elif key == "path":
            clauses.append(f"{pre}path=?")
            params.append(val)
    return (" AND " + " AND ".join(clauses), params) if clauses else ("", [])
