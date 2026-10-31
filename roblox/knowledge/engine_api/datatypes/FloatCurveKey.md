---
name: FloatCurveKey
last_updated: 2026-10-30T19:55:54Z
type: datatype
summary: "A time-value pair used with FloatCurve instances."
---

# FloatCurveKey

A time-value pair used with [FloatCurve](/docs/reference/engine/classes/FloatCurve.md) instances.

**Type:** datatype

## Description

A time-value pair used with [FloatCurve](/docs/reference/engine/classes/FloatCurve.md) instances.

The [Interpolation](/docs/reference/engine/datatypes/FloatCurveKey.md) property dictates the
interpolation mode for the segment started by this key and ended by the next
key on the curve. Each segment may use a different interpolation mode.

The [LeftTangent](/docs/reference/engine/datatypes/FloatCurveKey.md) and
[RightTangent](/docs/reference/engine/datatypes/FloatCurveKey.md) properties apply to the
cubic interpolation mode and define the desired tangent (slope) at the key.
Different left and right values can be used to encode discontinuities in slope
at the key. Attempting to set a
[RightTangent](/docs/reference/engine/datatypes/FloatCurveKey.md) value on a key that doesn't
use the cubic interpolation mode will result in a runtime error. It is
possible to set the [LeftTangent](/docs/reference/engine/datatypes/FloatCurveKey.md) property
on any key, as it will be used should the preceding segment use cubic
interpolation.

## Constructors

### FloatCurveKey.new

**Signature:** `FloatCurveKey.new(time: number, value: number, Interpolation: KeyInterpolationMode)`

Creates a new [FloatCurveKey](/docs/reference/engine/datatypes/FloatCurveKey.md) at a given time and value.
[LeftTangent](/docs/reference/engine/datatypes/FloatCurveKey.md) and
[RightTangent](/docs/reference/engine/datatypes/FloatCurveKey.md) are left uninitialized
and, if not initialized, tangent values of 0 will be used when evaluating
the curve.

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `time` | `number` |  | Time at which to create the new [FloatCurveKey](/docs/reference/engine/datatypes/FloatCurveKey.md). |
| `value` | `number` |  | Value of the new [FloatCurveKey](/docs/reference/engine/datatypes/FloatCurveKey.md). |
| `Interpolation` | `KeyInterpolationMode` |  | The interpolation mode for the curve segment starting at this key. Defaults to [Cubic](/docs/reference/engine/enums/KeyInterpolationMode.md) when omitted. |

## Properties

### FloatCurveKey.Interpolation

**Type:** `KeyInterpolationMode`

Specifies the interpolation mode used for the curve segment that begins at
this key and ends at the next key on the [FloatCurve](/docs/reference/engine/classes/FloatCurve.md). Each segment
of the curve can use a different interpolation mode. The default value is
[KeyInterpolationMode.Cubic](/docs/reference/engine/enums/KeyInterpolationMode.md).

The available modes are:

- **Constant** — the segment holds the value of this key until the next
  key.
- **Linear** — the segment linearly interpolates between this key's value
  and the next key's value.
- **Cubic** — the segment uses a cubic Hermite spline defined by this
  key's [RightTangent](/docs/reference/engine/datatypes/FloatCurveKey.md) and the next
  key's [LeftTangent](/docs/reference/engine/datatypes/FloatCurveKey.md).

Changing this property to a non-cubic mode automatically clears the
[RightTangent](/docs/reference/engine/datatypes/FloatCurveKey.md) of this key, because
only cubic segments use a right tangent.

### FloatCurveKey.Time

**Type:** `number`

The time position of this [FloatCurveKey](/docs/reference/engine/datatypes/FloatCurveKey.md) along the curve's
timeline. The default value is `0`. Keys within a [FloatCurve](/docs/reference/engine/classes/FloatCurve.md) are
kept sorted in ascending time order; if you insert a key at a time that
already exists on the curve, the existing key at that time is replaced.

### FloatCurveKey.Value

**Type:** `number`

The numerical output value at this key's position on the curve. The
default value is `0`. When a [FloatCurve](/docs/reference/engine/classes/FloatCurve.md) is sampled at this key's
[Time](/docs/reference/engine/datatypes/FloatCurveKey.md), the curve evaluates to this value
(subject to any interpolation with neighboring keys depending on the
sampling time).

### FloatCurveKey.RightTangent

**Type:** `number`

The slope of the curve leaving this key toward the next key. The default
value is `nil`, which means the tangent is automatically computed (an
effective value of `0` is used during evaluation). This property can only
be set when [Interpolation](/docs/reference/engine/datatypes/FloatCurveKey.md) is
[KeyInterpolationMode.Cubic](/docs/reference/engine/enums/KeyInterpolationMode.md); attempting to set it on a key with
Constant or Linear interpolation raises a runtime error. Pairing a
different RightTangent value on this key with a different
[LeftTangent](/docs/reference/engine/datatypes/FloatCurveKey.md) value on the next key
creates a discontinuity in slope (a "corner") at the next key.

### FloatCurveKey.LeftTangent

**Type:** `number`

The slope of the curve arriving at this key from the previous key. The
default value is `nil`, which means the tangent is automatically computed
(an effective value of `0` is used during evaluation). Unlike
[RightTangent](/docs/reference/engine/datatypes/FloatCurveKey.md), this property can be
set on a key with any interpolation mode, because the preceding segment
may itself use cubic interpolation and therefore needs a defined left
tangent at this endpoint.