---
name: Region3int16
last_updated: 2026-10-30T19:55:54Z
type: datatype
summary: "Represents a Region3 stored as two boundaries as opposed to position and size components."
---

# Region3int16

Represents a Region3 stored as two boundaries as opposed to position and size
components.

**Type:** datatype

## Description

Not to be confused with [Region3](/docs/reference/engine/datatypes/Region3.md), a separate class that fulfills a
different purpose.

The [Region3int16](/docs/reference/engine/datatypes/Region3int16.md) data type represents a volume in 3D space similar
to an **axis-aligned rectangular prism**. It uses two [Vector3int16](/docs/reference/engine/datatypes/Vector3int16.md)
to store the volume's bounds in the `Min` and `Max` properties. It is
constructed using `Region3int16.new(Min, Max)`, given the two
[Vector3int16](/docs/reference/engine/datatypes/Vector3int16.md) bounds. This data type features no functions or
operations.

## Calculating Center and Size

This data type differs from [Region3](/docs/reference/engine/datatypes/Region3.md) in that it stores its bounds
directly, rather than through a center and size combination. Nonetheless, it
is possible to calculate these dimensions using `Min` and `Max`:

```lua
local region = Region3int16.new(Vector3int16.new(0, 0, -3), Vector3int16.new(4, 4, 4))
local size = region.Max - region.Min
local center = (region.Max + region.Min) / 2
```

## Conversion to Region3

The following function can be used to convert a Region3int16 into a similar
[Region3](/docs/reference/engine/datatypes/Region3.md). It does this by converting the `Min` and `Max` properties,
which are Vector3int16, into [Vector3](/docs/reference/engine/datatypes/Vector3.md) used with
[Region3.new()](/docs/reference/engine/datatypes/Region3.md).

```lua
local function Region3int16toRegion3(region16)
	return Region3.new(
		Vector3.new(region16.Min.X, region16.Min.Y, region16.Min.Z),
		Vector3.new(region16.Max.X, region16.Max.Y, region16.Max.Z)
	)
end
```

See also:

- [Region3](/docs/reference/engine/datatypes/Region3.md), a similar data type

## Constructors

### Region3int16.new

**Signature:** `Region3int16.new(min: Vector3int16, max: Vector3int16)`

Returns a new Region3int16 from the provided boundaries.

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `min` | `Vector3int16` |  | The lower bound of the region. |
| `max` | `Vector3int16` |  | The upper bound of the region. |

## Properties

### Region3int16.Min

**Type:** `Vector3int16`

The lower bound of the [Region3int16](/docs/reference/engine/datatypes/Region3int16.md), as passed to
[Region3int16.new()](/docs/reference/engine/datatypes/Region3int16.md).

### Region3int16.Max

**Type:** `Vector3int16`

The upper bound of the [Region3int16](/docs/reference/engine/datatypes/Region3int16.md), as passed to
[Region3int16.new()](/docs/reference/engine/datatypes/Region3int16.md).