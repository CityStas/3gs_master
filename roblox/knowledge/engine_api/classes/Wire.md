---
name: Wire
last_updated: 2026-10-30T19:55:53Z
inherits:
  - Instance
  - Object
type: class
memory_category: Instances
summary: "Connects one or more Instances to form a processing graph of their streams. At the moment, only audio streams are supported, but this may expand in the future."
---

# Class: Wire

> Connects one or more [Instances](/docs/reference/engine/classes/Instance.md) to form a processing graph of
> their streams. At the moment, only audio streams are supported, but this may
> expand in the future.

## Description

[Wire](/docs/reference/engine/classes/Wire.md) connects one or more [Instances](/docs/reference/engine/classes/Instance.md) to form a
processing graph of their streams. Each [Wire](/docs/reference/engine/classes/Wire.md) connects a source and
target instance, and a source and target "pin" within each of those instances.
Pins are string identifiers that select which stream is to be carried by the
wire.

At the moment, only audio streams are supported, but this may expand in the
future.

The following instances may be connected by [Wires](/docs/reference/engine/classes/Wire.md):

- [AudioAnalyzer](/docs/reference/engine/classes/AudioAnalyzer.md)
- [AudioChannelMixer](/docs/reference/engine/classes/AudioChannelMixer.md)
- [AudioChannelSplitter](/docs/reference/engine/classes/AudioChannelSplitter.md)
- [AudioChorus](/docs/reference/engine/classes/AudioChorus.md)
- [AudioCompressor](/docs/reference/engine/classes/AudioCompressor.md)
- [AudioDeviceInput](/docs/reference/engine/classes/AudioDeviceInput.md)
- [AudioDeviceOutput](/docs/reference/engine/classes/AudioDeviceOutput.md)
- [AudioDistortion](/docs/reference/engine/classes/AudioDistortion.md)
- [AudioEcho](/docs/reference/engine/classes/AudioEcho.md)
- [AudioEmitter](/docs/reference/engine/classes/AudioEmitter.md)
- [AudioEqualizer](/docs/reference/engine/classes/AudioEqualizer.md)
- [AudioFader](/docs/reference/engine/classes/AudioFader.md)
- [AudioFilter](/docs/reference/engine/classes/AudioFilter.md)
- [AudioFlanger](/docs/reference/engine/classes/AudioFlanger.md)
- [AudioGate](/docs/reference/engine/classes/AudioGate.md)
- [AudioLimiter](/docs/reference/engine/classes/AudioLimiter.md)
- [AudioListener](/docs/reference/engine/classes/AudioListener.md)
- [AudioPitchShifter](/docs/reference/engine/classes/AudioPitchShifter.md)
- [AudioPlayer](/docs/reference/engine/classes/AudioPlayer.md)
- [AudioRecorder](/docs/reference/engine/classes/AudioRecorder.md)
- [AudioReverb](/docs/reference/engine/classes/AudioReverb.md)
- [AudioSpeechToText](/docs/reference/engine/classes/AudioSpeechToText.md)
- [AudioTextToSpeech](/docs/reference/engine/classes/AudioTextToSpeech.md)
- [AudioTremolo](/docs/reference/engine/classes/AudioTremolo.md)
- [VideoPlayer](/docs/reference/engine/classes/VideoPlayer.md)
- [VideoDisplay](/docs/reference/engine/classes/VideoDisplay.md)

## Properties

### Property: Wire.Connected

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
    "can_save": true
  },
  "thread_safety": "ReadSafe",
  "category": "Connections",
  "capabilities": [
    "Basic"
  ]
}
```

Denotes whether the [Wire](/docs/reference/engine/classes/Wire.md) is connected, meaning its
[SourceInstance](/docs/reference/engine/classes/Wire.md),
[TargetInstance](/docs/reference/engine/classes/Wire.md),
[SourceName](/docs/reference/engine/classes/Wire.md), and [TargetName](/docs/reference/engine/classes/Wire.md)
properties are all assigned, the corresponding
[SourceName](/docs/reference/engine/classes/Wire.md) and [TargetName](/docs/reference/engine/classes/Wire.md)
pins exist on [SourceInstance](/docs/reference/engine/classes/Wire.md) and
[TargetInstance](/docs/reference/engine/classes/Wire.md) respectively, and the
connection does not result in a cyclic processing graph.

### Property: Wire.SourceInstance

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
  "category": "Connections",
  "capabilities": [
    "Basic"
  ]
}
```

The [Instance](/docs/reference/engine/classes/Instance.md) producing a stream to be carried over the wire. At
the moment, only audio streams are wirable.

### Property: Wire.SourceName

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
  "category": "Connections",
  "capabilities": [
    "Basic"
  ]
}
```

The name of the pin on [SourceInstance](/docs/reference/engine/classes/Wire.md) that is
producing a stream. At the moment, various audio instances only have an
**Output** pin, but this may expand in the future. The default value of
this property is **Output** so it is not yet necessary to change.

### Property: Wire.TargetInstance

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
  "category": "Connections",
  "capabilities": [
    "Basic"
  ]
}
```

The [Instance](/docs/reference/engine/classes/Instance.md) intended to receive a stream from
[SourceInstance](/docs/reference/engine/classes/Wire.md). Currently, only audio streams
are wirable.

### Property: Wire.TargetName

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
  "category": "Connections",
  "capabilities": [
    "Basic"
  ]
}
```

The name of the pin on [TargetInstance](/docs/reference/engine/classes/Wire.md) that is
receiving a stream. At the moment, audio instances typically have an
**Input** pin, but [AudioCompressor](/docs/reference/engine/classes/AudioCompressor.md) has an additional **Sidechain**
pin. This may expand in the future.

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