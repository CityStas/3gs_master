---
name: table
last_updated: 2026-10-30T19:55:54Z
type: library
summary: "A library of table functions."
---

# table

A library of table functions.

**Type:** library

## Description

This library provides generic functions for table/array manipulation,
providing all its functions inside the global [table](/docs/reference/engine/globals/table.md) variable. Most
functions in the [table](/docs/reference/engine/globals/table.md) library assume that the table represents an
array or a list. For these functions, the "length" of a table means the result
of the length operator.

## Functions

### table.clear

**Signature:** `table.clear(table: table): ()`

Sets the value for all keys within the given table to `nil`. This causes
the `#` operator to return `0` for the given table. The allocated capacity
of the table's array portion is maintained, which allows for efficient
re-use of the space.

```lua
local grades = {95, 82, 71, 92, 100, 60}
print(grades[4], #grades) --> 92, 6
table.clear(grades)
print(grades[4], #grades) --> nil, 0
-- If grades is filled again with the same number of entries,
-- no potentially expensive array resizing will occur
-- because the capacity was maintained by table.clear.
```

This function does not delete/destroy the table provided to it. This
function is meant to be used specifically for tables that are to be
re-used.

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `table` | `table` |  | The table whose keys will be cleared. |

**Returns:** `()`

### table.clone

**Signature:** `table.clone(t: table): table`

Returns an unfrozen shallow copy of the provided table.

```lua
local original = {
	key = "value",
	engine = "Roblox",
	playerID = 505306092
}

local clone = table.clone(original)
```

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `t` | `table` |  | The table to be cloned. |

**Returns:** `table` — The clone of the provided table.

### table.concat

**Signature:** `table.concat(t: Array, sep: string, i?: int, j: int): string`

Given an array where all elements are strings or numbers, returns the
string `t[i] ... sep ... t[i+1] ... sep ... t[j]`. The default value for
sep is an empty string, the default for `i` is 1, and the default for `j`
is #t. If i is greater than `j`, returns the empty string.

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `t` | `Array` |  | The table that will be converted into a string. |
| `sep` | `string` |  | The string that will be concatenated between each entry in the table. |
| `i` | `int` | `1` | The starting index of the table concatenation. |
| `j` | `int` |  | The ending index of the table concatenation. |

**Returns:** `string` — The concatenated string of table elements joined by the separator.

### table.create

**Signature:** `table.create(count: number, value: Variant): table`

Creates a table with the array portion allocated to the given `number` of
elements, optionally filled with the given `value`.

```lua
local t = table.create(3, "Roblox")
print(table.concat(t)) --> RobloxRobloxRoblox
```

If you are inserting into large array-like tables and are certain of a
reasonable upper limit to the number of elements, it's recommended to use
this function to initialize the table. This ensures the table's array
portion of its memory is sufficiently sized, as resizing it can be
expensive. For small quantities this is typically not noticeable.

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `count` | `number` |  | The number of elements to allocate in the array portion of the new table. |
| `value` | `Variant` |  | The value to fill each element with. If omitted, elements are left as `nil`. |

**Returns:** `table` — A new table with the array portion pre-allocated to `count` elements,
filled with `value` if provided.

### table.find

**Signature:** `table.find(haystack: table, needle: Variant, init: number): Variant`

Within the given array-like table `haystack`, find the first occurrence of
value `needle`, starting from index `init` or the beginning if not
provided. If the value is not found, `nil` is returned.

