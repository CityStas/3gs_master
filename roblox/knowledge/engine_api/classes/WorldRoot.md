---
name: WorldRoot
last_updated: 2026-10-30T19:55:53Z
inherits:
  - Model
  - PVInstance
  - Instance
  - Object
type: class
memory_category: BaseParts
tags:
  - NotCreatable
summary: "Base class for handling physics simulation and 3D spatial queries."
---

# Class: WorldRoot

> Base class for handling physics simulation and 3D spatial queries.

## Description

This base class provides an API for any instance intended for handling 3D
spatial queries and simulation, such as [Workspace](/docs/reference/engine/classes/Workspace.md) and
[WorldModel](/docs/reference/engine/classes/WorldModel.md).

## Methods

### Method: WorldRoot:ArePartsTouchingOthers

**Signature:** `WorldRoot:ArePartsTouchingOthers(partList: Instances, overlapIgnored?: float): boolean`

**ArePartsTouchingOthers** returns true if at least one of the given
[BasePart](/docs/reference/engine/classes/BasePart.md) are touching any other parts. Two parts are considered
"touching" if they are within the distance threshold, `overlapIgnored`.

If no parts are provided, false is returned.

*Security: None · Thread Safety: Unsafe · Simulation Access: true*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `partList` | `Instances` |  | A list of parts checks to see if any parts in the list are touching any parts not in the list. |
| `overlapIgnored` | `float` | `0.000199999995` | The part overlap threshold in studs that is ignored before parts are considered to be touching. |

**Returns:** `boolean` — True if and only if any of the [parts](/docs/reference/engine/classes/Part.md) in `partList` are
touching any other parts (parts not in the partList). False if no
parts are passed.

**Checking for Touching Parts**

The code block below demonstrates how to use
[WorldRoot:ArePartsTouchingOthers()](/docs/reference/engine/classes/WorldRoot.md) to check if parts in a list are
touching any parts in the workspace not in the list.

First the script creates two square parts that overlap 1 stud, `Part1` and
`Part2`. Then, it prints the value returned by ArePartsTouchingOthers() when
Part1 is passed in `partList` at three different overlap values: `0`, `0.999`,
and `1`. The first two times ArePartsTouchingOthers() is called return `false`
because the overlap values are less than the distance that Part1 and Part2
overlap. The third call returns `true` because the overlap value is equal to
the distance that the parts overlap.

```lua
local part1 = Instance.new("Part")
part1.Name = "Part1"
part1.Anchored = true
part1.Transparency = 0.5
part1.Color = Color3.fromRGB(185, 100, 38)
part1.Size = Vector3.new(2, 2, 2)
part1.Position = Vector3.new(0, 4, 0)
part1.Parent = workspace

local part2 = Instance.new("Part")
part2.Name = "Part2"
part2.Anchored = true
part2.Transparency = 0.5
part2.Color = Color3.fromRGB(200, 10, 0)
part2.Size = Vector3.new(2, 2, 2)
part2.Position = Vector3.new(0, 5, 0)
part2.Parent = workspace

local partList = { part1 }

print(workspace:ArePartsTouchingOthers(partList, 0)) -- True
print(workspace:ArePartsTouchingOthers(partList, 0.999)) -- True
print(workspace:ArePartsTouchingOthers(partList, 1)) -- False
```

### Method: WorldRoot:Blockcast

**Signature:** `WorldRoot:Blockcast(cframe: CFrame, size: Vector3, direction: Vector3, params?: RaycastParams): RaycastResult?`

Casts a block shape in a given direction and returns the first collision
with a [BasePart](/docs/reference/engine/classes/BasePart.md) or [Terrain](/docs/reference/engine/classes/Terrain.md) cell. This is analogous to how
[WorldRoot:Raycast()](/docs/reference/engine/classes/WorldRoot.md) casts a linear ray in a direction to find a
collision, but it uses a 3D shape instead of a ray.

Unlike [WorldRoot:GetPartsInPart()](/docs/reference/engine/classes/WorldRoot.md), this method does not detect
[BaseParts](/docs/reference/engine/classes/BasePart.md) that **initially** intersect the shape.

If a hit is detected, a [RaycastResult](/docs/reference/engine/datatypes/RaycastResult.md) is returned containing
the hit information. The [Distance](/docs/reference/engine/datatypes/RaycastResult.md)
property represents the distance the shape has to travel to find a hit,
and the [Position](/docs/reference/engine/datatypes/RaycastResult.md) property represents the
intersection point that causes the hit.

This method throws an error if it is passed invalid [CFrame](/docs/reference/engine/datatypes/CFrame.md),
size, or direction inputs.

*Security: None · Thread Safety: Safe · Simulation Access: true*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `cframe` | `CFrame` |  | The initial position and rotation of the cast block shape. |
| `size` | `Vector3` |  | The size of the cast block shape in studs. The maximum size is 512 studs. |
| `direction` | `Vector3` |  | Direction of the shapecast, with the magnitude representing the maximum distance the shape can travel. The maximum distance is 1024 studs. |
| `params` | `RaycastParams` | `RaycastParams{IgnoreWater=false, BruteForceAllSlow=false, RespectCanCollide=false, CollisionGroup=Default, FilterDescendantsInstances={}}` | An object used to specify hit eligibility in the shapecast operation. If not provided, default values are used where all parts are considered and [Terrain](/docs/reference/engine/classes/Terrain.md) water is not ignored. |

**Returns:** `RaycastResult?` — Contains the result of the shapecast operation, or `nil` if no
eligible [BasePart](/docs/reference/engine/classes/BasePart.md) or [Terrain](/docs/reference/engine/classes/Terrain.md) cell was hit.

**Blockcasting**

Casts a block and returns the first collision with a [BasePart](/docs/reference/engine/classes/BasePart.md) or
[Terrain](/docs/reference/engine/classes/Terrain.md). Prints the properties of the RaycastResult if a result was
hit.

```lua
local Workspace = game:GetService("Workspace")

local function castBlock()
	-- The initial position and rotation of the cast block shape
	local originCFrame = CFrame.new(Vector3.new(0, 50, 0))
	-- The size of the cast block shape
	local size = Vector3.new(6, 3, 9)
	-- The direction the block is cast in
	local direction = -Vector3.yAxis
	-- The maximum distance of the cast
	local distance = 50

	-- Cast the block and create a visualization of it
	local raycastResult = Workspace:Blockcast(originCFrame, size, direction * distance)

	if raycastResult then
		-- Print all properties of the RaycastResult if it exists
		print(`Block intersected with: {raycastResult.Instance:GetFullName()}`)
		print(`Intersection position: {raycastResult.Position}`)
		print(`Distance between block's initial position and result: {raycastResult.Distance}`)
		print(`The normal vector of the intersected face: {raycastResult.Normal}`)
		print(`Material hit: {raycastResult.Material.Name}`)
	else
		print("Nothing was hit")
	end
end

-- Continually cast a block every 2 seconds
while true do
	castBlock()
	task.wait(2)
end
```

### Method: WorldRoot:BulkMoveTo

**Signature:** `WorldRoot:BulkMoveTo(partList: Instances, cframeList: Array, eventMode?: BulkMoveMode): ()`

This function moves an array of [BaseParts](/docs/reference/engine/classes/BasePart.md) to an array of
[CFrames](/docs/reference/engine/datatypes/CFrame.md) without necessarily firing the default property
[Changed](/docs/reference/engine/classes/Object.md) events. This provides a very fast way to
move large numbers of parts, as you don't have to pay the cost of separate
property sets for each individual part.

Both `partList` and `cframeList` are sequential arrays (Luau tables with
integer indices starting at 1), not dictionaries. Each part at index `i`
in `partList` is moved to the [CFrame](/docs/reference/engine/datatypes/CFrame.md) at index `i` in
`cframeList`. The arrays must contain the same number of entries.

```lua
local Workspace = game:GetService("Workspace")

