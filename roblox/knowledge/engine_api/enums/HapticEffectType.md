---
name: HapticEffectType
last_updated: 2026-10-30T19:55:54Z
type: enum
summary: "Enum used alongside HapticEffect.Type."
---

# HapticEffectType

Enum used alongside [HapticEffect.Type](/docs/reference/engine/classes/HapticEffect.md).

**Type:** enum

## Items

| Name | Value | Description |
|------|-------|-------------|
| `Custom` | 0 | Allows for application of a custom haptic waveform through the [HapticEffect:SetWaveformKeys()](/docs/reference/engine/classes/HapticEffect.md) method. |
| `UIHover` | 1 | Useful for when a player browses over an object (often a UI object) without the intention of triggering its action; it can also alert the player that they have browsed over an interactable object. This effect type is subtle and does not disrupt the gameplay experience. |
| `UIClick` | 2 | Useful for when a player has selected an object (often a UI object) with the intention of triggering its action. This effect type is crisp and it provides immediate feedback without being overwhelming. |
| `UINotification` | 3 | Useful for when there is an inbound message that should draw the player's attention away from their current gameplay and prompt them that the notification requires immediate attention or action. |
| `GameplayExplosion` | 4 | Useful to signify a large-scale physics event that triggers impact across a large portion of a given scene. This effect is high intensity in order to represent the magnitude of the impact and it lingers for a longer period of time than `GameplayCollision`. |
| `GameplayCollision` | 5 | This effect is a large immediate rumble that dies down quickly, useful to signify a clear and purposeful impact between objects. |