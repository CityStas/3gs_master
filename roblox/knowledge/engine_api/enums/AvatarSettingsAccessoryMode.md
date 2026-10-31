---
name: AvatarSettingsAccessoryMode
last_updated: 2026-10-30T19:55:54Z
type: enum
summary: "Determines whether `AvatarAccessoryRules` enforces custom size limits on rigid accessories worn by player avatars."
---

# AvatarSettingsAccessoryMode

Determines whether `AvatarAccessoryRules` enforces custom size limits on rigid
accessories worn by player avatars.

**Type:** enum

## Description

Determines whether `AvatarAccessoryRules` enforces custom size limits on rigid
(non-layered) accessories worn by player avatars in the experience. Used by
`AccessoryMode`, which defaults to
[AvatarSettingsAccessoryMode.PlayerChoice](/docs/reference/engine/enums/AvatarSettingsAccessoryMode.md). When set to
[AvatarSettingsAccessoryMode.CustomLimit](/docs/reference/engine/enums/AvatarSettingsAccessoryMode.md), the engine evaluates each
rigid accessory against `LimitBounds` and applies the enforcement strategy in
`LimitMethod`.

## Items

| Name | Value | Description |
|------|-------|-------------|
| `PlayerChoice` | 0 | No custom size limits are applied to rigid accessories; the player's own accessory choices are displayed without modification. |
| `CustomLimit` | 1 | The experience enforces custom size limits on rigid accessories using the LimitBounds and LimitMethod properties of `AvatarAccessoryRules`. |