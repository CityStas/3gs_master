from __future__ import annotations

import json
import os
import re
import time
import urllib.error
import urllib.request
from concurrent.futures import ThreadPoolExecutor, as_completed

from .. import config

# A single embedding input larger than the server's physical batch (`-ub`, and the
# per-slot context `-c / -np`) is rejected with HTTP 500 and takes the whole batch of
# EMBED_BATCH texts down with it. Minified bundles are the offenders: a 12 000-char
# slice of `chevrotain.module.min.js` tokenises to 12 002 tokens. Clipping the text
# before it is embedded costs nothing - the stored chunk keeps its full text, and the
# first 6 000 characters are what the embedding is really about anyway.
EMBED_MAX_CHARS = int(os.environ.get("THREE_EMBED_MAX_CHARS", "6000"))
_TOO_LARGE = re.compile(r"too large to process|larger than|exceed", re.I)


class EmbeddingError(RuntimeError):
    pass


def _clip(text: str, limit: int) -> str:
    t = text if text.strip() else " "
    return t if len(t) <= limit else t[:limit]


class Embedder:
    def __init__(self, base_url: str | None = None, dim: int | None = None, timeout: float = 120.0,
                 max_chars: int | None = None):
        self.base_url=(base_url or config.EMBED_BASE_URL).rstrip("/")
        self.dim=dim or config.EMBED_DIM
        self.timeout=timeout
        self.max_chars=int(max_chars or EMBED_MAX_CHARS)
        self._opener=urllib.request.build_opener(urllib.request.ProxyHandler({}))

    def _post(self, path: str, payload: dict) -> dict:
        data=json.dumps(payload).encode()
        req=urllib.request.Request(self.base_url+path,data=data,headers={"Content-Type":"application/json"},method="POST")
        try:
            with self._opener.open(req, timeout=self.timeout) as r:
                return json.loads(r.read().decode())
        except urllib.error.HTTPError as e:
            body=""
            try: body=e.read().decode(errors="replace")[:300]
            except Exception: pass
            raise EmbeddingError(f"HTTP {e.code} from {self.base_url}{path}: {body}") from e
        except (urllib.error.URLError, TimeoutError, OSError) as e:
            raise EmbeddingError(f"embedding server unavailable at {self.base_url}: {e}") from e

    def health(self)->dict:
        try:
            with self._opener.open(self.base_url+"/health", timeout=5) as r:
                return json.loads(r.read().decode())
        except Exception as e:
            return {"status":"down","error":str(e)}

    def embed_many(self, texts:list[str], batch:int|None=None)->list[list[float]]:
        if not texts: return []
        batch=batch or config.EMBED_BATCH
        parts=[texts[i:i+batch] for i in range(0,len(texts),batch)]
        workers=min(max(1,int(os.environ.get("THREE_EMBED_WORKERS",str(config.EMBED_WORKERS)))),len(parts))
        results=[None]*len(parts)
        if workers==1:
            for i,p in enumerate(parts): results[i]=self._embed_batch(p)
        else:
            with ThreadPoolExecutor(max_workers=workers) as ex:
                futs={ex.submit(self._embed_batch,p):i for i,p in enumerate(parts)}
                for f in as_completed(futs): results[futs[f]]=f.result()
        return [v for part in results if part for v in part]

    def _embed_batch(self, part:list[str])->list[list[float]]:
        try:
            return self._embed_request(part, self.max_chars)
        except EmbeddingError as e:
            # Distinguish "this input is too big" from "the server is gone". Only the
            # former is worth retrying item by item; retrying a dead server 32 times
            # just turns one clear failure into 32 slow ones.
            if not _TOO_LARGE.search(str(e)):
                raise
            return [self._embed_one(x) for x in part]

    def _embed_request(self, part:list[str], limit:int)->list[list[float]]:
        resp=self._post("/v1/embeddings",{"input":[_clip(x, limit) for x in part]})
        data=sorted(resp.get("data",[]),key=lambda x:x.get("index",0))
        if len(data)!=len(part): raise EmbeddingError("embedding count mismatch")
        return [x["embedding"] for x in data]

    def _embed_one(self, text:str)->list[float]:
        """Embed a single text, halving the clip until the server accepts it.

        The floor is 64 characters: below that a "too large" rejection cannot be about
        the input any more, it means the server itself is broken - and swallowing that
        would hide a real outage.
        """
        limit=self.max_chars
        while True:
            try:
                return self._embed_request([text], limit)[0]
            except EmbeddingError as e:
                if not _TOO_LARGE.search(str(e)) or limit<=64:
                    raise
                limit//=2

    def embed_query(self,text:str)->list[float]:
        return self.embed_many([text.strip()])[0]
