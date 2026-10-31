# Roblox-стек (`roblox/`)

Четвёртый движок в `3GS_Master`: **Roblox Studio + Luau**. Устроен так же, как
`unimaster` (Unity) и `gdmaster` (Godot) — один конфиг, гибридный индекс в SQLite, MCP-серверы,
которые читает агент, — и делит с ними те же локальные серверы моделей (`:8080` LLM,
`:8081` эмбеддинги, `:8083` реранкер). Ничего не запускается само по себе: стек добавляет
**корпус и инструменты**, а не рантайм.

## Что здесь есть

```
roblox/
  rbxmaster/
    config.py              один конфиг: пути, версия корпуса, Studio, порты, проект
    rag/                   store (SQLite+FTS5) · chunkers · embedder · reranker · retriever · indexer
    mcp/                   rag_mcp_server · project_mcp_server
    luau/                  paths (sandbox) · lint · place (.rbxlx) · studio (процесс, запуск)
  tools/                   fetch_docs · index · check · doctor · open
  knowledge/
    official_docs/         2323 страницы гайдов Creator Hub (из llms-full.txt)
    engine_api/            1210 страниц Engine API Reference (classes/datatypes/enums/…)
    cloud_docs/            114 страниц Open Cloud REST
    curated_kb/            16 файлов стартового набора (русский)
    cookbook/              рецепты, написанные под этот стек
    troubleshooting/       разбор частых ошибок
    anti_patterns/         что выглядит рабочим, но ломается
  data/sqlite/lexical.db   индекс
```

## Команды

```cmd
gs roblox-fetch                 :: корпус; --only <корпус> --limit N --force --workers 8
gs roblox-index                 :: индекс; --vectors | --only <корпус> | --force | --project <путь>
gs roblox-check <проект>        :: Luau-линт; --json | --errors-only
gs roblox-doctor                :: Studio, корпус, индекс, серверы
gs roblox-open [проект]         :: открыть Studio; --empty | --studio <путь>
gs test                         :: все тесты, включая tests/test_roblox.py
```

Из bash агента `.cmd` не запускаются — те же скрипты напрямую:

```bash
./.venv/Scripts/python.exe roblox/tools/check.py projects/games/my_game
./.venv/Scripts/python.exe roblox/tools/index.py --only engine_api
```

## MCP-инструменты

### `rbx-rag` (знания)

| Инструмент | Что делает |
|---|---|
| `rbx_rag_search(query, top_k, source, path_prefix, context)` | гибридный поиск: dense (bge-m3) + BM25, RRF, реранк |
| `rbx_rag_status()` | размер индекса, здоровье эмбеддера, размер корпуса, версия документации |

`source`: `project`, `curated_kb`, `official_docs`, `engine_api`, `cloud_docs`, `cookbook`,
`troubleshooting`, `anti_patterns`. `context`: `server`, `client`, `shared`.

### `rbx-project` (файлы на диске)

| Инструмент | Что делает |
|---|---|
| `rbx_project_info` | корень, `engine`, Rojo-файл, число `.luau`, place-файлы, состояние Studio |
| `rbx_list_files` / `rbx_read_file` | дерево и чтение с номерами строк |
| `rbx_write_file` / `rbx_edit_file` | запись с бэкапом в `.rbxmaster_backups/`; `edit` падает, если фрагмент не найден или неоднозначен |
| `rbx_search_scripts` | grep по Luau проекта |
| `rbx_lint` | правила Luau без внешнего тулчейна |
| `rbx_place_info` | `.rbxlx` без Studio: сервисы, счётчики классов, скрипты с путями |
| `rbx_studio_status` / `rbx_open_place` | установлена ли Studio, запущена ли, открыть место |

### `roblox-studio` (живой DataModel)

Это **не наш** сервер: встроенный MCP Roblox Studio (`StudioMCP.exe`, запускается через
`%LOCALAPPDATA%\Roblox\mcp.bat`). Даёт `script_read`, `multi_edit`, `script_grep`,
`search_game_tree`, `inspect_instance`, `execute_luau`, `start_stop_play`,
`get_console_output`, `screen_capture`. Включается **внутри Studio**: Assistant → … →
Manage MCP Servers → Enable Studio as MCP server.

Разделение простое: `rbx_project_*` правит **файлы**, `roblox-studio` правит **открытое
место**. Смешивать нельзя — Studio держит авторитетную копию открытого места и перезапишет
файл при сохранении.

## Корпус: откуда и почему так

