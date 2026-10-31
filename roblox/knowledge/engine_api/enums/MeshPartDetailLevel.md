---
name: MeshPartDetailLevel
last_updated: 2026-10-30T19:55:54Z
type: enum
summary: "The level of detail of `MeshParts` displayed in Studio."
---

# MeshPartDetailLevel

The level of detail of `MeshParts` displayed in Studio.

**Type:** enum

## Description

The level of detail of `MeshParts` displayed in Studio. Used to visually
verify the quality of MeshParts at lower level of detail at close range.
Level01 being the highest detail and Level04 being the lowest detail.

## Items

| Name | Value | Description |
|------|-------|-------------|
| `DistanceBased` | 0 | Select level of detail based on distance (default behavior as in game). |
| `Level00` | 1 | Forces MeshParts to render at LOD index 0, the finest detail level. |
| `Level01` | 2 | Highest level of detail. |
| `Level02` | 3 | Second highest level of detail. |
| `Level03` | 4 | Third highest level of detail. |
| `Level04` | 5 | Lowest level of detail. |
| `Level05` | 6 | Forces MeshParts to render at LOD index 5. |
| `Level06` | 7 | Forces MeshParts to render at LOD index 6. |
| `Level07` | 8 | Forces MeshParts to render at LOD index 7. |
| `Level08` | 9 | Forces MeshParts to render at LOD index 8. |
| `Level09` | 10 | Forces MeshParts to render at LOD index 9, the coarsest available. |