#!/usr/bin/env python
"""Open Roblox Studio on a project's place (or on an empty baseplate).

    python roblox/tools/open.py                 # active project's first place file
    python roblox/tools/open.py my_game         # by name under projects/games/
    python roblox/tools/open.py my_game --empty # just Studio, no place
    python roblox/tools/open.py --studio E:\\path\\RobloxStudioBeta.exe

Detached on purpose: Studio is a GUI and this command must return to the shell.
The MCP surface of Studio is NOT started by this - enable it once inside Studio
(Assistant -> ... -> Manage MCP Servers -> Enable Studio as MCP server).
"""
from __future__ import annotations

import argparse
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "roblox"))

from rbxmaster import config  # noqa: E402
from rbxmaster.luau import studio  # noqa: E402
from rbxmaster.luau.paths import place_files  # noqa: E402


def main() -> int:
    ap = argparse.ArgumentParser(description="Open Roblox Studio on a place.")
    ap.add_argument("project", nargs="?", default="", help="project name or path")
    ap.add_argument("--empty", action="store_true", help="open Studio without a place")
    ap.add_argument("--studio", default="", help="explicit path to RobloxStudioBeta.exe")
    a = ap.parse_args()

    if a.studio:
        exe = Path(a.studio)
        if not exe.is_file():
            print(f"[ERROR] not found: {exe}", file=sys.stderr)
            return 2
        config.STUDIO_EXE = exe                     # type: ignore[assignment]
    elif not config.STUDIO_EXE:
        print("[ERROR] Roblox Studio not found. Install it, or set ROBLOX_STUDIO to "
              "RobloxStudioBeta.exe.", file=sys.stderr)
        return 2

    place: Path | None = None
    if not a.empty:
        try:
            root = config.resolve_project(a.project)
        except ValueError as e:
            print(f"[WARN] {e} - opening Studio without a place", file=sys.stderr)
            root = None
        if root:
            places = [p for p in place_files(root) if p.suffix.lower() in (".rbxlx", ".rbxl")]
            if places:
                place = places[0]
            else:
                print(f"[WARN] no .rbxlx/.rbxl in {root} - opening Studio without a place",
                      file=sys.stderr)

    result = studio.launch(place)
    print(f"studio : {config.STUDIO_EXE}")
    print(f"place  : {place or '(none)'}")
    if not result.get("ok"):
        print(f"[ERROR] {result.get('error')}", file=sys.stderr)
        return 1
    print("opened. Enable the MCP server once: Assistant -> ... -> Manage MCP Servers.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
