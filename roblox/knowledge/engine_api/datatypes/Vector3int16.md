---
name: Vector3int16
last_updated: 2026-10-30T19:55:54Z
type: datatype
summary: "A Vector3 with signed 16-bit integers for components."
---

# Vector3int16

A Vector3 with signed 16-bit integers for components.

**Type:** datatype

## Description

The [Vector3int16](/docs/reference/engine/datatypes/Vector3int16.md) data type represents a vector in 3D space with a
**signed 16-bit integer** for its components. It is similar to
[Vector3](/docs/reference/engine/datatypes/Vector3.md) in that it allows for the same arithmetic operations, but
it lacks commonly used vector functions.

[Vector3int16](/docs/reference/engine/datatypes/Vector3int16.md) should **not** be confused with:

- [Vector3](/docs/reference/engine/datatypes/Vector3.md), a **more precise** and complete implementation for 3D
  vectors.
- [Vector2int16](/docs/reference/engine/datatypes/Vector2int16.md), a similar implementation for 2D vectors.

For each component:

- The **lower** bound is -2<sup>15</sup>, or **-32,768**.
- The **upper** bound is 2<sup>15</sup> &minus; 1, or **32,767**.

#### Converting to Vector3

To convert a [Vector3int16](/docs/reference/engine/datatypes/Vector3int16.md) to a [Vector3](/docs/reference/engine/datatypes/Vector3.md), construct a
[Vector3](/docs/reference/engine/datatypes/Vector3.md) by passing each **component** of the
[Vector3int16](/docs/reference/engine/datatypes/Vector3int16.md) to [Vector3.new()](/docs/reference/engine/datatypes/Vector3.md):

```lua
local vector3int16 = Vector3int16.new(1, 2, 3)
local vector3 = Vector3.new(vector3int16.X, vector3int16.Y, vector3int16.Z)
print(vector3)  --> 1, 2, 3
```

Do **not** pass an entire [Vector3int16](/docs/reference/engine/datatypes/Vector3int16.md) to [Vector3.new()](/docs/reference/engine/datatypes/Vector3.md),
as the constructor interprets a [Vector3int16](/docs/reference/engine/datatypes/Vector3int16.md) as a `0` within its
parameters **without producing an error**. This can lead to silent logic
errors if you do something like:

```lua
local vector3int16 = Vector3int16.new(1, 2, 3)
local vector3 = Vector3.new(vector3int16)
print(vector3)  --> 0, 0, 0
```

#### Math Operations

The following math operations are valid for the [Vector3int16](/docs/reference/engine/datatypes/Vector3int16.md) data
type. For all operations, be mindful of the bounds associated with signed
16-bit integers, described earlier.

| Operation | Description |
| --- | --- |
| [Vector3int16](/docs/reference/engine/datatypes/Vector3int16.md) `+` [Vector3int16](/docs/reference/engine/datatypes/Vector3int16.md) | Produces a [Vector3int16](/docs/reference/engine/datatypes/Vector3int16.md) whose components are the sum of the operands' respective components. |
| [Vector3int16](/docs/reference/engine/datatypes/Vector3int16.md) `-` [Vector3int16](/docs/reference/engine/datatypes/Vector3int16.md) | Produces a [Vector3int16](/docs/reference/engine/datatypes/Vector3int16.md) whose components are the difference of the operands' respective components. |
| [Vector3int16](/docs/reference/engine/datatypes/Vector3int16.md) `*` [Vector3int16](/docs/reference/engine/datatypes/Vector3int16.md) | Produces a [Vector3int16](/docs/reference/engine/datatypes/Vector3int16.md) whose components are the product of the operands' respective components. |
| [Vector3int16](/docs/reference/engine/datatypes/Vector3int16.md) `/` [Vector3int16](/docs/reference/engine/datatypes/Vector3int16.md) | Produces a [Vector3int16](/docs/reference/engine/datatypes/Vector3int16.md) whose components are the quotient of the operands' respective components. The results of the division are rounded down. |
| [Vector3int16](/docs/reference/engine/datatypes/Vector3int16.md) `*` `number` | Produces a [Vector3int16](/docs/reference/engine/datatypes/Vector3int16.md) whose components are the product of the respective [Vector3int16](/docs/reference/engine/datatypes/Vector3int16.md) components and the number (factor). This operation is commutative. |
| [Vector3int16](/docs/reference/engine/datatypes/Vector3int16.md) `/` `number` | Produces a [Vector3int16](/docs/reference/engine/datatypes/Vector3int16.md) whose components are the quotient of the respective [Vector3int16](/docs/reference/engine/datatypes/Vector3int16.md) components and the number (divisor). The results of the division are rounded toward zero. |

