---
name: Vector2int16
last_updated: 2026-10-30T19:55:54Z
type: datatype
summary: "Represents a Vector2 with signed 16-bit integers for components."
---

# Vector2int16

Represents a Vector2 with signed 16-bit integers for components.

**Type:** datatype

## Description

The [Vector2int16](/docs/reference/engine/datatypes/Vector2int16.md) data type represents a vector in 2D space with a
**signed 16-bit integer** for its components. It is similar to
[Vector2](/docs/reference/engine/datatypes/Vector2.md) in that it allows for the same arithmetic operations, but
it lacks commonly used vector functions.

[Vector2int16](/docs/reference/engine/datatypes/Vector2int16.md) should **not** be confused with:

- [Vector2](/docs/reference/engine/datatypes/Vector2.md), a **more precise** and complete implementation for 2D
  vectors.
- [Vector3int16](/docs/reference/engine/datatypes/Vector3int16.md), a similar implementation for 3D vectors.

For each component:

- The **lower** bound is -2<sup>15</sup>, or **-32,768**.
- The **upper** bound is 2<sup>15</sup> &minus; 1, or **32,767**.

#### Converting to Vector2

To convert a [Vector2int16](/docs/reference/engine/datatypes/Vector2int16.md) to a [Vector2](/docs/reference/engine/datatypes/Vector2.md), construct a
[Vector2](/docs/reference/engine/datatypes/Vector2.md) by passing each **component** of the
[Vector2int16](/docs/reference/engine/datatypes/Vector2int16.md) to [Vector2.new()](/docs/reference/engine/datatypes/Vector2.md):

```lua
local vector2int16 = Vector2int16.new(1, 2)
local vector2 = Vector2.new(vector2int16.X, vector2int16.Y)
print(vector2)  --> 1, 2
```

Do **not** pass an entire [Vector2int16](/docs/reference/engine/datatypes/Vector2int16.md) to [Vector2.new()](/docs/reference/engine/datatypes/Vector2.md),
as the constructor interprets a [Vector2int16](/docs/reference/engine/datatypes/Vector2int16.md) as a `0` within its
parameters **without producing an error**. This can lead to silent logic
errors if you do something like:

```lua
local vector2int16 = Vector2int16.new(1, 2)
local vector2 = Vector2.new(vector2int16)
print(vector2)  --> 0, 0
```

#### Math Operations

The following math operations are valid for the [Vector2int16](/docs/reference/engine/datatypes/Vector2int16.md) data
type. For all operations, be mindful of the bounds associated with signed
16-bit integers, described earlier.

| Operation | Description |
| --- | --- |
| [Vector2int16](/docs/reference/engine/datatypes/Vector2int16.md) `+` [Vector2int16](/docs/reference/engine/datatypes/Vector2int16.md) | Produces a [Vector2int16](/docs/reference/engine/datatypes/Vector2int16.md) whose components are the sum of the operands' respective components. |
| [Vector2int16](/docs/reference/engine/datatypes/Vector2int16.md) `-` [Vector2int16](/docs/reference/engine/datatypes/Vector2int16.md) | Produces a [Vector2int16](/docs/reference/engine/datatypes/Vector2int16.md) whose components are the difference of the operands' respective components. |
| [Vector2int16](/docs/reference/engine/datatypes/Vector2int16.md) `*` [Vector2int16](/docs/reference/engine/datatypes/Vector2int16.md) | Produces a [Vector2int16](/docs/reference/engine/datatypes/Vector2int16.md) whose components are the product of the operands' respective components. |
| [Vector2int16](/docs/reference/engine/datatypes/Vector2int16.md) `/` [Vector2int16](/docs/reference/engine/datatypes/Vector2int16.md) | Produces a [Vector2int16](/docs/reference/engine/datatypes/Vector2int16.md) whose components are the quotient of the operands' respective components. The results of the division are rounded down. |
| [Vector2int16](/docs/reference/engine/datatypes/Vector2int16.md) `*` `number` | Produces a [Vector2int16](/docs/reference/engine/datatypes/Vector2int16.md) whose components are the product of the respective [Vector2int16](/docs/reference/engine/datatypes/Vector2int16.md) components and the number (factor). This operation is commutative. |
| [Vector2int16](/docs/reference/engine/datatypes/Vector2int16.md) `/` `number` | Produces a [Vector2int16](/docs/reference/engine/datatypes/Vector2int16.md) whose components are the quotient of the respective [Vector2int16](/docs/reference/engine/datatypes/Vector2int16.md) components and the number (divisor). The results of the division are rounded toward zero. |

## Constructors

### Vector2int16.new

**Signature:** `Vector2int16.new(x: number, y: number)`

Returns a new [Vector2int16](/docs/reference/engine/datatypes/Vector2int16.md) given the x and y components.
Non-integer components are rounded down.

The components must fall within the range [-2<sup>15</sup>,
2<sup>15</sup>). If outside this range, integer overflow may occur. For
example, providing 32,768 (equal to 2<sup>15</sup>) as a component
overflows the 16-bit integer, and so the component is -32,768 (equal to
-2<sup>15</sup>) instead.

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `x` | `number` |  | The x-component of the vector, rounded down to a signed 16-bit integer. |
| `y` | `number` |  | The y-component of the vector, rounded down to a signed 16-bit integer. |

## Properties

### Vector2int16.X

**Type:** `number`

The x-coordinate of the [Vector2int16](/docs/reference/engine/datatypes/Vector2int16.md), also accessible in its
lower-case variant.

### Vector2int16.Y

**Type:** `number`

The y-coordinate of the [Vector2int16](/docs/reference/engine/datatypes/Vector2int16.md), also accessible in its
lower-case variant.

## Math Operations

| Operation | Type A | Type B | Returns | Description |
|-----------|--------|--------|---------|-------------|
| `+` | `Vector2int16` | `Vector2int16` | `Vector2int16` | Produces a [Vector2int16](/docs/reference/engine/datatypes/Vector2int16.md) whose components are the sum of the operands' respective components. |
| `-` | `Vector2int16` | `Vector2int16` | `Vector2int16` | Produces a [Vector2int16](/docs/reference/engine/datatypes/Vector2int16.md) whose components are the difference of the operands' respective components. |
| `*` | `Vector2int16` | `Vector2int16` | `Vector2int16` | Produces a [Vector2int16](/docs/reference/engine/datatypes/Vector2int16.md) whose components are the product of the operands' respective components. |
| `/` | `Vector2int16` | `Vector2int16` | `Vector2int16` | Produces a [Vector2int16](/docs/reference/engine/datatypes/Vector2int16.md) whose components are the quotient of the operands' respective components. |
| `*` | `Vector2int16` | `number` | `Vector2int16` | Produces a [Vector2int16](/docs/reference/engine/datatypes/Vector2int16.md) whose components are the product of the respective [Vector2int16](/docs/reference/engine/datatypes/Vector2int16.md) components and the number (factor). |
| `/` | `Vector2int16` | `number` | `Vector2int16` | Produces a [Vector2int16](/docs/reference/engine/datatypes/Vector2int16.md) whose components are the quotient of the respective [Vector2int16](/docs/reference/engine/datatypes/Vector2int16.md) components and the number (divisor). |