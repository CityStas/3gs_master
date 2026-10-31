---
name: Fire
last_updated: 2026-10-30T19:55:52Z
inherits:
  - Instance
  - Object
type: class
memory_category: Instances
summary: "A preconfigured particle emitter with the visual aesthetic of fire."
---

# Class: Fire

> A preconfigured particle emitter with the visual aesthetic of fire.

## Description

[Fire](/docs/reference/engine/classes/Fire.md) is one of several preconfigured particle-emitting classes,
alongside [Smoke](/docs/reference/engine/classes/Smoke.md), [Sparkles](/docs/reference/engine/classes/Sparkles.md), and others. Like the others, it
emits particles when parented to a [BasePart](/docs/reference/engine/classes/BasePart.md) or an [Attachment](/docs/reference/engine/classes/Attachment.md)
while [Enabled](/docs/reference/engine/classes/Fire.md). This object is useful to create a quick
visual effect for fire, but for more detailed work it's recommended that you
use a [ParticleEmitter](/docs/reference/engine/classes/ParticleEmitter.md) instead.

Particles emit from the center of the parent in an upward (**+Y**) direction,
but a negative [Heat](/docs/reference/engine/classes/Fire.md) value may be used to emit particles
downward (**-Y**). Using an [Attachment](/docs/reference/engine/classes/Attachment.md) as the parent instead of a
[BasePart](/docs/reference/engine/classes/BasePart.md) allows for the emission position/direction to be modified by
changing the [Attachment.CFrame](/docs/reference/engine/classes/Attachment.md) or related properties.

[Fire](/docs/reference/engine/classes/Fire.md) objects consist of two emitters, each affected in various ways by
the [Size](/docs/reference/engine/classes/Fire.md), [Heat](/docs/reference/engine/classes/Fire.md), [Color](/docs/reference/engine/classes/Fire.md),
and [SecondaryColor](/docs/reference/engine/classes/Fire.md) properties. Particles which
emit from the smaller, secondary emitter have a significantly longer lifetime
(and rise farther) than those emitted by the primary emitter.

When [Enabled](/docs/reference/engine/classes/Fire.md) is off, existing particles continue to
render until they expire. However, if the [Fire](/docs/reference/engine/classes/Fire.md) object's
[Parent](/docs/reference/engine/classes/Instance.md) is set to `nil`, all existing particles
immediately disappear, similar to the behavior of
[ParticleEmitter:Clear()](/docs/reference/engine/classes/ParticleEmitter.md).

[Fire](/docs/reference/engine/classes/Fire.md) objects emit no light on their own. To help create a cohesive
environment around a burning object, try adding a [PointLight](/docs/reference/engine/classes/PointLight.md) with an
orange [Color](/docs/reference/engine/classes/Light.md).

## Code Samples

**Lighting Torches**

This code sample adds [Fire](/docs/reference/engine/classes/Fire.md) to all [BasePart](/docs/reference/engine/classes/BasePart.md) instances in the
[Workspace](/docs/reference/engine/classes/Workspace.md) named `Torch`.

```lua
local Workspace = game:GetService("Workspace")

for _, descendant in Workspace:GetDescendants() do
	if descendant.Name == "Torch" and descendant:IsA("BasePart") then
		local fire = Instance.new("Fire")
		fire.Heat = 10
		fire.SecondaryColor = Color3.new(1, 1, 1)
		fire.Size = math.max(descendant.Size.X, descendant.Size.Z) -- Pick the larger of the two dimensions
		fire.Parent = descendant
	end
end
```

**Expected output:** When run, parts in the workspace named `Torch` should each have a `Class.Fire` object parented to them. The fire should be about the size of the part.

**Toggle Fire Effect**

This code sample allows a player to click the parent `BasePart` to toggle a
fire effect.

```lua
local part = script.Parent

local clickDetector = Instance.new("ClickDetector")
clickDetector.Parent = part

local fire = Instance.new("Fire")
fire.Parent = part

local light = Instance.new("PointLight")
light.Parent = part

local function onClick()
	fire.Enabled = not fire.Enabled
	light.Enabled = fire.Enabled
end

clickDetector.MouseClick:Connect(onClick)
```

