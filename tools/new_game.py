#!/usr/bin/env python
"""Скелет нового проекта 3GS: `projects/games/<имя>/`.

Зачем инструмент, а не «скопируй папку руками». Проект — это не один файл, а
набор: `web3d/vendor/` (рантайм three.js r186), `web3d/scene.js`, сервер
`tools/web/serve.py` и сборщик правок `tools/level_apply.py`. Пропустить один —
значит получить пустую панель или ошибку импорта, и искать причину в браузере.
Плюс сервер отказывается стартовать на каталоге без манифеста уровней, а
манифест и минимальный уровень тоже надо откуда-то взять.

ИСТОЧНИК СТЕКА — РЕПОЗИТОРИЙ, А НЕ ДРУГАЯ ИГРА. Раньше здесь был `find_sample`:
стек копировался из первой попавшейся папки с `web3d/scene.js`. Из-за этого
создание проекта зависело от соседей — удалили одну игру, перестали создаваться
все, — а «образец» выбирался по алфавиту имён. Теперь что и откуда берётся,
сказано одной таблицей `STACK_SRC` ниже; образец не нужен вовсе.

ОБОЛОЧКИ СТУДИИ ЗДЕСЬ НЕТ — и это важно. Страница и её модули
(`studio.html`, `app.js`, `leveledit.js`, `glbview.js`) лежат ОДНИ на все
проекты, в `<репозиторий>/studio`, и `serve.py` отдаёт их по прежним адресам
(`/web3d/studio.html`). Копировать их в проект значит вернуть «сто игр — сто
копий одного файла»: правка интерфейса требовала бы обойти все проекты.

Что копируется из репозитория (таблица `STACK_SRC`):
    web3d/vendor/     <- vendor/three/      (three.js r186 + аддоны)
    web3d/scene.js    <- stack/web3d/scene.js
    tools/level_apply.py, tools/level_edits.py, tools/level_lint.py,
    tools/web/serve.py

Что ГЕНЕРИРУЕТСЯ (это уже про новый проект, а не про стек):
    web3d/levels.json      манифест: один уровень, `editable: true`, `builder`
    web3d/level.json       минимальный уровень из ColorRect — его видно и
                           можно двигать сразу, без единой сгенерированной
                           картинки
    web3d/level_edit.json  пустой файл правок (документирует формат)
    serve.cmd              лаунчер: сервер + готовая ссылка на студию
    README.md              что где лежит и как запускать

Почему `level_0`/`level.json` по умолчанию: это родной исходник, его правит
`level_apply.py`. Имя при этом НИ НА ЧТО не влияет — чем уровень собирается,
сказано в манифесте полем `builder`. Раньше выбор инструмента был зашит по
идентификатору, и уровень с другим именем получал 500 «нет level_build.py».

Проекты живут ТОЛЬКО в `projects/games/` репозитория. Это не пожелание, а
условие работоспособности: на этот каталог смотрят `cmd/check.cmd`, гейты в
`tools/web/`, `cmd/gen.cmd --project projects/games/<имя>` и обновление стека
через `--sync`. Проект за пределами `projects/games/` отвязан от всего этого и
живёт сам по себе. Поэтому аргумент — ИМЯ, а не путь: всё, что ведёт наружу,
отвергается с подсказкой.

usage:
    python tools/new_game.py my_game
    python tools/new_game.py my_game --sync            # обновить стек
    python tools/new_game.py my_game --force           # перезаписать уровни
    python tools/new_game.py my_game --cli             # только то, что нужно CLI
"""
from __future__ import annotations

import argparse
import json
import pathlib
import shutil
import sys

REPO = pathlib.Path(__file__).resolve().parents[1]

