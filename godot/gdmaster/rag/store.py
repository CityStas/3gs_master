"""Хранилище индекса: dense-векторы + SQLite FTS5 (BM25).

Реализация по умолчанию — numpy + SQLite в одном файле:
  * один writer (индексатор), много reader'ов (MCP-сервер) — WAL;
  * никаких внешних сервисов и эксклюзивных локов на каталог;
  * brute-force cosine по 1024-d на десятках тысяч чанков — единицы мс.

Qdrant остаётся опциональным бэкендом (GDM_VECTOR_BACKEND=qdrant) — см.
`QdrantVectorStore` в конце файла. По умолчанию он не используется, потому
что Qdrant local mode (path=...) держит эксклюзивный лок на каталог и
конфликтует с постоянно живущим RAG MCP-сервером.
"""
from __future__ import annotations

import json
import os
import re
import sqlite3
import threading
import time
from pathlib import Path

import numpy as np

from .. import config
from .chunkers import Chunk

# --- токенизация для FTS ------------------------------------------------------
_TOKEN_RE = re.compile(r"[A-Za-z_][A-Za-z0-9_]{1,}")
_FTS_SPECIAL = re.compile(r'["*():^\-]')


def _fts_tokens(query: str) -> list[str]:
    return [t for t in _TOKEN_RE.findall(query)]


def _quote(tok: str) -> str:
    return '"' + _FTS_SPECIAL.sub(" ", tok).strip() + '"'


SCHEMA = """
PRAGMA journal_mode=WAL;
PRAGMA synchronous=NORMAL;

CREATE TABLE IF NOT EXISTS chunks (
    id              TEXT PRIMARY KEY,
    source          TEXT NOT NULL,
    path            TEXT NOT NULL,
    file_type       TEXT NOT NULL,
    symbol          TEXT,
    class_name      TEXT,
    extends         TEXT,
    node_type       TEXT,
    scene_path      TEXT,
    node_path       TEXT,
    section         TEXT,
    engine_version  TEXT,
    content_hash    TEXT NOT NULL,
    text            TEXT NOT NULL,
    meta            TEXT,
    vec             BLOB
);
CREATE INDEX IF NOT EXISTS idx_chunks_path ON chunks(path);
CREATE INDEX IF NOT EXISTS idx_chunks_source ON chunks(source);
CREATE INDEX IF NOT EXISTS idx_chunks_hash ON chunks(content_hash);

CREATE VIRTUAL TABLE IF NOT EXISTS chunks_fts USING fts5(
    id UNINDEXED,
    text,
    symbol,
    class_name,
    path,
    tokenize = "unicode61 remove_diacritics 2 tokenchars '_'"
);

CREATE TABLE IF NOT EXISTS files (
    path        TEXT PRIMARY KEY,
    source      TEXT NOT NULL,
    mtime       REAL,
    size        INTEGER,
    sha256      TEXT,
    indexed_at  REAL
);
CREATE TABLE IF NOT EXISTS meta (key TEXT PRIMARY KEY, value TEXT);
"""


def _row_to_chunk(row: sqlite3.Row) -> Chunk:
    return Chunk(
        text=row["text"], source=row["source"], path=row["path"],
        file_type=row["file_type"], symbol=row["symbol"] or "",
        class_name=row["class_name"] or "", extends=row["extends"] or "",
        node_type=row["node_type"] or "", scene_path=row["scene_path"] or "",
        node_path=row["node_path"] or "", section=row["section"] or "",
        engine_version=row["engine_version"] or "", content_hash=row["content_hash"],
        meta=json.loads(row["meta"] or "{}"),
    )


