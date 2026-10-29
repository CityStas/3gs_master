"""Tests for `tools/level_autotest.py` - the offline half of the model harness.

The harness has two jobs: score a model's level.json with the *real* linter, and prove
the scorer is honest. Only the second half is testable without a running server, and it
is the half that matters: a scorer that accepts a broken level is worse than no scorer,
because it turns "the model is bad" into "the model is fine".

These tests pin the three ways the scoring could silently rot:
  1. a reference level stops passing (the fixtures drifted from the schema);
  2. a broken variant starts passing (the linter gained a blind spot, or the harness
     stopped calling it);
  3. `extract_json` mis-parses a fenced or chatty answer.

The live half (`--live`) talks to `:8080` and is deliberately NOT exercised here - a
unit test must not require a GPU.
"""
from pathlib import Path
import json
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from tools import level_autotest as la  # noqa: E402


def _scratch(tmp: Path) -> Path:
    return tmp / "_scratch_game"


# --------------------------------------------------------------- fixtures are valid
def test_every_reference_level_passes_the_linter(tmp_path=None):
    import tempfile
    for task in la.TASKS:
        with tempfile.TemporaryDirectory() as d:
            sc = la.score_level(task.reference, task, _scratch(Path(d)))
            assert sc.ok, f"reference for {task.name} must pass, got: {sc.errors}"


def test_every_broken_variant_is_rejected(tmp_path=None):
    import tempfile
    for name, level in la.broken_variants():
        task = la.TASKS[0] if "platformer" in name else la.TASKS[1]
        with tempfile.TemporaryDirectory() as d:
            sc = la.score_level(level, task, _scratch(Path(d)))
            assert not sc.ok, f"linter accepted a broken level: {name}"


# ------------------------------------------------------- structural checks are live
def test_a_valid_but_empty_level_fails_the_structural_check():
    """The linter says an empty tree is schema-valid; the task says it is not an answer."""
    import tempfile
    empty = {
        "project": {"name": "x", "clear_color": [0, 0, 0, 1]},
        "textures": {}, "frames": {},
        "tree": {"type": "Node2D", "name": "Main", "path": "Main", "props": {}, "children": []},
    }
    with tempfile.TemporaryDirectory() as d:
        sc = la.score_level(empty, la.TASKS[0], _scratch(Path(d)))
        assert not sc.ok
        assert any("missing required" in e for e in sc.errors), sc.errors


# --------------------------------------------------------------------- json extraction
def test_extract_json_handles_fenced_answers():
    assert la.extract_json('```json\n{"a": 1}\n```') == {"a": 1}
    assert la.extract_json('```\n{"a": 1}\n```') == {"a": 1}


def test_extract_json_ignores_prose_around_the_object():
    assert la.extract_json('Sure! Here it is:\n{"a": {"b": 2}}\nDone.') == {"a": {"b": 2}}


def test_extract_json_tolerates_braces_inside_strings():
    assert la.extract_json('{"note": "a } brace", "n": 1}') == {"note": "a } brace", "n": 1}


def test_extract_json_returns_none_when_there_is_no_object():
    assert la.extract_json("no json here") is None
    assert la.extract_json("") is None


# ----------------------------------------------------------------- texture materialising
def test_materialise_textures_creates_files_the_linter_can_size():
    import tempfile
    from tools.level_lint import image_size
    with tempfile.TemporaryDirectory() as d:
        root = Path(d)
        la.materialize_textures({"textures": {"web3d/assets/x.png": [64, 32]}}, root)
        f = root / "web3d" / "assets" / "x.png"
        assert f.exists()
        assert image_size(f) == [64, 32]


if __name__ == "__main__":
    fails = 0
    for name, fn in sorted(globals().items()):
        if name.startswith("test_") and callable(fn):
            try:
                fn()
                print(f"  ok   {name}")
            except AssertionError as exc:
                fails += 1
                print(f"  FAIL {name}: {exc}")
    print("FAILED" if fails else "ok - test_level_autotest")
    raise SystemExit(1 if fails else 0)
