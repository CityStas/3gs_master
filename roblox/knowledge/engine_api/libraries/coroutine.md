---
name: coroutine
last_updated: 2026-10-30T19:55:54Z
type: library
summary: "A function that executes alongside the main thread."
---

# coroutine

A function that executes alongside the main thread.

**Type:** library

## Description

A **coroutine** is used to perform multiple tasks at the same time from within
the same script. Such tasks might include producing values from inputs or
performing work on a subroutine when solving a larger problem. A task doesn't
even need to have a defined ending point, but it does need to define
particular times at which it **yields** (pause) to let other things be worked
on.

## Using Coroutines

A new coroutine can be created by providing a function to
[coroutine.create()](/docs/reference/engine/globals/coroutine.md). Once created, a coroutine doesn't begin running
until the first call to [coroutine.resume()](/docs/reference/engine/globals/coroutine.md) which passes the
arguments to the function. This call returns when the function either halts or
calls [coroutine.yield()](/docs/reference/engine/globals/coroutine.md) and, when this happens,
[coroutine.resume()](/docs/reference/engine/globals/coroutine.md) returns either the values returned by the
function, the values sent to [coroutine.yield()](/docs/reference/engine/globals/coroutine.md), or an error message.
If it does error, the second return value is the thrown error.

```lua
local function task(...)
	-- This function might do some work for a bit then yield some value
	coroutine.yield("first")  -- To be returned by coroutine.resume()
	-- The function continues once it is resumed again
	return "second"
end

local taskCoro = coroutine.create(task)
-- Call resume for the first time, which runs the function from the beginning
local success, result = coroutine.resume(taskCoro, ...)
print(success, result)  --> true, first (task called coroutine.yield())
-- Continue running the function until it yields or halts
success, result = coroutine.resume(taskCoro)
print(success, result)  --> true, second (task halted because it returned "second")
```

During the lifetime of the coroutine, you can call
[coroutine.status()](/docs/reference/engine/globals/coroutine.md) to inspect its status:

| Status | Meaning |
| --- | --- |
| **suspended** | The coroutine is waiting to be resumed. Coroutines begin in this state and enter it when their function calls `coroutine.yield()`. |
| **running** | The coroutine is running right now. |
| **normal** | The coroutine is awaiting the yield of another coroutine; in other words, it has resumed another coroutine. |
| **dead** | The function has halted (returned or thrown an error). The coroutine cannot be used further. |

### Wrapping Coroutines

When working with coroutines, you can also forgo the use of the coroutine
object and instead use a wrapper function. Such a wrapper function will resume
a particular coroutine when it is called and will return only the yielded
values. You can do this using [coroutine.wrap()](/docs/reference/engine/globals/coroutine.md):

```lua
-- A simple coroutine body that returns a value
local function task()
	return "done"
end

-- Create coroutine and return a wrapper function that resumes it
local f = coroutine.wrap(task)
-- Resume the coroutine as if we called coroutine.resume()
local result = f()
print(result) --> done
-- If an error occurs it will be raised here!
-- This differs from coroutine.resume() which acts similar to pcall()
```

The first value returned from [coroutine.resume()](/docs/reference/engine/globals/coroutine.md) describes whether a
coroutine ran without errors. However, functions returned by
[coroutine.wrap()](/docs/reference/engine/globals/coroutine.md) will not do this: instead they directly return the
values returned or passed to [coroutine.yield()](/docs/reference/engine/globals/coroutine.md), if any. Should an
error have occurred while running the coroutine function, the error is raised
on the call of the returned function.

### Producer Pattern Example

Imagine a task that produces repetitions of a word: each time it produces a
repetition, the next one will produce one more. For example, providing `Hello`
will produce `Hello`, `HelloHello`, `HelloHelloHello`, etc. To do this, you
can define `repeatThis()`:

```lua
-- This function repeats a word every time its coroutine is resumed
local function repeatThis(word)
	local repetition = ""
	while true do
		-- Do one repetition then yield the result
		repetition = repetition .. word
		coroutine.yield(repetition)
	end
end
```

To run this function as a coroutine, you can use [coroutine.create()](/docs/reference/engine/globals/coroutine.md)
followed by multiple calls to [coroutine.resume()](/docs/reference/engine/globals/coroutine.md):

```lua
local function repeatThis(word)
	local repetition = ""
	while true do
		repetition = repetition .. word
		coroutine.yield(repetition)
	end
end

local repetitionCoro = coroutine.create(repeatThis)
print(coroutine.resume(repetitionCoro, "Hello"))  -- true, Hello
print(coroutine.resume(repetitionCoro))           -- true, HelloHello
print(coroutine.resume(repetitionCoro))           -- true, HelloHelloHello
```

For this producer function, you can also use [coroutine.wrap()](/docs/reference/engine/globals/coroutine.md) to get
a function that produces values:

```lua
local function repeatThis(word)
	local repetition = ""
	while true do
		repetition = repetition .. word
		coroutine.yield(repetition)
	end
end

local f = coroutine.wrap(repeatThis)
print(f("Hello"))  -- Hello
print(f())         -- HelloHello
print(f())         -- HelloHelloHello
```

## Functions

### coroutine.close

**Signature:** `coroutine.close(co: thread): bool, Variant<string, void>`

Closes and puts the provided coroutine in a dead state. This function
returns `true` unless the coroutine is in an error state, in which case it
returns `false` and the error message. A coroutine that is currently
running cannot be closed. A coroutine cannot be resumed after it is
closed.

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `co` | `thread` |  | The coroutine thread to close. |

**Returns:** `bool`, `Variant<string, void>` — `true` unless the coroutine being closed is in an error state. The error message, if any.

### coroutine.create

**Signature:** `coroutine.create(f: function): thread`

