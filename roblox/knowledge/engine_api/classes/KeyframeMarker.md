---
name: KeyframeMarker
last_updated: 2026-10-30T19:55:52Z
inherits:
  - Instance
  - Object
type: class
memory_category: Animation
summary: "An instance meant to represent an event that will eventually be fired when a Keyframe is hit."
---

# Class: KeyframeMarker

> An instance meant to represent an event that will eventually be fired when a
> [Keyframe](/docs/reference/engine/classes/Keyframe.md) is hit.

## Description

A KeyframeMarker is an instance meant to represent an event that will
eventually be fired when a [Keyframe](/docs/reference/engine/classes/Keyframe.md) is hit.

## Using a KeyframeMarker

KeyframeMarkers should always be parented to a Keyframe via setting the parent
directly or using the [Keyframe:AddMarker()](/docs/reference/engine/classes/Keyframe.md) function of Keyframe.
KeyframeMarkers can also be removed directly or using the
[Keyframe:RemoveMarker()](/docs/reference/engine/classes/Keyframe.md) function, and polled to check which markers
are attached to a specific Keyframe using [Keyframe:GetMarkers()](/docs/reference/engine/classes/Keyframe.md).

Whenever a Keyframe is detected as an animation is running, there will be an
event fired for each KeyframeMarker that is parented to the Keyframe. These
events are identifiable by the name of the KeyframeMarker. You can retrieve
and listen to these events using the
[AnimationTrack.GetKeyframeMarkerReached](/docs/reference/engine/classes/AnimationTrack.md) function. Optionally, you may
set the [KeyframeMarker.Value](/docs/reference/engine/classes/KeyframeMarker.md) property of the KeyframeMarker in order
to pass along a value with the event being fired.

It inherits the [Keyframe.Name](/docs/reference/engine/classes/Instance.md) property from
[Instance](/docs/reference/engine/classes/Instance.md) and behaves identically. Names are used for identification
and do not need to be unique. When multiple `KeyframeMarker` instances with
the same name are attached to a [Keyframe](/docs/reference/engine/classes/Keyframe.md), events such as the one
returned by [AnimationTrack:GetMarkerReachedSignal()](/docs/reference/engine/classes/AnimationTrack.md) will fire for
every marker.

See also:

- [Keyframe](/docs/reference/engine/classes/Keyframe.md), holds the [Poses](/docs/reference/engine/classes/Pose.md) applied to joints in a
  [Model](/docs/reference/engine/classes/Model.md) at a given point of time in an animation
- [AnimationTrack](/docs/reference/engine/classes/AnimationTrack.md), controls the playback of an animation on a
  [Humanoid](/docs/reference/engine/classes/Humanoid.md) or [AnimationController](/docs/reference/engine/classes/AnimationController.md)
- [Animation](/docs/reference/engine/classes/Animation.md), holds a reference to animation data required to play
  custom animations on characters or other models using the Roblox animation
  system

## Code Samples

**Get Keyframe Markers Attached to a Keyframe**

This example demonstrates the [Keyframe:AddMarker()](/docs/reference/engine/classes/Keyframe.md) and
[Keyframe:GetMarkers()](/docs/reference/engine/classes/Keyframe.md) functions. After adding two markers, _marker1_
and _marker2_ to the keyframe, this example gets and prints the names of the
added markers.

```lua
local keyframe = Instance.new("Keyframe")
keyframe.Parent = workspace

local marker1 = Instance.new("KeyframeMarker")
marker1.Name = "FootStep"
marker1.Value = 100

local marker2 = Instance.new("KeyframeMarker")
marker2.Name = "Wave"
marker2.Value = 100

keyframe:AddMarker(marker1) --marker.Parent = keyframe
keyframe:AddMarker(marker2) --marker.Parent = keyframe

local markers = keyframe:GetMarkers()
for _, marker in pairs(markers) do
	print(marker.Name)
end
```

**Listening to Keyframe Markers**