## Constructors

### Vector3int16.new

**Signature:** `Vector3int16.new(x: number, y: number, z: number)`

Returns a new [Vector3int16](/docs/reference/engine/datatypes/Vector3int16.md) from the given x, y and z
components. Non-integer components are rounded down.

The components must fall within the range [-2<sup>15</sup>,
2<sup>15</sup>). If outside this range, integer overflow may occur. For
example, providing 32,768 (equal to 2<sup>15</sup>) as a component
overflows the 16-bit integer, and so the component will be -32,768 (equal
to -2<sup>15</sup>) instead.

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `x` | `number` |  | The x-coordinate of the vector, rounded down to a signed 16-bit integer. |
| `y` | `number` |  | The y-coordinate of the vector, rounded down to a signed 16-bit integer. |
| `z` | `number` |  | The z-coordinate of the vector, rounded down to a signed 16-bit integer. |

## Properties

### Vector3int16.X

**Type:** `number`

The x-coordinate of the [Vector3int16](/docs/reference/engine/datatypes/Vector3int16.md), also accessible in its
lower-case variant.

### Vector3int16.Y

**Type:** `number`

The y-coordinate of the [Vector3int16](/docs/reference/engine/datatypes/Vector3int16.md), also accessible in its
lower-case variant.

### Vector3int16.Z

**Type:** `number`

The z-coordinate of the [Vector3int16](/docs/reference/engine/datatypes/Vector3int16.md), also accessible in its
lower-case variant.

## Math Operations

| Operation | Type A | Type B | Returns | Description |
|-----------|--------|--------|---------|-------------|
| `+` | `Vector3int16` | `Vector3int16` | `Vector3int16` | Produces a [Vector3int16](/docs/reference/engine/datatypes/Vector3int16.md) whose components are the sum of the operands' respective components. |
| `-` | `Vector3int16` | `Vector3int16` | `Vector3int16` | Produces a [Vector3int16](/docs/reference/engine/datatypes/Vector3int16.md) whose components are the difference of the operands' respective components. |
| `*` | `Vector3int16` | `Vector3int16` | `Vector3int16` | Produces a [Vector3int16](/docs/reference/engine/datatypes/Vector3int16.md) whose components are the product of the operands' respective components. |
| `/` | `Vector3int16` | `Vector3int16` | `Vector3int16` | Produces a [Vector3int16](/docs/reference/engine/datatypes/Vector3int16.md) whose components are the quotient of the operands' respective components. The results of the division are rounded down. |
| `*` | `Vector3int16` | `number` | `Vector3int16` | Produces a [Vector3int16](/docs/reference/engine/datatypes/Vector3int16.md) whose components are the product of the respective [Vector3int16](/docs/reference/engine/datatypes/Vector3int16.md) components and the number (factor). This operation is commutative. |
| `/` | `Vector3int16` | `number` | `Vector3int16` | Produces a [Vector3int16](/docs/reference/engine/datatypes/Vector3int16.md) whose components are the quotient of the respective [Vector3int16](/docs/reference/engine/datatypes/Vector3int16.md) components and the number (divisor). The results of the division are rounded toward zero. |