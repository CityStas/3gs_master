---
name: Vector2
last_updated: 2026-10-30T19:55:54Z
type: datatype
summary: "Represents a 2D value with direction and magnitude."
---

# Vector2

Represents a 2D value with direction and magnitude.

**Type:** datatype

## Description

The [Vector2](/docs/reference/engine/datatypes/Vector2.md) data type represents a 2D value with direction and
magnitude. Some applications include GUI elements and 2D mouse positions.

#### Math Operations

The following math operations are valid for the [Vector2](/docs/reference/engine/datatypes/Vector2.md) data type:

| Operation | Description |
| --- | --- |
| [Vector2](/docs/reference/engine/datatypes/Vector2.md) `+` [Vector2](/docs/reference/engine/datatypes/Vector2.md) | Produces a [Vector2](/docs/reference/engine/datatypes/Vector2.md) with each component of the second added to the corresponding component of the first. |
| [Vector2](/docs/reference/engine/datatypes/Vector2.md) `-` [Vector2](/docs/reference/engine/datatypes/Vector2.md) | Produces a [Vector2](/docs/reference/engine/datatypes/Vector2.md) with each component of the second subtracted from the corresponding component of the first. |
| [Vector2](/docs/reference/engine/datatypes/Vector2.md) `*` [Vector2](/docs/reference/engine/datatypes/Vector2.md) | Produces a [Vector2](/docs/reference/engine/datatypes/Vector2.md) with each component of the second multiplied by the corresponding component of the first. |
| [Vector2](/docs/reference/engine/datatypes/Vector2.md) `/` [Vector2](/docs/reference/engine/datatypes/Vector2.md) | Produces a [Vector2](/docs/reference/engine/datatypes/Vector2.md) with each component of the first divided by the corresponding component of the second. |
| [Vector2](/docs/reference/engine/datatypes/Vector2.md) `*` `number` | Produces a [Vector2](/docs/reference/engine/datatypes/Vector2.md) with each component multiplied by the number. |
| [Vector2](/docs/reference/engine/datatypes/Vector2.md) `/` `number` | Produces a [Vector2](/docs/reference/engine/datatypes/Vector2.md) with each component divided by the number. |

## Constructors

### Vector2.new

**Signature:** `Vector2.new(x: number, y: number)`

Returns a [Vector2](/docs/reference/engine/datatypes/Vector2.md) from the given x and y components. Both
parameters default to `0` if not provided.

```lua
local a = Vector2.new(3, 4)
print(a.X, a.Y)  --> 3  4

-- Omitted arguments default to 0
local b = Vector2.new()
print(b.X, b.Y)  --> 0  0
```

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `x` | `number` |  | The x-coordinate of the new vector (defaults to 0). |
| `y` | `number` |  | The y-coordinate of the new vector (defaults to 0). |

## Constants

| Name | Type | Description |
|------|------|-------------|
| `Vector2.zero` | `Vector2` | A [Vector2](/docs/reference/engine/datatypes/Vector2.md) with a magnitude of zero. |
| `Vector2.one` | `Vector2` | A [Vector2](/docs/reference/engine/datatypes/Vector2.md) with a value of 1 on every axis. |
| `Vector2.xAxis` | `Vector2` | A [Vector2](/docs/reference/engine/datatypes/Vector2.md) with a value of 1 on the X axis. |
| `Vector2.yAxis` | `Vector2` | A [Vector2](/docs/reference/engine/datatypes/Vector2.md) with a value of 1 on the Y axis. |

## Properties

### Vector2.X

**Type:** `number`

The x-coordinate of the [Vector2](/docs/reference/engine/datatypes/Vector2.md), corresponding to the first
argument passed to [Vector2.new()](/docs/reference/engine/datatypes/Vector2.md). This property is read-only.

```lua
local v = Vector2.new(3, 4)
print(v.X)  --> 3
```

### Vector2.Y

**Type:** `number`

The y-coordinate of the [Vector2](/docs/reference/engine/datatypes/Vector2.md), corresponding to the second
argument passed to [Vector2.new()](/docs/reference/engine/datatypes/Vector2.md). This property is read-only.

```lua
local v = Vector2.new(3, 4)
print(v.Y)  --> 4
```

### Vector2.Magnitude

**Type:** `number`

The length (magnitude) of the [Vector2](/docs/reference/engine/datatypes/Vector2.md), computed as
`math.sqrt(X^2 + Y^2)`. This property is read-only.

