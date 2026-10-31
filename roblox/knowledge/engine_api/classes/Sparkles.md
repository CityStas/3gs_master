---
name: Sparkles
last_updated: 2026-10-30T19:55:53Z
inherits:
  - Instance
  - Object
type: class
memory_category: Instances
summary: "A particle emitter with the visual aesthetic of sparkles."
---

# Class: Sparkles

> A particle emitter with the visual aesthetic of sparkles.

## Description

Sparkles is one of several particle-emitting classes. Like other particle
emitters of its kind, Sparkles objects emit particles when parented to a
[BasePart](/docs/reference/engine/classes/BasePart.md) (such as a [Part](/docs/reference/engine/classes/Part.md)) or an [Attachment](/docs/reference/engine/classes/Attachment.md) within such
a [BasePart](/docs/reference/engine/classes/BasePart.md). Compared to the [ParticleEmitter](/docs/reference/engine/classes/ParticleEmitter.md) class, Sparkles
lacks many different customization properties and special methods, such as
[ParticleEmitter.Lifetime](/docs/reference/engine/classes/ParticleEmitter.md) or [ParticleEmitter:Emit()](/docs/reference/engine/classes/ParticleEmitter.md). It is
useful to create a quick special effect in a pinch; for more detailed work it
is preferable to use a [ParticleEmitter](/docs/reference/engine/classes/ParticleEmitter.md) instead.

When [Sparkles.Enabled](/docs/reference/engine/classes/Sparkles.md) is toggled off, particles emit by this object
will continue to render until their lifetime expires. When a Sparkles object's
[Instance.Parent](/docs/reference/engine/classes/Instance.md) is set to `nil` (and/or [Instance:Destroy()](/docs/reference/engine/classes/Instance.md)ed),
all particles will instantly disappear. If this effect is not desired, try
hiding the parent object at a far away position, then removing the Sparkles
after a few seconds using [Debris](/docs/reference/engine/classes/Debris.md) to give the last particles a chance
to expire. This object does not have a [ParticleEmitter:Clear()](/docs/reference/engine/classes/ParticleEmitter.md) method,
but it is possible to set the [Instance.Parent](/docs/reference/engine/classes/Instance.md) to `nil` and back to the
exact same object for the same effect.

Sparkles particles are only emitted from the center of [BasePart](/docs/reference/engine/classes/BasePart.md) to
which they are parented. Parenting a Sparkles object to an [Attachment](/docs/reference/engine/classes/Attachment.md)
instead allows customization of the particles' start position.

## Code Samples

**Give Sparkles**

The code sample below gives any new players sparkles that are colored the same
as their torso color.

```lua
local Players = game:GetService("Players")

local function onCharacterSpawned(character)
	local hrp = character:WaitForChild("HumanoidRootPart")
	-- Add sparkles that are colored to the player's torso color
	local sparkles = Instance.new("Sparkles")
	sparkles.Parent = hrp
	sparkles.SparkleColor = character:WaitForChild("Body Colors").TorsoColor.Color
	sparkles.Enabled = true
end

local function onPlayerAdded(player)
	player.CharacterAdded:Connect(onCharacterSpawned)
end

Players.PlayerAdded:Connect(onPlayerAdded)
```

**Expected output:** When your character spawns while this script is running, they should have a very sparkly torso, customized for their character.

## Properties

### Property: Sparkles.Enabled

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
    "Basic"
  ]
}
```

The Enabled property, much like [ParticleEmitter.Enabled](/docs/reference/engine/classes/ParticleEmitter.md),
determines whether sparkle particles are emit. Any particles already emit
will continue to render until their lifetime expires. This property is
useful for keeping pre-made sparkle effects off until they are needed
later. Since sparkle particles are destroyed when the `Sparkle` object's
[Instance.Parent](/docs/reference/engine/classes/Instance.md) is set to `nil`, this property is useful in
allowing existing particles the opportunity to expire before destroying
the Fire object altogether. See the function below.

**Give Sparkles**

The code sample below gives any new players sparkles that are colored the same
as their torso color.

```lua
local Players = game:GetService("Players")

local function onCharacterSpawned(character)
	local hrp = character:WaitForChild("HumanoidRootPart")
	-- Add sparkles that are colored to the player's torso color
	local sparkles = Instance.new("Sparkles")
	sparkles.Parent = hrp
	sparkles.SparkleColor = character:WaitForChild("Body Colors").TorsoColor.Color
	sparkles.Enabled = true
end

