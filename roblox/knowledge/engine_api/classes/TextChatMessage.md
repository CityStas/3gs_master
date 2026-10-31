---
name: TextChatMessage
last_updated: 2026-10-30T19:55:53Z
inherits:
  - Instance
  - Object
type: class
memory_category: Instances
tags:
  - NotCreatable
summary: "A data object representing a text chat message."
---

# Class: TextChatMessage

> A data object representing a text chat message.

## Description

A data object representing a text chat message.

To learn more about using TextChatMessages, see
[In-Experience Text Chat](/docs/en-us/chat/in-experience-text-chat.md).

## Properties

### Property: TextChatMessage.BubbleChatMessageProperties

```json
{
  "type": "BubbleChatMessageProperties",
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
  "category": "Data",
  "capabilities": [
    "Chat"
  ]
}
```

A reference to the [BubbleChatMessageProperties](/docs/reference/engine/classes/BubbleChatMessageProperties.md) instance that
overrides [BubbleChatConfiguration](/docs/reference/engine/classes/BubbleChatConfiguration.md) properties for this individual
message's chat bubble.

This property is `nil` by default. It is populated when your
[TextChatService.OnBubbleAdded](/docs/reference/engine/classes/TextChatService.md) callback returns a
[BubbleChatMessageProperties](/docs/reference/engine/classes/BubbleChatMessageProperties.md) instance: the returned instance is
stored here on the resulting [TextChatMessage](/docs/reference/engine/classes/TextChatMessage.md). Any properties set
on it take precedence over the shared [BubbleChatConfiguration](/docs/reference/engine/classes/BubbleChatConfiguration.md) when
the message's bubble is rendered.

### Property: TextChatMessage.ChatWindowMessageProperties

```json
{
  "type": "ChatWindowMessageProperties",
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
  "category": "Data",
  "capabilities": [
    "Chat"
  ]
}
```

A reference to the [ChatWindowMessageProperties](/docs/reference/engine/classes/ChatWindowMessageProperties.md) instance that
overrides [ChatWindowConfiguration](/docs/reference/engine/classes/ChatWindowConfiguration.md) properties for this individual
message as displayed in the chat window.

This property is `nil` by default. It is populated when your
[TextChatService.OnChatWindowAdded](/docs/reference/engine/classes/TextChatService.md) callback returns a
[ChatWindowMessageProperties](/docs/reference/engine/classes/ChatWindowMessageProperties.md) instance, typically created with
[ChatWindowConfiguration:DeriveNewMessageProperties()](/docs/reference/engine/classes/ChatWindowConfiguration.md): the returned
instance is stored here on the resulting [TextChatMessage](/docs/reference/engine/classes/TextChatMessage.md). Any
properties set on it take precedence over the shared
[ChatWindowConfiguration](/docs/reference/engine/classes/ChatWindowConfiguration.md) when the message is rendered.

### Property: TextChatMessage.MessageId

```json
{
  "type": "string",
  "access": "ReadWrite",
  "security": {
    "read": "None",
    "write": "None"
  },
  "serialization": {
    "can_load": false,
    "can_save": false
  },
  "thread_safety": "ReadSafe",
  "category": "Data",
  "capabilities": [
    "Chat"
  ]
}
```

A unique identifier for the [TextChatMessage](/docs/reference/engine/classes/TextChatMessage.md).

### Property: TextChatMessage.Metadata

```json
{
  "type": "string",
  "access": "ReadWrite",
  "security": {
    "read": "None",
    "write": "None"
  },
  "serialization": {
    "can_load": false,
    "can_save": false
  },
  "thread_safety": "ReadSafe",
  "category": "Data",
  "capabilities": [
    "Chat"
  ]
}
```

A general purpose field for storing miscellaneous data about the
`TextChatMessage`. The second argument of [TextChannel:SendAsync()](/docs/reference/engine/classes/TextChannel.md)
and [TextChannel:DisplaySystemMessage()](/docs/reference/engine/classes/TextChannel.md) is used to populate this
field.

Use this field to apply additional formatting for special messages within
[TextChatService.OnIncomingMessage](/docs/reference/engine/classes/TextChatService.md) and
[TextChannel.OnIncomingMessage](/docs/reference/engine/classes/TextChannel.md) callbacks.

