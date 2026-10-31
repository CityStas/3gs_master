---
name: roblox-networking
description: "Roblox client-server networking: RemoteEvent vs RemoteFunction vs UnreliableRemoteEvent vs BindableEvent, server-side validation, rate limiting, replication, network ownership, payload design. Use when building multiplayer features or when a remote does not fire / is exploitable. Русские триггеры: «remoteevent», «remote», «клиент-сервер», «сеть», «синхронизация», «эксплойт», «читер», «валидация»."
---

# Networking

## Pick the right object

| Object | Direction | Yields | Use |
|---|---|---|---|
| `RemoteEvent` | both | no | one-way notifications: input, hits, "bought" |
| `RemoteFunction` | client → server | **yes** | a client asking a question that needs an answer |
| `UnreliableRemoteEvent` | both | no | high-frequency, loss-tolerant state (positions, aim) |
| `BindableEvent` | same side only | no | decoupling modules inside one machine |
| `Attribute` / `Value` | replicated | no | small state the client must read (`Health`, `Team`) |

Never `RemoteFunction` **server → client**: it yields the server thread until the client
answers, and a client that never answers (or is not there) hangs that thread. Use two
`RemoteEvent`s instead.

## The shape of a safe remote

```lua
-- ReplicatedStorage/Shared/Remotes.luau
local ReplicatedStorage = game:GetService("ReplicatedStorage")
local Remotes = ReplicatedStorage:FindFirstChild("Remotes")
if not Remotes then
    Remotes = Instance.new("Folder")
    Remotes.Name = "Remotes"
    Remotes.Parent = ReplicatedStorage
end

local function get(name: string, className: string): Instance
    local existing = Remotes:FindFirstChild(name)
    if existing then return existing end
    local remote = Instance.new(className)
    remote.Name = name
    remote.Parent = Remotes
    return remote
end

return {
    Purchase = get("Purchase", "RemoteEvent"),
    GetInventory = get("GetInventory", "RemoteFunction"),
}
```

```lua
-- ServerScriptService/Bootstrap.server.luau (excerpt)
local Purchase = Remotes.Purchase
local RATE_LIMIT = 4        -- requests per second per player
local buckets: { [Player]: { count: number, reset: number } } = {}

Purchase.OnServerEvent:Connect(function(player: Player, itemId: unknown)
    -- 1. type and shape
    if type(itemId) ~= "string" or #itemId > 64 then return end

    -- 2. rate
    local now = os.clock()
    local bucket = buckets[player]
    if not bucket or now >= bucket.reset then
        bucket = { count = 0, reset = now + 1 }
        buckets[player] = bucket
    end
    bucket.count += 1
    if bucket.count > RATE_LIMIT then return end

    -- 3. state: does the player exist, is the shop open, can they afford it
    local character = player.Character
    if not character or not character:FindFirstChild("HumanoidRootPart") then return end

    -- 4. authority: the price comes from the SERVER table, never from the client
    local item = ShopConfig[itemId]
    if not item then return end
    if not Inventory:canPay(player, item.price) then return end

    Inventory:charge(player, item.price)
    Inventory:grant(player, itemId)
end)

game:GetService("Players").PlayerRemoving:Connect(function(player)
    buckets[player] = nil          -- otherwise the table leaks every player who ever joined
end)
```

## Validation checklist

Every remote handler answers all of these before touching state:

1. **Type**: `type(x)`, `typeof(x)` for Instances. A client can send a table, a
   `userdata`, or 40 KB of nested tables.
2. **Range**: index, distance, direction, price, count. `0 < n and n <= 99`.
3. **Identity**: is this instance actually the player's? `part:IsDescendantOf(character)`.
4. **State**: is the round running, is the shop open, is the player alive.
5. **Rate**: a per-player bucket, not a global counter.
6. **Ownership**: does the server agree that this player owns this thing. Never trust
   `player.UserId`-adjacent claims carried in the payload - take the player from the event
   argument, which the engine fills in.

## Payload design

- Send ids and small numbers; let the server look up the rest. A client that sends
  `{itemId, price}` is telling the server what to charge.
- Strings are cheap, tables of Instances are not - Instances serialize by reference and
  only work if they replicate.
- High-frequency data (60/s aim direction) goes on `UnreliableRemoteEvent`; a dropped packet
  is cheaper than a queued one.
- `RemoteEvent:FireAllClients` for everyone, `FireClient` for one, `FireAllClientsExcept`
  where the API provides it. `FireServer` only from the client.

## Network ownership

`BasePart:SetNetworkOwner(player)` hands physics simulation to that client. The owner's
position is then *approximately* authoritative - which is why a client-reported hit
position is a hint, not a fact. For anything that matters (damage, capture, score) the
server re-checks with its own raycast or distance test.

## Symptoms and causes

| Symptom | Cause |
|---|---|
| "Remote event invocation discarded" | the remote was fired before the client replicated it, or the name does not match |
| handler never runs on the server | the event is a `RemoteEvent` in `ReplicatedStorage` but the script that connects is a `LocalScript` |
| "attempt to call a nil value" in the handler | `RemoteEvent.OnServerEvent` connected with `.` instead of `:` |
| the server thread freezes | `RemoteFunction:InvokeClient` from the server |
| exploiters spam the shop | no rate limit; validation only in the client UI |
