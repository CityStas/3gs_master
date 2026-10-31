---
name: roblox-datastore
description: "Roblox persistence: DataStoreService, UpdateAsync vs SetAsync, session locking, retries and budgets, schema versioning and migration, MemoryStoreService, MessagingService, Open Cloud. Use when saving player data or when a save silently fails. Русские триггеры: «datastore», «сохранение данных», «сейв», «прогресс игрока», «UpdateAsync», «лимиты», «потеря данных»."
---

# Persistence

## The rules that cause data loss

1. **`DataStoreService` is server-only.** In a `LocalScript` it errors immediately.
2. **Every call can fail.** `pcall` is mandatory; a failed save is not an exception you can
   ignore, it is a player's progress.
3. **`UpdateAsync`, not `SetAsync`,** whenever the new value depends on the old one - a
   session lock, a currency delta, a "read, modify, write" of any kind. `SetAsync` is a
   blind overwrite and loses concurrent writes.
4. **Requests are budgeted.** ~60 + 10 × players per minute for reads, 60 + 10 × players
   for writes, shared per key. A per-player `DataStore` call every frame is how a game gets
   throttled and starts silently dropping saves.
5. **The value must be serializable**: no Instances, no functions, no mixed-key tables with
   a nil hole. Numbers, strings, booleans, and tables of those.

## Load and save

```lua
--!strict
local DataStoreService = game:GetService("DataStoreService")
local store = DataStoreService:GetDataStore("PlayerData_v2")

local DEFAULT = {
    version = 2,
    coins = 0,
    inventory = {},
}

local function retry<T>(fn: () -> T, attempts: number): (boolean, T?)
    for i = 1, attempts do
        local ok, result = pcall(fn)
        if ok then return true, result end
        if i < attempts then
            task.wait(2 ^ i)              -- 2, 4, 8 s: never a tight retry loop
        end
    end
    return false, nil
end

local function load(player: Player): any
    local key = `player_{player.UserId}`
    local ok, data = retry(function()
        return store:GetAsync(key)
    end, 3)
    if not ok then
        warn(`load failed for {player.Name}: the session runs on defaults, saving is blocked`)
        return nil                          -- nil means "do not save over the real data"
    end
    return data or table.clone(DEFAULT)
end

local function save(player: Player, data: any): boolean
    local key = `player_{player.UserId}`
    local ok = retry(function()
        return store:UpdateAsync(key, function(old)
            return data                      -- the lock is released by writing
        end)
    end, 3)
    if not ok then
        warn(`SAVE FAILED for {player.Name} ({key}) - retry on the next autosave`)
    end
    return ok
end
```

`GetAsync` returning `nil` is a **new player**, not an error. A *failed* `GetAsync` must
not become "new player" - that is how a returning player gets reset. Keep the two apart,
as above: `nil` from a successful call means default data, `not ok` means "do not save".

## Session locking (two servers, one player)

A player can join server A, leave, and join server B while A is still saving. Without a
lock, B loads stale data and overwrites A's save. The minimal lock is a value inside the
record:

```lua
local function acquire(key: string, jobId: string): boolean
    local ok, acquired = pcall(function()
        return store:UpdateAsync(key, function(old)
            old = old or table.clone(DEFAULT)
            local lock = old.lock
            local stale = not lock or (os.time() - (lock.at or 0)) > 60
            if lock and lock.job ~= jobId and not stale then
                return nil                  -- returning nil aborts the write: someone holds it
            end
            old.lock = { job = jobId, at = os.time() }
            return old
        end)
    end)
    return ok and acquired ~= nil
end
```

Release the lock in `PlayerRemoving` **and** in `BindToClose`, and always release it before
the final save. `game:BindToClose` gives ~30 s; a save that takes longer than that is lost.

```lua
game:BindToClose(function()
    local pending = 0
    for _, player in Players:GetPlayers() do
        pending += 1
        task.spawn(function()
            save(player, sessions[player])
            pending -= 1
        end)
    end
    local deadline = os.clock() + 25
    while pending > 0 and os.clock() < deadline do
        task.wait(0.1)
    end
end)
```

## Schema versioning

Store `version` in the record and migrate on load, never on save:

```lua
local MIGRATIONS = {
    [1] = function(data)
        data.coins = data.money or 0
        data.money = nil
        data.version = 2
        return data
    end,
}

local function migrate(data)
    while (data.version or 1) < DEFAULT.version do
        local step = MIGRATIONS[data.version or 1]
        if not step then break end
        data = step(data)
    end
    return data
end
```

## Cross-server and cross-service

| Need | Service |
|---|---|
| Shared temporary state (matchmaking queue, live counters) | `MemoryStoreService` (TTL, no permanent storage) |
| Broadcast between servers ("server restarted", "event started") | `MessagingService` (best effort, ≤ 1 KB, not ordered) |
| Read/write from outside a running experience | Open Cloud (`cloud_docs` corpus) with an API key |
| Ordered leaderboard across servers | `OrderedDataStore` + a periodic refresh, not a per-frame query |

## Budget and failure symptoms

| Symptom | Meaning |
|---|---|
| "DataStore request was added to queue" | over budget; the call is throttled, and if the queue overflows it is **dropped** |
| "Cannot store dictionary in data store" | a non-serializable value (Instance, mixed table) |
| data resets for some players | a failed `GetAsync` was treated as "new player" |
| the same player's progress jumps backwards | two servers, no session lock |
| nothing saves in Studio | `DataStore` works in Studio only with API access enabled, and never in a local `.rbxl` without a published place |
