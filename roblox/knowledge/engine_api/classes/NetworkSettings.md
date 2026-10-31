---
name: NetworkSettings
last_updated: 2026-10-30T19:55:52Z
inherits:
  - Instance
  - Object
type: class
memory_category: Instances
tags:
  - NotCreatable
  - Service
  - NotReplicated
  - NotBrowsable
summary: "Settings related to networked engine behaviors."
---

# Class: NetworkSettings

> Settings related to networked engine behaviors.

## Description

`NetworkSettings` is a class that allows you to debug several features with
Roblox's server/client networking. It can be found in Roblox Studio's settings
under the **Network** tab.

## Properties

### Property: NetworkSettings.HttpProxyEnabled

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
  "category": "Proxy Settings",
  "capabilities": [
    "Network"
  ]
}
```

When `true`, the client routes its HTTP traffic through the proxy server
specified by [HttpProxyURL](/docs/reference/engine/classes/NetworkSettings.md). This
property defaults to `false`.

### Property: NetworkSettings.HttpProxyURL

```json
{
  "type": "string",
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
  "category": "Proxy Settings",
  "capabilities": [
    "Network"
  ]
}
```

Specifies the address of the proxy server through which the client routes
its HTTP traffic when
[HttpProxyEnabled](/docs/reference/engine/classes/NetworkSettings.md) is `true`. This
property defaults to an empty string.

### Property: NetworkSettings.InboundNetworkJitterMs

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
    "Network"
  ]
}
```

On [playtest](/docs/en-us/studio/testing-modes.md#playtesting) connections, this
property adds variability (jitter) in milliseconds to the latency added to
packets sent from server to client. This variable latency is in addition
to any latency introduced by
[InboundNetworkMinDelayMs](/docs/reference/engine/classes/NetworkSettings.md).
Per-packet delay sampled from delay and jitter is rounded to 1
millisecond. See
[network simulation](/docs/en-us/studio/testing-modes.md#network-simulation) for
additional details.

### Property: NetworkSettings.InboundNetworkLossPercent

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
    "Network"
  ]
}
```

On [playtest](/docs/en-us/studio/testing-modes.md#playtesting) connections, this
property sets a percent probability that packets sent from server to
client are dropped. To maintain a stable test environment, the value is
capped at 0.5%. See
[network simulation](/docs/en-us/studio/testing-modes.md#network-simulation) for
additional details.

### Property: NetworkSettings.InboundNetworkMinDelayMs

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
    "Network"
  ]
}
```

On [playtest](/docs/en-us/studio/testing-modes.md#playtesting) connections, this
property adds a minimum latency in milliseconds for packets sent from
server to client. Per-packet delay sampled from delay and jitter is
rounded to 1 millisecond. See
[network simulation](/docs/en-us/studio/testing-modes.md#network-simulation) for
additional details.

### Property: NetworkSettings.IncomingReplicationLag

```json
{
  "type": "double",
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
  "category": "Diagnostics",
  "capabilities": [
    "Network"
  ]
}
```

This property instructs the engine to simulate additional replication lag
by delaying all incoming messages. Units are seconds.

### Property: NetworkSettings.OutboundNetworkJitterMs

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
    "Network"
  ]
}
```

On [playtest](/docs/en-us/studio/testing-modes.md#playtesting) connections, this
property adds variability (jitter) in milliseconds to the latency added to
packets sent from client to server. This variable latency is in addition
to any latency introduced by
[OutboundNetworkMinDelayMs](/docs/reference/engine/classes/NetworkSettings.md).
Per-packet delay sampled from delay and jitter is rounded to 1
millisecond. See
[network simulation](/docs/en-us/studio/testing-modes.md#network-simulation) for
additional details.

### Property: NetworkSettings.OutboundNetworkLossPercent

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
    "Network"
  ]
}
```

On [playtest](/docs/en-us/studio/testing-modes.md#playtesting) connections, this
property sets a percent probability that packets sent from client to
server are dropped. To maintain a stable test environment, the value is
capped at 0.5%. See
[network simulation](/docs/en-us/studio/testing-modes.md#network-simulation) for
additional details.

### Property: NetworkSettings.OutboundNetworkMinDelayMs

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
    "Network"
  ]
}
```

On [playtest](/docs/en-us/studio/testing-modes.md#playtesting) connections, this
property adds a minimum latency in milliseconds for packets sent from
client to server. Per-packet delay sampled from delay and jitter is
rounded to 1 millisecond. See
[network simulation](/docs/en-us/studio/testing-modes.md#network-simulation) for
additional details.

### Property: NetworkSettings.PrintJoinSizeBreakdown

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
  "category": "Diagnostics",
  "capabilities": [
    "Network"
  ]
}
```

