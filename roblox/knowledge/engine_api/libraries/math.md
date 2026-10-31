---
name: math
last_updated: 2026-10-30T19:55:54Z
type: library
summary: "A library of math functions."
---

# math

A library of math functions.

**Type:** library

## Description

This library is an interface to the standard C math library, providing all of
its functions inside the [math](/docs/reference/engine/globals/math.md) table.

## Properties

### math.e

**Type:** `number`

The value of Euler's number, e.

### math.huge

**Type:** `number`

Returns a value larger than or equal to any other numerical value (about
2<sup>1024</sup>). Dividing a positive number by zero yields this same
value.

### math.nan

**Type:** `number`

A NaN value, as defined by the IEEE 754 standard. Comparing directly to
`math.nan` will always return false; use [math.isnan()](/docs/reference/engine/globals/math.md) instead.

### math.phi

**Type:** `number`

The value of the golden ratio.

### math.pi

**Type:** `number`

The value of pi.

### math.sqrt2

**Type:** `number`

The value of the square root of 2.

### math.tau

**Type:** `number`

The value of tau, which is defined as `2 * math.pi`.

## Functions

### math.abs

**Signature:** `math.abs(x: number): number`

Returns the absolute value of `x`.

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `x` | `number` |  | The number to return the absolute value of. |

**Returns:** `number` — The absolute value of `x`.

### math.acos

**Signature:** `math.acos(x: number): number`

Returns the arc cosine of `x`.

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `x` | `number` |  | The cosine value, between `-1` and `1`. |

**Returns:** `number` — The angle in radians whose cosine is `x`, in the range `[0, pi]`.

### math.asin

**Signature:** `math.asin(x: number): number`

Returns the arc sine of `x`.

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `x` | `number` |  | The sine value, between `-1` and `1`. |

**Returns:** `number` — The angle in radians whose sine is `x`, in the range `[-pi/2, pi/2]`.

### math.atan

**Signature:** `math.atan(x: number): number`

Returns the arc tangent of `x` in radians.

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `x` | `number` |  | The value to compute the arc tangent of. |

**Returns:** `number` — The arc tangent of `x` in radians, in the range `[-pi/2, pi/2]`.

### math.atan2

**Signature:** `math.atan2(y: number, x: number): number`

Returns the arc tangent of `y`/`x` (in radians) while using the signs of
both parameters to find the quadrant of the result. It also handles
correctly the case of `x` being zero.

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `y` | `number` |  | The **Y** coordinate. |
| `x` | `number` |  | The **X** coordinate. |

**Returns:** `number` — The arc tangent of `y`/`x` in radians, in the range `[-pi, pi]`.

### math.ceil

**Signature:** `math.ceil(x: number): int`

Returns the smallest integer larger than or equal to `x`.

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `x` | `number` |  | The number to round up. |

**Returns:** `int` — The smallest integer greater than or equal to `x`.

### math.clamp

**Signature:** `math.clamp(x: number, min: number, max: number): number`

Returns a number between `min` and `max`, inclusive.

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `x` | `number` |  | The number to clamp. |
| `min` | `number` |  | The minimum value of the range. |
| `max` | `number` |  | The maximum value of the range; must be greater than or equal to `min`. |

**Returns:** `number` — `x` constrained to the range `[`min`, `max`]`.

### math.cos

**Signature:** `math.cos(x: number): number`

Returns the cosine of `x`, assumed to be in radians.

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `x` | `number` |  | The angle in radians. |

**Returns:** `number` — The cosine of `x`.

### math.cosh

**Signature:** `math.cosh(x: number): number`

Returns the hyperbolic cosine of `x`.

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `x` | `number` |  | The number to compute the hyperbolic cosine of. |

**Returns:** `number` — The hyperbolic cosine of `x`.

### math.deg

**Signature:** `math.deg(x: number): number`

Returns the angle `x` (given in radians) in degrees.

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `x` | `number` |  | The angle in radians to convert. |

**Returns:** `number` — The angle `x` converted to degrees.

### math.exp

**Signature:** `math.exp(x: number): number`

Returns the value `e`^`x`.

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `x` | `number` |  | The exponent. |

**Returns:** `number` — The value of `e` raised to the power `x`.

### math.floor

**Signature:** `math.floor(x: number): int`

Returns the largest integer smaller than or equal to `x`.

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `x` | `number` |  | The number to round down. |

**Returns:** `int` — The largest integer less than or equal to `x`.

### math.fmod

**Signature:** `math.fmod(x: number, y: number): number`

Returns the remainder of the division of `x` by `y` that rounds the
quotient towards zero.

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `x` | `number` |  | The dividend. |
| `y` | `number` |  | The divisor. |

**Returns:** `number` — The remainder of the division of `x` by `y`.

### math.frexp

**Signature:** `math.frexp(x: number): number, int`

