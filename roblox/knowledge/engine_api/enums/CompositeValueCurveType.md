---
name: CompositeValueCurveType
last_updated: 2026-10-30T19:55:54Z
type: enum
summary: "Describes the type of value animated by a CompositeValueCurve."
---

# CompositeValueCurveType

Describes the type of value animated by a [CompositeValueCurve](/docs/reference/engine/classes/CompositeValueCurve.md).

**Type:** enum

## Items

| Name | Value | Description |
|------|-------|-------------|
| `ColorRGB` | 0 | The [CompositeValueCurve](/docs/reference/engine/classes/CompositeValueCurve.md) will animate children of type [FloatCurve](/docs/reference/engine/classes/FloatCurve.md) named `"R"`, `"G"`, and `"B"` to animate the corresponding components of the [Color3](/docs/reference/engine/datatypes/Color3.md) value returned by the method [CompositeValueCurve:GetValueAtTime()](/docs/reference/engine/classes/CompositeValueCurve.md). |
| `ColorHSV` | 1 | The [CompositeValueCurve](/docs/reference/engine/classes/CompositeValueCurve.md) will animate children of type [FloatCurve](/docs/reference/engine/classes/FloatCurve.md) named `"H"`, `"S"`, and `"V"` to animate hue, saturation, and value of a color that will be converted to RGB before returning a [Color3](/docs/reference/engine/datatypes/Color3.md) value from the method [CompositeValueCurve:GetValueAtTime()](/docs/reference/engine/classes/CompositeValueCurve.md). |
| `NumberRange` | 2 | The [CompositeValueCurve](/docs/reference/engine/classes/CompositeValueCurve.md) will animate children of type [FloatCurve](/docs/reference/engine/classes/FloatCurve.md) named `"Min"` and `"Max"` to animate the corresponding components of the [NumberRange](/docs/reference/engine/datatypes/NumberRange.md) value returned by the method [CompositeValueCurve:GetValueAtTime()](/docs/reference/engine/classes/CompositeValueCurve.md). |
| `Rect` | 3 | The [CompositeValueCurve](/docs/reference/engine/classes/CompositeValueCurve.md) will animate children of type [FloatCurve](/docs/reference/engine/classes/FloatCurve.md) named `"MinX"`, `"MaxX"`, `"MinY"`, and `"MaxY"` to animate the corresponding components of the [Rect](/docs/reference/engine/datatypes/Rect.md) value returned by the method [CompositeValueCurve:GetValueAtTime()](/docs/reference/engine/classes/CompositeValueCurve.md). |
| `UDim` | 4 | The [CompositeValueCurve](/docs/reference/engine/classes/CompositeValueCurve.md) will animate children of type [FloatCurve](/docs/reference/engine/classes/FloatCurve.md) named `"Scale"` and `"Offset"` to animate the corresponding components of the [UDim](/docs/reference/engine/datatypes/UDim.md) value returned by the method [CompositeValueCurve:GetValueAtTime()](/docs/reference/engine/classes/CompositeValueCurve.md). |
| `UDim2` | 5 | The [CompositeValueCurve](/docs/reference/engine/classes/CompositeValueCurve.md) will animate children of type [FloatCurve](/docs/reference/engine/classes/FloatCurve.md) named `"ScaleX"`, `"OffsetX"`, `"ScaleY"`, and `"OffsetY"` to animate the corresponding components of the [UDim2](/docs/reference/engine/datatypes/UDim2.md) value returned by the method [CompositeValueCurve:GetValueAtTime()](/docs/reference/engine/classes/CompositeValueCurve.md). |
| `Vector2` | 6 | The [CompositeValueCurve](/docs/reference/engine/classes/CompositeValueCurve.md) will animate children of type [FloatCurve](/docs/reference/engine/classes/FloatCurve.md) named `"X"` and `"Y"` to animate the corresponding components of the [Vector2](/docs/reference/engine/datatypes/Vector2.md) value returned by the method [CompositeValueCurve:GetValueAtTime()](/docs/reference/engine/classes/CompositeValueCurve.md). |
| `Vector3` | 7 | The [CompositeValueCurve](/docs/reference/engine/classes/CompositeValueCurve.md) will animate children of type [FloatCurve](/docs/reference/engine/classes/FloatCurve.md) named `"X"`, `"Y"`, and `"Z"` to animate the corresponding components of the [Vector3](/docs/reference/engine/datatypes/Vector3.md) value returned by the method [CompositeValueCurve:GetValueAtTime()](/docs/reference/engine/classes/CompositeValueCurve.md). |