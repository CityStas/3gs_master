---
name: AnimationClip
last_updated: 2026-10-30T19:55:51Z
inherits:
  - Instance
  - Object
type: class
memory_category: Instances
tags:
  - NotCreatable
summary: "Represents all types of animation data that the Roblox animation system can consume."
---

# Class: AnimationClip

> Represents all types of animation data that the Roblox animation system can
> consume.

## Description

The non-creatable [AnimationClip](/docs/reference/engine/classes/AnimationClip.md) instance type represents abstract
animation data that can be fed to the Roblox animation system.
[KeyframeSequence](/docs/reference/engine/classes/KeyframeSequence.md) and [CurveAnimation](/docs/reference/engine/classes/CurveAnimation.md) are two current instance
types that inherit from [AnimationClip](/docs/reference/engine/classes/AnimationClip.md).

There are different ways to represent animation data. To simplify the use of
Roblox's animation system, all such representations are their own instance
types but inherit from the [AnimationClip](/docs/reference/engine/classes/AnimationClip.md) instance. Animation clips
published to Roblox via the [Animation Editor](/docs/en-us/animation/editor.md)
can be loaded into the Roblox Engine using an [Animation](/docs/reference/engine/classes/Animation.md) instance.

## Properties

### Property: AnimationClip.Length

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
    "can_save": true
  },
  "thread_safety": "ReadSafe",
  "category": "Data",
  "capabilities": [
    "Animation"
  ]
}
```

The read-only length, in seconds, of this [AnimationClip](/docs/reference/engine/classes/AnimationClip.md), computed
from the timing of the underlying animation data (its keyframes or
curves).

Because a clip's animation data may still be downloading when the property
is first accessed, `Length` returns `0` until the animation has fully
loaded. Poll for a non-zero value if you need the duration right away.

[AnimationTrack](/docs/reference/engine/classes/AnimationTrack.md) instances load an [AnimationClip](/docs/reference/engine/classes/AnimationClip.md) when an
[Animation](/docs/reference/engine/classes/Animation.md) is requested via its
[AnimationId](/docs/reference/engine/classes/Animation.md), and
[AnimationTrack.Length](/docs/reference/engine/classes/AnimationTrack.md) reflects the underlying
[AnimationClip](/docs/reference/engine/classes/AnimationClip.md) value.

### Property: AnimationClip.Loop

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
    "Animation"
  ]
}
```

Determines whether the animation stored in this [AnimationClip](/docs/reference/engine/classes/AnimationClip.md) is
intended to loop. When set to true, the animation will continuously repeat
each time it finishes.

Note that [AnimationTrack](/docs/reference/engine/classes/AnimationTrack.md) instances internally load an
[AnimationClip](/docs/reference/engine/classes/AnimationClip.md) when an [Animation](/docs/reference/engine/classes/Animation.md) is requested via its
[AnimationId](/docs/reference/engine/classes/Animation.md), and the
[AnimationTrack.Looped](/docs/reference/engine/classes/AnimationTrack.md) property will default to the original
[AnimationClip](/docs/reference/engine/classes/AnimationClip.md) value. Note also that this value can be overwritten.

### Property: AnimationClip.Priority

```json
{
  "type": "AnimationPriority",
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

Determines which clip takes priority when multiple animations are playing
simultaneously. Multiple playing animations look to this property to
figure out which [Keyframe](/docs/reference/engine/classes/Keyframe.md) poses should be played over one another.

Note that [AnimationTrack](/docs/reference/engine/classes/AnimationTrack.md) instances internally load an
[AnimationClip](/docs/reference/engine/classes/AnimationClip.md) when an [Animation](/docs/reference/engine/classes/Animation.md) is requested via its
[AnimationId](/docs/reference/engine/classes/Animation.md), and the
[AnimationTrack.Priority](/docs/reference/engine/classes/AnimationTrack.md) property will default to the original
[AnimationClip](/docs/reference/engine/classes/AnimationClip.md) value. Note also that this value can be overwritten.

**KeyframeSequence Instantiation**

This sample demonstrates how a basic [KeyframeSequence](/docs/reference/engine/classes/KeyframeSequence.md) can be created.

```lua
-- Create the sequence
local keyframeSequence = Instance.new("KeyframeSequence")
keyframeSequence.Loop = false
keyframeSequence.Priority = Enum.AnimationPriority.Action

--  Create a keyframe
local keyframe = Instance.new("Keyframe")
keyframe.Time = 0

-- Create sample poses
local rootPose = Instance.new("Pose")
rootPose.Name = "HumanoidRootPart"
rootPose.Weight = 0
local lowerTorsoPose = Instance.new("Pose")
lowerTorsoPose.Name = "LowerTorso"
lowerTorsoPose.Weight = 1

-- Set the sequence hierarchy
rootPose:AddSubPose(lowerTorsoPose)
keyframe:AddPose(rootPose)
keyframeSequence:AddKeyframe(keyframe)

-- Parent the sequence
keyframeSequence.Parent = workspace
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