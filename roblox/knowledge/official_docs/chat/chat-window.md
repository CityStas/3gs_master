---
title: "Customize the chat window"
url: /docs/en-us/chat/chat-window
last_updated: 2026-10-30T19:55:38Z
description: "Customize the chat window and message UI of your in-game text chat."
---

# Customize the chat window

The [in-game text chat](/docs/en-us/chat/in-experience-text-chat.md) system, powered by `Class.TextChatService`, allows players to easily communicate and socialize with each other in live games. In addition to supporting the default text chat, you can [customize](#chat-window-configuration) the front‑end user interface.

## Chat window configuration

The overall chat window consists of:

- Chat window
- Input bar
- Channel tabs (optional)

![Core components of the text chat window.](../assets/players/in-experience-text-chat/Chat-Window-Components.jpg)

The channel tabs are disabled by default and each component can be toggled on and off in Studio or through scripting:

#### Studio

In the [Explorer](/docs/en-us/studio/explorer.md) window, expand the `Class.TextChatService` branch and select `Class.ChatWindowConfiguration`, `Class.ChatInputBarConfiguration`, or `Class.ChannelTabsConfiguration`. Then enable or disable the component in the [Properties](/docs/en-us/studio/properties.md) window.

#### Scripting

From a client script within `Class.StarterPlayerScripts`, enable each component as desired:

```lua
local TextChatService = game:GetService("TextChatService")

local ChatWindowConfiguration = TextChatService:FindFirstChildOfClass("ChatWindowConfiguration")
local ChatInputBarConfiguration = TextChatService:FindFirstChildOfClass("ChatInputBarConfiguration")
local ChannelTabsConfiguration = TextChatService:FindFirstChildOfClass("ChannelTabsConfiguration")

-- Enable chat window
if ChatWindowConfiguration then
	ChatWindowConfiguration.Enabled = true
end
-- Enable input bar
if ChatInputBarConfiguration then
	ChatInputBarConfiguration.Enabled = true
end
-- Enable channel tabs
if ChannelTabsConfiguration then
	ChannelTabsConfiguration.Enabled = true
end
```

When `Class.ChannelTabsConfiguration` is enabled, each default `Class.TextChannel` appears in a tab as outlined in the following table. In addition, each custom `Class.TextChannel` creates a tab corresponding to the channel's `Class.Instance.Name|Name` property.

| Default channel | Tab name |
| --- | --- |
| `RBXGeneral` | **General** |
| `RBXSystem` | **General** (combined into a single tab with `RBXGeneral`) |
| `RBXTeam` | **Team** |
| `RBXWhisper` | User name of the other player |

### Window appearance

Appearance of the overall chat window is customizable through `Class.ChatWindowConfiguration`.

![ChatWindowConfiguration instance in Explorer hierarchy.](../assets/studio/explorer/TextChatService-ChatWindowConfiguration.png)

| Property | Description | Default |
| --- | --- | --- |
| `Class.ChatWindowConfiguration.BackgroundColor3\|BackgroundColor3` | `Datatype.Color3` background color of the chat window. | `[25, 27, 29]` |
| `Class.ChatWindowConfiguration.BackgroundTransparency\|BackgroundTransparency` | Transparency of the chat window's background. | `0.3` |
| `Class.ChatWindowConfiguration.Enabled\|Enabled` | Whether to show the default chat window. Set to `false` to hide. | `true` |
| `Class.ChatWindowConfiguration.FontFace\|FontFace` | `Datatype.Font` of chat window text. | `Enum.Font.BuilderSansMedium\|BuilderSansMedium` |
| `Class.ChatWindowConfiguration.TextColor3\|TextColor3` | `Datatype.Color3` of chat window text. | `[255, 255, 255]` |
| `Class.ChatWindowConfiguration.TextSize\|TextSize` | Size of chat window text. | `14` |
| `Class.ChatWindowConfiguration.TextStrokeColor3\|TextStrokeColor3` | `Datatype.Color3` of the stroke for chat window text. | `[0, 0, 0]` |
| `Class.ChatWindowConfiguration.TextStrokeTransparency\|TextStrokeTransparency` | Transparency of the stroke for chat window text. | `0.5` |
| `Class.ChatWindowConfiguration.HorizontalAlignment\|HorizontalAlignment` | Horizontal alignment of the chat window. | `Enum.HorizontalAlignment.Left\|Left` |
| `Class.ChatWindowConfiguration.VerticalAlignment\|VerticalAlignment` | Vertical alignment of the chat window. | `Enum.VerticalAlignment.Top\|Top` |
| `Class.ChatWindowConfiguration.HeightScale\|HeightScale` | Height scale of the chat window relative to the screen size. | `1` |
| `Class.ChatWindowConfiguration.WidthScale\|WidthScale` | Width scale of the chat window relative to the screen size. | `1` |

### Input bar appearance

Appearance of the chat input bar is customizable through `Class.ChatInputBarConfiguration`.

![ChatInputBarConfiguration instance in Explorer hierarchy.](../assets/studio/explorer/TextChatService-ChatInputBarConfiguration.png)

| Property | Description | Default |
| --- | --- | --- |
| `Class.ChatInputBarConfiguration.BackgroundColor3\|BackgroundColor3` | `Datatype.Color3` background color of the chat input bar. | `[25, 27, 29]` |
| `Class.ChatInputBarConfiguration.BackgroundTransparency\|BackgroundTransparency` | Transparency of the chat input bar's background. | `0.2` |
| `Class.ChatInputBarConfiguration.FontFace\|FontFace` | `Datatype.Font` of chat input text. | `Enum.Font.BuilderSansMedium\|BuilderSansMedium` |
| `Class.ChatInputBarConfiguration.PlaceholderColor3\|PlaceholderColor3` | `Datatype.Color3` of placeholder chat input text. | `[178, 178, 178]` |
| `Class.ChatInputBarConfiguration.TextColor3\|TextColor3` | `Datatype.Color3` of player-entered chat input text. | `[255, 255, 255]` |
| `Class.ChatInputBarConfiguration.TextSize\|TextSize` | Size of chat input text. | `14` |
| `Class.ChatInputBarConfiguration.TextStrokeColor3\|TextStrokeColor3` | `Datatype.Color3` stroke color of chat input text. | `[0, 0, 0]` |
| `Class.ChatInputBarConfiguration.TextStrokeTransparency\|TextStrokeTransparency` | Transparency of the stroke for chat input text. | `0.5` |
| `Class.ChatInputBarConfiguration.AutocompleteEnabled\|AutocompleteEnabled` | Whether the text chat system shows autocomplete options for emojis and [commands](/docs/en-us/chat/in-experience-text-chat.md). Emojis are autocompleted by typing `:` followed by non-whitespace characters, while commands are autocompleted by typing `/`. | `true` |
| `Class.ChatInputBarConfiguration.KeyboardKeyCode\|KeyboardKeyCode` | Additional key players can press to trigger focusing on the default chat input bar. | `Enum.KeyCode.Slash\|Slash` |

### Channel tabs appearance

Appearance of the **channel tabs** is customizable through `Class.ChannelTabsConfiguration`.

![ChannelTabsConfiguration instance in Explorer hierarchy.](../assets/studio/explorer/TextChatService-ChannelTabsConfiguration.png)

| Property | Description | Default |
| --- | --- | --- |
| `Class.ChannelTabsConfiguration.BackgroundColor3\|BackgroundColor3` | `Datatype.Color3` background color of the channel tabs. | `[25, 27, 29]` |
| `Class.ChannelTabsConfiguration.BackgroundTransparency\|BackgroundTransparency` | Transparency of the channel tabs' background. | `0` |
| `Class.ChannelTabsConfiguration.HoverBackgroundColor3\|HoverBackgroundColor3` | `Datatype.Color3` background color of tabs when hovering over them. | `[125, 125, 125]` |
| `Class.ChannelTabsConfiguration.FontFace\|FontFace` | `Datatype.Font` for the text in channel tabs. | `Enum.Font.BuilderSansBold\|BuilderSansBold` |
| `Class.ChannelTabsConfiguration.TextColor3\|TextColor3` | `Datatype.Color3` of text in an unselected tab. | `[175, 175, 175]` |
| `Class.ChannelTabsConfiguration.SelectedTabTextColor3\|SelectedTabTextColor3` | `Datatype.Color3` of text in a selected tab. | `[255, 255, 255]` |
| `Class.ChannelTabsConfiguration.TextSize\|TextSize` | Size of the text in channel tabs. | `18` |
| `Class.ChannelTabsConfiguration.TextStrokeColor3\|TextStrokeColor3` | `Datatype.Color3` stroke color of the text in channel tabs. | `[0, 0, 0]` |
| `Class.ChannelTabsConfiguration.TextStrokeTransparency\|TextStrokeTransparency` | Transparency of the stroke for text in channel tabs. | `1` |

## Customize messages

You can customize the appearance of chat message bodies and prefixes using `Class.ChatWindowMessageProperties` and `Class.TextChatService.OnChatWindowAdded` callbacks without overriding the existing UI. The customization options let you modify the appearance of chat messages to match your game's theme, and you can also sort or highlight messages from different user groups by coloring prefixes or adding [chat tags](/docs/en-us/chat/examples/group-chat-tags.md).

> **Info:**`Class.ChatWindowMessageProperties` and `Class.TextChatService.OnChatWindowAdded|OnChatWindowAdded` only affect the appearance of messages in the chat window. To customize chat bubbles, see [Bubble Chat](/docs/en-us/chat/bubble-chat.md).
### Color user names

When a user sends a chat message, their `Class.Player.DisplayName|DisplayName` displays as the prefix portion of the message. By default, each user's name is colored according to their `Class.Player.TeamColor` but you can change the colors of chat names using `Class.ChatWindowMessageProperties|ChatWindowMessageProperties` and `Class.TextChatService.OnChatWindowAdded|OnChatWindowAdded`. The following `Class.LocalScript` in `Class.StarterPlayerScripts` assigns a predetermined color to each user, picking randomly from a table of RGB colors.

![Colored user name in the chat window.](../assets/players/in-experience-text-chat/Chat-User-Name-Colored.png)

```lua
local TextChatService = game:GetService("TextChatService")

local chatWindowConfiguration = TextChatService.ChatWindowConfiguration

local nameColors = {
	Color3.fromRGB(255, 0, 0),
	Color3.fromRGB(0, 255, 0),
	Color3.fromRGB(0, 0, 255),
	Color3.fromRGB(255, 255, 0),
}

TextChatService.OnChatWindowAdded = function(message: TextChatMessage)
	local properties = chatWindowConfiguration:DeriveNewMessageProperties()

	local textSource = message.TextSource
	if textSource then
		local index: number = (textSource.UserId % #nameColors) + 1
		local randomColor: Color3 = nameColors[index]

    	properties.PrefixTextProperties = chatWindowConfiguration:DeriveNewMessageProperties()
		properties.PrefixTextProperties.TextColor3 = randomColor
	end

	return properties
end
```

You can also apply color and transparency gradients to color message prefixes using `Class.UIGradient`.

![Gradient user name in the chat window.](../assets/players/in-experience-text-chat/Chat-User-Name-Gradient.png)

```lua
local TextChatService = game:GetService("TextChatService")

local chatWindowConfiguration = TextChatService.ChatWindowConfiguration

local gradient = Instance.new("UIGradient")
gradient.Color = ColorSequence.new{
	ColorSequenceKeypoint.new(0, Color3.fromRGB(255, 0, 0)),
	ColorSequenceKeypoint.new(0.5, Color3.fromRGB(255, 255, 0)),
	ColorSequenceKeypoint.new(1, Color3.fromRGB(255, 0, 255))
}

TextChatService.OnChatWindowAdded = function(message: TextChatMessage)
	local properties = chatWindowConfiguration:DeriveNewMessageProperties()

	local textSource = message.TextSource
	if textSource then
    	properties.PrefixTextProperties = chatWindowConfiguration:DeriveNewMessageProperties()
		gradient:Clone().Parent = properties.PrefixTextProperties
	end

	return properties
end
```

### Rich text customization

Rich text [font color tags](/docs/en-us/ui/rich-text.md#supported-tags) can be used to format chat messages, helpful if you want to apply formatting to very specific parts of the message. Note that rich text does not support gradients, but the following code sample shows how you can move the user name (stored in `Class.TextChatMessage.PrefixText`) into the message body and then apply rich text tagging to only the name portion.

![Rich text customization of user name in the chat window.](../assets/players/in-experience-text-chat/Chat-Rich-Text.png)

```lua
local TextChatService = game:GetService("TextChatService")
local Players = game:GetService("Players")

local chatWindowConfiguration = TextChatService.ChatWindowConfiguration

local gradient = Instance.new("UIGradient")
gradient.Color = ColorSequence.new{
	ColorSequenceKeypoint.new(0, Color3.fromRGB(255, 0, 0)),
	ColorSequenceKeypoint.new(0.5, Color3.fromRGB(255, 255, 0)),
	ColorSequenceKeypoint.new(1, Color3.fromRGB(255, 0, 255))
}

TextChatService.OnChatWindowAdded = function(message: TextChatMessage)
	local properties = chatWindowConfiguration:DeriveNewMessageProperties()

	if message.TextSource then
		properties.PrefixText = "[VIP]"
		properties.Text = string.format("<font color='#00ffff'>%s</font>", message.PrefixText) .. " " .. message.Text

		properties.PrefixTextProperties = chatWindowConfiguration:DeriveNewMessageProperties()
		gradient:Clone().Parent = properties.PrefixTextProperties
	end

	return properties
end
```

## Messages from non‑player sources

When `Class.TextChatService.CreateDefaultTextChannels` is `true`, one of the default text channels is the `RBXSystem` channel. The default chat scripts automatically display system messages in this channel. You can customize the appearance of these messages using the `Class.TextChannel.OnIncomingMessage` callback.

You might want to customize or alter the system messages that are automatically emitted by the chat system. Since the default system messages are localized for users, you should reference them by `Class.TextChatMessage.Metadata` in your [text chat callbacks](/docs/en-us/chat/in-experience-text-chat.md#text-chat-hooks-and-callbacks) if you wish to customize their appearance. For example, you could use `Class.TextChatMessage.Metadata|Metadata` to identify system messages, error messages, or messages from specific systems in your game.

### System

To deliver a system message to the local player, such as "speech" from a public address system, call `Class.TextChannel:DisplaySystemMessage()|DisplaySystemMessage()` from the default `RBXGeneral` channel with a prefix before the player's display name.

```lua
local Players = game:GetService("Players")
local TextChatService = game:GetService("TextChatService")

local player = Players.LocalPlayer
local generalChannel: TextChannel = TextChatService:WaitForChild("TextChannels").RBXGeneral

local PREFIX = "[Guide] Welcome "

-- Send "system message" to player with their display name appended
generalChannel:DisplaySystemMessage(PREFIX .. player.DisplayName)
```

![Image showing a basic system message in the chat window.](../assets/players/in-experience-text-chat/Chat-System.jpg) ### NPC/object

You can also stylize non-player dialogue and add [chat bubbles](/docs/en-us/chat/bubble-chat.md) to make it appear like messages are coming from an NPC or object within the 3D world.

```lua
local TextChatService = game:GetService("TextChatService")
local Workspace = game:GetService("Workspace")

local generalChannel: TextChannel = TextChatService:WaitForChild("TextChannels").RBXGeneral

TextChatService.OnIncomingMessage = function(textChatMessage: TextChatMessage)
	local properties = Instance.new("TextChatMessageProperties")

	-- Check for system messages that contain metadata
	if not textChatMessage.TextSource and textChatMessage.Metadata ~= "" then

		-- Add prefix to make message look like it was sent by a player
		properties.PrefixText = string.format("<font color='#%s'>%s: </font>", "#50C999", textChatMessage.Metadata)

		-- Add bubble chat
		TextChatService:DisplayBubble(Workspace.Statue, textChatMessage.Text)
	end

	return properties
end

local message = "Welcome! I will be your guide."
local speakerName = "Ancient Knight"
generalChannel:DisplaySystemMessage(message, speakerName)
```

![Image showing a knight statue NPC broadcasting a chat message to the chat window, along with a chat bubble above its head.](../assets/players/in-experience-text-chat/Chat-NPC.jpg)