# --- откуда берётся стек ------------------------------------------------------
# Источник — РЕПОЗИТОРИЙ, а не другая игра. Таблица ниже — единственное место,
# где сказано, что попадает в новый проект и откуда; добавил файл в стек —
# добавил строку сюда, иначе он не появится в новых проектах.
#
# Ключ — путь ОТ КАТАЛОГА ПРОЕКТА (он же путь внутри стека), значение — источник
# в репозитории. Каталоги копируются рекурсивно.
#
# Оболочки студии здесь НЕТ и быть не должно: она одна на все проекты и живёт в
# `<репозиторий>/studio`, а `serve.py` отдаёт её по адресу `/web3d/studio.html`.
# Копировать её в проект значит вернуть «сто игр — сто копий одного файла».
STACK_SRC = {
    # Рантайм three.js. Ревизия ЗАФИКСИРОВАНА и совпадает с той, на которую
    # написана документация в `knowledge/`: подняв рантайм до другой ревизии,
    # получаешь документацию, которая врёт про API. Сборка r186 разбита —
    # рядом с `three.module.js` обязан лежать `three.core.js`, он его импортирует.
    "web3d/vendor": REPO / "vendor" / "three",
    # Построитель сцены из level.json. Канонический исходник — `stack/`, потому
    # что в репозитории это единственный файл стека, которому негде больше лежать
    # (остальные и так живут в `tools/`).
    "web3d/scene.js": REPO / "stack" / "web3d" / "scene.js",
    "tools/level_apply.py": REPO / "tools" / "level_apply.py",
    # Разбор конверта правок (`nodes` + `add` + `remove`). Импортируется из
    # `level_apply.py`; без него «Пересобрать» падает на импорте, а не на
    # данных — и симптом выглядит как «сломался редактор».
    "tools/level_edits.py": REPO / "tools" / "level_edits.py",
    # Копируется в проект затем, что консольный агент работает С КАТАЛОГОМ
    # ПРОЕКТА как cwd: команда обязана быть
    # `python tools/level_lint.py web3d/level.json`, а не путь наружу на три
    # уровня вверх. Иначе он её не наберёт и запишет уровень «на глаз».
    "tools/level_lint.py": REPO / "tools" / "level_lint.py",
    # Статик-сервер студии: ручки /__save, /__build, /__lint.
    "tools/web/serve.py": REPO / "tools" / "web" / "serve.py",
}

# То, что реально нужно CLI-агенту (`agent.cmd`), а не студии. Отдельным списком,
# потому что это РАЗНЫЕ задачи: студия правит расстановку руками в браузере, CLI
# собирает уровень и генерирует арт из консоли.
#
# Чем определяется граница. CLI-агенту нужен уровень как ДАННЫЕ и проверка
# уровня: `web3d/scene.js` + `web3d/vendor/` + сам `level.json`, манифест
# `levels.json` (иначе `scene.js` и `tscheck` не найдут проект) и
# `tools/level_lint.py` (гейт после записи). Ни сервер, ни наложение правок ему
# не нужны: правки (`level_edit.json` -> `level_apply.py`) — это ровно то, что
# делает СТУДИЯ кнопкой «Пересобрать», и CLI-агент пишет уровень напрямую.
CLI_STACK_FILES = [
    "web3d/vendor",
    "web3d/scene.js",
    "tools/level_lint.py",
]

# Файлы, которые принадлежат ИГРЕ, а не стеку. `--sync` их не трогает никогда.
OWN_FILES = [
    "web3d/levels.json",
    "web3d/level.json",
    "web3d/level_edit.json",
    "serve.cmd",
    "README.md",
]

# Собственные файлы, которые пишутся и в CLI-режиме: без них игра не открывается
# как игра (`levels.json`) и уровня нет вовсе (`level.json`).
CLI_OWN_FILES = [
    "web3d/levels.json",
    "web3d/level.json",
]

# Студийная обвязка, которую CLI-режим НЕ создаёт. Список нужен для честного
# итога и для гейта `must` (см. main): иначе проверка требовала бы `serve.py`
# у игры, где его по замыслу нет, и `new_game.py --cli` падал бы с rc=1.
STUDIO_ONLY_FILES = [
    "tools/web/serve.py",
    "tools/level_apply.py",
    "tools/level_edits.py",
    "web3d/level_edit.json",
    "serve.cmd",
    "README.md",
]


