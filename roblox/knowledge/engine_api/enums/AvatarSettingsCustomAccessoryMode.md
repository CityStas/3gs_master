---
name: AvatarSettingsCustomAccessoryMode
last_updated: 2026-10-30T19:55:54Z
type: enum
summary: "Determines whether `AvatarAccessoryRules` replaces player accessories with experience-defined custom accessories."
---

# AvatarSettingsCustomAccessoryMode

Determines whether `AvatarAccessoryRules` replaces player accessories with
experience-defined custom accessories.

**Type:** enum

## Description

Determines whether `AvatarAccessoryRules` replaces the player's rigid
accessories with experience-defined custom accessories. Used by
`CustomAccessoryMode`, which defaults to
[AvatarSettingsCustomAccessoryMode.PlayerChoice](/docs/reference/engine/enums/AvatarSettingsCustomAccessoryMode.md). When set to
[AvatarSettingsCustomAccessoryMode.CustomAccessories](/docs/reference/engine/enums/AvatarSettingsCustomAccessoryMode.md), the engine removes
existing player accessories in each enabled slot and replaces them with the
asset IDs specified by the per-slot `Custom*AccessoryEnabled` and
`Custom*AccessoryId` properties on `AvatarAccessoryRules`.

## Items

| Name | Value | Description |
|------|-------|-------------|
| `PlayerChoice` | 0 | No custom accessory replacement is applied; the player's own accessory choices are displayed without modification. |
| `CustomAccessories` | 1 | The experience replaces player accessories with custom accessories defined by the per-slot properties on `AvatarAccessoryRules`. |