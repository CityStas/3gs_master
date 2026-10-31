---
name: CFrame
last_updated: 2026-10-30T19:55:54Z
type: datatype
summary: "A data type that represents both a 3D position and orientation."
---

# CFrame

A data type that represents both a 3D position and orientation.

**Type:** datatype

## Description

The [CFrame](/docs/reference/engine/datatypes/CFrame.md) data type, short for **coordinate frame**, describes a
3D position and orientation. It is made up of a **positional** component and a
**rotational** component and includes essential arithmetic operations for
working with 3D data on Roblox.

```lua
-- Create a CFrame at a certain position and Euler rotation
local cf = CFrame.new(0, 5, 0) * CFrame.fromEulerAngles(math.rad(45), 0, 0)
```

For an introduction to the [CFrame](/docs/reference/engine/datatypes/CFrame.md) data type, see
[CFrames](/docs/en-us/workspace/cframes.md).

#### Positional Component

The positional component is available as a [Vector3](/docs/reference/engine/datatypes/Vector3.md). In addition,
the components of a [CFrame](/docs/reference/engine/datatypes/CFrame.md) object's position are also available in
the [X](/docs/reference/engine/datatypes/CFrame.md), [Y](/docs/reference/engine/datatypes/CFrame.md) and [Z](/docs/reference/engine/datatypes/CFrame.md)
properties like a [Vector3](/docs/reference/engine/datatypes/Vector3.md).

#### Rotational Component

[CFrame](/docs/reference/engine/datatypes/CFrame.md) stores 3D rotation data in a 3&times;3 **rotation matrix**.
These values are returned by the [CFrame:GetComponents()](/docs/reference/engine/datatypes/CFrame.md) function
after the `x`, `y` and `z` positional values. This matrix is used internally
when doing calculations involving rotations, using **radians** as their unit
(for conversion from one to the other, use [math.rad()](/docs/reference/engine/globals/math.md) or
[math.deg()](/docs/reference/engine/globals/math.md)). For more information on how the Roblox Engine performs
rotations, see [RotationOrder](/docs/reference/engine/enums/RotationOrder.md).

The table below represents the components of a [CFrame](/docs/reference/engine/datatypes/CFrame.md) object's
rotation matrix and their relationship with the available vector properties
such as [LookVector](/docs/reference/engine/datatypes/CFrame.md) and
[RightVector](/docs/reference/engine/datatypes/CFrame.md). Although the individual components
of the rotation matrix are rarely useful by themselves, the vector properties
which derive from them are much more useful.

| XVector, RightVector | YVector, UpVector | ZVector, -LookVector<sup>†</sup> |
| --- | --- | --- |
| R00 | R01 | R02 |
| R10 | R11 | R12 |
| R20 | R21 | R22 |

<figcaption><sup>&dagger;</sup> Unlike the others,
<code>Datatype.CFrame.LookVector|LookVector</code> represents the negated
column components. The <code>Datatype.CFrame.LookVector|LookVector</code> is
useful because many <code>Class.Instance|Instances</code> such as the
<code>Class.Camera|Camera</code> and <code>Class.Attachment|Attachments</code>
treat that vector as the direction the instance is pointing.</figcaption>

## Constructors

### CFrame.new

**Signature:** `CFrame.new()`

Creates an identity [CFrame](/docs/reference/engine/datatypes/CFrame.md) with position `(0, 0, 0)` and no
rotation (identity rotation matrix). This is equivalent to
[CFrame.identity](/docs/reference/engine/datatypes/CFrame.md).

### CFrame.new

**Signature:** `CFrame.new(pos: Vector3)`

Returns a [CFrame](/docs/reference/engine/datatypes/CFrame.md) positioned at `pos` with no rotation (identity
rotation matrix). The orientation defaults to the identity, meaning the
local axes align with the world axes.

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `pos` | `Vector3` |  | The 3D position for the new CFrame. |

### CFrame.new

**Signature:** `CFrame.new(pos: Vector3, lookAt: Vector3)`

Returns a new [CFrame](/docs/reference/engine/datatypes/CFrame.md) located at `pos` and facing towards
`lookAt`, assuming that `(0, 1, 0)` is considered "up" in world space.

This constructor overload has been replaced by [CFrame.lookAt()](/docs/reference/engine/datatypes/CFrame.md),
which accomplishes a similar goal. It remains for the sake of backward
compatibility.

