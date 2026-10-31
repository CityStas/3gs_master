# Roblox Development Knowledge Base — RAG Starter Kit

**Назначение:** стартовый корпус знаний для AI-агента, который помогает разрабатывать Roblox experiences: проектировать игровые системы, писать и ревьюить Luau, работать в Roblox Studio, отлаживать, тестировать и пользоваться Roblox API.

**Язык корпуса:** русский текст + оригинальные английские названия API, классов, свойств, событий и терминов. Это намеренно: точные идентификаторы Roblox API лучше сохранять без перевода.

**Статус:** curated starter corpus, а не полная копия Creator Hub. Официальная документация меняется; перед генерацией кода агент обязан сверять актуальные API и поведение с первоисточником.

## Содержимое

| Файл | Назначение |
|---|---|
| `00_KB_MAP.md` | Карта тем, терминология и маршрутизация запросов |
| `01_SOURCE_CATALOG.md` | Каталог первичных и дополнительных источников |
| `02_ROBLOX_PLATFORM.md` | Платформа, experiences, places, DataModel, Instances, services |
| `03_ROBLOX_STUDIO.md` | Интерфейс Studio и рабочий процесс |
| `04_LUAU_LANGUAGE.md` | Язык Luau, отличия от Lua, типизация, примеры |
| `05_SCRIPTING_ARCHITECTURE.md` | Script, LocalScript, ModuleScript, service containers, lifecycle |
| `06_CLIENT_SERVER_NETWORKING.md` | Клиент-сервер, репликация, remotes, безопасность сетевых запросов |
| `07_DATA_PERSISTENCE_CLOUD.md` | DataStoreService, MemoryStoreService, MessagingService, Open Cloud |
| `08_GAMEPLAY_SYSTEMS.md` | UI, input, physics, characters, NPC, animation, audio, assets |
| `09_TESTING_SECURITY_PERFORMANCE.md` | Тестирование, защита от эксплойтов, оптимизация, публикация |
| `10_MCP_SETUP_WINDOWS.md` | Подключение официального Roblox Studio MCP на Windows |
| `11_RAG_INGESTION.md` | Как индексировать официальные документы и этот корпус |
| `12_AGENT_SYSTEM_RULES.md` | Системные правила для AI-агента-разработчика Roblox |
| `13_GLOSSARY.md` | Глоссарий Roblox/Luau |
| `14_UPDATE_POLICY.md` | Обновление базы и контроль устаревших сведений |

## Быстрый старт

1. Скопируйте папку в хранилище знаний вашего RAG-приложения.
2. Сначала проиндексируйте `00_KB_MAP.md`, `01_SOURCE_CATALOG.md`, `12_AGENT_SYSTEM_RULES.md` и `13_GLOSSARY.md`.
3. Затем загрузите тематические файлы `02`–`09`.
4. Добавьте официальную документацию как отдельный источник, используя `https://create.roblox.com/docs/llms.txt`, `https://create.roblox.com/docs/reference/engine/llms.txt` и `https://create.roblox.com/docs/cloud/llms.txt`.
5. Настройте hybrid retrieval: семантический поиск + полнотекстовый/лексический поиск. Для запросов по `RemoteEvent`, `DataStoreService`, `Humanoid`, `CFrame` и другим точным идентификаторам лексический поиск особенно важен.
6. Подключите официальный Roblox Studio MCP по инструкции в `10_MCP_SETUP_WINDOWS.md`.

## Важное разграничение

- **RAG** отвечает за поиск знаний и ссылок на документацию.
- **Roblox Studio MCP** даёт агенту доступ к открытому проекту Studio: осмотр DataModel, чтение/изменение скриптов, выполнение Luau и playtesting.
- **Rojo / Git / Rokit / Wally** — инструменты файлового workflow и управления проектом; сами по себе они не заменяют RAG и не являются необходимыми для первого запуска Studio MCP.

Не смешивайте содержимое проекта пользователя и общую документацию: храните их в разных коллекциях/namespace, чтобы агент не выдавал детали одного проекта за универсальное правило Roblox.

## Приоритет источников

1. Официальные Roblox Creator Hub docs и Engine API Reference.
2. Официальные репозитории Roblox (например, Luau и creator-docs).
3. Документация поддерживаемых инструментов (Rojo, Rokit, Wally и т. п.).
4. DevForum и community-репозитории — только как дополнительный опыт, а не как окончательная истина.

## Версия и актуальность

Дата подготовки стартового набора: **2026-10-31**. В метаданных чанков сохраняйте `source_last_checked` и `ingested_at`. Для быстро меняющихся API проверяйте первоисточник перед ответом.
