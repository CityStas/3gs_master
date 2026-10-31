---
name: RemoteFunction
last_updated: 2026-10-30T19:55:53Z
inherits:
  - Instance
  - Object
type: class
memory_category: Instances
summary: "An object which facilitates synchronous, two-way communication across the client-server boundary. Scripts invoking a RemoteFunction yield until they receive a response from the recipient."
---

# Class: RemoteFunction

> An object which facilitates synchronous, two-way communication across the
> client-server boundary. Scripts invoking a [RemoteFunction](/docs/reference/engine/classes/RemoteFunction.md) yield until
> they receive a response from the recipient.

## Description

The **RemoteFunction** object facilitates synchronous, two-way communication
across the [client-server](/docs/en-us/projects/client-server.md) boundary. You
can use it to define a custom callback function and invoke it manually by
calling [RemoteFunction:InvokeClient()](/docs/reference/engine/classes/RemoteFunction.md) or
[RemoteFunction:InvokeServer()](/docs/reference/engine/classes/RemoteFunction.md). The code invoking the function
**yields** until it receives a response from the recipient.

In order for both the server and clients to access a [RemoteFunction](/docs/reference/engine/classes/RemoteFunction.md)
instance, it must be in a place where both sides can see it, such as
[ReplicatedStorage](/docs/reference/engine/classes/ReplicatedStorage.md), although in some cases it's appropriate to store it
in [Workspace](/docs/reference/engine/classes/Workspace.md) or inside a [Tool](/docs/reference/engine/classes/Tool.md).

If the result is **not** needed, it is recommended that you use a
[RemoteEvent](/docs/reference/engine/classes/RemoteEvent.md) instead, since its call is asynchronous and doesn't need
to wait for a response to continue execution. See
[Remote Events and Callbacks](/docs/en-us/scripting/events/remote.md) for code
samples and further details on [RemoteFunction](/docs/reference/engine/classes/RemoteFunction.md).

#### Streaming Precautions

Note that if an invoked [RemoteFunction](/docs/reference/engine/classes/RemoteFunction.md) creates an instance on the
server, there is no guarantee that it exists on the client when the function
returns. This is particularly important in places where instance
[streaming](/docs/en-us/workspace/streaming.md) is enabled and when the
created instances are [BaseParts](/docs/reference/engine/classes/BasePart.md) or [Models](/docs/reference/engine/classes/Model.md),
since parts that are far away from the player's character may not be streamed
to the client, and models that are [Atomic](/docs/reference/engine/enums/ModelStreamingMode.md) depend on
whether their parts are streamed. Even if a model is
[Persistent](/docs/reference/engine/enums/ModelStreamingMode.md), there may be some delay between the
creation of the model and when it is replicated to the client.

#### Parameter Limitations

