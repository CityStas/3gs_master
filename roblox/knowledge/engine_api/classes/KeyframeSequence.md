---
name: KeyframeSequence
last_updated: 2026-10-30T19:55:52Z
inherits:
  - AnimationClip
  - Instance
  - Object
type: class
memory_category: Animation
summary: "This object stores all of the Keyframes and other data for the animation."
---

# Class: KeyframeSequence

> This object stores all of the [Keyframes](/docs/reference/engine/classes/Keyframe.md) and other data for
> the animation.

## Description

[KeyframeSequence](/docs/reference/engine/classes/KeyframeSequence.md) stores all the [Keyframes](/docs/reference/engine/classes/Keyframe.md) for an
[Animation](/docs/reference/engine/classes/Animation.md), determines if the animation will
[Loop](/docs/reference/engine/classes/KeyframeSequence.md), and determines its
[Priority](/docs/reference/engine/classes/KeyframeSequence.md) against other animations. The last
[Keyframe](/docs/reference/engine/classes/Keyframe.md) in the sequence, meaning the [Keyframe](/docs/reference/engine/classes/Keyframe.md) with the
highest [Time](/docs/reference/engine/classes/Keyframe.md) property, determines the length of an
animation.

Although [Priority](/docs/reference/engine/classes/KeyframeSequence.md) and
[Loop](/docs/reference/engine/classes/KeyframeSequence.md) save the priority and looped animation
settings for the sequence, note that [AnimationTrack](/docs/reference/engine/classes/AnimationTrack.md) properties can
eventually overwrite these properties at playback time.

If you want to preview an [Animation](/docs/reference/engine/classes/Animation.md) before uploading it to Roblox, you
can generate a temporary hash ID using
[KeyframeSequenceProvider:RegisterKeyframeSequence()](/docs/reference/engine/classes/KeyframeSequenceProvider.md) for localized
animation testing.

#### Obtaining Sequences

In some cases you may wish to download the [KeyframeSequence](/docs/reference/engine/classes/KeyframeSequence.md)
corresponding to an existing uploaded [Animation](/docs/reference/engine/classes/Animation.md). You can use
[AnimationClipProvider:GetAnimationClipAsync()](/docs/reference/engine/classes/AnimationClipProvider.md) to download an
animation.

## Code Samples

**Get KeyframeSequence Length**

This sample contains a simple function that will get the length of a
KeyframeSequence by finding the Keyframe with the highest Keyframe.Time value.

```lua
local function getSequenceLength(keyframeSequence)
	local length = 0
	for _, keyframe in pairs(keyframeSequence:GetKeyframes()) do
		if keyframe.Time > length then
			length = keyframe.Time
		end
	end
	return length
end

local keyframeSequence = Instance.new("KeyframeSequence")

getSequenceLength(keyframeSequence)
```

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

## Properties

### Property: KeyframeSequence.AuthoredHipHeight *(hidden)*

```json
{
  "type": "float",
  "access": "ReadOnly",
  "security": {
    "read": "PluginSecurity",
    "write": "PluginSecurity"
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

Contains the hip height of the [Humanoid](/docs/reference/engine/classes/Humanoid.md) of the model that was used
to author this [KeyframeSequence](/docs/reference/engine/classes/KeyframeSequence.md). Default value is `1.35` since
that is the hip height set for a standard R15 character.

## Methods

### Method: KeyframeSequence:AddKeyframe

**Signature:** `KeyframeSequence:AddKeyframe(keyframe: Instance): ()`

This method adds a [Keyframe](/docs/reference/engine/classes/Keyframe.md) to the [KeyframeSequence](/docs/reference/engine/classes/KeyframeSequence.md) by
parenting it to the [KeyframeSequence](/docs/reference/engine/classes/KeyframeSequence.md). It is functionally identical
to setting the keyframe's [Instance.Parent](/docs/reference/engine/classes/Instance.md) to the
[KeyframeSequence](/docs/reference/engine/classes/KeyframeSequence.md).

Note that this method will not error when called with an instance other
than a [Keyframe](/docs/reference/engine/classes/Keyframe.md) as the `keyframe` parameter and will parent it
successfully.

*Security: None · Thread Safety: Unsafe · Capabilities: Animation*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `keyframe` | `Instance` |  | The [Keyframe](/docs/reference/engine/classes/Keyframe.md) to be added. |

**Returns:** `()`

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

### Method: KeyframeSequence:GetKeyframes

**Signature:** `KeyframeSequence:GetKeyframes(): List<Keyframe>`

This method returns an array that contains all [Keyframes](/docs/reference/engine/classes/Keyframe.md)
that have been added to a [KeyframeSequence](/docs/reference/engine/classes/KeyframeSequence.md).

*Security: None · Thread Safety: Unsafe · Capabilities: Animation*

**Returns:** `List<Keyframe>` — An array of [Keyframes](/docs/reference/engine/classes/Keyframe.md).

**Get KeyframeSequence Length**

This sample contains a simple function that will get the length of a
KeyframeSequence by finding the Keyframe with the highest Keyframe.Time value.

```lua
local function getSequenceLength(keyframeSequence)
	local length = 0
	for _, keyframe in pairs(keyframeSequence:GetKeyframes()) do
		if keyframe.Time > length then
			length = keyframe.Time
		end
	end
	return length
end

local keyframeSequence = Instance.new("KeyframeSequence")

getSequenceLength(keyframeSequence)
```

### Method: KeyframeSequence:RemoveKeyframe

**Signature:** `KeyframeSequence:RemoveKeyframe(keyframe: Instance): ()`

This method removes a [Keyframe](/docs/reference/engine/classes/Keyframe.md) from the [KeyframeSequence](/docs/reference/engine/classes/KeyframeSequence.md)
by setting its parent to `nil`. It is functionally identical to setting
the keyframe's parent to `nil`.

Note that while this sets the keyframe's parent to `nil`, it does not
destroy it. Provided another reference to the keyframe remains, it can be
re-parented later.

Also note that this method will not error when called with an
[Instance](/docs/reference/engine/classes/Instance.md) other than a [Keyframe](/docs/reference/engine/classes/Keyframe.md) as the keyframe parameter.

*Security: None · Thread Safety: Unsafe · Capabilities: Animation*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `keyframe` | `Instance` |  | The [Keyframe](/docs/reference/engine/classes/Keyframe.md) to be removed. |

**Returns:** `()`

**KeyframeSequence RemoveKeyframe**

This sample adds a [Keyframe](/docs/reference/engine/classes/Keyframe.md) to a [KeyframeSequence](/docs/reference/engine/classes/KeyframeSequence.md) before
removing it and adding it again. Note that once a [Keyframe](/docs/reference/engine/classes/Keyframe.md) is removed,
it is not destroyed, meaning it can be re-added later.

```lua
local keyframeSequence = Instance.new("KeyframeSequence")
keyframeSequence.Parent = workspace

local keyframe = Instance.new("Keyframe")

keyframeSequence:AddKeyframe(keyframe)

task.wait(2)

keyframeSequence:RemoveKeyframe(keyframe)
```

## Inherited Members

### From [AnimationClip](/docs/reference/engine/classes/AnimationClip.md)

- **Property `Length`** (`float`): The length in seconds of this clip. Returns `0` until the animation has
- **Property `Loop`** (`boolean`): Determines whether the animation stored in this AnimationClip is
- **Property `Priority`** (`AnimationPriority`): Determines which clip takes priority when multiple animations are playing

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