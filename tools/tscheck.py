#!/usr/bin/env python
"""Compact TypeScript error report for a game directory.

`tsc --noEmit` is the only real feedback loop when editing the games, but its output
is raw and expensive: 75 errors is ~60 lines, and a single `head -50` both burns context
and silently hides every file after the 50th. The agent then fixes one file, re-runs,
fixes the next, and never sees the whole picture.

This prints the same information in a shape that is cheap to read and hard to misread:

    * a one-line verdict (`OK` / `errors: N`),
    * the count per error code and per file, worst first,
    * every *substantive* error in full,
    * unused-symbol noise (`TS6133`/`TS6196`) collapsed to one line each.

Usage
-----
    python tools/tscheck.py                    # the active project (data/active_project.txt)
    python tools/tscheck.py my_game                        # name under projects/games/
    python tools/tscheck.py projects/games/my_game         # by path
    python tools/tscheck.py --full             # raw tsc output, unsummarised
    python tools/tscheck.py --json             # machine-readable
    python tools/tscheck.py --code TS6133      # only one error code

Exit code is 0 when the project compiles, 1 when it does not - so it can gate a build.
"""

from __future__ import annotations

import argparse
import json
import re
import shutil
import subprocess
import sys
from collections import Counter, defaultdict
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from threejs import config  # noqa: E402

# `src/foo.ts(12,5): error TS2322: Type 'string' is not assignable to type 'number'.`
# tsc also emits continuation lines (indented, no file prefix) that explain the error;
# they are attached to the entry above them.
ERROR_RE = re.compile(r"^(?P<file>[^(]+)\((?P<line>\d+),(?P<col>\d+)\): error (?P<code>TS\d+): (?P<msg>.*)$")

# Errors that say "you declared something and never used it". Real, but they are style
# noise next to a type error, and on a strict scaffold they are usually the majority.
NOISE_CODES = {"TS6133", "TS6196", "TS6192"}


def decode(raw: bytes) -> str:
    """tsc writes UTF-8, but a Russian Windows console can hand back CP866."""
    for enc in ("utf-8", "cp866", "cp1251"):
        try:
            return raw.decode(enc)
        except UnicodeDecodeError:
            continue
    return raw.decode("utf-8", "replace")


def find_tsc(project: Path) -> Path | None:
    """Prefer the project-local compiler. `npx` may decide to install and then prompt,
    and there is no TTY - the prompt is cancelled and the turn is wasted."""
    for candidate in (
        project / "node_modules" / "typescript" / "bin" / "tsc",
        project / "node_modules" / ".bin" / "tsc",
    ):
        if candidate.exists():
            return candidate
    return None


def run_tsc(project: Path, tsc: Path) -> tuple[int, str]:
    node = shutil.which("node")
    if not node:
        raise SystemExit(
            "[ERROR] `node` is not on PATH. Start this from a shell where node works "
            "(the project launchers rely on it), or add node to PATH."
        )
    proc = subprocess.run(
        [node, str(tsc), "--noEmit"],
        cwd=str(project),
        capture_output=True,
        creationflags=getattr(subprocess, "CREATE_NO_WINDOW", 0),
    )
    return proc.returncode, decode(proc.stdout or b"") + decode(proc.stderr or b"")


def parse(text: str) -> list[dict]:
    """Group tsc's output into one record per error, with its continuation lines."""
    errors: list[dict] = []
    for line in text.splitlines():
        if not line.strip():
            continue
        m = ERROR_RE.match(line)
        if m:
            errors.append(
                {
                    "file": m.group("file").strip().replace("\\", "/"),
                    "line": int(m.group("line")),
                    "col": int(m.group("col")),
                    "code": m.group("code"),
                    "msg": m.group("msg").strip(),
                    "detail": [],
                }
            )
        elif errors:
            errors[-1]["detail"].append(line.rstrip())
    return errors


def summarise(errors: list[dict], top: int = 0) -> str:
    if not errors:
        return "OK - 0 errors"

    by_code = Counter(e["code"] for e in errors)
    by_file = Counter(e["file"] for e in errors)
    noise = [e for e in errors if e["code"] in NOISE_CODES]
    real = [e for e in errors if e["code"] not in NOISE_CODES]

    out: list[str] = [f"errors: {len(errors)}   (substantive {len(real)}, unused-symbol {len(noise)})"]
    out.append("")
    out.append("by code: " + "  ".join(f"{c} x{n}" for c, n in by_code.most_common()))
    out.append("by file:")
    shown = by_file.most_common(top) if top else by_file.most_common()
    for f, n in shown:
        out.append(f"  {n:3d}  {f}")
    if top and len(by_file) > top:
        out.append(f"  ... and {len(by_file) - top} more files")

    if real:
        out.append("")
        out.append(f"substantive errors ({len(real)}):")
        for e in real:
            out.append(f"  {e['file']}({e['line']},{e['col']}): {e['code']}: {e['msg']}")
            for d in e["detail"]:
                out.append(f"      {d.strip()}")
    if noise:
        out.append("")
        out.append(f"unused-symbol errors ({len(noise)}) - prefix the symbol with `_`, "
                   f"or delete it if it is genuinely dead:")
        for e in noise:
            out.append(f"  {e['file']}({e['line']}): {e['code']}: {e['msg']}")
    return "\n".join(out)


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description="Compact TypeScript error report for a game directory.")
    ap.add_argument("project", nargs="?", default="",
                    help="game name under projects/games/, a path, or empty for the active project")
    ap.add_argument("--full", action="store_true", help="raw tsc output, unsummarised")
    ap.add_argument("--json", action="store_true", help="machine-readable output")
    ap.add_argument("--code", help="only report this error code, e.g. TS2531")
    ap.add_argument("--top", type=int, default=0, help="show only the N worst files")
    args = ap.parse_args(argv)

    try:
        project = config.resolve_project(args.project)
    except ValueError as exc:
        print(f"[ERROR] {exc}", file=sys.stderr)
        return 2

    if not project.is_dir():
        print(f"[ERROR] not a directory: {project}", file=sys.stderr)
        return 2

    tsc = find_tsc(project)
    if tsc is None:
        print(
            f"[ERROR] no TypeScript compiler in {project / 'node_modules'}.\n"
            f"        Run `npm install` in that directory first.",
            file=sys.stderr,
        )
        return 2

    rc, text = run_tsc(project, tsc)
    errors = parse(text)
    if args.code:
        errors = [e for e in errors if e["code"] == args.code]

    if args.json:
        print(json.dumps({"project": str(project), "count": len(errors), "errors": errors},
                         ensure_ascii=False, indent=2))
    elif args.full:
        print(text.rstrip() or "OK - 0 errors")
    else:
        print(f"project: {project}")
        print(f"tsc:     {tsc.relative_to(project).as_posix()}")
        print(summarise(errors, top=args.top))

    return 0 if not errors else 1


if __name__ == "__main__":
    raise SystemExit(main())
