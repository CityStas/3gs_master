# gdmaster - Godot-only local RAG coding agent

Полностью локальный coding agent, который умеет работать **только** с Godot 4.7.  
Ни shell, ни PowerShell, ни произвольного доступа к файловой системе, ни интернета,  
ни сторонних MCP-серверов у модели нет - по архитектуре, а не по промпту.

Реализация мастер-спеки `godot_only_local_rag_agent_master_prompt.md`.

> **Нужна пошаговая инструкция по запуску - читай [`ЗАПУСК.md`](ЗАПУСК.md).**  
> Этот файл - техническая документация проекта; `ЗАПУСК.md` - короткая инструкция  
> «что нажать», без деталей реализации; `ПРОВЕРКА_RAG.md` - запуск на **новом  
> пустом** проекте плюс проверка RAG и сборка простого 2D-уровня.

---

## Что внутри

```
gdmaster/
├─ agent.cmd            <-- ЗАПУСК АГЕНТА, интерактивно (главная точка входа)
├─ ask.cmd              <-- разовый запрос без TUI: ask.cmd "задача"
├─ serve-all.cmd        <-- поднять оба сервера (LLM + embeddings)
├─ serve-llm.cmd        Qwen3.5-9B на :8080
├─ serve-embed.cmd      bge-m3 на :8081 (CPU)
├─ index.cmd            переиндексация базы знаний
├─ doctor.cmd           диагностика окружения
├─ play.cmd             ЗАПУСК ИГРЫ С ОКНОМ (не headless): play.cmd [проект] [сцена]
│
├─ bin/llama/           llama.cpp b11435 (CUDA 12.4 + cudart)
├─ bin/godot/           Godot 4.7.2 stable (своя копия)
├─ models/              Qwen3.5-9B-Q4_K_M (6.17 GB), bge-m3-q4_k_m (438 MB)
├─ data/                индекс (SQLite + FTS5), active_project.txt, логи
├─ knowledge/           корпус: 810 XML class ref + 503 RST туториала + cookbook
├─ gdmaster/            код: RAG, Godot-слой, MCP-серверы
├─ .pi/                 конфиг pi: SYSTEM.md, mcp.json, settings.json, skills/
├─ pi-home/             ИЗОЛИРОВАННЫЙ agent-dir pi (см. ниже)
└─ tests/               sandbox-проект и e2e-тесты
```

### Изоляция pi (важно)

`pi` читает два конфига: пользовательский `~/.pi/agent/` и проектный `.pi/`.  
Пользовательский каталог на этой машине содержит пять посторонних MCP-серверов  
(`filesystem`, `playwright`, `chrome-devtools`, `figma`, `sequential-thinking`),  
провайдера `bonsai`, смотрящего на `:8081` (это порт **embedding**-сервера), и четыре  
npm-пакета. В таком виде pi либо зависает, либо отдаёт модели чужие инструменты -  
то есть Godot-only граница рушится ещё до первого запроса.

Поэтому gdmaster **не использует** `~/.pi/agent`. `agent.cmd` / `ask.cmd` подставляют:

```
PI_CODING_AGENT_DIR=F:\Pets\Projects\gdmaster\pi-home
PI_OFFLINE=1
PI_SKIP_VERSION_CHECK=1
PI_TELEMETRY=0
```

`pi-home/` содержит только:

| Файл            | Что внутри                                                                       |
| --------------- | -------------------------------------------------------------------------------- |
| `settings.json` | провайдер/модель `gdmaster`, `defaultTools: []`, `defaultProjectTrust: "always"` |
| `models.json`   | единственный провайдер - `gdmaster` → `http://127.0.0.1:8080/v1`                 |
| `auth.json`     | пустой                                                                           |

`defaultProjectTrust: "always"` здесь обязателен: этот ключ читается **только** из  
agent-dir, и без него в неинтерактивном режиме (`.pi/` не грузится, доверие спросить  
негде) агент запустился бы без своего системного промпта, без MCP и без скиллов.

MCP-серверы берутся ровно из `.pi/mcp.json` проекта - там один сервер `godot`  
(Policy Gateway). Глобальные серверы не подключаются никогда.

## Архитектура

```
                 pi (agent harness, .pi/)
                        │  defaultTools: []  - встроенных инструментов НЕТ
                        ▼
              ┌───────────────────┐
              │ Policy Gateway    │  MCP, единственный видимый сервер
              │ allowlist + audit │
              └────┬─────────┬────┘
                   │         │
        ┌──────────▼──┐   ┌──▼─────────────┐
        │ Godot MCP   │   │ RAG MCP        │
        │ 17 tools    │   │ rag_search     │
        │ scene/script│   │ rag_status     │
        │ validate/run│   └──┬─────────────┘
        └──────┬──────┘      │
               │        ┌────▼──────────────────┐
        ┌──────▼──────┐ │ dense (bge-m3, 1024d) │
        │ Godot 4.7   │ │ + lexical (FTS5/BM25) │
        │ headless    │ │ + RRF fusion          │
        └─────────────┘ └───────────────────────┘
```

**Ключевые решения, отличающиеся от спеки (сознательно):**

