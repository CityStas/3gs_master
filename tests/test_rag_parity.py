"""Cross-stack parity tests: Three.js, Godot and Unity must behave IDENTICALLY.

The three RAG stacks are separate code trees (`threejs/`, `godot/gdmaster/`,
`unity/unimaster/`) that share no code, so every fix has to be applied three times and
every divergence is invisible until it bites on one engine only. That already happened:
the FTS `rowid` fix landed in Unity, then in Three.js, and Godot kept deleting FTS rows by
`id` - i.e. the O(chunks x corpus) full scan - for two more revisions.

So this file is deliberately NOT organised per stack. Each test loops over all three and
asserts the SAME contract, with the stack name in the failure message. A fix that lands in
one tree and not the others turns red here.

Three contracts are covered:

1. **Store / FTS layout** - `chunks_fts.rowid` mirrors `chunks.rowid`, a legacy index is
   healed on open, an empty vector matrix is never cached, and a lexical hit after a
   delete+reinsert cycle still returns its own row (rowids get reused).
2. **Reranker client** - one score per document in input order, long documents clipped,
   empty documents replaced, batching, and a hard error when the server answers short.
3. **Retriever integration** - a dead reranker degrades to the RRF order and is *counted*,
   and a live one actually reorders the fused shortlist.

Run:  .venv\\Scripts\\python.exe tests\\test_rag_parity.py
"""
from pathlib import Path
import importlib
import sqlite3
import sys
import tempfile

import numpy as np

ROOT = Path(__file__).resolve().parents[1]
for _p in (ROOT, ROOT / "godot", ROOT / "unity"):
    if str(_p) not in sys.path:
        sys.path.insert(0, str(_p))

# (label, import prefix) - three independent package trees, one contract.
STACKS = [
    ("threejs", "threejs.rag"),
    ("godot", "gdmaster.rag"),
    ("unity", "unimaster.rag"),
]

DIM = 4
FTS_COLS = "(rowid,id,text,symbol,class_name,path)"


def _mods(prefix):
    return (importlib.import_module(prefix + ".chunkers"),
            importlib.import_module(prefix + ".store"),
            importlib.import_module(prefix + ".retriever"),
            importlib.import_module(prefix + ".reranker"))


def _chunk(chunkers, text, path, symbol, section="s", source="project"):
    """Build a Chunk using only the columns all three dataclasses share."""
    return chunkers.Chunk(text=text, source=source, path=path, file_type="cs",
                          symbol=symbol, class_name="Player", section=section)


def _batch(chunkers, path, n=3, tag="a"):
    out = []
    for i in range(n):
        sym = f"Method{tag.upper()}{i}"
        out.append(_chunk(chunkers, f"void {sym}() {{ }} // {tag}", path, sym,
                          section=f"s{i}"))
    return out


def _aligned(conn):
    tot = conn.execute("SELECT COUNT(*) FROM chunks").fetchone()[0]
    joined = conn.execute("SELECT COUNT(*) FROM chunks_fts f "
                          "JOIN chunks c ON c.rowid=f.rowid").fetchone()[0]
    return tot == joined


def _orphans(conn):
    return conn.execute("SELECT COUNT(*) FROM chunks_fts f "
                        "LEFT JOIN chunks c ON c.rowid=f.rowid "
                        "WHERE c.rowid IS NULL").fetchone()[0]


def _fail(stack, msg):
    raise AssertionError("[%s] %s" % (stack, msg))


# =========================================================== 1. store / FTS layout
def test_store_keeps_fts_rowids_aligned_on_every_stack():
    """`chunks_fts.rowid` must mirror `chunks.rowid` after upsert and after delete.

    Deleting by `id` is *correct* but scans the whole FTS table per row (`id` is
    UNINDEXED in FTS5), which is what turned the Unity corpus build into days.
    """
    for stack, prefix in STACKS:
        chunkers, store_mod, _r, _k = _mods(prefix)
        with tempfile.TemporaryDirectory() as td:
            st = store_mod.IndexStore(Path(td) / "lexical.db")
            try:
                st.upsert(_batch(chunkers, "a.cs", 5), None)
                if not _aligned(st._conn):
                    _fail(stack, "first insert broke the rowid invariant")
                if _orphans(st._conn):
                    _fail(stack, "first insert left orphan FTS rows")

                # Byte-identical re-store must REPLACE, not duplicate.
                st.upsert(_batch(chunkers, "a.cs", 5), None)
                n = st._conn.execute("SELECT COUNT(*) FROM chunks").fetchone()[0]
                if n != 5:
                    _fail(stack, "re-storing identical chunks duplicated them (%d)" % n)
                if not _aligned(st._conn) or _orphans(st._conn):
                    _fail(stack, "re-store broke the rowid invariant")

                # A second file must not disturb the first one's rows.
                st.upsert(_batch(chunkers, "b.cs", 4, tag="b"), None)
                n = st._conn.execute("SELECT COUNT(*) FROM chunks").fetchone()[0]
                if n != 9:
                    _fail(stack, "second file produced %d chunks, expected 9" % n)

                st.delete_paths(["a.cs"])
                n = st._conn.execute("SELECT COUNT(*) FROM chunks").fetchone()[0]
                nf = st._conn.execute("SELECT COUNT(*) FROM chunks_fts").fetchone()[0]
                if (n, nf) != (4, 4):
                    _fail(stack, "delete_paths left chunks/fts = %d/%d, expected 4/4" % (n, nf))
                if _orphans(st._conn):
                    _fail(stack, "delete_paths left orphan FTS rows")
            finally:
                st.close()