Returns `m` and `e` such that `x` = `m`\*`2`^`e`. `e` is an integer and
the absolute value of `m` is in the range of `0.5` to `1` (inclusive of
`0.5` but exclusive of `1`), or zero when `x` is zero.

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `x` | `number` |  | The number to decompose into mantissa and exponent. |

**Returns:** `number`, `int` — The mantissa `m`, a value whose absolute value is in `[0.5, 1)` or
zero. The exponent `e` such that `x = m * 2^e`.

### math.isfinite

**Signature:** `math.isfinite(x: number): boolean`

Returns true if `x` is a finite number, meaning it is neither NaN nor
positive or negative infinity (±[math.huge](/docs/reference/engine/globals/math.md)).

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `x` | `number` |  | The number to test. |

**Returns:** `boolean` — True if `x` is neither NaN nor infinity, false otherwise.

### math.isinf

**Signature:** `math.isinf(x: number): boolean`

Returns true if `x` is positive or negative infinity
(±[math.huge](/docs/reference/engine/globals/math.md)) and false otherwise.

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `x` | `number` |  | The number to test. |

**Returns:** `boolean` — True if `x` is positive or negative infinity, false otherwise.

### math.isnan

**Signature:** `math.isnan(x: number): boolean`

Returns true if `x` is not a number (NaN) and false otherwise.

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `x` | `number` |  | The number to test. |

**Returns:** `boolean` — True if `x` is NaN, false otherwise.

### math.ldexp

**Signature:** `math.ldexp(x: number, e: int): number`

Returns `x`\*`2`^`e` (`e` should be an integer).

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `x` | `number` |  | The mantissa value. |
| `e` | `int` |  | The integer exponent. |

**Returns:** `number` — The value `x * 2^e`.

### math.lerp

**Signature:** `math.lerp(a: number, b: number, t: number): number`

Returns the linear interpolation between `a` and `b` based on the factor
`t`.

This function uses the formula `a`+`(b-a)`\*`t`. `t` is typically between
`0` and `1` but values outside this range are acceptable.

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `a` | `number` |  | The starting value. |
| `b` | `number` |  | The ending value. |
| `t` | `number` |  | The interpolation factor, typically between `0` and `1`. |

**Returns:** `number` — The interpolated value between `a` and `b`.

### math.log

**Signature:** `math.log(x: number, base?: number): number`

Returns the logarithm of `x` using the given base, or the mathematical
constant `e` if no base is provided (natural logarithm).

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `x` | `number` |  | The number to compute the logarithm of. |
| `base` | `number` | `2.7182818` | The base of the logarithm, the constant `e` by default. |

**Returns:** `number` — The logarithm of `x` in the given base.

### math.log10

**Signature:** `math.log10(x: number): number`

Returns the base-10 logarithm of `x`.

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `x` | `number` |  | The number to compute the base-10 logarithm of. |

**Returns:** `number` — The base-10 logarithm of `x`.

### math.map

**Signature:** `math.map(x: number, inmin: number, inmax: number, outmin: number, outmax: number): number`

Returns a value that represents `x` mapped linearly from the input range
(`inmin` to `inmax`) to the output range (`outmin` to `outmax`). This is
achieved by determining the relative position of `x` within the input
range and applying that ratio to the output range.

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `x` | `number` |  | The number to be mapped. |
| `inmin` | `number` |  | The lower bound of the input range. |
| `inmax` | `number` |  | The upper bound of the input range. |
| `outmin` | `number` |  | The lower bound of the output range. |
| `outmax` | `number` |  | The upper bound of the output range. |

**Returns:** `number` — The value of `x` mapped to the output range.

### math.max

**Signature:** `math.max(x: number, ...: number): number`

Returns the maximum value among the numbers passed to the function.

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `x` | `number` |  | The first number to compare. |
| `...` | `number` |  | Additional numbers to compare. |

**Returns:** `number` — The largest value among all arguments.

### math.min

**Signature:** `math.min(x: number, ...: number): number`

Returns the minimum value among the numbers passed to the function.

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `x` | `number` |  | The first number to compare. |
| `...` | `number` |  | Additional numbers to compare. |

**Returns:** `number` — The smallest value among all arguments.

### math.modf

**Signature:** `math.modf(x: number): number, number`

Returns two numbers: the integral part of `x` and the fractional part of
`x`.

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `x` | `number` |  | The number to split into integral and fractional parts. |

**Returns:** `number`, `number` — The integral part of `x`. The fractional part of `x`.

### math.noise

**Signature:** `math.noise(x: number, y?: number, z?: number): number`

Returns a Perlin noise value. The returned value is most often between the
range of `-1` to `1` (inclusive) but sometimes may be outside that range;
if the interval is critical to you, use [math.clamp(noise, -1, 1)](/docs/reference/engine/globals/math.md)
on the output.

If you leave arguments out, they will be interpreted as zero, so
[math.noise(1.158)](/docs/reference/engine/globals/math.md) is equivalent to
[math.noise(1.158, 0, 0)](/docs/reference/engine/globals/math.md) and [math.noise(1.158, 5.723)](/docs/reference/engine/globals/math.md)
is equivalent to [math.noise(1.158, 5.723, 0)](/docs/reference/engine/globals/math.md).

