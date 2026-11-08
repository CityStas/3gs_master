# 3GS_Master

Среда, в которой AI-агент делает игры для четырёх движков - **Three.js**, **Godot 4**,
**Unity 6** и **Roblox Studio (Luau)**. RAG по документации каждого движка, MCP-серверы
знаний и ассетов, генерация арта и 3D на одной видеокарте 8 ГБ.

![Четыре персонажа, сгенерированные локально](docs/preview.webp)

По умолчанию агент работает на локальной модели; облачную можно подключить вместо
неё или вести сессию сразу на двух.

## Требования

- Windows, Python 3.11+ (`.venv` в корне)
- веса моделей и бинарники в `bin/` - в репозиторий не входят, порядок установки
  описан в [`docs/ARCHITECTURE.md`](docs/ARCHITECTURE.md)
- 8 ГБ VRAM: на карте одновременно живёт одна модель - LLM, генератор картинок
  или ComfyUI

## Модели: где лежат

Веса (~65 ГБ) в git не входят, поэтому «где модели» - свойство машины, а не репозитория.
Корень задаётся одной переменной, по умолчанию `<repo>/models`:

| переменная | по умолчанию | что покрывает |
|---|---|---|
| `GS_MODELS_ROOT` | `<repo>/models` | всё: чат-GGUF, эмбеддер, реранкер, VLM, z-image, ComfyUI |
| `GS_LLM_MODELS_DIR` | пусто | доп. корни **только** для чат-моделей, через `;` |

Абсолютных путей в коде нет - буква диска не зашита нигде. Если веса лежат на другом
диске, это одна строка в `local.env.cmd` (копия `local.env.example.cmd`, в git не попадает):

```cmd
copy local.env.example.cmd local.env.cmd
:: затем в local.env.cmd:
set "GS_MODELS_ROOT=D:\AI\Models"
```

Проверить, что где лежит и чего не хватает:

```cmd
gs models --paths
```

Раскладка внутри корня: `*.gguf` в корне (9B чат, `bge-m3`, `bge-reranker`),
`vlm/Qwen2.5-VL-7B/`, `image/z-image-turbo/`, `text_image_3D/` (ComfyUI и его 3D-модели,
~45 ГБ). Этот же корень читают все четыре движка, роутер llama.cpp на :8080,
`vlm.cmd`, `sd-image.cmd` и приложение hc_local_ai_image_3D (через `HC_MODELS_ROOT`).

## Быстрый старт

```cmd
git clone https://github.com/CityStas/3gs_master
cd 3gs_master
python -m venv .venv && .venv\Scripts\pip install -r requirements.txt
gs models --paths                 :: что уже есть, чего не хватает
gs doctor                         :: окружение целиком
dev.cmd my_game
```

`dev.cmd <игра>` поднимает нужные сервисы, проверяет окружение и открывает агента
в папке игры. Флаг `--studio` добавляет редактор уровней (только для Three.js).

## Новый проект

Проект - это папка `projects/games/<имя>`. Движок задаёт файл `engine.json` в её
корне; без него агент работает в режиме Three.js.

| Движок | `engine.json` | Что сделать перед запуском |
| --- | --- | --- |
| Three.js | `{ "engine": "threejs", "version": "r186" }` | `cmd\init.cmd <имя>` — раскладывает three.js-стек по маркеру |
| Godot 4 | `{ "engine": "godot", "version": "4.7.2" }` | создать проект в Godot Project Manager в этой папке |
| Unity 6 | `{ "engine": "unity", "version": "6000.3" }` | создать проект в Unity Hub или дать это агенту |
| Roblox | `{ "engine": "roblox" }` | `gs roblox-fetch`, `gs roblox-index`, затем `gs roblox-open` |

Для Roblox дополнительно нужны две вещи, которых нет у остальных движков: корпус
документации скачивается отдельно (`gs roblox-fetch`, ~3600 страниц), а встроенный MCP
Studio включается **внутри Studio** - Assistant → … → Manage MCP Servers → Enable
Studio as MCP server.

Дальше - `dev.cmd <имя>`. Инструменты движка появляются у агента только под проект
с соответствующим `engine.json`.

## Документация

- [`docs/ARCHITECTURE.md`](docs/ARCHITECTURE.md) - архитектура, лаунчеры, MCP, диагностика
- [`AGENTS.md`](AGENTS.md) - правила агента
- [`ASSET-POLICY.md`](ASSET-POLICY.md) - откуда берутся ассеты
- [`LEVEL-SCHEMA.md`](LEVEL-SCHEMA.md), [`STUDIO.md`](STUDIO.md) - уровни и студия (Three.js)
- [`unity/README.md`](unity/README.md) - Unity-стек
- [`roblox/README.md`](roblox/README.md) - Roblox-стек (Luau, Studio MCP, корпус)
- [`mcp/registry.json`](mcp/registry.json) - единственное описание MCP-серверов для pi и WorkBuddy

## Что в репозитории, а что нет

В git лежит код, корпус документации и конфигурация агента. Абсолютных путей нет:
машинные (`GS_MODELS_ROOT`, `BLENDER_EXE`, `UNITY_EDITOR`) живут в `local.env.cmd`,
которого в git нет - есть только `local.env.example.cmd`. Исключены веса моделей,
бинарники движков, кэши RAG, пользовательские проекты и логи - поэтому клон без
дополнительных шагов не запустится: сначала нужны модели и `.venv`.
