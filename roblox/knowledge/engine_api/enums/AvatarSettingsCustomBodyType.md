---
name: AvatarSettingsCustomBodyType
last_updated: 2026-10-30T19:55:54Z
type: enum
summary: "Determines whether an experience's custom body override is identified by individual asset references or by a single bundle ID."
---

# AvatarSettingsCustomBodyType

Determines whether an experience's custom body override is identified by
individual asset references or by a single bundle ID.

**Type:** enum

## Description

This enum is used by the `CustomBodyType` property to control how a custom
avatar body is specified when `AppearanceMode` is set to `CustomBody`. The
default value is [AvatarSettingsCustomBodyType.AvatarReference](/docs/reference/engine/enums/AvatarSettingsCustomBodyType.md).

When set to [AvatarSettingsCustomBodyType.AvatarReference](/docs/reference/engine/enums/AvatarSettingsCustomBodyType.md), the avatar
body is assembled from per-part asset IDs configured on `AvatarBodyRules`
(head, torso, arms, legs, etc.). When set to
[AvatarSettingsCustomBodyType.BundleId](/docs/reference/engine/enums/AvatarSettingsCustomBodyType.md), the entire body is sourced from
the bundle specified in `CustomBodyBundleId`.

## Items

| Name | Value | Description |
|------|-------|-------------|
| `AvatarReference` | 0 | The custom body is assembled from individual per-part asset references on `AvatarBodyRules`. This is the default value. |
| `BundleId` | 1 | The custom body is sourced from a single avatar bundle, identified by the `CustomBodyBundleId` property. |