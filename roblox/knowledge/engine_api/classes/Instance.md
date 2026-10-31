---
name: Instance
last_updated: 2026-10-30T19:55:52Z
inherits:
  - Object
type: class
memory_category: Instances
tags:
  - NotCreatable
  - NotBrowsable
summary: "`Instance` is the base class for all classes in the Roblox class hierarchy which can be part of the DataModel tree."
---

# Class: Instance

> `Instance` is the base class for all classes in the Roblox class hierarchy
> which can be part of the [DataModel](/docs/reference/engine/classes/DataModel.md) tree.

## Description

`Instance` is the base class for all classes in the Roblox class hierarchy
which can be part of the [DataModel](/docs/reference/engine/classes/DataModel.md) tree.

It is not possible to directly create root `Instance` objects, but the special
[Instance.new()](/docs/reference/engine/datatypes/Instance.md) constructor creates objects via code, taking the
name of the class as a parameter and returning the created object.

## Properties

### Property: Instance.Archivable

```json
{
  "type": "boolean",
  "access": "ReadWrite",
  "security": {
    "read": "None",
    "write": "None"
  },
  "serialization": {
    "can_load": false,
    "can_save": false
  },
  "thread_safety": "ReadSafe",
  "category": "Behavior"
}
```

This property determines whether the instance should be included when the
experience is published or saved, or when [Clone()](/docs/reference/engine/classes/Instance.md)
is called on one of the instance's ancestors. Calling
[Clone()](/docs/reference/engine/classes/Instance.md) directly on an instance will return `nil`
if that instance is **not** [Archivable](/docs/reference/engine/classes/Instance.md).