Creates a new coroutine with body `f`, which must be a Luau function, and
returns it as a `thread`. The returned coroutine starts in the `suspended`
state and does not begin executing until [coroutine.resume()](/docs/reference/engine/globals/coroutine.md) is
called on it. The arguments passed to the first
[coroutine.resume()](/docs/reference/engine/globals/coroutine.md) call are forwarded as the arguments to `f`.

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `f` | `function` |  | The Luau function to use as the coroutine body. |

**Returns:** `thread` — A new coroutine in the suspended state, ready to be resumed.

### coroutine.finally

**Signature:** `coroutine.finally(co: thread, callback: Variant)`

Registers `callback` on coroutine `co` that will be called when `co`
reaches a terminal state. The callback is called with a status string and
a set of values:

- `callback("finished", ...results)`. The coroutine function returned. All
  result values are forwarded to the callback.
- `callback("error", err)`. The coroutine terminated with an error. The
  error value is passed as the only additional argument.
- `callback("cancelled")`. [coroutine.close()](/docs/reference/engine/globals/coroutine.md) or
  [task.cancel()](/docs/reference/engine/globals/task.md) was called on the coroutine. The coroutine did
  not complete its work. No extra values are provided.

Callbacks run at most once, in reverse registration order (LIFO).

When the coroutine reaches a terminal state during the invocation of
[coroutine.resume()](/docs/reference/engine/globals/coroutine.md) or [coroutine.close()](/docs/reference/engine/globals/coroutine.md), those
functions will return only after callbacks complete their work. Callbacks
are invoked on the calling thread and may yield. If a callback errors,
remaining callbacks in the list are not invoked and `false` status with
the callback error is returned.

Attempting to register a callback on a dead coroutine raises an error.

If a coroutine reaches a terminal state in a resume through
[coroutine.wrap()](/docs/reference/engine/globals/coroutine.md) closure and has callbacks registered, it raises
a "cannot run finalizers from a wrapped coroutine" error. A coroutine can
also reach the terminal state when it is being resumed by the engine or
closed with [task.cancel()](/docs/reference/engine/globals/task.md); in this case, callbacks are executed
on a separate thread with errors reported as script errors.

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `co` | `thread` |  | The coroutine thread to observe. |
| `callback` | `Variant` |  | Function or a callable object to invoke. |

### coroutine.isyieldable

**Signature:** `coroutine.isyieldable(): bool`

Returns `true` if the coroutine this function is called within can safely
yield. Yielding a coroutine inside metamethods or C functions is
prohibited, with the exception of `pcall` and `xpcall`.

**Returns:** `bool` — Whether or not the coroutine can safely yield at this point.

### coroutine.resume

**Signature:** `coroutine.resume(co: thread, ...: Variant): bool, Variant<Tuple, string>`

Starts or continues the execution of coroutine `co`. The first time you
resume a coroutine, it starts running its body. The values `...` are
passed as the arguments to the body function. If the coroutine has
yielded, resume restarts it; the values `...` are passed as the results
from the yield. If the coroutine runs without any errors, resume returns
true plus any values passed to yield (if the coroutine yields) or any
values returned by the body function (if the coroutine terminates). If
there is any error, resume returns false plus the error message.

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `co` | `thread` |  | The coroutine thread to resume. |
| `...` | `Variant` |  | Arguments passed to the coroutine body function (on first resume) or returned from `coroutine.yield()` inside the coroutine (on subsequent resumes). |

**Returns:** `bool`, `Variant<Tuple, string>` — `true` if the coroutine ran without errors, `false` if an error
occurred. The values passed to `coroutine.yield()` or returned by the body
function on success, or the error message on failure.

### coroutine.running

**Signature:** `coroutine.running(): thread`

Returns the currently running coroutine as a `thread` value, or `nil` if
called from the main thread. The main thread is not considered a
coroutine, so only threads created by [coroutine.create()](/docs/reference/engine/globals/coroutine.md) or
[coroutine.wrap()](/docs/reference/engine/globals/coroutine.md) are returned by this function.

**Returns:** `thread` — The currently running coroutine, or `nil` if called from the main
thread.

### coroutine.status

**Signature:** `coroutine.status(co: thread): string`

Returns the status of coroutine co, as a string: 'running', if the
coroutine is running (that is, it called status); 'suspended', if the
coroutine is suspended in a call to yield, or if it has not started
running yet; 'normal' if the coroutine is active but not running (that is,
it has resumed another coroutine); and 'dead' if the coroutine has
finished its body function, or if it has stopped with an error.

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `co` | `thread` |  | The coroutine thread to query. |

**Returns:** `string` — One of `"running"`, `"suspended"`, `"normal"`, or `"dead"`.

### coroutine.wrap

**Signature:** `coroutine.wrap(f: function): function`

Creates a new coroutine, with body f. f must be a Luau function. Returns a
function that resumes the coroutine each time it is called. Any arguments
passed to the function behave as the extra arguments to resume. Returns
the same values returned by resume, except the first boolean. In case of
error, propagates the error.

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `f` | `function` |  | The Luau function to use as the coroutine body. |

**Returns:** `function` — A wrapper function that resumes the coroutine each time it is called,
returning the yielded or returned values directly (without the boolean
status). Raises an error if the coroutine errors.

### coroutine.yield

**Signature:** `coroutine.yield(...: Tuple): Tuple<Variant>`

Suspends the execution of the calling coroutine. Any arguments to yield
are passed as extra results to resume. Yielding a coroutine inside
metamethods or C functions is prohibited, with the exception of `pcall`
and `xpcall`.

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `...` | `Tuple` |  | Values to return as additional results from the corresponding `coroutine.resume()` call. |

**Returns:** `Tuple<Variant>` — The arguments passed to the next `coroutine.resume()` call that
continues this coroutine.