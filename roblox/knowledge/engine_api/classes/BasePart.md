---
name: BasePart
last_updated: 2026-10-30T19:55:52Z
inherits:
  - PVInstance
  - Instance
  - Object
type: class
memory_category: Instances
tags:
  - NotCreatable
  - NotBrowsable
summary: "The abstract base class for in-world objects that physically interact."
---

# Class: BasePart

> The abstract base class for in-world objects that physically interact.

## Description

[BasePart](/docs/reference/engine/classes/BasePart.md) is an abstract base class for in-world objects that render
and are physically simulated while in the [Workspace](/docs/reference/engine/classes/Workspace.md). There are several
implementations of [BasePart](/docs/reference/engine/classes/BasePart.md), the most common being [Part](/docs/reference/engine/classes/Part.md) and
[MeshPart](/docs/reference/engine/classes/MeshPart.md). Others include [WedgePart](/docs/reference/engine/classes/WedgePart.md), [SpawnLocation](/docs/reference/engine/classes/SpawnLocation.md), and
the singleton [Terrain](/docs/reference/engine/classes/Terrain.md) object. Generally, when documentation refers to
a "part," most [BasePart](/docs/reference/engine/classes/BasePart.md) implementations will work and not just
[Part](/docs/reference/engine/classes/Part.md).

For information on how [BaseParts](/docs/reference/engine/classes/BasePart.md) are grouped into simulated
rigid bodies, see [Assemblies](/docs/en-us/physics/assemblies.md).

There are many different objects that interact with [BasePart](/docs/reference/engine/classes/BasePart.md) (other
than [Terrain](/docs/reference/engine/classes/Terrain.md)), including:

- Several [BaseParts](/docs/reference/engine/classes/BasePart.md) may be grouped within a [Model](/docs/reference/engine/classes/Model.md) and
  moved at the same time using [PVInstance:PivotTo()](/docs/reference/engine/classes/PVInstance.md). See
  [Models](/docs/en-us/parts/models.md).
- A [Decal](/docs/reference/engine/classes/Decal.md) applies a stretched image texture to the faces of a
  [BasePart](/docs/reference/engine/classes/BasePart.md), while a [Texture](/docs/reference/engine/classes/Texture.md) applies a tiled image texture to
  the faces. See [Textures and Decals](/docs/en-us/parts/textures-decals.md).
- A [SurfaceGui](/docs/reference/engine/classes/SurfaceGui.md) renders [GuiObjects](/docs/reference/engine/classes/GuiObject.md) on the face of a
  part. See
  [In-Experience UI Containers](/docs/en-us/ui/in-experience-containers.md).
- [Attachments](/docs/reference/engine/classes/Attachment.md) can be added to a [BasePart](/docs/reference/engine/classes/BasePart.md) to specify
  [CFrames](/docs/reference/engine/datatypes/CFrame.md) relative to the part. These are often used by
  physical [Constraint](/docs/reference/engine/classes/Constraint.md) objects as outlined in
  [Mechanical Constraints](/docs/en-us/physics/mechanical-constraints.md) and
  [Mover Constraints](/docs/en-us/physics/mover-constraints.md).
- [ParticleEmitter](/docs/reference/engine/classes/ParticleEmitter.md) objects emit particles uniformly in the volume of
  the [BasePart](/docs/reference/engine/classes/BasePart.md) to which they are parented. See
  [Particle Emitters](/docs/en-us/effects/particle-emitters.md).
- Light objects like [PointLight](/docs/reference/engine/classes/PointLight.md) emit light from the center of a
  [BasePart](/docs/reference/engine/classes/BasePart.md) as illustrated in
  [Light Sources](/docs/en-us/effects/light-sources.md).
- If parented to a [Tool](/docs/reference/engine/classes/Tool.md) and given the name **Handle**, a
  [BasePart](/docs/reference/engine/classes/BasePart.md) can be held by characters. See
  [In-Experience Tools](/docs/en-us/players/tools.md).

## Code Samples

**SmoothDamping a Part's CFrame**

Creates a blue part and red target Part. The blue part will try to smoothly
reach the red target part. Move and rotate the target to see the behavior.
Changing the smoothTime will result in different smoothing speed.

```lua
local TweenService = game:GetService("TweenService")

-- create a part and target
local part = Instance.new("Part", workspace)
part.Size = Vector3.one
part.Anchored = true
part.BrickColor = BrickColor.new("Electric blue")
part.CFrame = CFrame.new(0, 4, 0)

local target = Instance.new("Part", workspace)
target.Name = "Target"
target.Size = Vector3.one * 0.5
target.Anchored = true
target.BrickColor = BrickColor.new("Really red")
target.CFrame = CFrame.new(0, 8, 0)

-- setup a variable to store the velocity
local velocity = CFrame.new()
-- adjust the smoothing speed
local smoothTime = 0.5

game:GetService("RunService").Stepped:Connect(function(t, dt)
	part.CFrame, velocity = TweenService:SmoothDamp(part.CFrame, target.CFrame, velocity, smoothTime, math.huge, dt)
end)
```

## Properties

### Property: BasePart.Anchored

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
    "can_save": true
  },
  "thread_safety": "ReadSafe",
  "category": "Part",
  "simulationAccess": true
}
```

The `Anchored` property determines whether the part will be immovable by
physics. When enabled, a part will never change position due to gravity,
other part collisions, overlapping other parts, or any other
physics-related causes. As a result, two anchored parts will never fire
the [Touched](/docs/reference/engine/classes/BasePart.md) event on each other.

An anchored part may still be moved by changing its
[CFrame](/docs/reference/engine/classes/BasePart.md) or [Position](/docs/reference/engine/classes/BasePart.md), and
it still may have a nonzero
[AssemblyLinearVelocity](/docs/reference/engine/classes/BasePart.md) and
[AssemblyAngularVelocity](/docs/reference/engine/classes/BasePart.md).

Finally, if an unanchored part is joined with an anchored part through an
object like a [Weld](/docs/reference/engine/classes/Weld.md), it too will act anchored. If such a joint
breaks, the part may be affected by physics again. See
[Assemblies](/docs/en-us/physics/assemblies.md) for more details.

Network ownership cannot be set on anchored parts. If a part's anchored
status changes on the server, the network ownership of that part will be
affected.

**Part Anchored Toggle**

This code sample will allow a part to be clicked to toggle its anchored
property. When toggled, the visual appearance of the part is updated (red
means anchored, yellow means free).

```lua
local part = script.Parent

-- Create a ClickDetector so we can tell when the part is clicked
local cd = Instance.new("ClickDetector", part)

-- This function updates how the part looks based on its Anchored state
local function updateVisuals()
	if part.Anchored then
		-- When the part is anchored...
		part.BrickColor = BrickColor.new("Bright red")
		part.Material = Enum.Material.DiamondPlate
	else
		-- When the part is unanchored...
		part.BrickColor = BrickColor.new("Bright yellow")
		part.Material = Enum.Material.Wood
	end
end

local function onToggle()
	-- Toggle the anchored property
	part.Anchored = not part.Anchored

	-- Update visual state of the brick
	updateVisuals()
end

-- Update, then start listening for clicks
updateVisuals()
cd.MouseClick:Connect(onToggle)
```

### Property: BasePart.AssemblyAngularVelocity

```json
{
  "type": "Vector3",
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
  "category": "Assembly",
  "simulationAccess": true
}
```

The angular velocity vector of this part's assembly. It's the rate of
change of orientation in radians per second.

Angular velocity is the same at every point of the assembly.

Setting the velocity directly may lead to unrealistic motion. Using
[Torque](/docs/reference/engine/classes/Torque.md) or [AngularVelocity](/docs/reference/engine/classes/AngularVelocity.md) constraint is preferred, or use
[ApplyAngularImpulse()](/docs/reference/engine/classes/BasePart.md) if you want
instantaneous change in velocity.

If the part is [owned](/docs/en-us/physics/network-ownership.md) by the
server, this property must be changed from a server [Script](/docs/reference/engine/classes/Script.md) (not
from a [LocalScript](/docs/reference/engine/classes/LocalScript.md) or a [Script](/docs/reference/engine/classes/Script.md) with
[RunContext](/docs/reference/engine/classes/BaseScript.md) set to [RunContext.Client](/docs/reference/engine/enums/RunContext.md)).
If the part is owned by a client through **automatic** ownership, this
property can be changed from either a client script **or** a server
script; changing it from a client script for a server-owned part will have
no effect.

### Property: BasePart.AssemblyCenterOfMass

```json
{
  "type": "Vector3",
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
  "category": "Assembly",
  "simulationAccess": true
}
```

A position calculated via the [Mass](/docs/reference/engine/classes/BasePart.md) and
[Position](/docs/reference/engine/classes/BasePart.md) of all the parts in the assembly.

If the assembly has an anchored part, that part's center of mass will be
the assembly's center of mass, and the assembly will have infinite mass.

Knowing the center of mass can help the assembly maintain stability. A
force applied to the center of mass will not cause angular acceleration,
only linear. An assembly with a low center of mass will have a better time
staying upright under the effect of gravity.

### Property: BasePart.AssemblyLinearVelocity

```json
{
  "type": "Vector3",
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
  "category": "Assembly",
  "simulationAccess": true
}
```

The linear velocity vector of this part's assembly. It's the rate of
change in position of
[AssemblyCenterOfMass](/docs/reference/engine/classes/BasePart.md) in studs per
second.

If you want to know the velocity at a point other than the assembly's
center of mass, use
[GetVelocityAtPosition()](/docs/reference/engine/classes/BasePart.md).

Setting the velocity directly may lead to unrealistic motion. Using a
[VectorForce](/docs/reference/engine/classes/VectorForce.md) constraint is preferred, or use
[ApplyImpulse()](/docs/reference/engine/classes/BasePart.md) if you want instantaneous
change in velocity.

If the part is [owned](/docs/en-us/physics/network-ownership.md) by the
server, this property must be changed from a server [Script](/docs/reference/engine/classes/Script.md) (not
from a [LocalScript](/docs/reference/engine/classes/LocalScript.md) or a [Script](/docs/reference/engine/classes/Script.md) with
[RunContext](/docs/reference/engine/classes/BaseScript.md) set to [RunContext.Client](/docs/reference/engine/enums/RunContext.md)).
If the part is owned by a client through **automatic** ownership, this
property can be changed from either a client script **or** a server
script; changing it from a client script for a server-owned part will have
no effect.

### Property: BasePart.AssemblyMass

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
  "category": "Assembly",
  "simulationAccess": true
}
```

The sum of the mass of all the [BaseParts](/docs/reference/engine/classes/BasePart.md) in this part's
assembly. Parts that are [Massless](/docs/reference/engine/classes/BasePart.md) and are not
the assembly's root part will not contribute to the `AssemblyMass`.

If the assembly has an anchored part, the assembly's mass is considered
infinite. Constraints and other physical interactions between unanchored
assemblies with a large difference in mass may cause instabilities.

### Property: BasePart.AssemblyRootPart

```json
{
  "type": "BasePart",
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
  "category": "Assembly",
  "simulationAccess": true
}
```

This property indicates the [BasePart](/docs/reference/engine/classes/BasePart.md) automatically chosen to
represent the assembly's root part. If the part is not parented to the
[Workspace](/docs/reference/engine/classes/Workspace.md), this property will be `nil`.

The root part can be changed by changing the
[RootPriority](/docs/reference/engine/classes/BasePart.md) of the parts in the assembly.

Parts that all share the same `AssemblyRootPart` are in the same assembly.

For more information on root parts, see
[Assemblies](/docs/en-us/physics/assemblies.md).

### Property: BasePart.AudioCanCollide

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
    "can_save": true
  },
  "thread_safety": "ReadSafe",
  "category": "Collision",
  "simulationAccess": true
}
```

`AudioCanCollide` determines whether the part will physically interact
with audio simulation, similar to [CastShadow](/docs/reference/engine/classes/BasePart.md)
for lighting.

When disabled, audio passes through the part; it is not occluded or
reflected.

### Property: BasePart.BackSurface

```json
{
  "type": "SurfaceType",
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
  "category": "Surface"
}
```

The `BackSurface` property determines the type of surface used for the
positive **Z** direction of a part. When two parts' faces are placed next
to each other, they may create a joint between them.

### Property: BasePart.BottomSurface

```json
{
  "type": "SurfaceType",
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
  "category": "Surface"
}
```

The `BottomSurface` property determines the type of surface used for the
negative **Y** direction of a part. When two parts' faces are placed next
to each other, they may create a joint between them.

### Property: BasePart.BrickColor

```json
{
  "type": "BrickColor",
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
  "category": "Appearance"
}
```

This property determines the color of a part. If the part has a
[Material](/docs/reference/engine/classes/BasePart.md), this also determines the color used
when rendering the material texture. For more control over the color, the
[Color](/docs/reference/engine/classes/BasePart.md) property can be used and this property will
use the closest `BrickColor`.

Other visual properties of a part are determined by
[Transparency](/docs/reference/engine/classes/BasePart.md) and
[Reflectance](/docs/reference/engine/classes/BasePart.md).

### Property: BasePart.CanCollide

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
    "can_save": true
  },
  "thread_safety": "ReadSafe",
  "category": "Collision",
  "simulationAccess": true
}
```

`CanCollide` determines whether a part will physically interact with other
parts. When disabled, other parts can pass through the part uninterrupted.
Parts used for **decoration** usually have `CanCollide` disabled, as they
need not be considered by the physics engine.

If a part is not [Anchored](/docs/reference/engine/classes/BasePart.md) and has `CanCollide`
disabled, it may fall out of the world to be eventually destroyed by
[Workspace.FallenPartsDestroyHeight](/docs/reference/engine/classes/Workspace.md).

When `CanCollide` is disabled, parts may still fire the
[Touched](/docs/reference/engine/classes/BasePart.md) event (as well the other parts touching
them). You can disable this with [CanTouch](/docs/reference/engine/classes/BasePart.md).

For more information on collisions, see
[Collisions](/docs/en-us/workspace/collisions.md).

**Fade Door**

This code sample shows how a part can fade away when touched by a Humanoid
then reappear a moment after to create a passable door.

```lua
-- Paste into a Script inside a tall part
local part = script.Parent

local OPEN_TIME = 1

-- Can the door be opened at the moment?
local debounce = false

local function open()
	part.CanCollide = false
	part.Transparency = 0.7
	part.BrickColor = BrickColor.new("Black")
end

local function close()
	part.CanCollide = true
	part.Transparency = 0
	part.BrickColor = BrickColor.new("Bright blue")
end

local function onTouch(otherPart)
	-- If the door was already open, do nothing
	if debounce then
		print("D")
		return
	end

	-- Check if touched by a Humanoid
	local human = otherPart.Parent:FindFirstChildOfClass("Humanoid")
	if not human then
		print("not human")
		return
	end

	-- Perform the door opening sequence
	debounce = true
	open()
	task.wait(OPEN_TIME)
	close()
	debounce = false
end

part.Touched:Connect(onTouch)
close()
```

### Property: BasePart.CanQuery

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
    "can_save": true
  },
  "thread_safety": "ReadSafe",
  "category": "Collision",
  "simulationAccess": true
}
```

This property determines whether the part is considered during spatial
query operations, such as
[GetPartBoundsInBox](/docs/reference/engine/classes/WorldRoot.md) or
[Raycast](/docs/reference/engine/classes/WorldRoot.md). Note that
[CanCollide](/docs/reference/engine/classes/BasePart.md) must be disabled for `CanQuery` to
take effect, and spatial query functions will never include parts with
`CanQuery` of `false`.

Beyond this property, it is also possible to exclude parts which are
descendants of a given list of parts using an [OverlapParams](/docs/reference/engine/datatypes/OverlapParams.md) or
[RaycastParams](/docs/reference/engine/datatypes/RaycastParams.md) object when calling the spatial query functions.

### Property: BasePart.CanTouch

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
    "can_save": true
  },
  "thread_safety": "ReadSafe",
  "category": "Collision",
  "simulationAccess": true
}
```

This property determines if [Touched](/docs/reference/engine/classes/BasePart.md) and
[TouchEnded](/docs/reference/engine/classes/BasePart.md) events fire on the part. If `true`,
other touching parts must also have `CanTouch` set to `true` for touch
events to fire. If `false`, touch events cannot be set up for the part and
attempting to do so will throw an error. Similarly, if the property is set
to `false` after a touch event is connected, the event will be
disconnected and the [TouchTransmitter](/docs/reference/engine/classes/TouchTransmitter.md) removed.

Note that this collision logic can be set to respect
[collision groups](/docs/en-us/workspace/collisions.md#collision-filtering)
through the [Workspace.TouchesUseCollisionGroups](/docs/reference/engine/classes/Workspace.md) property. If
`true`, parts in non-colliding groups will ignore both collisions **and**
touch events, thereby making this property irrelevant.

#### Performance

There is a small performance gain on parts that have both `CanTouch` and
[CanCollide](/docs/reference/engine/classes/BasePart.md) set to `false`, as these parts will
never need to compute any kind of part to part collisions. However, they
can still be hit by [Raycasts](/docs/reference/engine/classes/WorldRoot.md) and
[OverlapParams](/docs/reference/engine/datatypes/OverlapParams.md) queries.

### Property: BasePart.CastShadow

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
    "can_save": true
  },
  "thread_safety": "ReadSafe",
  "category": "Appearance"
}
```

Determines whether or not a part casts a shadow. Disabling this property
for a given part can cause visual artifacts on the shadows cast upon that
part.

This property is not designed for performance enhancement, but in complex
scenes, strategically disabling it on certain parts can improve
performance. Due to the possibility of visual artifacts, we recommend
leaving it enabled on all parts in most situations.

### Property: BasePart.CenterOfMass

```json
{
  "type": "Vector3",
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
  "category": "Part",
  "simulationAccess": true
}
```

The `CenterOfMass` property describes the **local** position of a part's
center of mass. If this is a single part assembly, this is the
[AssemblyCenterOfMass](/docs/reference/engine/classes/BasePart.md) converted from
world space to local. On simple [Parts](/docs/reference/engine/classes/Part.md), the center of mass is
always `(0, 0, 0)`, but it can vary for [WedgePart](/docs/reference/engine/classes/WedgePart.md) or
[MeshPart](/docs/reference/engine/classes/MeshPart.md).

### Property: BasePart.CFrame

```json
{
  "type": "CFrame",
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
  "category": "Transform",
  "simulationAccess": true
}
```

The `CFrame` property determines both the position and orientation of the
[BasePart](/docs/reference/engine/classes/BasePart.md) in the world. It acts as an arbitrary reference location
on the geometry, but [ExtentsCFrame](/docs/reference/engine/classes/BasePart.md)
represents the actual [CFrame](/docs/reference/engine/datatypes/CFrame.md) of its physical center.

When setting `CFrame` on a part, other joined parts are also moved
relative to the part, but it is recommended that you use
[PVInstance:PivotTo()](/docs/reference/engine/classes/PVInstance.md) to move an entire model, such as when
teleporting a player's character.

Unlike setting [BasePart.Position](/docs/reference/engine/classes/BasePart.md), setting `CFrame` will always
move the part to the exact given [CFrame](/docs/reference/engine/datatypes/CFrame.md); in other words: **no
overlap checking is done** and the physics solver will attempt to resolve
any overlap unless both parts are [Anchored](/docs/reference/engine/classes/BasePart.md).

For keeping track of positions relative to a part's [CFrame](/docs/reference/engine/datatypes/CFrame.md), an
[Attachment](/docs/reference/engine/classes/Attachment.md) may be useful.

**Setting Part CFrame**

This code sample demonstrates setting a part's CFrame in many different ways.
It showcases how to create and compose CFrame values. It references a sibling
part called "OtherPart" for demonstrating relative positioning.

```lua
local part = script.Parent:WaitForChild("Part")
local otherPart = script.Parent:WaitForChild("OtherPart")

-- Reset the part's CFrame to (0, 0, 0) with no rotation.
-- This is sometimes called the "identity" CFrame
part.CFrame = CFrame.new()

