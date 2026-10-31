---
name: Explosion
last_updated: 2026-10-30T19:55:52Z
inherits:
  - Instance
  - Object
type: class
memory_category: Instances
summary: "Applies force to BaseParts within the explosion's Explosion.BlastRadius. Breaks JointInstances and WeldConstraints between parts and kills Humanoid characters not protected by a ForceField."
---

# Class: Explosion

> Applies force to [BaseParts](/docs/reference/engine/classes/BasePart.md) within the explosion's
> [Explosion.BlastRadius](/docs/reference/engine/classes/Explosion.md). Breaks [JointInstances](/docs/reference/engine/classes/JointInstance.md) and
> [WeldConstraints](/docs/reference/engine/classes/WeldConstraint.md) between parts and kills
> [Humanoid](/docs/reference/engine/classes/Humanoid.md) characters not protected by a [ForceField](/docs/reference/engine/classes/ForceField.md).

## Description

An Explosion applies force to [BaseParts](/docs/reference/engine/classes/BasePart.md) within the
explosion's [BlastRadius](/docs/reference/engine/classes/Explosion.md). This force breaks
[JointInstances](/docs/reference/engine/classes/JointInstance.md) and
[WeldConstraints](/docs/reference/engine/classes/WeldConstraint.md) between parts and kills
[Humanoid](/docs/reference/engine/classes/Humanoid.md) characters not protected by a [ForceField](/docs/reference/engine/classes/ForceField.md).
[Constraints](/docs/reference/engine/classes/Constraint.md) will not be broken by an explosion.

If an [Explosion](/docs/reference/engine/classes/Explosion.md) is parented anywhere in the data model while the
experience is running, it immediately sets off and, within a few seconds, it
becomes unparented. It is not destroyed with [Instance:Destroy()](/docs/reference/engine/classes/Instance.md) in
this case, so connections do not get disconnected and the parent is not
locked. As with all instances, keeping a strong reference an [Explosion](/docs/reference/engine/classes/Explosion.md)
will prevent it from being garbage collected.

Note that an [Explosion](/docs/reference/engine/classes/Explosion.md) must be a descendant of [Workspace](/docs/reference/engine/classes/Workspace.md) for
the explosion visuals to play and the physical/damaging effects to have an
impact.

#### Explosion Effects

[Humanoids](/docs/reference/engine/classes/Humanoid.md) are killed by explosions, as the explosion breaks
the character [Model](/docs/reference/engine/classes/Model.md) neck joint. Parenting a [ForceField](/docs/reference/engine/classes/ForceField.md) to a
model will protect all of its children from the explosion kill effect.

If you do not want joints between [BaseParts](/docs/reference/engine/classes/BasePart.md) to be broken, or
you want to implement your own formula for damaging
[Humanoids](/docs/reference/engine/classes/Humanoid.md), it's recommended that you set
[DestroyJointRadiusPercent](/docs/reference/engine/classes/Explosion.md) to 0 and
use the [Hit](/docs/reference/engine/classes/Explosion.md) event to handle the result of the explosion.

Explosions can also be configured to damage [Terrain](/docs/reference/engine/classes/Terrain.md), creating craters,
as configured through the [ExplosionType](/docs/reference/engine/classes/Explosion.md)
property.

Note that the effect of an explosion is **not** disrupted by obstacles,
meaning that parts/terrain shielded behind other parts/terrain will still be
affected.

## Code Samples

**Explosion Instantiation**

This code sample includes a brief snippet that creates a large explosion in
the game at 0, 10, 0.

```lua
local explosion = Instance.new("Explosion")
explosion.BlastRadius = 60
explosion.ExplosionType = Enum.ExplosionType.Craters -- damages terrain
explosion.Position = Vector3.new(0, 10, 0)
explosion.Parent = workspace
```

## Properties