| Спека                                     | Реализовано                                   | Почему                                                                                                                                                                       |
| ----------------------------------------- | --------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `hybridindie/godot-mcp` (193 инструмента) | свой Godot MCP, 17 инструментов               | локальная 9B-модель деградирует на большом tool surface; вместо 193 инструментов - минимальная поверхность, достаточная для задачи                                           |
| Qdrant local                              | numpy + SQLite (Qdrant - опциональный бэкенд) | Qdrant local mode держит эксклюзивный лок на каталог, а RAG MCP-сервер живёт постоянно → конфликт с индексатором. Brute-force по 1024d на десятках тысяч чанков - единицы мс |
| Pi как есть                               | Pi + Policy Gateway + `defaultTools: []`      | спека требует трёх слоёв защиты; gateway фильтрует и `tools/list`, и `tools/call`                                                                                            |
| -                                         | `mcp<2` пин                                   | mcp 2.x переименовал FastMCP → MCPServer и сменил lowlevel API                                                                                                               |

---

## Быстрый старт

### 0. Требования

- Windows 10/11 x64
- NVIDIA GPU ~8 GB VRAM (проверено на RTX 2060 Super)
- Python 3.11+ (используется 3.13)
- Node.js 22+ и установленный `pi` (`pi --version`)

### 1. Поднять серверы

Открой **два** окна `cmd.exe`.

Окно 1 - LLM:

```
cd /d F:\Pets\Projects\gdmaster
serve-llm.cmd
```

Окно 2 - embeddings:

```
cd /d F:\Pets\Projects\gdmaster
serve-embed.cmd
```

Или одной командой (откроет оба окна):

```
cd /d F:\Pets\Projects\gdmaster
serve-all.cmd
```

**Что должно появиться.** В каждом окне - строки загрузки модели, затем:

```
llama_server: model loaded
llama_server: listening on http://127.0.0.1:8080
```

Проверка, что оба живы:

```
curl http://127.0.0.1:8080/health
curl http://127.0.0.1:8081/health
```

Ожидаемый ответ в обоих случаях: `{"status":"ok"}`.  
Первый запуск LLM занимает ~60 секунд (6 ГБ весов в VRAM).

### 2. Проверить, что всё на месте

```
cd /d F:\Pets\Projects\gdmaster
doctor.cmd
```

Ожидаемый финал вывода: `== ВСЁ ОК ==`.

### 3. Запустить агента на своём Godot-проекте

```
cd /d F:\Pets\Projects\gdmaster
agent.cmd D:\path\to\your\godot-project
```

`agent.cmd` запоминает путь в `data\active_project.txt`, проверяет серверы и запускает `pi`.

**Что должно появиться:** `Active Godot project: D:\path\to\your\godot-project`,  
затем `LLM :8080 UP` / `EMBED :8081 UP`, затем интерфейс pi. Подтверждать доверие  
проекту не нужно - `pi-home/settings.json` уже содержит `defaultProjectTrust: "always"`.

Дальше можно писать по-русски:

```
Добавь игроку sprint на Shift, сделай stamina UI и не ломай существующее движение.
```

Без указания проекта (повторный запуск на том же проекте):

```
cd /d F:\Pets\Projects\gdmaster
agent.cmd
```

### Разовая задача без TUI

```
cd /d F:\Pets\Projects\gdmaster
ask.cmd "Добавь игроку sprint на Shift и не ломай движение"
```

`ask.cmd` делает `pi -p --no-session "<задача>"` и печатает только финальный ответ.  
Проект берётся из `data\active_project.txt`.

> Почему в `ask.cmd` есть `< nul`: в режиме `-p` pi читает stdin, и при запуске из  
> скрипта/пайпа он на нём блокируется навсегда. Подача `nul` это снимает. Если  
> запускаете `pi -p` вручную из bash - используйте `< /dev/null`.

Полный структурированный лог одного прогона (все tool-вызовы, thinking, usage):

```
pi -p --no-session --mode json "..." > run.json
```

### Запустить игру с окном (не headless)

Инструмент `godot_run_scene` внутри агента всегда идёт с `--headless` и **окна не  
открывает** - так задумано: агенту нужен stdout с ошибками, а не окно. Это не баг,  
но из-за этого «агент запустил сцену» не равно «я увидел игру». Для просмотра глазами  
есть отдельный лаунчер:

```
cd /d F:\Pets\Projects\gdmaster
play.cmd
```

Он берёт проект из `data\active_project.txt` и запускает `bin\godot\...\Godot.exe --path <проект>`  
**без** `--headless`. Аргументы:

```
play.cmd                                главная сцена активного проекта
play.cmd Main.tscn                      конкретная сцена активного проекта
play.cmd D:\path\to\project             главная сцена указанного проекта
play.cmd D:\path\to\project Main.tscn   конкретная сцена указанного проекта
play.cmd editor [D:\path\to\project]    открыть редактор Godot
```

Что проверять: в заголовке окна - имя проекта, в углу - счётчик кадров  
(у `test_2d`: `DED DEMO 2D (DEBUG)`, `FPS 47 | 1790 | 8.75%`). Отличить windowed-запуск  
от headless можно и по выводу: headless не печатает строку  
`Vulkan ... Using Device #0: NVIDIA ...`, windowed печатает.

Тест самого лаунчера (Godot подменяется заглушкой, окно не открывается):

```
.venv\Scripts\python.exe tests\test_play_cmd.py
```

Ожидаемый финал - `== ВСЁ ОК ==` и 12 пройденных сценариев разбора аргументов.

