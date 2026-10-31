---
name: Animator
last_updated: 2026-10-30T19:55:51Z
inherits:
  - Instance
  - Object
type: class
memory_category: Instances
summary: "Responsible for the playback and replication of Animations."
---

# Class: Animator

> Responsible for the playback and replication of [Animations](/docs/reference/engine/classes/Animation.md).

## Description

`Animator` is the main class responsible for the playback and replication of
[Animations](/docs/reference/engine/classes/Animation.md). All replication of playing
[AnimationTracks](/docs/reference/engine/classes/AnimationTrack.md) is handled through the `Animator`
instance.

See [Animation in Roblox](/docs/en-us/animation.md) to learn how to create and add
pre-built or custom animations to your game.

## Properties

### Property: Animator.EvaluationThrottled

```json
{
  "type": "boolean",
  "access": "ReadWrite",
  "security": {
    "read": "None",
    "write": "None"
  },
  "serialization": {
    "can_load": false,
    "can_save": false
  },
  "thread_safety": "Safe",
  "category": "Behavior",
  "capabilities": [
    "Animation"
  ]
}
```

A read-only property that indicates whether animation evaluation was
throttled (skipped) on this frame. When `true`, the [Animator](/docs/reference/engine/classes/Animator.md)
reused the pose from the previous frame instead of evaluating fresh
animation data.

This property is useful when layering procedural animation on top of
[Transform](/docs/reference/engine/classes/AnimationConstraint.md) — if evaluation was
throttled, applying procedural offsets would fight the stale pose and
should be skipped:

**Evaluation Throttled**

Demonstrates [Animator.EvaluationThrottled](/docs/reference/engine/classes/Animator.md).

```lua
local RunService = game:GetService("RunService")
local Workspace = game:GetService("Workspace")

local animationController = Instance.new("AnimationController")
local animator = Instance.new("Animator")
animator.Parent = animationController
animationController.Parent = Workspace

local neck = Instance.new("Motor6D")

local function computeNeckRotation()
    return CFrame.Angles(0, 0.01, 0)
end

RunService.PreSimulation:Connect(function()
    if not animator.EvaluationThrottled then
        neck.Transform = computeNeckRotation() * neck.Transform
    end
end)
```

