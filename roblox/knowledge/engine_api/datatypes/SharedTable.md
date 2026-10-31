---
name: SharedTable
last_updated: 2026-10-30T19:55:54Z
type: datatype
summary: "Provides sharable, table-like storage for key/value pairs."
---

# SharedTable

Provides sharable, table-like storage for key/value pairs.

**Type:** datatype

## Description

Represents a table-like data structure that can be shared across execution
contexts. While it can be used for various sorts of general data storage, it
is designed especially for use with
[Parallel Luau](/docs/en-us/scripting/multithreading.md), where it can be used to
share state across scripts parented under different [Actor](/docs/reference/engine/classes/Actor.md) instances.

There are a couple idiomatic ways to communicate shared tables between
scripts. One method is to store and retrieve [SharedTable](/docs/reference/engine/datatypes/SharedTable.md) objects in
the [SharedTableRegistry](/docs/reference/engine/classes/SharedTableRegistry.md). The registry lets any script in the same data
model get or set a [SharedTable](/docs/reference/engine/datatypes/SharedTable.md) by name. Another method is to use
[Actor:SendMessage()](/docs/reference/engine/classes/Actor.md) to send a shared table to another [Actor](/docs/reference/engine/classes/Actor.md)
inside a message.

Like a Luau table, a [SharedTable](/docs/reference/engine/datatypes/SharedTable.md) object stores a set of key-value
element pairs. Unlike a Luau table, only selected types of objects may be
stored in a SharedTable, similar to other restrictions you'll find elsewhere
in the Roblox Engine.

Keys must either be (1) a string or (2) a nonnegative integer number less than
2<sup>32</sup>. Other kinds of keys are not supported.

Values must have one of the following types: Boolean, Number, Vector, String,
[SharedTable](/docs/reference/engine/datatypes/SharedTable.md), or a serializable data type. The ability to store a
[SharedTable](/docs/reference/engine/datatypes/SharedTable.md) as a value in another [SharedTable](/docs/reference/engine/datatypes/SharedTable.md) permits
the construction of nested and recursive data structures.

[SharedTable](/docs/reference/engine/datatypes/SharedTable.md) objects are distinct and different
[SharedTable](/docs/reference/engine/datatypes/SharedTable.md) objects never compare equal, even if they have contents
that would compare equal.

Like a Luau table, a [SharedTable](/docs/reference/engine/datatypes/SharedTable.md) object may be frozen, in which
case it is read-only. An attempt to modify a frozen [SharedTable](/docs/reference/engine/datatypes/SharedTable.md)
will raise an error. A frozen [SharedTable](/docs/reference/engine/datatypes/SharedTable.md) can be created by first
creating a (non-frozen, modifiable) [SharedTable](/docs/reference/engine/datatypes/SharedTable.md) with the desired
contents, and then calling [SharedTable.cloneAndFreeze()](/docs/reference/engine/datatypes/SharedTable.md) to create a
frozen clone of it.

## Code Samples

**Element Access**

Accessing [SharedTable](/docs/reference/engine/datatypes/SharedTable.md) elements with `st[k]` / `st.k` syntax.

```lua
local st = SharedTable.new()
st[1] = "a"
st["x"] = true
st.y = 5

assert(st[1] == "a")
assert(st["x"] == true)
assert(st.x == true)
assert(st["y"] == 5)
assert(st.y == 5)

-- true is not a valid SharedTable key, so attempting to set that key
-- fails:
assert(not pcall(function() st[true] = 100 end))
-- A function is not a valid SharedTable value, so attempting to set a
-- value to a function fails:
assert(not pcall(function() st["f"] = function() end end))
```

**Element Iteration**

Iterating over the elements of a [SharedTable](/docs/reference/engine/datatypes/SharedTable.md) with a `for` loop.

```lua
local st = SharedTable.new({"a", "b", "c"})

for k, v in SharedTable.clone(st, false) do
	print(k, ": ", v)
end

for k, v in st do
	print(k, ": ", v)
end
```

## Constructors

### SharedTable.new

**Signature:** `SharedTable.new()`

Returns a new, empty [SharedTable](/docs/reference/engine/datatypes/SharedTable.md).

