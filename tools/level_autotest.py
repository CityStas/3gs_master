#!/usr/bin/env python
"""Autotest harness: can a local LLM produce a *working* 2D level?

Why this exists. `level_lint.py` answers "is this JSON a valid level", `tscheck` /
`pagecheck` answer "will the page load". None of them answers the question that actually
matters when swapping a model: **given a plain 2D task, does the model write a level that
passes the linter, on the first try, without inventing paths or looping?** The pi session
logs show the failure mode is not a crash - it is a model that keeps writing
`GRID resolution = 4.0`, `cd /d ...` in bash, or a `run.json` that never lands, while
reporting success. So the score here is deterministic and mechanical.

Two halves
----------
    offline   (default)  - check the *fixtures*: every task prompt has a hand-written
                           reference level that MUST pass `level_lint.py`, and every
                           broken variant MUST fail it. This proves the scoring is honest
                           and needs no server. Always runnable.
    live     (--live)    - point the harness at a running `llama-server` (`:8080`) and ask
                           the model for each task. Each answer is scored with the same
                           linter, plus structural checks (real files referenced, nodes
                           of the right type). This is the model comparison.

No 3D generation is involved: 2D levels reference images only as *paths*, and the harness
supplies those paths from a fixture dir, so a run is seconds per task, not minutes.

    python tools/level_autotest.py                     # offline: fixtures + scorer
    python tools/level_autotest.py --live              # score the model on :8080
    python tools/level_autotest.py --live --model qwen3.5-9b
    python tools/level_autotest.py --live --no-thinking   # thinking off via chat_template_kwargs
    python tools/level_autotest.py --list              # what the tasks are
    python tools/level_autotest.py --save out/         # keep raw answers next to the report

Exit code 0 when every check in the chosen mode passed, 1 otherwise (so `cmd\\test.cmd`
can gate on it).
"""
from __future__ import annotations

import argparse
import json
import sys
import time
import urllib.error
import urllib.request
from dataclasses import dataclass, field
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from tools import level_lint as lint  # noqa: E402

#: Where a generated level is written while scoring. Kept next to the tool so a live run
#: leaves an inspectable artefact; `--save` keeps it, otherwise it is overwritten.
SCRATCH = ROOT / "logs" / "level_autotest"
SERVER = "http://127.0.0.1:8080/v1/chat/completions"
HEALTH = "http://127.0.0.1:8080/health"


# --------------------------------------------------------------------------- tasks
@dataclass
class Task:
    """One 2D-level request, with a reference level that the linter MUST accept."""
    name: str
    prompt: str
    #: A level written by hand that satisfies the task and passes `level_lint.py`. Proves
    #: the task is answerable and that the scorer can tell a pass from a fail.
    reference: dict
    #: Structural expectations the reference satisfies; checked on live answers too.
    require_types: tuple[str, ...] = ()
    require_names: tuple[str, ...] = ()
    #: Extra rule: paths a valid answer must not contain (the classic invented files).
    forbid_substrings: tuple[str, ...] = ()


def _tex(name: str, w: int, h: int) -> dict:
    return {name: [w, h]}


def _node(t: str, name: str, path: str, props: dict, children: list) -> dict:
    return {"type": t, "name": name, "path": path, "props": props, "children": children}


