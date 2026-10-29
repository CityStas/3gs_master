"""Запуск игры С ОКНОМ (не headless) — чтобы сцену можно было показать глазами.

Зачем отдельный модуль. `runner.run_scene()` всегда идёт с `--headless`: он нужен,
чтобы прочитать ошибки парсинга/рантайма из stdout, и окна при этом не открывает
по определению. Из-за этого «агент запустил сцену» и «пользователь увидел игру» —
разные события, и на просьбу «покажи сцену» агент физически не мог ответить.
Здесь ровно эта дырка: оконный запуск + честный отчёт о том, появилось ли окно.

Процесс запускается отсоединённым (`DETACHED_PROCESS`), поэтому:
  * он не умирает вместе с MCP-сервером и pi;
  * игра живёт, пока пользователь сам не закроет окно;
  * `godot_stop_play()` закрывает её принудительно (через WinAPI, без shell).

Никакого shell и никаких внешних утилит: только `subprocess` на бинарник Godot
и `ctypes` для опроса/закрытия процесса.
"""
from __future__ import annotations

import ctypes
import json
import os
import subprocess
import sys
import time
from dataclasses import dataclass
from pathlib import Path

from .. import config
from .paths import PathDenied, project_root, res_path, resolve
from .runner import _env, _parse_output

# --- состояние последнего запуска -------------------------------------------
STATE_FILE: Path = config.DATA_DIR / "playing.json"
LOG_FILE: Path = config.LOGS_DIR / "play.log"

# Windows: CreateProcess flags
_DETACHED_PROCESS = 0x00000008
_CREATE_NEW_PROCESS_GROUP = 0x00000200
_CREATE_BREAKAWAY_FROM_JOB = 0x01000000

_PROCESS_QUERY_LIMITED_INFORMATION = 0x1000
_PROCESS_TERMINATE = 0x0001
_STILL_ACTIVE = 259


# ==========================================================================
# WinAPI: жизнь процесса, закрытие, заголовок окна
# ==========================================================================
def _kernel32():
    return ctypes.WinDLL("kernel32", use_last_error=True)


def pid_alive(pid: int) -> bool:
    """Жив ли процесс. Не требует прав и не трогает процесс."""
    if not pid or os.name != "nt":
        return False
    try:
        k32 = _kernel32()
        h = k32.OpenProcess(_PROCESS_QUERY_LIMITED_INFORMATION, False, int(pid))
        if not h:
            return False
        try:
            code = ctypes.c_ulong()
            if not k32.GetExitCodeProcess(h, ctypes.byref(code)):
                return False
            return code.value == _STILL_ACTIVE
        finally:
            k32.CloseHandle(h)
    except OSError:
        return False


def terminate(pid: int) -> bool:
    """Принудительно закрыть процесс по PID. True, если закрытие принято."""
    if not pid or os.name != "nt":
        return False
    try:
        k32 = _kernel32()
        h = k32.OpenProcess(_PROCESS_TERMINATE, False, int(pid))
        if not h:
            return False
        try:
            return bool(k32.TerminateProcess(h, 0))
        finally:
            k32.CloseHandle(h)
    except OSError:
        return False


def windows_for_pid(pid: int) -> list[dict]:
    """Видимые top-level окна процесса: [{"hwnd": int, "title": str}].

    Это и есть доказательство «окно реально открылось»: пустой список при живом
    процессе означает, что окна нет (например, Godot всё-таки ушёл в headless).
    """
    if not pid or os.name != "nt":
        return []
    try:
        from ctypes import wintypes

        user32 = ctypes.WinDLL("user32", use_last_error=True)
        found: list[dict] = []
        proc_type = ctypes.WINFUNCTYPE(
            wintypes.BOOL, wintypes.HWND, wintypes.LPARAM)

        def _cb(hwnd, _lparam):
            wpid = wintypes.DWORD()
            user32.GetWindowThreadProcessId(hwnd, ctypes.byref(wpid))
            if wpid.value == pid and user32.IsWindowVisible(hwnd):
                n = user32.GetWindowTextLengthW(hwnd)
                if n > 0:
                    buf = ctypes.create_unicode_buffer(n + 1)
                    user32.GetWindowTextW(hwnd, buf, n + 1)
                    title = buf.value.strip()
                    if title:
                        found.append({"hwnd": int(hwnd), "title": title})
            return True

        user32.EnumWindows(proc_type(_cb), 0)
        return found
    except (OSError, AttributeError):
        return []