Note that this function uses a Perlin noise algorithm to assign fixed
values to coordinates. For example, [math.noise(1.158, 5.723)](/docs/reference/engine/globals/math.md)
will always return `0.48397532105446` and [math.noise(1.158, 6)](/docs/reference/engine/globals/math.md)
will always return `0.15315161645412`.

If `x`, `y`, and `z` are all integers, the return value will be `0`. For
fractional values of `x`, `y`, and `z`, the return value will gradually
fluctuate between `-0.5` and `0.5`. For coordinates that are close to each
other, the return values will also be close to each other.

The noise repeats with a period of `256` on each axis, so
[math.noise(x, y, z)](/docs/reference/engine/globals/math.md) and [math.noise(x + 256, y, z)](/docs/reference/engine/globals/math.md)
return identical values.

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `x` | `number` |  | The **X** coordinate of the sample point. |
| `y` | `number` | `0` | The **Y** coordinate of the sample point. |
| `z` | `number` | `0` | The **Z** coordinate of the sample point. |

**Returns:** `number` — A Perlin noise value, typically between `-1` and `1`.

### math.pow

**Signature:** `math.pow(x: number, y: number): number`

Returns `x`^`y` (you can also use the expression `x`^`y` to compute this
value).

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `x` | `number` |  | The base value. |
| `y` | `number` |  | The exponent value. |

**Returns:** `number` — The value `x` raised to the power `y`.

### math.rad

**Signature:** `math.rad(x: number): number`

Returns the angle `x` (given in degrees) in radians.

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `x` | `number` |  | The angle in degrees to convert. |

**Returns:** `number` — The angle `x` converted to radians.

### math.random

**Signature:** `math.random(m?: number, n?: number): number`

When called without arguments, returns a uniform pseudo-random real number
in the range of `0` to `1` (inclusive of `0` but exclusive of `1`).

When called with an integer number `m`, returns a uniform pseudo-random
integer in the range of `1` to `m`, inclusive.

When called with two integer numbers `m` and `n`, returns a uniform
pseudo-random integer in the range of `m` to `n`, inclusive.

Internally, this uses a 32-bit PCG (Permuted Congruential Generator) which
achieves excellent statistical performance and makes its output hard to
predict.

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `m` | `number` | `0` | When used alone, the upper bound of the integer range (lower bound is `1`). When used with `n`, the lower bound. |
| `n` | `number` | `1` | The upper bound of the integer range. |

**Returns:** `number` — A pseudo-random number within the specified range.

### math.randomseed

**Signature:** `math.randomseed(x: number): ()`

Sets `x` as the seed for the pseudo-random generator: equal seeds produce
equal sequences of numbers.

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `x` | `number` |  | The seed value for the pseudo-random number generator. |

**Returns:** `()`

### math.round

**Signature:** `math.round(x: number): number`

Returns the integer with the smallest difference between it and the given
number. For example, the value `5.8` returns `6`.

For values like `0.5` that are equidistant to two integers, the value with
the greater difference between it and zero is chosen. In other words, the
function "rounds away from zero" such that `0.5` rounds to `1` and `-0.5`
rounds to `-1`.

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `x` | `number` |  | The value to be rounded. |

**Returns:** `number` — The nearest integer to `x`, rounding away from zero for midpoints.

### math.sign

**Signature:** `math.sign(x: number): int`

Returns `-1` if `x` is less than `0`, `0` if `x` equals `0`, or `1` if `x`
is greater than `0`.

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `x` | `number` |  | The number to determine the sign of. |

**Returns:** `int` — `-1` if `x` is negative, `0` if `x` is zero, or `1` if `x` is
positive.

### math.sin

**Signature:** `math.sin(x: number): number`

Returns the sine of `x`, assumed to be in radians.

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `x` | `number` |  | The angle in radians. |

**Returns:** `number` — The sine of `x`.

### math.sinh

**Signature:** `math.sinh(x: number): number`

Returns the hyperbolic sine of `x`.

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `x` | `number` |  | The number to compute the hyperbolic sine of. |

**Returns:** `number` — The hyperbolic sine of `x`.

### math.sqrt

**Signature:** `math.sqrt(x: number): number`

Returns the square root of `x`. You can also use the expression `x`^`0.5`
to compute this value.

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `x` | `number` |  | The number to compute the square root of. |

**Returns:** `number` — The square root of `x`.

### math.tan

**Signature:** `math.tan(x: number): number`

Returns the tangent of `x`, assumed to be in radians.

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `x` | `number` |  | The angle in radians. |

**Returns:** `number` — The tangent of `x`.

### math.tanh

**Signature:** `math.tanh(x: number): number`

Returns the hyperbolic tangent of `x`.

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `x` | `number` |  | The number to compute the hyperbolic tangent of. |

**Returns:** `number` — The hyperbolic tangent of `x`.