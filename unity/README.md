# unimaster — Unity-only local RAG coding agent

Полностью локальный coding agent, который умеет работать **только** с Unity 6000.3.
Третий движок в репозитории, рядом с Three.js и Godot: своя база знаний, свой RAG,
свой профиль `pi`, свой набор инструментов. Общее — только серверы моделей и `.venv`.

> Общая архитектура репозитория — [`../docs/ARCHITECTURE.md`](../docs/ARCHITECTURE.md).
> Правила агента в Unity-проекте — [`AGENTS.md`](AGENTS.md).

---

## Что внутри

```
unity/
├─ unimaster/                 код
│  ├─ config.py               все пути и константы (UNIM_HOME)
│  ├─ rag/
│  │  ├─ chunkers.py          чанкование C#, HTML, Markdown, Unity YAML, Shader
│  │  ├─ embedder.py          bge-m3 через HTTP (:8081), клип + повтор усечением
│  │  ├─ store.py             SQLite + FTS5, brute-force cosine по numpy
│  │  ├─ indexer.py           инкрементальная индексация, repair-режим для векторов
│  │  └─ retriever.py         RRF-слияние dense + lexical с приоритетом источника
│  ├─ unity/
│  │  ├─ paths.py             песочница путей, поиск редактора и CLI
│  │  ├─ lint.py              линт Unity 5/6 API (severity: error / warning)
│  │  └─ batch.py             -batchmode -quit, -createProject, -executeMethod
│  └─ mcp/
│     ├─ rag_mcp_server.py    unity_rag_search, unity_rag_status
│     └─ project_mcp_server.py  инспекция, правка, проверка, скелет
├─ tools/
│  ├─ fetch_docs.py           корпус по TOC (Manual, ScriptReference, packages, source)
│  ├─ index.py                сборка индекса
│  ├─ doctor.py               диагностика стека
│  └─ check.py                линт проекта (+ --compile)
├─ knowledge/                 корпус (см. ниже)
├─ data/                      индекс, логи. Указатель проекта - ОБЩИЙ (корень репозитория)
├─ logs/                      логи batch-прогонов Unity
├─ pi-home-unity/             ИЗОЛИРОВАННЫЙ agent-dir pi (SYSTEM.md + skills)
├─ AGENTS.md                  правила работы в Unity-проекте (справочник для человека)
└─ Unity_RAG_Resources.md     исходная карта ресурсов (откуда всё бралось)
```

### Изоляция `pi` (важно)

`pi` читает два конфига: пользовательский `~/.pi/agent/` и проектный `.pi/`.
Пользовательский каталог на этой машине содержит посторонние MCP-серверы и чужого
провайдера, смотрящего на `:8081` (это порт **embedding**-сервера). В таком виде pi
отдаёт модели чужие инструменты — Unity-граница рушится до первого запроса.

Поэтому Unity-профиль **не использует** `~/.pi/agent`. `agent.cmd` подставляет:

```
PI_CODING_AGENT_DIR=<репозиторий>\pi-home-unity
PI_SKIP_VERSION_CHECK=1
PI_TELEMETRY=0
```

Профиль выбирается по `engine.json` активного проекта:

| `engine`            | Профиль         |
| ------------------- | --------------- |
| `godot`             | `pi-home-godot` |
| `unity`             | `pi-home-unity` |
| `threejs` / нет     | `pi-home-three` |

`pi-home-unity/` содержит `SYSTEM.md`, `settings.json` (`defaultProjectTrust: "always"`,
`reserveTokens: 16384`), `models.json` (провайдер `3gs`, ctx 65536, maxTokens 12288),
`mcp.json` и `skills/` (7 скиллов).

Инструменты регистрирует не промпт, а `.pi/extensions/engine-gate.ts`. Под Unity-профилем
модель **не видит** godot-инструментов вообще: они не зарегистрированы. 9B-модель не может
вызвать инструмент, которого нет в `tools/list` — это надёжнее любого запрета текстом.

---

## Корпус знаний

