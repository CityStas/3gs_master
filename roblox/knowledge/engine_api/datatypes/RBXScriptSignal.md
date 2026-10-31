---
name: RBXScriptSignal
last_updated: 2026-10-30T19:55:54Z
type: datatype
summary: "An object that runs connected functions upon a specific occurrence."
---

# RBXScriptSignal

An object that runs connected functions upon a specific occurrence.

**Type:** datatype

## Description

The [RBXScriptSignal](/docs/reference/engine/datatypes/RBXScriptSignal.md) data type, more commonly known as an **Event**,
provides a way for user-defined functions, called **listeners**, to call when
something happens in the game. When an event happens, the
[RBXScriptSignal](/docs/reference/engine/datatypes/RBXScriptSignal.md) fires and calls any listeners that are connected to
it. An [RBXScriptSignal](/docs/reference/engine/datatypes/RBXScriptSignal.md) may also pass arguments to each listener to
provide extra information about the event.

## Methods

### RBXScriptSignal:Connect

**Signature:** `RBXScriptSignal:Connect(func: function): RBXScriptConnection`

Establishes a function to be called when the event fires. Returns an
[RBXScriptConnection](/docs/reference/engine/datatypes/RBXScriptConnection.md) object associated with the connection.

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `func` | `function` |  | The callback function to invoke each time the event fires. |

**Returns:** `RBXScriptConnection` — A connection object that can be used to disconnect the listener from
the event.

### RBXScriptSignal:ConnectParallel

**Signature:** `RBXScriptSignal:ConnectParallel(func: function): RBXScriptConnection`

Establishes a function to be called when the event fires. Returns an
[RBXScriptConnection](/docs/reference/engine/datatypes/RBXScriptConnection.md) object associated with the connection. When
the event fires, the signal callback is executed in a desynchronized
state. Using `ConnectParallel` is similar to, but more efficient than,
using `Connect` followed by a call to [task.desynchronize()](/docs/reference/engine/globals/task.md) in
the signal handler.

Note: Scripts that connect in parallel must be rooted under an Actor.

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `func` | `function` |  | The callback function to invoke when the event fires in a parallel execution context. |

**Returns:** `RBXScriptConnection` — A connection object that can be used to disconnect the listener from
the event.

### RBXScriptSignal:Once

**Signature:** `RBXScriptSignal:Once(func: function): RBXScriptConnection`

Establishes a function to be called when the event fires. Returns an
[RBXScriptConnection](/docs/reference/engine/datatypes/RBXScriptConnection.md) object associated with the connection. The
behavior of `Once` is similar to `Connect`. However, instead of allowing
multiple events to be received by the specified function, only the first
event will be delivered. Using `Once` also ensures that the connection to
the function will be automatically disconnected prior the function being
called.

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `func` | `function` |  | The callback function to invoke the next time the event fires, after which it is automatically disconnected. |

**Returns:** `RBXScriptConnection` — A connection object that can be used to disconnect the listener before
it fires.

### RBXScriptSignal:Wait

**Signature:** `RBXScriptSignal:Wait(): Variant`

Yields the current thread until the signal fires and returns the arguments
provided by the signal.

**Returns:** `Variant` — The arguments passed by the signal when it fires.