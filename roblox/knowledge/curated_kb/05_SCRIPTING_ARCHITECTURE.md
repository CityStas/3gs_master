# Roblox Scripting Architecture

## 1. Script containers and execution context

Roblox distinguishes server and client execution. Script type, parent location and `Script.RunContext` all matter. The current official guide explicitly warns that these three dimensions affect whether and where a script runs.

- **Script:** can run on server or client depending on location and `RunContext`. A newly created Script normally uses `Legacy`; in that mode it runs server-side only from supported server containers such as `ServerScriptService` or `Workspace`.
- **LocalScript:** client-side only and does not have a `RunContext` property. It runs only in supported client containers/contexts.
- **ModuleScript:** reusable module loaded with `require()`. It has no `RunContext`; it executes in the context of the caller and is not inherently server-only or client-only.

`RunContext` includes `Legacy`, `Server`, `Client` and `Plugin`. A Script configured as `Server` or `Client` may be able to run from additional locations, but location and replication implications still matter. For example, placing server code in `ReplicatedStorage` is generally a poor security choice because the contents replicate to clients. Prefer conventional containers and verify the exact current rules.

Do not infer execution side from the filename alone. Inspect the actual Instance class, parent path and `RunContext`.

Official guide: https://create.roblox.com/docs/scripting/locations and enum reference: https://create.roblox.com/docs/reference/engine/enums/RunContext.

## 2. Common containers

| Container | Typical purpose | Trust / availability |
|---|---|---|
| `ServerScriptService` | Server scripts and server systems | Server-only |
| `ServerStorage` | Server-only assets/templates | Server-only |
| `ReplicatedStorage` | Shared modules, remotes, replicated data | Replicated to clients; never put secrets here |
| `StarterPlayerScripts` | Client player scripts | Copied to each player's PlayerScripts |
| `StarterCharacterScripts` | Per-character client scripts | Copied when character spawns |
| `StarterGui` | UI templates | Copied to PlayerGui |
| `StarterPack` | Starter tools | Distributed to player Backpack |
| `Workspace` | Runtime world | Replicated according to engine rules |

## 3. ModuleScript design

Use modules to isolate responsibilities and define clear public interfaces.

Example pattern:

```lua
--!strict
-- ModuleScript: ServerScriptService/Services/CurrencyService

local CurrencyService = {}

function CurrencyService.addCoins(player: Player, amount: number)
    assert(amount > 0, "amount must be positive")
    -- Update server-authoritative player state here.
end

return CurrencyService
```

Avoid circular `require()` dependencies. Avoid storing mutable shared player state in a module unless the lifecycle and ownership are explicit.

## 4. Suggested project layout

This is a convention, not a Roblox engine requirement:

```text
ReplicatedStorage/
  Shared/
    Types/
    Config/
    Util/
  Remotes/
    Events/

ServerScriptService/
  Bootstrap.server.lua
  Services/
    PlayerDataService.lua
    CurrencyService.lua
    RoundService.lua

ServerStorage/
  ServerAssets/

StarterPlayer/
  StarterPlayerScripts/
    Controllers/

StarterGui/
  MainUI/
```

Adapt to the existing project rather than restructuring it automatically.

## 5. Initialization and lifecycle

Common lifecycle signals include player joins/leaves, character added/removing, tool equipped/unequipped and RunService frame signals. Prefer connecting events once and explicitly cleaning up per-player/per-character connections.

Potential pitfalls:

- Character objects can be replaced on respawn.
- A Player may leave while an asynchronous operation is pending.
- `WaitForChild()` may yield; use it intentionally and consider timeouts for critical startup paths.
- Event connections and long-running tasks need cleanup.
- Client and server copies of objects can differ.

## 6. Architecture checklist

Before creating a system, answer:

1. Which side owns the authoritative state?
2. Which scripts/containers execute the logic?
3. What information must replicate to clients?
4. What is the public ModuleScript interface?
5. How is state initialized, saved and cleaned up?
6. What happens on respawn, disconnect, retry and server shutdown?
7. What tests demonstrate correct behavior?

Reference: https://create.roblox.com/docs/projects/data-model and https://create.roblox.com/docs/projects/client-server.