| Источник | Что это | Откуда | Файлов |
| --- | --- | --- | --- |
| `official_docs/Manual` | руководство Unity | `docs.unity3d.com/6000.3/Documentation/Manual/` | 2805 |
| `official_docs/ScriptReference` | API по классам и namespace | `…/ScriptReference/` | 4132 |
| `official_source` | **реальный C#** Unity | `Unity-Technologies/UnityCsReference@6000.3` | 5724 |
| `packages_docs` | UPM-пакеты: Input System, URP, Addressables, AI Navigation, Cinemachine, Burst, Entities, glTFast, … (22 пакета) | `docs.unity3d.com/Packages/<name>@<ver>/` | 14028 |
| `cookbook` | рабочие паттерны | написано руками | 9 |
| `recipes` | пошаговые рецепты | написано руками | 3 |
| `troubleshooting` | разбор ошибок | написано руками | 3 |
| `anti_patterns` | ловушки Unity API | написано руками | 1 |

Всего ~26 700 файлов, ~455 МБ. Осталось докачать ~35 страниц ScriptReference и единицы в
пакетах (они упёрлись в HTTP 429) — `gs unity-fetch` добирает их идемпотентно.

Собранный индекс на этом корпусе:

| источник | файлов | чанков |
| --- | --- | --- |
| `official_source` | 5714 | 219 749 |
| `packages_docs` | 14 026 | 57 710 |
| `official_docs` | 6939 | 52 843 |
| локальные (`cookbook`, `recipes`, `troubleshooting`, `anti_patterns`) | 16 | 103 |
| **итого** | **26 695** | **330 405** (740 МБ) |

Исходники C# дают две трети индекса — и именно они отвечают на точные имена API
(`Rigidbody.AddForce` → `Modules/Physics/ScriptBindings/Rigidbody.bindings.cs`), тогда как
отрендеренная страница ScriptReference отдаёт только описание.

**Почему по TOC, а не краулером.** `docs.unity3d.com` отдаёт машиночитаемый
`<section>/docdata/toc.json` для Manual и ScriptReference, поэтому полный список страниц —
один запрос вместо обхода ссылок. Скачанные `toc.json` сохраняются в `_toc/`, чтобы индекс
был воспроизводим.

**У пакетов (UPM) TOC устроен иначе** — это выяснилось пробами, а не догадкой:

| | Manual / ScriptReference | `packages_docs` |
| --- | --- | --- |
| Список страниц | `<sec>/docdata/toc.json` | `<sec>/toc.html` (обычные `<a href>`) |
| Версия в URL | `/6000.3/Documentation/` | `/Packages/<name>@<ver>/` |
| Алиас `@latest` | не нужен | **не существует** |

Поэтому версия пакета берётся из реестра Unity (`https://packages.unity.com/<name>` →
`dist-tags.latest`), обрезается до `major.minor` (сайт документирует `@1.20`, а не `@1.20.1`)
и проверяется запросом; захардкоженная версия в таблице — только запасной вариант на случай
недоступности реестра. Пакет без доступной документации помечается предупреждением и не
ломает остальные.

**Почему исходник важнее страницы.** В `UnityCsReference` лежат настоящие атрибуты,
дефолты и перегрузки **установленной** версии. Страница API их часто опускает, а
рендеренный HTML ещё и меняет разметку между версиями. Для coding agent'а, которому нужна
точная сигнатура, C# — первичен.

**Почему в исходнике нужен `Modules/`.** Репозиторий UnityCsReference держит 5774 `.cs`:
`Modules/` — 3712, `Editor/` — 1497, `Runtime/` — 515. Всё, что агент реально вызывает
(`Rigidbody`, `Transform`, `NavMeshAgent`, `Animator`, `SpriteRenderer`, `AudioSource`),
лежит в `Modules/`. Первый вариант фетчера брал только `Runtime/` + `Editor/` — и в корпусе
не оказалось ни физики, ни анимации, ни навигации. Проверять состав корпуса нужно по
реальному дереву репозитория, а не по памяти о его структуре.

### Ограничение частоты (важно при докачке)

`docs.unity3d.com` жёстко режет частоту. Залп из 8 воркеров получил
**2225 отказов HTTP 429 из 2827** страниц Manual за один прогон. Поэтому:

- по умолчанию `--workers 4`;
- на 429/5xx запрос **ждёт** с экспоненциальной задержкой (уважая `Retry-After`), а не
  бросает страницу;
- есть `--delay` для ровного троттлинга (`--delay 0.3 --workers 3`);
- файлы докачиваются идемпотентно — повторный запуск берёт только отсутствующие.

Докачка обрывается и продолжается без потерь: `gs unity-fetch` можно запускать сколько
угодно раз.

---

## Быстрый старт

### 1. Поднять серверы (общие для всех трёх движков)

```cmd
cd /d F:\Pets\Projects\local_tools\3GS_Master
serve-all.cmd
```

LLM на `:8080`, embeddings на `:8081`. Без `:8081` индекс собирается **без векторов**
(только lexical-поиск) — см. «Индекс» ниже.

### 2. Скачать корпус

```cmd
gs unity-fetch                    :: Manual + ScriptReference + 22 UPM-пакета
gs unity-fetch --only manual      :: только руководство
gs unity-fetch --with-source      :: + UnityCsReference C# (5724 файла)
gs unity-fetch --check            :: что уже на диске
gs unity-fetch --delay 0.3 --workers 3   :: медленнее, если ловишь 429
```

Полный корпус — ~26 700 файлов, поэтому первый прогон идёт **десятки минут** (у меня
~20 мин только на Manual + ScriptReference и ~24 мин на пакеты). Прерывать можно:
следующий запуск продолжит с места остановки — фетчер идемпотентен.

### 3. Собрать индекс

```cmd
gs unity-index
```

Индексация инкрементальная: файл с неизменившимися mtime+size и совпавшим SHA-256 не
трогается. Если `:8081` был выключен, батчи сохранились без векторов — это лечится
точечно, без переиндексации всего:

```cmd
gs unity-index --vectors
```

Этой команде нужен **только `:8081`** (`:8080` — языковая модель агента, для доливки
векторов не требуется). Работа длинная: ~330k чанков на CPU — часы, а не минуты, поэтому
запускать в фоне. Прерывание безопасно: `chunks_without_vectors()` берёт `WHERE vec IS NULL`,
так что повторный запуск досчитывает только остаток. Прогресс — `gs unity-doctor`, строка
`index` (`… N vectors`).

Перезапускать агента после доливки не нужно: пустая матрица векторов не кэшируется, поэтому
живой MCP-сервер подхватит их сам.

Сервер эмбеддингов опрашивается **не на каждом батче**: после трёх неудач подряд прогон
перестаёт его дёргать и пишет остаток текстом, один раз сообщив об этом. Иначе выключенный
`:8081` стоил бы секунды на батч, а корпус — это ~1000 батчей. Вернувшийся сервер снова
используется: счётчик сбрасывается при первом успехе.

### 4. Проверить стек

```cmd
gs unity-doctor
```

Показывает редактор, CLI, корпус по источникам, состояние индекса и серверы.

### 5. Запустить агента на проекте

```cmd
dev.cmd my_unity_game
```

или явно:

```cmd
agent.cmd projects\games\my_unity_game
```

`engine.json` в корне проекта должен содержать `"engine": "unity"` — иначе поднимется
профиль Three.js и Unity-инструментов у модели не будет.

---

## Инструменты, которые видит модель

Всего **14** (12 у `unity-project` + 2 у `unity-rag`). Официальный Unity MCP отдаёт ~160
инструментов; для локальной 9B-модели это деградация, а не возможности (Godot-стек по той
же причине урезал 193 → 23).

**Знания** — `unity_rag_search` · `unity_rag_status`

**Инспекция (read-only)** — `unity_project_info` · `unity_list_files` · `unity_read_file` ·
`unity_script_symbols` · `unity_find_symbol`

**Правка** — `unity_write_script` · `unity_edit_script` (перед перезаписью кладёт копию в
`<проект>/.unim/backups/`; при неоднозначном `old_string` отказывает и показывает
ближайшие строки)

**Проверка** — `unity_validate` · `unity_console` · `unity_run_method`

