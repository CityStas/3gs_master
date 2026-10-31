---
name: PhysicsService
last_updated: 2026-10-30T19:55:52Z
inherits:
  - Instance
  - Object
type: class
memory_category: Instances
tags:
  - NotCreatable
  - Service
summary: "Service that provides methods for creating and managing collision groups, which control whether sets of BaseParts collide with each other."
---

# Class: PhysicsService

> Service that provides methods for creating and managing collision groups,
> which control whether sets of [BaseParts](/docs/reference/engine/classes/BasePart.md) collide with each
> other.

## Description

[PhysicsService](/docs/reference/engine/classes/PhysicsService.md) primarily contains methods for working with **collision
groups** which define whether a set of parts may or may not collide with parts
in other collision groups. You can register a collision group through
[RegisterCollisionGroup()](/docs/reference/engine/classes/PhysicsService.md) and
assign parts to it by setting those parts'
[CollisionGroup](/docs/reference/engine/classes/BasePart.md) property to the **name** of the
collision group.

Creating, deleting, and modifying collision relationships between collision
groups is limited to server-side [Scripts](/docs/reference/engine/classes/Script.md).

See
[Collision Filtering](/docs/en-us/workspace/collisions.md#collision-filtering)
for usage details in Studio and within scripts.

## Methods

### Method: PhysicsService:CollisionGroupsAreCollidable

**Signature:** `PhysicsService:CollisionGroupsAreCollidable(name1: string, name2: string): boolean`

Returns whether the two specified collision groups will collide. This
method will also return true if either of the groups are unregistered, as
the default collision mask collides with all groups.

*Security: None · Thread Safety: Unsafe · Capabilities: Physics · Simulation Access: true*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `name1` | `string` |  | The name of the first collision group. |
| `name2` | `string` |  | The name of the second collision group. |

**Returns:** `boolean` — `true` if the two groups are set to collide, `false` otherwise. Also
returns `true` if either group is unregistered.

### Method: PhysicsService:CollisionGroupSetCollidable

**Signature:** `PhysicsService:CollisionGroupSetCollidable(name1: string, name2: string, collidable: boolean): ()`

Sets the collision status between two groups. This method will throw an
error if either of the groups is unregistered, so it's recommended that
you confirm each group's registration through
[PhysicsService:IsCollisionGroupRegistered()](/docs/reference/engine/classes/PhysicsService.md) before making this
call.

*Security: None · Thread Safety: Unsafe · Capabilities: Physics · Simulation Access: true*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `name1` | `string` |  | The name of the first collision group. |
| `name2` | `string` |  | The name of the second collision group. |
| `collidable` | `boolean` |  | Whether the two groups should collide with each other. |

**Returns:** `()`

### Method: PhysicsService:GetMaxCollisionGroups

**Signature:** `PhysicsService:GetMaxCollisionGroups(): int`

Returns the maximum number of collision groups the engine supports. This
value is currently 32.

*Security: None · Thread Safety: Unsafe · Capabilities: Physics · Simulation Access: true*

**Returns:** `int` — The maximum number of collision groups supported, currently 32.

### Method: PhysicsService:GetRegisteredCollisionGroups

**Signature:** `PhysicsService:GetRegisteredCollisionGroups(): Array`

Returns a table with info on all of the place's collision groups. Each
value in the returned table is itself a table and containing two members:

| Member | Type | Description |
| --- | --- | --- |
| mask | integer | The collision group's mask; only for internal use. |
| name | string | Name of the collision group. |

*Security: None · Thread Safety: Unsafe · Capabilities: Physics · Simulation Access: true*

**Returns:** `Array` — An array of tables, each containing `name` (string) and `mask`
(integer) fields for a registered collision group.

### Method: PhysicsService:IsCollisionGroupRegistered

**Signature:** `PhysicsService:IsCollisionGroupRegistered(name: string): boolean`

Checks if a collision group is registered. It's recommended that you call
this method before calling methods that throw errors for unregistered
collision groups, such as
[PhysicsService:CollisionGroupSetCollidable()](/docs/reference/engine/classes/PhysicsService.md).

*Security: None · Thread Safety: Unsafe · Capabilities: Physics · Simulation Access: true*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `name` | `string` |  | The name of the collision group to check. |

**Returns:** `boolean` — `true` if a collision group with the given name is registered, `false`
otherwise.

### Method: PhysicsService:RegisterCollisionGroup

**Signature:** `PhysicsService:RegisterCollisionGroup(name: string): ()`

Registers a new collision group with the given name. The name cannot be
`"Default"`.

Note that this method has a slight performance overhead based on the
number of [BaseParts](/docs/reference/engine/classes/BasePart.md) in the workspace, so it's recommended
that you register all collision groups at edit time through the Studio
[editor](/docs/en-us/workspace/collisions.md#collision-groups) and call
[UnregisterCollisionGroup()](/docs/reference/engine/classes/PhysicsService.md)
and [RenameCollisionGroup()](/docs/reference/engine/classes/PhysicsService.md)
as infrequently as possible.

*Security: None · Thread Safety: Unsafe · Capabilities: Physics · Simulation Access: true*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `name` | `string` |  | The name of the collision group to register. |

**Returns:** `()`

**PhysicsService:RegisterCollisionGroup**

This example demonstrates one basic use of collision groups. It assigns
**BallPart** to `"CollisionGroupBall"` and **DoorPart** to
`"CollisionGroupDoor"`, then makes the two groups non-collidable using
[PhysicsService:CollisionGroupSetCollidable()](/docs/reference/engine/classes/PhysicsService.md).

```lua
local PhysicsService = game:GetService("PhysicsService")

local collisionGroupBall = "CollisionGroupBall"
local collisionGroupDoor = "CollisionGroupDoor"

-- Register collision groups
PhysicsService:RegisterCollisionGroup(collisionGroupBall)
PhysicsService:RegisterCollisionGroup(collisionGroupDoor)

-- Assign parts to collision groups
script.Parent.BallPart.CollisionGroup = collisionGroupBall
script.Parent.DoorPart.CollisionGroup = collisionGroupDoor

-- Set groups as non-collidable with each other and check the result
PhysicsService:CollisionGroupSetCollidable(collisionGroupBall, collisionGroupDoor, false)
print(PhysicsService:CollisionGroupsAreCollidable(collisionGroupBall, collisionGroupDoor)) --> false
```

### Method: PhysicsService:RenameCollisionGroup

**Signature:** `PhysicsService:RenameCollisionGroup(from: string, to: string): ()`

Renames the specified registered collision group, but does **not** rename
the [CollisionGroup](/docs/reference/engine/classes/BasePart.md) property of parts that
utilize the group. The first argument of this method is the name of the
group to rename, the second argument is the new name for the group. If the
specified group does not exist, this method will not do anything. The
naming conventions for the new name follow the same rules as if the group
was being created with
[RegisterCollisionGroup()](/docs/reference/engine/classes/PhysicsService.md).

This method will throw a runtime error in the following circumstances:

- Invalid or empty name provided for either argument.
- The method is called from a client.

Note that this method has a slight performance overhead based on the
number of [BaseParts](/docs/reference/engine/classes/BasePart.md) in the workspace, so it's recommended
that you register all collision groups at edit time through the Studio
[editor](/docs/en-us/workspace/collisions.md#collision-groups) and rename
them as infrequently as possible.

*Security: None · Thread Safety: Unsafe · Capabilities: Physics · Simulation Access: true*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `from` | `string` |  | The current name of the collision group to rename. |
| `to` | `string` |  | The new name for the collision group. |

**Returns:** `()`

### Method: PhysicsService:UnregisterCollisionGroup

**Signature:** `PhysicsService:UnregisterCollisionGroup(name: string): ()`

Unregisters the collision group for the given name, with the following
behaviors:

- If an invalid name is provided, the method will not do anything.
- If the reserved name `"Default"` is provided **or** if the method is
  called from a client, it will throw an error.
- If there are any parts in the collision group when it is removed, those
  parts will still maintain the same collision group name. The physical
  behavior of parts in a removed group is undefined, so it's recommended
  to move any parts in a removed group to another group, such as the
  `"Default"` group.

Note that this method has a slight performance overhead based on the
number of [BaseParts](/docs/reference/engine/classes/BasePart.md) in the workspace, so it's recommended
that you register all collision groups at edit time through the Studio
[editor](/docs/en-us/workspace/collisions.md#collision-groups) and call this
method as infrequently as possible.

*Security: None · Thread Safety: Unsafe · Capabilities: Physics · Simulation Access: true*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `name` | `string` |  | The name of the collision group to unregister. |

**Returns:** `()`

### Method: PhysicsService:CollisionGroupContainsPart

**Signature:** `PhysicsService:CollisionGroupContainsPart(name: string, part: BasePart): boolean`

> **Deprecated:** This method has been deprecated. It's recommended that you query a part's collision group through its [CollisionGroup](/docs/reference/engine/classes/BasePart.md) property.

Returns whether the specified part is in the specified collision group.
This method will throw a runtime error in the following circumstances:

- The specified group does not exist.
- The specified part is not a [BasePart](/docs/reference/engine/classes/BasePart.md).

*Security: None · Thread Safety: Unsafe · Capabilities: Physics*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `name` | `string` |  | The name of the collision group to check. |
| `part` | `BasePart` |  | The `BasePart` to check for membership in the collision group. |

**Returns:** `boolean` — `true` if the part belongs to the specified collision group, `false`
otherwise.

### Method: PhysicsService:CreateCollisionGroup

**Signature:** `PhysicsService:CreateCollisionGroup(name: string): int`

> **Deprecated:** This method has been superseded by [RegisterCollisionGroup()](/docs/reference/engine/classes/WorldRoot.md) which should be used for all new work.

Creates a new collision group with the given name, and returns the ID of
the created group.

*Security: None · Thread Safety: Unsafe · Capabilities: Physics*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `name` | `string` |  | The name of the new collision group to create. |

**Returns:** `int` — The integer ID assigned to the newly created collision group.

### Method: PhysicsService:GetCollisionGroupId

**Signature:** `PhysicsService:GetCollisionGroupId(name: string): int`

> **Deprecated:** This method has been deprecated. It's recommended that you query collision groups by **name** through a part's [CollisionGroup](/docs/reference/engine/classes/BasePart.md) property.

This method returns the ID of the collision group with the specified name.
It will throw an error if no group with the given name exists.

*Security: None · Thread Safety: Unsafe · Capabilities: Physics*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `name` | `string` |  | The name of the collision group being retrieved. |

**Returns:** `int` — The ID of the retrieved collision group, or `nil` if no such group
exists.

### Method: PhysicsService:GetCollisionGroupName

**Signature:** `PhysicsService:GetCollisionGroupName(name: int): string`

> **Deprecated:** This method has been deprecated. It's recommended that you query collision groups by **name** through a part's [CollisionGroup](/docs/reference/engine/classes/BasePart.md) property.

Returns the name of the collision group with the corresponding ID, or an
empty string if that ID (`0`–`31`) has not been assigned to a group. The
method throws an error if the ID is outside the valid range.

*Security: None · Thread Safety: Unsafe · Capabilities: Physics*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `name` | `int` |  | The integer ID of the collision group to look up. |

**Returns:** `string` — The name of the collision group with the given ID, or an empty string
if the ID has not been assigned to a group.

### Method: PhysicsService:GetCollisionGroups

**Signature:** `PhysicsService:GetCollisionGroups(): Array`

> **Deprecated:** This method has been superseded by [GetRegisteredCollisionGroups()](/docs/reference/engine/classes/WorldRoot.md) which should be used for all new work.

Returns a table with info on all of the place's collision groups. Each
value in the returned table is itself a table containing three members:

| Member | Type | Description |
| --- | --- | --- |
| id | integer | The ID of the group. |
| mask | integer | The collision group's mask; only for internal use. |
| name | string | The name of the collision group. |

*Security: None · Thread Safety: Unsafe · Capabilities: Physics*

**Returns:** `Array` — An array of tables, each containing `name` (string), `id` (integer),
and `mask` (integer) fields for a registered collision group.

### Method: PhysicsService:RemoveCollisionGroup

**Signature:** `PhysicsService:RemoveCollisionGroup(name: string): ()`

> **Deprecated:** This method has been superseded by [UnregisterCollisionGroup()](/docs/reference/engine/classes/WorldRoot.md) which should be used for all new work.

Removes the collision group with the given name. If an invalid name is
provided, this method will not do anything, although if the reserved name
`"Default"` is provided, it will throw an error. If there are any parts in
the collision group when it is removed, these parts will still maintain
the same collision group ID. The physical behavior of parts in a removed
group is undefined, so it is recommended to move any parts in a removed
group to another group. This method will throw a runtime error in the
following circumstances:

- The name `"Default"` is provided.
- The method is called from a client.

*Security: None · Thread Safety: Unsafe · Capabilities: Physics*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `name` | `string` |  | The name of the collision group to remove. |

**Returns:** `()`

### Method: PhysicsService:SetPartCollisionGroup

**Signature:** `PhysicsService:SetPartCollisionGroup(part: BasePart, name: string): ()`

> **Deprecated:** This method has been deprecated. It's recommended that you set a part's collision group by **name** through its [CollisionGroup](/docs/reference/engine/classes/BasePart.md) property.

This method sets the collision group of the specified part to the group
with the specified name. It is equivalent to setting the
[BasePart.CollisionGroupId](/docs/reference/engine/classes/BasePart.md), although calling this method is the
recommended approach.

This method will throw a runtime error in the following circumstances:

- The part parameter is not a [BasePart](/docs/reference/engine/classes/BasePart.md) instance.
- The specified group does not exist.

*Security: None · Thread Safety: Unsafe · Capabilities: Physics*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `part` | `BasePart` |  | The part being set. |
| `name` | `string` |  | The name of collision group that the part's collision group is being set to. |

**Returns:** `()`

## Inherited Members

### From [Instance](/docs/reference/engine/classes/Instance.md)

- **Property `Archivable`** (`boolean`): Determines if an Instance and its descendants can be cloned using
- **Property `archivable`** (`boolean`):  *(deprecated, hidden)*
- **Property `Capabilities`** (`SecurityCapabilities`): The set of capabilities allowed to be used for scripts inside this
- **Property `IsInSandbox`** (`boolean`): Indicates whether the instance is inside a sandboxed container.
- **Property `Name`** (`string`): A non-unique identifier of the Instance.
- **Property `Parent`** (`Instance`): Determines the hierarchical parent of the Instance.
- **Property `PredictionMode`** (`PredictionMode`): Reflects the client-side prediction mode applied to the instance under
- **Property `RobloxLocked`** (`boolean`): A deprecated property that used to protect CoreGui objects. *(hidden)*
- **Property `Sandboxed`** (`boolean`): When enabled, the instance can only access abilities in its `Capabilities`
- **Property `UniqueId`** (`UniqueId`): A unique identifier for the instance.
- **Method `AddTag(tag: string): ()`**: Applies a tag to the instance.
- **Method `children(): Instances`**: Returns an array of the object's children. *(deprecated)*
- **Method `ClearAllChildren(): ()`**: This method destroys all of an instance's children.
- **Method `Clone(): Instance`**: Create a copy of an instance and all its descendants, ignoring instances
- **Method `clone(): Instance`**:  *(deprecated)*
- **Method `Destroy(): ()`**: Sets the Instance.Parent property to `nil`, locks the
- **Method `destroy(): ()`**:  *(deprecated)*
- **Method `FindFirstAncestor(name: string): Instance?`**: Returns the first ancestor of the Instance whose
- **Method `FindFirstAncestorOfClass(className: string): Instance?`**: Returns the first ancestor of the Instance whose
- **Method `FindFirstAncestorWhichIsA(className: string): Instance?`**: Returns the first ancestor of the Instance for whom
- **Method `FindFirstChild(name: string, recursive?: boolean): Instance?`**: Returns the first child of the Instance found with the given name.
- **Method `findFirstChild(name: string, recursive?: boolean): Instance`**:  *(deprecated)*
- **Method `FindFirstChildOfClass(className: string): Instance?`**: Returns the first child of the Instance whose
- **Method `FindFirstChildWhichIsA(className: string, recursive?: boolean): Instance?`**: Returns the first child of the Instance for whom
- **Method `FindFirstDescendant(name: string): Instance?`**: Returns the first descendant found with the given Instance.Name.
- **Method `GetActor(): Actor?`**: Returns the Actor associated with the Instance, if any.
- **Method `GetAttribute(attribute: string): Variant`**: Returns the value which has been assigned to the given attribute name.
- **Method `GetAttributeChangedSignal(attribute: string): RBXScriptSignal`**: Returns an event that fires when the given attribute changes.
- **Method `GetAttributes(): Dictionary`**: Returns a dictionary of the instance's attributes.
- **Method `GetChildren(): Instances`**: Returns an array containing all of the instance's children.
- **Method `getChildren(): Instances`**:  *(deprecated)*
- **Method `GetDebugId(scopeLength?: int): string`**: Returns a coded string of the debug ID used internally by Roblox.
- **Method `GetDescendants(): Instances`**: Returns an array containing all of the descendants of the instance.
- **Method `GetFullName(): string`**: Returns a string describing the instance's ancestry.
- **Method `GetStyled(name: string, selector: string?): Variant`**: Returns the styled or explicitly modified value of the specified property,
- **Method `GetStyledPropertyChangedSignal(property: string): RBXScriptSignal`**: Returns an event that fires when the given style property changes on the
- **Method `GetTags(): Array`**: Gets an array of all tags applied to the instance.
- **Method `HasTag(tag: string): boolean`**: Check whether the instance has a given tag.
- **Method `IsAncestorOf(descendant: Instance): boolean`**: Returns true if an Instance is an ancestor of the given
- **Method `IsDescendantOf(ancestor: Instance): boolean`**: Returns `true` if an Instance is a descendant of the given
- **Method `isDescendantOf(ancestor: Instance): boolean`**:  *(deprecated)*
- **Method `IsPropertyModified(property: string): boolean`**: Returns `true` if the value stored in the specified property is not equal
- **Method `QueryDescendants(selector: string): Instances`**: Returns an array containing all descendants of the instance that match the
- **Method `Remove(): ()`**: Sets the object's `Parent` to `nil`, and does the same for all its *(deprecated)*
- **Method `remove(): ()`**:  *(deprecated)*
- **Method `RemoveTag(tag: string): ()`**: Removes a tag from the instance.
- **Method `ResetPropertyToDefault(property: string): ()`**: Resets a property to its default value.
- **Method `SetAttribute(attribute: string, value: Variant): ()`**: Sets the attribute with the given name to the given value.
- **Method `WaitForChild(childName: string, timeOut: double): Instance`**: Returns the child of the Instance with the given name. If the
- **Event `AncestryChanged`**: Fires when the Instance.Parent property of this object or one of
- **Event `AttributeChanged`**: Fires whenever an attribute is changed on the Instance.
- **Event `ChildAdded`**: Fires after an object is parented to this Instance.
- **Event `childAdded`**:  *(deprecated)*
- **Event `ChildRemoved`**: Fires after a child is removed from this Instance.
- **Event `DescendantAdded`**: Fires after a descendant is added to the Instance.
- **Event `DescendantRemoving`**: Fires immediately before a descendant of the Instance is removed.
- **Event `Destroying`**: Fires immediately before (or is deferred until after) the instance is
- **Event `StyledPropertiesChanged`**: Fires whenever any style property is changed on the instance, including

### From [Object](/docs/reference/engine/classes/Object.md)

- **Property `ClassName`** (`string`): A read-only string representing the class this Object belongs to.
- **Property `className`** (`string`):  *(deprecated)*
- **Method `GetPropertyChangedSignal(property: string): RBXScriptSignal`**: Get an event that fires when a given property of the object changes.
- **Method `IsA(className: string): boolean`**: Returns true if an object's class matches or inherits from a given class.
- **Method `isA(className: string): boolean`**:  *(deprecated)*
- **Event `Changed`**: Fires immediately after a property of the object changes, with some