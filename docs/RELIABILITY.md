# Reliability layer — циклы, ложный успех и «файл не найден»

Документ описывает то, что реально реализовано и проверено. Если чего-то здесь нет —
значит этого нет; список ограничений в конце честный.

**Проблема.** Локальная 9B-модель Q4_K_M на 8 ГБ VRAM в многошаговой задаче тратит ход
не на работу, а на повторение уже провалившегося вызова, и объявляет файл записанным,
когда запись не произошла. Логи сессии `2026-10-12`: 47 ходов ассистента, 20
повторных неудачных вызовов инструментов, компакция посреди задачи.

**Принцип.** Модель предлагает действия — рантайм проверяет реальность. Ни одно
утверждение модели о том, что файл прочитан, записан или проверен, не принимается без
результата инструмента и проверки постусловия.

---

## 1. Где что лежит

| Файл | Роль |
|---|---|
| `mcp/reliability.json` | **Единственный источник политики**: пороги, классификация ошибок, `next_action` для каждой. |
| `pi-extensions/reliability-core.ts` | Логика: классификация, отпечатки, loop guard, проверка записи, path guard, резолвер проекта, JSONL-лог. Без API pi. |
| `pi-extensions/loop-guard.ts` | Проводка к `tool_call` / `tool_result` pi. Только wiring. |
| `pi-home-*/extensions/loop-guard.ts` | Стабы-реэкспорты, по одному на профиль (pi читает `extensions/` профиля). |
| `tools/project_context.py` | Резолвер: repo root, активный проект, движок, **источник решения**, устаревший указатель, неоднозначный маркер. |
| `tools/reliability.py` | Python-двойник логики + CLI (`gs reliability`). |
| `tests/test_reliability.py` | Контракт обоих реализаций сразу. |
| `tests/reliability_parity.mjs` | Запускает TypeScript-ядро под голым node и печатает его ответы для сверки. |
| `logs/reliability/YYYY-MM-DD.jsonl` | События. Без содержимого файлов, без промптов, без секретов. |

Политика одна, реализаций две: живой guard обязан быть TypeScript (он внутри pi), всё
остальное — Python. Поэтому `tests/reliability_parity.mjs` прогоняет TS-ядро под node
(type stripping, без сборки) и `tests/test_reliability.py` сверяет ответы с Python на
одном и том же наборе фикстур. Изменение порога или паттерна в `mcp/reliability.json`
доходит до обеих; изменение только одной реализации валит тест, а не сессию.

---

## 2. Аудит: симптом → слой

| Симптом | Воспроизведён? | Подтверждённый слой | Доказательство | Что сделано |
|---|---|---|---|---|
| Модель повторяет тот же вызов после той же ошибки | да, детерминированно (`selftest`, сценарий `identical_hard_failure`) | клиент/рантайм (нет детектора), не модель | `tests/reliability_parity.mjs`: до guard'а — бесконечный повтор; после — `REPEATED_TOOL_CALL` | `loop-guard.ts` + `LoopGuard` |
| Чередование A→B→A→B без прогресса | да (`cycle_abab`) | рантайм | тот же harness | `TOOL_CYCLE_DETECTED` |
| «Файл записан», а файла нет / он старый / обрезан | да, четыре теста `verify_write` | инструмент + отсутствие постусловия | `test_verify_write_*` | проверка после каждого `write`/`edit`, иначе `WRITE_NOT_VERIFIED` и результат помечается ошибкой |
| Файл есть, но модель его «не находит» | да (`FILE_NOT_FOUND`) | промпт/контекст + отсутствие подсказки | `errorPayload` + `recoveryHint` | в ошибку добавляется ближайший существующий каталог, список имён, `did_you_mean`, `case_mismatch` |
| Неверный рабочий каталог / движок | да, `test_project_context_does_not_route_an_unknown_engine_into_threejs` | резолвер путей | `project_context.py` | неизвестный `engine` — ошибка, а не тихий threejs |
| Указатель на удалённый проект | да | резолвер | `test_project_context_reports_a_stale_pointer_*` | `pointer_stale` + отказ резолвить несуществующий путь |
| Потеря состояния задачи, повтор уже выполненного шага | да (`mutation_clears_counters`, `DUPLICATE_SUCCESS`) | рантайм | `SuccessLedger` | повтор удачного мутирующего вызова в том же поколении блокируется |
| Запись вне песочницы | да | инструмент | `checkPath` | мутация вне корня репозитория блокируется, `PATH_OUTSIDE_SANDBOX` |
| Слишком много инструментов / большие описания | не проверялось в этом заходе | клиент | — | не трогал: `mcp/registry.json` уже фильтрует по движку для pi; для WorkBuddy добавлен `--profile` |
| RAG «сломан» | не подтверждено | — | — | корпуса и retrieval не менялись |

