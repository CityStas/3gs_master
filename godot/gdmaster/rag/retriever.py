"""Гибридный retrieval: dense (bge-m3) + lexical (FTS5/BM25) + RRF-фьюжн.

Второй проход — кросс-энкодер bge-reranker-v2-m3 (`reranker.py`, :8083). Он читает
запрос и пассаж СОВМЕСТНО, чего ни косинус, ни BM25 не делают, и потому поднимает
настоящий ответ над чанком, который лишь повторяет слова запроса. Включается ручкой
`GDM_RERANK_ENABLED` (по умолчанию включён); при мёртвом реранкере порядок RRF
сохраняется, а сбой учитывается в `rerank_failures`.
"""
from __future__ import annotations

from dataclasses import dataclass

from .. import config
from .chunkers import Chunk
from .embedder import Embedder
from .reranker import Reranker
from .store import IndexStore

# приоритет источников истины (§20 спеки): project > official docs > cookbook
SOURCE_PRIORITY = {
    "project": 1.0,
    "official_docs": 0.92,
    "cookbook": 0.88,
    "troubleshooting": 0.86,
    "anti_patterns": 0.84,
    # Знания о внешних ассетах — справочные, не про текущий проект. Держим ниже
    # cookbook, чтобы описание источников не перебивало ответ про сам код.
    "external_assets": 0.82,
    "rules": 1.0,
}


@dataclass
class Hit:
    id: str
    score: float
    chunk: Chunk
    dense_rank: int | None = None
    lexical_rank: int | None = None
    dense_score: float | None = None
    lexical_score: float | None = None
    rerank_score: float | None = None

    def to_dict(self, max_chars: int = 2600) -> dict:
        c = self.chunk
        text = c.text
        if len(text) > max_chars:
            text = text[:max_chars] + "\n... [truncated]"
        return {
            "score": round(self.score, 5),
            "source": c.source,
            "path": c.path,
            "file_type": c.file_type,
            "symbol": c.symbol,
            "class": c.class_name,
            "extends": c.extends,
            "section": c.section,
            "node_path": c.node_path,
            "content": text,
        }


class Retriever:
    def __init__(self, store: IndexStore | None = None, embedder: Embedder | None = None,
                 reranker: Reranker | None = None):
        self.store = store or IndexStore()
        self.embedder = embedder or Embedder()
        # None отключает второй проход целиком; search() тогда возвращает ровно то же,
        # что возвращал до появления реранкера.
        self.reranker = reranker if reranker is not None else (
            Reranker() if config.RERANK_ENABLED else None)
        # Сбои считаются, а не просто глотаются: иначе мёртвый эмбеддер или реранкер
        # молча деградирует каждый ответ и нигде это не видно.
        self.dense_failures = 0
        self.last_dense_error: str | None = None
        self.rerank_failures = 0
        self.last_rerank_error: str | None = None

    # ------------------------------------------------------------------
    def search(
        self,
        query: str,
        top_k: int | None = None,
        filters: dict | None = None,
        dense_k: int | None = None,
        lexical_k: int | None = None,
        alpha: float = 1.0,
    ) -> list[Hit]:
        top_k = top_k or config.FINAL_TOP_K
        dense_k = dense_k or config.DENSE_TOP_K
        lexical_k = lexical_k or config.LEXICAL_TOP_K

        dense_hits: list[tuple[str, float]] = []
        if alpha > 0:
            try:
                qv = self.embedder.embed_query(query)
                dense_hits = self.store.dense_search(qv, top_k=dense_k, filters=filters)
            except Exception as e:  # noqa: BLE001 — dense деградирует, lexical остаётся
                self.dense_failures += 1
                self.last_dense_error = f"{type(e).__name__}: {e}"
                dense_hits = []

        lex_hits = self.store.lexical_search(query, top_k=lexical_k, filters=filters)

        # 1-based, только для отчёта: to_dict() их не отдаёт, бюджет промпта не тронут.
        d_rank = {cid: i + 1 for i, (cid, _s) in enumerate(dense_hits)}
        l_rank = {cid: i + 1 for i, (cid, _s) in enumerate(lex_hits)}
        d_score = dict(dense_hits)
        l_score = dict(lex_hits)

        fused = self._rrf(dense_hits, lex_hits, k=config.RRF_K, alpha=alpha)

        # Второй проход только по короткому списку: кросс-энкодер стоит O(пар), а ответ
        # лежит глубоко внутри RERANK_TOP_K — на корпусе Unity настоящий ответ стоял на
        # 46-м месте лексики, так что список обязан быть длинным.
        order = fused[:config.RERANK_TOP_K] if self.reranker is not None else fused
        chunks = self.store.get_chunks([i for i, _ in order])

        r_score: dict[str, float] = {}
        if self.reranker is not None:
            ids = [cid for cid, _s in order if cid in chunks]
            try:
                r_score = dict(zip(ids, self.reranker.rerank(
                    query, [chunks[cid].text for cid in ids])))
                order = sorted(r_score.items(), key=lambda kv: -kv[1])
            except Exception as e:  # noqa: BLE001 — реранкер не имеет права отменять ответ
                self.rerank_failures += 1
                self.last_rerank_error = f"{type(e).__name__}: {e}"
                r_score = {}
                order = fused[:config.RERANK_TOP_K]

        out: list[Hit] = []
        for cid, score in order:
            ch = chunks.get(cid)
            if ch is None:
                continue
            # Приоритет источников (§20): проект важнее cookbook, cookbook — важнее
            # общих примеров. Множитель мал, чтобы не перебить релевантность.
            score *= SOURCE_PRIORITY.get(ch.source, 0.9)
            out.append(Hit(id=cid, score=score, chunk=ch,
                           dense_rank=d_rank.get(cid), lexical_rank=l_rank.get(cid),
                           dense_score=d_score.get(cid), lexical_score=l_score.get(cid),
                           rerank_score=r_score.get(cid)))
        out.sort(key=lambda h: -h.score)
        return out[:top_k]

    # ------------------------------------------------------------------
    @staticmethod
    def _rrf(dense: list[tuple[str, float]], lexical: list[tuple[str, float]],
             k: int = 60, alpha: float = 1.0) -> list[tuple[str, float]]:
        scores: dict[str, float] = {}
        for rank, (cid, _s) in enumerate(dense):
            scores[cid] = scores.get(cid, 0.0) + alpha * (1.0 / (k + rank + 1))
        for rank, (cid, _s) in enumerate(lexical):
            scores[cid] = scores.get(cid, 0.0) + (1.0 / (k + rank + 1))
        return sorted(scores.items(), key=lambda kv: -kv[1])


def format_context(hits: list[Hit], max_total_chars: int = 14000) -> str:
    """Собрать компактный контекст для LLM: только релевантные passages."""
    parts: list[str] = []
    used = 0
    for h in hits:
        c = h.chunk
        head = f"[{c.source}] {c.path}"
        if c.symbol:
            head += f" :: {c.symbol}"
        body = c.text
        if len(body) > 2600:
            body = body[:2600] + "\n... [truncated]"
        block = f"--- {head} ---\n{body}"
        if used + len(block) > max_total_chars:
            break
        parts.append(block)
        used += len(block)
    return "\n\n".join(parts)