### Property: Animator.PreferLodEnabled

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
  "capabilities": [
    "Animation"
  ]
}
```

When `true` (the default), the engine may reduce animation evaluation
frequency for remotely-simulated characters based on distance, screen
coverage, and frame budget. When set to `false`, LOD-based throttling is
disabled and this [Animator](/docs/reference/engine/classes/Animator.md) always evaluates at full fidelity.

Setting this to `false` is useful for important NPCs or characters that
must always animate smoothly regardless of distance. However, disabling
LOD for many animators simultaneously can impact performance.

Note that this property only controls per-animator LOD throttling. The
workspace-level [Workspace.ClientAnimatorThrottlingMode](/docs/reference/engine/classes/Workspace.md) setting can
independently disable or enable throttling for all animators.

## Methods

### Method: Animator:ApplyJointVelocities

**Signature:** `Animator:ApplyJointVelocities(motors: Variant): ()`

Given the current set of [AnimationTracks](/docs/reference/engine/classes/AnimationTrack.md) playing
and their current times and play speeds, this method computes relative
velocities between the parts and applies them to [Motor6D.Part1](/docs/reference/engine/classes/Motor6D.md)
(the part which `Animator` considers the "child" part). These relative
velocity calculations and assignments happen in the order provided.

This method doesn't apply velocities for a given joint if both of the
joint's parts are currently part of the same assembly; for example, if
they are still connected directly or indirectly by motors or welds.

Note that this method doesn't disable or remove the joints for you. You
must disable or otherwise remove the rigid joints from the assembly before
calling this method.

The given [Motor6Ds](/docs/reference/engine/classes/Motor6D.md) are not required to be descendants of
the [DataModel](/docs/reference/engine/classes/DataModel.md). Removing the joints from the [DataModel](/docs/reference/engine/classes/DataModel.md)
before calling this method is supported.

*Security: None · Thread Safety: Unsafe · Capabilities: Animation*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `motors` | `Variant` |  | An array of [Motor6D](/docs/reference/engine/classes/Motor6D.md) instances to compute and apply velocities for. |

**Returns:** `()`

### Method: Animator:GetPlayingAnimationTracks

**Signature:** `Animator:GetPlayingAnimationTracks(): Array`

Returns the list of currently active
[AnimationTracks](/docs/reference/engine/classes/AnimationTrack.md) on this [Animator](/docs/reference/engine/classes/Animator.md). This
includes tracks that are fading out and does **not** depend on
[AnimationTrack.IsPlaying](/docs/reference/engine/classes/AnimationTrack.md) being `true`; as a result,
[GetTrackByAnimationId()](/docs/reference/engine/classes/Animator.md) may be a
better option to get a specific [AnimationTrack](/docs/reference/engine/classes/AnimationTrack.md) by its asset ID.
Fading tracks are automatically stopped and removed from this list once
their blend weight reaches zero.

*Security: None · Thread Safety: Unsafe · Capabilities: Animation · Simulation Access: true*

**Returns:** `Array` — An array of currently active [AnimationTracks](/docs/reference/engine/classes/AnimationTrack.md) on
this [Animator](/docs/reference/engine/classes/Animator.md), including tracks that are fading out.

### Method: Animator:GetTrackByAnimationId

**Signature:** `Animator:GetTrackByAnimationId(animationId: ContentId): AnimationTrack?`

Returns an existing [AnimationTrack](/docs/reference/engine/classes/AnimationTrack.md) on this [Animator](/docs/reference/engine/classes/Animator.md) that
was loaded from an [Animation](/docs/reference/engine/classes/Animation.md) with the given animation ID. Unlike
[LoadAnimation()](/docs/reference/engine/classes/Animator.md), this method does **not**
create a new [AnimationTrack](/docs/reference/engine/classes/AnimationTrack.md) instance; it only looks up a track
that was previously loaded.

If multiple tracks have been loaded for the same animation ID, this method
returns the first match. If no matching track exists, it returns `nil`.

*Security: None · Thread Safety: Unsafe · Capabilities: Animation · Simulation Access: true*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `animationId` | `ContentId` |  | The asset ID of the [Animation](/docs/reference/engine/classes/Animation.md) whose loaded track should be retrieved. |

**Returns:** `AnimationTrack?` — The first [AnimationTrack](/docs/reference/engine/classes/AnimationTrack.md) on this `Animator` that was loaded
from the given animation ID, or `nil` if none has been loaded.

**Get Animation Track by ID**

The following [LocalScript](/docs/reference/engine/classes/LocalScript.md), when placed in
[StarterPlayerScripts](/docs/reference/engine/classes/StarterPlayerScripts.md), loads a "kick" animation onto the player's
character and plays it. Then, after 1 second within a
[RunService:BindToSimulation()](/docs/reference/engine/classes/RunService.md) binding, it gets the animation track by
its animation asset ID and uses that reference to stop playing the track.

```lua
local Players = game:GetService("Players")
local RunService = game:GetService("RunService")

local ANIM_ID = "rbxassetid://2515090838"

local player = Players.LocalPlayer
local character = player.Character or player.CharacterAdded:Wait()

-- Ensure that the character's humanoid contains an Animator object
local humanoid = character:WaitForChild("Humanoid")
local animator = humanoid:WaitForChild("Animator")

-- Create a new Animation instance and assign an animation asset ID
local kickAnimation = Instance.new("Animation")
kickAnimation.AnimationId = ANIM_ID

-- Load the animation onto the animator
local kickAnimationTrack = animator:LoadAnimation(kickAnimation)

-- Play the animation track after a short delay
task.wait(3)
kickAnimationTrack:Play()

