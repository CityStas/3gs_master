from pathlib import Path
import sys
import tempfile

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

import numpy as np
from threejs.rag.chunkers import chunk_file
from threejs.rag.store import IndexStore
from threejs.rag.retriever import Retriever
from threejs.rag.embedder import EmbeddingError
from threejs.assets import naming

class DummyEmbedder:
    def health(self): return {"status":"ok"}
    def embed_query(self, q):
        return [1.0,0.0,0.0]

def test_chunk_and_store():
    with tempfile.TemporaryDirectory() as td:
        p=Path(td)/"main.ts"
        p.write_text("import * as THREE from 'three';\nclass Player extends THREE.Object3D {}\n",encoding='utf-8')
        chunks=chunk_file(p,"main.ts","project")
        assert any(c.symbol=="Player" for c in chunks)
        db=Path(td)/"index.db"; store=IndexStore(db)
        vec=np.zeros((len(chunks),3),dtype=np.float32); vec[:,0]=1
        store.upsert(chunks,vec)
        r=Retriever(store=store,embedder=DummyEmbedder())
        hits=r.search("Player Object3D",top_k=3)
        assert hits and hits[0].chunk.path=="main.ts"
        store.close()


def test_slug_is_derived_from_the_request():
    """Regression: the tokenizer used to be `[^a-z0-9]+`, which ate Cyrillic before
    transliteration and collapsed every Russian prompt to the literal `asset`."""
    assert naming.derive_name("Создай синего мохнатого монстра") == "sinego-mohnatogo-monstra"
    assert naming.derive_name("blue mossy monster") == "blue-mossy-monster"
    assert naming.derive_name("a low-poly crystal shard") == "low-poly-crystal-shard"
    assert naming.derive_name("Нарисуй деревянный бочонок", "barrel") == "barrel"
    # a prompt made only of stop-words must still produce something identifying
    assert naming.derive_name("создай модель") == "sozday-model"
    # nothing usable at all -> stable fallback, never an empty name
    assert naming.derive_name("") == "asset"
    assert naming.derive_name("   ") == "asset"
    # never a ComfyUI counter
    assert not naming.derive_name("monster").startswith("comfy")


def test_unique_path_does_not_overwrite():
    with tempfile.TemporaryDirectory() as td:
        d = Path(td)
        a = naming.unique_path(d, "monster", "", ".glb")
        a.write_bytes(b"1")
        b = naming.unique_path(d, "monster", "", ".glb")
        assert a.name == "monster.glb" and b.name == "monster-2.glb"
        c = naming.unique_path(d, "monster", "-nobg", ".png")
        assert c.name == "monster-nobg.png"


def test_upsert_survives_duplicate_chunk_ids():
    """Regression: minified bundles (examples/jsm/libs/*.min.js) contain byte-identical
    functions, so two chunks can share an id. The batch used to die on
    `UNIQUE constraint failed: chunks.id` and take the whole source down with it."""
    from threejs.rag.chunkers import Chunk
    with tempfile.TemporaryDirectory() as td:
        store = IndexStore(Path(td) / "index.db")
        dup = Chunk("function t(){}", "official_source", "libs/x.min.js", "js",
                    symbol="x.t", section="function")
        other = Chunk("function n(){}", "official_source", "libs/x.min.js", "js",
                      symbol="x.n", section="function")
        batch = [dup, other, dup, dup]          # 3 copies of `dup`
        vec = np.ones((len(batch), 3), dtype=np.float32)
        stored = store.upsert(batch, vec)
        assert stored == 2, stored
        assert store.stats()["chunks"] == 2
        assert store.stats()["with_vectors"] == 2
        # vectors must stay aligned with chunks after dedup
        mat, ids = store._load_vectors()
        assert len(ids) == 2 and mat.shape == (2, 3)
        store.close()


class _TooLargeOnce:
    """Stub server that models llama.cpp's rejection: an input whose *token* count
    exceeds `limit` comes back as HTTP 500 and kills the whole request."""
    def __init__(self, limit):
        self.limit = limit
        self.calls = []

    def __call__(self, path, payload):
        texts = payload["input"]
        self.calls.append([len(t) for t in texts])
        if max(len(t) for t in texts) > self.limit:   # 1 char == 1 token, worst case
            raise EmbeddingError(
                "HTTP 500 from http://x/v1/embeddings: "
                '{"error":{"message":"input (12002 tokens) is too large to process. '
                'increase the physical batch size (current batch size: 8192)"}}')
        return {"data": [{"index": i, "embedding": [0.1] * 4} for i in range(len(texts))]}


def test_embedder_clips_oversized_inputs():
    """Regression: one oversized input returned HTTP 500 and cost the entire 32-item
    batch (and with it all 256 vectors of the flush) -> 1958 chunks indexed without
    vectors. Clipping to max_chars must keep the rest of the batch alive."""
    from threejs.rag.embedder import Embedder
    stub = _TooLargeOnce(limit=200)
    e = Embedder(max_chars=100)
    e._post = stub

    short = ["f%d(){}" % i for i in range(31)]
    huge = "x" * 5000                       # denser than max_chars
    out = e._embed_batch(short + [huge])

    assert len(out) == 32, len(out)          # nothing was dropped
    assert all(len(v) == 4 for v in out)
    assert len(stub.calls) == 1              # clipping alone was enough
    assert len(stub.calls[0]) == 32
    assert max(stub.calls[0]) == 100         # the 5000-char input was clipped


def test_embedder_falls_back_per_item_when_clipping_is_not_enough():
    """If even the clipped text is rejected, the batch must degrade to per-item retries
    that halve the clip, instead of losing all 32 embeddings."""
    from threejs.rag.embedder import Embedder
    stub = _TooLargeOnce(limit=200)          # stricter than max_chars
    e = Embedder(max_chars=1000)
    e._post = stub

    out = e._embed_batch(["y" * 3000 for _ in range(3)])

    assert len(out) == 3, out
    assert len(stub.calls[0]) == 3           # one batched attempt
    assert min(stub.calls[0]) == 1000        # clipped on the first try
    assert any(len(c) == 1 for c in stub.calls[1:])   # then one request per item
    # the clip was halved until the stub accepted it (1000 -> 500 -> 250 -> 125)
    assert min(min(c) for c in stub.calls[1:]) == 125


def test_embedder_does_not_retry_a_dead_server():
    """A non-size failure must propagate: retrying an outage item-by-item would turn
    one clear error into 32 slow ones and hide the fact that the server is down."""
    from threejs.rag.embedder import Embedder
    e = Embedder(max_chars=100)
    calls = []

    def dead(path, payload):
        calls.append(1)
        raise EmbeddingError("embedding server unavailable at http://x: connection refused")

    e._post = dead
    try:
        e._embed_batch(["a", "b", "c"])
    except EmbeddingError:
        pass
    else:
        raise AssertionError("expected EmbeddingError to propagate")
    assert len(calls) == 1, calls          # one attempt, not three


if __name__ == "__main__":
    import sys, traceback
    fns = [v for k, v in sorted(globals().items()) if k.startswith("test_") and callable(v)]
    failed = 0
    for fn in fns:
        try:
            fn()
            print("PASS", fn.__name__)
        except Exception:
            failed += 1
            print("FAIL", fn.__name__)
            traceback.print_exc()
    print("\n%d/%d passed" % (len(fns) - failed, len(fns)))
    sys.exit(1 if failed else 0)
