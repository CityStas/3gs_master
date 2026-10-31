---
name: Model
last_updated: 2026-10-30T19:55:52Z
inherits:
  - PVInstance
  - Instance
  - Object
type: class
memory_category: BaseParts
summary: "Models are container objects, meaning they group objects together. They are best used to hold collections of BaseParts and have a number of functions that extend their functionality."
---

# Class: Model

> Models are container objects, meaning they group objects together. They are
> best used to hold collections of [BaseParts](/docs/reference/engine/classes/BasePart.md) and have a number
> of functions that extend their functionality.

## Description

Models are container objects, meaning they group objects together. They are
best used to hold collections of [BaseParts](/docs/reference/engine/classes/BasePart.md) and have a number
of functions that extend their functionality.

Models are intended to represent **geometric** groupings. If your grouping has
no geometric interpretation, for instance a collection of
[Scripts](/docs/reference/engine/classes/Script.md), use a [Folder](/docs/reference/engine/classes/Folder.md) instead.

Models whose constituent parts are joined together with joints (so that they
can move around or be destroyed via physics simulation) usually have a
[PrimaryPart](/docs/reference/engine/classes/Model.md) set, as it specifies which part within
the model the pivot and bounding box will "follow" as the model moves. Static
models which stay in one place do not benefit from having a primary part set.

Models have a wide range of applications, including Roblox player characters.
They also have a number of unique behaviors that are important to keep in
mind:

- When a [Humanoid](/docs/reference/engine/classes/Humanoid.md) and a [Part](/docs/reference/engine/classes/Part.md) named **Head** are parented under
  a model, a name/health GUI will appear over the model; see
  [Character Name/Health Display](/docs/en-us/characters/name-health-display.md)
  for details.
- If a part's position on the **Y** axis hits the
  [Workspace.FallenPartsDestroyHeight](/docs/reference/engine/classes/Workspace.md) value, and it was the last object
  inside of a [Model](/docs/reference/engine/classes/Model.md), the model will be destroyed as well.
- When used in a place with [Workspace.StreamingEnabled](/docs/reference/engine/classes/Workspace.md) set to true,
  the value of [ModelStreamingMode](/docs/reference/engine/classes/Model.md) controls
  various behaviors around how the model and any descendants are replicated
  and/or removed from clients. In addition, the value of
  [LevelOfDetail](/docs/reference/engine/classes/Model.md) impacts rendering of the model.

As with all [Instance](/docs/reference/engine/classes/Instance.md) types, the fact that a parent [Model](/docs/reference/engine/classes/Model.md) is
replicated to a client does not guarantee that all its children are
replicated. This is particularly important if these instances are being
accessed by code running on the client, such as in a [LocalScript](/docs/reference/engine/classes/LocalScript.md).
Using [ModelStreamingMode](/docs/reference/engine/classes/Model.md) with values such as
[Atomic](/docs/reference/engine/enums/ModelStreamingMode.md) can ensure that the entire model and all of
its descendants are present if the parent model exists on the client, or you
can use [WaitForChild()](/docs/reference/engine/classes/Instance.md) when atomicity is not
desired.

## Code Samples

**Basic Model Instantiation**

The following sample includes a basic function that takes a table of objects
and parents them into a new Model, returning that Model.

```lua
local function groupObjects(objectTable)
	local model = Instance.new("Model")
	for _, object in pairs(objectTable) do
		object.Parent = model
	end
	return model
end

local objects = {
	Instance.new("Part"),
	Instance.new("Part"),
}

groupObjects(objects)
```

## Properties

### Property: Model.LevelOfDetail

```json
{
  "type": "ModelLevelOfDetail",
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
  "category": "Appearance",
  "capabilities": [
    "PluginOrOpenCloud"
  ]
}
```

Sets the level of detail on the model for experiences with instance
[streaming](/docs/en-us/workspace/streaming.md) enabled. Composite or
imposter meshes do not support physics, collision detection, or
raycasting.

When set to [StreamingMesh](/docs/reference/engine/enums/ModelLevelOfDetail.md), a lower resolution
"imposter" mesh (colored, coarse mesh that wraps around all child parts of
the model) renders outside the streaming radius. Does not support
textures.

When set to [SLIM](/docs/reference/engine/enums/ModelLevelOfDetail.md), a **SLIM** model (Scalable
Lightweight Interactive Model) renders a composite of all child parts at
progressively lower resolutions at distances based on the streaming
radius. This greatly improves visual quality over
[StreamingMesh](/docs/reference/engine/enums/ModelLevelOfDetail.md).

When set to [Disabled](/docs/reference/engine/enums/ModelLevelOfDetail.md) or
[Automatic](/docs/reference/engine/enums/ModelLevelOfDetail.md), lower resolution meshes will not be
displayed.

### Property: Model.ModelStreamingMode

```json
{
  "type": "ModelStreamingMode",
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
  "category": "Behavior"
}
```

Controls how [Models](/docs/reference/engine/classes/Model.md) are streamed in and out when instance
[streaming](/docs/en-us/workspace/streaming.md) is enabled. Behavior
depends on the selected enum. Has no effect when streaming is not enabled.

This property should only be changed in Studio via the
[Properties](/docs/en-us/studio/properties.md) window when streaming is
enabled, or in [Scripts](/docs/reference/engine/classes/Script.md), but never in
[LocalScripts](/docs/reference/engine/classes/LocalScript.md) (doing so can result in undefined
behavior).

