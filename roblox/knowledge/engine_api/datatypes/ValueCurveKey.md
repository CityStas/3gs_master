---
name: ValueCurveKey
last_updated: 2026-10-30T19:55:54Z
type: datatype
summary: "A time-value pair used with ValueCurve instances."
---

# ValueCurveKey

A time-value pair used with [ValueCurve](/docs/reference/engine/classes/ValueCurve.md) instances.

**Type:** datatype

## Description

A time-value pair used with [ValueCurve](/docs/reference/engine/classes/ValueCurve.md) instances.

The [Interpolation](/docs/reference/engine/datatypes/ValueCurveKey.md) property dictates the
interpolation mode for the segment started by this key and ended by the next
key on the curve. Each segment may use a different interpolation mode.

The [LeftTangent](/docs/reference/engine/datatypes/ValueCurveKey.md) and
[RightTangent](/docs/reference/engine/datatypes/ValueCurveKey.md) properties apply to the
cubic interpolation mode and define the desired tangent (slope) at the key.
Different left and right values can be used to encode discontinuities in slope
at the key. Attempting to set a
[RightTangent](/docs/reference/engine/datatypes/ValueCurveKey.md) value on a key that doesn't
use the cubic interpolation mode will result in a runtime error. It is
possible to set the [LeftTangent](/docs/reference/engine/datatypes/ValueCurveKey.md) property
on any key, as it will be used should the preceding segment use cubic
interpolation.

## Constructors

### ValueCurveKey.new

**Signature:** `ValueCurveKey.new(time: number, value: any, Interpolation: KeyInterpolationMode)`

Creates a new [ValueCurveKey](/docs/reference/engine/datatypes/ValueCurveKey.md) at a given time and value.
[LeftTangent](/docs/reference/engine/datatypes/ValueCurveKey.md) and
[RightTangent](/docs/reference/engine/datatypes/ValueCurveKey.md) are left uninitialized
and, if not initialized, tangent values of '0' will be used when
evaluating the curve.

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `time` | `number` |  | Time at which to create the new [ValueCurveKey](/docs/reference/engine/datatypes/ValueCurveKey.md). |
| `value` | `any` |  | Value of the new [ValueCurveKey](/docs/reference/engine/datatypes/ValueCurveKey.md). |
| `Interpolation` | `KeyInterpolationMode` |  | The interpolation mode for the curve segment starting at this key. Defaults to [KeyInterpolationMode.Constant](/docs/reference/engine/enums/KeyInterpolationMode.md) if omitted. |

## Properties

### ValueCurveKey.Interpolation

**Type:** `KeyInterpolationMode`

Specifies the interpolation mode used for the curve segment that begins at
this key and ends at the next key on the [ValueCurve](/docs/reference/engine/classes/ValueCurve.md). Each segment
of the curve can use a different interpolation mode. The default value is
[KeyInterpolationMode.Constant](/docs/reference/engine/enums/KeyInterpolationMode.md).

The available modes are:

- **Constant** — the segment holds the value of this key until the next
  key.
- **Linear** — the segment linearly interpolates between this key's value
  and the next key's value.
- **Cubic** — the segment uses a cubic Hermite spline defined by this
  key's [RightTangent](/docs/reference/engine/datatypes/ValueCurveKey.md) and the next
  key's [LeftTangent](/docs/reference/engine/datatypes/ValueCurveKey.md).

Not all value types support Linear or Cubic interpolation. Non-numerical
types such as strings, booleans, and enums revert to Constant
interpolation regardless of this setting.

Changing this property to a non-cubic mode automatically clears the
[RightTangent](/docs/reference/engine/datatypes/ValueCurveKey.md) of this key, because
only cubic segments use a right tangent.

### ValueCurveKey.Time

**Type:** `number`

The time position of this [ValueCurveKey](/docs/reference/engine/datatypes/ValueCurveKey.md) along the curve.
Defaults to `0`. Keys within a [ValueCurve](/docs/reference/engine/classes/ValueCurve.md) are stored sorted by
their time values; the time determines where in the animation timeline
this key's value applies.

### ValueCurveKey.Value

**Type:** `any`

The value stored in this [ValueCurveKey](/docs/reference/engine/datatypes/ValueCurveKey.md). Defaults to `nil`. Can
hold any supported Luau type, including numbers, booleans, strings,
[Vector2](/docs/reference/engine/datatypes/Vector2.md), [Vector3](/docs/reference/engine/datatypes/Vector3.md), [CFrame](/docs/reference/engine/datatypes/CFrame.md),
[UDim](/docs/reference/engine/datatypes/UDim.md), [UDim2](/docs/reference/engine/datatypes/UDim2.md), [NumberRange](/docs/reference/engine/datatypes/NumberRange.md),
[NumberSequence](/docs/reference/engine/datatypes/NumberSequence.md), [ColorSequence](/docs/reference/engine/datatypes/ColorSequence.md), and enums. All keys
on a single [ValueCurve](/docs/reference/engine/classes/ValueCurve.md) must hold values of the same type;
attempting to insert a key whose value type differs from existing keys
produces an error.

### ValueCurveKey.RightTangent

**Type:** `number`

The outgoing tangent (slope) at this key, used when the
[Interpolation](/docs/reference/engine/datatypes/ValueCurveKey.md) is
[KeyInterpolationMode.Cubic](/docs/reference/engine/enums/KeyInterpolationMode.md). Defaults to `nil` (unset); when unset,
an effective tangent of `0` is used during curve evaluation. Attempting to
set this property on a key whose interpolation mode is not Cubic throws a
runtime error. This property is automatically cleared when
[Interpolation](/docs/reference/engine/datatypes/ValueCurveKey.md) is changed to a
non-cubic mode.

### ValueCurveKey.LeftTangent

**Type:** `number`

The incoming tangent (slope) at this key, used when the preceding segment
uses [KeyInterpolationMode.Cubic](/docs/reference/engine/enums/KeyInterpolationMode.md) interpolation. Defaults to `nil`
(unset); when unset, an effective tangent of `0` is used during curve
evaluation. Unlike [RightTangent](/docs/reference/engine/datatypes/ValueCurveKey.md),
this property can be set on any key regardless of its own interpolation
mode, because it defines the slope at the endpoint of the preceding cubic
segment.