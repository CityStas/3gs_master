"""Roblox Studio: is it installed, is it running, and how do we open a place.

Nothing here executes Luau. Studio itself is the execution surface - the built-in MCP
server (`StudioMCP.exe`, launched by `%LOCALAPPDATA%\\Roblox\\mcp.bat`) is what exposes
`execute_luau`, `start_stop_play` and `get_console_output` to the agent. This module only
answers "is the editor there" so the tools can tell the difference between "Studio is
closed" and "the code is wrong".
"""
from __future__ import annotations

import os
import subprocess
import sys
from pathlib import Path

from .. import config

STUDIO_PROCESS = "RobloxStudioBeta.exe"
MCP_PROCESS = "StudioMCP.exe"
_CREATE_NO_WINDOW = 0x08000000
_DETACHED = 0x00000008
_NEW_GROUP = 0x00000200

# --- Why Studio is launched with a scrubbed proxy environment ----------------
# Studio reaches its own MCP server over a plain local WebSocket:
# `ws://127.0.0.1:13469/proxy` (the `StudioMCP.exe` proxy binds 13469 and Studio
# dials it). Studio's network stack honours `HTTP_PROXY` / `HTTPS_PROXY` and has
# no loopback exemption of its own, so a system-wide proxy makes that handshake
# go to the proxy instead of to 127.0.0.1. The proxy cannot CONNECT to a local
# port, the WebSocket never opens, and Studio ends up with **zero** MCP tools
# while the Assistant setting still reads `"mcp-server": {"enabled": true}` -
# which is why the symptom looks like "MCP is off" and the fix looked like a
# manual toggle. Measured on this machine: with the proxy env inherited, the
# Studio log has 0 lines mentioning "mcp" and `list_roblox_studios` returns
# `{"studios":[]}`; launched through this function, Studio connects within a
# second of opening the place.
_PROXY_VARS = ("http_proxy", "https_proxy", "all_proxy", "ftp_proxy",
               "HTTP_PROXY", "HTTPS_PROXY", "ALL_PROXY", "FTP_PROXY")


def _studio_env() -> dict[str, str]:
    """Environment for the Studio process: no outbound proxy, loopback exempt."""
    env = {k: v for k, v in os.environ.items() if k not in _PROXY_VARS}
    # Belt and braces: if anything re-adds a proxy, NO_PROXY still keeps 127.0.0.1
    # direct. Studio's WS client reads these two, not only the uppercase forms.
    no_proxy = ",".join(x for x in ("127.0.0.1", "localhost", "::1",
                                    env.get("NO_PROXY", "")) if x)
    env["NO_PROXY"] = no_proxy
    env["no_proxy"] = no_proxy
    return env


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
        "note": ("The built-in Studio MCP server is what edits a live place. It is a "
                 "toggle in Studio (Assistant -> ... -> Manage MCP Servers -> 'Enable "
                 "Studio as MCP server'), already enabled on this machine, and the "
                 "handshake needs a proxy-free loopback - see launch(). If "
                 "list_roblox_studios is empty, relaunch Studio through "
                 "`cmd\\roblox-open.cmd`, which strips the proxy environment.")
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
        subprocess.Popen(args, close_fds=True, env=_studio_env(),
                         creationflags=_DETACHED | _NEW_GROUP | _CREATE_NO_WINDOW)
    except OSError as e:
        return {"ok": False, "error": f"{type(e).__name__}: {e}", "command": args}
    return {"ok": True, "launched": args,
            "hint": "Studio takes ~20 s to open a place. The MCP bridge connects by "
                    "itself (see _studio_env: the proxy is stripped on purpose)."}
