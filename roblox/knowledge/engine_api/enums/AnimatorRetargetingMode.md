---
name: AnimatorRetargetingMode
last_updated: 2026-10-30T19:55:54Z
type: enum
summary: "Animation Retargeting setting."
---

# AnimatorRetargetingMode

Animation Retargeting setting.

**Type:** enum

## Description

The AnimatorRetargetingMode Enum describes the setting for Animation
Retargeting. Retargeting adapts animations to various character rigs based on
their proportions.

## Items

| Name | Value | Description |
|------|-------|-------------|
| `Default` | 0 | Retargeting in default state, opt-in initially but subject to change. |
| `Disabled` | 1 | Animation retargeting is off; animations play exactly as authored without adapting joint transforms to the character's body proportions. |
| `Enabled` | 2 | Animation retargeting is always active; the Animator adapts animations to the character's body proportions regardless of the platform default. |