```lua
local v = Vector2.new(3, 4)
print(v.Magnitude)  --> 5
```

### Vector2.Unit

**Type:** `Vector2`

A normalized copy of the [Vector2](/docs/reference/engine/datatypes/Vector2.md) — one that has the same
direction as the original but a magnitude of 1. If the vector has zero
magnitude the result is undefined (contains `nan` values). This property
is read-only.

```lua
local v = Vector2.new(3, 4)
print(v.Unit)             --> 0.6, 0.8
print(v.Unit.Magnitude)   --> 1
```

## Methods

### Vector2:Cross

**Signature:** `Vector2:Cross(other: Vector2): number`

Returns the 2D cross product of this vector with `other`, computed as
`self.X * other.Y - self.Y * other.X`. Unlike [Vector3:Cross()](/docs/reference/engine/datatypes/Vector3.md)
which returns a vector, the 2D cross product returns a scalar representing
the signed magnitude of the perpendicular (Z) component. The result is
positive when `other` is counter-clockwise from `self`, negative when
clockwise, and zero when the vectors are parallel.

```lua
local a = Vector2.new(1, 0)
local b = Vector2.new(0, 1)
print(a:Cross(b))  -->  1
print(b:Cross(a))  --> -1
```

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `other` | `Vector2` |  | The vector to compute the cross product against. |

**Returns:** `number` — The signed scalar magnitude of the perpendicular component, computed
as `self.X * other.Y - self.Y * other.X`.

### Vector2:Abs

**Signature:** `Vector2:Abs(): Vector2`

Returns a new vector from the absolute values of the original's
components. For example, a vector of `(-2, 4)` returns a vector of
`(2, 4)`.

**Returns:** `Vector2` — A new vector whose components are the absolute values of the
original's components.

### Vector2:Ceil

**Signature:** `Vector2:Ceil(): Vector2`

Returns a new vector from the ceiling of the original's components. For
example, a vector of `(-2.6, 5.1)` returns a vector of `(-2, 6)`.

**Returns:** `Vector2` — A new vector whose components are the ceiling (rounded up) of the
original's components.

### Vector2:Floor

**Signature:** `Vector2:Floor(): Vector2`

Returns a new vector from the floor of the original's components. For
example, a vector of `(-2.6, 5.1)` returns a vector of `(-3, 5)`.

**Returns:** `Vector2` — A new vector whose components are the floor (rounded down) of the
original's components.

### Vector2:Sign

**Signature:** `Vector2:Sign(): Vector2`

Returns a new vector from the sign (-1, 0, or 1) of the original's
components. For example, a vector of `(-2.6, 5.1)` returns a vector of
`(-1, 1)`.

**Returns:** `Vector2` — A new vector whose components are the sign (-1, 0, or 1) of the
original's components.

### Vector2:Angle

**Signature:** `Vector2:Angle(other: Vector2, isSigned?: boolean): number`

Returns the angle in radians between the two vectors. Specify `true` for
the optional `isSigned` boolean if you want a signed angle. By default,
the method returns the absolute value. Signed angles are a negative when
going clockwise. Values are in the range `[0, pi]` for absolute angles and
`[-pi, pi]` for signed angles.

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `other` | `Vector2` |  | The vector to measure the angle to. |
| `isSigned` | `boolean` | `false` | Whether to return a signed angle (negative when clockwise) instead of the absolute value. |

**Returns:** `number`

### Vector2:Dot

**Signature:** `Vector2:Dot(v: Vector2): number`

Returns the scalar dot product of this vector and `v`, computed as
`self.X * v.X + self.Y * v.Y`. The result equals the product of the two
magnitudes multiplied by the cosine of the angle between them. A positive
value means the vectors point in roughly the same direction; zero means
they are perpendicular; negative means they point in roughly opposite
directions.

```lua
local a = Vector2.new(1, 0)
local b = Vector2.new(0, 1)
print(a:Dot(b))  --> 0  (perpendicular)
print(a:Dot(a))  --> 1  (parallel, equal to Magnitude^2)
```

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `v` | `Vector2` |  | The vector to compute the dot product with. |

**Returns:** `number`

### Vector2:Lerp

**Signature:** `Vector2:Lerp(v: Vector2, alpha: number): Vector2`

