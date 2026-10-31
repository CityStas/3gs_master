---
name: InputType
last_updated: 2026-10-30T19:55:54Z
type: enum
summary: "The InputType Enum controls the SurfaceInputs of Part."
---

# InputType

The InputType Enum controls the SurfaceInputs of [Part](/docs/reference/engine/classes/Part.md).

**Type:** enum

## Description

The InputType Enum controls the SurfaceInputs of [Part](/docs/reference/engine/classes/Part.md). Several
parameters here are left-overs from 2005, before Roblox was a multiplayer
game, and are used by [Part.BackSurfaceInput](/docs/reference/engine/classes/Part.md),
[Part.BottomSurfaceInput](/docs/reference/engine/classes/Part.md), [Part.FrontSurfaceInput](/docs/reference/engine/classes/Part.md),
[Part.LeftSurfaceInput](/docs/reference/engine/classes/Part.md), [Part.RightSurfaceInput](/docs/reference/engine/classes/Part.md),
[Part.TopSurfaceInput](/docs/reference/engine/classes/Part.md).

## Items

| Name | Value | Description |
|------|-------|-------------|
| `NoInput` | 0 | Behaves like a weld and does nothing. |
| `Constant` | 12 | Rotate at a constant velocity of [BasePart](/docs/reference/engine/classes/BasePart.md) `ParamB`. |
| `Sin` | 13 | Rotate at a velocity of: `ParamA * math.sin(workspace.DistributedGameTime * ParamB)`, where [BasePart](/docs/reference/engine/classes/BasePart.md) `ParamA` determines the maximum speed at which the part spins, and [BasePart](/docs/reference/engine/classes/BasePart.md) `ParamB` determines how frequently it changes direction. |