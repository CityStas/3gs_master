"""The reliability layer's contract, asserted on both implementations at once.

The policy is implemented twice - TypeScript inside `pi` (where the tool events are) and
Python everywhere else - so the interesting test is not "does Python classify ENOENT" but
"do both classify ENOENT identically". `tests/reliability_parity.mjs` runs the TypeScript
core under plain node (type stripping, no build step) and this file diffs the two answers.
A threshold or pattern changed in `mcp/reliability.json` therefore has to reach both, and a
change to one implementation alone fails here rather than in a live session.

The other half is the postcondition rule: a write that did not land must never be reported
as success. `verify_write` is tested against a real file, a missing file, a stale mtime and
a byte-count mismatch - the four ways the claim and the disk disagree.

Run:  .venv\\Scripts\\python.exe tests\\test_reliability.py
"""
from __future__ import annotations

import json
import os
import shutil
import subprocess
import sys
import tempfile
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
sys.path.insert(0, str(ROOT / "tools"))

import project_context  # noqa: E402
import reliability  # noqa: E402

PARITY = ROOT / "tests" / "reliability_parity.mjs"


def _node_parity() -> dict:
    """The TypeScript core's answers. Skips (loudly) when node is not on PATH."""
    node = shutil.which("node")
    if not node:
        raise AssertionError("node is not on PATH - cannot verify the TypeScript twin")
    proc = subprocess.run([node, str(PARITY)], capture_output=True, text=True, timeout=120)
    if proc.returncode != 0:
        raise AssertionError(f"reliability_parity.mjs failed:\n{proc.stderr[-2000:]}")
    return json.loads(proc.stdout)


# ---------------------------------------------------------------------------
# Policy
# ---------------------------------------------------------------------------

def test_the_policy_file_and_the_python_fallback_are_the_same_policy():
    """A fallback that disagrees with the file is a second policy nobody reads."""
    on_disk = json.loads((ROOT / "mcp" / "reliability.json").read_text(encoding="utf-8"))
    for section, value in reliability.DEFAULT_POLICY.items():
        if section == "errors":
            continue
        for key, expected in value.items():
            got = on_disk.get(section, {}).get(key, "<missing>")
            if got != expected:
                raise AssertionError(f"{section}.{key}: file has {got!r}, fallback has {expected!r}")
    codes_on_disk = set(on_disk["errors"]["codes"])
    codes_in_code = set(reliability.DEFAULT_POLICY["errors"]["codes"])
    if codes_on_disk != codes_in_code:
        raise AssertionError(
            f"error codes differ: file-only {codes_on_disk - codes_in_code}, "
            f"code-only {codes_in_code - codes_on_disk}"
        )
    if on_disk["errors"]["patterns"] != reliability.DEFAULT_POLICY["errors"]["patterns"]:
        raise AssertionError("error patterns differ between mcp/reliability.json and reliability.py")


def test_the_write_guard_constants_agree_with_the_extension():
    """write-guard.ts owns the block; the policy must describe the same budget."""
    src = (ROOT / "pi-extensions" / "write-guard.ts").read_text(encoding="utf-8")
    policy = reliability.load_policy()["write_guard"]
    for const, key in (("MAX_BYTES", "max_bytes"), ("MAX_LINES", "max_lines"), ("MAX_REWRITES", "max_rewrites")):
        needle = f"const {const} = "
        idx = src.find(needle)
        if idx < 0:
            raise AssertionError(f"{const} is not in write-guard.ts any more - update the policy")
        value = int(src[idx + len(needle):].split(";")[0].strip())
        if value != policy[key]:
            raise AssertionError(
                f"{const}={value} in write-guard.ts but {policy[key]} in mcp/reliability.json"
            )


# ---------------------------------------------------------------------------
# Parity: TypeScript core vs Python twin
# ---------------------------------------------------------------------------

