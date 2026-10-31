---
name: Axes
last_updated: 2026-10-30T19:55:54Z
type: datatype
summary: "The `Axes` data type is for the ArcHandles class to control which rotation axes are currently enabled."
---

# Axes

The `Axes` data type is for the [ArcHandles](/docs/reference/engine/classes/ArcHandles.md) class to control which
rotation axes are currently enabled.

**Type:** datatype

## Description

The [Axes](/docs/reference/engine/datatypes/Axes.md) data type contains a set of enabled 3D axes, represented
as a bitmask. It is used by the [ArcHandles](/docs/reference/engine/classes/ArcHandles.md) class through its
[Axes](/docs/reference/engine/classes/ArcHandles.md) property to control which rotation arc handles
are visible.

[Axes](/docs/reference/engine/datatypes/Axes.md) exposes three axis properties (`X`, `Y`, `Z`) and six face
properties (`Top`, `Bottom`, `Left`, `Right`, `Front`, `Back`). Because faces
map to their corresponding axis, face pairs always share the same value: `Top`
and `Bottom` both reflect the Y axis, `Left` and `Right` both reflect the X
axis, and `Front` and `Back` both reflect the Z axis.

```lua
-- Enable arc handles for the X and Y axes only
local arcHandles = Instance.new("ArcHandles")
arcHandles.Axes = Axes.new(Enum.Axis.X, Enum.Axis.Y)
```

Like most data types on Roblox, the [Axes](/docs/reference/engine/datatypes/Axes.md) data type is immutable:
you cannot assign to its properties once created.

## Constructors

### Axes.new

**Signature:** `Axes.new(axes: Tuple)`

Creates a new [Axes](/docs/reference/engine/datatypes/Axes.md) from up to 6 [Axis](/docs/reference/engine/enums/Axis.md) or [NormalId](/docs/reference/engine/enums/NormalId.md)
values. Each [NormalId](/docs/reference/engine/enums/NormalId.md) is converted to its corresponding axis (for
example, [NormalId.Top](/docs/reference/engine/enums/NormalId.md) and [NormalId.Bottom](/docs/reference/engine/enums/NormalId.md) both enable the Y
axis). Calling `Axes.new()` with no arguments returns an Axes with all
properties set to `false`.

```lua
-- Using Enum.Axis values
local axes = Axes.new(Enum.Axis.X, Enum.Axis.Z)
print(axes.X) -- true
print(axes.Y) -- false

-- Using Enum.NormalId values (converted to axes)
local axes2 = Axes.new(Enum.NormalId.Top, Enum.NormalId.Right)
print(axes2.Y) -- true (Top -> Y axis)
print(axes2.X) -- true (Right -> X axis)
```

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `axes` | `Tuple` |  | Any combination of [Axis](/docs/reference/engine/enums/Axis.md) and/or [NormalId](/docs/reference/engine/enums/NormalId.md) values (up to 6) specifying which axes to enable. |

## Properties

### Axes.X

**Type:** `bool`

Whether the X axis is enabled. Defaults to `false` when constructed via
`Axes.new()` with no arguments. This property is equivalent to both `Left`
and `Right`, which also reflect the X axis state.

### Axes.Y

**Type:** `bool`

Whether the Y axis is enabled. Defaults to `false` when constructed via
`Axes.new()` with no arguments. This property is equivalent to both `Top`
and `Bottom`, which also reflect the Y axis state.

### Axes.Z

**Type:** `bool`

Whether the Z axis is enabled. Defaults to `false` when constructed via
`Axes.new()` with no arguments. This property is equivalent to both
`Front` and `Back`, which also reflect the Z axis state.

### Axes.Top

**Type:** `bool`

Whether the top face is included. This corresponds to the positive Y
direction ([NormalId.Top](/docs/reference/engine/enums/NormalId.md)) and is always equal to the `Y` property.
Defaults to `false`.

### Axes.Bottom

**Type:** `bool`

Whether the bottom face is included. This corresponds to the negative Y
direction ([NormalId.Bottom](/docs/reference/engine/enums/NormalId.md)) and is always equal to the `Y`
property. Defaults to `false`.

### Axes.Left

**Type:** `bool`

Whether the left face is included. This corresponds to the negative X
direction ([NormalId.Left](/docs/reference/engine/enums/NormalId.md)) and is always equal to the `X` property.
Defaults to `false`.

### Axes.Right

**Type:** `bool`

Whether the right face is included. This corresponds to the positive X
direction ([NormalId.Right](/docs/reference/engine/enums/NormalId.md)) and is always equal to the `X` property.
Defaults to `false`.

### Axes.Back

**Type:** `bool`

Whether the back face is included. This corresponds to the positive Z
direction ([NormalId.Back](/docs/reference/engine/enums/NormalId.md)) and is always equal to the `Z` property.
Defaults to `false`.

### Axes.Front

**Type:** `bool`

Whether the front face is included. This corresponds to the negative Z
direction ([NormalId.Front](/docs/reference/engine/enums/NormalId.md)) and is always equal to the `Z` property.
Defaults to `false`.