```lua
local Players = game:GetService("Players")
local TextChatService = game:GetService("TextChatService")

local customChannel: TextChannel = Instance.new("TextChannel")
customChannel.Parent = TextChatService:WaitForChild("TextChannels")

customChannel.OnIncomingMessage = function(message: TextChatMessage)
  if string.find(message.Metadata, "Error") then
    local overrideProperties = Instance.new("TextChatMessageProperties")
    overrideProperties.Text = string.format("<font color='rgb(255,0,0)'>%s</font>", message.Text)
    return overrideProperties
  elseif string.find(message.Metadata, "Info") then
    local overrideProperties = Instance.new("TextChatMessageProperties")
    overrideProperties.Text = string.format("<font color='rgb(0, 255, 150)'>%s</font>", message.Text)
    return overrideProperties
  end

  return nil
end

Players.LocalPlayer.CharacterAdded:Connect(function()
  customChannel:DisplaySystemMessage("This is an error!", "Game.Error.Generic")
  customChannel:DisplaySystemMessage("Could not find save data!", "Game.Error.SaveDataNotFound")

  customChannel:DisplaySystemMessage("You won the game!", "Game.Info.Win")
  customChannel:DisplaySystemMessage("You lost the game!", "Game.Info.Lose")
end)
```

As follows is a reference of the default system messages emitted by the
chat system:

| Metadata | Description |
| --- | --- |
| `Roblox.ChatTranslation.ChatWindow.SystemMessage` | Indicates that the system may translate chat messages for the player. |
| `Roblox.Notification.Friend.Joined` | Displayed when one of the player's friends join the experience. |
| `Roblox.MessageStatus.Warning.Floodchecked` | Displayed when the player's sent message was rate limited by the server. |
| `Roblox.MessageStatus.Warning.TextFilterFailed` | Displayed when the player's sent message could not be displayed due to a text filtering issue. |
| `Roblox.MessageStatus.Warning.InvalidPrivacySettings` | Displayed when the player's privacy settings prevent them from sending a message. |
| `Roblox.MessageStatus.Warning.MessageTooLong` | Displayed when the player sends a message with content that is too long. |
| `Roblox.MessageStatus.Warning.Unknown` | Displays when the system fails to send the player's message for an unknown reason. |
| `Roblox.Help.Info` | Displays the response from the `RBXHelpCommand` [TextChatCommand](/docs/reference/engine/classes/TextChatCommand.md). |
| `Roblox.Version.Info` | Displays the response from the `RBXVersionCommand` [TextChatCommand](/docs/reference/engine/classes/TextChatCommand.md). |
| `Roblox.Team.Success.NowInTeam` | Displayed when the player's team changes. |
| `Roblox.Team.Error.CannotTeamChatIfNotInTeam` | Displayed when the player triggers the `RBXTeamCommand` [TextChatCommand](/docs/reference/engine/classes/TextChatCommand.md) without being on a [Team](/docs/reference/engine/classes/Team.md). |
| `Roblox.Whisper.Info.Success` | Displayed when the player successfully starts a whisper conversation. |
| `Roblox.Whisper.Welcome.Sent` | Displayed when entering a whisper [TextChannel](/docs/reference/engine/classes/TextChannel.md). |
| `Roblox.Whisper.Error.CannotWhisperToSelf` | An error response from the `RBXWhisperCommand` [TextChatCommand](/docs/reference/engine/classes/TextChatCommand.md). |
| `Roblox.Whisper.Error.TargetDoesNotExist` | An error response from the `RBXWhisperCommand` [TextChatCommand](/docs/reference/engine/classes/TextChatCommand.md). |
| `Roblox.Whisper.Error.TooManyMatches` | An error response from the `RBXWhisperCommand` [TextChatCommand](/docs/reference/engine/classes/TextChatCommand.md). |
| `Roblox.Whisper.Error.Unknown` | An error response from the `RBXWhisperCommand` [TextChatCommand](/docs/reference/engine/classes/TextChatCommand.md). |
| `Roblox.Emote.Error.DoesNotExist` | An error response from the `RBXEmoteCommand` [TextChatCommand](/docs/reference/engine/classes/TextChatCommand.md). |
| `Roblox.Emote.Error.UserEmotesNotEnabled` | An error response from the `RBXEmoteCommand` [TextChatCommand](/docs/reference/engine/classes/TextChatCommand.md). |
| `Roblox.Emote.Error.TemporarilyUnavailable` | An error response from the `RBXEmoteCommand` [TextChatCommand](/docs/reference/engine/classes/TextChatCommand.md). |
| `Roblox.Emote.Error.NotSupported` | An error response from the `RBXEmoteCommand` [TextChatCommand](/docs/reference/engine/classes/TextChatCommand.md). |
| `Roblox.Emote.Error.SwitchToR15` | An error response from the `RBXEmoteCommand` [TextChatCommand](/docs/reference/engine/classes/TextChatCommand.md). |
| `Roblox.Emote.Error.AnimationPlaying` | An error response from the `RBXEmoteCommand` [TextChatCommand](/docs/reference/engine/classes/TextChatCommand.md). |
| `Roblox.Mute.Error.PlayerNotFound` | An error response from the `RBXMuteCommand` [TextChatCommand](/docs/reference/engine/classes/TextChatCommand.md). |
| `Roblox.Mute.Error.MultipleMatches` | An error response from the `RBXMuteCommand` [TextChatCommand](/docs/reference/engine/classes/TextChatCommand.md). |
| `Roblox.Mute.Error.CannotMuteSelf` | An error response from the `RBXMuteCommand` [TextChatCommand](/docs/reference/engine/classes/TextChatCommand.md). |
| `Roblox.Mute.Info.Success` | An success response from the `RBXMuteCommand` [TextChatCommand](/docs/reference/engine/classes/TextChatCommand.md). |
| `Roblox.Unmute.Error.PlayerNotFound` | An error response from the `RBXUnmuteCommand` [TextChatCommand](/docs/reference/engine/classes/TextChatCommand.md). |
| `Roblox.Unmute.Error.MultipleMatches` | An error response from the `RBXUnmuteCommand` [TextChatCommand](/docs/reference/engine/classes/TextChatCommand.md). |
| `Roblox.Unmute.Error.CannotMuteSelf` | An error response from the `RBXUnmuteCommand` [TextChatCommand](/docs/reference/engine/classes/TextChatCommand.md). |
| `Roblox.Unmute.Info.Success` | An success response from the `RBXUnmuteCommand` [TextChatCommand](/docs/reference/engine/classes/TextChatCommand.md). |

