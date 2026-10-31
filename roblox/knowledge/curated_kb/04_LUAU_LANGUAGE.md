# Luau Language Reference — Practical Starter

## 1. Luau, not generic Lua

Roblox Studio scripts use **Luau**, a fast, gradually typed language derived from Lua 5.1. Luau preserves much Lua syntax but adds features and Roblox-specific runtime APIs. A plain Lua tutorial is useful for fundamentals, but code from it may not cover Roblox Instances, services, replication, engine datatypes or Luau extensions.

Official references:

- https://create.roblox.com/docs/luau
- https://luau.org/
- https://luau.org/compatibility/

## 2. Variables and scope

Use `local` for nearly all variables and helper functions. Avoid accidental globals.

```lua
local coins = 100
local playerName = "PlayerOne"

local function addCoins(current: number, amount: number): number
    return current + amount
end

coins = addCoins(coins, 25)
```

## 3. Primitive values and tables

Core values include `nil`, booleans, numbers, strings, functions and tables. Tables are used for array-like sequences, dictionaries and structured records.

```lua
local inventory = { "Sword", "Potion", "Key" }
local playerData = {
    Coins = 100,
    Level = 3,
    Inventory = inventory,
}

for index, itemName in ipairs(inventory) do
    print(index, itemName)
end

for key, value in pairs(playerData) do
    print(key, value)
end
```

Use `ipairs` for ordered sequence traversal and `pairs` for key-value traversal. Do not assume dictionary iteration order.

## 4. Functions and control flow

```lua
local function canPurchase(coins: number, price: number): boolean
    if price <= 0 then
        return false
    end

    return coins >= price
end
```

Use early returns to keep validation code readable. Handle `nil` explicitly where an object might not exist.

## 5. Type annotations and strict mode

Luau supports gradual typing. A script can opt into stricter type checking with a directive such as:

```lua
--!strict

 type ItemData = {
    Id: string,
    Price: number,
    Stackable: boolean,
 }

local item: ItemData = {
    Id = "health_potion",
    Price = 25,
    Stackable = true,
}
```

Common directives include `--!strict`, `--!nonstrict` and `--!nocheck`. Prefer `--!strict` for new reusable systems when feasible, while respecting the existing project's conventions.

Type annotations improve static analysis but do not replace runtime validation of network input or persisted data.

Official type docs: https://create.roblox.com/docs/luau/type-checking and https://luau.org/types/

## 6. Roblox-specific runtime patterns

```lua
local Players = game:GetService("Players")

Players.PlayerAdded:Connect(function(player: Player)
    print("Joined:", player.Name, player.UserId)
end)
```

`game`, `workspace`, `script`, `Instance`, `task`, Roblox services and engine datatypes are part of the Roblox runtime environment. They are not interchangeable with standard Lua globals or libraries.

## 7. Asynchronous work and scheduling

Use the `task` library for scheduling work (`task.wait`, `task.delay`, `task.spawn`, `task.defer`) and understand whether a call yields. Do not create unbounded loops or spawn a task every frame without a clear reason. Prefer event-driven behavior over polling.

```lua
task.delay(2, function()
    print("Two seconds elapsed")
end)
```

For frame-step logic, consult `RunService` documentation and choose the event appropriate to the simulation phase. Do not guess whether a callback runs before or after physics.

## 8. Object-oriented patterns

Luau tables and metatables can implement object-style APIs. Roblox Instances themselves are engine objects with classes, properties, methods and events. Do not confuse a custom table-based class with an engine Instance.

## 9. Error handling

Operations that can fail should be checked. For external/network/persistence calls, use `pcall` or the API's documented error/result pattern, then retry only where safe and bounded.

```lua
local ok, result = pcall(function()
    return someFunctionThatMayFail()
end)

if not ok then
    warn("Operation failed:", result)
    return
end
```

## 10. Luau coding conventions

- Keep identifiers descriptive and consistent with the project.
- Prefer `local` and small functions with a single responsibility.
- Separate data/configuration from behavior where it improves maintainability.
- Use types for stable data structures and public module interfaces.
- Avoid giant monolithic scripts.
- Avoid deprecated APIs; verify status in the current Engine API Reference.
- Do not invent `wait()`/legacy patterns when the `task` library or specific engine signal is appropriate.
- Keep code snippets labelled with expected script type and location when used in Roblox.