-- Set to a specific position (X, Y, Z)
part.CFrame = CFrame.new(0, 25, 10)

-- Same as above, but use a Vector3 instead
local point = Vector3.new(0, 25, 10)
part.CFrame = CFrame.new(point)

-- Set the part's CFrame to be at one point, looking at another
local lookAtPoint = Vector3.new(0, 20, 15)
part.CFrame = CFrame.lookAt(point, lookAtPoint)

-- Rotate the part's CFrame by pi/2 radians on local X axis
part.CFrame = part.CFrame * CFrame.Angles(math.pi / 2, 0, 0)
-- Rotate the part's CFrame by 45 degrees on local Y axis
part.CFrame = part.CFrame * CFrame.Angles(0, math.rad(45), 0)
-- Rotate the part's CFrame by 180 degrees on global Z axis (note the order!)
part.CFrame = CFrame.Angles(0, 0, math.pi) * part.CFrame -- Pi radians is equal to 180 degrees

-- Composing two CFrames is done using * (the multiplication operator)
part.CFrame = CFrame.new(2, 3, 4) * CFrame.new(4, 5, 6) --> equal to CFrame.new(6, 8, 10)

-- Unlike algebraic multiplication, CFrame composition is NOT communitative: a * b is not necessarily b * a!
-- Imagine * as an ORDERED series of actions. For example, the following lines produce different CFrames:
-- 1) Slide the part 5 units on X.
-- 2) Rotate the part 45 degrees around its Y axis.
part.CFrame = CFrame.new(5, 0, 0) * CFrame.Angles(0, math.rad(45), 0)
-- 1) Rotate the part 45 degrees around its Y axis.
-- 2) Slide the part 5 units on X.
part.CFrame = CFrame.Angles(0, math.rad(45), 0) * CFrame.new(5, 0, 0)

-- There is no "CFrame division", but instead simply "doing the inverse operation".
part.CFrame = CFrame.new(4, 5, 6) * CFrame.new(4, 5, 6):Inverse() --> is equal to CFrame.new(0, 0, 0)
part.CFrame = CFrame.Angles(0, 0, math.pi) * CFrame.Angles(0, 0, math.pi):Inverse() --> equal to CFrame.Angles(0, 0, 0)

-- Position a part relative to another (in this case, put our part on top of otherPart)
part.CFrame = otherPart.CFrame * CFrame.new(0, part.Size.Y / 2 + otherPart.Size.Y / 2, 0)
```

### Property: BasePart.CollisionGroup

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
  "category": "Collision",
  "simulationAccess": true
}
```

The `CollisionGroup` property describes the name of the part's collision
group (maximum of 100 characters). Parts start off in the default group
whose name is `"Default"`. This value cannot be empty.

Although this property itself is non-replicated, the engine internally
replicates the value through another private property to solve backward
compatibility issues.

**WorldRoot:RegisterCollisionGroup**

This example demonstrates one basic use of collision groups. It assigns
**BallPart** to `"CollisionGroupBall"` and **DoorPart** to
`"CollisionGroupDoor"`, then makes the two groups non-collidable using
[WorldRoot:CollisionGroupSetCollidable()](/docs/reference/engine/classes/WorldRoot.md).

```lua
local Workspace = game:GetService("Workspace")

local collisionGroupBall = "CollisionGroupBall"
local collisionGroupDoor = "CollisionGroupDoor"

-- Register collision groups in Workspace
Workspace:RegisterCollisionGroup(collisionGroupBall)
Workspace:RegisterCollisionGroup(collisionGroupDoor)

-- Assign parts to collision groups
script.Parent.BallPart.CollisionGroup = collisionGroupBall
script.Parent.DoorPart.CollisionGroup = collisionGroupDoor

-- Set groups as non-collidable with each other and check the result
Workspace:CollisionGroupSetCollidable(collisionGroupBall, collisionGroupDoor, false)
print(Workspace:CollisionGroupsAreCollidable(collisionGroupBall, collisionGroupDoor)) --> false
```

### Property: BasePart.Color

```json
{
  "type": "Color3",
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
  "category": "Appearance"
}
```

The `Color` property determines the color of a part. If the part has a
[Material](/docs/reference/engine/classes/BasePart.md), this also determines the color used
when rendering the material texture.

If this property is set, [BrickColor](/docs/reference/engine/classes/BasePart.md) will use
the closest match to this `Color` value.

Other visual properties of a part are determined by
[Transparency](/docs/reference/engine/classes/BasePart.md) and
[Reflectance](/docs/reference/engine/classes/BasePart.md).

**Character Health Body Color**

This code sample colors a player's entire character based on how much health
they have. It generates a color based on their max health, then sets the color
properties of objects within their character, removing any extra objects.

```lua
-- Paste into a Script within StarterCharacterScripts
-- Then play the game, and fiddle with your character's health
local char = script.Parent
local human = char.Humanoid

local colorHealthy = Color3.new(0.4, 1, 0.2)
local colorUnhealthy = Color3.new(1, 0.4, 0.2)

local function setColor(color)
	for _, child in pairs(char:GetChildren()) do
		if child:IsA("BasePart") then
			child.Color = color
			while child:FindFirstChildOfClass("Decal") do
				child:FindFirstChildOfClass("Decal"):Destroy()
			end
		elseif child:IsA("Accessory") then
			child.Handle.Color = color
			local mesh = child.Handle:FindFirstChildOfClass("SpecialMesh")
			if mesh then
				mesh.TextureId = ""
			end
		elseif child:IsA("Shirt") or child:IsA("Pants") then
			child:Destroy()
		end
	end
end

local function update()
	local percentage = human.Health / human.MaxHealth

	-- Create a color by tweening based on the percentage of your health
	-- The color goes from colorHealthy (100%) ----- > colorUnhealthy (0%)
	local color = Color3.new(
		colorHealthy.R * percentage + colorUnhealthy.r * (1 - percentage),
		colorHealthy.G * percentage + colorUnhealthy.g * (1 - percentage),
		colorHealthy.B * percentage + colorUnhealthy.b * (1 - percentage)
	)
	setColor(color)
end

update()
human.HealthChanged:Connect(update)
```

### Property: BasePart.CurrentPhysicalProperties

```json
{
  "type": "PhysicalProperties",
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
  "category": "Part"
}
```

`CurrentPhysicalProperties` indicates the current physical properties of
the part. You can set custom values for the physical properties per part,
[custom material](/docs/en-us/parts/materials.md), and material override. The
Roblox engine prioritizes more granular definitions when determining the
effective physical properties of a part. The values in the following list
are in order from highest to lowest priority:

- Custom physical properties of the part
- Custom physical properties of the part's custom material
- Custom physical properties of the material override of the part's
  material
- Default physical properties of the part's material

### Property: BasePart.CustomPhysicalProperties

```json
{
  "type": "PhysicalProperties",
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
  "category": "Part",
  "simulationAccess": true
}
```

`CustomPhysicalProperties` lets you customize various physical aspects of
a part, such as its density, friction, and elasticity.

If enabled, this property let's you configure these physical properties.
If disabled, these physical properties are determined by the
[Material](/docs/reference/engine/classes/BasePart.md) of the part.

**Set CustomPhysicalProperties**

This code sample demonstrates how to set the CustomPhysicalProperties property
of a part.

```lua
local part = script.Parent

-- This will make the part light and bouncy!
local DENSITY = 0.3
local FRICTION = 0.1
local ELASTICITY = 1
local FRICTION_WEIGHT = 1
local ELASTICITY_WEIGHT = 1

local physProperties = PhysicalProperties.new(DENSITY, FRICTION, ELASTICITY, FRICTION_WEIGHT, ELASTICITY_WEIGHT)
part.CustomPhysicalProperties = physProperties
```

### Property: BasePart.EnableFluidForces

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
    "can_save": true
  },
  "thread_safety": "ReadSafe",
  "category": "Behavior",
  "simulationAccess": true
}
```

When `true`, and when [Workspace.FluidForces](/docs/reference/engine/classes/Workspace.md) is enabled, causes the
physics engine to compute aerodynamic forces on this [BasePart](/docs/reference/engine/classes/BasePart.md).

### Property: BasePart.ExtentsCFrame

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
  "category": "Transform",
  "simulationAccess": true
}
```

The [CFrame](/docs/reference/engine/datatypes/CFrame.md) of the physical extents of the [BasePart](/docs/reference/engine/classes/BasePart.md),
representing its physical center.

### Property: BasePart.ExtentsSize

```json
{
  "type": "Vector3",
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
  "category": "Transform",
  "simulationAccess": true
}
```

The actual physical size of the [BasePart](/docs/reference/engine/classes/BasePart.md) as regarded by the
physics engine, for example in
[collision detection](/docs/en-us/workspace/collisions.md).

### Property: BasePart.FrontSurface

```json
{
  "type": "SurfaceType",
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
  "category": "Surface"
}
```

The `FrontSurface` property determines the type of surface used for the
negative **Z** direction of a part. When two parts' faces are placed next
to each other, they may create a joint between them.

### Property: BasePart.LeftSurface

```json
{
  "type": "SurfaceType",
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
  "category": "Surface"
}
```

The `LeftSurface` property determines the type of surface used for the
negative **X** direction of a part. When two parts' faces are placed next
to each other, they may create a joint between them.

### Property: BasePart.Locked

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
    "can_save": true
  },
  "thread_safety": "ReadSafe",
  "category": "Data",
  "simulationAccess": true
}
```

The `Locked` property determines whether a part (or a [Model](/docs/reference/engine/classes/Model.md) it is
contained within) may be selected in Studio by clicking on it. This
property is most often enabled on parts within environment models that
aren't being edited at the moment.

**Recursive Unlock**

This code sample uses the concept of recursion to unlock all parts that are a
descendant of a model.

```lua
-- Paste into a Script within a Model you want to unlock
local model = script.Parent

-- This function recurses through a model's heirarchy and unlocks
-- every part that it encounters.
local function recursiveUnlock(object)
	if object:IsA("BasePart") then
		object.Locked = false
	end

	-- Call the same function on the children of the object
	-- The recursive process stops if an object has no children
	for _, child in pairs(object:GetChildren()) do
		recursiveUnlock(child)
	end
end

recursiveUnlock(model)
```

### Property: BasePart.Mass

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
  "category": "Part",
  "simulationAccess": true
}
```

`Mass` is a read-only property that describes the product of a part's
volume and density. It is returned by the
[GetMass()](/docs/reference/engine/classes/BasePart.md) function.

- The volume of a part is determined by its [Size](/docs/reference/engine/classes/BasePart.md) and
  its [Shape](/docs/reference/engine/classes/Part.md), which varies depending on the kind of
  [BasePart](/docs/reference/engine/classes/BasePart.md) used, such as [WedgePart](/docs/reference/engine/classes/WedgePart.md).
- The density of a part is determined by its
  [Material](/docs/reference/engine/classes/BasePart.md) or
  [CustomPhysicalProperties](/docs/reference/engine/classes/BasePart.md), if
  specified.

### Property: BasePart.Massless

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
    "can_save": true
  },
  "thread_safety": "ReadSafe",
  "category": "Part",
  "simulationAccess": true
}
```

If this property is enabled, the part will not contribute to the total
mass or inertia of its assembly as long as it is welded to another part
that has mass.

If the part is its own root part according to
[AssemblyRootPart](/docs/reference/engine/classes/BasePart.md), this will be ignored
for that part, and it will still contribute mass and inertia to its
assembly like a normal part. Parts that are massless should never become
an assembly root part unless all other parts in the assembly are also
massless.

This might be useful for things like optional accessories on vehicles that
you don't want to affect the handling of the car or a massless render mesh
welded to a simpler collision mesh.

See also [Assemblies](/docs/en-us/physics/assemblies.md), an article
documenting what root parts are and how to use them.

### Property: BasePart.Material

```json
{
  "type": "Material",
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
  "simulationAccess": true
}
```

The `Material` property allows you to set a part's texture and default
physical properties (in the case that
[CustomPhysicalProperties](/docs/reference/engine/classes/BasePart.md) is
unset). The default [Plastic](/docs/reference/engine/enums/Material.md) material has a very light
texture, while the [SmoothPlastic](/docs/reference/engine/enums/Material.md) material has no texture
at all. Some material textures like [DiamondPlate](/docs/reference/engine/enums/Material.md) and
[Granite](/docs/reference/engine/enums/Material.md) have very visible textures. Each material's
texture reflects sunlight differently, especially [Foil](/docs/reference/engine/enums/Material.md).

Setting this property then enabling
[CustomPhysicalProperties](/docs/reference/engine/classes/BasePart.md) will
use the default physical properties of a material. For instance,
[DiamondPlate](/docs/reference/engine/enums/Material.md) is a very dense material while
[Wood](/docs/reference/engine/enums/Material.md) is very light. A part's density determines whether it
will float in terrain water.

The [Glass](/docs/reference/engine/enums/Material.md) material changes rendering behavior on moderate
graphics settings by applying a bit of reflectiveness (similar to
[Reflectance](/docs/reference/engine/classes/BasePart.md)) and perspective distortion. The
effect is especially pronounced on sphere-shaped parts. Semi‑transparent
parts behind [Glass](/docs/reference/engine/enums/Material.md) parts are not visible.

### Property: BasePart.MaterialVariant

```json
{
  "type": "string",
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
  "category": "Appearance",
  "simulationAccess": true
}
```

The system searches the [MaterialVariant](/docs/reference/engine/classes/MaterialVariant.md) instance with the
specified `MaterialVariant` name and [Material](/docs/reference/engine/classes/BasePart.md)
type. If it successfully finds a matching [MaterialVariant](/docs/reference/engine/classes/MaterialVariant.md)
instance, it uses that instance to replace the default material. The
default material can be the built-in material or an override
[MaterialVariant](/docs/reference/engine/classes/MaterialVariant.md) specified in [MaterialService](/docs/reference/engine/classes/MaterialService.md).

### Property: BasePart.PivotOffset

```json
{
  "type": "CFrame",
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
  "category": "Pivot",
  "simulationAccess": true
}
```

This property specifies the offset of the part's pivot from its
[CFrame](/docs/reference/engine/datatypes/CFrame.md), that is [BasePart:GetPivot()](/docs/reference/engine/classes/BasePart.md) is the same as
[BasePart.CFrame](/docs/reference/engine/classes/BasePart.md) multiplied by [BasePart.PivotOffset](/docs/reference/engine/classes/BasePart.md).

This is convenient for setting the pivot to a location in **local** space,
but setting a part's pivot to a location in **world** space can be done as
follows:

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

**Clock Hands**

This code sample creates a clock at the origin with a minute, second, and hour
hand, and makes it tick, displaying the local time.

```lua
local function createHand(length, width, yOffset)
	local part = Instance.new("Part")
	part.Size = Vector3.new(width, 0.1, length)
	part.Material = Enum.Material.Neon
	part.PivotOffset = CFrame.new(0, -(yOffset + 0.1), length / 2)
	part.Anchored = true
	part.Parent = workspace
	return part
end

local function positionHand(hand, fraction)
	hand:PivotTo(CFrame.fromEulerAnglesXYZ(0, -fraction * 2 * math.pi, 0))
end

-- Create dial
for i = 0, 11 do
	local dialPart = Instance.new("Part")
	dialPart.Size = Vector3.new(0.2, 0.2, 1)
	dialPart.TopSurface = Enum.SurfaceType.Smooth
	if i == 0 then
		dialPart.Size = Vector3.new(0.2, 0.2, 2)
		dialPart.Color = Color3.new(1, 0, 0)
	end
	dialPart.PivotOffset = CFrame.new(0, -0.1, 10.5)
	dialPart.Anchored = true
	dialPart:PivotTo(CFrame.fromEulerAnglesXYZ(0, (i / 12) * 2 * math.pi, 0))
	dialPart.Parent = workspace
end

-- Create hands
local hourHand = createHand(7, 1, 0)
local minuteHand = createHand(10, 0.6, 0.1)
local secondHand = createHand(11, 0.2, 0.2)

-- Run clock
while true do
	local components = os.date("*t")
	positionHand(hourHand, (components.hour + components.min / 60) / 12)
	positionHand(minuteHand, (components.min + components.sec / 60) / 60)
	positionHand(secondHand, components.sec / 60)
	task.wait()
end
```

**Pivot Offset**

Demonstrates [BasePart.PivotOffset](/docs/reference/engine/classes/BasePart.md).

```lua
local Workspace = game:GetService("Workspace")

local bluePart = Instance.new("Part")
bluePart.Name = "BluePart"
bluePart.Parent = Workspace

local part = Workspace.BluePart
local desiredPivotCFrameInWorldSpace = CFrame.new(0, 10, 0)
part.PivotOffset = part.CFrame:ToObjectSpace(desiredPivotCFrameInWorldSpace)
```

### Property: BasePart.Reflectance

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
    "can_save": true
  },
  "thread_safety": "ReadSafe",
  "category": "Appearance"
}
```

The `Reflectance` property determines how much a part reflects the sky. A
value of `0` indicates the part is not reflective at all, and a value of
`1` indicates the part should fully reflect.

Reflectance is not affected by [Transparency](/docs/reference/engine/classes/BasePart.md)
unless the part is fully transparent, in which case reflectance will not
render at all. Reflectance may or may not be ignored depending on the
[Material](/docs/reference/engine/classes/BasePart.md) of the part.

### Property: BasePart.ResizeableFaces

```json
{
  "type": "Faces",
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

The `ResizeableFaces` property uses a [Faces](/docs/reference/engine/datatypes/Faces.md) object to describe
the different faces on which a part may be resized. For most
implementations of [BasePart](/docs/reference/engine/classes/BasePart.md), such as [Part](/docs/reference/engine/classes/Part.md) and
[WedgePart](/docs/reference/engine/classes/WedgePart.md), this property includes all faces. However,
[TrussPart](/docs/reference/engine/classes/TrussPart.md) will set its `ResizeableFaces` set to only two faces
since those kinds of parts must have two [Size](/docs/reference/engine/classes/BasePart.md)
dimensions of length `2`.

This property is most commonly used with tools for building and
manipulating parts and has little use outside of that context. The
[Handles](/docs/reference/engine/classes/Handles.md) class, which has the [Handles.Faces](/docs/reference/engine/classes/Handles.md) property, can
be used in conjunction with this property to display only the handles on
faces that can be resized on a part.

**Resize Handles**

This code sample creates a Handles object and shows how to set the Faces
property of the object. It also references ResizeableFaces of a part. Try
placing this script in multiple kinds of parts to see how ResizeableFaces
varies.

```lua
-- Put this Script in several kinds of BasePart, like
-- Part, TrussPart, WedgePart, CornerWedgePart, etc.
local part = script.Parent

-- Create a handles object for this part
local handles = Instance.new("Handles")
handles.Adornee = part
handles.Parent = part

-- Manually specify the faces applicable for this handle
handles.Faces = Faces.new(Enum.NormalId.Top, Enum.NormalId.Front, Enum.NormalId.Left)

