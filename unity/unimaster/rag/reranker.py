"""Cross-encoder reranker client for `llama-server --rerank` (bge-reranker-v2-m3).

The hybrid retriever fuses two *independent* scores - cosine between two embeddings, and
BM25 between a query and a chunk. Neither ever reads the query and the passage together,
so a chunk that merely repeats the query's words can outrank the passage that actually
answers it. A cross-encoder reads the pair jointly and is much better at that judgement,
so it runs as a second pass over the fused shortlist.

Strictly optional. Every failure path raises `RerankError` and the caller falls back to
the RRF order, because a dead reranker must cost relevance, never answers.
"""
from __future__ import annotations

import json
import urllib.error
import urllib.request

from .. import config


class RerankError(RuntimeError):
    pass


def _clip(text: str, limit: int) -> str:
    # An empty string is not a valid input for the server; a single space is.
    t = text if text.strip() else " "
    return t if len(t) <= limit else t[:limit]


class Reranker:
    def __init__(self, base_url: str | None = None, timeout: float | None = None,
                 max_chars: int | None = None, batch: int | None = None):
        self.base_url = (base_url or config.RERANK_BASE_URL).rstrip("/")
        self.timeout = float(timeout or config.RERANK_TIMEOUT)
        self.max_chars = int(max_chars or config.RERANK_MAX_CHARS)
        self.batch = int(batch or config.RERANK_BATCH)
        self._opener = urllib.request.build_opener(urllib.request.ProxyHandler({}))

    def _post(self, path: str, payload: dict) -> dict:
        data = json.dumps(payload).encode()
        req = urllib.request.Request(self.base_url + path, data=data,
                                     headers={"Content-Type": "application/json"}, method="POST")
        try:
            with self._opener.open(req, timeout=self.timeout) as r:
                return json.loads(r.read().decode())
        except urllib.error.HTTPError as e:
            body = ""
            try:
                body = e.read().decode(errors="replace")[:300]
            except Exception:  # noqa: BLE001
                pass
            raise RerankError(f"HTTP {e.code} from {self.base_url}{path}: {body}") from e
        except (urllib.error.URLError, TimeoutError, OSError) as e:
            raise RerankError(f"reranker unavailable at {self.base_url}: {e}") from e

    def health(self) -> dict:
        try:
            with self._opener.open(self.base_url + "/health", timeout=5) as r:
                return json.loads(r.read().decode())
        except Exception as e:  # noqa: BLE001
            return {"status": "down", "error": str(e)}

    def rerank(self, query: str, docs: list[str]) -> list[float]:
        """One score per document, in the input order.

        The server returns raw logits, not probabilities - they are unbounded and
        routinely negative, so only their *order* means anything. Callers must sort by
        them, never threshold on them.
        """
        if not docs:
            return []
        scores = [0.0] * len(docs)
        for i in range(0, len(docs), self.batch):
            part = docs[i:i + self.batch]
            resp = self._post("/v1/rerank", {
                "query": query,
                "documents": [_clip(d, self.max_chars) for d in part],
            })
            results = resp.get("results") or []
            if len(results) != len(part):
                raise RerankError(f"rerank count mismatch: {len(results)} != {len(part)}")
            for r in results:
                scores[i + int(r["index"])] = float(r["relevance_score"])
        return scores
