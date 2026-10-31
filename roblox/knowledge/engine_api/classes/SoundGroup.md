---
name: SoundGroup
last_updated: 2026-10-30T19:55:53Z
inherits:
  - Instance
  - Object
type: class
memory_category: Internal
summary: "A SoundGroup is used to manage the volume and sound effects on multiple Sounds at once. Sounds in the SoundGroup will have their volume and effects adjusted by the SoundGroup."
---

# Class: SoundGroup

> A [SoundGroup](/docs/reference/engine/classes/SoundGroup.md) is used to manage the volume and sound effects on
> multiple [Sounds](/docs/reference/engine/classes/Sound.md) at once. [Sounds](/docs/reference/engine/classes/Sound.md) in the SoundGroup
> will have their volume and effects adjusted by the SoundGroup.

## Description

A [SoundGroup](/docs/reference/engine/classes/SoundGroup.md) is used to manage the volume and effects on multiple
[Sounds](/docs/reference/engine/classes/Sound.md) at once. Every sound in the sound group will have its
volume adjusted by the group's [Volume](/docs/reference/engine/classes/SoundGroup.md) property which
acts as a multiplier, meaning a [Sound](/docs/reference/engine/classes/Sound.md) with volume `0.5` assigned to a
[SoundGroup](/docs/reference/engine/classes/SoundGroup.md) with a volume of `0.5` will have an effective volume of
`0.25`.

If the [SoundGroup](/docs/reference/engine/classes/SoundGroup.md) has any [SoundEffects](/docs/reference/engine/classes/SoundEffect.md) as
children, those effects will be applied to all of the [Sounds](/docs/reference/engine/classes/Sound.md) in
the group.

Note that a [Sound](/docs/reference/engine/classes/Sound.md) must be added to a [SoundGroup](/docs/reference/engine/classes/SoundGroup.md) by setting its
[SoundGroup](/docs/reference/engine/classes/Sound.md) property, not by simply parenting the
[Sound](/docs/reference/engine/classes/Sound.md) to the [SoundGroup](/docs/reference/engine/classes/SoundGroup.md). A [Sound](/docs/reference/engine/classes/Sound.md) can only belong to
one [SoundGroup](/docs/reference/engine/classes/SoundGroup.md) at a time, although you can nest groups as outlined
[here](/docs/en-us/sound/groups.md#nesting-soundgroups).

See [Sound Groups](/docs/en-us/sound/groups.md) for further details on working
with the [SoundGroup](/docs/reference/engine/classes/SoundGroup.md) class.

## Properties

### Property: SoundGroup.Volume

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
  "category": "State",
  "capabilities": [
    "LegacySound"
  ]
}
```

The volume multiplier applied to [Sounds](/docs/reference/engine/classes/Sound.md) which belong to the
[SoundGroup](/docs/reference/engine/classes/SoundGroup.md). Value can range from `0` to `10`.

**SoundGroups**

This sample demonstrates how a SoundGroup can be used to change the volume of
its associated Sounds and apply SoundEffects.

In this example a Sound is instanced in the Workspace and assigned to a new
SoundGroup. The Sound is played and during playback the volume is changed via
the SoundGroup and a SoundEffect is added.

```lua
local SoundService = game:GetService("SoundService")

-- create a sound group
local soundGroup = Instance.new("SoundGroup")
soundGroup.Parent = SoundService

-- create a sound
local sound = Instance.new("Sound")
sound.SoundId = "rbxassetid://9120386436"
sound.Looped = true
sound.PlaybackSpeed = 2
sound.SoundGroup = soundGroup
sound.Parent = workspace

-- play the sound
sound:Play()

task.wait(10)

-- change the volume
soundGroup.Volume = 0.1

task.wait(3)

-- return the volume
soundGroup.Volume = 0.5

task.wait(4)

-- add a sound effect
local reverb = Instance.new("ReverbSoundEffect")
reverb.Parent = soundGroup
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