def test_store_realigns_a_legacy_index_on_every_stack():
    """An index built before the rowid change must be repaired on open.

    Pre-fix indexes have FTS rowids independent of `chunks.rowid`, so a rowid join
    would return the WRONG row for a lexical hit. Silently returning a plausible but
    unrelated chunk is worse than an exception.
    """
    for stack, prefix in STACKS:
        chunkers, store_mod, _r, _k = _mods(prefix)
        with tempfile.TemporaryDirectory() as td:
            db = Path(td) / "lexical.db"
            st = store_mod.IndexStore(db)
            try:
                st.upsert(_batch(chunkers, "a.cs", 4), None)
                c = st._conn
                c.execute("DELETE FROM chunks_fts")
                c.execute("INSERT INTO chunks_fts%s "
                          "SELECT rowid+1000,id,text,symbol,class_name,path FROM chunks"
                          % FTS_COLS)
                c.execute("DELETE FROM meta WHERE key='fts_rowid_aligned'")
                c.commit()
                if _aligned(c):
                    _fail(stack, "fixture did not reproduce the legacy layout")
            finally:
                st.close()

            st2 = store_mod.IndexStore(db)
            try:
                if not _aligned(st2._conn):
                    _fail(stack, "legacy index was not realigned on open")
                if _orphans(st2._conn):
                    _fail(stack, "legacy realign left orphan FTS rows")
                nf = st2._conn.execute("SELECT COUNT(*) FROM chunks_fts").fetchone()[0]
                if nf != 4:
                    _fail(stack, "legacy realign produced %d FTS rows, expected 4" % nf)
            finally:
                st2.close()


def test_store_does_not_cache_an_empty_vector_matrix_on_every_stack():
    """A cached empty matrix would keep a long-lived reader lexical-only forever.

    `gs *-index --vectors` fills the table from a SEPARATE process. The agent's MCP
    server is long-lived, so if it cached "no vectors" from before that run it would
    never see them - with no error anywhere to explain the empty dense half.
    """
    for stack, prefix in STACKS:
        chunkers, store_mod, _r, _k = _mods(prefix)
        with tempfile.TemporaryDirectory() as td:
            db = Path(td) / "lexical.db"
            st = store_mod.IndexStore(db)
            try:
                st.upsert(_batch(chunkers, "a.cs", 3), None)
                if st.dense_search(np.zeros(DIM, dtype=np.float32), top_k=3) != []:
                    _fail(stack, "a text-only index returned dense hits")

                # The `--vectors` run, simulated from a second connection.
                c = sqlite3.connect(str(db))
                c.execute("UPDATE chunks SET vec=?",
                          (np.ones(DIM, dtype=np.float32).tobytes(),))
                c.commit()
                c.close()

                hits = st.dense_search(np.ones(DIM, dtype=np.float32), top_k=3)
                if len(hits) != 3:
                    _fail(stack, "reader kept a cached empty vector matrix (%d hits)" % len(hits))
            finally:
                st.close()


def test_lexical_hit_returns_its_own_row_after_rowid_reuse_on_every_stack():
    """Rowids are reused after a delete, so a stale FTS row would shadow the new one.

    This is the case a plain `c.id = f.id` join cannot catch in a fresh index but a
    `c.rowid = f.rowid` join must survive.
    """
    for stack, prefix in STACKS:
        chunkers, store_mod, _r, _k = _mods(prefix)
        with tempfile.TemporaryDirectory() as td:
            st = store_mod.IndexStore(Path(td) / "lexical.db")
            try:
                st.upsert(_batch(chunkers, "a.cs", 3), None)
                st.delete_paths(["a.cs"])
                b = _batch(chunkers, "b.cs", 3, tag="b")
                st.upsert(b, None)

                for c in b:
                    hits = st.lexical_search(c.symbol, top_k=5)
                    if not hits:
                        _fail(stack, "lexical_search(%r) found nothing" % c.symbol)
                    if hits[0][0] != c.id:
                        _fail(stack, "lexical_search(%r) returned %s, expected its own row %s"
                              % (c.symbol, hits[0][0], c.id))
            finally:
                st.close()


