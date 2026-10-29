#!/usr/bin/env python
"""Check that a sector-2 spec and its textures agree with the level it extends.

`sector2.json` extends the Godot-derived level with new parallax textures and extra
gameplay islands. Nothing enforces that the spec and the assets stay in step, and every
way they can disagree fails *quietly* in the browser - a missing texture just leaves the
level_0 tile in place, a wrong-size texture stretches, a bad slot silently puts an island
in empty space.

What this checks, and why each one matters:

  * **The textures exist and match the level_0 reference size.** The spec swaps a texture
    onto the ODD parallax tiles only; the even tiles remain the level_0 originals, cloned
    adjacently on the same plane geometry (`scene.js`, `content.clone(true)` at `k*repeat`).
    Mismatched sizes are therefore visible as a seam that jumps at every tile boundary.
  * **`repeat_size` and the tile keys are consistent.** `applySector2` looks a layer up by
    `scroll_scale` and then patches only the tiles with an odd `k`. If `repeat_times` is 0
    there are no odd tiles at all, so the texture would load and never be used.
  * **`walk_max` and `camera_limit_right` agree.** `walk_max` is where the auto-walk loops
    and `camera_limit_right` is how far the camera may go; a `walk_max` beyond the camera
    limit walks the player off the edge of the frame, and one far short of it leaves dead
    space the camera can reach but the level does not fill.
  * **The gameplay slots land inside the reachable world.** An island at an x the camera
    can never reach is invisible work.

Usage
-----
    python tools/sector_check.py                       # ded_test
    python tools/sector_check.py --project projects/games/my_game
    python tools/sector_check.py --json
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from threejs import config  # noqa: E402

try:
    from PIL import Image
except ImportError:  # pragma: no cover
    raise SystemExit("Pillow is required:  .venv/Scripts/python.exe -m pip install Pillow")


def find(node: dict, name: str) -> dict | None:
    if node.get("name") == name:
        return node
    for child in node.get("children", []):
        hit = find(child, name)
        if hit:
            return hit
    return None


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--project", "-p", default="projects/games/my_game")
    ap.add_argument("--json", action="store_true")
    args = ap.parse_args()

    project = config.resolve_project(args.project)
    web3d = project / "web3d"
    level_p, spec_p = web3d / "level.json", web3d / "sector2.json"
    for p in (level_p, spec_p):
        if not p.exists():
            raise SystemExit(f"missing: {p}")

    level = json.loads(level_p.read_text(encoding="utf-8"))
    spec = json.loads(spec_p.read_text(encoding="utf-8"))

    checks: list[dict] = []

    def check(name: str, ok: bool, detail: str) -> None:
        checks.append({"check": name, "ok": bool(ok), "detail": detail})

    # --- the level's parallax layers, keyed by scroll_scale, as applySector2 finds them
    layers = {}
    for lname in ("FarBackground", "MidLayer"):
        node = find(level["tree"], lname)
        if not node:
            continue
        props = node.get("props", {})
        layers[lname] = {
            "scroll_scale": props.get("scroll_scale", [1, 0])[0],
            "repeat_size": props.get("repeat_size", [0, 0])[0],
            "repeat_times": props.get("repeat_times", 0),
        }

    check("level has FarBackground+MidLayer", len(layers) == 2,
          f"found {sorted(layers)}")

    # --- textures: exist, and sit at the reference size (level_0 is the reference)
    ref: dict[str, tuple[int, int]] = {}
    for key, sub in (("far", "far_back.png"), ("mid", "mid_layer.png"),
                     ("gameplay", "gameplay_layer.png")):
        refp = project / "Shrooms" / "level_0" / sub
        if refp.exists():
            ref[key] = Image.open(refp).size

    sizes: dict[str, tuple[int, int] | None] = {}
    for key in ("far", "mid", "gameplay"):
        part = spec.get(key)
        if not part:
            continue
        tp = project / part["texture"]
        if not tp.exists():
            sizes[key] = None
            check(f"{key} texture exists", False, f"missing {tp}")
            continue
        got = Image.open(tp).size
        sizes[key] = got
        want = ref.get(key)
        if want:
            check(f"{key} texture size == level_0", got == want,
                  f"{got[0]}x{got[1]} vs reference {want[0]}x{want[1]}"
                  if got != want else f"{got[0]}x{got[1]} matches reference")
        else:
            check(f"{key} texture size == level_0", True,
                  f"{got[0]}x{got[1]} (no level_0 reference to compare)")

    # --- odd tiles must exist for far/mid, or the texture is loaded and never used
    for key, lname, want_scale in (("far", "FarBackground", 0.25), ("mid", "MidLayer", 0.5)):
        if key not in spec:
            continue
        lay = layers.get(lname)
        if not lay:
            check(f"{key}: layer {lname} present", False, "not in level.json")
            continue
        check(f"{key}: layer found by scroll_scale", abs(lay["scroll_scale"] - want_scale) < 1e-6,
              f"scroll_scale={lay['scroll_scale']} (expected {want_scale})")
        times = lay["repeat_times"]
        odd = [k for k in range(-times, times + 1) if k != 0 and k % 2]
        check(f"{key}: has odd tiles to repaint", bool(odd),
              f"repeat_times={times} -> odd tiles {odd or 'NONE (texture would be unused)'}")

    # --- sector width vs the far layer's repeat_size: the tile step
    far = layers.get("FarBackground")
    if far and "sector_width" in spec:
        check("sector_width == FarBackground.repeat_size",
              abs(spec["sector_width"] - far["repeat_size"]) < 0.5,
              f"{spec['sector_width']} vs {far['repeat_size']}")

    # --- camera reach must cover walk_max, and both must cover the gameplay slots
    wr = spec.get("camera_limit_right")
    wm = spec.get("walk_max")
    if wr is not None and wm is not None:
        check("walk_max <= camera_limit_right", wm <= wr,
              f"walk_max={wm} camera_limit_right={wr}"
              + ("" if wm <= wr else "  (player walks past the camera's reach)"))

    gp = spec.get("gameplay") or {}
    slots = gp.get("slots") or []
    if slots and wr is not None:
        half = level["project"]["viewport"][0] / 2
        far_slot = max(slots)
        reach = wr - half
        check("gameplay slots inside camera reach", far_slot <= reach,
              f"furthest slot x={far_slot}, camera can frame up to x~{reach:.0f}")

    # --- the gameplay layer needs the size the level declares, not just any size
    if "gameplay" in spec and sizes.get("gameplay"):
        declared = None
        t = level.get("textures", {}).get("Shrooms/level_0/gameplay_layer.png")
        if t:
            declared = tuple(t)
        if declared:
            check("gameplay texture size == level.json declaration", sizes["gameplay"] == declared,
                  f"{sizes['gameplay']} vs {declared}")

    if args.json:
        print(json.dumps({"project": str(project), "checks": checks}, indent=2))
    else:
        print(f"project : {project}")
        print(f"spec    : {spec_p}")
        print()
        width = max(len(c["check"]) for c in checks) if checks else 0
        for c in checks:
            mark = "ok  " if c["ok"] else "FAIL"
            print(f"  {mark}  {c['check']:<{width}}  {c['detail']}")
        bad = [c for c in checks if not c["ok"]]
        print()
        if bad:
            print(f"{len(bad)} of {len(checks)} check(s) FAILED")
            return 1
        print(f"all {len(checks)} checks passed")

    return 1 if any(not c["ok"] for c in checks) else 0


if __name__ == "__main__":
    raise SystemExit(main())
