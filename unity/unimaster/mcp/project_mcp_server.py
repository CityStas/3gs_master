"""MCP server: the Unity project tool surface for the local 9B agent.

Deliberately small. The official Unity MCP exposes ~160 tools; a 9B model degrades
badly on a surface that wide (the Godot stack cut 193 -> 23 for the same reason). What
is here is the minimum that closes every step of a normal task:

  knowledge   unity_rag_search, unity_rag_status          (separate server)
  inspect     unity_project_info, unity_list_files, unity_read_file,
              unity_script_symbols, unity_find_symbol
  mutate      unity_write_script, unity_edit_script
  validate    unity_validate, unity_console, unity_run_method
  scaffold    unity_project_create
  show        unity_open_editor

Every path is sandboxed to the project root (`unimaster.unity.paths.safe_path`), and
every write drops a timestamped backup under `<project>/.unim/backups/` first.
"""
from __future__ import annotations

import json
import re
import subprocess
import sys
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

from mcp.server.fastmcp import FastMCP  # noqa: E402

from unimaster import config  # noqa: E402
from unimaster.rag.chunkers import chunk_csharp  # noqa: E402
from unimaster.unity import batch, lint, paths  # noqa: E402

mcp = FastMCP("unity-project")

WRITABLE_EXTS = {
    ".cs", ".shader", ".compute", ".cginc", ".hlsl", ".glsl", ".asmdef", ".asmref",
    ".json", ".md", ".txt", ".uxml", ".uss", ".yaml", ".yml", ".xml", ".meta",
}
BACKUP_DIRNAME = ".unim"


def _j(payload) -> str:
    return json.dumps(payload, ensure_ascii=False, indent=1)


def _root(project: str = "") -> Path:
    return paths.project_root(project)


def _backup(project: Path, target: Path) -> str:
    """Copy the current file aside before a write. Empty string when there was none."""
    if not target.is_file():
        return ""
    bdir = project / BACKUP_DIRNAME / "backups" / target.parent.relative_to(project)
    bdir.mkdir(parents=True, exist_ok=True)
    dst = bdir / f"{target.name}.{time.strftime('%Y%m%d-%H%M%S')}-{int(time.time()*1000)%1000}.bak"
    dst.write_bytes(target.read_bytes())
    return paths.rel_to(project, dst)


def _check_ext(path: Path) -> None:
    if path.suffix.lower() not in WRITABLE_EXTS:
        raise paths.UnityPathError(
            f"refusing to write '{path.suffix}' - allowed: {', '.join(sorted(WRITABLE_EXTS))}")


# =============================================================================
# Inspection
# =============================================================================
@mcp.tool()
def unity_project_info(project: str = "") -> str:
    """Summarise the active Unity project: editor version, packages, asset counts,
    scenes, assemblies, and whether the editor/CLI were found.

    Call this first in any Unity task - the version here decides which API is correct,
    and it is not the same as the version the RAG corpus was built from if the project
    was made with a different editor.
    """
    try:
        root = _root(project)
        if not paths.is_unity_project(root):
            return _j({"ok": False, "error": f"{root} is not a Unity project",
                       "hint": "a Unity project has ProjectSettings/ProjectVersion.txt and Assets/"})
        man = paths.manifest(root)
        assets = root / "Assets"
        cs = [p for p in assets.rglob("*.cs")] if assets.is_dir() else []
        scenes = [p for p in assets.rglob("*.unity")] if assets.is_dir() else []
        prefabs = [p for p in assets.rglob("*.prefab")] if assets.is_dir() else []
        asmdefs = [p for p in assets.rglob("*.asmdef")] if assets.is_dir() else []
        handler = lint.active_input_handler(root)
        return _j({
            "ok": True,
            "project": str(root),
            "editor_version": paths.unity_version_of(root),
            "rag_corpus_version": config.UNITY_VERSION,
            "version_matches_corpus": paths.unity_version_of(root).startswith(
                config.UNITY_DOC_VERSION),
            "unity_exe": str(config.UNITY_EDITOR) if config.UNITY_EDITOR else None,
            "unity_cli": str(config.UNITY_CLI) if config.UNITY_CLI else None,
            "editor_running": paths.editor_running(root),
            "active_input_handler": {0: "legacy Input Manager", 1: "Input System only",
                                     2: "both"}.get(handler, "unknown"),
            "packages": man.get("dependencies", {}),
            "counts": {"cs": len(cs), "scenes": len(scenes), "prefabs": len(prefabs),
                       "asmdef": len(asmdefs)},
            "scenes": [paths.rel_to(root, p) for p in scenes[:40]],
            "assemblies": [paths.rel_to(root, p) for p in asmdefs[:20]],
        })
    except Exception as e:  # noqa: BLE001
        return _j({"ok": False, "error": f"{type(e).__name__}: {e}"})


