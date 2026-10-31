---
name: Keyframe
last_updated: 2026-10-30T19:55:52Z
inherits:
  - Instance
  - Object
type: class
memory_category: Animation
summary: "A Keyframe holds the Poses applied to joints in a Model at a given point of time in an animation. Keyframes are interpolated between during animation playback."
---

# Class: Keyframe

> A Keyframe holds the [Poses](/docs/reference/engine/classes/Pose.md) applied to joints in a [Model](/docs/reference/engine/classes/Model.md)
> at a given point of time in an animation. [Keyframes](/docs/reference/engine/classes/Keyframe.md) are
> interpolated between during animation playback.

## Description

A Keyframe holds the [Poses](/docs/reference/engine/classes/Pose.md) applied to joints in a [Model](/docs/reference/engine/classes/Model.md)
at a given point of time in an animation. [Keyframes](/docs/reference/engine/classes/Keyframe.md) are
interpolated between during animation playback.

Note, in most cases developers do not need to manipulate
[KeyframeSequences](/docs/reference/engine/classes/KeyframeSequence.md) as the animation editor covers most
animation functionality. However, in some cases a developer may wish to
generate an animation from a [Script](/docs/reference/engine/classes/Script.md) or build their own plugin.

## Structure

Keyframes are held within a [KeyframeSequence](/docs/reference/engine/classes/KeyframeSequence.md) and contain [Pose](/docs/reference/engine/classes/Pose.md)
objects. The poses are named in accordance with the [BaseParts](/docs/reference/engine/classes/BasePart.md)
they correspond to and are structured in terms of joint hierarchy. This means
each [Pose](/docs/reference/engine/classes/Pose.md) is parented to the [Pose](/docs/reference/engine/classes/Pose.md) corresponding to the part it
is attached to.

Note, as [Poses](/docs/reference/engine/classes/Pose.md) are named in accordance with the
[BaseParts](/docs/reference/engine/classes/BasePart.md) they correspond to, animations require distinct
part names to play correctly.

## Interpolation

During animation playback the poses in different keyframes are interpolated
between. This allows a smooth animation to be created without needing to
define every frame. Note, the style of interpolation is determined in the
[Pose](/docs/reference/engine/classes/Pose.md) object. The Keyframe object merely holds the [Poses](/docs/reference/engine/classes/Pose.md)
at a defined point of time in the animation ([Keyframe.Time](/docs/reference/engine/classes/Keyframe.md)).

## Code Samples

**Keyframe Generate Poses**

This sample includes a function that will generate a 'blank' keyframe
containing blank poses for all of the model's connected parts in the correct
hierarchical order.

```lua
local function generateKeyframe(model)
	if not model.PrimaryPart then
		warn("No primary part set")
		return
	end

	local rootPart = model.PrimaryPart:GetRootPart()

	if not rootPart then
		warn("Root part not found")
		return
	end

	local partsAdded = {}
	partsAdded[rootPart] = true

	local function addPoses(part, parentPose)
		-- get all of the joints attached to the part
		for _, joint in pairs(part:GetJoints()) do
			-- we're only interested in Motor6Ds
			if joint:IsA("Motor6D") then
				-- find the connected part
				local connectedPart = nil
				if joint.Part0 == part then
					connectedPart = joint.Part1
				elseif joint.Part1 == part then
					connectedPart = joint.Part0
				end
				if connectedPart then
					-- make sure we haven't already added this part
					if not partsAdded[connectedPart] then
						partsAdded[connectedPart] = true
						-- create a pose
						local pose = Instance.new("Pose")
						pose.Name = connectedPart.Name
						parentPose:AddSubPose(pose)
						-- recurse
						addPoses(connectedPart, pose)
					end
				end
			end
		end
	end

	local keyframe = Instance.new("Keyframe")

	-- populate the keyframe
	local rootPose = Instance.new("Pose")
	rootPose.Name = rootPart.Name
	addPoses(rootPart, rootPose)
	keyframe:AddPose(rootPose)

	return keyframe
end

local character = script.Parent

local keyframe = generateKeyframe(character)

print(keyframe)
```

## Properties