-- Alternatively, use the faces on which the part can be resized.
-- If part is a TrussPart with only two Size dimensions
-- of length 2, then ResizeableFaces will only have two
-- enabled faces. For other parts, all faces will be enabled.
handles.Faces = part.ResizeableFaces
```

### Property: BasePart.ResizeIncrement

```json
{
  "type": "int",
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

The `ResizeIncrement` property is a read-only property that describes the
smallest change in size allowable by the
[Resize()](/docs/reference/engine/classes/BasePart.md) method. It differs between
implementations of the [BasePart](/docs/reference/engine/classes/BasePart.md) abstract class; for instance,
[Part](/docs/reference/engine/classes/Part.md) has this set to `1` while [TrussPart](/docs/reference/engine/classes/TrussPart.md) has this set to
`2` since individual truss sections are 2&times;2&times;2 in size.

### Property: BasePart.RightSurface

```json
{
  "type": "SurfaceType",
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
  "category": "Surface"
}
```

The `RightSurface` property determines the type of surface used for the
positive **X** direction of a part. When two parts' faces are placed next
to each other, they may create a joint between them.

### Property: BasePart.RootPriority

```json
{
  "type": "int",
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
  "category": "Part"
}
```

This property is an integer between `-127` and `127` that takes precedence
over all other rules for root part sort. When considering multiple parts
that are not [Anchored](/docs/reference/engine/classes/BasePart.md) and which share the same
[Massless](/docs/reference/engine/classes/BasePart.md) value, a part with a higher
`RootPriority` will take priority over those with lower `RootPriority`.

You can use this property to control which part of an assembly is the root
part and keep the root part stable if size changes.

See also [Assemblies](/docs/en-us/physics/assemblies.md), an article
documenting what root parts are and how to use them.

### Property: BasePart.Rotation

```json
{
  "type": "Vector3",
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
  "category": "Data",
  "simulationAccess": true
}
```

The rotation of the part in degrees for the three axes.

When setting this property, any [Welds](/docs/reference/engine/classes/Weld.md) or
[Motor6Ds](/docs/reference/engine/classes/Motor6D.md) connected to this part will have the matching
[C0](/docs/reference/engine/classes/JointInstance.md) or [C1](/docs/reference/engine/classes/JointInstance.md) property
updated to allow the part to move relative to any other parts it is joined
to. [WeldConstraints](/docs/reference/engine/classes/WeldConstraint.md) will also be temporarily
disabled and re-enabled during the move.

### Property: BasePart.Size

```json
{
  "type": "Vector3",
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
  "category": "Transform",
  "simulationAccess": true
}
```

A part's `Size` property determines its **visual** dimensions, while
[ExtentsSize](/docs/reference/engine/classes/BasePart.md) represents the actual size used
by the physics engine, such as in
[collision detection](/docs/en-us/workspace/collisions.md). The individual
dimensions (length, height, width) can be as low as `0.001` and as high as
`2048`. Size dimensions below `0.05` will be **physically** simulated as
if the part's dimensions are `0.05`, while visual rendering preserves the
actual size.

A part's `Size` is used in a variety of additional ways:

- To influence its mass as given by [GetMass()](/docs/reference/engine/classes/BasePart.md).
- By [ParticleEmitter](/docs/reference/engine/classes/ParticleEmitter.md) to determine the area from which particles
  are spawned.
- By [BlockMesh](/docs/reference/engine/classes/BlockMesh.md) to partially determine the rendered rectangular
  prism.
- By [SpecialMesh](/docs/reference/engine/classes/SpecialMesh.md) for certain
  [MeshTypes](/docs/reference/engine/classes/SpecialMesh.md) to determine the size of the
  rendered mesh.
- By [SurfaceLight](/docs/reference/engine/classes/SurfaceLight.md) to determine the space to illuminate.

**Pyramid Builder**

This code sample constructs a pyramid by stacking parts that get progressively
smaller. It also colors the parts so they blend between a start color and end
color.

```lua
local TOWER_BASE_SIZE = 30

local position = Vector3.new(50, 50, 50)

local hue = math.random()
local color0 = Color3.fromHSV(hue, 1, 1)
local color1 = Color3.fromHSV((hue + 0.35) % 1, 1, 1)

local model = Instance.new("Model")
model.Name = "Tower"

for i = TOWER_BASE_SIZE, 1, -2 do
	local part = Instance.new("Part")
	part.Size = Vector3.new(i, 2, i)
	part.Position = position
	part.Anchored = true
	part.Parent = model
	-- Tween from color0 and color1
	local perc = i / TOWER_BASE_SIZE
	part.Color = Color3.new(
		color0.R * perc + color1.R * (1 - perc),
		color0.G * perc + color1.G * (1 - perc),
		color0.B * perc + color1.B * (1 - perc)
	)

	position = position + Vector3.new(0, part.Size.Y, 0)
end
model.Parent = workspace
```

### Property: BasePart.TopSurface

```json
{
  "type": "SurfaceType",
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
  "category": "Surface"
}
```

The `TopSurface` property determines the type of surface used for the
positive **Y** direction of a part. When two parts' faces are placed next
to each other, they may create a joint between them.

### Property: BasePart.Transparency

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
    "can_save": true
  },
  "thread_safety": "ReadSafe",
  "category": "Appearance"
}
```

The `Transparency` property controls the visibility of a part on a scale
of `0` to `1` where `0` is completely visible (opaque) and `1` is
completely invisible (not rendered at all).

While fully transparent parts are not rendered at all, partially
transparent objects have some significant rendering costs. Having many
translucent parts may impact performance.

When transparent parts overlap, render order may act unpredictably, so you
should avoid semi-transparent parts from overlapping.

See also
[LocalTransparencyModifier](/docs/reference/engine/classes/BasePart.md) as a
multiplier to `Transparency` that's only visible to the local client.

**Fade Door**

This code sample shows how a part can fade away when touched by a Humanoid
then reappear a moment after to create a passable door.

```lua
-- Paste into a Script inside a tall part
local part = script.Parent

local OPEN_TIME = 1

-- Can the door be opened at the moment?
local debounce = false

local function open()
	part.CanCollide = false
	part.Transparency = 0.7
	part.BrickColor = BrickColor.new("Black")
end

local function close()
	part.CanCollide = true
	part.Transparency = 0
	part.BrickColor = BrickColor.new("Bright blue")
end

local function onTouch(otherPart)
	-- If the door was already open, do nothing
	if debounce then
		print("D")
		return
	end

	-- Check if touched by a Humanoid
	local human = otherPart.Parent:FindFirstChildOfClass("Humanoid")
	if not human then
		print("not human")
		return
	end

	-- Perform the door opening sequence
	debounce = true
	open()
	task.wait(OPEN_TIME)
	close()
	debounce = false
end

part.Touched:Connect(onTouch)
close()
```

### Property: BasePart.brickColor

```json
{
  "type": "BrickColor",
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
  "category": "Appearance"
}
```

> **Deprecated:** This deprecated property is an old Camel Case variant of the Pascal Case [BasePart.BrickColor](/docs/reference/engine/classes/BasePart.md), which should be used instead.

### Property: BasePart.CollisionGroupId

```json
{
  "type": "int",
  "access": "ReadWrite",
  "security": {
    "read": "None",
    "write": "None"
  },
  "serialization": {
    "can_load": true,
    "can_save": true
  },
  "deprecated": true,
  "thread_safety": "ReadSafe",
  "category": "Collision",
  "simulationAccess": true
}
```

The [BasePart.CollisionGroupId](/docs/reference/engine/classes/BasePart.md) property describes the ID number of
the part's collision group. Parts start off in the `"Default"` group whose
ID is 0. If a part is unregistered, the value becomes -1. This value
cannot be less than -1 and it cannot exceed
[WorldRoot:GetMaxCollisionGroups()](/docs/reference/engine/classes/WorldRoot.md). Invalid IDs are clamped.

Although this property can be directly changed, it's recommended that you
specify the collision group by setting [BasePart.CollisionGroup](/docs/reference/engine/classes/BasePart.md) to
the collision group's **name**.

### Property: BasePart.SpecificGravity

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
  "deprecated": true,
  "thread_safety": "ReadSafe",
  "category": "Data"
}
```

> **Deprecated:** This item is deprecated. See [BasePart.CustomPhysicalProperties](/docs/reference/engine/classes/BasePart.md) to see how to configure the physical properties of BaseParts. Do not use it for new work.

The ratio of the part's density to the density of water determined by the
[BasePart.Material](/docs/reference/engine/classes/BasePart.md). Effects the part's behavior when in a water
terrain cell. Essentially, SpecificGravity refers to how many times more
dense a part is than water.

| Material | SpecificGravity |
| --- | --- |
| Plastic | 0.7 |
| Wood | 0.35 |
| Slate | 2.7 |
| Concrete | 2.4 |
| CorrodedMetal | 7.85 |
| DiamondMetal | 7.85 |
| Foil | 7.6 |
| Grass | 0.9 |
| Ice | 0.91 |
| Marble | 2.56 |
| Granite | 2.7 |
| Brick | 1.92 |
| Pebble | 2.4 |
| Sand | 1.6 |
| Fabric | 0.7 |
| SmoothPlastic | 0.7 |
| Metal | 7.85 |
| WoodPlanks | 0.35 |
| Cobblestone | 2.7 |

### Property: BasePart.BackParamA *(hidden)*

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
    "can_save": true
  },
  "deprecated": true,
  "thread_safety": "ReadSafe",
  "category": "Surface Inputs"
}
```

The `BackParamA` property is relevant when a part's
[BasePart.BackSurface](/docs/reference/engine/classes/BasePart.md) is set to Motor or SteppingMotor and
[BasePart.BackSurfaceInput](/docs/reference/engine/classes/BasePart.md) is set to Sin. It determines the
**amplitude** of the motor's rotational velocity.

**Motor Control**

This code sample demonstrates how surface properties can be set using only a
NormalId (Top, Front, etc). It switches a motor's -SurfaceInput from NoInput,
Constant and Sin to show how each work using -ParamA and -ParamB properties.

```lua
-- Paste this into a Script inside a part with a Motor SurfaceType
local partMotor = script.Parent
-- Place a brick called "MovingPart" so it is touching the Motor surface

-- For this example, we use TopSurface, TopSurfaceInput, TopParamA and TopParamB
-- However, this will work for all faces (NormalId): Top, Bottom, Left, Right, Front and Back

-- A function to quickly set all surface properties at once
local function setFaceSurfaceInputParams(normalId, surfaceType, inputType, paramA, paramB)
	local surfaceName = normalId.Name -- e.g. "Top", "Bottom", etc

	-- Syntax Note: in Lua, part.Something is the same as part["Something"]
	-- The difference is that the latter allows us to use a string ("Something"), while
	-- the former requires use of an identifier (.Something). Below, we build of each the surface
	-- properties below by concatenating the surface name with the property postfix.

	-- Set "___Surface", eg "TopSurface"
	partMotor[surfaceName .. "Surface"] = surfaceType
	-- Set "___SurfaceInput", eg "TopSurfaceInput"
	partMotor[surfaceName .. "SurfaceInput"] = inputType
	-- Set "___ParamA", eg "TopParamA"
	partMotor[surfaceName .. "ParamA"] = paramA
	-- Set "___ParamB", eg "TopParamB"
	partMotor[surfaceName .. "ParamB"] = paramB
end

local normalId = Enum.NormalId.Top

while true do
	-- Set to NoInput, where the motor will not operate at all
	setFaceSurfaceInputParams(normalId, Enum.SurfaceType.Motor, Enum.InputType.NoInput, 0, 0)
	task.wait(1)
	-- Set to Constant, where motor rotational velocity = paramB
	setFaceSurfaceInputParams(normalId, Enum.SurfaceType.Motor, Enum.InputType.Constant, 0, 0.25)
	task.wait(2)
	-- Set to Sin, where motor rotational velocity = paramA * math.sin(time * paramB)
	-- Since we're using pi (~3.14), the frequency of rotation is 1 second (per definition of sine function)
	setFaceSurfaceInputParams(normalId, Enum.SurfaceType.Motor, Enum.InputType.Sin, 0.25, math.pi)
	task.wait(3)
end
```

### Property: BasePart.BackParamB *(hidden)*

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
    "can_save": true
  },
  "deprecated": true,
  "thread_safety": "ReadSafe",
  "category": "Surface Inputs"
}
```

The `BackParamB` property is relevant when a part's
[BasePart.BackSurface](/docs/reference/engine/classes/BasePart.md) is set to Motor or SteppingMotor and
[BasePart.BackSurfaceInput](/docs/reference/engine/classes/BasePart.md) is set to Constant or Sin. For Constant,
it determines the constant rotational velocity of the motor. For Sin, it
determines the **frequency** of the motor's rotational velocity.

**Motor Control**

This code sample demonstrates how surface properties can be set using only a
NormalId (Top, Front, etc). It switches a motor's -SurfaceInput from NoInput,
Constant and Sin to show how each work using -ParamA and -ParamB properties.

```lua
-- Paste this into a Script inside a part with a Motor SurfaceType
local partMotor = script.Parent
-- Place a brick called "MovingPart" so it is touching the Motor surface

-- For this example, we use TopSurface, TopSurfaceInput, TopParamA and TopParamB
-- However, this will work for all faces (NormalId): Top, Bottom, Left, Right, Front and Back

-- A function to quickly set all surface properties at once
local function setFaceSurfaceInputParams(normalId, surfaceType, inputType, paramA, paramB)
	local surfaceName = normalId.Name -- e.g. "Top", "Bottom", etc

	-- Syntax Note: in Lua, part.Something is the same as part["Something"]
	-- The difference is that the latter allows us to use a string ("Something"), while
	-- the former requires use of an identifier (.Something). Below, we build of each the surface
	-- properties below by concatenating the surface name with the property postfix.

	-- Set "___Surface", eg "TopSurface"
	partMotor[surfaceName .. "Surface"] = surfaceType
	-- Set "___SurfaceInput", eg "TopSurfaceInput"
	partMotor[surfaceName .. "SurfaceInput"] = inputType
	-- Set "___ParamA", eg "TopParamA"
	partMotor[surfaceName .. "ParamA"] = paramA
	-- Set "___ParamB", eg "TopParamB"
	partMotor[surfaceName .. "ParamB"] = paramB
end

local normalId = Enum.NormalId.Top

while true do
	-- Set to NoInput, where the motor will not operate at all
	setFaceSurfaceInputParams(normalId, Enum.SurfaceType.Motor, Enum.InputType.NoInput, 0, 0)
	task.wait(1)
	-- Set to Constant, where motor rotational velocity = paramB
	setFaceSurfaceInputParams(normalId, Enum.SurfaceType.Motor, Enum.InputType.Constant, 0, 0.25)
	task.wait(2)
	-- Set to Sin, where motor rotational velocity = paramA * math.sin(time * paramB)
	-- Since we're using pi (~3.14), the frequency of rotation is 1 second (per definition of sine function)
	setFaceSurfaceInputParams(normalId, Enum.SurfaceType.Motor, Enum.InputType.Sin, 0.25, math.pi)
	task.wait(3)
end
```

### Property: BasePart.BackSurfaceInput *(hidden)*

```json
{
  "type": "InputType",
  "access": "ReadWrite",
  "security": {
    "read": "None",
    "write": "None"
  },
  "serialization": {
    "can_load": true,
    "can_save": true
  },
  "deprecated": true,
  "thread_safety": "ReadSafe",
  "category": "Surface Inputs"
}
```

The `BackSurfaceInput` property determines the kind of input provided to a
part's [BasePart.BackSurface](/docs/reference/engine/classes/BasePart.md). This is only relevant for Motor or
SteppingMotor SurfaceTypes. This property determines how
[BasePart.BackParamA](/docs/reference/engine/classes/BasePart.md) and [BasePart.BackParamB](/docs/reference/engine/classes/BasePart.md) are used. For
brevity, these properties will be referred to as ParamA and ParamB,
respectively.

- By default, this is set to NoInput. This stops the motor altogether.
- For Constant, the motor rotates at a constant velocity equal to
  `ParamB`.
- For Sin, the motor rotates at a velocity equal to
  `ParamA * math.sin(workspace.DistributedGameTime * ParamB)`. See
  [Workspace.DistributedGameTime](/docs/reference/engine/classes/Workspace.md).

**Motor Control**

This code sample demonstrates how surface properties can be set using only a
NormalId (Top, Front, etc). It switches a motor's -SurfaceInput from NoInput,
Constant and Sin to show how each work using -ParamA and -ParamB properties.

```lua
-- Paste this into a Script inside a part with a Motor SurfaceType
local partMotor = script.Parent
-- Place a brick called "MovingPart" so it is touching the Motor surface

-- For this example, we use TopSurface, TopSurfaceInput, TopParamA and TopParamB
-- However, this will work for all faces (NormalId): Top, Bottom, Left, Right, Front and Back

-- A function to quickly set all surface properties at once
local function setFaceSurfaceInputParams(normalId, surfaceType, inputType, paramA, paramB)
	local surfaceName = normalId.Name -- e.g. "Top", "Bottom", etc

	-- Syntax Note: in Lua, part.Something is the same as part["Something"]
	-- The difference is that the latter allows us to use a string ("Something"), while
	-- the former requires use of an identifier (.Something). Below, we build of each the surface
	-- properties below by concatenating the surface name with the property postfix.

	-- Set "___Surface", eg "TopSurface"
	partMotor[surfaceName .. "Surface"] = surfaceType
	-- Set "___SurfaceInput", eg "TopSurfaceInput"
	partMotor[surfaceName .. "SurfaceInput"] = inputType
	-- Set "___ParamA", eg "TopParamA"
	partMotor[surfaceName .. "ParamA"] = paramA
	-- Set "___ParamB", eg "TopParamB"
	partMotor[surfaceName .. "ParamB"] = paramB
end

local normalId = Enum.NormalId.Top

while true do
	-- Set to NoInput, where the motor will not operate at all
	setFaceSurfaceInputParams(normalId, Enum.SurfaceType.Motor, Enum.InputType.NoInput, 0, 0)
	task.wait(1)
	-- Set to Constant, where motor rotational velocity = paramB
	setFaceSurfaceInputParams(normalId, Enum.SurfaceType.Motor, Enum.InputType.Constant, 0, 0.25)
	task.wait(2)
	-- Set to Sin, where motor rotational velocity = paramA * math.sin(time * paramB)
	-- Since we're using pi (~3.14), the frequency of rotation is 1 second (per definition of sine function)
	setFaceSurfaceInputParams(normalId, Enum.SurfaceType.Motor, Enum.InputType.Sin, 0.25, math.pi)
	task.wait(3)
end
```

### Property: BasePart.BottomParamA *(hidden)*

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
    "can_save": true
  },
  "deprecated": true,
  "thread_safety": "ReadSafe",
  "category": "Surface Inputs"
}
```

The `BottomParamA` property is relevant when a part's
[BasePart.BottomSurface](/docs/reference/engine/classes/BasePart.md) is set to Motor or SteppingMotor and
[BasePart.BottomSurfaceInput](/docs/reference/engine/classes/BasePart.md) is set to Sin. It determines the
**amplitude** of the motor's rotational velocity.

**Motor Control**

This code sample demonstrates how surface properties can be set using only a
NormalId (Top, Front, etc). It switches a motor's -SurfaceInput from NoInput,
Constant and Sin to show how each work using -ParamA and -ParamB properties.

```lua
-- Paste this into a Script inside a part with a Motor SurfaceType
local partMotor = script.Parent
-- Place a brick called "MovingPart" so it is touching the Motor surface

-- For this example, we use TopSurface, TopSurfaceInput, TopParamA and TopParamB
-- However, this will work for all faces (NormalId): Top, Bottom, Left, Right, Front and Back

-- A function to quickly set all surface properties at once
local function setFaceSurfaceInputParams(normalId, surfaceType, inputType, paramA, paramB)
	local surfaceName = normalId.Name -- e.g. "Top", "Bottom", etc

	-- Syntax Note: in Lua, part.Something is the same as part["Something"]
	-- The difference is that the latter allows us to use a string ("Something"), while
	-- the former requires use of an identifier (.Something). Below, we build of each the surface
	-- properties below by concatenating the surface name with the property postfix.

	-- Set "___Surface", eg "TopSurface"
	partMotor[surfaceName .. "Surface"] = surfaceType
	-- Set "___SurfaceInput", eg "TopSurfaceInput"
	partMotor[surfaceName .. "SurfaceInput"] = inputType
	-- Set "___ParamA", eg "TopParamA"
	partMotor[surfaceName .. "ParamA"] = paramA
	-- Set "___ParamB", eg "TopParamB"
	partMotor[surfaceName .. "ParamB"] = paramB
end

local normalId = Enum.NormalId.Top

