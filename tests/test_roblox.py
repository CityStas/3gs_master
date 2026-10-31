"""Tests for the Roblox stack (`roblox/rbxmaster`).

The failure modes here are the ones that produce a *plausible* wrong answer rather than an
exception, so each test pins one of them:

1. **Luau block scanning** - `end` is a substring of `append`, of `-- end of file` and of
   the string `"end"`. A chunker that does `text.find("end")` swallows the rest of the file
   and the index silently attributes every later function to the first one.
2. **`for ... do` double count** - the `do` of a loop header must not open a second block,
   otherwise every loop eats the remainder of the file.
3. **Per-member API chunking** - the whole reason the Engine API corpus is usable is that
   `BasePart:SetNetworkOwner` is its own chunk with its own security tag. If members merge,
   the agent gets a 40 KB class page instead of an answer.
4. **Lint severity** - `error` must redden the verdict and `warning` must not, and a clean
   file must produce nothing at all. A linter that cries wolf gets switched off.
5. **Path sandbox** - every project tool path goes through `safe_path`; a hole there is a
   hole in the whole boundary.
6. **MCP registry coverage** - a missing engine entry means that profile boots with no
   tools at all, which is how `pi-home-godot` and `pi-home-unity` once shipped.

Run:  .venv\\Scripts\\python.exe tests\\test_roblox.py
"""
from pathlib import Path
import json
import sys
import tempfile

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "roblox"))

from rbxmaster.rag.chunkers import (chunk_api_md, chunk_luau,  # noqa: E402
                                    chunk_markdown, chunk_place_xml)
from rbxmaster.rag.store import IndexStore  # noqa: E402
from rbxmaster.rag.indexer import Indexer  # noqa: E402
from rbxmaster.rag.retriever import Retriever, SOURCE_PRIORITY  # noqa: E402
from rbxmaster.luau import lint, paths  # noqa: E402
from rbxmaster.luau.place import inspect as inspect_place  # noqa: E402
from rbxmaster import config  # noqa: E402

import numpy as np  # noqa: E402

FIXTURES = ROOT / "tests" / "fixtures" / "rbx_lint_place"
FIXTURES_CLEAN = ROOT / "tests" / "fixtures" / "rbx_clean_place"


class _ZeroEmbedder:
    """Stands in for bge-m3: the indexer only needs *a* matrix of the right shape."""

    def embed_many(self, texts):
        return np.zeros((len(texts), config.EMBED_DIM), dtype=np.float32)


def _indexed_paths(store) -> set[str]:
    return {r[0] for r in store._conn.execute("SELECT DISTINCT path FROM chunks")}


# ======================================================================= chunking
SAMPLE_LUAU = '''--!strict
-- Shop module. The header comment must survive into the chunk.
local Players = game:GetService("Players")

export type Item = {
	name: string,
	price: number,
}

local Shop = {}
Shop.__index = Shop

function Shop.new(owner: Player): Shop
	local self = setmetatable({}, Shop)
	self.owner = owner
	return self
end

-- Buy one item. Returns true when the purchase went through.
function Shop:buy(item: Item): boolean
	if item.price <= 0 then
		return false
	end
	local label = "end"          -- a string that looks like a closer
	local note = [[
end
]]
	print(label, note)
	return true
end

local function helper(a, b)
	for i = 1, 10 do
		if a == b then
			return i
		end
	end
	return 0
end

return Shop
'''


def test_chunk_luau_splits_every_declaration():
    chunks = chunk_luau(SAMPLE_LUAU, "src/ServerScriptService/Shop.luau")
    symbols = {c.symbol for c in chunks}
    for expected in ("Shop.new", "Shop:buy", "helper"):
        assert expected in symbols, "missing %s in %s" % (expected, sorted(symbols))
    assert any(c.symbol.endswith(":header") for c in chunks), "no file header chunk"
    # The type alias is a declaration of its own, not part of `Shop.new`.
    assert any(c.symbol == "Item" for c in chunks), "type alias was not chunked"