**Скелет** — `unity_project_create` (создаёт проект через `-createProject` и **пишет
`engine.json`** с `"engine": "unity"`, иначе следующий запуск `agent.cmd` поднимет профиль
Three.js и Unity-инструментов у модели не будет)

**Показать** — `unity_open_editor`

### `unity_validate` — два уровня

| Аргумент | Что делает | Сколько |
| --- | --- | --- |
| `paths=[…]` | линт Unity 5/6 API | секунды |
| `compile=true` | + реальная компиляция редактором | минуты, редактор должен быть закрыт |

Ответ содержит `ok` (нет **ошибок**), `errors`, `warnings` и `lint_hint`. Находки линта
дублируются в `warnings` — модель читает это поле, даже когда игнорирует новые.

---

## Линт Unity 5/6 API (то, чего не видит компилятор)

Компилятор проверяет **синтаксис**, а не существование API. Строка

```csharp
rb.velocity = new Vector3(1, 0, 0);
```

синтаксически безупречна — а в Unity 6 свойство называется `linearVelocity`. Локальная
9B-модель пишет Unity 5 API по памяти постоянно: его в обучающих данных на порядок больше.

Ловится:

| Код | Severity | Что |
| --- | --- | --- |
| `CS-VALUE-COMPONENT` | **error** | `transform.position.x = 5f` — CS1612, присваивание в поле структуры по значению |
| `LEGACY-COMPONENT-ACCESSOR` | **error** | `gameObject.rigidbody`, `.renderer`, `.camera` — удалено в Unity 5 |
| `LEGACY-APPLICATION-LEVEL` | **error** | `Application.LoadLevel*`, `Application.loadedLevel` |
| `LEGACY-ONLEVELWASLOADED` | **error** | `OnLevelWasLoaded` — удалено в 5.4 |
| `LEGACY-WWW` | **error** | `WWW`, `WWWForm` — удалено в 2018 |
| `LEGACY-UNITY-NETWORKING` | **error** | `Network.*`, `NetworkView` |
| `LEGACY-FINDCHILD` / `LEGACY-SETACTIVERECURSIVELY` / `LEGACY-PREFABUTILITY` | **error** | удалённые API |
| `LEGACY-UNITYSCRIPT` | **error** | `function foo()` — UnityScript удалён в 2018 |
| `NEW-INPUT-SYSTEM-ONLY` | **error** | `Input.*` в проекте с `activeInputHandler: 1` — `InvalidOperationException` в рантайме |
| `UNITY6-RIGIDBODY-VELOCITY` | warning | `.velocity` — в Unity 6 это `linearVelocity` (у `NavMeshAgent` `.velocity` законен) |
| `UNITY6-FIND-OBJECTS` / `UNITY6-FIND-OBJECT` | warning | `FindObjectsOfType<T>()` → `FindObjectsByType<T>(…)` |
| `LEGACY-STRING-COMPONENT` | warning | `GetComponent("Name")` |
| `EDITOR-API-IN-RUNTIME` | warning | `UnityEditor.*` в рантайм-скрипте — ломает билд |

**Severity решает вердикт:** `error` краснит `ok`, `warning` — нет. Это не косметика:
`NavMeshAgent.velocity` существует, поэтому `.velocity` сам по себе — только совет, а вот
`.rigidbody` не существует нигде.

`EDITOR-API-IN-RUNTIME` **не срабатывает**, если файл лежит в папке `Editor/`/`EditorTools/`
или содержит `#if UNITY_EDITOR` — там editor-API законен.

Комментарии и строковые литералы вырезаются перед проверкой: старое API в `//`-комментарии
находкой не считается.

---

## Два правила, которые закрывают типовые провалы

### Сцены и префабы не пишутся текстом

`.unity`, `.prefab`, `.asset`, `.controller` — это Unity YAML с GUID-ссылками на `m_Script`,
fileID и локальными id. Написанный руками файл **синтаксически валиден и мёртв по ссылкам**:
сцена открывается, компоненты пустые, **исключения нет**. Ошибка тихая.

Правильный путь — editor-скрипт, который исполняет сама Unity:

```csharp
// Assets/Editor/LevelBuilder.cs
public static class LevelBuilder {
    [MenuItem("Tools/Build Level")]
    public static void Build() {
        var root = new GameObject("Level");
        var light = root.AddComponent<Light>();
        light.type = LightType.Directional;
        UnityEditor.SceneManagement.EditorSceneManager.SaveScene(
            UnityEngine.SceneManagement.SceneManager.GetActiveScene(), "Assets/Scenes/Main.unity");
    }
}
```

```
unity_write_script("Assets/Editor/LevelBuilder.cs", "...")
unity_run_method("LevelBuilder.Build")      # -batchmode -executeMethod
```

YAML тогда пишет Unity, и он корректен by construction — ровно как в Godot-стеке сцена
меняется через `SceneTree`-скрипт, а не правкой `.tscn`.

### Один редактор на проект

Unity **отказывается** открывать уже открытый проект: batch-прогон против живого редактора
падает не с ошибкой компиляции, а с локом (`Temp/UnityLockfile`). `unity_validate(compile=true)`
и `unity_run_method` проверяют лок **до** запуска и говорят об этом прямо, вместо того чтобы
вернуть непонятную ошибку.

Обратная сторона: если редактор открыт, ошибки компиляции и так видны — через
`unity_console()` (читает `%LOCALAPPDATA%\Unity\Editor\Editor.log`), и batch не нужен.

---

## Проверка без агента

```cmd
gs unity-check my_unity_game               :: линт, секунды
gs unity-check my_unity_game --compile     :: + компиляция редактором, минуты
gs unity-check my_unity_game --json        :: машинный вывод
gs unity-doctor                            :: окружение, корпус, индекс
```

Вердикт по худшему: код возврата 1 при **ошибках** (линта или компиляции). Warning'и
вердикт не краснят.

---

## Индекс

```cmd
gs unity-index                          :: инкрементально
gs unity-index --force                  :: полная пересборка (после смены версии)
gs unity-index --vectors                :: только недостающие векторы
gs unity-index --only official_docs     :: один корпус
gs unity-index --project <путь>         :: + исходники проекта как source=project
```

Архитектура — как у Three.js и Godot: SQLite + FTS5 (BM25) для lexical, numpy-матрица
(1024d, brute-force cosine) для dense, слияние **RRF** (k=60) с весами по источнику
(`project` и `recipes` — 1.00, `cookbook` — 0.95, …). Векторной БД нет намеренно:
Qdrant в local-режиме держит эксклюзивный лок на каталог, а MCP-сервер живёт постоянно —
конфликт с индексатором. Brute-force по десяткам тысяч чанков — единицы миллисекунд.

`Symbol` / `class_name` / `path` в BM25 весят 8/4/1: точное имя API
(`Rigidbody.AddForce`, `MissingReferenceException`) — весь смысл lexical-половины.

### Инвариант: `chunks_fts.rowid == chunks.rowid`

**Не «упрощать» удаление обратно на `WHERE id=?`.** Колонка `id` в FTS5 объявлена как
`UNINDEXED`, поэтому равенство по ней не может использовать полнотекстовый индекс — это
полный скан таблицы. На корпусе в 26.7k файлов такой скан на каждый чанк пакета давал
**15 чанков/с вместо 35 000**: сборка индекса шла сутки. Ключ — `rowid` (первичный ключ
FTS5, удаление O(log n)), поэтому `upsert` пишет явный `rowid` в обе таблицы, а
`delete_paths` и `lexical_search` работают по нему же. Разбор и замеры — `REFERENCE.md`.

Если индекс собран до этой правки, `_ensure_fts_alignment()` при первом открытии
пересоберёт FTS из `chunks` (флаг `meta.fts_rowid_aligned`) — ручных шагов не нужно.

### Чанкование

| Тип | Как режется |
| --- | --- |
| C# (`.cs`) | по типам, методам, свойствам, полям; `_cs_block_end` пропускает `//`, `/* */`, `"…"`, `@"…"`, `'…'` |
| Unity YAML (`.unity`, `.prefab`, `.asset`) | по документам `--- !u!<class> &<id>`, метка из `m_Name` |
| HTML (документация) | по секциям (`h1`–`h3`) |
| Shader (`.shader`, `.hlsl`, `.cginc`) | по блокам `CGPROGRAM`/`HLSLPROGRAM` … `ENDCG`/`ENDHLSL` |
| Markdown (cookbook, recipes) | по заголовкам, с маскировкой код-фенсов |