while true do
	-- Set to NoInput, where the motor will not operate at all
	setFaceSurfaceInputParams(normalId, Enum.SurfaceType.Motor, Enum.InputType.NoInput, 0, 0)
	task.wait(1)
	-- Set to Constant, where motor rotational velocity = paramB
	setFaceSurfaceInputParams(normalId, Enum.SurfaceType.Motor, Enum.InputType.Constant, 0, 0.25)
	task.wait(2)
	-- Set to Sin, where motor rotational velocity = paramA * math.sin(time * paramB)
	-- Since we're using pi (~3.14), the frequency of rotation is 1 second (per definition of sine function)
	setFaceSurfaceInputParams(normalId, Enum.SurfaceType.Motor, Enum.InputType.Sin, 0.25, math.pi)
	task.wait(3)
end
```

### Property: BasePart.BottomParamB *(hidden)*

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
    "can_save": true
  },
  "deprecated": true,
  "thread_safety": "ReadSafe",
  "category": "Surface Inputs"
}
```

The `BottomParamB` property is relevant when a part's
[BasePart.BottomSurface](/docs/reference/engine/classes/BasePart.md) is set to Motor or SteppingMotor and
[BasePart.BottomSurfaceInput](/docs/reference/engine/classes/BasePart.md) is set to Constant or Sin. For
Constant, it determines the constant rotational velocity of the motor. For
Sin, it determines the **frequency** of the motor's rotational velocity.

**Motor Control**

This code sample demonstrates how surface properties can be set using only a
NormalId (Top, Front, etc). It switches a motor's -SurfaceInput from NoInput,
Constant and Sin to show how each work using -ParamA and -ParamB properties.

```lua
-- Paste this into a Script inside a part with a Motor SurfaceType
local partMotor = script.Parent
-- Place a brick called "MovingPart" so it is touching the Motor surface

-- For this example, we use TopSurface, TopSurfaceInput, TopParamA and TopParamB
-- However, this will work for all faces (NormalId): Top, Bottom, Left, Right, Front and Back

-- A function to quickly set all surface properties at once
local function setFaceSurfaceInputParams(normalId, surfaceType, inputType, paramA, paramB)
	local surfaceName = normalId.Name -- e.g. "Top", "Bottom", etc

	-- Syntax Note: in Lua, part.Something is the same as part["Something"]
	-- The difference is that the latter allows us to use a string ("Something"), while
	-- the former requires use of an identifier (.Something). Below, we build of each the surface
	-- properties below by concatenating the surface name with the property postfix.

	-- Set "___Surface", eg "TopSurface"
	partMotor[surfaceName .. "Surface"] = surfaceType
	-- Set "___SurfaceInput", eg "TopSurfaceInput"
	partMotor[surfaceName .. "SurfaceInput"] = inputType
	-- Set "___ParamA", eg "TopParamA"
	partMotor[surfaceName .. "ParamA"] = paramA
	-- Set "___ParamB", eg "TopParamB"
	partMotor[surfaceName .. "ParamB"] = paramB
end

local normalId = Enum.NormalId.Top

while true do
	-- Set to NoInput, where the motor will not operate at all
	setFaceSurfaceInputParams(normalId, Enum.SurfaceType.Motor, Enum.InputType.NoInput, 0, 0)
	task.wait(1)
	-- Set to Constant, where motor rotational velocity = paramB
	setFaceSurfaceInputParams(normalId, Enum.SurfaceType.Motor, Enum.InputType.Constant, 0, 0.25)
	task.wait(2)
	-- Set to Sin, where motor rotational velocity = paramA * math.sin(time * paramB)
	-- Since we're using pi (~3.14), the frequency of rotation is 1 second (per definition of sine function)
	setFaceSurfaceInputParams(normalId, Enum.SurfaceType.Motor, Enum.InputType.Sin, 0.25, math.pi)
	task.wait(3)
end
```

### Property: BasePart.BottomSurfaceInput *(hidden)*

```json
{
  "type": "InputType",
  "access": "ReadWrite",
  "security": {
    "read": "None",
    "write": "None"
  },
  "serialization": {
    "can_load": true,
    "can_save": true
  },
  "deprecated": true,
  "thread_safety": "ReadSafe",
  "category": "Surface Inputs"
}
```

The `BottomSurfaceInput` property determines the kind of input provided to
a part's [BasePart.BottomSurface](/docs/reference/engine/classes/BasePart.md). This is only relevant for Motor
or SteppingMotor SurfaceTypes. This property determines how
[BasePart.BottomParamA](/docs/reference/engine/classes/BasePart.md) and [BasePart.BottomParamB](/docs/reference/engine/classes/BasePart.md) are used.
For brevity, these properties will be referred to as ParamA and ParamB,
respectively.

- By default, this is set to NoInput. This stops the motor altogether.
- For Constant, the motor rotates at a constant velocity equal to
  `ParamB`.
- For Sin, the motor rotates at a velocity equal to
  `ParamA * math.sin(workspace.DistributedGameTime * ParamB)`. See
  [Workspace.DistributedGameTime](/docs/reference/engine/classes/Workspace.md).

**Motor Control**

This code sample demonstrates how surface properties can be set using only a
NormalId (Top, Front, etc). It switches a motor's -SurfaceInput from NoInput,
Constant and Sin to show how each work using -ParamA and -ParamB properties.

```lua
-- Paste this into a Script inside a part with a Motor SurfaceType
local partMotor = script.Parent
-- Place a brick called "MovingPart" so it is touching the Motor surface

-- For this example, we use TopSurface, TopSurfaceInput, TopParamA and TopParamB
-- However, this will work for all faces (NormalId): Top, Bottom, Left, Right, Front and Back

-- A function to quickly set all surface properties at once
local function setFaceSurfaceInputParams(normalId, surfaceType, inputType, paramA, paramB)
	local surfaceName = normalId.Name -- e.g. "Top", "Bottom", etc

	-- Syntax Note: in Lua, part.Something is the same as part["Something"]
	-- The difference is that the latter allows us to use a string ("Something"), while
	-- the former requires use of an identifier (.Something). Below, we build of each the surface
	-- properties below by concatenating the surface name with the property postfix.

	-- Set "___Surface", eg "TopSurface"
	partMotor[surfaceName .. "Surface"] = surfaceType
	-- Set "___SurfaceInput", eg "TopSurfaceInput"
	partMotor[surfaceName .. "SurfaceInput"] = inputType
	-- Set "___ParamA", eg "TopParamA"
	partMotor[surfaceName .. "ParamA"] = paramA
	-- Set "___ParamB", eg "TopParamB"
	partMotor[surfaceName .. "ParamB"] = paramB
end

local normalId = Enum.NormalId.Top

while true do
	-- Set to NoInput, where the motor will not operate at all
	setFaceSurfaceInputParams(normalId, Enum.SurfaceType.Motor, Enum.InputType.NoInput, 0, 0)
	task.wait(1)
	-- Set to Constant, where motor rotational velocity = paramB
	setFaceSurfaceInputParams(normalId, Enum.SurfaceType.Motor, Enum.InputType.Constant, 0, 0.25)
	task.wait(2)
	-- Set to Sin, where motor rotational velocity = paramA * math.sin(time * paramB)
	-- Since we're using pi (~3.14), the frequency of rotation is 1 second (per definition of sine function)
	setFaceSurfaceInputParams(normalId, Enum.SurfaceType.Motor, Enum.InputType.Sin, 0.25, math.pi)
	task.wait(3)
end
```

### Property: BasePart.Elasticity *(hidden)*

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
  "category": "Part"
}
```

> **Deprecated:** This is only one of multiple physics-related properties. It has been deprecated in favor of [BasePart.CustomPhysicalProperties](/docs/reference/engine/classes/BasePart.md), which combines these properties into one.

The Elasticity of a part is now determined by either its [Material](/docs/reference/engine/enums/Material.md)
or its `CustomPhysicalProperties`.

### Property: BasePart.Friction *(hidden)*

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
  "category": "Part"
}
```

> **Deprecated:** This is only one of multiple physics-related properties. It has been deprecated in favor of [BasePart.CustomPhysicalProperties](/docs/reference/engine/classes/BasePart.md), which combines these properties into one.

Used to control the Friction of the part, but now it no longer does
anything. The Friction of a part is now determined by either its
[Material](/docs/reference/engine/classes/BasePart.md) or its
[CustomPhysicalProperties](/docs/reference/engine/classes/BasePart.md).

### Property: BasePart.FrontParamA *(hidden)*

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
    "can_save": true
  },
  "deprecated": true,
  "thread_safety": "ReadSafe",
  "category": "Surface Inputs"
}
```

The `FrontParamA` property is relevant when a part's
[BasePart.FrontSurface](/docs/reference/engine/classes/BasePart.md) is set to Motor or SteppingMotor and
[BasePart.FrontSurfaceInput](/docs/reference/engine/classes/BasePart.md) is set to Sin. It determines the
**amplitude** of the motor's rotational velocity.

**Motor Control**

This code sample demonstrates how surface properties can be set using only a
NormalId (Top, Front, etc). It switches a motor's -SurfaceInput from NoInput,
Constant and Sin to show how each work using -ParamA and -ParamB properties.

```lua
-- Paste this into a Script inside a part with a Motor SurfaceType
local partMotor = script.Parent
-- Place a brick called "MovingPart" so it is touching the Motor surface

-- For this example, we use TopSurface, TopSurfaceInput, TopParamA and TopParamB
-- However, this will work for all faces (NormalId): Top, Bottom, Left, Right, Front and Back

-- A function to quickly set all surface properties at once
local function setFaceSurfaceInputParams(normalId, surfaceType, inputType, paramA, paramB)
	local surfaceName = normalId.Name -- e.g. "Top", "Bottom", etc

	-- Syntax Note: in Lua, part.Something is the same as part["Something"]
	-- The difference is that the latter allows us to use a string ("Something"), while
	-- the former requires use of an identifier (.Something). Below, we build of each the surface
	-- properties below by concatenating the surface name with the property postfix.

	-- Set "___Surface", eg "TopSurface"
	partMotor[surfaceName .. "Surface"] = surfaceType
	-- Set "___SurfaceInput", eg "TopSurfaceInput"
	partMotor[surfaceName .. "SurfaceInput"] = inputType
	-- Set "___ParamA", eg "TopParamA"
	partMotor[surfaceName .. "ParamA"] = paramA
	-- Set "___ParamB", eg "TopParamB"
	partMotor[surfaceName .. "ParamB"] = paramB
end

local normalId = Enum.NormalId.Top

while true do
	-- Set to NoInput, where the motor will not operate at all
	setFaceSurfaceInputParams(normalId, Enum.SurfaceType.Motor, Enum.InputType.NoInput, 0, 0)
	task.wait(1)
	-- Set to Constant, where motor rotational velocity = paramB
	setFaceSurfaceInputParams(normalId, Enum.SurfaceType.Motor, Enum.InputType.Constant, 0, 0.25)
	task.wait(2)
	-- Set to Sin, where motor rotational velocity = paramA * math.sin(time * paramB)
	-- Since we're using pi (~3.14), the frequency of rotation is 1 second (per definition of sine function)
	setFaceSurfaceInputParams(normalId, Enum.SurfaceType.Motor, Enum.InputType.Sin, 0.25, math.pi)
	task.wait(3)
end
```

### Property: BasePart.FrontParamB *(hidden)*

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
    "can_save": true
  },
  "deprecated": true,
  "thread_safety": "ReadSafe",
  "category": "Surface Inputs"
}
```

The `FrontParamB` property is relevant when a part's
[BasePart.FrontSurface](/docs/reference/engine/classes/BasePart.md) is set to Motor or SteppingMotor and
[BasePart.FrontSurfaceInput](/docs/reference/engine/classes/BasePart.md) is set to Constant or Sin. For
Constant, it determines the constant rotational velocity of the motor. For
Sin, it determines the **frequency** of the motor's rotational velocity.

**Motor Control**

This code sample demonstrates how surface properties can be set using only a
NormalId (Top, Front, etc). It switches a motor's -SurfaceInput from NoInput,
Constant and Sin to show how each work using -ParamA and -ParamB properties.

```lua
-- Paste this into a Script inside a part with a Motor SurfaceType
local partMotor = script.Parent
-- Place a brick called "MovingPart" so it is touching the Motor surface

-- For this example, we use TopSurface, TopSurfaceInput, TopParamA and TopParamB
-- However, this will work for all faces (NormalId): Top, Bottom, Left, Right, Front and Back

-- A function to quickly set all surface properties at once
local function setFaceSurfaceInputParams(normalId, surfaceType, inputType, paramA, paramB)
	local surfaceName = normalId.Name -- e.g. "Top", "Bottom", etc

	-- Syntax Note: in Lua, part.Something is the same as part["Something"]
	-- The difference is that the latter allows us to use a string ("Something"), while
	-- the former requires use of an identifier (.Something). Below, we build of each the surface
	-- properties below by concatenating the surface name with the property postfix.

	-- Set "___Surface", eg "TopSurface"
	partMotor[surfaceName .. "Surface"] = surfaceType
	-- Set "___SurfaceInput", eg "TopSurfaceInput"
	partMotor[surfaceName .. "SurfaceInput"] = inputType
	-- Set "___ParamA", eg "TopParamA"
	partMotor[surfaceName .. "ParamA"] = paramA
	-- Set "___ParamB", eg "TopParamB"
	partMotor[surfaceName .. "ParamB"] = paramB
end

local normalId = Enum.NormalId.Top

while true do
	-- Set to NoInput, where the motor will not operate at all
	setFaceSurfaceInputParams(normalId, Enum.SurfaceType.Motor, Enum.InputType.NoInput, 0, 0)
	task.wait(1)
	-- Set to Constant, where motor rotational velocity = paramB
	setFaceSurfaceInputParams(normalId, Enum.SurfaceType.Motor, Enum.InputType.Constant, 0, 0.25)
	task.wait(2)
	-- Set to Sin, where motor rotational velocity = paramA * math.sin(time * paramB)
	-- Since we're using pi (~3.14), the frequency of rotation is 1 second (per definition of sine function)
	setFaceSurfaceInputParams(normalId, Enum.SurfaceType.Motor, Enum.InputType.Sin, 0.25, math.pi)
	task.wait(3)
end
```

### Property: BasePart.FrontSurfaceInput *(hidden)*

```json
{
  "type": "InputType",
  "access": "ReadWrite",
  "security": {
    "read": "None",
    "write": "None"
  },
  "serialization": {
    "can_load": true,
    "can_save": true
  },
  "deprecated": true,
  "thread_safety": "ReadSafe",
  "category": "Surface Inputs"
}
```

The `FrontSurfaceInput` property determines the kind of input provided to
a part's [BasePart.FrontSurface](/docs/reference/engine/classes/BasePart.md). This is only relevant for Motor or
SteppingMotor SurfaceTypes. This property determines how
[BasePart.FrontParamA](/docs/reference/engine/classes/BasePart.md) and [BasePart.FrontParamB](/docs/reference/engine/classes/BasePart.md) are used.
For brevity, these properties will be referred to as ParamA and ParamB,
respectively.

- By default, this is set to NoInput. This stops the motor altogether.
- For Constant, the motor rotates at a constant velocity equal to
  `ParamB`.
- For Sin, the motor rotates at a velocity equal to
  `ParamA * math.sin(workspace.DistributedGameTime * ParamB)`. See
  [Workspace.DistributedGameTime](/docs/reference/engine/classes/Workspace.md).

**Motor Control**

This code sample demonstrates how surface properties can be set using only a
NormalId (Top, Front, etc). It switches a motor's -SurfaceInput from NoInput,
Constant and Sin to show how each work using -ParamA and -ParamB properties.

```lua
-- Paste this into a Script inside a part with a Motor SurfaceType
local partMotor = script.Parent
-- Place a brick called "MovingPart" so it is touching the Motor surface

-- For this example, we use TopSurface, TopSurfaceInput, TopParamA and TopParamB
-- However, this will work for all faces (NormalId): Top, Bottom, Left, Right, Front and Back

-- A function to quickly set all surface properties at once
local function setFaceSurfaceInputParams(normalId, surfaceType, inputType, paramA, paramB)
	local surfaceName = normalId.Name -- e.g. "Top", "Bottom", etc

	-- Syntax Note: in Lua, part.Something is the same as part["Something"]
	-- The difference is that the latter allows us to use a string ("Something"), while
	-- the former requires use of an identifier (.Something). Below, we build of each the surface
	-- properties below by concatenating the surface name with the property postfix.

	-- Set "___Surface", eg "TopSurface"
	partMotor[surfaceName .. "Surface"] = surfaceType
	-- Set "___SurfaceInput", eg "TopSurfaceInput"
	partMotor[surfaceName .. "SurfaceInput"] = inputType
	-- Set "___ParamA", eg "TopParamA"
	partMotor[surfaceName .. "ParamA"] = paramA
	-- Set "___ParamB", eg "TopParamB"
	partMotor[surfaceName .. "ParamB"] = paramB
end

local normalId = Enum.NormalId.Top

while true do
	-- Set to NoInput, where the motor will not operate at all
	setFaceSurfaceInputParams(normalId, Enum.SurfaceType.Motor, Enum.InputType.NoInput, 0, 0)
	task.wait(1)
	-- Set to Constant, where motor rotational velocity = paramB
	setFaceSurfaceInputParams(normalId, Enum.SurfaceType.Motor, Enum.InputType.Constant, 0, 0.25)
	task.wait(2)
	-- Set to Sin, where motor rotational velocity = paramA * math.sin(time * paramB)
	-- Since we're using pi (~3.14), the frequency of rotation is 1 second (per definition of sine function)
	setFaceSurfaceInputParams(normalId, Enum.SurfaceType.Motor, Enum.InputType.Sin, 0.25, math.pi)
	task.wait(3)
end
```

### Property: BasePart.LeftParamA *(hidden)*

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
    "can_save": true
  },
  "deprecated": true,
  "thread_safety": "ReadSafe",
  "category": "Surface Inputs"
}
```

The `LeftParamA` property is relevant when a part's
[BasePart.LeftSurface](/docs/reference/engine/classes/BasePart.md) is set to Motor or SteppingMotor and
[BasePart.LeftSurfaceInput](/docs/reference/engine/classes/BasePart.md) is set to Sin. It determines the
**amplitude** of the motor's rotational velocity.

**Motor Control**

This code sample demonstrates how surface properties can be set using only a
NormalId (Top, Front, etc). It switches a motor's -SurfaceInput from NoInput,
Constant and Sin to show how each work using -ParamA and -ParamB properties.

```lua
-- Paste this into a Script inside a part with a Motor SurfaceType
local partMotor = script.Parent
-- Place a brick called "MovingPart" so it is touching the Motor surface

-- For this example, we use TopSurface, TopSurfaceInput, TopParamA and TopParamB
-- However, this will work for all faces (NormalId): Top, Bottom, Left, Right, Front and Back

-- A function to quickly set all surface properties at once
local function setFaceSurfaceInputParams(normalId, surfaceType, inputType, paramA, paramB)
	local surfaceName = normalId.Name -- e.g. "Top", "Bottom", etc

	-- Syntax Note: in Lua, part.Something is the same as part["Something"]
	-- The difference is that the latter allows us to use a string ("Something"), while
	-- the former requires use of an identifier (.Something). Below, we build of each the surface
	-- properties below by concatenating the surface name with the property postfix.

	-- Set "___Surface", eg "TopSurface"
	partMotor[surfaceName .. "Surface"] = surfaceType
	-- Set "___SurfaceInput", eg "TopSurfaceInput"
	partMotor[surfaceName .. "SurfaceInput"] = inputType
	-- Set "___ParamA", eg "TopParamA"
	partMotor[surfaceName .. "ParamA"] = paramA
	-- Set "___ParamB", eg "TopParamB"
	partMotor[surfaceName .. "ParamB"] = paramB
end

local normalId = Enum.NormalId.Top