At high pitch angles (around 82 degrees), you may experience numerical
instability. If this is an issue, or if you require a different "up"
vector, use [CFrame.fromMatrix()](/docs/reference/engine/datatypes/CFrame.md) to more accurately construct
the [CFrame](/docs/reference/engine/datatypes/CFrame.md). Additionally, if `lookAt` is directly above `pos`
(pitch angle of 90 degrees), the "up" vector switches to the X axis.

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `pos` | `Vector3` |  | The world-space position of the CFrame. |
| `lookAt` | `Vector3` |  | The world-space point the CFrame should face toward. |

### CFrame.new

**Signature:** `CFrame.new(x: number, y: number, z: number)`

Returns a [CFrame](/docs/reference/engine/datatypes/CFrame.md) positioned at `(x, y, z)` with no rotation
(identity rotation matrix). This is equivalent to
`CFrame.new(Vector3.new(x, y, z))`.

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `x` | `number` |  | The X component of the position. |
| `y` | `number` |  | The Y component of the position. |
| `z` | `number` |  | The Z component of the position. |

### CFrame.new

**Signature:** `CFrame.new(x: number, y: number, z: number, qX: number, qY: number, qZ: number, qW: number)`

Returns a [CFrame](/docs/reference/engine/datatypes/CFrame.md) from position (`x`, `y`, `z`) and quaternion
(`qX`, `qY`, `qZ`, `qW`). The quaternion is expected to be of unit length
to represent a valid rotation. If this isn't the case, the quaternion will
be normalized.

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `x` | `number` |  | The X component of the position. |
| `y` | `number` |  | The Y component of the position. |
| `z` | `number` |  | The Z component of the position. |
| `qX` | `number` |  | The X component of the quaternion rotation. |
| `qY` | `number` |  | The Y component of the quaternion rotation. |
| `qZ` | `number` |  | The Z component of the quaternion rotation. |
| `qW` | `number` |  | The W (scalar) component of the quaternion rotation. |

### CFrame.new

**Signature:** `CFrame.new(x: number, y: number, z: number, R00: number, R01: number, R02: number, R10: number, R11: number, R12: number, R20: number, R21: number, R22: number)`

Creates a [CFrame](/docs/reference/engine/datatypes/CFrame.md) from position (`x`, `y`, `z`) with an
orientation specified by the rotation matrix.

`[[R00 R01 R02] [R10 R11 R12] [R20 R21 R22]]`

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `x` | `number` |  | The X component of the position. |
| `y` | `number` |  | The Y component of the position. |
| `z` | `number` |  | The Z component of the position. |
| `R00` | `number` |  | The row 1, column 1 element of the rotation matrix. |
| `R01` | `number` |  | The row 1, column 2 element of the rotation matrix. |
| `R02` | `number` |  | The row 1, column 3 element of the rotation matrix. |
| `R10` | `number` |  | The row 2, column 1 element of the rotation matrix. |
| `R11` | `number` |  | The row 2, column 2 element of the rotation matrix. |
| `R12` | `number` |  | The row 2, column 3 element of the rotation matrix. |
| `R20` | `number` |  | The row 3, column 1 element of the rotation matrix. |
| `R21` | `number` |  | The row 3, column 2 element of the rotation matrix. |
| `R22` | `number` |  | The row 3, column 3 element of the rotation matrix. |

### CFrame.lookAt

**Signature:** `CFrame.lookAt(at: Vector3, lookAt: Vector3, up?: Vector3)`

Returns a new [CFrame](/docs/reference/engine/datatypes/CFrame.md) with the position of `at` and facing
towards `lookAt`, optionally specifying the upward direction (`up`) with a
default of `(0, 1, 0)`.

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `at` | `Vector3` |  | The world-space position of the CFrame. |
| `lookAt` | `Vector3` |  | The world-space point the CFrame should face toward. |
| `up` | `Vector3` | `Vector3.yAxis` | The unit vector specifying the upward direction. Defaults to `(0, 1, 0)`. |

### CFrame.lookAlong

**Signature:** `CFrame.lookAlong(at: Vector3, direction: Vector3, up?: Vector3)`

Returns a new [CFrame](/docs/reference/engine/datatypes/CFrame.md) with the position of `at` and facing along
`direction`, optionally specifying the upward direction (`up`) with a
default of `(0, 1, 0)`.