Prints diagnostic information to the **Output** window after connecting.
The data will indicate the largest individual [Instances](/docs/reference/engine/classes/Instance.md)
sent, as well as aggregate data about data sent by [Instance](/docs/reference/engine/classes/Instance.md) type.
The data sent for initial loading is compressed so the contributions are
approximate.

### Property: NetworkSettings.PrintPhysicsErrors

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
  "category": "Diagnostics",
  "capabilities": [
    "Network"
  ]
}
```

When set to `true`, debug messages will be printed to the **Output**
window pertaining to physics replication errors. The following are debug
outputs that are made available:

- `Physics-in old packet` prints for a part that has been updated ahead of
  the packet's submission time. This happens if the packet is received
  late, and a newer packet has already been processed.

- `Physics-in of unidentified {GUID}` prints for an unfound part that is
  trying to be updated because the provided [Instance](/docs/reference/engine/classes/Instance.md) identifier
  was invalid, where `{GUID}` is the unknown [Instance:GetDebugId()](/docs/reference/engine/classes/Instance.md)
  identifier that is supposed to be targeting the part. This typically
  happens if a part is removed before the physics update packet is
  received.

- `Physics-in of part not in workspace {GUID}` prints for a request to
  update the physics of a part that is not a descendant of the
  [Workspace](/docs/reference/engine/classes/Workspace.md), where `{GUID}` is the [Instance:GetDebugId()](/docs/reference/engine/classes/Instance.md)
  identifier of the target part. This happens if the part was just moved
  out of the [Workspace](/docs/reference/engine/classes/Workspace.md), and was previously being simulated.

### Property: NetworkSettings.PrintStreamInstanceQuota

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
  "category": "Diagnostics",
  "capabilities": [
    "Network"
  ]
}
```

When set to `true`, debug information is printed to the **Output** window
regarding the replication of instances when
[Workspace.StreamingEnabled](/docs/reference/engine/classes/Workspace.md) is set to `true`.

### Property: NetworkSettings.RandomizeJoinInstanceOrder

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
  "category": "Advanced",
  "capabilities": [
    "Network"
  ]
}
```

Emulates the behavior of a server that has been online a long time by
randomizing the order that instances initially arrive on clients. It is
recommended to keep this setting enabled to help discover potential bugs
while testing in Studio.

### Property: NetworkSettings.RenderStreamedRegions

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
  "category": "Appearance",
  "capabilities": [
    "Network"
  ]
}
```

When set to `true`, regions of space that are being streamed to the client
will be outlined in red. This will only be shown if
[Workspace.StreamingEnabled](/docs/reference/engine/classes/Workspace.md) is set to `true`.

### Property: NetworkSettings.ShowActiveAnimationAsset

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
  "category": "Appearance",
  "capabilities": [
    "Network",
    "Animation"
  ]
}
```

When set to `true`, a label will be shown above each player character's
head, showing the current animation (if any) being played by the
character's [Humanoid](/docs/reference/engine/classes/Humanoid.md).

### Property: NetworkSettings.EmulatedTotalMemoryInMB *(hidden)*

```json
{
  "type": "int",
  "access": "ReadOnly",
  "security": {
    "read": "PluginSecurity",
    "write": "PluginSecurity"
  },
  "serialization": {
    "can_load": false,
    "can_save": false
  },
  "thread_safety": "ReadSafe",
  "category": "Data",
  "capabilities": [
    "Network"
  ]
}
```

Sets the total amount of memory, in MiB, that the client pretends the
device has when testing under a simulated device. Studio's device emulator
writes this property when you select a device to emulate. Values are
clamped to a minimum of `0`, and the property defaults to the machine's
actual total physical memory.

### Property: NetworkSettings.FreeMemoryMBytes *(hidden)*

```json
{
  "type": "float",
  "access": "ReadOnly",
  "security": {
    "read": "PluginSecurity",
    "write": "PluginSecurity"
  },
  "serialization": {
    "can_load": false,
    "can_save": false
  },
  "thread_safety": "ReadSafe",
  "category": "Data",
  "capabilities": [
    "Network"
  ]
}
```

`FreeMemoryMBytes` is a read-only property that describes how much free
memory is available, in MiBs.

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