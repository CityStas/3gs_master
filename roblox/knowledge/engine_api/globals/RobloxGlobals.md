---
name: Roblox globals
last_updated: 2026-10-30T19:55:54Z
type: global
summary: "Built-in functions and constants unique to Roblox."
---

# Roblox globals

Built-in functions and constants unique to Roblox.

**Type:** global

## Description

Roblox provides several unique built-in functions and variables in its
embedding of Luau. These are only found on Roblox and are not packaged by
default with Luau or Lua.

## Properties

### Enum

**Type:** `Enums`

A reference to the Enums data type, which stores all of the available
enums that can be used on Roblox.

### game

**Type:** `DataModel`

A reference to the [DataModel](/docs/reference/engine/classes/DataModel.md), which is the root Instance of
Roblox's parent/child hierarchy.

### plugin

**Type:** `Plugin`

A reference to the [Plugin](/docs/reference/engine/classes/Plugin.md) object that represents the plugin being
run from this [Script](/docs/reference/engine/classes/Script.md). This reference exists only in the context
where a script is executed as a plugin and is not passed to
[ModuleScripts](/docs/reference/engine/classes/ModuleScript.md) within the plugin. To use this
reference in a [ModuleScript](/docs/reference/engine/classes/ModuleScript.md), you must explicitly pass it.

**Roblox Globals Plugin**

Demonstrates the `plugin` global.

```lua
assert(plugin, "This script must be run as a plugin!")
-- Code beyond this point will execute only if the script is run as a plugin
```

### shared

**Type:** `Array`

A table that is shared across all scripts that share the same execution
context level. This serves the exact same purpose as `_G`.

### script

**Type:** `LuaSourceContainer`

A reference to the script object that is executing the code you are
writing. It can be either a [Script](/docs/reference/engine/classes/Script.md), a [LocalScript](/docs/reference/engine/classes/LocalScript.md), or a
[ModuleScript](/docs/reference/engine/classes/ModuleScript.md). This variable is not available when executing code
from Roblox Studio's command bar.

### workspace

**Type:** `Workspace`

A reference to the [Workspace](/docs/reference/engine/classes/Workspace.md) service, which contains all of the
physical components of a Roblox world.

## Functions

### PluginManager

**Signature:** `PluginManager(): PluginManager`