```lua
local st = SharedTable.new()
```

### SharedTable.new

**Signature:** `SharedTable.new(t: table)`

Returns a new [SharedTable](/docs/reference/engine/datatypes/SharedTable.md) containing elements equivalent to
those in the provided Luau table.

If the provided Luau table contains any keys or values that cannot be
stored in a [SharedTable](/docs/reference/engine/datatypes/SharedTable.md), construction of the
[SharedTable](/docs/reference/engine/datatypes/SharedTable.md) fails. See the summary at the top of this page for
a list of types of objects that can be stored in a [SharedTable](/docs/reference/engine/datatypes/SharedTable.md).
If the Luau table contains any table as a value, that table is converted
into a new [SharedTable](/docs/reference/engine/datatypes/SharedTable.md).

```lua
local t = {}
t.x = 1
t.y = 2
t.z = {"a", "b", "c"}

local st = SharedTable.new(t)
assert(st.x == 1)
assert(st.y == 2)
assert(st.z[1] == "a")
assert(st.z[2] == "b")
assert(st.z[3] == "c")
```

Note that in some cases it may be desirable to store a
[SharedTable](/docs/reference/engine/datatypes/SharedTable.md) in the [SharedTableRegistry](/docs/reference/engine/classes/SharedTableRegistry.md). The
[ShareTableRegistry:GetSharedTable()](/docs/reference/engine/classes/ShareTableRegistry.md) method provides a convenient
way to accomplish this.

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `t` | `table` |  | The Luau table whose elements are to be stored in the new [SharedTable](/docs/reference/engine/datatypes/SharedTable.md). |

## Functions

### SharedTable.clear

**Signature:** `SharedTable.clear(st: SharedTable): ()`

Atomically removes all of the elements from a [SharedTable](/docs/reference/engine/datatypes/SharedTable.md).

If the [SharedTable](/docs/reference/engine/datatypes/SharedTable.md) is frozen, the operation fails and an error
will be raised.

```lua
local st = SharedTable.new({"a", "b", "c"})
assert(SharedTable.size(st) == 3)

SharedTable.clear(st)
assert(SharedTable.size(st) == 0)
```

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `st` | `SharedTable` |  | The [SharedTable](/docs/reference/engine/datatypes/SharedTable.md) to clear. |

**Returns:** `()`

### SharedTable.clone

**Signature:** `SharedTable.clone(st: SharedTable, deep?: boolean?): SharedTable`

Creates a clone of a [SharedTable](/docs/reference/engine/datatypes/SharedTable.md) and returns the clone.

If the optional `deep` argument is not present, or if it is present and
its value is `false`, then a shallow clone is created. A shallow clone
copies only the top-level [SharedTable](/docs/reference/engine/datatypes/SharedTable.md) object. If any value in
the [SharedTable](/docs/reference/engine/datatypes/SharedTable.md) itself is a [SharedTable](/docs/reference/engine/datatypes/SharedTable.md), then both
the original [SharedTable](/docs/reference/engine/datatypes/SharedTable.md) and the clone [SharedTable](/docs/reference/engine/datatypes/SharedTable.md)
will refer to the same [SharedTable](/docs/reference/engine/datatypes/SharedTable.md).

The shallow clone operation is atomic, so the clone [SharedTable](/docs/reference/engine/datatypes/SharedTable.md)
will contain a consistent snapshot of the state in the original
[SharedTable](/docs/reference/engine/datatypes/SharedTable.md), even if it is being modified concurrently from
other scripts.

If the optional `deep` argument is present and its value is `true`, then a
deep clone is created. A deep clone recursively copies a structure of
[SharedTable](/docs/reference/engine/datatypes/SharedTable.md) objects, such that there is no state shared between
the original [SharedTable](/docs/reference/engine/datatypes/SharedTable.md) and the clone.