def task_platformer() -> Task:
    """Ground + two platforms + player with camera. The canonical minimal 2D level."""
    tex = "web3d/assets/tile_ground.png"
    return Task(
        name="platformer",
        prompt=(
            "Write a level.json for a 2D platformer in Three.js (format: LEVEL-SCHEMA.md).\n"
            "Requirements:\n"
            "- project.clear_color set;\n"
            "- a Backdrop layer with a ColorRect sky;\n"
            f"- a Platforms layer: solid Ground at y=660 with a CollisionShape2D, plus two\n"
            "  raised platforms;\n"
            "- a Player (CharacterBody2D) with position, a CollisionShape2D and a Camera2D\n"
            "  whose limits span the level;\n"
            "- textures may stay empty {} (no image files are available);\n"
            "Return ONLY the JSON object, no prose."
        ),
        reference={
            "project": {"name": "platformer", "viewport": [1280, 720],
                        "clear_color": [0.06, 0.07, 0.10, 1.0]},
            "textures": {},
            "frames": {},
            "tree": _node("Node2D", "Main", "Main", {}, [
                _node("Node2D", "Backdrop", "Backdrop", {"z_index": -200}, [
                    _node("ColorRect", "Sky", "Backdrop/Sky",
                          {"rect": [0, 0, 2560, 720], "color": [0.06, 0.07, 0.10, 1.0]}, []),
                ]),
                _node("Node2D", "Platforms", "Platforms", {"z_index": -100}, [
                    _node("StaticBody2D", "Ground", "Platforms/Ground",
                          {"position": [1280, 660]}, [
                              _node("CollisionShape2D", "CollisionShape2D",
                                    "Platforms/Ground/CollisionShape2D",
                                    {"shape": {"size": [2560, 80]}}, []),
                          ]),
                    _node("StaticBody2D", "Platform1", "Platforms/Platform1",
                          {"position": [700, 480]}, [
                              _node("CollisionShape2D", "CollisionShape2D",
                                    "Platforms/Platform1/CollisionShape2D",
                                    {"shape": {"size": [260, 32]}}, []),
                          ]),
                    _node("StaticBody2D", "Platform2", "Platforms/Platform2",
                          {"position": [1500, 360]}, [
                              _node("CollisionShape2D", "CollisionShape2D",
                                    "Platforms/Platform2/CollisionShape2D",
                                    {"shape": {"size": [260, 32]}}, []),
                          ]),
                ]),
                _node("CharacterBody2D", "Player", "Player", {"position": [160, 560], "z_index": 0}, [
                    _node("CollisionShape2D", "CollisionShape2D", "Player/CollisionShape2D",
                          {"shape": {"size": [40, 60]}}, []),
                    _node("Camera2D", "Camera2D", "Player/Camera2D",
                          {"limits": {"limit_left": 0, "limit_top": 0,
                                      "limit_right": 2560, "limit_bottom": 720},
                           "offset": [0, -180]}, []),
                ]),
            ]),
        },
        require_types=("StaticBody2D", "CharacterBody2D", "Camera2D", "CollisionShape2D"),
        require_names=("Player", "Camera2D", "Ground"),
        forbid_substrings=("example_tex", "REPLACE_ME", "TODO"),
    )


def task_sprite_scene() -> Task:
    """A decorative scene: parallax background + one sprite node that references a texture."""
    tex = "web3d/assets/far_sky.png"
    return Task(
        name="sprite_scene",
        prompt=(
            "Write a level.json: a 2D scene with a parallax far background and one sprite.\n"
            f"The only available texture is `{tex}` at 2170x725 - reference it by that path.\n"
            "Use a Parallax2D layer (scroll_scale 0.25) containing the sprite, and a\n"
            "Backdrop ColorRect behind it. Return ONLY the JSON object."
        ),
        reference={
            "project": {"name": "sprite_scene", "viewport": [1280, 720],
                        "clear_color": [0.02, 0.02, 0.05, 1.0]},
            "textures": _tex(tex, 2170, 725),
            "frames": {},
            "tree": _node("Node2D", "Main", "Main", {}, [
                _node("Node2D", "Backdrop", "Backdrop", {"z_index": -200}, [
                    _node("ColorRect", "Sky", "Backdrop/Sky",
                          {"rect": [0, 0, 2560, 720], "color": [0.02, 0.02, 0.05, 1.0]}, []),
                ]),
                _node("Parallax2D", "FarBackground", "FarBackground",
                      {"scroll_scale": [0.25, 0.25], "repeat_size": [1280, 0],
                       "repeat_times": 1, "z_index": -100}, [
                          _node("Sprite2D", "SkySprite", "FarBackground/SkySprite",
                                {"position": [1085, 362], "texture": tex}, []),
                      ]),
            ]),
        },
        require_types=("Parallax2D", "Sprite2D"),
        require_names=("FarBackground",),
        forbid_substrings=("example_tex", "REPLACE_ME"),
    )


TASKS: tuple[Task, ...] = (task_platformer(), task_sprite_scene())


