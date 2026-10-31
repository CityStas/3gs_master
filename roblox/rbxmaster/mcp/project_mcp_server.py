"""MCP server: file-level tools for a Roblox project, sandboxed to its root.

Deliberately narrow. The *live* DataModel is Roblox Studio's job - the built-in Studio MCP
server (Assistant -> Manage MCP Servers -> Enable Studio as MCP server) already exposes
`script_read`, `multi_edit`, `execute_luau`, `start_stop_play` and `get_console_output`,
and duplicating those here would give a 9B model two competing surfaces for one job.

What Studio's MCP cannot do is work on a project as files: a Rojo tree on disk, a place
that is currently closed, a lint pass before anything is opened. That is this server:

  info / list / read / write / edit / search   - the file layer, every path sandboxed
  lint                                        - Luau rules that need no toolchain
  place_info                                  - what is inside a .rbxlx without Studio
  studio_status / open_place                  - is the editor there, and open this place

Run standalone:

    python -m rbxmaster.mcp.project_mcp_server     # from the roblox/ directory
"""
from __future__ import annotations

import json
import sys
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

from mcp.server.fastmcp import FastMCP  # noqa: E402

from rbxmaster import config  # noqa: E402
from rbxmaster.luau import place as place_mod  # noqa: E402
from rbxmaster.luau import studio  # noqa: E402
from rbxmaster.luau.lint import lint_project, lint_text  # noqa: E402
from rbxmaster.luau.paths import (  # noqa: E402
    OutsideProject, place_files, project_engine, project_root, rojo_project, safe_path,
    script_context, source_files,
)

mcp = FastMCP("rbx-project")

TEXT_EXTS = {".luau", ".lua", ".json", ".jsonc", ".toml", ".yaml", ".yml", ".md", ".txt",
             ".xml", ".rbxlx", ".rbxmx"}
BACKUP_DIR = ".rbxmaster_backups"
MAX_READ_BYTES = 400_000


def _root(project: str = "") -> Path:
    return project_root(project)


def _fail(msg: str) -> str:
    return json.dumps({"ok": False, "error": msg}, ensure_ascii=False)


@mcp.tool()
def rbx_project_info(project: str = "") -> str:
    """What the active project is: root path, engine marker, Rojo project file, Luau file
    count, place files, and whether Roblox Studio is installed and running.

    Call this first in a new session - it is the difference between "I know the path" and
    "I know what is in it".
    """
    try:
        root = _root(project)
    except (ValueError, OutsideProject) as e:
        return _fail(str(e))
    src = source_files(root)
    places = place_files(root)
    rojo = rojo_project(root)
    return json.dumps({
        "ok": True,
        "root": str(root),
        "engine": project_engine(root),
        "rojo_project": str(rojo) if rojo else None,
        "luau_files": len(src),
        "luau_sample": [p.relative_to(root).as_posix() for p in src[:40]],
        "place_files": [{"path": p.relative_to(root).as_posix(), "bytes": p.stat().st_size}
                        for p in places],
        "studio": studio.status(),
    }, ensure_ascii=False, indent=1)


@mcp.tool()
def rbx_list_files(path: str = "", project: str = "", limit: int = 200) -> str:
    """List files and directories under `path` (relative to the project root, default ".").

    Directories come first. Hidden and vendored trees (`.git`, `Packages`, `node_modules`)
    are skipped - they are never what you are looking for.
    """
    try:
        root = _root(project)
        target = safe_path(root, path or ".")
    except (ValueError, OutsideProject) as e:
        return _fail(str(e))
    if not target.exists():
        return _fail(f"no such path: {path!r}")
    if target.is_file():
        return json.dumps({"ok": True, "file": path, "bytes": target.stat().st_size})
    dirs, files = [], []
    for p in sorted(target.iterdir(), key=lambda x: x.name.lower()):
        if p.name in config.PROJECT_SKIP_DIRS or p.name.startswith(".git"):
            continue
        rel = p.relative_to(root).as_posix()
        if p.is_dir():
            dirs.append(rel + "/")
        else:
            try:
                files.append({"path": rel, "bytes": p.stat().st_size})
            except OSError:
                files.append({"path": rel, "bytes": None})
    return json.dumps({"ok": True, "dir": str(target.relative_to(root).as_posix()),
                       "dirs": dirs[:limit], "files": files[:limit],
                       "truncated": len(dirs) + len(files) > limit}, ensure_ascii=False, indent=1)


