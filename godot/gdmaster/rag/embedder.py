"""Клиент embedding-сервера (bge-m3 через llama-server).

Отдельный процесс от LLM — как требует спека: embedding не должен
отнимать VRAM у основной модели (bge-m3 считаем на CPU, -ngl 0).
"""
from __future__ import annotations

import json
import os
import time
import urllib.error
import urllib.request
from concurrent.futures import ThreadPoolExecutor, as_completed

from .. import config


class EmbeddingError(RuntimeError):
    pass


class Embedder:
    def __init__(self, base_url: str | None = None, dim: int | None = None, timeout: float = 120.0):
        self.base_url = (base_url or config.EMBED_BASE_URL).rstrip("/")
        self.dim = dim or config.EMBED_DIM
        self.timeout = timeout
        self._model_id: str | None = None
        # Локальный embedding-сервер обязан ходить напрямую. Если в среде выставлен
        # HTTP_PROXY (на этой машине он есть), urllib по умолчанию отправит запрос
        # на 127.0.0.1:8081 через прокси и получит 502 вместо ответа.
        self._opener = urllib.request.build_opener(urllib.request.ProxyHandler({}))

    # -- низкий уровень ----------------------------------------------------
    def _post(self, path: str, payload: dict) -> dict:
        data = json.dumps(payload).encode("utf-8")
        req = urllib.request.Request(
            self.base_url + path, data=data,
            headers={"Content-Type": "application/json"}, method="POST",
        )
        try:
            with self._opener.open(req, timeout=self.timeout) as r:
                return json.loads(r.read().decode("utf-8"))
        except urllib.error.HTTPError as e:
            body = e.read().decode("utf-8", "replace")[:500]
            raise EmbeddingError(f"HTTP {e.code} от {self.base_url}{path}: {body}") from e
        except (urllib.error.URLError, TimeoutError, OSError) as e:
            raise EmbeddingError(
                f"embedding-сервер недоступен на {self.base_url}. "
                f"Запусти serve-embed.cmd. Причина: {e}"
            ) from e

    # -- публичный API -----------------------------------------------------
    def health(self) -> dict:
        try:
            with self._opener.open(self.base_url + "/health", timeout=5) as r:
                return json.loads(r.read().decode("utf-8"))
        except Exception as e:  # noqa: BLE001
            return {"status": "down", "error": str(e)}

    def wait_ready(self, timeout: float = 120.0) -> bool:
        t0 = time.time()
        while time.time() - t0 < timeout:
            if self.health().get("status") == "ok":
                return True
            time.sleep(1.0)
        return False

    def _detect_dim(self) -> int:
        v = self.embed_one("dimension probe")
        return len(v)

    def embed_one(self, text: str) -> list[float]:
        return self.embed_many([text])[0]

    def embed_many(self, texts: list[str], batch: int | None = None) -> list[list[float]]:
        """Батчевое эмбеддинг с параллельными запросами.

        llama-server держит несколько слотов (n_slots), поэтому параллельные
        HTTP-запросы реально ускоряют CPU-инференс в разы.
        """
        if not texts:
            return []
        batch = batch or config.EMBED_BATCH
        chunks = [texts[i:i + batch] for i in range(0, len(texts), batch)]
        workers = max(1, int(os.environ.get("GDM_EMBED_WORKERS", "4")))
        workers = min(workers, len(chunks))

        results: list[list[list[float]] | None] = [None] * len(chunks)
        if workers == 1:
            for i, part in enumerate(chunks):
                results[i] = self._embed_batch(part)
        else:
            with ThreadPoolExecutor(max_workers=workers) as ex:
                futs = {ex.submit(self._embed_batch, part): i for i, part in enumerate(chunks)}
                for f in as_completed(futs):
                    results[futs[f]] = f.result()
        out: list[list[float]] = []
        for r in results:
            out.extend(r or [])
        return out

    def _embed_batch(self, part: list[str]) -> list[list[float]]:
        part = [t if t.strip() else " " for t in part]
        resp = self._post("/v1/embeddings", {"input": part})
        data = sorted(resp.get("data", []), key=lambda d: d.get("index", 0))
        if len(data) != len(part):
            raise EmbeddingError(
                f"сервер вернул {len(data)} векторов на {len(part)} входов"
            )
        return [d["embedding"] for d in data]

    def embed_query(self, text: str) -> list[float]:
        # bge-m3 не требует instruction-префикса для запроса
        return self.embed_one(text.strip())