The clone of each [SharedTable](/docs/reference/engine/datatypes/SharedTable.md) within the graph of
[SharedTable](/docs/reference/engine/datatypes/SharedTable.md) objects is atomic, but the deep clone as a whole is
not atomic. Thus, the clone of each [SharedTable](/docs/reference/engine/datatypes/SharedTable.md) within the
graph will contain a consistent snapshot of the state of the original
[SharedTable](/docs/reference/engine/datatypes/SharedTable.md) object from which it was cloned, but the states of
different [SharedTable](/docs/reference/engine/datatypes/SharedTable.md) objects may be inconsistent if the graph
is being modified concurrently from other scripts.

The [SharedTable](/docs/reference/engine/datatypes/SharedTable.md) object(s) being cloned may be frozen
(read-only) or not. Regardless, the newly created clones are _not_ frozen
(and are thus modifiable). To create frozen clones, use the
[SharedTable.cloneAndFreeze](/docs/reference/engine/datatypes/SharedTable.md) function.

To illustrate the difference between a shallow clone and a deep clone,
consider the following samples. This first sample creates a shallow clone
and the second creates a deep clone.

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `st` | `SharedTable` |  | The [SharedTable](/docs/reference/engine/datatypes/SharedTable.md) object to clone. |
| `deep` | `boolean?` | `false` | Whether to create a deep clone (`true`) or a shallow clone (`false`). |

**Returns:** `SharedTable`

**Shallow Clone**

Creates a shallow clone of a [SharedTable](/docs/reference/engine/datatypes/SharedTable.md).

```lua
local original = SharedTable.new()
original["a"] = "original a"
original["b"] = "original b"
original["c"] = SharedTable.new()
original["c"]["d"] = "original d"

local clone = SharedTable.clone(original, false)
clone["a"] = "new a"
clone["b"] = "new b"
clone["c"]["d"] = "new d"
assert(original["a"] == "original a")
assert(original["b"] == "original b")

-- Because this was a shallow clone, original["c"] and clone["c"] are
-- the same SharedTable object.
assert(original["c"] == clone["c"])
assert(original["c"]["d"] == "new d")
```

**Deep Clone**

Creates a deep clone of a [SharedTable](/docs/reference/engine/datatypes/SharedTable.md).

```lua
local original = SharedTable.new()
original["a"] = "original a"
original["b"] = "original b"
original["c"] = SharedTable.new()
original["c"]["d"] = "original d"

local clone = SharedTable.clone(original, true)
clone["a"] = "new a"
clone["b"] = "new b"
clone["c"]["d"] = "new d"
assert(original["a"] == "original a")
assert(original["b"] == "original b")

-- Because this was a deep clone, clone["c"] is a clone of original["c"];
-- they are distinct SharedTable objects.
assert(original["c"] ~= clone["c"])
assert(original["c"]["d"] == "original d")
```

### SharedTable.cloneAndFreeze

**Signature:** `SharedTable.cloneAndFreeze(st: SharedTable, deep?: boolean?): SharedTable`

Creates a frozen (read-only) clone of a [SharedTable](/docs/reference/engine/datatypes/SharedTable.md) and returns
the clone. The behavior of this function is the same as the behavior of
clone, except that the clone is frozen.

If a deep clone is requested, then all of the cloned
[SharedTable](/docs/reference/engine/datatypes/SharedTable.md) objects are frozen.

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `st` | `SharedTable` |  | The SharedTable object to clone. |
| `deep` | `boolean?` | `false` | Whether to create a deep clone (`true`) or a shallow clone (`false`). |

**Returns:** `SharedTable`

### SharedTable.increment

**Signature:** `SharedTable.increment(st: SharedTable, key: string | number, delta: number): number`

Atomically increments the value of an element. An element with the
specified key must exist in the [SharedTable](/docs/reference/engine/datatypes/SharedTable.md), and it must be of
type `number`. The specified `delta` is added to the value, and the
original value is returned.

The `SharedTable.update` function can also be used for this purpose; this
`increment` function exists for convenience and performance (in general,
`increment` is much faster than `update`, so it should be preferred where
possible). The following two function calls have the same effect:

```lua
local st = SharedTable.new()
st["x"] = 1

local oldValue = SharedTable.increment(st, "x", 1)

SharedTable.update(st, "x", function(v)
    oldValue = v
    return v + 1
end)
```