# ------------------------------------------------------------------- broken variants
#: Each entry is (name, mutator) applied to a *reference* level to produce something the
#: linter MUST reject. This is what stops the scorer from being a rubber stamp.
def broken_variants() -> list[tuple[str, dict]]:
    out: list[tuple[str, dict]] = []

    ref = json.loads(json.dumps(TASKS[0].reference))
    del ref["tree"]["children"][1]["children"][0]["children"]  # drop a node's children[]
    out.append(("platformer: node without children[]", ref))

    ref = json.loads(json.dumps(TASKS[1].reference))
    # The classic: a Sprite2D referencing props.sprite instead of props.texture.
    ref["tree"]["children"][1]["children"][0]["props"].pop("texture", None)
    ref["tree"]["children"][1]["children"][0]["props"]["sprite"] = "far_sky.png"
    out.append(("sprite_scene: props.sprite instead of texture", ref))

    ref = json.loads(json.dumps(TASKS[1].reference))
    ref["textures"] = {"example_tex": {"url": "far_sky.png"}}  # name-keyed textures
    out.append(("sprite_scene: textures keyed by name", ref))

    ref = json.loads(json.dumps(TASKS[1].reference))
    ref["tree"]["children"][0]["children"][0]["type"] = "Sprite"  # Godot-ish type
    out.append(("sprite_scene: unknown node type", ref))

    ref = json.loads(json.dumps(TASKS[0].reference))
    del ref["project"]["clear_color"]
    out.append(("platformer: project without clear_color", ref))

    return out


# --------------------------------------------------------------------------- scoring
@dataclass
class Score:
    ok: bool
    errors: list[str] = field(default_factory=list)
    warnings: list[str] = field(default_factory=list)


def _write_stub_png(path: Path, w: int, h: int) -> None:
    """A real, tiny PNG with the requested dimensions in its IHDR.

    The linter reads the size straight from the file header and matches it against the
    `textures` block, so the fixture must contain true headers - a placeholder byte
    string would fail for the wrong reason.
    """
    import struct
    import zlib
    path.parent.mkdir(parents=True, exist_ok=True)
    raw = b"".join(b"\x00" + b"\x00\xff\x00\x00" * w for _ in range(h))

    def chunk(tag: bytes, data: bytes) -> bytes:
        return (struct.pack(">I", len(data)) + tag + data
                + struct.pack(">I", zlib.crc32(tag + data) & 0xffffffff))

    png = (b"\x89PNG\r\n\x1a\n"
           + chunk(b"IHDR", struct.pack(">IIBBBBB", w, h, 8, 6, 0, 0, 0))
           + chunk(b"IDAT", zlib.compress(raw, 9))
           + chunk(b"IEND", b""))
    path.write_bytes(png)


def materialize_textures(level: dict, project_root: Path) -> None:
    """Create the image files a level references, at the size it declares.

    The linter checks that `textures` keys are files that exist *and* that the declared
    size matches. Fixtures are self-contained: the harness makes the files instead of
    shipping binaries in the repo.
    """
    tex = level.get("textures")
    if not isinstance(tex, dict):
        return
    for key, size in tex.items():
        if not isinstance(key, str) or not isinstance(size, list) or len(size) != 2:
            continue
        try:
            w, h = int(size[0]), int(size[1])
        except (TypeError, ValueError):
            continue
        if w <= 0 or h <= 0:
            continue
        _write_stub_png(project_root / key, w, h)


def score_level(level: dict, task: Task, project_root: Path) -> Score:
    """Run the real linter and the task's structural expectations.

    The linter is the source of truth for schema; the structural checks are the source of
    truth for *intent* (a run that returns a syntactically fine but empty level must not
    pass).
    """
    level_file = project_root / "web3d" / "level.autotest.json"
    level_file.parent.mkdir(parents=True, exist_ok=True)
    materialize_textures(level, project_root)
    level_file.write_text(json.dumps(level, ensure_ascii=False, indent=2), encoding="utf-8")

    report = lint.lint(level_file)
    errors = [f"{where}: {msg}" for where, msg in report.errors]
    warnings = [f"{where}: {msg}" for where, msg in report.warns]

    # structural: required node types / names anywhere in the tree
    types, names = _walk(level.get("tree", {}))

    for want in task.require_types:
        if want not in types:
            errors.append(f"missing required node type: {want}")
    for want in task.require_names:
        if want not in names:
            errors.append(f"missing required node name: {want}")

    blob = json.dumps(level, ensure_ascii=False)
    for bad in task.forbid_substrings:
        if bad in blob:
            errors.append(f"contains forbidden token: {bad}")

    return Score(ok=not errors, errors=errors, warnings=warnings)


