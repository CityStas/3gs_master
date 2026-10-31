---
name: AdornShading
last_updated: 2026-10-30T19:55:54Z
type: enum
summary: "Determines the shading material and render pass used to draw a handle adornment."
---

# AdornShading

Determines the shading material and render pass used to draw a handle
adornment.

**Type:** enum

## Description

Used by the `Shading` property on handle adornments
([BoxHandleAdornment](/docs/reference/engine/classes/BoxHandleAdornment.md), [SphereHandleAdornment](/docs/reference/engine/classes/SphereHandleAdornment.md),
[CylinderHandleAdornment](/docs/reference/engine/classes/CylinderHandleAdornment.md), [ConeHandleAdornment](/docs/reference/engine/classes/ConeHandleAdornment.md),
[PyramidHandleAdornment](/docs/reference/engine/classes/PyramidHandleAdornment.md)) to control whether the adornment is drawn
unlit or lit by the scene, and whether it renders through occluding geometry
or on top of everything.

## Items

| Name | Value | Description |
|------|-------|-------------|
| `Default` | 0 | Draws the adornment unlit and occluded by scene geometry like an ordinary world object. |
| `Shaded` | 1 | Draws the adornment lit by scene lighting and occluded by scene geometry. |
| `XRay` | 2 | Draws the adornment unlit and visible through geometry that would otherwise occlude it. |
| `XRayShaded` | 3 | Draws the adornment lit by scene lighting and visible through geometry that would otherwise occlude it. |
| `AlwaysOnTop` | 4 | Draws the adornment unlit on top of all other geometry with no depth testing. |