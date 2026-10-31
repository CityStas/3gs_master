---
name: Smoke
last_updated: 2026-10-30T19:55:53Z
inherits:
  - Instance
  - Object
type: class
memory_category: Instances
summary: "A particle emitter with the visual aesthetic of smoke."
---

# Class: Smoke

> A particle emitter with the visual aesthetic of smoke.

## Description

Smoke is one of several particle-emitting classes. Like other particle
emitters of its kind, Smoke objects emit particles when parented to a
[BasePart](/docs/reference/engine/classes/BasePart.md) (such as a [Part](/docs/reference/engine/classes/Part.md)) or an [Attachment](/docs/reference/engine/classes/Attachment.md) within such
a [BasePart](/docs/reference/engine/classes/BasePart.md). Compared to the [ParticleEmitter](/docs/reference/engine/classes/ParticleEmitter.md) class, Smoke lacks
many different customization properties and special methods, such as
[ParticleEmitter.Lifetime](/docs/reference/engine/classes/ParticleEmitter.md) or [ParticleEmitter:Emit()](/docs/reference/engine/classes/ParticleEmitter.md). It is
useful to create a quick special effect in a pinch; for more detailed work it
is preferable to use a [ParticleEmitter](/docs/reference/engine/classes/ParticleEmitter.md) instead.

When [Smoke.Enabled](/docs/reference/engine/classes/Smoke.md) is toggled off, particles emit by this object will
continue to render until their lifetime expires. When a Smoke object's
[Instance.Parent](/docs/reference/engine/classes/Instance.md) is set to `nil` (and/or [Instance:Destroy()](/docs/reference/engine/classes/Instance.md)ed),
all particles will instantly disappear. If this effect is not desired, try
hiding the parent object at a far away position, then removing the Smoke after
a few seconds using [Debris](/docs/reference/engine/classes/Debris.md) to give the last particles a chance to
expire. This object does not have a [ParticleEmitter:Clear()](/docs/reference/engine/classes/ParticleEmitter.md) method,
but it is possible to set the [Instance.Parent](/docs/reference/engine/classes/Instance.md) to `nil` and back to the
exact same object for the same effect.

Smoke particles are only emitted from the center of [BasePart](/docs/reference/engine/classes/BasePart.md) to which
they are parented. Parenting a Smoke object to an [Attachment](/docs/reference/engine/classes/Attachment.md) instead
allows customization of the particles' start position.

## Code Samples

**Add Smoke to All Fire**

This code sample adds a `Smoke` object to every `Fire` object in the
`Workspace`. It does this by using a recursive search.

```lua
local function recurseForFire(object)
	-- Check if we found a Fire object that has no Smoke
	if object:IsA("Fire") and not object.Parent:FindFirstChildOfClass("Smoke") then
		-- Create a smoke effect for this fire
		local smoke = Instance.new("Smoke")
		smoke.Color = Color3.new(0, 0, 0)
		smoke.Opacity = 0.15
		smoke.RiseVelocity = 4
		smoke.Size = object.Size / 4
		smoke.Parent = object.Parent
	end
	-- Continue search for Fire objects
	for _, child in pairs(object:GetChildren()) do
		recurseForFire(child)
	end
end

recurseForFire(workspace)
```

**Expected output:** When run, you should see every Fire object in the workspace have a Smoke sibling object (if it did not have one before).

## Properties

### Property: Smoke.Color

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

The Color property determines the color of all the particles emit by a
[Smoke](/docs/reference/engine/classes/Smoke.md) object (both existing and future particles). It behaves
similarly to [ParticleEmitter.Color](/docs/reference/engine/classes/ParticleEmitter.md), except that it is only one
color and not a [ColorSequence](/docs/reference/engine/datatypes/ColorSequence.md). A color of white with some
[Smoke.Opacity](/docs/reference/engine/classes/Smoke.md) makes for a nice fog effect, and a very opaque black
color can compliment a [Fire](/docs/reference/engine/classes/Fire.md) object nicely.