def _walk(node: dict) -> tuple[set[str], set[str]]:
    types: set[str] = set()
    names: set[str] = set()
    stack = [node]
    while stack:
        n = stack.pop()
        if not isinstance(n, dict):
            continue
        if n.get("type"):
            types.add(n["type"])
        if n.get("name"):
            names.add(n["name"])
        stack.extend(n.get("children") or [])
    return types, names


# ------------------------------------------------------------------------ live model
def server_up(timeout: float = 2.0) -> bool:
    try:
        req = urllib.request.Request(HEALTH, headers={"User-Agent": "level-autotest"})
        opener = urllib.request.build_opener(urllib.request.ProxyHandler({}))
        with opener.open(req, timeout=timeout):
            return True
    except (urllib.error.URLError, OSError):
        return False


def chat(model: str, prompt: str, thinking: bool, timeout: float = 600.0) -> tuple[str, str, int]:
    """One completion, tools off.

    `thinking` sets `chat_template_kwargs.enable_thinking`, which OVERRIDES the server's
    `--reasoning` flag. This is not cosmetic: measured on 2026-10-12, `enable_thinking:
    true` sent all 256 completion tokens into `reasoning_content` and returned an EMPTY
    `content` with `finish_reason='length'` - the model never wrote the answer. So the
    caller gets `finish_reason` and the token count back, to tell "no JSON" apart from
    "ran out of tokens mid-thought".
    """
    body = {
        "model": model,
        "messages": [
            {"role": "system",
             "content": "You write Three.js level.json files. Answer with JSON only."},
            {"role": "user", "content": prompt},
        ],
        "temperature": 0.2,
        "max_tokens": 8192,
        "chat_template_kwargs": {"enable_thinking": bool(thinking)},
    }
    data = json.dumps(body).encode("utf-8")
    req = urllib.request.Request(SERVER, data=data,
                                 headers={"Content-Type": "application/json"})
    opener = urllib.request.build_opener(urllib.request.ProxyHandler({}))
    with opener.open(req, timeout=timeout) as r:
        payload = json.loads(r.read().decode("utf-8", "replace"))
    choice = payload["choices"][0]
    msg = choice["message"]
    finish = choice.get("finish_reason", "?")
    used = (payload.get("usage") or {}).get("completion_tokens", 0)
    return (msg.get("content") or ""), finish, used


def extract_json(text: str) -> dict | None:
    """Pull the first balanced JSON object out of a model answer (fenced or bare)."""
    text = text.strip()
    if text.startswith("```"):
        text = text.split("```", 2)[1]
        if text.startswith("json"):
            text = text[4:]
    start = text.find("{")
    if start < 0:
        return None
    depth = 0
    in_str = False
    esc = False
    for i in range(start, len(text)):
        ch = text[i]
        if in_str:
            if esc:
                esc = False
            elif ch == "\\":
                esc = True
            elif ch == '"':
                in_str = False
            continue
        if ch == '"':
            in_str = True
        elif ch == "{":
            depth += 1
        elif ch == "}":
            depth -= 1
            if depth == 0:
                try:
                    return json.loads(text[start:i + 1])
                except json.JSONDecodeError:
                    return None
    return None