def test_chunk_luau_block_end_survives_decoys():
    """`"end"`, `[[ end ]]` and `-- end` must not close the function."""
    chunks = {c.symbol: c.text for c in chunk_luau(SAMPLE_LUAU, "src/Shop.luau")}
    buy = chunks["Shop:buy"]
    assert "return true" in buy, "buy() was cut short by a decoy `end`"
    assert "Shop.new" not in buy, "buy() swallowed the next function"
    # And the loop body stayed inside helper(), i.e. `for ... do` did not double count.
    helper = chunks["helper"]
    assert "return i" in helper and "return 0" in helper, "helper() lost its tail"
    assert "Shop:buy" not in helper, "helper() swallowed the next function"


def test_chunk_luau_context_from_path():
    server = chunk_luau("local x = 1", "src/ServerScriptService/A.server.luau")
    client = chunk_luau("local x = 1", "src/StarterPlayer/StarterPlayerScripts/B.client.luau")
    shared = chunk_luau("local x = 1", "src/ReplicatedStorage/C.luau")
    assert {c.context for c in server} == {"server"}
    assert {c.context for c in client} == {"client"}
    assert {c.context for c in shared} == {"shared"}


API_PAGE = '''---
name: BasePart
type: class
summary: The base class for all parts.
url: https://create.roblox.com/docs/reference/engine/classes/BasePart
inherits: [PVInstance]
---

# Class: BasePart

The base class for all parts.

## Methods

### Method: BasePart:SetNetworkOwner

Sets the network owner.

**Signature:** `BasePart:SetNetworkOwner(playerInstance: Player?): ()`

*Security: None · Thread Safety: Unsafe*

### Method: BasePart:GetMass

Returns the mass.

**Signature:** `BasePart:GetMass(): number`

*Security: None · Thread Safety: ReadSafe*

## Properties

### Property: BasePart.Anchored

Whether the part is anchored.

```json
{"access":"ReadWrite","security":{"read":"None","write":"None"},"thread_safety":"ReadSafe"}
```

## Events

### Event: BasePart.Touched

Fires on touch.

**Signature:** `BasePart.Touched(otherPart: BasePart): ()`

*Security: None · Thread Safety: Unsafe*

## Inherited Members

### Method: PVInstance:GetPivot

Not ours, must be skipped.
'''


def test_chunk_api_md_one_chunk_per_member():
    chunks = chunk_api_md(API_PAGE, "engine_api/classes/BasePart.md")
    by_symbol = {c.symbol: c for c in chunks}
    assert "BasePart:SetNetworkOwner" in by_symbol, sorted(by_symbol)
    assert "BasePart:GetMass" in by_symbol
    assert "BasePart.Touched" in by_symbol
    assert "PVInstance:GetPivot" not in by_symbol, "inherited members must be skipped"

    setter = by_symbol["BasePart:SetNetworkOwner"]
    assert setter.member_kind == "method"
    assert setter.class_name == "BasePart"
    assert setter.meta.get("thread_safety") == "Unsafe"
    assert "SetNetworkOwner" in setter.meta.get("signature", "")
    assert "GetMass" not in setter.text, "member chunk bled into the next member"

    # The fenced-JSON contract form (properties) must yield the same facts.
    anchored = by_symbol["BasePart.Anchored"]
    assert anchored.meta.get("thread_safety") == "ReadSafe"
    assert "read:None" in anchored.meta.get("security", "")
    assert anchored.meta.get("access") == "ReadWrite"


