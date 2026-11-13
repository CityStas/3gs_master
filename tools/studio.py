#!/usr/bin/env python
"""Студия одним файлом: двойной щелчок по `studio.cmd` — и всё готово.

    studio.cmd                 # ПУСТАЯ студия, проект выбирается в UI
    studio.cmd three/my_game   # (совместимость) сразу открыть конкретный проект
    studio.cmd three/my_game 8788
    studio.cmd --models        # дополнительно поднять модели для консольного pi

Главное отличие от прежней версии: НИКАКОГО консольного меню выбора проекта.
Раньше при нескольких проектах скрипт печатал список и ждал номер, а при
запуске не из терминала молча брал «первый подходящий» — человек видел чужой
проект и не понимал почему. Теперь сервер стартует в hub-режиме вообще без
проекта (`serve.py --hub`), а страница сама спрашивает `/__projects` и
показывает список ТОЛЬКО из `projects/three/` — это редактор three.js-сцен,
проекты Roblox/Unity/Godot были бы в нём заведомо пустым выбором. Выбор
уходит на `POST /__open`, сервер переключает корень НА ЖИВОМ соединении,
студия перезагружается и полностью инициализирует проект (уровни, ассеты,
игру, правки). Новый проект создаётся прямо в UI: `POST /__new` зовёт
канонический `tools/project_init.py`, который раскладывает стек в
`projects/three/<имя>`.

Модели НЕ поднимаются по умолчанию: они нужны только консольному агенту
`pi` (RAG и чат), а не студии. Раньше каждый запуск ждал ~30 с загрузки 9B,
хотя в редакторе модели не используются. Кто работает и с агентом тоже —
`dev.cmd` / `serve-all.cmd` поднимают модели сами; либо явный флаг `--models`.

Что поднимается:

    serve.py :8777   пустая студия -> выбранный проект, всё в одном окне
                     (берётся из tools/web/, не из копии в проекте)
    [только с --models]
    llama-server :8080  9B, для консольного pi  -> logs/studio-llm.log
    llama-server :8081  bge-m3, для RAG         -> logs/studio-embed.log

Структура папок по движкам (`projects/<движок>/<имя>`, `godot/`, `threejs/`,
`unity/`, `roblox/`, их RAG и `pi-home-*`) НЕ трогается вообще: студия только
читает ОДНУ папку `projects/three/`. Новый проект появляется в списке сам,
как только в этой папке появится его каталог.
"""
from __future__ import annotations

import argparse
import os
import pathlib
import subprocess
import sys
import threading
import time
import urllib.request
import webbrowser

TOOLS = pathlib.Path(__file__).resolve().parent
REPO = TOOLS.parent
sys.path.insert(0, str(TOOLS))
# project_layout.py lives at the repository root, not in tools/. When studio.py
# is launched as a script, sys.path[0] is tools/ and the CWD is NOT added, so
# the root-level import below used to fail with ModuleNotFoundError.
sys.path.insert(0, str(REPO))

import project_init as new_game  # noqa: E402  (TargetError, the skeleton, engine rules)
from project_layout import find_project  # noqa: E402

# Вывод должен появляться сразу. Под перенаправлением (лог, `| more`) Python
# копит stdout в буфере, и баннер со ссылкой показался бы только после Ctrl+C -
# то есть никогда, пока ждёшь его на экране.
try:
    sys.stdout.reconfigure(line_buffering=True)
except (AttributeError, OSError):
    pass

LLAMA = REPO / "bin" / "llama" / "llama-server.exe"
# Реестр моделей роутера. Сама модель больше не одна: `llm_models.py` пишет сюда список
# всех найденных GGUF, и :8080 отдаёт их по имени в запросе (router mode llama.cpp).
PRESET = REPO / "models" / "llm-preset.ini"
MODEL_EMBED = REPO / "models" / "bge-m3-q4_k_m.gguf"
LOGS = REPO / "logs"
VENV_PY = REPO / ".venv" / "Scripts" / "python.exe"

LLM_URL = "http://127.0.0.1:8080/v1/models"
EMBED_URL = "http://127.0.0.1:8081/health"
DEVNULL = subprocess.DEVNULL


def probe(url: str, timeout: float = 2.0) -> bool:
    """HTTP 200 = сервер жив. Прокси обходим: 127.0.0.1 наружу не ходит."""
    opener = urllib.request.build_opener(urllib.request.ProxyHandler({}))
    try:
        with opener.open(url, timeout=timeout) as r:
            return r.status == 200
    except Exception:
        return False


def ensure_preset() -> bool:
    """Пересобрать реестр моделей. Дешево: читаются только заголовки GGUF.

    Студия поднимает :8080 сама, если он молчит, - и обязана поднять ТУ ЖЕ конфигурацию,
    что `cmd\\serve-llm.cmd`, иначе агент, запущенный следом, попадёт на сервер без
    половины моделей. Реестр один на всех: models\\llm-preset.ini.
    """
    r = subprocess.run([str(VENV_PY), str(TOOLS / "llm_models.py")],
                       cwd=str(REPO), capture_output=True, text=True,
                       errors="replace")
    if r.returncode != 0:
        print("[ОШИБКА] реестр моделей не собрался:")
        print((r.stderr or r.stdout or "").strip()[-1500:])
        return False
    return True