def test_both_implementations_classify_every_fixture_identically():
    parity = _node_parity()
    policy = reliability.load_policy()
    for case in parity["classification"]:
        mine = reliability.classify(case["text"], policy)
        if mine["code"] != case["code"]:
            raise AssertionError(f"{case['text']!r}: ts={case['code']} py={mine['code']}")
        if mine["retryable"] != case["retryable"]:
            raise AssertionError(f"{case['text']!r}: retryable ts={case['retryable']} py={mine['retryable']}")
        if mine["next_action"] != case["next_action"]:
            raise AssertionError(f"{case['text']!r}: next_action differs between the twins")


def test_both_implementations_fingerprint_identically():
    parity = _node_parity()
    fixtures = [
        ("read", {"path": "a.ts", "limit": 10}, "projects/three/x"),
        ("read", {"limit": 10, "path": "a.ts"}, "projects/three/x"),
        ("read", {"path": "a.ts", "limit": 20}, "projects/three/x"),
        ("read", {"path": "a.ts", "limit": 10}, "projects/three/y"),
        ("rbx-project__read_file", {"path": "src/init.luau"}, ""),
        ("edit", {"path": "a.ts", "edits": [{"oldText": "x", "newText": "y"}]}, ""),
        ("edit", {"edits": [{"newText": "y", "oldText": "x"}], "path": "a.ts"}, ""),
    ]
    for (tool, args, ctx), expected in zip(fixtures, parity["fingerprints"]):
        got = reliability.fingerprint(tool, args, ctx)
        if got != expected:
            raise AssertionError(f"fingerprint({tool}, {args}) ts={expected} py={got}")
    # The properties the fingerprints are supposed to have, stated as tests.
    if reliability.fingerprint("read", {"path": "a", "n": 1}) != reliability.fingerprint("read", {"n": 1, "path": "a"}):
        raise AssertionError("key order changed the fingerprint")
    if reliability.fingerprint("read", {"path": "a"}, "p1") == reliability.fingerprint("read", {"path": "a"}, "p2"):
        raise AssertionError("the active project did not change the fingerprint")


def test_both_implementations_reach_the_same_guard_verdicts():
    parity = _node_parity()
    policy = reliability.load_policy()
    call = lambda tool, args, ctx="": (tool, args, ctx)  # noqa: E731
    read_a = call("read", {"path": "a.ts"})
    read_b = call("read", {"path": "b.ts"})
    grep_x = call("grep", {"pattern": "x"})
    build = call("bash", {"command": "npm run build"})

    scenarios = {
        "identical_hard_failure": [("after", read_a, True, "FILE_NOT_FOUND"), ("before", read_a, None, None)],
        "different_path_after_failure": [("after", read_a, True, "FILE_NOT_FOUND"), ("before", read_b, None, None)],
        "transient_budget": [
            ("after", build, True, "TIMEOUT"), ("after", build, True, "TIMEOUT"), ("before", build, None, None),
        ],
        "transient_exhausted": [
            ("after", build, True, "TIMEOUT"), ("after", build, True, "TIMEOUT"),
            ("after", build, True, "TIMEOUT"), ("before", build, None, None),
        ],
        "cycle_abab": [
            ("after", read_a, True, "FILE_NOT_FOUND"), ("after", grep_x, True, "INVALID_ARGUMENT"),
            ("after", read_a, True, "FILE_NOT_FOUND"), ("before", grep_x, None, None),
        ],
        "not_a_cycle": [
            ("after", read_a, True, "FILE_NOT_FOUND"), ("after", grep_x, True, "INVALID_ARGUMENT"),
            ("after", read_b, True, "FILE_NOT_FOUND"),
            ("before", call("grep", {"pattern": "y"}), None, None),
        ],
        "success_clears_counters": [("after", read_a, True, "FILE_NOT_FOUND"), ("after", read_a, False, None),
                                    ("before", read_a, None, None)],
        "mutation_clears_counters": [("after", read_a, True, "FILE_NOT_FOUND"), ("reset", None, None, None),
                                     ("before", read_a, None, None)],
    }

    for name, steps in scenarios.items():
        guard = reliability.LoopGuard(policy)
        verdict = None
        for op, target, is_error, code in steps:
            if op == "after":
                guard.after(target[0], target[1], bool(is_error), code, target[2])
            elif op == "reset":
                guard.reset_on_mutation()
            else:
                verdict = guard.before(target[0], target[1], target[2])
        expected = parity["scenarios"][name]
        got = {"decision": verdict["decision"], "code": verdict.get("code")}
        if got != expected:
            raise AssertionError(f"scenario {name}: ts={expected} py={got}")


