---
name: AudioDeviceInput
last_updated: 2026-10-30T19:55:51Z
inherits:
  - Instance
  - Object
type: class
memory_category: Internal
summary: "Produces audio streams from physical devices, such as microphones."
---

# Class: AudioDeviceInput

> Produces audio streams from physical devices, such as microphones.

## Description

[AudioDeviceInput](/docs/reference/engine/classes/AudioDeviceInput.md) produces audio streams from physical devices, such as
microphones. It provides a single **Output** pin which can be connected to
other pins via [Wires](/docs/reference/engine/classes/Wire.md). [AudioDeviceInput](/docs/reference/engine/classes/AudioDeviceInput.md) has properties for
selecting which [Player](/docs/reference/engine/classes/Player.md) is producing the stream, and controlling
whether or not they are muted.

## Properties

### Property: AudioDeviceInput.AccessType

```json
{
  "type": "AccessModifierType",
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
  "category": "Permissions",
  "capabilities": [
    "Audio",
    "Input"
  ]
}
```

Determines whether the list of user IDs provided to
[SetUserIdAccessList](/docs/reference/engine/classes/AudioDeviceInput.md) is
treated as an allow-list or deny-list.

If [AccessType](/docs/reference/engine/classes/AudioDeviceInput.md) is
[AccessModifierType.Allow](/docs/reference/engine/enums/AccessModifierType.md), then **only** the supplied user IDs are
**permitted** to hear this [AudioDeviceInput](/docs/reference/engine/classes/AudioDeviceInput.md). If
[AccessType](/docs/reference/engine/classes/AudioDeviceInput.md) is
[AccessModifierType.Deny](/docs/reference/engine/enums/AccessModifierType.md), then **only** the supplied user IDs are
**blocked** from hearing this [AudioDeviceInput](/docs/reference/engine/classes/AudioDeviceInput.md).

Since player voices are networked, this property should only be assigned
from the server in order to replicate properly.

### Property: AudioDeviceInput.Active

```json
{
  "type": "boolean",
  "access": "ReadOnly",
  "security": {
    "read": "None",
    "write": "RobloxScriptSecurity"
  },
  "serialization": {
    "can_load": true,
    "can_save": true
  },
  "thread_safety": "ReadSafe",
  "category": "Recording",
  "capabilities": [
    "Audio",
    "Input"
  ]
}
```

Controls whether the physical device is actively recording. This property
is only set by Roblox core scripts, but it may be read by user scripts.
Generally, an [AudioDeviceInput](/docs/reference/engine/classes/AudioDeviceInput.md) may only be producing sound if
[Active](/docs/reference/engine/classes/AudioDeviceInput.md) is true **and**
[Muted](/docs/reference/engine/classes/AudioDeviceInput.md) is false.

### Property: AudioDeviceInput.IsReady

```json
{
  "type": "boolean",
  "access": "ReadOnly",
  "security": {
    "read": "RobloxScriptSecurity",
    "write": "RobloxScriptSecurity"
  },
  "serialization": {
    "can_load": false,
    "can_save": true
  },
  "thread_safety": "ReadSafe",
  "category": "Recording",
  "capabilities": [
    "Audio",
    "Input"
  ]
}
```

Denotes whether this [AudioDeviceInput](/docs/reference/engine/classes/AudioDeviceInput.md) is ready to produce sound,
meaning all network connections have been established.

### Property: AudioDeviceInput.Muted

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
  "category": "Recording",
  "capabilities": [
    "Audio",
    "Input"
  ]
}
```

Controls whether this [AudioDeviceInput](/docs/reference/engine/classes/AudioDeviceInput.md) is muted. Unlike
[Active](/docs/reference/engine/classes/AudioDeviceInput.md), this property is publicly
scriptable.

Generally, an [AudioDeviceInput](/docs/reference/engine/classes/AudioDeviceInput.md) may only be heard if
[Active](/docs/reference/engine/classes/AudioDeviceInput.md) is true **and**
[Muted](/docs/reference/engine/classes/AudioDeviceInput.md) is false.

**Push-to-talk**

```lua
local players = game:GetService("Players")
local userInput = game:GetService("UserInputService")
local audioIn: AudioDeviceInput = players.LocalPlayer:WaitForChild("AudioDeviceInput")
audioIn.Muted = true

local pushToTalkKey = Enum.KeyCode.V

userInput.InputBegan:Connect(function(input: InputObject)
	if input.KeyCode == pushToTalkKey then
		audioIn.Muted = false
	end
end)

userInput.InputEnded:Connect(function(input: InputObject)
	if input.KeyCode == pushToTalkKey then
		audioIn.Muted = true
	end
end)
```

### Property: AudioDeviceInput.Player

```json
{
  "type": "Player",
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
  "category": "Recording",
  "capabilities": [
    "Audio",
    "Input",
    "Players"
  ]
}
```

Determines whose device is producing sound. In order to replicate
properly, this should only be assigned from the server. Assigning this
property locally generally does not work, unless
[Player](/docs/reference/engine/classes/AudioDeviceInput.md) is [Players.LocalPlayer](/docs/reference/engine/classes/Players.md).

### Property: AudioDeviceInput.Volume

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
    "Audio",
    "Input"
  ]
}
```

