---
name: Chat
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
summary: "Houses the Luau code responsible for running the legacy chat system."
---

# Class: Chat

> Houses the Luau code responsible for running the legacy chat system.

## Description

The **Chat** service houses the Luau code responsible for running the
[legacy chat system](/docs/en-us/chat/in-experience-text-chat.md#migrate-from-legacy-chat).
Similar to [StarterPlayerScripts](/docs/reference/engine/classes/StarterPlayerScripts.md), default objects like
[Scripts](/docs/reference/engine/classes/Script.md) and [ModuleScripts](/docs/reference/engine/classes/ModuleScript.md) are inserted
into the service.

## Properties

### Property: Chat.BubbleChatEnabled

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
  "category": "Behavior",
  "capabilities": [
    "Chat"
  ]
}
```

If true, entering a message in the chat will result in a chat bubble
popping up above the player's [Player.Character](/docs/reference/engine/classes/Player.md). This behavior can
either be enabled by directly ticking this checkbox in Studio, or by using
a [LocalScript](/docs/reference/engine/classes/LocalScript.md):

```lua
local ChatService = game:GetService("Chat")
ChatService.BubbleChatEnabled = true
```

This must be done on the client, toggling this value in a server-side
[Script](/docs/reference/engine/classes/Script.md) will have no effect.

### Property: Chat.LoadDefaultChat

```json
{
  "type": "boolean",
  "access": "ReadOnly",
  "security": {
    "read": "None",
    "write": "NotAccessibleSecurity"
  },
  "serialization": {
    "can_load": true,
    "can_save": true
  },
  "thread_safety": "ReadSafe",
  "category": "Behavior",
  "capabilities": [
    "Chat"
  ]
}
```

When set to `true` (the default), the engine inserts the default Luau chat
system scripts (such as `ChatScript` and `BubbleChat`) into the `Chat`
service at runtime. Setting this to `false` prevents the legacy chat
framework from loading, which is useful if you are replacing it with a
custom chat implementation or migrating to [TextChatService](/docs/reference/engine/classes/TextChatService.md).

This property defaults to `true`. It is not writable by scripts at
runtime.

## Methods

### Method: Chat:CanUserChatAsync

**Signature:** `Chat:CanUserChatAsync(userId: int64): boolean`

Returns whether the player identified by `userId` is permitted to use
in-game text chat. The check evaluates the player's chat privacy mode,
third-party platform restrictions, and any active moderation timeouts.

On the server, the specified player must be connected to the current
server; otherwise the call errors. On the client, the method must be
called only for the local player's [Player.UserId](/docs/reference/engine/classes/Player.md).

*Yields · Security: None · Thread Safety: Unsafe · Capabilities: Chat*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `userId` | `int64` |  |  |

**Returns:** `boolean`

### Method: Chat:CanUsersChatAsync

**Signature:** `Chat:CanUsersChatAsync(userIdFrom: int64, userIdTo: int64): boolean`

Returns whether two players are permitted to exchange chat messages with
each other. The method evaluates user blocking, age-based communication
constraints, and chat privacy mode compatibility between the two accounts.

This method can only be called from server-side [Scripts](/docs/reference/engine/classes/Script.md).
Both players must be connected to the current server; otherwise the call
errors.

*Yields · Security: None · Thread Safety: Unsafe · Capabilities: Chat*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `userIdFrom` | `int64` |  |  |
| `userIdTo` | `int64` |  |  |

**Returns:** `boolean`

### Method: Chat:Chat

**Signature:** `Chat:Chat(partOrCharacter: Instance, message: string, color?: ChatColor): ()`

The Chat function fires the [Chat.Chatted](/docs/reference/engine/classes/Chat.md) event with the parameters
specified in this method.

By default, there is a [LocalScript](/docs/reference/engine/classes/LocalScript.md) inside of each player's
[PlayerScripts](/docs/reference/engine/classes/PlayerScripts.md) object named _BubbleChat_, which causes a
dialog-like billboard to appear above the _partOrCharacter_ when the
chatted event is fired.

_Note:_ Since dialogs are controlled by a LocalScript, you will not be
able to see any dialogs created from this method unless you are running in
_Play Solo_ mode.

*Security: None · Thread Safety: Unsafe · Capabilities: Chat*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `partOrCharacter` | `Instance` |  | An instance that is the part or character which the _BubbleChat_ dialog should appear above. |
| `message` | `string` |  | The message string being chatted. |
| `color` | `ChatColor` | `Blue` | An [ChatColor](/docs/reference/engine/enums/ChatColor.md) specifying the color of the chatted message. |

**Returns:** `()`

**Chat:Chat**

The below example would create a part in Workspace and cause it to exclaim
"Blame John!"

```lua
local ChatService = game:GetService("Chat")

local part = Instance.new("Part")
part.Anchored = true
part.Parent = workspace