**Add Smoke to All Fire**

This code sample adds a `Smoke` object to every `Fire` object in the
`Workspace`. It does this by using a recursive search.

```lua
local function recurseForFire(object)
	-- Check if we found a Fire object that has no Smoke
	if object:IsA("Fire") and not object.Parent:FindFirstChildOfClass("Smoke") then
		-- Create a smoke effect for this fire
		local smoke = Instance.new("Smoke")
		smoke.Color = Color3.new(0, 0, 0)
		smoke.Opacity = 0.15
		smoke.RiseVelocity = 4
		smoke.Size = object.Size / 4
		smoke.Parent = object.Parent
	end
	-- Continue search for Fire objects
	for _, child in pairs(object:GetChildren()) do
		recurseForFire(child)
	end
end

recurseForFire(workspace)
```

**Expected output:** When run, you should see every Fire object in the workspace have a Smoke sibling object (if it did not have one before).

### Property: Smoke.Enabled

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
determines whether smoke particles are emitted. Any particles already emit
will continue to render until their lifetime expires. This property is
useful for keeping pre-made smoke effects off until they are needed later.
Since smoke particles are destroyed when the [Smoke](/docs/reference/engine/classes/Smoke.md) object's
[Instance.Parent](/docs/reference/engine/classes/Instance.md) is set to `nil`, this property is useful in
allowing existing particles the opportunity to expire before destroying
the Fire object altogether. See the function below.

**Add Smoke to All Fire**

This code sample adds a `Smoke` object to every `Fire` object in the
`Workspace`. It does this by using a recursive search.

```lua
local function recurseForFire(object)
	-- Check if we found a Fire object that has no Smoke
	if object:IsA("Fire") and not object.Parent:FindFirstChildOfClass("Smoke") then
		-- Create a smoke effect for this fire
		local smoke = Instance.new("Smoke")
		smoke.Color = Color3.new(0, 0, 0)
		smoke.Opacity = 0.15
		smoke.RiseVelocity = 4
		smoke.Size = object.Size / 4
		smoke.Parent = object.Parent
	end
	-- Continue search for Fire objects
	for _, child in pairs(object:GetChildren()) do
		recurseForFire(child)
	end
end

recurseForFire(workspace)
```

**Expected output:** When run, you should see every Fire object in the workspace have a Smoke sibling object (if it did not have one before).

**Enabled**

Demonstrates [Smoke.Enabled](/docs/reference/engine/classes/Smoke.md).

```lua
local Debris = game:GetService("Debris")
local part = Instance.new("Part")
part.Parent = workspace
local smoke = Instance.new("Smoke")
smoke.Parent = part
function stopSmoke(smoke)
	smoke.Enabled = false -- No more new particles
	Debris:AddItem(smoke, 10) -- Remove the object after a delay (after existing particles have expired)
end
stopSmoke(part.Smoke)
```

### Property: Smoke.Opacity

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

Opacity determines the opaqueness of the smoke particles. It must be in
the range [0, 1]. This property works **inversely** in comparison to a
part's [BasePart.Transparency](/docs/reference/engine/classes/BasePart.md) or ParticleEmitter's
[ParticleEmitter.Transparency](/docs/reference/engine/classes/ParticleEmitter.md): a value of 0 is completely
invisible, 1 is completely visible.

The texture that Roblox uses for [Smoke](/docs/reference/engine/classes/Smoke.md) particles is partially
transparent, so setting this property to 1 still yields transparency in
rendered smoke.

**Add Smoke to All Fire**

This code sample adds a `Smoke` object to every `Fire` object in the
`Workspace`. It does this by using a recursive search.

