---
name: AnimationController
last_updated: 2026-10-30T19:55:51Z
inherits:
  - Instance
  - Object
type: class
memory_category: Animation
summary: "Allows animations to be loaded and applied to a character or model in place of a Humanoid."
---

# Class: AnimationController

> Allows animations to be loaded and applied to a character or model in place of
> a [Humanoid](/docs/reference/engine/classes/Humanoid.md).

## Description

An object which allows animations to be loaded and applied to a character or
model in place of a [Humanoid](/docs/reference/engine/classes/Humanoid.md). Creates an [Animator](/docs/reference/engine/classes/Animator.md) and loads
animations to update [Motor6Ds](/docs/reference/engine/classes/Motor6D.md) of said character to react in
the way that is described within the animation asset referenced by an
[Animation](/docs/reference/engine/classes/Animation.md) object.

Note that the [LoadAnimation()](/docs/reference/engine/classes/AnimationController.md)
method of this class has been deprecated. Instead, you should call
[Animator:LoadAnimation()](/docs/reference/engine/classes/Animator.md) directly from an [Animator](/docs/reference/engine/classes/Animator.md) which can
be created manually in Studio and directly referenced in scripts. When the
deprecated method is called from an [AnimationController](/docs/reference/engine/classes/AnimationController.md), the
controller itself does nothing regarding the animation intended to be loaded,
except to automatically generate an [Animator](/docs/reference/engine/classes/Animator.md), onto which the loading
call and animation ID are transferred. In this way, the
[AnimationController](/docs/reference/engine/classes/AnimationController.md) can be thought of as nothing more than an empty
shell for a child [Animator](/docs/reference/engine/classes/Animator.md) object which handles any actual
functionality regarding animations.

## Code Samples

**Using an AnimationController to animation non-player objects**

This code sample demonstrates how an `AnimationController` can be used in
place of a `Humanoid` for non player character objects.

A basic rig is loaded using `InsertService` and the default `Humanoid` is
replaced with an `AnimationController`. An `AnimationTrack` is then created
and played.

```lua
local InsertService = game:GetService("InsertService")

-- Load a model for demonstration
local npcModel = InsertService:LoadAsset(516159357):GetChildren()[1]
npcModel.Name = "NPC"
npcModel.PrimaryPart.Anchored = true
npcModel:SetPrimaryPartCFrame(CFrame.new(0, 5, 0))
npcModel.Parent = workspace

-- Replace the humanoid with an animationcontroller
local humanoid = npcModel:FindFirstChildOfClass("Humanoid")
humanoid:Destroy()
local animationController = Instance.new("AnimationController")
animationController.Parent = npcModel

-- Create and load an animation
local animation = Instance.new("Animation")
animation.AnimationId = "http://www.roblox.com/asset/?id=507771019" -- Roblox dance emote
local animationTrack = animationController:LoadAnimation(animation)

-- Play the animation
animationTrack:Play()
```

## Methods

### Method: AnimationController:GetPlayingAnimationTracks

**Signature:** `AnimationController:GetPlayingAnimationTracks(): Array`

Returns an array of all [AnimationTracks](/docs/reference/engine/classes/AnimationTrack.md) that are
currently being played by the [AnimationController](/docs/reference/engine/classes/AnimationController.md).

A typical use for this function is stopping currently playing tracks using
[AnimationTrack:Stop()](/docs/reference/engine/classes/AnimationTrack.md).

Note this function will not return [AnimationTracks](/docs/reference/engine/classes/AnimationTrack.md)
that have loaded but are not playing. If the developer wishes to track
these they will need to index them manually. See below for one example of
how this could be achieved:

*Security: None · Thread Safety: Unsafe · Capabilities: Animation*

**Returns:** `Array` — An array of playing [AnimationTracks](/docs/reference/engine/classes/AnimationTrack.md).

**Stop All Tracks**

This sample contains a quick function to stop all playing AnimationTracks on
an AnimationController or Humanoid.