Метаданные чанка: `source`, `path`, `file_type`, `symbol`, `class_name`, `namespace`,
`member_kind`, `section`, `engine_version`, `content_hash`.

---

## Переменные окружения

| Переменная | Смысл | По умолчанию |
| --- | --- | --- |
| `UNIM_HOME` | корень стека | `<репозиторий>/unity` |
| `UNITY_PROJECT` / `UNIM_PROJECT` | корень Unity-проекта (перебивает `active_project.txt`) | — |
| `UNITY_EDITOR` / `UNIM_UNITY` | путь к `Unity.exe` | автоопределение |
| `UNITY_DOC_VERSION` | версия документации | `6000.3` |
| `UNITY_EDITOR_VERSION` | версия редактора | `6000.3.26f1` |
| `UNIM_LLM_PORT` / `UNIM_EMBED_PORT` | порты моделей | `8080` / `8081` |
| `UNIM_EMBED_DIM` | размерность эмбеддинга | `1024` (bge-m3) |
| `UNIM_DENSE_TOP_K` / `UNIM_LEXICAL_TOP_K` | кандидатов на этапе retrieval | `20` / `20` |
| `UNIM_FINAL_TOP_K` | passages в контексте | `8` |
| `UNIM_RRF_K` | константа RRF | `60` |
| `UNIM_MAX_INDEX_FILE_BYTES` | файлы больше — не индексируются | 1 МиБ |

---

## Диагностика

| Симптом | Причина / что делать |
| --- | --- |
| `unity_*` не видно у модели | нет `"engine": "unity"` в `engine.json` проекта, либо агент запущен не через `agent.cmd` |
| `Unity.exe not found` | задать `UNITY_EDITOR` или поставить редактор в `E:\Programs\Unity Hub\Unity\Editors\<ver>` |
| `the Unity editor is already open on …` | закрыть редактор, либо использовать `unity_console()` вместо batch |
| `rag_search` возвращает пусто | индекс пуст → `gs unity-index`; состояние → `unity_rag_status` |
| Dense-поиск ничего не находит | индекс собран при выключенном `:8081` → `gs unity-index --vectors` |
| Фетчер сыпет `http 429` | нормальное поведение под лимитом; докачать `gs unity-fetch --delay 0.3 --workers 3` |
| Сцена открывается, компоненты пустые | `.unity`/`.prefab` писался текстом → строить editor-скриптом |
| Материал розовый | Built-in `Standard` в URP-проекте → `Universal Render Pipeline/Lit`, цвет `_BaseColor` |
| `.glb` не импортируется | нет `com.unity.cloud.gltfast` в `Packages/manifest.json` |
| `InvalidOperationException` на `Input.GetAxis` | проект на «Input System Package (New)» only |

Логи batch-прогонов: `unity/logs/unity-batch-*.log`, `unity/logs/unity-create-*.log`.

---

## Известные ограничения

- `-nographics` не рисует: визуальные дефекты агент поймать не может. Он проверяет
  компиляцию и линт, а не картинку.
- Play mode из batch не запускается: `-executeMethod` исполняет editor-код, а не игровой
  цикл. Проверить поведение в рантайме — только открыв редактор.
- Документация зафиксирована на 6000.3. Если проект на другой версии, `unity_rag_search`
  может вернуть API из 6000.3 — сверять через `unity_project_info`.
- Линт — регекспы, а не Roslyn: он ловит известные ловушки, а не «любое неверное API».
  Неизвестное модели API проверяет компилятор (`compile=true`).
- `packages_docs` фиксирует версию пакета на момент скачивания (реестр → `major.minor`),
  поэтому она может отличаться от той, что в `manifest.json` проекта. Для точной сигнатуры —
  `official_source` и сам проект.
- `.unim/backups/` растёт без автоочистки. Чистить вручную.
