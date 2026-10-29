#!/usr/bin/env python
"""run_pi.py — запуск pi так, как это делает agent.cmd, минуя doctor.py.

agent.cmd делает три вещи, которые важны для пилота и которые теряются при
прямом вызове pi.cmd:

  1. проверяет, что data/active_project.txt указывает на ЖИВОЙ проект
     (мёртвый -> очищает указатель и запускает без проекта);
  2. выбирает профиль по engine.json проекта: godot -> pi-home-godot,
     unity -> pi-home-unity, иначе pi-home-three;
  3. передаёт проект в СИСТЕМНЫЙ промпт через --append-system-prompt,
     потому что pi стартует в корне репозитория и сам проект не читает.

Четвёртым шагом идёт doctor.py — проверка окружения, которая ходит по всем
серверам (включая ComfyUI :8188 и Blender) и может висеть минутами. Здесь он
пропускается: это диагностика, а не условие запуска.

Запуск:
    .venv/Scripts/python.exe tools/run_pi.py --project three_test_1 -- <промпт>
    .venv/Scripts/python.exe tools/run_pi.py --project three_test_1 --prompt-file logs/task.txt
"""

from __future__ import annotations

import argparse
import json
import os
import subprocess
import sys
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PI_CMD = r"C:\Users\tio\.pi\agent\bin\pi.cmd"

PROFILE_BY_ENGINE = {
    "godot": "pi-home-godot",
    "unity": "pi-home-unity",
}
DEFAULT_PROFILE = "pi-home-three"


def resolve_project(name: str) -> Path | None:
    """Имя -> путь проекта. Голое имя ищем в projects/games, иначе как путь от корня."""
    if not name:
        return None
    cand = Path(name)
    if cand.is_absolute():
        return cand if cand.is_dir() else None
    for base in (ROOT / "projects" / "games", ROOT):
        p = (base / name).resolve()
        if p.is_dir():
            return p
    return None


def read_pointer() -> str:
    f = ROOT / "data" / "active_project.txt"
    try:
        return f.read_text(encoding="utf-8").strip()
    except OSError:
        return ""


def main() -> int:
    ap = argparse.ArgumentParser(description="Запуск pi в обход doctor.py")
    ap.add_argument("--project", default=None, help="имя проекта; по умолчанию — из указателя")
    ap.add_argument("--prompt-file", default=None, help="файл с промптом")
    ap.add_argument("--prompt", default=None, help="промпт строкой")
    ap.add_argument("--no-session", action="store_true", help="не писать сессию на диск")
    ap.add_argument("--timeout", type=int, default=1800)
    ap.add_argument("--out", default=None, help="куда писать поток pi (по умолчанию stdout)")
    args, extra = ap.parse_known_args()

    raw_project = args.project or read_pointer()
    if not raw_project and not args.project:
        print("[run_pi] указатель пуст и --project не задан", file=sys.stderr)
        return 2

    # Указатель — подсказка, не факт: мёртвый -> честная ошибка, не выдуманный путь.
    proj = resolve_project(raw_project)
    if proj is None:
        print(f"[run_pi] FATAL: проект не найден: {raw_project!r}", file=sys.stderr)
        print(f"[run_pi]   (указатель: {ROOT / 'data' / 'active_project.txt'})", file=sys.stderr)
        return 2

    rel = proj.relative_to(ROOT).as_posix()

    # engine.json -> профиль
    engine = "threejs"
    eng_file = proj / "engine.json"
    if eng_file.is_file():
        try:
            engine = json.loads(eng_file.read_text(encoding="utf-8")).get("engine", "threejs")
        except (OSError, ValueError):
            pass
    profile = PROFILE_BY_ENGINE.get(engine.lower(), DEFAULT_PROFILE)

    prompt = args.prompt
    if args.prompt_file:
        prompt = Path(args.prompt_file).read_text(encoding="utf-8")
    if not prompt:
        print("[run_pi] нужен --prompt или --prompt-file", file=sys.stderr)
        return 2

    env = dict(os.environ)
    env["PI_CODING_AGENT_DIR"] = str(ROOT / profile)
    env["PI_SKIP_VERSION_CHECK"] = "1"
    env["PI_TELEMETRY"] = "0"
    env["NO_PROXY"] = "127.0.0.1,localhost,::1"
    env["THREE_PROJECT"] = rel
    env["GS_ENGINE"] = engine

    sp = (f"Active project: {rel} (engine: {engine}) - work ONLY inside it; "
          f"never create another project or a sibling folder unless the user asks for one "
          f"by name. The working dir stays the repo root; reach the project with a relative "
          f"path such as {rel}/ - that is where your files go. "
          f"data/active_project.txt and THREE_PROJECT hold the same value.")

    # Промпт уходит в pi ЧЕРЕЗ STDIN, а не аргументом.
    #
    # argv идёт через cmd.exe, а его кодовая страница (cp866/cp1251) калечит кириллицу:
    # «уровень» доезжало как «уровенÑ», и модель видела битую инструкцию. stdin —
    # байтовый канал, UTF-8 проходит целиком.
    #
    # Второе следствие: в режиме -p pi ЖДЁТ stdin. Раньше я ставил DEVNULL, чтобы
    # процесс не висел, но тогда он не получал и промпта — отсюда прогоны, которые
    # «работали» 30 секунд и ничего не делали. Корректно: подать промпт в stdin и
    # закрыть его (communicate сам закроет после записи).
    cmd = [PI_CMD, "--append-system-prompt", sp]
    if args.no_session:
        cmd.append("--no-session")
    cmd += ["--model", "qwen3.5-9b"]

    print(f"[run_pi] проект : {rel}")
    print(f"[run_pi] engine : {engine}  -> профиль {profile}")
    print(f"[run_pi] промпт : {len(prompt)} символов (через stdin)")
    print(f"[run_pi] лог    : {args.out or '(stdout)'}")
    sys.stdout.flush()

    t0 = time.time()
    quoted = subprocess.list2cmdline(cmd)
    run_kw = dict(shell=True, env=env, cwd=str(ROOT), timeout=args.timeout)
    if args.out:
        out_path = Path(args.out)
        out_path.parent.mkdir(parents=True, exist_ok=True)
        with open(out_path, "w", encoding="utf-8", errors="replace") as fh:
            r = subprocess.run(quoted, stdout=fh, stderr=subprocess.STDOUT,
                               input=prompt.encode("utf-8"), **run_kw)
        rc = r.returncode
    else:
        r = subprocess.run(quoted, input=prompt.encode("utf-8"), **run_kw)
        rc = r.returncode

    dt = time.time() - t0
    print(f"\n[run_pi] RC={rc} за {dt:.0f}s")
    return rc


if __name__ == "__main__":
    sys.exit(main())