### Property: Model.PrimaryPart

```json
{
  "type": "BasePart",
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
  "category": "Pivot"
}
```

Points to the primary part of the [Model](/docs/reference/engine/classes/Model.md). The primary part is the
[BasePart](/docs/reference/engine/classes/BasePart.md) that acts as the physical reference for the pivot of the
model. That is, when parts within the model are moved due to physical
simulation or other means, the pivot will move in sync with the primary
part.

Note that [Models](/docs/reference/engine/classes/Model.md) do not have `PrimaryPart` set by default.
If you are creating a model that needs to be acted upon by physics, you
should manually set this property in Studio or within a script. If the
primary part is **not** set, the pivot will remain at the same location in
world space, even if parts within the model are moved.

Also note that when setting this property, it must be a [BasePart](/docs/reference/engine/classes/BasePart.md)
that is a descendant of the model. If you try to set
[Model.PrimaryPart](/docs/reference/engine/classes/Model.md) to a [BasePart](/docs/reference/engine/classes/BasePart.md) that is **not** a
descendant of the model, it will be set to that part but reset to `nil`
during the next simulation step &mdash; this is legacy behavior to support
scripts which assume they can temporarily set the primary part to a
[BasePart](/docs/reference/engine/classes/BasePart.md) which isn't a descendant of the model.

The general rule for models is that:

- Models whose parts are joined together via physical joints such as
  [WeldConstraints](/docs/reference/engine/classes/WeldConstraint.md) or [Motor6Ds](/docs/reference/engine/classes/Motor6D.md)
  should have a primary part assigned. For example, Roblox character
  models have their [Model.PrimaryPart](/docs/reference/engine/classes/Model.md) set to the
  **HumanoidRootPart** by default.
- Static (usually [Anchored](/docs/reference/engine/classes/BasePart.md)) models which stay in
  one place unless a script explicitly moves them don't require a
  [Model.PrimaryPart](/docs/reference/engine/classes/Model.md) and tend not to benefit from having one set.

**Throwing Dice**

This code sample creates and throws a dice model, then outputs whether it
landed with the blue side facing up. If [Model.PrimaryPart](/docs/reference/engine/classes/Model.md) was not set,
the pivot / bounding box of the dice would rotate, as the parts inside of it
are physically simulated during the roll.

```lua
-- Create a dice model with two halves and attach them together
local diceModel = Instance.new("Model")
diceModel.Name = "ChanceCube"

local diceTop = Instance.new("Part")
diceTop.Size = Vector3.new(4, 2, 4)
diceTop.Position = Vector3.new(0, 1, 0)
diceTop.Color = Color3.new(0, 0, 1)
diceTop.Parent = diceModel

local diceBottom = diceTop:Clone()
diceBottom.Position = Vector3.new(0, -1, 0)
diceBottom.Color = Color3.new(1, 0, 0)
diceBottom.Parent = diceModel

local weld = Instance.new("WeldConstraint")
weld.Part0 = diceTop
weld.Part1 = diceBottom
weld.Parent = diceModel

-- Put the dice up in the air above the workspace origin (does not require a primary part)
diceModel.Parent = workspace
diceModel:PivotTo(CFrame.new(0, 10, 0))

-- Assign the primary part before physical simulation
-- Without this line, the script will always output the same thing and the bounding box of the model will not change orientation
diceModel.PrimaryPart = diceTop

-- Wait a bit before rolling the dice (let it settle onto the floor)
for i = 5, 1, -1 do
	print("Rolling dice in...", i)
	task.wait(1)
end

diceTop:ApplyAngularImpulse(Vector3.new(15000, 1000, 5000))
diceTop:ApplyImpulse(Vector3.new(0, 3000, 0))
task.wait(1)

-- Wait for the roll to complete
while diceTop.AssemblyLinearVelocity.Magnitude > 0.1 or diceTop.AssemblyAngularVelocity.Magnitude > 0.1 do
	task.wait()
end

-- Get the dice orientation, impacted by the primary part
local orientation = diceModel:GetBoundingBox()
if orientation.YVector.Y > 0.5 then
	print("It's the boy!")
else
	print("It's his mother!")
end
```

### Property: Model.Scale

```json
{
  "type": "float",
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
  "category": "Pivot"
}
```

Setting this property in the Properties window will scale the model as
though [Model:ScaleTo()](/docs/reference/engine/classes/Model.md) was called on it, scaling all descendant
Instances in the model, such as materials, images, and the 3D geometry of
parts, so that the model has the specified scale factor relative to its
original size.

This property is only available in Studio and will throw an error if used
in a [Script](/docs/reference/engine/classes/Script.md) or [LocalScript](/docs/reference/engine/classes/LocalScript.md). [Model:ScaleTo()](/docs/reference/engine/classes/Model.md) and
[Model:GetScale()](/docs/reference/engine/classes/Model.md) should be used from scripts.

### Property: Model.WorldPivot

```json
{
  "type": "CFrame",
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
  "category": "Pivot"
}
```

This property determines where the pivot of a [Model](/docs/reference/engine/classes/Model.md) which does
**not** have a set [Model.PrimaryPart](/docs/reference/engine/classes/Model.md) is located. If the
[Model](/docs/reference/engine/classes/Model.md) **does** have a [PrimaryPart](/docs/reference/engine/classes/Model.md), the
pivot of the [Model](/docs/reference/engine/classes/Model.md) is equal to the pivot of that primary part
instead, and this [WorldPivot](/docs/reference/engine/classes/Model.md) property is ignored.

