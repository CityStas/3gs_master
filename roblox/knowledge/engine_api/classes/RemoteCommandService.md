---
name: RemoteCommandService
last_updated: 2026-10-30T19:55:53Z
inherits:
  - Instance
  - Object
type: class
memory_category: Instances
tags:
  - NotCreatable
  - Service
summary: "Team Create service that executes Luau commands sent from a Studio client on the collaborative editing server and relays their output back to that client."
---

# Class: RemoteCommandService

> Team Create service that executes Luau commands sent from a Studio client on
> the collaborative editing server and relays their output back to that client.

## Description

Studio-only Team Create service; not accessible from experience scripts.
Powers remote command execution: a Studio client submits Luau source, which
the collaborative editing server runs inside a dedicated sandboxed thread,
streaming the command's output and errors back to the client that started it.

Commands take one of two forms: a persistent command that opens a two-way
channel between the client and the running code, and a one-shot command that
runs once and hands back a single result or error.

While a persistent command runs, its server-side code communicates with the
originating client through the members on this service:
[SendUpdate()](/docs/reference/engine/classes/RemoteCommandService.md) pushes values to the
client,
[GetReceivedUpdateSignal()](/docs/reference/engine/classes/RemoteCommandService.md)
delivers values the client sends back,
[GetStoppingSignal()](/docs/reference/engine/classes/RemoteCommandService.md) fires
when the command is stopped, and
[GetExecutingPlayer()](/docs/reference/engine/classes/RemoteCommandService.md)
identifies the collaborator who started it.

## Methods

### Method: RemoteCommandService:GetExecutingPlayer

**Signature:** `RemoteCommandService:GetExecutingPlayer(): Player`

Call this from inside a running command on the collaborative editing
server to find the [Player](/docs/reference/engine/classes/Player.md) that represents the collaborator who
submitted it. The server compares the command's originating network
address against the connected players and returns the matching
[Player](/docs/reference/engine/classes/Player.md), or `nil` when no player matches.

This method may only be called from within an active persistent command,
and raises an error if there is no such command, such as when called from
a one-shot command or after the command has stopped.

*Security: None · Thread Safety: Unsafe · Capabilities: Unknown*

**Returns:** `Player` — The [Player](/docs/reference/engine/classes/Player.md) representing the collaborator who started the
running command, or `nil` if no connected player matches.

### Method: RemoteCommandService:GetReceivedUpdateSignal

**Signature:** `RemoteCommandService:GetReceivedUpdateSignal(): RBXScriptSignal`

Server-side command code connects to this signal to receive data pushed
from the Studio client that started the command. The event fires with the
tuple of values the client sends, forming the client-to-server half of the
command's two-way channel.

This method may only be called from within an active persistent command,
and raises an error if there is no such command, such as when called from
a one-shot command or after the command has stopped.

*Security: None · Thread Safety: Unsafe · Capabilities: Unknown*

**Returns:** `RBXScriptSignal` — An event that fires with the values the initiating Studio client
passes each time it sends an update to the running command.

### Method: RemoteCommandService:GetStoppingSignal

**Signature:** `RemoteCommandService:GetStoppingSignal(): RBXScriptSignal`

Server-side command code connects to this signal to learn when its command
is being stopped, giving it a chance to clean up before the sandboxed
thread is torn down. The event fires when the initiating Studio client
stops the command, or when that collaborator disconnects from the Team
Create session.

This method may only be called from within an active persistent command,
and raises an error if there is no such command, such as when called from
a one-shot command or after the command has stopped.

*Security: None · Thread Safety: Unsafe · Capabilities: Unknown*

**Returns:** `RBXScriptSignal` — An event that fires, with no arguments, when the running command is
stopped.

### Method: RemoteCommandService:SendUpdate

**Signature:** `RemoteCommandService:SendUpdate(args: Tuple): ()`

Server-side command code calls this to push values to the Studio client
that started the command, forming the server-to-client half of the
command's two-way channel; the values reach that client through the
command's update event.

This method may only be called from within an active persistent command.
When there is no such command, such as when called from a one-shot command
or after the command has stopped, the call has no effect.

*Security: None · Thread Safety: Unsafe · Capabilities: Unknown*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `args` | `Tuple` |  | The values to deliver to the initiating Studio client. |

**Returns:** `()`

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