def test_both_implementations_classify_inspection_identically():
    """The progress guard's only input: is this call looking or doing?"""
    parity = _node_parity()
    policy = reliability.load_policy()
    for case in parity["inspection"]:
        got = reliability.is_inspection(case["tool"], case["args"], policy)
        if got != case["inspection"]:
            raise AssertionError(
                f"is_inspection({case['tool']}, {case['args']}) ts={case['inspection']} py={got}"
            )


def test_both_implementations_reach_the_same_progress_verdicts():
    parity = _node_parity()
    policy = reliability.load_policy()
    budget = policy["progress_guard"]["block_after_inspections"]
    inspect = ("bash", {"command": "ls -la projects/three/test-space"})
    again = ("bash", {"command": "sed -n '1,40p' a.ts"})
    writes = ("write", {"path": "a.ts", "content": "x"})

    scenarios = {
        "blocks_after_the_budget": [(budget, inspect), ("before", again)],
        "allows_a_write_after_the_budget": [(budget, inspect), ("before", writes)],
        "silent_before_the_budget": [(budget - 1, inspect), ("before", again)],
        "stops_counting_once_something_was_written": [
            ("after", writes), (budget + 5, inspect), ("before", again),
        ],
        "read_only_mcp_tool_counts_as_inspection": [
            (budget, ("mcp__threejs_rag__threejs_rag_search", {"query": "terrain"}, True)),
            ("before", ("mcp__threejs_rag__threejs_rag_search", {"query": "craters"}, True)),
        ],
        "a_non_read_only_mcp_tool_is_progress": [
            (budget, inspect),
            ("before", ("mcp__assets__asset_image", {"prompt": "moon"}, False)),
        ],
    }
    for name, steps in scenarios.items():
        guard = reliability.ProgressGuard(policy)
        verdict = None
        for step in steps:
            if isinstance(step[0], int):
                tool, args, *rest = step[1]
                for _ in range(step[0]):
                    guard.after(tool, args, False, read_only=bool(rest and rest[0]))
            elif step[0] == "after":
                tool, args, *rest = step[1]
                guard.after(tool, args, False, read_only=bool(rest and rest[0]))
            else:
                tool, args, *rest = step[1]
                verdict = guard.before(tool, args, read_only=bool(rest and rest[0]))
        expected = parity["progress"][name]
        got = {"decision": verdict["decision"], "code": verdict.get("code")}
        if got != expected:
            raise AssertionError(f"progress scenario {name}: ts={expected} py={got}")


def test_both_implementations_reach_the_same_duplicate_success_verdicts():
    """`write` twice is refused; a `bash` in between makes the retry legitimate again."""
    parity = _node_parity()
    policy = reliability.load_policy()
    write_a = ("write", {"path": "a.ts", "content": "x"})
    edit_a = ("edit", {"path": "a.ts", "edits": [{"oldText": "x", "newText": "y"}]})
    build = ("bash", {"command": "npm run build"})

    scenarios = {
        "write_twice": [("after", write_a, False), ("before", write_a, None)],
        "write_bash_write": [("after", write_a, False), ("after", build, False), ("before", write_a, None)],
        "bash_twice_is_allowed": [("after", build, False), ("before", build, None)],
        "edit_after_write_is_a_different_call": [("after", write_a, False), ("before", edit_a, None)],
        "a_failed_write_records_nothing": [("after", write_a, True), ("before", write_a, None)],
    }
    for name, steps in scenarios.items():
        ledger = reliability.SuccessLedger(policy)
        verdict = None
        for op, target, is_error in steps:
            if op == "after":
                ledger.after(target[0], target[1], bool(is_error))
            else:
                verdict = ledger.before(target[0], target[1])
        expected = parity["ledger"][name]
        got = {"decision": verdict["decision"], "code": verdict.get("code")}
        if got != expected:
            raise AssertionError(f"ledger scenario {name}: ts={expected} py={got}")