For a newly created [Model](/docs/reference/engine/classes/Model.md), its pivot will be treated as the center
of the bounding box of its contents until the **first time** its
[Model.WorldPivot](/docs/reference/engine/classes/Model.md) property is set. Once the world pivot is set for
the first time, it is impossible to restore this initial behavior.

Most commonly, moving the model with the Studio tools, or with model
movement functions such as [PVInstance:PivotTo()](/docs/reference/engine/classes/PVInstance.md) and
[Model:MoveTo()](/docs/reference/engine/classes/Model.md), will set the world pivot and thus end this new
model behavior.

The purpose of this behavior is to allow Luau code to get a sensible pivot
simply by creating a new model and parenting objects to it, avoiding the
need to explicitly set [Model.WorldPivot](/docs/reference/engine/classes/Model.md) every time you create a
model in code.

**Reset Pivot**

This code sample shows a custom function for resetting the pivot of a model
back to the center of that model's bounding box.

```lua
local function resetPivot(model)
	local boundsCFrame = model:GetBoundingBox()
	if model.PrimaryPart then
		model.PrimaryPart.PivotOffset = model.PrimaryPart.CFrame:ToObjectSpace(boundsCFrame)
	else
		model.WorldPivot = boundsCFrame
	end
end

resetPivot(script.Parent)
```

**World Pivot**

Demonstrates [Model.WorldPivot](/docs/reference/engine/classes/Model.md).

```lua
local Workspace = game:GetService("Workspace")

local bluePart = Instance.new("Part")
bluePart.Name = "BluePart"
bluePart.Parent = Workspace

local redPart = Instance.new("Part")
redPart.Name = "RedPart"
redPart.Parent = Workspace

local model = Instance.new("Model")
Workspace.BluePart.Parent = model
Workspace.RedPart.Parent = model
model.Parent = Workspace

print(model:GetPivot())  -- Currently equal to the center of the bounding box containing "BluePart" and "RedPart"

model:PivotTo(CFrame.new(0, 10, 0))  -- This works without needing to explicitly set "model.WorldPivot"
```

## Methods

### Method: Model:AddPersistentPlayer

**Signature:** `Model:AddPersistentPlayer(playerInstance?: Player): ()`

Sets this model to be persistent for the specified player. Persistent
models stay present for the player regardless of streaming settings or
conditions.

[ModelStreamingMode](/docs/reference/engine/classes/Model.md) must be set to
[PersistentPerPlayer](/docs/reference/engine/enums/ModelStreamingMode.md) for behavior to be changed
as a result of addition.

*Security: None · Thread Safety: Unsafe*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `playerInstance` | `Player` | `nil` | The [Player](/docs/reference/engine/classes/Player.md) to make this model persistent for. |

**Returns:** `()`

### Method: Model:GetBoundingBox

**Signature:** `Model:GetBoundingBox(): Tuple`

This function returns a description of a volume that contains all
[BasePart](/docs/reference/engine/classes/BasePart.md) children within a [Model](/docs/reference/engine/classes/Model.md). The volume's orientation
is based on the orientation of the [PrimaryPart](/docs/reference/engine/classes/Model.md),
and matches the selection box rendered in Studio when the model is
selected. Mirroring the behavior of [Terrain:FillBlock()](/docs/reference/engine/classes/Terrain.md), it
returns a [CFrame](/docs/reference/engine/datatypes/CFrame.md) representing the center of that bounding box
and a [Vector3](/docs/reference/engine/datatypes/Vector3.md) representing its size. The size may be inaccurate
at runtime if physics constraints are acting upon the parts within the
[Model](/docs/reference/engine/classes/Model.md).

The orientation of the bounding box matches the orientation of the
[Pivot](/docs/reference/engine/classes/PVInstance.md) - either the pivot of the
[PrimaryPart](/docs/reference/engine/classes/Model.md) (if present) or the
[WorldPivot](/docs/reference/engine/classes/Model.md) of the model.

*Security: None · Thread Safety: Unsafe*

**Returns:** `Tuple` — A [CFrame](/docs/reference/engine/datatypes/CFrame.md) representing the orientation of the volume
followed by a [Vector3](/docs/reference/engine/datatypes/Vector3.md) representing the size of the volume.

**Get Bounding Box**

Demonstrates [Model:GetBoundingBox()](/docs/reference/engine/classes/Model.md).

```lua
local Workspace = game:GetService("Workspace")

local model = Workspace.Model
local part = Workspace.Part
local orientation, size = model:GetBoundingBox()

-- Resize and position part equal to bounding box of model
part.Size = size
part.CFrame = orientation
```

### Method: Model:GetExtentsSize

**Signature:** `Model:GetExtentsSize(): Vector3`

Returns the size of the smallest bounding box that contains all of the
[BaseParts](/docs/reference/engine/classes/BasePart.md) in the [Model](/docs/reference/engine/classes/Model.md). The orientation matches
the orientation of the [Pivot](/docs/reference/engine/classes/PVInstance.md) - either the
pivot of the [PrimaryPart](/docs/reference/engine/classes/Model.md) (if present) or the
[WorldPivot](/docs/reference/engine/classes/Model.md) of the model.