local function onPlayerAdded(player)
	player.CharacterAdded:Connect(onCharacterSpawned)
end

Players.PlayerAdded:Connect(onPlayerAdded)
```

**Expected output:** When your character spawns while this script is running, they should have a very sparkly torso, customized for their character.

**Enabled**

Demonstrates [Sparkles.Enabled](/docs/reference/engine/classes/Sparkles.md).

```lua
local Debris = game:GetService("Debris")
local part = Instance.new("Part")
part.Parent = workspace
local sparkles = Instance.new("Sparkles")
sparkles.Parent = part
function stopSparkling(sparkles)
	sparkles.Enabled = false -- No more new particles
	Debris:AddItem(sparkles, 4) -- Remove the object after a delay (after existing particles have expired)
end
stopSparkling(part.Sparkles)
```

### Property: Sparkles.SparkleColor

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
    "can_save": true
  },
  "thread_safety": "ReadSafe",
  "category": "Data",
  "capabilities": [
    "Basic"
  ]
}
```

This property functions identically to [Sparkles.Color](/docs/reference/engine/classes/Sparkles.md).

The SparkleColor property determines the color of all the particles emit
by a [Sparkles](/docs/reference/engine/classes/Sparkles.md) object (both existing and future particles). It
behaves similarly to [ParticleEmitter.Color](/docs/reference/engine/classes/ParticleEmitter.md), except that it is only
one color and not a [ColorSequence](/docs/reference/engine/datatypes/ColorSequence.md). Sparkles have a natural
color sequence applied which is most apparent when this property is set to
white; sparkles very faintly animate between a subtle green and red.

It should be noted that sparkles have a partial
[ParticleEmitter.LightEmission](/docs/reference/engine/classes/ParticleEmitter.md) effect, so dark colors tend to
render more transparent and white colors look very bright.

**Give Sparkles**

The code sample below gives any new players sparkles that are colored the same
as their torso color.

```lua
local Players = game:GetService("Players")

local function onCharacterSpawned(character)
	local hrp = character:WaitForChild("HumanoidRootPart")
	-- Add sparkles that are colored to the player's torso color
	local sparkles = Instance.new("Sparkles")
	sparkles.Parent = hrp
	sparkles.SparkleColor = character:WaitForChild("Body Colors").TorsoColor.Color
	sparkles.Enabled = true
end

local function onPlayerAdded(player)
	player.CharacterAdded:Connect(onCharacterSpawned)
end

Players.PlayerAdded:Connect(onPlayerAdded)
```

**Expected output:** When your character spawns while this script is running, they should have a very sparkly torso, customized for their character.

### Property: Sparkles.TimeScale

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
    "Basic"
  ]
}
```

A value from 0 to 1 that controls the speed of the sparkle effect. A value
of 1 runs the effect at normal speed, 0.5 runs it at half speed, and 0
freezes the effect.

### Property: Sparkles.Color *(hidden)*

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
  "category": "Data",
  "capabilities": [
    "Basic"
  ]
}
```

The Color property determines the color of all the particles emit by a
[Sparkles](/docs/reference/engine/classes/Sparkles.md) object (both existing and future particles). It behaves
similarly to [ParticleEmitter.Color](/docs/reference/engine/classes/ParticleEmitter.md), except that it is only one
color and not a [ColorSequence](/docs/reference/engine/datatypes/ColorSequence.md). Sparkles have a natural color
sequence applied which is most apparent when this property is set to
white; sparkles very faintly animate between a subtle green and red.

It should be noted that sparkles have a partial
[ParticleEmitter.LightEmission](/docs/reference/engine/classes/ParticleEmitter.md) effect, so dark colors tend to
render more transparent and white colors look very bright.

**Give Sparkles**

The code sample below gives any new players sparkles that are colored the same
as their torso color.

```lua
local Players = game:GetService("Players")

local function onCharacterSpawned(character)
	local hrp = character:WaitForChild("HumanoidRootPart")
	-- Add sparkles that are colored to the player's torso color
	local sparkles = Instance.new("Sparkles")
	sparkles.Parent = hrp
	sparkles.SparkleColor = character:WaitForChild("Body Colors").TorsoColor.Color
	sparkles.Enabled = true
end

local function onPlayerAdded(player)
	player.CharacterAdded:Connect(onCharacterSpawned)
end

Players.PlayerAdded:Connect(onPlayerAdded)
```

**Expected output:** When your character spawns while this script is running, they should have a very sparkly torso, customized for their character.

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