ChatService:Chat(part, "Blame John!", "Red")
```

### Method: Chat:FilterStringAsync

**Signature:** `Chat:FilterStringAsync(stringToFilter: string, playerFrom: Player, playerTo: Player): string`

**Partial Deprecation Warning**: Calling this function from the client
using a [LocalScript](/docs/reference/engine/classes/LocalScript.md) is deprecated, and will be disabled in the
future. Text filtering should be done from a [Script](/docs/reference/engine/classes/Script.md) on the server
using the similarly-named [TextService:FilterStringAsync()](/docs/reference/engine/classes/TextService.md), which
uses a different set of parameters and return type.

Games that do not properly filter player-generated text might be subject
to moderation action. Please be sure a game properly filters text before
publishing it.

**FilterStringAsync** filters a string using filtering that is appropriate
for the sending and receiving player. If the filtered string is to be used
for a persistent message, such as the name of a shop, writing on a plaque,
etc, then the function should be called with the author as both the sender
and receiver.

This function should be used **every time** a player can enter custom text
in **any context**, most commonly using a [TextBox](/docs/reference/engine/classes/TextBox.md). Some examples
of text to be filtered:

- Custom chat messages
- Custom character names
- Names for a shop in a tycoon-style game

*Yields · Security: None · Thread Safety: Unsafe · Capabilities: Chat*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `stringToFilter` | `string` |  | The raw string to be filtered, exactly as entered by the player. |
| `playerFrom` | `Player` |  | The author of the text. |
| `playerTo` | `Player` |  | The intended recipient of the provided text; use the author if the text is persistent (see description). |

**Returns:** `string`

### Method: Chat:FilterStringForBroadcast

**Signature:** `Chat:FilterStringForBroadcast(stringToFilter: string, playerFrom: Player): string`

Filters a string sent from _playerFrom_ for broadcast to no particular
target. The filtered message has more restrictions than
[Chat:FilterStringAsync()](/docs/reference/engine/classes/Chat.md).

Some examples of where this method could be used:

- Message walls
- Cross-server shouts
- User-created signs

Calling FilterString from [LocalScripts](/docs/reference/engine/classes/LocalScript.md) is deprecated
and will be disabled in the future. Text filtering should be done from
server-side [Scripts](/docs/reference/engine/classes/Script.md) using FilterStringAsync.

_Note:_ A game not using this filter function for custom chat or other
user generated text may be subjected to moderation action.

*Yields · Security: None · Thread Safety: Unsafe · Capabilities: Chat*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `stringToFilter` | `string` |  | Message string being filtered. |
| `playerFrom` | `Player` |  | Instance of the player sending the message. |

**Returns:** `string` — Filtered message string.

**Chat:FilterStringForBroadcast**

The following example shows a simple way to use the FilterStringForBroadcast
function. The example uses the message variable as the _stringToFilter_
argument and the local player as the _playerFrom_ argument.

The example then prints the result of the filtering function,
_FilteredString_.

```lua
local Players = game:GetService("Players")
local Chat = game:GetService("Chat")

local playerFrom = Players.LocalPlayer
local message = "Hello world!"

-- Filter the string and store the result in the 'FilteredString' variable
local filteredString = Chat:FilterStringForBroadcast(message, playerFrom)