Не подтверждено и не выдаётся за исправленное: вопросы к бюджету контекста/вывода и к
chat-template конкретной модели (§4.9 брифа). Для этого нужен замер на живой сессии —
раздел 7.

---

## 3. Что делает guard

### 3.1 Отпечаток вызова

`sha1` от стабильного JSON: `server`, `tool`, нормализованные аргументы (ключи
отсортированы на всех уровнях), контекст (активный проект + движок). Два вызова —
«один и тот же» только при равном отпечатке. Порядок ключей не важен: 9B чаще
переставляет ключи, чем меняет аргументы.

### 3.2 Что считается провалом

Только **неудачные** вызовы. Успешный `read` счётчик не двигает никогда — опрос,
пагинация и перечитывание файла после правки остаются законными.

| Класс | Порог повтора (`max_identical_failures`) |
|---|---|
| жёсткий: `FILE_NOT_FOUND`, `PERMISSION_DENIED`, `INVALID_ARGUMENT`, `PATH_OUTSIDE_SANDBOX`, `VALIDATION_FAILED` | 1 — первый же идентичный повтор блокируется |
| транзиентный: `TIMEOUT`, `SERVER_UNAVAILABLE`, `OUTPUT_TOO_LARGE` | 3 — ограниченный повтор разрешён |

Успешный **мутирующий** вызов (`write`/`edit`/`bash`/`powershell`) очищает счётчики:
мир мог измениться, и то, что падало, теперь может сработать по-настоящему. Окно цикла
при этом сохраняется — иначе «read падает → edit ок → read падает → edit ок» выживает.

### 3.3 Что возвращается модели

Не «нельзя», а контракт (`errorPayload`), в котором есть следующий шаг:

```json
{
  "ok": false,
  "error_code": "REPEATED_TOOL_CALL",
  "retryable": false,
  "operation": "read",
  "attempts": 1,
  "message": "this exact call to read has already failed 1x with FILE_NOT_FOUND, and nothing changed in between.",
  "next_action": "Do not repeat this call. Inspect the parent directory, verify the active project, search for the name, or change the arguments."
}
```

Для `FILE_NOT_FOUND` контракт дополняется фактической обстановкой на диске:
`nearest_existing_directory`, `entries` (до 25 имён), `did_you_mean`, `case_mismatch`.
Это два `syscall` и одна строчка, которая для 9B полезнее любого абзаца в промпте.

Ошибка сервера не подменяется: исходный текст остаётся первым, контракт дописывается
после. Клиент, который не понимает JSON, видит обычную ошибку.

### 3.4 Проверка записи

После `write`/`edit` с `isError: false` проверяется диск: файл существует, не пуст
(если писали непустое), размер совпадает с длиной `content` в UTF-8 (для `write`),
`mtime` свежий. Не сошлось — результат помечается ошибкой и получает
`WRITE_NOT_VERIFIED`. Шаг не считается выполненным.

### 3.5 Песочница

Мутация (`write`/`edit`) с путём вне корня репозитория блокируется. Внутри репозитория,
но вне активного проекта — разрешена и логируется: править `tools/`, `docs/`,
`pi-extensions/` — половина смысла этого репозитория.

### 3.6 Состояние задачи