This constructor is equivalent to `CFrame.lookAt(at, at + direction)`.

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `at` | `Vector3` |  | The world-space position of the CFrame. |
| `direction` | `Vector3` |  | The direction the CFrame should face along. |
| `up` | `Vector3` | `Vector3.yAxis` | The unit vector specifying the upward direction. Defaults to `(0, 1, 0)`. |

### CFrame.fromRotationBetweenVectors

**Signature:** `CFrame.fromRotationBetweenVectors(from: Vector3, to: Vector3)`

Returns a [CFrame](/docs/reference/engine/datatypes/CFrame.md) whose rotation represents the shortest-arc
rotation that aligns vector `from` with vector `to`. The input vectors do
not need to be unit length; they are normalized internally. The resulting
[CFrame](/docs/reference/engine/datatypes/CFrame.md) has its position set to `(0, 0, 0)`.

```lua
-- Rotate a direction to face another direction
local from = Vector3.new(0, 1, 0)
local to = Vector3.new(1, 0, 0)
local cf = CFrame.fromRotationBetweenVectors(from, to)
print(cf * from) --> approximately (1, 0, 0)
```

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `from` | `Vector3` |  | Vector representing the "from" direction. |
| `to` | `Vector3` |  | Vector representing the "to" direction. |

### CFrame.fromEulerAngles

**Signature:** `CFrame.fromEulerAngles(rx: number, ry: number, rz: number, order?: RotationOrder)`

Returns a rotated [CFrame](/docs/reference/engine/datatypes/CFrame.md) from angles `rx`, `ry`, and `rz` in
radians. Rotations are applied in the optional [RotationOrder](/docs/reference/engine/enums/RotationOrder.md) with a
default of `XYZ`, equivalent to:

```lua
local rx, ry, rz = math.rad(30), math.rad(45), math.rad(60)
local cframe = CFrame.fromEulerAngles(rx, 0, 0) -- X
               * CFrame.fromEulerAngles(0, ry, 0) -- Y
               * CFrame.fromEulerAngles(0, 0, rz) -- Z
local rx_out, ry_out, rz_out = cframe:ToEulerAnglesXYZ()
print(string.format("rx: %.2f, ry: %.2f, rz: %.2f", math.deg(rx_out), math.deg(ry_out), math.deg(rz_out))) --> rx: 30.00, ry: 45.00, rz: 60.00
```

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `rx` | `number` |  | Rotation angle around the X axis in radians. |
| `ry` | `number` |  | Rotation angle around the Y axis in radians. |
| `rz` | `number` |  | Rotation angle around the Z axis in radians. |
| `order` | `RotationOrder` | `Enum.RotationOrder.XYZ` | The order in which rotations are applied. |

### CFrame.fromEulerAnglesXYZ

**Signature:** `CFrame.fromEulerAnglesXYZ(rx: number, ry: number, rz: number)`

Returns a rotated [CFrame](/docs/reference/engine/datatypes/CFrame.md) from angles `rx`, `ry`, and `rz` in
radians using [RotationOrder.XYZ](/docs/reference/engine/enums/RotationOrder.md), equivalent to:

```lua
local rx, ry, rz = math.rad(30), math.rad(45), math.rad(60)
local cframe = CFrame.fromEulerAngles(rx, 0, 0) -- X
               * CFrame.fromEulerAngles(0, ry, 0) -- Y
               * CFrame.fromEulerAngles(0, 0, rz) -- Z
local rx_out, ry_out, rz_out = cframe:ToEulerAnglesXYZ()
print(string.format("rx: %.2f, ry: %.2f, rz: %.2f", math.deg(rx_out), math.deg(ry_out), math.deg(rz_out))) --> rx: 30.00, ry: 45.00, rz: 60.00
```

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `rx` | `number` |  | Rotation angle around the X axis in radians. |
| `ry` | `number` |  | Rotation angle around the Y axis in radians. |
| `rz` | `number` |  | Rotation angle around the Z axis in radians. |

### CFrame.fromEulerAnglesYXZ

**Signature:** `CFrame.fromEulerAnglesYXZ(rx: number, ry: number, rz: number)`

Returns a rotated [CFrame](/docs/reference/engine/datatypes/CFrame.md) from angles `rx`, `ry`, and `rz` in
radians using [RotationOrder.YXZ](/docs/reference/engine/enums/RotationOrder.md), equivalent to:

```lua
local rx, ry, rz = math.rad(30), math.rad(45), math.rad(60)
local cframe = CFrame.fromEulerAngles(0, ry, 0) -- Y
               * CFrame.fromEulerAngles(rx, 0, 0) -- X
               * CFrame.fromEulerAngles(0, 0, rz) -- Z
local rx_out, ry_out, rz_out = cframe:ToEulerAnglesYXZ()
print(string.format("rx: %.2f, ry: %.2f, rz: %.2f", math.deg(rx_out), math.deg(ry_out), math.deg(rz_out))) --> rx: 30.00, ry: 45.00, rz: 60.00
```

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `rx` | `number` |  | Rotation angle around the X axis in radians. |
| `ry` | `number` |  | Rotation angle around the Y axis in radians. |
| `rz` | `number` |  | Rotation angle around the Z axis in radians. |

### CFrame.Angles

**Signature:** `CFrame.Angles(rx: number, ry: number, rz: number)`

Equivalent to [fromEulerAnglesXYZ()](/docs/reference/engine/datatypes/CFrame.md).

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `rx` | `number` |  | Rotation angle around the X axis in radians. |
| `ry` | `number` |  | Rotation angle around the Y axis in radians. |
| `rz` | `number` |  | Rotation angle around the Z axis in radians. |

### CFrame.fromOrientation

**Signature:** `CFrame.fromOrientation(rx: number, ry: number, rz: number)`

Equivalent to [fromEulerAnglesYXZ()](/docs/reference/engine/datatypes/CFrame.md).

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `rx` | `number` |  | Rotation angle around the X axis in radians. |
| `ry` | `number` |  | Rotation angle around the Y axis in radians. |
| `rz` | `number` |  | Rotation angle around the Z axis in radians. |

### CFrame.fromAxisAngle

**Signature:** `CFrame.fromAxisAngle(v: Vector3, r: number)`

Returns a [CFrame](/docs/reference/engine/datatypes/CFrame.md) rotated `r` radians around the axis `v`. The
axis vector is normalized internally, so it does not need to be unit
length. The resulting [CFrame](/docs/reference/engine/datatypes/CFrame.md) has no translation (position is
`(0, 0, 0)`). A positive angle represents a counter-clockwise rotation
when looking from the tip of the axis vector toward the origin (right-hand
rule).

```lua
-- Rotate 90 degrees around the Y axis
local cf = CFrame.fromAxisAngle(Vector3.yAxis, math.rad(90))
```

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `v` | `Vector3` |  | The axis of rotation (normalized internally). |
| `r` | `number` |  | The rotation angle in radians. |

### CFrame.fromMatrix

**Signature:** `CFrame.fromMatrix(pos: Vector3, vX: Vector3, vY: Vector3, vZ: Vector3)`

Returns a [CFrame](/docs/reference/engine/datatypes/CFrame.md) from a translation and the columns of a
rotation matrix. If `vZ` is excluded, the third column is calculated as
`vX:Cross(vY).Unit`.

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `pos` | `Vector3` |  | The 3D position of the [CFrame](/docs/reference/engine/datatypes/CFrame.md). |
| `vX` | `Vector3` |  | Equivalent to [RightVector](/docs/reference/engine/datatypes/CFrame.md). |
| `vY` | `Vector3` |  | Equivalent to [UpVector](/docs/reference/engine/datatypes/CFrame.md). |
| `vZ` | `Vector3` |  | Equivalent to -[LookVector](/docs/reference/engine/datatypes/CFrame.md). |

## Constants

| Name | Type | Description |
|------|------|-------------|
| `CFrame.identity` | `CFrame` | An identity [CFrame](/docs/reference/engine/datatypes/CFrame.md) with no translation or rotation. |

## Properties

### CFrame.Position

**Type:** `Vector3`

The positional component of the [CFrame](/docs/reference/engine/datatypes/CFrame.md) as a [Vector3](/docs/reference/engine/datatypes/Vector3.md).
Equivalent to `Vector3.new(cf.X, cf.Y, cf.Z)`.

### CFrame.Rotation

**Type:** `CFrame`

A copy of the [CFrame](/docs/reference/engine/datatypes/CFrame.md) with the positional component set to
`(0, 0, 0)`, retaining only the rotational component. Useful for isolating
a [CFrame](/docs/reference/engine/datatypes/CFrame.md) object's orientation independent of its position.

### CFrame.X

**Type:** `number`