Volume level which is multiplied onto the output audio stream. Ranges from
0 to 3.

## Methods

### Method: AudioDeviceInput:GetConnectedWires

**Signature:** `AudioDeviceInput:GetConnectedWires(pin: string): List<Wire>`

Returns an array of [Wires](/docs/reference/engine/classes/Wire.md) that are connected to the specified
pin. [AudioDeviceInput](/docs/reference/engine/classes/AudioDeviceInput.md) has one "Output" pin.

*Security: None · Thread Safety: Unsafe · Capabilities: Audio, Input*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `pin` | `string` |  | An input or output pin on this instance |

**Returns:** `List<Wire>` — An array of [Wires](/docs/reference/engine/classes/Wire.md)

### Method: AudioDeviceInput:GetInputPins

**Signature:** `AudioDeviceInput:GetInputPins(): Array`

Gets the list of pins that [Wire](/docs/reference/engine/classes/Wire.md) can use in [Wire.TargetName](/docs/reference/engine/classes/Wire.md)
to connect to this instance via its [Wire.TargetInstance](/docs/reference/engine/classes/Wire.md) property.

For [AudioDeviceInput](/docs/reference/engine/classes/AudioDeviceInput.md), there are none.

*Security: None · Thread Safety: Unsafe · Capabilities: Audio, Input*

**Returns:** `Array` — An array of strings representing valid pin names.

### Method: AudioDeviceInput:GetOutputPins

**Signature:** `AudioDeviceInput:GetOutputPins(): Array`

Gets the list of pins that [Wire](/docs/reference/engine/classes/Wire.md) can use in [Wire.SourceName](/docs/reference/engine/classes/Wire.md)
to connect to this instance via its [Wire.SourceInstance](/docs/reference/engine/classes/Wire.md) property.

For [AudioDeviceInput](/docs/reference/engine/classes/AudioDeviceInput.md), this is `Output` only.

*Security: None · Thread Safety: Unsafe · Capabilities: Audio, Input*

**Returns:** `Array` — An array of strings representing valid pin names.

### Method: AudioDeviceInput:GetUserIdAccessList

**Signature:** `AudioDeviceInput:GetUserIdAccessList(): Array`

Returns a list of user IDs that are either permitted to hear or blocked
from hearing this [AudioDeviceInput](/docs/reference/engine/classes/AudioDeviceInput.md), depending on the
[AccessType](/docs/reference/engine/classes/AudioDeviceInput.md).

*Security: None · Thread Safety: Unsafe · Capabilities: Audio, Input*

**Returns:** `Array` — An array of user IDs that are either in the allow-list or the
deny-list.

### Method: AudioDeviceInput:SetUserIdAccessList

**Signature:** `AudioDeviceInput:SetUserIdAccessList(userIds: Array): ()`

Sets a list of user IDs that are either permitted to hear or blocked from
hearing this [AudioDeviceInput](/docs/reference/engine/classes/AudioDeviceInput.md), depending on the
[AccessType](/docs/reference/engine/classes/AudioDeviceInput.md).

Note that this method replicates from server to client; in general, it
should only be called from the server in order to replicate properly.

*Security: None · Thread Safety: Unsafe · Capabilities: Audio, Input*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `userIds` | `Array` |  | An array of user IDs to apply to this [AudioDeviceInput](/docs/reference/engine/classes/AudioDeviceInput.md). |

**Returns:** `()` — void

## Events

### Event: AudioDeviceInput.WiringChanged

**Signature:** `AudioDeviceInput.WiringChanged(connected: boolean, pin: string, wire: Wire, instance: Instance)`

Event that fires after a [Wire](/docs/reference/engine/classes/Wire.md) becomes connected or disconnected,
and that [Wire](/docs/reference/engine/classes/Wire.md) is now or was previously connected to a pin on the
[AudioDeviceInput](/docs/reference/engine/classes/AudioDeviceInput.md) and to some other wirable instance.

*Security: None · Capabilities: Audio, Input*

**Parameters:**

| Name | Type | Description |
|------|------|-------------|
| `connected` | `boolean` | Whether the instance got connected or disconnected. |
| `pin` | `string` | The pin on the [AudioDeviceInput](/docs/reference/engine/classes/AudioDeviceInput.md) that the [Wire](/docs/reference/engine/classes/Wire.md) targets. |
| `wire` | `Wire` | The [Wire](/docs/reference/engine/classes/Wire.md) between the [AudioDeviceInput](/docs/reference/engine/classes/AudioDeviceInput.md) and the other instance. |
| `instance` | `Instance` | The other instance that is or was connected through the [Wire](/docs/reference/engine/classes/Wire.md). |

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