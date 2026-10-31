---
name: LocationType
last_updated: 2026-10-30T19:55:54Z
type: enum
summary: "Specifies how `HeatmapService` determines a player's representative world position for heatmap data collection."
---

# LocationType

Specifies how `HeatmapService` determines a player's representative world
position for heatmap data collection.

**Type:** enum

## Description

Controls which point in 3D space is sampled as a player's location when
`HeatmapService` records positional heatmap events. The value is stored per
[Player](/docs/reference/engine/classes/Player.md) and defaults to [LocationType.Character](/docs/reference/engine/enums/LocationType.md). See the items
below for each sampling mode.

## Items

| Name | Value | Description |
|------|-------|-------------|
| `Character` | 0 | Use the player's character model world position as the heatmap location (default). |
| `Camera` | 1 | Use the current workspace camera's world position as the player's heatmap location. |
| `ObjectPosition` | 2 | Use the world position of a configured target object as the player's heatmap location. |