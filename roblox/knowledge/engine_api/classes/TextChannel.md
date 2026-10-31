---
name: TextChannel
last_updated: 2026-10-30T19:55:53Z
inherits:
  - Instance
  - Object
type: class
memory_category: Instances
summary: "Represents a text chat channel."
---

# Class: TextChannel

> Represents a text chat channel.

## Description

Represents a text chat channel. Contains [TextSources](/docs/reference/engine/classes/TextSource.md) as
descendants.

To send a chat message to the [TextChannel](/docs/reference/engine/classes/TextChannel.md), call
[TextChannel:SendAsync()](/docs/reference/engine/classes/TextChannel.md) from a [LocalScript](/docs/reference/engine/classes/LocalScript.md). The corresponding
[TextSource](/docs/reference/engine/classes/TextSource.md) of the user with `TextSource.CanSend = true` must be in
that channel.

Messages from different TextChannels can be separated into different tabs in
the chat window using [ChannelTabsConfiguration](/docs/reference/engine/classes/ChannelTabsConfiguration.md). Multiple channels with
the same name might cause unexpected behavior with the chat window, even if
the player isn't a member of the other channels.

To learn more, see
[In-Experience Text Chat](/docs/en-us/chat/in-experience-text-chat.md).

## Properties

### Property: TextChannel.DirectChatRequester

```json
{
  "type": "Player",
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
  "category": "Data",
  "capabilities": [
    "Chat"
  ]
}
```

The `TextChannel` will only deliver messages to users that can send direct
messages to the `DirectChatRequester`. This property can only be set using
[SetDirectChatRequester()](/docs/reference/engine/classes/TextChannel.md).

## Methods

### Method: TextChannel:AddUserAsync

**Signature:** `TextChannel:AddUserAsync(userId: User): Tuple`

Adds a [TextSource](/docs/reference/engine/classes/TextSource.md) to the [TextChannel](/docs/reference/engine/classes/TextChannel.md) given userId of the
user (with [Player.UserId](/docs/reference/engine/classes/Player.md)). Can only be used in a [Script](/docs/reference/engine/classes/Script.md).

If a [TextSource](/docs/reference/engine/classes/TextSource.md) representing the user does not exist, this adds a
[TextSource](/docs/reference/engine/classes/TextSource.md).

If a [TextSource](/docs/reference/engine/classes/TextSource.md) representing the user does exist, this returns the
[TextSource](/docs/reference/engine/classes/TextSource.md).

If the user has chat off or isn't in the server, this returns a tuple
`nil`, `false`.

*Yields · Security: None · Thread Safety: Unsafe · Capabilities: Chat*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `userId` | `User` |  | The userId of the [Player](/docs/reference/engine/classes/Player.md). |

**Returns:** `Tuple` — Returns [TextSource](/docs/reference/engine/classes/TextSource.md) and `true` if a new [TextSource](/docs/reference/engine/classes/TextSource.md) is
created for the user, [TextSource](/docs/reference/engine/classes/TextSource.md) and `false` if there is an
existing [TextSource](/docs/reference/engine/classes/TextSource.md), or `nil` and `false` if the user has chat
off or is not in this server.

### Method: TextChannel:DisplaySystemMessage

**Signature:** `TextChannel:DisplaySystemMessage(systemMessage: string, metadata: string): TextChatMessage`

Displays a system message to user. Can only be used in a
[LocalScript](/docs/reference/engine/classes/LocalScript.md), or in a [Script](/docs/reference/engine/classes/Script.md) with
[RunContext](/docs/reference/engine/classes/Script.md) of [RunContext.Client](/docs/reference/engine/enums/RunContext.md). Messages
are only visible to that user and aren't automatically filtered or
localized.

*Security: None · Thread Safety: Unsafe · Capabilities: Chat*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `systemMessage` | `string` |  | The system message sent to the [TextChannel](/docs/reference/engine/classes/TextChannel.md). |
| `metadata` | `string` |  | Use to identify system message types, such as the default system messages. |

**Returns:** `TextChatMessage` — A [TextChatMessage](/docs/reference/engine/classes/TextChatMessage.md) with [TextChatMessage.Status](/docs/reference/engine/classes/TextChatMessage.md) property
that indicates the condition of the message.