Copying an object in Studio using the **Duplicate** or **Copy**/**Paste**
options will ignore its own [Archivable](/docs/reference/engine/classes/Instance.md)
property and set [Archivable](/docs/reference/engine/classes/Instance.md) to `true` for the
copy.

**Archivable**

Demonstrates [Instance.Archivable](/docs/reference/engine/classes/Instance.md).

```lua
local part = Instance.new("Part")
print(part:Clone())  --> Part
part.Archivable = false
print(part:Clone())  --> nil
```

### Property: Instance.Capabilities

```json
{
  "type": "SecurityCapabilities",
  "access": "ReadWrite",
  "security": {
    "read": "None",
    "write": "None"
  },
  "serialization": {
    "can_load": true,
    "can_save": true
  },
  "thread_safety": "ReadSafe",
  "category": "Permissions",
  "capabilities": [
    "CapabilityControl"
  ]
}
```

The set of capabilities allowed to be used for scripts inside this
instance. For the capabilities to take effect, [Instance.Sandboxed](/docs/reference/engine/classes/Instance.md)
property must be enabled.

This property is used by an experimental feature. See
[script capabilities](/docs/en-us/scripting/capabilities.md) for further
details.

### Property: Instance.IsInSandbox

```json
{
  "type": "boolean",
  "access": "ReadWrite",
  "security": {
    "read": "None",
    "write": "None"
  },
  "serialization": {
    "can_load": false,
    "can_save": false
  },
  "thread_safety": "ReadSafe",
  "category": "Permissions"
}
```

This read-only property returns `true` if the instance is contained within
a sandboxed container — that is, if the instance itself or any of its
ancestors has [Instance.Sandboxed](/docs/reference/engine/classes/Instance.md) enabled. Otherwise it returns
`false`.

This property is not scriptable and is only visible in Studio's Properties
window. See [script capabilities](/docs/en-us/scripting/capabilities.md) for
further details.

### Property: Instance.Name

```json
{
  "type": "string",
  "access": "ReadWrite",
  "security": {
    "read": "None",
    "write": "None"
  },
  "serialization": {
    "can_load": true,
    "can_save": true
  },
  "thread_safety": "ReadSafe",
  "category": "Data"
}
```

A non-unique identifier of the [Instance](/docs/reference/engine/classes/Instance.md). Names are used to keep
the object hierarchy organized, along with allowing scripts to access
specific objects. The name of an instance cannot exceed 100 characters in
size.

The name of an object is often used to access the object through the data
model hierarchy using the following methods:

```
local Workspace = game:GetService("Workspace")

local baseplate = Workspace.Baseplate
local baseplate = Workspace["Baseplate"]
local baseplate = Workspace:FindFirstChild("BasePlate")
```

In order to make an object accessible using the dot operator (`.`), its
name must start with an underscore or letter, and the rest of the name can
only contain letters, numbers, or underscores (no other special
characters). If an object's name does not follow this syntax, it will not
be accessible using the dot operator and Luau will not interpret its name
as an identifier.

If more than one object with the same name are siblings, any attempt to
index an object by that name will return only one of the objects, similar
to [Instance:FindFirstChild()](/docs/reference/engine/classes/Instance.md), but not always the desired object.
If a specific object needs to be accessed through code, it's recommended
to give it a unique name or guarantee that none of its siblings share the
same name.

See also [Instance:GetFullName()](/docs/reference/engine/classes/Instance.md) to obtain a full name including
the object's hierarchy.

### Property: Instance.Parent

```json
{
  "type": "Instance",
  "access": "ReadWrite",
  "security": {
    "read": "None",
    "write": "None"
  },
  "serialization": {
    "can_load": true,
    "can_save": false
  },
  "thread_safety": "ReadSafe",
  "category": "Data"
}
```

The `Parent` property determines the hierarchical parent of the
[Instance](/docs/reference/engine/classes/Instance.md). The following terminology is commonly used when talking
about how this property is set:

- An object is a **child** of, or is **parented to**, another object when
  its `Parent` is set to that object.

- The **descendants** of an [Instance](/docs/reference/engine/classes/Instance.md) are the children of that
  object, plus the descendants of the children as well.

- The **ancestors** of an [Instance](/docs/reference/engine/classes/Instance.md) are all the objects that the
  instance is a descendant of.

It is from the `Parent` property that many other API members get their
name, such as [GetChildren()](/docs/reference/engine/classes/Instance.md) and
[FindFirstChild()](/docs/reference/engine/classes/Instance.md). This property is also
used to manage whether an object exists in the experience or needs to be
removed. As long as an object's parent is in the [DataModel](/docs/reference/engine/classes/DataModel.md), is
stored in a variable, or is referenced by another object's property, the
object remains in the experience; otherwise, the object will automatically
be removed.

Calling [Destroy()](/docs/reference/engine/classes/Instance.md) will set the `Parent` of an
[Instance](/docs/reference/engine/classes/Instance.md) and all of its descendants to `nil`, and also **lock**
the `Parent` property. An error is raised when setting the `Parent` of a
destroyed object.

Newly created objects using [Instance.new()](/docs/reference/engine/datatypes/Instance.md) will not have a
parent, and usually will not be visible or function until one is set.

#### Object Replication

An object created by the server will not replicate to clients until it is
parented to some object that is replicated. When creating an object and
setting many properties, it's recommended to set the `Parent` property
**last**. This ensures the object replicates once, instead of replicating
many property changes.

```lua
local Workspace = game:GetService("Workspace")

-- Set new instance's parent last (recommended)
local part = Instance.new("Part")
part.Position = Vector3.new(0, 10, 0)
part.Parent = Workspace
```

However, if parenting parts to a [Model](/docs/reference/engine/classes/Model.md) whose parent hasn't been
set yet, parenting each part to that model is acceptable since the model
would not have replicated.

### Property: Instance.PredictionMode

```json
{
  "type": "PredictionMode",
  "access": "ReadWrite",
  "security": {
    "read": "None",
    "write": "None"
  },
  "serialization": {
    "can_load": false,
    "can_save": false
  },
  "thread_safety": "ReadSafe",
  "category": "Data"
}
```

This property reflects the [PredictionMode](/docs/reference/engine/enums/PredictionMode.md) currently applied to the
instance, which determines whether the instance's state is predicted on
the client ahead of the authoritative server state under
server-authoritative physics. It defaults to
[Automatic](/docs/reference/engine/enums/PredictionMode.md).

This property is read-only and cannot be assigned directly from a script;
the prediction mode is set through [RunService:SetPredictionMode()](/docs/reference/engine/classes/RunService.md).
The property is shown in Studio's Properties window only when the
experience uses server-authoritative physics.

- [Automatic](/docs/reference/engine/enums/PredictionMode.md) (default) — the engine automatically
  decides whether to predict the instance. Currently, only
  [BaseParts](/docs/reference/engine/classes/BasePart.md) near the local player character's
  [Humanoid](/docs/reference/engine/classes/Humanoid.md) are predicted, within a dynamic radius that grows and
  shrinks based on the device's capacity to handle the simulation load.
- [On](/docs/reference/engine/enums/PredictionMode.md) — the instance is always predicted. If it is a
  [BasePart](/docs/reference/engine/classes/BasePart.md), its physics properties are predicted ahead of the
  replicated authoritative server state, and mismatches in the instance's
  attributes between the client and server cause a rollback and
  resimulation.
- [Off](/docs/reference/engine/enums/PredictionMode.md) — the instance is not predicted, and regular
  network ownership semantics apply.

### Property: Instance.Sandboxed

```json
{
  "type": "boolean",
  "access": "ReadWrite",
  "security": {
    "read": "None",
    "write": "None"
  },
  "serialization": {
    "can_load": false,
    "can_save": false
  },
  "thread_safety": "ReadSafe",
  "category": "Permissions",
  "capabilities": [
    "CapabilityControl"
  ]
}
```

Turns the instance to be a **sandboxed container**, an experimental
feature which limits the actions that scripts inside a particular
container can perform. See
[script capabilities](/docs/en-us/scripting/capabilities.md) for further
details.

### Property: Instance.UniqueId

```json
{
  "type": "UniqueId",
  "access": "ReadOnly",
  "security": {
    "read": "RobloxScriptSecurity",
    "write": "RobloxEngineSecurity"
  },
  "serialization": {
    "can_load": true,
    "can_save": true
  },
  "thread_safety": "ReadSafe",
  "category": "Data"
}
```

A unique identifier for the instance, distinct from [Instance.Name](/docs/reference/engine/classes/Instance.md)
which is not necessarily unique. This property is visible in the
Properties window in Studio but is not readable or writable from scripts.

### Property: Instance.archivable *(hidden)*

```json
{
  "type": "boolean",
  "access": "ReadWrite",
  "security": {
    "read": "None",
    "write": "None"
  },
  "serialization": {
    "can_load": true,
    "can_save": false
  },
  "deprecated": true,
  "thread_safety": "ReadSafe",
  "category": "Behavior"
}
```

> **Deprecated:** This deprecated property is a variant of [Instance.Archivable](/docs/reference/engine/classes/Instance.md) which should be used instead.

### Property: Instance.RobloxLocked *(hidden)*

```json
{
  "type": "boolean",
  "access": "ReadOnly",
  "security": {
    "read": "PluginSecurity",
    "write": "PluginSecurity"
  },
  "serialization": {
    "can_load": false,
    "can_save": false
  },
  "thread_safety": "ReadSafe",
  "category": "Data"
}
```

This property used to protect objects in the [CoreGui](/docs/reference/engine/classes/CoreGui.md) service from
being altered by users in an unauthorized manner. It has been deprecated
and does not do anything.

## Methods

### Method: Instance:AddTag

**Signature:** `Instance:AddTag(tag: string): ()`

This method applies a tag to the instance, with no effect if the tag is
already applied. Successfully adding a tag will fire a signal created by
[CollectionService:GetInstanceAddedSignal()](/docs/reference/engine/classes/CollectionService.md) with the given tag.

#### Warnings

- An instance's tags that were added client-side will be dropped if the
  server later adds or removes a tag on that instance because the server
  replicates all tags together and overwrites previous tags.

- When tagging an instance, it is common that some resources are used to
  give the tag its functionality, for example event connections or tables.
  To prevent memory leaks, it's a good idea to clean these up (disconnect,
  set to `nil`, etc.) when no longer needed for a tag. Do this when
  calling [Instance:RemoveTag()](/docs/reference/engine/classes/Instance.md), calling
  [Instance:Destroy()](/docs/reference/engine/classes/Instance.md), or in a function connected to a signal
  returned by [CollectionService:GetInstanceRemovedSignal()](/docs/reference/engine/classes/CollectionService.md).

*Security: None · Thread Safety: Unsafe*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `tag` | `string` |  | The tag to apply to the instance. |

**Returns:** `()`

### Method: Instance:ClearAllChildren

**Signature:** `Instance:ClearAllChildren(): ()`

This method destroys all of an instance's children and descendants.

```
local part = Instance.new("Part")

-- Add some sparkles
for i = 1, 3 do
	local sparkles = Instance.new("Sparkles")
	sparkles.Parent = part

  local sc = Instance.new("Sparkles")
  sc.Parent = sparkles
end

print("Children:", #part:GetChildren())  --> Children: 3

part:ClearAllChildren()

print("Children:", #part:GetChildren())  --> Children: 0
```

If you do not wish to destroy **all** children and descendants, use either
[Instance:GetChildren()](/docs/reference/engine/classes/Instance.md) or [Instance:GetDescendants()](/docs/reference/engine/classes/Instance.md) to
loop through those children/descendants and select what to destroy. For
example, the following code sample will destroy all
[BaseParts](/docs/reference/engine/classes/BasePart.md) descending from a [Model](/docs/reference/engine/classes/Model.md):

```
local Workspace = game:GetService("Workspace")

local model = Workspace:FindFirstChild("TestModel")

for _, descendant in model:GetDescendants() do
	if descendant:IsA("BasePart") then
		descendant:Destroy()
	end
end
```

*Security: None · Thread Safety: Unsafe*

**Returns:** `()`

### Method: Instance:Clone

**Signature:** `Instance:Clone(): Instance`

`Clone()` creates a copy of an instance and all of its descendants,
ignoring all instances that are not
[Archivable](/docs/reference/engine/classes/Instance.md). The copy of the root instance is
returned by this method and its [Parent](/docs/reference/engine/classes/Instance.md) is set to
`nil`. Note that if the instance itself has
[Archivable](/docs/reference/engine/classes/Instance.md) set to `false`, this method will
return `nil`.

If a reference property such as [ObjectValue.Value](/docs/reference/engine/classes/ObjectValue.md) is set in a
cloned instance, the value of the copy's property depends on the
original's value:

- If a reference property refers to an instance that was **also** cloned,
  the copy will refer to the copy.
- If a reference property refers to an instance that was **not** cloned,
  the same value is maintained in the copy.

*Security: None · Thread Safety: Unsafe · Capabilities: CreateInstances · Simulation Access: true*

**Returns:** `Instance` — A copy of the instance, or `nil` if the instance is not
[Archivable](/docs/reference/engine/classes/Instance.md).

**Cloning an Instance**

Demonstrates cloning a model using [Instance:Clone()](/docs/reference/engine/classes/Instance.md).

```lua
local Workspace = game:GetService("Workspace")

-- Get a reference to an existing object
local model = script.Parent.Model

-- Create a clone of the model
local clone = model:Clone()

-- Move the clone so it's not overlapping the original model
clone:PivotTo(model.PrimaryPart.CFrame - (Vector3.xAxis * 10))

-- Add the clone to the Workspace
clone.Parent = Workspace
```

### Method: Instance:Destroy

**Signature:** `Instance:Destroy(): ()`

Sets the [Instance.Parent](/docs/reference/engine/classes/Instance.md) property to `nil`, locks the
[Instance.Parent](/docs/reference/engine/classes/Instance.md) property, disconnects all connections, and calls
`Destroy()` on all children. This method is the correct way to dispose of
objects that are no longer required.

Disposing of unneeded objects is important, since unnecessary objects and
connections in a place use up memory which can lead to serious performance
issues over time.

As a best practice after calling `Destroy()` on an object, set any
variables referencing the object (or its descendants) to `nil`. This
prevents your code from accessing anything to do with the object.

```lua
local part = Instance.new("Part")
part.Name = "Hello, world"
part:Destroy()
-- Don't do this:
print(part.Name)  --> "Hello, world"
-- Do this to prevent the above line from working:
part = nil
```

Once an [Instance](/docs/reference/engine/classes/Instance.md) has been destroyed by this method, it cannot be
reused because the [Instance.Parent](/docs/reference/engine/classes/Instance.md) property is locked. To
**temporarily** remove an object instead of destroying it, set
[Parent](/docs/reference/engine/classes/Instance.md) to `nil`. For example:

```
local Workspace = game:GetService("Workspace")

object.Parent = nil
task.wait(2)
object.Parent = Workspace
```

To destroy an object after a set amount of time, use
[Debris:AddItem()](/docs/reference/engine/classes/Debris.md).

*Security: None · Thread Safety: Unsafe*

**Returns:** `()`

**Instance:Destroy()**

Demonstrates destroying a Part using the [Instance:Destroy()](/docs/reference/engine/classes/Instance.md) function.

This function is the correct way to dispose of objects that are no longer
required.

```lua
local part = script.Parent.Part

part:Destroy()
```

### Method: Instance:FindFirstAncestor

**Signature:** `Instance:FindFirstAncestor(name: string): Instance?`

Returns the first ancestor of the [Instance](/docs/reference/engine/classes/Instance.md) whose
[Instance.Name](/docs/reference/engine/classes/Instance.md) is equal to the given name.

This method works upwards, meaning it starts at the instance's immediate
[Instance.Parent](/docs/reference/engine/classes/Instance.md) and works up towards the [DataModel](/docs/reference/engine/classes/DataModel.md). If no
matching ancestor is found, it returns `nil`.

The following code snippet would find the first ancestor of the object
named `Car`.

```
local car = object:FindFirstAncestor("Car")
```

For variants of this method that find ancestors of a specific class,
please see [Instance:FindFirstAncestorOfClass()](/docs/reference/engine/classes/Instance.md) and
[Instance:FindFirstAncestorWhichIsA()](/docs/reference/engine/classes/Instance.md).

*Security: None · Thread Safety: Safe*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `name` | `string` |  | The [Instance.Name](/docs/reference/engine/classes/Instance.md) to be looked for. |

**Returns:** `Instance?` — The [Instance](/docs/reference/engine/classes/Instance.md) found.

### Method: Instance:FindFirstAncestorOfClass

**Signature:** `Instance:FindFirstAncestorOfClass(className: string): Instance?`

Returns the first ancestor of the [Instance](/docs/reference/engine/classes/Instance.md) whose
[Object.ClassName](/docs/reference/engine/classes/Object.md) is equal to the given className.

This method works upwards, meaning it starts at the instance's immediate
[Instance.Parent](/docs/reference/engine/classes/Instance.md) and works up towards the [DataModel](/docs/reference/engine/classes/DataModel.md). If no
matching ancestor is found, it returns `nil`.

A common use of this method is finding the [Model](/docs/reference/engine/classes/Model.md) a
[BasePart](/docs/reference/engine/classes/BasePart.md) belongs to. For example:

```
local model = part:FindFirstAncestorOfClass("Model")
```

This method is a variant of [Instance:FindFirstAncestor()](/docs/reference/engine/classes/Instance.md) which
checks the [Object.ClassName](/docs/reference/engine/classes/Object.md) property rather than
[Instance.Name](/docs/reference/engine/classes/Instance.md). [Instance:FindFirstAncestorWhichIsA()](/docs/reference/engine/classes/Instance.md) also
exists, using the [Object:IsA()](/docs/reference/engine/classes/Object.md) method instead to respect class
inheritance.

*Security: None · Thread Safety: Safe*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `className` | `string` |  | The [Object.ClassName](/docs/reference/engine/classes/Object.md) to be looked for. |

**Returns:** `Instance?` — The [Instance](/docs/reference/engine/classes/Instance.md) found.

### Method: Instance:FindFirstAncestorWhichIsA

**Signature:** `Instance:FindFirstAncestorWhichIsA(className: string): Instance?`

Returns the first ancestor of the [Instance](/docs/reference/engine/classes/Instance.md) for whom
[Object:IsA()](/docs/reference/engine/classes/Object.md) returns true for the given className.

This method works upwards, meaning it starts at the instance's immediate
[Instance.Parent](/docs/reference/engine/classes/Instance.md) and works up towards the [DataModel](/docs/reference/engine/classes/DataModel.md). If no
matching ancestor is found, it returns `nil`.

Unlike [Instance:FindFirstAncestorOfClass()](/docs/reference/engine/classes/Instance.md), this method uses
[Object:IsA()](/docs/reference/engine/classes/Object.md) which respects class inheritance. For example:

```
print(part:IsA("Part"))  --> true
print(part:IsA("BasePart"))  --> true
print(part:IsA("Instance"))  --> true
```

Therefore, the following code sample will return the first
[BasePart](/docs/reference/engine/classes/BasePart.md) ancestor, regardless of if it is a [WedgePart](/docs/reference/engine/classes/WedgePart.md),
[MeshPart](/docs/reference/engine/classes/MeshPart.md) or [Part](/docs/reference/engine/classes/Part.md).

```
local part = object:FindFirstAncestorWhichIsA("BasePart")
```

See also [Instance:FindFirstAncestor()](/docs/reference/engine/classes/Instance.md).

*Security: None · Thread Safety: Safe*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `className` | `string` |  | The [Object.ClassName](/docs/reference/engine/classes/Object.md) to be looked for. |

**Returns:** `Instance?` — The [Instance](/docs/reference/engine/classes/Instance.md) found.

### Method: Instance:FindFirstChild

**Signature:** `Instance:FindFirstChild(name: string, recursive?: boolean): Instance?`

Returns the first child of the [Instance](/docs/reference/engine/classes/Instance.md) with the given name, or
`nil` if no such child exists. If the optional `recursive` argument is
`true`, this method searches all descendants rather than only the
immediate children of the [Instance](/docs/reference/engine/classes/Instance.md).

#### Checking the Existence of an Object

`FindFirstChild()` is necessary if you need to verify an object exists
before continuing. Attempting to index a child by name using the dot
operator throws an error if the child doesn't exist.

```lua
local Workspace = game:GetService("Workspace")

-- The following line errors if the part doesn't exist in the workspace
Workspace.Part.Transparency = 0.5
```

A better approach is to use `FindFirstChild()` to first check for `Part`,
then use an `if` statement to run code that needs it.

```lua
local Workspace = game:GetService("Workspace")

local part = Workspace:FindFirstChild("Part")
if part then
	part.Transparency = 0.5
end
```

#### Finding a Child Whose Name Matches a Property

Sometimes the [Name](/docs/reference/engine/classes/Instance.md) of an object is the same as that
of a property of its [Parent](/docs/reference/engine/classes/Instance.md). When using the dot
operator, properties take precedence over children if they share a name.

In the following example, a [Folder](/docs/reference/engine/classes/Folder.md) called `Color` is added to a
[Part](/docs/reference/engine/classes/Part.md), which also has the [Part.Color](/docs/reference/engine/classes/Part.md) property. Notice that
`part.Color` refers to the [Color3](/docs/reference/engine/datatypes/Color3.md) property value, not the child
[Folder](/docs/reference/engine/classes/Folder.md) instance. A benefit of using
[FindFirstChild()](/docs/reference/engine/classes/Instance.md) is that the
introduction of new properties does not impose a risk on your code.

```lua
local part = Instance.new("Part")
local folder = Instance.new("Folder")
folder.Name = "Color"
folder.Parent = part
local c1 = part.Color  -- The property
local c2 = part:FindFirstChild("Color")  -- The child folder
```

#### Performance Notes

[FindFirstChild()](/docs/reference/engine/classes/Instance.md) takes about 20% longer
than using the dot operator and almost 8 times longer than simply storing
a reference to an object. Therefore, you should avoid calling it in
performance-dependent code such as in tight loops or functions connected
to [RunService.Heartbeat](/docs/reference/engine/classes/RunService.md) and [RunService.PreRender](/docs/reference/engine/classes/RunService.md). Instead,
store the result in a variable, or consider using
[ChildAdded](/docs/reference/engine/classes/Instance.md) or
[WaitForChild()](/docs/reference/engine/classes/Instance.md) to detect when a child of a
given name becomes available.

*Security: None · Thread Safety: Safe · Simulation Access: true*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `name` | `string` |  | The [Instance.Name](/docs/reference/engine/classes/Instance.md) to be searched for. |
| `recursive` | `boolean` | `false` | Whether or not the search should be conducted recursively. |

**Returns:** `Instance?` — The [Instance](/docs/reference/engine/classes/Instance.md) found.

**Instance:FindFirstChild**

The below would look in Workspace for an object name "Brick". If found, it
will change the name of the object to "Foo".

```lua
local found = workspace:FindFirstChild("Brick")

if found then
	found.Name = "Foo"
end
```

### Method: Instance:FindFirstChildOfClass

**Signature:** `Instance:FindFirstChildOfClass(className: string): Instance?`

Returns the first child of the [Instance](/docs/reference/engine/classes/Instance.md) whose
[ClassName](/docs/reference/engine/classes/Object.md) is equal to the given `className`.
Unlike [Instance:FindFirstChildWhichIsA()](/docs/reference/engine/classes/Instance.md), this method only returns
objects whose class matches `className`, ignoring class inheritance. If no
matching child is found, this method returns `nil`.

*Security: None · Thread Safety: Safe*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `className` | `string` |  | The [Object.ClassName](/docs/reference/engine/classes/Object.md) to be looked for. |

**Returns:** `Instance?` — The [Instance](/docs/reference/engine/classes/Instance.md) found.

**Instance:FindFirstChildOfClass**

```lua
local Players = game:GetService("Players")

local player = Players.LocalPlayer
local character = player.Character or player.CharacterAdded:Wait()

local humanoid

while not humanoid do
	humanoid = character:FindFirstChildOfClass("Humanoid")
	if not humanoid then
		character.ChildAdded:Wait()
	end
end
```

### Method: Instance:FindFirstChildWhichIsA

**Signature:** `Instance:FindFirstChildWhichIsA(className: string, recursive?: boolean): Instance?`

Returns the first child of the [Instance](/docs/reference/engine/classes/Instance.md) for whom
[Object:IsA()](/docs/reference/engine/classes/Object.md) returns true for the given className.

If no matching child is found, this method returns `nil`. If the optional
recursive argument is true, this method searches all descendants rather
than only the immediate children of the [Instance](/docs/reference/engine/classes/Instance.md).

Unlike [Instance:FindFirstChildOfClass()](/docs/reference/engine/classes/Instance.md), this method uses
[Object:IsA()](/docs/reference/engine/classes/Object.md) which respects class inheritance. For example:

```lua
print(part:IsA("Part")) --> true
print(part:IsA("BasePart")) --> true
print(part:IsA("Instance")) --> true
```

Therefore, the following code sample will return the first
[BasePart](/docs/reference/engine/classes/BasePart.md) child, regardless of if it is a [WedgePart](/docs/reference/engine/classes/WedgePart.md),
[MeshPart](/docs/reference/engine/classes/MeshPart.md) or [Part](/docs/reference/engine/classes/Part.md).

```
local part = object:FindFirstChildWhichIsA("BasePart")
```

Developers looking for a child by name, should use
[Instance:FindFirstChild()](/docs/reference/engine/classes/Instance.md) instead.

*Security: None · Thread Safety: Safe · Simulation Access: true*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `className` | `string` |  | The [Object.ClassName](/docs/reference/engine/classes/Object.md) to be searched for. |
| `recursive` | `boolean` | `false` | Whether or not the search should be conducted recursively. |

**Returns:** `Instance?` — The [Instance](/docs/reference/engine/classes/Instance.md) found.

### Method: Instance:FindFirstDescendant

**Signature:** `Instance:FindFirstDescendant(name: string): Instance?`

Returns the first descendant found with the given [Instance.Name](/docs/reference/engine/classes/Instance.md).

This method is disabled and cannot be used. To find the first descendant
of an instance, consider using the `recursive` parameter on
[Instance:FindFirstChild()](/docs/reference/engine/classes/Instance.md) instead.

*Security: None · Thread Safety: Safe*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `name` | `string` |  | The [Instance.Name](/docs/reference/engine/classes/Instance.md) to search for. |

**Returns:** `Instance?` — The [Instance](/docs/reference/engine/classes/Instance.md) found.

### Method: Instance:GetActor

**Signature:** `Instance:GetActor(): Actor?`

If the [Instance](/docs/reference/engine/classes/Instance.md) is an [Actor](/docs/reference/engine/classes/Actor.md), the [Actor](/docs/reference/engine/classes/Actor.md) itself is
returned. Otherwise, its closest ancestor [Actor](/docs/reference/engine/classes/Actor.md) is returned. If no
ancestor is an [Actor](/docs/reference/engine/classes/Actor.md), the result is `nil`.

*Security: None · Thread Safety: Safe*

**Returns:** `Actor?` — The [Actor](/docs/reference/engine/classes/Actor.md) found.

### Method: Instance:GetAttribute

**Signature:** `Instance:GetAttribute(attribute: string): Variant`

This method returns the value which has been assigned to the given
attribute name. If no attribute has been assigned, `nil` is returned.

For example, the following code snippet sets and then gets the value of
the instance's `InitialPosition` attribute:

```lua
local Workspace = game:GetService("Workspace")

local part = Workspace.Part
part:SetAttribute("InitialPosition", part.Position)

local initialPosition = instance:GetAttribute("InitialPosition")
print(initialPosition)
```

#### See Also

- [Instance:SetAttribute()](/docs/reference/engine/classes/Instance.md) which sets the attribute with the given
  name to the given value.
- [Instance:GetAttributes()](/docs/reference/engine/classes/Instance.md) which returns a dictionary of key‑value
  pairs for each of the instance's attributes.

*Security: None · Thread Safety: Safe · Simulation Access: true*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `attribute` | `string` |  | The name of the attribute being retrieved. |

**Returns:** `Variant` — The value which has been assigned to the given attribute name. If no
attribute has been assigned, `nil` is returned.

### Method: Instance:GetAttributeChangedSignal

**Signature:** `Instance:GetAttributeChangedSignal(attribute: string): RBXScriptSignal`

This method returns an event that behaves exactly like the
[Changed](/docs/reference/engine/classes/Object.md) event, except that it only fires when the
specific given attribute changes; effectively it is similar to
[GetPropertyChangedSignal()](/docs/reference/engine/classes/Object.md) but
for attributes.

It's generally a good idea to use this method instead of a connection to
[Changed](/docs/reference/engine/classes/Object.md) with a function that checks the attribute
name. Subsequent calls to this method on the same object with the same
attribute name return the same event.

The following code example returns a signal that fires the function
`attributeChanged()` when the part's `InitialPosition` attribute changes:

```lua
local Workspace = game:GetService("Workspace")

local part = Workspace.Part
part:SetAttribute("InitialPosition", part.Position)

local function attributeChanged()
	print("Attribute changed")
end

part:GetAttributeChangedSignal("InitialPosition"):Connect(attributeChanged)
```

See also [Instance.AttributeChanged](/docs/reference/engine/classes/Instance.md) which fires whenever any
attribute is changed on the instance.

*Security: None · Thread Safety: Unsafe*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `attribute` | `string` |  | The name of the specified attribute for which the change signal is being returned. |

**Returns:** `RBXScriptSignal` — An event that fires when the given attribute changes.

### Method: Instance:GetAttributes

**Signature:** `Instance:GetAttributes(): Dictionary`

This method returns a dictionary of key‑value pairs for each attribute
where the key is the attribute's name and the value is a non‑`nil` value.

For example, the following code snippet outputs an instance's attributes
and values:

```lua
local Workspace = game:GetService("Workspace")

local part = Workspace.Part
part:SetAttribute("InitialPosition", part.Position)
part:SetAttribute("CanUse", true)

for name, value in part:GetAttributes() do
	print(name .. " = " .. value)
end
```

See also [Instance:GetAttribute()](/docs/reference/engine/classes/Instance.md) which returns the value that has
been assigned to the given attribute name.

*Security: None · Thread Safety: Safe · Simulation Access: true*

**Returns:** `Dictionary` — A dictionary of string → variant pairs for each attribute where the
string is the name of the attribute and the variant is a non-nil
value.

### Method: Instance:GetChildren

**Signature:** `Instance:GetChildren(): Instances`

Returns an array (a numerically indexed table) containing all of the
instance's direct children, or every [Instance](/docs/reference/engine/classes/Instance.md) whose
[Parent](/docs/reference/engine/classes/Instance.md) is equal to the object. The array can be
iterated upon using either a numeric or generic `for` loop:

```lua
local Workspace = game:GetService("Workspace")

-- Numeric loop example
local children = Workspace:GetChildren()
for i = 1, #children do
	local child = children[i]
	print(child.Name .. " is child number " .. i)
end
```

```lua
local Workspace = game:GetService("Workspace")

-- Generic loop example
local children = Workspace:GetChildren()
for i, child in children do
	print(child.Name .. " is child number " .. i)
end
```

Note that the returned array is **not** sorted in any particular order, so
manual sorting (for example using [table.sort()](/docs/reference/engine/globals/table.md)) is advised for
sorting the children returned by this method.

See also the [GetDescendants()](/docs/reference/engine/classes/Instance.md) method.

*Security: None · Thread Safety: Safe · Simulation Access: true*

**Returns:** `Instances` — An array containing the instance's children.

**Instance:GetChildren**

The below would print the name of all objects currently in Workspace when ran.

```lua
local children = workspace:GetChildren()

for i = 1, #children do
	print(i, children[i].Name)
end
```

### Method: Instance:GetDebugId

**Signature:** `Instance:GetDebugId(scopeLength?: int): string`

Returns a coded string of the debug ID used internally by Roblox. Note
that:

- This item is protected. Attempting to use it in a [Script](/docs/reference/engine/classes/Script.md) or
  [LocalScript](/docs/reference/engine/classes/LocalScript.md) will cause an error.
- A debug ID is an ID used in debugging processes. It allows a debugger to
  read each instruction before an application processes it. All objects in
  Roblox act like processes and each run instructions (or 'code') that can
  be debugged if needed.
- This can be helpful for plugins which need to distinguish similar
  objects from one-another (such as objects that share the same name).

*Security: PluginSecurity · Thread Safety: Unsafe*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `scopeLength` | `int` | `4` | The scope length. |

**Returns:** `string` — The Debug ID string.

**Instance:GetDebugId**

```lua
print(workspace:GetDebugId()) --> 39FA_12
print(workspace:GetDebugId(10)) --> 39FA2FEF4D_12
print(workspace:GetDebugId(math.huge)) --> 12
```

### Method: Instance:GetDescendants

**Signature:** `Instance:GetDescendants(): Instances`

This object method returns an array that contains all of the descendants
of that object. Unlike [Instance:GetChildren()](/docs/reference/engine/classes/Instance.md), which only returns
the immediate children of an object, this method finds every child of the
object, every child of those children, and so on.

Note that the returned array is **not** sorted in any particular order, so
manual sorting (for example using [table.sort()](/docs/reference/engine/globals/table.md)) is advised for
sorting the descendants returned by this method. Also consdier the
[QueryDescendants()](/docs/reference/engine/classes/Instance.md) method to query
descendants by a combination of selectors and combinators.

*Security: None · Thread Safety: Safe · Simulation Access: true*

**Returns:** `Instances` — An array containing the instance's descendants.

**Instance:GetDescendants**

GetDescendants is often used to do something to all the descendants that are a
particular type of object. The code in this example uses GetDescendants and
[Instance:IsA()](/docs/reference/engine/classes/Instance.md) to find all of the parts in the workspace and turns
them green.

```lua
local descendants = workspace:GetDescendants()

-- Loop through all of the descendants of the Workspace. If a
-- BasePart is found, the code changes that parts color to green
for _, descendant in pairs(descendants) do
	if descendant:IsA("BasePart") then
		descendant.BrickColor = BrickColor.Green()
	end
end
```

### Method: Instance:GetFullName

**Signature:** `Instance:GetFullName(): string`

Returns a string describing the instance's ancestry. The string is a
concatenation of the [Name](/docs/reference/engine/classes/Instance.md) of the object and its
ancestors, separated by periods. The [DataModel](/docs/reference/engine/classes/DataModel.md) (`game`) is not
considered. For example, a [Part](/docs/reference/engine/classes/Part.md) in the [Workspace](/docs/reference/engine/classes/Workspace.md) may
return [Workspace.Part](/docs/reference/engine/classes/Workspace.md).

When called on an [Instance](/docs/reference/engine/classes/Instance.md) that is not a descendant of the
[DataModel](/docs/reference/engine/classes/DataModel.md), this method considers all ancestors up to and including
the topmost one without a [Parent](/docs/reference/engine/classes/Instance.md).

This method is useful for logging and debugging. You shouldn't attempt to
parse the returned string for any useful operation; this method does not
escape periods (or any other symbol) in object names. In other words,
although its output often appears to be a valid Luau identifier, it is not
guaranteed.

*Security: None · Thread Safety: Safe · Simulation Access: true*

**Returns:** `string` — The full name of the [Instance](/docs/reference/engine/classes/Instance.md).

**Instance:GetFullName**

This code sample demonstrates the behavior of [Instance:GetFullName()](/docs/reference/engine/classes/Instance.md).
It shows how the function behaves when called on an object not in the
`DataModel` hierarchy, and it also shows how the return value does not escape
special characters.

```lua
-- Create a simple hierarchy
local model = Instance.new("Model")
local part = Instance.new("Part")
part.Parent = model
local fire = Instance.new("Fire")
fire.Parent = part

print(fire:GetFullName()) --> Model.Part.Fire

model.Parent = workspace

print(fire:GetFullName()) --> Workspace.Model.Part.Fire

part.Name = "Hello, world"

print(fire:GetFullName()) --> Workspace.Model.Hello, world.Fire
```

**Expected output:** Model.Part.Fire
Workspace.Model.Part.Fire
Workspace.Model.Hello, world.Fire

**Instance:GetFullName Lua Implementation**

This code sample re-implements the [Instance:GetFullName()](/docs/reference/engine/classes/Instance.md) function in
Lua.

```lua
local function getFullName(object)
	local result = object.Name
	object = object.Parent
	while object and object ~= game do
		-- Prepend parent name
		result = object.Name .. "." .. result
		-- Go up the hierarchy
		object = object.Parent
	end
	return result
end

print(getFullName(workspace.Camera)) --> Workspace.Camera
```

**Expected output:** Workspace.Camera

### Method: Instance:GetStyled

**Signature:** `Instance:GetStyled(name: string, selector: string?): Variant`

This method returns the styled or explicitly modified value of the
specified property, or else the default property value if it hasn't been
styled/modified. This differs slightly from accessing the property value
directly, such as `[GuiObject].Rotation`, which returns the default or
modified value of the property.

*Security: None · Thread Safety: Unsafe*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `name` | `string` |  | Name of the property to query. |
| `selector` | `string?` |  | Optional selector for the pseudo instance you are targeting on the instance. |

**Returns:** `Variant` — The styled or explicitly modified value of the specified property, or
else the default property value if it hasn't been styled/modified.

**Get Styled**

Demonstrates [Instance:GetStyled()](/docs/reference/engine/classes/Instance.md).

```lua
local Players = game:GetService("Players")
local ReplicatedStorage = game:GetService("ReplicatedStorage")

local player = Players.LocalPlayer
local playerGui = player.PlayerGui
local HUDContainer = playerGui:WaitForChild("HUDContainer")

local coreSheet = ReplicatedStorage:FindFirstChild("CoreSheet")
local rule = coreSheet:FindFirstChildWhichIsA("StyleRule")
rule.Selector = "TextButton"

-- Reference to a button
local button = HUDContainer:FindFirstChildWhichIsA("TextButton")

print(button:GetStyled("Rotation")) --> 0 (default value)
print(button.Rotation) --> 0 (default value)

-- Apply rotation through style rule property
rule:SetProperty("Rotation", 30)

print(button:GetStyled("Rotation")) --> 30 (styled value based on rule)
print(button.Rotation) --> 0 (default value)

-- Explicitly modify/override styled property
button.Rotation = 45

print(button:GetStyled("Rotation")) --> 45 (modified value)
print(button.Rotation) --> 45 (modified value)
```

### Method: Instance:GetStyledPropertyChangedSignal

**Signature:** `Instance:GetStyledPropertyChangedSignal(property: string): RBXScriptSignal`

This method returns an event that behaves exactly like the
[StyledPropertiesChanged](/docs/reference/engine/classes/Instance.md) event,
except that it only fires when the given style property changes. It's
generally a good idea to use this method instead of a connection to
[StyledPropertiesChanged](/docs/reference/engine/classes/Instance.md) with a
function that checks the property name. Subsequent calls to this method on
the same object with the same property name return the same event.

Note that this event will not pass any arguments to a connected function,
so the value of the changed property must be read directly within a
script.

*Security: None · Thread Safety: Unsafe*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `property` | `string` |  | Name of the style property for which to listen for changes. |

**Returns:** `RBXScriptSignal` — Event that fires when the given style property changes.

**Get Styled Property Changed Signal**

Demonstrates [Instance:GetStyledPropertyChangedSignal()](/docs/reference/engine/classes/Instance.md).

```lua
local Players = game:GetService("Players")

local player = Players.LocalPlayer
local playerGui = player.PlayerGui
local HUDContainer = playerGui:WaitForChild("HUDContainer")
local meterBar = HUDContainer.MeterBar

local function stylePropertyChanged()
	print("Style property changed!")
end

meterBar:GetStyledPropertyChangedSignal("AnchorPoint"):Connect(stylePropertyChanged)
```

### Method: Instance:GetTags

**Signature:** `Instance:GetTags(): Array`

This method returns an array of the tags applied to the given instance, as
strings. You can add tags either in Studio in the
[Properties](/docs/en-us/studio/properties.md) window or at runtime with
[AddTag()](/docs/reference/engine/classes/Instance.md).

This method is useful when you want to do something with multiple tags on
an instance at once. However, it is inefficient to use this method to
check for the existence of a single tag; instead, use
[HasTag()](/docs/reference/engine/classes/Instance.md) to check for a specific tag.

*Security: None · Thread Safety: Safe · Simulation Access: true*

**Returns:** `Array` — An array of strings, each representing a tag applied to the instance.

### Method: Instance:HasTag

**Signature:** `Instance:HasTag(tag: string): boolean`

This method returns `true` if the provided tag has been added to the
object. You can add tags either in Studio in the
[Properties](/docs/en-us/studio/properties.md) window or at runtime with
[AddTag()](/docs/reference/engine/classes/Instance.md).

*Security: None · Thread Safety: Safe · Simulation Access: true*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `tag` | `string` |  | The tag to check for on the instance. |

**Returns:** `boolean` — `true` if the instance has the given tag, `false` otherwise.

### Method: Instance:IsAncestorOf

**Signature:** `Instance:IsAncestorOf(descendant: Instance): boolean`

Returns true if an [Instance](/docs/reference/engine/classes/Instance.md) is an ancestor of the given
descendant.

An [Instance](/docs/reference/engine/classes/Instance.md) is considered the ancestor of an object if the
object's [Instance.Parent](/docs/reference/engine/classes/Instance.md) or one of it's parent's
[Instance.Parent](/docs/reference/engine/classes/Instance.md) is set to the [Instance](/docs/reference/engine/classes/Instance.md).

See also, [Instance:IsDescendantOf()](/docs/reference/engine/classes/Instance.md).

*Security: None · Thread Safety: Safe · Simulation Access: true*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `descendant` | `Instance` |  | The descendant [Instance](/docs/reference/engine/classes/Instance.md). |

**Returns:** `boolean` — True if the [Instance](/docs/reference/engine/classes/Instance.md) is an ancestor of the given descendant.

**Instance:IsAncestorOf()**

Demonstrates determining if one instance is the ancestor of another using
[Instance:IsAncestorOf()](/docs/reference/engine/classes/Instance.md)

Workspace and SpawnLocation are ancestors of the SpawnLocation's decal.
Workspace is an ancestor of SpawnLocation.

SpawnLocation and its decal are descendants of Workspace, not ancenstors.
Decal is a descendant to SpawnLocation, not an ancestor.

```lua
local Workspace = game:GetService("Workspace")
local spawnLocation = Workspace.SpawnLocation
local decal = spawnLocation.Decal

-- These statements are true
print(Workspace:IsAncestorOf(spawnLocation))
print(Workspace:IsAncestorOf(decal))
print(spawnLocation:IsAncestorOf(decal))

-- These statements are false
print(spawnLocation:IsAncestorOf(Workspace))
print(decal:IsAncestorOf(Workspace))
print(decal:IsAncestorOf(spawnLocation))
```

### Method: Instance:IsDescendantOf

**Signature:** `Instance:IsDescendantOf(ancestor: Instance): boolean`

Returns `true` if an [Instance](/docs/reference/engine/classes/Instance.md) is a descendant of the given
ancestor.

Note that `IsDescendantOf()` cannot be used with a parameter of `nil` to
check if an object has been removed.

See also [Instance:IsAncestorOf()](/docs/reference/engine/classes/Instance.md).

*Security: None · Thread Safety: Safe · Simulation Access: true*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `ancestor` | `Instance` |  | The ancestor [Instance](/docs/reference/engine/classes/Instance.md). |

**Returns:** `boolean` — True if the [Instance](/docs/reference/engine/classes/Instance.md) is a descendant of the given ancestor.

**Instance:IsDescendantOf**

```lua
local part = Instance.new("Part")
print(part:IsDescendantOf(game))
--> false

part.Parent = workspace
print(part:IsDescendantOf(game))
--> true

part.Parent = game
print(part:IsDescendantOf(game))
--> true
```

### Method: Instance:IsPropertyModified

**Signature:** `Instance:IsPropertyModified(property: string): boolean`

This method indicates whether a specific property has been modified from
the code‑instantiated default. If called on an instance newly created via
code ([Instance.new()](/docs/reference/engine/datatypes/Instance.md)), this method will return `false`. If
called on an object newly created by Studio workflows such as
[Explorer](/docs/en-us/studio/explorer.md) window insertion, the result may
differ.

For example, querying the
[BackgroundColor3](/docs/reference/engine/classes/TextLabel.md) property of a
[TextLabel](/docs/reference/engine/classes/TextLabel.md) inserted via the [Explorer](/docs/en-us/studio/explorer.md)
will return `true`, but querying the same property of a [TextLabel](/docs/reference/engine/classes/TextLabel.md)
created through [Instance.new()](/docs/reference/engine/datatypes/Instance.md) will return `false`, assuming no
other changes were made to its
[BackgroundColor3](/docs/reference/engine/classes/TextLabel.md).

Note that this method only returns useful results for services and
user‑creatable instances. Return values for system‑populated properties of
instances like [PackageLink](/docs/reference/engine/classes/PackageLink.md) is undefined behavior.

Also note that if this method returns `true`, styling will **not** affect
the property because explicitly modifying a property takes precedence over
styling it. To reset a property to its code‑instantiated default and allow
styling on it, use
[ResetPropertyToDefault()](/docs/reference/engine/classes/Instance.md).

*Security: None · Thread Safety: Unsafe · Simulation Access: true*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `property` | `string` |  | Name of the property to query. |

**Returns:** `boolean` — Boolean indicating whether the property is modified from its
code‑instantiated default.

### Method: Instance:QueryDescendants

**Signature:** `Instance:QueryDescendants(selector: string): Instances`

This object method returns an array that contains all descendants of the
object that match the provided `selector` string. `selector` can include
multiple selectors and combinators to match characteristics such as the
class name, instance name, and hierarchy relationships, as well as
specific values of instance properties and attributes. The `selector`
grammar is similar to the one used in [StyleRule](/docs/reference/engine/classes/StyleRule.md), with only a few
differences regarding which parts of the grammar are supported or not.

#### Selectors

- `ClassName` — Matches instances of the specified class in a
  [Object:IsA()](/docs/reference/engine/classes/Object.md) relationship.
- `.Tag` — Matches instances tagged with a [CollectionService](/docs/reference/engine/classes/CollectionService.md) tag.
- `#Name` — Matches instances of a specific [Instance.Name](/docs/reference/engine/classes/Instance.md).
- `[property = value]` — Matches instances which have the specified
  property and that property has the specified value. Boolean, number, and
  string values are supported. Letters, numbers, `_`, and `-` can be used
  without putting the value in quotation marks.
- `[$attribute]` — Matches instances which have the specified
  [attribute](/docs/en-us/studio/properties.md#instance-attributes) set.
- `[$attribute = value]` — Matches instances which have the specified
  attribute **and** that attribute has the specified value. Same
  limitations apply as for property selectors. If you want to check for
  the absence of an attribute, do not query it as `nil`; instead use the
  `:not` pseudo‑class as in `:not([$attribute])`.

Selectors can also be combined. For example,
`Model.Apple[$Variety = Fuji][$Flavor = 4]` will match instances which are
a [Model](/docs/reference/engine/classes/Model.md) tagged as `Apple` and which have a `Variety` attribute
equal to `Fuji` as well as a `Flavor` attribute equal to `4`.

```lua
local Workspace = game:GetService("Workspace")

-- Get all MeshPart descendants
print(Workspace:QueryDescendants("MeshPart"))

-- Get all descendants tagged as "Fruit"
print(Workspace:QueryDescendants(".Fruit"))

-- Get all descendants with the name "RedTree"
print(Workspace:QueryDescendants("#RedTree"))

-- Get all descendants with CanCollide property set to false
print(Workspace:QueryDescendants("[CanCollide = false]"))

-- Get all descendants with a "FuelCapacity" attribute assigned
print(Workspace:QueryDescendants("[$FuelCapacity]"))
-- Get all descendants with a "FuelCapacity" attribute set to 75
print(Workspace:QueryDescendants("[$FuelCapacity = 75]"))
```

#### Combinators

Combinators let you mix basic selectors to match deeper hierarchy
relationships.

- `>` — Matches instances that are **direct children** of the previous
  filter matches.

- `>>` — Matches instances that are **descendants** of the previous filter
  matches. This is the default first filter, meaning that `SpotLight.Red`
  is the same as `>> SpotLight.Red`.

- `,` — Specifies a list of multiple independent selectors for the
  descendant query. Only elements matching the filter are placed in the
  returned array; `nil` will not be included for non‑matches in a query
  list.

```lua
local Workspace = game:GetService("Workspace")

-- Get direct children of any Model that are tagged as "SwordPart"
print(Workspace:QueryDescendants("Model > .SwordPart"))

-- Get direct children which are a Part and are tagged as "Apple"
print(Workspace:QueryDescendants("> Part.Apple"))

-- Get descendants of any Model with an attribute "OnFire" set to true
print(Workspace:QueryDescendants("Model >> [$OnFire = true]"))

-- Get MeshPart descendants tagged as "SwordPart" OR with an attribute "OnFire" set to true
print(Workspace:QueryDescendants("MeshPart.SwordPart, MeshPart[$OnFire = true]"))
```

#### Pseudo-class selectors

- `:not(complex-selector-list)` — Allows selecting instances which do
  **not** match any of the selectors inside, effectively performing a
  negation of the selectors. Since the expression inside is a list of
  complex selectors, it's possible to filter based on multiple conditions.

- `:has(relative-selector-list)` — Allows selecting instances based on
  which instances they contain inside. The selector list is evaluated
  relative to each instance.

```lua
local Workspace = game:GetService("Workspace")

-- Get all descendants which are NOT of class SpotLight
print(Workspace:QueryDescendants(":not(SpotLight)"))
-- Get all descendants which are NOT of class SpotLight OR PointLight
print(Workspace:QueryDescendants(":not(SpotLight, PointLight)"))
-- Get all descendants which do NOT have an attribute "OnFire"
print(Workspace:QueryDescendants(":not([$OnFire])"))
-- Get all descendants EXCEPT children of a Model tagged as "SwordPart"
print(Workspace:QueryDescendants(":not(Model > .SwordPart)"))

-- Get descendants which contain a Tool instance as their own descendant
print(Workspace:QueryDescendants(":has(Tool)"))
-- Get MeshPart descendants which contain a direct child tagged as "SwordPart"
print(Workspace:QueryDescendants("MeshPart:has(> .SwordPart)"))

-- Get MeshPart descendants with direct children NOT of SurfaceAppearance or Texture class
print(Workspace:QueryDescendants("MeshPart:has(> :not(SurfaceAppearance, Texture))"))
```

*Security: None · Thread Safety: Unsafe · Simulation Access: true*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `selector` | `string` |  | Selector string used to filter elements. |

**Returns:** `Instances` — An array of instances (empty if nothing matched the selector).

### Method: Instance:RemoveTag

**Signature:** `Instance:RemoveTag(tag: string): ()`

This method removes a tag from an instance. It will not throw an error if
the object does not have the tag. Successfully removing a tag will fire a
signal created by [CollectionService:GetInstanceRemovedSignal()](/docs/reference/engine/classes/CollectionService.md)
with the given tag.

Note that when tagging an instance, it's common that some resources are
used to give the tag its functionality, for example event connections or
tables. To prevent memory leaks, it's a good idea to clean these up
(disconnect, set to `nil`, etc.) when no longer needed for a tag.

*Security: None · Thread Safety: Unsafe*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `tag` | `string` |  | The tag to remove from the instance. |

**Returns:** `()`

### Method: Instance:ResetPropertyToDefault

**Signature:** `Instance:ResetPropertyToDefault(property: string): ()`

Resets a property to its default value. For example, calling
`ResetPropertyToDefault("Rotation")` on a [TextLabel](/docs/reference/engine/classes/TextLabel.md) is equivalent
to setting its [Rotation](/docs/reference/engine/classes/TextLabel.md) to `0` (the property's
default value). This method can be used to ensure styling will override
this property's default value.

*Security: None · Thread Safety: Unsafe*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `property` | `string` |  | Name of the property to reset. |

**Returns:** `()`

### Method: Instance:SetAttribute

**Signature:** `Instance:SetAttribute(attribute: string, value: Variant): ()`

This method sets the attribute with the given name to the given value. If
the value given is `nil`, the attribute will be removed, since `nil` is
returned by default.

For example, the following code snippet sets the instance's
`InitialPosition` attribute to [Vector3.new(0, 10, 0)](/docs/reference/engine/datatypes/Vector3.md):

```lua
local Workspace = game:GetService("Workspace")

local part = Workspace.Part
part:SetAttribute("InitialPosition", Vector3.new(0, 10, 0))
```

#### Limitations

Naming requirements and restrictions:

- Names must only use alphanumeric characters.
  - You may also include periods, hyphens, slashes, and underscores.
- No spaces or unique symbols (such as @, ~, !) are allowed.
- Strings must be 100 characters or less.
- Names are not allowed to start with **RBX** unless the caller is a
  Roblox core script (reserved for Roblox).

When attempting to set an attribute to an unsupported type, an error will
be thrown.

#### See Also

- [Instance:GetAttribute()](/docs/reference/engine/classes/Instance.md) which returns the value that has been
  assigned to the given attribute name.
- [Instance:GetAttributes()](/docs/reference/engine/classes/Instance.md) which returns a dictionary of key‑value
  pairs for each of the instance's attributes.

*Security: None · Thread Safety: Unsafe · Simulation Access: true*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `attribute` | `string` |  | The name of the attribute being set. |
| `value` | `Variant` |  | The value to set the specified attribute to. |

**Returns:** `()`

### Method: Instance:WaitForChild

**Signature:** `Instance:WaitForChild(childName: string, timeOut: double): Instance`

Returns the child of the [Instance](/docs/reference/engine/classes/Instance.md) with the given name. If the
child does not exist, it will yield the current thread until it does. If
the `timeOut` parameter is specified, this method will time out after the
specified number of seconds and return `nil`.

#### Primary Usage

[WaitForChild()](/docs/reference/engine/classes/Instance.md) is extremely important when
working on code run by the client in a [LocalScript](/docs/reference/engine/classes/LocalScript.md). The Roblox
engine does not guarantee the time or order in which objects are
replicated from the server to the client. Additionally, if an experience
has [Workspace.StreamingEnabled](/docs/reference/engine/classes/Workspace.md) set to true,
[BaseParts](/docs/reference/engine/classes/BasePart.md) that are far away from the player's character
may not be streamed to the client, potentially causing scripts to break
when indexing objects that do not yet exist on the client.

#### Notes

- This method does not yield if a child with the given name exists when
  the call is made.
- [Instance:FindFirstChild()](/docs/reference/engine/classes/Instance.md) is a more efficient alternative to
  [WaitForChild()](/docs/reference/engine/classes/Instance.md) for objects that are
  assumed to exist.
- If a call to this method exceeds 5 seconds without returning, and no
  `timeOut` parameter has been specified, a warning will be printed to the
  output that the thread may yield indefinitely.

*Security: None · Thread Safety: Unsafe*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `childName` | `string` |  | The [Instance.Name](/docs/reference/engine/classes/Instance.md) to be looked for. |
| `timeOut` | `double` |  | An optional time out parameter. |

**Returns:** `Instance` — The [Instance](/docs/reference/engine/classes/Instance.md) found.

**Instance:WaitForChild**

The following code waits for an instance named "Part" to be added to
Workspace.

```lua
local part = workspace:WaitForChild("Part")
print(part.Name .. " has been added to the Workspace")
```

### Method: Instance:children

**Signature:** `Instance:children(): Instances`

> **Deprecated:** This item has been superseded by [Instance:GetChildren()](/docs/reference/engine/classes/Instance.md) which should be used in all new work.

The children function returns an array of the object's children.

*Security: None · Thread Safety: Unsafe*

**Returns:** `Instances` — Array of child objects/instances.

### Method: Instance:clone

**Signature:** `Instance:clone(): Instance`

> **Deprecated:** This deprecated function is a variant of [Instance:Clone()](/docs/reference/engine/classes/Instance.md) which should be used instead.

*Security: None · Thread Safety: Unsafe · Capabilities: CreateInstances · Simulation Access: true*

**Returns:** `Instance`

### Method: Instance:destroy

**Signature:** `Instance:destroy(): ()`

> **Deprecated:** This deprecated function is a variant of [Instance:Destroy()](/docs/reference/engine/classes/Instance.md) which should be used instead.

*Security: None · Thread Safety: Unsafe*

**Returns:** `()`

### Method: Instance:findFirstChild

**Signature:** `Instance:findFirstChild(name: string, recursive?: boolean): Instance`

> **Deprecated:** This deprecated function is a variant of [Instance:FindFirstChild()](/docs/reference/engine/classes/Instance.md) which should be used instead.

*Security: None · Thread Safety: Unsafe · Simulation Access: true*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `name` | `string` |  |  |
| `recursive` | `boolean` | `false` |  |

**Returns:** `Instance`

### Method: Instance:getChildren

**Signature:** `Instance:getChildren(): Instances`

> **Deprecated:** This deprecated function is a variant of [Instance:GetChildren()](/docs/reference/engine/classes/Instance.md) which should be used instead.

*Security: None · Thread Safety: Unsafe*

**Returns:** `Instances`

### Method: Instance:isDescendantOf

**Signature:** `Instance:isDescendantOf(ancestor: Instance): boolean`

> **Deprecated:** This deprecated function is a variant of [Instance:IsDescendantOf()](/docs/reference/engine/classes/Instance.md) which should be used instead.

*Security: None · Thread Safety: Unsafe · Simulation Access: true*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `ancestor` | `Instance` |  |  |

**Returns:** `boolean`

### Method: Instance:Remove

**Signature:** `Instance:Remove(): ()`

> **Deprecated:** This item is deprecated in favor of [Instance:Destroy()](/docs/reference/engine/classes/Instance.md) and [Instance:ClearAllChildren()](/docs/reference/engine/classes/Instance.md). If you must remove an object from the game, and wish to use the object later, set its `Parent` property to `nil` instead of using this method.

This method sets the object's [Instance.Parent](/docs/reference/engine/classes/Instance.md) to `nil`, and does
the same for all its descendants.

If the object is referenced before being removed, it is possible to
retrieve the object at a later point.

*Security: None · Thread Safety: Unsafe*

**Returns:** `()`

**Instance:Remove**

The following code demonstrates how a part can be re-added to the DataModel
after being removed:

```lua
local part = Instance.new("Part")
part.Parent = workspace
print(part.Parent) --> Workspace

part:Remove()

print(part.Parent) --> nil

part.Parent = workspace

print(part.Parent) --> Workspace
```

### Method: Instance:remove

**Signature:** `Instance:remove(): ()`

> **Deprecated:** This deprecated function is a variant of [Instance:Remove()](/docs/reference/engine/classes/Instance.md) which has also been deprecated. Neither function should be used in new work.

*Security: None · Thread Safety: Unsafe*

**Returns:** `()`

## Events

### Event: Instance.AncestryChanged

**Signature:** `Instance.AncestryChanged(child: Instance, parent: Instance)`

Fires when this instance is reparented or when any of its ancestors is
reparented.

You can use this event to track the deletion of an instance in Studio,
such as manual deletion in the Explorer or through a plugin. If you need
to detect when an instance is destroyed using [Instance:Destroy()](/docs/reference/engine/classes/Instance.md),
use the [Instance.Destroying](/docs/reference/engine/classes/Instance.md) event instead.

*Security: None*

**Parameters:**

| Name | Type | Description |
|------|------|-------------|
| `child` | `Instance` | The instance whose [Parent](/docs/reference/engine/classes/Instance.md) property changed, which can be this instance or a more distant ancestor, **not** necessarily the instance the handler is connected to. |
| `parent` | `Instance` | The new parent of the `child` parameter. |

**Instance.AncestryChanged**

Demonstrates detecting changes to an instance's ancestry by connecting to the
[Instance.AncestryChanged](/docs/reference/engine/classes/Instance.md) event.

The ChangingPart's Parent is set to different values overtime. The parent of
the part is the part's ancestor, so the [Instance.AncestryChanged](/docs/reference/engine/classes/Instance.md) event
will fire whenever it changes.

```lua
local Workspace = game:GetService("Workspace")

local redPart = script.Parent.RedPart
local bluePart = script.Parent.BluePart
local changingPart = script.Parent.ChangingPart

-- Change the color of changingPart based on it's Parent
local function onAncestryChanged(part: Part, parent: Instance)
	if parent == redPart then
		changingPart.Color = Color3.new(1, 0, 0)
	elseif parent == bluePart then
		changingPart.Color = Color3.new(0, 0, 1)
	else
		changingPart.Color = Color3.new(1, 1, 1)
	end
	print(`{part.Name} is now parented to {parent.Name}`)
end

changingPart.AncestryChanged:Connect(onAncestryChanged)

-- Set changingPart's Parent property to different instances over time
while true do
	task.wait(2)
	changingPart.Parent = redPart

	task.wait(2)
	changingPart.Parent = bluePart

	task.wait(2)
	changingPart.Parent = Workspace
end
```

### Event: Instance.AttributeChanged

**Signature:** `Instance.AttributeChanged(attribute: string)`

This event fires whenever any attribute is changed on the instance,
including when an attribute is set to `nil`. The name of the changed
attribute is passed to the connected function.

For example, the following code snippet connects the `attributeChanged()`
function to fire whenever one of the part's attributes changes:

```lua
local Workspace = game:GetService("Workspace")

local part = Workspace.Part

local function attributeChanged(attributeName)
	print(attributeName, "changed")
end

part.AttributeChanged:Connect(attributeChanged)
```

See also [Instance:GetAttributeChangedSignal()](/docs/reference/engine/classes/Instance.md) which returns an
event that fires when a specific given attribute changes.

*Security: None*

**Parameters:**

| Name | Type | Description |
|------|------|-------------|
| `attribute` | `string` | The name of the attribute that has been changed. |

### Event: Instance.ChildAdded

**Signature:** `Instance.ChildAdded(child: Instance)`

Fires after an object is parented to this [Instance](/docs/reference/engine/classes/Instance.md).

Note, when using this method on a client to detect objects created by the
server it is necessary to use [Instance:WaitForChild()](/docs/reference/engine/classes/Instance.md) when
indexing these object's descendants. This is because the object and its
descendants are not guaranteed to replicate from the server to the client
simultaneously. For example:

```
local Workspace = game:GetService("Workspace")

Workspace.ChildAdded:Connect(function(child)
	-- Use WaitForChild() since descendants may not have replicated yet
	local head = child:WaitForChild("Head")
end)
```

Note, this event only operates for immediate children of the
[Instance](/docs/reference/engine/classes/Instance.md). For an event that captures all descendants, use
[Instance.DescendantAdded](/docs/reference/engine/classes/Instance.md).

See also [Instance.ChildRemoved](/docs/reference/engine/classes/Instance.md).

*Security: None*

**Parameters:**

| Name | Type | Description |
|------|------|-------------|
| `child` | `Instance` | The [Instance](/docs/reference/engine/classes/Instance.md) that has been added. |

**Instance.ChildAdded**

This snippet prints the names of objects as they are added to the Workspace:

```lua
local function onChildAdded(instance)
	print(instance.Name .. " added to the workspace")
end

workspace.ChildAdded:Connect(onChildAdded)

local part = Instance.new("Part")
part.Parent = workspace --> Part added to the Workspace
```

### Event: Instance.ChildRemoved

**Signature:** `Instance.ChildRemoved(child: Instance)`

Fires after a child is removed from this [Instance](/docs/reference/engine/classes/Instance.md).

Removed refers to when an object's parent is changed from this
[Instance](/docs/reference/engine/classes/Instance.md) to something other than this [Instance](/docs/reference/engine/classes/Instance.md). Note, this
event will also fire when a child is destroyed (using
[Instance:Destroy()](/docs/reference/engine/classes/Instance.md)) as the destroy function sets an object's
parent to `nil`.

This event only operates for immediate children of the [Instance](/docs/reference/engine/classes/Instance.md).
For an event that captures all descendants, use
[Instance.DescendantRemoving](/docs/reference/engine/classes/Instance.md).

See also [Instance.ChildAdded](/docs/reference/engine/classes/Instance.md).

*Security: None*

**Parameters:**

| Name | Type | Description |
|------|------|-------------|
| `child` | `Instance` | The [Instance](/docs/reference/engine/classes/Instance.md) that has been removed. |

**Instance.ChildRemoved**

This snippet prints the names of objects as they are removed from the
Workspace:

```lua
local function onChildRemoved(instance)
	print(instance.Name .. " removed from the workspace")
end

workspace.ChildRemoved:Connect(onChildRemoved)

local part = Instance.new("Part")
part.Parent = workspace

task.wait(2)

part:Destroy()
```

### Event: Instance.DescendantAdded

**Signature:** `Instance.DescendantAdded(descendant: Instance)`

This event fires after a descendant is added to the [Instance](/docs/reference/engine/classes/Instance.md).

As it fires for every descendant, parenting an object to the
[Instance](/docs/reference/engine/classes/Instance.md) will fire the event for this object and all of its
descendants individually.

If you're only concerned with the **direct children** of the
[Instance](/docs/reference/engine/classes/Instance.md), use [Instance.ChildAdded](/docs/reference/engine/classes/Instance.md) instead.

See also [Instance.DescendantRemoving](/docs/reference/engine/classes/Instance.md).

*Security: None*

**Parameters:**

| Name | Type | Description |
|------|------|-------------|
| `descendant` | `Instance` | The [Instance](/docs/reference/engine/classes/Instance.md) that has been added. |

**Instance.DescendantAdded**

This following example will print the name of any object that is added to the
Workspace:

```lua
local function onDescendantAdded(descendant)
	print(descendant)
end

workspace.DescendantAdded:Connect(onDescendantAdded)

local part = Instance.new("Part")
part.Parent = workspace
```

### Event: Instance.DescendantRemoving

**Signature:** `Instance.DescendantRemoving(descendant: Instance)`

This event fires **immediately before** the parent [Instance](/docs/reference/engine/classes/Instance.md)
changes such that a **descendant** instance will no longer be a
descendant. [Destroy()](/docs/reference/engine/classes/Instance.md) changes an instance's
[Parent](/docs/reference/engine/classes/Instance.md) to `nil`, so calling that method on a
descendant of the parent will cause this event to fire.

Since this event fires **before** the descendant's removal, the parent of
the descendant will be unchanged at the time of this event firing. If the
descendant is also a **direct child** of the parent, this event will fire
before [Instance.ChildRemoved](/docs/reference/engine/classes/Instance.md).

If a descendant has children, this event fires with the descendant first,
followed by its descendants.

#### Warning

This event fires with the descendant object that is being removed.
Attempting to set the [Parent](/docs/reference/engine/classes/Instance.md) of the descendant to
something else will fail. Below is an example that demonstrates this:

```
local Workspace = game:GetService("Workspace")

Workspace.DescendantRemoving:Connect(function(descendant)
	-- Do not manipulate the parent of the descendant in this function!
	-- This event fires BECAUSE the parent was manipulated, and the change hasn't happened yet
	-- Therefore, it is problematic to change the parent like this:
	descendant.Parent = game
end)

local part = Instance.new("Part")
part.Parent = Workspace
part.Parent = nil
```

See also [DescendantAdded](/docs/reference/engine/classes/Instance.md).

*Security: None*

**Parameters:**

| Name | Type | Description |
|------|------|-------------|
| `descendant` | `Instance` | The [Instance](/docs/reference/engine/classes/Instance.md) that is being removed. |

**Instance.DescendantRemoving**

The following example prints the name of any descendant as it is being removed
from the Workspace:

```lua
workspace.DescendantRemoving:Connect(function(descendant)
	print(descendant.Name .. " is currently parented to " .. tostring(descendant.Parent))
end)
local part = Instance.new("Part")
part.Parent = workspace
part.Parent = nil
--> Part is currently parented to Workspace
print(part.Parent)
--> nil
```

### Event: Instance.Destroying

**Signature:** `Instance.Destroying()`

The [Instance](/docs/reference/engine/classes/Instance.md) will never be deleted from memory while a connected
function is still using it. However, if the function yields at any point,
the [Instance](/docs/reference/engine/classes/Instance.md) and its descendants will be parented to `nil`.

If the [Workspace.SignalBehavior](/docs/reference/engine/classes/Workspace.md) property is set to
[SignalBehavior.Immediate](/docs/reference/engine/enums/SignalBehavior.md), this event fires immediately before the
[Instance](/docs/reference/engine/classes/Instance.md) or one of its ancestors is destroyed with
[Instance:Destroy()](/docs/reference/engine/classes/Instance.md).

If the [Workspace.SignalBehavior](/docs/reference/engine/classes/Workspace.md) property is set to
[SignalBehavior.Deferred](/docs/reference/engine/enums/SignalBehavior.md), this event fires at the next resumption
point, which will be after the [Instance](/docs/reference/engine/classes/Instance.md) or one of its ancestors is
destroyed with [Instance:Destroy()](/docs/reference/engine/classes/Instance.md).

With [Deferred](/docs/reference/engine/enums/SignalBehavior.md) behavior, connecting a script
to its own [Instance.Destroying](/docs/reference/engine/classes/Instance.md) event is problematic, as the script
will be destroyed before the callback can be called (meaning it will not
execute).

When deleting an [Instance](/docs/reference/engine/classes/Instance.md) in Studio, such as manually deleting
through the [Explorer](/docs/en-us/studio/explorer.md) or through a plugin,
the [Instance](/docs/reference/engine/classes/Instance.md) isn't destroyed. Instead, the parent is set to `nil`
which you can track with [Instance.AncestryChanged](/docs/reference/engine/classes/Instance.md).

*Security: None*

**Using the Destroying Event (Immediate signals)**

This sample demonstrates how, when using Immediate signal behavior, an
Instance being destroyed remains in place until the connected function yields.

```lua
local part = Instance.new("Part", workspace)

local function onPartDestroying()
	print("Before yielding:", part:GetFullName(), #part:GetChildren())
	task.wait()
	print("After yielding:", part:GetFullName(), #part:GetChildren())
end

part.Destroying:Connect(onPartDestroying)

part:Destroy()
```

**Expected output:** Before yielding: Workspace.Part 1
After yielding: Part 0

**Using the Destroying Event (Deferred signals)**

This sample demonstrates how, when using Deferred signal behavior, an Instance
is destroyed before the signal fires.

```lua
local part = Instance.new("Part", workspace)

local function onPartDestroying()
	print("In signal:", part:GetFullName(), #part:GetChildren())
end

part.Destroying:Connect(onPartDestroying)

print("Before destroying:", part:GetFullName(), #part:GetChildren())
part:Destroy()
print("After destroying:", part:GetFullName(), #part:GetChildren())
```

**Expected output:** Before destroying: Workspace.Part 1
After destroying: Part 0
In signal: Part 0

### Event: Instance.StyledPropertiesChanged

**Signature:** `Instance.StyledPropertiesChanged()`

This event fires whenever any style property is changed on the instance,
including when a property is set to `nil`.

*Security: None*

**Styled Properties Changed**

Demonstrates [Instance.StyledPropertiesChanged](/docs/reference/engine/classes/Instance.md).

```lua
local Players = game:GetService("Players")

local player = Players.LocalPlayer
local playerGui = player.PlayerGui
local HUDContainer = playerGui:WaitForChild("HUDContainer")
local meterBar = HUDContainer.MeterBar

local function stylePropertyChanged()
	print("Styled properties changed")
end

meterBar:StyledPropertiesChanged():Connect(stylePropertyChanged)
```

### Event: Instance.childAdded

**Signature:** `Instance.childAdded(child: Instance)`

> **Deprecated:** This deprecated event is a variant of [Instance.ChildAdded](/docs/reference/engine/classes/Instance.md) which should be used instead.

*Security: None*

**Parameters:**

| Name | Type | Description |
|------|------|-------------|
| `child` | `Instance` |  |

## Inherited Members

### From [Object](/docs/reference/engine/classes/Object.md)

- **Property `ClassName`** (`string`): A read-only string representing the class this Object belongs to.
- **Property `className`** (`string`):  *(deprecated)*
- **Method `GetPropertyChangedSignal(property: string): RBXScriptSignal`**: Get an event that fires when a given property of the object changes.
- **Method `IsA(className: string): boolean`**: Returns true if an object's class matches or inherits from a given class.
- **Method `isA(className: string): boolean`**:  *(deprecated)*
- **Event `Changed`**: Fires immediately after a property of the object changes, with some