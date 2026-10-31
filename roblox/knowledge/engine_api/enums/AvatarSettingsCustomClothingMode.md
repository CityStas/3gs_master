---
name: AvatarSettingsCustomClothingMode
last_updated: 2026-10-30T19:55:54Z
type: enum
summary: "Determines whether an experience overrides a player's classic 2D or layered 3D clothing with creator-specified assets or preserves the player's own clothing choices."
---

# AvatarSettingsCustomClothingMode

Determines whether an experience overrides a player's classic 2D or layered 3D
clothing with creator-specified assets or preserves the player's own clothing
choices.

**Type:** enum

## Description

Determines whether the classic 2D clothing or layered 3D clothing worn by
player avatars in an experience is controlled by the creator or left to each
player's own selection. Used by `AvatarClothingRules.CustomClothingMode`
within `AvatarSettings`.

When set to [AvatarSettingsCustomClothingMode.CustomClothing](/docs/reference/engine/enums/AvatarSettingsCustomClothingMode.md), the engine
applies the asset IDs from the `AvatarClothingRules` custom clothing
properties to each player's [HumanoidDescription](/docs/reference/engine/classes/HumanoidDescription.md) on join, replacing the
player's equipped clothing.

## Items

| Name | Value | Description |
|------|-------|-------------|
| `PlayerChoice` | 0 | Players keep their own clothing selections. The experience does not override clothing assets. This is the default value. |
| `CustomClothing` | 1 | The experience enforces creator-specified clothing assets from `AvatarClothingRules`, overriding each player's own equipped clothing. |