---
name: CommandPermission
last_updated: 2026-10-30T19:55:54Z
type: enum
summary: "Specifies the minimum security permission level required to invoke a Studio command."
---

# CommandPermission

Specifies the minimum security permission level required to invoke a Studio
command.

**Type:** enum

## Description

Specifies the minimum security permission level a Lua execution context must
hold to invoke a Studio command registered through the plugin command system.
[CommandPermission.Plugin](/docs/reference/engine/enums/CommandPermission.md) is the standard permission for plugin scripts;
[CommandPermission.LocalUser](/docs/reference/engine/enums/CommandPermission.md) is the higher-privilege level reserved for
IDE-only APIs.

## Items

| Name | Value | Description |
|------|-------|-------------|
| `Plugin` | 0 | The command is accessible to scripts running at the standard Plugin security level. |
| `LocalUser` | 1 | The command requires the LocalUser security level, granting access to IDE-only APIs. |