The X component of the [CFrame](/docs/reference/engine/datatypes/CFrame.md) object's world-space position.
Equivalent to `CFrame.Position.X`.

### CFrame.Y

**Type:** `number`

The Y component of the [CFrame](/docs/reference/engine/datatypes/CFrame.md) object's world-space position.
Equivalent to `CFrame.Position.Y`.

### CFrame.Z

**Type:** `number`

The Z component of the [CFrame](/docs/reference/engine/datatypes/CFrame.md) object's world-space position.
Equivalent to `CFrame.Position.Z`.

### CFrame.LookVector

**Type:** `Vector3`

The forward-direction component of the [CFrame](/docs/reference/engine/datatypes/CFrame.md) object's
orientation, equivalent to the negated [ZVector](/docs/reference/engine/datatypes/CFrame.md)
or the negated third column of the rotation matrix.

```lua
local cf = CFrame.new(0, 0, 0)
local x, y, z, R00, R01, R02, R10, R11, R12, R20, R21, R22 = cf:GetComponents()

print(cf.LookVector)     --> (-0, -0, -1)
print(-cf.ZVector)       --> (-0, -0, -1)
print(-R02, -R12, -R22)  --> (-0 -0 -1)
```

Adding a [CFrame](/docs/reference/engine/datatypes/CFrame.md) object's
[LookVector](/docs/reference/engine/datatypes/CFrame.md) to itself produces a
[CFrame](/docs/reference/engine/datatypes/CFrame.md) moved forward in whichever direction it's facing by 1
unit.

### CFrame.RightVector

**Type:** `Vector3`

The right-direction component of the [CFrame](/docs/reference/engine/datatypes/CFrame.md) object's
orientation. Equivalent to [XVector](/docs/reference/engine/datatypes/CFrame.md) or the first
column of the rotation matrix.

```lua
local cf = CFrame.new(0, 0, 0)
local x, y, z, R00, R01, R02, R10, R11, R12, R20, R21, R22 = cf:GetComponents()

print(cf.RightVector)  --> (1, 0, 0)
print(cf.XVector)      --> (1, 0, 0)
print(R00, R10, R20)   --> (1 0 0)
```

### CFrame.UpVector

**Type:** `Vector3`

The up-direction component of the [CFrame](/docs/reference/engine/datatypes/CFrame.md) object's orientation.
Equivalent to [YVector](/docs/reference/engine/datatypes/CFrame.md) or the second column of
the rotation matrix.

```lua
local cf = CFrame.new(0, 0, 0)
local x, y, z, R00, R01, R02, R10, R11, R12, R20, R21, R22 = cf:GetComponents()

print(cf.UpVector)    --> (0, 1, 0)
print(cf.YVector)     --> (0, 1, 0)
print(R01, R11, R21)  --> (0 1 0)
```

### CFrame.XVector

**Type:** `Vector3`

The X component of the [CFrame](/docs/reference/engine/datatypes/CFrame.md) object's orientation. Equivalent
to [RightVector](/docs/reference/engine/datatypes/CFrame.md) or the first column of the
rotation matrix.

```lua
local cf = CFrame.new(0, 0, 0)
local x, y, z, R00, R01, R02, R10, R11, R12, R20, R21, R22 = cf:GetComponents()

print(cf.XVector)      --> (1, 0, 0)
print(cf.RightVector)  --> (1, 0, 0)
print(R00, R10, R20)   --> (1 0 0)
```

### CFrame.YVector

**Type:** `Vector3`

The Y component of the [CFrame](/docs/reference/engine/datatypes/CFrame.md) object's orientation. Equivalent
to [UpVector](/docs/reference/engine/datatypes/CFrame.md) or the second column of the
rotation matrix.

```lua
local cf = CFrame.new(0, 0, 0)
local x, y, z, R00, R01, R02, R10, R11, R12, R20, R21, R22 = cf:GetComponents()

print(cf.YVector)     --> (0, 1, 0)
print(cf.UpVector)    --> (0, 1, 0)
print(R01, R11, R21)  --> (0 1 0)
```

### CFrame.ZVector

**Type:** `Vector3`

The Z component of the [CFrame](/docs/reference/engine/datatypes/CFrame.md) object's orientation. Equivalent
to the negated [LookVector](/docs/reference/engine/datatypes/CFrame.md) or the third column
of the rotation matrix.

