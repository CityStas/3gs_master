---
name: bit32
last_updated: 2026-10-30T19:55:54Z
type: library
summary: "A library of functions to perform bitwise operations."
---

# bit32

A library of functions to perform bitwise operations.

**Type:** library

## Description

This library provides functions to perform bitwise operations.

#### Number Limitations

This library treats numbers as unsigned 32-bit integers; numbers will be
converted to this before being used (see image below). Numbers with decimal
numbers are rounded to the nearest whole number.

![32-bit integer conversion (in hexadecimal)](../../../assets/engine-api/libraries/bit32/32-Bit-Restriction.png)

## Functions

### bit32.arshift

**Signature:** `bit32.arshift(x: number, disp: number): number`

Returns the number `x` shifted `disp` bits to the right. The number `disp`
may be any representable integer. Negative displacements shift to the
left.

This shift operation is what is called arithmetic shift. Vacant bits on
the left are filled with copies of the higher bit of `x`; vacant bits on
the right are filled with zeros. In particular, displacements with
absolute values higher than 31 result in zero or 0xFFFFFFFF (all original
bits are shifted out).

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `x` | `number` |  | The number whose bits shall be shifted. |
| `disp` | `number` |  | The integer number of bits to shift by. |

**Returns:** `number` — The result of arithmetically shifting `x` by `disp` bits to the right.

### bit32.band

**Signature:** `bit32.band(numbers: Tuple): number`

Returns the bitwise AND of all provided numbers.

Each bit is tested against the following truth table:

| A | B | Output |
| --- | --- | --- |
| 0 | 0 | 0 |
| 1 | 0 | 0 |
| 0 | 1 | 0 |
| 1 | 1 | 1 |

![Bitwise AND of 3 numbers](../../../assets/engine-api/libraries/bit32/AND.png)

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `numbers` | `Tuple` |  | The numbers to combine with bitwise AND. |

**Returns:** `number` — The bitwise AND of all provided numbers.

### bit32.bnot

**Signature:** `bit32.bnot(x: number): number`

Returns the bitwise negation of `x`.

![Negation of a provided number](../../../assets/engine-api/libraries/bit32/NOT.png)

For any integer `x`, the following identity holds:

```lua
local x = 0xF0
assert(bit32.bnot(x) == (-1 - x) % 2^32)
```

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `x` | `number` |  | The number to negate. |

**Returns:** `number` — The bitwise negation of `x`.

### bit32.bor

**Signature:** `bit32.bor(numbers: Tuple): number`

Returns the bitwise OR of all provided numbers.

Each bit is tested against the following truth table:

| A | B | Output |
| --- | --- | --- |
| 0 | 0 | 0 |
| 1 | 0 | 1 |
| 0 | 1 | 1 |
| 1 | 1 | 1 |

![Bitwise OR of 3 numbers](../../../assets/engine-api/libraries/bit32/OR.png)

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `numbers` | `Tuple` |  | The numbers to combine with bitwise OR. |

**Returns:** `number` — The bitwise OR of all provided numbers.

### bit32.btest

**Signature:** `bit32.btest(numbers: Tuple): bool`

Returns `true` if the bitwise AND of all its operands is different from
zero, `false` otherwise. This is functionally equivalent to
`bit32.band(...) ~= 0` but returns a boolean directly without the
intermediate number.

This function is useful for testing whether one or more specific bits are
set in a value. For example, you can check whether a particular flag is
active in a bitmask:

```lua
local flags = 0x5 -- bits 0 and 2 are set
print(bit32.btest(flags, 1)) --> true (bit 0 is set)
print(bit32.btest(flags, 2)) --> false (bit 1 is not set)
print(bit32.btest(flags, 4)) --> true (bit 2 is set)
```

When called with more than two arguments, all values are ANDed together
before the zero-test:

```lua
print(bit32.btest(0xFF, 0x0F, 0x03)) --> true (0xFF & 0x0F & 0x03 == 0x03)
```

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `numbers` | `Tuple` |  | The numbers to test with bitwise AND. |

**Returns:** `bool` — True if the bitwise AND of all operands is non-zero, false otherwise.

### bit32.bxor

**Signature:** `bit32.bxor(numbers: Tuple): number`

Returns the bitwise XOR of all provided numbers.

Each bit is tested against the following truth table:

| A | B | Output |
| --- | --- | --- |
| 0 | 0 | 0 |
| 1 | 0 | 1 |
| 0 | 1 | 1 |
| 1 | 1 | 0 |

![Bitwise XOR of 3 numbers](../../../assets/engine-api/libraries/bit32/XOR.png)

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `numbers` | `Tuple` |  | The numbers to combine with bitwise XOR. |

**Returns:** `number` — The bitwise XOR of all provided numbers.

### bit32.byteswap

**Signature:** `bit32.byteswap(x: number): number`

Reverses the byte order of the 32-bit unsigned integer representation of
`x`. The four bytes are rearranged so that the most-significant byte
becomes the least-significant byte and vice versa, converting between
big-endian and little-endian representations.

```lua
print(bit32.byteswap(0xAABBCCDD)) --> 0xDDCCBBAA
print(bit32.byteswap(0x00000001)) --> 0x01000000
```

This is useful when reading or writing binary data that uses a different
byte order (endianness) than expected, such as network protocols or file
formats that store multi-byte integers in big-endian order.

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `x` | `number` |  | The number whose bytes to swap. |

**Returns:** `number` — The number with its byte order reversed.

### bit32.countlz