Отдельного файла состояния нет: `loop-guard` пишет одну JSONL-строку на вызов, а
`gs reliability state` собирает из неё список шагов прогона. Второй файл с теми же
данными — это второе, что может разойтись. Чего достаточно, чтобы ответить «это уже
выполнялось?» и «что именно упало?» без доверия к пересказу модели.

---

## 4. Команды

```cmd
gs reliability                      :: политика + сводка последнего прогона
gs reliability state                :: шаги последнего прогона
gs reliability state --run pi-1234  :: конкретный прогон
gs reliability log --tail 40        :: события
gs reliability log --code FILE_NOT_FOUND
gs reliability classify "ENOENT: ..."   :: как guard назовёт эту ошибку
gs reliability verify <path>        :: проверка постусловия на одном файле
gs reliability selftest             :: регрессия самой политики (12 проверок)
gs reliability prune                :: ретенция логов (14 файлов)
```

`python tools/project_context.py [name] [--shell]` — резолвер проекта отдельно:

```cmd
.venv\Scripts\python.exe tools\project_context.py
{
  "repo": "...\\3GS_Master",
  "project": "...\\projects\\three\\test-space",
  "project_rel": "projects/three/test-space",
  "engine": "threejs",
  "engine_source": "projects/three/test-space/engine.json",
  "project_exists": true,
  "pointer_stale": false,
  "engine_ambiguous": null,
  "error": null
}
```

`--shell` печатает `set "GS_PROJECT=..."` / `set "GS_ENGINE=..."` для cmd; пустые
значения, если проекта нет. Код возврата 1 — указатель мёртв, движок неоднозначен или
явный аргумент никуда не резолвится.

---

## 5. WorkBuddy: что реально поддерживается

Проверено по установленному клиенту и по `mcp/registry.json`:

| Возможность | pi | WorkBuddy |
|---|---|---|
| Свой профиль на движок | да (`PI_CODING_AGENT_DIR`, `engine-gate.ts`) | нет — один `~/.workbuddy-ai/mcp.json` на все сессии |
| Хуки на вызов инструмента | да (`tool_call` / `tool_result`) | **нет** — расширения pi в WorkBuddy не выполняются |
| Переключение набора серверов в сессии | да (регистрация/снятие MCP) | нет — нужен reload |
| Генерация конфигурации из `mcp/registry.json` | да | да (`gs mcp-sync`) |

Отсюда: **loop guard и проверка записи в WorkBuddy не работают** — там нет точки
перехвата, и делать вид, что есть, нельзя. Что сделано вместо:

```cmd
gs mcp-sync --only workbuddy --profile threejs          :: dry run
gs mcp-sync --apply --only workbuddy --profile threejs  :: записать
gs mcp-sync --apply --only workbuddy --profile all      :: вернуть дефолт (флаги workbuddy.enabled)
```

Профиль не удаляет серверы, а выставляет `disabled: true` всем, чей движок не выбран
(`engines: ["any"]` — общий пайплайн ассетов — остаётся включённым всегда). Состояние
по-прежнему выводится из `mcp/registry.json`, руками `~/.workbuddy-ai/mcp.json` не
правится. После `--apply` **WorkBuddy нужно перезагрузить** (Settings → Connectors/MCP →
reload), иначе список инструментов останется прежним.

Матрица видимости (профиль `--profile <engine>`):

| Сервер | threejs | godot | unity | roblox | pi (по движку проекта) |
|---|---|---|---|---|---|
| `threejs-rag` | ✓ | – | – | – | threejs |
| `godot-rag` | – | ✓ | – | – | godot |
| `godot` (policy_gateway) | – | ✓ | – | – | godot |
| `unity-rag` | – | – | ✓ | – | unity |
| `unity-project` | – | – | ✓ | – | unity |
| `rbx-rag` | – | – | – | ✓ | roblox |
| `rbx-project` | – | – | – | ✓ | roblox |
| `roblox-studio` | – | – | – | ✓ | roblox |
| `assets` | ✓ | ✓ | ✓ | ✓ | все |

---

## 6. Регрессия