Note this function only returns the size of the smallest bounding box, and
the developer must employ their own method to obtain the position of the
bounding box.

*Security: None · Thread Safety: Unsafe*

**Returns:** `Vector3` — The [Vector3](/docs/reference/engine/datatypes/Vector3.md) extents size of the [Model](/docs/reference/engine/classes/Model.md).

**Model GetExtentsSize**

The code sample below demonstrates how Model.GetExtentsSize can be used to get
the size of the bounding box containing the parts.

```lua
local model = Instance.new("Model")
model.Parent = workspace

local RNG = Random.new()

for _ = 1, 5 do
	local part = Instance.new("Part")
	part.Anchored = true
	part.Size = Vector3.new(RNG:NextNumber(0.05, 5), RNG:NextNumber(0.05, 5), RNG:NextNumber(0.05, 5))
	part.Parent = model
end

print(model:GetExtentsSize())
```

### Method: Model:GetPersistentPlayers

**Signature:** `Model:GetPersistentPlayers(): List<Player>`

When this method is called from a [Script](/docs/reference/engine/classes/Script.md), it returns all the
[Player](/docs/reference/engine/classes/Player.md) objects that this model is persistent for. When called from
a [LocalScript](/docs/reference/engine/classes/LocalScript.md), this method only checks if this model is persistent
for the [LocalPlayer](/docs/reference/engine/classes/Players.md).

*Security: None · Thread Safety: Unsafe*

**Returns:** `List<Player>` — A table with all the [Player](/docs/reference/engine/classes/Player.md) objects that this model object is
persistent for.

### Method: Model:GetScale

**Signature:** `Model:GetScale(): float`

Models contain a persistent canonical scale factor, which starts out at 1
for newly created models and changes as the model is scaled by calling
[Model:ScaleTo()](/docs/reference/engine/classes/Model.md). This function returns the current canonical scale
factor of the model.

The current scale factor does not _directly_ impact the size of Instances
under the model. It is used for content authoring and scripting purposes
to remember how the model has been scaled relative to its original size.

Within a given session, the model will cache the precise original size
information of the descendant Instances after the first
[Model:ScaleTo()](/docs/reference/engine/classes/Model.md) call. This means that calling
[ScaleTo(x)](/docs/reference/engine/classes/Model.md) followed by
[ScaleTo(1)](/docs/reference/engine/classes/Model.md) will get you back _exactly_ the
original configuration of the model with no floating point drift. Avoiding
floating point drift is the motivation for having a Scale**To** function
instead of a Scale**By** function.

The scale factor does impact engine behavior in one way: The scale factor
of a model will be applied to joint offsets of
[Animations](/docs/reference/engine/classes/Animation.md) played on an [AnimationController](/docs/reference/engine/classes/AnimationController.md)
under that model, so that animated rigs will correctly play back
animations even when scaled.

*Security: None · Thread Safety: Unsafe · Simulation Access: true*

**Returns:** `float` — The current canonical scale factor of the model.

**Substituting in a replacement model using PivotTo and ScaleTo**

This code sample demonstrates substituting in a replacement for all the copies
of a tree model using [Model:PivotTo()](/docs/reference/engine/classes/Model.md) and [Model:ScaleTo()](/docs/reference/engine/classes/Model.md). The
pivot and scale of the models are used as a reference ensuring that the
relative sizes and locations of the replacement models match those of the
originals.

```lua
local CollectionService = game:GetService("CollectionService")
local ReplicatedStorage = game:GetService("ReplicatedStorage")

-- Find all the models with the tag we want to replace
local items = CollectionService:GetTagged("Tree")
local newModel = ReplicatedStorage.FancyTreeReplacementModel
for _, item in items do
	-- Make the new item and scale / position it where the old one was
	local newItem = newModel:Clone()
	newItem:ScaleTo(item:GetScale())
	newItem:PivotTo(item:GetPivot())

	-- Add the same tag to the replacement
	CollectionService:AddTag(newItem, "Tree")

	-- Delete the old item and parent the new one
	newItem.Parent = item.Parent
	item:Destroy()
end
```

### Method: Model:MoveTo

**Signature:** `Model:MoveTo(position: Vector3): ()`

Moves the [PrimaryPart](/docs/reference/engine/classes/Model.md) to the given position. If
a primary part has not been specified, the root part of the model will be
used, but the root part is not deterministic and it is recommended that
you always set a primary part when using [MoveTo()](/docs/reference/engine/classes/Model.md).

If there are any obstructions where the model is to be moved, such as
[Terrain](/docs/reference/engine/classes/Terrain.md) or other [BaseParts](/docs/reference/engine/classes/BasePart.md), the model will be
moved vertically upward until there is nothing in the way. If this
behavior is not desired, [PVInstance:PivotTo()](/docs/reference/engine/classes/PVInstance.md) should be used
instead.

Note that rotation is not preserved when moving a model with
[MoveTo()](/docs/reference/engine/classes/Model.md). It is recommended to use either
[TranslateBy()](/docs/reference/engine/classes/Model.md) or [PVInstance:PivotTo()](/docs/reference/engine/classes/PVInstance.md)
if the current rotation of the model needs to be preserved.

*Security: None · Thread Safety: Unsafe*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `position` | `Vector3` |  | The [Vector3](/docs/reference/engine/datatypes/Vector3.md) the [Model](/docs/reference/engine/classes/Model.md) is moved to. |

