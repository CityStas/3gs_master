"""Tests for the Unity stack (`unity/unimaster`).

Five things are worth testing here, and each one exists because it broke or would have:

1. **Chunking** - the C# splitter is regex-based, so the two ways it can fail silently are
   "one chunk swallows the rest of the file" (`_cs_block_end` with no brace) and "a member
   is attributed to the wrong class" (`owner()`). Both produce a plausible-looking index
   that retrieves the wrong thing, which is worse than an exception.
2. **Lint severity** - the whole point of the layer is that `error` reddens the verdict and
   `warning` does not. If severity is wrong the gate is either useless or blocks work.
3. **Lint false positives** - `EDITOR-API-IN-RUNTIME` must not fire inside `Editor/` or
   under `#if UNITY_EDITOR`, and `.velocity` must stay a warning (`NavMeshAgent.velocity`
   is a real API). A linter that cries wolf gets ignored.
4. **Path sandbox** - every tool path goes through `safe_path`; a hole there is a hole in
   the whole boundary.
5. **Store open under load** - a search landing inside an index-build commit window used to
   die with SQLITE_CANTOPEN; the corpus takes hours to build, so the retry needs a guard.

Run:  .venv\\Scripts\\python.exe tests\\test_unity.py
"""
from pathlib import Path
import sys
import tempfile

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "unity"))

from unimaster.rag.chunkers import (chunk_csharp, chunk_html, chunk_markdown,  # noqa: E402
                                    chunk_unity_yaml, chunk_shader)
from unimaster.rag.retriever import Retriever, SOURCE_PRIORITY  # noqa: E402
from unimaster.unity import lint, paths  # noqa: E402


# ======================================================================= chunking
SAMPLE_CS = """using System;
using UnityEngine;

namespace Game.Player
{
    public class PlayerController : MonoBehaviour
    {
        [SerializeField] private float _moveSpeed = 5f;
        private int _hp = 100;
        private Rigidbody _rb;

        public float Health => _hp;

        void Awake()
        {
            _rb = GetComponent<Rigidbody>();
        }

        // A comment with a brace } that must not close the block.
        public void Move(Vector3 dir)
        {
            var p = transform.position;
            p.x += dir.x * _moveSpeed;
            transform.position = p;
        }
    }

    public enum PlayerState { Idle, Run, Jump }
}
"""


def test_csharp_splits_into_types_and_members():
    chunks = chunk_csharp(SAMPLE_CS, "Assets/Scripts/PlayerController.cs", "project")
    kinds = {c.member_kind for c in chunks}
    assert "class" in kinds, kinds
    assert "enum" in kinds, kinds
    assert "method" in kinds, kinds
    assert "property" in kinds, kinds
    assert "field" in kinds, kinds


def test_csharp_members_are_owned_by_their_class():
    chunks = chunk_csharp(SAMPLE_CS, "Assets/Scripts/PlayerController.cs", "project")
    move = next(c for c in chunks if c.symbol == "PlayerController.Move")
    assert move.class_name == "PlayerController"
    assert move.namespace == "Game.Player"
    # The enum is a sibling type, not the owner of Move().
    assert not any(c.class_name == "PlayerState" and c.member_kind == "method" for c in chunks)


def test_a_field_does_not_swallow_the_rest_of_the_file():
    """`private int _hp = 100;` has no brace - the chunk must end at the `;`, not run on."""
    chunks = chunk_csharp(SAMPLE_CS, "Assets/Scripts/PlayerController.cs", "project")
    hp = next(c for c in chunks if c.symbol == "PlayerController._hp")
    # The whole file is ~900 chars; a runaway chunk would be near that size.
    assert len(hp.text) < 300, len(hp.text)


def test_a_brace_in_a_comment_does_not_close_the_block():
    """`Move()` contains `// ... } ...`; the body must still contain its real statements."""
    chunks = chunk_csharp(SAMPLE_CS, "Assets/Scripts/PlayerController.cs", "project")
    move = next(c for c in chunks if c.symbol == "PlayerController.Move")
    assert "transform.position = p;" in move.text, move.text
    assert "_moveSpeed" in move.text


