---
name: MessagingService
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
summary: "Allows servers of the same experience to communicate with each other."
---

# Class: MessagingService

> Allows servers of the same experience to communicate with each other.

## Description

**MessagingService** allows servers of the same experience to communicate with
each other in real time, typically within 1-2 seconds, using topics. Topics
are developer‑defined strings (1–80 characters) that servers use to send and
receive messages.

Delivery is best effort and not guaranteed. Make sure to architect your
experience so delivery failures are not critical.

[Cross-Server Messaging](/docs/en-us/cloud-services/cross-server-messaging.md)
explores how to communicate between servers in greater detail.

If you want to publish ad-hoc messages to live game servers, or publish across
experiences, you can use the
[Open Cloud APIs](/docs/en-us/cloud/guides/usage-messaging.md).

#### Limitations

Note that these limits are subject to change.

| Limit | Maximum |
| --- | --- |
| **Size of message** | 1kB |
| **Messages sent per game server** | 600 + 240 * (number of players in this game server) per minute |
| **Messages received per topic** | (40 + 80 * number of servers) per minute |
| **Messages received for entire game** | (400 + 200 * number of servers) per minute |
| **Subscriptions allowed per game server** | 20 + 8 * (number of players in this game server) |
| **Subscribe requests per game server** | 240 requests per minute |

## Methods

### Method: MessagingService:PublishAsync

**Signature:** `MessagingService:PublishAsync(topic: string, message: Variant): ()`

This function sends the provided message to all subscribers to the topic,
triggering their registered callbacks to be invoked.

Yields until the message is received by the backend.

*Yields · Security: None · Thread Safety: Unsafe · Capabilities: ServerCommunication*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `topic` | `string` |  | Determines where the message is sent. |
| `message` | `Variant` |  | The data to include in the message. |

**Returns:** `()`

### Method: MessagingService:SubscribeAsync

**Signature:** `MessagingService:SubscribeAsync(topic: string, callback: Function): RBXScriptConnection`

This function registers a callback to begin listening to the given topic.
The callback is invoked when a topic receives a message. It can be called
multiple times for the same topic.

#### Callback

The callback is invoked with a single argument, a table with the following
entries:

| Field | Summary |
| --- | --- |
| **Data** | Developer supplied payload |
| **Sent** | Unix time in seconds at which the message was sent |

It yields until the subscription is properly registered and returns a
connection object.

To unsubscribe, call [Disconnect()](/docs/reference/engine/datatypes/RBXScriptConnection.md) on the
returned object. Once called, the callback should never be invoked.
Killing the script containing the connections also causes the underlying
connect to be unsubscribed.

See also [MessagingService:PublishAsync()](/docs/reference/engine/classes/MessagingService.md) which sends the provided
message to all subscribers to the topic, triggering their registered
callbacks to be invoked.

*Yields · Security: None · Thread Safety: Unsafe · Capabilities: ServerCommunication*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `topic` | `string` |  | Determines where to listen for messages. |
| `callback` | `Function` |  | Function to be invoked whenever a message is received. |

**Returns:** `RBXScriptConnection` — Connection that can be used to unsubscribe from the topic.

**Subscribing to Cross Server Messages**

This example demonstrates how to use [MessagingService:SubscribeAsync()](/docs/reference/engine/classes/MessagingService.md)
to listen to a topic for cross-server chat within a game universe.

When a player joins, the example subscribes to the topic
_player-<player.UserId>_. When a message is sent with this topic, the
connected callback executes and prints _Received message for <player.Name">_.
It also disconnects the connection when the player's
[ancestry changes](/docs/reference/engine/classes/Player.md).

In order for this to work as expected it must be placed in a server `Script`.

```lua
local MessagingService = game:GetService("MessagingService")
local Players = game:GetService("Players")

local function onPlayerAdded(player)
	--subscribe to the topic
	local topic = "player-" .. player.UserId
	local connection = MessagingService:SubscribeAsync(topic, function(message)
		print("Received message for", player.Name, message.Data)
	end)

	player.AncestryChanged:Connect(function()
		-- unsubscribe from the topic
		connection:Disconnect()
	end)
end

Players.PlayerAdded:Connect(onPlayerAdded)
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