# ============================================================== 2. reranker client
class _StubPost:
    """Stands in for `Reranker._post` - no server, but the same payload contract."""

    def __init__(self, scores=None, short_by=0):
        self.calls = []
        self.scores = scores
        self.short_by = short_by

    def __call__(self, path, payload):
        docs = payload["documents"]
        self.calls.append((path, list(docs)))
        n = len(docs) - self.short_by
        if self.scores is not None:
            vals = list(self.scores)[:n]
        else:
            vals = [float(i) for i in range(n)]
        # Deliberately reversed: the client must index by `index`, not by position.
        return {"results": [{"index": i, "relevance_score": v}
                            for i, v in reversed(list(enumerate(vals)))]}


def test_reranker_returns_one_score_per_document_in_input_order_on_every_stack():
    """`results` arrives in server order and carries its own `index`; only that counts."""
    for stack, prefix in STACKS:
        _c, _s, _r, reranker_mod = _mods(prefix)
        rr = reranker_mod.Reranker(max_chars=100, batch=32)
        rr._post = _StubPost(scores=[2.0, -3.0])
        got = rr.rerank("q", ["doc a", "doc b"])
        if got != [2.0, -3.0]:
            _fail(stack, "scores came back as %r, expected [2.0, -3.0]" % (got,))


def test_reranker_clips_a_long_document_on_every_stack():
    """llama-server answers HTTP 400 when a pair exceeds one slot's context."""
    for stack, prefix in STACKS:
        _c, _s, _r, reranker_mod = _mods(prefix)
        rr = reranker_mod.Reranker(max_chars=100, batch=32)
        stub = _StubPost()
        rr._post = stub
        rr.rerank("q", ["x" * 5000])
        sent = stub.calls[0][1][0]
        if len(sent) != 100:
            _fail(stack, "sent %d chars, expected the 100-char clip" % len(sent))


def test_reranker_replaces_an_empty_document_with_a_space_on_every_stack():
    """An empty string is not a valid server input; a single space is."""
    for stack, prefix in STACKS:
        _c, _s, _r, reranker_mod = _mods(prefix)
        rr = reranker_mod.Reranker(max_chars=100, batch=32)
        stub = _StubPost()
        rr._post = stub
        rr.rerank("q", ["   "])
        if stub.calls[0][1] != [" "]:
            _fail(stack, "an all-whitespace document was sent as %r" % (stub.calls[0][1],))


def test_reranker_batches_a_long_input_list_on_every_stack():
    """The cross-encoder is O(pairs), so the client must chunk the shortlist."""
    for stack, prefix in STACKS:
        _c, _s, _r, reranker_mod = _mods(prefix)
        rr = reranker_mod.Reranker(max_chars=100, batch=2)
        stub = _StubPost()
        rr._post = stub
        got = rr.rerank("q", ["d%d" % i for i in range(5)])
        sizes = [len(docs) for _path, docs in stub.calls]
        if sizes != [2, 2, 1]:
            _fail(stack, "batch sizes were %r, expected [2, 2, 1]" % (sizes,))
        if len(got) != 5:
            _fail(stack, "returned %d scores for 5 documents" % len(got))


def test_reranker_raises_when_the_server_answers_short_on_every_stack():
    """A short answer would silently misalign scores with documents - refuse instead."""
    for stack, prefix in STACKS:
        _c, _s, _r, reranker_mod = _mods(prefix)
        rr = reranker_mod.Reranker(max_chars=100, batch=32)
        rr._post = _StubPost(short_by=1)
        try:
            rr.rerank("q", ["a", "b"])
        except reranker_mod.RerankError:
            continue
        _fail(stack, "a short server answer did not raise RerankError")


# ========================================================= 3. retriever integration
class _FakeStore:
    """Just enough store for `Retriever.search` - the real one wants GBs of vectors.

    `*args, **kwargs` on purpose: the three retrievers disagree on how they call their
    own store. Three.js and Unity pass `dense_search(qv, k, filters)` positionally,
    Godot passes `dense_search(qv, top_k=..., filters=...)`. Harmless, but it means a
    stub written for one stack raises TypeError on another - which is exactly the kind
    of divergence this file exists to surface.
    """

    def __init__(self, dense, lexical, chunks):
        self._dense, self._lexical, self._chunks = dense, lexical, chunks

    def dense_search(self, *_a, **_kw):
        return self._dense

    def lexical_search(self, *_a, **_kw):
        return self._lexical

    def get_chunks(self, ids):
        return {i: self._chunks[i] for i in ids if i in self._chunks}