while true do
	-- Set to NoInput, where the motor will not operate at all
	setFaceSurfaceInputParams(normalId, Enum.SurfaceType.Motor, Enum.InputType.NoInput, 0, 0)
	task.wait(1)
	-- Set to Constant, where motor rotational velocity = paramB
	setFaceSurfaceInputParams(normalId, Enum.SurfaceType.Motor, Enum.InputType.Constant, 0, 0.25)
	task.wait(2)
	-- Set to Sin, where motor rotational velocity = paramA * math.sin(time * paramB)
	-- Since we're using pi (~3.14), the frequency of rotation is 1 second (per definition of sine function)
	setFaceSurfaceInputParams(normalId, Enum.SurfaceType.Motor, Enum.InputType.Sin, 0.25, math.pi)
	task.wait(3)
end
```

### Property: BasePart.LeftParamB *(hidden)*

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
    "can_save": true
  },
  "deprecated": true,
  "thread_safety": "ReadSafe",
  "category": "Surface Inputs"
}
```

The LeftParamB property is relevant when a part's
[BasePart.LeftSurface](/docs/reference/engine/classes/BasePart.md) is set to Motor or SteppingMotor and
[BasePart.LeftSurfaceInput](/docs/reference/engine/classes/BasePart.md) is set to Constant or Sin. For Constant,
it determines the constant rotational velocity of the motor. For Sin, it
determines the **frequency** of the motor's rotational velocity.

**Motor Control**

This code sample demonstrates how surface properties can be set using only a
NormalId (Top, Front, etc). It switches a motor's -SurfaceInput from NoInput,
Constant and Sin to show how each work using -ParamA and -ParamB properties.

```lua
-- Paste this into a Script inside a part with a Motor SurfaceType
local partMotor = script.Parent
-- Place a brick called "MovingPart" so it is touching the Motor surface

-- For this example, we use TopSurface, TopSurfaceInput, TopParamA and TopParamB
-- However, this will work for all faces (NormalId): Top, Bottom, Left, Right, Front and Back

-- A function to quickly set all surface properties at once
local function setFaceSurfaceInputParams(normalId, surfaceType, inputType, paramA, paramB)
	local surfaceName = normalId.Name -- e.g. "Top", "Bottom", etc

	-- Syntax Note: in Lua, part.Something is the same as part["Something"]
	-- The difference is that the latter allows us to use a string ("Something"), while
	-- the former requires use of an identifier (.Something). Below, we build of each the surface
	-- properties below by concatenating the surface name with the property postfix.

	-- Set "___Surface", eg "TopSurface"
	partMotor[surfaceName .. "Surface"] = surfaceType
	-- Set "___SurfaceInput", eg "TopSurfaceInput"
	partMotor[surfaceName .. "SurfaceInput"] = inputType
	-- Set "___ParamA", eg "TopParamA"
	partMotor[surfaceName .. "ParamA"] = paramA
	-- Set "___ParamB", eg "TopParamB"
	partMotor[surfaceName .. "ParamB"] = paramB
end

local normalId = Enum.NormalId.Top

while true do
	-- Set to NoInput, where the motor will not operate at all
	setFaceSurfaceInputParams(normalId, Enum.SurfaceType.Motor, Enum.InputType.NoInput, 0, 0)
	task.wait(1)
	-- Set to Constant, where motor rotational velocity = paramB
	setFaceSurfaceInputParams(normalId, Enum.SurfaceType.Motor, Enum.InputType.Constant, 0, 0.25)
	task.wait(2)
	-- Set to Sin, where motor rotational velocity = paramA * math.sin(time * paramB)
	-- Since we're using pi (~3.14), the frequency of rotation is 1 second (per definition of sine function)
	setFaceSurfaceInputParams(normalId, Enum.SurfaceType.Motor, Enum.InputType.Sin, 0.25, math.pi)
	task.wait(3)
end
```

### Property: BasePart.LeftSurfaceInput *(hidden)*

```json
{
  "type": "InputType",
  "access": "ReadWrite",
  "security": {
    "read": "None",
    "write": "None"
  },
  "serialization": {
    "can_load": true,
    "can_save": true
  },
  "deprecated": true,
  "thread_safety": "ReadSafe",
  "category": "Surface Inputs"
}
```

The `LeftSurfaceInput` property determines the kind of input provided to a
part's [BasePart.LeftSurface](/docs/reference/engine/classes/BasePart.md). This is only relevant for Motor or
SteppingMotor SurfaceTypes. This property determines how
[BasePart.LeftParamA](/docs/reference/engine/classes/BasePart.md) and [BasePart.LeftParamB](/docs/reference/engine/classes/BasePart.md) are used. For
brevity, these properties will be referred to as ParamA and ParamB,
respectively.

- By default, this is set to NoInput. This stops the motor altogether.
- For Constant, the motor rotates at a constant velocity equal to
  `ParamB`.
- For Sin, the motor rotates at a velocity equal to
  `ParamA * math.sin(workspace.DistributedGameTime * ParamB)`. See
  [Workspace.DistributedGameTime](/docs/reference/engine/classes/Workspace.md).

**Motor Control**

This code sample demonstrates how surface properties can be set using only a
NormalId (Top, Front, etc). It switches a motor's -SurfaceInput from NoInput,
Constant and Sin to show how each work using -ParamA and -ParamB properties.

```lua
-- Paste this into a Script inside a part with a Motor SurfaceType
local partMotor = script.Parent
-- Place a brick called "MovingPart" so it is touching the Motor surface

-- For this example, we use TopSurface, TopSurfaceInput, TopParamA and TopParamB
-- However, this will work for all faces (NormalId): Top, Bottom, Left, Right, Front and Back

-- A function to quickly set all surface properties at once
local function setFaceSurfaceInputParams(normalId, surfaceType, inputType, paramA, paramB)
	local surfaceName = normalId.Name -- e.g. "Top", "Bottom", etc

	-- Syntax Note: in Lua, part.Something is the same as part["Something"]
	-- The difference is that the latter allows us to use a string ("Something"), while
	-- the former requires use of an identifier (.Something). Below, we build of each the surface
	-- properties below by concatenating the surface name with the property postfix.

	-- Set "___Surface", eg "TopSurface"
	partMotor[surfaceName .. "Surface"] = surfaceType
	-- Set "___SurfaceInput", eg "TopSurfaceInput"
	partMotor[surfaceName .. "SurfaceInput"] = inputType
	-- Set "___ParamA", eg "TopParamA"
	partMotor[surfaceName .. "ParamA"] = paramA
	-- Set "___ParamB", eg "TopParamB"
	partMotor[surfaceName .. "ParamB"] = paramB
end

local normalId = Enum.NormalId.Top

while true do
	-- Set to NoInput, where the motor will not operate at all
	setFaceSurfaceInputParams(normalId, Enum.SurfaceType.Motor, Enum.InputType.NoInput, 0, 0)
	task.wait(1)
	-- Set to Constant, where motor rotational velocity = paramB
	setFaceSurfaceInputParams(normalId, Enum.SurfaceType.Motor, Enum.InputType.Constant, 0, 0.25)
	task.wait(2)
	-- Set to Sin, where motor rotational velocity = paramA * math.sin(time * paramB)
	-- Since we're using pi (~3.14), the frequency of rotation is 1 second (per definition of sine function)
	setFaceSurfaceInputParams(normalId, Enum.SurfaceType.Motor, Enum.InputType.Sin, 0.25, math.pi)
	task.wait(3)
end
```

### Property: BasePart.LocalTransparencyModifier *(hidden)*

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
  "category": "Data"
}
```

The `LocalTransparencyModifier` property is a multiplier to
[Transparency](/docs/reference/engine/classes/BasePart.md) that is only visible to the
local client. It does not replicate from client to server and is useful
for when a part should not render for a specific client, such as how the
player does not see their character's body parts when they zoom into first
person mode.

This property modifies the local part's transparency through the following
formula, with resulting values clamped between `0` and `1`.

`1` - ((`1` - [Transparency](/docs/reference/engine/classes/BasePart.md)) &times; (`1` -
`LocalTransparencyModifier`))

| [Transparency](/docs/reference/engine/classes/BasePart.md) | `LocalTransparencyModifier` | Server-Side | Client-Side |
| --- | --- | --- | --- |
| `0.5` | `0` | `0.5` | `0.5` |
| `0.5` | `0.25` | `0.5` | `0.625` |
| `0.5` | `0.5` | `0.5` | `0.75` |
| `0.5` | `0.75` | `0.5` | `0.875` |
| `0.5` | `1` | `0.5` | `1` |

### Property: BasePart.Orientation *(hidden)*

```json
{
  "type": "Vector3",
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
  "category": "Transform",
  "simulationAccess": true
}
```

The `Orientation` property describes the part's rotation in degrees around
the **X**, **Y**, and **Z** axes using a [Vector3](/docs/reference/engine/datatypes/Vector3.md). The rotations
are applied in **Y**&nbsp;⟩&nbsp;**X**&nbsp;⟩&nbsp;**Z** order. This
differs from proper [Euler][1] angles and is instead [Tait-Bryan][2]
angles which describe **yaw**, **pitch**, and **roll**.

It is also worth noting how this property differs from the
[CFrame.Angles()](/docs/reference/engine/datatypes/CFrame.md) constructor which applies rotations in a
different order (**Z**&nbsp;⟩&nbsp;**Y**&nbsp;⟩&nbsp;**X**). For better
control over the rotation of a part, it's recommended that
[CFrame](/docs/reference/engine/classes/BasePart.md) is set instead.

[1]: https://en.wikipedia.org/wiki/Euler_angles
[2]: https://en.wikipedia.org/wiki/Euler_angles#Tait-Bryan_angles

When setting this property, any [Welds](/docs/reference/engine/classes/Weld.md) or
[Motor6Ds](/docs/reference/engine/classes/Motor6D.md) connected to this part will have the matching
[C0](/docs/reference/engine/classes/JointInstance.md) or [C1](/docs/reference/engine/classes/JointInstance.md) property
updated to allow the part to move relative to any other parts it is joined
to. [WeldConstraints](/docs/reference/engine/classes/WeldConstraint.md) will also be temporarily
disabled and re-enabled during the move.

**Part Spinner**

This code sample rotates a part continually on the Y axis.

```lua
local part = script.Parent

local INCREMENT = 360 / 20

-- Rotate the part continually
while true do
	for degrees = 0, 360, INCREMENT do
		-- Set only the Y axis rotation
		part.Rotation = Vector3.new(0, degrees, 0)
		-- A better way to do this would be setting CFrame
		--part.CFrame = CFrame.new(part.Position) * CFrame.Angles(0, math.rad(degrees), 0)
		task.wait()
	end
end
```

### Property: BasePart.Position *(hidden)*

```json
{
  "type": "Vector3",
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
  "category": "Transform",
  "simulationAccess": true
}
```

The `Position` property describes the coordinates of a part using a
[Vector3](/docs/reference/engine/datatypes/Vector3.md). It reflects the position of the part's
[CFrame](/docs/reference/engine/classes/BasePart.md), however it can also be set.

When setting this property, any [Welds](/docs/reference/engine/classes/Weld.md) or
[Motor6Ds](/docs/reference/engine/classes/Motor6D.md) connected to this part will have the matching
[C0](/docs/reference/engine/classes/JointInstance.md) or [C1](/docs/reference/engine/classes/JointInstance.md) property
updated to allow the part to move relative to any other parts it is joined
to. [WeldConstraints](/docs/reference/engine/classes/WeldConstraint.md) will also be temporarily
disabled and re-enabled during the move.

### Property: BasePart.ReceiveAge *(hidden)*

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
  "category": "Part"
}
```

Indicates the time in seconds since the part's physics were last updated
on the local client or the server. This value will be `0` when the part
has no physics ([Anchored](/docs/reference/engine/classes/BasePart.md) is `true`).

### Property: BasePart.RightParamA *(hidden)*

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
    "can_save": true
  },
  "deprecated": true,
  "thread_safety": "ReadSafe",
  "category": "Surface Inputs"
}
```

The `RightParamA` property is relevant when a part's
[BasePart.RightSurface](/docs/reference/engine/classes/BasePart.md) is set to Motor or SteppingMotor and
[BasePart.RightSurfaceInput](/docs/reference/engine/classes/BasePart.md) is set to Sin. It determines the
**amplitude** of the motor's rotational velocity.

**Motor Control**

This code sample demonstrates how surface properties can be set using only a
NormalId (Top, Front, etc). It switches a motor's -SurfaceInput from NoInput,
Constant and Sin to show how each work using -ParamA and -ParamB properties.

```lua
-- Paste this into a Script inside a part with a Motor SurfaceType
local partMotor = script.Parent
-- Place a brick called "MovingPart" so it is touching the Motor surface

-- For this example, we use TopSurface, TopSurfaceInput, TopParamA and TopParamB
-- However, this will work for all faces (NormalId): Top, Bottom, Left, Right, Front and Back

-- A function to quickly set all surface properties at once
local function setFaceSurfaceInputParams(normalId, surfaceType, inputType, paramA, paramB)
	local surfaceName = normalId.Name -- e.g. "Top", "Bottom", etc

	-- Syntax Note: in Lua, part.Something is the same as part["Something"]
	-- The difference is that the latter allows us to use a string ("Something"), while
	-- the former requires use of an identifier (.Something). Below, we build of each the surface
	-- properties below by concatenating the surface name with the property postfix.

	-- Set "___Surface", eg "TopSurface"
	partMotor[surfaceName .. "Surface"] = surfaceType
	-- Set "___SurfaceInput", eg "TopSurfaceInput"
	partMotor[surfaceName .. "SurfaceInput"] = inputType
	-- Set "___ParamA", eg "TopParamA"
	partMotor[surfaceName .. "ParamA"] = paramA
	-- Set "___ParamB", eg "TopParamB"
	partMotor[surfaceName .. "ParamB"] = paramB
end

local normalId = Enum.NormalId.Top

while true do
	-- Set to NoInput, where the motor will not operate at all
	setFaceSurfaceInputParams(normalId, Enum.SurfaceType.Motor, Enum.InputType.NoInput, 0, 0)
	task.wait(1)
	-- Set to Constant, where motor rotational velocity = paramB
	setFaceSurfaceInputParams(normalId, Enum.SurfaceType.Motor, Enum.InputType.Constant, 0, 0.25)
	task.wait(2)
	-- Set to Sin, where motor rotational velocity = paramA * math.sin(time * paramB)
	-- Since we're using pi (~3.14), the frequency of rotation is 1 second (per definition of sine function)
	setFaceSurfaceInputParams(normalId, Enum.SurfaceType.Motor, Enum.InputType.Sin, 0.25, math.pi)
	task.wait(3)
end
```

### Property: BasePart.RightParamB *(hidden)*

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
    "can_save": true
  },
  "deprecated": true,
  "thread_safety": "ReadSafe",
  "category": "Surface Inputs"
}
```

The `RightParamB` property is relevant when a part's
[BasePart.RightSurface](/docs/reference/engine/classes/BasePart.md) is set to Motor or SteppingMotor and
[BasePart.RightSurfaceInput](/docs/reference/engine/classes/BasePart.md) is set to Constant or Sin. For
Constant, it determines the constant rotational velocity of the motor. For
Sin, it determines the **frequency** of the motor's rotational velocity.

**Motor Control**

This code sample demonstrates how surface properties can be set using only a
NormalId (Top, Front, etc). It switches a motor's -SurfaceInput from NoInput,
Constant and Sin to show how each work using -ParamA and -ParamB properties.

```lua
-- Paste this into a Script inside a part with a Motor SurfaceType
local partMotor = script.Parent
-- Place a brick called "MovingPart" so it is touching the Motor surface

-- For this example, we use TopSurface, TopSurfaceInput, TopParamA and TopParamB
-- However, this will work for all faces (NormalId): Top, Bottom, Left, Right, Front and Back

-- A function to quickly set all surface properties at once
local function setFaceSurfaceInputParams(normalId, surfaceType, inputType, paramA, paramB)
	local surfaceName = normalId.Name -- e.g. "Top", "Bottom", etc

	-- Syntax Note: in Lua, part.Something is the same as part["Something"]
	-- The difference is that the latter allows us to use a string ("Something"), while
	-- the former requires use of an identifier (.Something). Below, we build of each the surface
	-- properties below by concatenating the surface name with the property postfix.

	-- Set "___Surface", eg "TopSurface"
	partMotor[surfaceName .. "Surface"] = surfaceType
	-- Set "___SurfaceInput", eg "TopSurfaceInput"
	partMotor[surfaceName .. "SurfaceInput"] = inputType
	-- Set "___ParamA", eg "TopParamA"
	partMotor[surfaceName .. "ParamA"] = paramA
	-- Set "___ParamB", eg "TopParamB"
	partMotor[surfaceName .. "ParamB"] = paramB
end

local normalId = Enum.NormalId.Top

while true do
	-- Set to NoInput, where the motor will not operate at all
	setFaceSurfaceInputParams(normalId, Enum.SurfaceType.Motor, Enum.InputType.NoInput, 0, 0)
	task.wait(1)
	-- Set to Constant, where motor rotational velocity = paramB
	setFaceSurfaceInputParams(normalId, Enum.SurfaceType.Motor, Enum.InputType.Constant, 0, 0.25)
	task.wait(2)
	-- Set to Sin, where motor rotational velocity = paramA * math.sin(time * paramB)
	-- Since we're using pi (~3.14), the frequency of rotation is 1 second (per definition of sine function)
	setFaceSurfaceInputParams(normalId, Enum.SurfaceType.Motor, Enum.InputType.Sin, 0.25, math.pi)
	task.wait(3)
end
```

### Property: BasePart.RightSurfaceInput *(hidden)*

```json
{
  "type": "InputType",
  "access": "ReadWrite",
  "security": {
    "read": "None",
    "write": "None"
  },
  "serialization": {
    "can_load": true,
    "can_save": true
  },
  "deprecated": true,
  "thread_safety": "ReadSafe",
  "category": "Surface Inputs"
}
```

The RightSurfaceInput property determines the kind of input provided to a

- For Sin, the motor rotates at a velocity equal to
  `ParamA * math.sin(workspace.DistributedGameTime * ParamB)`. See
  [Workspace.DistributedGameTime](/docs/reference/engine/classes/Workspace.md).

**Motor Control**

This code sample demonstrates how surface properties can be set using only a
NormalId (Top, Front, etc). It switches a motor's -SurfaceInput from NoInput,
Constant and Sin to show how each work using -ParamA and -ParamB properties.

```lua
-- Paste this into a Script inside a part with a Motor SurfaceType
local partMotor = script.Parent
-- Place a brick called "MovingPart" so it is touching the Motor surface

-- For this example, we use TopSurface, TopSurfaceInput, TopParamA and TopParamB
-- However, this will work for all faces (NormalId): Top, Bottom, Left, Right, Front and Back

-- A function to quickly set all surface properties at once
local function setFaceSurfaceInputParams(normalId, surfaceType, inputType, paramA, paramB)
	local surfaceName = normalId.Name -- e.g. "Top", "Bottom", etc

	-- Syntax Note: in Lua, part.Something is the same as part["Something"]
	-- The difference is that the latter allows us to use a string ("Something"), while
	-- the former requires use of an identifier (.Something). Below, we build of each the surface
	-- properties below by concatenating the surface name with the property postfix.

	-- Set "___Surface", eg "TopSurface"
	partMotor[surfaceName .. "Surface"] = surfaceType
	-- Set "___SurfaceInput", eg "TopSurfaceInput"
	partMotor[surfaceName .. "SurfaceInput"] = inputType
	-- Set "___ParamA", eg "TopParamA"
	partMotor[surfaceName .. "ParamA"] = paramA
	-- Set "___ParamB", eg "TopParamB"
	partMotor[surfaceName .. "ParamB"] = paramB
end

local normalId = Enum.NormalId.Top

while true do
	-- Set to NoInput, where the motor will not operate at all
	setFaceSurfaceInputParams(normalId, Enum.SurfaceType.Motor, Enum.InputType.NoInput, 0, 0)
	task.wait(1)
	-- Set to Constant, where motor rotational velocity = paramB
	setFaceSurfaceInputParams(normalId, Enum.SurfaceType.Motor, Enum.InputType.Constant, 0, 0.25)
	task.wait(2)
	-- Set to Sin, where motor rotational velocity = paramA * math.sin(time * paramB)
	-- Since we're using pi (~3.14), the frequency of rotation is 1 second (per definition of sine function)
	setFaceSurfaceInputParams(normalId, Enum.SurfaceType.Motor, Enum.InputType.Sin, 0.25, math.pi)
	task.wait(3)
end
```