If the [SharedTable](/docs/reference/engine/datatypes/SharedTable.md) is frozen, the operation fails and an error
will be raised.

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `st` | `SharedTable` |  | The [SharedTable](/docs/reference/engine/datatypes/SharedTable.md) object to be updated. |
| `key` | `string | number` |  | The key of the element in the [SharedTable](/docs/reference/engine/datatypes/SharedTable.md) object to be updated. |
| `delta` | `number` |  | The value to be added to the element in the [SharedTable](/docs/reference/engine/datatypes/SharedTable.md). |

**Returns:** `number` — The original value of the element, before `delta` was added to it.

**Increment**

Demonstrates usage of [SharedTable.increment()](/docs/reference/engine/datatypes/SharedTable.md).

```lua
local st = SharedTable.new()
st["x"] = 1

local oldValue = SharedTable.increment(st, "x", 1)
assert(oldValue == 1)
assert(st["x"] == 2)

-- The value of the specified key must be a number.  If it is not a
-- number, the call will fail:
st["y"] = "test"
assert(not pcall(function() SharedTable.increment(st, "y", 1) end))
```

### SharedTable.isFrozen

**Signature:** `SharedTable.isFrozen(st: SharedTable): boolean`

Returns `true` if the [SharedTable](/docs/reference/engine/datatypes/SharedTable.md) is frozen (read-only).

```lua
local st1 = SharedTable.new({"a", "b", "c"})
assert(not SharedTable.isFrozen(st1))

local st2 = SharedTable.cloneAndFreeze(st1)
assert(SharedTable.isFrozen(st2))
```

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `st` | `SharedTable` |  | The [SharedTable](/docs/reference/engine/datatypes/SharedTable.md) object whose frozen state is to be queried. |

**Returns:** `boolean`

### SharedTable.size

**Signature:** `SharedTable.size(st: SharedTable): number`

Returns the number of elements stored in the SharedTable. Note that if
other scripts are concurrently modifying the SharedTable, the returned
size may no longer be correct after it is returned, since other scripts
may have added or removed elements from the SharedTable.

```lua
local st = SharedTable.new({"a", "b", "c"})
assert(SharedTable.size(st) == 3)

st[2] = nil
assert(SharedTable.size(st) == 2)
```

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `st` | `SharedTable` |  | The [SharedTable](/docs/reference/engine/datatypes/SharedTable.md) object whose size is to be queried. |

**Returns:** `number`

### SharedTable.update

**Signature:** `SharedTable.update(st: SharedTable, key: string | number, f: function): ()`

Atomically updates the value of an element.

When a [SharedTable](/docs/reference/engine/datatypes/SharedTable.md) is accessed concurrently from scripts
running in different execution contexts, it is possible for their accesses
to interleave unpredictably. Because of this, code like the following is
generally incorrect, because the value may have changed between the read
on the first line and the update on the second line:

```lua
local st = SharedTable.new({ x = "a" })
local oldValue = st["x"]
st["x"] = oldValue .. ",x"
print(st["x"]) --> a,x
```

The update function makes it possible to perform an atomic update to an
element. It takes a function that it will call with the current value of
the element. The function can then compute and return the new value. Note
that the function may be called multiple times if the
[SharedTable](/docs/reference/engine/datatypes/SharedTable.md) is being concurrently modified from other scripts.

If the [SharedTable](/docs/reference/engine/datatypes/SharedTable.md) is frozen, the operation fails and an error
will be raised.

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `st` | `SharedTable` |  | The [SharedTable](/docs/reference/engine/datatypes/SharedTable.md) object to be updated. |
| `key` | `string | number` |  | The key of the element in the [SharedTable](/docs/reference/engine/datatypes/SharedTable.md) object to be updated. |
| `f` | `function` |  | The function that will be called to compute the new value for the element. |

**Returns:** `()`

**Update**

Demonstrates usage of [SharedTable.update()](/docs/reference/engine/datatypes/SharedTable.md).

```lua
local st = SharedTable.new()
st["x"] = "abcd"

SharedTable.update(st, "x", function(v)
	assert(v == "abcd")
	return v .. "e"
end)

assert(st["x"] == "abcde")
```