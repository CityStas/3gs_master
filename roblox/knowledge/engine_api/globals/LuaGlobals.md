---
name: Luau globals
last_updated: 2026-10-30T19:55:54Z
type: global
summary: "A list of functions and variables that are native to Luau."
---

# Luau globals

A list of functions and variables that are native to Luau.

**Type:** global

## Description

The following is a list of functions and variables that are native to Luau.
These functions can be used in a standard installation of both
[Luau](https://luau.org) and [Lua 5.1.4](https://www.lua.org/manual/5.1/),
though there are some differences in how some of these work on Roblox.

## Properties

### _G

**Type:** `Array`

A table that is shared between all scripts of the same context level. Any
value written to `_G` from one script is visible to every other script at
that same context level, which makes it a simple way to share state
between scripts.

```lua
-- Script A (sets a value)
_G.mySharedValue = "hello from Script A"

Note that relying on `_G` for cross-script communication introduces
ordering dependencies and makes code harder to reason about. Prefer
[ModuleScript](/docs/reference/engine/classes/ModuleScript.md) for shared state when possible.
```

### _VERSION

**Type:** `string`

A global variable (not a function) that holds a string containing the
current interpreter version.

## Functions

### assert

**Signature:** `assert(value: Variant, errorMessage?: string): Variant`

Throws an error if the provided `value` is `false` or `nil`. If the
assertion passes, it returns all values passed to it.

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `value` | `Variant` |  | The value that will be asserted against. |
| `errorMessage` | `string` | `assertion failed!` | The text that will be shown in the error if the assertion fails. |

**Returns:** `Variant` — All values originally passed to `assert` if the assertion succeeds.

**Assert**

Demonstrates the `assert` global.

```lua
local product = 90 * 4
assert(product == 360, "Oh dear, multiplication is broken")
-- The line above does nothing, because 90 times 4 is 360
```

### error

**Signature:** `error(message: Variant, level?: int): ()`

Terminates the last protected function called and outputs `message` as an
error message. If the function containing the error is not called in a
protected function such as `pcall()`, then the script which called the
function will terminate. The error function itself never returns and acts
like a script error.

The `level` argument specifies how to get the error position. With level
`1` (the default), the error position is where the error function was
called. Level 2 points the error to where the function that called error
was called; and so on. Passing a level `0` avoids the addition of error
position information to the message.

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `message` | `Variant` |  | The error message to display. |
| `level` | `int` | `1` | The level of information that should be printed. Defaults to 1. |

**Returns:** `()`

### gcinfo

**Signature:** `gcinfo(): number`

Returns the total memory heap size in kilobytes. The number reflects the
current heap consumption from the operating system perspective, which
fluctuates over time as garbage collector frees objects.

**Returns:** `number` — The total memory heap size in kilobytes.

### getmetatable

**Signature:** `getmetatable(t: Variant): Variant`

Returns the metatable of the given value `t` if it has one, otherwise
returns `nil`. If `t` does have a metatable, and the `__metatable`
metamethod is set, it returns that value instead.

`t` can be a value of any type, not only a table, and this function
doesn't error when `t` isn't a table. However, it doesn't always return
`nil` for non-table values. Strings and many Roblox types, such as
[Instance](/docs/reference/engine/classes/Instance.md), have locked metatables, so this function returns the
string `"The metatable is locked"` for them. To check whether a value uses
a specific metatable, compare the result directly, such as
`getmetatable(value) == MyClass`.

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `t` | `Variant` |  | The value to fetch the metatable of. |

**Returns:** `Variant` — The metatable of `t`, the value of the `__metatable` metamethod if
set, or `nil` if no metatable exists.

**Getmetatable**

Demonstrates the `getmetatable` global.

```lua
local meta = {}
local t = setmetatable({}, meta)
print(getmetatable(t) == meta) --> true
-- Make the original metatable unrecoverable by setting the __metatable metamethod:
meta.__metatable = "protected"
print(getmetatable(t)) --> protected
```

### ipairs

**Signature:** `ipairs(t: Array): function, Array, int`

Returns three values: an iterator function, the table `t` and the number
`0`. Each time the iterator function is called, it returns the next
numerical index-value pair in the table. When used in a generic for-loop,
the return values can be used to iterate over each numerical index in the
table:

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `t` | `Array` |  | A table whose elements are to be iterated over. |

**Returns:** `function`, `Array`, `int` — An iterator function that returns the next index-value pair on each
call. The table `t` passed as the invariant state. The initial control value `0`.

**Ipairs**

Demonstrates the `ipairs` global.

```lua
local fruits = {"apples", "oranges", "kiwi"}
for index, fruit in ipairs(fruits) do
   print(index, fruit) --> 1 apples, 2 oranges, 3 kiwi, etc...
end
```

### loadstring

**Signature:** `loadstring(contents: string, chunkname: string): Variant`

Loads Luau code from a string and returns it as a function.

Unlike standard Lua 5.1, Roblox's Luau cannot load the compiled bytecode
using `loadstring()`.

`loadstring()` is disabled by default. For guidance around enabling it,
see [ServerScriptService](/docs/reference/engine/classes/ServerScriptService.md).

**WARNING:** This method disables certain Luau optimizations on the
returned function. Extreme caution should be taken when using
[LuaGlobals.loadstring()](/docs/reference/engine/globals/LuaGlobals.md); if your intention is to allow users to
run code in your experience, make sure to protect the returned function's
environment by using [LuaGlobals.getfenv()](/docs/reference/engine/globals/LuaGlobals.md) and
[LuaGlobals.setfenv()](/docs/reference/engine/globals/LuaGlobals.md).

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `contents` | `string` |  | The specified string to be loaded as Luau code. |
| `chunkname` | `string` |  | An optional chunk name for error messages and debug information. If unspecified, Luau uses the `contents` string. |

**Returns:** `Variant` — The compiled function on success, or `nil` followed by an error
message string on failure.

### newproxy

**Signature:** `newproxy(addMetatable?: bool): userdata`

Creates a blank zero-size `userdata` with the option for it to have a
metatable. If `addMetatable` is `true`, an empty metatable is created and
assigned to the userdata; you can then retrieve it with
[LuaGlobals.getmetatable()](/docs/reference/engine/globals/LuaGlobals.md) and populate it with metamethods. If
`addMetatable` is `false` or omitted, the userdata has no metatable and
only serves as a unique identity token.

Unlike host-created userdata (Roblox instances), a `newproxy`-created
userdata always reports `"userdata"` from both [LuaGlobals.type()](/docs/reference/engine/globals/LuaGlobals.md)
and `typeof()`; setting a `__type` metamethod on it does not change the
`typeof()` result.

```lua
-- Create a proxy with a metatable to implement custom tostring
local proxy = newproxy(true)
local mt = getmetatable(proxy)

mt.__tostring = function()
	return "MyProxy"
end

print(tostring(proxy)) --> MyProxy
print(type(proxy)) --> userdata
```

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `addMetatable` | `bool` | `false` | Whether to attach an empty metatable to the new userdata. |

**Returns:** `userdata` — A new blank userdata, with an empty metatable attached if
`addMetatable` is `true`.

### next

**Signature:** `next(t: table, lastKey?: Variant): Variant, Variant`

Returns the first key/value pair in the array. If a `lastKey` argument was
specified then returns the next element in the array based on the key that
provided. The order in which the indices are enumerated is not specified,
even for numeric indices. To traverse a table in numeric order, use a
numerical for loop or `ipairs`.

The behavior of next is undefined if, during the traversal, you assign any
value to a non-existent field in the table. You may, however, modify
existing fields. In particular, you may clear existing fields.

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `t` | `table` |  | The array to be traversed. |
| `lastKey` | `Variant` | `nil` | The last key that was previously retrieved from a call to next. |

**Returns:** `Variant`, `Variant` — The next key in the table, or `nil` if the traversal is complete. The value associated with the returned key.

### pairs

**Signature:** `pairs(t: table): function, table, Variant`

Returns an iterator function, the passed table `t`, and `nil`, so that the
construction will iterate over all key/value pairs of that table when used
in a generic `for` loop:

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `t` | `table` |  | An array or dictionary table to iterate over. |

**Returns:** `function`, `table`, `Variant` — The `next` function as the iterator. The table `t` passed as the invariant state. The initial control value `nil`.

**Pairs**

Demonstrates the `pairs` global.

```lua
local scores = {
    ["John"] = 5,
    ["Sally"] = 10
}

for name, score in pairs(scores) do
    print(name .. " has score: " .. score)
end
```

### pcall

**Signature:** `pcall(func: function, args: Tuple): bool, Variant`

Calls the function `func` with the given arguments in protected mode. This
means that any error inside `func` is not propagated; instead, `pcall()`
catches the error and returns a status code. Its first result is the
status code (a boolean), which is true if the call succeeds without
errors. In such case, `pcall()` also returns all results from the call,
after this first result. In case of any error, `pcall()` returns false
plus the error message.

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `func` | `function` |  | The function to be called in protected mode. |
| `args` | `Tuple` |  | The arguments to send to `func` when executing. |

**Returns:** `bool`, `Variant` — `true` if `func` executed without errors, `false` otherwise. All return values of `func` on success, or the error message on
failure.

**Pcall**

Demonstrates the `pcall` global.

```lua
local function divideByFive(n: number): number
	return n / 5
end

local success, errorMessage = pcall(divideByFive, "notANumber")  -- Results in error...

if success then
	-- Handle successful response...
else
	print("Error message:", errorMessage)
end
```

### print

**Signature:** `print(params: Tuple): ()`

Receives any number of arguments, and prints their values to the output.
`print` is not intended for formatted output, but only as a quick way to
show a value, typically for debugging. For a formatted output, use
[string.format()](/docs/reference/engine/globals/string.md). On Roblox, `print` does not call `tostring`,
but the `__tostring` metamethod still fires if the table has one.

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `params` | `Tuple` |  | Any number of arguments to be outputted. |

**Returns:** `()`

### rawequal

**Signature:** `rawequal(v1: Variant, v2: Variant): bool`

Checks whether `v1` is equal to `v2` without invoking the `__eq`
metamethod. The comparison uses primitive equality rules: values of
different types are never equal; `nil` equals only itself; numbers and
vectors are compared by value; booleans are compared by value; and all
reference types (tables, functions, threads, userdata) are compared by
identity (same object in memory).

This is useful when you need to compare two tables or userdata objects
that have an `__eq` metamethod and you want to test whether they are
literally the same object rather than semantically equal.

```lua
local a = setmetatable({}, {__eq = function() return true end})
local b = setmetatable({}, {__eq = function() return true end})
print(a == b) --> true (metamethod fires)
print(rawequal(a, b)) --> false (different objects)
print(rawequal(a, a)) --> true (same object)
```

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `v1` | `Variant` |  | The first variable to compare. |
| `v2` | `Variant` |  | The second variable to compare. |

**Returns:** `bool` — `true` if `v1` and `v2` are primitively equal without metamethod
invocation, `false` otherwise.

### rawget

**Signature:** `rawget(t: table, index: Variant): Variant`

Gets the real value of `table[index]` without invoking the `__index`
metamethod. The first argument must be a table; the second can be any
non-`nil` value. If the key does not exist in the table itself, `rawget()`
returns `nil` rather than walking up the metatable chain.

This is useful for inspecting a table's own stored fields when a
metatable-based lookup chain would otherwise intercept the access.

```lua
local fallback = {x = 10}
local t = setmetatable({}, {__index = fallback})
print(t.x) --> 10 (found via __index)
print(rawget(t, "x")) --> nil (not in t itself)
t.y = 20
print(rawget(t, "y")) --> 20 (stored directly in t)
```

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `t` | `table` |  | The table to be referenced. |
| `index` | `Variant` |  | The index to get from `t`. |

**Returns:** `Variant` — The value stored at `t[index]`, or `nil` if the key does not exist in
the table itself.

### rawlen

**Signature:** `rawlen(t: table): number`

Returns the length of a table or string without invoking the `__len`
metamethod. The argument must be a table or string; passing any other type
raises an argument error. For tables, the result is equivalent to what the
`#` operator would return before any metamethod fires; the length of the
array portion as determined by the boundary search. For strings, it
returns the byte count.

```lua
local t = setmetatable({1, 2, 3}, {__len = function() return 999 end})
print(#t) --> 999 (metamethod fires)
print(rawlen(t)) --> 3 (actual array length)
print(rawlen("hello")) --> 5
```

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `t` | `table` |  | The table to be referenced. |

**Returns:** `number` — The raw length of the table or string without metamethod invocation.

### rawset

**Signature:** `rawset(t: table, index: Variant, value: Variant): table`

Sets `table[index]` to `value` without invoking the `__newindex`
metamethod. The first argument must be a table, the second is the key
(must not be `nil`), and the third is the value to assign. Returns the
table itself, which allows chained calls when building tables that have a
`__newindex` guard.

This is the complement of [LuaGlobals.rawget()](/docs/reference/engine/globals/LuaGlobals.md) for write
operations; use it when you need to bypass a proxy table's write
interception.

```lua
local log = {}
local proxy = setmetatable({}, {
    __newindex = function(_, k, v)
        table.insert(log, k)
        rawset(proxy, k, v) -- actually store the value
    end
})
rawset(proxy, "x", 42) -- bypasses __newindex; no log entry
proxy.y = 7 -- triggers __newindex; log entry created
print(proxy.x, proxy.y) --> 42  7
print(#log) --> 1 (only "y" was logged)
```

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `t` | `table` |  | The table to be referenced. |
| `index` | `Variant` |  | The index to set in `t` to a specified `value`. Must be different from `nil`. |
| `value` | `Variant` |  | The value to be set to a specified `index` in table `t`. |

**Returns:** `table` — The table `t` that was passed in, allowing chained calls.

### require

**Signature:** `require(module: ModuleScript | string | number): Variant`

Runs the supplied [ModuleScript](/docs/reference/engine/classes/ModuleScript.md) and returns what the
[ModuleScript](/docs/reference/engine/classes/ModuleScript.md) returned (usually a table or a function). If the
[ModuleScript](/docs/reference/engine/classes/ModuleScript.md) has not been run yet, it will be executed.

If a string path is provided instead, it is first resolved to a
[ModuleScript](/docs/reference/engine/classes/ModuleScript.md) relative to the script that called
[LuaGlobals.require()](/docs/reference/engine/globals/LuaGlobals.md), mimicking the Unix-like semantics of Luau's
`require()` expression.

Specifically, require-by-string's resolution semantics are as follows:

- Paths with the `./` prefix begin resolution at `script.Parent`.
- Paths with the `../` prefix begin resolution at `script.Parent.Parent`.
- Paths with the `@self/` prefix begin resolution at `script`.
- Paths with the `@game/` prefix begin resolution at `game`.
- Each non-prefix component in a given path corresponds to a child
  instance of the previous component. The exception to this is the `..`
  component, which corresponds to the parent of the previous component.
- If the desired [ModuleScript](/docs/reference/engine/classes/ModuleScript.md) is not present at the time that
  [LuaGlobals.require()](/docs/reference/engine/globals/LuaGlobals.md) is called, the call will fail and throw an
  error. In other words, require-by-string is non-blocking: it does not
  implicitly wait for a [ModuleScript](/docs/reference/engine/classes/ModuleScript.md) to be created.

To illustrate this, each pair of [LuaGlobals.require()](/docs/reference/engine/globals/LuaGlobals.md) expressions
in the example below contains two functionally equivalent calls. Redundant
parentheses have been added to clarify exactly how each path component
maps onto an instance.

Once the return object is created by an **initial**
[LuaGlobals.require()](/docs/reference/engine/globals/LuaGlobals.md) call of a [ModuleScript](/docs/reference/engine/classes/ModuleScript.md), future
[LuaGlobals.require()](/docs/reference/engine/globals/LuaGlobals.md) calls for the same [ModuleScript](/docs/reference/engine/classes/ModuleScript.md) (on
the same side of the client-server boundary) will not run the code again.
Instead, a reference to the **same** return object created by the initial
[LuaGlobals.require()](/docs/reference/engine/globals/LuaGlobals.md) call will be supplied. This behavior allows
for the sharing of values across different scripts, as multiple
[LuaGlobals.require()](/docs/reference/engine/globals/LuaGlobals.md) calls from different scripts will reference
the same returned object. If the returned object is a table, any values
stored within the table are shared and accessible by any script requiring
that [ModuleScript](/docs/reference/engine/classes/ModuleScript.md).

As noted above, the "object sharing" behavior does not cross the
client-server boundary. This means that if a [ModuleScript](/docs/reference/engine/classes/ModuleScript.md) is
accessible to both the client **and** server (such as by being placed in
[ReplicatedStorage](/docs/reference/engine/classes/ReplicatedStorage.md)) and [LuaGlobals.require()](/docs/reference/engine/globals/LuaGlobals.md) is called
from both a [LocalScript](/docs/reference/engine/classes/LocalScript.md) as well as a [Script](/docs/reference/engine/classes/Script.md), the code in
the [ModuleScript](/docs/reference/engine/classes/ModuleScript.md) will be run twice, and the [LocalScript](/docs/reference/engine/classes/LocalScript.md)
will receive a distinct return object from the one received by the
[Script](/docs/reference/engine/classes/Script.md).

Also note that if the [ModuleScript](/docs/reference/engine/classes/ModuleScript.md) the user wants to run has been
uploaded to Roblox (with the instance's name being `MainModule`), it can
be loaded by using the [LuaGlobals.require()](/docs/reference/engine/globals/LuaGlobals.md) function on the asset
ID of the [ModuleScript](/docs/reference/engine/classes/ModuleScript.md), though only on the server.

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `module` | `ModuleScript | string | number` |  | The [ModuleScript](/docs/reference/engine/classes/ModuleScript.md) that will be executed to retrieve the return value it provides, or a reference to one (a string path or asset ID). |

**Returns:** `Variant` — What the [ModuleScript](/docs/reference/engine/classes/ModuleScript.md) returned (usually a table or a
function).

**Require Module Resolution**

Demonstrates the `require` global.

```lua
-- "./" prefix is equivalent to script.Parent
require("./MySibling")
require((script.Parent).MySibling)

-- "../" prefix is equivalent to script.Parent.Parent
require("../SiblingOfMyParent")
require((script.Parent.Parent).SiblingOfMyParent)

-- "../" can be chained to go up multiple levels
require("../../SiblingOfMyGrandparent")
require((script.Parent.Parent).Parent.SiblingOfMyGrandparent)

-- "@self" prefix corresponds to the script itself
require("@self/MyChild")
require((script).MyChild)

-- "@game" prefix corresponds to the DataModel root
require("@game/ReplicatedStorage/Shared/MyModule")
require((game).ReplicatedStorage.Shared.MyModule)
```

### select

**Signature:** `select(index: Variant, args: Tuple): Tuple`

Returns all arguments after argument number `index`. If negative, it will
return from the end of the argument list.

If the `index` argument is set to `"#"`, the number of arguments that were
passed after it is returned.

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `index` | `Variant` |  | The index of the argument to return all arguments after in `args`. If it's set to `"#"`, the number of arguments that were passed after it is returned. |
| `args` | `Tuple` |  | A tuple of arguments. |

**Returns:** `Tuple` — All arguments after position `index`, or the count of arguments if
`index` is `"#"`.

**Select**

Demonstrates the `select` global.

```lua
print(select(2, "A", "B", "C")) --> B C
print(select(-1, "A", "B", "C")) --> C
print(select("#", "A", "B", "C")) --> 3
```

### setmetatable

**Signature:** `setmetatable(t: table, newMeta: Variant): table`

Sets the metatable for the given table `t` to `newMeta`. If `newMeta` is
`nil`, the metatable of `t` is removed. Finally, this function returns the
table `t` which was passed to it. If `t` already has a metatable whose
`__metatable` metamethod is set, calling this on `t` raises an error.

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `t` | `table` |  | The table to set the metatable of. |
| `newMeta` | `Variant` |  | If `nil`, the metatable of the given table `t` is removed. Otherwise, the metatable to set for the given table `t`. |

**Returns:** `table` — The table `t` that was passed in, with its metatable now set to
`newMeta`.

**Setmetatable**

Demonstrates the `setmetatable` global.

```lua
local meta = {__metatable = "protected"}
local t = {}
setmetatable(t, meta) -- This sets the metatable of t
-- We now have a table, t, with a metatable. If we try to change it...
local ok, err = pcall(setmetatable, t, {})
assert(not ok and err:find("protected")) -- Error: cannot change a protected metatable
```

### tonumber

**Signature:** `tonumber(arg: Variant, base?: int): Variant`

Attempts to convert the arg into a number with a specified base to
interpret the value in. If it cannot be converted, this function returns
`nil`.

The base may be any integer between 2 and 36, inclusive. In bases above
10, the letter 'A' (in either upper or lower case) represents 10, 'B'
represents 11, and so forth, with 'Z' representing 35. In base 10 (the
default), the number may have a decimal part, as well as an optional
exponent part. In other bases, only unsigned integers are accepted.

If a string begins with `0x` and a base is not provided, the `0x` is
trimmed and the base is assumed to be 16, or hexadecimal.

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `arg` | `Variant` |  | The object to be converted into a number. |
| `base` | `int` | `10` | The numerical base to convert `arg` into. |

**Returns:** `Variant` — The numeric value of `arg` in the given base, or `nil` if conversion
is not possible.

**Tonumber**

Demonstrates the `tonumber` global.

```lua
print(tonumber("1337")) --> 1337 (assumes base 10, decimal)
print(tonumber("1.25")) --> 1.25 (base 10 may have decimal portions)
print(tonumber("3e2")) --> 300 (base 10 may have exponent portion, 3 &times; 10 ^ 2)
print(tonumber("25", 8)) --> 21 (base 8, octal)
print(tonumber("0x100")) --> 256 (assumes base 16, hexadecimal)
print(tonumber("roblox")) --> nil (does not raise an error)
-- Tip: use with assert if you would like unconvertable numbers to raise an error
local ok, err = pcall(function() assert(tonumber("roblox")) end)
print(ok and "Success" or "Error: " .. tostring(err)) --> Error: assertion failed
```

### tostring

**Signature:** `tostring(e: Variant): string`

Receives an argument of any type and converts it to a string in a
reasonable format. For complete control of how numbers are converted, use
string.format. If the metatable of `e` has a `__tostring` metamethod, then
it will be called with `e` as the only argument and will return the
result.

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `e` | `Variant` |  | The object to be converted into a string. |

**Returns:** `string` — A string representation of `e`, using the `__tostring` metamethod if
available.

**Tostring**

Demonstrates the `tostring` global.

```lua
local isRobloxCool = true
-- Convert the boolean to a string then concatenate:
print("Roblox is cool: " .. tostring(isRobloxCool)) --> Roblox is cool: true
```

### type

**Signature:** `type(v: Variant): string`

Returns the type of its only argument, coded as a string. The possible
results of this function are `"nil"` (a string, not the value nil),
`"number"`, `"string"`, `"boolean"`, `"table"`, `"vector"`, `"function"`,
`"thread"`, `"userdata"`, and `"buffer"`. The `buffer` and `vector`
primitives are additions from Luau, not from Lua.

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `v` | `Variant` |  | The object to return the type of. |

**Returns:** `string` — The basic type name of `v` as a string (e.g. `"number"`, `"string"`,
`"table"`).

### unpack

**Signature:** `unpack(list: table, i?: int, j?: int): Variant`

Returns the elements from the given `list` as separate return values,
equivalent to `list[i], list[i+1], ..., list[j]`. By default, `i` is `1`
and `j` is the length of `list` (as defined by the `#` operator). If the
range is empty (`i > j`), no values are returned. An error is raised if
the requested range is too large to fit on the stack.

```lua
local t = {10, 20, 30, 40, 50}
print(unpack(t)) --> 10  20  30  40  50
print(unpack(t, 2, 4)) --> 20  30  40

-- Common pattern: forwarding a stored argument list
local args = {1, "hello", true}
someFunction(unpack(args))
```

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `list` | `table` |  | The list of elements to be unpacked. |
| `i` | `int` | `1` | The index of the first element to unpack. |
| `j` | `int` | `#list` | The index of the last element to unpack. |

**Returns:** `Variant` — The elements `list[i]` through `list[j]` as separate return values.

### xpcall

**Signature:** `xpcall(f: function, err: function, args: Tuple): bool, Variant`

This function is similar to [LuaGlobals.pcall()](/docs/reference/engine/globals/LuaGlobals.md), except that you
can set a new error handler.

`xpcall()` calls function `f` in protected mode, using `err` as the error
handler, and passes a list of arguments. Any error inside `f` is not
propagated; instead, `xpcall()` catches the error, calls the `err`
function with the original error object, and returns a status code. Its
first result is the status code (a boolean), which is true if the call
succeeds without errors. In this case, `xpcall()` also returns all results
from the call, after this first result. In case of any error, `xpcall()`
returns false plus the result from `err`.

Unlike [LuaGlobals.pcall()](/docs/reference/engine/globals/LuaGlobals.md), the `err` function preserves the stack
trace of function `f`, which can be inspected using [debug.info()](/docs/reference/engine/globals/debug.md)
or [debug.traceback()](/docs/reference/engine/globals/debug.md).

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `f` | `function` |  | The function to be called in protected mode. |
| `err` | `function` |  | The function to be used as an error handle if xpcall catches an error. |
| `args` | `Tuple` |  | Additional arguments passed to `f` when it is called. |

**Returns:** `bool`, `Variant` — `true` if `f` executed without errors, `false` otherwise. All return values of `f` on success, or the result of
`err(errorObject)` on failure.

### collectgarbage *(deprecated)*

**Signature:** `collectgarbage(operation: string): Variant`

Performs the specified operation of the garbage collector. Note that
Roblox's Luau sandbox only allows the `count` option to be used (the total
memory in use by Luau, in kilobytes), as other options can interfere with
existing processes. Effectively, this makes [LuaGlobals.gcinfo()](/docs/reference/engine/globals/LuaGlobals.md) a
superior alternative that should be used instead.

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `operation` | `string` |  | The name of the operation that should be performed by the garbage collector. |

**Returns:** `Variant` — The result of the garbage collector operation; for the `count` option,
returns the total memory in use in kilobytes.

### getfenv *(deprecated)*

**Signature:** `getfenv(stack?: Variant): table`

> **Deprecated:** This function allows uncontrolled change of the global/function environment and disables script optimizations. Changes to the environment are not tracked by the script analysis tooling and may result in missing or incorrect warnings. As a replacement, consider using [debug.info()](/docs/reference/engine/globals/debug.md) instead.

Returns the current environment in use by the caller, as a dictionary.

- If provided with a function, the environment of the function will be
  returned.
- If provided with an integer, [LuaGlobals.getfenv()](/docs/reference/engine/globals/LuaGlobals.md) will provide
  the environment of the function at the provided stack level: Level 1 is
  the function calling [LuaGlobals.getfenv()](/docs/reference/engine/globals/LuaGlobals.md). If `stack` is `0`,
  [LuaGlobals.getfenv()](/docs/reference/engine/globals/LuaGlobals.md) returns the global environment of the
  current script. When using [LuaGlobals.getfenv()](/docs/reference/engine/globals/LuaGlobals.md) to get the
  current environment of a script, it will return the same table every
  time within the specific thread.

**WARNING:** This function allows uncontrolled change of the
global/function environment and disables script optimizations. Changes to
the environment are not tracked by the script analysis tooling and may
result in missing or incorrect warnings. As a replacement, consider using
[debug.info()](/docs/reference/engine/globals/debug.md) instead.

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `stack` | `Variant` | `1` | The stack level (int) of the environment to be returned; or the function whose environment will be returned. |

**Returns:** `table` — The environment table of the specified function or stack level.

### setfenv *(deprecated)*

**Signature:** `setfenv(f: Variant, fenv: table): Variant`

> **Deprecated:** This function allows uncontrolled change of the global/function environment and disables script optimizations. Changes to the environment are not tracked by the script analysis tooling and may result in missing or incorrect warnings.

Sets the environment to be used by the given function. `f` can be a
function or a number that specifies the function at that stack level:
Level 1 is the function calling `setfenv()`. `setfenv()` returns the given
function.

If `f` is `0`, then `setfenv()` changes the environment of the running
thread and returns no values.

**WARNING:** This function allows uncontrolled change of the
global/function environment and disables script optimizations. Changes to
the environment are not tracked by the script analysis tooling and may
result in missing or incorrect warnings.

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `f` | `Variant` |  | Either a function or a number that specifies the function at that stack level. |
| `fenv` | `table` |  | The function environment table to set for the specified function. |

**Returns:** `Variant` — The function whose environment was set, or no value if `f` is `0`.