### Property: BasePart.RotVelocity *(hidden)*

```json
{
  "type": "Vector3",
  "access": "ReadWrite",
  "security": {
    "read": "None",
    "write": "None"
  },
  "serialization": {
    "can_load": true,
    "can_save": true
  },
  "deprecated": true,
  "thread_safety": "ReadSafe",
  "category": "Data",
  "simulationAccess": true
}
```

> **Deprecated:** This property is deprecated. Use `AssemblyAngularVelocity` instead.

The `RotVelocity` of a [part](/docs/reference/engine/classes/BasePart.md) describes how its
[BasePart.Orientation](/docs/reference/engine/classes/BasePart.md) is presently changing. In other words, this
property describes how the fast part is rotating. The part only rotates if
it is not anchored.

The unit of this property is **radians per second**.

Using this in conjunction with [AlignOrientation](/docs/reference/engine/classes/AlignOrientation.md) allows for aligned
parts to have matching RotVelocity and Orientation values.

**Rotating a Part with RotVelocity**

The script below creates a new `BasePart|part` and sets its
[Part.RotVelocity](/docs/reference/engine/classes/Part.md) to `Vector3.new(0, 10, 0)` every
[RunService.RenderStepped](/docs/reference/engine/classes/RunService.md) so that the part rotates in a circular
motion.

```lua
local RunService = game:GetService("RunService")

local part = Instance.new("Part")
part.Name = "RotatingPart"
part.Position = Vector3.new(0, 1, 0)
part.Parent = workspace

local function renderStepped()
	part.RotVelocity = Vector3.new(0, 10, 0)
end

RunService.RenderStepped:Connect(renderStepped)
```

### Property: BasePart.TopParamA *(hidden)*

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
    "can_save": true
  },
  "deprecated": true,
  "thread_safety": "ReadSafe",
  "category": "Surface Inputs"
}
```

The TopParamA property is relevant when a part's
[BasePart.TopSurface](/docs/reference/engine/classes/BasePart.md) is set to Motor or SteppingMotor and
[BasePart.TopSurfaceInput](/docs/reference/engine/classes/BasePart.md) is set to Sin. It determines the
**amplitude** of the motor's rotational velocity.

**Motor Control**

This code sample demonstrates how surface properties can be set using only a
NormalId (Top, Front, etc). It switches a motor's -SurfaceInput from NoInput,
Constant and Sin to show how each work using -ParamA and -ParamB properties.

```lua
-- Paste this into a Script inside a part with a Motor SurfaceType
local partMotor = script.Parent
-- Place a brick called "MovingPart" so it is touching the Motor surface

-- For this example, we use TopSurface, TopSurfaceInput, TopParamA and TopParamB
-- However, this will work for all faces (NormalId): Top, Bottom, Left, Right, Front and Back

-- A function to quickly set all surface properties at once
local function setFaceSurfaceInputParams(normalId, surfaceType, inputType, paramA, paramB)
	local surfaceName = normalId.Name -- e.g. "Top", "Bottom", etc

	-- Syntax Note: in Lua, part.Something is the same as part["Something"]
	-- The difference is that the latter allows us to use a string ("Something"), while
	-- the former requires use of an identifier (.Something). Below, we build of each the surface
	-- properties below by concatenating the surface name with the property postfix.

	-- Set "___Surface", eg "TopSurface"
	partMotor[surfaceName .. "Surface"] = surfaceType
	-- Set "___SurfaceInput", eg "TopSurfaceInput"
	partMotor[surfaceName .. "SurfaceInput"] = inputType
	-- Set "___ParamA", eg "TopParamA"
	partMotor[surfaceName .. "ParamA"] = paramA
	-- Set "___ParamB", eg "TopParamB"
	partMotor[surfaceName .. "ParamB"] = paramB
end

local normalId = Enum.NormalId.Top

while true do
	-- Set to NoInput, where the motor will not operate at all
	setFaceSurfaceInputParams(normalId, Enum.SurfaceType.Motor, Enum.InputType.NoInput, 0, 0)
	task.wait(1)
	-- Set to Constant, where motor rotational velocity = paramB
	setFaceSurfaceInputParams(normalId, Enum.SurfaceType.Motor, Enum.InputType.Constant, 0, 0.25)
	task.wait(2)
	-- Set to Sin, where motor rotational velocity = paramA * math.sin(time * paramB)
	-- Since we're using pi (~3.14), the frequency of rotation is 1 second (per definition of sine function)
	setFaceSurfaceInputParams(normalId, Enum.SurfaceType.Motor, Enum.InputType.Sin, 0.25, math.pi)
	task.wait(3)
end
```

### Property: BasePart.TopParamB *(hidden)*

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
    "can_save": true
  },
  "deprecated": true,
  "thread_safety": "ReadSafe",
  "category": "Surface Inputs"
}
```

The TopParamB property is relevant when a part's
[BasePart.TopSurface](/docs/reference/engine/classes/BasePart.md) is set to Motor or SteppingMotor and
[BasePart.TopSurfaceInput](/docs/reference/engine/classes/BasePart.md) is set to Constant or Sin. For Constant,
it determines the constant rotational velocity of the motor. For Sin, it
determines the **frequency** of the motor's rotational velocity.

**Motor Control**

This code sample demonstrates how surface properties can be set using only a
NormalId (Top, Front, etc). It switches a motor's -SurfaceInput from NoInput,
Constant and Sin to show how each work using -ParamA and -ParamB properties.

```lua
-- Paste this into a Script inside a part with a Motor SurfaceType
local partMotor = script.Parent
-- Place a brick called "MovingPart" so it is touching the Motor surface

-- For this example, we use TopSurface, TopSurfaceInput, TopParamA and TopParamB
-- However, this will work for all faces (NormalId): Top, Bottom, Left, Right, Front and Back

-- A function to quickly set all surface properties at once
local function setFaceSurfaceInputParams(normalId, surfaceType, inputType, paramA, paramB)
	local surfaceName = normalId.Name -- e.g. "Top", "Bottom", etc

	-- Syntax Note: in Lua, part.Something is the same as part["Something"]
	-- The difference is that the latter allows us to use a string ("Something"), while
	-- the former requires use of an identifier (.Something). Below, we build of each the surface
	-- properties below by concatenating the surface name with the property postfix.

	-- Set "___Surface", eg "TopSurface"
	partMotor[surfaceName .. "Surface"] = surfaceType
	-- Set "___SurfaceInput", eg "TopSurfaceInput"
	partMotor[surfaceName .. "SurfaceInput"] = inputType
	-- Set "___ParamA", eg "TopParamA"
	partMotor[surfaceName .. "ParamA"] = paramA
	-- Set "___ParamB", eg "TopParamB"
	partMotor[surfaceName .. "ParamB"] = paramB
end

local normalId = Enum.NormalId.Top

while true do
	-- Set to NoInput, where the motor will not operate at all
	setFaceSurfaceInputParams(normalId, Enum.SurfaceType.Motor, Enum.InputType.NoInput, 0, 0)
	task.wait(1)
	-- Set to Constant, where motor rotational velocity = paramB
	setFaceSurfaceInputParams(normalId, Enum.SurfaceType.Motor, Enum.InputType.Constant, 0, 0.25)
	task.wait(2)
	-- Set to Sin, where motor rotational velocity = paramA * math.sin(time * paramB)
	-- Since we're using pi (~3.14), the frequency of rotation is 1 second (per definition of sine function)
	setFaceSurfaceInputParams(normalId, Enum.SurfaceType.Motor, Enum.InputType.Sin, 0.25, math.pi)
	task.wait(3)
end
```

### Property: BasePart.TopSurfaceInput *(hidden)*

```json
{
  "type": "InputType",
  "access": "ReadWrite",
  "security": {
    "read": "None",
    "write": "None"
  },
  "serialization": {
    "can_load": true,
    "can_save": true
  },
  "deprecated": true,
  "thread_safety": "ReadSafe",
  "category": "Surface Inputs"
}
```

The `TopSurfaceInput` property determines the kind of input provided to a
part's [BasePart.TopSurface](/docs/reference/engine/classes/BasePart.md). This is only relevant for Motor or
SteppingMotor SurfaceTypes. This property determines how
[BasePart.TopParamA](/docs/reference/engine/classes/BasePart.md) and [BasePart.TopParamB](/docs/reference/engine/classes/BasePart.md) are used. For
brevity, these properties will be referred to as ParamA and ParamB,
respectively.

- By default, this is set to NoInput. This stops the motor altogether,
- For Constant, the motor rotates at a constant velocity equal to
  `ParamB`.
- For Sin, the motor rotates at a velocity equal to
  `ParamA * math.sin(workspace.DistributedGameTime * ParamB)`. See
  [Workspace.DistributedGameTime](/docs/reference/engine/classes/Workspace.md).

**Motor Control**

This code sample demonstrates how surface properties can be set using only a
NormalId (Top, Front, etc). It switches a motor's -SurfaceInput from NoInput,
Constant and Sin to show how each work using -ParamA and -ParamB properties.

```lua
-- Paste this into a Script inside a part with a Motor SurfaceType
local partMotor = script.Parent
-- Place a brick called "MovingPart" so it is touching the Motor surface

-- For this example, we use TopSurface, TopSurfaceInput, TopParamA and TopParamB
-- However, this will work for all faces (NormalId): Top, Bottom, Left, Right, Front and Back

-- A function to quickly set all surface properties at once
local function setFaceSurfaceInputParams(normalId, surfaceType, inputType, paramA, paramB)
	local surfaceName = normalId.Name -- e.g. "Top", "Bottom", etc

	-- Syntax Note: in Lua, part.Something is the same as part["Something"]
	-- The difference is that the latter allows us to use a string ("Something"), while
	-- the former requires use of an identifier (.Something). Below, we build of each the surface
	-- properties below by concatenating the surface name with the property postfix.

	-- Set "___Surface", eg "TopSurface"
	partMotor[surfaceName .. "Surface"] = surfaceType
	-- Set "___SurfaceInput", eg "TopSurfaceInput"
	partMotor[surfaceName .. "SurfaceInput"] = inputType
	-- Set "___ParamA", eg "TopParamA"
	partMotor[surfaceName .. "ParamA"] = paramA
	-- Set "___ParamB", eg "TopParamB"
	partMotor[surfaceName .. "ParamB"] = paramB
end

local normalId = Enum.NormalId.Top

while true do
	-- Set to NoInput, where the motor will not operate at all
	setFaceSurfaceInputParams(normalId, Enum.SurfaceType.Motor, Enum.InputType.NoInput, 0, 0)
	task.wait(1)
	-- Set to Constant, where motor rotational velocity = paramB
	setFaceSurfaceInputParams(normalId, Enum.SurfaceType.Motor, Enum.InputType.Constant, 0, 0.25)
	task.wait(2)
	-- Set to Sin, where motor rotational velocity = paramA * math.sin(time * paramB)
	-- Since we're using pi (~3.14), the frequency of rotation is 1 second (per definition of sine function)
	setFaceSurfaceInputParams(normalId, Enum.SurfaceType.Motor, Enum.InputType.Sin, 0.25, math.pi)
	task.wait(3)
end
```

### Property: BasePart.Velocity *(hidden)*

```json
{
  "type": "Vector3",
  "access": "ReadWrite",
  "security": {
    "read": "None",
    "write": "None"
  },
  "serialization": {
    "can_load": true,
    "can_save": true
  },
  "deprecated": true,
  "thread_safety": "ReadSafe",
  "category": "Data",
  "simulationAccess": true
}
```

> **Deprecated:** This property is deprecated. Use `AssemblyLinearVelocity` instead.

The Velocity of a part describes how its [BasePart.Position](/docs/reference/engine/classes/BasePart.md) is
presently changing. The unit of this property is **studs per second**. For
reference, the default Roblox character moves at 16 studs per second via
[Humanoid.WalkSpeed](/docs/reference/engine/classes/Humanoid.md). The acceleration due to gravity is found in
[Workspace.Gravity](/docs/reference/engine/classes/Workspace.md) (by default, -196.2 studs per second per
second).

Setting the Velocity of a part that is [BasePart.Anchored](/docs/reference/engine/classes/BasePart.md) will
cause it to act like a conveyor belt. Any object that touches the part
will begin to move in accordance with the Velocity.

Some [BodyMover](/docs/reference/engine/classes/BodyMover.md) objects will apply forces and thus change the
Velocity of a part over time. The simplest of these is a [BodyForce](/docs/reference/engine/classes/BodyForce.md)
which can be used to counteract the acceleration due to gravity on a
single part (set the +Y axis of the [BodyForce.Force](/docs/reference/engine/classes/BodyForce.md) to the product
of the mass ([BasePart:GetMass()](/docs/reference/engine/classes/BasePart.md)) and the gravity constant).

**Projectile Firing**

This code sample fires a part from one position toward another. It calculates
the velocity needed to reach the destination in time, and applies an
anti-gravity effect using a BodyForce. In addition, it adds a Trail to better
visualize the path of the projectile as it arcs through the air.

```lua
-- Put this Script in a Part, preferably bullet-shaped :)
local part = script.Parent
part.Shape = Enum.PartType.Ball
part.Size = Vector3.new(2, 2, 2)
part.BrickColor = BrickColor.new("Really black")
part.CanCollide = false

local MY_START_POINT = Vector3.new(0, 50, 0)
local MY_TARGET_POINT = Vector3.new(50, 100, 0)
local TRAVEL_TIME = 1
local ANTI_GRAVITY = 0.5

-- Anti-gravity effect: add a BodyForce to counter gravity
local bf = Instance.new("BodyForce")
bf.Force = Vector3.new(0, workspace.Gravity * part:GetMass() * ANTI_GRAVITY, 0)
bf.Parent = part

local a0 = Instance.new("Attachment")
a0.Position = Vector3.new(1, 0, 0)
a0.Parent = part

local a1 = Instance.new("Attachment")
a1.Position = Vector3.new(-1, 0, 0)
a1.Parent = part

local trail = Instance.new("Trail")
trail.Parent = part
trail.Attachment0 = a0
trail.Attachment1 = a1
trail.FaceCamera = true
trail.Transparency = NumberSequence.new({
	NumberSequenceKeypoint.new(0, 0),
	NumberSequenceKeypoint.new(1, 1),
})
trail.Lifetime = 0.35

local function fire(startPoint, targetPoint)
	-- Calculate how far we have to travel
	local distance = (targetPoint - startPoint).magnitude
	local speed = distance / TRAVEL_TIME
	part.CFrame = CFrame.new(startPoint, targetPoint)
	-- Shoot the part
	part.Velocity = part.CFrame.LookVector * speed
end

while true do
	fire(MY_START_POINT, MY_TARGET_POINT)
	task.wait(TRAVEL_TIME)
end
```

## Methods

### Method: BasePart:AngularAccelerationToTorque

**Signature:** `BasePart:AngularAccelerationToTorque(angAcceleration: Vector3, angVelocity?: Vector3): Vector3`

Returns the world-space torque vector that must be applied to the part's
assembly to achieve the specified angular acceleration. This result can be
used to determine the torque that should be applied via a [Torque](/docs/reference/engine/classes/Torque.md)
instance or [BasePart:ApplyAngularImpulse()](/docs/reference/engine/classes/BasePart.md).

The calculation uses Euler's rotation equation where _I_ is the assembly's
world-space inertia tensor, _α_ is the desired angular acceleration, and
_ω_ is the angular velocity.

_τ = I · α + ω × (I · ω)_

If the part is not a descendant of [Workspace](/docs/reference/engine/classes/Workspace.md), this method returns
a vector of infinity. If the assembly is anchored, it similarly returns a
vector of infinity.

#### Gyroscopic Effects

When a spinning assembly has an asymmetric inertia tensor, the torque
required to achieve a specified angular acceerlation is augmented due to
the changing orientation of the body. The optional `angVelocity` parameter
accounts for these gyroscopic effects. If omitted, these gyroscopic
effects are omitted from the calculation.

*Security: None · Thread Safety: Unsafe · Simulation Access: true*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `angAcceleration` | `Vector3` |  | The desired angular acceleration vector in world space. |
| `angVelocity` | `Vector3` | `0, 0, 0` | The current angular velocity of the assembly in world space. Defaults to `(0, 0, 0)`. Supply the assembly's angular velocity to account for gyroscopic effects. |

**Returns:** `Vector3` — A [Vector3](/docs/reference/engine/datatypes/Vector3.md) representing the world-space torque required to
produce the specified angular acceleration.

**Angular Acceleration To Torque**

Demonstrates [BasePart:AngularAccelerationToTorque()](/docs/reference/engine/classes/BasePart.md).

```lua
local part = Instance.new("Part")
part.Parent = workspace

local angularVelocity = part.AssemblyAngularVelocity
local desiredAcceleration = Vector3.new(0, 10, 0)

-- Compute the torque needed to achieve the desired acceleration
local torque = part:AngularAccelerationToTorque(desiredAcceleration, angularVelocity)
```

### Method: BasePart:ApplyAngularImpulse

**Signature:** `BasePart:ApplyAngularImpulse(impulse: Vector3): ()`

Applies an instant angular force impulse to this part's assembly, causing
the assembly to spin.

The resulting angular velocity from the impulse relies on the assembly's
[mass](/docs/reference/engine/classes/BasePart.md). So a higher impulse is required to
move more massive assemblies. Impulses are useful for cases where you want
a force applied instantly, such as an explosion or collision.

If the part is [owned](/docs/en-us/physics/network-ownership.md) by the
server, this function must be called from a server [Script](/docs/reference/engine/classes/Script.md) (not
from a [LocalScript](/docs/reference/engine/classes/LocalScript.md) or a [Script](/docs/reference/engine/classes/Script.md) with
[RunContext](/docs/reference/engine/classes/BaseScript.md) set to [RunContext.Client](/docs/reference/engine/enums/RunContext.md)).
If the part is owned by a client through **automatic** ownership, this
function can be called from either a client script **or** a server script;
calling it from a client script for a server-owned part will have no
effect.

*Security: None · Thread Safety: Unsafe · Simulation Access: true*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `impulse` | `Vector3` |  | An angular impulse vector to be applied to the assembly. |

**Returns:** `()`

### Method: BasePart:ApplyImpulse

**Signature:** `BasePart:ApplyImpulse(impulse: Vector3): ()`

This function applies an instant force impulse to this part's assembly.

The force is applied at the assembly's
[center of mass](/docs/reference/engine/classes/BasePart.md), so the resulting
movement will only be linear.

The resulting velocity from the impulse relies on the assembly's
[mass](/docs/reference/engine/classes/BasePart.md). So a higher impulse is required to
move more massive assemblies. Impulses are useful for cases where you want
a force applied instantly, such as an explosion or collision.

If the part is [owned](/docs/en-us/physics/network-ownership.md) by the
server, this function must be called from a server [Script](/docs/reference/engine/classes/Script.md) (not
from a [LocalScript](/docs/reference/engine/classes/LocalScript.md) or a [Script](/docs/reference/engine/classes/Script.md) with
[RunContext](/docs/reference/engine/classes/BaseScript.md) set to [RunContext.Client](/docs/reference/engine/enums/RunContext.md)).
If the part is owned by a client through **automatic** ownership, this
function can be called from either a client script **or** a server script;
calling it from a client script for a server-owned part will have no
effect.

*Security: None · Thread Safety: Unsafe · Simulation Access: true*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `impulse` | `Vector3` |  | A linear impulse vector to be applied to the assembly. |

**Returns:** `()`

### Method: BasePart:ApplyImpulseAtPosition

