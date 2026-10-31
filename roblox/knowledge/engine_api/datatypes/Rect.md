---
name: Rect
last_updated: 2026-10-30T19:55:54Z
type: datatype
summary: "A value that represents a two-dimensional rectangle."
---

# Rect

A value that represents a two-dimensional rectangle.

**Type:** datatype

## Description

**Rect** describes a rectangle on a 2D plane. It is constructed using two
corners, either two [Vector2](/docs/reference/engine/datatypes/Vector2.md) positions or four numbers:

```lua
local rect1 = Rect.new(Vector2.new(10, 10), Vector2.new(80, 80))
local rect2 = Rect.new(10, 10, 80, 80)
```

This data type is used in the [ImageLabel.SliceCenter](/docs/reference/engine/classes/ImageLabel.md) property which
determines the center area of a scaled image.

## Constructors

### Rect.new

**Signature:** `Rect.new()`

Constructs a new **Rect** with two zero [Vector2](/docs/reference/engine/datatypes/Vector2.md) positions.

### Rect.new

**Signature:** `Rect.new(min: Vector2, max: Vector2)`

Constructs a new **Rect** given two [Vector2](/docs/reference/engine/datatypes/Vector2.md) positions: `min` as
the top-left corner and `max` as the bottom-right corner.

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `min` | `Vector2` |  | One corner of the rectangle as a [Vector2](/docs/reference/engine/datatypes/Vector2.md). The constructor computes the component-wise minimum of `min` and `max` to determine the top-left corner. |
| `max` | `Vector2` |  | The other corner of the rectangle as a [Vector2](/docs/reference/engine/datatypes/Vector2.md). The constructor computes the component-wise maximum of `min` and `max` to determine the bottom-right corner. |

### Rect.new

**Signature:** `Rect.new(minX: number, minY: number, maxX: number, maxY: number)`

Constructs a new **Rect** using `minX` and `minY` as coordinates for the
top-left corner, and `maxX` and `maxY` as coordinates for the bottom-right
corner.

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `minX` | `number` |  | The X coordinate of the top-left corner of the rectangle. |
| `minY` | `number` |  | The Y coordinate of the top-left corner of the rectangle. |
| `maxX` | `number` |  | The X coordinate of the bottom-right corner of the rectangle. |
| `maxY` | `number` |  | The Y coordinate of the bottom-right corner of the rectangle. |

## Properties

### Rect.Width

**Type:** `number`

The horizontal span of the rectangle, equal to `Max.X - Min.X`. This value
is always non-negative because the constructor normalizes the input
coordinates so that [Min](/docs/reference/engine/datatypes/Rect.md) is component-wise less than or
equal to [Max](/docs/reference/engine/datatypes/Rect.md). Defaults to `0` for a [Rect](/docs/reference/engine/datatypes/Rect.md)
created with no arguments.

### Rect.Height

**Type:** `number`

The vertical span of the rectangle, equal to `Max.Y - Min.Y`. This value
is always non-negative because the constructor normalizes the input
coordinates so that [Min](/docs/reference/engine/datatypes/Rect.md) is component-wise less than or
equal to [Max](/docs/reference/engine/datatypes/Rect.md). Defaults to `0` for a [Rect](/docs/reference/engine/datatypes/Rect.md)
created with no arguments.

### Rect.Min

**Type:** `Vector2`

The top-left corner of the rectangle as a [Vector2](/docs/reference/engine/datatypes/Vector2.md). When you
construct a [Rect](/docs/reference/engine/datatypes/Rect.md) with two positions, this property returns the
component-wise minimum of those positions regardless of the order they
were passed in. Defaults to `(0, 0)` for a [Rect](/docs/reference/engine/datatypes/Rect.md) created with no
arguments.

### Rect.Max

**Type:** `Vector2`

The bottom-right corner of the rectangle as a [Vector2](/docs/reference/engine/datatypes/Vector2.md). When you
construct a [Rect](/docs/reference/engine/datatypes/Rect.md) with two positions, this property returns the
component-wise maximum of those positions regardless of the order they
were passed in. Defaults to `(0, 0)` for a [Rect](/docs/reference/engine/datatypes/Rect.md) created with no
arguments.