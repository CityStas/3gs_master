---
name: AvatarSettingsLegacyCollisionMode
last_updated: 2026-10-30T19:55:54Z
type: enum
summary: "Determines which legacy collision geometry is applied to R15 avatars when AvatarSettingsCollisionMode is set to Legacy."
---

# AvatarSettingsLegacyCollisionMode

Determines which legacy collision geometry is applied to R15 avatars when
[AvatarSettingsCollisionMode](/docs/reference/engine/enums/AvatarSettingsCollisionMode.md) is set to Legacy.

**Type:** enum

## Description

When the avatar collision rules' `CollisionMode` is set to
[Legacy](/docs/reference/engine/enums/AvatarSettingsCollisionMode.md), this enum selects which collision
strategy the engine uses for R15 characters. `InnerBoxColliders` replaces each
mesh part's physics data with inner-box geometry derived from the standard R15
scaling model, while `R6Colliders` creates six invisible box parts that
approximate the classic R6 body shape.

## Items

| Name | Value | Description |
|------|-------|-------------|
| `R6Colliders` | 0 | Creates six invisible box collider parts welded to R15 limbs to approximate classic R6 collision geometry. The engine spawns six invisible [Part](/docs/reference/engine/classes/Part.md) instances (head, torso, left arm, right arm, left leg, right leg) parented to the character and welded to the corresponding R15 body parts. All original R15 mesh parts have their [BasePart.CanCollide](/docs/reference/engine/classes/BasePart.md), [BasePart.CanTouch](/docs/reference/engine/classes/BasePart.md), and [BasePart.CanQuery](/docs/reference/engine/classes/BasePart.md) disabled and are made massless; only the HumanoidRootPart retains mass so it remains the physics assembly root. |
| `InnerBoxColliders` | 1 | Overrides each R15 mesh part's collision physics with inner-box geometry derived from the standard R15 scaling model. The engine recalculates every [MeshPart](/docs/reference/engine/classes/MeshPart.md) in the character with collision data from the default R15 model's bounding dimensions, producing tighter collision volumes that follow the avatar's proportions without adding extra parts. This is the default value of `LegacyCollisionMode`. |