**Returns:** `()`

**Model MoveTo**

This sample demonstrates how [Model:MoveTo()](/docs/reference/engine/classes/Model.md) avoids collisions.

A simple two part [Model](/docs/reference/engine/classes/Model.md) is created, and its [Model.PrimaryPart](/docs/reference/engine/classes/Model.md)
is set. An large obstruction part is placed next to it.

After 5 seconds [Model:MoveTo()](/docs/reference/engine/classes/Model.md) is used to direct the model to move
inside the obstruction part. However, as MoveTo will not move a model inside
of an obstruction the [Model](/docs/reference/engine/classes/Model.md) is moved up on the Y axis and placed above
the obstruction.

```lua
local START_POSITION = Vector3.new(-20, 10, 0)
local END_POSITION = Vector3.new(0, 10, 0)

local model = Instance.new("Model")
model.Parent = workspace

local part1 = Instance.new("Part")
part1.Size = Vector3.new(4, 4, 4)
part1.Position = START_POSITION
part1.Anchored = true
part1.BrickColor = BrickColor.new("Bright yellow")
part1.Parent = model

local part2 = Instance.new("Part")
part2.Size = Vector3.new(2, 2, 2)
part2.Position = START_POSITION + Vector3.new(0, 3, 0)
part2.Anchored = true
part2.BrickColor = BrickColor.new("Bright blue")
part2.Parent = model

model.PrimaryPart = part1
model.Parent = workspace

local obstruction = Instance.new("Part")
obstruction.Name = "Obstruction"
obstruction.Size = Vector3.new(10, 10, 10)
obstruction.Position = Vector3.new(0, 10, 0)
obstruction.Anchored = true
obstruction.BrickColor = BrickColor.new("Bright green")
obstruction.Parent = workspace

task.wait(3)

model:MoveTo(END_POSITION)
```

### Method: Model:RemovePersistentPlayer

**Signature:** `Model:RemovePersistentPlayer(playerInstance?: Player): ()`

Makes this model no longer persistent for the specified player. This does
not guarantee the model will immediately be removed for the player; after
calling this method, the model will be treated as
[Atomic](/docs/reference/engine/enums/ModelStreamingMode.md) for that player and will remain present
as long as it is within the target streaming radius.

[ModelStreamingMode](/docs/reference/engine/classes/Model.md) must be set to
[PersistentPerPlayer](/docs/reference/engine/enums/ModelStreamingMode.md) for behavior to be changed
as a result of removal.

*Security: None · Thread Safety: Unsafe*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `playerInstance` | `Player` | `nil` | The [Player](/docs/reference/engine/classes/Player.md) to make this model no longer persistent for. |

**Returns:** `()`

### Method: Model:ScaleTo

**Signature:** `Model:ScaleTo(newScaleFactor: float): ()`

Models contain a persistent canonical scale factor, which starts out at 1
for newly created models. This function scales the model, around the pivot
location, relative to how it would look at a scale factor of 1. To
accomplish this it does two things:

- Sets the current scale factor of the model to the specified value
- Resizes and repositions all descendant Instances accordingly

The scaling of locations is done around the pivot location.

All "geometric" properties of descendant Instances will be scaled. That
obviously includes the sizes of parts, but here are some other examples of
properties which are scaled:

- The length of joints like [WeldConstraints](/docs/reference/engine/classes/WeldConstraint.md), and
  [RopeConstraint](/docs/reference/engine/classes/RopeConstraint.md)
- Physical velocities and forces like [HingeConstraint](/docs/reference/engine/classes/HingeConstraint.md)
- Visual properties like sizes of particle emitters
- Other length properties like [Sound.RollOffMinDistance](/docs/reference/engine/classes/Sound.md)

*Security: None · Thread Safety: Unsafe*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `newScaleFactor` | `float` |  | The new scale factor for the model, which must be a positive non-zero number. A value of 1 represents the model's original size. |

**Returns:** `()`

### Method: Model:TranslateBy

**Signature:** `Model:TranslateBy(delta: Vector3): ()`

Shifts a [Model](/docs/reference/engine/classes/Model.md) by the given [Vector3](/docs/reference/engine/datatypes/Vector3.md) offset, preserving
the model's orientation. If another [BasePart](/docs/reference/engine/classes/BasePart.md) or [Terrain](/docs/reference/engine/classes/Terrain.md)
already exists at the new position then the [Model](/docs/reference/engine/classes/Model.md) will overlap
said object.

The translation is applied in world space rather than object space,
meaning even if the model's parts are orientated differently it will still
move along the standard axis.

*Security: None · Thread Safety: Unsafe*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `delta` | `Vector3` |  | The [Vector3](/docs/reference/engine/datatypes/Vector3.md) to translate the [Model](/docs/reference/engine/classes/Model.md) by. |

**Returns:** `()`

**Model TranslateBy**

This sample demonstrates how [Model:TranslateBy()](/docs/reference/engine/classes/Model.md) ignores collisions
and respects the orientation of the model.

A simple two part [Model](/docs/reference/engine/classes/Model.md) is created, rotated 45 degrees on the Y axis,
and its [Model.PrimaryPart](/docs/reference/engine/classes/Model.md) is set. An large obstruction part is placed
next to it.