```lua
local function recurseForFire(object)
	-- Check if we found a Fire object that has no Smoke
	if object:IsA("Fire") and not object.Parent:FindFirstChildOfClass("Smoke") then
		-- Create a smoke effect for this fire
		local smoke = Instance.new("Smoke")
		smoke.Color = Color3.new(0, 0, 0)
		smoke.Opacity = 0.15
		smoke.RiseVelocity = 4
		smoke.Size = object.Size / 4
		smoke.Parent = object.Parent
	end
	-- Continue search for Fire objects
	for _, child in pairs(object:GetChildren()) do
		recurseForFire(child)
	end
end

recurseForFire(workspace)
```

**Expected output:** When run, you should see every Fire object in the workspace have a Smoke sibling object (if it did not have one before).

### Property: Smoke.RiseVelocity

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

RiseVelocity behaves similarly to [ParticleEmitter.Speed](/docs/reference/engine/classes/ParticleEmitter.md) and
[Fire.Heat](/docs/reference/engine/classes/Fire.md): it determines how fast the smoke particles move during
their lifetime. It must be in the range [-25, 25]. Negative values will
cause particles to emit in the bottom (-Y) direction of the parent
[BasePart](/docs/reference/engine/classes/BasePart.md).

When using a [Smoke](/docs/reference/engine/classes/Smoke.md) effect to create fog, set this property to 0.
For large smoke effects, make the rise subtle (2 to 8). For chimneys and
smokestacks, higher values are appropriate.

**Add Smoke to All Fire**

This code sample adds a `Smoke` object to every `Fire` object in the
`Workspace`. It does this by using a recursive search.

```lua
local function recurseForFire(object)
	-- Check if we found a Fire object that has no Smoke
	if object:IsA("Fire") and not object.Parent:FindFirstChildOfClass("Smoke") then
		-- Create a smoke effect for this fire
		local smoke = Instance.new("Smoke")
		smoke.Color = Color3.new(0, 0, 0)
		smoke.Opacity = 0.15
		smoke.RiseVelocity = 4
		smoke.Size = object.Size / 4
		smoke.Parent = object.Parent
	end
	-- Continue search for Fire objects
	for _, child in pairs(object:GetChildren()) do
		recurseForFire(child)
	end
end

recurseForFire(workspace)
```

**Expected output:** When run, you should see every Fire object in the workspace have a Smoke sibling object (if it did not have one before).

### Property: Smoke.Size

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

The Size property of [Smoke](/docs/reference/engine/classes/Smoke.md) determines the size of the newly emit
smoke particles. Unlike [Smoke.Color](/docs/reference/engine/classes/Smoke.md), this property will not change
the size of existing particles. It must be in the range [0.1, 100]. Unlike
[ParticleEmitter.Size](/docs/reference/engine/classes/ParticleEmitter.md), this property is only a number (not a
[NumberSequence](/docs/reference/engine/datatypes/NumberSequence.md)). Also note also that the size of the particles
is not 1-to-1 with studs; in fact, the size of the smoke particle is more
than twice as large. At the largest size, smoke particles can render
larger than 200 studs wide!

**Add Smoke to All Fire**

This code sample adds a `Smoke` object to every `Fire` object in the
`Workspace`. It does this by using a recursive search.

```lua
local function recurseForFire(object)
	-- Check if we found a Fire object that has no Smoke
	if object:IsA("Fire") and not object.Parent:FindFirstChildOfClass("Smoke") then
		-- Create a smoke effect for this fire
		local smoke = Instance.new("Smoke")
		smoke.Color = Color3.new(0, 0, 0)
		smoke.Opacity = 0.15
		smoke.RiseVelocity = 4
		smoke.Size = object.Size / 4
		smoke.Parent = object.Parent
	end
	-- Continue search for Fire objects
	for _, child in pairs(object:GetChildren()) do
		recurseForFire(child)
	end
end

recurseForFire(workspace)
```

**Expected output:** When run, you should see every Fire object in the workspace have a Smoke sibling object (if it did not have one before).

### Property: Smoke.TimeScale

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

A value between 0-1 than controls the speed of the particle effect. At 1
it runs at normal speed, at 0.5 it runs at half speed, and at 0 it freezes
time.

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