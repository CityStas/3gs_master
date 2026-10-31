---
name: Vector3
last_updated: 2026-10-30T19:55:54Z
type: datatype
summary: "Represents a 3D value with a direction and magnitude."
---

# Vector3

Represents a 3D value with a direction and magnitude.

**Type:** datatype

## Description

The [Vector3](/docs/reference/engine/datatypes/Vector3.md) data type represents a vector in 3D space, typically
used as a point in 3D space or the dimensions of a rectangular prism.
[Vector3](/docs/reference/engine/datatypes/Vector3.md) supports basic component-based arithmetic operations (sum,
difference, product, and quotient) and these operations can be applied on the
left or right hand side to either another [Vector3](/docs/reference/engine/datatypes/Vector3.md) or a number. It
also features methods for common vector operations, such as
[Cross()](/docs/reference/engine/datatypes/Vector3.md) and [Dot()](/docs/reference/engine/datatypes/Vector3.md).

Alternatively to [Vector3](/docs/reference/engine/datatypes/Vector3.md), consider using the methods and properties
of the [vector](/docs/reference/engine/globals/vector.md) library.

Some example usages of [Vector3](/docs/reference/engine/datatypes/Vector3.md) are the
[Position](/docs/reference/engine/classes/BasePart.md), [Rotation](/docs/reference/engine/classes/BasePart.md), and
[Size](/docs/reference/engine/classes/BasePart.md) of parts, for example:

```lua
local part = Instance.new("Part")
part.Position = part.Position + Vector3.new(5, 2, 10) -- Move part by (5, 2, 10)
print(part.Position) --> 5, 2, 10
```

[Vector3](/docs/reference/engine/datatypes/Vector3.md) is also commonly used when constructing more complex 3D
data types such as [CFrame](/docs/reference/engine/datatypes/CFrame.md). Many of these data types' methods will
use a [Vector3](/docs/reference/engine/datatypes/Vector3.md) within their parameters, such as
[CFrame:PointToObjectSpace()](/docs/reference/engine/datatypes/CFrame.md).

## Constructors

### Vector3.new

**Signature:** `Vector3.new(x?: number, y?: number, z?: number)`

Returns a new [Vector3](/docs/reference/engine/datatypes/Vector3.md) using the given `x`, `y`, and `z`
components.

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `x` | `number` | `0` | The x-axis component of the vector. |
| `y` | `number` | `0` | The y-axis component of the vector. |
| `z` | `number` | `0` | The z-axis component of the vector. |

### Vector3.FromNormalId

**Signature:** `Vector3.FromNormalId(normal: NormalId)`

Returns a unit [Vector3](/docs/reference/engine/datatypes/Vector3.md) pointing in the direction of the given
[NormalId](/docs/reference/engine/enums/NormalId.md). For example, [NormalId.Top](/docs/reference/engine/enums/NormalId.md) returns `(0, 1, 0)` and
[NormalId.Front](/docs/reference/engine/enums/NormalId.md) returns `(0, 0, -1)`.

```lua
print(Vector3.FromNormalId(Enum.NormalId.Right)) --> 1, 0, 0
print(Vector3.FromNormalId(Enum.NormalId.Left))  --> -1, 0, 0
```

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `normal` | `NormalId` |  | The [NormalId](/docs/reference/engine/enums/NormalId.md) specifying the face direction to convert into a unit vector. |

### Vector3.FromAxis

**Signature:** `Vector3.FromAxis(axis: Axis)`

Returns a unit [Vector3](/docs/reference/engine/datatypes/Vector3.md) for the given [Axis](/docs/reference/engine/enums/Axis.md). The mapping
is [Axis.X](/docs/reference/engine/enums/Axis.md) to `(1, 0, 0)`, [Axis.Y](/docs/reference/engine/enums/Axis.md) to `(0, 1, 0)`, and
[Axis.Z](/docs/reference/engine/enums/Axis.md) to `(0, 0, 1)`.