```lua
local cf = CFrame.new(0, 0, 0)
local x, y, z, R00, R01, R02, R10, R11, R12, R20, R21, R22 = cf:GetComponents()

print(cf.ZVector)      --> (0, 0, 1)
print(-cf.LookVector)  --> (0, 0, 1)
print(R02, R12, R22)   --> (0 0 1)
```

## Methods

### CFrame:Inverse

**Signature:** `CFrame:Inverse(): CFrame`

Returns the inverse of the [CFrame](/docs/reference/engine/datatypes/CFrame.md), representing the
transformation that undoes the original. For any [CFrame](/docs/reference/engine/datatypes/CFrame.md) `cf`,
the expression `cf * cf:Inverse()` produces the identity
[CFrame](/docs/reference/engine/datatypes/CFrame.md). The inverse reverses both the rotation (transposing the
rotation matrix) and the translation.

**Returns:** `CFrame` — The inverse CFrame that reverses this transformation.

### CFrame:Lerp

**Signature:** `CFrame:Lerp(goal: CFrame, alpha: number): CFrame`

Returns a [CFrame](/docs/reference/engine/datatypes/CFrame.md) interpolated between itself and `goal` by the
fraction `alpha`. The positional component is interpolated linearly while
the rotational component is interpolated using spherical linear
interpolation (slerp), producing a constant-speed rotation along the
shortest arc. An `alpha` of 0 returns the original [CFrame](/docs/reference/engine/datatypes/CFrame.md) and
an `alpha` of 1 returns `goal`.

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `goal` | `CFrame` |  | The target CFrame to interpolate toward. |
| `alpha` | `number` |  | The interpolation fraction, where 0 is the original and 1 is `goal`. |

**Returns:** `CFrame` — The interpolated CFrame between the original and `goal`.

### CFrame:Orthonormalize

**Signature:** `CFrame:Orthonormalize(): CFrame`

Returns an orthonormalized copy of the [CFrame](/docs/reference/engine/datatypes/CFrame.md). The
[BasePart.CFrame](/docs/reference/engine/classes/BasePart.md) property automatically applies orthonormalization,
but other APIs which take [CFrames](/docs/reference/engine/datatypes/CFrame.md) do not, so this method
is occasionally necessary when incrementally updating a [CFrame](/docs/reference/engine/datatypes/CFrame.md)
and using it with them.

**Returns:** `CFrame` — A copy of this CFrame with its rotation matrix orthonormalized.

### CFrame:ToWorldSpace

**Signature:** `CFrame:ToWorldSpace(...: Tuple<CFrame>): Tuple<CFrame>`

Receives one or more [CFrame](/docs/reference/engine/datatypes/CFrame.md) objects and returns them
transformed from object to world space. Equivalent to:

`CFrame * cf`

```lua
local cf = CFrame.new(5, 10, 0)

local offset = CFrame.new(0, 2, 0)

-- Output world space of offset CFrame relative to calling CFrame
print(cf:ToWorldSpace(offset))  --> 5, 12, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1
```

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `...` | `Tuple<CFrame>` |  | One or more CFrames specified in object (local) space. |

**Returns:** `Tuple<CFrame>` — The CFrames transformed into world space.

### CFrame:ToObjectSpace

**Signature:** `CFrame:ToObjectSpace(...: Tuple<CFrame>): Tuple<CFrame>`

Receives one or more [CFrame](/docs/reference/engine/datatypes/CFrame.md) objects and returns them
transformed from world to object space. Equivalent to:

`CFrame:Inverse() * cf`

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `...` | `Tuple<CFrame>` |  | One or more CFrames specified in world space. |

**Returns:** `Tuple<CFrame>` — The CFrames transformed into object (local) space.

### CFrame:PointToWorldSpace

**Signature:** `CFrame:PointToWorldSpace(...: Tuple<Vector3>): Tuple<Vector3>`

Receives one or more [Vector3](/docs/reference/engine/datatypes/Vector3.md) objects and returns them
transformed from object to world space. Equivalent to:

`CFrame * v3`

```lua
local cf = CFrame.new(5, 10, 0)

-- Output core world space of the CFrame
print(cf:PointToWorldSpace())  --> 5, 10, 0
-- Output world space of a Vector3 (0, 4, 0) relative to the CFrame (object space)
print(cf:PointToWorldSpace(Vector3.new(0, 4, 0)))  --> 5, 14, 0
```

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `...` | `Tuple<Vector3>` |  | One or more points specified in object (local) space. |

