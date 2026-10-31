---
name: RunContext
last_updated: 2026-10-30T19:55:54Z
type: enum
summary: "Controls the execution context of a Script, determining whether it runs as server, client, plugin, or legacy container-based code."
---

# RunContext

Controls the execution context of a [Script](/docs/reference/engine/classes/Script.md), determining whether it
runs as server, client, plugin, or legacy container-based code.

**Type:** enum

## Description

The `RunContext` enum is used with the [BaseScript.RunContext](/docs/reference/engine/classes/BaseScript.md) property
to specify the context in which a [Script](/docs/reference/engine/classes/Script.md) executes. The default value
is [RunContext.Legacy](/docs/reference/engine/enums/RunContext.md), which preserves the original container-based
behavior where a [Script](/docs/reference/engine/classes/Script.md) runs on the server and a [LocalScript](/docs/reference/engine/classes/LocalScript.md)
runs on the client depending on its placement in the instance hierarchy.

Setting a non-`Legacy` value allows a [Script](/docs/reference/engine/classes/Script.md) to run explicitly on the
server, client, or as plugin code, regardless of container placement.
[LocalScript](/docs/reference/engine/classes/LocalScript.md) objects cannot use this property — only [Script](/docs/reference/engine/classes/Script.md)
objects support non-`Legacy` run contexts.

Changing this property while the script is running terminates any active
threads and restarts the script under the new context if conditions permit.

## Items

| Name | Value | Description |
|------|-------|-------------|
| `Legacy` | 0 | Runs with legacy container-based behavior that depends on the script type, such as [LocalScript](/docs/reference/engine/classes/LocalScript.md) or [Script](/docs/reference/engine/classes/Script.md). |
| `Server` | 1 | Runs on the server. |
| `Client` | 2 | Runs on the client. |
| `Plugin` | 3 | Runs as a descendant of [Plugin](/docs/reference/engine/classes/Plugin.md) instances. |