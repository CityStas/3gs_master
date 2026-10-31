---
title: "Script types and locations"
url: /docs/en-us/scripting/locations
last_updated: 2026-10-30T19:55:56Z
description: "How scripts run in Roblox, and how location impacts that behavior."
---

# Script types and locations

For many developers, the fundamental challenge of adapting to Roblox scripting is the importance of file location and the `Class.Script.RunContext` property. Depending on script type, location in the **Explorer**, and run context, scripts can behave very differently. Certain method calls might fail, objects in your game might be inaccessible, or scripts might not run at all.

The reason for this complexity is that Roblox games are multiplayer by default. Scripts need the ability to only run on the server, only run on the client, or be shared across both. The evolution of the Roblox platform over time has further complicated the situation.

## Script types

Roblox has three types of scripts:

- `Class.Script` - Code that runs on either the server or the client, depending on its location and `Class.Script.RunContext` property.
- `Class.LocalScript` - Code that runs only on the client. Does not have a run context.
- `Class.ModuleScript` - Code that you can reuse in other scripts. Does not have a run context.

When you create a `Class.Script`, its default run context is `Legacy`, meaning that it a) is a server-side script and b) only runs if it is in a server container, such as `Class.ServerScriptService` or `Class.Workspace`.

- If you change the script's run context to `Server`, it can now also run in `Class.ReplicatedStorage`, but we don't recommend it. The contents of that location are replicated to clients, so it's a poor location for server-side scripts.
- If you change the script's run context to `Client`, it can run in `Class.ReplicatedStorage`. It can also run in `Class.StarterCharacterScripts` and `Class.StarterPlayerScripts`. Starter containers are copied to clients, though, so the original script **and** the copy run, which isn't desirable.

To change a script run context, select it in the [Explorer](/docs/en-us/studio/explorer.md) and change the value in the [Properties](/docs/en-us/studio/properties.md) window.

![RunContext property indicated for a Script.](../assets/studio/properties/Script-RunContext.png) ## Recommendations

- Put a single `Class.Script` with a `RunContext` of `Client` into `Class.ReplicatedStorage`.
- Put a single `Class.Script` with a `RunContext` of `Server` into `Class.ServerScriptService`.
- Use `Class.ModuleScript|ModuleScripts` for as much client and server code as possible. Require these modules from your client script and your server script. This approach gives your code a single entry point on the client and server sides, which simplifies organization and makes it easy to isolate or disable problematic modules. Add a `start()` function to each `Class.ModuleScript|ModuleScript` so that all modules can load before you begin executing their code:```lua
--!strict
local ServerScriptService = game:GetService("ServerScriptService")
local SampleModule = require(ServerScriptService.SampleModule)
local AnotherSampleModule = require(ServerScriptService.AnotherSampleModule)
SampleModule.start()
AnotherSampleModule.start()
``````lua
--!strict
local CollectionService = game:GetService("CollectionService")

local NPC_TAG = "npc"

local SampleModule = {}

local function setUpNpc(npc: Instance)
    -- initialize each NPC
end

local function cleanUpNpc(npc: Instance)
    -- run when event fires
end

function SampleModule.start() -- add the function to the table
    -- example loop for setup based on tags
    for _, npc in CollectionService:GetTagged(NPC_TAG) do
        setUpNpc(npc)
    end

    -- run functions when events fire
    CollectionService:GetInstanceAddedSignal(NPC_TAG):Connect(setUpNpc)
    CollectionService:GetInstanceRemovedSignal(NPC_TAG):Connect(cleanUpNpc)
end

return SampleModule
```
- To share code, use `Class.ModuleScript|ModuleScripts` in `ReplicatedStorage` and require them in both your client script and your server script.
- If necessary for your game, repeat the same pattern in `Class.ReplicatedFirst` with a single client script and a minimal number of `Class.ModuleScript|ModuleScripts` to implement a loading screen. To learn more about `ReplicatedFirst`, see [Replication order](/docs/en-us/scripting/attributes.md#replication-order).
- Use `Class.LocalScript|LocalScripts` sparingly. If you must use them, put them in `StarterCharacterScripts`, `StarterPlayerScripts`, `StarterGui`, or `StarterPack`. Scripts in these containers clone to player containers rather than running from one location, which can complicate debugging. Using `ReplicatedStorage` for client code lets you click lines in the **Output** window and go to `ReplicatedStorage.YourScript` (the stable location of the script) rather than `Players.YourName.PlayerScripts.YourLocalScript` (the ephemeral location that the script was copied to at runtime).
- Avoid attaching scripts directly to instances in `Class.Workspace`. Instead, [tag instances](/docs/en-us/studio/properties.md#instance-tags) and use `Class.CollectionService` to work with them from a single `Class.ModuleScript|ModuleScript`. The key exception is if you distribute models or packages on the Creator Store. In that case, you might need to include scripts within the instance hierarchy; specify a `RunContext` for each script to remove ambiguity from how it runs. Explicitly setting this property makes models and packages more likely to work properly from a variety of locations.

### Example project structure

The [Plant](/docs/en-us/resources/plant-reference-project.md) reference project shows how you might organize your code in a large, complex game. It stores the vast majority of its code as reusable `Class.ModuleScript|ModuleScripts`.

## Script locations

| Location | Description |
| --- | --- |
| `Class.Workspace` | Represents the game's 3D world. Can run server scripts that attach directly to objects and control their behavior. |
| `Class.ReplicatedFirst` | Contains objects that replicate to the client before anything else. This location is ideal for the absolute minimum set of objects and client scripts necessary to display a loading screen. |
| `Class.ReplicatedStorage` | Contains objects that are replicated to both the client and the server. This location is ideal for `Class.Script\|Scripts` with a `Class.BaseScript.RunContext\|RunContext` of `Enum.RunContext\|Client`, client `Class.ModuleScript\|ModuleScripts`, and `Class.ModuleScript\|ModuleScripts` that you want to use on both the server and the client. `Class.LocalScript\|LocalScripts` do not run from this location. |
| `Class.ServerScriptService` | Contains server scripts. This location is ideal for scripts that need to access server-side functionality or objects, such as game logic and cloud storage. |
| `Class.ServerStorage` | Contains server-side objects. This location is ideal for large objects that don't need to be immediately replicated to clients when they join a game. Scripts do not run from this location, but you can store server-side `Class.ModuleScript\|ModuleScripts` here. |
| `Class.StarterPlayer` ⟩ `Class.StarterCharacterScripts` | Contains `Class.LocalScript\|LocalScripts` that run when the character spawns. |
| `Class.StarterPlayer` ⟩ `Class.StarterPlayerScripts` | Contains `Class.LocalScript\|LocalScripts` that run when the player joins the game. |
| `Class.StarterGui` | Contains GUI elements that the client displays when it loads the game. `Class.LocalScript\|LocalScripts` can run from this location. |
| `Class.StarterPack` | Generally only contains `Class.Tool\|Tools`, but can also include `Class.LocalScript\|LocalScripts` for setting up player backpacks. |

This image shows which **Explorer** window locations can contain client scripts. Remember, `ReplicatedFirst` and `ReplicatedStorage` can contain `Class.Script|Scripts` with a `Class.BaseScript.RunContext|RunContext` of `Enum.RunContext|Client`, whereas the `Starter[]` containers should use `Class.LocalScript|LocalScripts`.

![Diagram showing which script locations run on clients.](../assets/scripting/client-server/Client-Script-Containers.png)
