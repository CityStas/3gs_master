# Knowledge Map — Roblox Development

## Цель

Эта карта помогает RAG-агенту определить, какие документы и источники нужны для ответа. В первую очередь ищите по официальным названиям классов, методов, событий и свойств.

## Домены знаний

### A. Roblox Platform
Ключевые темы: experience, universe, place, Creator Dashboard, publishing, permissions, DataModel, Instance, hierarchy, replication.

Основные документы: `02_ROBLOX_PLATFORM.md`, `03_ROBLOX_STUDIO.md`.

### B. Luau
Ключевые темы: syntax, variables, functions, tables, metatables, iteration, type annotations, strict mode, generics, type refinement, coroutines, task library, standard libraries, compatibility with Lua 5.1.

Основной документ: `04_LUAU_LANGUAGE.md`.

### C. Roblox Engine API
Ключевые темы: classes, services, datatypes, enums, properties, methods, events, callbacks, security tags, thread safety, replication behavior.

Основной источник: Engine API Reference — https://create.roblox.com/docs/reference/engine.

### D. Game scripting architecture
Ключевые темы: Script, LocalScript, ModuleScript, ServerScriptService, ServerStorage, ReplicatedStorage, StarterPlayer, StarterGui, Workspace, lifecycle, module boundaries, dependency management.

Основной документ: `05_SCRIPTING_ARCHITECTURE.md`.

### E. Client-server networking
Ключевые темы: server authority, client prediction, replication, RemoteEvent, RemoteFunction, UnreliableRemoteEvent, BindableEvent, network ownership, latency, exploit mitigation, rate limiting.

Основной документ: `06_CLIENT_SERVER_NETWORKING.md`.

### F. Persistence and cloud
Ключевые темы: DataStoreService, UpdateAsync, MemoryStoreService, MessagingService, Open Cloud, API keys, OAuth, webhooks, HttpService, retries, budgets, serialization.

Основной документ: `07_DATA_PERSISTENCE_CLOUD.md`.

### G. Gameplay systems
Ключевые темы: UI, ScreenGui, PlayerGui, ContextActionService, UserInputService, ProximityPrompt, Humanoid, Animator, PathfindingService, PhysicsService, constraints, audio, assets.

Основной документ: `08_GAMEPLAY_SYSTEMS.md`.

### H. Quality, safety and production
Ключевые темы: Studio test modes, Server & Clients, device simulation, network simulation, profiling, microprofiler, memory, performance, security, moderation, publishing, monetization.

Основной документ: `09_TESTING_SECURITY_PERFORMANCE.md`.

### I. AI tooling and MCP
Ключевые темы: Model Context Protocol, Roblox Studio MCP, stdio, tools, studio_id, script_read, multi_edit, execute_luau, playtesting, asset search/insert.

Основной документ: `10_MCP_SETUP_WINDOWS.md`.

## Retrieval routing

| Тип вопроса | Что искать в первую очередь |
|---|---|
| «Как написать скрипт…» | Luau + Engine API + scripting architecture |
| «Почему скрипт не работает?» | Luau + API class/member + Output/debugging + script placement |
| «Как сделать multiplayer…» | client-server + remotes + security + testing modes |
| «Как сохранить данные игрока?» | DataStoreService + persistence + security + budgets |
| «Как исправить лаги?» | performance docs + конкретные API (physics, rendering, networking) |
| «Как создать UI/инвентарь/магазин?» | UI + input + remotes + server validation + persistence + monetization |
| «Как агенту изменить игру в Studio?» | MCP setup + MCP tools + текущая структура проекта |
| «Что делает API X?» | Engine API Reference по точному имени `X` прежде всего |
| «Какой API сейчас правильный?» | только актуальный официальный источник; не полагаться на старые community answers |

## Правила точности

- Всегда различайте Roblox Luau и стандартный Lua.
- Не придумывайте API members. Если метод/свойство не найдено в Engine API Reference, прямо обозначьте это.
- Учитывайте место исполнения: server, client или shared/replicated.
- Учитывайте контекст DataModel: одинаковое имя объекта в разных контейнерах не означает одинаковую доступность.
- Не переносите правила из Unity, Unreal или обычного Lua в Roblox без проверки.
- Для важных изменений в проекте сначала изучите существующую структуру и соглашения проекта.