### Запуск из любого каталога (полные пути)

```
F:\Pets\Projects\gdmaster\serve-llm.cmd
F:\Pets\Projects\gdmaster\serve-embed.cmd
F:\Pets\Projects\gdmaster\agent.cmd D:\path\to\godot-project
F:\Pets\Projects\gdmaster\ask.cmd "Добавь прыжок на Space"
F:\Pets\Projects\gdmaster\play.cmd
```

`agent.cmd`, `ask.cmd` и `play.cmd` сами делают `cd` в свой каталог, поэтому запускать  
их можно откуда угодно.

---

## Проверка: всё ли работает

Семь уровней, от дешёвого к дорогому. Первые три и пятый–шестой - секунды,  
четвёртый - пара минут, седьмой - минута и открывает окно.

### 1. Серверы подняты?

```
cd /d F:\Pets\Projects\gdmaster
curl http://127.0.0.1:8080/health
curl http://127.0.0.1:8081/health
```

Ожидается `{"status":"ok"}` дважды. Если не отвечает - серверы не запущены:

```
cd /d F:\Pets\Projects\gdmaster
serve-all.cmd
```

Откроются два отдельных окна. Первая загрузка LLM - ~60 с (6 ГБ весов в VRAM).  
Признак готовности в окне LLM: `main: server is listening on http://127.0.0.1:8080`.  
Эти два окна и есть серверы: закрыл окно - остановил сервер.

### 2. Окружение и индекс на месте?

```
cd /d F:\Pets\Projects\gdmaster
doctor.cmd
```

Ожидаемый финал - ровно эта строка:

```
== ВСЁ ОК ==
```

Выше должно быть: `Godot exe ... [OK]`, три `OK` по файлам (llama-server и обе GGUF),  
`LLM llama-server : UP`, `embed server : UP`, `chunks=25605 files=1321`,  
`policy gateway: OK`.

Если `chunks=0` - индекс пуст, собрать: `index.cmd` (полная сборка ~15 мин,  
embedding идёт на CPU и займёт все ядра).

### 3. Шлюз отдаёт инструменты и держит границу?

```
cd /d F:\Pets\Projects\gdmaster
.venv\Scripts\python.exe tests\test_gateway.py
```

Ожидаемый финал:

```
tools/list -> 23 инструмента
-- DENIED: bash --                error: TOOL_DENIED | Инструмент 'bash' вне разрешённой Godot-only границы.
-- DENIED: read arbitrary file -- error: абсолютные пути запрещены
-- DENIED: path escape --         error: выход за корень проекта запрещён
```

Плюс блок `-- godot_validate: линт API Godot 3 --` - проверяет, что новый слой
линта исполняется и для скрипта, и для сцены (в песочнице он чист, поэтому там
`чисто`). Сам линт подробно гоняется отдельно, секунды:

```
cd /d F:\Pets\Projects\gdmaster
.venv\Scripts\python.exe tests\test_lint.py
```

Ожидаемый финал - `== ВСЁ ОК ==` и 17 строк `[OK ]`, включая границу
«чистый Godot 4 -> 0 находок».


### 4. Агент реально работает?

Быстро, без TUI:

```
cd /d F:\Pets\Projects\gdmaster
ask.cmd "Перечисли узлы сцены Main.tscn"
```

Ожидается: сначала `Active Godot project: ...`, затем ответ со списком узлов  
(`Main`, `Player`, `Player/Body`, `Player/Collision`, `StaminaUI`, `StaminaLabel`).  
Первый ответ идёт 1–3 минуты - модель грузится в VRAM и думает.

Интерактивно, на своём проекте:

```
cd /d F:\Pets\Projects\gdmaster
agent.cmd D:\path\to\your\godot-project
```

Ожидается: `Active Godot project: ...`, `LLM :8080 UP`, `EMBED :8081 UP`,  
`Launching pi (Godot-only agent)`, дальше интерфейс pi. Внутри можно писать по-русски:

```
Добавь игроку sprint на Shift и не ломай существующее движение.
```

Выход из pi - `Ctrl+C`. Доверие проекту подтверждать не нужно.

> Если запускаешь из PowerShell, а не из `cmd.exe`, помни: `cd` без `/d` не сменит  
> диск. Пиши `cd /d F:\Pets\Projects\gdmaster` или `Set-Location F:\Pets\Projects\gdmaster`.

### 5. Лаунчер игры разбирает аргументы?

Godot не запускается - вместо него подставляется `tests\stub_godot.cmd`, который  
печатает свои аргументы. Окно не открывается, тест идёт секунды.

```
cd /d F:\Pets\Projects\gdmaster
.venv\Scripts\python.exe tests\test_play_cmd.py
```

Ожидаемый финал:

```
== ВСЁ ОК ==
```

и 12 строк `[OK ]` выше - включая «без проекта -> понятная ошибка, код 1».

### 6. Инструмент показа игры цел?

Безопасные пути, окно не открывается:

```
cd /d F:\Pets\Projects\gdmaster
.venv\Scripts\python.exe tests\test_play_module.py
```

Ожидаемый финал - `== ВСЁ ОК ==` и 12 строк `[OK ]`: отказы на несуществующей  
сцене, на `.gd` вместо `.tscn`, на выходе за корень проекта и на папке без  
`project.godot` - все **до** запуска Godot.