# Каталог проектов. ЕДИНСТВЕННОЕ определение в Python; лаунчеры читают то же
# самое из `cmd/_env.cmd` (GS_GAMES). Меняешь раскладку — правишь оба места.
GAMES_DIR = REPO / "projects" / "games"


class TargetError(Exception):
    """Аргумент не сводится к каталогу проекта внутри `projects/games/`."""


def resolve_under_games(arg: str, hint: str, example: str) -> pathlib.Path:
    """Аргумент -> абсолютный путь ВНУТРИ `projects/games/`, иначе TargetError.

    Голое имя (`my_game`) означает `projects/games/my_game`; всё, что похоже на
    путь (`projects/games/my_game`), разрешается как есть — и тоже должно
    оказаться внутри `projects/games/`. Путь наружу не «поддерживается с
    оговоркой», а отвергается: проект вне `projects/games/` не попадает ни в
    `cmd/check.cmd`, ни в гейты, ни в `cmd/gen.cmd`, и обнаружится это позже и
    дороже.

    `hint` — что именно не так («куда создать»), `example` — готовая команда
    для копирования.
    """
    p = pathlib.Path(arg)
    looks_like_path = (p.is_absolute() or "/" in arg or "\\" in arg
                       or arg.startswith("."))
    dst = (p if looks_like_path else GAMES_DIR / arg).resolve()
    # Голое `games` даёт `projects/games/games` — формально внутри, по смыслу —
    # мусорный каталог, который потом путается под ногами. Ловим и его.
    if dst == GAMES_DIR or (dst.parent == GAMES_DIR
                            and dst.name.lower() == GAMES_DIR.name.lower()):
        raise TargetError(f"{hint}: «{arg}» — это сам каталог проектов, а не игра.\n"
                          f"Нужно имя: {example}")
    if not dst.is_relative_to(GAMES_DIR):
        raise TargetError(
            f"{hint}: {dst} — вне {GAMES_DIR}.\n"
            f"Проекты живут только в projects/games/ репозитория: только там\n"
            f"их видят cmd/check.cmd, гейты, cmd/gen.cmd и --sync.\n"
            f"  {example}")
    return dst


def resolve_target(arg: str) -> pathlib.Path:
    return resolve_under_games(arg, "куда создать",
                               "cmd/newgame.cmd my_game   ->  projects/games/my_game")


def copy_stack(dst: pathlib.Path, cli: bool = False) -> list[str]:
    """Скопировать стек из РЕПОЗИТОРИЯ в новый проект.

    `cli=True` — только то, что нужно консольному агенту (`CLI_STACK_FILES`):
    уровень как данные и гейт проверки. Студийная обвязка (`serve.py`,
    `level_apply.py`, `level_edits.py`) не копируется вовсе.

    Образца-игры у функции больше нет: источник задан таблицей `STACK_SRC`.
    Поэтому отсутствующий файл — это сломанный РЕПОЗИТОРИЙ, а не «неполный
    образец», и сообщение говорит именно об этом: раньше оно отправляло искать
    другую игру, которой может не быть.
    """
    done: list[str] = []
    rels = CLI_STACK_FILES if cli else list(STACK_SRC)
    for rel in rels:
        s = STACK_SRC[rel]
        if not s.exists():
            sys.exit(f"в репозитории нет {s} — а он нужен для {rel}.\n"
                     f"Стек неполный: почините источник в STACK_SRC "
                     f"(tools/new_game.py).")
        d = dst / rel
        d.parent.mkdir(parents=True, exist_ok=True)
        if s.is_dir():
            if d.exists():
                shutil.rmtree(d)
            shutil.copytree(s, d)
        else:
            shutil.copy2(s, d)
        done.append(rel)
    return done