print(filteredString)
```

**Expected output:** Hello world!

### Method: Chat:InvokeChatCallback

**Signature:** `Chat:InvokeChatCallback(callbackType: ChatCallbackType, callbackArguments: Tuple): Tuple`

InvokeChatCallback will call a function registered by
[RegisterChatCallback](/docs/reference/engine/classes/Chat.md), given the
ChatCallbackType enum and the arguments to send the function. It will
return the result of the registered function, or raise an error if no
function has been registered.

This function is called by the Luau Chat System so that chat callbacks may
be registered to change the behavior of certain features. Unless you are
replacing the default Luau Chat System with your own, you should not need
to call this function. You can read about the different callback functions
at [Chat:RegisterChatCallback()](/docs/reference/engine/classes/Chat.md).

*Security: None · Thread Safety: Unsafe · Capabilities: Chat*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `callbackType` | `ChatCallbackType` |  | The type of callback to invoke. |
| `callbackArguments` | `Tuple` |  | The arguments that will be sent to the registered callback function. |

**Returns:** `Tuple` — The values returned by the function registered to the given
ChatCallbackType.

### Method: Chat:RegisterChatCallback

**Signature:** `Chat:RegisterChatCallback(callbackType: ChatCallbackType, callbackFunction: Function): ()`

RegisterChatCallback binds a function to some chat system event in order
to affect the behavior of the Luau chat system. The first argument
determines the event (using the [ChatCallbackType](/docs/reference/engine/enums/ChatCallbackType.md) enum) to which the
second argument, the function, shall be bound. The default Luau chat
system uses [InvokeChatCallback](/docs/reference/engine/classes/Chat.md) to invoke
registered functions. Attempting to register a server- or client- only
callback on a peer that isn't a server or client respectively will raise
an error. The following sections describe in what ways registered
functions will be used.

#### OnCreatingChatWindow

Client-only. Invoked before the client constructs the chat window. Must
return a table of settings to be merged into the information returned by
the ChatSettings module.

#### OnClientFormattingMessage

Client-only. Invoked before the client displays a message (whether it is a
player chat message, system message, or /me command). This function is
invoked with the message object and may (or may not) return a table to be
merged into `message.ExtraData`.

#### OnClientSendingMessage

Not invoked at this time.

#### OnServerReceivingMessage

Server-only. Invoked when the server receives a message from a speaker
(note that speakers may not necessarily be a [Player](/docs/reference/engine/classes/Player.md) chatting).
This callback is called with the Message object. The function can make
changes to the Message object to change the manner in which the message is
processed. **The Message object must be returned for this callback to do
anything.** Setting this callback can allow the server to, for example:

- Set `message.ShouldDeliver` to false in order to cancel delivery of the
  message to players (useful for implementing a chat exclusion list)
- Get/set the speaker's name color (`message.ExtraData.NameColor`, a
  Color3) on a message-by-message basis

*Security: None · Thread Safety: Unsafe · Capabilities: Chat*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `callbackType` | `ChatCallbackType` |  | The callback to which the function shall be registered (this determines in what way the function is called). |
| `callbackFunction` | `Function` |  | The function to call when the callback is invoked using Chat:InvokeChatCallback. |

**Returns:** `()`

### Method: Chat:SetBubbleChatSettings

**Signature:** `Chat:SetBubbleChatSettings(settings: Variant): ()`

This function customizes various settings of the in-game bubble chat.

Before using this, make sure that bubble chat is enabled by setting
[Chat.BubbleChatEnabled](/docs/reference/engine/classes/Chat.md) to true.

The settings argument is a table where the keys are the names of the
settings you want to edit and the values are what you want to change these
settings to. Note that you don't have to include all of them in the
settings argument, omitting some will result in them keeping their default
value.

This function is client-side only, attempting to call it on the server
will trigger an error.

*Security: None · Thread Safety: Unsafe · Capabilities: Chat*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `settings` | `Variant` |  | A settings table. |

**Returns:** `()`

**Customize visual aspects**

When run from a `LocalScript`, this snippet will make all the chat bubbles
appear with bigger text under a different font and a light blue background.
Note that all the other settings will keep their default value.

```lua
local ChatService = game:GetService("Chat")

ChatService:SetBubbleChatSettings({
	BackgroundColor3 = Color3.fromRGB(180, 210, 228),
	TextSize = 20,
	Font = Enum.Font.Cartoon,
})
```

**Restore default settings**

If you want to reset the bubble chat to its default look, you can call this
function with an empty table, because any setting you omit from the argument
will result in it returning to its default value:

```lua
local ChatService = game:GetService("Chat")

ChatService:SetBubbleChatSettings({})
```

### Method: Chat:FilterStringForPlayerAsync

**Signature:** `Chat:FilterStringForPlayerAsync(stringToFilter: string, playerToFilterFor: Player): string`

> **Deprecated:** This item has been superseded by [Chat:FilterStringAsync()](/docs/reference/engine/classes/Chat.md) and [Chat:FilterStringForBroadcast()](/docs/reference/engine/classes/Chat.md) which should be used in all new work

The FilterStringForPlayerAsync function filters a string appropriate to
the given player's age settings, so they see what is appropriate to them.
This function will only work if called from a [Script](/docs/reference/engine/classes/Script.md) on the
server. If called on a client it will fail.

*Yields · Security: None · Thread Safety: Unsafe · Capabilities: Chat*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `stringToFilter` | `string` |  | String being filtered. |
| `playerToFilterFor` | `Player` |  | Player that the string is being filtered for. |

**Returns:** `string` — Filtered string result.

## Events

### Event: Chat.Chatted

**Signature:** `Chat.Chatted(part: Instance, message: string, color: ChatColor)`

Fires when [Chat:Chat()](/docs/reference/engine/classes/Chat.md) is called. The event passes the part or
character the message is associated with, the message string, and the
[ChatColor](/docs/reference/engine/enums/ChatColor.md). When fired on the server, the event replicates to all
connected clients. The default `BubbleChat` [LocalScript](/docs/reference/engine/classes/LocalScript.md) listens
for this event and displays a chat bubble above the specified part or
character.

*Security: None · Capabilities: Chat*

**Parameters:**

| Name | Type | Description |
|------|------|-------------|
| `part` | `Instance` |  |
| `message` | `string` |  |
| `color` | `ChatColor` |  |

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