### Property: Keyframe.Time

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
    "Animation"
  ]
}
```

This property gives the [Keyframe](/docs/reference/engine/classes/Keyframe.md) time position (in seconds) in an
animation. This determines the time at which the [Poses](/docs/reference/engine/classes/Pose.md) inside
the keyframe will be shown.

Note the [Keyframe](/docs/reference/engine/classes/Keyframe.md) with the highest time value in a
[KeyframeSequence](/docs/reference/engine/classes/KeyframeSequence.md) is used to determine the length of the animation.

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

## Methods

### Method: Keyframe:AddMarker

**Signature:** `Keyframe:AddMarker(marker: Instance): ()`

This function adds a [KeyframeMarker](/docs/reference/engine/classes/KeyframeMarker.md) to the [Keyframe](/docs/reference/engine/classes/Keyframe.md) by
parenting it to the keyframe. It is functionally identical to setting the
marker's [Instance.Parent](/docs/reference/engine/classes/Instance.md) to the Keyframe.

Note, this function will not error when an instance other than a
KeyframeMarker is given as the parameter and will parent it successfully.

#### More about Keyframes

[Keyframe](/docs/reference/engine/classes/Keyframe.md) names do not need to be unique. For example, if an
Animation has three keyframes named "Particles" the connected event
returned by [AnimationTrack:GetMarkerReachedSignal()](/docs/reference/engine/classes/AnimationTrack.md) will fire each
time one of these keyframes is reached.

[Keyframe](/docs/reference/engine/classes/Keyframe.md) names can be set in the Roblox Animation Editor when
creating or editing an animation. They cannot however be set by a
[Script](/docs/reference/engine/classes/Script.md) on an existing animation prior to playing it.

See also:

- [Keyframe:RemoveMarker()](/docs/reference/engine/classes/Keyframe.md)
- [Keyframe:GetMarkers()](/docs/reference/engine/classes/Keyframe.md)
- [AnimationTrack:GetMarkerReachedSignal()](/docs/reference/engine/classes/AnimationTrack.md)

*Security: None · Thread Safety: Unsafe · Capabilities: Animation*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `marker` | `Instance` |  | The [KeyframeMarker](/docs/reference/engine/classes/KeyframeMarker.md) being parented to the [Keyframe](/docs/reference/engine/classes/Keyframe.md). |

**Returns:** `()`

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

### Method: Keyframe:AddPose

**Signature:** `Keyframe:AddPose(pose: Instance): ()`

This function adds a [Pose](/docs/reference/engine/classes/Pose.md) to the [Keyframe](/docs/reference/engine/classes/Keyframe.md) by parenting it
to the keyframe. It is functionally identical to setting the pose's
[Instance.Parent](/docs/reference/engine/classes/Instance.md) to the keyframe.

Note, this function will not error when an instance other than a
[Pose](/docs/reference/engine/classes/Pose.md) is given as the pose parameter and will parent it
successfully.

*Security: None · Thread Safety: Unsafe · Capabilities: Animation*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `pose` | `Instance` |  | The [Pose](/docs/reference/engine/classes/Pose.md) to be added. |

**Returns:** `()`

**Keyframe Generate Poses**

This sample includes a function that will generate a 'blank' keyframe
containing blank poses for all of the model's connected parts in the correct
hierarchical order.

```lua
local function generateKeyframe(model)
	if not model.PrimaryPart then
		warn("No primary part set")
		return
	end

	local rootPart = model.PrimaryPart:GetRootPart()

	if not rootPart then
		warn("Root part not found")
		return
	end

	local partsAdded = {}
	partsAdded[rootPart] = true

	local function addPoses(part, parentPose)
		-- get all of the joints attached to the part
		for _, joint in pairs(part:GetJoints()) do
			-- we're only interested in Motor6Ds
			if joint:IsA("Motor6D") then
				-- find the connected part
				local connectedPart = nil
				if joint.Part0 == part then
					connectedPart = joint.Part1
				elseif joint.Part1 == part then
					connectedPart = joint.Part0
				end
				if connectedPart then
					-- make sure we haven't already added this part
					if not partsAdded[connectedPart] then
						partsAdded[connectedPart] = true
						-- create a pose
						local pose = Instance.new("Pose")
						pose.Name = connectedPart.Name
						parentPose:AddSubPose(pose)
						-- recurse
						addPoses(connectedPart, pose)
					end
				end
			end
		end
	end

	local keyframe = Instance.new("Keyframe")

	-- populate the keyframe
	local rootPose = Instance.new("Pose")
	rootPose.Name = rootPart.Name
	addPoses(rootPart, rootPose)
	keyframe:AddPose(rootPose)

	return keyframe
