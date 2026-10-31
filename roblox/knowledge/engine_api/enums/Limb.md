---
name: Limb
last_updated: 2026-10-30T19:55:54Z
type: enum
summary: "Describes which limb a particular Instance belongs to (assuming the Instance is part of a Humanoid)."
---

# Limb

Describes which limb a particular Instance belongs to (assuming the Instance
is part of a Humanoid).

**Type:** enum

## Description

Describes which limb a particular Instance belongs to (assuming the Instance
is part of a Humanoid). Passing an Instance to the Humanoid:GetLimb() function
will return the Limb for the Instance.

## Items

| Name | Value | Description |
|------|-------|-------------|
| `Head` | 0 | If the limb is a part of the Humanoid's Head. |
| `Torso` | 1 | If the limb is a part of the Humanoid's Torso. This includes UpperTorso and LowerTorso for R15 rigs. |
| `LeftArm` | 2 | If the limb is a part of the Humanoid's Left Arm. This includes UpperLeftArm, LowerLeftArm, and LeftHand for R15 rigs. |
| `RightArm` | 3 | If the limb is a part of the Humanoid's Right Arm. This includes UpperRightArm, LowerRightArm and RightHand for R15 rigs. |
| `LeftLeg` | 4 | If the limb is a part of the Humanoid's Left Leg. This includes UpperLeftLeg, LowerLeftLeg and LeftFoot for R15 rigs. |
| `RightLeg` | 5 | If the limb is a part of the Humanoid's Right Leg. This includes UpperRightLeg, LowerRightLeg, and RightFoot for R15 rigs. |
| `Unknown` | 6 | If a part is not a limb (e.g. running the [Humanoid:GetLimb()](/docs/reference/engine/classes/Humanoid.md) function and passing it an accessory which is a sibling of the Humanoid will return this value). |