### Property: TextChatMessage.PrefixText

```json
{
  "type": "string",
  "access": "ReadWrite",
  "security": {
    "read": "None",
    "write": "None"
  },
  "serialization": {
    "can_load": false,
    "can_save": false
  },
  "thread_safety": "ReadSafe",
  "category": "Data",
  "capabilities": [
    "Chat"
  ]
}
```

A prefix to add to a user's message. This supports Rich Text, so
developers can set custom properties for this text to support chat tags.

By default, [TextChatMessage.PrefixText](/docs/reference/engine/classes/TextChatMessage.md) is the name of the
[TextSource](/docs/reference/engine/classes/TextSource.md), which is the [Player.DisplayName](/docs/reference/engine/classes/Player.md) of the user
associated with the [TextSource](/docs/reference/engine/classes/TextSource.md) via [TextSource.UserId](/docs/reference/engine/classes/TextSource.md).

### Property: TextChatMessage.Status

```json
{
  "type": "TextChatMessageStatus",
  "access": "ReadWrite",
  "security": {
    "read": "None",
    "write": "None"
  },
  "serialization": {
    "can_load": false,
    "can_save": false
  },
  "thread_safety": "ReadSafe",
  "category": "Data",
  "capabilities": [
    "Chat"
  ]
}
```

Indicates the status of the [TextChatMessage](/docs/reference/engine/classes/TextChatMessage.md).

### Property: TextChatMessage.Text

```json
{
  "type": "string",
  "access": "ReadWrite",
  "security": {
    "read": "None",
    "write": "None"
  },
  "serialization": {
    "can_load": false,
    "can_save": false
  },
  "thread_safety": "ReadSafe",
  "category": "Data",
  "capabilities": [
    "Chat"
  ]
}
```

The filtered text message for the user. Different users may receive
different strings from this property based on filtering rules. It can be
an empty string.

### Property: TextChatMessage.TextChannel

```json
{
  "type": "TextChannel",
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
  "category": "Data",
  "capabilities": [
    "Chat"
  ]
}
```

A reference to the origin [TextChannel](/docs/reference/engine/classes/TextChannel.md).

### Property: TextChatMessage.TextSource

```json
{
  "type": "TextSource",
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
  "category": "Data",
  "capabilities": [
    "Chat"
  ]
}
```

A reference to the origin [TextSource](/docs/reference/engine/classes/TextSource.md).

### Property: TextChatMessage.Timestamp

```json
{
  "type": "DateTime",
  "access": "ReadWrite",
  "security": {
    "read": "None",
    "write": "None"
  },
  "serialization": {
    "can_load": false,
    "can_save": false
  },
  "thread_safety": "ReadSafe",
  "category": "Data",
  "capabilities": [
    "Chat"
  ]
}
```

A timestamp of when the message was originally sent.

### Property: TextChatMessage.Translation

```json
{
  "type": "string",
  "access": "ReadWrite",
  "security": {
    "read": "None",
    "write": "None"
  },
  "serialization": {
    "can_load": false,
    "can_save": false
  },
  "thread_safety": "ReadSafe",
  "category": "Data",
  "capabilities": [
    "Chat"
  ]
}
```

Represents translated and filtered text messages based on users'
localization settings. The system doesn't translate messages between users
with the same localization settings or using languages without the text
filter support, so this property can be an empty string if no translation
happens. For customization, see
[Customizing Translated Messages](/docs/en-us/chat/chat-window.md).

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