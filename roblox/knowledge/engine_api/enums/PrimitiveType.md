---
name: PrimitiveType
last_updated: 2026-10-30T19:55:54Z
type: enum
summary: "Identifies the base primitive shape of a BasePart node within a CSG operation graph."
---

# PrimitiveType

Identifies the base primitive shape of a [BasePart](/docs/reference/engine/classes/BasePart.md) node within a CSG
operation graph.

**Type:** enum

## Description

Identifies the base primitive shape of a [BasePart](/docs/reference/engine/classes/BasePart.md) node within a CSG
(Constructive Solid Geometry) operation graph (`OperationGraph`). Used when
performing union, negate, and intersect operations to determine how each input
part's geometry is represented during the operation.

## Items

| Name | Value | Description |
|------|-------|-------------|
| `Null` | 0 | Sentinel value indicating no valid primitive shape; used for uninitialized or invalid nodes in a CSG operation graph. |
| `Ball` | 1 | A spherical primitive shape, corresponding to the ball/sphere geometry of a [Part](/docs/reference/engine/classes/Part.md). |
| `Cylinder` | 2 | A cylindrical primitive shape, corresponding to the cylinder geometry of a [Part](/docs/reference/engine/classes/Part.md). |
| `Block` | 3 | A box primitive shape, corresponding to the standard rectangular block geometry of a [Part](/docs/reference/engine/classes/Part.md); the default primitive type for new Part nodes in a CSG operation graph. |
| `Wedge` | 4 | A wedge primitive shape, corresponding to the geometry of a [WedgePart](/docs/reference/engine/classes/WedgePart.md). |
| `CornerWedge` | 5 | A corner wedge primitive shape, corresponding to the geometry of a [CornerWedgePart](/docs/reference/engine/classes/CornerWedgePart.md). |