def test_api_tag_line_with_extra_segments():
    """The real tag line has three or four segments, not two.

    `*Security: None · Thread Safety: Unsafe · Simulation Access: true*` - an earlier
    regex required `*` immediately after `Thread Safety`, so it never matched a real page
    and `thread_safety` was dropped from every method in the corpus while `security`
    survived through a looser fallback. That silent half-loss is the point of this test.
    """
    page = '''---
name: BasePart
type: class
---

# Class: BasePart

## Methods

### Method: BasePart:SetNetworkOwner

Sets the owner.

**Signature:** `BasePart:SetNetworkOwner(playerInstance?: Player): ()`

*Security: None · Thread Safety: Unsafe · Simulation Access: true*

### Method: BasePart:GetMass

Returns the mass.

**Signature:** `BasePart:GetMass(): float`

*Security: None · Thread Safety: Safe · Capabilities: Basic*

### Method: BasePart:BreakJoints

A yielding method with the flag FIRST.

**Signature:** `BasePart:BreakJoints(): ()`

*Yields · Security: None · Thread Safety: Unsafe · Capabilities: Monetization*
'''
    by_symbol = {c.symbol: c for c in chunk_api_md(page, "classes/BasePart.md")}
    owner = by_symbol["BasePart:SetNetworkOwner"]
    assert owner.meta.get("thread_safety") == "Unsafe", owner.meta
    assert owner.meta.get("simulation_access") == "true", owner.meta
    assert owner.meta.get("security") == "None"
    mass = by_symbol["BasePart:GetMass"]
    assert mass.meta.get("thread_safety") == "Safe", mass.meta
    assert mass.meta.get("capabilities") == "Basic", mass.meta
    # `Yields` sits BEFORE `Security:` on 368 methods in the corpus; a regex anchored on
    # `*Security:` drops every one of them.
    joints = by_symbol["BasePart:BreakJoints"]
    assert joints.meta.get("yields") == "true", joints.meta
    assert joints.meta.get("thread_safety") == "Unsafe", joints.meta
    assert joints.meta.get("capabilities") == "Monetization", joints.meta


def test_chunk_markdown_keeps_fences():
    text = """---
title: Remote events
---

# Remote events

Intro paragraph.

## Server to client

```lua
local ev = game.ReplicatedStorage.Remote
ev:FireClient(player, 1)
```

## Client to server

Use `FireServer`.
"""
    chunks = chunk_markdown(text, "official_docs/remote.md")
    sections = {c.section: c for c in chunks}
    assert any("Server to client" in s for s in sections), sorted(sections)
    s2c = next(c for s, c in sections.items() if "Server to client" in s)
    assert "FireClient" in s2c.text, "fenced code was dropped"


# ============================================================================ lint
def test_lint_fixture_place_rules():
    issues = lint.lint_project(FIXTURES)
    got = {(i.rule, Path(i.file).name) for i in issues}
    expected = {
        ("localplayer-on-server", "Bootstrap.server.luau"),
        ("unclosed-block", "Broken.luau"),
        ("server-only-service", "ClientMain.client.luau"),
        ("method-case", "ClientMain.client.luau"),
        ("busy-loop", "Bootstrap.server.luau"),
        ("deprecated-api", "Bootstrap.server.luau"),
        ("instance-new-parent", "ClientMain.client.luau"),
    }
    missing = expected - got
    assert not missing, "lint missed %s (got %s)" % (sorted(missing), sorted(got))

    errors = [i for i in issues if i.severity == "error"]
    warnings = [i for i in issues if i.severity == "warning"]
    assert len(errors) == 4, [i.rule for i in errors]
    assert len(warnings) == 3, [i.rule for i in warnings]


def test_lint_clean_file_is_silent():
    """No false positives on idiomatic code: a linter that cries wolf gets ignored."""
    clean = '''--!strict
local Players = game:GetService("Players")
local ReplicatedStorage = game:GetService("ReplicatedStorage")

local function onPlayerAdded(player: Player)
	local data = nil
	for _, child in ipairs(ReplicatedStorage:GetChildren()) do
		if child:IsA("Folder") then
			data = child
		end
	end
	task.wait(0.1)
	print("end of setup", data, player)
end

Players.PlayerAdded:Connect(onPlayerAdded)
local part = Instance.new("Part")
part.Parent = workspace
'''
    issues = lint.lint_text(clean, "src/ServerScriptService/Clean.server.luau")
    assert issues == [], [(i.severity, i.rule, i.line) for i in issues]