**Signature:** `bit32.countlz(n: number): number`

Returns the number of consecutive zero bits in the 32-bit representation
of the provided number starting from the left-most (most significant) bit.
Returns 32 if the provided number is zero.

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `n` | `number` |  | The number to count leading zeros in. |

**Returns:** `number` — The count of consecutive zero bits from the most significant bit, or
32 if `n` is zero.

### bit32.countrz

**Signature:** `bit32.countrz(n: number): number`

Returns the number of consecutive zero bits in the 32-bit representation
of the provided number starting from the right-most (least significant)
bit. Returns 32 if the provided number is zero.

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `n` | `number` |  | The number to count trailing zeros in. |

**Returns:** `number` — The count of consecutive zero bits from the least significant bit, or
32 if `n` is zero.

### bit32.extract

**Signature:** `bit32.extract(n: number, field: number, width?: number): number`

Returns the unsigned number formed by the bits `field` to
`field + width - 1` from `n`. Bits are numbered from 0 (least significant)
to 31 (most significant). The default for `width` is 1.

For any valid `field` and `width`, this operation is equivalent to
`bit32.band(bit32.rshift(n, field), 2^width - 1)`. `field` must be in the
range `[0, 31]`, and `width` must be in the range `[1, 32 - field]`.
Values outside those ranges raise an error.

```lua
local n = 0x12345678
assert(bit32.extract(n, 0, 8) == 0x78) -- bits 0 through 7
assert(bit32.extract(n, 4, 8) == 0x67) -- bits 4 through 11
assert(bit32.extract(n, 16, 8) == 0x34) -- bits 16 through 23
assert(bit32.extract(n, 24, 8) == 0x12) -- bits 24 through 31
```

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `n` | `number` |  | The number to extract bits from. |
| `field` | `number` |  | The zero-based position of the least significant bit to extract. |
| `width` | `number` | `1` | The number of bits to extract. |

**Returns:** `number` — The unsigned number formed by the extracted bit range.

### bit32.replace

**Signature:** `bit32.replace(n: number, v: number, field: number, width?: number): number`

Returns a copy of `n` with the bits `field` to `field + width - 1`
replaced by the value `v`. See [bit32.extract()](/docs/reference/engine/globals/bit32.md) for details about
`field` and `width`.

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `n` | `number` |  | The number in which to replace bits. |
| `v` | `number` |  | The replacement value to insert into the bit range. |
| `field` | `number` |  | The zero-based position of the least significant bit to replace. |
| `width` | `number` | `1` | The number of bits to replace. |

**Returns:** `number` — A copy of `n` with the specified bit range replaced by `v`.

### bit32.lrotate

**Signature:** `bit32.lrotate(x: number, disp: number): number`

Returns the number `x` rotated `disp` bits to the left. The number `disp`
may be any representable integer. For any valid displacement, the
following identity holds:

```lua
local x, disp = 0xF0, 35
assert(bit32.lrotate(x, disp) == bit32.lrotate(x, disp % 32))
```

In particular, negative displacements rotate to the right.

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `x` | `number` |  | The number whose bits to rotate. |
| `disp` | `number` |  | The number of bit positions to rotate left. |

**Returns:** `number` — The result of rotating `x` left by `disp` bits.

### bit32.lshift

**Signature:** `bit32.lshift(x: number, disp: number): number`

Returns the number `x` shifted `disp` bits to the left. The number `disp`
may be any representable integer. Negative displacements shift to the
right. In any direction, vacant bits are filled with zeros. In particular,
displacements with absolute values higher than 31 result in zero (all bits
are shifted out).

![Number shifted 3 to the left](../../../assets/engine-api/libraries/bit32/LSHIFT.png)

For positive displacements, the following equality holds:

```lua
local b, disp = 0xF0, 3
assert(bit32.lshift(b, disp) == (b * 2^disp) % 2^32)
```

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `x` | `number` |  | The number whose bits to shift. |
| `disp` | `number` |  | The number of bit positions to shift left. |

**Returns:** `number` — The result of logically shifting `x` left by `disp` bits.

### bit32.rrotate

**Signature:** `bit32.rrotate(x: number, disp: number): number`

Returns the number `x` rotated `disp` bits to the right. The number `disp`
may be any representable integer.

For any valid displacement, the following identity holds:

```lua
local x, disp = 0xF0, 35
assert(bit32.rrotate(x, disp) == bit32.rrotate(x , disp % 32))
```

In particular, negative displacements rotate to the left.

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `x` | `number` |  | The number whose bits to rotate. |
| `disp` | `number` |  | The number of bit positions to rotate right. |

**Returns:** `number` — The result of rotating `x` right by `disp` bits.

### bit32.rshift

**Signature:** `bit32.rshift(x: number, disp: number): number`

Returns the number `x` shifted `disp` bits to the right. The number `disp`
may be any representable integer. Negative displacements shift to the
left. In any direction, vacant bits are filled with zeros. In particular,
displacements with absolute values higher than 31 result in zero (all bits
are shifted out).

![Number shifted 3 to the right](../../../assets/engine-api/libraries/bit32/RSHIFT.png)

For positive displacements, the following equality holds:

```lua
local b, disp = 0xF00, 3
assert(bit32.rshift(b, disp) == (b % 2^32 / 2^disp) // 1)
```

This shift operation is what is called logical shift.

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `x` | `number` |  | The number whose bits to shift. |
| `disp` | `number` |  | The number of bit positions to shift right. |

**Returns:** `number` — The result of logically shifting `x` right by `disp` bits.