**Signature:** `BasePart:ApplyImpulseAtPosition(impulse: Vector3, position: Vector3): ()`

This function applies an instant force impulse to this part's assembly, at
the specified position in world space.

If the position is not at the assembly's
[center of mass](/docs/reference/engine/classes/BasePart.md), the impulse will
cause a positional and rotational movement.

The resulting velocity from the impulse relies on the assembly's
[mass](/docs/reference/engine/classes/BasePart.md). So a higher impulse is required to
move more massive assemblies. Impulses are useful for cases where
developers want a force applied instantly, such as an explosion or
collision.

If the part is [owned](/docs/en-us/physics/network-ownership.md) by the
server, this function must be called from a server [Script](/docs/reference/engine/classes/Script.md) (not
from a [LocalScript](/docs/reference/engine/classes/LocalScript.md) or a [Script](/docs/reference/engine/classes/Script.md) with
[RunContext](/docs/reference/engine/classes/BaseScript.md) set to [RunContext.Client](/docs/reference/engine/enums/RunContext.md)).
If the part is owned by a client through **automatic** ownership, this
function can be called from either a client script **or** a server script;
calling it from a client script for a server-owned part will have no
effect.

*Security: None · Thread Safety: Unsafe · Simulation Access: true*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `impulse` | `Vector3` |  | An impulse vector to be applied to the assembly. |
| `position` | `Vector3` |  | The position, in world space, to apply the impulse. |

**Returns:** `()`

### Method: BasePart:BindToCollisionSummaries

**Signature:** `BasePart:BindToCollisionSummaries(callback: Function): RBXScriptConnection`

Subscribes `callback` to the contact data that the physics engine
generates for this part while detecting collisions. Once per frame, after
the simulation has stepped, `callback` receives an array of summaries
describing every contact patch this part was involved in during that
frame. Each summary reports where the contact occurred, which direction it
faced, and how fast the two parts were moving relative to each other at
that point.

This method is a separate mechanism from [BasePart.Touched](/docs/reference/engine/classes/BasePart.md).

Throws an error if `callback` is `nil`, or if the part is not a descendant
of [Workspace](/docs/reference/engine/classes/Workspace.md).

#### Summary Fields

Each entry in the array passed to `callback` is a table with the following
keys:

| Key | Type | Summary |
| --- | --- | --- |
| `Time` | `number` | Simulation time, in seconds, of the physics substep that produced this summary. |
| `Part0` | [BasePart](/docs/reference/engine/classes/BasePart.md) | The subscribed part. |
| `Part1` | [BasePart](/docs/reference/engine/classes/BasePart.md) | The other part in the pair, which may be [Terrain](/docs/reference/engine/classes/Terrain.md). |
| `Point` | [Vector3](/docs/reference/engine/datatypes/Vector3.md) | Contact point in world space, averaged across the points in the patch. |
| `Normal` | [Vector3](/docs/reference/engine/datatypes/Vector3.md) | Unit contact normal for the patch, oriented relative to the subscribed part. |
| `RelativeVelocity` | [Vector3](/docs/reference/engine/datatypes/Vector3.md) | Velocity of `Part1` relative to `Part0` at the contact point. |
| `Area` | `number` | Estimated area of the contact patch, in square studs. `0` for a patch of fewer than three points, such as an edge or corner contact. |

`Normal` is oriented relative to the subscribed part rather than to
whichever part the engine happened to list first, so if both parts of a
pair are subscribed, each subscription receives its own summary with
itself as `Part0` and the normal flipped to match.

`RelativeVelocity` is the velocity of `Part1` relative to `Part0`, so the
magnitude of its projection onto `Normal` is the speed at which the two
parts are approaching or separating head-on, and the component tangential
to `Normal` describes sliding and glancing contact.

#### Reporting Behavior

- Contact recording is enabled only while at least one subscription exists
  anywhere in the [Workspace](/docs/reference/engine/classes/Workspace.md), and the cost of it scales with the
  number of subscribed parts rather than with the total number of
  collisions in the scene.
- Contacts between multiple sleeping parts do not produce summaries.
- Contacts from Parts with [BasePart.CanCollide](/docs/reference/engine/classes/BasePart.md) set to `false` do
  not produce summaries.
- Physics may run several substeps per frame, so a pair that stays in
  contact across several of them produces up to one summary per patch per
  substep, all delivered in the same invocation of `callback`. Use `Time`
  to order them.
- Non-convex collision geometry produces one summary per pair of touching
  convex hulls, and contact with [Terrain](/docs/reference/engine/classes/Terrain.md) is split further by
  contact normal, so either can yield several summaries for the same pair
  within one substep.
- Nothing is replicated. Each client generates summaries for the
  collisions it owns. See
  [network ownership](/docs/en-us/physics/network-ownership.md).
- Destroying the part disconnects its subscriptions.

*Security: None · Thread Safety: Unsafe · Capabilities: Basic*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `callback` | `Function` |  | Invoked with an array of summary tables, at most once per frame, if the part was involved in a collision. |

**Returns:** `RBXScriptConnection` — A [RBXScriptConnection](/docs/reference/engine/datatypes/RBXScriptConnection.md) that ends the subscription when
disconnected.

### Method: BasePart:CanCollideWith

**Signature:** `BasePart:CanCollideWith(part: BasePart): boolean`

Returns whether the parts can collide with each other or not. This
function takes into account the collision groups of the two parts. This
function will error if the specified part is not a BasePart.

*Security: None · Thread Safety: Safe · Simulation Access: true*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `part` | `BasePart` |  | The specified part being checked for collidability. |

**Returns:** `boolean` — Whether the parts can collide with each other.

### Method: BasePart:CanSetNetworkOwnership

**Signature:** `BasePart:CanSetNetworkOwnership(): Tuple`

The CanSetNetworkOwnership function checks whether you can set a part's
network ownership.

The function's return value verifies whether or not you can call
[BasePart:SetNetworkOwner()](/docs/reference/engine/classes/BasePart.md) or
[BasePart:SetNetworkOwnershipAuto()](/docs/reference/engine/classes/BasePart.md) without encountering an error.
It returns true if you can modify/read the network ownership, or returns
false and the reason you can't, as a string.

*Security: None · Thread Safety: Unsafe · Simulation Access: true*

**Returns:** `Tuple` — Whether you can modify or read the network ownership and the reason.

**Check if a Part's Network Ownership Can Be Set**

This example checks whether or not the network ownership of the first
`BasePart` named _Part_ in the `Workspace` can be set.

```lua
local part = workspace:FindFirstChild("Part")

if part and part:IsA("BasePart") then
	local canSet, errorReason = part:CanSetNetworkOwnership()
	if canSet then
		print(part:GetFullName() .. "'s Network Ownership can be changed!")
	else
		warn("Cannot change the Network Ownership of " .. part:GetFullName() .. " because: " .. errorReason)
	end
end
```

### Method: BasePart:GetClosestPointOnSurface

**Signature:** `BasePart:GetClosestPointOnSurface(position: Vector3): Vector3`

Returns the closest point on the part's surface to the given world-space
position. If the provided position is inside the part, it is returned
as-is.

For [MeshPart](/docs/reference/engine/classes/MeshPart.md) and [PartOperation](/docs/reference/engine/classes/PartOperation.md) instances, this method
respects the part's [CollisionFidelity](/docs/reference/engine/enums/CollisionFidelity.md) value. Return values can
differ based on whether the mesh is being treated as a box, a hull, or a
more complex shape.

*Security: None · Thread Safety: Unsafe · Simulation Access: true*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `position` | `Vector3` |  | The world-space point to find the closest surface point to. |

**Returns:** `Vector3` — The closest point on the part's surface in world space.

### Method: BasePart:GetConnectedParts

**Signature:** `BasePart:GetConnectedParts(recursive?: boolean): List<BasePart>`

Returns a table of parts connected to the object by any kind of rigid
joint.

If `recursive` is true this function will return all of the parts in the
assembly rigidly connected to the BasePart.

#### Rigid Joints

When a joint connects two parts together `(Part0 → Part1)`, a joint is
**rigid** if the physics of `Part1` are completely locked down by `Part0`.
This only applies to the following joint types:

- [Weld](/docs/reference/engine/classes/Weld.md)
- [Snap](/docs/reference/engine/classes/Snap.md)
- [ManualWeld](/docs/reference/engine/classes/ManualWeld.md)
- [Motor](/docs/reference/engine/classes/Motor.md)
- [Motor6D](/docs/reference/engine/classes/Motor6D.md)
- [WeldConstraint](/docs/reference/engine/classes/WeldConstraint.md)

*Security: None · Thread Safety: Safe*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `recursive` | `boolean` | `false` | A table of parts connected to the object by any kind of [joint](/docs/reference/engine/classes/JointInstance.md). |

**Returns:** `List<BasePart>` — An array of [BaseParts](/docs/reference/engine/classes/BasePart.md) connected to this part by rigid
joints. If `recursive` is true, includes all parts in the assembly.

### Method: BasePart:GetJoints

**Signature:** `BasePart:GetJoints(): Instances`

Returns an array of all [Joints](/docs/reference/engine/classes/JointInstance.md) and
[Constraints](/docs/reference/engine/classes/Constraint.md) connected to this part that are active in
the simulation.

A joint or constraint only becomes active once both of the parts it
connects are inside the **same** simulated container, such as
[Workspace](/docs/reference/engine/classes/Workspace.md) or a [WorldModel](/docs/reference/engine/classes/WorldModel.md). If one of the connected parts
is outside that container — for example, parented to
[ServerStorage](/docs/reference/engine/classes/ServerStorage.md), or in a different [WorldModel](/docs/reference/engine/classes/WorldModel.md) — the joint is
not activated. **GetJoints()** does not include that joint on either part,
even though the joint instance still exists in the data model.

*Security: None · Thread Safety: Safe · Simulation Access: true*

**Returns:** `Instances` — An array of all [Joints](/docs/reference/engine/classes/JointInstance.md) and
[Constraints](/docs/reference/engine/classes/Constraint.md) connected to the part that are active
in the simulation.

### Method: BasePart:GetMass

**Signature:** `BasePart:GetMass(): float`

**GetMass** returns the value of the read-only [Mass](/docs/reference/engine/classes/BasePart.md)
property.

This function predates the Mass property. It remains supported for
backward-compatibility; you should use the Mass property directly.

*Security: None · Thread Safety: Safe · Simulation Access: true*

**Returns:** `float` — The part's mass.

**Finding a Part's Mass**

This example creates a new part, myPart, in the game's Workspace, with
dimensions 4x6x4 studs. The part is also anchored.

Then, myMass is set to equal the mass of the new part. The mass of the part is
printed at the end of the print statement:

> My part's mass is ...

```lua
local myPart = Instance.new("Part")
myPart.Size = Vector3.new(4, 6, 4)
myPart.Anchored = true
myPart.Parent = workspace

local myMass = myPart:GetMass()

print("My part's mass is " .. myMass)
```

### Method: BasePart:GetNetworkOwner

**Signature:** `BasePart:GetNetworkOwner(): Instance`

Returns the current player who is the network owner of this part, or `nil`
in case of the server.

*Security: None · Thread Safety: Safe · Simulation Access: true*

**Returns:** `Instance` — The current player who is the network owner of this part, or `nil` in
case of the server.

### Method: BasePart:GetNetworkOwnershipAuto

**Signature:** `BasePart:GetNetworkOwnershipAuto(): boolean`

Returns true if the game engine automatically decides the network owner
for this part.

*Security: None · Thread Safety: Safe · Simulation Access: true*

**Returns:** `boolean` — Whether the game engine automatically decides the network owner for
this part.

### Method: BasePart:GetNoCollisionConstraints

**Signature:** `BasePart:GetNoCollisionConstraints(): Instances`

Returns the enabled [NoCollisionConstraint](/docs/reference/engine/classes/NoCollisionConstraint.md) objects currently
registered for this part in its physics world. A
[NoCollisionConstraint](/docs/reference/engine/classes/NoCollisionConstraint.md) disables collisions between the two specific
parts it references, while each of those parts may still collide with the
rest of the world.

The returned array is empty if no such constraint is currently registered
for this part. The order of the returned constraints is not guaranteed.

*Security: None · Thread Safety: Unsafe · Simulation Access: true*

**Returns:** `Instances` — An array of the enabled [NoCollisionConstraint](/docs/reference/engine/classes/NoCollisionConstraint.md) objects
currently registered for this part in its physics world.

### Method: BasePart:GetTouchingParts

**Signature:** `BasePart:GetTouchingParts(): Instances`

Returns a table of all parts that are physically interacting with this
part. If the part itself has CanCollide set to false, then this function
returns an empty table unless the part has a
[TouchInterest](/docs/reference/engine/classes/TouchTransmitter.md) object parented to it (meaning
something is connected to its Touched event). Parts that are adjacent but
not intersecting are not considered touching. This function predates the
[WorldRoot:GetPartsInPart()](/docs/reference/engine/classes/WorldRoot.md) function, which provides more
flexibility and avoids the special [TouchInterest](/docs/reference/engine/classes/TouchTransmitter.md)
rules described above. Use [WorldRoot:GetPartsInPart()](/docs/reference/engine/classes/WorldRoot.md) instead.

*Security: None · Thread Safety: Unsafe · Simulation Access: true*

**Returns:** `Instances` — A table of all parts that intersect and can collide with this part.

### Method: BasePart:GetVelocityAtPosition

**Signature:** `BasePart:GetVelocityAtPosition(position: Vector3): Vector3`

Returns the linear velocity of the part's assembly at the given position
relative to this part. It can be used to identify the linear velocity of
parts in an assembly other than the root part. If the assembly has no
angular velocity, than the linear velocity will always be the same for
every position.

*Security: None · Thread Safety: Safe · Simulation Access: true*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `position` | `Vector3` |  | The world-space position at which to compute the assembly's linear velocity. |

**Returns:** `Vector3` — A [Vector3](/docs/reference/engine/datatypes/Vector3.md) representing the linear velocity of the assembly
at the specified world-space position.

### Method: BasePart:IntersectAsync

**Signature:** `BasePart:IntersectAsync(parts: Instances, collisionfidelity?: CollisionFidelity, renderFidelity?: RenderFidelity): Instance`

Creates a new [IntersectOperation](/docs/reference/engine/classes/IntersectOperation.md) from the intersecting geometry of
the part and the other parts in the given array. Only [Parts](/docs/reference/engine/classes/Part.md)
are supported, not [Terrain](/docs/reference/engine/classes/Terrain.md) or [MeshParts](/docs/reference/engine/classes/MeshPart.md). Similar
to [Clone()](/docs/reference/engine/classes/Instance.md), the returned object has no set
[Parent](/docs/reference/engine/classes/Instance.md).

The following properties from the calling part are applied to the
resulting [IntersectOperation](/docs/reference/engine/classes/IntersectOperation.md):

- [Color](/docs/reference/engine/classes/BasePart.md), [Material](/docs/reference/engine/classes/BasePart.md),
  [MaterialVariant](/docs/reference/engine/classes/BasePart.md),
  [Reflectance](/docs/reference/engine/classes/BasePart.md),
  [Transparency](/docs/reference/engine/classes/BasePart.md)
- [CanCollide](/docs/reference/engine/classes/BasePart.md)
- [Anchored](/docs/reference/engine/classes/BasePart.md), [Density](/docs/reference/engine/classes/BasePart.md),
  [Elasticity](/docs/reference/engine/classes/BasePart.md),
  [ElasticityWeight](/docs/reference/engine/classes/BasePart.md),
  [Friction](/docs/reference/engine/classes/BasePart.md),
  [FrictionWeight](/docs/reference/engine/classes/BasePart.md)

#### Migration

It is highly recommended to use the newer
[GeometryService:IntersectAsync()](/docs/reference/engine/classes/GeometryService.md) instead of this method. As well
as having better performance and more features, the new method differs as
follows:

- The output is an array of instances rather than a single instance.
- The input parts do not need to be parented to the scene, allowing for
  background operations.
- When the `SplitApart` option is set to `true` (default), each distinct
  body will be returned in its own [PartOperation](/docs/reference/engine/classes/PartOperation.md).
- All the returned parts are in the coordinate space of the main part, so
  their [PVInstance.Origin](/docs/reference/engine/classes/PVInstance.md) positions are the same as the main
  part's. This keeps the vertices of the mesh in the same position
  relative to the object as before the operation, but it does also mean
  the `(0, 0, 0)` of a returned part is not necessarily at the center of
  its body.

#### Notes

- The original parts remain intact following a successful intersect
  operation. In most cases, you should [Destroy()](/docs/reference/engine/classes/Instance.md)
  all of the original parts and parent the returned
  [IntersectOperation](/docs/reference/engine/classes/IntersectOperation.md) to the same place as the calling
  [BasePart](/docs/reference/engine/classes/BasePart.md).
- By default, the face colors of the resulting intersection are borrowed
  from the [Color](/docs/reference/engine/classes/BasePart.md) property of the original parts. To
  change the entire intersection to a specific color, set its
  [UsePartColor](/docs/reference/engine/classes/PartOperation.md) property to `true`.
- If an intersect operation would result in a part with more than 20,000
  triangles, it will be simplified to 20,000 triangles.

*Yields · Security: None · Thread Safety: Unsafe · Capabilities: CSG*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `parts` | `Instances` |  | The objects taking part in the intersection. |
| `collisionfidelity` | `CollisionFidelity` | `Default` | The [CollisionFidelity](/docs/reference/engine/enums/CollisionFidelity.md) value for the resulting [IntersectOperation](/docs/reference/engine/classes/IntersectOperation.md). |
| `renderFidelity` | `RenderFidelity` | `Automatic` | The [RenderFidelity](/docs/reference/engine/enums/RenderFidelity.md) value of the resulting [PartOperation](/docs/reference/engine/classes/PartOperation.md). |

**Returns:** `Instance` — Resulting [IntersectOperation](/docs/reference/engine/classes/IntersectOperation.md) with default name **Intersect**.

### Method: BasePart:IsGrounded

**Signature:** `BasePart:IsGrounded(): boolean`

Returns true if the object is connected to a part that will hold it in
place (eg an [Anchored](/docs/reference/engine/classes/BasePart.md) part), otherwise returns
false. In an assembly that has an [Anchored](/docs/reference/engine/classes/BasePart.md) part,
every other part is grounded.

*Security: None · Thread Safety: Safe · Simulation Access: true*

**Returns:** `boolean` — Whether the object is connected to a part that will hold it in place.

### Method: BasePart:Resize

**Signature:** `BasePart:Resize(normalId: NormalId, deltaAmount: int): boolean`

Changes the size of an object just like using the Studio resize tool.

*Security: None · Thread Safety: Unsafe · Simulation Access: true*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `normalId` | `NormalId` |  | The side to resize. |
| `deltaAmount` | `int` |  | How much to grow/shrink on the specified side. |

**Returns:** `boolean` — Whether the part is resized.

### Method: BasePart:SetNetworkOwner

**Signature:** `BasePart:SetNetworkOwner(playerInstance?: Player): ()`

Sets the given player as network owner for this and all connected parts.
When playerInstance is `nil`, the server will be the owner instead of a
player.

*Security: None · Thread Safety: Unsafe · Simulation Access: true*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `playerInstance` | `Player` | `nil` | The player being given network ownership of the part. |

**Returns:** `()`

### Method: BasePart:SetNetworkOwnershipAuto

**Signature:** `BasePart:SetNetworkOwnershipAuto(): ()`

Lets the game engine dynamically decide who will handle the part's physics
(one of the clients or the server).

*Security: None · Thread Safety: Unsafe · Simulation Access: true*

**Returns:** `()`

### Method: BasePart:SubtractAsync

**Signature:** `BasePart:SubtractAsync(parts: Instances, collisionfidelity?: CollisionFidelity, renderFidelity?: RenderFidelity): Instance`

