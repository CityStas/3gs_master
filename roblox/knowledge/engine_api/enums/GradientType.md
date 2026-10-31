---
name: GradientType
last_updated: 2026-10-30T19:55:54Z
type: enum
summary: "Used alongside UIGradient.Type to set the shape of the gradient."
---

# GradientType

Used alongside [UIGradient.Type](/docs/reference/engine/classes/UIGradient.md) to set the shape of the gradient.

**Type:** enum

## Description

Used alongside [UIGradient.Type](/docs/reference/engine/classes/UIGradient.md) to set the shape of the gradient as
linear, radial, elliptical, or conical.

## Items

| Name | Value | Description |
|------|-------|-------------|
| `Linear` | 0 | The color/transparency sequence transitions in a straight line across the element. The direction is controlled by [Rotation](/docs/reference/engine/classes/UIGradient.md) and the position by [Offset](/docs/reference/engine/classes/UIGradient.md). |
| `Radial` | 1 | The color/transparency sequence radiates outward from the element's center, optionally shifted by [Offset](/docs/reference/engine/classes/UIGradient.md). The radius is defined by the average of the element's width and height divided by two, effectively `(width+height)/4`. [Rotation](/docs/reference/engine/classes/UIGradient.md) has no effect on a radial gradient. |
| `Conical` | 2 | The color/transparency sequence sweeps clockwise around the center of the element, optionally shifted by [Offset](/docs/reference/engine/classes/UIGradient.md). [Rotation](/docs/reference/engine/classes/UIGradient.md) controls the starting angle of the sweep. |
| `Elliptical` | 3 | The color/transparency sequence radiates outward from the element's center in an ellipse, optionally shifted by [Offset](/docs/reference/engine/classes/UIGradient.md). The ellipse's horizontal and vertical radii are half the element's width and height, respectively, so the ellipse fits the element's bounds. [Rotation](/docs/reference/engine/classes/UIGradient.md) rotates the ellipse's axes. |