---
name: NumberRange
last_updated: 2026-10-30T19:55:54Z
type: datatype
summary: "Represents a range of numbers."
---

# NumberRange

Represents a range of numbers.

**Type:** datatype

## Description

The [NumberRange](/docs/reference/engine/datatypes/NumberRange.md) represents a range of numbers.

`NumberRange` stores its [NumberRange.Min](/docs/reference/engine/datatypes/NumberRange.md) and
[NumberRange.Max](/docs/reference/engine/datatypes/NumberRange.md) values as 32-bit floating-point numbers. Very large
numbers or numbers requiring high decimal precision may lose accuracy.

## Constructors

### NumberRange.new

**Signature:** `NumberRange.new(value: number)`

Returns a new [NumberRange](/docs/reference/engine/datatypes/NumberRange.md) with the minimum and maximum set to
the `value`.

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `value` | `number` |  | The number that both the minimum and maximum of the range are set to. |

### NumberRange.new

**Signature:** `NumberRange.new(minimum: number, maximum: number)`

Returns a new [NumberRange](/docs/reference/engine/datatypes/NumberRange.md) with the provided `minimum` and
`maximum`. The `minimum` must be less than or equal to `maximum`.

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `minimum` | `number` |  | The lower bound of the range. |
| `maximum` | `number` |  | The upper bound of the range. |

## Properties

### NumberRange.Min

**Type:** `number`

The minimum value of the [NumberRange](/docs/reference/engine/datatypes/NumberRange.md), always less than or equal
to the maximum.

### NumberRange.Max

**Type:** `number`

The maximum value of the [NumberRange](/docs/reference/engine/datatypes/NumberRange.md), always greater than or
equal to the minimum.