local partList = { Workspace.Part1, Workspace.Part2 }
local cframeList = { CFrame.new(0, 5, 0), CFrame.new(10, 5, 0) }
Workspace:BulkMoveTo(partList, cframeList, Enum.BulkMoveMode.FireCFrameChanged)
```

The third argument allows you to further optimize the movement operation.
By default, the [Changed](/docs/reference/engine/classes/Object.md) event of each part fires
for [Position](/docs/reference/engine/classes/BasePart.md),
[Orientation](/docs/reference/engine/classes/BasePart.md), and
[CFrame](/docs/reference/engine/classes/BasePart.md). However, if you specify
[FireCFrameChanged](/docs/reference/engine/enums/BulkMoveMode.md) as the third argument, only the
[Changed](/docs/reference/engine/classes/Object.md) event for the
[CFrame](/docs/reference/engine/classes/BasePart.md) property will fire.

Note that you should only use this function if you're sure that part
movement is a bottleneck in your code. Simply setting the
[CFrame](/docs/reference/engine/classes/BasePart.md) property of individual parts and welded
models is fast enough in the majority of cases.

*Security: None · Thread Safety: Unsafe · Simulation Access: true*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `partList` | `Instances` |  | An array of [BaseParts](/docs/reference/engine/classes/BasePart.md) to be moved. Each entry is matched by index to the corresponding entry in `cframeList`. |
| `cframeList` | `Array` |  | An array of [CFrames](/docs/reference/engine/datatypes/CFrame.md) that the parts will be moved to, matched by index to `partList`. Both arrays must be the same length. |
| `eventMode` | `BulkMoveMode` | `FireAllEvents` | An [BulkMoveMode](/docs/reference/engine/enums/BulkMoveMode.md) enum specifying which [Changed](/docs/reference/engine/classes/Object.md) events fire during the move. Default is [FireAllEvents](/docs/reference/engine/enums/BulkMoveMode.md). |

**Returns:** `()`

### Method: WorldRoot:CollisionGroupsAreCollidable

**Signature:** `WorldRoot:CollisionGroupsAreCollidable(name1: string, name2: string): boolean`

Returns whether the two specified collision groups will collide in this
world. This method will also return `true` if either of the groups are
unregistered in this world, as the default collision mask collides with
all groups.

*Security: None · Thread Safety: Unsafe · Capabilities: Physics · Simulation Access: true*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `name1` | `string` |  |  |
| `name2` | `string` |  |  |

**Returns:** `boolean`

### Method: WorldRoot:CollisionGroupSetCollidable

**Signature:** `WorldRoot:CollisionGroupSetCollidable(name1: string, name2: string, collidable: boolean): ()`

Sets the collision status between two groups in this world. This method
will throw an error if either of the groups is unregistered in this world,
so it's recommended that you confirm each group's registration through
[WorldRoot:IsCollisionGroupRegistered()](/docs/reference/engine/classes/WorldRoot.md) before making this call.

*Security: None · Thread Safety: Unsafe · Capabilities: Physics · Simulation Access: true*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `name1` | `string` |  |  |
| `name2` | `string` |  |  |
| `collidable` | `boolean` |  |  |

**Returns:** `()`

### Method: WorldRoot:GetMaxCollisionGroups

**Signature:** `WorldRoot:GetMaxCollisionGroups(): int`

Returns the maximum number of collision groups the engine supports per
world. This value is currently 32.

*Security: None · Thread Safety: Unsafe · Capabilities: Physics · Simulation Access: true*

**Returns:** `int`

### Method: WorldRoot:GetPartBoundsInBox

**Signature:** `WorldRoot:GetPartBoundsInBox(cframe: CFrame, size: Vector3, overlapParams?: OverlapParams): List<BasePart>`

[WorldRoot:GetPartBoundsInBox()](/docs/reference/engine/classes/WorldRoot.md) returns an array of parts whose
**bounding boxes** overlap a box whose volume is described using the given
center ([CFrame](/docs/reference/engine/datatypes/CFrame.md)) and size ([Vector3](/docs/reference/engine/datatypes/Vector3.md)).

As emphasized, this spatial query method efficiently considers the volume
of parts' bounding boxes rather than their actual occupied volume. This
may be important when considering cylinders, spheres, unions, and
[MeshParts](/docs/reference/engine/classes/MeshPart.md) which have non-block shapes. For cases where
accuracy especially matters, use [WorldRoot:GetPartsInPart()](/docs/reference/engine/classes/WorldRoot.md)
instead, or further filter the results of this method yourself.

This method uses a [OverlapParams](/docs/reference/engine/datatypes/OverlapParams.md) object to describe reusable
portions of the spatial query, such as an inclusion or exclusion list, the
maximum number of parts to query, what
[collision group](/docs/en-us/workspace/collisions.md#collision-filtering) to
use, and whether the query favors an intersected part's
[BasePart.CanCollide](/docs/reference/engine/classes/BasePart.md) value over its [BasePart.CanQuery](/docs/reference/engine/classes/BasePart.md)
value.

*Security: None · Thread Safety: Safe · Simulation Access: true*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `cframe` | `CFrame` |  | The location of the center of the given box volume to be queried. |
| `size` | `Vector3` |  | The size of the given box volume to be queried. |
| `overlapParams` | `OverlapParams` | `OverlapParams{MaxParts=0, Tolerance=0, BruteForceAllSlow=false, RespectCanCollide=false, CollisionGroup=Default, FilterDescendantsInstances={}}` | Contains reusable portions of the spatial query parameters. |

**Returns:** `List<BasePart>` — An array of [BaseParts](/docs/reference/engine/classes/BasePart.md) which matched the spatial
query.

### Method: WorldRoot:GetPartBoundsInRadius

**Signature:** `WorldRoot:GetPartBoundsInRadius(position: Vector3, radius: float, overlapParams?: OverlapParams): List<BasePart>`

[WorldRoot:GetPartBoundsInRadius()](/docs/reference/engine/classes/WorldRoot.md) returns an array of parts whose
**bounding boxes** overlap a sphere whose volume is described using the
given center ([Vector3](/docs/reference/engine/datatypes/Vector3.md)) and radius (number).

As emphasized, this spatial query method efficiently considers the volume
of parts' bounding boxes rather than their actual occupied volume. This
may be important when considering cylinders, spheres, unions, and
[MeshParts](/docs/reference/engine/classes/MeshPart.md) which have non-block shapes. For cases where
accuracy especially matters, use [WorldRoot:GetPartsInPart()](/docs/reference/engine/classes/WorldRoot.md)
instead, or further filter the results of this method yourself.

This method uses a [OverlapParams](/docs/reference/engine/datatypes/OverlapParams.md) object to describe reusable
portions of the spatial query, such as an inclusion or exclusion list, the
maximum number of parts to query, what
[collision group](/docs/en-us/workspace/collisions.md#collision-filtering) to
use, and whether the query favors an intersected part's
[BasePart.CanCollide](/docs/reference/engine/classes/BasePart.md) value over its [BasePart.CanQuery](/docs/reference/engine/classes/BasePart.md)
value.

*Security: None · Thread Safety: Safe · Simulation Access: true*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `position` | `Vector3` |  | The location of the center of the given sphere volume to be queried. |
| `radius` | `float` |  | The radius of the given sphere volume to be queried. |
| `overlapParams` | `OverlapParams` | `OverlapParams{MaxParts=0, Tolerance=0, BruteForceAllSlow=false, RespectCanCollide=false, CollisionGroup=Default, FilterDescendantsInstances={}}` | Contains reusable portions of the spatial query parameters. |

**Returns:** `List<BasePart>` — An array of [BaseParts](/docs/reference/engine/classes/BasePart.md) which matched the spatial
query.

### Method: WorldRoot:GetPartsInPart

**Signature:** `WorldRoot:GetPartsInPart(part: BasePart, overlapParams?: OverlapParams): List<BasePart>`

[WorldRoot:GetPartsInPart()](/docs/reference/engine/classes/WorldRoot.md) returns an array of parts whose
occupied space is shared with the given part (which must exist in the same
[WorldRoot](/docs/reference/engine/classes/WorldRoot.md) as the parts to be queried). This method can be used in
place of [BasePart:GetTouchingParts()](/docs/reference/engine/classes/BasePart.md) and is generally a better
choice.

As noted, this spatial query method considers the **exact volume**
occupied by the given part using a full geometric collision check. As an
example, a concave/hollow part won't match queried parts within it unless
they actually overlap/touch such a part. For simpler volumes, consider
using [WorldRoot:GetPartBoundsInBox()](/docs/reference/engine/classes/WorldRoot.md) or
[WorldRoot:GetPartBoundsInRadius()](/docs/reference/engine/classes/WorldRoot.md), as they are less accurate but
perform more efficiently.

This method uses a [OverlapParams](/docs/reference/engine/datatypes/OverlapParams.md) object to describe reusable
portions of the spatial query, such as an inclusion or exclusion list, the
maximum number of parts to query, what
[collision group](/docs/en-us/workspace/collisions.md#collision-filtering) to
use, and whether the query favors an intersected part's
[BasePart.CanCollide](/docs/reference/engine/classes/BasePart.md) value over its [BasePart.CanQuery](/docs/reference/engine/classes/BasePart.md)
value.

*Security: None · Thread Safety: Safe · Simulation Access: true*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `part` | `BasePart` |  | The part whose volume is to be checked against other parts. |
| `overlapParams` | `OverlapParams` | `OverlapParams{MaxParts=0, Tolerance=0, BruteForceAllSlow=false, RespectCanCollide=false, CollisionGroup=Default, FilterDescendantsInstances={}}` | Contains reusable portions of the spatial query parameters. |

**Returns:** `List<BasePart>` — An array of [BaseParts](/docs/reference/engine/classes/BasePart.md) which matched the spatial
query.

### Method: WorldRoot:GetRegisteredCollisionGroups

**Signature:** `WorldRoot:GetRegisteredCollisionGroups(): Array`

Returns a table with info on all of this world's collision groups. Each
value in the returned table is itself a table and containing two members:

| Member | Type | Description |
| --- | --- | --- |
| mask | integer | The collision group's mask; only for internal use. |
| name | string | Name of the collision group. |

*Security: None · Thread Safety: Unsafe · Capabilities: Physics · Simulation Access: true*

**Returns:** `Array`

### Method: WorldRoot:IKMoveTo

**Signature:** `WorldRoot:IKMoveTo(part: BasePart, target: CFrame, translateStiffness?: float, rotateStiffness?: float, collisionsMode?: IKCollisionsMode): ()`

This function moves the specified part to the specified location via
[inverse kinematics](https://en.wikipedia.org/wiki/Inverse_kinematics)
rather than moving it there directly, to ensure any joints,
[constraints](/docs/reference/engine/classes/Constraint.md), or collisions that part is participating
in remain physically satisfied. Currently this function is only available
in Studio to [plugins](/docs/reference/engine/classes/Plugin.md), as it currently conflicts with the
physics of a running game.

**Translate stiffness** is a number between 0 and 1 specifying how
aggressively to match the part's position to the position part of the
target CFrame. **Rotate stiffness** is a number between 0 and 1 specifying
how aggressively to match the part's rotation to the rotation part of the
target CFrame.

For example:

- If translate stiffness and rotate stiffness are both equal to 1, then
  the part will be moved exactly to the target CFrame regardless of what
  physical constraints there are on it.
- If translate stiffness and rotate stiffness are both equal to 0.5, then
  the part will try to move to exactly the target CFrame, but may be
  pushed out of the way by physical constraints on it.
- If translate stiffness and rotate stiffness are both equal to 0, then
  the target CFrame will be ignored and physical constraints will be
  solved for the object at the position where it was.

*Security: PluginSecurity · Thread Safety: Unsafe · Simulation Access: true*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `part` | `BasePart` |  | The part being moved. |
| `target` | `CFrame` |  | The location to move the specified part. |
| `translateStiffness` | `float` | `0.5` | A number between 0 and 1 specifying how aggressively to match the part's position to the position part of the target [CFrame](/docs/reference/engine/datatypes/CFrame.md). |
| `rotateStiffness` | `float` | `0.5` | A number between 0 and 1 specifying how aggressively to match the part's rotation to the rotation part of the target [CFrame](/docs/reference/engine/datatypes/CFrame.md). |
| `collisionsMode` | `IKCollisionsMode` | `OtherMechanismsAnchored` | Allows you to specify what objects should be effected by the physical resolution. |

**Returns:** `()`

### Method: WorldRoot:IsCollisionGroupRegistered

**Signature:** `WorldRoot:IsCollisionGroupRegistered(name: string): boolean`

Checks if a collision group is registered in this world. It's recommended
that you call this method before calling methods that throw errors for
unregistered collision groups, such as
[WorldRoot:CollisionGroupSetCollidable()](/docs/reference/engine/classes/WorldRoot.md).

*Security: None · Thread Safety: Unsafe · Capabilities: Physics · Simulation Access: true*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `name` | `string` |  |  |

**Returns:** `boolean`

### Method: WorldRoot:Raycast

**Signature:** `WorldRoot:Raycast(origin: Vector3, direction: Vector3, raycastParams?: RaycastParams): RaycastResult?`

Casts a ray using an origin, direction, and optional
[RaycastParams](/docs/reference/engine/datatypes/RaycastParams.md). If it finds an eligible [BasePart](/docs/reference/engine/classes/BasePart.md) or
[Terrain](/docs/reference/engine/classes/Terrain.md) cell, a [RaycastResult](/docs/reference/engine/datatypes/RaycastResult.md) is returned containing
the results of the operation. If no [RaycastParams](/docs/reference/engine/datatypes/RaycastParams.md) object is
provided, the defaults are used (all parts are considered and
[Terrain](/docs/reference/engine/classes/Terrain.md) water is not ignored).

Note that the length (magnitude) of the directional vector is important,
as objects/terrain further away than its length will not be tested. If
you're using a [CFrame](/docs/reference/engine/datatypes/CFrame.md) to help create the ray components,
consider using [CFrame.LookVector](/docs/reference/engine/datatypes/CFrame.md) as the directional vector and
multiply it by the desired length as shown in the example below. The
maximum length of the direction vector is 15,000 studs.

This method does **not** use a [Ray](/docs/reference/engine/datatypes/Ray.md) object, but its origin and
direction components can be borrowed from [Ray.Origin](/docs/reference/engine/datatypes/Ray.md) and
[Ray.Direction](/docs/reference/engine/datatypes/Ray.md).

*Security: None · Thread Safety: Safe · Simulation Access: true*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `origin` | `Vector3` |  | The origin point of the ray. |
| `direction` | `Vector3` |  | The directional vector of the ray. Note that the length of this vector matters, as parts/terrain further away than its length will not be tested. |
| `raycastParams` | `RaycastParams` | `RaycastParams{IgnoreWater=false, BruteForceAllSlow=false, RespectCanCollide=false, CollisionGroup=Default, FilterDescendantsInstances={}}` | An object used to specify hit eligibility in the raycast operation. If not provided, default values are used where all parts are considered and [Terrain](/docs/reference/engine/classes/Terrain.md) water is not ignored. |

**Returns:** `RaycastResult?` — Contains the results of a raycast operation, or `nil` if no eligible
[BasePart](/docs/reference/engine/classes/BasePart.md) or [Terrain](/docs/reference/engine/classes/Terrain.md) cell was hit.

**Raycasting**

Casts a ray and returns the first collision with a [BasePart](/docs/reference/engine/classes/BasePart.md) or
[Terrain](/docs/reference/engine/classes/Terrain.md). Prints the properties of the RaycastResult if a result was
hit.

```lua
local Workspace = game:GetService("Workspace")

