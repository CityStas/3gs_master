---
name: FormFactor
last_updated: 2026-10-30T19:55:54Z
type: enum
summary: "Deprecated enum that previously controlled the minimum size and resize increment of a FormFactorPart along each axis."
---

# FormFactor

Deprecated enum that previously controlled the minimum size and resize
increment of a [FormFactorPart](/docs/reference/engine/classes/FormFactorPart.md) along each axis.

**Type:** enum

## Description

The FormFactor Enum for [FormFactorPart.FormFactor](/docs/reference/engine/classes/FormFactorPart.md).

Minimum size along a given axis is 1 \* RateOfIncrease for that axis, except
in the case of the "Custom" FormFactor, which has a minimum size of 0.2 along
all axes.

## Items

| Name | Value | Description |
|------|-------|-------------|
| `Symmetric` | 0 | Increases by a rate of 1 along all axes. |
| `Brick` | 1 | Increases by a rate of 1 along the x- and z- axes, 1.2 along the y-axis. |
| `Plate` | 2 | Increases by a rate of 1 along the x- and z- axes, 0.4 along the y-axis. |
| `Custom` | 3 | Increases by a rate as low as .001 along all axes. |