Полный прогон через gateway **открывает реальное окно**, держит его ~35 с и  
закрывает. Запускать вручную, когда никто не работает:

```
cd /d F:\Pets\Projects\gdmaster
.venv\Scripts\python.exe tests\e2e_play_tool.py F:\Pets\Projects\gdmaster\tests\sandbox
```

Ожидаемый финал:

```
tools/list -> 23 инструмента
  [OK ] godot_play_scene виден модели
  [OK ] godot_stop_play виден модели
...
 "window_opened": true,
 "window_title": "gdmaster-sandbox (DEBUG)",
 "verdict": "OK: окно игры открыто и поднято наверх"
...
  [OK ] pid <N> закрыт

== ВСЁ ОК ==
```

Отдельно, глазами: `play.cmd` должен открыть окно игры (см. раздел  
«Запустить игру с окном»).

### 7. Тулчейн собирает уровень из пустой папки?

Самый полный прогон: чистит `tests\_smoke`, собирает в ней простой 2D-уровень  
(проект → сцена → узлы → скрипт → InputMap → валидация → прогон → главная сцена →  
окно) **через gateway**, то есть тем же путём, что и агент. Окно открывается на  
экране и держится ~6 с. Запускать вручную.

```
cd /d F:\Pets\Projects\gdmaster
.venv\Scripts\python.exe tests\e2e_new_project.py
```

Ожидаемый финал:

```
tools/list -> 23 инструмента
  [OK ] godot_project_init виден модели

1. проект из пустой папки
  [OK ] godot_project_init       {"ok": true, "created": true}
...
9. окно на экране
  [OK ] godot_play_scene         {"ok": true, "window_opened": true,
                                  "window_title": "smoke2d (DEBUG)"}

== ВСЁ ОК ==
```

Если прогон падает на каком-то шаге - значит в тулчейне опять дыра: именно так  
нашлась нехватка `godot_project_init` (Godot не создаёт проект из пустой папки).

---

## Управление индексом

```
cd /d F:\Pets\Projects\gdmaster
index.cmd                                  :: инкрементально (только изменённое)
index.cmd --project D:\path\to\project     :: явно указать проект
index.cmd --full                           :: игнорировать sha256, переиндексировать всё
index.cmd --reset                          :: снести индекс и собрать заново
index.cmd --only official_docs             :: только документация движка
```

Индексация инкрементальная: файл с неизменившимся sha256 не трогается.  
Текущее состояние корпуса: **25 605 чанков / 1 321 файл** -  
21 920 `class_ref` (810 XML), 3 623 `tutorial` (503 RST), 62 `cookbook`, 20 прочее.  
Полная сборка на i3-12100 занимает ~15 минут (embedding идёт на CPU).  
Обычная переиндексация после правки одного скрипта - секунды.

Проверить поиск без агента:

```
cd /d F:\Pets\Projects\gdmaster
.venv\Scripts\python.exe tools\gdm.py search "CharacterBody3D move_and_slide" --top-k 3
```

---

## Инструменты, которые видит модель

Всего 23 (21 у Godot-сервера + 2 у RAG-сервера). Больше у неё ничего нет.

**Знания**  
`rag_search` · `rag_status`

**Инспекция (read-only)**  
`godot_project_info` · `godot_list_files` · `godot_read_file` ·  
`godot_scene_tree` · `godot_script_symbols` · `godot_find_symbol`

**Мутации**  
`godot_write_script` · `godot_patch_script` · `godot_scene_create` ·  
`godot_scene_add_node` · `godot_scene_remove_node` · `godot_scene_set_property` ·  
`godot_scene_attach_script` · `godot_scene_connect_signal`

**Настройки проекта**  
`godot_project_init` · `godot_input_action_add`

**Валидация / runtime**  
`godot_validate` · `godot_run_scene` · `godot_check_project`

**Показать человеку (окно на экране)**  
`godot_play_scene` · `godot_stop_play`

Сцены меняются **не текстовой правкой `.tscn`**, а самой Godot: генерируется  
SceneTree-скрипт, который инстанцирует сцену, меняет дерево и сохраняет `PackedScene`  
через `ResourceSaver`. `.tscn` остаётся валидным by construction.

`godot_validate` принимает и `.gd`, и `.tscn`:

| Аргумент | Что делает                                                                                           |
| -------- | ---------------------------------------------------------------------------------------------------- |
| `*.gd`   | парсинг GDScript без запуска игры                                                                    |
| `*.tscn` | движок реально грузит и инстанцирует сцену; возвращает `node_count`, `root_type` или ошибку загрузки |
| пусто    | headless-прогон проекта на 30 кадров                                                                 |

Проверка `.tscn` существует не для красоты: сцену всё-таки можно записать текстом  
(например, ради `[sub_resource]`, которые scene-инструменты не умеют), а проверка  
синтаксиса GDScript такую сцену не ловит. Типичный результат ручной записи - дубли  
узлов, `[sub_resource]` не на своём месте, выдуманные `uid://` - и молча  
незагружаемая сцена уже в рантайме. `godot_validate("ui/hud.tscn")` ловит это за 0.4 с  
с сообщением вида `Parse Error: Unknown tag 'sub_resource' in file`.

### Линт API Godot 3 (то, чего не видит парсер)

`godot --check-only` проверяет **синтаксис**, а не существование методов. Строка