Returns a [Vector2](/docs/reference/engine/datatypes/Vector2.md) linearly interpolated between this
[Vector2](/docs/reference/engine/datatypes/Vector2.md) and the given goal `v` by the fraction `alpha`, using
the formula `self + (v - self) * alpha`. An `alpha` of 0 returns `self`,
an `alpha` of 1 returns `v`, and values between 0 and 1 return a point in
between. Note that `alpha` is **not** clamped to `[0, 1]` — values outside
that range extrapolate beyond the two endpoints.

```lua
local a = Vector2.new(0, 0)
local b = Vector2.new(4, 8)
print(a:Lerp(b, 0.5))  --> 2, 4
```

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `v` | `Vector2` |  | The goal vector to interpolate toward. |
| `alpha` | `number` |  | The interpolation fraction, where 0 returns this vector and 1 returns `v`. |

**Returns:** `Vector2`

### Vector2:Max

**Signature:** `Vector2:Max(others...: Tuple): Vector2`

Returns a [Vector2](/docs/reference/engine/datatypes/Vector2.md) with each component as the highest among the
respective components of the provided [Vector2](/docs/reference/engine/datatypes/Vector2.md) objects.

```lua
local a = Vector2.new(1, 2)
local b = Vector2.new(2, 1)

print(a:Max(b)) -- Vector2.new(2, 2)
```

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `others...` | `Tuple` |  | One or more [Vector2](/docs/reference/engine/datatypes/Vector2.md) objects to compare against. |

**Returns:** `Vector2`

### Vector2:Min

**Signature:** `Vector2:Min(others...: Tuple): Vector2`

Returns a [Vector2](/docs/reference/engine/datatypes/Vector2.md) with each component as the lowest among the
respective components of the provided [Vector2](/docs/reference/engine/datatypes/Vector2.md) objects.

```lua
local a = Vector2.new(1, 2)
local b = Vector2.new(2, 1)

print(a:Min(b)) -- Vector2.new(1, 1)
```

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `others...` | `Tuple` |  | One or more [Vector2](/docs/reference/engine/datatypes/Vector2.md) objects to compare against. |

**Returns:** `Vector2`

### Vector2:FuzzyEq

**Signature:** `Vector2:FuzzyEq(other: Vector2, epsilon?: number): bool`

Returns `true` if the X and Y components of the other [Vector2](/docs/reference/engine/datatypes/Vector2.md)
are within `epsilon` units of each corresponding component of this
[Vector2](/docs/reference/engine/datatypes/Vector2.md). The comparison is per-component: both
`math.abs(self.X - other.X)` and `math.abs(self.Y - other.Y)` must be less
than or equal to `epsilon`. The optional `epsilon` parameter defaults to
`1e-5` (0.00001) and must be a positive value no greater than `0.1`.

```lua
local a = Vector2.new(1, 2)
local b = Vector2.new(1.000009, 2.000009)
print(a:FuzzyEq(b))           --> true  (within default 1e-5)
print(a:FuzzyEq(b, 0.000001)) --> false (tighter epsilon)
```

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `other` | `Vector2` |  | The vector to compare against. |
| `epsilon` | `number` | `0.00001 (1e-5)` | The maximum difference allowed for each component to still be considered equal. |

**Returns:** `bool`

## Math Operations

| Operation | Type A | Type B | Returns | Description |
|-----------|--------|--------|---------|-------------|
| `+` | `Vector2` | `Vector2` | `Vector2` | Produces a [Vector2](/docs/reference/engine/datatypes/Vector2.md) with each component of the second added to the corresponding component of the first. |
| `-` | `Vector2` | `Vector2` | `Vector2` | Produces a [Vector2](/docs/reference/engine/datatypes/Vector2.md) with each component of the second subtracted from the corresponding component of the first. |
| `*` | `Vector2` | `Vector2` | `Vector2` | Produces a [Vector2](/docs/reference/engine/datatypes/Vector2.md) with each component of the second multiplied by the corresponding component of the first. |
| `/` | `Vector2` | `Vector2` | `Vector2` | Produces a [Vector2](/docs/reference/engine/datatypes/Vector2.md) with each component of the first divided by the corresponding component of the second. |
| `*` | `Vector2` | `number` | `Vector2` | Produces a [Vector2](/docs/reference/engine/datatypes/Vector2.md) with each component multiplied by the number. |
| `/` | `Vector2` | `number` | `Vector2` | Produces a [Vector2](/docs/reference/engine/datatypes/Vector2.md) with each component divided by the number. |