def test_lint_clean_place_fixture_is_silent():
    """An idiomatic project - Rojo tree, module with methods, typed returns - must pass.

    This fixture is the regression guard for `method-case`: an earlier version matched any
    `:lowercase(` and reddened `Shop:total()`, `Shop:notify()` and the return-type
    annotation `): typeof(Shop)`. Every real project would have failed the gate.
    """
    issues = lint.lint_project(FIXTURES_CLEAN)
    assert issues == [], [(i.severity, i.rule, i.file, i.line) for i in issues]


def test_method_case_only_fires_on_api_methods():
    """Only a *real* API method in the wrong case is an error, never a user method."""
    quiet = '''--!strict
local Shop = {}
function Shop:total(items): number
	return #items
end
function Shop.new(): typeof(Shop)
	return setmetatable({}, Shop)
end
local n = (1 :: any) :: number
local s = string:find("abc", "b")
Shop:total({})
local x: number = 1
'''
    issues = lint.lint_text(quiet, "src/ReplicatedStorage/Shop.luau")
    assert issues == [], [(i.severity, i.rule, i.line, i.message) for i in issues]

    bad = '''local kids = workspace:getchildren()
local part = workspace:waitforchild("Part")
'''
    issues = lint.lint_text(bad, "src/ServerScriptService/Bad.server.luau")
    rules = {(i.rule, i.severity) for i in issues}
    assert ("method-case", "error") in rules, rules
    msgs = " ".join(i.message for i in issues)
    assert "GetChildren" in msgs and "WaitForChild" in msgs, msgs


def test_lint_severity_split():
    """`error` must be reserved for things that cannot run; style stays `warning`."""
    warn_only = 'local p = Instance.new("Part", workspace)\n'
    issues = lint.lint_text(warn_only, "src/Client.client.luau")
    assert issues, "Instance.new parent form should at least warn"
    assert all(i.severity == "warning" for i in issues), [i.severity for i in issues]

    broken = "function f()\n\tif true then\n\t\tprint(1)\nend\n"
    issues = lint.lint_text(broken, "src/ServerScriptService/Bad.server.luau")
    assert any(i.rule == "unclosed-block" and i.severity == "error" for i in issues), \
        [(i.rule, i.severity) for i in issues]


# ========================================================================== paths
def test_safe_path_blocks_escape():
    root = FIXTURES
    ok = paths.safe_path(root, "src/ServerScriptService/Bootstrap.server.luau")
    assert ok.is_file()

    for bad in ("../outside.luau", "src/../../outside.luau", "/etc/passwd",
                "C:/Windows/system.ini"):
        try:
            paths.safe_path(root, bad)
        except (ValueError, PermissionError, OSError):
            continue
        raise AssertionError("safe_path allowed %r" % bad)


def test_safe_path_prefix_is_not_string_prefix():
    """`<root>-evil` must not pass just because it shares a string prefix with `<root>`."""
    evil = FIXTURES.parent / (FIXTURES.name + "-evil")
    evil.mkdir(exist_ok=True)
    try:
        try:
            paths.safe_path(FIXTURES, "../%s/x.luau" % evil.name)
        except (ValueError, PermissionError, OSError):
            return
        raise AssertionError("safe_path accepted a sibling directory")
    finally:
        try:
            evil.rmdir()
        except OSError:
            pass


def test_script_context_rules():
    assert paths.script_context("src/ServerScriptService/A.server.luau") == "server"
    assert paths.script_context("src/StarterPlayer/StarterPlayerScripts/B.client.luau") == "client"
    assert paths.script_context("src/ReplicatedStorage/Shared.luau") == "shared"
    # The suffix wins over the folder: a .server.luau inside a client tree is still server.
    assert paths.script_context("src/StarterPlayer/X.server.luau") == "server"


