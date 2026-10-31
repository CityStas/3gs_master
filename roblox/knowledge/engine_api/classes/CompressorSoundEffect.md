---
name: CompressorSoundEffect
last_updated: 2026-10-30T19:55:52Z
inherits:
  - SoundEffect
  - Instance
  - Object
type: class
memory_category: Instances
summary: "Adjusts the dynamic range of audio."
---

# Class: CompressorSoundEffect

> Adjusts the dynamic range of audio.

## Description

A [CompressorSoundEffect](/docs/reference/engine/classes/CompressorSoundEffect.md) is used to reduce the dynamic range of audio
by moving the highs and lows of a signal closer together. It does this by
lowering the volume of the highest parts of a source while at the same time
raising the overall volume. This type of effect is useful when you have many
sounds playing and you want to make sure the quieter ones are still audible.
This effect can be applied to either an individual [Sound](/docs/reference/engine/classes/Sound.md) or
[SoundGroup](/docs/reference/engine/classes/SoundGroup.md) by parenting it to the desired instance.

A compressor has several properties which determine how it works. The
[Threshold](/docs/reference/engine/classes/CompressorSoundEffect.md) is the audio level where the
compressor will start to lower the volume. As soon as the source goes below
the threshold, the compressor will stop lowering the volume.

The [Attack](/docs/reference/engine/classes/CompressorSoundEffect.md) determines how long it takes
for the compressed effect to fully apply. After the threshold has been crossed
the compressor will lower the volume over time until the desired ratio has
been reached. It will take the time specified by
[Attack](/docs/reference/engine/classes/CompressorSoundEffect.md) to reach this ratio.

The [Release](/docs/reference/engine/classes/CompressorSoundEffect.md) determines how long it takes
for the compressor to remove its effect. After the volume of the source is
under the threshold, the compressor will restore the volume back to the
original over the time specified by
[Release](/docs/reference/engine/classes/CompressorSoundEffect.md).

Along with lowering the volume when the sound has passed the threshold, a
compressor will also amplify the entire sound (after any threshold lowering
has taken effect). This allows quieter sounds to be amplified while louder
sounds can stay about the same. The
[GainMakeup](/docs/reference/engine/classes/CompressorSoundEffect.md) determines how much the
effect amplifies the sound.

## Properties

### Property: CompressorSoundEffect.Attack

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

The time the effect takes to become active after its
[Threshold](/docs/reference/engine/classes/CompressorSoundEffect.md) has been reached. Range
is `0.1` to `1` (default `0.1`), measured in seconds.

### Property: CompressorSoundEffect.GainMakeup

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

The overall amplification applied to the effect's [Sound](/docs/reference/engine/classes/Sound.md) or
[SoundGroup](/docs/reference/engine/classes/SoundGroup.md) after attenuation of sounds above the threshold. Keep
in mind this amplification will occur as long as the effect is active,
regardless of whether the
[Threshold](/docs/reference/engine/classes/CompressorSoundEffect.md) has been reached or not.
Range is `-30` to `30` (default `0`), measured in dB.

### Property: CompressorSoundEffect.Ratio

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

The ratio between the [SideChain](/docs/reference/engine/classes/CompressorSoundEffect.md)
sound effect, and this sound effect.

### Property: CompressorSoundEffect.Release

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

The time the effect takes to become inactive after its sound is below the
[Threshold](/docs/reference/engine/classes/CompressorSoundEffect.md). Range is `0` to `5`
(default `0.1`), measured in seconds.

### Property: CompressorSoundEffect.SideChain

```json
{
  "type": "Instance",
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

Applies a ducking effect to the compressor sound effect. The behavior of
the sidechain depends on the [Sound](/docs/reference/engine/classes/Sound.md) or [SoundGroup](/docs/reference/engine/classes/SoundGroup.md) linked to
it.

### Property: CompressorSoundEffect.Threshold

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

Volume level at which point the compressor applies its effect. If the
effect's [Sound](/docs/reference/engine/classes/Sound.md) or [SoundGroup](/docs/reference/engine/classes/SoundGroup.md) is below the effect will not
attenuate the sound, although the
[GainMakeup](/docs/reference/engine/classes/CompressorSoundEffect.md) will still be applied.
Range is `-80` to `0` (default `0`), measured in dB.

## Inherited Members

### From [SoundEffect](/docs/reference/engine/classes/SoundEffect.md)

- **Property `Enabled`** (`boolean`): Toggles the effect on and off.
- **Property `Priority`** (`int`): Determines the order the effect will be applied in relation to other

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