def gen_level(name: str) -> dict:
    """Минимальный уровень: его ВИДНО и его можно двигать без ассетов.

    Всё на `ColorRect` намеренно. Спрайту нужна текстура, у новой игры её нет,
    а `scene.js` молча пропускает `Sprite2D` с неизвестной текстурой — уровень
    открылся бы пустым кадром, и это читалось бы как «студия сломана».

    Имена узлов выбраны так, чтобы редактор их НЕ выбросил: у `LevelEditor`
    есть чёрный список корневых слоёв (`NO_EDIT`: `Backdrop`, `GameplayLayer*`,
    `Terrain*`, `WallLeft/Right`, `Ceiling`, `Strip`) — их позиция вычисляется,
    а не задаётся руками. Поэтому фон лежит под `Backdrop`, а всё подвижное —
    под `Platforms`/`Props`/`Player`.
    """
    def node(typ, nm, path, props=None, children=None):
        return {"type": typ, "name": nm, "path": path,
                "props": props or {}, "children": children or []}

    def rect(nm, path, pos, box, color):
        # `position` — обязательное условие того, что узел попадёт в правимые:
        # редактор берёт только узлы с позицией, потому что двигать умеет
        # именно её. `rect` — в ЛОКАЛЬНЫХ координатах, вокруг позиции.
        return node("ColorRect", nm, path,
                    {"position": pos, "rect": box, "color": color})

    sky = [0.06, 0.07, 0.10, 1.0]
    ground = [0.20, 0.26, 0.22, 1.0]
    block = [0.28, 0.34, 0.29, 1.0]
    marker = [0.95, 0.75, 0.30, 1.0]

    return {
        "project": {
            "name": name,
            "viewport": [1280, 720],
            "clear_color": sky,
            "backdrop_color": [0.14, 0.15, 0.18, 1.0],
        },
        # Пусто — и это нормально: текстуры появляются вместе с первым
        # сгенерированным артом (cmd/gen.cmd). Формат тот же, что у игр с артом:
        # "путь/от/корня/игры.png": [ширина, высота].
        "textures": {},
        "frames": {},
        "tree": node("Node2D", "Main", "Main", children=[
            node("Node2D", "Backdrop", "Backdrop", children=[
                node("ColorRect", "Sky", "Sky",
                     {"rect": [0, 0, 2560, 720], "color": sky}),
            ]),
            node("Node2D", "Platforms", "Platforms", children=[
                rect("Ground", "Ground", [1280, 660], [-1280, -40, 1280, 40], ground),
                rect("Block1", "Block1", [420, 470], [-90, -26, 90, 26], block),
                rect("Block2", "Block2", [900, 360], [-90, -26, 90, 26], block),
            ]),
            node("Node2D", "Props", "Props", children=[
                rect("Marker", "Marker", [160, 560], [-12, -44, 12, 44], marker),
            ]),
            node("Node2D", "Player", "Player", {"position": [160, 560]}, children=[
                # `Camera2D` позиции не имеет — и правильно: он не объект сцены,
                # а источник лимитов камеры. `scene.js` ищет его по имени и
                # берёт `props.limits`; студия потом перекрывает их своими
                # (ей нужен обзор всего уровня, а не кадр игрока).
                node("Camera2D", "Camera2D", "Player/Camera2D",
                     {"limits": {"limit_left": 0, "limit_top": 0,
                                 "limit_right": 2560, "limit_bottom": 720},
                      "offset": [0, -180]}),
            ]),
        ]),
    }