def llm_args() -> list[str]:
    """Роутер, а не одна модель: /v1/models отдаёт все id из реестра."""
    maxmodels = os.environ.get("GS_LLM_MAXMODELS") or "1"
    ngl = os.environ.get("GS_LLM_NGL") or "999"
    return ["--models-preset", str(PRESET), "--models-max", maxmodels,
            "--host", "127.0.0.1", "--port", "8080",
            "--jinja", "-ngl", ngl, "-fa", "on", "-np", "1",
            "--no-webui", "--cache-type-k", "q8_0", "--cache-type-v", "q8_0",
            "--reasoning", "off",
            "--temp", "0.6", "--top-p", "0.95", "--top-k", "20"]


def embed_args() -> list[str]:
    return ["-m", str(MODEL_EMBED), "--host", "127.0.0.1", "--port", "8081",
            "--embedding", "--pooling", "cls", "-c", "32768", "-ngl", "0",
            "-b", "8192", "-ub", "8192", "-np", "4", "--no-webui"]


def spawn_llama(args: list[str], log: pathlib.Path):
    """Модель без своего окна. Возвращает (процесс, файл лога)."""
    LOGS.mkdir(parents=True, exist_ok=True)
    fh = open(log, "wb")
    flags = 0
    if os.name == "nt":
        # Отдельная группа -> Ctrl+C в нашем окне её не убьёт; без окна -> не
        # плодим консоли, вывод уходит в файл.
        flags = (subprocess.CREATE_NEW_PROCESS_GROUP
                 | subprocess.CREATE_NO_WINDOW)
    p = subprocess.Popen([str(LLAMA), *args], cwd=str(REPO),
                         stdout=fh, stderr=subprocess.STDOUT,
                         stdin=DEVNULL, creationflags=flags)
    return p, fh


def tail(path: pathlib.Path, lines: int = 12) -> str:
    try:
        data = path.read_text(encoding="utf-8", errors="replace").splitlines()
    except OSError:
        return "(лог пуст)"
    return "\n".join(data[-lines:])


def wait_models(timeout: float, targets: list[tuple[str, str]],
                logs: list[tuple[str, pathlib.Path]]) -> bool:
    """Ждём готовности моделей. Возвращает False и печатает хвост логов."""
    deadline = time.monotonic() + timeout
    done: set[str] = set()
    t0 = time.monotonic()
    while True:
        for label, url in targets:
            if label not in done and probe(url):
                done.add(label)
                print("  [ готово ] %-5s %s  (%.1f с)"
                      % (label, url, time.monotonic() - t0))
        if len(done) == len(targets):
            print("модели готовы за %.1f с" % (time.monotonic() - t0))
            return True
        if time.monotonic() >= deadline:
            missing = [l for l, _ in targets if l not in done]
            print("\n[ОШИБКА] за %.0f с не поднялись: %s" % (timeout, ", ".join(missing)))
            for label, path in logs:
                if label in missing:
                    print("\n--- хвост %s ---\n%s" % (path.name, tail(path)))
            print("\nСкорее всего порт занят чужой копией "
                  "(netstat -ano | findstr :8080) или модель не влезла в VRAM.")
            return False
        time.sleep(2.0)


def open_later(url: str, port: int, timeout: float = 30.0) -> None:
    """Открыть браузер, как только сервер ответит. Не блокирует запуск."""
    def run():
        deadline = time.monotonic() + timeout
        while time.monotonic() < deadline:
            if probe(f"http://127.0.0.1:{port}/web3d/studio.html"):
                webbrowser.open(url)
                return
            time.sleep(0.5)
    threading.Thread(target=run, daemon=True).start()


def kill(p) -> None:
    if p is None or p.poll() is not None:
        return
    if os.name == "nt":
        # /T - вместе с деревом: llama-server.exe это шим, он может породить
        # дочерний процесс, и одиночный kill оставил бы порт занятым.
        subprocess.run(["taskkill", "/T", "/F", "/PID", str(p.pid)],
                       stdout=DEVNULL, stderr=DEVNULL)
    else:
        p.terminate()


def _proj_key(p: pathlib.Path) -> str:
    """Имя проекта так, как его удобно набирать: `<движок>/<имя>`.

    Голого имени мало: `dedspace_three` и одноимённый проект в другом движке —
    разные каталоги, и выбор «по имени» открыл бы не тот.
    """
    return f"{p.parent.name}/{p.name}"


def ensure_game(arg: str | None) -> pathlib.Path | None:
    """Явный проект по имени ИЛИ `None` = пустая студия (выбор в UI).

    `None` здесь не ошибка и не «возьми первый попавшийся». Это штатный
    старт: сервер поднимается в hub-режиме, а список проектов и выбор
    живут в браузере. Консольное меню убрано полностью — см. докстринг
    модуля. Скелет по-прежнему НЕ создаётся: студия ничего не раскладывает
    по проекту, она только открывает то, что уже есть.
    """
    if not arg:
        return None
    dst = find_project(arg)
    if dst is None:
        raise new_game.TargetError(
            f"проекта нет: {arg}\n"
            f"Создать пустую папку: mkdir \"{arg}\"\n"
            f"Разложить стандартный стек: cmd\\init.cmd <каталог>")
    return dst