| Источник | Как забирается | Почему |
|---|---|---|
| Гайды | `docs/llms-full.txt` — один ответ 23.8 МБ, внутри `<document url=…>` на страницу | 2323 страницы одним запросом: нет риска рейт-лимита |
| Engine API | 1210 отдельных `.md` по индексу `reference/engine/llms.txt` | `llms-full` для Engine API отдаёт 404 — только постранично |
| Open Cloud | 114 `.md` по индексу `cloud/llms.txt` | REST-справочник, отдельный корпус |
| Стартовый набор | копия `Roblox_RAG_Starter_Kit/*.md` | единственный русскоязычный корпус |

Версия корпуса — дата публикации индекса (`<!-- Last updated: … -->`), а не семантическая
версия: у Roblox её нет. Она проставляется в шапку каждого чанка, поэтому устаревший хит
видно в результате.

## Чанкинг: что именно режется

| Файл | Гранулярность | Ключевое |
|---|---|---|
| `.luau` / `.lua` | одна функция / один `type` | сканер блоков понимает `--`, `--[[ ]]`, `"…"`, `[[…]]`, `[=[…]=]`; `do` у `for`/`while` не считается вторым блоком |
| Engine API `.md` | один член класса | `### Method: RemoteEvent:FireClient` → `symbol=RemoteEvent:FireClient`, плюс `security`, `thread_safety`, `capabilities` из JSON-блока или тега |
| гайды `.md` | один заголовок `#`/`##`/`###` | фронт-маттер (title/url/description) уходит в meta, а не в текст |
| `.rbxlx` / `.rbxmx` | один `<Item>` | класс + `Name` + свойства; вложенность сохраняется в `parent` |
| `*.project.json` | один ключ верхнего уровня | `name` и `tree` адресуются отдельно |
| `.toml` | одна `[секция]` | wally / rokit |

Приоритет корпусов после RRF: `project` 1.00, `curated_kb` 0.99, `cookbook` 0.96,
`troubleshooting` 0.95, `anti_patterns` 0.93, `official_docs` 0.92, `engine_api` 0.90,
`cloud_docs` 0.88. Веса BM25 (`symbol` ×8, `class_name` ×4) вытаскивают точный символ
вперёд **внутри** корпуса; между корпусами решает таблица. Поэтому страницы API не
должны дублироваться в гайдах: копия из гайдов (без `security`/`thread_safety`) стоит
выше настоящей — см. «Грабли».

## Линтер: что он ловит и чего не делает

| Правило | Severity | Что значит |
|---|---|---|
| `unclosed-block` / `stray-close` | error | несбалансированный `end` — скрипт не скомпилируется |
| `method-case` | error | `:findFirstChild(` — метода не существует, вернётся `nil` |
| `server-only-service` | error | `DataStoreService` в клиентском скрипте |
| `localplayer-on-server` | error | `Players.LocalPlayer` на сервере всегда `nil` |
| `removed-api` | error | `LoadLibrary` удалён из Roblox |
| `deprecated-api` | warning | `wait` / `spawn` / `delay` / `tick` |
| `instance-new-parent` | warning | `Instance.new(class, parent)` |
| `numeric-require` | warning | `require(<assetId>)` |
| `busy-loop` | warning | `while true do` без `task.wait` |

**`method-case` срабатывает только на настоящий API-метод**, записанный не в том
регистре (`API_METHOD_CASE` в `luau/lint.py`). Наивная версия «любой `:lowercase(` — ошибка»
красила `Shop:total()`, `Shop:notify()` и аннотацию возвращаемого типа `): typeof(Shop)`,
то есть **любой живой проект**. Линтер, который кричит на нормальный код, выключают — и
тогда он не ловит ничего. Регистр проверяется только там, где известно, что слева
Roblox-инстанс.

Это **линтер, а не проверка типов**: он говорит «это не заработает», но не «это не
скомпилируется». Настоящая проверка поведения — плейтест через Studio MCP
(`start_stop_play` + `get_console_output`), и `check.py` пишет это в вердикте.

## Тесты

`tests/test_roblox.py` (входит в `gs test`) — 22 проверки, каждая на конкретный способ
соврать правдоподобно, а не упасть:

- **сканер блоков Luau** — `end` внутри `"end"`, `[[ end ]]` и `-- end` не должен
  закрывать функцию, а `for … do` не должен считаться дважды;
- **чанкинг API по членам** — `SetNetworkOwner` отдельным чанком со своим
  `thread_safety`, унаследованные члены пропущены, JSON-контракт свойства разобран;