### Property: Explosion.BlastPressure

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
  "category": "Data",
  "capabilities": [
    "AvatarBehavior"
  ]
}
```

Used to determine the amount of force applied to
[BaseParts](/docs/reference/engine/classes/BasePart.md) caught in the [Explosion.BlastRadius](/docs/reference/engine/classes/Explosion.md).

Currently this level of force applied does not vary based on distance from
[Explosion.Position](/docs/reference/engine/classes/Explosion.md). Unanchored `BaseParts` will accelerate equally
away from the origin regardless of distance provided they are within the
blast radius.

The blast pressure determines the acceleration of parts due to an
explosion. It does not determine the degree to which joints are broken.
When [Explosion.DestroyJointRadiusPercent](/docs/reference/engine/classes/Explosion.md) is equal to 1 all joints
between parts in the [Explosion.BlastRadius](/docs/reference/engine/classes/Explosion.md) will be destroyed
provided BlastPressure is greater than 0.

The BlastPressure also does not determine the amount of damage given to
[Terrain](/docs/reference/engine/classes/Terrain.md). Provided BlastPressure is greater than 0 and
[Explosion.ExplosionType](/docs/reference/engine/classes/Explosion.md) isn't set to Enum.ExplosionType.NoCraters
the size of the crater created is determined exclusively by the
[Explosion.BlastRadius](/docs/reference/engine/classes/Explosion.md).

Setting BlastPressure to 0 eliminates the effect of the explosion and is
useful when developers want to program their own custom behavior for
explosions using the [Explosion.Hit](/docs/reference/engine/classes/Explosion.md) event.

**Custom Explosion**

This sample contains a simple function that creates a custom explosion. The
custom explosion will not break joints as Explosion.DestroyJointRadiusPercent
is equal to 0. This means Humanoids will not be instantly killed as their neck
joints are broken. In this example explosion.BlastPressure is equal to zero so
as not to apply force or damage terrain but this can be changed.

The Explosion.Hit event is used to listen for contact. Once contact has been
made the code will look for the parent model of the BasePart hit by the
explosion. If that model exists, hasn't already been damaged and has a
Humanoid in it damage will be applied based on distance from the explosion's
origin.

```lua
local function customExplosion(position, radius, maxDamage)
	local explosion = Instance.new("Explosion")
	explosion.BlastPressure = 0 -- this could be set higher to still apply velocity to parts
	explosion.DestroyJointRadiusPercent = 0 -- joints are safe
	explosion.BlastRadius = radius
	explosion.Position = position

	-- set up a table to track the models hit
	local modelsHit = {}

	-- listen for contact
	explosion.Hit:Connect(function(part, distance)
		local parentModel = part.Parent
		if parentModel then
			-- check to see if this model has already been hit
			if modelsHit[parentModel] then
				return
			end
			-- log this model as hit
			modelsHit[parentModel] = true

			-- look for a humanoid
			local humanoid = parentModel:FindFirstChild("Humanoid")
			if humanoid then
				local distanceFactor = distance / explosion.BlastRadius -- get the distance as a value between 0 and 1
				distanceFactor = 1 - distanceFactor -- flip the amount, so that lower == closer == more damage
				humanoid:TakeDamage(maxDamage * distanceFactor) -- TakeDamage to respect ForceFields
			end
		end
	end)

	explosion.Parent = game.Workspace

	-- Roblox removes explosions after a few seconds, but does not destroy them.
	-- To ensure our .Hit connection gets disconnected, destroy the explosion once it's removed.
	explosion.AncestryChanged:Connect(function()
		if not explosion.Parent then
			explosion:Destroy()
		end
	end)
end

customExplosion(Vector3.new(0, 10, 0), 12, 50)
```

### Property: Explosion.BlastRadius

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
  "category": "Data",
  "capabilities": [
    "AvatarBehavior"
  ]
}
```

This property determines the radius of the [Explosion](/docs/reference/engine/classes/Explosion.md), in studs.
This property accepts any value between 0 and 100.

This radius determines the area of effect of the Explosion, not the size
of the Explosion's visuals. The size of the Explosion's visual effect is
the same regardless of BlastRadius (even if BlastRadius is 0).

[BaseParts](/docs/reference/engine/classes/BasePart.md) within the BlastRadius will be affected by the
explosion. Meaning, if [Explosion.BlastPressure](/docs/reference/engine/classes/Explosion.md) is greater than 0,
force will be applied to parts. The degree to which joints are broken
within the BlastRadius depends on
[Explosion.DestroyJointRadiusPercent](/docs/reference/engine/classes/Explosion.md). [Explosion.Hit](/docs/reference/engine/classes/Explosion.md) will
fire for any every [BasePart](/docs/reference/engine/classes/BasePart.md) within the radius.

[BaseParts](/docs/reference/engine/classes/BasePart.md) are considered within
[Explosion.BlastRadius](/docs/reference/engine/classes/Explosion.md) even if they are only partially in range.

**Explosion Instantiation**

This code sample includes a brief snippet that creates a large explosion in
the game at 0, 10, 0.

```lua
local explosion = Instance.new("Explosion")
explosion.BlastRadius = 60
explosion.ExplosionType = Enum.ExplosionType.Craters -- damages terrain
explosion.Position = Vector3.new(0, 10, 0)
explosion.Parent = workspace
```

