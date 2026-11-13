# projects/ - где живут проекты

Одна раскладка, один движок на папку:

```
projects/
  three/<name>/     engine=threejs   (папка называется `three`, движок - `threejs`)
  godot/<name>/     engine=godot
  unity/<name>/     engine=unity
  roblox/<name>/    engine=roblox
```

`<name>/engine.json` **не обязателен для Python-стеков**: `project_layout.nearest_engine()`
поднимается вверх от каталога проекта и наследует `projects/<engine>/engine.json`
(его читают MCP-серверы, `tools/pi_launch.py`, `tools/project_context.py`,
`tools/find_project.py --engine`). Именно поэтому эти четыре файла лежат в git,
а сами проекты - нет.

**Но лаунчеры читают маркер САМОГО проекта**: `agent.cmd`, `pi-here.cmd` и
`pi-extensions/engine-gate.ts` открывают `<проект>/engine.json` напрямую и при
его отсутствии берут дефолт `threejs`. Поэтому для Godot/Unity/Roblox свой
`engine.json` в папке проекта всё-таки нужен — иначе сессия получит Three.js
профиль, даже если лежит в `projects/godot/`. Папка без обоих маркеров тоже
попадает в `threejs`, и это молчаливое решение по умолчанию.

Раскладку читает **один** модуль - [`project_layout.py`](../project_layout.py);
`projects/README.md` - документация, а не второй источник правды.

## Создать проект

```cmd
dev.cmd my_game          :: создаёт ПУСТУЮ папку projects/three/my_game + агент
studio.cmd               :: ПУСТАЯ студия, проект выбирается в UI (ничего не создаёт)
gs init projects\three\my_game --engine threejs   :: разложить three.js-стек
```

`dev.cmd` создаёт папку и пишет `data/active_project.txt`, но **не раскладывает
стек** — файлы создаёт агент или явный `cmd\init.cmd <полный путь>`. Голое имя
в `cmd\init.cmd` разрешается относительно текущего каталога: из корня репозитория
`cmd\init.cmd my_game` создаст `<repo>\my_game` вне `projects/` (инструмент
предупредит, что студия и гейты его не увидят). Надёжнее полный путь или кнопка
«+ Создать и открыть» в студии: она сама кладёт проект в `projects/three/`.

Проект другого движка: положить папку в `projects/godot/` (или `unity/`, `roblox/`) -
маркер родителя сработает сам. Свой `engine.json` внутри проекта нужен, только если
проект лежит не в своей папке; значение обязано быть одним из `threejs`, `godot`,
`unity`, `roblox` - иначе `tools/project_context.py` вернёт ошибку, а не догадку.

## Что здесь НЕ лежит

Содержимое проектов не версионируется: `projects/*` закрыт в `.gitignore`, открыты
только четыре `engine.json` и этот файл. Проверить, что видит git:

```cmd
git ls-files projects
```

Должно быть ровно шесть строк: `.gitignore`, `README.md` и четыре `engine.json`.
Если появилась седьмая - в `.gitignore` сломали `!projects/<engine>/engine.json`
(типичная причина: правило `projects/` вместо `projects/*`, при котором git
вообще не заходит внутрь каталога). Ни одной игры в репозитории нет и быть не
должно: это локальные данные каждого пользователя.
