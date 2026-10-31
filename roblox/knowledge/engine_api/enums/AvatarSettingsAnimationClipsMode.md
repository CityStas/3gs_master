---
name: AvatarSettingsAnimationClipsMode
last_updated: 2026-10-30T19:55:54Z
type: enum
summary: "Determines whether avatar animation clips are defined by the experience or if they are determined by `AnimationPacksMode`."
---

# AvatarSettingsAnimationClipsMode

Determines whether avatar animation clips are defined by the experience or if
they are determined by `AnimationPacksMode`.

**Type:** enum

## Description

Determines whether custom experience-defined avatar animation clips override
the clips determined by the `AnimationPacksMode` setting. This enum is the
type of `AnimationClipsMode`, which defaults to
[AvatarSettingsAnimationClipsMode.PlayerChoice](/docs/reference/engine/enums/AvatarSettingsAnimationClipsMode.md).

## Items

| Name | Value | Description |
|------|-------|-------------|
| `PlayerChoice` | 0 | The clips determined by the `AnimationPacksMode` are used, without experience-level overrides. |
| `CustomClips` | 1 | The experience overrides individual animation clips using the per-clip enabled and ID properties on `AvatarAnimationRules` (for example, `CustomRunAnimationEnabled` and `CustomRunAnimationId`). Only clips whose enabled flag is true are replaced. |