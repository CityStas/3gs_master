---
name: roblox-luau
description: "Luau for Roblox: type annotations and --!strict, generics, type refinement, the task library, string interpolation, compound assignment, tables and metatables, OOP patterns, error handling. Use for any question about Luau syntax or idiom, or when a script must be written from scratch. Русские триггеры: «луай», «luau», «типы», «аннотации типов», «строгий режим», «метатаблицы», «класс», «модуль», «task.wait», «корутина»."
---

# Luau

Luau is not Lua 5.1 with extra libraries: it has a real type system, `continue`, compound
assignment, string interpolation, generalized iteration, and a scheduler that replaces the
old `wait`/`spawn`/`delay`. Write Luau. When in doubt about a signature, `rbx_rag_search`
the exact symbol.

## Types

```lua
--!strict
export type Item = {
    id: string,
    price: number,
    tags: {string}?,          -- optional field
}

export type Inventory = { [string]: number }   -- map, not an array

local function total(items: {Item}): number
    local sum = 0
    for _, item in items do          -- generalized iteration: no ipairs needed
        sum += item.price
    end
    return sum
end
```

- `--!strict` at the top of new modules; `--!nonstrict` where the project already is.
- `type` is local, `export type` is visible to requirers. Put shared types in one module
  under `ReplicatedStorage` and `require` it from both sides.
- Generic functions: `local function first<T>(list: {T}): T?`.
- Type refinement works on `if x then` and on `type(x) == "Instance"`; it does NOT refine
  through a function call. `if not player then return end` is how you narrow, not `assert`.
- `any` is a last resort, not a default. A wrong type annotation is worse than none: it
  makes the editor lie.

## The scheduler

| Don't | Do |
|---|---|
| `wait(1)` | `task.wait(1)` |
| `spawn(f)` | `task.spawn(f)` |
| `delay(1, f)` | `task.delay(1, f)` |
| `tick()` | `os.clock()` for durations, `DateTime.now().UnixTimestampMillis` for wall time |
| `coroutine.wrap` for scheduling | `task.spawn` / `task.defer` |

`task.wait()` with no argument yields one frame. `task.wait(n)` yields *at least* n
seconds - it is not a precise timer, and it is not `os.time`. `task.defer` runs after the
current resumption finishes; `task.spawn` runs immediately in a new thread.

## Syntax worth using

```lua
local name = "Part"
print(`Hello {name}, you have {#items} items`)   -- string interpolation
counter += 1                                      -- compound assignment
if x == 1 then continue end                       -- continue exists in Luau
for i, v in {10, 20, 30} do end                   -- generalized iteration
local t = table.create(100, 0)                    -- preallocate
table.clear(t)                                    -- reuse instead of reallocating
```

## OOP

```lua
local Shop = {}
Shop.__index = Shop

function Shop.new(store: any): Shop
    local self = setmetatable({}, Shop)
    self.store = store
    return self
end

function Shop:buy(player: Player, itemId: string): boolean
    return self.store:purchase(player, itemId)
end

return Shop
```

`Shop.new` is a static constructor (`.`), `Shop:buy` is a method (`:`). A `.` call on a
method passes no `self` and fails with "attempt to index nil" - the most common Luau error
after a typo in a member name.

## Errors

```lua
local ok, result = pcall(function()
    return store:GetAsync(key)
end)
if not ok then
    warn(`GetAsync failed: {result}`)   -- result is the error message here
    return nil
end
```

`pcall` for anything that crosses a boundary (DataStore, HttpService, `require` of a
user-supplied module). Do not wrap code you control in `pcall` to hide bugs - fix them.

## Common mistakes

- `#tbl` is the array length only for a sequence; on a dictionary it is 0 and on a table
  with holes it is undefined. Use a counter or `next`.
- `ipairs` stops at the first `nil`. `pairs`/generalized iteration does not.
- `..` on numbers is fine but slow in a loop - build with `table.concat`.
- A `LocalScript` cannot `require` a `ModuleScript` in `ServerStorage`; it is not
  replicated, so the require hangs forever instead of erroring.
- `Instance.new("Part", parent)` is deprecated: every property write after it replicates
  separately. Set `.Parent` last.
- Method names are PascalCase. `:findFirstChild(` returns nil because the method does not
  exist - it does not throw.