```gdscript
var bullet = preload("res://bullet.tscn").instance()
```

синтаксически безупречна, парсер молчит, `ok: true` - а в Godot 4 у `PackedScene`
нет метода `instance()`, и это ошибка **рантайма**. Локальная 9B-модель пишет
Godot 3 API по памяти постоянно: его в обучающих данных на порядок больше.

Поэтому `godot_validate` дописывает в ответ два поля:

| Поле        | Что там                                                                |
| ----------- | ---------------------------------------------------------------------- |
| `lint`      | список `{line, code, message, fix, script}` - что не так и чем заменить |
| `lint_hint` | одна строка «исправь и провалидируй заново»                             |

Строки находок дублируются в уже существующий `warnings` - модель читает его даже
когда игнорирует новые поля. Для `.tscn` линтуются **все скрипты, привязанные к
сцене** (из `ext_resource type="Script"`): модель почти всегда валидирует сцену, а
не каждый скрипт по отдельности.

Ловится: `.instance()`, `yield(`, `KinematicBody*`, `export var` / `export(...)`,
`onready var`, `Pool*Array`, `File.new()` / `Directory.new()`, `rand_range()`,
`OS.window_size`, `change_scene()`, `.empty()`, `Tween.new()`,
`connect(sig, self, method)` и `move_and_slide()` вне `CharacterBody*`.

Комментарии и строковые литералы вырезаются перед проверкой - упоминание старого
API в `#`-комментарии не считается находкой. Обратная совместимость: `ok`,
`errors`, `error_count` не меняются, поля только добавляются.
Тест: `tests/test_lint.py` (17 кейсов, включая границу «чистый Godot 4 - 0 находок»).

### Approval policy

`godot_scene_remove_node(scene_path, node_path, confirm=False)` - удаление поддерева  
больше `GDM_APPROVAL_SUBTREE_NODES` узлов (по умолчанию 5) возвращает  
`APPROVAL_REQUIRED` с указанием размера поддерева. Агент должен осознанно повторить  
вызов с `confirm=true`. Порог проверен на поддереве из 9 узлов.

Все мутации сцен (`create`, `add_node`, `remove_node`, `set_property`, `attach_script`,  
`connect_signal`) перед записью кладут копию `.tscn` в `.gdmaster_backups/`.  
Имя включает секунду и счётчик (`...120049-1.bak`), поэтому несколько мутаций  
в одну секунду не затирают друг друга.

### InputMap

`godot_input_action_add(action, keys, deadzone)` - добавить или перезаписать действие  
ввода. Файл `project.godot` пишет сама Godot через `ProjectSettings.save()`, поэтому  
формат гарантированно корректный, а остальные настройки сохраняются.

```
godot_input_action_add("ui_sprint", ["Shift"])
godot_input_action_add("shoot", ["mouse_left"])
godot_input_action_add("run", ["Shift", "W"])
```

Инструмент появился не «на всякий случай». Без него модель, которой нужен новый  
ввод, идёт править секцию `[input]` в `project.godot` текстом и изобретает  
несуществующий формат:

```ini
[input_map]
[action(name="ui_sprint")]
events=[{"event_key": {"keycode": 16}}]
```

Godot такие секции молча игнорирует - ошибки нет, а действие в InputMap не  
появляется, и `Input.is_action_pressed("ui_sprint")` падает в рантайме.  
Правильный формат (`ui_sprint={"deadzone": 0.5, "events": [Object(InputEventKey,...)]}`)  
угадать нельзя, его должен писать движок.

### Проект с нуля: `godot_project_init`

Godot **не умеет создавать проект из пустой папки** - проверено: ни  
`--editor --quit`, ни `--import` на пустом каталоге не делают ничего (`--import`  
лишь отвечает `Can't run project: no main scene defined in the project`). Без  
этого инструмента первый же шаг задачи «сделай уровень в пустой папке» невыполним.

```
godot_project_init(project_name="", renderer="forward_plus", main_scene="")
```

Что делает:

1. если `project.godot` нет - пишет минимальный валидный файл  
   (`config_version=5` + `[application]` с именем и рендерером);
2. прогоняет `--headless --editor --quit`, после чего Godot сам разворачивает  
   проект: появляется `.godot/`, скан файловой системы, глобальные имена классов;
3. если задан `main_scene` - назначает `application/run/main_scene` (тоже через  
   `ProjectSettings.save()`, а не текстом).

**Идемпотентен:** существующий `project.godot` не пересоздаётся, но `main_scene`  
применяется. Поэтому его же вызывают повторно, чтобы поменять главную сцену.

Рендерер: `forward_plus` (по умолчанию), `mobile`, `gl_compatibility`.  
Для простого 2D хватает любого, самый нетребовательный - `gl_compatibility`.

Главная сцена нужна не для галочки: без неё проект не запускается «просто по F5»  
и `godot_play_scene()` без аргумента не находит, что показывать.

Полный путь «пустая папка → 2D-уровень» проверяется приёмочным прогоном  
`tests/e2e_new_project.py` (23 инструмента, окно на экране, `== ВСЁ ОК ==`).

Посмотреть реальный tool surface:

```
cd /d F:\Pets\Projects\gdmaster
.venv\Scripts\python.exe tools\gdm.py tools
```

### Показать игру пользователю: `godot_play_scene`