After 5 seconds [Model:TranslateBy()](/docs/reference/engine/classes/Model.md) is used to direct the model to
move inside the obstruction part. The model will move inside of the
obstruction and maintain it's current orientation.

```lua
local START_POSITION = Vector3.new(-20, 10, 0)
local END_POSITION = Vector3.new(0, 10, 0)

local model = Instance.new("Model")

local part1 = Instance.new("Part")
part1.Size = Vector3.new(4, 4, 4)
part1.CFrame = CFrame.new(START_POSITION) * CFrame.Angles(0, math.rad(45), 0)
part1.Anchored = true
part1.BrickColor = BrickColor.new("Bright yellow")
part1.Parent = model

local part2 = Instance.new("Part")
part2.Size = Vector3.new(2, 2, 2)
part2.CFrame = part1.CFrame * CFrame.new(0, 3, 0)
part2.Anchored = true
part2.BrickColor = BrickColor.new("Bright blue")
part2.Parent = model

model.PrimaryPart = part1
model.Parent = workspace

local obstruction = Instance.new("Part")
obstruction.Name = "Obstruction"
obstruction.Size = Vector3.new(10, 10, 10)
obstruction.Position = Vector3.new(0, 10, 0)
obstruction.Transparency = 0.5
obstruction.Anchored = true
obstruction.BrickColor = BrickColor.new("Bright green")
obstruction.Parent = workspace

task.wait(3)
-- use TranslateBy to shift the model into the obstruction
model:TranslateBy(END_POSITION - START_POSITION)
```

### Method: Model:BreakJoints

**Signature:** `Model:BreakJoints(): ()`

Breaks connections between `BaseParts`, including surface connections with
any adjacent parts, [WeldConstraints](/docs/reference/engine/classes/WeldConstraint.md), and all
[Welds](/docs/reference/engine/classes/Weld.md) and other [JointInstances](/docs/reference/engine/classes/JointInstance.md).

When BreakJoints is used on a Player character [Model](/docs/reference/engine/classes/Model.md), the
character's [Humanoid](/docs/reference/engine/classes/Humanoid.md) will die as it relies on the Neck joint.

Note that although joints produced by surface connections with adjacent
Parts can technically be recreated using [Model:MakeJoints()](/docs/reference/engine/classes/Model.md), this
will only recreate joints produced by surfaces. Developers should not rely
on this as following the joints being broken parts may no longer be in
contact with each other.

*Security: None · Thread Safety: Unsafe*

**Returns:** `()`

**Break Character Joints**

In this sample the joints in every Player character Model added will be broken
3 seconds after spawning. Breaking these joints will cause the Humanoid to
die.

```lua
local Players = game:GetService("Players")

local function onCharacterAdded(character)
	task.wait(3)
	character:BreakJoints()
end

local function onPlayerAdded(player)
	player.CharacterAdded:Connect(onCharacterAdded)
end

Players.PlayerAdded:Connect(onPlayerAdded)
```

**Manual Joint Creation**

This code sample demonstrates manual creation of joints on two parts that are
siblings of the script (PartA and PartB). It creates a joints on two touching
parts with compatible surface types (Studs and Inlet).

```lua
local JointsService = game:GetService("JointsService")

local partA = script.Parent.PartA
local partB = script.Parent.PartB

local function join(part0, part1, jointClass, parent)
	local newJoint = Instance.new(jointClass or "ManualWeld")
	newJoint.Part0 = part0
	newJoint.Part1 = part1
	newJoint.C0 = CFrame.new()
	newJoint.C1 = part1.CFrame:toObjectSpace(part0.CFrame)
	newJoint.Parent = parent or part0

	return newJoint
end

-- Create some joints and break them
join(partA, partB)
partA:BreakJoints()

-- Glue joints are wobbly
join(partA, partB, "Glue")
partA:BreakJoints()

-- Most of the time, joints ought to be put in JointsService
join(partA, partB, "Weld", JointsService)
```

### Method: Model:breakJoints

**Signature:** `Model:breakJoints(): ()`

> **Deprecated:** This deprecated function is a variant of [Model:BreakJoints()](/docs/reference/engine/classes/Model.md) which should be used instead.

*Security: None · Thread Safety: Unsafe*

**Returns:** `()`

### Method: Model:GetModelCFrame

**Signature:** `Model:GetModelCFrame(): CFrame`

> **Deprecated:** This function has been deprecated as it did not provide reliable results. You can instead use [Model:GetPrimaryPartCFrame()](/docs/reference/engine/classes/Model.md) to retrieve the [CFrame](/docs/reference/engine/datatypes/CFrame.md) of the model's primary part.

This value historically returned the CFrame of a central position in the
model.

*Security: None · Thread Safety: Unsafe*

**Returns:** `CFrame` — A [CFrame](/docs/reference/engine/datatypes/CFrame.md) representing a central position in the model.

### Method: Model:GetModelSize

**Signature:** `Model:GetModelSize(): Vector3`

> **Deprecated:** This item is deprecated. Do not use it for new work. Developers can instead use [Model.GetExtentsSize](/docs/reference/engine/classes/Model.md).

The GetModelSize function returns the [Vector3](/docs/reference/engine/datatypes/Vector3.md) size of the
[Model](/docs/reference/engine/classes/Model.md).

*Security: None · Thread Safety: Unsafe*

**Returns:** `Vector3` — The [Vector3](/docs/reference/engine/datatypes/Vector3.md) size of the [Model](/docs/reference/engine/classes/Model.md).