def window_titles_for_pid(pid: int) -> list[str]:
    return [w["title"] for w in windows_for_pid(pid)]


def focus_window(hwnd: int) -> bool:
    """Поднять окно наверх и отдать ему фокус. True — только если реально вышло.

    Без этого игра открывается ПОД уже развёрнутым окном (мессенджер, агент,
    редактор), и пользователь снова говорит «я ничего не вижу» — инструмент
    формально сработал, а задачу не решил.

    `SetForegroundWindow` из фонового процесса Windows обычно игнорирует (лишь
    мигает кнопкой на панели задач): право на смену фокуса есть только у
    foreground-процесса. Поэтому, если прямой вызов не сработал, цепляемся
    к потоку текущего foreground-окна через `AttachThreadInput` — тогда система
    считает нас «своими» и переключение проходит.

    Возвращаем результат ПРОВЕРКИ (`GetForegroundWindow() == hwnd`), а не факта
    вызова API: иначе отчёт «поднял окно» был бы ложью.
    """
    if not hwnd or os.name != "nt":
        return False
    try:
        from ctypes import wintypes

        user32 = ctypes.WinDLL("user32", use_last_error=True)
        k32 = _kernel32()

        SW_RESTORE = 9
        HWND_TOP = 0
        SWP_NOSIZE, SWP_NOMOVE, SWP_SHOWWINDOW = 0x0001, 0x0002, 0x0040
        place = SWP_NOSIZE | SWP_NOMOVE | SWP_SHOWWINDOW

        user32.ShowWindow(hwnd, SW_RESTORE)
        user32.SetWindowPos(hwnd, HWND_TOP, 0, 0, 0, 0, place)
        user32.BringWindowToTop(hwnd)
        if user32.SetForegroundWindow(hwnd) and user32.GetForegroundWindow() == hwnd:
            return True

        our = k32.GetCurrentThreadId()
        fg = user32.GetForegroundWindow()
        fg_thread = user32.GetWindowThreadProcessId(fg, None) if fg else 0
        tgt_thread = user32.GetWindowThreadProcessId(hwnd, None)

        attached: list[int] = []
        for th in (fg_thread, tgt_thread):
            if th and th != our and user32.AttachThreadInput(our, th, True):
                attached.append(th)
        try:
            user32.SetWindowPos(hwnd, HWND_TOP, 0, 0, 0, 0, place)
            user32.BringWindowToTop(hwnd)
            user32.SetForegroundWindow(hwnd)
            user32.SetFocus(hwnd)
        finally:
            for th in attached:
                user32.AttachThreadInput(our, th, False)

        return user32.GetForegroundWindow() == hwnd
    except (OSError, AttributeError):
        return False


def focus_window_retry(hwnd: int, attempts: int = 4, pause: float = 0.4) -> bool:
    """Окну нужно время, чтобы стать готовым к переключению фокуса."""
    for i in range(max(1, attempts)):
        if focus_window(hwnd):
            return True
        time.sleep(pause)
    return False


# ==========================================================================
# Состояние
# ==========================================================================
@dataclass
class PlayState:
    pid: int = 0
    scene: str = ""
    project: str = ""
    started: float = 0.0
    log: str = ""

    def to_dict(self) -> dict:
        return {
            "pid": self.pid,
            "scene": self.scene or "(main scene)",
            "project": self.project,
            "started": self.started,
            "log": self.log,
        }