- **severity линтера** — `error` только на нерабочее, `warning` на стиль;
- **ложные срабатывания** — фикстура `tests/fixtures/rbx_clean_place` (обычный проект с
  Rojo-деревом, методами модуля и `--!strict`) обязана давать **ноль** замечаний;
- **песочница путей** — `..`, абсолютный путь и соседняя папка `<root>-evil` отбиваются;
- **реестр MCP** — у каждого движка есть rag-сервер, у godot/unity/roblox — project-сервер,
  а все плейсхолдеры `{repo}`/`{python}`/`{studio_mcp}` известны рендереру.

Фикстуры: `tests/fixtures/rbx_lint_place` (7 заведомых дефектов, 4 error + 3 warning) и
`tests/fixtures/rbx_clean_place` (эталон, 0 замечаний).

## Грабли, на которые уже наступили

- **`Path(dest) / "/docs/en-us/…"` — абсолютный путь.** Индекс Cloud содержит ссылки
  двух видов, и вторая форма уводила 43 страницы в `F:\docs\en-us\…`. Теперь `_target()`
  принудительно делает путь относительным и отказывается писать вне корпуса.
- **`llms-full` есть только у гайдов.** `reference/engine/llms-full.txt` и
  `cloud/llms-full.txt` отдают 404 — это HTML страницы 404, а не документ. Проверять
  `Content-Type`, а не только код ответа.
- **`llms-full.txt` содержит и страницы API.** 1210 страниц `reference/engine/**` лежали
  дважды: в `official_docs` (из дампа) и в `engine_api` (постранично), байт в байт. Это
  дало **9940 дублирующих чанков — 56% корпуса гайдов**, причём выигрывал худший вариант:
  чанкер гайдов не умеет per-member `signature`/`security`, а `official_docs` в
  `SOURCE_PRIORITY` стоит выше `engine_api`. Теперь `fetch_guides` пропускает страницу,
  если её копия уже есть в `engine_api/`; страницы, которых там нет (`globals.md`,
  `libraries.md`, `overview.md` — индексные разделы), остаются в гайдах.
- **Индексатор не вычищал удалённые файлы.** `delete_paths` заменяет только устаревшую
  ревизию существующего файла, поэтому удалённая из `knowledge/` страница продолжала
  отвечать на запросы вечно. Добавлен `prune` (`source_paths(source) - seen`), с защитой:
  при `scanned == 0` (пустой/отсутствующий корпус) не удаляется ничего.
- **Свойства и дататипы описывают контракт JSON-блоком**, а не строкой
  `*Security: … · Thread Safety: …*` как методы. Оба формата разбираются.
- **В теге метода не два сегмента, а три-четыре, и первый может быть флагом.** В корпусе
  семь форм: `*Security: None · Thread Safety: Unsafe*`, `… · Capabilities: X*`,
  `… · Simulation Access: true*`, и **368 методов начинаются с `*Yields · Security: …`**.
  Две регулярки подряд соврали молча: первая требовала `*` сразу после `Thread Safety` и
  не совпадала ни с одной страницей, вторая была заякорена на `*Security:` и теряла все
  `Yields`-методы. При этом `security` выживал через слабый фолбэк, поэтому потеря
  `thread_safety` была незаметной. Теперь строка тега **разбирается по сегментам**, а не
  матчится шаблоном: `key: value` → snake_case-ключ, голый сегмент → флаг
  (`yields: "true"`).
- **`context` для Luau берётся из пути, а не из текста.** `_context_of` — эвристика по
  прозе документации («only works when used in a Script»); в коде таких слов нет, поэтому
  фильтр `rbx_rag_search(context="server")` возвращал пустоту. Теперь `script_context()`
  по Rojo-пути, и заголовочный чанк тоже получает `context`.
- **`default.project.json` — приоритет, а не «самое короткое имя».** `alt.project.json` и
  `default.project.json` одной длины, и алфавитный порядок выбирал не тот файл.
- **`tasklist` на русской Windows отдаёт cp866**, а не UTF-8 — `text=True` в
  `subprocess` падал с `UnicodeDecodeError` на 0x88. Читать байты и декодировать с
  `errors="replace"`.
- **`mcp.bat` версионно-независим**: он сам ищет `StudioMCP.exe` рядом с текущим билдом,
  поэтому в конфиге MCP используется он, а не путь с хешем версии.
- **Studio MCP не работает, пока Studio закрыта** — это не ошибка установки. `rbx_studio_status`
  отвечает на вопрос «закрыта» vs «сломана».