def test_namespace_is_carried_on_every_chunk():
    chunks = chunk_csharp(SAMPLE_CS, "Assets/Scripts/PlayerController.cs", "project")
    assert all(c.namespace == "Game.Player" for c in chunks), \
        [c.namespace for c in chunks]


def test_chunk_ids_are_unique_and_stable():
    a = chunk_csharp(SAMPLE_CS, "Assets/Scripts/PlayerController.cs", "project")
    b = chunk_csharp(SAMPLE_CS, "Assets/Scripts/PlayerController.cs", "project")
    assert len({c.id for c in a}) == len(a), "duplicate chunk ids"
    assert [c.id for c in a] == [c.id for c in b], "chunk ids are not deterministic"


# =================================================================== Unity YAML
SAMPLE_UNITY_YAML = """%YAML 1.1
%TAG !u! tag:unity3d.com,2011:
--- !u!1 &1234567890
GameObject:
  m_ObjectHideFlags: 0
  m_Name: PlayerRoot
  m_Component:
  - component: {fileID: 1234567891}
--- !u!4 &1234567891
Transform:
  m_GameObject: {fileID: 1234567890}
  m_LocalPosition: {x: 0, y: 1, z: 0}
--- !u!114 &1234567892
MonoBehaviour:
  m_Script: {fileID: 11500000, guid: abcdef0123456789abcdef0123456789, type: 3}
"""


def test_unity_yaml_splits_per_document():
    chunks = chunk_unity_yaml(SAMPLE_UNITY_YAML, "Assets/Scenes/Main.unity", "project")
    assert len(chunks) == 3, [c.symbol for c in chunks]
    assert all(c.file_type == "unityyaml" for c in chunks)


def test_unity_yaml_labels_the_gameobject_by_name():
    chunks = chunk_unity_yaml(SAMPLE_UNITY_YAML, "Assets/Scenes/Main.unity", "project")
    assert any("PlayerRoot" in c.symbol for c in chunks), [c.symbol for c in chunks]


def test_unity_yaml_labels_a_nameless_component_by_class_not_by_file_id():
    """Components have no `m_Name`; `Transform:...` is searchable, `!u!4` is not."""
    chunks = chunk_unity_yaml(SAMPLE_UNITY_YAML, "Assets/Scenes/Main.unity", "project")
    symbols = [c.symbol for c in chunks]
    assert any(s.startswith("Main:Transform:") for s in symbols), symbols
    assert not any("!u!" in s for s in symbols), symbols


# ========================================================================= lint
def test_removed_api_is_an_error():
    src = "void F() { GetComponent<Rigidbody>().velocity = Vector3.zero;\n" \
          "  Application.LoadLevel(\"Next\"); }"
    codes = {f.code: f.severity for f in lint.lint_csharp(src, "Assets/A.cs")}
    assert codes.get("LEGACY-APPLICATION-LEVEL") == "error", codes


def test_obsolete_but_working_api_is_only_a_warning():
    """`NavMeshAgent.velocity` is real, so `.velocity` alone must not redden the build."""
    src = "void F(NavMeshAgent a) { var v = a.velocity; }"
    findings = lint.lint_csharp(src, "Assets/A.cs")
    vel = [f for f in findings if f.code == "UNITY6-RIGIDBODY-VELOCITY"]
    assert vel and vel[0].severity == "warning", [f.code for f in findings]
    assert lint.errors(findings) == []


def test_struct_assignment_is_an_error():
    src = "void F() { transform.position.x = 5f; }"
    errs = lint.errors(lint.lint_csharp(src, "Assets/A.cs"))
    assert any(f.code == "CS-VALUE-COMPONENT" for f in errs), [f.code for f in errs]


def test_editor_api_is_suppressed_in_an_editor_folder():
    src = "using UnityEditor;\nvoid F() { AssetDatabase.Refresh(); }"
    assert not [f for f in lint.lint_csharp(src, "Assets/Editor/Tool.cs")
                if f.code == "EDITOR-API-IN-RUNTIME"]
    assert not [f for f in lint.lint_csharp(src, "Assets/EditorTools/Tool.cs")
                if f.code == "EDITOR-API-IN-RUNTIME"]


