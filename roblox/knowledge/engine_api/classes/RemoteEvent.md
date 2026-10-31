---
name: RemoteEvent
last_updated: 2026-10-30T19:55:53Z
inherits:
  - BaseRemoteEvent
  - Instance
  - Object
type: class
memory_category: Instances
summary: "An object which facilitates asynchronous, one-way communication across the client-server boundary. Scripts firing a RemoteEvent do not yield."
---

# Class: RemoteEvent

> An object which facilitates asynchronous, one-way communication across the
> client-server boundary. Scripts firing a [RemoteEvent](/docs/reference/engine/classes/RemoteEvent.md) do not yield.

## Description

The **RemoteEvent** object facilitates asynchronous, one-way communication
across the [client-server](/docs/en-us/projects/client-server.md) boundary
without yielding for a response. This communication can be directed from one
client to the server, from the server to a specific client, or from the server
to all clients.

In order for both the server and clients to access a [RemoteEvent](/docs/reference/engine/classes/RemoteEvent.md)
instance, it must be in a place where both sides can see it, such as
[ReplicatedStorage](/docs/reference/engine/classes/ReplicatedStorage.md), although in some cases it's appropriate to store it
in [Workspace](/docs/reference/engine/classes/Workspace.md) or inside a [Tool](/docs/reference/engine/classes/Tool.md).

If no connected listener exists to handle an event, you might see a
`Remote event invocation discarded` error in the log to indicate that the
event was discarded and that you need to implement either `OnClientEvent` or
`OnServerEvent`. Unlike [UnreliableRemoteEvents](/docs/reference/engine/classes/UnreliableRemoteEvent.md),
[RemoteEvents](/docs/reference/engine/classes/RemoteEvent.md) buffer a large number of events before
throwing this error.

If you need the result of the call, you should use a [RemoteFunction](/docs/reference/engine/classes/RemoteFunction.md)
instead. Otherwise a remote event is recommended since it will minimize
network traffic/latency and won't yield the script to wait for a response.

See [Remote events and callbacks](/docs/en-us/scripting/events/remote.md) for
code samples and further details.

#### Throttling

Remote events are subject to rate limits when sent from the client to the
server with the [FireServer()](/docs/reference/engine/classes/RemoteEvent.md) method.
[RemoteEvents](/docs/reference/engine/classes/RemoteEvent.md) and
[UnreliableRemoteEvents](/docs/reference/engine/classes/UnreliableRemoteEvent.md) both have a limit of
approximately 500 requests per second, per client. This limit is **shared
among all remote events of the same type**. To avoid throttling and latency
issues, limit recurring remote events whenever possible.

#### Parameter limitations

