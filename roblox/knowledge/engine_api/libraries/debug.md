---
name: debug
last_updated: 2026-10-30T19:55:54Z
type: library
summary: "This library provides functions useful for debugging and profiling code."
---

# debug

This library provides functions useful for debugging and profiling code.

**Type:** library

## Description

Provides a few basic functions for debugging code in Roblox. Unlike the
[debug](/docs/reference/engine/globals/debug.md) library found in Lua natively, this version has been heavily
sandboxed.

## Functions

### debug.traceback

**Signature:** `debug.traceback(message: string, level?: number): string`

Returns a traceback of the current function call stack as a string; in
other words, a description of the functions that have been called up to
this point. During debugging, this behaves like an error stack trace but
does not stop execution of the script.

The `level` parameter specifies what level of the call stack to consider,
with `1` being the call of [debug.traceback()](/docs/reference/engine/globals/debug.md) itself, `2` being
the call of the function calling [debug.traceback()](/docs/reference/engine/globals/debug.md), and so on.
See the code sample below for an example of sequential function calls.

Note that this function will often return inaccurate results (compared to
the original source code) and that the format of the returned traceback
may change at any time. You should **not** parse the return value for
specific information such as script names or line numbers.

The following example includes sequential function calls; `fnB()` is
called, and it calls `fnA()` which then calls [debug.traceback()](/docs/reference/engine/globals/debug.md).

```lua
local function fnA()
	print(debug.traceback("Specific moment during fnA()"))
end

local function fnB()
	fnA()
end

-- Call function fnB() to begin traceback
fnB()
```

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `message` | `string` |  | The first line of the returned string. |
| `level` | `number` | `1` | The number of calls "up" the call stack to return. |

**Returns:** `string` — Traceback of the current function call stack.

### debug.traceback

**Signature:** `debug.traceback(thread: thread, message: string, level?: number): string`

Returns a traceback of the current function call stack as a string; in
other words, a description of the functions that have been called up to
this point. During debugging, this behaves like an error stack trace but
does not stop execution of the script.

The `level` parameter specifies what level of the call stack to consider,
with `1` being the call of [debug.traceback()](/docs/reference/engine/globals/debug.md) itself, `2` being
the call of the function calling [debug.traceback()](/docs/reference/engine/globals/debug.md), and so on.
See the code sample below for an example of sequential function calls.

Note that this function will often return inaccurate results (compared to
the original source code) and that the format of the returned traceback
may change at any time. You should **not** parse the return value for
specific information such as script names or line numbers.

The following example includes sequential function calls; `fnB()` is
called, and it calls `fnA()` which then calls [debug.traceback()](/docs/reference/engine/globals/debug.md).

```lua
local function fnA()
	print(debug.traceback("Specific moment during fnA()"))
end

local function fnB()
	fnA()
end

-- Call function fnB() to begin traceback
fnB()
```

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `thread` | `thread` |  | A thread as returned by [coroutine.create()](/docs/reference/engine/globals/coroutine.md). |
| `message` | `string` |  | The first line of the returned string. |
| `level` | `number` | `1` | The number of calls "up" the call stack to return. |

**Returns:** `string` — Traceback of the current function call stack.

### debug.info

**Signature:** `debug.info(level: number, options: string): Tuple`

Allows programmatic inspection of the call stack. This function differs
from [debug.traceback()](/docs/reference/engine/globals/debug.md) in that it guarantees the format of the
data it returns. This is useful for general logging and filtering purposes
as well as for sending the data to systems expecting structured input,
such as crash aggregation.

```lua
local function fnA()
	-- Output source identifier ("s") and line ("l") at levels 1 and 2
	print(debug.info(1, "sl"))  --> fnA() 3
	print(debug.info(2, "sl"))  --> fnA() 7
end

fnA()
```