def test_editor_api_is_suppressed_under_a_unity_editor_guard():
    src = "#if UNITY_EDITOR\nusing UnityEditor;\nvoid F() { AssetDatabase.Refresh(); }\n#endif"
    assert not [f for f in lint.lint_csharp(src, "Assets/Tool.cs")
                if f.code == "EDITOR-API-IN-RUNTIME"]


def test_editor_api_in_a_runtime_script_is_a_warning():
    src = "void F() { UnityEditor.EditorApplication.isPlaying = false; }"
    f = [x for x in lint.lint_csharp(src, "Assets/Scripts/A.cs")
         if x.code == "EDITOR-API-IN-RUNTIME"]
    assert f and f[0].severity == "warning", [x.code for x in f]


def test_old_api_in_a_comment_is_not_a_finding():
    src = "// Application.LoadLevel is gone\nvoid F() { }"
    assert lint.lint_csharp(src, "Assets/A.cs") == []


def test_old_api_inside_a_string_literal_is_not_a_finding():
    src = 'void F() { Debug.Log("WWW is gone"); }'
    assert not [f for f in lint.lint_csharp(src, "Assets/A.cs") if f.code == "LEGACY-WWW"]


def test_input_system_only_project_makes_input_an_error():
    """`activeInputHandler: 1` = new Input System only -> UnityEngine.Input throws."""
    with tempfile.TemporaryDirectory() as td:
        root = Path(td)
        (root / "ProjectSettings").mkdir()
        (root / "ProjectSettings" / "ProjectSettings.asset").write_text(
            "PlayerSettings:\n  activeInputHandler: 1\n", encoding="utf-8")
        src = "void F() { if (Input.GetKeyDown(KeyCode.Space)) { } }"
        errs = lint.errors(lint.lint_csharp(src, "Assets/A.cs", root))
        assert any(f.code == "NEW-INPUT-SYSTEM-ONLY" for f in errs), [f.code for f in errs]


def test_legacy_input_is_fine_in_a_legacy_project():
    with tempfile.TemporaryDirectory() as td:
        root = Path(td)
        (root / "ProjectSettings").mkdir()
        (root / "ProjectSettings" / "ProjectSettings.asset").write_text(
            "PlayerSettings:\n  activeInputHandler: 0\n", encoding="utf-8")
        src = "void F() { if (Input.GetKeyDown(KeyCode.Space)) { } }"
        assert lint.errors(lint.lint_csharp(src, "Assets/A.cs", root)) == []


def test_unityscript_is_an_error():
    src = "function Start() {\n  Debug.Log(\"hi\");\n}"
    errs = lint.errors(lint.lint_csharp(src, "Assets/Old.js"))
    assert any(f.code == "LEGACY-UNITYSCRIPT" for f in errs), [f.code for f in errs]


def test_lint_hint_mentions_the_counts():
    findings = lint.lint_csharp("void F() { transform.position.x = 1f; }", "Assets/A.cs")
    hint = lint.lint_hint(findings)
    assert "error" in hint and "fix" in hint.lower(), hint


# ================================================================ path sandbox
def test_safe_path_rejects_absolute_drive_and_unc():
    with tempfile.TemporaryDirectory() as td:
        root = Path(td)
        for bad in ("C:/Windows/System32/drivers/etc/hosts", "/etc/passwd",
                    "//server/share/x.cs", "\\\\server\\share\\x.cs"):
            try:
                paths.safe_path(root, bad)
            except paths.UnityPathError:
                continue
            raise AssertionError(f"safe_path accepted {bad!r}")


def test_safe_path_rejects_escape():
    with tempfile.TemporaryDirectory() as td:
        root = Path(td)
        try:
            paths.safe_path(root, "../../secrets.txt")
        except paths.UnityPathError:
            return
        raise AssertionError("safe_path accepted a path that escapes the project root")


def test_safe_path_allows_a_normal_relative_path():
    with tempfile.TemporaryDirectory() as td:
        root = Path(td)
        p = paths.safe_path(root, "Assets/Scripts/Player.cs")
        assert p == (root / "Assets/Scripts/Player.cs").resolve()


