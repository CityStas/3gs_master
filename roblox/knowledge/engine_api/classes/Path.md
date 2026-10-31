---
name: Path
last_updated: 2026-10-30T19:55:52Z
inherits:
  - Instance
  - Object
type: class
memory_category: Instances
tags:
  - NotCreatable
  - NotReplicated
summary: "Stores the result of paths created by PathfindingService:CreatePath()."
---

# Class: Path

> Stores the result of paths created by [PathfindingService:CreatePath()](/docs/reference/engine/classes/PathfindingService.md).

## Description

`Path` objects store the result of paths created by
[PathfindingService:CreatePath()](/docs/reference/engine/classes/PathfindingService.md).

Once a `Path` object is created, you can call
[ComputeAsync()](/docs/reference/engine/classes/Path.md) with a starting point and ending
point. This will attempt to compute a valid path for a character to move
along, based on default or custom parameters passed to
[CreatePath()](/docs/reference/engine/classes/PathfindingService.md). If
[ComputeAsync()](/docs/reference/engine/classes/Path.md) successfully finds a path, the
`Path` object will have a [Status](/docs/reference/engine/classes/Path.md) value of
[PathStatus.Success](/docs/reference/engine/enums/PathStatus.md). Otherwise the status will be
[PathStatus.NoPath](/docs/reference/engine/enums/PathStatus.md) which can occur if there are obstacles between the
two points (and no way around) or if the points are inside of solid objects.

In addition to [ComputeAsync()](/docs/reference/engine/classes/Path.md), `Path` objects have
the [GetWaypoints()](/docs/reference/engine/classes/Path.md) method which returns a list of
waypoints representing the points a character should follow in sequence to get
from the beginning to the end of the path.

Finally, `Path` objects can be **connected** to the
[Blocked](/docs/reference/engine/classes/Path.md) event which will fire if, at any time during the
path's existence, the path is blocked. Note that this can occur **behind** a
character moving along the path, not just in front of it.

See [Pathfinding](/docs/en-us/characters/pathfinding.md) for details on
implementing character pathfinding.

## Properties

### Property: Path.Status

```json
{
  "type": "PathStatus",
  "access": "ReadWrite",
  "security": {
    "read": "None",
    "write": "None"
  },
  "serialization": {
    "can_load": false,
    "can_save": true
  },
  "thread_safety": "ReadSafe",
  "category": "Data",
  "capabilities": [
    "Basic"
  ]
}
```

The [PathStatus](/docs/reference/engine/enums/PathStatus.md) of the generated `Path`.

## Methods

### Method: Path:CheckOcclusionAsync

**Signature:** `Path:CheckOcclusionAsync(start: int): int`

This function checks if a path is blocked starting at the waypoint
indicated by **start**.

It returns the first waypoint of occlusion if blocked, -1 if not. it
returns an error if **start** is less than 0 or greater than the number of
waypoints in the `Path`.

*Yields · Security: None · Thread Safety: Unsafe · Capabilities: Basic*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `start` | `int` |  | The 1-based index of the waypoint from which to begin checking for occlusion. |

**Returns:** `int` — The 1-based index of the first blocked waypoint starting from `start`,
or `-1` if the path is not blocked.

### Method: Path:ComputeAsync

**Signature:** `Path:ComputeAsync(start: Vector3, finish: Vector3): ()`

This function computes a `Path` from a start position to an end position.
This function is not automatically called when a path is created and must
be invoked each time the path needs to be updated.

Once the path is computed, it will have a series of waypoints that, when
followed, can lead a character along the path. These points are gathered
with the [GetWaypoints()](/docs/reference/engine/classes/Path.md) function.

*Yields · Security: None · Thread Safety: Unsafe · Capabilities: Basic*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `start` | `Vector3` |  | The world position where the computed path begins. |
| `finish` | `Vector3` |  | The world position where the computed path finishes. |

**Returns:** `()`

### Method: Path:GetWaypoints

**Signature:** `Path:GetWaypoints(): Array`

This method returns an array of all the
[PathWaypoints](/docs/reference/engine/datatypes/PathWaypoint.md) in a `Path` as computed by
[ComputeAsync()](/docs/reference/engine/classes/Path.md).

Each waypoint in the array specifies a [Vector3](/docs/reference/engine/datatypes/Vector3.md) position and
[PathWaypointAction](/docs/reference/engine/enums/PathWaypointAction.md) to take when the waypoint is reached. The array
is arranged in the order of waypoints from the path start to path end.

If a path could not be computed, this function will return an empty array.

*Security: None · Thread Safety: Unsafe · Capabilities: Basic*

**Returns:** `Array` — An array of [PathWaypoints](/docs/reference/engine/datatypes/PathWaypoint.md) ordered from path
start to path end.

**Get Path Waypoints**

The example below demonstrates how to create a `Path` and it's
[PathWaypoints](/docs/reference/engine/datatypes/PathWaypoint.md) using the `PathService`.

It tries to [Path:ComputeAsync()](/docs/reference/engine/classes/Path.md) a path between two [Vector3](/docs/reference/engine/datatypes/Vector3.md)
positions, from pathStart to pathEnd. If a path is successfully created,
indicated by it's [PathStatus](/docs/reference/engine/enums/PathStatus.md), the code block gets an array of its
waypoints using [Path:GetWaypoints()](/docs/reference/engine/classes/Path.md). Then, it loops through the array
and prints each waypoint's position.

```lua
local PathfindingService = game:GetService("PathfindingService")

local path = PathfindingService:CreatePath()

local PATH_START = Vector3.new(0, 1, 0)
local PATH_END = Vector3.new(100, 1, 25)

path:ComputeAsync(PATH_START, PATH_END)

if path.Status == Enum.PathStatus.Success then
	local waypoints = path:GetWaypoints()
	for _, waypoint in pairs(waypoints) do
		print(waypoint.Position)
	end
end
```

### Method: Path:GetPointCoordinates

**Signature:** `Path:GetPointCoordinates(): Array`

> **Deprecated:** This item has been superseded by [GetWaypoints()](/docs/reference/engine/classes/Path.md) which should be used in all new work instead.

This function returns a table of `Path` instances.

*Security: None · Thread Safety: Unsafe · Capabilities: Basic*

**Returns:** `Array` — An array of [Vector3](/docs/reference/engine/datatypes/Vector3.md) positions for each waypoint in the
path.

## Events

### Event: Path.Blocked

**Signature:** `Path.Blocked(blockedWaypointIdx: int)`

Fires when the computed path becomes blocked. Note that paths may become
blocked somewhere **behind** the agent, such as a pile of rubble falling
on a path as the agent runs away. See
[blocked paths](/docs/en-us/characters/pathfinding.md#blocked-paths) for
details on checking the forward waypoint progress of an agent along a
path.

*Security: None · Capabilities: Basic*

**Parameters:**

| Name | Type | Description |
|------|------|-------------|
| `blockedWaypointIdx` | `int` | The 1-based index of the waypoint at which the path became blocked. |

### Event: Path.Unblocked

**Signature:** `Path.Unblocked(unblockedWaypointIdx: int)`

Fires when a computed path that was blocked becomes unblocked. Note that a
blocked path may become unblocked somewhere **behind** the agent,
effectively making reaction to this event unnecessary. See
[blocked paths](/docs/en-us/characters/pathfinding.md#blocked-paths) for
details on checking the forward waypoint progress of an agent along a
path.

*Security: None · Capabilities: Basic*

**Parameters:**

| Name | Type | Description |
|------|------|-------------|
| `unblockedWaypointIdx` | `int` | The 1-based index of the waypoint at which the path became unblocked. |

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