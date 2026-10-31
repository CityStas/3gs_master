---
name: PartType
last_updated: 2026-10-30T19:55:54Z
type: enum
summary: "Controls the Part.Shape of an object."
---

# PartType

Controls the [Part.Shape](/docs/reference/engine/classes/Part.md) of an object.

**Type:** enum

## Description

The **PartType** enum specifies the primitive geometry shape of a
[Part](/docs/reference/engine/classes/Part.md), assigned through its [Shape](/docs/reference/engine/classes/Part.md) property. A new
[Part](/docs/reference/engine/classes/Part.md) defaults to `Block`. The five available shapes are Ball (sphere),
Block (rectangular prism), Cylinder (oriented along the X axis), Wedge (a ramp
with a slope on one face), and CornerWedge (a ramp with slopes on two
perpendicular faces).

## Items

| Name | Value | Description |
|------|-------|-------------|
| `Ball` | 0 | A spherical shape. |
| `Block` | 1 | A block shape. |
| `Cylinder` | 2 | A cylinder shape oriented along the **X** axis. |
| `Wedge` | 3 | A wedge shape with a slope on one side. |
| `CornerWedge` | 4 | A wedge shape with slopes on two sides. |