---
name: string
last_updated: 2026-10-30T19:55:54Z
type: library
summary: "Provides generic functions to manipulate strings."
---

# string

Provides generic functions to manipulate strings.

**Type:** library

## Description

The string library provides generic functions to manipulate strings, such as
to extract substrings or match patterns. You can access the string library by
the global [string](/docs/reference/engine/globals/string.md) library.

See
[String pattern reference](/docs/en-us/luau/strings.md#string-pattern-reference)
for details on using [string.match()](/docs/reference/engine/globals/string.md), [string.gmatch()](/docs/reference/engine/globals/string.md), and
[string.gsub()](/docs/reference/engine/globals/string.md) to find (and replace) substrings.

## Functions

### string.byte

**Signature:** `string.byte(s: string, i?: number, j?: number): int`

Returns the internal numerical codes of the characters
`s[i], s[i+1], ..., s[j]`. The default value for `i` is 1; the default
value for `j` is `i`. These indices are corrected following the same rules
of function [string.sub()](/docs/reference/engine/globals/string.md).

Numerical codes correspond to single-byte character values (`0`-`255`).
The function returns one number per character in the specified range, so
calling it on a multi-character slice yields multiple return values. If
the resolved range is empty (start index greater than end index after
adjustment), no values are returned.

```lua
-- Single character
print(string.byte("A")) -- 65

-- Range of characters
print(string.byte("hello", 1, 3)) -- 104 101 108

-- Negative indices (counts from end)
print(string.byte("abc", -1)) -- 99 (the byte value of 'c')

-- Roundtrip with string.char
local a, b, c = string.byte("ABC", 1, 3)
print(string.char(a, b, c)) -- ABC
```

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `s` | `string` |  | The string to extract byte values from. |
| `i` | `number` | `1` | The starting index of the range of characters to convert. |
| `j` | `number` | `i` | The ending index of the range of characters to convert. |

**Returns:** `int`

### string.char

**Signature:** `string.char(...: int): string`

Receives zero or more integers and returns a string with length equal to
the number of arguments, in which each character has the internal
numerical code equal to its corresponding argument.

Each integer must be in the range `[0, 255]`; values outside that range
raise an error. This is the inverse of [string.byte()](/docs/reference/engine/globals/string.md).

```lua
-- Basic usage
print(string.char(72, 101, 108, 108, 111)) -- Hello

-- Single character
print(string.char(65)) -- A

-- Construct from byte values (e.g. null byte)
local s = string.char(0)
print(#s) -- 1

-- Roundtrip with string.byte
local code = string.byte("Z")
print(string.char(code)) -- Z
```

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `...` | `int` |  | Zero or more integers in the range `[0, 255]`, each representing a byte value. |

**Returns:** `string`

### string.find

**Signature:** `string.find(s: string, pattern: string, init?: number, plain?: bool): number, number`

Searches for the first occurrence of a pattern in a string and returns the
start and end indices of the match. If no match is found, it returns
`nil.` You can specify where to start the search using the optional `init`
parameter which defaults to `1` and can be negative. An optional `plain`
parameter turns off pattern matching, so the function performs a plain
substring search; note that if you use `plain`, you must also provide
`init.`

```lua
-- Example 1: Basic usage
local s = "Hello, world!"
local pattern = "world"
local start_index, end_index = string.find(s, pattern)
print(start_index, end_index)  -- Output: 8 12
```

```lua
-- Example 2: Using init parameter
local s = "Hello, world! Hello, Roblox!"
local pattern = "Hello"
local start_index, end_index = string.find(s, pattern, 10)
print(start_index, end_index)  -- Output: 15 19
```

```lua
-- Example 3: Using plain parameter
local s = "Hello, world! (Hello)"
local pattern = "(Hello)"
local start_index, end_index = string.find(s, pattern, 1, true)
print(start_index, end_index)  -- Output: 14 20
```

```lua
-- Example 4: No Pattern found
local s = "Hello, world!"
local pattern = "Roblox"
local start_index, end_index = string.find(s, pattern)
print(start_index, end_index)  -- Output: nil
```

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `s` | `string` |  | The string to search within. |
| `pattern` | `string` |  | The pattern to search for in given string. |
| `init` | `number` | `1` | The starting index for the search. |
| `plain` | `bool` | `false` | If true, turns off pattern matching and performs a plain substring search. |

**Returns:** `number`, `number` — The starting index of the match. The ending index of the match.

### string.format

**Signature:** `string.format(formatstring: string, ...: string): string`

Returns a formatted version of its variable number of arguments following
the description given in its first argument, which must be a string.

You can convert variables into user-friendly strings of text using the
[string.format()](/docs/reference/engine/globals/string.md) function. The function requires the following
format:

`%[flags][width].[precision][specifier]`.

#### Specifiers

The most important part of string formatting is the **specifiers**.

| Specifier | Accepts | Outputs | Example Output |
| --- | --- | --- | --- |
| `c` | integer |  | `3` |
| `d` or `i` | integer | Decimal representation. | `321` |
| `e` or `E` | float | Scientific notation using `e` or `E`. | `3.296e2`
`3.296E2` |
| `f` | float |  | `3231.1231` |
| `g` or `G` | float | The shorter of `e`/`E` and `f`. | `3E14`
`3e14` |
| `o` | integer | Octal representation. | `610` |
| `q` | string | String in a form suitable to be safely read back by the Luau interpreter. The string is written between double quotes and all double quotes, new lines, embedded zeros, and backslashes are correctly escaped. | `"print(\"Hi\")"` |
| `s` | string |  | `Hello world!` |
| `u` | integer | Decimal representation. | `3131` |
| `x` or `X` | integer | Hexadecimal representation. | `7fa`
`7FA` |
| `*` | any | Equivalent to `s` but accepts any variable by converting it to a string using [LuaGlobals.tostring()](/docs/reference/engine/globals/LuaGlobals.md). | `table: 0x0123456789abcdef` |
| `%` |  | `%` followed by another `%` will return the `%` sign itself. | `%` |

```lua
local str = "The magic word is %s"
print(string.format(str, "Roblox"))
-- The magic word is Roblox

local str = "The magic word is %q"
print(string.format(str, "Roblox"))
-- The magic word is "Roblox"

local str = "Skip to \na new line and \nanother new line!"
print(string.format(str, "%q"))
--[[ Output:
Skip to
a new line and
another new line!
]]
```

#### Flags

| Flag | Description |
| --- | --- |
| `-` | Left-justify the given field width (see **Width** below). Right justification is the default. |
| `+` | Forces a `+` sign to precede a number. Has no effect on negative numbers. |
| (space) | One blank space is inserted before a positive number, while negative numbers are unaffected. This is useful for making positive and negative numbers vertically align in a visual stacked list. |
| `#` | When used with `o` and `x`/`X`, writes a `0` (octal) or `0x`/`0X` (hex) before values other than zero.
When used with `e`/`E` and `f`, forces the output to contain a decimal point, even if no digits would follow (by default, no decimal point is written if no digits follow).
When used with `g` or `G`, the result is the same as with `e` or `E` but trailing zeros are not removed. |
| `0` | Left-pads the number with zeros instead of empty spaces (see **Width** below). |

```lua
local str = "%-10d"
print(string.format(str, 300) .. "]")
-- 300       ]
-- There are 7 spaces between '300' and ']'

local str = "%+i versus %+i"
print(string.format(str, 300, -300)) -- +300 versus -300

local str = "There is a% i%% chance of rain in Seattle today."
print(string.format(str, 100))
-- There is a 100% chance of rain in Seattle today.
```

#### Width

| Width | Description |
| --- | --- |
| (number) | Minimum number of characters to return. If the number of characters to be formatted is less than this number, the result is padded with blank spaces. |

```lua
local str = "%012i"
print("Score: " .. string.format(str, 15000))
-- Output: Score: 000000015000
-- The output has 12 digits total, left-padded with zeros
```

#### Precision

The default precision is <code>1</code>. If you give a period without a
value, the default is <code>0</code>.

| Precision | Description |
| --- | --- |
| `.`(number) | For integer specifiers (`d`, `i`, `o`, `u`, `x`/`X`), precision specifies the minimum number of digits to be returned. If the value to be formatted is shorter than this number, the result is padded with leading zeros. A precision of `0` means that no character is written for the value `0`.
For `e`/`E` and `f` specifiers, this is the number of digits to be printed after the decimal point.
For `g`/`G` specifiers, this is the maximum number of digits (before the `e`/`E`, if present).
For `s`, this is the maximum number of characters to be returned.
For `c` and `q`, this has no effect. |

```lua
-- Add decimal with precision of 2 for a currency output
local str = "$%.2f"
print(string.format(str, 300)) -- Output: $300.00

-- Return first 6 letters of a string
local str = "%.6s"
print(string.format(str, "Robloxian")) -- Output: Roblox

local str = "Once upon a time, there was a dragon named %s and it had %.8f horns."
print(string.format(str, "Pi", math.pi))
-- Output: Once upon a time, there was a dragon named Pi and it had 3.14159265 horns.
```

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `formatstring` | `string` |  | A string containing format specifiers that control how subsequent arguments are formatted. |
| `...` | `string` |  | Values to be formatted according to the specifiers in the format string. |

**Returns:** `string`

### string.gmatch

**Signature:** `string.gmatch(s: string, pattern: string): function`

Returns an iterator function that, each time it is called, returns the
next captures from `pattern` over the string `s`. If the pattern has no
captures, the whole match is returned on each call.

The iterator is typically used in a generic `for` loop. When the pattern
contains capture groups, each call returns the captured substrings as
separate values. An empty match (zero-width) advances past the current
position by one character to avoid an infinite loop.

```lua
-- Iterate over all words in a sentence
for word in string.gmatch("Hello Roblox world", "%a+") do
    print(word)
end
-- Hello
-- Roblox
-- world

-- Extract key-value pairs using captures
local t = {}
for key, value in string.gmatch("name=Roblox, version=1.0", "(%w+)=(%w[%w.]*)") do
    t[key] = value
end
print(t.name, t.version) -- Roblox 1.0

-- Collect all digits
local digits = {}
for d in string.gmatch("abc123def456", "%d+") do
    table.insert(digits, d)
end
print(table.concat(digits, ", ")) -- 123, 456
```

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `s` | `string` |  | The string to search for pattern matches. |
| `pattern` | `string` |  | The pattern to match repeatedly against the string. |

**Returns:** `function`

### string.gsub

**Signature:** `string.gsub(s: string, pattern: string, replacement: Variant, replacements: number): string, number`

Short for global substitution. Returns a copy of `s` in which all (or the
first `n`, if given) occurrences of the pattern are substituted (replaced)
with the given `replacement`. The second value returned is the total
number of substitutions made.

The `replacement` can be one of several types, each used differently to
determine the actual string:

- string: The pattern is replaced with the string directly
- table: The string that matched the pattern is looked up in the table as
  a key, and the value (string) is what replaces it, if it exists.
- function: Called with the string that matched the pattern, should return
  the string to replace the matched pattern.

An optional final argument can be provided which specifies the maximum
number of substitutions to make (for example, stop after 2 replacements)

#### Various Examples

```lua
-- Basic replacement
string.gsub("I love tacos!", "tacos", "Roblox") --> I love Roblox! 1
-- Replacement with a pattern
string.gsub("I like red!", "%w+", "word") --> word word word! 3
-- Replacement table
string.gsub("I play Roblox.", "%w+", {I="Je", play="joue à"}) --> "Je joue à Roblox." 3
-- Replacement function
string.gsub("I have 2 cats.", "%d+", function(n) return tonumber(n) * 12 end) --> "I have 24 cats." 1
-- Replace only twice
string.gsub("aaa", "a", "b", 2) --> "bba" 2
-- Replacement with capture groups (maximum of nine)
string.gsub("love2play Roblox", "(%w+)(%d+)(%w+)%s+(%w+)", "I %1 %2 %3 %4!") --> "I love 2 play Roblox!" 1
```

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `s` | `string` |  | The string whose occurrences of the given pattern shall be replaced. |
| `pattern` | `string` |  | The pattern to be matched and replaced. |
| `replacement` | `Variant` |  | Determines what should replace the occurrence(s) of the given pattern. |
| `replacements` | `number` |  | The maximum number of substitutions to make. |

**Returns:** `string`, `number`

### string.len

**Signature:** `string.len(s: string): int`

Returns the number of bytes in the string `s`. Because Luau strings are
byte sequences, this counts bytes rather than Unicode characters or
grapheme clusters. An empty string returns `0`. Embedded null bytes (`\0`)
are included in the count.

```lua
print(string.len("Hello")) -- 5
print(string.len(""))      -- 0

-- Embedded null bytes are counted
local s = "ab\0cd"
print(string.len(s)) -- 5

-- Equivalent to the # length operator
local str = "Roblox"
print(string.len(str) == #str) -- true
```

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `s` | `string` |  | The string to measure. |

**Returns:** `int`

### string.lower

**Signature:** `string.lower(s: string): string`

Returns a copy of the string `s` with all uppercase ASCII letters
(`A`-`Z`) changed to their lowercase equivalents (`a`-`z`). Characters
outside the ASCII letter range, including accented or multibyte
characters, are left unchanged.

```lua
print(string.lower("HELLO")) -- hello
print(string.lower("Hello World!")) -- hello world!

-- Non-letter characters are unaffected
print(string.lower("Roblox 123!")) -- roblox 123!

-- Only ASCII letters are converted
print(string.lower("ABC abc")) -- abc abc
```

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `s` | `string` |  | The string to convert to lowercase. |

**Returns:** `string`

### string.match

**Signature:** `string.match(s: string, pattern: string, init?: number): string`

Looks for the first match of `pattern` in the string `s`. If the pattern
contains captures, the captured substrings are returned as separate
values; otherwise, the whole match is returned. If no match is found, the
function returns `nil`.

The optional third argument `init` specifies the byte position to start
the search (default `1`). A negative `init` counts from the end of the
string. Unlike [string.find()](/docs/reference/engine/globals/string.md), this function returns captured
values directly rather than the match indices.

```lua
-- Extract matched substring
print(string.match("I have 42 cats", "%d+")) -- 42

-- Multiple captures
local year, month, day = string.match("2024-03-15", "(%d+)-(%d+)-(%d+)")
print(year, month, day) -- 2024 03 15

-- No match returns nil
print(string.match("hello", "%d+")) -- nil

-- Using init to skip ahead
print(string.match("foo123bar456", "%d+", 7)) -- 456

-- Anchored pattern
print(string.match("hello", "^%a+")) -- hello
```

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `s` | `string` |  | The string to search for a pattern match. |
| `pattern` | `string` |  | The pattern to match against the string. |
| `init` | `number` | `1` | The byte position at which to start searching. |

**Returns:** `string`

### string.pack

**Signature:** `string.pack(format: string, ...: Variant): string`

Returns a binary string containing the provided arguments. The first
argument, `format`, determines the way the remaining arguments are packed;
see [here](https://www.lua.org/manual/5.3/manual.html#6.4.2) for options.

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `format` | `string` |  | A format string that describes the layout and types of the values to pack. |
| `...` | `Variant` |  | The values to serialize into binary form according to the format string. |

**Returns:** `string`

### string.packsize

**Signature:** `string.packsize(format: string): number`

Returns the size in bytes of any string packed with a given description.
The sole argument, `format`, determines the way the remaining arguments
are packed, but you cannot use `s` and `z` because they have variable
lengths. See [here](https://www.lua.org/manual/5.3/manual.html#6.4.2) for
options.

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `format` | `string` |  | A format string describing the packing layout (must not contain variable-length options `s` or `z`). |

**Returns:** `number`

### string.rep

**Signature:** `string.rep(s: string, n: int): string`

Returns a string that is the concatenation of `n` copies of the string
`s`. If `n` is zero or negative, the function returns an empty string. An
error is raised if the resulting string would exceed the maximum string
size.

```lua
print(string.rep("ab", 3))  -- ababab
print(string.rep("Go! ", 2)) -- Go! Go!

-- Zero or negative repeats return empty string
print(string.rep("x", 0))  -- (empty string)
print(string.rep("x", -1)) -- (empty string)

-- Useful for padding or separators
local separator = string.rep("-", 20)
print(separator) -- --------------------
```

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `s` | `string` |  | The string to repeat. |
| `n` | `int` |  | The number of times to repeat the string. |

**Returns:** `string`

### string.reverse

**Signature:** `string.reverse(s: string): string`

Returns a string that is the string `s` reversed byte-by-byte. Because the
reversal operates on individual bytes, multibyte UTF-8 sequences are not
preserved as valid characters after reversal.

```lua
print(string.reverse("hello"))  -- olleh
print(string.reverse("Roblox")) -- xolboR

-- Single character or empty string
print(string.reverse("a")) -- a
print(string.reverse(""))  -- (empty string)

-- Palindrome check
local function isPalindrome(s)
    local lower = string.lower(s)
    return lower == string.reverse(lower)
end
print(isPalindrome("racecar")) -- true
print(isPalindrome("hello"))   -- false
```

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `s` | `string` |  | The string to reverse. |

**Returns:** `string`

### string.split

**Signature:** `string.split(s: string, separator?: string): table`

Splits a string into parts based on the defined separator character(s),
returning a table of ordered results.

If an empty "slice" is located, that part will be returned as an empty
string. For instance `string.split("abc||def", "|")` will return a table
with three strings: `"abc"`, `""`, and `"def"`.

```lua
local input = "a,b,c"
local values = input:split(",")
print(values[1], values[2], values[3]) --> "a" "b" "c"
```

Also note that whitespace from the original string will be preserved, for
example `string.split("abc _ def", "_")` will honor the whitespace on both
sides of the `_` separator. By default, the separator character is `,` but
you can specify an alternative character or series of characters.

**Corner Cases**

#### Empty String

```lua
local result = string.split("", ",")
print(#result) --> 1
print(result[1]) --> ""
```

#### Empty Slices

```lua
local result = string.split("foo,,bar", ",")
print(result[1], result[2], result[3]) --> "foo" "" "bar"

local result2 = string.split(",foo", ",")
print(result2[1], result2[2]) --> "" "foo"

local result3 = string.split("foo,", ",")
print(result3[1], result3[2]) --> "foo" ""

local result4 = string.split(",", ",")
print(result4[1], result4[2]) --> "" ""

local result5 = string.split(",,", ",")
print(result5[1], result5[2], result5[3]) --> "" "" ""
```

#### Whitespace Preserved

```lua
local result = string.split("   whitespace   ", ",")
print(result[1]) --> "   whitespace   "

local result2 = string.split("foo , bar", ",")
print(result2[1], result2[2]) --> "foo " " bar"
```

#### Invalid UTF-8

```lua
local result = string.split("\xFF", ",")
print(result[1]) --> "\xFF"

local result = string.split("\xFF,\xFE", ",")
print(result[1], result[2]) --> "\xFF" "\xFE"
```

#### Unicode

```lua
local result = string.split("我很高兴，你呢？", "，")
print(result[1], result[2]) --> "我很高兴" "你呢？"

local result2 = string.split("hello•world", "•")
print(result2[1], result2[2]) --> "hello" "world"
```

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `s` | `string` |  | The string to split. |
| `separator` | `string` | `,` | The separator character(s) to be used for splitting the string. |

**Returns:** `table`

### string.sub

**Signature:** `string.sub(s: string, i?: int, j?: int): string`

Returns the substring of `s` that starts at byte position `i` and
continues until and including byte position `j`. Both `i` and `j` can be
negative: `-1` refers to the last byte, `-2` to the second-to-last, and so
on. The default for `i` is `1` (the beginning) and `j` defaults to `-1`
(the end).

If the resolved `i` is less than `1`, it is corrected to `1`. If `j`
exceeds the string length, it is corrected to the string length. If after
these corrections `i` is greater than `j`, the function returns an empty
string.

```lua
local s = "Hello, world!"
print(string.sub(s, 1, 5))   -- Hello
print(string.sub(s, 8))      -- world!
print(string.sub(s, -6))     -- orld!
print(string.sub(s, -6, -2)) -- orld

-- Extract file extension
local filename = "script.lua"
local dot = string.find(filename, "%.")
print(string.sub(filename, dot + 1)) -- lua

-- Empty result when start > end
print(string.sub("abc", 3, 1)) -- (empty string)
```

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `s` | `string` |  | The source string to extract a substring from. |
| `i` | `int` | `1` | The starting byte position of the substring (negative values count from the end). |
| `j` | `int` | `-1` | The ending byte position of the substring, inclusive (negative values count from the end). |

**Returns:** `string`

### string.unpack

**Signature:** `string.unpack(format: string, data: string, readStart?: string): Tuple`

Extracts the values packed in the provided binary string based on the
first argument, `format`, which should match the one originally used to
[pack()](/docs/reference/engine/globals/string.md) the string; see
[here](https://www.lua.org/manual/5.3/manual.html#6.4.2) for options. The
optional third parameter determines the byte at which the reading starts.

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `format` | `string` |  | The format string that describes how the binary data was packed. |
| `data` | `string` |  | The binary string to unpack values from. |
| `readStart` | `string` | `1` | The byte position in `data` at which to begin reading. |

**Returns:** `Tuple` — The values packed into the provided binary string, plus the index of
the first unread byte.

### string.upper

**Signature:** `string.upper(s: string): string`

Returns a copy of the string `s` with all lowercase ASCII letters
(`a`-`z`) changed to their uppercase equivalents (`A`-`Z`). Characters
outside the ASCII letter range, including accented or multibyte
characters, are left unchanged.

```lua
print(string.upper("hello")) -- HELLO
print(string.upper("Hello World!")) -- HELLO WORLD!

-- Non-letter characters are unaffected
print(string.upper("roblox 123!")) -- ROBLOX 123!

-- Only ASCII letters are converted
print(string.upper("abc ABC")) -- ABC ABC
```

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `s` | `string` |  | The string to convert to uppercase. |

**Returns:** `string`