def test_rojo_and_project_engine():
    assert paths.project_engine(FIXTURES) == "roblox"
    with tempfile.TemporaryDirectory() as td:
        d = Path(td)
        assert paths.rojo_project(d) is None
        (d / "default.project.json").write_text('{"name":"Game","tree":{}}', encoding="utf-8")
        assert paths.rojo_project(d) is not None
        # `default` beats a longer per-place variant.
        (d / "aaa-alt.project.json").write_text("{}", encoding="utf-8")
        assert paths.rojo_project(d).name == "default.project.json"


# ========================================================================== place
def test_place_inspect_services_and_scripts():
    info = inspect_place(FIXTURES / "smoke.rbxlx")
    assert "Workspace" in info["services"], info["services"]
    assert "ServerScriptService" in info["services"]
    assert info["class_counts"].get("Part") == 1, info["class_counts"]
    names = {s["name"] for s in info["scripts"]}
    assert "Bootstrap" in names, info["scripts"]
    boot = next(s for s in info["scripts"] if s["name"] == "Bootstrap")
    assert boot["lines"] >= 2
    assert "ServerScriptService" in boot["path"], boot["path"]


def test_place_chunker_one_chunk_per_item():
    xml = (FIXTURES / "smoke.rbxlx").read_text(encoding="utf-8")
    chunks = chunk_place_xml(xml, "smoke.rbxlx")
    assert chunks, "place chunker produced nothing"
    joined = "\n".join(c.text for c in chunks)
    assert "Bootstrap" in joined
    assert any(c.symbol and "Part" in c.symbol for c in chunks), [c.symbol for c in chunks]


# ======================================================================== registry
def test_mcp_registry_covers_every_engine():
    """Every engine needs its rag server, or that profile boots with no knowledge base.

    A *project* server is not universal: three.js edits `projects/games/*` straight through
    the filesystem, so `threejs` legitimately has none. The three engines with a real
    project boundary (Godot's res://, Unity's Assets/, Roblox's DataModel) each need one.
    """
    reg = json.loads((ROOT / "mcp" / "registry.json").read_text(encoding="utf-8"))
    servers = reg["servers"] if isinstance(reg, dict) and "servers" in reg else reg
    by_engine: dict[str, set[str]] = {}
    for name, spec in servers.items():
        for eng in spec.get("engines", []):
            by_engine.setdefault(eng, set()).add(name)

    for engine in ("threejs", "godot", "unity", "roblox"):
        names = by_engine.get(engine, set())
        assert names, "engine %s has no MCP servers" % engine
        assert any(n.endswith("-rag") for n in names), "%s has no rag server: %s" % (engine, names)

    for engine in ("godot", "unity", "roblox"):
        names = by_engine[engine]
        assert any(n.endswith("-project") or n == engine for n in names), \
            "%s has no project server: %s" % (engine, names)

    # Roblox additionally needs the Studio (live DataModel) server.
    assert "roblox-studio" in by_engine["roblox"], by_engine["roblox"]
    # And the shared asset generator must reach every engine.
    assert set(servers["assets"]["engines"]) == {"threejs", "godot", "unity", "roblox"}, \
        servers["assets"]["engines"]


def test_mcp_registry_placeholders_are_known():
    reg = json.loads((ROOT / "mcp" / "registry.json").read_text(encoding="utf-8"))
    known = {"repo", "python", "studio_mcp"}
    servers = reg["servers"] if isinstance(reg, dict) and "servers" in reg else reg
    import re
    for name, spec in servers.items():
        blob = json.dumps(spec)
        for ph in re.findall(r"\{(\w+)\}", blob):
            assert ph in known, "server %s uses unknown placeholder {%s}" % (name, ph)


def test_generated_profiles_match_manifest():
    """The rendered pi profiles must agree with the ownership manifest."""
    manifest_path = ROOT / "mcp" / ".generated.json"
    if not manifest_path.is_file():
        return
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    for profile, names in manifest.items():
        if profile == "workbuddy":
            cfg_path = Path.home() / ".workbuddy-ai" / "mcp.json"
        else:
            cfg_path = ROOT / profile / "mcp.json"
        if not cfg_path.is_file():
            continue
        cfg = json.loads(cfg_path.read_text(encoding="utf-8"))
        have = set(cfg.get("mcpServers", {}))
        assert set(names) <= have, "%s is missing %s" % (profile, set(names) - have)


