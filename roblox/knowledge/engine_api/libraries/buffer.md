---
name: buffer
last_updated: 2026-10-30T19:55:54Z
type: library
summary: "A library of buffer functions."
---

# buffer

A library of buffer functions.

**Type:** library

## Description

A buffer is an object that represents a fixed-size mutable block of memory.
The buffer library provides functions for creation and manipulation of buffer
objects, providing all its functions inside the global [buffer](/docs/reference/engine/globals/buffer.md)
variable.

Buffer is intended to be used a low-level binary data storage structure,
replacing the uses of [string.pack()](/docs/reference/engine/globals/string.md) and [string.unpack()](/docs/reference/engine/globals/string.md).
Use cases include reading and writing existing binary formats, working with
data in a more compact form, serialization to custom binary formats, and
general work with native memory types like fixed-length integers and floats.

When passed through Roblox APIs, including sending a buffer through custom
events, the identity of the buffer object is not preserved and the target will
receive a copy. Similar to other limitations, the same buffer object cannot be
used from multiple [Actor](/docs/reference/engine/classes/Actor.md) scripts (Parallel Luau).

Many of the functions accept an offset in bytes from the start of the buffer.
Offset of `0` from the start of the buffer memory block accesses the first
byte. All offsets, counts and sizes should be non-negative integer numbers. If
the bytes that are accessed by any read or write operation are outside the
buffer memory, an error is thrown.