### Method: TextChannel:SendAsync

**Signature:** `TextChannel:SendAsync(message: string, metadata: string): TextChatMessage`

Sends a [TextChatMessage](/docs/reference/engine/classes/TextChatMessage.md) to the server. Can only be used in a
[LocalScript](/docs/reference/engine/classes/LocalScript.md), or in a [Script](/docs/reference/engine/classes/Script.md) with
[RunContext](/docs/reference/engine/classes/Script.md) of [RunContext.Client](/docs/reference/engine/enums/RunContext.md). Please
note that only messages typed and sent by the user will be delivered.

The `metadata` argument has a limit of 200 characters. If this is called
with a `metadata` argument that has more than 200 characters, the message
will not be sent to other users. Instead, the sender will receive a
[TextChatMessage](/docs/reference/engine/classes/TextChatMessage.md) with the [TextChatMessage.Metadata](/docs/reference/engine/classes/TextChatMessage.md) and
[TextChatMessage.Text](/docs/reference/engine/classes/TextChatMessage.md) properties set to empty strings.

*Yields · Security: None · Thread Safety: Unsafe · Capabilities: Chat*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `message` | `string` |  | The message to send to the [TextChannel](/docs/reference/engine/classes/TextChannel.md). |
| `metadata` | `string` |  | Custom metadata to attach to the message. |

**Returns:** `TextChatMessage` — A [TextChatMessage](/docs/reference/engine/classes/TextChatMessage.md) with [TextChatMessage.Status](/docs/reference/engine/classes/TextChatMessage.md) property
that indicates the condition of the message.

### Method: TextChannel:SetDirectChatRequester

**Signature:** `TextChannel:SetDirectChatRequester(requester: Player): ()`

Sets the [DirectChatRequester](/docs/reference/engine/classes/TextChannel.md) for
the `TextChannel`. This method is only available for use in server
scripts.

Use this API if you are working with [TextChatService](/docs/reference/engine/classes/TextChatService.md) and have a
custom implementation of direct chat outside of the default text channels.

When called on a `TextChannel` that is parented to `TextChatService` and
has no existing `TextSources`, `SetDirectChatRequester` adds the requested
users as a `TextSource` and set the `DirectChatRequester` property for the
channel.

When `DirectChatRequester` is set, only messages between users that can
direct chat with the `DirectChatRequester` are delivered.

*Security: None · Thread Safety: Unsafe · Capabilities: Chat*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `requester` | `Player` |  | The [Player](/docs/reference/engine/classes/Player.md) whose direct-message permissions gate the channel; only users who can send direct messages to this player are delivered messages on the channel. |

**Returns:** `()`

**Set Direct Chat Requester**

Demonstrates [TextChannel:SetDirectChatRequester()](/docs/reference/engine/classes/TextChannel.md).

```lua
local function createWhisperChannel(fromPlayer, toPlayer)
  local whisperChannel = Instance.new("TextChannel")
  whisperChannel:SetDirectChatRequester(fromPlayer)
  whisperChannel:AddUserAsync(toPlayer.UserId)
  -- The TextChannel instance now has two TextSource instances.
  return whisperChannel
end
```

## Events

### Event: TextChannel.MessageReceived

**Signature:** `TextChannel.MessageReceived(incomingMessage: TextChatMessage)`

Like [TextChatService.MessageReceived](/docs/reference/engine/classes/TextChatService.md), fires when
[TextChannel:DisplaySystemMessage()](/docs/reference/engine/classes/TextChannel.md) is invoked on the client, or
when the client receives a valid [TextChannel:SendAsync()](/docs/reference/engine/classes/TextChannel.md) response
from the server. This event is only fired on the client.

If the server's [TextChannel.ShouldDeliverCallback](/docs/reference/engine/classes/TextChannel.md) property is
bound and returns `false`, the client will not fire
[TextChannel.MessageReceived](/docs/reference/engine/classes/TextChannel.md).

Use the [TextChatMessage](/docs/reference/engine/classes/TextChatMessage.md) parameter to get the [TextSource](/docs/reference/engine/classes/TextSource.md)
and the text of the message (with [TextChatMessage.Text](/docs/reference/engine/classes/TextChatMessage.md)).

