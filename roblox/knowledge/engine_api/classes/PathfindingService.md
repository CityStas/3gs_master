---
name: PathfindingService
last_updated: 2026-10-30T19:55:52Z
inherits:
  - Instance
  - Object
type: class
memory_category: Instances
tags:
  - NotCreatable
  - Service
  - NotReplicated
summary: "Used to find logical paths between two points."
---

# Class: PathfindingService

> Used to find logical paths between two points.

## Description

`PathfindingService` is used to find logical paths between two points,
ensuring that characters can move between the points without running into
walls or other obstacles. By default, the shortest path is calculated, but you
can implement pathfinding modifiers to compute smarter paths across various
materials, around defined regions, or through obstacles.

See [Pathfinding](/docs/en-us/characters/pathfinding.md) for details on
implementing character pathfinding.

## Code Samples

**Using the Pathfinding Service**

The code sample below explores how to move an NPC along a more complex path or
around obstacles. This is known as <strong>pathfinding</strong>.

```lua
local PathfindingService = game:GetService("PathfindingService")

local agentParams = {
	AgentRadius = 2.0,
	AgentHeight = 5.0,
	AgentCanJump = false,
}
local currentWaypointIdx = 1

local path = PathfindingService:CreatePath(agentParams)

local humanoidRootPart = script.Parent:FindFirstChild("HumanoidRootPart")
local targetPosition = Vector3.new(50, 0, 50)
path:ComputeAsync(humanoidRootPart.Position, targetPosition)

-- When the path is blocked...
local function OnPathBlocked(blockedWaypointIdx)
	-- Check if the obstacle is further down the path
	if blockedWaypointIdx > currentWaypointIdx then
		-- Recompute the path
		path:ComputeAsync(humanoidRootPart.Position, targetPosition)
		if path.Status == Enum.PathStatus.Success then

			-- Retrieve update waypoint list with path:GetWaypoints()
			-- and Continue walking towards target
		else
			-- Error, path not found
		end
	end
end

path.Blocked:Connect(OnPathBlocked)
```

## Properties

### Property: PathfindingService.EmptyCutoff

```json
{
  "type": "float",
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
  "category": "Data",
  "capabilities": [
    "Basic"
  ]
}
```

> **Deprecated:** This property is deprecated, since the legacy pathfinding system using it has since been removed. Do not use it for new work.

This function worked with the legacy pathfinding system. The pathfinding
system currently uses a navigation grid and the EmptyCutoff is unused.

When the [PathfindingService](/docs/reference/engine/classes/PathfindingService.md) computes a path using
[PathfindingService:ComputeRawPathAsync()](/docs/reference/engine/classes/PathfindingService.md) or
[PathfindingService:ComputeRawPathAsync()](/docs/reference/engine/classes/PathfindingService.md) it uses the voxel
representation of the world. A voxel is one cube in a grid overlaid on the
world. In this case the voxels being used are 4x4x4. This property sets
the percent of a voxel has to be occupied to be considered empty. Defaults
to 0.16.

## Methods

### Method: PathfindingService:CreatePath

**Signature:** `PathfindingService:CreatePath(agentParameters?: Dictionary): Path`

Creates a [Path](/docs/reference/engine/classes/Path.md) object based on various agent parameters. Valid
keys and values in the `agentParameters` table are as follows:

| Key | Type | Default | Description |
| --- | --- | --- | --- |
| `AgentRadius` | integer | `2` | Determines the minimum amount of horizontal space required for empty space to be considered traversable. |
| `AgentHeight` | integer | `5` | Determines the minimum amount of vertical space required for empty space to be considered traversable. |
| `AgentCanJump` | boolean | `true` | Determines whether jumping during pathfinding is allowed. |
| `AgentCanClimb` | boolean | `false` | Determines whether climbing [TrussParts](/docs/reference/engine/classes/TrussPart\.md) during pathfinding is allowed. |
| `WaypointSpacing` | number | 4 | Determines the spacing between intermediate waypoints in path. |
| `Costs` | table | `{}` | Table of materials or defined [PathfindingModifiers](/docs/reference/engine/classes/PathfindingModifier\.md) and their "cost" for traversal. Useful for making the agent prefer certain materials/regions over others. |

*Security: None · Thread Safety: Unsafe · Capabilities: Basic*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `agentParameters` | `Dictionary` | `nil` | Lua table which lets you fine-tune the path based on various agent parameters. |

**Returns:** `Path` — A [Path](/docs/reference/engine/classes/Path.md) object.

**Creating a Path with Pathfinding Service**

Demonstrates creating a path using [PathfindingService:CreatePath()](/docs/reference/engine/classes/PathfindingService.md)

'PathOptions' represents a Model with three paths made of different materials.
When creating the path we define a large 'Cost' for two of the three paths
materials. This will ensure the path created steers towards the path with the
material of the lowest 'Cost'.