# ---------------------------------------------------------------------------
# Postcondition verification
# ---------------------------------------------------------------------------

def test_verify_write_accepts_a_file_that_really_changed():
    with tempfile.TemporaryDirectory() as td:
        target = Path(td) / "note.md"
        target.write_text("hello", encoding="utf-8")
        result = reliability.verify_write(target, expected_bytes=5)
        if not result["ok"]:
            raise AssertionError(f"a fresh 5-byte file was rejected: {result}")
        if result["bytes"] != 5:
            raise AssertionError(f"byte count is wrong: {result}")


def test_verify_write_rejects_a_missing_file():
    with tempfile.TemporaryDirectory() as td:
        result = reliability.verify_write(Path(td) / "never-written.ts", expected_bytes=10)
        if result["ok"] or result["code"] != "WRITE_NOT_VERIFIED":
            raise AssertionError(f"a missing file passed verification: {result}")


def test_verify_write_rejects_a_stale_file():
    """The 'success' claim with an old mtime: the call did not touch this file."""
    with tempfile.TemporaryDirectory() as td:
        target = Path(td) / "old.ts"
        target.write_text("x" * 10, encoding="utf-8")
        old = time.time() - 3600
        os.utime(target, (old, old))
        result = reliability.verify_write(target, expected_bytes=10)
        if result["ok"] or result["code"] != "WRITE_NOT_VERIFIED":
            raise AssertionError(f"an untouched file passed verification: {result}")


def test_verify_write_rejects_a_truncated_write():
    with tempfile.TemporaryDirectory() as td:
        target = Path(td) / "short.ts"
        target.write_text("half", encoding="utf-8")
        result = reliability.verify_write(target, expected_bytes=4096)
        if result["ok"] or "4096" not in result["message"]:
            raise AssertionError(f"a truncated write passed verification: {result}")


# ---------------------------------------------------------------------------
# Structured errors
# ---------------------------------------------------------------------------

def test_the_error_contract_carries_a_next_action_and_is_parseable():
    payload = reliability.error_payload("FILE_NOT_FOUND", "read", path="projects/three/x/world.ts")
    body = json.loads(payload)
    for key in ("ok", "error_code", "retryable", "operation", "message", "next_action"):
        if key not in body:
            raise AssertionError(f"the contract is missing {key}: {body}")
    if body["ok"] is not False or body["retryable"] is not False:
        raise AssertionError(f"FILE_NOT_FOUND must be a hard failure: {body}")
    if "parent directory" not in body["next_action"]:
        raise AssertionError(f"the next action does not tell the model what to do: {body}")
    if body["path"] != "projects/three/x/world.ts":
        raise AssertionError(f"the path did not survive: {body}")


def test_every_declared_code_has_a_next_action():
    policy = reliability.load_policy()
    for code, entry in policy["errors"]["codes"].items():
        if not entry.get("next_action"):
            raise AssertionError(f"{code} has no next_action - the model would get a bare failure")
        if not isinstance(entry.get("retryable"), bool):
            raise AssertionError(f"{code} has no explicit retryable flag")


