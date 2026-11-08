#!/usr/bin/env python
"""Snapshot the open Studio place into the project folder.

    python roblox/tools/save.py                  # active project, wait for a fresh dump
    python roblox/tools/save.py test_1           # by name
    python roblox/tools/save.py test_1 --now     # newest dump, however old
    python roblox/tools/save.py test_1 --wait 0  # do not wait, fail if stale
    python roblox/tools/save.py --list           # what is in AutoSaves

WHY THIS EXISTS - and why it is not `Save`

A local `.rbxl` cannot be written from inside Studio by a script. The only two
documented entry points are cloud-only:

  * `DataModel:SavePlace()`        -> "placeID is not valid" on a PlaceId=0 file
  * `AssetService:SavePlaceAsync()`-> needs a place created by CreatePlaceAsync or a
                                      place with the save API enabled

`StudioService` has no save member at all (checked by name: Save, SavePlace,
SavePlaceAsync, PromptSavePlace, PromptSavePlaceAsync, PromptSaveSelection,
SaveSelectedToRoblox, SaveAs - every one absent), and `Plugin:PromptSaveSelectionAsync`
is unreachable because `plugin` is nil inside `execute_luau`. The MCP surface has no
save tool either (38 tools, none of them write the place), and `user_keyboard_input`
only accepts `datamodel_type = Client`, i.e. it types into the running *game*, never
into Studio's own File menu - so Ctrl+S cannot be injected.

What Studio does write on its own is an AutoRecovery dump: a complete `.rbxl`
serialisation of the live DataModel, every few minutes, into

    %LOCALAPPDATA%\\Roblox\\RobloxStudio\\AutoSaves\\<place>_AutoRecovery_0.rbxl

That file is a real save; it is just written on Studio's schedule, not ours
(`FIntAutoSaveFailSafeThresholdMs` = 420000, i.e. up to 7 minutes). This tool waits for
the next dump to appear, then copies it over the project's place file. It refuses to
overwrite with a dump that predates the current file unless `--now` is given, because
a stale dump silently reverts work.

If you want a *real* save - instant, no waiting, no snapshot - publish the place once
(File -> Publish). It then has a PlaceId, and `AssetService:SavePlaceAsync()` works
from `execute_luau` on every subsequent change.
"""
from __future__ import annotations

import argparse
import os
import shutil
import sys
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "roblox"))

from rbxmaster import config  # noqa: E402
from rbxmaster.luau.paths import place_files  # noqa: E402

POLL_SECONDS = 5.0


def auto_save_dir() -> Path:
    """Studio's AutoSaves folder, following the LOCALAPPDATA junction if there is one."""
    local = Path(os.environ.get("LOCALAPPDATA") or Path.home() / "AppData" / "Local")
    return local / "Roblox" / "RobloxStudio" / "AutoSaves"


def dumps() -> list[Path]:
    d = auto_save_dir()
    if not d.is_dir():
        return []
    return sorted((p for p in d.glob("*AutoRecovery*.rbxl")),
                  key=lambda p: p.stat().st_mtime, reverse=True)


def target_for(root: Path | None) -> Path | None:
    """The place file this project keeps. Prefers an existing one."""
    if root is None:
        return None
    places = [p for p in place_files(root) if p.suffix.lower() in (".rbxl", ".rbxlx")]
    return places[0] if places else None


def stamp(ts: float) -> str:
    return time.strftime("%H:%M:%S", time.localtime(ts))


def main() -> int:
    ap = argparse.ArgumentParser(description="Snapshot the open Studio place.")
    ap.add_argument("project", nargs="?", default="", help="project name or path")
    ap.add_argument("--wait", type=int, default=480,
                    help="seconds to wait for a dump newer than the target (default 480)")
    ap.add_argument("--now", action="store_true",
                    help="copy the newest dump even if it is older than the target")
    ap.add_argument("--list", action="store_true", help="list AutoSaves and exit")
    ap.add_argument("--out", default="", help="explicit destination file")
    a = ap.parse_args()

    found = dumps()
    if a.list:
        if not found:
            print(f"no dumps in {auto_save_dir()}")
            return 1
        print(f"AutoSaves: {auto_save_dir()}")
        for p in found:
            print(f"  {stamp(p.stat().st_mtime)}  {p.stat().st_size:>9,}  {p.name}")
        return 0

    if not found:
        print(f"[ERROR] no AutoRecovery dump in {auto_save_dir()}\n"
              f"        Studio writes one every few minutes while a place is open.",
              file=sys.stderr)
        return 2

    try:
        root = config.resolve_project(a.project)
    except ValueError as e:
        print(f"[WARN] {e}", file=sys.stderr)
        root = None

    target = Path(a.out) if a.out else target_for(root)
    if target is None:
        print("[ERROR] no place file in the project and no --out given", file=sys.stderr)
        return 2

    target_mtime = target.stat().st_mtime if target.is_file() else 0.0
    print(f"dump   : {found[0].name}  ({stamp(found[0].stat().st_mtime)}, "
          f"{found[0].stat().st_size:,} bytes)")
    print(f"target : {target}")
    print(f"current: {stamp(target_mtime) if target_mtime else '(missing)'}")

    newest = found[0]
    if newest.stat().st_mtime <= target_mtime and not a.now:
        deadline = time.time() + max(0, a.wait)
        print(f"stale - waiting up to {a.wait}s for Studio's next dump ...", flush=True)
        seen = newest.stat().st_mtime
        while time.time() < deadline:
            time.sleep(POLL_SECONDS)
            found = dumps()
            if found and found[0].stat().st_mtime > max(seen, target_mtime):
                newest = found[0]
                print(f"  fresh dump at {stamp(newest.stat().st_mtime)}", flush=True)
                break
            print(f"  {stamp(time.time())} still {stamp(seen)}", flush=True)
        else:
            print("[ERROR] no fresh dump appeared. Studio only autosaves on its own "
                  "timer (up to 7 min).\n"
                  "        Options: run again with --wait 0 to see this, or --now to "
                  "accept the stale dump,\n"
                  "        or publish the place once so AssetService:SavePlaceAsync "
                  "works instantly.", file=sys.stderr)
            return 3

    if target.is_file():
        backup = target.with_suffix(target.suffix + ".bak")
        shutil.copy2(target, backup)
        print(f"backup : {backup.name}")

    shutil.copy2(newest, target)
    size = target.stat().st_size
    print(f"wrote  : {target}  ({size:,} bytes, from {stamp(newest.stat().st_mtime)})")
    if size < 1024:
        print("[ERROR] the copy is suspiciously small", file=sys.stderr)
        return 4
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
