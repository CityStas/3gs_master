---
name: Region3
last_updated: 2026-10-30T19:55:54Z
type: datatype
summary: "Describes a rectangular volume in 3D space."
---

# Region3

Describes a rectangular volume in 3D space.

**Type:** datatype

## Description

The [Region3](/docs/reference/engine/datatypes/Region3.md) data type describes a volume in 3D space similar to an
**axis-aligned rectangular prism**. It is commonly used with [Terrain](/docs/reference/engine/classes/Terrain.md)
functions and functions that detect parts within a volume, such as
[WorldRoot:FindPartsInRegion3()](/docs/reference/engine/classes/WorldRoot.md).

The prism's center is accessible using the [Region3.CFrame](/docs/reference/engine/datatypes/Region3.md) property
and the prism's size is accessible through the [Region3.Size](/docs/reference/engine/datatypes/Region3.md)
property. Note that the components of this property may be **negative**.

The [Region3:ExpandToGrid()](/docs/reference/engine/datatypes/Region3.md) method returns a new [Region3](/docs/reference/engine/datatypes/Region3.md)
whose bounds comply with a provided resolution value. The resulting volume may
be equal to or greater than the original volume, but never smaller.

See also:

- [Region3int16](/docs/reference/engine/datatypes/Region3int16.md)

## Constructors

### Region3.new

**Signature:** `Region3.new(min: Vector3, max: Vector3)`

Returns a new [Region3](/docs/reference/engine/datatypes/Region3.md) given the [Vector3](/docs/reference/engine/datatypes/Vector3.md) bounds of
the rectangular prism volume.

Note that the order of the provided bounds matters: by switching them, the
polarity of the size components will switch. It is possible to create a
[Region3](/docs/reference/engine/datatypes/Region3.md) with a **negative volume**.

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `min` | `Vector3` |  | The lower corner of the rectangular volume. |
| `max` | `Vector3` |  | The upper corner of the rectangular volume. |

## Properties

### Region3.CFrame

**Type:** `CFrame`

The [CFrame](/docs/reference/engine/datatypes/CFrame.md) representing the center position and orientation of
the [Region3](/docs/reference/engine/datatypes/Region3.md). The position component is the midpoint of the
`min` and `max` vectors passed to [Region3.new()](/docs/reference/engine/datatypes/Region3.md), computed as
`(min + max) / 2`. Because a [Region3](/docs/reference/engine/datatypes/Region3.md) is always axis-aligned,
the rotation component of the returned [CFrame](/docs/reference/engine/datatypes/CFrame.md) is always the
identity (no rotation). This property is read-only.

### Region3.Size

**Type:** `Vector3`

The size of the [Region3](/docs/reference/engine/datatypes/Region3.md) as a [Vector3](/docs/reference/engine/datatypes/Vector3.md), equal to
`max - min` from the constructor arguments. Individual components may be
**negative** if the corresponding component of `min` is greater than `max`
in the call to [Region3.new()](/docs/reference/engine/datatypes/Region3.md). This property is read-only.

## Methods

### Region3:ExpandToGrid

**Signature:** `Region3:ExpandToGrid(resolution: number): Region3`

Expands the [Region3](/docs/reference/engine/datatypes/Region3.md) based on the provided resolution and
returns the expanded [Region3](/docs/reference/engine/datatypes/Region3.md) aligned to the [Terrain](/docs/reference/engine/classes/Terrain.md)
voxel grid.

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `resolution` | `number` |  | The grid resolution to align the region bounds to, in studs. Must be a positive number. |

**Returns:** `Region3` — A new Region3 whose minimum bounds are floored and maximum bounds are
ceiled to the nearest multiple of `resolution`.