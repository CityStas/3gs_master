---
title: "Memory usage"
url: /docs/en-us/studio/optimization/memory-usage
last_updated: 2026-10-30T19:55:57Z
description: "Use Memory and Luau Heap tools within the Developer Console to monitor the memory usage of your game."
---

# Memory usage

Every building and scripting component that you add to your game consumes memory. When memory usage reaches engine limits, the user's device or server may crash, so you need to actively monitor usage.

The **Developer Console** provides two tools for monitoring memory usage:

- [Memory](#memory) — View real-time memory consumption by usage categories, including your custom components and the engine internal processes.
- [Luau heap](#luau-heap) — Create snapshots of heap memory, which refers to the memory allocation of your scripts. This tool provides several views to help you identify current memory allocation and issues from different perspectives, such as object types and engine classes. It also allows you to create multiple snapshots to compare differences in memory usage over time.

You can open the console during a testing or live game session using any of the following ways:

- Press `F9`.
- Type `/console` into the chat.
- Use the in-game menu:
  1. Open the in-game **Roblox Menu**.
  2. Select the **Settings** tab.
  3. Scroll down to **Developer Console** and click **Open**.

## Memory

The **Memory** tool categorizes and displays real-time memory usage. It displays memory usage in MB of each category and generates a chart on usage change over time.

To view memory allocation:

1. Open the **Developer Console**.
2. Expand the tools dropdown to select **Memory**.![Dropdown menu of all Developer Console tools with the Memory option highlighted for selection.](../../assets/studio/console/Memory-Open.png)
3. Expand the client-server dropdown to select **Client** or **Server**.
4. Browse the memory usage categories and items. If you want to see usage over time, expand the category to display a chart.
  - **CoreMemory** — Memory usage by the core building processes of the engine, including networking, avatars, and GUI elements that you don't have direct control over.
  - **PlaceMemory** — Memory usage based on how you build your game, including models, terrain, parts, scripts, and all other custom elements that you add to your game.**###### PlaceMemory reference**| Category | Description |
| --- | --- | | **HttpCache** | Assets (images, meshes, etc.) loaded from Roblox servers and now held in a cache in memory. | | **Instances** | `Class.Instance\|Instances` in the place. | | **Signals** | Signals that fire between instances (an event firing on one instance to trigger an event on another instance). | | **LuaHeap** | Heap memory for both core scripts (scripts that ship with the Roblox client) and custom scripts. | | **Script** | Luau scripts. | | **PhysicsCollision** | Collision data for physics simulations. | | **PhysicsParts** | Physics geometry and kinetics. | | **GraphicsSolidModels** | Graphics data to render solid models. | | **GraphicsMeshParts** | Graphics for `Class.MeshPart` objects. | | **GraphicsParticles** | Graphics for particle systems. | | **GraphicsParts** | Graphics for parts. | | **GraphicsSpatialHash** | General rendering. | | **GraphicsTerrain** | Graphics for terrain. | | **GraphicsTexture** | Texture memory. | | **GraphicsTextureCharacter** | Texture memory for characters. | | **Sounds** | In-memory sounds. | | **StreamingSounds** | Streaming sounds. | | **TerrainVoxels** | Terrain voxels. | | **TerrainPhysics** | Terrain physics. | | **Gui** | Memory used by common GUI elements. | | **Animation** | Memory used for animation data, such as poses and `Class.KeyframeSequence` cached data for avatar animations. | | **Navigation** | Memory used by supporting structures for `Class.PathfindingService`. |
  - **UntrackedMemory** — Memory allocations that the system can't easily attribute to a particular source.
  - **PlaceScriptMemory** — Memory usage of your scripts with insights into how individual scripts and custom memory tags contribute to overall memory usage.
  - **CoreScriptMemory** — Memory usage by internal engine scripts that you don't have direct control over. Among these categories, **PlaceMemory** and **PlaceScriptMemory** are the most important ones for performance optimization, because they help you understand how your building and scripting choices affect memory consumption and potential areas for optimization. For more insights into **PlaceScriptMemory**, use the [Luau heap](#luau-heap) tool to create snapshots and analyze memory allocation by different metrics.

> **Info:** For more information on common memory usage problems and best practices, see [Performance Optimization](/docs/en-us/performance-optimization/improve.md#memory-usage).
## Luau heap

The **Luau heap** tool allows you to create snapshots of the current allocation of heap memory, which refers to the memory Luau scripts use to store variables, tables, functions, and other runtime data structures. This tool provides several views to help you identify issues from different perspectives, such as object types and engine classes. It also allows you to create multiple snapshots to compare differences in memory usage over time.

### Create snapshots

To create a snapshot of your memory allocation:

1. Open the **Developer Console**.
2. Expand the tools dropdown to select **LuauHeap**.![Dropdown menu of all Developer Console tools with the LuauHeap option highlighted for selection.](../../assets/studio/console/LuauHeap-Open.png)
3. Expand the client-server dropdown to select **Client** or **Server**.
4. Click the **Create Snapshot** button.

### Analyze memory usage

The tool provides many views into Luau memory usage:

- **Graph** — Shows an aggregated memory usage tree, with each node representing an object with memory allocated.
- **Object Tags** — Shows memory sizes and counts by runtime types, such as `function`, `table`, and `thread`.
- **Memory Categories** — Shows memory sizes and counts by engine-assigned memory categories. The engine assigns a memory category to an object at allocation time.
- **Object Classes** — Shows memory sizes and counts by engine classes that your scripts use and store their instances, such as `EnumItem`, `Animation`, `CFrame`. Critically, this view does not show memory usage within the engine itself, only the Luau VM.
- **Unique References** and **Unparented Instances** — Shows counts and total numbers of instances for **unique references** or **all remaining references** that don't have a parent in the data model and are only reachable by scripts. Also shows all paths that pin the instance object.

#### Graph

The **Graph** view is the most detailed and complex view among all Luau heap views. It shows an aggregated memory usage tree with each node representing an object with memory allocated. The tree shows how objects connect to each other and derives the shortest path between object references. It has the following columns of memory size:

- Size — The self memory usage plus the memory usage by contents within the data structure.
- Self — The memory directly allocated for the data structure itself, excluding the memory usage by any content it contains.

> **Info:** The graph view displays elements smaller than 2 KB as a single `…` node.
![An example Graph view](../../assets/studio/console/Graph-View.jpeg)

The root of the tree graph is `registry`, which stores all engine and Luau references, such as functions connected to signals or the task library, tables returned by module scripts, and global functions, tables and classes. It usually parents the following common entries:

- `Module @Path.To.Module` is the table returned by a module script.
- `name:123 =Path.To.Module` is a function inside a specified script. Anonymous functions don't have names. The top level node often refers to the global script function. Example: `:1= Workspace.[Username].Animate`.
- `upvalue` is a reference for captured functions. See [Capture local scope](/docs/en-us/luau/scope.md#capture) for more information.
- `env` refers to the environment of a function. For most cases, it's a table representing the global scope of a script.
- `globals` refers to the environment of a thread.
- `[key]` represents objects that serve as table keys.
- `array` represents an array.
- `stack` refers to the array that stores all function locals.
- `constants` represents all constant values that functions use.

#### Memory categories

The **Memory Categories** view shows memory sizes and counts by memory categories, which the engine assigns to objects at allocation time. By default, the memory category has the same name as the script, or you can assign custom memory category names using the `debug.setmemorycategory` function.

#### Unique references and unparented instances

The **Unique References** and **Unparented Instances** views are related. Both show memory usage of instances that don't have a parent in the data model and are only reachable by scripts, along with all paths that pin the instance object. If an instance is only referenced within Luau scripts, it appears under **Unique References**. Otherwise, it's also in use by Roblox systems and appears under **Unparented Instances**. Both views show two metrics:

- **Count** — The number of instances with the same name that are reachable from the same path, such as multiple instances named `Dragon` in the same table.
- **Total Instances** — The total number of objects inside those roots, such as all parts, scripts, and sound objects that construct a `Dragon` instance.

![An example Unique Reference view](../../assets/studio/console/Unique-Reference-View.jpeg)

These views are useful for identifying unnecessary connected instances, which you need to disconnect when you no longer need them. If you see many unexpected instances in this view, check out the paths holding them and evaluate whether they are necessary.
