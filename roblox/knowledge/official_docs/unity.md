---
title: "Roblox for Unity developers"
url: /docs/en-us/unity
last_updated: 2026-10-30T19:56:03Z
description: "If you're an experienced Unity developer, use this page to get oriented with Roblox."
---

# Roblox for Unity developers

This page contains information to help experienced Unity developers get started with Roblox, including basic orientation, a conceptual comparison, and key differences between the two platforms.

## Get oriented

![The Unity user interface with markup to show the various windows and panels.](./assets/engine-comparisons/Unity-Editor-Layout.png)![The Roblox Studio user interface with markup to show the various windows and panels.](./assets/studio/general/Studio-Layout.png)

Unity's **Hierarchy** window and Roblox Studio's [Explorer](/docs/en-us/studio/explorer.md) are the primary windows for organizing elements in 3D scenes:

- Both allow you to manage and organize objects (for example, characters and environmental assets).
- Both use a tree structure for the parent-child relationships between objects.

However, the **Hierarchy** window has no predefined structure, whereas the **Explorer** window has a strict structure. It might help to think of the **Explorer** window as a combination of Unity's **Hierarchy** and **Project** windows, with the `Class.Workspace` folder as the most recognizable element.

Similarly, the Roblox Studio [Asset Manager](/docs/en-us/projects/assets/manager.md) and [Toolbox](/docs/en-us/projects/assets/toolbox.md) overlap with the Unity **Project** window. The **Asset Manager** lets you manage all assets within your game, whereas the **Toolbox** lets you access any assets you've published. The **Toolbox** also lets you search the [Creator Store](/docs/en-us/production/creator-store.md) for assets from Roblox or the community, similar to the Unity **Asset Store**.

## Philosophical differences

Roblox is a "simulation engine" rather than a traditional game engine. Unity `GameObjects` and Roblox `Class.Part|Parts` both serve as the fundamental building blocks for creating objects in a 3D environment, but in practice, the two are quite different:

- **Representation**: `GameObjects` in Unity are a higher-level concept for any object in a scene, whereas `Parts` in Roblox are designed to represent physical objects like wooden blocks and plastic spheres, rather than abstract geometry like primitive objects in Unity.
- **Physics**: To perform physics simulations in Unity, you attach components like `Rigidbody` and `Collider` to a `GameObject`. In Roblox, physics are built into the `Parts` data type; the engine handles interactions automatically.

You can see the difference immediately if you create a `GameObject` and a `Part`. The `GameObject` has nothing more than a position, rotation, and scale. The `Part` has that same information—plus a material and color, values for reflectance and transparency, mass and shape, and much more. Turning a `Part` into something more akin to an empty `GameObject` means **removing** a lot of built-in properties. Conversely, you can make a `GameObject` that looks a lot like a `Part` by adding `MeshFilter`, `MeshRenderer`, `Collider`, and `Rigidbody` components to it.

From a scripting perspective, `GameObject` is most similar to the Roblox `Class.Instance`, the base class for all other Roblox classes, but because you don't (and can't) create objects of type `Instance`, the comparison isn't especially practical.

Another comparison is the Unity `GameObject` to the Roblox `Class.Model`. Models act as a container for a collection of interconnected parts in the same way that you might establish a parent-child relationship between many `GameObjects` in Unity. You specify one of the model's parts as its [primary part](/docs/en-us/parts/models.md#set-a-primary-part) to define the pivot point. Models also hold scripts, animations, sound effects, prompts, constraints, particle emitters, and more.

For example, a Unity `GameObject` might have components for `ParticleSystem`, `Physics3D`, `SpringConstraint`, and a script. In the Hierarchy window, you see a single `GameObject` named `SpringyFireball`. The Inspector window shows the collection of components and properties.

In Roblox, a comparable `SpringyFireball` model in the **Explorer** window might look something like this:

```text
Model
|- ParticleEmitter
|- MeshPart
|- SpringConstraint
|- ClickDetector
|  |- Script
```