local function castRay()
	-- The origin point of the ray
	local originPosition = Vector3.new(0, 50, 0)
	-- The direction the ray is cast in
	local direction = -Vector3.yAxis
	-- The maximum distance of the ray
	local distance = 50

	-- Cast the ray and create a visualization of it
	local raycastResult = Workspace:Raycast(originPosition, direction * distance)

	if raycastResult then
		-- Print all properties of the RaycastResult if it exists
		print(`Ray intersected with: {raycastResult.Instance:GetFullName()}`)
		print(`Intersection position: {raycastResult.Position}`)
		print(`Distance between ray origin and result: {raycastResult.Distance}`)
		print(`The normal vector of the intersected face: {raycastResult.Normal}`)
		print(`Material hit: {raycastResult.Material.Name}`)
	else
		print("Nothing was hit")
	end
end

-- Continually cast a ray every 2 seconds
while true do
	castRay()
	task.wait(2)
end
```

### Method: WorldRoot:RegisterCollisionGroup

**Signature:** `WorldRoot:RegisterCollisionGroup(name: string): ()`

Registers a new collision group in this world with the given name. The
name cannot be `"Default"`.

Note that this method has a slight performance overhead based on the
number of [BaseParts](/docs/reference/engine/classes/BasePart.md) in the world, so it's recommended
that you register all collision groups at edit time through the Studio
[editor](/docs/en-us/workspace/collisions.md#collision-groups) and call
[UnregisterCollisionGroup()](/docs/reference/engine/classes/WorldRoot.md)
and [RenameCollisionGroup()](/docs/reference/engine/classes/WorldRoot.md) as
infrequently as possible.

*Security: None · Thread Safety: Unsafe · Capabilities: Physics · Simulation Access: true*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `name` | `string` |  |  |

**Returns:** `()`

### Method: WorldRoot:RenameCollisionGroup

**Signature:** `WorldRoot:RenameCollisionGroup(from: string, to: string): ()`

Renames the specified registered collision group in this world, but does
**not** rename the [CollisionGroup](/docs/reference/engine/classes/BasePart.md) property
of parts that utilize the group. The first argument of this method is the
name of the group to rename, the second argument is the new name for the
group. If the specified group does not exist, this method will not do
anything. The naming conventions for the new name follow the same rules as
if the group was being created with
[RegisterCollisionGroup()](/docs/reference/engine/classes/WorldRoot.md).

This method will throw a runtime error in the following circumstances:

- Invalid or empty name provided for either argument.
- The method is called from a client.

Note that this method has a slight performance overhead based on the
number of [BaseParts](/docs/reference/engine/classes/BasePart.md) in the world, so it's recommended
that you register all collision groups at edit time through the Studio
[editor](/docs/en-us/workspace/collisions.md#collision-groups) and rename
them as infrequently as possible.

*Security: None · Thread Safety: Unsafe · Capabilities: Physics · Simulation Access: true*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `from` | `string` |  |  |
| `to` | `string` |  |  |

**Returns:** `()`

### Method: WorldRoot:Shapecast

**Signature:** `WorldRoot:Shapecast(part: BasePart, direction: Vector3, params?: RaycastParams, cframeOverride?: CFrame?, sizeOverride?: Vector3?): RaycastResult?`

Casts the shape of the given [BasePart](/docs/reference/engine/classes/BasePart.md) in a given direction and
returns the first collision with a [BasePart](/docs/reference/engine/classes/BasePart.md) or [Terrain](/docs/reference/engine/classes/Terrain.md)
cell. This is analogous to how [WorldRoot:Raycast()](/docs/reference/engine/classes/WorldRoot.md) casts a linear
ray in a direction to find a collision, but it uses a 3D shape instead of
a ray. Unlike [WorldRoot:Blockcast()](/docs/reference/engine/classes/WorldRoot.md) and
[WorldRoot:Spherecast()](/docs/reference/engine/classes/WorldRoot.md), which use a simple box or sphere, this
method casts the actual geometry of the provided part.

Unlike [WorldRoot:GetPartsInPart()](/docs/reference/engine/classes/WorldRoot.md), this method does not detect
[BaseParts](/docs/reference/engine/classes/BasePart.md) that **initially** intersect the shape.

If a hit is detected, a [RaycastResult](/docs/reference/engine/datatypes/RaycastResult.md) is returned containing
the hit information. The [Distance](/docs/reference/engine/datatypes/RaycastResult.md)
property represents the distance the shape has to travel to find a hit,
and the [Position](/docs/reference/engine/datatypes/RaycastResult.md) property represents the
intersection point that causes the hit.

This method throws an error if it is passed a non-existent part, an
invalid direction, or a part with [Terrain](/docs/reference/engine/classes/Terrain.md) geometry.

*Security: None · Thread Safety: Unsafe · Simulation Access: true*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `part` | `BasePart` |  | The part whose shape is cast. The cast uses this part's geometry (block, ball, mesh, and so on) and size; excessively large parts may not be supported, and it cannot be a [Terrain](/docs/reference/engine/classes/Terrain.md) part. |
| `direction` | `Vector3` |  | Direction of the shapecast, with the magnitude representing the maximum distance the shape can travel. The maximum distance is 1024 studs. |
| `params` | `RaycastParams` | `RaycastParams{IgnoreWater=false, BruteForceAllSlow=false, RespectCanCollide=false, CollisionGroup=Default, FilterDescendantsInstances={}}` | An object used to specify hit eligibility in the shapecast operation. If not provided, default values are used where all other parts are considered and [Terrain](/docs/reference/engine/classes/Terrain.md) water is not ignored. The part being cast is always excluded from the results. |
| `cframeOverride` | `CFrame?` | `nil` | The [CFrame](/docs/reference/engine/datatypes/CFrame.md) from which the shape begins the cast. If not provided, the part's own [CFrame](/docs/reference/engine/classes/BasePart.md) is used. |
| `sizeOverride` | `Vector3?` | `nil` | The size of the cast shape. If not provided, the part's own [Size](/docs/reference/engine/classes/BasePart.md) is used. Every component must be finite and greater than or equal to `0`, and the shape must not exceed the maximum supported side length. |

**Returns:** `RaycastResult?` — Contains the result of the shapecast operation, or `nil` if no
eligible [BasePart](/docs/reference/engine/classes/BasePart.md) or [Terrain](/docs/reference/engine/classes/Terrain.md) cell was hit.

### Method: WorldRoot:Spherecast

**Signature:** `WorldRoot:Spherecast(position: Vector3, radius: float, direction: Vector3, params?: RaycastParams): RaycastResult?`

Casts a spherical shape in a given direction and returns the first
collision with a [BasePart](/docs/reference/engine/classes/BasePart.md) or [Terrain](/docs/reference/engine/classes/Terrain.md) cell. This is
analogous to how [WorldRoot:Raycast()](/docs/reference/engine/classes/WorldRoot.md) casts a linear ray in a
direction to find a collision, but it uses a 3D shape instead of a ray.

Unlike [WorldRoot:GetPartsInPart()](/docs/reference/engine/classes/WorldRoot.md), this method does not detect
[BaseParts](/docs/reference/engine/classes/BasePart.md) that **initially** intersect the shape.

If a hit is detected, a [RaycastResult](/docs/reference/engine/datatypes/RaycastResult.md) is returned containing
the hit information. The [Distance](/docs/reference/engine/datatypes/RaycastResult.md)
property represents the distance the shape has to travel to find a hit,
and the [Position](/docs/reference/engine/datatypes/RaycastResult.md) property represents the
intersection point that causes the hit.

This method throws an error if it is passed invalid radius or direction
inputs.

*Security: None · Thread Safety: Safe · Simulation Access: true*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `position` | `Vector3` |  | The initial position of the cast spherical shape. |
| `radius` | `float` |  | The radius of the cast spherical shape in studs. The maximum radius is 256 studs. |
| `direction` | `Vector3` |  | Direction of the shapecast, with the magnitude representing the maximum distance the shape can travel. The maximum distance is 1024 studs. |
| `params` | `RaycastParams` | `RaycastParams{IgnoreWater=false, BruteForceAllSlow=false, RespectCanCollide=false, CollisionGroup=Default, FilterDescendantsInstances={}}` | An object used to specify hit eligibility in the shapecast operation. If not provided, default values are used where all parts are considered and [Terrain](/docs/reference/engine/classes/Terrain.md) water is not ignored. |

**Returns:** `RaycastResult?` — Contains the result of the shapecast operation, or `nil` if no
eligible [BasePart](/docs/reference/engine/classes/BasePart.md) or [Terrain](/docs/reference/engine/classes/Terrain.md) cell was hit.

**Spherecasting**

Casts a sphere and returns the first collision with a [BasePart](/docs/reference/engine/classes/BasePart.md) or
[Terrain](/docs/reference/engine/classes/Terrain.md). Prints the properties of the RaycastResult if a result was
hit.

```lua
local Workspace = game:GetService("Workspace")