def gen_manifest(name: str) -> dict:
    return {
        "_comment": (
            "Манифест игры: какие уровни есть и чем кончается каждый. Геометрия "
            "живёт в самих level*.json — дублировать сюда точки старта нельзя, "
            "вторая копия разъедется при первой же правке. `editable: true` — "
            "уровень можно выравнивать руками в студии; правки ложатся в "
            "<level>_edit.json рядом с уровнем. `builder` говорит, ЧЕМ уровень "
            "пересобирается: `level_apply` — уровень и есть исходник, "
            "накладываются только правки; `level_build` — уровень собирается "
            "из таблиц арта (такой сборщик есть не у каждой игры). Поле "
            "необязательное, но с ним имя уровня перестаёт что-либо значить."),
        "start": "level_0",
        "levels": {
            "level_0": {
                "file": "level.json",
                "editable": True,
                "builder": "level_apply",
                "title": "LEVEL 0",
                "subtitle": name,
                "objective": "EDIT ME",
                # `door`/`fall_y` читает игровой слой (engine.js), а не студия.
                # Здесь они лежат как описание формата: у новой игры движка
                # ещё нет, и это честно видно.
                "door": {"x": 0.0, "y": 0.0, "half": 64, "gate": ""},
                "fall_y": 900,
                "next": "",
            },
        },
    }


SERVE_CMD = r"""@echo off
setlocal
set "GAME=%~dp0"
rem --- Projects live only in projects\games\<name>\, so the repo root is THREE
rem --- levels up from this script - no absolute path baked in, and it survives
rem --- moving the repo. (It was two levels when projects sat in games\ directly;
rem --- this is exactly the line a path move breaks.)
set "REPO=%GAME%..\..\.."
set "PY=%REPO%\.venv\Scripts\python.exe"
if not exist "%PY%" set "PY=%GAME%.venv\Scripts\python.exe"
if not exist "%PY%" (
  echo [ERROR] Python venv not found. Create it in the repo root:
  echo         cd /d "%REPO%"
  echo         python -m venv .venv
  exit /b 1
)

rem --- Repo root, handed to the server explicitly. The server needs it for the
rem --- default asset roots (assets/3d, assets/images, assets/previews) shown in
rem --- the studio panels.
set "GS_REPO=%REPO%"

set "NO_PROXY=127.0.0.1,localhost,::1,%NO_PROXY%"
set "no_proxy=%NO_PROXY%"
set "PORT=8777"
if not "%~1"=="" set "PORT=%~1"
echo.
echo   STUDIO : http://127.0.0.1:%PORT%/web3d/studio.html
echo   Stop   : Ctrl+C in this window
echo.
"%PY%" "%GAME%tools\web\serve.py" --dir "%GAME%." --port %PORT%
"""


