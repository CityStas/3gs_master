---
name: PlayerCharacterDestroyBehavior
last_updated: 2026-10-30T19:55:54Z
type: enum
summary: "Controls destruction behavior when a player character is removed."
---

# PlayerCharacterDestroyBehavior

Controls destruction behavior when a player character is removed.

**Type:** enum

## Description

Controls whether the engine automatically calls `Destroy()` on a player's old
character when it is replaced and on the `Player` object when the player
leaves. This enum is used by [Workspace.PlayerCharacterDestroyBehavior](/docs/reference/engine/classes/Workspace.md).

## Items

| Name | Value | Description |
|------|-------|-------------|
| `Default` | 0 | Uses the engine-default behavior. |
| `Disabled` | 1 | Automatic `Destroy()` calls on character replacement and player removal are disabled. |
| `Enabled` | 2 | The engine automatically calls `Destroy()` on old characters when they are replaced (for example, on respawn) and on `Player` objects when players leave. |