### Property: Explosion.DestroyJointRadiusPercent

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
  "category": "Data",
  "capabilities": [
    "AvatarBehavior"
  ]
}
```

Used to set the proportion of the [Explosion.BlastRadius](/docs/reference/engine/classes/Explosion.md), between 0
and 1, within which all joints will be destroyed. Anything outside of this
range will only have the [Explosion](/docs/reference/engine/classes/Explosion.md) force applied to it.

For example, if [Explosion.BlastRadius](/docs/reference/engine/classes/Explosion.md) is set to 100 and
DestroyJointRadiusPercent is set to 0.5, any joints within a radius of 50
studs would be broken. Any joints between the ranges of 50 and 100 studs
wouldn't be destroyed, but the [Explosion](/docs/reference/engine/classes/Explosion.md) force would still be
applied to the [BaseParts](/docs/reference/engine/classes/BasePart.md).

This property allows developers to make [Explosions](/docs/reference/engine/classes/Explosion.md)
'non-lethal' to [Humanoids](/docs/reference/engine/classes/Humanoid.md) by setting
DestroyJointRadiusPercent to 0. This means the neck joint will not be
broken when characters come into contact with the [Explosion](/docs/reference/engine/classes/Explosion.md).

**Non lethal explosions**

This sample includes an example of how Explosions can be made non lethal to
player characters.

```lua
local function onDescendantAdded(instance)
	if instance:IsA("Explosion") then
		local explosion = instance
		explosion.DestroyJointRadiusPercent = 0

		local destroyJointRadiusPercent = 1
		explosion.Hit:Connect(function(part, distance)
			-- check the part is in range to break joints
			if distance <= destroyJointRadiusPercent * explosion.BlastRadius then
				-- make sure the part does not belong to a character
				if not game.Players:GetPlayerFromCharacter(part.Parent) then
					part:BreakJoints()
				end
			end
		end)
	end
end

workspace.DescendantAdded:Connect(onDescendantAdded)
```

**Custom Explosion**

This sample contains a simple function that creates a custom explosion. The
custom explosion will not break joints as Explosion.DestroyJointRadiusPercent
is equal to 0. This means Humanoids will not be instantly killed as their neck
joints are broken. In this example explosion.BlastPressure is equal to zero so
as not to apply force or damage terrain but this can be changed.

The Explosion.Hit event is used to listen for contact. Once contact has been
made the code will look for the parent model of the BasePart hit by the
explosion. If that model exists, hasn't already been damaged and has a
Humanoid in it damage will be applied based on distance from the explosion's
origin.

```lua
local function customExplosion(position, radius, maxDamage)
	local explosion = Instance.new("Explosion")
	explosion.BlastPressure = 0 -- this could be set higher to still apply velocity to parts
	explosion.DestroyJointRadiusPercent = 0 -- joints are safe
	explosion.BlastRadius = radius
	explosion.Position = position

	-- set up a table to track the models hit
	local modelsHit = {}

	-- listen for contact
	explosion.Hit:Connect(function(part, distance)
		local parentModel = part.Parent
		if parentModel then
			-- check to see if this model has already been hit
			if modelsHit[parentModel] then
				return
			end
			-- log this model as hit
			modelsHit[parentModel] = true

			-- look for a humanoid
			local humanoid = parentModel:FindFirstChild("Humanoid")
			if humanoid then
				local distanceFactor = distance / explosion.BlastRadius -- get the distance as a value between 0 and 1
				distanceFactor = 1 - distanceFactor -- flip the amount, so that lower == closer == more damage
				humanoid:TakeDamage(maxDamage * distanceFactor) -- TakeDamage to respect ForceFields
			end
		end
	end)

	explosion.Parent = game.Workspace

	-- Roblox removes explosions after a few seconds, but does not destroy them.
	-- To ensure our .Hit connection gets disconnected, destroy the explosion once it's removed.
	explosion.AncestryChanged:Connect(function()
		if not explosion.Parent then
			explosion:Destroy()
		end
	end)
end

