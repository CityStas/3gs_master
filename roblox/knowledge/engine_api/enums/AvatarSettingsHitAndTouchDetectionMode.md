---
name: AvatarSettingsHitAndTouchDetectionMode
last_updated: 2026-10-30T19:55:54Z
type: enum
summary: "Determines whether hit detection and spatial queries use the individual body parts or the single collider when `AvatarCollisionRules.CollisionMode` is AvatarSettingsCollisionMode.SingleCollider."
---

# AvatarSettingsHitAndTouchDetectionMode

Determines whether hit detection and spatial queries use the individual body
parts or the single collider when `AvatarCollisionRules.CollisionMode` is
[AvatarSettingsCollisionMode.SingleCollider](/docs/reference/engine/enums/AvatarSettingsCollisionMode.md).

**Type:** enum

## Description

Determines whether [BasePart.CanTouch](/docs/reference/engine/classes/BasePart.md) (hit detection) and
[BasePart.CanQuery](/docs/reference/engine/classes/BasePart.md) (spatial queries) are routed to the individual
avatar body parts or to the single collider part. Only takes effect when
`AvatarCollisionRules.CollisionMode` is
[AvatarSettingsCollisionMode.SingleCollider](/docs/reference/engine/enums/AvatarSettingsCollisionMode.md); in other collision modes it
is ignored.

## Items

| Name | Value | Description |
|------|-------|-------------|
| `UseParts` | 0 | Individual avatar body parts handle `Touched` events and spatial queries (`CanTouch` and `CanQuery` enabled on body parts) while the single collider part has `CanTouch` and `CanQuery` disabled. This is the default value for `AvatarCollisionRules.HitAndTouchDetectionMode`. |
| `UseCollider` | 1 | The single collider part handles `Touched` events and spatial queries (`CanTouch` and `CanQuery` enabled on the collider) while all individual body parts have `CanTouch` and `CanQuery` disabled. |