# --------------------------------------------------------------------------- modes
def run_offline(save_dir: Path | None) -> int:
    print("offline mode: fixtures and scorer\n")
    failures = 0

    scratch = SCRATCH / "_fixture_game"
    for task in TASKS:
        sc = score_level(task.reference, task, scratch)
        status = "PASS" if sc.ok else "FAIL"
        print(f"  [{status}] reference for {task.name}")
        for e in sc.errors:
            print(f"         error: {e}")
        if not sc.ok:
            failures += 1

    print()
    for name, level in broken_variants():
        sc = score_level(level, TASKS[0] if "platformer" in name else TASKS[1], scratch)
        status = "PASS" if not sc.ok else "FAIL"
        print(f"  [{status}] rejects {name}"
              + ("" if not sc.ok else "  <- linter accepted a broken level!"))
        if sc.ok:
            failures += 1

    print()
    if failures:
        print(f"OFFLINE FAILED: {failures} check(s) wrong")
    else:
        print("OFFLINE OK: every reference passes, every broken variant is rejected")
    return 1 if failures else 0


def run_live(args, save_dir: Path | None) -> int:
    if not server_up():
        print(f"no server at {HEALTH}. Start it with cmd\\serve-llm.cmd first.", file=sys.stderr)
        return 2

    print(f"live mode: model={args.model} thinking={'on' if args.thinking else 'off'}\n")
    scratch = SCRATCH / f"_live_{args.model.replace('/', '_').replace('.', '_')}"
    results = []

    for task in TASKS:
        t0 = time.time()
        try:
            answer, finish, used = chat(args.model, task.prompt,
                                        thinking=args.thinking, timeout=args.timeout)
        except Exception as exc:  # noqa: BLE001 - report, keep going
            print(f"  [ERROR] {task.name}: {exc}")
            results.append((task.name, False, 0.0, [f"request failed: {exc}"]))
            continue
        dt = time.time() - t0

        if save_dir is not None:
            save_dir.mkdir(parents=True, exist_ok=True)
            (save_dir / f"{task.name}.raw.txt").write_text(answer, encoding="utf-8")

        level = extract_json(answer)
        if level is None:
            # An empty answer with finish=length means the token budget went elsewhere -
            # almost always the thinking block. Say so, instead of a bare "no JSON".
            hint = ""
            if not answer.strip() and finish == "length":
                hint = (f" - EMPTY answer, finish=length after {used} tokens: the budget "
                        f"was spent in reasoning. Run with thinking OFF.")
            print(f"  [FAIL ] {task.name}: no JSON object in the answer "
                  f"({dt:.0f}s, finish={finish}, tokens={used}){hint}")
            results.append((task.name, False, dt,
                            [f"no JSON (finish={finish}, tokens={used})"]))
            continue

        sc = score_level(level, task, scratch)
        status = "PASS" if sc.ok else "FAIL"
        print(f"  [{status}] {task.name}  ({dt:.0f}s)")
        for e in sc.errors:
            print(f"         error: {e}")
        results.append((task.name, sc.ok, dt, sc.errors))

    passed = sum(1 for _, ok, _, _ in results if ok)
    total = len(results)
    print(f"\n{passed}/{total} tasks passed")
    if save_dir is not None:
        (save_dir / "report.json").write_text(
            json.dumps([{"task": n, "ok": ok, "seconds": round(d, 1), "errors": e}
                        for n, ok, d, e in results], ensure_ascii=False, indent=2),
            encoding="utf-8")
        print(f"raw answers + report in {save_dir}")
    return 0 if passed == total else 1


def main() -> int:
    p = argparse.ArgumentParser(description="Autotest 2D level generation with a local LLM.")
    p.add_argument("--live", action="store_true", help="score the model on :8080")
    p.add_argument("--model", default="qwen3.5-9b", help="model id / alias on the server")
    p.add_argument("--thinking", dest="thinking", action="store_true", default=False,
                   help="enable thinking (default: OFF - the known-good setting)")
    p.add_argument("--timeout", type=float, default=600.0, help="per-task seconds")
    p.add_argument("--list", action="store_true", help="print the tasks and exit")
    p.add_argument("--save", type=Path, default=None, help="directory for raw answers")
    a = p.parse_args()

    if a.list:
        for t in TASKS:
            print(f"{t.name}: {t.prompt.splitlines()[0]}")
        return 0

    save_dir = a.save
    if a.live:
        return run_live(a, save_dir)
    return run_offline(save_dir)


if __name__ == "__main__":
    raise SystemExit(main())