Creates a new [UnionOperation](/docs/reference/engine/classes/UnionOperation.md) from the part, minus the geometry
occupied by the parts in the given array. Only [Parts](/docs/reference/engine/classes/Part.md) are
supported, not [Terrain](/docs/reference/engine/classes/Terrain.md) or [MeshParts](/docs/reference/engine/classes/MeshPart.md). Similar to
[Clone()](/docs/reference/engine/classes/Instance.md), the returned object has no set
[Parent](/docs/reference/engine/classes/Instance.md).

Note that the resulting union cannot be empty due to subtractions. If the
operation would result in completely empty geometry, it will fail.

#### Migration

It is highly recommended to use the newer
[GeometryService:SubtractAsync()](/docs/reference/engine/classes/GeometryService.md) instead of this method. As well as
having better performance and more features, the new method differs as
follows:

- The output is an array of instances rather than a single instance.
- The input parts do not need to be parented to the scene, allowing for
  background operations.
- When the `SplitApart` option is set to `true` (default), each distinct
  body will be returned in its own [PartOperation](/docs/reference/engine/classes/PartOperation.md).
- All the returned parts are in the coordinate space of the main part, so
  their [PVInstance.Origin](/docs/reference/engine/classes/PVInstance.md) positions are the same as the main
  part's. This keeps the vertices of the mesh in the same position
  relative to the object as before the operation, but it does also mean
  the `(0, 0, 0)` of a returned part is not necessarily at the center of
  its body.

*Yields · Security: None · Thread Safety: Unsafe · Capabilities: CSG*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `parts` | `Instances` |  | The objects taking part in the subtraction. |
| `collisionfidelity` | `CollisionFidelity` | `Default` | The [CollisionFidelity](/docs/reference/engine/enums/CollisionFidelity.md) value for the resulting [UnionOperation](/docs/reference/engine/classes/UnionOperation.md). |
| `renderFidelity` | `RenderFidelity` | `Automatic` | The [RenderFidelity](/docs/reference/engine/enums/RenderFidelity.md) value of the resulting [PartOperation](/docs/reference/engine/classes/PartOperation.md). |

**Returns:** `Instance` — Resulting [UnionOperation](/docs/reference/engine/classes/UnionOperation.md) with default name **Union**.

### Method: BasePart:TorqueToAngularAcceleration

**Signature:** `BasePart:TorqueToAngularAcceleration(torque: Vector3, angVelocity?: Vector3): Vector3`

Returns the world-space angular acceleration that would result from
applying the specified torque to the part's assembly, optionally taking
into account gyroscopic effects.

This is the inverse of [BasePart:AngularAccelerationToTorque()](/docs/reference/engine/classes/BasePart.md). It
is useful for predicting how an assembly will respond to an applied
torque.

The calculation uses:

**α = I⁻¹ · (τ − ω × (I · ω))**

where **I** is the assembly's world-space inertia tensor, **τ** is the
applied torque, and **ω** is the angular velocity.

If the part is not a descendant of [Workspace](/docs/reference/engine/classes/Workspace.md), returns `(0, 0, 0)`.
If the assembly is anchored, returns `(0, 0, 0)`.

#### Gyroscopic Effects

When a spinning assembly has an asymmetric inertia tensor, the
acceleration resulting from an applied torque also depends on the current
angular velocity. The `angVelocity` parameter accounts for these
gyroscopic effects. If omitted (defaults to zero), the result neglects
this contribution from the result.

*Security: None · Thread Safety: Unsafe · Simulation Access: true*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `torque` | `Vector3` |  | The torque vector applied to the assembly in world space. |
| `angVelocity` | `Vector3` | `0, 0, 0` | The current angular velocity of the assembly in world space. Defaults to `(0, 0, 0)`. Supply the assembly's angular velocity to account for gyroscopic effects. |

**Returns:** `Vector3` — A [Vector3](/docs/reference/engine/datatypes/Vector3.md) representing the resulting angular acceleration
in world space.

**Torque To Angular Acceleration**

Demonstrates [BasePart:TorqueToAngularAcceleration()](/docs/reference/engine/classes/BasePart.md).

```lua
local part = Instance.new("Part")
part.Parent = workspace

local angularVelocity = part.AssemblyAngularVelocity
local appliedTorque = Vector3.new(0, 100, 0)

-- Predict the angular acceleration from this torque
local angAccel = part:TorqueToAngularAcceleration(appliedTorque, angularVelocity)
```

### Method: BasePart:UnionAsync

**Signature:** `BasePart:UnionAsync(parts: Instances, collisionfidelity?: CollisionFidelity, renderFidelity?: RenderFidelity): Instance`

Creates a new [UnionOperation](/docs/reference/engine/classes/UnionOperation.md) from the part, plus the geometry
occupied by the parts in the given array. Only [Parts](/docs/reference/engine/classes/Part.md) are
supported, not [Terrain](/docs/reference/engine/classes/Terrain.md) or [MeshParts](/docs/reference/engine/classes/MeshPart.md). Similar to
[Clone()](/docs/reference/engine/classes/Instance.md), the returned object has no set
[Parent](/docs/reference/engine/classes/Instance.md).

The following properties from the calling part are applied to the
resulting [UnionOperation](/docs/reference/engine/classes/UnionOperation.md):

- [Color](/docs/reference/engine/classes/BasePart.md), [Material](/docs/reference/engine/classes/BasePart.md),
  [MaterialVariant](/docs/reference/engine/classes/BasePart.md),
  [Reflectance](/docs/reference/engine/classes/BasePart.md),
  [Transparency](/docs/reference/engine/classes/BasePart.md)
- [CanCollide](/docs/reference/engine/classes/BasePart.md)
- [Anchored](/docs/reference/engine/classes/BasePart.md), [Density](/docs/reference/engine/classes/BasePart.md),
  [Elasticity](/docs/reference/engine/classes/BasePart.md),
  [ElasticityWeight](/docs/reference/engine/classes/BasePart.md),
  [Friction](/docs/reference/engine/classes/BasePart.md),
  [FrictionWeight](/docs/reference/engine/classes/BasePart.md)

#### Migration

It is highly recommended to use the newer
[GeometryService:UnionAsync()](/docs/reference/engine/classes/GeometryService.md) instead of this method. As well as
having better performance and more features, the new method differs as
follows:

- The output is an array of instances rather than a single instance.
- The input parts do not need to be parented to the scene, allowing for
  background operations.
- When the `SplitApart` option is set to `true` (default), each distinct
  body will be returned in its own [PartOperation](/docs/reference/engine/classes/PartOperation.md).
- All the returned parts are in the coordinate space of the main part, so
  their [PVInstance.Origin](/docs/reference/engine/classes/PVInstance.md) positions are the same as the main
  part's. This keeps the vertices of the mesh in the same position
  relative to the object as before the operation, but it does also mean
  the `(0, 0, 0)` of a returned part is not necessarily at the center of
  its body.

#### Notes

- The original parts remain intact following a successful union operation.
  In most cases, you should [Destroy()](/docs/reference/engine/classes/Instance.md) all of the
  original parts and parent the returned [UnionOperation](/docs/reference/engine/classes/UnionOperation.md) to the
  same place as the calling [BasePart](/docs/reference/engine/classes/BasePart.md).
- By default, the resulting union respects the
  [Color](/docs/reference/engine/classes/BasePart.md) property of each of its parts. To change
  the entire union to a specific color, set its
  [UsePartColor](/docs/reference/engine/classes/PartOperation.md) property to `true`.
- If a union operation would result in a part with more than 20,000
  triangles, it will be simplified to 20,000 triangles.

*Yields · Security: None · Thread Safety: Unsafe · Capabilities: CSG*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `parts` | `Instances` |  | The objects taking part in the union with the calling part. |
| `collisionfidelity` | `CollisionFidelity` | `Default` | The [CollisionFidelity](/docs/reference/engine/enums/CollisionFidelity.md) value for the resulting [UnionOperation](/docs/reference/engine/classes/UnionOperation.md). |
| `renderFidelity` | `RenderFidelity` | `Automatic` | The [RenderFidelity](/docs/reference/engine/enums/RenderFidelity.md) value of the resulting [PartOperation](/docs/reference/engine/classes/PartOperation.md). |

**Returns:** `Instance` — Resulting [UnionOperation](/docs/reference/engine/classes/UnionOperation.md) with default name **Union**.

### Method: BasePart:BreakJoints

**Signature:** `BasePart:BreakJoints(): ()`

> **Deprecated:** This method is deprecated. To break specific joints, iterate over the part's connections using [BasePart:GetJoints()](/docs/reference/engine/classes/BasePart.md) and call [Instance:Destroy()](/docs/reference/engine/classes/Instance.md) on the joints you want to remove.

Breaks any surface connection with any adjacent part, including
[Weld](/docs/reference/engine/classes/Weld.md) and other [JointInstance](/docs/reference/engine/classes/JointInstance.md).

*Security: None · Thread Safety: Unsafe · Simulation Access: true*

**Returns:** `()`

### Method: BasePart:breakJoints

**Signature:** `BasePart:breakJoints(): ()`

> **Deprecated:** This deprecated function is a variant of [BasePart:BreakJoints()](/docs/reference/engine/classes/BasePart.md) which should be used instead.

*Security: None · Thread Safety: Unsafe*

**Returns:** `()`

### Method: BasePart:getMass

**Signature:** `BasePart:getMass(): float`

> **Deprecated:** This Camel Case property has been deprecated in favor of its Pascal Case variant, [BasePart:GetMass()](/docs/reference/engine/classes/BasePart.md).

*Security: None · Thread Safety: Unsafe*

**Returns:** `float`

### Method: BasePart:GetRenderCFrame

**Signature:** `BasePart:GetRenderCFrame(): CFrame`

> **Deprecated:** This item is been deprecated since interpolation is now applied to the [CFrame](/docs/reference/engine/datatypes/CFrame.md) directly. Do not use it for new work.

This function used to be relevant when Roblox's lag-compensating
interpolation of parts online was internal. The interpolation is now
applied to the [CFrame](/docs/reference/engine/datatypes/CFrame.md) directly.

*Security: None · Thread Safety: Unsafe*

**Returns:** `CFrame` — The [CFrame](/docs/reference/engine/datatypes/CFrame.md) representing where the part is being rendered,
which is now equivalent to the part's [CFrame](/docs/reference/engine/classes/BasePart.md).

### Method: BasePart:GetRootPart

**Signature:** `BasePart:GetRootPart(): Instance`

Returns the base part of an assembly. When moving an assembly of parts
using a [CFrame](/docs/reference/engine/datatypes/CFrame.md). it is important to move this base part (this
will move all other parts connected to it accordingly). More information
is available in the [Assemblies](/docs/en-us/physics/assemblies.md) article.

This function predates the
[AssemblyRootPart](/docs/reference/engine/classes/BasePart.md) property. It remains
supported for backwards compatibility, but you should use
[AssemblyRootPart](/docs/reference/engine/classes/BasePart.md) directly.

*Security: None · Thread Safety: Safe · Simulation Access: true*

**Returns:** `Instance` — The base part of an assembly (a collection of parts connected
together).

### Method: BasePart:MakeJoints

**Signature:** `BasePart:MakeJoints(): ()`

> **Deprecated:** SurfaceType based joining is deprecated, do not use MakeJoints for new projects. [WeldConstraints](/docs/reference/engine/classes/WeldConstraint.md) and [HingeConstraints](/docs/reference/engine/classes/HingeConstraint.md) should be used instead.

Creates a joint on any side of the [Part](/docs/reference/engine/classes/BasePart.md) that has a
[SurfaceType](/docs/reference/engine/enums/SurfaceType.md) that can make a joint it will create a joint with any
adjacent parts.

Joints will be created between the sides and any planar touching surfaces,
depending on the sides' surfaces.

- Smooth surfaces will not create joints
- Glue surfaces will create a [Glue](/docs/reference/engine/classes/Glue.md) joint
- Weld will create a [Weld](/docs/reference/engine/classes/Weld.md) joint with any surface except for
  Unjoinable
- Studs, Inlet, or Universal will each create a [Snap](/docs/reference/engine/classes/Snap.md) joint with
  either of other the other two surfaces (e.g. Studs with Inlet and
  Universal)
- Hinge and Motor surfaces create [Rotate](/docs/reference/engine/classes/Rotate.md) and [RotateV](/docs/reference/engine/classes/RotateV.md) joint
  instances

Unlike [Model:MakeJoints()](/docs/reference/engine/classes/Model.md), this function requires an array of
parts as a parameter. This array is given as follows:

```
part:MakeJoints({part1, part2, part3})
```

Joints are broken if enough force is applied to them due to an
[Explosion](/docs/reference/engine/classes/Explosion.md), unless a [ForceField](/docs/reference/engine/classes/ForceField.md) object is parented to the
[BasePart](/docs/reference/engine/classes/BasePart.md) or ancestor [Model](/docs/reference/engine/classes/Model.md). For this reason, they are
often used to make simple destructible buildings and other models.

*Security: None · Thread Safety: Unsafe*

**Returns:** `()`

### Method: BasePart:makeJoints

**Signature:** `BasePart:makeJoints(): ()`

> **Deprecated:** This deprecated function is a variant of [BasePart:MakeJoints()](/docs/reference/engine/classes/BasePart.md) which should be used instead.

*Security: None · Thread Safety: Unsafe*

**Returns:** `()`

### Method: BasePart:resize

**Signature:** `BasePart:resize(normalId: NormalId, deltaAmount: int): boolean`

> **Deprecated:** This deprecated function is a variant of [BasePart:Resize()](/docs/reference/engine/classes/BasePart.md) which should be used instead.

*Security: None · Thread Safety: Unsafe*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `normalId` | `NormalId` |  |  |
| `deltaAmount` | `int` |  |  |

**Returns:** `boolean`

## Events

### Event: BasePart.Touched

**Signature:** `BasePart.Touched(otherPart: BasePart)`

The **Touched** event fires when a part comes in contact with another
part. For instance, if **PartA** bumps into **PartB**, then
[PartA.Touched](/docs/reference/engine/classes/BasePart.md) fires with **PartB**, and
[PartB.Touched](/docs/reference/engine/classes/BasePart.md) fires with **PartA**.

This event only fires as a result of physical movement, so it will not
fire if the [CFrame](/docs/reference/engine/classes/BasePart.md) property was changed such that
the part overlaps another part. This also means that at least one of the
parts involved must **not** be [Anchored](/docs/reference/engine/classes/BasePart.md) at the
time of the collision.

This event works in conjunction with
[Workspace.TouchesUseCollisionGroups](/docs/reference/engine/classes/Workspace.md) to specify whether
[collision groups](/docs/en-us/workspace/collisions.md#collision-filtering)
are acknowledged for detection.

*Security: None*

**Parameters:**

| Name | Type | Description |
|------|------|-------------|
| `otherPart` | `BasePart` | The other part that came in contact with the given part. |

**Touching Parts Count**

This code sample creates a BillboardGui on a part that displays the number of
parts presently touching it.

```lua
local part = script.Parent

local billboardGui = Instance.new("BillboardGui")
billboardGui.Size = UDim2.new(0, 200, 0, 50)
billboardGui.Adornee = part
billboardGui.AlwaysOnTop = true
billboardGui.Parent = part

local tl = Instance.new("TextLabel")
tl.Size = UDim2.new(1, 0, 1, 0)
tl.BackgroundTransparency = 1
tl.Parent = billboardGui

local numTouchingParts = 0

local function onTouch(otherPart)
	print("Touch started: " .. otherPart.Name)
	numTouchingParts = numTouchingParts + 1
	tl.Text = numTouchingParts
end

local function onTouchEnded(otherPart)
	print("Touch ended: " .. otherPart.Name)
	numTouchingParts = numTouchingParts - 1
	tl.Text = numTouchingParts
end

part.Touched:Connect(onTouch)
part.TouchEnded:Connect(onTouchEnded)
```

**Model Touched**

This code sample demonstrates how to connect the [BasePart.Touched](/docs/reference/engine/classes/BasePart.md)
event of multiple parts in a [Model](/docs/reference/engine/classes/Model.md) to one function.

```lua
local model = script.Parent

local function onTouched(otherPart)
	-- Ignore instances of the model coming in contact with itself
	if otherPart:IsDescendantOf(model) then
		return
	end

	print(model.Name .. " collided with " .. otherPart.Name)
end

for _, child in pairs(model:GetChildren()) do
	if child:IsA("BasePart") then
		child.Touched:Connect(onTouched)
	end
end
```

### Event: BasePart.TouchEnded

**Signature:** `BasePart.TouchEnded(otherPart: BasePart)`

Fires when a part stops touching another part under similar conditions to
those of [BasePart.Touched](/docs/reference/engine/classes/BasePart.md).

This event works in conjunction with
[Workspace.TouchesUseCollisionGroups](/docs/reference/engine/classes/Workspace.md) to specify whether
[collision groups](/docs/en-us/workspace/collisions.md#collision-filtering)
are acknowledged for detection.

*Security: None*

**Parameters:**

| Name | Type | Description |
|------|------|-------------|
| `otherPart` | `BasePart` | The other part that stopped touching this part. |

**Touching Parts Count**

This code sample creates a BillboardGui on a part that displays the number of
parts presently touching it.

```lua
local part = script.Parent

local billboardGui = Instance.new("BillboardGui")
billboardGui.Size = UDim2.new(0, 200, 0, 50)
billboardGui.Adornee = part
billboardGui.AlwaysOnTop = true
billboardGui.Parent = part

local tl = Instance.new("TextLabel")
tl.Size = UDim2.new(1, 0, 1, 0)
tl.BackgroundTransparency = 1
tl.Parent = billboardGui

local numTouchingParts = 0

local function onTouch(otherPart)
	print("Touch started: " .. otherPart.Name)
	numTouchingParts = numTouchingParts + 1
	tl.Text = numTouchingParts
end

local function onTouchEnded(otherPart)
	print("Touch ended: " .. otherPart.Name)
	numTouchingParts = numTouchingParts - 1
	tl.Text = numTouchingParts
end

part.Touched:Connect(onTouch)
part.TouchEnded:Connect(onTouchEnded)
```

### Event: BasePart.LocalSimulationTouched

**Signature:** `BasePart.LocalSimulationTouched(part: BasePart)`

> **Deprecated:** This event is deprecated in favor of [BasePart.Touched](/docs/reference/engine/classes/BasePart.md).

Fired when another part comes in contact with another object. This event
only sends data to the client notifying it that two parts have collided,
whereas [BasePart.Touched](/docs/reference/engine/classes/BasePart.md) sends data to the server.

*Security: None*

**Parameters:**

| Name | Type | Description |
|------|------|-------------|
| `part` | `BasePart` | The other part that came in contact with this part. |

**BasePart.LocalSimulationTouched**

```lua
workspace.Part.LocalSimulationTouched:Connect(function(part)
	print(part.Name)
end)
```

### Event: BasePart.OutfitChanged

**Signature:** `BasePart.OutfitChanged()`

> **Deprecated:** This event is deprecated. Do not use it for new work.

Fired if the part's appearance is affected by the [Shirt](/docs/reference/engine/classes/Shirt.md) class.

*Security: None*

### Event: BasePart.StoppedTouching

**Signature:** `BasePart.StoppedTouching(otherPart: BasePart)`

> **Deprecated:** This event is deprecated in favor of [BasePart.TouchEnded](/docs/reference/engine/classes/BasePart.md), which should be used instead.

Deprecated. Fires on the local client when a part stops touching another
part, under conditions similar to those of [BasePart.TouchEnded](/docs/reference/engine/classes/BasePart.md).
This event is the client-only counterpart to [BasePart.TouchEnded](/docs/reference/engine/classes/BasePart.md):
it only notifies the local client that the two parts have separated,
whereas [BasePart.TouchEnded](/docs/reference/engine/classes/BasePart.md) also sends data to the server. Use
[BasePart.TouchEnded](/docs/reference/engine/classes/BasePart.md) instead.

*Security: None*

**Parameters:**

| Name | Type | Description |
|------|------|-------------|
| `otherPart` | `BasePart` | The other part that stopped touching the given part. |

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