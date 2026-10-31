---
name: Pose
last_updated: 2026-10-30T19:55:53Z
inherits:
  - PoseBase
  - Instance
  - Object
type: class
memory_category: Animation
summary: "Holds the CFrame applied to the Motor6D connected to its associated BasePart. The part which is controlled depends on the name of the Pose."
---

# Class: Pose

> Holds the [CFrame](/docs/reference/engine/datatypes/CFrame.md) applied to the [Motor6D](/docs/reference/engine/classes/Motor6D.md) connected to its
> associated [BasePart](/docs/reference/engine/classes/BasePart.md). The part which is controlled depends on the name
> of the Pose.

## Description

A Pose holds the [CFrame](/docs/reference/engine/datatypes/CFrame.md) applied to the [Motor6D](/docs/reference/engine/classes/Motor6D.md) connected to
its associated [BasePart](/docs/reference/engine/classes/BasePart.md). The part which is controlled depends on the
name of the Pose.

Poses are the fundamental building blocks of animations and, with `Keyframes`,
make up `KeyframeSequences`.

## Poses, joints and hierarchy

Although a Pose is assigned to a [BasePart](/docs/reference/engine/classes/BasePart.md) by name, the object
manipulated during animation playback is actually the [Motor6D](/docs/reference/engine/classes/Motor6D.md)
connected to this part. Animation rigs branch out from the model's root part
through such joints.

In an
[R15 character rig](/docs/en-us/avatar/character-bodies/specifications.md#rigging),
the root part is the HumanoidRootPart. The LowerTorso is connected to the
HumanoidRootPart by the a motor named 'Root'. Therefore, the [CFrame](/docs/reference/engine/datatypes/CFrame.md)
of a Pose named 'LowerTorso' in a [Keyframe](/docs/reference/engine/classes/Keyframe.md) would be applied to the
motor named 'Root', and not the LowerTorso itself.

Poses are arranged in a [Keyframe](/docs/reference/engine/classes/Keyframe.md) based on joint hierarchy. This means,
the Pose's [CFrame](/docs/reference/engine/datatypes/CFrame.md) is applied to the motor connecting the part
associated with the pose to the part associated with the pose's parent. See
below for a visual example of the structure of Poses on a R15 character.

## Pose CFrame

The Roblox animation system applies [Pose.CFrame](/docs/reference/engine/classes/Pose.md) to the corresponding
[Motor6D](/docs/reference/engine/classes/Motor6D.md) by manipulating the relative transformation of the motor, the
[Motor6D.Transform](/docs/reference/engine/classes/Motor6D.md) property. The original [C0](/docs/reference/engine/classes/JointInstance.md)
and [C1](/docs/reference/engine/classes/JointInstance.md) values are not changed.

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

## Properties

### Property: Pose.CFrame

```json
{
  "type": "CFrame",
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

This [CFrame](/docs/reference/engine/datatypes/CFrame.md) applies to the [Motor6D](/docs/reference/engine/classes/Motor6D.md) corresponding with
the [Pose](/docs/reference/engine/classes/Pose.md) when the [Motor6D.Transform](/docs/reference/engine/classes/Motor6D.md) is changed. The
original [Motor6D.C0](/docs/reference/engine/classes/Motor6D.md) and [Motor6D.C1](/docs/reference/engine/classes/Motor6D.md) values are not changed.

[Pose](/docs/reference/engine/classes/Pose.md) objects are arranged in a [Keyframe](/docs/reference/engine/classes/Keyframe.md) based on joint
hierarchy. This means, that the [Pose.CFrame](/docs/reference/engine/classes/Pose.md) is applied to the
motor connecting the part associated with the pose to the part associated
with the pose's parent.

### Property: Pose.MaskWeight

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
    "Animation"
  ]
}
```

> **Deprecated:** This property is deprecated. Use the [AnimationTrack:AdjustWeight()](/docs/reference/engine/classes/AnimationTrack.md) function when blending multiple animations.

## Methods

### Method: Pose:AddSubPose

**Signature:** `Pose:AddSubPose(pose: Instance): ()`

Adds a sub [Pose](/docs/reference/engine/classes/Pose.md) to the [Pose](/docs/reference/engine/classes/Pose.md) by parenting it to it. It is
functionally identical to setting the new pose's [Instance.Parent](/docs/reference/engine/classes/Instance.md)
to the pose.

Note, this function will not error when an instance other than a
[Pose](/docs/reference/engine/classes/Pose.md) is given as the pose parameter and will parent it
successfully.

*Security: None · Thread Safety: Unsafe · Capabilities: Animation*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `pose` | `Instance` |  | The [Pose](/docs/reference/engine/classes/Pose.md) to be added. |

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

### Method: Pose:GetSubPoses

**Signature:** `Pose:GetSubPoses(): Instances`

Returns an array containing all sub [Poses](/docs/reference/engine/classes/Pose.md) that have been
added to a [Pose](/docs/reference/engine/classes/Pose.md). This is functionally the same as using the
[Instance:GetChildren()](/docs/reference/engine/classes/Instance.md) function on the [Pose](/docs/reference/engine/classes/Pose.md).

Note: this function returns all children of the [Pose](/docs/reference/engine/classes/Pose.md), including
non [Pose](/docs/reference/engine/classes/Pose.md) [Instances](/docs/reference/engine/classes/Instance.md) if any are present.

*Security: None · Thread Safety: Unsafe · Capabilities: Animation*

**Returns:** `Instances` — An array of sub [Poses](/docs/reference/engine/classes/Pose.md).

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

### Method: Pose:RemoveSubPose

**Signature:** `Pose:RemoveSubPose(pose: Instance): ()`

Removes a sub [Pose](/docs/reference/engine/classes/Pose.md) from the [Pose](/docs/reference/engine/classes/Pose.md) by parenting it to `nil`.
This is functionally identical to setting the new pose's
[Instance.Parent](/docs/reference/engine/classes/Instance.md) to `nil`.

Note: If an [Instance](/docs/reference/engine/classes/Instance.md) other than [Pose](/docs/reference/engine/classes/Pose.md) is used as a
[Pose](/docs/reference/engine/classes/Pose.md) parameter, this function removes that [Instance](/docs/reference/engine/classes/Instance.md) and
does not provide an error.

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

### From [PoseBase](/docs/reference/engine/classes/PoseBase.md)

- **Property `EasingDirection`** (`PoseEasingDirection`): The easing direction to use to reach the next Pose's value.
- **Property `EasingStyle`** (`PoseEasingStyle`): The easing style to use to reach the next Pose's value.
- **Property `Weight`** (`float`): 

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