**Model:GetModelSize**

This code would create a model, put some parts in it, position them randomly,
and then print its size:

```lua
local model = Instance.new("Model")
model.Parent = workspace

local RNG = Random.new()

for _ = 1, 5 do
	local part = Instance.new("Part")
	part.Parent = model
	part.Anchored = true
	part.Size = Vector3.new(RNG:NextNumber(0.05, 5), RNG:NextNumber(0.05, 5), RNG:NextNumber(0.05, 5))
end

print(model:GetModelSize())
```

### Method: Model:GetPrimaryPartCFrame

**Signature:** `Model:GetPrimaryPartCFrame(): CFrame`

This function has been superseded by [PVInstance:GetPivot()](/docs/reference/engine/classes/PVInstance.md) which
acts as a replacement and does not change your code's behavior. Use
[PVInstance:GetPivot()](/docs/reference/engine/classes/PVInstance.md) for new work and migrate your existing
[Model:GetPrimaryPartCFrame()](/docs/reference/engine/classes/Model.md) calls when convenient.

Returns the [CFrame](/docs/reference/engine/datatypes/CFrame.md) of the model's [Model.PrimaryPart](/docs/reference/engine/classes/Model.md).

This function is equivalent to the following.

    Model.PrimaryPart.CFrame

Note this function will throw an error if no primary part exists for the
[Model](/docs/reference/engine/classes/Model.md). If this behavior is not desired developers can do the
following, which will be equal to `nil` if there is no primary part.

    local cFrame = Model.PrimaryPart and Model.PrimaryPart.CFrame

*Security: None · Thread Safety: Unsafe*

**Returns:** `CFrame` — The [CFrame](/docs/reference/engine/datatypes/CFrame.md) of the model's [Model.PrimaryPart](/docs/reference/engine/classes/Model.md).

**Rotating a Model**

The following code demonstrates how GetPrimaryPartCFrame and
SetPrimaryPartCFrame can be used to rotate a model.

A simple model is created in the Workspace and a loop is started that will
rotate the model 10 degrees around the Y axis every 0.2 seconds.

```lua
local START_POSITION = Vector3.new(0, 10, 0)

local model = Instance.new("Model")

local part1 = Instance.new("Part")
part1.Size = Vector3.new(4, 4, 4)
part1.CFrame = CFrame.new(START_POSITION)
part1.Anchored = true
part1.BrickColor = BrickColor.new("Bright yellow")
part1.Parent = model

local part2 = Instance.new("Part")
part2.Size = Vector3.new(2, 2, 2)
part2.CFrame = part1.CFrame * CFrame.new(0, 3, 0)
part2.Anchored = true
part2.BrickColor = BrickColor.new("Bright blue")
part2.Parent = model

-- set the primary part
model.PrimaryPart = part1
model.Parent = workspace

while true do
	local primaryPartCFrame = model:GetPrimaryPartCFrame()
	local newCFrame = primaryPartCFrame * CFrame.Angles(0, math.rad(1), 0)
	model:SetPrimaryPartCFrame(newCFrame)
	task.wait()
end
```

### Method: Model:MakeJoints

**Signature:** `Model:MakeJoints(): ()`

> **Deprecated:** This joint type has been deprecated. Don't use it for new work. Use [WeldConstraints](/docs/reference/engine/classes/WeldConstraint.md) and [HingeConstraints](/docs/reference/engine/classes/HingeConstraint.md) instead.

SurfaceType based joining is deprecated. Don't use MakeJoints for new
projects. Use [WeldConstraints](/docs/reference/engine/classes/WeldConstraint.md) and
[HingeConstraints](/docs/reference/engine/classes/HingeConstraint.md) instead.

Goes through all [Parts](/docs/reference/engine/classes/BasePart.md) in the [Model](/docs/reference/engine/classes/Model.md) and creates
joints between the specified Parts and any planar touching surfaces,
depending on the parts' surfaces.

- Smooth surfaces will not create joints
- Glue surfaces will create a [Glue](/docs/reference/engine/classes/Glue.md) joint
- Weld will create a [Weld](/docs/reference/engine/classes/Weld.md) joint with any surface except for
  Unjoinable
- Studs, Inlet, or Universal will each create a [Snap](/docs/reference/engine/classes/Snap.md) joint with
  either of other the other two surfaces (e.g. Studs with Inlet and
  Universal)
- Hinge and Motor surfaces create [Rotate](/docs/reference/engine/classes/Rotate.md) and [RotateV](/docs/reference/engine/classes/RotateV.md) joint
  instances

This function doesn't work if the Part is not a descendant of
[Workspace](/docs/reference/engine/classes/Workspace.md). Therefore, you must first ensure the Model is parented
to Workspace before using MakeJoints.

*Security: None · Thread Safety: Unsafe*

**Returns:** `()`

**Model MakeJoints**

This code sample demonstrates how joints can be made using the
Model:MakeJoints function.

A model is instanced, with two parts on top of each other. The top part is
anchored and the bottom part is not. Normally, when parented to the Workspace
the bottom part would fall to the Baseplate.

However, as TopSurface property of the bottom part is set to
Enum.SurfaceType.Weld, this means that when Model:MakeJoints is ran a
connection is made between them.

Therefore the bottom part does not drop until the joints in the model are
broken. This is often done using Model:BreakJoints, but in this example the
connection is broken using an explosion.

