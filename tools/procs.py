#!/usr/bin/env python
"""procs.py — какой процесс на каком порту и что у него в командной строке.

Нужен для диагностики: tasklist даёт только PID, а понять, КТО держит :8188
(ComfyUI) или :8080 (llama-server) и с какими аргументами — нельзя.

Пути к сторонним скриптам берутся через ctypes/psutil-подобный обход по WMI,
но т.к. wmic в песочнице заблокирован, читаем через CIM напрямую (PowerShell
запрещён изнутри Bash тоже). Поэтому самый надёжный путь — netstat (он есть)
плюс чтение того, что просили: имя процесса по PID через tasklist.

Запуск:
    .venv/Scripts/python.exe tools/procs.py            # порты + имена
    .venv/Scripts/python.exe tools/procs.py 8188 8080  # только эти порты
"""

from __future__ import annotations

import re
import subprocess
import sys


PORTS = ("8188", "8080", "8081", "8082", "8083", "8084", "8777")


def netstat_listeners() -> dict[str, list[int]]:
    """Порт -> список PID, которые на нём LISTENING."""
    try:
        out = subprocess.run(["netstat", "-ano"], capture_output=True, text=True,
                             encoding="utf-8", errors="replace").stdout or ""
    except OSError:
        return {}
    found: dict[str, list[int]] = {}
    for line in out.splitlines():
        if "LISTENING" not in line:
            continue
        parts = line.split()
        if len(parts) < 5:
            continue
        addr, pid = parts[1], parts[-1]
        m = re.search(r":(\d+)$", addr)
        if not m:
            continue
        port = m.group(1)
        try:
            found.setdefault(port, []).append(int(pid))
        except ValueError:
            pass
    return found


def names_for(pids: set[int]) -> dict[int, str]:
    """PID -> имя образа (tasklist)."""
    if not pids:
        return {}
    try:
        out = subprocess.run(["tasklist", "/FO", "CSV", "/NH"],
                             capture_output=True, text=True,
                             encoding="utf-8", errors="replace").stdout or ""
    except OSError:
        return {}
    names: dict[int, str] = {}
    for line in out.splitlines():
        cells = [c.strip('"') for c in line.split('","')]
        if len(cells) < 2:
            continue
        try:
            pid = int(cells[1])
        except ValueError:
            continue
        if pid in pids:
            names[pid] = cells[0]
    return names


def main() -> int:
    want = sys.argv[1:] or list(PORTS)
    listeners = netstat_listeners()
    pids = {p for port in want for p in listeners.get(port, [])}
    names = names_for(pids)

    print(f"{'порт':>6}  {'PID':>7}  процесс")
    print("-" * 40)
    for port in want:
        entries = listeners.get(port, [])
        if not entries:
            print(f"{port:>6}  {'-':>7}  (свободен)")
            continue
        for pid in entries:
            print(f"{port:>6}  {pid:>7}  {names.get(pid, '?')}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