# ==================================================================== retriever
def test_rrf_fuses_dense_and_lexical_ranks():
    """A doc found by both halves must outrank one found by only one, at equal ranks."""
    dense = [("a", 0.9), ("b", 0.8)]
    lexical = [("b", 5.0), ("c", 4.0)]
    fused = dict(Retriever._rrf(dense, lexical, k=60))
    assert fused["b"] > fused["a"], fused
    assert fused["b"] > fused["c"], fused


def test_source_priority_puts_project_above_bulk_docs():
    assert SOURCE_PRIORITY["project"] > SOURCE_PRIORITY["official_docs"]
    assert SOURCE_PRIORITY["cookbook"] > SOURCE_PRIORITY["official_source"]


# ===================================================================== misc
def test_html_chunk_section_carries_the_heading():
    html = ("<html><body><h1>Rigidbody</h1><p>Body.</p>"
            "<h2>Properties</h2><p>velocity is renamed.</p></body></html>")
    chunks = chunk_html(html, "ScriptReference/Rigidbody.html", "official_docs")
    assert any(c.section == "Properties" for c in chunks), [c.section for c in chunks]


def test_markdown_fences_do_not_create_sections():
    md = ("# Title\n\n```csharp\n#pragma strict\n#if UNITY_EDITOR\n#endif\n```\n\n"
          "## Real\nThis body is long enough to become its own chunk.\n")
    chunks = chunk_markdown(md, "cookbook/x.md", "cookbook")
    sections = [c.section for c in chunks]
    assert "Real" in sections, sections
    # `#pragma` / `#if` inside the fence must not be mistaken for headings.
    assert not any(s.startswith("#") for s in sections), sections
    assert all("section" != s for s in sections), sections


def test_shader_blocks_are_chunked():
    src = ("Shader \"G/Lit\" {\n SubShader {\n  Pass {\n"
           "   CGPROGRAM\n   #pragma vertex vert\n   ENDCG\n"
           "  }\n }\n}\n")
    chunks = chunk_shader(src, "Assets/Shaders/Lit.shader", "project")
    assert chunks, "shader produced no chunks"
    assert all(c.file_type == "shader" for c in chunks)


# ==================================================================== store open
def test_store_open_retries_a_transient_failure():
    """Opening the index while `unity-index` is mid-commit must not kill the search.

    `executescript` implicitly commits, so it needs the write lock for a moment; a
    connection landing inside that window gets SQLITE_CANTOPEN/SQLITE_BUSY even though
    the file is readable. The corpus build runs for hours, so this is not theoretical.
    """
    import sqlite3
    from unimaster.rag import store as store_mod

    real_connect = store_mod.sqlite3.connect
    real_sleep = store_mod.time.sleep
    counter = {"n": 0}

    class Flaky:
        """Delegates to the real connection but fails the first two schema scripts."""

        def __init__(self, real):
            object.__setattr__(self, "_real", real)

        def __getattr__(self, name):
            return getattr(object.__getattribute__(self, "_real"), name)

        def __setattr__(self, name, value):
            setattr(object.__getattribute__(self, "_real"), name, value)

        def executescript(self, sql):
            counter["n"] += 1
            if counter["n"] <= 2:
                raise sqlite3.OperationalError("unable to open database file")
            return object.__getattribute__(self, "_real").executescript(sql)

    with tempfile.TemporaryDirectory() as td:
        db = Path(td) / "lexical.db"
        store_mod.sqlite3.connect = lambda *a, **kw: Flaky(real_connect(*a, **kw))
        store_mod.time.sleep = lambda _s: None
        try:
            st = store_mod.IndexStore(db)
            st.close()
        finally:
            store_mod.sqlite3.connect = real_connect
            store_mod.time.sleep = real_sleep

    assert counter["n"] == 3, "expected 2 failures then a success, got %d" % counter["n"]


