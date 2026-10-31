---
name: Path2DControlPoint
last_updated: 2026-10-30T19:55:54Z
type: datatype
summary: "Stores the info for a single control point used with the Path2D instance."
---

# Path2DControlPoint

Stores the info for a single control point used with the [Path2D](/docs/reference/engine/classes/Path2D.md)
instance.

**Type:** datatype

## Description

The `Path2DControlPoint` data type represents a single control point used with
the [Path2D](/docs/reference/engine/classes/Path2D.md) instance.

## Constructors

### Path2DControlPoint.new

**Signature:** `Path2DControlPoint.new()`

Returns an empty [Path2DControlPoint](/docs/reference/engine/datatypes/Path2DControlPoint.md).

### Path2DControlPoint.new

**Signature:** `Path2DControlPoint.new(Position: UDim2)`

Returns a [Path2DControlPoint](/docs/reference/engine/datatypes/Path2DControlPoint.md) with the position set. This
constructor will set the tangents to default [UDim2](/docs/reference/engine/datatypes/UDim2.md) values.

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `Position` | `UDim2` |  | The [UDim2](/docs/reference/engine/datatypes/UDim2.md) position of the control point. |

### Path2DControlPoint.new

**Signature:** `Path2DControlPoint.new(Position: UDim2, Left Tangent: UDim2, Right Tangent: UDim2)`

Returns a [Path2DControlPoint](/docs/reference/engine/datatypes/Path2DControlPoint.md) with the position, left tangent,
and right tangent set.

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `Position` | `UDim2` |  | The [UDim2](/docs/reference/engine/datatypes/UDim2.md) position of the control point. |
| `Left Tangent` | `UDim2` |  | The [UDim2](/docs/reference/engine/datatypes/UDim2.md) left tangent of the control point. |
| `Right Tangent` | `UDim2` |  | The [UDim2](/docs/reference/engine/datatypes/UDim2.md) right tangent of the control point. |

## Properties

### Path2DControlPoint.Position

**Type:** `UDim2`

The position of the [Path2DControlPoint](/docs/reference/engine/datatypes/Path2DControlPoint.md) relative to the path's
container.

### Path2DControlPoint.LeftTangent

**Type:** `UDim2`

The left tangent of the [Path2DControlPoint](/docs/reference/engine/datatypes/Path2DControlPoint.md).

### Path2DControlPoint.RightTangent

**Type:** `UDim2`

The right tangent of the [Path2DControlPoint](/docs/reference/engine/datatypes/Path2DControlPoint.md).