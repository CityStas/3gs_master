---
name: CharacterControlMode
last_updated: 2026-10-30T19:55:54Z
type: enum
summary: "Specifies which character controller implementation an experience uses."
---

# CharacterControlMode

Specifies which character controller implementation an experience uses.

**Type:** enum

## Description

Controls the character controller selected by
[StarterPlayer.LuaCharacterController](/docs/reference/engine/classes/StarterPlayer.md).

## Items

| Name | Value | Description |
|------|-------|-------------|
| `Default` | 0 | Uses Roblox's default character controller selection. |
| `Legacy` | 1 | Uses the legacy character controller. |
| `NoCharacterController` | 2 | Does not load a character controller. |
| `LuaCharacterController` | 3 | Uses the Luau character controller. |