def _ensure_fts_alignment(conn: sqlite3.Connection) -> None:
    """Гарантировать инвариант `chunks_fts.rowid == chunks.rowid`.

    Зачем: `id` в FTS5 объявлен UNINDEXED, поэтому `DELETE FROM chunks_fts WHERE id=?`
    не может воспользоваться полнотекстовым индексом — он сканирует всю таблицу.
    Старый `upsert` делал это по разу на чанк, то есть O(чанки x корпус) на пакет:
    терпимо на паре тысяч документов и безнадёжно на большом корпусе (на Unity
    измерено 15 чанков/с против индекса 200 МБ и 35k чанков/с против пустого).
    Ключ по rowid превращает это удаление в поиск O(log n) по первичному ключу FTS.

    Индекс, собранный до этой правки, имеет независимые rowid, и join по rowid
    вернул бы для лексического попадания чужую строку — поэтому выравниваем один раз
    и отмечаем это в `meta`.
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
    """Открыть БД, убедившись, что схема на месте.

    `executescript` неявно коммитит, то есть на миг требует блокировку записи.
    Соединение, открытое, когда индексатор в середине коммита, падает с
    "unable to open database file", хотя файл прекрасно читается. Reader здесь —
    это собственный `gd_rag_search` агента. Короткий повтор вместо отказа поиска.
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
        self._vec_cache: np.ndarray | None = None
        self._ids_cache: list[str] | None = None
        self._conn = _open(self.db_path)

    # -- lifecycle ---------------------------------------------------------
    def close(self) -> None:
        with self._lock:
            self._conn.close()

    def invalidate_cache(self) -> None:
        with self._lock:
            self._vec_cache = None
            self._ids_cache = None

    # -- запись ------------------------------------------------------------
    def upsert(self, chunks: list[Chunk], vectors: np.ndarray | None) -> int:
        if not chunks:
            return 0
        if vectors is not None and len(vectors) != len(chunks):
            raise ValueError("число векторов не совпадает с числом чанков")
        # `Chunk.id` = sha1(source|path|symbol|section|content_hash), поэтому два
        # БАЙТ-в-БАЙТ одинаковых чанка под тем же symbol+section дают один id и
        # роняют весь пакет на UNIQUE-констрейнте `chunks.id` - вместе с ним падает
        # весь source. Строки при этом идентичны, так что оставить одну ничего не теряет.
        # У threejs и unity эта защита была, у godot её не было - расхождение.
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
            # Снять старые версии этих же id (переиндексация изменившегося файла).
            # Удаляем по rowid, а не по id: `chunks_fts.rowid` повторяет `chunks.rowid`
            # (см. `_ensure_fts_alignment`) и rowid — первичный ключ FTS, тогда как
            # выборка по `id` сканирует всю FTS-таблицу на каждую строку.
            for i in range(0, len(ids), 400):
                part = ids[i:i + 400]
                old = [r["rowid"] for r in cur.execute(
                    "SELECT rowid FROM chunks WHERE id IN (%s)" % ",".join("?" * len(part)),
                    part)]
                if old:
                    cur.executemany("DELETE FROM chunks_fts WHERE rowid=?",
                                    [(r,) for r in old])
            cur.executemany("DELETE FROM chunks WHERE id = ?", [(i,) for i in ids])
            base = cur.execute("SELECT COALESCE(MAX(rowid),0) FROM chunks").fetchone()[0] + 1
            rows = []
            fts_rows = []
            for i, c in enumerate(chunks):
                blob = None
                if vectors is not None:
                    blob = np.asarray(vectors[i], dtype=np.float32).tobytes()
                rid = base + i
                rows.append((
                    rid, c.id, c.source, c.path, c.file_type, c.symbol, c.class_name,
                    c.extends, c.node_type, c.scene_path, c.node_path, c.section,
                    c.engine_version, c.content_hash, c.text,
                    json.dumps(c.meta, ensure_ascii=False), blob,
                ))
                fts_rows.append((rid, c.id, c.text, c.symbol, c.class_name, c.path))
            cur.executemany(
                "INSERT INTO chunks (rowid,id,source,path,file_type,symbol,class_name,extends,"
                "node_type,scene_path,node_path,section,engine_version,content_hash,text,meta,vec) "
                "VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)", rows,
            )
            cur.executemany(
                "INSERT INTO chunks_fts (rowid,id,text,symbol,class_name,path) VALUES (?,?,?,?,?,?)",
                fts_rows,
            )
            self._conn.commit()
        self.invalidate_cache()
        return len(chunks)

    def delete_paths(self, paths: list[str]) -> int:
        if not paths:
            return 0
        with self._lock:
            cur = self._conn.cursor()
            n = 0
            for p in paths:
                old = [r["rowid"] for r in cur.execute("SELECT rowid FROM chunks WHERE path = ?", (p,))]
                if old:
                    cur.executemany("DELETE FROM chunks_fts WHERE rowid = ?", [(r,) for r in old])
                cur.execute("DELETE FROM chunks WHERE path = ?", (p,))
                cur.execute("DELETE FROM files WHERE path = ?", (p,))
                n += len(old)
            self._conn.commit()
        self.invalidate_cache()
        return n

    def record_file(self, path: str, source: str, mtime: float, size: int, sha256: str) -> None:
        import time as _t
        with self._lock:
            self._conn.execute(
                "INSERT OR REPLACE INTO files (path,source,mtime,size,sha256,indexed_at) VALUES (?,?,?,?,?,?)",
                (path, source, mtime, size, sha256, _t.time()),
            )
            self._conn.commit()

    def file_state(self) -> dict[str, tuple[float, int, str]]:
        with self._lock:
            return {
                r["path"]: (r["mtime"], r["size"], r["sha256"])
                for r in self._conn.execute("SELECT path,mtime,size,sha256 FROM files")
            }

    # -- dense -------------------------------------------------------------
    def _load_vectors(self) -> tuple[np.ndarray, list[str]]:
        with self._lock:
            if self._vec_cache is not None and self._ids_cache is not None:
                return self._vec_cache, self._ids_cache
            rows = list(self._conn.execute(
                "SELECT id, vec FROM chunks WHERE vec IS NOT NULL ORDER BY rowid"
            ))
            if not rows:
                # Намеренно НЕ кэшируем: `gs godot-index --vectors` наполняет таблицу
                # из другого процесса, и закэшированная пустая матрица заставила бы
                # этот процесс до конца жизни отвечать только лексикой, без единой
                # ошибки в логах. Пока таблица пуста, повторный запрос бесплатен.
                return np.zeros((0, config.EMBED_DIM), dtype=np.float32), []
            dim = len(rows[0]["vec"]) // 4
            mat = np.empty((len(rows), dim), dtype=np.float32)
            ids: list[str] = []
            for i, r in enumerate(rows):
                mat[i] = np.frombuffer(r["vec"], dtype=np.float32)
                ids.append(r["id"])
            # нормализуем один раз — cosine превращается в dot
            norms = np.linalg.norm(mat, axis=1, keepdims=True)
            np.divide(mat, norms, out=mat, where=norms > 0)
            self._vec_cache, self._ids_cache = mat, ids
            return mat, ids

    def dense_search(self, query_vec: list[float] | np.ndarray, top_k: int = 20,
                     filters: dict | None = None) -> list[tuple[str, float]]:
        mat, ids = self._load_vectors()
        if mat.shape[0] == 0:
            return []
        q = np.asarray(query_vec, dtype=np.float32)
        n = np.linalg.norm(q)
        if n > 0:
            q = q / n
        scores = mat @ q
        k = min(max(top_k * 4, top_k), scores.shape[0])
        idx = np.argpartition(-scores, k - 1)[:k]
        idx = idx[np.argsort(-scores[idx])]
        out = [(ids[i], float(scores[i])) for i in idx]
        if filters:
            allowed = self._filter_ids(filters)
            out = [(i, s) for i, s in out if i in allowed]
        return out[:top_k]

    def _filter_ids(self, filters: dict) -> set[str]:
        where, params = _build_where(filters)
        with self._lock:
            rows = self._conn.execute(f"SELECT id FROM chunks {where}", params)
            return {r["id"] for r in rows}

    # -- lexical -----------------------------------------------------------
    # Веса колонок FTS5: (id UNINDEXED, text, symbol, class_name, path).
    # Без весов BM25 не различает точное совпадение символа API от простого
    # упоминания класса в длинном тексте — запрос "CharacterBody3D move_and_slide"
    # выдавал get_position_delta. symbol весит в 8 раз больше текста.
    BM25_WEIGHTS = "0.0, 1.0, 8.0, 4.0, 1.0"

    def lexical_search(self, query: str, top_k: int = 20, filters: dict | None = None) -> list[tuple[str, float]]:
        toks = _fts_tokens(query)
        if not toks:
            return []
        and_expr = " AND ".join(_quote(t) for t in toks)
        or_expr = " OR ".join(_quote(t) for t in toks)
        where, params = _build_where(filters, alias="c")
        for expr, mode in ((and_expr, "and"), (or_expr, "or")):
            sql = (
                f"SELECT f.id AS id, bm25(chunks_fts, {self.BM25_WEIGHTS}) AS score "
                "FROM chunks_fts f JOIN chunks c ON c.rowid = f.rowid "
                f"WHERE chunks_fts MATCH ? {where} "
                "ORDER BY score LIMIT ?"
            )
            try:
                with self._lock:
                    rows = list(self._conn.execute(sql, [expr, *params, top_k]))
            except sqlite3.OperationalError:
                rows = []
            if rows or mode == "or":
                # bm25 возвращает отрицательные значения: меньше = релевантнее
                return [(r["id"], -float(r["score"])) for r in rows]
        return []

    # -- чтение ------------------------------------------------------------
    def get_chunks(self, ids: list[str]) -> dict[str, Chunk]:
        if not ids:
            return {}
        out: dict[str, Chunk] = {}
        with self._lock:
            for i in range(0, len(ids), 400):
                part = ids[i:i + 400]
                q = "SELECT * FROM chunks WHERE id IN (%s)" % ",".join("?" * len(part))
                for r in self._conn.execute(q, part):
                    out[r["id"]] = _row_to_chunk(r)
        return out

    def stats(self) -> dict:
        with self._lock:
            total = self._conn.execute("SELECT COUNT(*) c FROM chunks").fetchone()["c"]
            files = self._conn.execute("SELECT COUNT(*) c FROM files").fetchone()["c"]
            with_vec = self._conn.execute("SELECT COUNT(*) c FROM chunks WHERE vec IS NOT NULL").fetchone()["c"]
            by_source = {
                r["source"]: r["c"] for r in
                self._conn.execute("SELECT source, COUNT(*) c FROM chunks GROUP BY source")
            }
            by_type = {
                r["file_type"]: r["c"] for r in
                self._conn.execute("SELECT file_type, COUNT(*) c FROM chunks GROUP BY file_type")
            }
        return {
            "chunks": total, "files": files, "with_vectors": with_vec,
            "by_source": by_source, "by_type": by_type,
            "db": str(self.db_path),
        }

    def list_paths(self, source: str | None = None) -> list[str]:
        with self._lock:
            if source:
                rows = self._conn.execute("SELECT DISTINCT path FROM chunks WHERE source=?", (source,))
            else:
                rows = self._conn.execute("SELECT DISTINCT path FROM chunks")
            return [r["path"] for r in rows]