customExplosion(Vector3.new(0, 10, 0), 12, 50)
```

### Property: Explosion.ExplosionType

```json
{
  "type": "ExplosionType",
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
  "capabilities": [
    "AvatarBehavior"
  ]
}
```

This property determines how the [Explosion](/docs/reference/engine/classes/Explosion.md) will interact with
[Terrain](/docs/reference/engine/classes/Terrain.md). It is an Enum.ExplosionType value and can be set to one
of three options.

- **NoCraters** - Explosions will not damage Terrain
- **Craters** - Explosions will create craters in Terrain
- **CratersAndDebris** - Redundant, behaves the same as Craters

If ExplosionType is set to create craters in [Terrain](/docs/reference/engine/classes/Terrain.md), the radius
of the crater will be roughly equal to the [Explosion.BlastRadius](/docs/reference/engine/classes/Explosion.md).
Craters are created in all [Terrain](/docs/reference/engine/classes/Terrain.md) materials other than water. The
size of the crater is not influenced by the material, although some
materials create rougher edges than others.

**Stop Explosions from Damaging Terrain**

This code sample includes an example of how the Explosion.ExplosionType
property can be used to stop Explosions from damaging terrain. It is
recommended to set the ExplosionType to NoCraters at the point of Explosion
instantiation, but if that is not practical the code below will work.

```lua
local function onDescendantAdded(instance)
	if instance:IsA("Explosion") then
		instance.ExplosionType = Enum.ExplosionType.NoCraters
		instance:GetPropertyChangedSignal("ExplosionType"):Connect(function()
			instance.ExplosionType = Enum.ExplosionType.NoCraters
		end)
	end
end

workspace.DescendantAdded:Connect(onDescendantAdded)
```

### Property: Explosion.Position

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
  "thread_safety": "ReadSafe",
  "category": "Data",
  "capabilities": [
    "AvatarBehavior"
  ]
}
```

This property is the position of the center of the [Explosion](/docs/reference/engine/classes/Explosion.md). It
is defined in world-space and not influenced by the [Explosion](/docs/reference/engine/classes/Explosion.md)
parent.

[BaseParts](/docs/reference/engine/classes/BasePart.md) will be influenced by the [Explosion](/docs/reference/engine/classes/Explosion.md) if
they are within [Explosion.BlastRadius](/docs/reference/engine/classes/Explosion.md) studs of the explosion's
position.

The effect of an explosion is instantaneous. This means that although the
position of an explosion can be changed after it has been set it cannot
affect two different areas. Once an explosion has been 'detonated',
shortly after parenting it to a descendant of the [Workspace](/docs/reference/engine/classes/Workspace.md), it
will not do so again. In some cases the visual effect of the explosion
will move but it will have no effect.

For this reason a new Explosion should be created if the developer wants
an explosion to appear at a different position.

**Explosion Instantiation**

This code sample includes a brief snippet that creates a large explosion in
the game at 0, 10, 0.

```lua
local explosion = Instance.new("Explosion")
explosion.BlastRadius = 60
explosion.ExplosionType = Enum.ExplosionType.Craters -- damages terrain
explosion.Position = Vector3.new(0, 10, 0)
explosion.Parent = workspace
```

### Property: Explosion.TimeScale

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
  "category": "Data",
  "capabilities": [
    "AvatarBehavior"
  ]
}
```

A value between 0 and 1 that controls the speed of the particle effect. At
1 it runs at normal speed, at 0.5 it runs at half speed, and at 0 it
freezes time.

### Property: Explosion.Visible

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
  "capabilities": [
    "AvatarBehavior"
  ]
}
```

This property determines whether or not the visual effect of an
[Explosion](/docs/reference/engine/classes/Explosion.md) is shown or not.

When Visible is set to false, the explosion will still affect
[BaseParts](/docs/reference/engine/classes/BasePart.md) in its [Explosion.BlastRadius](/docs/reference/engine/classes/Explosion.md), the only
difference is it will not be seen.

One use for this property would be for a developer to make their own
custom explosion effects using a [ParticleEmitter](/docs/reference/engine/classes/ParticleEmitter.md), while retaining
the default [Explosion](/docs/reference/engine/classes/Explosion.md) functionality.

**Explosion Custom Visuals**

This sample includes a function that will create an Explosion but replace the
default Explosion visuals but those of a ParticleEmitter.

```lua
local function customExplosion(position)
	local explosion = Instance.new("Explosion")
	explosion.Position = position
	explosion.Visible = false

	local attachment = Instance.new("Attachment")
	attachment.Position = position
	attachment.Parent = workspace.Terrain

	local particleEmitter = Instance.new("ParticleEmitter")
	particleEmitter.Enabled = false
	particleEmitter.Parent = attachment
	particleEmitter.Speed = NumberRange.new(5, 30)
	particleEmitter.SpreadAngle = Vector2.new(-90, 90)

	explosion.Parent = workspace
	particleEmitter:Emit(20)

	task.delay(5, function()
		if attachment then
			attachment:Destroy()
		end
	end)
end

customExplosion(Vector3.new(0, 10, 0))
```