```lua
local model = Instance.new("Model")

-- create one part on top of another
local topPart = Instance.new("Part")
topPart.Size = Vector3.new(5, 1, 5)
topPart.Position = Vector3.new(0, 10, 0)
topPart.BrickColor = BrickColor.new("Bright green")
topPart.Anchored = true -- anchor the top part
topPart.Parent = model

local bottomPart = Instance.new("Part")
bottomPart.Size = Vector3.new(8, 1, 8)
bottomPart.Position = Vector3.new(0, 9, 0)
bottomPart.BrickColor = BrickColor.new("Bright green")
bottomPart.Anchored = false -- leave bottom unanchored
bottomPart.Parent = model

topPart.BottomSurface = Enum.SurfaceType.Smooth
topPart.TopSurface = Enum.SurfaceType.Smooth
bottomPart.BottomSurface = Enum.SurfaceType.Smooth
bottomPart.TopSurface = Enum.SurfaceType.Weld -- 'Weld' to create a joint

model.Parent = workspace

model:MakeJoints()

task.wait(2)
-- unanchor the bottom part - part does not fall
print("Unanchored!")
bottomPart.BrickColor = BrickColor.new("Bright red")
bottomPart.Anchored = false

task.wait(2)
-- break the joints using an explosion - part falls
local explosion = Instance.new("Explosion")
explosion.Position = bottomPart.Position
explosion.Parent = workspace
```

**Simple Joint Creation**

This code sample demonstrates creation of joints on two parts that are
siblings of the script (PartA and PartB). It uses MakeJoints on two touching
parts with compatible surface types (Studs and Inlet).

```lua
local partA = script.Parent.PartA
local partB = script.Parent.PartB

-- Move PartB on top of PartA
partB.CFrame = partA.CFrame * CFrame.new(0, partB.Size.Y / 2 + partA.Size.Y / 2, 0)
-- Studs and Inlet will make joints
partA.TopSurface = Enum.SurfaceType.Studs
partB.BottomSurface = Enum.SurfaceType.Inlet
-- Automatically create a joint between PartA and PartB
partA:MakeJoints()
```

### Method: Model:makeJoints

**Signature:** `Model:makeJoints(): ()`

> **Deprecated:** This deprecated function is a variant of [Model:MakeJoints()](/docs/reference/engine/classes/Model.md) which should be used instead.

*Security: None · Thread Safety: Unsafe*

**Returns:** `()`

### Method: Model:move

**Signature:** `Model:move(location: Vector3): ()`

> **Deprecated:** This item has been superseded by [Model:MoveTo()](/docs/reference/engine/classes/Model.md) which should be used in all new work

*Security: None · Thread Safety: Unsafe*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `location` | `Vector3` |  |  |

**Returns:** `()`

### Method: Model:moveTo

**Signature:** `Model:moveTo(location: Vector3): ()`

> **Deprecated:** This deprecated function is a variant of [Model:MoveTo()](/docs/reference/engine/classes/Model.md) which should be used instead.

*Security: None · Thread Safety: Unsafe*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `location` | `Vector3` |  |  |

**Returns:** `()`

### Method: Model:ResetOrientationToIdentity

**Signature:** `Model:ResetOrientationToIdentity(): ()`

> **Deprecated:** This function has been deprecated; it remains to prevent legacy scripts from throwing errors, but it does nothing when called.

Resets the rotation of the model's parts to the previously set identity
rotation, which is done through the [Model:SetIdentityOrientation()](/docs/reference/engine/classes/Model.md)
method.

*Security: None · Thread Safety: Unsafe*

**Returns:** `()`

### Method: Model:SetIdentityOrientation

**Signature:** `Model:SetIdentityOrientation(): ()`

> **Deprecated:** This function has been deprecated; it remains to prevent legacy scripts from throwing errors, but it does nothing when called.

Sets the identity rotation of the given model, allowing you to reset the
rotation of the entire model later, through the use of the
`ResetOrientationToIdentity` method.

*Security: None · Thread Safety: Unsafe*

**Returns:** `()`

### Method: Model:SetPrimaryPartCFrame

**Signature:** `Model:SetPrimaryPartCFrame(cframe: CFrame): ()`

This function has been superseded by [PVInstance:PivotTo()](/docs/reference/engine/classes/PVInstance.md) which
acts as a more performant replacement and does not change your code's
behavior. Use [PVInstance:PivotTo()](/docs/reference/engine/classes/PVInstance.md) for new work and migrate your
existing [Model:SetPrimaryPartCFrame()](/docs/reference/engine/classes/Model.md) calls when convenient.

Sets the [BasePart.CFrame](/docs/reference/engine/classes/BasePart.md) of the model's [Model.PrimaryPart](/docs/reference/engine/classes/Model.md).
All other parts in the model will also be moved and will maintain their
orientation and offset respective to the [Model.PrimaryPart](/docs/reference/engine/classes/Model.md).

Note, this function will throw an error if no [Model.PrimaryPart](/docs/reference/engine/classes/Model.md)
exists for the model. This can cause issues if, for example, the primary
part was never set or has been destroyed.

*Security: None · Thread Safety: Unsafe*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `cframe` | `CFrame` |  | The [CFrame](/docs/reference/engine/datatypes/CFrame.md) to be set. |

**Returns:** `()`

## Inherited Members

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