Roblox's physics-by-default philosophy extends to the process of building 3D models. In Roblox, welding multiple parts together into an [assembly](/docs/en-us/physics/assemblies.md) is an excellent way to quickly build things, because Roblox treats the welded parts as a single rigid body. This approach isn't available in Unity.

Rather than using standard metric units for length and mass, Roblox uses notional units called studs and Roblox Mass Units (RMUs). For approximate metric conversions and recommendations around use, see [Units](/docs/en-us/physics/units.md).

## Location matters

Roblox games are multiplayer by default, so Roblox Studio includes many different storage locations with specific behaviors. For more information, see [client-server runtime](/docs/en-us/projects/client-server.md) and [object organization](/docs/en-us/projects/data-model.md#object-organization).

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

## Scripting

Roblox games support three different types of Luau scripts:

- **Client scripts** These scripts run on the client, and the server has no visibility into their behavior. For legacy reasons, these scripts can take the form of `Class.LocalScript|LocalScripts` or `Class.Script|Scripts` with a `Class.BaseScript.RunContext|RunContext` value of `Enum.RunContext|Client`. Client scripts typically live in `Class.ReplicatedStorage`, `Class.StarterPlayerScripts`, or `Class.StarterCharacterScripts`.
- **Server scripts** These scripts run on the server, and the client has no visibility into their behavior. Server scripts have a `Class.BaseScript.RunContext|RunContext` value of `Enum.RunContext|Server` and typically live in `Class.ServerScriptService`, the contents of which are not replicated to the client.
- **Module scripts** These scripts are reusable pieces of code that return exactly one value, typically a function or table (or a table of functions). Rather than duplicating code in client and server scripts, use module scripts to share code and data between the two. Module scripts often live in `Class.ReplicatedStorage`, but can live elsewhere if you want to share code between scripts on the same side of the client-server boundary.

Unity doesn't have the concept of different script types. If you choose to make a multiplayer game, Unity uses its networking libraries to indicate when a `GameObject` (and its scripts) should be exclusive to the server.

In Unity, much of the engine's functionality is available through the methods of `MonoBehaviour`. For example, to run code before the render loop, you add code to the `Update()` method. To handle physics collision events, you add code to the `OnCollideEnter()` method.

Roblox scripts are more event-driven. You access similar functionality by subscribing to services and listening for updates.

### C# and Luau

For scripting, Unity uses C#. Roblox uses [Luau](/docs/en-us/luau.md), a scripting language derived from [Lua 5.1](https://www.lua.org/manual/5.1/).

Compared to C#, Luau is gradually typed and generally has a less verbose syntax. In larger projects, however, gradual typing can introduce categories of bugs that strongly typed languages like C# avoid, so consider enabling [strict type checking](/docs/en-us/luau/type-checking.md#inference-modes) in Roblox scripts.

For basic syntax differences between the scripting languages, see [Luau and C# comparison](/docs/en-us/luau/luau-csharp-comparison.md).

### Luau code sample

The following Luau code sample demonstrates how to, after a player equips a fishing pole, listen for user input (in this case, the `E` key) and call additional functions:

```lua
local ContextActionService = game:GetService("ContextActionService")
local ReplicatedStorage = game:GetService("ReplicatedStorage")

-- Get a module script from ReplicatedStorage that returns a single function
local performSomeAction = require(ReplicatedStorage.performSomeAction)

-- Assumes that this script is a child of the fishing pole
local fishingPole = script.Parent
local ACTION_CAST = "Cast"

-- Check that the key is down, then call another function
local function castLine(_actionName, inputState, _inputObject)
	if inputState == Enum.UserInputState.Begin then
		performSomeAction()
	end
end

-- Only enable the action when the player equips the fishing pole
fishingPole.Equipped:Connect(function()
	ContextActionService:BindAction(ACTION_CAST, castLine, true, Enum.KeyCode.E)
end)

-- Disable the action when the player unequips the fishing pole
fishingPole.Unequipped:Connect(function()
	ContextActionService:UnbindAction(ACTION_CAST)
end)
```

The Roblox script can be relatively concise because Roblox has many built-in assumptions: a `Class.Player` with a `Class.Humanoid` character connected to the server and can equip `Class.Tool|Tools`. These assumptions don't exist in Unity, so the implementation would be very different.

## Assets

Unity and Roblox both support importing custom meshes and models in `.fbx` format. Certain types of assets may require specific configurations and export settings from your third-party modeling software. For more information, see the following pages:

- [Importer](/docs/en-us/studio/importer.md)
- [General specifications](/docs/en-us/art/modeling/specifications.md)
- [Blender and Maya export requirements](/docs/en-us/art/modeling/export-requirements.md)

In Unity, objects import into your `Assets` directory, visible in the **Project** window. In Roblox, assets import into your `Class.Workspace` and into the [Toolbox](/docs/en-us/projects/assets/toolbox.md) or [Asset Manager](/docs/en-us/projects/assets/manager.md).

Roblox also offers an open-source [Blender plugin](/docs/en-us/art/modeling/roblox-blender-plugin.md) to streamline the import process.

## Transforms

Unity's transforms and Roblox's `Datatype.CFrame|CFrames` serve similar purposes in representing 3D transformations of objects:

- Both transforms and `Datatype.CFrame|CFrames` represent the position and rotation of an object in 3D space. Transforms include scale, whereas Roblox uses a `Class.BasePart.Size` property that isn't part of the `Datatype.CFrame`.
- Both support multiplication for complex transformations and have built-in methods for other manipulations.

## Collaboration

In Unity, you collaborate with standard version control systems or paid services like Unity Version Control.

Roblox files live in the cloud (although you can export copies), so Roblox Studio provides built-in collaboration workflows for simultaneous editing, group management, permissions, script drafting, and more. See [Collaboration](/docs/en-us/projects/collaboration.md).

> **Info:** Cloud syncing provides further benefits with [packages](/docs/en-us/projects/assets/packages.md), the Roblox equivalent of Unity prefabs. Converting an asset or asset hierarchy to a package helps with local reusability, but also with collaboration. When you or your collaborators publish a new version of a package, you can quickly update existing instances of that package within a game or set them to auto-update.
## Plugins

Similar to Unity tools, Roblox Studio supports [plugins](/docs/en-us/studio/plugins.md), which can simplify or give you additional control over various aspects of the development process. Plugins are available in the [Creator Store](/docs/en-us/production/creator-store.md), just like assets, many for free.

## Glossary

| Unity | Roblox | Notes |
| --- | --- | --- |
| Scene | [Place](/docs/en-us/projects.md#places) | |
| GameObject | `Class.Part` or `Class.Model` | See [Philosophical differences](#philosophical-differences). |
| Prefab | [Package](/docs/en-us/projects/assets/packages.md) | |
| Transform | `Datatype.CFrame` | `Datatype.CFrame` doesn't include scale information. See [Transforms](#transforms). |
| Hierarchy | [Explorer](/docs/en-us/studio/explorer.md) | |
| Inspector | [Properties](/docs/en-us/studio/properties.md) | |
| Scene view | [3D viewport](/docs/en-us/studio/overview.md#3d-viewport) | |
| Game view | [3D viewport](/docs/en-us/studio/overview.md#3d-viewport) | The viewport transitions into a gameplay view when you test your game. |
| Project window | [Asset Manager](/docs/en-us/projects/assets/manager.md) or [Toolbox](/docs/en-us/projects/assets/toolbox.md) | |
| Terrain Inspector | [Terrain Editor](/docs/en-us/studio/terrain-editor.md) | |
| Spawn point | `Class.SpawnLocation` | |
| Console | [Output](/docs/en-us/studio/output.md) | |
| Asset Store | [Creator Store](/docs/en-us/production/creator-store.md) | |
| Overlays | [Toolbar](/docs/en-us/studio/overview.md#toolbar-and-mezzanine) | |
| Tool | [Plugin](/docs/en-us/studio/plugins.md) | |