**Returns:** `Tuple<Vector3>` — The points transformed into world space.

### CFrame:PointToObjectSpace

**Signature:** `CFrame:PointToObjectSpace(...: Tuple<Vector3>): Tuple<Vector3>`

Receives one or more [Vector3](/docs/reference/engine/datatypes/Vector3.md) objects and returns them
transformed from world to object space. Equivalent to:

`CFrame:Inverse() * v3`

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `...` | `Tuple<Vector3>` |  | One or more points specified in world space. |

**Returns:** `Tuple<Vector3>` — The points transformed into object (local) space.

### CFrame:VectorToWorldSpace

**Signature:** `CFrame:VectorToWorldSpace(...: Tuple<Vector3>): Tuple<Vector3>`

Receives one or more [Vector3](/docs/reference/engine/datatypes/Vector3.md) objects and returns them rotated
from object to world space. Equivalent to:

`(CFrame - CFrame.Position) * v3`

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `...` | `Tuple<Vector3>` |  | One or more direction vectors specified in object (local) space. |

**Returns:** `Tuple<Vector3>` — The vectors rotated into world space (translation ignored).

### CFrame:VectorToObjectSpace

**Signature:** `CFrame:VectorToObjectSpace(...: Tuple<Vector3>): Tuple<Vector3>`

Receives one or more [Vector3](/docs/reference/engine/datatypes/Vector3.md) objects and returns them rotated
from world to object space. Equivalent to:

`(CFrame:Inverse() - CFrame:Inverse().Position) * v3`

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `...` | `Tuple<Vector3>` |  | One or more direction vectors specified in world space. |

**Returns:** `Tuple<Vector3>` — The vectors rotated into object (local) space (translation ignored).

### CFrame:GetComponents

**Signature:** `CFrame:GetComponents(): Tuple`

Returns the 12 numeric components of the [CFrame](/docs/reference/engine/datatypes/CFrame.md) as a tuple:
`x`, `y`, `z` (position), followed by `R00`, `R01`, `R02`, `R10`, `R11`,
`R12`, `R20`, `R21`, `R22` (the 3&times;3 rotation matrix in row-major
order). This is the reverse of the 12-argument [CFrame.new()](/docs/reference/engine/datatypes/CFrame.md)
constructor.

```lua
local cf = CFrame.new(1, 2, 3) * CFrame.fromEulerAnglesXYZ(0, math.rad(90), 0)
local x, y, z, R00, R01, R02, R10, R11, R12, R20, R21, R22 = cf:GetComponents()
```

**Returns:** `Tuple` — The 12 numeric values: x, y, z, R00, R01, R02, R10, R11, R12, R20,
R21, R22.

### CFrame:ToEulerAngles

**Signature:** `CFrame:ToEulerAngles(order?: RotationOrder): number, number, number`

Returns approximate angles that could be used to generate the
[CFrame](/docs/reference/engine/datatypes/CFrame.md) using the optional [RotationOrder](/docs/reference/engine/enums/RotationOrder.md). If you don't
provide `order`, the method uses [RotationOrder.XYZ](/docs/reference/engine/enums/RotationOrder.md).

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `order` | `RotationOrder` | `Enum.RotationOrder.XYZ` | The rotation order used for decomposition. |

**Returns:** `number`, `number`, `number` — The X-axis rotation angle in radians. The Y-axis rotation angle in radians. The Z-axis rotation angle in radians.

### CFrame:ToEulerAnglesXYZ

**Signature:** `CFrame:ToEulerAnglesXYZ(): number, number, number`

Returns the approximate angles, in radians, that could be used to generate
the [CFrame](/docs/reference/engine/datatypes/CFrame.md) using [RotationOrder.XYZ](/docs/reference/engine/enums/RotationOrder.md). The three returned
values represent rotations around the X, Y, and Z axes respectively. Due
to the nature of Euler angle decomposition, the angles are approximate and
subject to gimbal lock near pitch angles of &plusmn;90 degrees.

**Returns:** `number`, `number`, `number` — The X-axis rotation angle in radians. The Y-axis rotation angle in radians. The Z-axis rotation angle in radians.

### CFrame:ToEulerAnglesYXZ

**Signature:** `CFrame:ToEulerAnglesYXZ(): number, number, number`