end

local character = script.Parent

local keyframe = generateKeyframe(character)

print(keyframe)
```

**Keyframe Add/Remove Pose**

This sample demonstrates quickly the Keyframe.AddPose, Keyframe.RemovePose and
Pose.AddSubPose and Pose.RemoveSubPose functions. Note these are functionally
equivalent to parenting and un-parenting the poses.

```lua
local keyframe = Instance.new("Keyframe")
keyframe.Parent = workspace

local pose = Instance.new("Pose")
pose.EasingStyle = Enum.PoseEasingStyle.Cubic
pose.EasingDirection = Enum.PoseEasingDirection.Out

local pose2 = Instance.new("Pose")
pose2.EasingStyle = Enum.PoseEasingStyle.Cubic
pose2.EasingDirection = Enum.PoseEasingDirection.Out

keyframe:AddPose(pose) -- pose.Parent = keyframe

task.wait(2)

keyframe:RemovePose(pose) -- pose.Parent = nil

task.wait(2)

keyframe:AddPose(pose) -- pose.Parent = keyframe

task.wait(2)

pose:AddSubPose(pose2) -- pose2.Parent = pose

task.wait(2)

pose:RemoveSubPose(pose2) -- pose2.Parent = nil
```

### Method: Keyframe:GetMarkers

**Signature:** `Keyframe:GetMarkers(): List<KeyframeMarker>`

This function returns an array containing all
[KeyframeMarkers](/docs/reference/engine/classes/KeyframeMarker.md) that have been added to the
[Keyframe](/docs/reference/engine/classes/Keyframe.md). Note, this function will only return
[instances](/docs/reference/engine/classes/Instance.md) of type KeyframeMarker.

#### More about Keyframes

[Keyframe](/docs/reference/engine/classes/Keyframe.md) names do not need to be unique. For example, if an
Animation has three keyframes named "Particles" the connected event
returned by [AnimationTrack:GetMarkerReachedSignal()](/docs/reference/engine/classes/AnimationTrack.md) will fire each
time one of these keyframes is reached.

[Keyframe](/docs/reference/engine/classes/Keyframe.md) names can be set in the Roblox Animation Editor when
creating or editing an animation. They cannot however be set by a
[Script](/docs/reference/engine/classes/Script.md) on an existing animation prior to playing it.

See also:

- [Keyframe:AddMarker()](/docs/reference/engine/classes/Keyframe.md)
- [Keyframe:RemoveMarker()](/docs/reference/engine/classes/Keyframe.md)
- [AnimationTrack:GetMarkerReachedSignal()](/docs/reference/engine/classes/AnimationTrack.md)

*Security: None · Thread Safety: Unsafe · Capabilities: Animation*

**Returns:** `List<KeyframeMarker>` — An array containing all [KeyframeMarkers](/docs/reference/engine/classes/KeyframeMarker.md) that
have been added to the [Keyframe](/docs/reference/engine/classes/Keyframe.md).

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

### Method: Keyframe:GetPoses

**Signature:** `Keyframe:GetPoses(): List<Pose>`

This function returns an array containing all [Poses](/docs/reference/engine/classes/Pose.md) that have
been added to a [Keyframe](/docs/reference/engine/classes/Keyframe.md).

*Security: None · Thread Safety: Unsafe · Capabilities: Animation*

**Returns:** `List<Pose>` — An array of [Poses](/docs/reference/engine/classes/Pose.md).

**Keyframe Reset Poses**

This code sample includes a function to reset the CFrame of the Poses in a
Keyframe.

```lua
local function resetPoses(parent)
	-- both functions are equivalent to GetChildren
	local poses = parent:IsA("Keyframe") and parent:GetPoses() or parent:IsA("Pose") and parent:GetSubPoses()

	for _, pose in pairs(poses) do
		if pose:IsA("Pose") then
			pose.CFrame = CFrame.new()
			-- recurse
			resetPoses(pose)
		end
	end