```lua
print(Vector3.FromAxis(Enum.Axis.X)) --> 1, 0, 0
print(Vector3.FromAxis(Enum.Axis.Z)) --> 0, 0, 1
```

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `axis` | `Axis` |  | The [Axis](/docs/reference/engine/enums/Axis.md) specifying which coordinate axis to convert into a unit vector. |

## Constants

| Name | Type | Description |
|------|------|-------------|
| `Vector3.zero` | `Vector3` | A [Vector3](/docs/reference/engine/datatypes/Vector3.md) with a magnitude of `0`. |
| `Vector3.one` | `Vector3` | A [Vector3](/docs/reference/engine/datatypes/Vector3.md) with a value of `1` on every axis. |
| `Vector3.xAxis` | `Vector3` | A [Vector3](/docs/reference/engine/datatypes/Vector3.md) with a value of `1` on the **X** axis. |
| `Vector3.yAxis` | `Vector3` | A [Vector3](/docs/reference/engine/datatypes/Vector3.md) with a value of `1` on the **Y** axis. |
| `Vector3.zAxis` | `Vector3` | A [Vector3](/docs/reference/engine/datatypes/Vector3.md) with a value of `1` on the **Z** axis. |

## Properties

### Vector3.X

**Type:** `number`

The **X** coordinate of the [Vector3](/docs/reference/engine/datatypes/Vector3.md). In world space, this axis
corresponds to the left-right (east-west) direction.

### Vector3.Y

**Type:** `number`

The **Y** coordinate of the [Vector3](/docs/reference/engine/datatypes/Vector3.md). In world space, this axis
corresponds to the up-down (vertical) direction.

### Vector3.Z

**Type:** `number`

The **Z** coordinate of the [Vector3](/docs/reference/engine/datatypes/Vector3.md). In world space, this axis
corresponds to the north-south (forward-back) direction.

### Vector3.Magnitude

**Type:** `number`

The length (magnitude) of the [Vector3](/docs/reference/engine/datatypes/Vector3.md), computed as
`math.sqrt(X^2 + Y^2 + Z^2)`. This is useful for comparing distances or
determining how far a point is from the origin.

```lua
local v = Vector3.new(3, 4, 0)
print(v.Magnitude) --> 5
```

### Vector3.Unit

**Type:** `Vector3`

A normalized copy of the [Vector3](/docs/reference/engine/datatypes/Vector3.md) — one that has the same
direction as the original but a magnitude of `1`. This is useful when you
need only the direction of a vector without its length, for example to get
a movement direction regardless of speed.

If the vector has a magnitude of `0` (i.e. all components are zero), the
resulting `Unit` vector will have `NaN` components. Check
[Magnitude](/docs/reference/engine/datatypes/Vector3.md) before using `Unit` when the vector
may be zero-length.

```lua
local v = Vector3.new(3, 4, 0)
print(v.Unit)      --> 0.6, 0.8, 0
print(v.Unit.Magnitude) --> 1
```

## Methods

### Vector3:Abs

**Signature:** `Vector3:Abs(): Vector3`

Returns a new vector from the absolute values of the original's
components. For example, a vector of `(-2, 4, -6)` returns a vector of
`(2, 4, 6)`.

**Returns:** `Vector3`

### Vector3:Ceil

**Signature:** `Vector3:Ceil(): Vector3`

Returns a new vector from the ceiling of the original's components. For
example, a vector of `(-2.6, 5.1, 8.8)` returns a vector of `(-2, 6, 9)`.

**Returns:** `Vector3`

### Vector3:Floor

**Signature:** `Vector3:Floor(): Vector3`

Returns a new vector from the floor of the original's components. For
example, a vector of `(-2.6, 5.1, 8.8)` returns a vector of `(-3, 5, 8)`.

**Returns:** `Vector3`

### Vector3:Sign

**Signature:** `Vector3:Sign(): Vector3`

Returns a new vector from the sign (-1, 0, or 1) of the original's
components. For example, a vector of `(-2.6, 5.1, 0)` returns a vector of
`(-1, 1, 0)`.

**Returns:** `Vector3`

### Vector3:Cross