def test_store_open_gives_up_with_the_real_error():
    """After the retries are exhausted the original error must surface, not a bare assert."""
    import sqlite3
    from unimaster.rag import store as store_mod

    real_connect = store_mod.sqlite3.connect
    real_sleep = store_mod.time.sleep

    class AlwaysBroken:
        def __init__(self, real):
            object.__setattr__(self, "_real", real)

        def __getattr__(self, name):
            return getattr(object.__getattribute__(self, "_real"), name)

        def __setattr__(self, name, value):
            setattr(object.__getattribute__(self, "_real"), name, value)

        def executescript(self, _sql):
            raise sqlite3.OperationalError("unable to open database file")

    with tempfile.TemporaryDirectory() as td:
        db = Path(td) / "lexical.db"
        store_mod.sqlite3.connect = lambda *a, **kw: AlwaysBroken(real_connect(*a, **kw))
        store_mod.time.sleep = lambda _s: None
        try:
            try:
                store_mod.IndexStore(db)
            except sqlite3.OperationalError as exc:
                assert "unable to open database file" in str(exc), exc
            else:
                raise AssertionError("IndexStore should have raised")
        finally:
            store_mod.sqlite3.connect = real_connect
            store_mod.time.sleep = real_sleep


def test_indexer_stops_probing_a_dead_embedding_server():
    """A dead embedding server must cost a moment, not a connect attempt per batch.

    Every batch still stores its chunks (text-only) - only the *probing* stops, because
    a full corpus is ~1000 batches and each failed attempt costs seconds.
    """
    from unimaster.rag.indexer import EMBED_FAIL_LIMIT, IndexReport, Indexer
    from unimaster.rag.store import IndexStore

    class DeadEmbedder:
        def __init__(self):
            self.calls = 0

        def embed_many(self, texts):
            self.calls += 1
            raise RuntimeError("embedding server unavailable")

    with tempfile.TemporaryDirectory() as td:
        st = IndexStore(Path(td) / "lexical.db")
        emb = DeadEmbedder()
        try:
            ix = Indexer(store=st, embedder=emb, verbose=False)
            rep = IndexReport(source="project")
            for _ in range(EMBED_FAIL_LIMIT + 4):
                ix._flush(_mk_chunks(n=2), ["a", "b"], rep)
            assert emb.calls == EMBED_FAIL_LIMIT, \
                "probed the dead server %d times, expected %d" % (emb.calls, EMBED_FAIL_LIMIT)
            # Chunks must still be stored, and the count reported as embed errors.
            assert st._conn.execute("SELECT COUNT(*) FROM chunks").fetchone()[0] == 2
            assert st._conn.execute("SELECT COUNT(*) FROM chunks WHERE vec IS NULL").fetchone()[0] == 2
            assert rep.embed_errors == EMBED_FAIL_LIMIT + 4
        finally:
            st.close()


def test_indexer_resumes_embedding_when_the_server_returns():
    """The breaker must not latch: a server that comes back is used again."""
    from unimaster.rag.indexer import EMBED_FAIL_LIMIT, IndexReport, Indexer
    from unimaster.rag.store import IndexStore
    import numpy as np

    class FlakyEmbedder:
        def __init__(self):
            self.calls = 0

        def embed_many(self, texts):
            self.calls += 1
            if self.calls == 2:          # one transient failure, well under the limit
                raise RuntimeError("blip")
            return np.zeros((len(texts), 4), dtype=np.float32)

    with tempfile.TemporaryDirectory() as td:
        st = IndexStore(Path(td) / "lexical.db")
        emb = FlakyEmbedder()
        try:
            ix = Indexer(store=st, embedder=emb, verbose=False)
            rep = IndexReport(source="project")
            for _ in range(EMBED_FAIL_LIMIT + 2):
                ix._flush(_mk_chunks(n=2), ["a", "b"], rep)
            assert not ix._embed_skip, "a single blip tripped the breaker"
            assert emb.calls == EMBED_FAIL_LIMIT + 2, "stopped probing after a blip"
            assert rep.vectors > 0, "vectors were not stored after recovery"
        finally:
            st.close()


def test_store_picks_up_vectors_written_by_another_process():
    """A cached empty vector matrix must not outlive the `--vectors` run that fills it.

    The agent's MCP server is a long-lived process; `gs unity-index --vectors` runs in a
    different one. If the reader cached "no vectors" from before that run, it would keep
    answering lexical-only for the rest of its life.
    """
    import numpy as np
    from unimaster.rag.store import IndexStore

    with tempfile.TemporaryDirectory() as td:
        db = Path(td) / "lexical.db"
        reader, writer = IndexStore(db), IndexStore(db)
        try:
            reader.upsert(_mk_chunks(n=2), None)          # text-only, as after a build
            assert reader.dense_search(np.zeros(4, dtype=np.float32), top_k=2) == []

            ids = [c.id for c in _mk_chunks(n=2)]
            writer.set_vectors(ids, np.ones((2, 4), dtype=np.float32))   # the --vectors run

            hits = reader.dense_search(np.ones(4, dtype=np.float32), top_k=2)
            assert len(hits) == 2, "reader kept a cached empty vector matrix"
        finally:
            reader.close()
            writer.close()