A [linear search](https://en.wikipedia.org/wiki/Linear_search) algorithm
is performed.

```lua
local t = {"a", "b", "c", "d", "e"}
print(table.find(t, "d")) --> 4
print(table.find(t, "z")) --> nil, because z is not in the table
print(table.find(t, "b", 3)) --> nil, because b appears before index 3
```

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `haystack` | `table` |  | The array-like table to search through. |
| `needle` | `Variant` |  | The value to search for within the table. |
| `init` | `number` |  | The index at which to begin searching. Defaults to `1`. |

**Returns:** `Variant` — The numeric index of the first occurrence of `needle`, or `nil` if not
found.

### table.freeze

**Signature:** `table.freeze(t: table): table`

This function makes the given table read-only, effectively "freezing" it
in its current state. Attempting to modify a frozen table throws an error.

This freezing effect is shallow, which means that you can write to a table
within a frozen table. To deep freeze a table, call this function
recursively on all of the descending tables.

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `t` | `table` |  | The table to be frozen. |

**Returns:** `table` — The frozen table.

### table.insert

**Signature:** `table.insert(t: Array, pos: number, value: Variant): ()`

Inserts `value` into array `t` at position `pos`, shifting up the elements
`t[pos], t[pos+1], ..., t[#t]` by one position. The position must be
between `1` and `#t` (inclusive) for the shift to occur; the value is then
written at `t[pos]`.

```lua
local t = {"a", "b", "c"}
table.insert(t, 2, "new")
print(table.concat(t, ", ")) --> a, new, b, c
```

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `t` | `Array` |  | The table that is being appended to. |
| `pos` | `number` |  | The position at which the value will be inserted. |
| `value` | `Variant` |  | The value that will be appended to the table. |

**Returns:** `()`

### table.insert

**Signature:** `table.insert(t: Array, value: Variant): ()`

Appends `value` to the end of array `t` at position `#t + 1`. Unlike the
positional overload, no existing elements are shifted, making this the
most efficient way to grow an array by one element.

```lua
local t = {"a", "b", "c"}
table.insert(t, "d")
print(table.concat(t, ", ")) --> a, b, c, d
```

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `t` | `Array` |  | The table that is being appended to. |
| `value` | `Variant` |  | The value that will be appended to the table. |

**Returns:** `()`

### table.isfrozen

**Signature:** `table.isfrozen(t: table): bool`

This function returns `true` if the given table is frozen and `false` if
it isn't frozen. You can freeze tables using [table.freeze()](/docs/reference/engine/globals/table.md).

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `t` | `table` |  | The table to check. |

**Returns:** `bool` — Whether the table is frozen from [table.freeze()](/docs/reference/engine/globals/table.md).

### table.maxn

**Signature:** `table.maxn(t: table): number`

Returns the maximum numeric key of the provided table, or zero if the
table has no numeric keys. Gaps in the table are ignored.

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `t` | `table` |  | The table to scan for numeric keys. |

**Returns:** `number` — The largest positive numeric key in the table, or `0` if the table has
no numeric keys.

### table.move

**Signature:** `table.move(src: table, a: number, b: number, t: number, dst?: table): table`

Copies elements in table `src` from `src[a]` up to `src[b]` into table
`dst` starting at index `t`. Equivalent to the assignment statement
`dst[t], ..., dst[t + (b - a)] = src[a], ..., src[b]`.

The default for `dst` is `src`. The destination range may overlap with the
source range. Returns `dst` for convenience.

```lua
local sourceTable = {4, 5} -- Table of data to copy from
local destTable = {1, 2, 3} -- Table to add copied data to

table.move(
	sourceTable, -- Source table
	1, -- Index to start from in source table
	#sourceTable, -- Index up to (and including) from source table
	#destTable + 1, -- Index within destination table to move data into
	destTable -- Destination table
)
print(destTable) --> {1, 2, 3, 4, 5}
```

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `src` | `table` |  | Source table. |
| `a` | `number` |  | Start copying at `src[a]`. |
| `b` | `number` |  | Copy up to and including `src[b]`. |
| `t` | `number` |  | Copy into `dst[t], ...`. |
| `dst` | `table` | `src` | Destination table. |

**Returns:** `table` — `dst` for convenience.

### table.pack

**Signature:** `table.pack(values...: Variant): Variant`

Returns a new table with all arguments stored into keys 1, 2, etc. and
with a field "n" with the total number of arguments. Note that the
resulting table may not be a sequence.

```lua
local t = table.pack(1, 2, 3)
print(table.concat(t, ", ")) --> 1, 2, 3
```

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `values...` | `Variant` |  | The values to store sequentially in the new table. |

**Returns:** `Variant` — A new table with arguments at keys `1` through `n`, plus an `n` field
storing the total argument count.

### table.remove

**Signature:** `table.remove(t: Array, pos: number): Variant`

Removes from array t the element at position pos, returning the value of
the removed element. When pos is an integer between `1` and `#t`, it
shifts down the elements `t[pos+1], t[pos+2], ..., t[#t]` and erases
element `t[#t]`. If the pos parameter is not provided, pos defaults to the
length of the table removing the last element.

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `t` | `Array` |  | The table that is having an element removed. |
| `pos` | `number` |  | The index of the element being removed. |

**Returns:** `Variant` — The value of the element that was removed, or nothing if the position
is out of bounds.

### table.sort

**Signature:** `table.sort(t: Array, comp?: function): ()`

Sorts elements of array t in a given order, from `t[1]` to `t[#t]`. If
`comp` is given, then it must be a function that receives two elements and
returns true when the first element must come before the second in the
final order.

The error `invalid order function for sorting` is thrown if both
`comp(a, b)` and `comp(b, a)` return `true`.

If `comp` is not given, then the standard Luau operator `<` is used
instead.

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `t` | `Array` |  | The array to sort in place. |
| `comp` | `function` | `nil` | An optional comparison function to be used when comparing elements in the table. This function receives two elements, and should return true if the first element should be sorted before the second in the final order. |

**Returns:** `()`

### table.unpack

**Signature:** `table.unpack(list: table, i?: number, j?: number): Tuple`

Returns the elements from the given list. By default, `i` is 1 and `j` is
the length of `list`.

Note that this same functionality is also provided by the global
[LuaGlobals.unpack()](/docs/reference/engine/globals/LuaGlobals.md) function.

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `list` | `table` |  | The list of elements to be unpacked. |
| `i` | `number` | `1` | The index of the first element to unpack. |
| `j` | `number` | `#list` | The index of the last element to unpack. |

**Returns:** `Tuple` — The elements `list[i], list[i+1], ..., list[j]` as individual return
values.

### table.foreach *(deprecated)*

**Signature:** `table.foreach(t: table, f: function): ()`

Iterates over the provided table, passing the key and value of each
iteration over to the provided function. This function has been deprecated
and is not recommended for use in new code; use a `for` loop instead.

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `t` | `table` |  | The table to be iterated over. |
| `f` | `function` |  | The function that will be used for the iteration. This function will receive 2 arguments for each iteration, where the 1st argument is the key, and the 2nd argument is the value. |

**Returns:** `()`

### table.foreachi *(deprecated)*

**Signature:** `table.foreachi(t: Array, f: function): ()`

This is similar to [table.foreach()](/docs/reference/engine/globals/table.md) except that index-value pairs
are passed, not key-value pairs. This function has been deprecated and is
not recommended for use in new code; use a `for` loop instead.

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `t` | `Array` |  | The table to be iterated over. |
| `f` | `function` |  | The function that will be used for the iteration. This function will receive 2 arguments for each iteration, where the 1st argument is the index, and the 2nd argument is the value. |

**Returns:** `()`

### table.getn *(deprecated)*

**Signature:** `table.getn(t: Array): number`

Returns the number of elements in the table passed. This function has been
deprecated and is not recommended for use in new code; use `#t` instead.

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `t` | `Array` |  | The table whose size is being measured. |

**Returns:** `number` — The length of the array portion of the table, equivalent to the `#`
operator.