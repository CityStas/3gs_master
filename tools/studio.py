#!/usr/bin/env python
"""Студия одним файлом: `studio.cmd` - и всё поднято в ОДНОМ окне.

Зачем: раньше запуск требовал двух-трёх окон и знания путей -
`serve-all.cmd` (модели, два окна) + `serve.py` (игра, третье окно) + браузер.
Здесь это один двойной щелчок:

    studio.cmd                # единственный проект, все модели
    studio.cmd test_game_1    # конкретный проект; папка должна существовать
    studio.cmd my_game 8788   # другой порт
    studio.cmd --no-models    # сразу, без моделей (студии они не нужны)

Проект задаётся ИМЕНЕМ в `projects/games/`. Скелет НЕ создаётся: студия ничего
не раскладывает по проекту. Нет папки - скажет об этом и предложит `newgame.cmd`.
Пустой проект открывается пустой сценой - это нормальный случай, а не ошибка.

Агента в студии нет: модель работает только через консольный `pi`
(`agent.cmd`), а студия - инструмент просмотра и ручной правки. Модели здесь
поднимаются затем, что их использует консольный агент (RAG и чат), и удобно
держать всё в одном окне.

Что поднимается и куда смотрит:

    llama-server :8080  9B, для консольного pi  -> logs/studio-llm.log
    llama-server :8081  bge-m3, для RAG         -> logs/studio-embed.log
    serve.py     :8777  студия и игра           -> вывод в это окно
                        (берётся из tools/web/, не из копии в проекте)

Модели стартуют БЕЗ своих окон (CREATE_NO_WINDOW) и в отдельной группе
процессов: Ctrl+C в этом окне их не задевает, а гасит их этот скрипт - в
`finally`, вместе с сервером игры. Поэтому закрывать нечего: одно окно, один
Ctrl+C.

Уже запущенные модели не поднимаются второй раз (проверка порта): повторный
старт занял бы порт и умер, а старое окно продолжало бы отвечать - это
выглядит как успех, но новые ручки не появились бы.
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

import new_game  # noqa: E402  (GAMES_DIR, TargetError, resolve_under_games)

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


def ensure_game(arg: str | None) -> pathlib.Path:
    """Проект по имени. Папка должна существовать - скелет НЕ создаётся.

    Раньше здесь звался `new_game.py`, если в папке не было
    `web3d/levels.json`: одно имя тянуло за собой раскладку двадцати файлов.
    Теперь проект - это просто каталог, и что в нём лежит, студия не решает.
    Пустая папка - нормальный случай (пустая сцена); стек раскладывает
    `newgame.cmd`, и только по явной просьбе.
    """
    if arg:
        dst = new_game.resolve_under_games(arg, "какой проект",
                                           "studio.cmd my_game")
        if not dst.is_dir():
            raise new_game.TargetError(
                f"проекта нет: {dst}\n"
                f"Создать пустую папку: mkdir \"{dst}\"\n"
                f"Разложить стандартный стек: newgame.cmd {dst.name}")
        return dst

    if not new_game.GAMES_DIR.is_dir():
        raise new_game.TargetError(
            f"нет каталога проектов: {new_game.GAMES_DIR}\n"
            f"Создать: newgame.cmd my_game")
    found = sorted(p for p in new_game.GAMES_DIR.iterdir()
                   if p.is_dir() and not p.name.startswith((".", "_")))
    if not found:
        raise new_game.TargetError(
            f"в {new_game.GAMES_DIR} нет ни одного проекта\n"
            f"(ни одной подпапки).\n"
            f"Создать: newgame.cmd my_game")
    if len(found) > 1:
        print(f"проектов несколько, беру первый по алфавиту: {found[0].name}")
        print(f"  другие: {', '.join(p.name for p in found[1:])}")
        print(f"  выбрать другую: studio.cmd <имя>")
    return found[0]


def main() -> int:
    ap = argparse.ArgumentParser(
        description="студия одним файлом: модели + сервер игры в одном окне")
    ap.add_argument("game", nargs="?", default=None,
                    help="имя проекта в projects/games/ (по умолчанию - единственный)")
    ap.add_argument("port", nargs="?", type=int, default=8777,
                    help="порт студии (по умолчанию 8777)")
    ap.add_argument("--no-models", action="store_true",
                    help="не поднимать модели: только студия (мгновенно)")
    ap.add_argument("--no-open", action="store_true",
                    help="не открывать браузер")
    a = ap.parse_args()

    if not VENV_PY.is_file():
        print(f"[ОШИБКА] нет venv: {VENV_PY}\n"
              f"Создать из корня репозитория: python -m venv .venv")
        return 1

    try:
        game = ensure_game(a.game)
    except new_game.TargetError as e:
        print(e)
        return 1

    url = f"http://127.0.0.1:{a.port}/web3d/studio.html"
    print("проект  : %s" % game)
    print("студия  : %s" % url)

    kids: list = []
    handles: list = []
    try:
        if a.no_models:
            print("модели  : пропущены (--no-models) - студии они и не нужны")
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
        print("  СТОП   : Ctrl+C в этом окне")
        print()

        srv = subprocess.Popen(
            [str(VENV_PY), str(serve), "--dir", str(game),
             "--port", str(a.port)],
            cwd=str(game), env=env)
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
