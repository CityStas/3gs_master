---
name: DigitsRigDescriptionSide
last_updated: 2026-10-30T19:55:54Z
type: enum
summary: "Specifies which hand side a DigitsRigDescription instance is assigned to."
---

# DigitsRigDescriptionSide

Specifies which hand side a [DigitsRigDescription](/docs/reference/engine/classes/DigitsRigDescription.md) instance is assigned
to.

**Type:** enum

## Description

Identifies the hand that a [DigitsRigDescription](/docs/reference/engine/classes/DigitsRigDescription.md) maps to within a
character rig. The animation system routes finger-joint data by this value; an
instance whose [DigitsRigDescription.Side](/docs/reference/engine/classes/DigitsRigDescription.md) is
[DigitsRigDescriptionSide.None](/docs/reference/engine/enums/DigitsRigDescriptionSide.md) is skipped. Defaults to
[DigitsRigDescriptionSide.None](/docs/reference/engine/enums/DigitsRigDescriptionSide.md).

## Items

| Name | Value | Description |
|------|-------|-------------|
| `None` | 0 | The [DigitsRigDescription](/docs/reference/engine/classes/DigitsRigDescription.md) has not been assigned to a hand side and is skipped by the animation system. |
| `Left` | 1 | The [DigitsRigDescription](/docs/reference/engine/classes/DigitsRigDescription.md) is assigned to the left hand. |
| `Right` | 2 | The [DigitsRigDescription](/docs/reference/engine/classes/DigitsRigDescription.md) is assigned to the right hand. |