Any type of Roblox object such as an [Enum](/docs/reference/engine/datatypes/Enum.md), [Instance](/docs/reference/engine/classes/Instance.md), or
others can be passed as a parameter when a [RemoteFunction](/docs/reference/engine/classes/RemoteFunction.md) is invoked,
as well as Luau types such as numbers, strings, and booleans, although you
should carefully explore the
[limitations](/docs/en-us/scripting/events/remote.md#argument-limitations).

## Methods

### Method: RemoteFunction:InvokeClient

**Signature:** `RemoteFunction:InvokeClient(player: Player, arguments: Tuple): Tuple`

Invokes the [RemoteFunction](/docs/reference/engine/classes/RemoteFunction.md) which in turn calls the
[OnClientInvoke](/docs/reference/engine/classes/RemoteFunction.md) callback. Since this
method is used to communicate from the server to a client, it will only
work when used in a [Script](/docs/reference/engine/classes/Script.md).

Any type of Roblox object such as an [Enum](/docs/reference/engine/datatypes/Enum.md), [Instance](/docs/reference/engine/classes/Instance.md), or
others can be passed as a parameter to
[InvokeClient()](/docs/reference/engine/classes/RemoteFunction.md), as well as Luau
types such as numbers, strings, and booleans, although you should
carefully explore the
[limitations](/docs/en-us/scripting/events/remote.md#argument-limitations).

See [Remote Events and Callbacks](/docs/en-us/scripting/events/remote.md) for
code samples and further details on [RemoteFunction](/docs/reference/engine/classes/RemoteFunction.md).

#### Warning

In practice, the server does not often invoke the client, as clients
typically do not have information that the server doesn't have, and
actions that only a client can take, such as displaying a GUI, typically
do not require a callback. As such, [RemoteEvent:FireClient()](/docs/reference/engine/classes/RemoteEvent.md) is
recommended as an asynchronous method that doesn't need to wait for a
response to continue execution.

If you legitimately need to invoke a client from the server, note the
following risks:

- If the client throws an error, the server throws the error too.
- If the client disconnects while it's being invoked,
  [InvokeClient()](/docs/reference/engine/classes/RemoteFunction.md) throws an error.
- If the client doesn't return a value, the server yields forever.

*Yields · Security: None · Thread Safety: Unsafe · Capabilities: RemoteEvent*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `player` | `Player` |  | The [Player](/docs/reference/engine/classes/Player.md) associated with the client to invoke. |
| `arguments` | `Tuple` |  | Values to pass to the [OnClientInvoke](/docs/reference/engine/classes/RemoteFunction.md) callback. |

**Returns:** `Tuple` — Values returned from the
[OnClientInvoke](/docs/reference/engine/classes/RemoteFunction.md) callback.

### Method: RemoteFunction:InvokeServer

**Signature:** `RemoteFunction:InvokeServer(arguments: Tuple): Tuple`

Invokes the [RemoteFunction](/docs/reference/engine/classes/RemoteFunction.md) which in turn calls the
[OnServerInvoke](/docs/reference/engine/classes/RemoteFunction.md) callback. Since this
method is used to communicate from a client to the server, it will only
work when used in a [LocalScript](/docs/reference/engine/classes/LocalScript.md).

If a returned result is not needed, it's recommended to use
[RemoteEvent:FireServer()](/docs/reference/engine/classes/RemoteEvent.md) instead, as its call is asynchronous and
doesn't need to wait for a response to continue execution.

Any type of Roblox object such as an [Enum](/docs/reference/engine/datatypes/Enum.md), [Instance](/docs/reference/engine/classes/Instance.md), or
others can be passed as a parameter to
[InvokeServer()](/docs/reference/engine/classes/RemoteFunction.md), as well as Luau
types such as numbers, strings, and booleans, although you should
carefully explore the
[limitations](/docs/en-us/scripting/events/remote.md#argument-limitations).

See [Remote Events and Callbacks](/docs/en-us/scripting/events/remote.md) for
code samples and further details on [RemoteFunction](/docs/reference/engine/classes/RemoteFunction.md).

*Yields · Security: None · Thread Safety: Unsafe · Capabilities: RemoteEvent*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `arguments` | `Tuple` |  | Values to pass to the [OnServerInvoke](/docs/reference/engine/classes/RemoteFunction.md) callback. |

**Returns:** `Tuple` — Values returned from the
[OnServerInvoke](/docs/reference/engine/classes/RemoteFunction.md) callback.

## Callbacks

### Callback: RemoteFunction.OnClientInvoke

**Signature:** `RemoteFunction.OnClientInvoke(arguments: Tuple): Tuple`

This callback is called when the [RemoteFunction](/docs/reference/engine/classes/RemoteFunction.md) is invoked with
[InvokeClient()](/docs/reference/engine/classes/RemoteFunction.md). When the bound
function returns, the returned values are sent back to the calling server.

See [Remote Events and Callbacks](/docs/en-us/scripting/events/remote.md) for
code samples and further details on
[OnClientInvoke](/docs/reference/engine/classes/RemoteFunction.md).

*Security: None · Thread Safety: Unsafe · Capabilities: RemoteEvent*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `arguments` | `Tuple` |  | The parameters sent through [InvokeClient()](/docs/reference/engine/classes/RemoteFunction.md). |

**Returns:** `Tuple` — Values returned by the callback function.

### Callback: RemoteFunction.OnServerInvoke

**Signature:** `RemoteFunction.OnServerInvoke(player: Player, arguments: Tuple): Tuple`

This callback is called when the [RemoteFunction](/docs/reference/engine/classes/RemoteFunction.md) is invoked with
[InvokeServer()](/docs/reference/engine/classes/RemoteFunction.md). When the bound
function returns, the returned values are sent back to the calling client.

See [Remote Events and Callbacks](/docs/en-us/scripting/events/remote.md) for
code samples and further details on
[OnServerInvoke](/docs/reference/engine/classes/RemoteFunction.md).

*Security: None · Thread Safety: Unsafe · Capabilities: RemoteEvent*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `player` | `Player` |  | The [Player](/docs/reference/engine/classes/Player.md) associated with the client that the [InvokeServer()](/docs/reference/engine/classes/RemoteFunction.md) call originates from. |
| `arguments` | `Tuple` |  | The parameters sent through [InvokeServer()](/docs/reference/engine/classes/RemoteFunction.md). |

**Returns:** `Tuple` — Values returned by the callback function.

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