#!/usr/bin/env python
"""write_probe.py — где пилот pi на самом деле пишет файлы.

Гипотеза (из разбора бандла pi 1.0.2): `write` пишет в cwd СЕССИИ, а не в
cwd процесса. Сессия берёт cwd: cwdOverride ?? cwd из заголовка сессии ??
process.cwd(). При `--no-session` -> SessionManager.inMemory(cwd) с cwd =
process.cwd(), но при `--continue` / обычном старте в каталоге проекта
pi может подхватить сессию с ДРУГИМ cwd.

Проверка — не чтением кода, а файлом на диске.

Запуск:
    .venv/Scripts/python.exe tools/write_probe.py --cwd <путь> [--flag --no-session]

Пишет маркер с временем через `write`, потом ищет его на диске во всех
каталогах, куда pi мог его положить.
"""

from __future__ import annotations

import argparse
import json
import os
import subprocess
import sys
import time
from pathlib import Path

MARKER_NAME = "_pi_probe_marker.txt"
PI_CMD = r"C:\Users\tio\.pi\agent\bin\pi.cmd"


def find_marker(roots: list[Path], name: str) -> list[Path]:
    """Ищем файл с именем name во всех roots (неглубоко, без 45ГБ-деревьев)."""
    hits: list[Path] = []
    skip = {"node_modules", ".venv", ".git", "vendor", "models", ".cache"}
    for root in roots:
        if not root.is_dir():
            continue
        for dirpath, dirnames, filenames in os.walk(root):
            dirnames[:] = [d for d in dirnames if d not in skip]
            depth = len(Path(dirpath).relative_to(root).parts)
            if depth > 4:
                dirnames[:] = []
            if name in filenames:
                hits.append(Path(dirpath) / name)
    return hits


def main() -> int:
    ap = argparse.ArgumentParser(description="Где pi пишет файлы на самом деле")
    ap.add_argument("--cwd", required=True, help="рабочий каталог, куда запускаем pi")
    ap.add_argument("--session-flag", default="no-session", dest="flag",
                    help="флаг сессии: no-session | continue | none")
    ap.add_argument("--target", default=".",
                    help="относительный путь, который просим записать ('web3d/...' и т.п.)")
    ap.add_argument("--timeout", type=int, default=300)
    ap.add_argument("--model", default="qwen3.5-9b")
    args = ap.parse_args()

    repo = Path(__file__).resolve().parent.parent
    cwd = Path(args.cwd).resolve()
    if not cwd.is_dir():
        print(f"FATAL: cwd не каталог: {cwd}", file=sys.stderr)
        return 2

    # Маркер уникален по времени, чтобы отличить от старых прогонов.
    stamp = time.strftime("%Y%m%d-%H%M%S")
    rel_target = str(Path(args.target) / MARKER_NAME) if args.target not in (".", "") else MARKER_NAME
    abs_expected = cwd / rel_target

    prompt = (
        f"Запиши ровно один файл: `{rel_target}` с содержимым `{stamp}`.\n"
        f"Затем ничего больше не делай. Не используй bash, только инструмент write."
    )

    env = dict(os.environ)
    env["PI_CODING_AGENT_DIR"] = str(repo / "pi-home-three")
    env["PI_SKIP_VERSION_CHECK"] = "1"
    env["PI_TELEMETRY"] = "0"
    env["NO_PROXY"] = "127.0.0.1,localhost,::1"

    cmd = [PI_CMD, "-p"]
    flag = (args.flag or "").strip()
    if flag == "no-session":
        cmd += ["--no-session"]
    elif flag == "continue":
        cmd += ["--continue"]
    elif flag in ("", "none"):
        pass
    else:
        # Разрешаем передать сырые флаги, но не начинающиеся с "--" во избежание
        # съедания их argparse'ом — принимаем строку и сплитим.
        cmd += flag.split()
    cmd += ["--model", args.model, "--", prompt]

    print(f"[probe] cwd процесс : {cwd}")
    print(f"[probe] флаг        : {args.flag!r}")
    print(f"[probe] ждём файл  : {abs_expected}")
    print(f"[probe] маркер     : {stamp}")
    print("[probe] запускаю pi ...")

    t0 = time.time()
    try:
        r = subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8",
                           errors="replace", env=env, timeout=args.timeout, cwd=str(cwd),
                           stdin=subprocess.DEVNULL)
        rc, out, err = r.returncode, r.stdout, r.stderr
    except subprocess.TimeoutExpired:
        rc, out, err = None, "", f"TIMEOUT {args.timeout}s"
    dt = time.time() - t0

    print(f"\n[probe] RC={rc} за {dt:.0f}s")
    if out.strip():
        print("--- stdout ---")
        print(out[-2500:])
    if err.strip():
        print("--- stderr ---")
        print(err[-1500:])

    # Ищем маркер в реальных местах.
    found_expected = abs_expected.is_file()
    print(f"\n[probe] ожидаемый путь существует: {found_expected}")

    roots = [
        cwd,
        repo,
        repo / "projects" / "games",
        repo / "projects" / "research",
        Path.home() / ".pi" / "agent" / "sessions",
    ]
    hits = find_marker(roots, MARKER_NAME)
    # Ищем только свежие — с нашим штампом.
    fresh: list[Path] = []
    for h in hits:
        try:
            if stamp in h.read_text(encoding="utf-8", errors="replace"):
                fresh.append(h)
        except OSError:
            pass

    print(f"\n[probe] найдено файлов-маркеров: {len(hits)}, из них с нашим штампом: {len(fresh)}")
    for h in hits:
        tag = "  <== НАШ" if h in fresh else ""
        print(f"   {h}{tag}")

    print("\n[probe] ИТОГ:")
    if found_expected:
        print("   write работает и пишет в cwd процесса.")
        verdict = "ok"
    elif fresh:
        print("   write РАБОТАЕТ, но пишет В ДРУГОЕ МЕСТО (см. выше с пометкой НАШ).")
        verdict = "wrong_dir"
    else:
        print("   write НИЧЕГО не записал никуда — инструмент не работает.")
        verdict = "no_write"

    print(json.dumps({"verdict": verdict, "expected": str(abs_expected),
                      "found": [str(p) for p in hits], "fresh": [str(p) for p in fresh],
                      "rc": rc, "seconds": round(dt, 1)}, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    sys.exit(main())
