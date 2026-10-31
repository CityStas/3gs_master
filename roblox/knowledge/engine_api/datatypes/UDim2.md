---
name: UDim2
last_updated: 2026-10-30T19:55:54Z
type: datatype
summary: "Represents a two-dimensional value where each dimension is composed of a relative scale and an absolute offset."
---

# UDim2

Represents a two-dimensional value where each dimension is composed of a
relative scale and an absolute offset.

**Type:** datatype

## Description

The [UDim2](/docs/reference/engine/datatypes/UDim2.md) data type represents a two-dimensional value where each
dimension is composed of a relative scale and an absolute offset in logical
pixels. It is a combination of two [UDim](/docs/reference/engine/datatypes/UDim.md) data types representing the
**X** and **Y** dimensions. The most common usages for [UDim2](/docs/reference/engine/datatypes/UDim2.md) are
setting the [Size](/docs/reference/engine/classes/GuiObject.md) and
[Position](/docs/reference/engine/classes/GuiObject.md) of [GuiObjects](/docs/reference/engine/classes/GuiObject.md).

```lua
local guiObject = Instance.new("Frame")
guiObject.Size = UDim2.new(0, 300, 1, 0)  -- 300 logical pixels wide; full height of parent
guiObject.Position = UDim2.new(0, 50, 0, 0)  -- 50 logical pixels from the left
print(guiObject.Size) --> {0, 300}, {1, 0}
```

## Constructors

### UDim2.new

**Signature:** `UDim2.new()`

Returns a new [UDim2](/docs/reference/engine/datatypes/UDim2.md) with both dimensions set to zero —
equivalent to `UDim2.new(0, 0, 0, 0)`. All four components (X scale, X
offset, Y scale, Y offset) default to `0`.

### UDim2.new

**Signature:** `UDim2.new(xScale?: number, xOffset?: number, yScale?: number, yOffset?: number)`

Returns a new [UDim2](/docs/reference/engine/datatypes/UDim2.md) from four numbers that define both axes.
Each pair of arguments defines one dimension: `xScale` and `xOffset` for
the horizontal (**X**) axis, then `yScale` and `yOffset` for the vertical
(**Y**) axis. Scale is a relative fraction of the parent container's size
(typically between `0` and `1`), while offset is an absolute logical pixel
value added after scaling. All parameters default to `0`.

```lua
-- 50% width + 20 logical pixels padding, full height
local size = UDim2.new(0.5, 20, 1, 0)
```

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `xScale` | `number` | `0` | The **X** dimension scale. |
| `xOffset` | `number` | `0` | The **X** dimension offset. |
| `yScale` | `number` | `0` | The **Y** dimension scale. |
| `yOffset` | `number` | `0` | The **Y** dimension offset. |

### UDim2.new

**Signature:** `UDim2.new(x: UDim, y: UDim)`

Constructs a [UDim2](/docs/reference/engine/datatypes/UDim2.md) by composing two [UDim](/docs/reference/engine/datatypes/UDim.md) values
directly. The first argument becomes the horizontal dimension (accessible
via `.X` or `.Width`) and the second becomes the vertical dimension
(accessible via `.Y` or `.Height`).

```lua
local x = UDim.new(0.5, 10)
local y = UDim.new(1, 0)
local size = UDim2.new(x, y)  -- equivalent to UDim2.new(0.5, 10, 1, 0)
```

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `x` | `UDim` |  | The [UDim](/docs/reference/engine/datatypes/UDim.md) for the horizontal (**X**) axis. |
| `y` | `UDim` |  | The [UDim](/docs/reference/engine/datatypes/UDim.md) for the vertical (**Y**) axis. |

### UDim2.fromScale

**Signature:** `UDim2.fromScale(xScale?: number, yScale?: number)`

Returns a new [UDim2](/docs/reference/engine/datatypes/UDim2.md) with the given scalar coordinates and no
offsets. Equivalent to:

```lua
local xScale, yScale = 0.5, 0.25
print(UDim2.fromScale(xScale, yScale) == UDim2.new(xScale, 0, yScale, 0)) --> true
```

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `xScale` | `number` | `0` | The relative scale for the horizontal (**X**) axis. |
| `yScale` | `number` | `0` | The relative scale for the vertical (**Y**) axis. |

### UDim2.fromOffset

**Signature:** `UDim2.fromOffset(xOffset?: number, yOffset?: number)`

Returns a new [UDim2](/docs/reference/engine/datatypes/UDim2.md) with the given offset coordinates and no
scaling. Equivalent to:

```lua
local xOffset, yOffset = 100, 50
print(UDim2.fromOffset(xOffset, yOffset) == UDim2.new(0, xOffset, 0, yOffset)) --> true
```

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `xOffset` | `number` | `0` | The absolute logical pixel offset for the horizontal (**X**) axis. |
| `yOffset` | `number` | `0` | The absolute logical pixel offset for the vertical (**Y**) axis. |

## Properties

### UDim2.X

**Type:** `UDim`

The [UDim](/docs/reference/engine/datatypes/UDim.md) component for the horizontal axis. The returned
[UDim](/docs/reference/engine/datatypes/UDim.md) has a `.Scale` (relative fraction) and `.Offset` (absolute
logical pixels). This property is equivalent to [UDim2.Width](/docs/reference/engine/datatypes/UDim2.md).

```lua
local pos = UDim2.new(0.5, 10, 1, 0)
print(pos.X.Scale)   -- 0.5
print(pos.X.Offset)  -- 10
```

### UDim2.Y

**Type:** `UDim`

The [UDim](/docs/reference/engine/datatypes/UDim.md) component for the vertical axis. The returned
[UDim](/docs/reference/engine/datatypes/UDim.md) has a `.Scale` (relative fraction) and `.Offset` (absolute
logical pixels). This property is equivalent to [UDim2.Height](/docs/reference/engine/datatypes/UDim2.md).

```lua
local pos = UDim2.new(0.5, 10, 1, 0)
print(pos.Y.Scale)   -- 1
print(pos.Y.Offset)  -- 0
```

### UDim2.Width

**Type:** `UDim`

A synonym for [UDim2.X](/docs/reference/engine/datatypes/UDim2.md). Returns the [UDim](/docs/reference/engine/datatypes/UDim.md) component
for the horizontal axis, containing both `.Scale` and `.Offset`.

### UDim2.Height

**Type:** `UDim`

A synonym for [UDim2.Y](/docs/reference/engine/datatypes/UDim2.md). Returns the [UDim](/docs/reference/engine/datatypes/UDim.md) component
for the vertical axis, containing both `.Scale` and `.Offset`.

## Methods

### UDim2:Lerp

**Signature:** `UDim2:Lerp(goal: UDim2, alpha: number): UDim2`

Returns a [UDim2](/docs/reference/engine/datatypes/UDim2.md) interpolated linearly between this
[UDim2](/docs/reference/engine/datatypes/UDim2.md) and the given `goal`. The `alpha` value should be a
number between `0` and `1`.

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `goal` | `UDim2` |  | The target [UDim2](/docs/reference/engine/datatypes/UDim2.md) to interpolate toward. |
| `alpha` | `number` |  | A value between `0` (returns this UDim2) and `1` (returns `goal`) controlling the interpolation. |

**Returns:** `UDim2` — A [UDim2](/docs/reference/engine/datatypes/UDim2.md) where each axis is independently interpolated
between this value and `goal` by the fraction `alpha`.

## Math Operations

| Operation | Type A | Type B | Returns | Description |
|-----------|--------|--------|---------|-------------|
| `+` | `UDim2` | `UDim2` | `UDim2` | Produces a [UDim2](/docs/reference/engine/datatypes/UDim2.md) with components that are the sum of the respective components of the two [UDim2](/docs/reference/engine/datatypes/UDim2.md) objects. |
| `-` | `UDim2` | `UDim2` | `UDim2` | Produces a [UDim2](/docs/reference/engine/datatypes/UDim2.md) with components that are the difference of the respective components of the two [UDim2](/docs/reference/engine/datatypes/UDim2.md) objects. |