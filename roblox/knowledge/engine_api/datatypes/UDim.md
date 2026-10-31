---
name: UDim
last_updated: 2026-10-30T19:55:54Z
type: datatype
summary: "Represents a one-dimensional value with two components, a relative scale and an absolute offset."
---

# UDim

Represents a one-dimensional value with two components, a relative scale and
an absolute offset.

**Type:** datatype

## Description

The [UDim](/docs/reference/engine/datatypes/UDim.md) data type represents a one-dimensional value with two
components: a relative scale and an absolute offset in logical pixels. At
evaluation time, the engine computes the final pixel value as
`Scale * referenceMeasurement + Offset`, where the reference measurement is
typically the size of a parent [GuiObject](/docs/reference/engine/classes/GuiObject.md) along the corresponding axis.

UDim values appear individually in properties such as
[UICorner.CornerRadius](/docs/reference/engine/classes/UICorner.md), [UIPadding.PaddingTop](/docs/reference/engine/classes/UIPadding.md), and
[UIStroke.Thickness](/docs/reference/engine/classes/UIStroke.md), or paired as a [UDim2](/docs/reference/engine/datatypes/UDim2.md) for
two-dimensional sizing and positioning.

```lua
-- 50% of the parent plus 10 extra logical pixels
local dimension = UDim.new(0.5, 10)
```

## Constructors

### UDim.new

**Signature:** `UDim.new(Scale: number, Offset: number)`

Returns a new [UDim](/docs/reference/engine/datatypes/UDim.md) from the given `Scale` and `Offset`
components. Both parameters are optional and default to `0` when omitted;
calling `UDim.new()` with no arguments produces a UDim equivalent to
`UDim.new(0, 0)`.

```lua
local fullScale = UDim.new(1, 0)    -- 100% of parent, no pixel offset
local fixedPixels = UDim.new(0, 200) -- 0% scale, 200 pixel offset
local mixed = UDim.new(0.5, 20)      -- 50% of parent plus 20 pixels
```

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `Scale` | `number` |  | The relative scale component, expressed as a fraction of the reference measurement (for example, `0.5` for 50% of the parent size along the corresponding axis). Defaults to `0`. |
| `Offset` | `number` |  | The absolute pixel offset added after the scale is applied. Stored as an integer. Defaults to `0`. |

## Properties

### UDim.Scale

**Type:** `number`

The relative scale component of the [UDim](/docs/reference/engine/datatypes/UDim.md), expressed as a
fraction of a reference measurement (typically the corresponding axis of a
parent [GuiObject](/docs/reference/engine/classes/GuiObject.md)). A value of `1` represents the full reference
measurement, `0.5` represents half, and `0` means the scale contributes
nothing to the resolved pixel value. Defaults to `0` when not specified in
the constructor. This property is read-only.

### UDim.Offset

**Type:** `number`

The absolute offset component of the [UDim](/docs/reference/engine/datatypes/UDim.md) in pixels. This value
is added to the resolved scale portion (`Scale * referenceMeasurement`) to
produce the final pixel measurement. The offset is stored as an integer.
Defaults to `0` when not specified in the constructor. This property is
read-only.

## Math Operations

| Operation | Type A | Type B | Returns | Description |
|-----------|--------|--------|---------|-------------|
| `+` | `UDim` | `UDim` | `UDim` | Produces a [UDim](/docs/reference/engine/datatypes/UDim.md) representing the sum of the two [UDim](/docs/reference/engine/datatypes/UDim.md) values. |
| `-` | `UDim` | `UDim` | `UDim` | Produces a [UDim](/docs/reference/engine/datatypes/UDim.md) representing the difference between the two [UDim](/docs/reference/engine/datatypes/UDim.md) values. |