`godot_run_scene` и `godot_play_scene` - **разные задачи**, и путать их нельзя:

|             | `godot_run_scene`                | `godot_play_scene`                 |
| ----------- | -------------------------------- | ---------------------------------- |
| Флаг движка | `--headless`                     | без `--headless`                   |
| Окно        | не открывается никогда           | открывается на экране пользователя |
| Зачем       | поймать ошибки рантайма в stdout | дать человеку посмотреть на игру   |
| Процесс     | ждём завершения, читаем вывод    | отсоединённый, живёт до закрытия   |

Инструмент появился не «на всякий случай», а потому что без него запрос  
«запусти и покажи сцену» невыполним в принципе: у агента был только headless-прогон,  
и на просьбу показать игру он честно отвечал «ok, errors: []» - при том, что окна  
пользователь не видел. Это ровно та же дыра, что `godot_input_action_add`: шага нет  
в тулчейне, и 9B-модель не спрашивает, а начинает перебирать.

```
godot_play_scene(scene_path="", wait=6.0)   # пусто = главная сцена проекта
godot_stop_play()                           # закрыть окно
```

Что делает запуск:

1. закрывает предыдущее окно, если оно ещё живо (окна не копятся);
2. запускает `Godot.exe --path <проект> [res://Scene.tscn]` **отсоединённым**  
   (`DETACHED_PROCESS`, плюс попытка `CREATE_BREAKAWAY_FROM_JOB` - чтобы игра  
   не умирала вместе с pi);
3. ждёт появления окна и **поднимает его наверх**;
4. возвращает `window_opened`, `window_title`, `brought_to_front`, `pid`.


Ключевое: `window_opened` - это не «мы вызвали CreateProcess», а результат  
`EnumWindows` по PID процесса. Если окна нет, вернётся `window_opened: false`,  
и агент обязан сказать это честно, а не отрапортовать успех.

`brought_to_front` - тоже проверенный факт (`GetForegroundWindow() == hwnd`).  
`SetForegroundWindow` из фонового процесса Windows игнорирует, поэтому при отказе  
используется `AttachThreadInput` к потоку текущего foreground-окна. Без этого шага  
игра открывается **под** развёрнутым окном и пользователь снова говорит «я ничего  
не вижу» - то есть инструмент сработал, а задача не решена.

Если Godot упал на старте, вернётся `ok: false` и хвост `logs/play.log` с уже  
разобранными ошибками - тот же парсер, что у `godot_run_scene`.

---

## Границы безопасности

Три независимых слоя (спека §23):

1. **Промпт** - `.pi/SYSTEM.md` (заменяет системный промпт pi).
2. **Tool allowlist** - `defaultTools: []` отключает встроенные `read/bash/edit/write/grep/find/ls`;  
   `-builtin:codemode`, `-builtin:tool-search`, `-builtin:llama.cpp` выключены.
3. **Policy Gateway** - фильтрует `tools/list` и `tools/call`; вызов вне allowlist  
   возвращает `TOOL_DENIED`; всё пишется в `logs/policy_audit.jsonl`.

Дополнительно:

- **Path sandbox** - любой путь нормализуется и обязан лежать внутри корня Godot-проекта.  
  Абсолютные пути, `..`, диски, UNC, `%APPDATA%` - отклоняются.
- **Extension sandbox** - на запись разрешены только Godot-текстовые расширения.
- **Backup** - перед каждой перезаписью файла (и перед каждой мутацией сцены) копия  
  кладётся в `.gdmaster_backups/`.
- **Approval policy** - удаление поддерева больше N узлов требует явного `confirm=true`.
- **Project content = data** - комментарии, строки и импортированные документы  
  не могут переопределять системные правила.

Проверка границ:

```
cd /d F:\Pets\Projects\gdmaster
.venv\Scripts\python.exe tests\test_gateway.py
```

Ожидаемые строки в конце:

```
-- DENIED: bash --                error: TOOL_DENIED
-- DENIED: read arbitrary file -- error: абсолютные пути запрещены
-- DENIED: path escape --         error: выход за корень проекта запрещён
```

---

## Настройка под задачу

| Что                                  | Где                                                                             |
| ------------------------------------ | ------------------------------------------------------------------------------- |
| Системный промпт агента              | `.pi/SYSTEM.md`                                                                 |
| Скиллы (workflow)                    | `.pi/skills/*/SKILL.md`                                                         |
| MCP-серверы проекта                  | `.pi/mcp.json`                                                                  |
| Инструменты/расширения pi            | `.pi/settings.json`                                                             |
| Провайдер/модель pi, доверие проекту | `pi-home/settings.json`, `pi-home/models.json`                                  |
| Allowlist инструментов               | `gdmaster/mcp/policy_gateway.py` → `ALLOWED_TOOLS`                              |
| Правила проекта                      | `AGENTS.md`, `AI_RULES.md`                                                      |
| Паттерны и грабли                    | `knowledge/cookbook/`, `knowledge/troubleshooting/`, `knowledge/anti_patterns/` |

Параметры окружения:

| Переменная                              | Смысл                                                  | По умолчанию    |
| --------------------------------------- | ------------------------------------------------------ | --------------- |
| `GDM_PROJECT`                           | корень Godot-проекта (перебивает `active_project.txt`) | -               |
| `GDM_LLM_CTX`                           | контекст LLM                                           | 65536           |
| `GDM_LLM_NGL`                           | слоёв на GPU                                           | 999             |
| `GDM_EMBED_WORKERS`                     | параллельных embedding-запросов                        | 4               |
| `GDM_DENSE_TOP_K` / `GDM_LEXICAL_TOP_K` | кандидатов на этапе retrieval                          | 20 / 20         |
| `GDM_FINAL_TOP_K`                       | passages в контексте                                   | 8               |
| `GDM_APPROVAL_SUBTREE_NODES`            | порог approval при удалении поддерева                  | 5               |
| `GDM_GODOT`                             | путь к Godot.exe                                       | автоопределение |

Если на 8 ГБ VRAM не хватает места: `set GDM_LLM_CTX=32768` перед `serve-llm.cmd`.

### Почему контекст именно 65536

Qwen3.5-9B - **гибридная** архитектура: полный attention только в 8 блоках из 33
(`full_attention_interval=4`), остальные - SSM с константным состоянием. Поэтому
KV-кеш считается по 8 слоям, а не по 33, и стоит **17 КиБ/токен** при `q8_0`
(замерено, совпало с расчётом по метаданным GGUF).

| ctx   | KV-буфер | VRAM всего | свободно под Godot |
| ----- | -------- | ---------- | ------------------ |
| 8192  | 136 МиБ  | ~5.6 ГиБ   | ~2.0 ГиБ           |
| 24576 | 408 МиБ  | ~5.9 ГиБ   | ~1.7 ГиБ           |
| 65536 | 1088 МиБ | ~6.4 ГиБ   | **~0.9 ГиБ**       |
| 98304 | 1632 МиБ | ~7.1 ГиБ   | ~0.5 ГиБ (тесно)   |

Настоящий потолок задаёт не VRAM, а **бюджет компакции**. pi считает порог как
`contextWindow - reserveTokens`, и тот же `reserveTokens` ограничивает длину
сводки: `maxTokens = 0.8 * reserveTokens`. При старых 24576/4096 агент уходил в
аварийную компакцию на первом же ходу (порог 20480, а системный промпт + 23
инструмента ≈ 6000 токенов), а сводке оставалось 3276 токенов - она обрывалась
на `generation hit the token cap`.

Рабочая связка (все три числа обязаны совпадать):

| Где                            | Что             | Значение |
| ------------------------------ | --------------- | -------- |
| `serve-llm.cmd`                | `-c`            | 65536    |
| `pi-home/models.json`          | `contextWindow` | 65536    |
| `pi-home/settings.json`        | `reserveTokens` | 16384    |
| `pi-home/settings.json`        | `keepRecentTokens` | 16384 |

Порог компакции становится 49152, сводке доступно 13107 токенов вместо 3276.
Менять `-c` без `contextWindow` бессмысленно: pi не знает про настоящий контекст
сервера и будет компактить по своей цифре.

---

## Тесты

```
cd /d F:\Pets\Projects\gdmaster
.venv\Scripts\python.exe tests\make_sandbox.py    :: собрать сцену через свои же инструменты
.venv\Scripts\python.exe tests\test_gateway.py    :: MCP-клиент: tools/list, вызовы, отказы
```

`tests/make_sandbox.py` создаёт `tests/sandbox/Main.tscn`, добавляет узлы,  
прикрепляет скрипт, читает дерево и прогоняет сцену headless. Это одновременно  
проверка Godot-слоя и пример работы инструментов.

### Приёмочный прогон агента

Задача из спеки (§ «критерий успеха»), запускается через реальный harness:

```
cd /d F:\Pets\Projects\gdmaster
ask.cmd "Добавь игроку sprint на Shift, сделай stamina UI и не ломай существующее движение"
```

Структурированный лог прогона (все tool-вызовы, thinking, usage):

```
pi -p --no-session --mode json "..." > run.json
```

Первый такой прогон вскрыл три дыры, которые видны только на живой задаче  
и не видны на юнит-проверках. Baseline: **45 tool-вызовов, 5 компакций контекста,  
9м46с, задача не доведена** (агент зациклился на InputMap и ручной записи `.tscn`).

| Что сломалось                                                                        | Причина                                                                                                                                                    | Исправление                                                      |
| ------------------------------------------------------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------- |
| `InputMap action "ui_sprint" doesn't exist`                                          | у агента не было способа добавить действие ввода, он правил `[input]` текстом и выдумывал `[input_map]` / `[action(name=...)]`, что Godot молча игнорирует | инструмент `godot_input_action_add` (пишет сама Godot)           |
| битый `ui/hud.tscn` (дубли узлов, `[sub_resource]` не на месте, выдуманные `uid://`) | `.tscn` писался текстом, а `godot_validate` проверял только GDScript                                                                                       | `godot_validate` принимает `.tscn`; правило в `SYSTEM.md`        |
| `Node not found: "/root/HUD"`                                                        | скрипт обращался по абсолютному пути, а HUD лежал в `/root/Main/UI/HUD`                                                                                    | ловится `godot_run_scene` - цикл валидации сработал как задумано |

После исправлений тот же запрос: **28 tool-вызовов, 1 компакция, 3м28с, задача  
доведена и проверена независимо**.

```
input_actions: ['ui_shift']
Main.tscn     : 6 узлов, загружается, ok
player.gd     : парсинг ok
ui_stamina.gd : парсинг ok
run_scene 120 : errors []
```

