"""Детерминированный линт GDScript: ловит API Godot 3, которое пропускает парсер.

Зачем отдельный слой. `godot --check-only` проверяет **синтаксис**, а не наличие
методов у типа. Строка

    preload("res://bullet.tscn").instance()

синтаксически безупречна, парсер молчит, `godot_validate` возвращает ok — а в
Godot 4 у PackedScene нет метода `instance()`, и это ошибка РАНТАЙМА. Ровно так
локальная модель «успешно» написала стрельбу, которая не стреляет.

Локальная 9B-модель регулярно пишет Godot 3 API по памяти (его в обучающих данных
на порядок больше). Поэтому проверка живёт в тулчейне, а не в промпте: правило
проекта — «нет шага в тулчейне → модель не спросит, а уйдёт в перебор».

Линт намеренно консервативный: только однозначные текстовые шаблоны, без разбора
AST. Ложное срабатывание стоит одного лишнего взгляда модели, пропуск — часа
отладки, поэтому перекос в сторону «лучше сказать».
"""
from __future__ import annotations

import re

# (шаблон, что не так, чем заменить)
RULES: list[tuple[str, str, str]] = [
    (r"\.instance\s*\(\s*\)", "PackedScene.instance() — API Godot 3", "instantiate()"),
    (r"\byield\s*\(", "yield — API Godot 3", "await"),
    (r"\bKinematicBody2D\b", "KinematicBody2D — API Godot 3", "CharacterBody2D"),
    (r"\bKinematicBody\b", "KinematicBody — API Godot 3", "CharacterBody3D"),
    (r"^\s*export\s*\(", "@export(...) — API Godot 3", "@export var / @export_range"),
    (r"^\s*export\s+var\b", "export var — API Godot 3", "@export var"),
    (r"^\s*onready\s+var\b", "onready var — API Godot 3", "@onready var"),
    (r"\bPoolStringArray\b", "PoolStringArray — API Godot 3", "PackedStringArray"),
    (r"\bPoolVector2Array\b", "PoolVector2Array — API Godot 3", "PackedVector2Array"),
    (r"\bPoolVector3Array\b", "PoolVector3Array — API Godot 3", "PackedVector3Array"),
    (r"\bPoolByteArray\b", "PoolByteArray — API Godot 3", "PackedByteArray"),
    (r"\bPoolIntArray\b", "PoolIntArray — API Godot 3", "PackedInt32Array"),
    (r"\bPoolRealArray\b", "PoolRealArray — API Godot 3", "PackedFloat32Array"),
    (r"\bPoolColorArray\b", "PoolColorArray — API Godot 3", "PackedColorArray"),
    (r"\bFile\.new\s*\(", "File — API Godot 3", "FileAccess.open()"),
    (r"\bDirectory\.new\s*\(", "Directory — API Godot 3", "DirAccess.open()"),
    (r"\brand_range\s*\(", "rand_range() — API Godot 3", "randf_range() / randi_range()"),
    (r"\bOS\.window_size\b", "OS.window_size — API Godot 3", "DisplayServer.window_get_size()"),
    (r"\bOS\.set_window_size\b", "OS.set_window_size — API Godot 3", "DisplayServer.window_set_size()"),
    (r"\bchange_scene\s*\(", "change_scene() — API Godot 3", "change_scene_to_file()"),
    (r"\.empty\s*\(\s*\)", "String/Array.empty() — API Godot 3", "is_empty()"),
    (r"\bTween\s*\.new\s*\(", "Tween как узел — API Godot 3", "create_tween()"),
    (r"\bconnect\s*\(\s*\"[^\"]+\"\s*,\s*self\s*,", "connect(sig, self, method) — API Godot 3",
     "signal.connect(method)"),
]

_COMPILED = [(re.compile(p), msg, fix) for p, msg, fix in RULES]

# Классы, у которых реально есть move_and_slide() в Godot 4.
_BODY_BASES = ("CharacterBody2D", "CharacterBody3D")
_EXTENDS_RE = re.compile(r"^\s*extends\s+([A-Za-z_][\w.]*)")


def _code_only(line: str) -> str:
    """Оставить только код: убрать #-комментарий и обнулить содержимое строк.

    Без этого и комментарий «# .instance() — это Godot 3», и подсказка
    `print(".instance()")` превращаются в ложные срабатывания, а текст рядом с
    исправленным местом — самый частый повод упомянуть старое API.
    Длину строки сохраняем, чтобы позиции символов не поехали.
    """
    out: list[str] = []
    quote = ""
    i = 0
    while i < len(line):
        ch = line[i]
        if quote:
            if ch == "\\":
                out.append("  ")
                i += 2
                continue
            if ch == quote:
                quote = ""
                out.append(ch)
            else:
                out.append(" ")
        elif ch in "\"'":
            quote = ch
            out.append(ch)
        elif ch == "#":
            break
        else:
            out.append(ch)
        i += 1
    return "".join(out)


def lint_gdscript(text: str) -> list[dict]:
    """Вернуть список находок: [{"line", "code", "message", "fix"}].

    Пустой список = чисто. Функция никогда не бросает: линт не имеет права
    ломать валидацию, если сам споткнётся.
    """
    findings: list[dict] = []
    try:
        lines = text.splitlines()
    except Exception:
        return findings

    base = ""
    for ln in lines:
        m = _EXTENDS_RE.match(ln)
        if m:
            base = m.group(1)
            break

    for n, raw in enumerate(lines, 1):
        code = _code_only(raw)
        if not code.strip():
            continue
        for rx, msg, fix in _COMPILED:
            if rx.search(code):
                findings.append({
                    "line": n, "code": raw.strip()[:120],
                    "message": msg, "fix": fix,
                })
        # move_and_slide() существует только у CharacterBody*; в скрипте на
        # Node2D он молча ничего не делает (или падает при вызове).
        if "move_and_slide" in code and base and base not in _BODY_BASES:
            findings.append({
                "line": n, "code": raw.strip()[:120],
                "message": f"move_and_slide() при `extends {base}` — метод есть только у CharacterBody2D/3D",
                "fix": "extends CharacterBody2D и velocity вместо position",
            })
    return findings
