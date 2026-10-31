---
name: utf8
last_updated: 2026-10-30T19:55:54Z
type: library
summary: "This library provides basic support for `UTF-8` encoding."
---

# utf8

This library provides basic support for `UTF-8` encoding.

**Type:** library

## Description

This library provides basic support for `UTF-8` encoding. This library does
not provide any support for Unicode other than the handling of the encoding.
Any operation that needs the meaning of a character, such as character
classification, is outside its scope.

Unless stated otherwise, all functions that expect a byte position as a
parameter assume that the given position is either the start of a byte
sequence or one plus the length of the subject string. As in the string
library, negative indices count from the end of the string.

You can find a large catalog of usable `UTF-8` characters
[here](https://www.w3schools.com/charsets/ref_html_utf8.asp).

## Properties

### utf8.charpattern

**Type:** `string`

The pattern `"[%z\x01-\x7F\xC2-\xF4][\x80-\xBF]*"`, which matches exactly
zero or more UTF-8 byte sequence, assuming that the subject is a valid
UTF-8 string.

## Functions

### utf8.char

**Signature:** `utf8.char(codepoints: Tuple<int>): string`

Receives zero or more codepoints as integers, converts each one to its
corresponding UTF-8 byte sequence and returns a string with the
concatenation of all these sequences.

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `codepoints` | `Tuple<int>` |  | Zero or more integer codepoints in the range `[0, 0x10ffff]` to encode. |

**Returns:** `string` — A string containing the concatenated UTF-8 byte sequences for each
codepoint.

### utf8.codes

**Signature:** `utf8.codes(str: string): function, string, int`

Returns an iterator function so that the construction:

```lua
local str = "héllo"
for position, codepoint in utf8.codes(str) do
	print(position, codepoint)
end
```

will iterate over all codepoints in string `str`. It raises an error if it
meets any invalid byte sequence.

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `str` | `string` |  | The string to iterate over. |

**Returns:** `function`, `string`, `int` — The iterator function that, on each call, returns the byte position
and codepoint of the next character. The input string (passed as the invariant state to the iterator). The initial control value (`0`) for the iterator.

### utf8.codepoint

**Signature:** `utf8.codepoint(str: string, i?: int, j?: int): Tuple<int>`

Returns the codepoints (as integers) from all codepoints in the provided
string (str) that start between byte positions `i` and `j` (both
included). The default for `i` is `1` and for `j` is `i`. It raises an
error if it meets any invalid byte sequence.

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `str` | `string` |  | The UTF-8 encoded string to extract codepoints from. |
| `i` | `int` | `1` | The index of the codepoint that should be fetched from this string. |
| `j` | `int` | `i` | The index of the last codepoint between `i` and `j` that will be returned. If excluded, this will default to the value of `i`. |

**Returns:** `Tuple<int>` — The codepoints as integers for all characters that start between byte
positions `i` and `j`.

### utf8.len

**Signature:** `utf8.len(s: string, i?: int, j?: int): int`

Returns the number of UTF-8 codepoints in the string _str_ that start
between positions `i` and `j` (both inclusive). The default for `i` is `1`
and for `j` is `-1`. If it finds any invalid byte sequence, returns a nil
value plus the position of the first invalid byte.

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `s` | `string` |  | The UTF-8 encoded string to measure. |
| `i` | `int` | `1` | The starting position. |
| `j` | `int` | `-1` | The ending position. |

**Returns:** `int` — The number of UTF-8 codepoints in the specified range, or `nil`
followed by the byte position of the first invalid byte sequence.

### utf8.offset

**Signature:** `utf8.offset(s: string, n: int, i?: int): int?`

Returns the position (in bytes) where the encoding of the `n`‑th codepoint
of `s` (counting from byte position `i`) starts. A negative `n` gets
characters before position `i`. The default for `i` is `1` when `n` is
non-negative and `#s + 1` otherwise, so that `utf8.offset(s, -n)` gets the
offset of the `n`‑th character from the end of the string. If the
specified character is neither in the subject nor right after its end, the
function returns `nil`.

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `s` | `string` |  | The UTF-8 encoded string to search within. |
| `n` | `int` |  | The character offset to seek. Positive values count forward, negative values count backward, and `0` finds the start of the character at byte position `i`. |
| `i` | `int` | `1` | The byte position from which to start counting. Defaults to `1` when `n` is non-negative and `#s + 1` when `n` is negative. |

**Returns:** `int?` — The byte position where the target codepoint begins, or `nil` if the
character is not within the string.

### utf8.graphemes

**Signature:** `utf8.graphemes(str: string, i: number, j: number): function`

Returns an iterator function so that

```lua
for first, last in utf8.graphemes(str) do
	local grapheme = s:sub(first, last)
	-- body
end
```

will iterate the grapheme clusters of the string.

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `str` | `string` |  | The UTF-8 encoded string to iterate over for grapheme clusters. |
| `i` | `number` |  | The starting byte position within the string. Negative values count from the end. |
| `j` | `number` |  | The ending byte position within the string. Negative values count from the end. |

**Returns:** `function` — An iterator function that returns the start and end byte positions of
each grapheme cluster.

### utf8.nfcnormalize

**Signature:** `utf8.nfcnormalize(str: string): string`

Converts the input string to Normal Form C, which tries to convert
decomposed characters into composed characters.

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `str` | `string` |  | The UTF-8 encoded string to normalize. |

**Returns:** `string` — The NFC-normalized string with decomposed characters composed into
their precomposed equivalents.

### utf8.nfdnormalize

**Signature:** `utf8.nfdnormalize(str: string): string`

Converts the input string to Normal Form D, which tries to break up
composed characters into decomposed characters.

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `str` | `string` |  | The string to convert. |

**Returns:** `string` — The NFD-normalized string with precomposed characters decomposed into
their component parts.