local startTime = tick()
RunService:BindToSimulation(function(deltaTime: number)
	if tick() - startTime > 1 then
		-- Get track by ID and stop its playback
		local kickTrack = animator:GetTrackByAnimationId(ANIM_ID)
		if kickTrack and kickTrack.IsPlaying then
			kickTrack:Stop()
		end
	end
end)
```

### Method: Animator:LoadAnimation

**Signature:** `Animator:LoadAnimation(animation: Animation): AnimationTrack`

This method loads the given [Animation](/docs/reference/engine/classes/Animation.md) onto this `Animator`,
returning a playable [AnimationTrack](/docs/reference/engine/classes/AnimationTrack.md). When called on an `Animator`
within models that the client has network ownership of, for example the
local player's character or from [BasePart:SetNetworkOwner()](/docs/reference/engine/classes/BasePart.md), this
method also loads the animation for the server as well.

Note that the `Animator` must be in the [Workspace](/docs/reference/engine/classes/Workspace.md) before making a
call to `LoadAnimation()` or else it will be unable to retrieve the
[AnimationClipProvider](/docs/reference/engine/classes/AnimationClipProvider.md) service and throw an error.

#### Warning

Do **not** use `LoadAnimation()` in an attempt to retrieve an existing
track. Calling `LoadAnimation()` always creates a **new**
[AnimationTrack](/docs/reference/engine/classes/AnimationTrack.md) instance which may impact game performance if
overused. Instead, use
[GetTrackByAnimationId()](/docs/reference/engine/classes/Animator.md) when you
need to look up a track that was already loaded.

#### Loading an Animation on Client or Server

In order for [AnimationTracks](/docs/reference/engine/classes/AnimationTrack.md) to replicate
correctly, it's important to know when they should be loaded on the client
or on the server:

- If an `Animator` is a descendant of a [Humanoid](/docs/reference/engine/classes/Humanoid.md) or
  [AnimationController](/docs/reference/engine/classes/AnimationController.md) in a player's [Player.Character](/docs/reference/engine/classes/Player.md),
  animations started on that player's client will be replicated to the
  server and other clients.

- If the `Animator` is **not** a descendant of a player character, its
  animations must be loaded and started on the server to replicate.

The `Animator` object must be initially created on the server and
replicated to clients for animation replication to work at all. If an
`Animator` is created locally, then [AnimationTracks](/docs/reference/engine/classes/AnimationTrack.md)
loaded with that `Animator` will not replicate.

*Security: None · Thread Safety: Unsafe · Capabilities: Animation · Simulation Access: true*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `animation` | `Animation` |  | The [Animation](/docs/reference/engine/classes/Animation.md) to be used. |

**Returns:** `AnimationTrack` — A new [AnimationTrack](/docs/reference/engine/classes/AnimationTrack.md) linked to the given [Animation](/docs/reference/engine/classes/Animation.md).

### Method: Animator:StepAnimations

**Signature:** `Animator:StepAnimations(deltaTime: float): ()`

Increments the [AnimationTrack.TimePosition](/docs/reference/engine/classes/AnimationTrack.md) of all playing
[AnimationTracks](/docs/reference/engine/classes/AnimationTrack.md) that are loaded onto the
`Animator`, applying the offsets to the model associated with the
`Animator`. For use in the command bar or by plugins only.

The `deltaTime` parameter determines the number of seconds to increment on
the animation's progress. Typically this method will be called in a loop
to preview the length of an animation (see example).

Note that once animations have stopped playing, the model's joints will
need to be manually reset to their original positions (see example).

#### Access

This method requires Plugin-level security. It can only be called from the
Studio command bar or from a [Plugin](/docs/reference/engine/classes/Plugin.md). Regular [Script](/docs/reference/engine/classes/Script.md) and
[LocalScript](/docs/reference/engine/classes/LocalScript.md) instances cannot call this method.

*Security: None · Thread Safety: Unsafe · Capabilities: Animation, PluginOrOpenCloud*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `deltaTime` | `float` |  | The amount of time in seconds animation playback is to be incremented. by. |

**Returns:** `()`

**Preview Animation in Studio**

This code sample includes a function that can be used to preview an animation
on a character model in Roblox Studio, without needing to run the game.

```lua
local RunService = game:GetService("RunService")

local function previewAnimation(model, animation)
	-- Find the AnimationController and Animator
	local animationController = model:FindFirstChildOfClass("AnimationController")
	local animator = animationController and animationController:FindFirstChildOfClass("Animator")
	if not animator then return end

	-- Load the Animation to create an AnimationTrack
	local track = animationController:LoadAnimation(animation)
	track:Play()

	-- Preview the animation
	local startTime = tick()
	while (tick() - startTime) < track.Length do
		local step = RunService.Heartbeat:wait()
		animator:StepAnimations(step)
	end

	-- Stop the animation
	track:Stop(0)
	animator:StepAnimations(0)

	-- Reset the joints
	for _, descendant in pairs(model:GetDescendants()) do
		if descendant:IsA("Motor6D") then
			local joint = descendant
			joint.CurrentAngle = 0
			joint.Transform = CFrame.new()
		end
	end
end

local character = script.Parent
local animation = Instance.new("Animation")
animation.AnimationId = "rbxassetid://507765644"

previewAnimation(character, animation)
```

## Events

### Event: Animator.AnimationPlayed

**Signature:** `Animator.AnimationPlayed(animationTrack: AnimationTrack)`

Fires for all [AnimationTrack:Play()](/docs/reference/engine/classes/AnimationTrack.md) calls on
[AnimationTracks](/docs/reference/engine/classes/AnimationTrack.md) created and owned by the
`Animator`.

*Security: None · Capabilities: Animation*

**Parameters:**

| Name | Type | Description |
|------|------|-------------|
| `animationTrack` | `AnimationTrack` | The [AnimationTrack](/docs/reference/engine/classes/AnimationTrack.md) that began playing. |

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