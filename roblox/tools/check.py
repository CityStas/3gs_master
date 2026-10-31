#!/usr/bin/env python
"""Luau gate for a Roblox project - the `check.cmd` equivalent of this stack.

Two layers, one verdict:

  lint     the rules in `rbxmaster.luau.lint` (seconds, no toolchain)
  studio   a reminder that behaviour is only proven by a playtest (Studio MCP)

Warnings alone do not fail the gate; only errors do.

    python roblox/tools/check.py                     # active project
    python roblox/tools/check.py my_game             # by name under projects/games/
    python roblox/tools/check.py my_game --json
    python roblox/tools/check.py my_game --errors-only
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "roblox"))

from rbxmaster import config  # noqa: E402
from rbxmaster.luau.lint import lint_project  # noqa: E402
from rbxmaster.luau.paths import project_root, rojo_project, source_files  # noqa: E402


def main() -> int:
    ap = argparse.ArgumentParser(description="Lint a Roblox project's Luau.")
    ap.add_argument("project", nargs="?", default="",
                    help="project name or path (default: data/active_project.txt)")
    ap.add_argument("--json", action="store_true", help="machine-readable output")
    ap.add_argument("--errors-only", action="store_true", help="hide warnings")
    ap.add_argument("--limit", type=int, default=400, help="max files to lint")
    a = ap.parse_args()

    try:
        root = project_root(a.project)
    except ValueError as e:
        print(f"[ERROR] {e}", file=sys.stderr)
        return 2
    if not root.is_dir():
        print(f"[ERROR] not a directory: {root}", file=sys.stderr)
        return 2

    files = source_files(root)
    issues = lint_project(root, limit=a.limit)
    if a.errors_only:
        issues = [i for i in issues if i.severity == "error"]
    errors = sum(1 for i in issues if i.severity == "error")
    warnings = len(issues) - errors

    if a.json:
        print(json.dumps({"project": str(root), "files": len(files), "errors": errors,
                          "warnings": warnings,
                          "issues": [i.to_dict() for i in issues]},
                         ensure_ascii=False, indent=1))
        return 1 if errors else 0

    print(f"project : {root}")
    print(f"rojo    : {rojo_project(root) or 'no *.project.json (place-only project)'}")
    print(f"luau    : {len(files)} files")
    print()
    for i in issues:
        print("  " + i.text())
    if not issues:
        print("  no issues")
    print()
    print(f"errors {errors}, warnings {warnings}")
    if errors:
        print("\nVERDICT: FAIL - fix the errors above before opening Studio.")
    else:
        print("\nVERDICT: pass (static). Behaviour is only proven by a playtest: "
              "Studio MCP `start_stop_play` + `get_console_output`.")
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