end
```

### Method: Keyframe:RemoveMarker

**Signature:** `Keyframe:RemoveMarker(marker: Instance): ()`

This function removes a [KeyframeMarker](/docs/reference/engine/classes/KeyframeMarker.md) from the [Keyframe](/docs/reference/engine/classes/Keyframe.md)
by settings its [Instance.Parent](/docs/reference/engine/classes/Instance.md) to `nil`.

The KeyframeMarker's [Instance.Parent](/docs/reference/engine/classes/Instance.md) is set to `nil` but it is not
destroyed. This means, provided the marker is referenced it can be
re-parented later.

Note, this function will not error when an instance other than a
KeyframeMarker is given as the parameter.

#### More about Keyframes

[Keyframe](/docs/reference/engine/classes/Keyframe.md) names do not need to be unique. For example, if an
Animation has three keyframes named "Particles" the connected event
returned by [AnimationTrack:GetMarkerReachedSignal()](/docs/reference/engine/classes/AnimationTrack.md) will fire each
time one of these keyframes is reached.

[Keyframe](/docs/reference/engine/classes/Keyframe.md) names can be set in the Roblox Animation Editor when
creating or editing an animation. They cannot however be set by a
[Script](/docs/reference/engine/classes/Script.md) on an existing animation prior to playing it.

See also:

- [Keyframe:AddMarker()](/docs/reference/engine/classes/Keyframe.md)
- [Keyframe:GetMarkers()](/docs/reference/engine/classes/Keyframe.md)
- [AnimationTrack:GetMarkerReachedSignal()](/docs/reference/engine/classes/AnimationTrack.md)

*Security: None · Thread Safety: Unsafe · Capabilities: Animation*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `marker` | `Instance` |  | The marker being removed from the [Keyframe](/docs/reference/engine/classes/Keyframe.md). |

**Returns:** `()`

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

### Method: Keyframe:RemovePose

**Signature:** `Keyframe:RemovePose(pose: Instance): ()`

This function removes a [Pose](/docs/reference/engine/classes/Pose.md) from the [Keyframe](/docs/reference/engine/classes/Keyframe.md) by setting
its [Instance.Parent](/docs/reference/engine/classes/Instance.md) to `nil` without destroying it. This means the
provided the pose is referenced and it can be re-parented later.

Note, this function will not error when an instance other than a
[Pose](/docs/reference/engine/classes/Pose.md) is given as the pose parameter.

*Security: None · Thread Safety: Unsafe · Capabilities: Animation*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `pose` | `Instance` |  | The [Pose](/docs/reference/engine/classes/Pose.md) to be removed. |

**Returns:** `()`

**Keyframe Add/Remove Pose**

This sample demonstrates quickly the Keyframe.AddPose, Keyframe.RemovePose and
Pose.AddSubPose and Pose.RemoveSubPose functions. Note these are functionally
equivalent to parenting and un-parenting the poses.

```lua
local keyframe = Instance.new("Keyframe")
keyframe.Parent = workspace

local pose = Instance.new("Pose")
pose.EasingStyle = Enum.PoseEasingStyle.Cubic
pose.EasingDirection = Enum.PoseEasingDirection.Out

local pose2 = Instance.new("Pose")
pose2.EasingStyle = Enum.PoseEasingStyle.Cubic
pose2.EasingDirection = Enum.PoseEasingDirection.Out

keyframe:AddPose(pose) -- pose.Parent = keyframe

task.wait(2)

keyframe:RemovePose(pose) -- pose.Parent = nil

task.wait(2)

keyframe:AddPose(pose) -- pose.Parent = keyframe

task.wait(2)

pose:AddSubPose(pose2) -- pose2.Parent = pose

task.wait(2)

pose:RemoveSubPose(pose2) -- pose2.Parent = nil
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