Returns the approximate angles, in radians, that could be used to generate
the [CFrame](/docs/reference/engine/datatypes/CFrame.md) using [RotationOrder.YXZ](/docs/reference/engine/enums/RotationOrder.md). The three returned
values represent rotations around the X, Y, and Z axes respectively. Due
to the nature of Euler angle decomposition, the angles are approximate and
subject to gimbal lock near pitch angles of &plusmn;90 degrees.

**Returns:** `number`, `number`, `number` — The X-axis rotation angle in radians. The Y-axis rotation angle in radians. The Z-axis rotation angle in radians.

### CFrame:ToOrientation

**Signature:** `CFrame:ToOrientation(): number, number, number`

Returns the approximate angles, in radians, that could be used to generate
the [CFrame](/docs/reference/engine/datatypes/CFrame.md) using [RotationOrder.YXZ](/docs/reference/engine/enums/RotationOrder.md). Equivalent to
[CFrame:ToEulerAnglesYXZ()](/docs/reference/engine/datatypes/CFrame.md).

**Returns:** `number`, `number`, `number` — The X-axis rotation angle in radians. The Y-axis rotation angle in radians. The Z-axis rotation angle in radians.

### CFrame:ToAxisAngle

**Signature:** `CFrame:ToAxisAngle(): Vector3, number`

Returns a unit [Vector3](/docs/reference/engine/datatypes/Vector3.md) representing the axis of rotation and a
number representing the angle of rotation in radians. A positive angle
represents counter-clockwise rotation when looking from the tip of the
axis vector toward the origin (right-hand rule). This is the inverse of
[CFrame.fromAxisAngle()](/docs/reference/engine/datatypes/CFrame.md).

**Returns:** `Vector3`, `number` — A unit vector representing the axis of rotation. The rotation angle in radians.

### CFrame:components

**Signature:** `CFrame:components(): Tuple`

Equivalent to [CFrame:GetComponents()](/docs/reference/engine/datatypes/CFrame.md).

**Returns:** `Tuple` — The 12 numeric values: x, y, z, R00, R01, R02, R10, R11, R12, R20,
R21, R22.

### CFrame:FuzzyEq

**Signature:** `CFrame:FuzzyEq(other: CFrame, epsilon?: number): bool`

Returns `true` if the other [CFrame](/docs/reference/engine/datatypes/CFrame.md) is sufficiently close to
this [CFrame](/docs/reference/engine/datatypes/CFrame.md) in both position and rotation. The `epsilon` value
is used to control the tolerance for this similarity; this value is
optional and should be a small positive value if provided. The similarity
for position is component-wise while rotation uses a fast approximation of
the angle difference.

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `other` | `CFrame` |  | The CFrame to compare against. |
| `epsilon` | `number` | `0.00001 (1e-5)` | The tolerance for comparing position and rotation components. |

**Returns:** `bool` — True if the two CFrames are within `epsilon` of each other.

### CFrame:AngleBetween

**Signature:** `CFrame:AngleBetween(other: CFrame): number`

Returns the angle, in radians, between the orientation of one
[CFrame](/docs/reference/engine/datatypes/CFrame.md) and another. This function does not take the position of
either [CFrame](/docs/reference/engine/datatypes/CFrame.md) into account and only looks at the relative
orientation.

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `other` | `CFrame` |  | The CFrame whose orientation is compared against this CFrame. |

**Returns:** `number` — The angle in radians between the two orientations, in the range [0,
pi].

## Math Operations

| Operation | Type A | Type B | Returns | Description |
|-----------|--------|--------|---------|-------------|
| `*` | `CFrame` | `CFrame` | `CFrame` | Produces a new [CFrame](/docs/reference/engine/datatypes/CFrame.md) representing the composition of the two [CFrames](/docs/reference/engine/datatypes/CFrame.md). |
| `*` | `CFrame` | `Vector3` | `Vector3` | Produces a [Vector3](/docs/reference/engine/datatypes/Vector3.md) transformed from object to world coordinates. |
| `+` | `CFrame` | `Vector3` | `CFrame` | Produces a [CFrame](/docs/reference/engine/datatypes/CFrame.md) translated in world space by the [Vector3](/docs/reference/engine/datatypes/Vector3.md). |
| `-` | `CFrame` | `Vector3` | `CFrame` | Produces a [CFrame](/docs/reference/engine/datatypes/CFrame.md) translated in world space by the negative [Vector3](/docs/reference/engine/datatypes/Vector3.md). |