### Property: Explosion.LocalTransparencyModifier *(hidden)*

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
  "category": "Data",
  "capabilities": [
    "AvatarBehavior"
  ]
}
```

A client-local multiplier for the transparency of the [Explosion](/docs/reference/engine/classes/Explosion.md)
visual effect. It does not replicate from client to server and is useful
when the explosion visual should appear differently for a specific client.

A value of `0`, the default, has no effect on the explosion's appearance,
while a value of `1` makes the visual effect completely invisible to the
local client. Values are clamped between `0` and `1`.

This property does not alter the explosion's physical or damaging effects.
To hide the visual effect for all clients while retaining force and
damage, set [Visible](/docs/reference/engine/classes/Explosion.md) to `false` instead.

## Events

### Event: Explosion.Hit

**Signature:** `Explosion.Hit(part: BasePart, distance: float)`

Fires when the [Explosion](/docs/reference/engine/classes/Explosion.md) hits a [BasePart](/docs/reference/engine/classes/BasePart.md) within its
[Explosion.BlastRadius](/docs/reference/engine/classes/Explosion.md). Returns the part hit along with the
distance of the part from [Explosion.Position](/docs/reference/engine/classes/Explosion.md).

Note that the effect of an [Explosion](/docs/reference/engine/classes/Explosion.md) is not disrupted by
obstacles, this means parts shielded behind other parts will still be hit,
even if the [BasePart](/docs/reference/engine/classes/BasePart.md) they are shielded behind is anchored.

This event will also fire when [Explosion.BlastPressure](/docs/reference/engine/classes/Explosion.md) is equal to
zero. This means developers can program their own custom behavior for
explosions by eliminating the explosion's influence on
[BaseParts](/docs/reference/engine/classes/BasePart.md) and [Terrain](/docs/reference/engine/classes/Terrain.md).

Note that this event will fire for every [BasePart](/docs/reference/engine/classes/BasePart.md) hit. This means
it can fire multiple times for the same player character (as the character
[Model](/docs/reference/engine/classes/Model.md) is made up of multiple parts). For this reason when dealing
custom damage using the [Explosion.Hit](/docs/reference/engine/classes/Explosion.md) event it's recommended to
implement a check to see if the character has already been hit by the
[Explosion](/docs/reference/engine/classes/Explosion.md).

*Security: None · Capabilities: AvatarBehavior*

**Parameters:**

| Name | Type | Description |
|------|------|-------------|
| `part` | `BasePart` | The [BasePart](/docs/reference/engine/classes/BasePart.md) hit by the [Explosion](/docs/reference/engine/classes/Explosion.md). |
| `distance` | `float` | The distance of the hit from [Explosion.Position](/docs/reference/engine/classes/Explosion.md). |

**Custom Explosion**

This sample contains a simple function that creates a custom explosion. The
custom explosion will not break joints as Explosion.DestroyJointRadiusPercent
is equal to 0. This means Humanoids will not be instantly killed as their neck
joints are broken. In this example explosion.BlastPressure is equal to zero so
as not to apply force or damage terrain but this can be changed.

The Explosion.Hit event is used to listen for contact. Once contact has been
made the code will look for the parent model of the BasePart hit by the
explosion. If that model exists, hasn't already been damaged and has a
Humanoid in it damage will be applied based on distance from the explosion's
origin.

```lua
local function customExplosion(position, radius, maxDamage)
	local explosion = Instance.new("Explosion")
	explosion.BlastPressure = 0 -- this could be set higher to still apply velocity to parts
	explosion.DestroyJointRadiusPercent = 0 -- joints are safe
	explosion.BlastRadius = radius
	explosion.Position = position

	-- set up a table to track the models hit
	local modelsHit = {}

	-- listen for contact
	explosion.Hit:Connect(function(part, distance)
		local parentModel = part.Parent
		if parentModel then
			-- check to see if this model has already been hit
			if modelsHit[parentModel] then
				return
			end
			-- log this model as hit
			modelsHit[parentModel] = true

			-- look for a humanoid
			local humanoid = parentModel:FindFirstChild("Humanoid")
			if humanoid then
				local distanceFactor = distance / explosion.BlastRadius -- get the distance as a value between 0 and 1
				distanceFactor = 1 - distanceFactor -- flip the amount, so that lower == closer == more damage
				humanoid:TakeDamage(maxDamage * distanceFactor) -- TakeDamage to respect ForceFields
			end
		end
	end)

	explosion.Parent = game.Workspace

	-- Roblox removes explosions after a few seconds, but does not destroy them.
	-- To ensure our .Hit connection gets disconnected, destroy the explosion once it's removed.
	explosion.AncestryChanged:Connect(function()
		if not explosion.Parent then
			explosion:Destroy()
		end
	end)
end

customExplosion(Vector3.new(0, 10, 0), 12, 50)
```

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