def read_state() -> PlayState | None:
    if not STATE_FILE.exists():
        return None
    try:
        raw = json.loads(STATE_FILE.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return None
    if not isinstance(raw, dict):
        return None
    return PlayState(
        pid=int(raw.get("pid") or 0),
        scene=str(raw.get("scene") or ""),
        project=str(raw.get("project") or ""),
        started=float(raw.get("started") or 0.0),
        log=str(raw.get("log") or ""),
    )


def _write_state(state: PlayState) -> None:
    try:
        STATE_FILE.write_text(
            json.dumps(state.to_dict(), ensure_ascii=False, indent=1), encoding="utf-8")
    except OSError:
        pass


def _clear_state() -> None:
    try:
        STATE_FILE.unlink()
    except OSError:
        pass


def _log_tail(path: Path, limit: int = 4000) -> str:
    try:
        return path.read_text(encoding="utf-8", errors="replace")[-limit:]
    except OSError:
        return ""


def stop_play() -> dict:
    """Закрыть запущенную игру. Безопасно вызывать, когда ничего не запущено."""
    state = read_state()
    if state is None or not state.pid:
        return {"ok": True, "stopped": False, "message": "игра не запущена"}
    if not pid_alive(state.pid):
        _clear_state()
        return {"ok": True, "stopped": False, "pid": state.pid,
                "message": "процесс уже завершился сам", "scene": state.scene}
    killed = terminate(state.pid)
    _clear_state()
    return {"ok": killed, "stopped": killed, "pid": state.pid, "scene": state.scene,
            "message": ("окно игры закрыто" if killed
                        else f"не удалось закрыть процесс {state.pid}")}


def status() -> dict:
    """Что сейчас запущено — без побочных эффектов."""
    state = read_state()
    if state is None or not state.pid:
        return {"ok": True, "running": False}
    alive = pid_alive(state.pid)
    titles = window_titles_for_pid(state.pid) if alive else []
    if not alive:
        _clear_state()
    return {
        "ok": True,
        "running": alive,
        "window_visible": bool(titles),
        "window_title": titles[0] if titles else None,
        **state.to_dict(),
    }


# ==========================================================================
# Запуск
# ==========================================================================
def play_scene(scene_path: str = "", wait: float = 6.0,
               project: Path | None = None) -> dict:
    """Открыть сцену в отдельном ОКОННОМ процессе Godot.

    Возвращает отчёт о факте: `window_opened` — подтверждено ли окно по WinAPI,
    `window_title` — его заголовок. Если Godot упал на старте, вернётся
    `ok: False` и хвост лога с разобранными ошибками.
    """
    if os.name != "nt":
        return {"ok": False, "error": "оконный запуск поддержан только на Windows"}

    root = Path(project or project_root()).resolve()
    if not (root / "project.godot").exists():
        raise PathDenied(f"в {root} нет project.godot — это не корень Godot-проекта")

    exe = Path(config.GODOT_EXE)
    if not exe.exists():
        return {"ok": False, "error": f"движок Godot не найден: {exe}"}

    scene_res = ""
    if scene_path:
        target = resolve(scene_path, root, must_exist=True)
        if target.suffix.lower() != ".tscn":
            raise PathDenied(f"ожидалась сцена .tscn, получено: {scene_path}")
        scene_res = res_path(scene_path, root)

    # предыдущий запуск заменяется, а не копится окнами
    previous = read_state()
    replaced = 0
    if previous and previous.pid and pid_alive(previous.pid):
        terminate(previous.pid)
        replaced = previous.pid
    _clear_state()

    cmd = [str(exe), "--path", str(root)]
    if scene_res:
        cmd.append(scene_res)

    LOG_FILE.parent.mkdir(parents=True, exist_ok=True)
    flags = _DETACHED_PROCESS | _CREATE_NEW_PROCESS_GROUP
    try:
        log = LOG_FILE.open("wb")
    except OSError as e:
        return {"ok": False, "error": f"не удалось открыть лог {LOG_FILE}: {e}"}

    try:
        proc = _spawn(cmd, root, flags, log)
    except OSError as e:
        log.close()
        return {"ok": False, "error": f"не удалось запустить Godot: {e}"}
    finally:
        try:
            log.close()
        except OSError:
            pass

    t0 = time.time()
    deadline = t0 + max(1.0, float(wait))
    windows: list[dict] = []
    focused = False
    exit_code: int | None = None
    while time.time() < deadline:
        exit_code = proc.poll()
        if exit_code is not None:
            break
        windows = windows_for_pid(proc.pid)
        if windows:
            # окно найдено -> сразу поднимаем наверх, не дожидаясь дедлайна
            focused = focus_window_retry(windows[0]["hwnd"])
            break
        time.sleep(0.25)
    if exit_code is None and not windows:
        windows = windows_for_pid(proc.pid)
        if windows:
            focused = focus_window_retry(windows[0]["hwnd"])
    titles = [w["title"] for w in windows]

    elapsed = round(time.time() - t0, 2)
    state = PlayState(pid=proc.pid, scene=scene_res, project=str(root),
                      started=t0, log=str(LOG_FILE))
    payload: dict = {
        "scene": scene_res or "(main scene)",
        "project": str(root),
        "pid": proc.pid,
        "seconds": elapsed,
        "log": str(LOG_FILE),
    }
    if replaced:
        payload["replaced_pid"] = replaced

    # --- упал на старте ---------------------------------------------------
    if exit_code is not None:
        tail = _log_tail(LOG_FILE)
        errors, warnings = _parse_output(tail)
        payload.update({
            "ok": False,
            "window_opened": False,
            "exit_code": exit_code,
            "verdict": "FAILED: игра завершилась сразу после запуска, окна нет",
            "errors": errors[:20],
            "warnings": warnings[:10],
            "stdout": tail,
        })
        _clear_state()
        return payload

    # --- живёт ------------------------------------------------------------
    payload.update({
        "ok": True,
        "window_opened": bool(titles),
        "window_title": titles[0] if titles else None,
        "all_windows": titles,
        "brought_to_front": focused,
        "running": True,
        "note": ("Окно игры открыто на экране пользователя и поднято наверх. Скажи ему, "
                 "что игра запущена и её можно закрыть. Закрыть программно — "
                 "godot_stop_play."
                 if titles and focused else
                 "Окно игры открыто, но поднять наверх не удалось — оно может быть "
                 "за другими окнами. Скажи пользователю нажать Alt+Tab."
                 if titles else
                 "Процесс жив, но окна не видно: возможно, оно ушло за другие окна. "
                 "Проверь godot_stop_play, чтобы не оставлять процесс висеть."),
        "verdict": ("OK: окно игры открыто и поднято наверх" if titles and focused
                    else "OK: окно игры открыто (не удалось поднять наверх)"
                    if titles else "окно не подтверждено (процесс жив)"),
    })
    if not titles:
        tail = _log_tail(LOG_FILE)
        errors, warnings = _parse_output(tail)
        if errors:
            payload["errors"] = errors[:20]
        payload["stdout"] = tail[-1500:]
    _write_state(state)
    return payload


def _spawn(cmd: list[str], cwd: Path, flags: int, log) -> subprocess.Popen:
    """Popen с отсоединением от родителя.

    Сначала пробуем выйти из job-объекта (`CREATE_BREAKAWAY_FROM_JOB`): если агент
    запущен из-под оболочки, помещающей детей в job с kill-on-close, без этого
    игра умрёт вместе с сервером. Job может запрещать breakaway — тогда Windows
    вернёт отказ, и мы спокойно перезапускаемся без флага.
    """
    common = dict(
        cwd=str(cwd), env=_env(), stdin=subprocess.DEVNULL,
        stdout=log, stderr=subprocess.STDOUT, close_fds=True,
    )
    try:
        return subprocess.Popen(cmd, creationflags=flags | _CREATE_BREAKAWAY_FROM_JOB, **common)
    except OSError:
        return subprocess.Popen(cmd, creationflags=flags, **common)


if __name__ == "__main__":  # ручная проверка: python -m gdmaster.godot.play [scene]
    arg = sys.argv[1] if len(sys.argv) > 1 else ""
    print(json.dumps(play_scene(arg), ensure_ascii=False, indent=1))