README_TPL = """# {name}

Проект 3GS (three.js, формат уровней `level.json`). Скелет создан
`tools/new_game.py` из репозитория 3GS_Master; стек скопирован из самого
репозитория, а не из соседней игры.

## Запуск

Из **любого** каталога — путь в команде абсолютный:

```cmd
{serve}
```

Или из каталога игры (тогда `.\\serve.cmd`, в PowerShell нужен префикс `.\\`):

```cmd
cd {game}
.\\serve.cmd
```

На экране должно появиться:

```
  STUDIO : http://127.0.0.1:8777/web3d/studio.html
  Stop   : Ctrl+C in this window
serving {game} on http://127.0.0.1:8777/
  ext:3d -> ...\\assets\\3d
```

Дальше открыть ссылку **STUDIO**. Сервер остановить — `Ctrl+C` в том же окне.

Порт занят? Первый аргумент: `.\\serve.cmd 8788`.

## Что где лежит

```
web3d/
  vendor/                three.js + аддоны (GLTFLoader, OrbitControls)
  scene.js               сборка сцены из level.json
  levels.json            манифест: какие уровни есть, чем кончается каждый
  level.json             уровень 0 — он же исходник, он же данные
  level_edit.json        правки руками поверх level.json
tools/
  level_apply.py         накладывает level_edit.json на level.json
  web/serve.py           статик-сервер + ручки (/__save, /__build, /__lint)
```

Оболочки студии здесь нет: `studio.html` и его модули (`app.js`, `leveledit.js`,
`glbview.js`) лежат ОДНИ на все игры — в `studio\\` в корне репозитория. Сервер
отдаёт их по адресу `/web3d/studio.html`, поэтому правка интерфейса видна сразу
всем играм. Игра владеет только данными и игровым рантаймом.

## Чего в скелете НЕТ (и почему)

Скелет — это редактор и один пустой уровень, а не игра. Движка нет: ни
`engine.js` (ввод, физика, враги), ни `play.html`, ни HUD. Их пишет автор игры —
шаблон «как выглядит игра» здесь был бы чужим кодом, который придётся вырезать.
Смотреть и править уровень до тех пор — вкладка «Уровень» в студии, она и есть
просмотрщик.

Ассетов тоже нет: `textures` и `frames` в `level.json` пустые, поэтому уровень
собран из `ColorRect`. Первый `Sprite2D` появится, когда будет первая картинка
(`cmd/gen.cmd` из корня репозитория).

## Как править уровень

Студия пишет правки **не в `level.json`**, а в `web3d/level_edit.json` —
отдельный файл рядом. Кнопка «Сохранить правки» пишет туда, «Пересобрать»
запускает `tools/level_apply.py`, который накладывает их на `level.json`.
Разделение намеренное: `level.json` можно пересобрать/перегенерировать, и
правки, лежащие внутри него, при этом исчезли бы.

Ключ правки — поле `path` узла, и оно **плоское** (`Block1`, а не
`Platforms/Block1`). Значение — `[x, y]` в координатах уровня (**y вниз**).

Черный список: узлы `Backdrop`, `GameplayLayer*`, `Terrain*`, `WallLeft/Right`,
`Ceiling`, `Strip` студия не даёт двигать — их позиция вычисляется из камеры,
и ручная правка тут же вернулась бы. Поэтому фон лежит под `Backdrop`, а всё
подвижное — под `Platforms` / `Props` / `Player`.

## Ассеты

Ассеты репозитория (`assets/3d`, `assets/images`, `assets/previews`) подключены
к панели по умолчанию. Свои каталоги — флагом:

```cmd
python tools\\web\\serve.py --dir . --assets my=assets/my
```

Генерация — из корня репозитория 3GS_Master:

```cmd
cd F:\\Pets\\Projects\\local_tools\\3GS_Master
.\\cmd\\gen.cmd --project projects\\games\\{name} --jobs <план.json>
```

Правила ассетов — `AGENTS.md` в корне репозитория и `ASSET-POLICY.md`.
"""



def write_json(path: pathlib.Path, data: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, ensure_ascii=False, indent=1) + "\n",
                    encoding="utf-8")


