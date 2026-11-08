#!/usr/bin/env python
"""Keeps one Studio MCP proxy alive so Roblox Studio has something to attach to.

Studio connects to a fixed local websocket port (13469 on this build) and gives up after
~8 retries (about 25 s). A proxy spawned per tool call exists for a few seconds, so Studio
usually finds nothing and stops trying - that is the "studios: []" failure mode.

This process owns the port for as long as it runs; per-call proxies from studio_cli.py
relay through it. Start it once per session:

    python roblox/tools/studio_anchor.py &          # bash, background
    python roblox/tools/studio_anchor.py --check    # is anything already listening

It spawns StudioMCP.exe directly (not through mcp.bat) so no shell is involved.
"""
from __future__ import annotations

import argparse
import json
import os
import subprocess
import sys
import time
from pathlib import Path

STUDIO_MCP = Path(r"E:\Programs\Roblox Studio\app\Versions\version-67c8b1dedbb74fed\StudioMCP.exe")
PORT = 13469


def listening(port: int = PORT) -> bool:
    import socket
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.settimeout(0.3)
        return sock.connect_ex(("127.0.0.1", port)) == 0


def main() -> int:
    ap = argparse.ArgumentParser(description="Anchor proxy for the Studio MCP server.")
    ap.add_argument("--check", action="store_true")
    ap.add_argument("--log", default=str(Path(__file__).resolve().parents[1] / "output" / "mcp_anchor.log"))
    a = ap.parse_args()

    if a.check:
        print(f"port {PORT}: {'LISTENING' if listening() else 'free'}")
        return 0 if listening() else 1

    if listening():
        print(f"[anchor] port {PORT} already served by another process", file=sys.stderr)
        return 0

    if not STUDIO_MCP.is_file():
        print(f"[anchor] not found: {STUDIO_MCP}", file=sys.stderr)
        return 2

    Path(a.log).parent.mkdir(parents=True, exist_ok=True)
    log = open(a.log, "ab", buffering=0)
    proc = subprocess.Popen([str(STUDIO_MCP)], stdin=subprocess.PIPE,
                            stdout=log, stderr=log, close_fds=True)
    print(f"[anchor] pid {proc.pid}, log {a.log}", flush=True)

    # The proxy only starts accepting Studio connections after an MCP client has completed
    # the handshake. Without this, Studio's websocket upgrade is closed immediately
    # ("Connection closed during ws upgrade") and it gives up after ~8 retries.
    init = {
        "jsonrpc": "2.0", "id": 1, "method": "initialize",
        "params": {
            "protocolVersion": "2024-11-05",
            "capabilities": {},
            "clientInfo": {"name": "studio-anchor", "version": "1.0"},
        },
    }
    assert proc.stdin is not None
    proc.stdin.write((json.dumps(init) + "\n").encode("utf-8"))
    proc.stdin.write(b'{"jsonrpc":"2.0","method":"notifications/initialized"}\n')
    # The proxy caches the tool list (StudioMCP/tools-cache.json) and only then behaves as
    # a fully registered client towards Studio.
    proc.stdin.write(b'{"jsonrpc":"2.0","id":2,"method":"tools/list"}\n')
    proc.stdin.flush()
    print("[anchor] handshake sent", flush=True)

    # Hold the pipe open. Writing nothing is the point: the proxy speaks JSON-RPC on stdout
    # and only reads stdin for client requests, which this process is not.
    try:
        while proc.poll() is None:
            time.sleep(5)
    except KeyboardInterrupt:
        proc.terminate()
    print("[anchor] proxy exited", flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