Note that this function is similar to
[debug.getinfo](https://www.lua.org/pil/23.1.html), an unavailable part of
the standard Lua library which serves a similar purpose.

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `level` | `number` |  | Determines at what level of the call stack the information returned should describe. A value of `1` represents the function which is calling [debug.info()](/docs/reference/engine/globals/debug.md), a value of `2` represents the function that called that function, and so on. |
| `options` | `string` |  | A string that describes what the returned information should represent. It must only contain 0 or 1 instances of the characters `slnaf`, each representing a piece of information:  - `s` ([string](/docs/en-us/luau/strings.md)) — The function source identifier,   equal to the full name of the script the function is defined in. - `l` ([number](/docs/en-us/luau/numbers.md)) — The line number of the function   call represented by `level`. - `n` ([string](/docs/en-us/luau/strings.md)) — The name of the function; may be   `nil` for anonymous functions and C functions without an assigned   debug name. - `a` ([number](/docs/en-us/luau/numbers.md), [boolean](/docs/en-us/luau/booleans.md)) —   Arity of the function, which refers to the parameter count and   whether the function is variadic. - `f` ([function](/docs/en-us/luau/functions.md)) — The function which was   inspected. |

**Returns:** `Tuple` — One value per character in `options`, in the order they appear: source
identifier (`s`), line number (`l`), function name (`n`), parameter
count and whether variadic (`a`), or the function itself (`f`).

### debug.info

**Signature:** `debug.info(function: function, options: string): Tuple`

Allows programmatic inspection of the call stack. This function differs
from [debug.traceback()](/docs/reference/engine/globals/debug.md) in that it guarantees the format of the
data it returns. This is useful for general logging and filtering purposes
as well as for sending the data to systems expecting structured input,
such as crash aggregation.

```lua
local function fnA()

end

local function fnB()

end

-- Output line ("l"), name ("n"), and identifier ("f") for both fnA() and fnB()
print(debug.info(fnA, "lnf"))  --> 1 fnA function: 0x75e3d3c398a81252
print(debug.info(fnB, "lnf"))  --> 5 fnB function: 0x6022a6dc5ccf4ab2
```

Note that this function is similar to
[debug.getinfo](https://www.lua.org/pil/23.1.html), an unavailable part of
the standard Lua library which serves a similar purpose.

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `function` | `function` |  | The function of the call stack which the information returned should describe. |
| `options` | `string` |  | A string that describes what the returned information should represent. It must only contain 0 or 1 instances of the characters `slnaf`, each representing a piece of information:  - `s` ([string](/docs/en-us/luau/strings.md)) — The function source identifier,   equal to the full name of the script the function is defined in. - `l` ([number](/docs/en-us/luau/numbers.md)) — The line that `function` is   defined on. - `n` ([string](/docs/en-us/luau/strings.md)) — The name of the function; may be   `nil` for anonymous functions and C functions without an assigned   debug name. - `a` ([number](/docs/en-us/luau/numbers.md), [boolean](/docs/en-us/luau/booleans.md)) —   Arity of the function, which refers to the parameter count and   whether the function is variadic. - `f` ([function](/docs/en-us/luau/functions.md)) — The function which was   inspected. |

**Returns:** `Tuple` — One value per character in `options`, in the order they appear: source
identifier (`s`), line number (`l`), function name (`n`), parameter
count and whether variadic (`a`), or the function itself (`f`).

### debug.info

**Signature:** `debug.info(thread: thread, level: number, options: string): Tuple`

Allows programmatic inspection of the call stack. This function differs
from [debug.traceback()](/docs/reference/engine/globals/debug.md) in that it guarantees the format of the
data it returns. This is useful for general logging and filtering purposes
as well as for sending the data to systems expecting structured input,
such as crash aggregation.

```lua
local function fnA()
	-- Output source identifier ("s") and line ("l") at levels 1 and 2
	print(debug.info(1, "sl"))  --> fnA() 3
	print(debug.info(2, "sl"))  --> fnA() 7
end

fnA()
```

Note that this function is similar to
[debug.getinfo](https://www.lua.org/pil/23.1.html), an unavailable part of
the standard Lua library which serves a similar purpose.

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `thread` | `thread` |  | A thread as returned by [coroutine.create()](/docs/reference/engine/globals/coroutine.md). |
| `level` | `number` |  | Determines at what level of the call stack the information returned should describe. A value of `1` represents the function which is calling [debug.info()](/docs/reference/engine/globals/debug.md), a value of `2` represents the function that called that function, and so on. |
| `options` | `string` |  | A string that describes what the returned information should represent. It must only contain 0 or 1 instances of the characters `slnaf`, each representing a piece of information:  - `s` ([string](/docs/en-us/luau/strings.md)) — The function source identifier,   equal to the full name of the script the function is defined in. - `l` ([number](/docs/en-us/luau/numbers.md)) — The line number of the function   call represented by `level`. - `n` ([string](/docs/en-us/luau/strings.md)) — The name of the function; may be   `nil` for anonymous functions and C functions without an assigned   debug name. - `a` ([number](/docs/en-us/luau/numbers.md), [boolean](/docs/en-us/luau/booleans.md)) —   Arity of the function, which refers to the parameter count and   whether the function is variadic. - `f` ([function](/docs/en-us/luau/functions.md)) — The function which was   inspected. |

**Returns:** `Tuple` — One value per character in `options`, in the order they appear: source
identifier (`s`), line number (`l`), function name (`n`), parameter
count and whether variadic (`a`), or the function itself (`f`).

### debug.profilebegin

**Signature:** `debug.profilebegin(label: string): ()`

Starts profiling for a
[MicroProfiler](/docs/en-us/performance-optimization/microprofiler.md) label.

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `label` | `string` |  | The text that this [MicroProfiler](/docs/en-us/performance-optimization/microprofiler.md) label displays. |

**Returns:** `()`

### debug.profileend

**Signature:** `debug.profileend(): ()`

Stops profiling for the most recent
[MicroProfiler](/docs/en-us/performance-optimization/microprofiler.md) label
that [debug.profilebegin()](/docs/reference/engine/globals/debug.md) opened.

**Returns:** `()`

### debug.getmemorycategory

**Signature:** `debug.getmemorycategory(): string`

Returns the name of the current thread's active memory category.

**Returns:** `string` — The current thread's active memory category.

### debug.setmemorycategory

**Signature:** `debug.setmemorycategory(tag: string): string`

Assigns a custom tag name to the current thread's memory category in the
[Developer Console](/docs/en-us/studio/developer-console.md). Useful for analyzing
memory usage of multiple threads in the same script which would otherwise
be grouped together under the same tag/name. Returns the name of the
current thread's previous memory category.

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `tag` | `string` |  | The custom name to assign to the current thread's memory category in the Developer Console. |

**Returns:** `string` — The current thread's previous memory category.

### debug.resetmemorycategory

**Signature:** `debug.resetmemorycategory(): ()`

Resets the tag assigned by [debug.setmemorycategory()](/docs/reference/engine/globals/debug.md) to the
automatically assigned value (typically, the script name).

**Returns:** `()`

### debug.dumpcodesize

**Signature:** `debug.dumpcodesize(): ()`

Displays a table of native code size of individual functions and scripts.
This function is only available in the Command Bar in Studio. More details
can be found on the [Native Code Generation](/docs/en-us/luau/native-code-gen.md)
page.

**Returns:** `()`