```lua
local function stopAllTracks(animationController)
	for _, track in pairs(animationController:GetPlayingAnimationTracks()) do
		track:Stop()
	end
end

local animationController = script.Parent:FindFirstChild("AnimationController")

stopAllTracks(animationController)
```

**Get Playing Animation Tracks**

Demonstrates [AnimationController:GetPlayingAnimationTracks()](/docs/reference/engine/classes/AnimationController.md).

```lua
local Workspace = game:GetService("Workspace")

local animationController = Instance.new("AnimationController")
local animator = Instance.new("Animator")
animator.Parent = animationController
animationController.Parent = Workspace

local animationTracks = animationController:GetPlayingAnimationTracks()
for _, track in animationTracks do
	print(track.Animation.Name)
end
```

### Method: AnimationController:LoadAnimation

**Signature:** `AnimationController:LoadAnimation(animation: Animation): AnimationTrack`

> **Deprecated:** This function is deprecated in favor of using [Animator:LoadAnimation()](/docs/reference/engine/classes/Animator.md) directly (the [Animator](/docs/reference/engine/classes/Animator.md) may be created while editing or at runtime).

This function loads an [Animation](/docs/reference/engine/classes/Animation.md) onto an
[AnimationController](/docs/reference/engine/classes/AnimationController.md), returning an [AnimationTrack](/docs/reference/engine/classes/AnimationTrack.md) that can
be used for playback.

*Security: None · Thread Safety: Unsafe · Capabilities: Animation*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `animation` | `Animation` |  | The [Animation](/docs/reference/engine/classes/Animation.md) to be used. |

**Returns:** `AnimationTrack`

**Using an AnimationController to animation non-player objects**

This code sample demonstrates how an `AnimationController` can be used in
place of a `Humanoid` for non player character objects.

A basic rig is loaded using `InsertService` and the default `Humanoid` is
replaced with an `AnimationController`. An `AnimationTrack` is then created
and played.

```lua
local InsertService = game:GetService("InsertService")

-- Load a model for demonstration
local npcModel = InsertService:LoadAsset(516159357):GetChildren()[1]
npcModel.Name = "NPC"
npcModel.PrimaryPart.Anchored = true
npcModel:SetPrimaryPartCFrame(CFrame.new(0, 5, 0))
npcModel.Parent = workspace

-- Replace the humanoid with an animationcontroller
local humanoid = npcModel:FindFirstChildOfClass("Humanoid")
humanoid:Destroy()
local animationController = Instance.new("AnimationController")
animationController.Parent = npcModel

-- Create and load an animation
local animation = Instance.new("Animation")
animation.AnimationId = "http://www.roblox.com/asset/?id=507771019" -- Roblox dance emote
local animationTrack = animationController:LoadAnimation(animation)

-- Play the animation
animationTrack:Play()
```

## Events

### Event: AnimationController.AnimationPlayed

**Signature:** `AnimationController.AnimationPlayed(animationTrack: AnimationTrack)`

This event fires whenever the [AnimationController](/docs/reference/engine/classes/AnimationController.md) begins playing
an animation. It returns the [AnimationTrack](/docs/reference/engine/classes/AnimationTrack.md) playing.

The [AnimationTrack](/docs/reference/engine/classes/AnimationTrack.md) can be used to access the animation's playback
functions and events. It will only fire for animations playing on the
specific [AnimationController](/docs/reference/engine/classes/AnimationController.md).

See [Humanoid.AnimationPlayed](/docs/reference/engine/classes/Humanoid.md) for the [Humanoid](/docs/reference/engine/classes/Humanoid.md) variant of
this function.

*Security: None · Capabilities: Animation*

**Parameters:**

| Name | Type | Description |
|------|------|-------------|
| `animationTrack` | `AnimationTrack` | The [AnimationTrack](/docs/reference/engine/classes/AnimationTrack.md) that was played. |

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