Итоговый код - движение не тронуто (`Input.get_vector("ui_left", ...)` +  
`move_and_slide()` как было), спринт через реальный InputMap-экшен, stamina через  
сигнал `stamina_changed`, UI подписывается с null-safe поиском игрока.

Вывод, который стоит держать в голове при развитии проекта: 9B-модель **не  
останавливается с вопросом**, когда нужного инструмента нет - она начинает перебирать  
варианты. Лечится не промптом, а добавлением инструмента. Приёмочный прогон -  
основной способ находить такие дыры.

---

## Диагностика

| Симптом                                                         | Причина / что делать                                                                                                                                                                                                 |                                                                       |
| --------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------- |
| `LLM :8080 DOWN`                                                | не запущен `serve-llm.cmd`                                                                                                                                                                                           |                                                                       |
| `EMBED :8081 DOWN`                                              | не запущен `serve-embed.cmd`; dense-поиск деградирует до lexical                                                                                                                                                     |                                                                       |
| `rag_search` возвращает пусто                                   | индекс пуст → `index.cmd`; или `rag_status` покажет состояние                                                                                                                                                        |                                                                       |
| Godot-инструменты отвечают «проект не задан»                    | `agent.cmd D:\path\to\project`                                                                                                                                                                                       |                                                                       |
| `Connection error.` в pi                                        | LLM-сервер не поднялся или упал по VRAM                                                                                                                                                                              |                                                                       |
| Медленные ответы                                                | идёт индексация и занимает все 4 ядра CPU                                                                                                                                                                            |                                                                       |
| Сцена «не подхватывает» новый файл                              | `godot_check_project` (переимпорт ресурсов)                                                                                                                                                                          |                                                                       |
| pi виснет без вывода                                            | запущен `pi -p` без `--no-session`/без подачи `nul` на stdin; используйте `ask.cmd`                                                                                                                                  |                                                                       |
| pi подтянул чужие инструменты                                   | не выставлен `PI_CODING_AGENT_DIR` → запускать только через `agent.cmd` / `ask.cmd`                                                                                                                                  |                                                                       |
| pi не грузит `.pi/SYSTEM.md`, MCP и скиллы                      | то же: проектные ресурсы требуют доверия; `pi-home/settings.json` ставит `defaultProjectTrust: "always"`                                                                                                             |                                                                       |
| `rag_search` не находит туториалы                               | в индексе нет `tutorial`-чанков → `index.cmd --only official_docs`                                                                                                                                                   |                                                                       |
| `curl` на `127.0.0.1:8080` отдаёт `502 upstream connect failed` | в системе настроен `HTTP_PROXY`, и `curl` ушёл через него, а не напрямую. Проверяй `doctor.cmd` (сырой сокет, прокси не влияет) или добавляй `curl --noproxy '*'`. Лаунчеры сами выставляют `NO_PROXY` для localhost |                                                                       |
| Агент «запустил сцену», но окна нет                             | `godot_run_scene` всегда с `--headless` - окно не открывается by design                                                                                                                                              | это не ошибка; окно открывает `play.cmd`                              |
| `play.cmd`: `Godot not found`                                   | нет `bin\godot\Godot_v4.7.2-stable_win64.exe`                                                                                                                                                                        | положить движок в `bin\godot\` или поправить путь в начале `play.cmd` |
| `play.cmd`: `No Godot project`                                  | не задан проект                                                                                                                                                                                                      | `agent.cmd D:\path\to\project` или `play.cmd D:\path\to\project`      |
| Окно игры есть, но его не видно                                 | ушло за другие окна / на второй монитор                                                                                                                                                                              | `Alt + Tab`                                                           |

Логи: `logs/llm-server.log`, `logs/embed-server.log`,  
`logs/policy_audit.jsonl`, `logs/godot_mcp_audit.jsonl`.

---

## Известные ограничения

- `--headless` не рисует: визуальные дефекты агент поймать не может. Он проверяет  
  парсинг и рантайм, а не картинку.
- Ввод (мышь/клавиатура) в headless не эмулируется.
- Прогон сцены ограничен числом кадров; сценарий, срабатывающий через 10 секунд,  
  за 180 кадров не проявится.
- Reranker (`bge-reranker-v2-m3`) не подключён - по спеке это Phase 4,  
  только если бенчмарк покажет выигрыш.
- RAG работает по документации 4.7; если проект на другой версии, `rag_search`  
  может дать API из 4.7 - проверять через `godot_project_info`.
- **Контекст 24k - узкое место на многосоставных задачах.** Задача вида «добавь фичу +  
  сделай UI + не сломай существующее» упирается в компакцию и начинает терять  
  историю правок. Помогает `GDM_LLM_CTX` (на 8 ГБ VRAM 32768 влезает с  
  `--cache-type-k q8_0 --cache-type-v q8_0`), либо разбиение задачи на шаги.
- **9B-модель не выходит из тупика, если нужного инструмента нет.** Она не  
  останавливается с вопросом, а начинает перебирать варианты (11 `write_script` и  
  8 `run_scene` за один прогон). Лечение - не промптом, а добавлением инструмента:  
  тулчейн должен закрывать каждый шаг задачи. Приёмочный прогон - основной способ  
  находить такие дыры.
- `.gdmaster_backups/` растёт без автоочистки. Чистить вручную.
