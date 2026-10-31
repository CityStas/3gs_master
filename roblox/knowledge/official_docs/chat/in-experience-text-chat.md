---
title: "Text chat overview"
url: /docs/en-us/chat/in-experience-text-chat
last_updated: 2026-10-30T19:55:38Z
description: "TextChatService lets players communicate with each other using text-based messages in live sessions."
---

# Text chat overview

Roblox offers text-based messaging between players in live sessions through `Class.TextChatService`, a singleton class responsible for managing the overall chat system, including chat message filtering, moderation, and user permissions. This service has its standard functionality and also provides a set of methods and events for extending and customizing chat, such as delivering messages based on [customized requirements](#conditionally-deliver-messages), adding special permissions or moderation to specific players, and creating [custom commands](/docs/en-us/chat/examples/custom-text-chat-commands.md) to execute specific actions.

> **Warning:** When [platform-integrated chat](/docs/en-us/chat/platform-integrated-chat.md) is enabled, custom chat must use Roblox's native systems, and message content isn't accessible in code.
## UI configuration

`Class.TextChatService` provides a default UI that can be customized to fit your game's needs. Disable any of these configurations to hide its associated UI element. If desired, you can also replace these UI elements with custom interfaces:

- `Class.ChatWindowConfiguration`
- `Class.ChatInputBarConfiguration`
- `Class.ChannelTabsConfiguration`
- `Class.BubbleChatConfiguration`

For more information, see [Chat window](/docs/en-us/chat/chat-window.md) and [Bubble chat](/docs/en-us/chat/bubble-chat.md).

## Channels, messages, and commands

- `Class.TextChannel` — Text channels pass user-sent messages from the client to the server, which then displays them to other users based on permissions. Text channels must be parented to `Class.TextChatService` in order to function.
  > **Info:** If `Class.TextChatService.CreateDefaultTextChannels` is set to `true`, the service automatically creates two text channels, `RBXGeneral` and `RBXSystem`. You can manually create additional `Class.TextChannel` instances and parent them to `Class.TextChatService`, as well.
  > **Warning:** Having multiple `Class.TextChannel|TextChannels` with the same name can cause unintended behavior with the default [chat window](/docs/en-us/chat/chat-window.md).
- `Class.TextSource` — A user in a `Class.TextChannel`. Text sources are directly parented to the `Class.TextChannel` when `Class.TextChannel:AddUserAsync()|AddUserAsync()` is called. Text sources contains detailed permissions of a user in the channel, such as their ability to send messages. If a single user is in multiple text channels, they are associated with multiple text sources.
- `Class.TextChatMessage` — A message in a text channel. Chat messages contain basic information such as the sender of the message, the original message, the filtered message, and the creation timestamp.
- `Class.TextChatCommand` — Lets users invoke specific actions or behaviors by sending messages that match the `Class.TextChatCommand.PrimaryAlias|PrimaryAlias` or `Class.TextChatCommand.SecondaryAlias|SecondaryAlias` properties. Chat commands must be parented to `Class.TextChatService` in order to function.
  > **Info:** If `Class.TextChatService.CreateDefaultCommands` is set to `true`, default chat commands will be created automatically. You can manually create additional `Class.TextChatCommand` instances and parent them to `Class.TextChatService`, as well.

## Chat flowchart

Text chat uses the [client‑server](/docs/en-us/projects/client-server.md) model, with a **sending client**, the **server**, and **receiving clients**.

![A flowchart for in-game text chat.](../assets/players/in-experience-text-chat/Chat-Workflow.png)

1. A player sends a message from their local device, triggering the `Class.TextChannel:SendAsync()` method. This method processes the message and determines whether it's a chat command or a regular chat message.
  - If the message is a chat command, it fires the `Class.TextChatCommand.Triggered` event to perform the defined action. No further steps are required.
  - If the message is a regular chat message, it fires the `Class.TextChatService.SendingMessage` event to display the message to the sender on the sending client. At the same time, `Class.TextChannel:SendAsync()` passes the message to the server.
2. The server fires `Class.TextChannel.ShouldDeliverCallback` to determine whether to deliver the message to other players based on permissions and Roblox community filtering requirements.
3. If `Class.TextChannel.ShouldDeliverCallback` determines that message is eligible to deliver to other players, the server applies any filters and fires `Class.TextChannel.OnIncomingMessage` twice:
  1. The first time is on the sending client and signals that the server is processing the message through the `Class.TextChatService.MessageReceived` event. This event replaces the local message on the sending client with the processed message from the server. The message is identical if the original didn't require filtering.
  2. The second time is on the receiving clients, which triggers the `Class.TextChatService.MessageReceived` event to display the message to other players.

## Text chat hooks and callbacks

The `Class.TextChatService` API encourages a clear separation on the appearance and delivery of chat messages. Multiple instances of the text chat system provide hooks and callbacks to format in centralized, clear locations.

> **Warning:** All callbacks are expected to be non-yielding functions. Yielding or waiting for a response in a callback blocks the chat system and can cause unexpected behavior.
![A flowchart of the TextChatService callbacks order](../assets/players/in-experience-text-chat/TextChatService-Callbacks.png)

| Callback | Return Value |
| --- | --- |
| `Class.TextChannel.ShouldDeliverCallback` | boolean |
| `Class.TextChatService.OnIncomingMessage` | `Class.TextChatMessageProperties` |
| `Class.TextChannel.OnIncomingMessage` | `Class.TextChatMessageProperties` |
| `Class.TextChatService.OnBubbleAdded` | `Class.BubbleChatMessageProperties` |
| `Class.TextChatService.OnChatWindowAdded` | `Class.ChatWindowMessageProperties` |

### Conditionally deliver messages

The `Class.TextChannel.ShouldDeliverCallback` callback should be defined on the server only. The callback is fired for each `Class.TextSource` child of the text channel when a message is sent to determine whether the message should be delivered. This callback can be used to implement custom message delivery logic that may depend on additional gameplay context, such as:

- [Proximity-based chat](/docs/en-us/chat/examples/proximity-chat.md) where users can only send messages to those close to them.
- Preventing users with certain attributes from sending messages to others.

### Customize message display

The default `Class.TextChatService` UI relies on [rich text](/docs/en-us/ui/rich-text.md) to format and customize how messages are displayed. You can use the following callbacks to format messages before they are displayed to users, for example to add colors or [chat tags](/docs/en-us/chat/examples/group-chat-tags.md) to user names or format message content.

The following callbacks are called on every `Class.TextChatMessage` that is about to be displayed, which lets you customize chat window appearance based on the `Class.TextChannel`, `Class.TextSource`, or `Class.TextChatMessage` content. When a client sends a message, these callbacks are called once when the message is sent to the server and the `Class.TextChatMessage.Status` value will be `Enum.TextChatMessageStatus.Sending`. Once the message is received by the server and is being delivered to other users, the sender client receives the message again with an updated `Enum.TextChatMessageStatus` value.

- `Class.TextChatService.OnIncomingMessage` — This callback should be defined on the client only. The callback is fired when a message is received, either from the server or if the local client has just sent a message. The callback is called on every `Class.TextChatMessage` received from all `Class.TextChannel` instances and is the first to process the message before it is displayed to the user.
- `Class.TextChannel.OnIncomingMessage` — This callback should be defined on the client only. The callback is fired when a message is received from the server. The callback is called on every `Class.TextChatMessage` received from the `Class.TextChannel`. Default `Class.TextChannel` instances created from `Class.TextChatService.CreateDefaultTextChannels` have this callback defined and can be overwritten.
- `Class.TextChatService.OnBubbleAdded` — This callback should be defined on the client only. Use it to customize the appearance of chat bubbles independent of the appearance of the message in the chat window UI.
- `Class.TextChatService.OnChatWindowAdded` — This callback should be defined on the client only. Use it to customize the appearance of chat messages in the chat window UI independent of the appearance of the message in chat bubbles.

## Migrate from legacy chat

This section assists you in migrating from the legacy chat system by providing alternative methods for implementing common chat functionalities and behaviors using `Class.TextChatService`.

1. In the [Explorer](/docs/en-us/studio/explorer.md) window, select `Class.TextChatService`.
2. In the [Properties](/docs/en-us/studio/properties.md) window, find the `Class.TextChatService.ChatVersion|ChatVersion` dropdown and select `Enum.ChatVersion|TextChatService`.

### Basic functionalities

Though both systems share the same basic chat functionalities, `Class.TextChatService` implementations are in general more sustainable and easier to iterate on.

| Functionality | Legacy chat | TextChatService | Differences |
| --- | --- | --- | --- |
| Send a chat message | `Class.Players:Chat()` | `Class.TextChannel:SendAsync()` | The `Class.TextChannel:SendAsync()\|SendAsync()` method supports more advanced chat features, such as rich text formatting and message priority. It also includes built-in filtering to help prevent inappropriate messages from being sent. |
| Implement messaging callbacks | `Class.Chat:InvokeChatCallback()`<br>`Class.Chat:RegisterChatCallback()` | `Class.TextChatService.SendingMessage`<br>`Class.TextChatService.OnIncomingMessage` | The legacy chat system binds a function to chat system events for delivering messages. The two methods of `TextChatService` offer better flexibility and customization. |
| Add custom chat commands | `ChatService/ChatCommand` module | `Class.TextChatCommand` | `TextChatService` has a dedicated class for text commands rather than using a legacy chat module. |
| Display a system message | `Class.StarterGui:SetCore()` using `ChatMakeSystemMessage` | `Class.TextChannel:DisplaySystemMessage()` | The `Class.TextChannel.OnIncomingMessage` callback can return a `Class.TextChatMessageProperties` instance to customize the message appearance. |
| Disable chat | `ChatWindow/ChatSettings` module for hiding the chat window | `Class.ChatWindowConfiguration.Enabled` | |

### Message filtering

`Class.TextChatService` automatically filters chat messages based on each player's account information, so you don't need to manually implement text filtering for all kinds of chat messages.

| Functionality | Legacy chat | TextChatService |
| --- | --- | --- |
| Filter chat message for individual player | `Class.Chat:FilterStringAsync()` | Automatic |
| Filter broadcasting messages | `Class.Chat:FilterStringForBroadcast()` | Automatic |

### Window and bubble chat

Both the [chat window](/docs/en-us/chat/chat-window.md) and [bubble chat](/docs/en-us/chat/bubble-chat.md) behavior and customization options of `Class.TextChatService` are identical to those of the legacy chat system. As the legacy chat system only allows customization using chat modules or the `Class.Players` container, the service provides dedicated classes (`Class.ChatWindowConfiguration` and `Class.BubbleChatConfiguration`) to manage all chat window and bubble chat properties. Additionally, you can easily adjust and preview your bubble chat appearance and behavior properties using Studio settings instead of having to script them all.

| Functionality | Legacy chat | TextChatService |
| --- | --- | --- |
| Enable Chat Window | `Class.Chat.LoadDefaultChat`<br>`Class.Players.ClassicChat` | `Class.ChatWindowConfiguration.Enabled` |
| Enable Bubble Chat | `Class.Chat.BubbleChatEnabled`<br>`Class.Players.BubbleChat` | `Class.BubbleChatConfiguration.Enabled` |
| Set Chat Window Properties | `Class.Players:SetChatStyle()` | `Class.ChatWindowConfiguration` |
| Set Bubble Chat Properties | `Class.Chat:SetBubbleChatSettings()`<br>`Class.Chat.BubbleChatSettingsChanged()`<br>`Class.Players.BubbleChat`<br>`Class.Players:SetChatStyle()` | `Class.BubbleChatConfiguration` |
| Enable NPC Bubbles | `Class.Chat:Chat()` | `Class.TextChatService:DisplayBubble()` |

### Migrate speaker "extra data"

The legacy Lua chat system allowed developers to use `SetExtraData` on the `Speaker` class. This data was used to format the name color, chat color, or to apply name tags for a given speaker.

```lua
-- An example of setting extra data on a speaker in the legacy chat system
ChatService.SpeakerAdded:Connect(function(playerName)
	local speaker = ChatService:GetSpeaker(playerName)
	speaker:SetExtraData("NameColor", Color3.fromRGB(255, 255, 55))
	speaker:SetExtraData("ChatColor", Color3.fromRGB(212, 175, 55))
	speaker:SetExtraData("Tags", {{TagText = "YourTagName", TagColor = Color3.fromRGB(0, 255, 0)}, {TagText = "OtherTagName", TagColor = Color3.fromRGB(255, 0, 0)}})
end)
```

`Class.TextChatService` does not have a direct equivalent to `SetExtraData`. Instead, use [callbacks](#text-chat-hooks-and-callbacks) such as `Class.TextChatService.OnWindowAdded|OnWindowAdded` to customize the appearance of messages using rich text based on the `Class.TextSource` of the message.

The following is an example of emulating legacy Lua chat's "extra data" by accessing attributes on `Class.Player` objects:

```lua
local Players = game:GetService("Players")

Players.PlayerAdded:Connect(function(player)
	player:SetAttribute("NameColor", Color3.fromRGB(255, 255, 55))
	player:SetAttribute("ChatColor", Color3.fromRGB(212, 175, 55))
	player:SetAttribute("isYourTag", true)
	player:SetAttribute("isOtherTag", true)
end)
```

Then you can use the `Class.TextChatService.OnChatWindowAdded|OnChatWindowAdded` callback to customize the appearance of the chat window based on the attributes set on the player:

```lua
local TextChatService = game:GetService("TextChatService")
local Players = game:GetService("Players")

TextChatService.OnChatWindowAdded = function(textChatMessage)
	local textSource = textChatMessage.TextSource
	if textSource then
		local player = Players:GetPlayerByUserId(textSource.UserId)
		if player then
			local overrideProperties = TextChatService.ChatWindowConfiguration:DeriveNewMessageProperties()
			overrideProperties.PrefixText = textChatMessage.PrefixText
			overrideProperties.Text = textChatMessage.Text

			local nameColor = player:GetAttribute("NameColor")
			if nameColor and typeof(nameColor) == "Color3" then
				overrideProperties.PrefixTextProperties.TextColor3 = nameColor
			end

			local chatColor = player:GetAttribute("ChatColor")
			if chatColor and typeof(chatColor) == "Color3" then
				overrideProperties.TextColor3 = chatColor
			end

			local isYourTag = player:GetAttribute("isYourTag")
			if isYourTag == true then
				overrideProperties.PrefixText = \`<font color='rgb(0, 255, 0)'>[YourTag]</font> {overrideProperties.PrefixText}\`
			end

			local isOtherTag = player:GetAttribute("isOtherTag")
			if isOtherTag == true then
				overrideProperties.PrefixText = \`<font color='rgb(255, 0, 0)'>[OtherTag]</font> {overrideProperties.PrefixText}\`
			end

			return overrideProperties
		end
	end

	return nil
end
```
