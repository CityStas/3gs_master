---
name: AnimationPriority
last_updated: 2026-10-30T19:55:54Z
type: enum
summary: "The AnimationPriority Enum determines how concurrently-playing AnimationTracks contribute to the final animation."
---

# AnimationPriority

The AnimationPriority Enum determines how concurrently-playing AnimationTracks
contribute to the final animation.

**Type:** enum

## Description

When multiple [AnimationTracks](/docs/reference/engine/classes/AnimationTrack.md) are played concurrently
by the same [Animator](/docs/reference/engine/classes/Animator.md) and affect the same animated joints, the tracks
are evaluated in order from high to low priority, per joint, while the total
track weight sum remains less than 1.0. When the track weight sum reaches or
exceeds 1.0 for a joint, evaluation stops and no lower-priority tracks will be
evaluated for that joint. [AnimationTracks](/docs/reference/engine/classes/AnimationTrack.md) with the same
priority that are playing concurrently will blend proportional to their track
weights (normalized if the sum exceeds 1).

Higher priority animation will override lower priority ones per joint. The
priority order is:

1. **Action4**
2. **Action3**
3. **Action2**
4. **Action**
5. **Movement**
6. **Idle**
7. **Core**

Roblox's default character animations, including catalog animation bundles,
play at **Core** priority. **Idle** through **Action4** priority are for
developer use.

## Items

| Name | Value | Description |
|------|-------|-------------|
| `Idle` | 0 | (6) - Recommended priority for character idle animations. |
| `Movement` | 1 | (5) - Recommended priority for walk, run, swim, climb, and other locomotion animations. |
| `Action` | 2 | (4) - Recommended priority for character actions that must override idle and locomotion animations. |
| `Action2` | 3 | (3) - Action2 will override Action. |
| `Action3` | 4 | (2) - Action3 will override Action2. |
| `Action4` | 5 | (1) - Action4 is the highest priority available, overriding all other priority values. |
| `Core` | 1000 | (7) - Lowest priority, intended for use by Roblox default animations and catalog animation bundles. |