This `LocalScript` code waits for the local player's `Humanoid` object to
load, then it creates a new `Animation` instance with the proper
[Animation.AnimationId](/docs/reference/engine/classes/Animation.md). The animation is then loaded onto the humanoid,
creating an `AnimationTrack`, and the track is played with
[AnimationTrack:Play()](/docs/reference/engine/classes/AnimationTrack.md). Following that, the
[AnimationTrack:GetMarkerReachedSignal()](/docs/reference/engine/classes/AnimationTrack.md) function detects when the
"KickEnd" marker is hit.

```lua
local Players = game:GetService("Players")

local player = Players.LocalPlayer
local character = player.Character or player.Character:Wait()
local humanoid = character:WaitForChild("Humanoid")

-- Create new "Animation" instance
local kickAnimation = Instance.new("Animation")
-- Set its "AnimationId" to the corresponding animation asset ID
kickAnimation.AnimationId = "rbxassetid://2515090838"

-- Load animation onto the humanoid
local kickAnimationTrack = humanoid:LoadAnimation(kickAnimation)

-- Play animation track
kickAnimationTrack:Play()

-- If a named event was defined for the animation, connect it to "GetMarkerReachedSignal()"
kickAnimationTrack:GetMarkerReachedSignal("KickEnd"):Connect(function(paramString)
	print(paramString)
end)
```

## Properties

### Property: KeyframeMarker.Value

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
  "category": "Data",
  "capabilities": [
    "Animation"
  ]
}
```

A value that is specified for a [KeyframeMarker](/docs/reference/engine/classes/KeyframeMarker.md). Whenever the
signal created from [AnimationTrack:GetMarkerReachedSignal()](/docs/reference/engine/classes/AnimationTrack.md) gets
fired, this value will be passed into the connected function.

See also:

- [Keyframe](/docs/reference/engine/classes/Keyframe.md), holds the [Poses](/docs/reference/engine/classes/Pose.md) applied to joints in a
  [Model](/docs/reference/engine/classes/Model.md) at a given point of time in an animation
- [AnimationTrack](/docs/reference/engine/classes/AnimationTrack.md), controls the playback of an animation on a
  [Humanoid](/docs/reference/engine/classes/Humanoid.md) or [AnimationController](/docs/reference/engine/classes/AnimationController.md)

**Get Keyframe Markers Attached to a Keyframe**

This example demonstrates the [Keyframe:AddMarker()](/docs/reference/engine/classes/Keyframe.md) and
[Keyframe:GetMarkers()](/docs/reference/engine/classes/Keyframe.md) functions. After adding two markers, _marker1_
and _marker2_ to the keyframe, this example gets and prints the names of the
added markers.

```lua
local keyframe = Instance.new("Keyframe")
keyframe.Parent = workspace

local marker1 = Instance.new("KeyframeMarker")
marker1.Name = "FootStep"
marker1.Value = 100

local marker2 = Instance.new("KeyframeMarker")
marker2.Name = "Wave"
marker2.Value = 100

keyframe:AddMarker(marker1) --marker.Parent = keyframe
keyframe:AddMarker(marker2) --marker.Parent = keyframe

local markers = keyframe:GetMarkers()
for _, marker in pairs(markers) do
	print(marker.Name)
end
```

**Add Marker/Remove Marker**

This example demonstrates the [Keyframe:AddMarker()](/docs/reference/engine/classes/Keyframe.md) and
[Keyframe:RemoveMarker()](/docs/reference/engine/classes/Keyframe.md) functions. Note these are functionally
equivalent to [parenting](/docs/reference/engine/classes/Instance.md) and un-parenting the markers.

```lua
local keyframe = Instance.new("Keyframe")
keyframe.Parent = workspace

local marker = Instance.new("KeyframeMarker")
marker.Name = "FootStep"
marker.Value = 100

keyframe:AddMarker(marker) --marker.Parent = keyframe

task.wait(2)

keyframe:RemoveMarker(marker) --marker.Parent = nil
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