Returns the [PluginManager](/docs/reference/engine/classes/PluginManager.md) which is a deprecated singleton that was
previously required to create plugins. It still has some applicable uses,
such as if you need to create a [Plugin](/docs/reference/engine/classes/Plugin.md) object from Studio's
[Command Bar](/docs/en-us/studio/ui-overview.md#command-bar).

**Returns:** `PluginManager` — The PluginManager singleton instance.

### settings

**Signature:** `settings(): GlobalSettings`

Returns the [GlobalSettings](/docs/reference/engine/classes/GlobalSettings.md) object, which can be used to access the
settings objects that are used in Roblox Studio's settings menu.

**Returns:** `GlobalSettings` — The GlobalSettings singleton used to access Roblox Studio's settings
objects.

### tick

**Signature:** `tick(): number`

Returns how much time has elapsed, in seconds, since the Unix epoch, on
the current local session's computer. The Unix epoch is represented by
00:00:00 on 1 January 1970.

`tick()` isn't officially deprecated, but has a variety of issues. It can
be off by up to one second and returns inconsistent results across time
zones and operating systems. Use [os.time()](/docs/reference/engine/globals/os.md),
[os.clock()](/docs/reference/engine/globals/os.md), or [RobloxGlobals.time()](/docs/reference/engine/globals/RobloxGlobals.md) instead. Also
consider [DateTime.UnixTimestamp](/docs/reference/engine/datatypes/DateTime.md) and
[DateTime.UnixTimestampMillis](/docs/reference/engine/datatypes/DateTime.md).

**Returns:** `number` — The elapsed time, in seconds, since the Unix epoch (January 1, 1970)
according to the local device clock.

### time

**Signature:** `time(): number`

Returns the amount of time, in seconds, that has elapsed since the current
game instance started running. If the current game instance is not
running, this will be `0`.

If [Workspace.AuthorityMode](/docs/reference/engine/classes/Workspace.md) is [AuthorityMode.Server](/docs/reference/engine/enums/AuthorityMode.md), this
value is synchronized between client and server.

**Returns:** `number` — The elapsed time, in seconds, since the current game instance started
running.

### typeof

**Signature:** `typeof(object: Variant): string`

Returns the type of the object specified, as a string. This function is
more accurate than Luau's native `type` function, as it does not denote
Roblox-specific types as `userdata`.

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `object` | `Variant` |  | The Luau type that will have its type checked. |

**Returns:** `string` — A string representation of the object's type, including
Roblox-specific types such as "Vector3" or "CFrame".

### UserSettings

**Signature:** `UserSettings(): UserSettings`

Returns the [UserSettings](/docs/reference/engine/classes/UserSettings.md) object, which is used to read information
from the current user's game menu settings.

**Returns:** `UserSettings` — The UserSettings singleton instance.

### warn

**Signature:** `warn(params: Tuple): ()`

Behaves identically to Luau's print function, except the output is styled
as a warning, with yellow text and a timestamp. This function accepts any
number of arguments, and will attempt to convert them into strings which
will then be joined together with spaces between them.

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `params` | `Tuple` |  | This function accepts any number of arguments, and will attempt to convert them into strings which will then be joined together with spaces between them. |

**Returns:** `()`

### delay *(deprecated)*

**Signature:** `delay(delayTime: number, callback: function): ()`

> **Deprecated:** This method has been superseded by [task.delay()](/docs/reference/engine/globals/task.md) and should not be used for future work.

Schedules a function to be executed after `delayTime` seconds have passed,
without yielding the current thread. This function allows multiple Luau
threads to be executed in parallel from the same stack. The delay will
have a minimum duration of 29 milliseconds, but this minimum may be higher
depending on the target framerate and various throttling conditions. If
the `delayTime` parameter is not specified, the minimum duration will be
used.

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `delayTime` | `number` |  | The amount of time that this function will be queued before being executed. |
| `callback` | `function` |  | The function that will be executed once `delayTime` seconds have passed. |

**Returns:** `()`

### DebuggerManager *(deprecated)*

**Signature:** `DebuggerManager(): DebuggerManager`

> **Deprecated:** The `DebuggerManager` is obsolete and serves little to no use case for developers.

Returns the legacy `DebuggerManager` class which acts as an interface for
Roblox's Luau debugger feature.

This function is not recognized by Luau's analysis tool and will raise an
undefined global warning.

**Returns:** `DebuggerManager` — The DebuggerManager singleton instance.

### elapsedTime *(deprecated)*

**Signature:** `elapsedTime(): number`

Returns how much time has elapsed since the current instance of Roblox was
started. In Roblox Studio, this begins counting up from the moment Roblox
Studio starts running, not just when opening a place.

**Returns:** `number` — The elapsed time, in seconds, since the current Roblox instance
started running.

### printidentity *(deprecated)*

**Signature:** `printidentity(prefix?: string): ()`

Prints `Current identity is [ID]` to the output, where [ID] corresponds to
the current thread's security context level.

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `prefix` | `string` | `Current identity is` | A custom string to print before the identity number; if omitted, defaults to "Current identity is". |

**Returns:** `()`

### spawn *(deprecated)*

**Signature:** `spawn(callback: function): ()`

> **Deprecated:** This method has been superseded by [task.spawn()](/docs/reference/engine/globals/task.md) and should not be used for future work.

Runs the specified callback function in a separate thread, without
yielding the current thread.

The function will be executed the next time Roblox's Task Scheduler runs
an update cycle. This delay will take at least 29 milliseconds but can
arbitrarily take longer, depending on the target framerate and various
throttling conditions.

The callback function is invoked with two arguments:

1. The first being the amount of time which elapsed from when spawn was
   called to when the function was invoked.
2. The second being equivalent to elapsedTime() or roughly how long the
   engine has been running.

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `callback` | `function` |  | The function that will be executed. |

**Returns:** `()`

**Spawn**

Demonstrates the `spawn` global.

```lua
spawn(print) -- 0.0079617658390703 451.55683163643
```

### stats *(deprecated)*

**Signature:** `stats(): Stats`

Returns the [Stats](/docs/reference/engine/classes/Stats.md) service. It is preferred that developers use
[ServiceProvider:GetService()](/docs/reference/engine/classes/ServiceProvider.md) to retrieve it instead.

**Returns:** `Stats` — The Stats service instance.

### version *(deprecated)*

**Signature:** `version(): string`

Returns the current version of Roblox as a string. The integers in the
version string are separated by periods, and each integers represent the
following, in order:

- Generation - The current generation of the application shell that is
  hosting the client.
- Version - The current release version of Roblox.
- Patch - The current patch number for this version of Roblox.
- Commit - The ID of the last internal commit that was accepted into this
  version of the client.

**Returns:** `string` — A period-separated version string in the format
"generation.version.patch.commit".

### wait *(deprecated)*

**Signature:** `wait(seconds?: number): number, number`

> **Deprecated:** This method has been superseded by [task.wait()](/docs/reference/engine/globals/task.md) and should not be used for future work.

Yields the current thread until the specified amount of seconds have
elapsed.

The delay will have a minimum duration of 29 milliseconds, but this
minimum may be higher depending on the target framerate and various
throttling conditions. If the `seconds` parameter is not specified, the
minimum duration will be used. This function returns:

- Actual time yielded (in seconds).
- Total time since the software was initialized (in seconds).

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `seconds` | `number` | `0.03` | Specifies how long the thread should yield for. |

**Returns:** `number`, `number` — The actual time yielded, in seconds. The total time elapsed since the engine started, in seconds.

### ypcall *(deprecated)*

**Signature:** `ypcall(f: function, args: Tuple): bool, Variant`

Legacy function to work around an old task scheduling limitation of
[LuaGlobals.pcall()](/docs/reference/engine/globals/LuaGlobals.md); should not be used for new work (use
[LuaGlobals.pcall()](/docs/reference/engine/globals/LuaGlobals.md) instead).

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `f` | `function` |  | The function to be called in protected mode. |
| `args` | `Tuple` |  | Additional arguments to pass to the function. |

**Returns:** `bool`, `Variant` — Whether the function executed successfully without raising an error. The return values of the function on success, or the error message on
failure.