**Signature:** `Vector3:Cross(other: Vector3): Vector3`

Returns the cross product of this vector and `other`. The resulting vector
is perpendicular to both input vectors and has a magnitude equal to the
area of the parallelogram they span. The direction follows the right-hand
rule: if you curl the fingers of your right hand from `self` toward
`other`, your thumb points in the direction of the result.

The cross product is commonly used to find normals to surfaces, determine
the axis of rotation between two directions, and test whether two vectors
are parallel (cross product of parallel vectors is the zero vector).

```lua
local a = Vector3.new(1, 0, 0)
local b = Vector3.new(0, 1, 0)
print(a:Cross(b)) --> 0, 0, 1
print(b:Cross(a)) --> 0, 0, -1
```

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `other` | `Vector3` |  | The other [Vector3](/docs/reference/engine/datatypes/Vector3.md) to compute the cross product with. |

**Returns:** `Vector3`

### Vector3:Angle

**Signature:** `Vector3:Angle(other: Vector3, axis?: Vector3): number`

Returns the angle in radians between this vector and `other`. The input
vectors do not need to be unit vectors. Without an `axis` argument, the
returned angle is always in the range `[0, math.pi]` (unsigned).

If you provide an `axis` [Vector3](/docs/reference/engine/datatypes/Vector3.md), the returned angle is signed:
positive when the rotation from `self` to `other` follows the right-hand
rule around `axis`, and negative otherwise. The signed result is in the
range `[-math.pi, math.pi]`. The `axis` is used only to determine the
sign; the plane of rotation is still defined by `self` and `other`.

```lua
local a = Vector3.new(1, 0, 0)
local b = Vector3.new(0, 1, 0)
print(a:Angle(b))                         --> 1.5707963... (pi/2)
print(a:Angle(b, Vector3.new(0, 0, 1)))   --> 1.5707963... (positive, CCW about +Z)
print(b:Angle(a, Vector3.new(0, 0, 1)))   --> -1.5707963... (negative, CW about +Z)
```

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `other` | `Vector3` |  | The [Vector3](/docs/reference/engine/datatypes/Vector3.md) to measure the angle to. |
| `axis` | `Vector3` | `nil` | An optional [Vector3](/docs/reference/engine/datatypes/Vector3.md) used to determine the sign of the angle via the right-hand rule. |

**Returns:** `number`

### Vector3:Dot

**Signature:** `Vector3:Dot(other: Vector3): number`

Returns the scalar dot product of this vector and `other`, computed as
`self.X * other.X + self.Y * other.Y + self.Z * other.Z`.

The dot product is useful for determining the relationship between two
directions: it equals the product of their magnitudes multiplied by the
cosine of the angle between them. For unit vectors, a result of `1` means
they point in the same direction, `0` means they are perpendicular, and
`-1` means they point in opposite directions.

```lua
local a = Vector3.new(1, 0, 0)
local b = Vector3.new(0, 1, 0)
print(a:Dot(b)) --> 0

local c = Vector3.new(1, 2, 3)
local d = Vector3.new(4, 5, 6)
print(c:Dot(d)) --> 32
```

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `other` | `Vector3` |  | The [Vector3](/docs/reference/engine/datatypes/Vector3.md) to compute the dot product with. |

**Returns:** `number`

### Vector3:FuzzyEq

**Signature:** `Vector3:FuzzyEq(other: Vector3, epsilon?: number): bool`

Returns `true` if the two vectors are approximately equal within the
tolerance defined by `epsilon`. The comparison is performed per-component
using a hybrid epsilon that scales relative to the magnitude of each
component, making it suitable for both small and large values. The default
`epsilon` of `0.00001` (1e-5) works well for most cases.

```lua
local a = Vector3.new(1, 2, 3)
local b = Vector3.new(1.000001, 2, 3)
print(a:FuzzyEq(b))        --> true  (within default epsilon)
print(a:FuzzyEq(b, 1e-8))  --> false (tighter tolerance)
```

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `other` | `Vector3` |  | The [Vector3](/docs/reference/engine/datatypes/Vector3.md) to compare against. |
| `epsilon` | `number` | `0.00001 aka 1e-5` | The tolerance threshold for the comparison, scaled relative to the component magnitudes. |