@mcp.tool()
def unity_list_files(subdir: str = "Assets", pattern: str = "*", limit: int = 300,
                     project: str = "") -> str:
    """List project files. `subdir` is relative to the project root (default Assets),
    `pattern` is a glob (`*.cs`, `*.prefab`, `*Player*`)."""
    try:
        root = _root(project)
        files = paths.list_files(root, subdir, pattern, max(1, min(int(limit or 300), 2000)))
        return _j({"ok": True, "count": len(files), "files": files})
    except Exception as e:  # noqa: BLE001
        return _j({"ok": False, "error": f"{type(e).__name__}: {e}"})


@mcp.tool()
def unity_read_file(path: str, max_bytes: int = 60000, project: str = "") -> str:
    """Read a project file. `path` is relative to the project root, e.g.
    "Assets/Scripts/PlayerController.cs". Output is clipped at `max_bytes`."""
    try:
        root = _root(project)
        target = paths.safe_path(root, path)
        if not target.is_file():
            return _j({"ok": False, "error": f"no such file: {paths.rel_to(root, target)}"})
        raw = target.read_bytes()
        clipped = len(raw) > max_bytes
        text = raw[:max_bytes].decode("utf-8", errors="replace")
        return _j({"ok": True, "path": paths.rel_to(root, target), "bytes": len(raw),
                   "clipped": clipped, "content": text})
    except Exception as e:  # noqa: BLE001
        return _j({"ok": False, "error": f"{type(e).__name__}: {e}"})


@mcp.tool()
def unity_script_symbols(path: str, project: str = "") -> str:
    """List the types and members declared in one C# file (namespace, classes with their
    base type, methods, properties, fields). Cheaper and more exact than reading the
    whole file when you only need to know what already exists."""
    try:
        root = _root(project)
        target = paths.safe_path(root, path)
        if not target.is_file():
            return _j({"ok": False, "error": f"no such file: {paths.rel_to(root, target)}"})
        chunks = chunk_csharp(target.read_text(encoding="utf-8", errors="replace"),
                              paths.rel_to(root, target), "project")
        symbols = [{"symbol": c.symbol, "kind": c.section, "class": c.class_name,
                    "namespace": c.namespace} for c in chunks if c.section != "header"]
        header = next((c for c in chunks if c.section == "header"), None)
        return _j({"ok": True, "path": paths.rel_to(root, target), "symbols": symbols,
                   "header": header.text if header else ""})
    except Exception as e:  # noqa: BLE001
        return _j({"ok": False, "error": f"{type(e).__name__}: {e}"})


@mcp.tool()
def unity_find_symbol(name: str, kind: str = "", limit: int = 40, project: str = "") -> str:
    """Find a C# type or member by name across the project's scripts.

    `name` is a substring (case-insensitive). `kind` filters to class/struct/interface/
    enum/method/property/field. Use it before adding a type that may already exist."""
    try:
        root = _root(project)
        assets = root / "Assets"
        if not assets.is_dir():
            return _j({"ok": False, "error": "no Assets/ directory in the project"})
        needle = name.lower()
        out = []
        for p in sorted(assets.rglob("*.cs")):
            if len(out) >= limit:
                break
            rel = paths.rel_to(root, p)
            try:
                chunks = chunk_csharp(p.read_text(encoding="utf-8", errors="replace"), rel, "project")
            except Exception:  # noqa: BLE001
                continue
            for c in chunks:
                if c.section == "header":
                    continue
                if needle in c.symbol.lower() and (not kind or c.section == kind):
                    out.append({"symbol": c.symbol, "kind": c.section, "path": rel,
                                "class": c.class_name})
                    if len(out) >= limit:
                        break
        return _j({"ok": True, "count": len(out), "matches": out})
    except Exception as e:  # noqa: BLE001
        return _j({"ok": False, "error": f"{type(e).__name__}: {e}"})


# =============================================================================
# Mutation
# =============================================================================
@mcp.tool()
def unity_write_script(path: str, content: str, project: str = "") -> str:
    """Create or overwrite a text asset (C#, shader, asmdef, json, ...) inside the project.

    The previous file, if any, is copied to .unim/backups/ first. Overwriting a file that
    already compiles is the single most expensive mistake with a small local model -
    prefer unity_edit_script for a targeted change to an existing file, and keep writes
    under ~150 lines (split larger files)."""
    try:
        root = _root(project)
        target = paths.safe_path(root, path)
        _check_ext(target)
        backup = _backup(root, target)
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(content, encoding="utf-8", newline="\n")
        return _j({"ok": True, "path": paths.rel_to(root, target),
                   "bytes": len(content.encode("utf-8")), "backup": backup,
                   "note": "validate with unity_validate before reporting it as done"})
    except Exception as e:  # noqa: BLE001
        return _j({"ok": False, "error": f"{type(e).__name__}: {e}"})


