---
name: TextureQueryType
last_updated: 2026-10-30T19:55:54Z
type: enum
summary: "Used to get memory information about textures."
---

# TextureQueryType

Used to get memory information about textures.

**Type:** enum

## Items

| Name | Value | Description |
|------|-------|-------------|
| `NonHumanoid` | 0 | Texture memory for objects other than [Humanoid](/docs/reference/engine/classes/Humanoid.md). |
| `NonHumanoidOrphaned` | 1 | Unreferenced texture memory for objects other than [Humanoid](/docs/reference/engine/classes/Humanoid.md). |
| `Humanoid` | 2 | Texture memory for [Humanoid](/docs/reference/engine/classes/Humanoid.md). |
| `HumanoidOrphaned` | 3 | Unreferenced texture memory for [Humanoid](/docs/reference/engine/classes/Humanoid.md). |