```cmd
gs test                        :: все тесты, включая tests\test_reliability.py
gs reliability selftest        :: только политика
node tests\reliability_parity.mjs   :: ответы TS-ядра (для отладки расхождений)
```

`tests/test_reliability.py` покрывает: совпадение файла политики и fallback'а,
совпадение констант с `write-guard.ts`, побайтовое совпадение классификации,
отпечатков и вердиктов guard'а между TS и Python, четыре случая `verify_write`,
форму контракта ошибки, наличие `next_action` у каждого кода, резолвер проекта
(наследование движка, неоднозначный маркер, мёртвый указатель, пустой указатель),
группировку лога в шаги и ретенцию.

Сценарии 1–6 и 8 из брифа покрыты этими тестами. Сценарий 7 (профиль WorkBuddy) —
`mcp_sync` в dry-run проверен вручную, тестом не закрыт. Сценарий 9 (совместимость
модели) — раздел 7.

---

## 7. Совместимость модели: что мерить

`tools/reliability.py` и `gs reliability` дают для этого готовые данные, но сам замер
делается на живой сессии:

```cmd
gs up                       :: llama.cpp router :8080
gs reliability state        :: после прогона: шаги, ошибки, блокировки
```

Смотреть в `state`: число `blocked` (сколько раз guard остановил цикл), распределение
`error_code` и есть ли `WRITE_NOT_VERIFIED`. Модель, у которой `blocked` растёт на
каждом шаге, не «нестабильна» — она не понимает сообщение guard'а; тогда правится
`next_action` в `mcp/reliability.json`, а не порог.

`mcp/reliability.json` — это тюнинг-поверхность. Менять там, а не в коде: обе
реализации читают один файл, и тест сверит их после изменения.

---

## 8. Ограничения

- **WorkBuddy без guard'ов.** Нет хуков — нет перехвата. Единственное, что там есть,
  это профиль серверов (`--profile`) и `AGENTS.md`.
- **Детектор циклов — эвристика на отпечатках.** Он не понимает смысла вызова. Если
  модель делает два разных вызова, которые оба бесполезны, цикл не будет назван —
  будет только накопление ошибок в логе.
- **`edit` проверяется слабее, чем `write`:** у `edit` нет полного payload'а, поэтому
  проверяются существование, непустота и свежесть `mtime`, а не байтовое совпадение.
- **Порог 1 для жёстких ошибок — сознательно агрессивный.** Для транзиентных он 3. Если
  на практике законный повтор блокируется, это видно в `gs reliability log` как
  `REPEATED_TOOL_CALL` там, где вы ждали успеха; тогда порог поднимается в политике.
- **Бюджет контекста/вывода не измерялся** в этом заходе. `write-guard.ts` (12000 байт /
  320 строк / 3 перезаписи) сохранён как был, его константы теперь продублированы в
  политике и сверяются тестом.
- **RAG не трогали.** Корпуса, chunking, reranker, гибридный поиск — как были.

---

## 9. Откат

Всё новое — отдельные файлы; ничего существующего не переписано, кроме трёх
однострочных правок.

```cmd
:: 1. выключить guard, не удаляя код
::    в mcp/reliability.json:  "loop_guard": { "enabled": false }, "write_verification": { "enabled": false }
gs reliability status

:: 2. убрать стабы из профилей (pi перестанет грузить расширение)
del pi-home-three\extensions\loop-guard.ts
del pi-home-godot\extensions\loop-guard.ts
del pi-home-unity\extensions\loop-guard.ts
del pi-home-roblox\extensions\loop-guard.ts

:: 3. вернуть дефолтный набор серверов WorkBuddy
gs mcp-sync --apply --only workbuddy --profile all
```

Удалять `logs/reliability/` не нужно — это логи, они не влияют на поведение.
`data/reliability/` в `.gitignore`, в git ничего не попадает.

Правки существующих файлов, которые придётся откатить вручную: `.gitignore`
(скелет `projects/`), `gs.cmd` (команда `reliability`), `cmd/test.cmd` (новый тест в
списке), `tools/mcp_sync.py` (`--profile`).