@mcp.tool()
def unity_edit_script(path: str, old_string: str, new_string: str,
                      replace_all: bool = False, project: str = "") -> str:
    """Patch an existing file by exact string replacement. This is the correct way to
    change a file that already works: a full rewrite regenerates every line and drops
    whatever was fixed before.

    `old_string` must match the file exactly, including indentation, and must be unique
    unless `replace_all` is true. A failed match returns the closest line numbers so the
    next attempt can be precise."""
    try:
        root = _root(project)
        target = paths.safe_path(root, path)
        if not target.is_file():
            return _j({"ok": False, "error": f"no such file: {paths.rel_to(root, target)}"})
        text = target.read_text(encoding="utf-8", errors="replace")
        count = text.count(old_string)
        if count == 0:
            # Give the model something actionable instead of just "not found".
            first = old_string.strip().splitlines()[0] if old_string.strip() else ""
            hints = [f"{i+1}: {ln.strip()}" for i, ln in enumerate(text.splitlines())
                     if first and first[:24] in ln][:5]
            return _j({"ok": False, "error": "old_string not found",
                       "nearby_lines": hints})
        if count > 1 and not replace_all:
            return _j({"ok": False,
                       "error": f"old_string occurs {count} times - add more context or "
                                f"pass replace_all=true"})
        backup = _backup(root, target)
        new_text = text.replace(old_string, new_string) if replace_all \
            else text.replace(old_string, new_string, 1)
        target.write_text(new_text, encoding="utf-8", newline="\n")
        return _j({"ok": True, "path": paths.rel_to(root, target),
                   "replacements": count if replace_all else 1, "backup": backup})
    except Exception as e:  # noqa: BLE001
        return _j({"ok": False, "error": f"{type(e).__name__}: {e}"})


# =============================================================================
# Validation / runtime
# =============================================================================
@mcp.tool()
def unity_validate(paths_list: list[str] | None = None, compile: bool = False,
                   timeout: int = 900, project: str = "") -> str:
    """Check the project's C# without (by default) launching the editor.

    Two layers, and they answer different questions:

    * `lint` - always runs, seconds. Catches what the compiler does *not*: API removed
      between Unity 4/5 and Unity 6 (`Application.LoadLevel`, `gameObject.rigidbody`,
      `rb.velocity`, `FindObjectsOfType<T>()`), editor-only API used in a runtime script,
      and the C# struct trap `transform.position.x = 5f` (CS1612). Pass `paths_list` to
      lint specific files; omit it to lint the whole Assets/ tree.
    * `compile` - `compile=true` runs the editor in batch mode (`-batchmode -nographics
      -quit`), which is the only real compile gate. It takes minutes and it **cannot run
      while the editor has the project open**; when the editor is open, read the errors
      it already produced with `unity_console()` instead - that is instant.

    A file that "was written" is not a result. A clean compile is.
    """
    try:
        root = _root(project)
        targets: list[Path] = []
        if paths_list:
            for rel in paths_list:
                p = paths.safe_path(root, rel)
                if p.is_file():
                    targets.append(p)
        else:
            assets = root / "Assets"
            targets = [p for p in assets.rglob("*.cs")] if assets.is_dir() else []

        objs: list[lint.Finding] = []
        for p in targets[:400]:
            try:
                text = p.read_text(encoding="utf-8", errors="replace")
            except OSError:
                continue
            objs.extend(lint.lint_csharp(text, paths.rel_to(root, p), root))

        findings = [f.to_dict() for f in objs]
        errs = lint.errors(objs)
        payload: dict = {
            "ok": not errs,
            "linted_files": len(targets),
            "error_count": len(errs),
            "warning_count": len(objs) - len(errs),
            "lint": findings[:80],
            "lint_hint": lint.lint_hint(objs),
        }
        if compile:
            res = batch.compile_project(root, timeout=max(60, int(timeout)))
            payload["compile"] = res.to_dict()
            payload["ok"] = payload["ok"] and res.ok
        else:
            payload["compile"] = "skipped (pass compile=true to run the editor batch gate)"
        # The model reads `warnings` even when it ignores the newer fields - mirror the
        # findings there, exactly like the Godot stack's godot_validate does.
        payload["warnings"] = [f"{f['script']}:{f['line']} {f['code']} {f['message']}"
                               for f in findings[:40]]
        return _j(payload)
    except Exception as e:  # noqa: BLE001
        return _j({"ok": False, "error": f"{type(e).__name__}: {e}"})