def main() -> None:
    ap = argparse.ArgumentParser(
        description="скелет нового проекта 3GS (web3d + студия + сервер)")
    ap.add_argument("name", help="имя проекта; создаётся в projects/games/<имя>")
    ap.add_argument("--sync", action="store_true",
                    help="только обновить стек студии; уровни и README не трогать")
    ap.add_argument("--force", action="store_true",
                    help="перезаписать уровни и манифест, если игра уже есть")
    ap.add_argument("--cli", action="store_true",
                    help="только то, что нужно консольному агенту (agent.cmd): "
                         "уровень как данные + level_lint.py. Без сервера и "
                         "правок уровня — их создаёт студия")
    a = ap.parse_args()

    dst = resolve_target(a.name)
    name = dst.name
    exists = (dst / "web3d" / "levels.json").is_file()
    if exists and not (a.force or a.sync):
        sys.exit(f"{dst} уже похож на игру (есть web3d/levels.json).\n"
                 f"  --sync  — обновить только стек студии, уровни не трогать\n"
                 f"  --force — перезаписать и уровни тоже (правки в "
                 f"level_edit.json останутся, но привяжутся к новому уровню)")

    dst.mkdir(parents=True, exist_ok=True)
    copied = copy_stack(dst, cli=a.cli)

    made: list[str] = []
    if not a.sync:
        # CLI-режим пишет только то, без чего игра не откроется и уровня не
        # будет. Студийная обвязка (serve.cmd/README/level_edit.json)
        # НЕ генерируется: её место — студия, и создавать её «на всякий случай»
        # значит снова смешивать два слоя.
        if a.cli:
            own = {
                "web3d/levels.json": gen_manifest(name),
                "web3d/level.json": gen_level(name),
            }
            for rel, data in own.items():
                p = dst / rel
                if p.exists() and not a.force and exists:
                    continue
                write_json(p, data)
                made.append(rel)
        else:
            own = {
                "web3d/levels.json": gen_manifest(name),
                "web3d/level.json": gen_level(name),
                "web3d/level_edit.json": {"level": "level.json", "nodes": {}},
            }
            for rel, data in own.items():
                p = dst / rel
                if p.exists() and not a.force and exists:
                    continue
                write_json(p, data)
                made.append(rel)

            files = {
                "serve.cmd": SERVE_CMD,
                "README.md": README_TPL.format(
                    name=name, game=dst, serve=dst / "serve.cmd"),
            }
            for rel, text in files.items():
                p = dst / rel
                if p.exists() and not a.force and exists:
                    continue
                p.write_text(text, encoding="utf-8", newline="\r\n")
                made.append(rel)

    # Что получилось — по факту на диске, а не по списку намерений. Проверка
    # «файл на месте» здесь не паранойя: половина стека — импорты, и
    # отсутствие одного файла видно только в консоли браузера.
    #
    # Набор требуемого ЗАВИСИТ от режима: в CLI-режиме `serve.py` и правок нет
    # по замыслу, и требовать их значит падать с rc=1 на здоровом скелете.
    must = ["web3d/levels.json", "web3d/level.json", "web3d/scene.js",
            "web3d/vendor/three.module.js",
            "web3d/vendor/addons/loaders/GLTFLoader.js",
            "web3d/vendor/addons/controls/OrbitControls.js",
            "tools/level_lint.py"]
    if not a.cli:
        must += ["tools/web/serve.py", "tools/level_apply.py",
                 "tools/level_edits.py"]
    missing = [r for r in must if not (dst / r).exists()]

    mode = "cli" if a.cli else "studio"
    print(f"проект    : {dst}")
    print(f"режим     : {mode}")
    print(f"стек      : {len(copied)} записей ({', '.join(copied)})")
    if made:
        print(f"создано   : {', '.join(made)}")
    if a.cli:
        print(f"без студии: {', '.join(STUDIO_ONLY_FILES)}")
    if missing:
        print(f"НЕ ХВАТАЕТ : {', '.join(missing)}")
        sys.exit(1)

    print()
    if a.cli:
        # Лаунчера у игры нет намеренно — запускает агент из корня репозитория.
        print("Дальше — консольный агент (из корня репозитория):")
        print(f'  serve-all.cmd && cmd\\doctor.cmd && agent.cmd projects\\games\\{name}')
        print()
        print(f"Проверка уровня (cwd = каталог игры):")
        print(f"  python tools/level_lint.py web3d/level.json")
    else:
        print("Запуск (из любого каталога, путь абсолютный):")
        print(f'  "{dst}\\serve.cmd"')
        print()
        print("Студия:")
        print(f"  http://127.0.0.1:8777/web3d/studio.html")
        print()
        print("Правки расстановки -> web3d/level_edit.json; накладывает "
              "tools/level_apply.py")
        print("(кнопка «Пересобрать» в студии, или вручную:")
        print(f'  python "{dst}\\tools\\level_apply.py")')


if __name__ == "__main__":
    # Ошибка «путь наружу» — не трейсбек, а сообщение: её читает человек,
    # который просто ошибся каталогом.
    try:
        main()
    except TargetError as e:
        sys.exit(str(e))