@mcp.tool()
def rbx_read_file(path: str, project: str = "", start_line: int = 0, end_line: int = 0) -> str:
    """Read a project file with line numbers. `start_line`/`end_line` are 1-based and
    inclusive; 0 means "from the start" / "to the end".

    Luau files are returned verbatim - read the script you are about to change, not a
    fragment of it.
    """
    try:
        root = _root(project)
        target = safe_path(root, path)
    except (ValueError, OutsideProject) as e:
        return _fail(str(e))
    if not target.is_file():
        return _fail(f"not a file: {path!r}")
    if target.stat().st_size > MAX_READ_BYTES:
        return _fail(f"{path!r} is {target.stat().st_size} bytes - too large to read whole; "
                     f"use start_line/end_line")
    text = target.read_text(encoding="utf-8", errors="replace")
    lines = text.splitlines()
    a = max(1, int(start_line or 1))
    b = min(len(lines), int(end_line) if end_line else len(lines))
    body = "\n".join(f"{i:5d}  {lines[i - 1]}" for i in range(a, b + 1))
    return json.dumps({"ok": True, "path": path, "lines": len(lines), "from": a, "to": b,
                       "content": body}, ensure_ascii=False, indent=1)


@mcp.tool()
def rbx_write_file(path: str, content: str, project: str = "", backup: bool = True) -> str:
    """Create or overwrite a project file. A timestamped copy of the previous revision is
    kept in `.rbxmaster_backups/` unless `backup=false`.

    This writes to DISK. If the same script is also open in Studio, Studio holds the live
    copy and will overwrite you on save - use the Studio MCP `multi_edit` for a place that
    is open, and this tool for file-based (Rojo) projects.
    """
    try:
        root = _root(project)
        target = safe_path(root, path)
    except (ValueError, OutsideProject) as e:
        return _fail(str(e))
    if target.suffix.lower() not in TEXT_EXTS:
        return _fail(f"refusing to write {target.suffix!r}: not a text/source extension "
                     f"({', '.join(sorted(TEXT_EXTS))})")
    target.parent.mkdir(parents=True, exist_ok=True)
    backup_path = None
    if backup and target.is_file():
        rel = target.relative_to(root)
        stamp = time.strftime("%Y%m%d-%H%M%S")
        backup_path = root / BACKUP_DIR / rel.with_suffix(rel.suffix + f".{stamp}.bak")
        backup_path.parent.mkdir(parents=True, exist_ok=True)
        backup_path.write_bytes(target.read_bytes())
    target.write_text(content, encoding="utf-8", newline="\n")
    issues = lint_text(content, target.relative_to(root).as_posix())
    return json.dumps({"ok": True, "path": path, "bytes": len(content.encode("utf-8")),
                       "backup": str(backup_path.relative_to(root)) if backup_path else None,
                       "lint": [i.to_dict() for i in issues[:20]]}, ensure_ascii=False, indent=1)


@mcp.tool()
def rbx_edit_file(path: str, old: str, new: str, project: str = "", count: int = 1) -> str:
    """Replace an exact snippet in a file (`old` -> `new`), at most `count` times.

    Preferred over `rbx_write_file` for an existing script: it cannot silently drop the
    rest of the file. Fails loudly when `old` is absent or ambiguous, rather than guessing.
    """
    try:
        root = _root(project)
        target = safe_path(root, path)
    except (ValueError, OutsideProject) as e:
        return _fail(str(e))
    if not target.is_file():
        return _fail(f"not a file: {path!r}")
    text = target.read_text(encoding="utf-8", errors="replace")
    found = text.count(old)
    if found == 0:
        return _fail("`old` does not occur in the file - read it again before editing")
    if found > 1 and count == 1:
        return _fail(f"`old` occurs {found} times; pass count={found} to replace all, or "
                     f"include more context to make it unique")
    updated = text.replace(old, new, count if count else found)
    rel = target.relative_to(root)
    stamp = time.strftime("%Y%m%d-%H%M%S")
    backup_path = root / BACKUP_DIR / rel.with_suffix(rel.suffix + f".{stamp}.bak")
    backup_path.parent.mkdir(parents=True, exist_ok=True)
    backup_path.write_bytes(target.read_bytes())
    target.write_text(updated, encoding="utf-8", newline="\n")
    issues = lint_text(updated, rel.as_posix())
    return json.dumps({"ok": True, "path": path, "replaced": min(found, count or found),
                       "backup": str(backup_path.relative_to(root)),
                       "lint": [i.to_dict() for i in issues[:20]]}, ensure_ascii=False, indent=1)


