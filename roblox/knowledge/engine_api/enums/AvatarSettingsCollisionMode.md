---
name: AvatarSettingsCollisionMode
last_updated: 2026-10-30T19:55:54Z
type: enum
summary: "Determines the collision geometry mode for avatars managed by `AvatarCollisionRules`."
---

# AvatarSettingsCollisionMode

Determines the collision geometry mode for avatars managed by
`AvatarCollisionRules`.

**Type:** enum

## Description

Determines the collision geometry mode for avatars managed by
`AvatarCollisionRules`. [AvatarSettingsCollisionMode.Default](/docs/reference/engine/enums/AvatarSettingsCollisionMode.md) uses each
body part's native collision geometry.
[AvatarSettingsCollisionMode.SingleCollider](/docs/reference/engine/enums/AvatarSettingsCollisionMode.md) replaces per-part collision
with a single box collider welded to the HumanoidRootPart.
[AvatarSettingsCollisionMode.Legacy](/docs/reference/engine/enums/AvatarSettingsCollisionMode.md) delegates to the
`LegacyCollisionMode` setting.

## Items

| Name | Value | Description |
|------|-------|-------------|
| `Default` | 0 | Each body part uses its native collision geometry. The HumanoidRootPart, UpperTorso, and LowerTorso collide while other parts do not. This is the default value for `CollisionMode`. |
| `SingleCollider` | 1 | A single box-shaped collider part replaces all per-part collision. The collider is welded to the HumanoidRootPart and sized by `SingleColliderSize` (default 2, 3, 1). All other parts become non-collidable and massless. |
| `Legacy` | 2 | Collision geometry is determined by `LegacyCollisionMode`, which selects either inner-box colliders or R6-style colliders. |