class _FakeEmbedder:
    def embed_query(self, q):
        return [0.0] * DIM


class _DeadReranker:
    def __init__(self, exc):
        self.exc = exc

    def rerank(self, query, docs):
        raise self.exc


class _FlipReranker:
    """Scores documents so the RRF order is exactly reversed."""

    def __init__(self, scores):
        self.scores = scores

    def rerank(self, query, docs):
        return [self.scores[i] for i in range(len(docs))]


def _two_chunk_fixture(chunkers):
    a = _chunk(chunkers, "void Alpha() { }", "a.cs", "Alpha")
    b = _chunk(chunkers, "void Beta() { }", "b.cs", "Beta")
    store = _FakeStore(dense=[(a.id, 0.9)], lexical=[(b.id, 5.0)],
                       chunks={a.id: a, b.id: b})
    return a, b, store


def test_a_dead_reranker_costs_relevance_not_answers_on_every_stack():
    """Every stack must keep answering in RRF order and COUNT the failure.

    Without the counter the degradation is invisible: answers still arrive, they are
    just worse, and nothing anywhere says the reranker is down.
    """
    for stack, prefix in STACKS:
        chunkers, _s, retriever_mod, reranker_mod = _mods(prefix)
        a, b, store = _two_chunk_fixture(chunkers)

        plain = retriever_mod.Retriever(store=store, embedder=_FakeEmbedder(), reranker=None)
        expected = [h.id for h in plain.search("q", top_k=5)]

        dead = retriever_mod.Retriever(store=store, embedder=_FakeEmbedder(),
                                       reranker=_DeadReranker(reranker_mod.RerankError("down")))
        hits = dead.search("q", top_k=5)
        if [h.id for h in hits] != expected:
            _fail(stack, "a dead reranker changed the order: %r != %r"
                  % ([h.id for h in hits], expected))
        if dead.rerank_failures != 1:
            _fail(stack, "rerank_failures = %d, expected 1" % dead.rerank_failures)
        if not (dead.last_rerank_error or "").startswith("RerankError"):
            _fail(stack, "last_rerank_error = %r" % (dead.last_rerank_error,))
        if any(h.rerank_score is not None for h in hits):
            _fail(stack, "rerank_score was filled despite the reranker failing")


def test_a_live_reranker_reorders_the_fused_shortlist_on_every_stack():
    """The second pass must actually win - and fill `rerank_score` for inspection."""
    for stack, prefix in STACKS:
        chunkers, _s, retriever_mod, _k = _mods(prefix)
        a, b, store = _two_chunk_fixture(chunkers)

        plain = retriever_mod.Retriever(store=store, embedder=_FakeEmbedder(), reranker=None)
        if plain.search("q", top_k=5)[0].id != a.id:
            _fail(stack, "fixture assumption broken: RRF did not put Alpha first")

        # `docs` arrives in fused order [Alpha, Beta] -> give Beta the high score.
        rr = retriever_mod.Retriever(store=store, embedder=_FakeEmbedder(),
                                     reranker=_FlipReranker([-5.0, 5.0]))
        hits = rr.search("q", top_k=5)
        if hits[0].id != b.id:
            _fail(stack, "the reranker did not lift Beta to the top (got %s)" % hits[0].id)
        if hits[0].rerank_score != 5.0:
            _fail(stack, "rerank_score = %r, expected 5.0" % (hits[0].rerank_score,))
        if rr.rerank_failures != 0:
            _fail(stack, "rerank_failures = %d on a healthy reranker" % rr.rerank_failures)


def test_reranking_can_be_switched_off_on_every_stack():
    """`reranker=None` must reproduce the pre-reranker result exactly, not merely similar.

    This is the escape hatch when the second pass misbehaves on a real corpus.
    """
    for stack, prefix in STACKS:
        chunkers, _s, retriever_mod, _k = _mods(prefix)
        a, b, store = _two_chunk_fixture(chunkers)
        r = retriever_mod.Retriever(store=store, embedder=_FakeEmbedder(), reranker=None)
        hits = r.search("q", top_k=5)
        if any(h.rerank_score is not None for h in hits):
            _fail(stack, "rerank_score was filled with the reranker disabled")
        if {h.id for h in hits} != {a.id, b.id}:
            _fail(stack, "disabled-reranker search returned %r" % ([h.id for h in hits],))


if __name__ == "__main__":
    import traceback
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
