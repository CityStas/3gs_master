# Source Catalog — Roblox / Studio / Luau

Используйте этот файл как allowlist источников для загрузчика RAG. Для динамических разделов сохраняйте URL страницы, дату загрузки и контрольную сумму.

## 1. Официальные источники Roblox — highest trust

### Главные индексы для AI/агентных загрузчиков

- Creator documentation index: https://create.roblox.com/docs/llms.txt
- Engine API index: https://create.roblox.com/docs/reference/engine/llms.txt
- Cloud API index: https://create.roblox.com/docs/cloud/llms.txt
- Creator Hub home: https://create.roblox.com/docs

Документация Roblox предоставляет страницы в Markdown-виде. На страницах с пометкой `For Agents` обычно доступна ссылка на `.md`-версию. По возможности забирайте Markdown-страницу, а не HTML.

### Platform / Studio / Projects

- Studio overview: https://create.roblox.com/docs/studio
- Studio setup: https://create.roblox.com/docs/studio/setup
- Studio interface: https://create.roblox.com/docs/studio/interface
- Data model: https://create.roblox.com/docs/projects/data-model
- Client-server runtime: https://create.roblox.com/docs/projects/client-server
- Third-party tools / file-based workflow: https://create.roblox.com/docs/projects/external-tools
- Studio CLI: https://create.roblox.com/docs/studio/cli
- Studio MCP: https://create.roblox.com/docs/studio/mcp
- Studio testing modes: https://create.roblox.com/docs/studio/testing-modes
- Developer Console: https://create.roblox.com/docs/studio/developer-console

### Luau

- Roblox Luau overview: https://create.roblox.com/docs/luau
- Luau language docs: https://luau.org/
- Luau syntax: https://luau.org/syntax/
- Luau types: https://luau.org/types/
- Luau compatibility: https://luau.org/compatibility/
- Luau standard library: https://luau.org/library/
- Luau GitHub repository: https://github.com/luau-lang/luau
- Lua 5.1 reference (for historical comparison only): https://www.lua.org/manual/5.1/

### Engine API

- Engine API Reference: https://create.roblox.com/docs/reference/engine
- Engine API LLM index: https://create.roblox.com/docs/reference/engine/llms.txt
- Class pages are addressable by their official Creator Hub reference paths. Search the API index for exact class/property/method names.

### Scripting / networking / security

- Scripting overview: https://create.roblox.com/docs/scripting
- Script types and locations / RunContext: https://create.roblox.com/docs/scripting/locations
- Services: https://create.roblox.com/docs/scripting/services
- Remote events and callbacks: https://create.roblox.com/docs/scripting/events/remote
- Securing the client-server boundary: https://create.roblox.com/docs/scripting/security/client-server-boundary
- Security tactics: https://create.roblox.com/docs/scripting/security/security-tactics

### Data / cloud

- Data stores: https://create.roblox.com/docs/cloud-services/data-stores
- Memory stores: https://create.roblox.com/docs/cloud-services/memory-stores
- Messaging service: https://create.roblox.com/docs/cloud-services/messaging-service
- Open Cloud: https://create.roblox.com/docs/cloud
- Open Cloud API reference: https://create.roblox.com/docs/cloud/reference
- OpenAPI description: https://create.roblox.com/docs/cloud/reference/openapi

### Performance / monetization / assets

- Performance optimization: https://create.roblox.com/docs/performance-optimization
- Pathfinding: https://create.roblox.com/docs/characters/pathfinding
- Animation: https://create.roblox.com/docs/animation
- Animation usage: https://create.roblox.com/docs/animation/using
- Physics: https://create.roblox.com/docs/physics
- Raycasting: https://create.roblox.com/docs/workspace/raycasting
- Collision filtering: https://create.roblox.com/docs/workspace/collisions
- Asset management: https://create.roblox.com/docs/projects/assets
- Monetization: https://create.roblox.com/docs/production/monetization
- Passes: https://create.roblox.com/docs/production/monetization/passes

## 2. Official/community tooling — trusted for its own tool

Roblox itself notes that many external workflow tools are not maintained by Roblox and may change. Pin versions and review release notes.

- Rojo: https://rojo.space/docs/
- Rojo GitHub: https://github.com/rojo-rbx/rojo
- Rokit: https://github.com/rojo-rbx/rokit
- Wally: https://github.com/UpliftGames/wally
- Lune: https://lune-org.github.io/docs/
- StyLua: https://github.com/JohnnyMorganz/StyLua
- Selene: https://github.com/Kampfkarren/selene

## 3. Roblox DevForum — secondary / community evidence

- DevForum: https://devforum.roblox.com/

Use for real-world bugs, migration notes, edge cases, and community practice. Never treat a forum answer as stronger than a current official API reference. Store author, post date, accepted/official status if available, and thread URL.

## 4. Source metadata schema

Attach these fields to every document or chunk:

```json
{
  "source_id": "roblox_docs_client_server",
  "source_title": "Client-server runtime",
  "source_url": "https://create.roblox.com/docs/projects/client-server",
  "source_type": "official_documentation",
  "publisher": "Roblox",
  "trust_level": "primary",
  "language": "en",
  "topic": ["networking", "architecture", "replication"],
  "retrieved_at": "YYYY-MM-DD",
  "source_last_modified": null,
  "version_scope": "current Roblox platform; verify before use",
  "content_hash": "sha256:..."
}
```

## 5. Source conflict policy

If sources conflict, prefer in this order:

1. Current Engine API Reference and current Creator Hub docs.
2. Current official Roblox announcements/release notes.
3. Official Roblox GitHub repositories.
4. Maintainer docs for third-party tools.
5. Recent DevForum posts with reproducible evidence.
6. Older tutorials, videos, blogs, answers, and copied snippets.

Do not silently merge incompatible answers. Explain the conflict and show the source dates/versions.
