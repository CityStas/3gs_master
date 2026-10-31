---
name: AvatarSettingsScaleMode
last_updated: 2026-10-30T19:55:54Z
type: enum
summary: "Determines whether the experience enforces a custom height range on player characters or allows players to spawn at their natural avatar height."
---

# AvatarSettingsScaleMode

Determines whether the experience enforces a custom height range on player
characters or allows players to spawn at their natural avatar height.

**Type:** enum

## Description

Determines whether the experience overrides player character height with a
creator-defined range or leaves it at the player's own avatar height. Used by
`ScaleMode`. When set to [AvatarSettingsScaleMode.CustomScale](/docs/reference/engine/enums/AvatarSettingsScaleMode.md), the
engine clamps character height to `CustomHeight` and applies layered clothing
bounds from the resulting body extents. Defaults to
[AvatarSettingsScaleMode.PlayerChoice](/docs/reference/engine/enums/AvatarSettingsScaleMode.md).

## Items

| Name | Value | Description |
|------|-------|-------------|
| `PlayerChoice` | 0 | Characters spawn at their natural avatar height without any experience-level height override. This is the default value. |
| `CustomScale` | 1 | The experience clamps the character's height to the range specified by `CustomHeight`, overriding the player's natural avatar height. |