**Returns:** `bool`

### Vector3:Lerp

**Signature:** `Vector3:Lerp(goal: Vector3, alpha: number): Vector3`

Returns a [Vector3](/docs/reference/engine/datatypes/Vector3.md) linearly interpolated between this
[Vector3](/docs/reference/engine/datatypes/Vector3.md) and the given `goal` [Vector3](/docs/reference/engine/datatypes/Vector3.md) by the fraction
`alpha`. Note that `alpha` is **not** limited to the range `[0, 1]`.

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `goal` | `Vector3` |  | The target [Vector3](/docs/reference/engine/datatypes/Vector3.md) to interpolate toward. |
| `alpha` | `number` |  | The interpolation fraction, typically between 0 (returns self) and 1 (returns goal), but not clamped. |

**Returns:** `Vector3`

### Vector3:Max

**Signature:** `Vector3:Max(vector: Vector3): Vector3`

Returns a [Vector3](/docs/reference/engine/datatypes/Vector3.md) with each component as the highest among the
respective components of both provided [Vector3](/docs/reference/engine/datatypes/Vector3.md) objects.

```lua
local a = Vector3.new(1, 2, 1)
local b = Vector3.new(2, 1, 2)

print(a:Max(b))  --> Vector3.new(2, 2, 2)
```

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `vector` | `Vector3` |  | The [Vector3](/docs/reference/engine/datatypes/Vector3.md) to compare component-wise against. |

**Returns:** `Vector3`

### Vector3:Min

**Signature:** `Vector3:Min(vector: Vector3): Vector3`

Returns a [Vector3](/docs/reference/engine/datatypes/Vector3.md) with each component as the lowest among the
respective components of both provided [Vector3](/docs/reference/engine/datatypes/Vector3.md) objects.

```lua
local a = Vector3.new(1, 2, 1)
local b = Vector3.new(2, 1, 2)

print(a:Min(b))  --> Vector3.new(1, 1, 1)
```

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `vector` | `Vector3` |  | The [Vector3](/docs/reference/engine/datatypes/Vector3.md) to compare component-wise against. |

**Returns:** `Vector3`

## Math Operations

| Operation | Type A | Type B | Returns | Description |
|-----------|--------|--------|---------|-------------|
| `+` | `Vector3` | `Vector3` | `Vector3` | Produces a [Vector3](/docs/reference/engine/datatypes/Vector3.md) by adding each component of the first vector to the corresponding component of the second. |
| `-` | `Vector3` | `Vector3` | `Vector3` | Produces a [Vector3](/docs/reference/engine/datatypes/Vector3.md) by subtracting each component of the second vector from the corresponding component of the first. |
| `*` | `Vector3` | `Vector3` | `Vector3` | Produces a [Vector3](/docs/reference/engine/datatypes/Vector3.md) by multiplying each component of the first vector by the corresponding component of the second. |
| `/` | `Vector3` | `Vector3` | `Vector3` | Produces a [Vector3](/docs/reference/engine/datatypes/Vector3.md) by dividing each component of the first vector by the corresponding component of the second. |
| `//` | `Vector3` | `Vector3` | `Vector3` | Produces a [Vector3](/docs/reference/engine/datatypes/Vector3.md) by **floor dividing** each component of the first vector by the corresponding component of the second. |
| `*` | `Vector3` | `number` | `Vector3` | Produces a [Vector3](/docs/reference/engine/datatypes/Vector3.md) by multiplying each component of the provided vector by the number. |
| `/` | `Vector3` | `number` | `Vector3` | Produces a [Vector3](/docs/reference/engine/datatypes/Vector3.md) by dividing each component of the provided vector by the number. |
| `//` | `Vector3` | `number` | `Vector3` | Produces a [Vector3](/docs/reference/engine/datatypes/Vector3.md) by **floor dividing** each component of the provided vector by the number. |