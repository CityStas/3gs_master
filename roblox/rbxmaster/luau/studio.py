"""Roblox Studio: is it installed, is it running, and how do we open a place.

Nothing here executes Luau. Studio itself is the execution surface - the built-in MCP
server (`StudioMCP.exe`, launched by `%LOCALAPPDATA%\\Roblox\\mcp.bat`) is what exposes
`execute_luau`, `start_stop_play` and `get_console_output` to the agent. This module only
answers "is the editor there" so the tools can tell the difference between "Studio is
closed" and "the code is wrong".
"""
from __future__ import annotations

import subprocess
import sys
from pathlib import Path

from .. import config

STUDIO_PROCESS = "RobloxStudioBeta.exe"
MCP_PROCESS = "StudioMCP.exe"
_CREATE_NO_WINDOW = 0x08000000
_DETACHED = 0x00000008
_NEW_GROUP = 0x00000200


def _tasklist(name: str) -> bool | None:
    """True if `name` is running, False if not, None when the check itself failed.

    `tasklist` is the only process query available without a dependency (psutil is not in
    the venv, and the WMI route needs COM, which the sandbox forbids). A failure returns
    None rather than False: "I could not look" must not be reported as "it is not there".
    """
    if sys.platform != "win32":
        return None
    try:
        proc = subprocess.run(
            ["tasklist", "/FI", f"IMAGENAME eq {name}", "/NH"],
            capture_output=True, timeout=10,
            creationflags=_CREATE_NO_WINDOW)
    except (OSError, subprocess.SubprocessError):
        return None
    # Bytes, not `text=True`: tasklist prints in the OEM codepage (cp866 on a Russian
    # Windows), and letting Python decode it as UTF-8 raises inside subprocess's reader
    # thread - the check then "fails" with a UnicodeDecodeError instead of answering.
    # The image name is pure ASCII either way, so utf-8-with-replace keeps it intact.
    out = (proc.stdout or b"").decode("utf-8", "replace").lower()
    if not out.strip():
        return None
    return name.lower() in out


def studio_running() -> bool | None:
    return _tasklist(STUDIO_PROCESS)


def mcp_running() -> bool | None:
    return _tasklist(MCP_PROCESS)


def status() -> dict:
    studio = config.STUDIO_EXE
    mcp = config.STUDIO_MCP
    return {
        "studio_exe": str(studio) if studio else None,
        "studio_build": config.STUDIO_BUILD or None,
        "studio_running": studio_running(),
        "studio_mcp": str(mcp) if mcp else None,
        "studio_mcp_running": mcp_running(),
        "docs_version": config.RBX_VERSION,
        "note": ("The built-in Studio MCP server is what edits a live place. Enable it in "
                 "Studio: Assistant -> ... -> Manage MCP Servers -> "
                 "'Enable Studio as MCP server'. This stack provides the knowledge base and "
                 "the file-level tools; it does not proxy Studio.")
    }


def launch(place: Path | None = None, timeout: float = 0.0) -> dict:
    """Open Studio, optionally with a place. Returns what was attempted, never blocks.

    Detached on purpose: Studio is a GUI application and the MCP server that calls this is
    a stdio child of the agent - waiting for Studio to exit would hang the session until
    the user closes the editor.
    """
    exe = config.STUDIO_EXE
    if not exe:
        return {"ok": False, "error": "Roblox Studio is not installed (or not found). "
                                      "Set ROBLOX_STUDIO to RobloxStudioBeta.exe."}
    args = [str(exe)]
    if place:
        args.append(str(place))
    try:
        subprocess.Popen(args, close_fds=True,
                         creationflags=_DETACHED | _NEW_GROUP | _CREATE_NO_WINDOW)
    except OSError as e:
        return {"ok": False, "error": f"{type(e).__name__}: {e}", "command": args}
    return {"ok": True, "launched": args,
            "hint": "Studio takes ~20 s to open a place; enable the MCP server once, in "
                    "Assistant -> ... -> Manage MCP Servers."}