local function castSphere()
	-- The initial position of the cast spherical shape
	local originPosition = Vector3.new(0, 50, 0)
	-- The radius of the cast spherical shape in studs
	local radius = 10
	-- The direction the sphere is cast in
	local direction = -Vector3.yAxis
	-- The maximum distance of the cast
	local distance = 50

	-- Cast the sphere and create a visualization of it
	local raycastResult = Workspace:Spherecast(originPosition, radius, direction * distance)

	if raycastResult then
		-- Print all properties of the RaycastResult if it exists
		print(`Sphere intersected with: {raycastResult.Instance:GetFullName()}`)
		print(`Intersection position: {raycastResult.Position}`)
		print(`Distance between sphere's initial position and result: {raycastResult.Distance}`)
		print(`The normal vector of the intersected face: {raycastResult.Normal}`)
		print(`Material hit: {raycastResult.Material.Name}`)
	else
		print("Nothing was hit")
	end
end

-- Continually cast a sphere every 2 seconds
while true do
	castSphere()
	task.wait(2)
end
```

### Method: WorldRoot:StepPhysics

**Signature:** `WorldRoot:StepPhysics(dt: float, parts?: Instances): ()`

Advances the simulation for parts in the world forward based on a
specified time increment and an optional set of [BasePart](/docs/reference/engine/classes/BasePart.md). When a
set of parts is specified, only these parts will be simulated and all
other parts in the world will be treated as anchored. When this argument
is left out, all parts in the world will be included in the simulation.
The specified time increment can be any positive number, with larger
values increasing the runtime of the function. Depending on the value of
the time increment, the physics system may subdivide it into multiple
individual steps to maintain the accuracy and stability of the simulation.
Even if the function performs multiple substeps, the results of the
simulation will only be seen once the function completes. To visualize the
individual steps of a simulation, the function can be called once per
RenderStep via the [RunService.RenderStepped](/docs/reference/engine/classes/RunService.md) event.

*Security: PluginSecurity · Thread Safety: Unsafe*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `dt` | `float` |  | The amount of time that will be simulated. This argument must be a positive number. Larger values will increase the runtime of this function. |
| `parts` | `Instances` | `{}` | Optional array of parts that will be simulated. This set must contain instances that are of type [BasePart](/docs/reference/engine/classes/BasePart.md); any other types will be ignored. |

**Returns:** `()`

**StepPhysics**

Simulates the parts in the workspace for a fixed period of time by calling the
StepPhysics function once per frame until a specified time has elaspsed.

```lua
local RunService = game:GetService("RunService")

