"""Клиент кросс-энкодер-реранкера (`llama-server --rerank`, bge-reranker-v2-m3, :8083).

Гибридный ретривер складывает два НЕЗАВИСИМЫХ скора: косинус между двумя эмбеддингами
и BM25 между запросом и чанком. Ни один из них не читает запрос и пассаж вместе,
поэтому чанк, который просто повторяет слова запроса, легко обгоняет пассаж, который
на вопрос отвечает. Кросс-энкодер читает пару совместно и различает это заметно лучше,
поэтому работает вторым проходом по короткому списку после RRF.

Строго опционален: любая ошибка поднимает `RerankError`, и ретривер возвращается к
порядку RRF. Мёртвый реранкер обязан стоить релевантности, но не ответов.
"""
from __future__ import annotations

import json
import urllib.error
import urllib.request

from .. import config


class RerankError(RuntimeError):
    pass


def _clip(text: str, limit: int) -> str:
    # Пустая строка — невалидный вход для сервера; один пробел — валидный.
    t = text if text.strip() else " "
    return t if len(t) <= limit else t[:limit]


class Reranker:
    def __init__(self, base_url: str | None = None, timeout: float | None = None,
                 max_chars: int | None = None, batch: int | None = None):
        self.base_url = (base_url or config.RERANK_BASE_URL).rstrip("/")
        self.timeout = float(timeout or config.RERANK_TIMEOUT)
        self.max_chars = int(max_chars or config.RERANK_MAX_CHARS)
        self.batch = int(batch or config.RERANK_BATCH)
        # Прокси обходится: 127.0.0.1 наружу не ходит никогда.
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
            except Exception:
                pass
            raise RerankError(f"HTTP {e.code} от {self.base_url}{path}: {body}") from e
        except (urllib.error.URLError, TimeoutError, OSError) as e:
            raise RerankError(f"реранкер недоступен на {self.base_url}: {e}") from e

    def health(self) -> dict:
        try:
            with self._opener.open(self.base_url + "/health", timeout=5) as r:
                return json.loads(r.read().decode())
        except Exception as e:
            return {"status": "down", "error": str(e)}

    def rerank(self, query: str, docs: list[str]) -> list[float]:
        """По одному скору на документ, в порядке входа.

        Сервер отдаёт сырые логиты, а не вероятности: они не ограничены и регулярно
        отрицательны, так что смысл имеет только их ПОРЯДОК. Сортировать по ним —
        никогда не сравнивать с порогом.
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
                raise RerankError(f"реранкер вернул {len(results)} скоров на {len(part)} документов")
            for r in results:
                scores[i + int(r["index"])] = float(r["relevance_score"])
        return scores