# ========================================================================= store
def test_store_fts_is_aligned_and_searchable():
    with tempfile.TemporaryDirectory() as td:
        db = Path(td) / "lexical.db"
        st = IndexStore(db)
        try:
            chunks = chunk_luau(SAMPLE_LUAU, "src/Shop.luau")
            n = st.upsert(chunks, None)
            assert n == len(chunks)
            assert st._conn.execute("SELECT COUNT(*) FROM chunks_fts").fetchone()[0] == n
            hits = st.lexical_search("FireClient", top_k=5)
            assert hits == [] or isinstance(hits, list)
            hits = st.lexical_search("setmetatable", top_k=5)
            assert hits, "BM25 found nothing for a word that is in the corpus"
        finally:
            st.close()


def test_indexer_prunes_files_that_left_the_corpus():
    """A deleted page must stop answering queries.

    `delete_paths` only replaces a stale revision of a file that still exists, so removing
    a page from `knowledge/` used to leave its chunks in the index forever - and they kept
    winning searches. That is how 1210 duplicate API pages would have survived a cleanup.
    """
    with tempfile.TemporaryDirectory() as td:
        root = Path(td) / "corpus"
        root.mkdir()
        (root / "A.luau").write_text("function A.run() end\n", encoding="utf-8")
        (root / "B.luau").write_text("function B.run() end\n", encoding="utf-8")
        st = IndexStore(Path(td) / "lexical.db")
        try:
            idx = Indexer(store=st, embedder=_ZeroEmbedder(), verbose=False)
            idx.index_source(root, "project")
            assert _indexed_paths(st) == {"A.luau", "B.luau"}, _indexed_paths(st)

            (root / "B.luau").unlink()
            rep = idx.index_source(root, "project")
            assert rep.pruned == 1, rep.pruned
            assert _indexed_paths(st) == {"A.luau"}, _indexed_paths(st)
            assert st._conn.execute("SELECT COUNT(*) FROM chunks_fts").fetchone()[0] == \
                st._conn.execute("SELECT COUNT(*) FROM chunks").fetchone()[0]
        finally:
            st.close()


def test_indexer_does_not_prune_an_empty_root():
    """A missing/empty corpus is a bug, not a reason to wipe 20k chunks."""
    with tempfile.TemporaryDirectory() as td:
        root = Path(td) / "corpus"
        root.mkdir()
        (root / "A.luau").write_text("function A.run() end\n", encoding="utf-8")
        st = IndexStore(Path(td) / "lexical.db")
        try:
            idx = Indexer(store=st, embedder=_ZeroEmbedder(), verbose=False)
            idx.index_source(root, "project")
            empty = Path(td) / "gone"
            empty.mkdir()
            rep = idx.index_source(empty, "project")
            assert rep.scanned == 0
            assert rep.pruned == 0, rep.pruned
            assert _indexed_paths(st) == {"A.luau"}, "an empty root wiped the index"
        finally:
            st.close()


def test_retriever_rrf_ordering():
    """RRF must rank a document present in both lists above one present in a single list."""
    dense = [("a", 0.9), ("b", 0.8)]
    lexical = [("b", 5.0), ("c", 4.0)]
    fused = Retriever._rrf(dense, lexical, k=60)
    order = [doc_id for doc_id, _ in fused]
    assert order[0] == "b", order          # b is in both lists
    assert set(order) == {"a", "b", "c"}, order


def test_source_priority_prefers_project_over_docs():
    assert SOURCE_PRIORITY["project"] > SOURCE_PRIORITY["official_docs"]
    assert SOURCE_PRIORITY["curated_kb"] > SOURCE_PRIORITY["engine_api"]
    assert SOURCE_PRIORITY["official_docs"] > SOURCE_PRIORITY["cloud_docs"]


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
