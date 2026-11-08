# 3GS_Master

Среда, в которой AI-агент делает игры для четырёх движков - **Three.js**, **Godot 4**,
**Unity 6** и **Roblox Studio (Luau)**. RAG по документации каждого движка, MCP-серверы
знаний и ассетов, генерация арта и 3D на одной видеокарте 8 ГБ.

![Четыре персонажа, сгенерированные локально](docs/preview.webp)

По умолчанию агент работает на локальной модели; облачную можно подключить вместо
неё или вести сессию сразу на двух.

## Требования

- Windows, Python 3.11+ (`.venv` в корне)
- **~39 ГБ весов** (скачиваются одной командой, см. ниже) и бинарники в `bin/` - в git
  они не входят
- 8 ГБ VRAM: на карте одновременно живёт одна модель - LLM, генератор картинок
  или ComfyUI

## Модели: скачать

Веса в git не входят: клон получает код и пустой `models/`. Что именно нужно и откуда
это брать, записано в [`models.manifest.json`](models.manifest.json) - на каждый файл
репозиторий на HuggingFace, точный размер и `sha256`.

```cmd
python -m venv .venv && .venv\Scripts\pip install -r requirements.txt
gs models --fetch              :: всё, что помечено default (~39 ГБ)
gs models --verify             :: пересчитать хеши
```

`--fetch` качает только отсутствующее, докачивает с места обрыва (`.part` + `Range`) и
сверяет `sha256` на лету - недокачанный файл никогда не станет похож на рабочий.
Плохая связь с HuggingFace - добавь `--mirror` (hf-mirror.com).

Можно взять не всё:

| группа | размер | что это | нужна для |
|---|---|---|---|
| `llm` | 6.2 ГБ | Qwen3.5-9B Q4_K_M | агент (роутер :8080) |
| `rag` | 1.1 ГБ | `bge-m3` + `bge-reranker-v2-m3` | поиск по документации |
| `vlm` | 5.5 ГБ | Qwen2.5-VL-7B + mmproj | «посмотри на скриншот» (:8082) |
| `image` | 6.5 ГБ | z-image-turbo + VAE + текстовый энкодер | текст → картинка (:8687) |
| `3d` | 13.3 ГБ | Pixal3D, MoGe, TripoSplat, BiRefNet | картинка → GLB (ComfyUI :8188) |
| `3d-x` | 6.5 ГБ | бэкбон Trellis2 (`switch=True`) | альтернатива Pixal3D |

```cmd
gs models --fetch llm,rag      :: 7.2 ГБ - хватает на агента и RAG
gs models --fetch all          :: включая необязательный 3d-x
gs models --verify rag --strict
```

**3D отдельно:** модели `3d` кладутся внутрь ComfyUI, поэтому сначала сам движок.
`--fetch` скажет, куда именно, если его нет; после установки ComfyUI повтори команду.

## Модели: где лежат

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
`vlm/Qwen2.5-VL-7B/`, `image/z-image-turbo/`, `text_image_3D/` (ComfyUI и его 3D-модели).
Этот же корень читают все четыре движка, роутер llama.cpp на :8080, `vlm.cmd`,
`sd-image.cmd` и приложение hc_local_ai_image_3D (через `HC_MODELS_ROOT`).

## Быстрый старт

```cmd
git clone https://github.com/CityStas/3gs_master
cd 3gs_master
python -m venv .venv && .venv\Scripts\pip install -r requirements.txt
gs models --fetch                 :: ~39 ГБ весов, один раз
gs doctor                         :: окружение целиком
dev.cmd my_game
```

`dev.cmd <игра>` поднимает нужные сервисы, проверяет окружение и открывает агента
в папке игры. Флаг `--studio` добавляет редактор уровней (только для Three.js).

## Новый проект

Проект - это папка `projects/<движок>/<имя>`. Движок задаёт `engine.json` - на самой
папке проекта или на папке движка, откуда он наследуется:

| Движок | папка | `engine.json` | Что сделать перед запуском |
| --- | --- | --- | --- |
| Three.js | `projects/three/<имя>` | `{ "engine": "threejs", "version": "r186" }` | `cmd\init.cmd <имя>` — раскладывает three.js-стек по маркеру |
| Godot 4 | `projects/godot/<имя>` | `{ "engine": "godot", "version": "4.7.2" }` | создать проект в Godot Project Manager в этой папке |
| Unity 6 | `projects/unity/<имя>` | `{ "engine": "unity", "version": "6000.3" }` | создать проект в Unity Hub или дать это агенту |
| Roblox | `projects/roblox/<имя>` | `{ "engine": "roblox" }` | `gs roblox-fetch`, `gs roblox-index`, затем `gs roblox-open` |

Старый `projects/games/<имя>` продолжает резолвиться как legacy, но нового там не
появляется. Раскладка описана в одном месте - `project_layout.py`.

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

В git лежит код, корпус документации, конфигурация агента и **`models.manifest.json`** -
опись весов со ссылками и хешами, по которой `gs models --fetch` их и забирает.
Абсолютных путей нет: машинные (`GS_MODELS_ROOT`, `BLENDER_EXE`, `UNITY_EDITOR`) живут
в `local.env.cmd`, которого в git нет - есть только `local.env.example.cmd`.
Исключены сами веса, бинарники движков, кэши RAG, пользовательские проекты и логи -
поэтому клон без `gs models --fetch` и `.venv` не запустится.