The [TextChatMessage](/docs/reference/engine/classes/TextChatMessage.md) parameter is the final result of any functions
bound to [TextChatService.OnIncomingMessage](/docs/reference/engine/classes/TextChatService.md) or
[TextChannel.OnIncomingMessage](/docs/reference/engine/classes/TextChannel.md).

*Security: None · Capabilities: Chat*

**Parameters:**

| Name | Type | Description |
|------|------|-------------|
| `incomingMessage` | `TextChatMessage` | The received [TextChatMessage](/docs/reference/engine/classes/TextChatMessage.md). |

## Callbacks

### Callback: TextChannel.OnIncomingMessage

**Signature:** `TextChannel.OnIncomingMessage(message: TextChatMessage): Tuple`

Called when [TextChannel](/docs/reference/engine/classes/TextChannel.md) is receiving an incoming message. Can only
be implemented on the client.

Use this to decorate [TextChatMessages](/docs/reference/engine/classes/TextChatMessage.md). If this
callback returns a [TextChatMessageProperties](/docs/reference/engine/classes/TextChatMessageProperties.md), those properties are
merged with the [TextChatMessage](/docs/reference/engine/classes/TextChatMessage.md) parameter to create a new
[TextChatMessage](/docs/reference/engine/classes/TextChatMessage.md).

When bound to the client sending a message, this callback is run twice;
first when the message is initially sent and received locally, and again
when the client receives the result of the filtered message from the
server.

[TextChannel.OnIncomingMessage](/docs/reference/engine/classes/TextChannel.md) callbacks always run **after** the
[TextChatService.OnIncomingMessage](/docs/reference/engine/classes/TextChatService.md) callback.

This should be defined only once per [TextChannel](/docs/reference/engine/classes/TextChannel.md) in the source
code. Multiple bindings to the same channel will override one another in a
nondeterministic manner.

When [TextChatService:CreateDefaultTextChannels()](/docs/reference/engine/classes/TextChatService.md) is true, those
default [TextChannels](/docs/reference/engine/classes/TextChannel.md) have their
[TextChannel.OnIncomingMessage](/docs/reference/engine/classes/TextChannel.md) callbacks assigned internally in
order to exhibit special default behavior.

*Security: None · Thread Safety: Unsafe · Capabilities: Chat*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `message` | `TextChatMessage` |  | The incoming [TextChatMessage](/docs/reference/engine/classes/TextChatMessage.md). |

**Returns:** `Tuple` — If a [TextChatMessageProperties](/docs/reference/engine/classes/TextChatMessageProperties.md) is returned, those properties
are merged with the [TextChatMessage](/docs/reference/engine/classes/TextChatMessage.md) parameter to create a new
[TextChatMessage](/docs/reference/engine/classes/TextChatMessage.md) with those properties.

### Callback: TextChannel.ShouldDeliverCallback

**Signature:** `TextChannel.ShouldDeliverCallback(message: TextChatMessage, textSource: TextSource): Tuple`

Called for each client when [TextChannel](/docs/reference/engine/classes/TextChannel.md) is receiving an incoming
message to determine whether or not it should be delivered to that client.
Can only be defined on the server.

Once defined, this callback needs to return a truthy value such as `true`,
`1`, or `"hello"` to deliver the message to said client. If the callback
returns anything else (including `nil`), the message won't be delivered to
that client, although the sender will see the message regardless.

The sender can be referenced by [TextChatMessage.TextSource](/docs/reference/engine/classes/TextChatMessage.md), while
the receiver is the `textSource` argument. Note that the sender and
receiver can be the same, as the callback iterates through all possible
receivers.

*Security: None · Thread Safety: Unsafe · Capabilities: Chat*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `message` | `TextChatMessage` |  | The message being sent, which also contains the sender of the message. |
| `textSource` | `TextSource` |  | The [TextSource](/docs/reference/engine/classes/TextSource.md) of the user who will be receiving the message. |

**Returns:** `Tuple` — A truthy value (such as `true`, `1`, or a non-empty string) to deliver
the message to the given client, or a falsy value (including `nil`) to
withhold it from that client.

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