The `read` and `write` methods that work with integers and floats use
[little-endian](https://en.wikipedia.org/wiki/Endianness) encoding.

## Functions

### buffer.create

**Signature:** `buffer.create(size: number): buffer`

Creates a buffer of the requested size with all bytes initialized to `0`.
Size limit is 1 GiB, or 1,073,741,824 bytes. Keep in mind that larger
buffers might fail to allocate if device is running low on memory.

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `size` | `number` |  | Size of the buffer in bytes. Must be a positive integer. |

**Returns:** `buffer`

### buffer.fromstring

**Signature:** `buffer.fromstring(str: string): buffer`

Creates a buffer initialized to the contents of the string. The size of
the buffer equals the length of the string.

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `str` | `string` |  | The string whose bytes initialize the new buffer. |

**Returns:** `buffer`

### buffer.tostring

**Signature:** `buffer.tostring(b: buffer): string`

Returns the buffer data as a string.

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `b` | `buffer` |  | The buffer to convert. |

**Returns:** `string`

### buffer.len

**Signature:** `buffer.len(b: buffer): number`

Returns the size of the buffer in bytes.

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `b` | `buffer` |  | The buffer to get the size of. |

**Returns:** `number`

### buffer.readbits

**Signature:** `buffer.readbits(b: buffer, bitOffset: number, bitCount: number): number`

Reads a range of bits into an unsigned integer from the buffer based on a
specific `bitCount` integer from `0` to `32`, inclusive. For example:

- `buffer.readbits(b, 0, 8)` is equivalent to
  [buffer.readu8(b, 0)](/docs/reference/engine/globals/buffer.md).
- `buffer.readbits(b, 0, 16)` is equivalent to
  [buffer.readu16(b, 0)](/docs/reference/engine/globals/buffer.md).
- `buffer.readbits(b, 0, 32)` is equivalent to
  [buffer.readu32(b, 0)](/docs/reference/engine/globals/buffer.md).
- `buffer.readbits(b, 0, 24)` reads 24 bits from the buffer.

Note that `0` bit width is supported only to not error in generalized
cases where bit count is dynamic, and reading 0 bits returns `0`. Also
note that, since the max size of the buffer is 1&nbsp;GB, `bitOffset`
cannot be handled as a 32‑bit integer number like byte offset in other
buffer functions.

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `b` | `buffer` |  | The buffer to read from. |
| `bitOffset` | `number` |  | Offset from the beginning of the buffer memory, starting from `0`. |
| `bitCount` | `number` |  | Integer bit count to read. Error is thrown if this value is not in range of `0` to `32`, inclusive. |

**Returns:** `number`

### buffer.readi8

**Signature:** `buffer.readi8(b: buffer, offset: number): number`

Reads the data from the buffer by reinterpreting bytes at the offset as an
8-bit signed integer and converting it into a number.

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `b` | `buffer` |  | The buffer to read from. |
| `offset` | `number` |  | Offset from the beginning of the buffer memory, starting from `0`. |

**Returns:** `number`

### buffer.readu8

**Signature:** `buffer.readu8(b: buffer, offset: number): number`

Reads the data from the buffer by reinterpreting bytes at the offset as an
8-bit unsigned integer and converting it into a number.

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `b` | `buffer` |  | The buffer to read from. |
| `offset` | `number` |  | Offset from the beginning of the buffer memory, starting from `0`. |

**Returns:** `number`

### buffer.readi16

**Signature:** `buffer.readi16(b: buffer, offset: number): number`

Reads the data from the buffer by reinterpreting bytes at the offset as a
16-bit signed integer and converting it into a number.

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `b` | `buffer` |  | The buffer to read from. |
| `offset` | `number` |  | Offset from the beginning of the buffer memory, starting from `0`. |

**Returns:** `number`

### buffer.readu16

**Signature:** `buffer.readu16(b: buffer, offset: number): number`

Reads the data from the buffer by reinterpreting bytes at the offset as a
16-bit unsigned integer and converting it into a number.

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `b` | `buffer` |  | The buffer to read from. |
| `offset` | `number` |  | Offset from the beginning of the buffer memory, starting from `0`. |

**Returns:** `number`

### buffer.readi32

**Signature:** `buffer.readi32(b: buffer, offset: number): number`

Reads the data from the buffer by reinterpreting bytes at the offset as a
32-bit signed integer and converting it into a number.

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `b` | `buffer` |  | The buffer to read from. |
| `offset` | `number` |  | Offset from the beginning of the buffer memory, starting from `0`. |

**Returns:** `number`

### buffer.readu32

**Signature:** `buffer.readu32(b: buffer, offset: number): number`

Reads the data from the buffer by reinterpreting bytes at the offset as a
32-bit unsigned integer and converting it into a number.

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `b` | `buffer` |  | The buffer to read from. |
| `offset` | `number` |  | Offset from the beginning of the buffer memory, starting from `0`. |

**Returns:** `number`

### buffer.readf32

**Signature:** `buffer.readf32(b: buffer, offset: number): number`

Reads the data from the buffer by reinterpreting bytes at the offset as a
32-bit floating-point value and converting it into a number. If the
floating-point value matches any bit patterns that represent `NaN` (not a
number), the returned value may be converted to a different quiet `NaN`
representation.

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `b` | `buffer` |  | The buffer to read from. |
| `offset` | `number` |  | Offset from the beginning of the buffer memory, starting from `0`. |

**Returns:** `number`

### buffer.readf64

**Signature:** `buffer.readf64(b: buffer, offset: number): number`

Reads the data from the buffer by reinterpreting bytes at the offset as a
64-bit floating-point value and converting it into a number. If the
floating-point value matches any bit patterns that represent `NaN` (not a
number), the returned value may be converted to a different quiet `NaN`
representation.

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `b` | `buffer` |  | The buffer to read from. |
| `offset` | `number` |  | Offset from the beginning of the buffer memory, starting from `0`. |

**Returns:** `number`

### buffer.writebits

**Signature:** `buffer.writebits(b: buffer, bitOffset: number, bitCount: number, value: number): ()`

Writes data to the buffer based on a specific `bitCount` integer from `0`
to `32`, inclusive. `value` is treated as an unsigned 32‑bit number and
only `bitCount` least significant bits are written.

Note that `0` bit width is supported only to not error in generalized
cases where bit count is dynamic, and writing 0 bits has no effect. Also
note that, since the max size of the buffer is 1&nbsp;GB, `bitOffset`
cannot be handled as a 32‑bit integer number like byte offset in other
buffer functions.

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `b` | `buffer` |  | The buffer to write to. |
| `bitOffset` | `number` |  | Offset from the beginning of the buffer memory, starting from `0`. |
| `bitCount` | `number` |  | Integer bit count to write. Error is thrown if this value is not in range of `0` to `32`, inclusive. |
| `value` | `number` |  | Unsigned 32‑bit number. Only `bitCount` least significant bits are written. |

**Returns:** `()`

### buffer.writei8

**Signature:** `buffer.writei8(b: buffer, offset: number, value: number): ()`

Writes data to the buffer by converting the number into an 8-bit signed
integer and writing a single byte.

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `b` | `buffer` |  | The buffer to write to. |
| `offset` | `number` |  | Offset from the beginning of the buffer memory, starting from `0`. |
| `value` | `number` |  | An integer number in range [-128, 127]. |

**Returns:** `()`

### buffer.writeu8

**Signature:** `buffer.writeu8(b: buffer, offset: number, value: number): ()`

Writes data to the buffer by converting the number into an 8-bit unsigned
integer and writing a single byte.

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `b` | `buffer` |  | The buffer to write to. |
| `offset` | `number` |  | Offset from the beginning of the buffer memory, starting from `0`. |
| `value` | `number` |  | An integer number in range [0, 255]. |

**Returns:** `()`

### buffer.writei16

**Signature:** `buffer.writei16(b: buffer, offset: number, value: number): ()`

Writes data to the buffer by converting the number into a 16-bit signed
integer and reinterpreting it as individual bytes.

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `b` | `buffer` |  | The buffer to write to. |
| `offset` | `number` |  | Offset from the beginning of the buffer memory, starting from `0`. |
| `value` | `number` |  | An integer number in range [-32,768, 32,767]. |

**Returns:** `()`

### buffer.writeu16

**Signature:** `buffer.writeu16(b: buffer, offset: number, value: number): ()`

Writes data to the buffer by converting the number into a 16-bit unsigned
integer and reinterpreting it as individual bytes.

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `b` | `buffer` |  | The buffer to write to. |
| `offset` | `number` |  | Offset from the beginning of the buffer memory, starting from `0`. |
| `value` | `number` |  | An integer number in range [0, 65,535]. |

**Returns:** `()`

### buffer.writei32

**Signature:** `buffer.writei32(b: buffer, offset: number, value: number): ()`

Writes data to the buffer by converting the number into a 32-bit signed
integer and reinterpreting it as individual bytes.

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `b` | `buffer` |  | The buffer to write to. |
| `offset` | `number` |  | Offset from the beginning of the buffer memory, starting from `0`. |
| `value` | `number` |  | An integer number in range [-2,147,483,648, 2,147,483,647]. |

**Returns:** `()`

### buffer.writeu32

**Signature:** `buffer.writeu32(b: buffer, offset: number, value: number): ()`

Writes data to the buffer by converting the number into a 32-bit unsigned
integer and reinterpreting it as individual bytes.

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `b` | `buffer` |  | The buffer to write to. |
| `offset` | `number` |  | Offset from the beginning of the buffer memory, starting from `0`. |
| `value` | `number` |  | An integer number in range [0, 4,294,967,295]. |

**Returns:** `()`

### buffer.writef32

**Signature:** `buffer.writef32(b: buffer, offset: number, value: number): ()`

Writes data to the buffer by converting the number into a 32-bit
floating-point value and reinterpreting it as individual bytes.

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `b` | `buffer` |  | The buffer to write to. |
| `offset` | `number` |  | Offset from the beginning of the buffer memory, starting from `0`. |
| `value` | `number` |  | A single-precision floating-point number. |

**Returns:** `()`

### buffer.writef64

**Signature:** `buffer.writef64(b: buffer, offset: number, value: number): ()`

Writes data to the buffer by converting the number into a 64-bit
floating-point value and reinterpreting it as individual bytes.

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `b` | `buffer` |  | The buffer to write to. |
| `offset` | `number` |  | Offset from the beginning of the buffer memory, starting from `0`. |
| `value` | `number` |  | A double-precision floating-point number. |

**Returns:** `()`

### buffer.readstring

**Signature:** `buffer.readstring(b: buffer, offset: number, count: number): string`

Reads a string of length `count` from the buffer at the specified
`offset`.

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `b` | `buffer` |  | The buffer to read from. |
| `offset` | `number` |  | Offset from the beginning of the buffer memory, starting from `0`. |
| `count` | `number` |  | Length to read. |

**Returns:** `string`

### buffer.writestring

**Signature:** `buffer.writestring(b: buffer, offset: number, value: string, count: number?): ()`

Writes data from a string into the buffer at the specified `offset`. If an
optional `count` is specified, only `count` bytes are taken from the
string.

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `b` | `buffer` |  | The buffer to write to. |
| `offset` | `number` |  | Offset from the beginning of the buffer memory, starting from `0`. |
| `value` | `string` |  | Data to write. |
| `count` | `number?` |  | Number of bytes to take from the string. This value cannot be larger than the string length. |

**Returns:** `()`

### buffer.copy

**Signature:** `buffer.copy(target: buffer, targetOffset: number, source: buffer, sourceOffset?: number?, count: number?): ()`

Copies `count` bytes from `source` starting at offset `sourceOffset` into
the `target` at `targetOffset`.

It's possible for `source` and `target` to be the same. Copying an
overlapping region inside the same buffer acts as if the source region is
copied into a temporary buffer and then that buffer is copied over to the
target.

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `target` | `buffer` |  | Buffer to copy data into. |
| `targetOffset` | `number` |  | Offset from the beginning of the buffer memory, starting from `0`. |
| `source` | `buffer` |  | Buffer to take the data from. |
| `sourceOffset` | `number?` | `0` | Offset from the beginning of the buffer memory, starting from `0`. |
| `count` | `number?` |  | Number of bytes to copy. If omitted, the whole `source` data starting from `sourceOffset` is taken. |

**Returns:** `()`

### buffer.fill

**Signature:** `buffer.fill(b: buffer, offset: number, value: number, count: number?): ()`

Sets `count` bytes in the buffer starting at the specified `offset` to
`value`.

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `b` | `buffer` |  | Buffer to write the data into. |
| `offset` | `number` |  | Offset from the beginning of the buffer memory, starting from `0`. |
| `value` | `number` |  | An integer number in range [0, 255]. |
| `count` | `number?` |  | Number of bytes to write. If omitted, all bytes after the specified offset are set. |

**Returns:** `()`