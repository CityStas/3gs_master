---
name: AvatarSettingsAccessoryLimitMethod
last_updated: 2026-10-30T19:55:54Z
type: enum
summary: "Determines how `AvatarAccessoryRules` enforces accessory size limits when an accessory exceeds the configured bounds."
---

# AvatarSettingsAccessoryLimitMethod

Determines how `AvatarAccessoryRules` enforces accessory size limits when an
accessory exceeds the configured bounds.

**Type:** enum

## Description

Determines how `AvatarAccessoryRules` enforces accessory size limits when an
accessory exceeds `LimitBounds`. Used by `LimitMethod`, which defaults to
[AvatarSettingsAccessoryLimitMethod.Remove](/docs/reference/engine/enums/AvatarSettingsAccessoryLimitMethod.md). Only takes effect when
`AccessoryMode` is [AvatarSettingsAccessoryMode.CustomLimit](/docs/reference/engine/enums/AvatarSettingsAccessoryMode.md).

## Items

| Name | Value | Description |
|------|-------|-------------|
| `Scale` | 0 | Scales down rigid accessories that exceed the configured bounds, or removes them if scaling would reduce them below minimum size thresholds. |
| `Remove` | 1 | Destroys any rigid accessory whose bounding box exceeds the configured bounds. |
| `PreviewScale` | 2 | Reports whether an accessory would be scaled or removed for exceeding the configured bounds without actually modifying it. |
| `PreviewRemove` | 3 | Reports whether an accessory would be removed for exceeding the configured bounds without actually destroying it. |