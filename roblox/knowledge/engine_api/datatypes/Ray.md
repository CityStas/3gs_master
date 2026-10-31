---
name: Ray
last_updated: 2026-10-30T19:55:54Z
type: datatype
summary: "Represents a line with a starting point that casts infinitely in a specific direction."
---

# Ray

Represents a line with a starting point that casts infinitely in a specific
direction.

**Type:** datatype

## Description

The [Ray](/docs/reference/engine/datatypes/Ray.md) data type represents a half-line, finite in one direction
but infinite in the other. It can be defined by a 3D point, where the line
originates from, and a direction vector, which is the direction it goes in.

## Constructors

### Ray.new

**Signature:** `Ray.new(Origin: Vector3, Direction: Vector3)`

Returns a new [Ray](/docs/reference/engine/datatypes/Ray.md) with given `Origin` and `Direction`.

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `Origin` | `Vector3` |  | The starting point of the ray in 3D space. |
| `Direction` | `Vector3` |  | The direction vector of the ray. Does not need to be a unit vector. |

## Properties

### Ray.Unit

**Type:** `Ray`

The [Ray](/docs/reference/engine/datatypes/Ray.md) with a normalized direction (the direction has a
magnitude of `1`).

### Ray.Origin

**Type:** `Vector3`

The position of the origin.

### Ray.Direction

**Type:** `Vector3`

The direction vector of the [Ray](/docs/reference/engine/datatypes/Ray.md).

## Methods

### Ray:ClosestPoint

**Signature:** `Ray:ClosestPoint(point: Vector3): Vector3`

Returns a [Vector3](/docs/reference/engine/datatypes/Vector3.md) projected onto the ray so that it is within
the [Ray](/docs/reference/engine/datatypes/Ray.md) line of sight.

**Note:** the [Ray](/docs/reference/engine/datatypes/Ray.md) **must** be a unit ray for this method to
behave as expected!

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `point` | `Vector3` |  | The point in 3D space to project onto the ray. |

**Returns:** `Vector3` — The point on the ray closest to the given point, or the ray origin if
the projection falls behind it.

### Ray:Distance

**Signature:** `Ray:Distance(point: Vector3): number`

Returns the distance between the given point and the point on the ray
nearest to the given point ([Ray.ClosestPoint(point)](/docs/reference/engine/datatypes/Ray.md)).

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `point` | `Vector3` |  | The point in 3D space to measure distance from. |

**Returns:** `number` — The shortest distance between the given point and the closest point on
the ray.