---
name: Instance
last_updated: 2026-10-30T19:55:54Z
type: datatype
summary: "Holds the constructor for Instances."
---

# Instance

Holds the constructor for Instances.

**Type:** datatype

## Description

The [Instance](/docs/reference/engine/classes/Instance.md) data type holds constructors for [Instance](/docs/reference/engine/classes/Instance.md)
objects.

## Constructors

### Instance.new

**Signature:** `Instance.new(className: string, parent: Instance?)`

Creates a new [Instance](/docs/reference/engine/classes/Instance.md) of type `className`. Abstract classes and
services cannot be created with this constructor.

Note that when the [Parent](/docs/reference/engine/classes/Instance.md) of an object is set,
Luau listens to a variety of different property changes for replication,
rendering, and physics. For performance reasons, it's recommended to set
the instance's [Parent](/docs/reference/engine/classes/Instance.md) property **last** when
creating new objects, instead of specifying the second argument (`parent`)
of this constructor.

```lua
local Workspace = game:GetService("Workspace")

-- Set new instance's parent last (recommended)
local part = Instance.new("Part")
part.Position = Vector3.new(0, 10, 0)
part.Parent = Workspace

-- Set new instance's parent in constructor (discouraged)
local part = Instance.new("Part", Workspace)
part.Position = Vector3.new(0, 10, 0)
```

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `className` | `string` |  | Class name of the new instance to create. |
| `parent` | `Instance?` |  | Optional object to parent the new instance to. Not recommended for performance reasons (see description above). |

### Instance.fromExisting

**Signature:** `Instance.fromExisting(existingInstance: Instance)`

Creates a new object with the same type and property values as an existing
object. In most cases using [Instance:Clone()](/docs/reference/engine/classes/Instance.md) is more appropriate,
but this constructor is useful when implementing low‑level libraries or
systems.

There are two behavioral differences between this constructor and the
[Instance:Clone()](/docs/reference/engine/classes/Instance.md) method:

- This constructor will not copy any of the descendant
  [Instances](/docs/reference/engine/classes/Instance.md) parented to the existing object.

- This constructor will return a new object even if the existing object
  had [Instance.Archivable](/docs/reference/engine/classes/Instance.md) set to `false`.

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `existingInstance` | `Instance` |  | The existing [Instance](/docs/reference/engine/classes/Instance.md) to copy property values from. |