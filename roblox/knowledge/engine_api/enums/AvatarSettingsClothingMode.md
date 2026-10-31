---
name: AvatarSettingsClothingMode
last_updated: 2026-10-30T19:55:54Z
type: enum
summary: "Determines whether the experience applies a spatial bounding limit to layered clothing on player characters."
---

# AvatarSettingsClothingMode

Determines whether the experience applies a spatial bounding limit to layered
clothing on player characters.

**Type:** enum

## Description

Determines whether the experience applies a spatial bounding limit to layered
clothing on player characters. Used by `ClothingMode` to control how far
layered clothing accessories can extend from the character body. When set to
[AvatarSettingsClothingMode.CustomLimit](/docs/reference/engine/enums/AvatarSettingsClothingMode.md), the engine reads `LimitBounds`
and clips layered clothing deformation to those bounds. Defaults to
[AvatarSettingsClothingMode.PlayerChoice](/docs/reference/engine/enums/AvatarSettingsClothingMode.md).

## Items

| Name | Value | Description |
|------|-------|-------------|
| `PlayerChoice` | 0 | No spatial limit is applied to layered clothing; the player's layered clothing accessories deform without a bounding constraint. |
| `CustomLimit` | 1 | Applies a custom spatial limit to layered clothing based on `LimitBounds`. |