def test_store_preload_warms_the_vector_matrix():
    """`preload()` exists so a 95 s cold read does not land on the user's first query.

    Measured on the real corpus: `_load_vectors()` takes ~95 s with the file cold and
    ~2.9 s warm, because it reads ~1.3 GB of BLOBs. The MCP server runs it on a daemon
    thread at startup; the only thing that matters here is that it fills the cache.
    """
    import numpy as np
    from unimaster.rag.store import IndexStore

    with tempfile.TemporaryDirectory() as td:
        db = Path(td) / "lexical.db"
        st = IndexStore(db)
        try:
            st.upsert(_mk_chunks(n=2), np.ones((2, 4), dtype=np.float32))
            st.invalidate_cache()
            assert st._vec_cache is None
            st.preload()
            assert st._vec_cache is not None and st._vec_cache.shape == (2, 4)
        finally:
            st.close()


# ================================================================ retriever reporting
class _FakeStore:
    """Just enough store for `Retriever.search` - the real one needs 1.3 GB of vectors."""

    def __init__(self, dense, lexical, chunks, raise_dense=False):
        self._dense, self._lexical, self._chunks = dense, lexical, chunks
        self._raise = raise_dense

    def dense_search(self, qv, k, filters):
        if self._raise:
            raise RuntimeError("embedding server unavailable")
        return self._dense

    def lexical_search(self, q, k, filters):
        return self._lexical

    def get_chunks(self, ids):
        return {i: self._chunks[i] for i in ids if i in self._chunks}


class _FakeEmbedder:
    def embed_query(self, q):
        return [0.0]


def test_search_reports_which_half_produced_a_hit():
    """`dense_rank`/`lexical_rank` were declared on `Hit` and never filled.

    After RRF a dense-only, lexical-only and both-halves hit were indistinguishable -
    which also hid the case where the dense half had died entirely.
    """
    from unimaster.rag.retriever import Retriever

    cs = (_mk_chunks(path="Assets/A.cs", n=1)
          + _mk_chunks(path="Assets/B.cs", n=1, tag="b")
          + _mk_chunks(path="Assets/C.cs", n=1, tag="c"))
    d_only, shared, l_only = (c.id for c in cs)
    store = _FakeStore(dense=[(d_only, 0.9), (shared, 0.8)],
                       lexical=[(shared, 5.0), (l_only, 4.0)],
                       chunks={c.id: c for c in cs})
    r = Retriever(store=store, embedder=_FakeEmbedder())

    hits = {h.id: h for h in r.search("q", top_k=10)}
    assert (hits[d_only].dense_rank, hits[d_only].lexical_rank) == (1, None)
    assert (hits[shared].dense_rank, hits[shared].lexical_rank) == (2, 1)
    assert (hits[l_only].dense_rank, hits[l_only].lexical_rank) == (None, 2)
    assert hits[shared].dense_score == 0.8 and hits[shared].lexical_score == 5.0
    assert r.dense_failures == 0


def test_search_counts_a_dead_embedding_server():
    """A dead embed server degrades every answer to lexical-only, silently.

    `search()` must keep answering - losing the corpus would be worse - but the count is
    the only thing that makes the degradation visible to `unity_rag_status`.
    """
    from unimaster.rag.retriever import Retriever

    cs = _mk_chunks(path="Assets/A.cs", n=1)
    store = _FakeStore(dense=[], lexical=[(cs[0].id, 1.0)],
                       chunks={cs[0].id: cs[0]}, raise_dense=True)
    r = Retriever(store=store, embedder=_FakeEmbedder())

    hits = r.search("q", top_k=5)
    assert len(hits) == 1, "lexical half must survive a dead embed server"
    assert hits[0].dense_rank is None
    assert r.dense_failures == 1 and "RuntimeError" in r.last_dense_error


