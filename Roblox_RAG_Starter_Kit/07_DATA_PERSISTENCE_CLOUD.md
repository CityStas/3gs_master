# Persistence, Cloud Services and Open Cloud

## 1. Service selection

| Need | Common Roblox service | Nature |
|---|---|---|
| Persistent player progress/inventory | `DataStoreService` | Durable across sessions |
| Temporary high-throughput shared data | `MemoryStoreService` | Ephemeral / short-lived |
| Messaging across live servers | `MessagingService` | Pub/sub-style server messaging |
| External management/automation | Open Cloud APIs | HTTP APIs with keys or OAuth |

Always check current limits, quotas, request budgets and API availability in current docs.

Official references:

- Data stores: https://create.roblox.com/docs/cloud-services/data-stores
- Memory stores: https://create.roblox.com/docs/cloud-services/memory-stores
- Messaging service: https://create.roblox.com/docs/cloud-services/messaging-service
- Open Cloud: https://create.roblox.com/docs/cloud

## 2. DataStoreService

DataStoreService stores data across sessions. A data store is accessed by a name and key. Common data includes player progress, inventory and currency. It is accessed from server-side scripts, not LocalScripts.

Important practices:

- Wrap network-backed operations in `pcall` and handle failure.
- Prefer `UpdateAsync()` when the update must be based on the current stored value and avoid simple read-modify-write races.
- Keep payloads serializable and bounded.
- Validate loaded data as untrusted input; old schemas and corrupted records can exist.
- Add a schema version and migration path for long-lived player data.
- Avoid saving every frame or every tiny state change.
- Design for retries, throttling, player leave and server shutdown.
- Never test against production data accidentally.

Example:

```lua
local DataStoreService = game:GetService("DataStoreService")
local PlayerStore = DataStoreService:GetDataStore("PlayerData_v1")

local function loadPlayerData(userId: number)
    local key = "Player_" .. userId
    local ok, data = pcall(function()
        return PlayerStore:GetAsync(key)
    end)

    if not ok then
        warn("Data load failed:", data)
        return nil
    end

    return data
end
```

This is intentionally a minimal example; production systems need defaults, schema validation, retry/backoff strategy, write coordination and failure policies.

### UpdateAsync pattern

```lua
local ok, updated = pcall(function()
    return PlayerStore:UpdateAsync("Player_" .. userId, function(oldData)
        local data = if typeof(oldData) == "table" then oldData else {}
        data.Coins = if typeof(data.Coins) == "number" then data.Coins else 0
        data.SchemaVersion = 1
        return data
    end)
end)
```

The `UpdateAsync` callback must not yield. Keep it deterministic and short. Consult current API docs for callback semantics and limitations.

## 3. Studio testing warning

Roblox documents that enabling Studio API access can cause Studio to read/write the same DataStores as the live client. Use a separate test experience or test data store configuration. Never casually enable API access on a production place.

## 4. MemoryStoreService and MessagingService

Use MemoryStore for short-lived, frequently updated data such as matchmaking queues or temporary cross-server state. Use MessagingService to communicate messages between live servers. Neither is a substitute for durable player persistence.

## 5. Open Cloud

Open Cloud provides REST APIs for managing Roblox resources externally. Prefer API key or OAuth 2.0 authentication where supported; avoid cookie-based legacy APIs for production integrations. Keep API keys in environment variables/secret storage, never in client scripts, public repositories or RAG documents.

Possible automation use cases include data store access, game management, user-related operations and creator workflow integrations, subject to the scopes and permissions of the selected API.

## 6. RAG guidance

Index DataStore documentation by individual operation (`GetAsync`, `SetAsync`, `UpdateAsync`, `IncrementAsync`, `RemoveAsync`, budgets, limits and errors) so retrieval returns the relevant contract and caveats. Do not rely on a generic paragraph when answering data-loss or concurrency questions.
