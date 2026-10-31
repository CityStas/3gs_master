---
name: AvatarSettingsAppearanceMode
last_updated: 2026-10-30T19:55:54Z
type: enum
summary: "Determines how the avatar's body-part appearance is sourced in an experience that uses `AvatarBodyRules`."
---

# AvatarSettingsAppearanceMode

Determines how the avatar's body-part appearance is sourced in an experience
that uses `AvatarBodyRules`.

**Type:** enum

## Description

Used by `AppearanceMode` to control whether players retain their own avatar
body parts or the experience overrides them with custom assets. Defaults to
[AvatarSettingsAppearanceMode.PlayerChoice](/docs/reference/engine/enums/AvatarSettingsAppearanceMode.md).

When set to [AvatarSettingsAppearanceMode.CustomParts](/docs/reference/engine/enums/AvatarSettingsAppearanceMode.md), individual body
parts (head, face, torso, arms, legs, eyebrows, eyelashes, mood) can each be
independently enabled and assigned a custom asset ID. When set to
[AvatarSettingsAppearanceMode.CustomBody](/docs/reference/engine/enums/AvatarSettingsAppearanceMode.md), the entire body is replaced as
a single unit using `CustomBodyType` and `CustomBodyBundleId`.

## Items

| Name | Value | Description |
|------|-------|-------------|
| `PlayerChoice` | 0 | Players keep their own avatar body parts; the experience does not override any body-part assets. |
| `CustomParts` | 1 | The experience overrides individual body parts (head, face, torso, arms, legs) using per-part asset IDs and enablement settings on `AvatarBodyRules`. |
| `CustomBody` | 2 | The experience replaces the avatar's entire body as a single unit, using `CustomBodyType` and `CustomBodyBundleId`. |