# ================================================================ FTS rowid layout
def _mk_chunks(path="Assets/Player.cs", n=3, tag="a"):
    from unimaster.rag.chunkers import Chunk
    return [Chunk(text=f"void M{i}() {{ }} // {tag}", source="project", path=path,
                  file_type="csharp", symbol=f"M{i}", class_name="Player",
                  section=f"m{i}") for i in range(n)]


def _fts_orphans(conn):
    return conn.execute("SELECT COUNT(*) FROM chunks_fts f "
                        "LEFT JOIN chunks c ON c.rowid=f.rowid WHERE c.rowid IS NULL").fetchone()[0]


def _aligned(conn):
    tot = conn.execute("SELECT COUNT(*) FROM chunks").fetchone()[0]
    joined = conn.execute("SELECT COUNT(*) FROM chunks_fts f "
                          "JOIN chunks c ON c.rowid=f.rowid").fetchone()[0]
    return tot == joined


def test_store_keeps_fts_rowids_aligned_across_upsert_and_delete():
    """`chunks_fts.rowid` must mirror `chunks.rowid`, or a lexical hit joins the wrong row.

    Deleting by `id` instead would be correct but scans the whole FTS table per row
    (`id` is UNINDEXED), which is what made the 26.7k-file corpus take days.
    """
    from unimaster.rag.store import IndexStore

    with tempfile.TemporaryDirectory() as td:
        st = IndexStore(Path(td) / "lexical.db")
        try:
            st.upsert(_mk_chunks(n=5), None)
            assert st._conn.execute("SELECT COUNT(*) FROM chunks").fetchone()[0] == 5
            assert _aligned(st._conn), "first insert broke the rowid invariant"
            assert _fts_orphans(st._conn) == 0

            # Re-storing byte-identical chunks must replace them, not duplicate them.
            # (New *text* is a new content hash and therefore a new chunk id - dropping
            # that revision is `delete_paths`' job, which the indexer does per file.)
            st.upsert(_mk_chunks(n=5), None)
            assert st._conn.execute("SELECT COUNT(*) FROM chunks").fetchone()[0] == 5, \
                "re-storing identical chunks duplicated them"
            assert _aligned(st._conn), "re-store broke the rowid invariant"
            assert _fts_orphans(st._conn) == 0

            # A different file must not disturb the first one's rows.
            st.upsert(_mk_chunks(path="Assets/Enemy.cs", n=4), None)
            assert st._conn.execute("SELECT COUNT(*) FROM chunks").fetchone()[0] == 9
            assert _aligned(st._conn)

            st.delete_paths(["Assets/Player.cs"])
            assert st._conn.execute("SELECT COUNT(*) FROM chunks").fetchone()[0] == 4
            assert st._conn.execute("SELECT COUNT(*) FROM chunks_fts").fetchone()[0] == 4, \
                "delete_paths left FTS rows behind"
            assert _fts_orphans(st._conn) == 0
            assert _aligned(st._conn)
        finally:
            st.close()


def test_store_realigns_a_legacy_fts_index_on_open():
    """An index built before the rowid change must be repaired, not silently mis-joined."""
    from unimaster.rag.store import IndexStore

    with tempfile.TemporaryDirectory() as td:
        db = Path(td) / "lexical.db"
        st = IndexStore(db)
        try:
            st.upsert(_mk_chunks(n=4), None)
            # Recreate the pre-fix layout: FTS rowids independent of chunks rowids.
            c = st._conn
            c.execute("DELETE FROM chunks_fts")
            c.execute("INSERT INTO chunks_fts(rowid,id,text,symbol,class_name,path) "
                      "SELECT rowid+1000,id,text,symbol,class_name,path FROM chunks")
            c.execute("DELETE FROM meta WHERE key='fts_rowid_aligned'")
            c.commit()
            assert not _aligned(c), "fixture did not reproduce the legacy layout"
        finally:
            st.close()

        st2 = IndexStore(db)
        try:
            assert _aligned(st2._conn), "legacy index was not realigned on open"
            assert _fts_orphans(st2._conn) == 0
            assert st2._conn.execute("SELECT COUNT(*) FROM chunks_fts").fetchone()[0] == 4
        finally:
            st2.close()


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