-- Optional array of parts to simulate; otherwise all parts will be simulated
local partsToSimulate = {
	workspace.Part,
}

local function simulateParts(duration)
	local time = 0.0
	local stepJob

	stepJob = RunService.RenderStepped:Connect(function(dt)
		if time + dt > duration then
			dt = duration - time
		end

		workspace:StepPhysics(dt, partsToSimulate)
		time = time + dt
		if time >= duration then
			stepJob:Disconnect()
		end
	end)
end

-- Simulate workspace parts for 5 seconds, stepping the parts once per frame
simulateParts(5.0)
```

### Method: WorldRoot:UnregisterCollisionGroup

**Signature:** `WorldRoot:UnregisterCollisionGroup(name: string): ()`

Unregisters the collision group for the given name in this world, with the
following behaviors:

- If an invalid name is provided, the method will not do anything.
- If the reserved name `"Default"` is provided **or** if the method is
  called from a client, it will throw an error.
- If there are any parts in the collision group when it is removed, those
  parts will still maintain the same collision group name. The physical
  behavior of parts in a removed group is undefined, so it's recommended
  to move any parts in a removed group to another group, such as the
  `"Default"` group.

Note that this method has a slight performance overhead based on the
number of [BaseParts](/docs/reference/engine/classes/BasePart.md) in the world, so it's recommended
that you register all collision groups at edit time through the Studio
[editor](/docs/en-us/workspace/collisions.md#collision-groups) and call this
method as infrequently as possible.

*Security: None · Thread Safety: Unsafe · Capabilities: Physics · Simulation Access: true*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `name` | `string` |  |  |

**Returns:** `()`

### Method: WorldRoot:FindPartOnRay

**Signature:** `WorldRoot:FindPartOnRay(ray: Ray, ignoreDescendantsInstance?: Instance, terrainCellsAreCubes?: boolean, ignoreWater?: boolean): Tuple`

> **Deprecated:** This function has been deprecated. Use [WorldRoot:Raycast()](/docs/reference/engine/classes/WorldRoot.md) along with [RaycastParams](/docs/reference/engine/datatypes/RaycastParams.md) for new work.

**FindPartOnRay** uses [raycasting](/docs/en-us/workspace/raycasting.md) to
find the first [BasePart](/docs/reference/engine/classes/BasePart.md) or [Terrain](/docs/reference/engine/classes/Terrain.md) cell intersecting with
a given [Ray](/docs/reference/engine/datatypes/Ray.md). This function returns the [BasePart](/docs/reference/engine/classes/BasePart.md) or
terrain cell hit, the point of intersection, the surface normal at the
point of intersection, and the associated [Material](/docs/reference/engine/enums/Material.md) hit.

If the `ignoreDescendantsInstance` parameter is provided, the raycasting
calculation will ignore the given object and all of its descendants. It
behaves similar to the [Mouse.TargetFilter](/docs/reference/engine/classes/Mouse.md) property.

The `terrainCellsAreCubes` and `ignoreWater` parameters determine whether
[Terrain](/docs/reference/engine/classes/Terrain.md) cells should be treated as cubes or not, and whether water
should be ignored or not.

In order to include or exclude multiple objects and their descendants, use
the [WorldRoot:FindPartOnRayWithWhitelist()](/docs/reference/engine/classes/WorldRoot.md) and
[WorldRoot:FindPartOnRayWithIgnoreList()](/docs/reference/engine/classes/WorldRoot.md) variants.

#### Notes

- Theoretically, a ray extends infinitely in one direction. However, the
  max length of the direction vector on Roblox is 15000 studs.
- The length (magnitude) of the directional vector is important, as parts
  further away than its length will not be tested.
- If the ray does not intersect anything, the return values will be `nil`
  and the point at the end of the ray, respectively.
- Parts that are in a
  [collision group](/docs/en-us/workspace/collisions.md#collision-filtering)
  that does not collide with the "Default" collision group are ignored
  implicitly.

*Security: None · Thread Safety: Unsafe*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `ray` | `Ray` |  | A [Ray](/docs/reference/engine/datatypes/Ray.md) whose origin and direction define the raycast. |
| `ignoreDescendantsInstance` | `Instance` | `nil` | An [Instance](/docs/reference/engine/classes/Instance.md) whose descendants are ignored in the raycast. |
| `terrainCellsAreCubes` | `boolean` | `false` | Whether [Terrain](/docs/reference/engine/classes/Terrain.md) cells are treated as full cubes when calculating intersection. Default is false. |
| `ignoreWater` | `boolean` | `false` | Whether [Terrain](/docs/reference/engine/classes/Terrain.md) water cells are ignored by the ray. Default is false. |

**Returns:** `Tuple` — The [BasePart](/docs/reference/engine/classes/BasePart.md) or [Terrain](/docs/reference/engine/classes/Terrain.md) cell hit, the
[Vector3](/docs/reference/engine/datatypes/Vector3.md) point of intersection, the [Vector3](/docs/reference/engine/datatypes/Vector3.md)
surface normal at the point of intersection, and the [Material](/docs/reference/engine/enums/Material.md)
of the [BasePart](/docs/reference/engine/classes/BasePart.md) or terrain cell hit.

### Method: WorldRoot:findPartOnRay

**Signature:** `WorldRoot:findPartOnRay(ray: Ray, ignoreDescendantsInstance?: Instance, terrainCellsAreCubes?: boolean, ignoreWater?: boolean): Tuple`

> **Deprecated:** This deprecated function is a variant of [WorldRoot:FindPartOnRay()](/docs/reference/engine/classes/WorldRoot.md) which should be used instead.

*Security: None · Thread Safety: Unsafe*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `ray` | `Ray` |  |  |
| `ignoreDescendantsInstance` | `Instance` | `nil` |  |
| `terrainCellsAreCubes` | `boolean` | `false` |  |
| `ignoreWater` | `boolean` | `false` |  |

**Returns:** `Tuple`

### Method: WorldRoot:FindPartOnRayWithIgnoreList

**Signature:** `WorldRoot:FindPartOnRayWithIgnoreList(ray: Ray, ignoreDescendantsTable: Instances, terrainCellsAreCubes?: boolean, ignoreWater?: boolean): Tuple`

> **Deprecated:** This function has been deprecated. Use [WorldRoot:Raycast()](/docs/reference/engine/classes/WorldRoot.md) along with [RaycastParams](/docs/reference/engine/datatypes/RaycastParams.md) for new work.

This function is a variant of [WorldRoot:FindPartOnRay()](/docs/reference/engine/classes/WorldRoot.md) with the
addition of an ignore list. This lets you ignore certain parts or
[Models](/docs/reference/engine/classes/Model.md).

Those looking to **include** a specific group of objects should instead
use [WorldRoot:FindPartOnRayWithWhitelist()](/docs/reference/engine/classes/WorldRoot.md).

*Security: None · Thread Safety: Unsafe*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `ray` | `Ray` |  | A [Ray](/docs/reference/engine/datatypes/Ray.md) whose origin and direction define the raycast. |
| `ignoreDescendantsTable` | `Instances` |  | An array of objects whose descendants are excluded from the raycast. |
| `terrainCellsAreCubes` | `boolean` | `false` | Whether [Terrain](/docs/reference/engine/classes/Terrain.md) cells are treated as full cubes when calculating intersection. Default is false. |
| `ignoreWater` | `boolean` | `false` | Whether [Terrain](/docs/reference/engine/classes/Terrain.md) water cells are ignored by the ray. Default is false. |

**Returns:** `Tuple` — The [BasePart](/docs/reference/engine/classes/BasePart.md) or [Terrain](/docs/reference/engine/classes/Terrain.md) cell hit, the
[Vector3](/docs/reference/engine/datatypes/Vector3.md) point of intersection, the [Vector3](/docs/reference/engine/datatypes/Vector3.md)
surface normal at the point of intersection, and the [Material](/docs/reference/engine/enums/Material.md)
of the [BasePart](/docs/reference/engine/classes/BasePart.md) or terrain cell hit.

### Method: WorldRoot:FindPartOnRayWithWhitelist

**Signature:** `WorldRoot:FindPartOnRayWithWhitelist(ray: Ray, whitelistDescendantsTable: Instances, ignoreWater?: boolean): Tuple`

> **Deprecated:** This function has been deprecated. Use [WorldRoot:Raycast()](/docs/reference/engine/classes/WorldRoot.md) along with [RaycastParams](/docs/reference/engine/datatypes/RaycastParams.md) for new work.

This function is a variant of [WorldRoot:FindPartOnRay()](/docs/reference/engine/classes/WorldRoot.md) with the
addition of an inclusion list. This lets you detect only certain parts or
[Models](/docs/reference/engine/classes/Model.md) and is particularly useful when, for example, looking
for points of intersection between a ray and a single part.

If a `nil` value is given in the inclusion list, instances after it will
be disregarded.

Those looking to **exclude** a specific group of objects should instead
use [WorldRoot:FindPartOnRayWithIgnoreList()](/docs/reference/engine/classes/WorldRoot.md).

*Security: None · Thread Safety: Unsafe*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `ray` | `Ray` |  | A [Ray](/docs/reference/engine/datatypes/Ray.md) whose origin and direction define the raycast. |
| `whitelistDescendantsTable` | `Instances` |  | An array of objects whose descendants are the only candidates considered in the raycast. |
| `ignoreWater` | `boolean` | `false` | Whether [Terrain](/docs/reference/engine/classes/Terrain.md) water cells are ignored by the ray. Default is false. |

**Returns:** `Tuple` — The [BasePart](/docs/reference/engine/classes/BasePart.md) or [Terrain](/docs/reference/engine/classes/Terrain.md) cell hit, the
[Vector3](/docs/reference/engine/datatypes/Vector3.md) point of intersection, the [Vector3](/docs/reference/engine/datatypes/Vector3.md)
surface normal at the point of intersection, and the [Material](/docs/reference/engine/enums/Material.md)
of the [BasePart](/docs/reference/engine/classes/BasePart.md) or terrain cell hit.

### Method: WorldRoot:FindPartsInRegion3

**Signature:** `WorldRoot:FindPartsInRegion3(region: Region3, ignoreDescendantsInstance?: Instance, maxParts?: int): List<BasePart>`

> **Deprecated:** This function has been deprecated. Use [WorldRoot:GetPartBoundsInBox()](/docs/reference/engine/classes/WorldRoot.md) along with [OverlapParams](/docs/reference/engine/datatypes/OverlapParams.md) for new work.

Returns an array of [BaseParts](/docs/reference/engine/classes/BasePart.md) in the given
[Region3](/docs/reference/engine/datatypes/Region3.md).

This function takes an optional maxParts parameter (default 20) which
limits the number of [BaseParts](/docs/reference/engine/classes/BasePart.md) that can be returned. Once
this number has been reached, the search for [BaseParts](/docs/reference/engine/classes/BasePart.md)
will stop. This means some [BaseParts](/docs/reference/engine/classes/BasePart.md) may not be returned
even if they are within the [Region3](/docs/reference/engine/datatypes/Region3.md)

The optional `ignoreDescendantsInstance` parameter can be used to specify
a specific instance for whom itself and all of its descendants should be
ignored by this function. This can be useful when, for example, looking to
see if any [BaseParts](/docs/reference/engine/classes/BasePart.md) are inside a [BasePart](/docs/reference/engine/classes/BasePart.md) other
than the [BasePart](/docs/reference/engine/classes/BasePart.md) itself.

```
local min = part.Position - (0.5 * part.Size)
local max = part.Position + (0.5 * part.Size)
local region = Region3.new(min, max)
local parts = worldroot:FindPartsInRegion3(region, part)  -- Ignore part
```

The [WorldRoot:FindPartsInRegion3WithIgnoreList()](/docs/reference/engine/classes/WorldRoot.md) and
[WorldRoot:FindPartsInRegion3WithWhiteList()](/docs/reference/engine/classes/WorldRoot.md) variants of this
method exist to provide specific exclusion and inclusion functionality.

If no [BaseParts](/docs/reference/engine/classes/BasePart.md) are found, an empty array will be
returned.

*Security: None · Thread Safety: Unsafe*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `region` | `Region3` |  | The [Region3](/docs/reference/engine/datatypes/Region3.md) to be checked. |
| `ignoreDescendantsInstance` | `Instance` | `nil` | An [Instance](/docs/reference/engine/classes/Instance.md) to be ignored. |
| `maxParts` | `int` | `20` | The maximum amount of [BaseParts](/docs/reference/engine/classes/BasePart.md) to be returned. |

**Returns:** `List<BasePart>` — An array of [BaseParts](/docs/reference/engine/classes/BasePart.md) within the [Region3](/docs/reference/engine/datatypes/Region3.md).

### Method: WorldRoot:findPartsInRegion3

**Signature:** `WorldRoot:findPartsInRegion3(region: Region3, ignoreDescendantsInstance?: Instance, maxParts?: int): List<BasePart>`

> **Deprecated:** This deprecated function is a variant of [WorldRoot:FindPartsInRegion3()](/docs/reference/engine/classes/WorldRoot.md) which should be used instead.

*Security: None · Thread Safety: Unsafe*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `region` | `Region3` |  |  |
| `ignoreDescendantsInstance` | `Instance` | `nil` |  |
| `maxParts` | `int` | `20` |  |

**Returns:** `List<BasePart>`

### Method: WorldRoot:FindPartsInRegion3WithIgnoreList

**Signature:** `WorldRoot:FindPartsInRegion3WithIgnoreList(region: Region3, ignoreDescendantsTable: Instances, maxParts?: int): List<BasePart>`

> **Deprecated:** This function has been deprecated. Use [WorldRoot:GetPartBoundsInBox()](/docs/reference/engine/classes/WorldRoot.md) along with [OverlapParams](/docs/reference/engine/datatypes/OverlapParams.md) for new work.

Returns an array of [BaseParts](/docs/reference/engine/classes/BasePart.md) in the given
[Region3](/docs/reference/engine/datatypes/Region3.md) that aren't in, or a descendant of an entry in, the
given ignore list.

If a `nil` value is given in the ignore list, instances after this value
will not be ignored. If no [BaseParts](/docs/reference/engine/classes/BasePart.md) are found, an empty
array will be returned.

This function is a variant of [WorldRoot:FindPartsInRegion3()](/docs/reference/engine/classes/WorldRoot.md) with
the addition of an ignore list. This allows the developer to exclude
certain [BaseParts](/docs/reference/engine/classes/BasePart.md) or [Models](/docs/reference/engine/classes/Model.md) from the
search. Those looking to find [BaseParts](/docs/reference/engine/classes/BasePart.md) in a
[Region3](/docs/reference/engine/datatypes/Region3.md) using an inclusion list should use
[WorldRoot:FindPartsInRegion3WithWhiteList()](/docs/reference/engine/classes/WorldRoot.md).

*Security: None · Thread Safety: Unsafe*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `region` | `Region3` |  | The [Region3](/docs/reference/engine/datatypes/Region3.md) to be checked. |
| `ignoreDescendantsTable` | `Instances` |  | An array of objects to be ignored. |
| `maxParts` | `int` | `20` | The maximum number of [BaseParts](/docs/reference/engine/classes/BasePart.md) to be returned. |

**Returns:** `List<BasePart>` — An array of [BaseParts](/docs/reference/engine/classes/BasePart.md) found within the
[Region3](/docs/reference/engine/datatypes/Region3.md).

### Method: WorldRoot:FindPartsInRegion3WithWhiteList

**Signature:** `WorldRoot:FindPartsInRegion3WithWhiteList(region: Region3, whitelistDescendantsTable: Instances, maxParts?: int): List<BasePart>`

> **Deprecated:** This function has been deprecated. Use [WorldRoot:GetPartBoundsInBox()](/docs/reference/engine/classes/WorldRoot.md) along with [OverlapParams](/docs/reference/engine/datatypes/OverlapParams.md) for new work.

Returns an array of [BaseParts](/docs/reference/engine/classes/BasePart.md) in the given
[Region3](/docs/reference/engine/datatypes/Region3.md) that are in, or descendant of an entry in, the given
inclusion list.

If a `nil` value is given in the inclusion list, instances after this
value will not be ignored. If no [BaseParts](/docs/reference/engine/classes/BasePart.md) are found, an
empty array will be returned.

This function is a variant of [WorldRoot:FindPartsInRegion3()](/docs/reference/engine/classes/WorldRoot.md) with
the addition of an inclusion list. This allows the developer to include
only certain [BaseParts](/docs/reference/engine/classes/BasePart.md) or [Models](/docs/reference/engine/classes/Model.md) in the
search. Those looking to find [BaseParts](/docs/reference/engine/classes/BasePart.md) in a
[Region3](/docs/reference/engine/datatypes/Region3.md) using an exclusion list should use
[WorldRoot:FindPartsInRegion3WithIgnoreList()](/docs/reference/engine/classes/WorldRoot.md).

*Security: None · Thread Safety: Unsafe*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `region` | `Region3` |  | The [Region3](/docs/reference/engine/datatypes/Region3.md) to be checked. |
| `whitelistDescendantsTable` | `Instances` |  | An array of objects to check. |
| `maxParts` | `int` | `20` | The maximum number of [BaseParts](/docs/reference/engine/classes/BasePart.md) to be returned. |

**Returns:** `List<BasePart>` — An array of [BaseParts](/docs/reference/engine/classes/BasePart.md) within the [Region3](/docs/reference/engine/datatypes/Region3.md).

### Method: WorldRoot:IsRegion3Empty

**Signature:** `WorldRoot:IsRegion3Empty(region: Region3, ignoreDescendentsInstance?: Instance): boolean`

> **Deprecated:** This function has been deprecated. Use [WorldRoot:GetPartBoundsInBox()](/docs/reference/engine/classes/WorldRoot.md) along with [OverlapParams](/docs/reference/engine/datatypes/OverlapParams.md) for new work.

**IsRegion3Empty** returns a bool indicating whether there are no
[BaseParts](/docs/reference/engine/classes/BasePart.md) within the given [Region3](/docs/reference/engine/datatypes/Region3.md).

The optional `ignoreDescendantsInstance` parameter can be used to specify
a specific instance for whom itself and all of its descendants should be
ignored by this function. This can be useful when, for example, looking to
see if any [BaseParts](/docs/reference/engine/classes/BasePart.md) are inside a [BasePart](/docs/reference/engine/classes/BasePart.md) other
than the [BasePart](/docs/reference/engine/classes/BasePart.md) itself.

```
local min = part.Position - (0.5 * part.Size)
local max = part.Position + (0.5 * part.Size)
local region = Region3.new(min, max)
local isPartEmpty = worldroot:IsRegion3Empty(region, part)  -- Ignore part
```

If more than one object and its descendants need to be excluded from the
search, developers should use
[WorldRoot:IsRegion3EmptyWithIgnoreList()](/docs/reference/engine/classes/WorldRoot.md).

This function only returns if a region is empty or not. Developers looking
to find [BaseParts](/docs/reference/engine/classes/BasePart.md) in a region should use
[WorldRoot:FindPartsInRegion3()](/docs/reference/engine/classes/WorldRoot.md).

#### How do Region3 checks work?

Checking if a part overlaps a [Region3](/docs/reference/engine/datatypes/Region3.md) is not a simple process.
It actually is time consuming and complicated. Instead it checks if parts
are roughly in the same area. When this function is called, it figures out
which voxels contain the [Region3](/docs/reference/engine/datatypes/Region3.md). It then figures out which
parts might be in those voxels. It does this by comparing the axis-aligned
bounding box (sometimes called the AABB) of the part with the voxels. The
axis-aligned bounding box can be seen in Roblox Studio when a part is
selected.

This means that the area that is inspected by the function may be larger
than the [Region3](/docs/reference/engine/datatypes/Region3.md). For this reason it is recommended to make
sure that the [Region3](/docs/reference/engine/datatypes/Region3.md) is on the voxel grid. The best way to do
this is by setting the coordinates of the [Region3](/docs/reference/engine/datatypes/Region3.md) to multiples
of 4 (since voxels are 4 x 4 x 4 studs).

This method is a fairly quick and easy way to see if any parts are in a
general area. If a game needs to know if parts are exactly in an area,
then [BasePart:GetTouchingParts()](/docs/reference/engine/classes/BasePart.md) should be used. There is a higher
cost to using [BasePart:GetTouchingParts()](/docs/reference/engine/classes/BasePart.md) since a part is needed
in the [WorldRoot](/docs/reference/engine/classes/WorldRoot.md) and the function takes more time to run.

*Security: None · Thread Safety: Unsafe*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `region` | `Region3` |  | The [Region3](/docs/reference/engine/datatypes/Region3.md) to be checked. |
| `ignoreDescendentsInstance` | `Instance` | `nil` | An [Instance](/docs/reference/engine/classes/Instance.md) to be ignored. |

**Returns:** `boolean` — True if the [Region3](/docs/reference/engine/datatypes/Region3.md) is empty.

### Method: WorldRoot:IsRegion3EmptyWithIgnoreList

**Signature:** `WorldRoot:IsRegion3EmptyWithIgnoreList(region: Region3, ignoreDescendentsTable: Instances): boolean`

> **Deprecated:** This function has been deprecated. Use [WorldRoot:GetPartBoundsInBox()](/docs/reference/engine/classes/WorldRoot.md) along with [OverlapParams](/docs/reference/engine/datatypes/OverlapParams.md) for new work.

Returns a boolean indicating whether there are no
[BaseParts](/docs/reference/engine/classes/BasePart.md) within the given [Region3](/docs/reference/engine/datatypes/Region3.md), ignoring
any [BaseParts](/docs/reference/engine/classes/BasePart.md) that are descendants of the objects within
the given ignore list. If a `nil` value is given in the ignore list,
instances after this value will not be ignored.

This function only returns if a region is empty or not. Developers looking
to find specific [BaseParts](/docs/reference/engine/classes/BasePart.md) in a region should use
[WorldRoot:FindPartsInRegion3WithIgnoreList()](/docs/reference/engine/classes/WorldRoot.md).

This function is a variant of [WorldRoot:IsRegion3Empty()](/docs/reference/engine/classes/WorldRoot.md) with the
addition of an ignore list. In cases where an inclusion list is required
instead, developers should check to see if any parts are returned by
[WorldRoot:FindPartsinRegion3WithWhitelist()](/docs/reference/engine/classes/WorldRoot.md).

*Security: None · Thread Safety: Unsafe*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `region` | `Region3` |  | The [Region3](/docs/reference/engine/datatypes/Region3.md) to be checked. |
| `ignoreDescendentsTable` | `Instances` |  | An array of objects to be ignored. |

**Returns:** `boolean` — True if the [Region3](/docs/reference/engine/datatypes/Region3.md) is empty.

## Inherited Members

### From [Model](/docs/reference/engine/classes/Model.md)

- **Property `LevelOfDetail`** (`ModelLevelOfDetail`): Sets the level of detail on the model for experiences with instance
- **Property `ModelStreamingMode`** (`ModelStreamingMode`): Controls the model streaming behavior on Models when
- **Property `PrimaryPart`** (`BasePart`): The primary part of the Model, or `nil` if not explicitly set.
- **Property `Scale`** (`float`): Editor-only property used to scale the model around its pivot. Setting
- **Property `WorldPivot`** (`CFrame`): Determines where the pivot of a Model which does **not** have a
- **Method `AddPersistentPlayer(playerInstance?: Player): ()`**: Sets this model to be persistent for the specified player.
- **Method `BreakJoints(): ()`**: Breaks connections between `BaseParts`, including surface connections with *(deprecated)*
- **Method `breakJoints(): ()`**:  *(deprecated)*
- **Method `GetBoundingBox(): Tuple`**: Returns a description of a volume that contains all parts of a Model.
- **Method `GetExtentsSize(): Vector3`**: Returns the size of the smallest bounding box that contains all of the
- **Method `GetModelCFrame(): CFrame`**: This value historically returned the CFrame of a central position in the *(deprecated)*
- **Method `GetModelSize(): Vector3`**: Returns the Vector3 size of the Model. *(deprecated)*
- **Method `GetPersistentPlayers(): List<Player>`**: Returns all the Player objects that this model object is
- **Method `GetPrimaryPartCFrame(): CFrame`**: Returns the CFrame of the model's Model.PrimaryPart. *(deprecated)*
- **Method `GetScale(): float`**: Returns the canonical scale of the model, which defaults to 1 for newly
- **Method `MakeJoints(): ()`**: Goes through all BaseParts in the Model. If any *(deprecated)*
- **Method `makeJoints(): ()`**:  *(deprecated)*
- **Method `move(location: Vector3): ()`**:  *(deprecated)*
- **Method `MoveTo(position: Vector3): ()`**: Moves the PrimaryPart to the given position. If
- **Method `moveTo(location: Vector3): ()`**:  *(deprecated)*
- **Method `RemovePersistentPlayer(playerInstance?: Player): ()`**: Makes this model no longer persistent for the specified player.
- **Method `ResetOrientationToIdentity(): ()`**: Resets the rotation of the model's parts to the previously set identity *(deprecated)*
- **Method `ScaleTo(newScaleFactor: float): ()`**: Sets the scale factor of the model, adjusting the sizing and location of
- **Method `SetIdentityOrientation(): ()`**: Sets the identity rotation of the given model, allowing you to reset the *(deprecated)*
- **Method `SetPrimaryPartCFrame(cframe: CFrame): ()`**: Sets the BasePart.CFrame of the model's Model.PrimaryPart. *(deprecated)*
- **Method `TranslateBy(delta: Vector3): ()`**: Shifts a Model by the given Vector3 offset, preserving

### From [PVInstance](/docs/reference/engine/classes/PVInstance.md)

- **Property `Origin`** (`CFrame`): Editor-only property that reads and sets the world CFrame of
- **Property `Pivot Offset`** (`CFrame`): Editor-only property that displays and edits the pivot's CFrame
- **Method `GetPivot(): CFrame`**: Gets the pivot of a PVInstance.
- **Method `PivotTo(targetCFrame: CFrame): ()`**: Transforms the PVInstance along with all of its descendant

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