**Expected output:** When run, ClickDetector, Fire and PointLight objects are added to the part. Upon clicking the part, the Fire and PointLight should toggle on or off.

## Properties

### Property: Fire.Color

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

This property determines the color of the larger particles emitted by a
[Fire](/docs/reference/engine/classes/Fire.md) object. It is essentially the color of the outer portion of
the flame.

In general, the cooler flames are on the outside of a fire. Therefore,
fire looks more realistic if the outer portions are red or orange-yellow.
A fire that is bright all throughout doesn't look very realistic, so avoid
setting this property to yellow or white.

### Property: Fire.Enabled

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

This property, much like [ParticleEmitter.Enabled](/docs/reference/engine/classes/ParticleEmitter.md), determines
whether flame particles are emitted. Any particles already emitted will
continue to render until their lifetime expires.

Since all fire particles are destroyed when the [Fire](/docs/reference/engine/classes/Fire.md) object's
[Parent](/docs/reference/engine/classes/Instance.md) is set to `nil`, this property is useful in
allowing existing particles the opportunity to expire before destroying
the [Fire](/docs/reference/engine/classes/Fire.md) object altogether (see the code example below).

**Enabled**

Demonstrates [Fire.Enabled](/docs/reference/engine/classes/Fire.md).

```lua
local Debris = game:GetService("Debris")

local function douseFlames(fire)
	fire.Enabled = false -- No more new particles
	Debris:AddItem(fire, 2) -- Remove the object after existing particles have expired
end

local part = Instance.new("Part")
part.Anchored = true
part.Parent = workspace

local fire = Instance.new("Fire")
fire.Parent = part

douseFlames(part.Fire)
```

### Property: Fire.Heat

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
  "thread_safety": "ReadSafe",
  "category": "Data",
  "capabilities": [
    "Basic"
  ]
}
```

This property determines how fast particles are emitted from the
[Fire](/docs/reference/engine/classes/Fire.md) object. It is limited to the range of `-25` to `25`
inclusive. Positive values are in the top (**+Y**) direction of the parent
[BasePart](/docs/reference/engine/classes/BasePart.md) or [Attachment](/docs/reference/engine/classes/Attachment.md), while negative values are in the
downward (**-Y**) direction. It also affects the
[ParticleEmitter.Acceleration](/docs/reference/engine/classes/ParticleEmitter.md) of the inner particles.

### Property: Fire.SecondaryColor

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

This property determines the color of the smaller particles emitted by a
[Fire](/docs/reference/engine/classes/Fire.md) object. It is essentially the color of the inner portion of
the flame.

Note that the inner particles use a [ParticleEmitter.LightEmission](/docs/reference/engine/classes/ParticleEmitter.md)
of `1`, so darker colors will instead cause the particles to appear
transparent, and black will stop rendering inner particles altogether.

### Property: Fire.Size

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
  "thread_safety": "ReadSafe",
  "category": "Data",
  "capabilities": [
    "Basic"
  ]
}
```

This property determines the size of the flame particles. It must be in
the range of `2` to `30`. Unlike [ParticleEmitter.Size](/docs/reference/engine/classes/ParticleEmitter.md), the actual
size of the flames will not match 1:1 with the equivalent size in studs;
it is somewhat smaller.

If you add a [PointLight](/docs/reference/engine/classes/PointLight.md) as a sibling to the [Fire](/docs/reference/engine/classes/Fire.md) object to
generate light, try setting the light's
[Brightness](/docs/reference/engine/classes/PointLight.md) and
[Range](/docs/reference/engine/classes/PointLight.md) proportional to this property so that
larger flames produce more light.

### Property: Fire.TimeScale

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

A value between `0` and `1` than controls the speed of the particle
effect. `1` runs at normal speed, `0.5` runs at half speed, and `0`
freezes time.

### Property: Fire.size

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

> **Deprecated:** This property is a deprecated variant of [Fire.Size](/docs/reference/engine/classes/Fire.md) which should be used instead.

### Property: Fire.LocalTransparencyModifier *(hidden)*

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
    "Basic"
  ]
}
```

This property is a multiplier for the [Fire](/docs/reference/engine/classes/Fire.md) object's transparency
that is only visible to the local client. It does not replicate from
client to server and is useful for when the object should appear
differently for a specific client.

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