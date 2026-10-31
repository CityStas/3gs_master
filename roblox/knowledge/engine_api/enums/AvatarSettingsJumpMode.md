---
name: AvatarSettingsJumpMode
last_updated: 2026-10-30T19:55:54Z
type: enum
summary: "Determines whether the avatar jump setting for an experience is configured using jump height (studs) or jump power (force)."
---

# AvatarSettingsJumpMode

Determines whether the avatar jump setting for an experience is configured
using jump height (studs) or jump power (force).

**Type:** enum

## Description

Determines whether the avatar jump setting for an experience is configured
using jump height (in studs) or jump power (as an upward force). Maps to
[Humanoid.UseJumpPower](/docs/reference/engine/classes/Humanoid.md): [AvatarSettingsJumpMode.JumpHeight](/docs/reference/engine/enums/AvatarSettingsJumpMode.md) sets
`UseJumpPower` to false so that [Humanoid.JumpHeight](/docs/reference/engine/classes/Humanoid.md) is used, while
[AvatarSettingsJumpMode.JumpPower](/docs/reference/engine/enums/AvatarSettingsJumpMode.md) sets `UseJumpPower` to true so that
[Humanoid.JumpPower](/docs/reference/engine/classes/Humanoid.md) is used.

## Items

| Name | Value | Description |
|------|-------|-------------|
| `JumpHeight` | 0 | The avatar jump is configured using [Humanoid.JumpHeight](/docs/reference/engine/classes/Humanoid.md), which specifies the target jump height in studs. Corresponds to [Humanoid.UseJumpPower](/docs/reference/engine/classes/Humanoid.md) being false. |
| `JumpPower` | 1 | The avatar jump is configured using [Humanoid.JumpPower](/docs/reference/engine/classes/Humanoid.md), which applies an upward force to the character. Corresponds to [Humanoid.UseJumpPower](/docs/reference/engine/classes/Humanoid.md) being true. |