def main() -> int:
    ap = argparse.ArgumentParser(
        description="студия одним файлом: пустой старт, проект выбирается в UI")
    ap.add_argument("game", nargs="?", default=None,
                    help="(необязательно) сразу открыть projects/<движок>/<имя>")
    ap.add_argument("port", nargs="?", type=int, default=8777,
                    help="порт студии (по умолчанию 8777)")
    ap.add_argument("--port", dest="port_opt", type=int, default=None,
                    help="порт студии флагом: studio.cmd --port 8788")
    ap.add_argument("--models", action="store_true",
                    help="дополнительно поднять модели для консольного агента pi")
    ap.add_argument("--no-models", action="store_true",
                    help="(устаревший флаг, теперь это поведение по умолчанию)")
    ap.add_argument("--no-open", action="store_true",
                    help="не открывать браузер")
    a = ap.parse_args()
    # Флаг удобнее позиционного: `studio.cmd --port 8788` не требует пустого
    # первого аргумента (иначе «8788» приняли бы за ИМЯ проекта).
    if a.port_opt is not None:
        a.port = a.port_opt

    if not VENV_PY.is_file():
        print(f"[ОШИБКА] нет venv: {VENV_PY}\n"
              f"Создать из корня репозитория: python -m venv .venv")
        return 1

    try:
        game = ensure_game(a.game)
    except new_game.TargetError as e:
        print(e)
        return 1

    hub = game is None
    url = f"http://127.0.0.1:{a.port}/web3d/studio.html"
    if hub:
        print("проект  : НЕ ВЫБРАН — список проектов откроется в студии")
    else:
        print("проект  : %s  (%s)" % (_proj_key(game), game))
    print("студия  : %s" % url)

    kids: list = []
    handles: list = []
    try:
        if not a.models:
            print("модели  : не нужны студии (флаг --models — только для pi)")
        else:
            targets: list[tuple[str, str]] = []
            logs: list[tuple[str, pathlib.Path]] = []
            if probe(LLM_URL):
                print("LLM     : уже поднят (:8080)")
            else:
                if not ensure_preset():
                    return 1
                p, fh = spawn_llama(llm_args(), LOGS / "studio-llm.log")
                kids.append(p)
                handles.append(fh)
                targets.append(("LLM", LLM_URL))
                logs.append(("LLM", LOGS / "studio-llm.log"))
            if probe(EMBED_URL):
                print("EMBED   : уже поднят (:8081)")
            else:
                p, fh = spawn_llama(embed_args(), LOGS / "studio-embed.log")
                kids.append(p)
                handles.append(fh)
                targets.append(("EMBED", EMBED_URL))
                logs.append(("EMBED", LOGS / "studio-embed.log"))
            if targets:
                print("модели  : грузятся (9B - примерно 30 с), логи в logs/")
                if not wait_models(300.0, targets, logs):
                    return 1
            else:
                print("модели  : обе уже работали")

        env = dict(os.environ)
        env["GS_REPO"] = str(REPO)
        env["NO_PROXY"] = "127.0.0.1,localhost,::1," + env.get("NO_PROXY", "")
        env["no_proxy"] = env["NO_PROXY"]

        # Сервер берём из РЕПОЗИТОРИЯ, а не из копии в проекте. Копия
        # появляется только там, где звали newgame.cmd, и требовать её -
        # значит требовать скелет, которого может и не быть. serve.py
        # одинаков везде, а корень репозитория находит по GS_REPO (выше),
        # так что каталог проекта ему задаёт только --dir.
        serve = TOOLS / "web" / "serve.py"
        if not serve.is_file():
            print(f"[ОШИБКА] нет {serve} - репозиторий неполный.")
            return 1

        print()
        print("  СТУДИЯ : %s" % url)
        if hub:
            print("  ПРОЕКТ : выберите в окне студии — всё подгрузится само")
        print("  СТОП   : Ctrl+C в этом окне")
        print()

        # hub = сервер без --dir: проект приедет с POST /__open из UI.
        # Явный аргумент сохраняет прежний путь (--dir) для скриптов и гейтов.
        cmd = [str(VENV_PY), str(serve), "--port", str(a.port)]
        cmd += ["--hub"] if hub else ["--dir", str(game)]
        srv = subprocess.Popen(cmd, cwd=str(game or REPO), env=env)
        kids.append(srv)
        if not a.no_open:
            open_later(url, a.port)
        srv.wait()
        return srv.returncode or 0
    except KeyboardInterrupt:
        print("\nостановлено")
        return 0
    finally:
        for p in kids:
            kill(p)
        for fh in handles:
            try:
                fh.close()
            except OSError:
                pass


if __name__ == "__main__":
    raise SystemExit(main())