Once the path is created, small parts are created at each waypoint to
visualize the path.

```lua
local Workspace = game:GetService("Workspace")
local PathfindingService = game:GetService("PathfindingService")

-- This model contains a start, end and three paths between the player can walk on: Snow, Metal and LeafyGrass
local PathOptionsModel = script.Parent.PathOptions
local startPosition = PathOptionsModel.Start.Position
local finishPosition = PathOptionsModel.End.Position

-- Create a path that avoids Snow and Metal materials
-- This will ensure the path created avoids the Snow and Metal paths and guides
-- the user towards the LeafyGrass path
local path = PathfindingService:CreatePath({
	AgentRadius = 3,
	AgentHeight = 6,
	AgentCanJump = false,
	Costs = {
		Snow = math.huge,
		Metal = math.huge,
	},
})

-- Compute the path
local success, errorMessage = pcall(function()
	path:ComputeAsync(startPosition, finishPosition)
end)

-- Confirm the computation was successful
if success and path.Status == Enum.PathStatus.Success then
	-- For each waypoint, create a part to visualize the path
	for _, waypoint in path:GetWaypoints() do
		local part = Instance.new("Part")
		part.Position = waypoint.Position
		part.Size = Vector3.new(0.5, 0.5, 0.5)
		part.Color = Color3.new(1, 0, 1)
		part.Anchored = true
		part.CanCollide = false
		part.Parent = Workspace
	end
else
	print(`Path unable to be computed, error: {errorMessage}`)
end
```

### Method: PathfindingService:FindPathAsync

**Signature:** `PathfindingService:FindPathAsync(start: Vector3, finish: Vector3): Path`

This function is used to find a [Path](/docs/reference/engine/classes/Path.md) between two provided points.
This path uses the navigation grid created by [PathfindingService](/docs/reference/engine/classes/PathfindingService.md)
and makes sure that the path can be followed by a regular-sized Roblox
character.

This function returns a [Path](/docs/reference/engine/classes/Path.md) object which contains the coordinates
of the path. If no path is found between the two points, this function
will still return a [Path](/docs/reference/engine/classes/Path.md) object, but that object's
[Path.Status](/docs/reference/engine/classes/Path.md) will be [PathStatus.NoPath](/docs/reference/engine/enums/PathStatus.md).

To get the waypoints of a [Path](/docs/reference/engine/classes/Path.md) object, you can use the
[Path:GetWaypoints()](/docs/reference/engine/classes/Path.md) function.

*Yields · Security: None · Thread Safety: Unsafe · Capabilities: Basic*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `start` | `Vector3` |  | Path start coordinates. |
| `finish` | `Vector3` |  | Path finish coordinates. |

**Returns:** `Path` — A [Path](/docs/reference/engine/classes/Path.md) object.

### Method: PathfindingService:ComputeRawPathAsync

**Signature:** `PathfindingService:ComputeRawPathAsync(start: Vector3, finish: Vector3, maxDistance: float): Path`

> **Deprecated:** This item has been superseded by [PathfindingService:FindPathAsync()](/docs/reference/engine/classes/PathfindingService.md) which should be used in all new work instead.

This function computes and returns a [Path](/docs/reference/engine/classes/Path.md) between two
[Vector3s](/docs/reference/engine/datatypes/Vector3.md). If the given MaxDistance is greater than 512,
an error will be thrown. (MaxDistance is too large).

*Yields · Security: None · Thread Safety: Unsafe · Capabilities: Basic*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `start` | `Vector3` |  |  |
| `finish` | `Vector3` |  |  |
| `maxDistance` | `float` |  |  |

**Returns:** `Path` — A [Path](/docs/reference/engine/classes/Path.md) object.

### Method: PathfindingService:ComputeSmoothPathAsync

**Signature:** `PathfindingService:ComputeSmoothPathAsync(start: Vector3, finish: Vector3, maxDistance: float): Path`

> **Deprecated:** This item has been superseded by [PathfindingService:FindPathAsync()](/docs/reference/engine/classes/PathfindingService.md) which should be used in all new work instead.

This function computes and returns a smooth [Path](/docs/reference/engine/classes/Path.md) between two
[Vector3s](/docs/reference/engine/datatypes/Vector3.md). This function fulfills the same purpose as
[PathfindingService:ComputeRawPathAsync()](/docs/reference/engine/classes/PathfindingService.md), but creates a much
smoother path for an NPC to follow in comparison.

*Yields · Security: None · Thread Safety: Unsafe · Capabilities: Basic*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `start` | `Vector3` |  |  |
| `finish` | `Vector3` |  |  |
| `maxDistance` | `float` |  |  |

**Returns:** `Path`

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