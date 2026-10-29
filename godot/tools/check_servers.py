"""Проверка доступности локальных серверов (для agent.cmd)."""
from __future__ import annotations

import socket
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from gdmaster import config  # noqa: E402


def up(host: str, port: int) -> bool:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.settimeout(0.4)
        return s.connect_ex((host, port)) == 0


def main() -> int:
    llm = up(config.LLM_HOST, config.LLM_PORT)
    emb = up(config.EMBED_HOST, config.EMBED_PORT)
    print(f"  LLM   :{config.LLM_PORT}  {'UP' if llm else 'DOWN'}")
    print(f"  EMBED :{config.EMBED_PORT}  {'UP' if emb else 'DOWN'}")
    if not (llm and emb):
        print()
        print("  Start servers first:  serve-all.cmd")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