Any type of Roblox object ([Enum](/docs/reference/engine/datatypes/Enum.md), [Instance](/docs/reference/engine/classes/Instance.md), etc.) can be
passed as a parameter when a [RemoteEvent](/docs/reference/engine/classes/RemoteEvent.md) is fired, as well as Luau
types such as numbers, strings, and booleans, although you should carefully
explore the
[limitations](/docs/en-us/scripting/events/remote.md#argument-limitations).

## Methods

### Method: RemoteEvent:FireAllClients

**Signature:** `RemoteEvent:FireAllClients(arguments: Tuple): ()`

Fires the [OnClientEvent](/docs/reference/engine/classes/RemoteEvent.md) event for each
connected client. Unlike [FireClient()](/docs/reference/engine/classes/RemoteEvent.md),
this event does not take a target [Player](/docs/reference/engine/classes/Player.md) as the first argument,
since it fires to multiple clients. Since this method is used to
communicate from the server to clients, it only works when used in a
[Script](/docs/reference/engine/classes/Script.md).

*Security: None · Thread Safety: Unsafe · Capabilities: RemoteEvent*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `arguments` | `Tuple` |  | Values to pass to all [OnClientEvent](/docs/reference/engine/classes/RemoteEvent.md) events connected to the same [RemoteEvent](/docs/reference/engine/classes/RemoteEvent.md). |

**Returns:** `()`

### Method: RemoteEvent:FireClient

**Signature:** `RemoteEvent:FireClient(player: Player, arguments: Tuple): ()`

Fires the [OnClientEvent](/docs/reference/engine/classes/RemoteEvent.md) event for the
specific client in the required [Player](/docs/reference/engine/classes/Player.md) argument. Since this method
is used to communicate from the server to a client, it only works when
used in a [Script](/docs/reference/engine/classes/Script.md).

*Security: None · Thread Safety: Unsafe · Capabilities: RemoteEvent*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `player` | `Player` |  | The client of the [Player](/docs/reference/engine/classes/Player.md) to fire the event to. |
| `arguments` | `Tuple` |  | Values to pass to [OnClientEvent](/docs/reference/engine/classes/RemoteEvent.md) events connected to the same [RemoteEvent](/docs/reference/engine/classes/RemoteEvent.md). |

**Returns:** `()`

### Method: RemoteEvent:FireServer

**Signature:** `RemoteEvent:FireServer(arguments: Tuple): ()`

Fires the [OnServerEvent](/docs/reference/engine/classes/RemoteEvent.md) event on the
server from one client. Connected events receive the [Player](/docs/reference/engine/classes/Player.md)
argument of the firing client. Since this method is used to communicate
from a client to the server, it only works when used in a client script.

*Security: None · Thread Safety: Unsafe · Capabilities: RemoteEvent*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `arguments` | `Tuple` |  | Values to pass to [OnServerEvent](/docs/reference/engine/classes/RemoteEvent.md) events connected to the same [RemoteEvent](/docs/reference/engine/classes/RemoteEvent.md). |

**Returns:** `()`

## Events

### Event: RemoteEvent.OnClientEvent

**Signature:** `RemoteEvent.OnClientEvent(arguments: Tuple)`

Fires from a [LocalScript](/docs/reference/engine/classes/LocalScript.md) when either
[FireClient()](/docs/reference/engine/classes/RemoteEvent.md) or
[FireAllClients()](/docs/reference/engine/classes/RemoteEvent.md) is called on the
same [RemoteEvent](/docs/reference/engine/classes/RemoteEvent.md) instance from a [Script](/docs/reference/engine/classes/Script.md).

See [Remote Events and Callbacks](/docs/en-us/scripting/events/remote.md) for
code samples and further details on
[OnClientEvent](/docs/reference/engine/classes/RemoteEvent.md).

*Security: None · Capabilities: RemoteEvent*

**Parameters:**

| Name | Type | Description |
|------|------|-------------|
| `arguments` | `Tuple` | The parameters sent through [FireClient()](/docs/reference/engine/classes/RemoteEvent.md) or [FireAllClients()](/docs/reference/engine/classes/RemoteEvent.md). |

### Event: RemoteEvent.OnServerEvent

**Signature:** `RemoteEvent.OnServerEvent(player: Player, arguments: Tuple)`

Fires from a [Script](/docs/reference/engine/classes/Script.md) when
[FireServer()](/docs/reference/engine/classes/RemoteEvent.md) is called on the same
[RemoteEvent](/docs/reference/engine/classes/RemoteEvent.md) instance from a [LocalScript](/docs/reference/engine/classes/LocalScript.md).

See [Remote Events and Callbacks](/docs/en-us/scripting/events/remote.md) for
code samples and further details on
[OnServerEvent](/docs/reference/engine/classes/RemoteEvent.md).

*Security: None · Capabilities: RemoteEvent*

**Parameters:**

| Name | Type | Description |
|------|------|-------------|
| `player` | `Player` | The [Player](/docs/reference/engine/classes/Player.md) associated with the client that the [FireServer()](/docs/reference/engine/classes/RemoteEvent.md) call originates from. |
| `arguments` | `Tuple` | The parameters sent through [FireServer()](/docs/reference/engine/classes/RemoteEvent.md). |

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