---
name: AvatarSettingsAnimationPacksMode
last_updated: 2026-10-30T19:55:54Z
type: enum
summary: "Determines which base animation pack is applied to avatar characters, controlling whether players use their own equipped animations or the experience forces a standard R15 or R6 animation set."
---

# AvatarSettingsAnimationPacksMode

Determines which base animation pack is applied to avatar characters,
controlling whether players use their own equipped animations or the
experience forces a standard R15 or R6 animation set.

**Type:** enum

## Description

Determines which base animation pack (locomotion assets such as run, walk,
fall, jump, idle, swim, swim idle, and climb) is applied to avatar characters.
This is the type of `AvatarAnimationRules.AnimationPacksMode`, which defaults
to [AvatarSettingsAnimationPacksMode.PlayerChoice](/docs/reference/engine/enums/AvatarSettingsAnimationPacksMode.md).

## Items

| Name | Value | Description |
|------|-------|-------------|
| `PlayerChoice` | 0 | The player's own equipped animation pack is used. The character's Animate script supplies the animations without experience-level overrides. |
| `StandardR15` | 1 | The experience forces the standard R15 animation pack on all characters, overriding player-equipped animations with a fixed set of R15 locomotion clips. |
| `StandardR6` | 2 | The experience forces the standard R6 animation pack on all (R15) characters, overriding player-equipped animations with a fixed set of R6-style locomotion clips plus additional R6-style emote and tool animations. |