def _build_where(filters: dict | None, alias: str = "") -> tuple[str, list]:
    if not filters:
        return "", []
    pre = f"{alias}." if alias else ""
    clauses, params = [], []
    for key, val in filters.items():
        if key in ("source", "file_type", "class_name", "extends", "engine_version", "symbol", "node_type"):
            if isinstance(val, (list, tuple)):
                clauses.append(f"{pre}{key} IN ({','.join('?' * len(val))})")
                params.extend(val)
            else:
                clauses.append(f"{pre}{key} = ?")
                params.append(val)
        elif key == "path_prefix":
            clauses.append(f"{pre}path LIKE ?")
            params.append(f"{val}%")
        elif key == "path":
            clauses.append(f"{pre}path = ?")
            params.append(val)
    if not clauses:
        return "", []
    return " AND " + " AND ".join(clauses), params


# --------------------------------------------------------------------------
# Опциональный бэкенд Qdrant (GDM_VECTOR_BACKEND=qdrant)
# --------------------------------------------------------------------------

class QdrantVectorStore:
    """Тонкая обёртка над qdrant-client local mode.

    Не используется по умолчанию: local mode держит эксклюзивный лок на
    каталог, а RAG MCP-сервер живёт постоянно. Включать, только если
    индексация и поиск гарантированно не пересекаются по времени.
    """

    def __init__(self, path: Path | None = None, collection: str = "godot_chunks"):
        from qdrant_client import QdrantClient  # локальный импорт: опциональная зависимость
        self.client = QdrantClient(path=str(path or config.QDRANT_DIR))
        self.collection = collection

    def upsert(self, chunks: list[Chunk], vectors: np.ndarray) -> int:
        from qdrant_client import models as qm
        if not chunks:
            return 0
        self.client.upsert(
            collection_name=self.collection,
            points=[
                qm.PointStruct(id=_uuid_from(c.id), vector=vectors[i].tolist(), payload=c.payload())
                for i, c in enumerate(chunks)
            ],
        )
        return len(chunks)


def _uuid_from(s: str) -> str:
    import uuid
    return str(uuid.UUID(hashlib_sha1_hex(s)))


def hashlib_sha1_hex(s: str) -> str:
    import hashlib
    h = hashlib.sha1(s.encode("utf-8")).hexdigest()
    return f"{h[:8]}-{h[8:12]}-{h[12:16]}-{h[16:20]}-{h[20:32]}"


def open_store() -> IndexStore:
    backend = os.environ.get("GDM_VECTOR_BACKEND", "sqlite").lower()
    if backend == "qdrant":
        # dense в Qdrant, метаданные/lexical всё равно в SQLite
        pass
    return IndexStore()