def test_every_pattern_code_exists():
    policy = reliability.load_policy()
    known = set(policy["errors"]["codes"])
    for code, needles in policy["errors"]["patterns"]:
        if code not in known:
            raise AssertionError(f"pattern code {code} is not declared in errors.codes")
        if not needles:
            raise AssertionError(f"pattern {code} has no needles")


# ---------------------------------------------------------------------------
# Project context
# ---------------------------------------------------------------------------

class _TempRepo:
    """A throwaway repository root, so the resolver is tested against a real tree."""

    def __init__(self):
        self.td = tempfile.TemporaryDirectory()
        self.root = Path(self.td.name)
        (self.root / "data").mkdir()
        (self.root / "projects" / "three").mkdir(parents=True)
        (self.root / "projects" / "three" / "engine.json").write_text('{"engine":"threejs"}', encoding="utf-8")
        (self.root / "projects" / "godot").mkdir(parents=True)
        (self.root / "projects" / "godot" / "engine.json").write_text('{"engine":"godot"}', encoding="utf-8")
        self._saved = (project_context.ROOT, getattr(project_context.project_layout, "REPO", None))

    def __enter__(self):
        project_context.ROOT = self.root
        project_context.project_layout.REPO = self.root
        return self

    def __exit__(self, *exc):
        project_context.ROOT, repo = self._saved
        project_context.project_layout.REPO = repo
        self.td.cleanup()
        return False

    def pointer(self, text: str) -> None:
        (self.root / "data" / "active_project.txt").write_text(text, encoding="utf-8")


def test_project_context_reports_where_the_engine_came_from():
    with _TempRepo() as repo:
        (repo.root / "projects" / "three" / "game").mkdir()
        repo.pointer("projects/three/game")
        info = project_context.resolve()
        if info["engine"] != "threejs":
            raise AssertionError(f"engine is {info['engine']}, expected the inherited threejs")
        if not info["engine_source"].endswith("projects/three/engine.json"):
            raise AssertionError(f"engine_source does not name the marker: {info['engine_source']}")
        if not info["project_exists"]:
            raise AssertionError("a live project was reported missing")
        if info["pointer_stale"]:
            raise AssertionError("a live pointer was reported stale")


def test_project_context_does_not_route_an_unknown_engine_into_threejs():
    """The silent misroute: a marker that says something else must be an error, not a default."""
    with _TempRepo() as repo:
        project = repo.root / "projects" / "godot" / "g"
        project.mkdir()
        (project / "engine.json").write_text('{"engine":"godot4"}', encoding="utf-8")
        repo.pointer("projects/godot/g")
        info = project_context.resolve()
        if info["engine"] is not None:
            raise AssertionError(f"an unknown engine was resolved to {info['engine']}")
        if not info["engine_ambiguous"] or "godot4" not in info["engine_ambiguous"]:
            raise AssertionError(f"the ambiguity was not named: {info}")
        import contextlib
        import io

        with contextlib.redirect_stdout(io.StringIO()), contextlib.redirect_stderr(io.StringIO()):
            rc = project_context.main(["x", "--json"])
        if rc == 0:
            raise AssertionError("the CLI exited 0 for an ambiguous engine")


def test_project_context_reports_a_stale_pointer_without_inventing_a_path():
    with _TempRepo() as repo:
        repo.pointer("projects/three/deleted-last-week")
        info = project_context.resolve()
        if not info["pointer_stale"]:
            raise AssertionError(f"a dead pointer was not reported stale: {info}")
        if info["project_exists"]:
            raise AssertionError("a nonexistent project was reported present")
        if "does not exist" not in (info["error"] or ""):
            raise AssertionError(f"the error does not say what is wrong: {info['error']}")


def test_project_context_with_no_pointer_is_not_an_error():
    with _TempRepo() as repo:
        info = project_context.resolve()
        if info["project"] is not None or info["error"] is not None:
            raise AssertionError(f"an empty pointer should be a plain session, got {info}")
        if info["engine"] != "threejs":
            raise AssertionError("the no-pointer default should be threejs")


