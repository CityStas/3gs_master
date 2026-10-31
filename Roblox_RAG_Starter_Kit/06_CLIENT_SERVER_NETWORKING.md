# Client-Server Networking and Remote Security

## 1. Server authority

Roblox experiences use a client-server model. The server is the authority for shared game state. Clients handle local input, camera and responsive presentation, but client claims must not be trusted for important state changes.

Official references:

- https://create.roblox.com/docs/projects/client-server
- https://create.roblox.com/docs/scripting/events/remote
- https://create.roblox.com/docs/scripting/security/client-server-boundary
- https://create.roblox.com/docs/scripting/security/security-tactics

## 2. Remote communication types

- `RemoteEvent`: asynchronous one-way communication; does not yield for a response.
- `RemoteFunction`: request/response communication; caller yields until the response is returned. Avoid using it in latency-sensitive or high-frequency flows without a clear reason.
- `UnreliableRemoteEvent`: one-way communication for continuously changing or non-critical data where ordering/reliability can be traded for performance.
- `BindableEvent` / `BindableFunction`: communication within the same execution side; they do not cross the client-server boundary.

Remote instances are commonly stored in `ReplicatedStorage` so both sides can access them. The server must still validate every client request.

## 3. Secure remote pattern

A client should send an intent/request, not the final authoritative result. For example, ask to buy an item by a known item ID; the server looks up the price and checks eligibility itself.

Client example:

```lua
-- LocalScript
local ReplicatedStorage = game:GetService("ReplicatedStorage")
local BuyItem = ReplicatedStorage.Remotes:WaitForChild("BuyItem")

BuyItem:FireServer("health_potion")
```

Server example:

```lua
--!strict
-- Script in ServerScriptService
local ReplicatedStorage = game:GetService("ReplicatedStorage")
local BuyItem = ReplicatedStorage.Remotes:WaitForChild("BuyItem") :: RemoteEvent

local catalog = {
    health_potion = { price = 25 },
}

local lastRequestAt: {[number]: number} = {}
local COOLDOWN = 0.25

BuyItem.OnServerEvent:Connect(function(player: Player, itemId: unknown)
    -- 1. Validate input type and shape.
    if typeof(itemId) ~= "string" or #itemId > 40 then
        return
    end

    -- 2. Rate-limit on the server.
    local now = os.clock()
    local previous = lastRequestAt[player.UserId] or 0
    if now - previous < COOLDOWN then
        return
    end
    lastRequestAt[player.UserId] = now

    -- 3. Resolve authoritative item data on the server.
    local item = catalog[itemId]
    if not item then
        return
    end

    -- 4. Check server-owned currency, inventory capacity, game state,
    --    distance/permissions if applicable, then commit the purchase.
end)
```

This is a conceptual pattern, not a complete production shop. Add persistence, transaction handling, logging and cleanup as required.

## 4. Mandatory validation layers

For every client-originated action, consider:

1. **Type and shape:** expected types, bounded string lengths, table depth/size, allowed keys, numeric ranges, finite numbers.
2. **Permission:** is this player allowed to perform this action?
3. **Context:** alive, in the correct round, close enough, has the required tool/item, target exists?
4. **Rate limit:** per-player server-side limits; client cooldown is only UX and is not a security control.
5. **Authoritative calculation:** server calculates cost, damage, reward, cooldown and result.
6. **State transition:** reject impossible or duplicate transitions.
7. **Observability:** log suspicious/high-value actions without leaking secrets.

Assume exploiters can fire remotes with arbitrary arguments and frequency, alter their local DataModel, manipulate character movement and claim client-side events happened. See Roblox security tactics.

## 5. Network ownership and physics

Network ownership can allow clients to simulate physics for assemblies. Do not rely only on client-reported position or touch events for high-value actions. For critical interactions, validate distance and state server-side; understand the network ownership of unanchored assemblies.

## 6. Latency and reliability

Test with realistic inbound/outbound latency, jitter and packet loss. Do not assume Studio's default no-latency test represents live conditions. Keep high-frequency cosmetic updates separate from important authoritative state.

## 7. Anti-patterns

- Client tells server: "give me 1000 coins" and server accepts it.
- Client sends a price; server trusts it.
- Client reports a hit, reward, or item drop without server verification.
- Remote is callable without rate limiting.
- A `RemoteFunction` is used for a continuous stream or high-frequency loop.
- Secrets or server-only logic are stored in replicated containers.
