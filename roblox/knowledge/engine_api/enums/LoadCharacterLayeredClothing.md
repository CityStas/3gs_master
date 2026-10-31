---
name: LoadCharacterLayeredClothing
last_updated: 2026-10-30T19:55:54Z
type: enum
summary: "Indicates whether characters spawning into an experience will have layered clothing accessories equipped on them."
---

# LoadCharacterLayeredClothing

Indicates whether characters spawning into an experience will have layered
clothing accessories equipped on them.

**Type:** enum

## Description

Indicates whether characters spawning into an experience will have layered
clothing accessories equipped on them (Although
[MeshPartHeadsAndAccessories](/docs/reference/engine/enums/MeshPartHeadsAndAccessories.md) also need to be enabled). This is set in
[StarterPlayer.LoadCharacterLayeredClothing](/docs/reference/engine/classes/StarterPlayer.md).

## Items

| Name | Value | Description |
|------|-------|-------------|
| `Default` | 0 | The behavior of the default setting is not constant. It can mean Disabled or Enabled depending on what the global back-end flag settings are currently. |
| `Disabled` | 1 | This means layered clothing will not be equipped on characters in the experience. |
| `Enabled` | 2 | This means layered clothing will be equipped on characters in the experience (Although [MeshPartHeadsAndAccessories](/docs/reference/engine/enums/MeshPartHeadsAndAccessories.md) also need to be enabled for the experience). |