# ---------------------------------------------------------------------------
# Logs and state
# ---------------------------------------------------------------------------

def _event(run, tool, ok, code=None, decision=None, verification=None):
    return {
        "ts": "2026-11-08T12:00:00.000Z",
        "run_id": run,
        "client": "pi",
        "engine": "threejs",
        "project": "projects/three/test-space",
        "tool": tool,
        "server": reliability.server_of(tool),
        "fingerprint": "abc",
        "ok": ok,
        "error_code": code,
        "decision": decision,
        "verification": verification,
    }


def test_the_log_roundtrips_and_state_groups_it_into_steps():
    policy = json.loads(json.dumps(reliability.DEFAULT_POLICY))
    with tempfile.TemporaryDirectory() as td:
        policy["logging"]["dir"] = str(Path(td) / "logs")
        log = Path(policy["logging"]["dir"])
        log.mkdir(parents=True)
        lines = [
            _event("run-1", "read", False, "FILE_NOT_FOUND", "classify"),
            _event("run-1", "read", False, "REPEATED_TOOL_CALL", "block"),
            _event("run-1", "write", True, None, "verify", "ok 12b"),
            _event("run-2", "bash", True),
        ]
        (log / "2026-11-08.jsonl").write_text(
            "\n".join(json.dumps(e) for e in lines) + "\nnot json at all\n", encoding="utf-8"
        )
        events = reliability.read_events(policy=policy)
        if len(events) != 4:
            raise AssertionError(f"a malformed line should be skipped, got {len(events)} events")
        grouped = reliability.runs(events)
        if len(grouped) != 2:
            raise AssertionError(f"expected 2 runs, got {len(grouped)}")
        first = next(r for r in grouped if r["run_id"] == "run-1")
        if first["steps"] != 3 or first["failures"] != 2 or first["blocked"] != 1:
            raise AssertionError(f"the step summary is wrong: {first}")
        if first["error_codes"] != ["FILE_NOT_FOUND", "REPEATED_TOOL_CALL"]:
            raise AssertionError(f"error codes are wrong: {first['error_codes']}")


def test_prune_keeps_the_newest_files_only():
    policy = json.loads(json.dumps(reliability.DEFAULT_POLICY))
    with tempfile.TemporaryDirectory() as td:
        policy["logging"]["dir"] = str(Path(td) / "logs")
        policy["logging"]["max_files"] = 3
        log = Path(policy["logging"]["dir"])
        log.mkdir(parents=True)
        for i in range(6):
            file = log / f"2026-11-0{i + 1}.jsonl"
            file.write_text("{}\n", encoding="utf-8")
            os.utime(file, (time.time() + i, time.time() + i))
        removed = reliability.prune(policy=policy)
        if len(removed) != 3:
            raise AssertionError(f"expected 3 files removed, got {removed}")
        remaining = sorted(p.name for p in log.glob("*.jsonl"))
        if remaining != ["2026-11-04.jsonl", "2026-11-05.jsonl", "2026-11-06.jsonl"]:
            raise AssertionError(f"the wrong files survived: {remaining}")


def test_the_extension_wiring_passes_its_smoke_test():
    """Drives loop-guard.ts through a fake pi API with real files (scenarios 1-6)."""
    node = shutil.which("node")
    if not node:
        raise AssertionError("node is not on PATH - cannot run tests/loop_guard_smoke.mjs")
    proc = subprocess.run(
        [node, str(ROOT / "tests" / "loop_guard_smoke.mjs")],
        capture_output=True, text=True, timeout=180,
    )
    if proc.returncode != 0:
        raise AssertionError(f"loop_guard_smoke.mjs failed:\n{proc.stdout[-2000:]}{proc.stderr[-2000:]}")


def test_the_selftest_suite_passes():
    rc = reliability.main(["reliability.py", "selftest"])
    if rc != 0:
        raise AssertionError("tools/reliability.py selftest reported failures")


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