@mcp.tool()
def rbx_search_scripts(pattern: str, project: str = "", regex: bool = False,
                       limit: int = 60) -> str:
    """Search the project's Luau sources for a string or regular expression.

    Returns `file:line: text` for each hit. Use it to find where a RemoteEvent is fired,
    where a service is required, or every use of a deprecated call.
    """
    import re
    try:
        root = _root(project)
    except (ValueError, OutsideProject) as e:
        return _fail(str(e))
    try:
        rx = re.compile(pattern if regex else re.escape(pattern), re.M)
    except re.error as e:
        return _fail(f"bad regex: {e}")
    hits = []
    for p in source_files(root):
        try:
            text = p.read_text(encoding="utf-8", errors="replace")
        except OSError:
            continue
        for i, line in enumerate(text.splitlines(), 1):
            if rx.search(line):
                hits.append(f"{p.relative_to(root).as_posix()}:{i}: {line.strip()[:200]}")
                if len(hits) >= limit:
                    break
        if len(hits) >= limit:
            break
    return json.dumps({"ok": True, "pattern": pattern, "count": len(hits), "hits": hits},
                      ensure_ascii=False, indent=1)


@mcp.tool()
def rbx_lint(path: str = "", project: str = "", errors_only: bool = False) -> str:
    """Lint Luau: one file when `path` is given, the whole project otherwise.

    Catches unbalanced `end`, deprecated globals (`wait`, `spawn`, `delay`, `tick`),
    two-argument `Instance.new`, lowercase method names (`:findFirstChild`), numeric
    `require`, `LoadLibrary`, server-only services used from a client script and
    `LocalPlayer` on the server. It is NOT a type checker and cannot prove the script
    compiles - Studio's own output is the authority for that.
    """
    try:
        root = _root(project)
    except (ValueError, OutsideProject) as e:
        return _fail(str(e))
    if path:
        try:
            target = safe_path(root, path)
        except (ValueError, OutsideProject) as e:
            return _fail(str(e))
        if not target.is_file():
            return _fail(f"not a file: {path!r}")
        issues = lint_text(target.read_text(encoding="utf-8", errors="replace"),
                           target.relative_to(root).as_posix())
    else:
        issues = lint_project(root)
    if errors_only:
        issues = [i for i in issues if i.severity == "error"]
    errors = sum(1 for i in issues if i.severity == "error")
    return json.dumps({"ok": errors == 0, "errors": errors,
                       "warnings": len(issues) - errors,
                       "issues": [i.to_dict() for i in issues[:120]]},
                      ensure_ascii=False, indent=1)


@mcp.tool()
def rbx_place_info(path: str = "", project: str = "") -> str:
    """Inspect a `.rbxlx`/`.rbxmx` place file without opening Studio: services, instance
    counts by class, and every script with its DataModel path, size and first lines.

    With no `path`, the project's first place file is used. This is how you answer "where
    is the shop logic" while Studio is closed.
    """
    try:
        root = _root(project)
    except (ValueError, OutsideProject) as e:
        return _fail(str(e))
    if path:
        try:
            target = safe_path(root, path)
        except (ValueError, OutsideProject) as e:
            return _fail(str(e))
    else:
        places = [p for p in place_files(root) if p.suffix.lower() in (".rbxlx", ".rbxmx")]
        if not places:
            return _fail("no .rbxlx/.rbxmx in the project - a binary .rbxl cannot be parsed "
                         "without Studio; save it as .rbxlx (File -> Save to File As)")
        target = places[0]
    info = place_mod.inspect(target)
    info["path"] = target.relative_to(root).as_posix()
    return json.dumps({"ok": "error" not in info, **info}, ensure_ascii=False, indent=1)


@mcp.tool()
def rbx_studio_status() -> str:
    """Is Roblox Studio installed, is it running, and is the built-in Studio MCP server up.

    Also restates the one-time setup: Studio's MCP server is enabled in the editor
    (Assistant -> ... -> Manage MCP Servers), not from here.
    """
    return json.dumps({"ok": True, **studio.status()}, ensure_ascii=False, indent=1)


@mcp.tool()
def rbx_open_place(path: str = "", project: str = "") -> str:
    """Open a place in Roblox Studio (detached - this call does not wait for the editor).

    Use it when the user asks to open the project and Studio is not running. Never call it
    to "test" a change: playtesting goes through the Studio MCP `start_stop_play`.
    """
    try:
        root = _root(project)
    except (ValueError, OutsideProject) as e:
        return _fail(str(e))
    target = None
    if path:
        try:
            target = safe_path(root, path)
        except (ValueError, OutsideProject) as e:
            return _fail(str(e))
        if not target.is_file():
            return _fail(f"not a file: {path!r}")
    else:
        places = place_files(root)
        target = places[0] if places else None
    return json.dumps({"ok": True, **studio.launch(target)}, ensure_ascii=False, indent=1)


def main() -> None:
    mcp.run(transport="stdio")


if __name__ == "__main__":
    main()