@mcp.tool()
def unity_console(limit: int = 40, project: str = "") -> str:
    """Compile and import errors from the live editor log and the project's import logs.

    When the Unity editor is open, it recompiles on every save, so this is the fast path:
    write a script, wait a moment, read the errors here. Prefer it over `compile=true`,
    which needs the editor closed and takes minutes."""
    try:
        root = _root(project)
        return _j({"ok": True, **batch.console_errors(root, max(1, min(int(limit or 40), 200)))})
    except Exception as e:  # noqa: BLE001
        return _j({"ok": False, "error": f"{type(e).__name__}: {e}"})


@mcp.tool()
def unity_run_method(method: str, args: str = "", timeout: int = 900, project: str = "") -> str:
    """Run a static Editor method in batch mode: `Unity.exe -batchmode -quit
    -executeMethod <Namespace.Class.Method>`.

    This is how a scene, a prefab or an asset is built from code the way the Unity docs
    recommend - the project's own editor script does the work, so the `.unity`/`.prefab`
    YAML stays valid by construction instead of being hand-written (the same reasoning as
    the Godot stack's "scenes are changed by Godot, not by editing .tscn").

    Requires the editor to be closed on this project."""
    try:
        root = _root(project)
        res = batch.execute_method(root, method, args, timeout=max(60, int(timeout)))
        return _j(res.to_dict())
    except Exception as e:  # noqa: BLE001
        return _j({"ok": False, "error": f"{type(e).__name__}: {e}"})


@mcp.tool()
def unity_project_create(name: str, timeout: int = 900, project: str = "") -> str:
    """Create a Unity project from nothing, via `Unity.exe -createProject`.

    Unity cannot be scaffolded by hand: a folder with a written `ProjectVersion.txt` and
    `manifest.json` is rejected by the editor, so the only reliable way to get a valid
    skeleton (`Assets/`, `Packages/`, `ProjectSettings/`, `Library/`) is to let the
    editor build it. Without this tool the very first step of "make me a level in an
    empty folder" is impossible - the same gap `godot_project_init` closes for Godot.

    `name` is a project NAME, not a path: it resolves under `projects/games/<name>`.
    Idempotent - an existing project is reported as `created: false` and left alone.

    Also writes `engine.json` (`{"engine": "unity", ...}`) into the project root. Without
    it `agent.cmd` picks the Three.js profile on the next launch and the model sees no
    `unity_*` tools at all - a project that exists but is unreachable. `ProjectVersion.txt`
    is the version source, so it is read back after the editor writes it.
    """
    try:
        root = config.resolve_project(project or name)
        if root.exists() and paths.is_unity_project(root):
            return _j({"ok": True, "created": False, "project": str(root),
                       "note": "already a Unity project; left untouched"})
        res = batch.create_project(root, timeout=max(120, int(timeout)))
        payload = res.to_dict()
        payload["created"] = bool(res.ok)
        payload["project"] = str(root)
        if res.ok:
            payload["engine_json"] = _write_engine_marker(root)
        return _j(payload)
    except Exception as e:  # noqa: BLE001
        return _j({"ok": False, "error": f"{type(e).__name__}: {e}"})


def _write_engine_marker(root: Path) -> str:
    """Drop `engine.json` with `"engine": "unity"` so `agent.cmd` picks this profile."""
    marker = root / "engine.json"
    if marker.exists():
        return "already present"
    # `ProjectVersion.txt` says `6000.3.26f1`; the marker records the docs line (`6000.3`),
    # which is what the corpus and the RAG are pinned to.
    ver = paths.unity_version_of(root) or config.UNITY_VERSION
    parts = ver.split(".")
    if len(parts) >= 2:
        ver = f"{parts[0]}.{parts[1]}"
    try:
        marker.write_text(json.dumps({"engine": "unity", "version": ver}, indent=2) + "\n",
                          encoding="utf-8")
        return "written"
    except OSError as e:
        return f"could not write engine.json: {e}"


@mcp.tool()
def unity_open_editor(project: str = "") -> str:
    """Open the project in the Unity editor window (for the human to look at), detached
    from this process so it survives the agent session.

    The editor is also the fastest feedback loop: once it is open it recompiles on save
    and `unity_console()` reports errors without any batch run."""
    try:
        root = _root(project)
        exe = paths.editor_exe()
        flags = 0
        try:  # Windows: detach so the editor does not die with the agent
            flags = subprocess.DETACHED_PROCESS | subprocess.CREATE_NEW_PROCESS_GROUP
        except AttributeError:
            pass
        proc = subprocess.Popen([str(exe), "-projectPath", str(root)],
                                creationflags=flags, close_fds=True)
        return _j({"ok": True, "pid": proc.pid, "project": str(root),
                   "note": "the editor takes 30-120 s to open; use unity_console() afterwards"})
    except Exception as e:  # noqa: BLE001
        return _j({"ok": False, "error": f"{type(e).__name__}: {e}"})


def main() -> None:
    mcp.run(transport="stdio")


if __name__ == "__main__":
    main()
