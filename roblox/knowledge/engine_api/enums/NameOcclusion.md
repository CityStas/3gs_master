---
name: NameOcclusion
last_updated: 2026-10-30T19:55:54Z
type: enum
summary: "The NameOcclusion Enum is used to set the Humanoid.NameOcclusion property."
---

# NameOcclusion

The NameOcclusion Enum is used to set the [Humanoid.NameOcclusion](/docs/reference/engine/classes/Humanoid.md)
property.

**Type:** enum

## Description

`NameOcclusion` controls whether overhead name labels on [Humanoid](/docs/reference/engine/classes/Humanoid.md)
characters are hidden when solid geometry blocks the line of sight between the
viewer and the character. When the local player's
[Humanoid.NameOcclusion](/docs/reference/engine/classes/Humanoid.md) is set to `EnemyOcclusion` or `OccludeAll`, the
engine performs a raycast; if the character's head is behind a solid part, the
name label is not rendered for that frame. Setting the value to `NoOcclusion`
skips the raycast entirely and names are always visible regardless of
intervening geometry.

## Items

| Name | Value | Description |
|------|-------|-------------|
| `NoOcclusion` | 0 | Do not occlude (hide) any humanoid names. |
| `EnemyOcclusion` | 1 | Occlude (hide) all enemy humanoid names. |
| `OccludeAll` | 2 | Occlude (hide) all humanoid names. |