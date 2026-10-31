---
title: "Customize bubble chat"
url: /docs/en-us/chat/bubble-chat
last_updated: 2026-10-30T19:55:38Z
description: "The text chat system allows users to communicate and socialize with each other."
---

# Customize bubble chat

With [TextChatService](/docs/en-us/chat/in-experience-text-chat.md), you can use bubble chat to display customizable speech chat bubbles above user avatars and NPCs. Bubble chat can make your game more visually immersive and help users easily identify messages and their speakers in a contextually relevant manner. This feature is especially useful for games where users need to focus on the content in the meantime communicating with others in a less obtrusive way.

## Enable bubble chat

To enable bubble chat in your game:

1. In the **Explorer** window, select `Class.BubbleChatConfiguration` under `Class.TextChatService`.
2. In the **Properties** window, check the `Class.BubbleChatConfiguration.Enabled` checkbox.

## Bubble customization

After enabling bubble chat, you can customize the appearance and behavior of your chat bubbles to match your game's theme. Use the **Properties** window of `Class.BubbleChatConfiguration` for [basic](#basic-customization) changes like text color and spacing, or implement [advanced](#advanced-customization) customization for bubble background images and other visual adjustments.

Alternatively, add a `Class.LocalScript` in `Class.StarterPlayerScripts` with all your customization settings. This allows the engine to apply your customizations during runtime, overriding the settings in Studio. It's useful for adding special effects to chat bubbles when users trigger certain events or conditions.

### Basic customization

The following table shows common bubble chat customization properties. For a full list of customization properties, see `Class.BubbleChatConfiguration`.

#### Appearance

| Property | Description | Default |
| --- | --- | --- |
| `Class.BubbleChatConfiguration.BackgroundColor3\|BackgroundColor3` | Background color of bubbles in `Datatype.Color3`. | `[250, 250, 250]` |
| `Class.BubbleChatConfiguration.FontFace\|FontFace` | `Datatype.Font` of the bubble text. | `Enum.Font.BuilderSansMedium\|BuilderSansMedium` |
| `Class.BubbleChatConfiguration.TextColor3\|TextColor3` | Color of bubble text in `Datatype.Color3`. | `[57, 59, 61]` |
| `Class.BubbleChatConfiguration.TextSize\|TextSize` | Size of bubble text. | `16` |

#### Behavior

| Property | Description | Default |
| --- | --- | --- |
| `Class.BubbleChatConfiguration.Enabled\|Enabled` | Indicating whether bubble chat is enabled in the game. | `true` (checked) |
| `Class.BubbleChatConfiguration.AdorneeName\|AdorneeName` | String name of the body part or `Class.Attachment` that bubbles attach to; if multiple instances of the same name exist, the system attaches to the first instance found. | `HumanoidRootPart` |
| `Class.BubbleChatConfiguration.BubbleDuration\|BubbleDuration` | Time before a bubble fades out, in seconds. | `30` |
| `Class.BubbleChatConfiguration.BubblesSpacing\|BubblesSpacing` | Vertical space between stacked bubbles, in pixels. | `6` |
| `Class.BubbleChatConfiguration.LocalPlayerStudsOffset\|LocalPlayerStudsOffset` | If adorned to the local player, the offset of bubbles in studs from their adornee, relative to the camera orientation (`Datatype.Vector3`). | `(0, 0, 0)` |
| `Class.BubbleChatConfiguration.MaxDistance\|MaxDistance` | Maximum distance from the camera that bubbles are shown. | `100` |
| `Class.BubbleChatConfiguration.MinimizeDistance\|MinimizeDistance` | Distance from the camera when bubbles turn into a single bubble with an ellipsis (**⋯**) to indicate chatter. | `40` |
| `Class.BubbleChatConfiguration.VerticalStudsOffset\|VerticalStudsOffset` | Extra space between bubbles and their adornee, in studs. | `0` |
| `Class.BubbleChatConfiguration.MaxBubbles\|MaxBubbles` | Maximum number of bubbles displayed before older bubbles disappear. | `3` |

### Advanced customization

For advanced customization of your bubble, add UI objects representing certain aspects of the bubble appearance as children under `Class.BubbleChatConfiguration`, including:

- `Class.ImageLabel` for background image settings.
- `Class.UIGradient` for background gradient settings.
- `Class.UICorner` for the corner shape of bubbles.
- `Class.UIPadding` for the padding space between the text and bubble edges, relative to the parent's normal size.

After adding these objects, you can modify properties of these objects applicable to chat bubbles for advanced bubble customization. The following example `Class.LocalScript` adds a background image and sharp corners to bubbles:

```lua
local TextChatService = game:GetService("TextChatService")

local bubbleChatConfiguration = TextChatService.BubbleChatConfiguration
bubbleChatConfiguration.TailVisible = false
bubbleChatConfiguration.TextColor3 = Color3.fromRGB(220, 50, 50)
bubbleChatConfiguration.FontFace = Font.fromEnum(Enum.Font.LuckiestGuy)

local bubbleUICorner = bubbleChatConfiguration:FindFirstChildOfClass("UICorner")
if not bubbleUICorner then
	bubbleUICorner = Instance.new("UICorner")
	bubbleUICorner.Parent = bubbleChatConfiguration
end
bubbleUICorner.CornerRadius = UDim.new(0, 0)

local bubbleUIPadding = bubbleChatConfiguration:FindFirstChildOfClass("UIPadding")
if not bubbleUIPadding then
	bubbleUIPadding = Instance.new("UIPadding")
	bubbleUIPadding.Parent = bubbleChatConfiguration
end
bubbleUIPadding.PaddingTop = UDim.new(0, 20)
bubbleUIPadding.PaddingRight = UDim.new(0, 10)
bubbleUIPadding.PaddingBottom = UDim.new(0, 15)
bubbleUIPadding.PaddingLeft = UDim.new(0, 10)

local bubbleImageLabel = bubbleChatConfiguration:FindFirstChildOfClass("ImageLabel")
if not bubbleImageLabel then
	bubbleImageLabel = Instance.new("ImageLabel")
	bubbleImageLabel.Parent = bubbleChatConfiguration
end
bubbleImageLabel.Image = "rbxassetid://109157529833093"
bubbleImageLabel.ScaleType = Enum.ScaleType.Slice
bubbleImageLabel.SliceCenter = Rect.new(40, 40, 320, 120)
bubbleImageLabel.SliceScale = 0.5
```

The following tables outline the available `Class.GuiObject` and [appearance modifier](/docs/en-us/ui/appearance-modifiers.md) children along with their valid customization properties:

#### ImageLabel

| Property | Description | Default |
| --- | --- | --- |
| `Class.ImageLabel.Image\|Image` | Asset ID of the bubble background image. | |
| `Class.ImageLabel.ImageColor3\|ImageColor3` | Color tint of the bubble background image in `Datatype.Color3`. | `[255, 255, 255]` |
| `Class.ImageLabel.ImageRectOffset\|ImageRectOffset` | Offset of the image area to be displayed from the top-left in pixels. | `(0, 0)` |
| `Class.ImageLabel.ImageRectSize\|ImageRectSize` | Size of the image area to be displayed in pixels. To display the entire image, set either dimension to `0`. | `(0, 0)` |
| `Class.ImageLabel.ScaleType\|ScaleType` | The scale type for rendering the image when its size is different from the absolute size of the bubble. | `Enum.ScaleType\|Stretch` |
| `Class.ImageLabel.SliceCenter\|SliceCenter` | Slice boundaries of the image if the image is a 9-sliced image. Only applicable when you set `Class.ImageLabel.ScaleType\|ScaleType` as `Enum.ScaleType\|Slice`. | `(0, 0, 0, 0)` |
| `Class.ImageLabel.SliceScale\|SliceScale` | Scale ratio of slice edges if the image is a 9-sliced image. Only applicable when you set `Class.ImageLabel.ScaleType\|ScaleType` as `Enum.ScaleType\|Slice`. | `1` |
| `Class.ImageLabel.TileSize\|TileSize` | Tiling size of the image. Only applicable when you set `Class.ImageLabel.ScaleType\|ScaleType` as `Enum.ScaleType\|Tile`. | `(1, 0, 1, 0)` |

#### UIGradient

| Property | Description | Default |
| --- | --- | --- |
| `Class.UIGradient.Enabled\|Enabled` | Indicating whether the bubble background gradient is enabled. | `false` (unchecked) |
| `Class.UIGradient.Color\|Color` | Color of the background gradient. | `[250, 250, 250]` |
| `Class.UIGradient.Offset\|Offset` | Scalar translation of the gradient from the center of the bubble. | `(0, 0)` |
| `Class.UIGradient.Rotation\|Rotation` | Clockwise rotation, in degrees, of the gradient starts from left to right. | `0` |
| `Class.UIGradient.Transparency\|Transparency` | Transparency of the background gradient. | `(1, 0)` |

#### UICorner

| Property | Description | Default |
| --- | --- | --- |
| `Class.UICorner.CornerRadius\|CornerRadius` | Radius of the bubble corner shape in pixels. | `(0, 12)` |

#### UIPadding

| Property | Description | Default |
| --- | --- | --- |
| `Class.UIPadding.PaddingBottom\|PaddingBottom` | Padding on the bottom. | `Datatype.UDim.new(0,8)` |
| `Class.UIPadding.PaddingLeft\|PaddingLeft` | Padding on the left. | `Datatype.UDim.new(0,8)` |
| `Class.UIPadding.PaddingRight\|PaddingRight` | Padding on the right. | `Datatype.UDim.new(0,8)` |
| `Class.UIPadding.PaddingTop\|PaddingTop` | Padding on the top. | `Datatype.UDim.new(0,8)` |

## Per-bubble customization

You can individually style and modify chat bubble behaviors based on specific conditions in order to override your general settings. For example, you can use chat bubbles to differentiate NPCs and users, highlight critical health status, and apply special effects to messages with pre-defined keywords.

To set per-bubble customization, add a client-side `Class.LocalScript` using `Class.BubbleChatMessageProperties`, which overrides matching properties of `Class.BubbleChatConfiguration`, and the `Class.TextChatService.OnBubbleAdded` callback to specify how to customize each bubble. The callback supplies you with the `Class.TextChatMessage` property as well as the adornee, so you can apply the customization based on attributes associated with users, the chat text content, user character properties, and any special conditions you want to define.

The following basic customization properties are available for per-bubble customization:

| Property | Description | Default |
| --- | --- | --- |
| `Class.BubbleChatConfiguration.BackgroundColor3\|BackgroundColor3` | Background color of bubbles in `Datatype.Color3`. | `(250, 250, 250)` |
| `Class.BubbleChatConfiguration.BackgroundTransparency\|BackgroundTransparency` | Background transparency of bubbles. | `0.1` |
| `Class.BubbleChatConfiguration.FontFace\|FontFace` | `Datatype.Font` of the bubble text. | `Enum.Font.BuilderSansMedium\|BuilderSansMedium` |
| `Class.BubbleChatConfiguration.TextColor3\|TextColor3` | Color of bubble text in `Datatype.Color3`. | `[57, 59, 61]` |
| `Class.BubbleChatConfiguration.TextSize\|TextSize` | Size of bubble text. | `16` |

The following example adds special appearance to VIP users' chat bubbles by checking if a chat message sender has the `IsVIP` attribute:

```lua
local TextChatService = game:GetService("TextChatService")
local Players = game:GetService("Players")

-- Event handler for when a new chat bubble is added to the game
TextChatService.OnBubbleAdded = function(message: TextChatMessage, adornee: Instance)
	-- Check if the chat message has a TextSource (sender) associated with it
	if message.TextSource then
		-- Create a new BubbleChatMessageProperties instance to customize the chat bubble
		local bubbleProperties = Instance.new("BubbleChatMessageProperties")

		-- Get the user who sent the chat message based on their UserId
		local player = Players:GetPlayerByUserId(message.TextSource.UserId)

		if player:GetAttribute("IsVIP") then
			-- If the player is a VIP, customize the chat bubble properties
			bubbleProperties.TextColor3 = Color3.fromHex("#F5CD30")
			bubbleProperties.BackgroundColor3 = Color3.fromRGB(25, 27, 29)
			bubbleProperties.FontFace = Font.fromEnum(Enum.Font.PermanentMarker)
		end
		return bubbleProperties
	end
end
```

All advanced customization options are available for per-bubble customization. Similar to advanced customization for general bubbles, add instances that you want to customize as children of `Class.BubbleChatMessageProperties`. The following example adds a special gradient effect along with other properties to chat bubbles of users with low health status by checking the `Class.Humanoid.Health` property of chat message senders' characters:

```lua
local TextChatService = game:GetService("TextChatService")
local Players = game:GetService("Players")

-- Event handler for when a new chat bubble is added to the game
TextChatService.OnBubbleAdded = function(message: TextChatMessage, adornee: Instance)
	-- Check if the chat message has a TextSource (sender) associated with it
	if message.TextSource then
		-- Get the user who sent the chat message by using their UserId
		local player = Players:GetPlayerByUserId(message.TextSource.UserId)

		-- Find the humanoid in the user's character
		local humanoid = player.Character:FindFirstChildWhichIsA("Humanoid")

		if humanoid and humanoid.Health < 25 then
			-- Create a new BubbleChatMessageProperties instance to customize the chat bubble
			local bubbleProperties :BubbleChatMessageProperties = Instance.new("BubbleChatMessageProperties")

			-- Customize the chat bubble properties for low health condition
			bubbleProperties.BackgroundColor3 = Color3.fromRGB(245, 245, 245)
			bubbleProperties.TextColor3 = Color3.fromRGB(234, 51, 96)
			bubbleProperties.TextSize = 20
			bubbleProperties.FontFace = Font.fromEnum(Enum.Font.DenkOne)

			-- Add a UIGradient as a child to customize the gradient
			local uiGradient : UIGradient = Instance.new("UIGradient")
			uiGradient.Color = ColorSequence.new(Color3.fromRGB(110, 4, 0), Color3.fromRGB(0, 0, 0))
			uiGradient.Rotation = 90
			uiGradient.Parent = bubbleProperties

			return bubbleProperties
		end
	end
end
```

## Manually display bubbles

You might want to display a chat bubble when players haven't sent a message, such as with NPCs. Use the `Class.TextChatService:DisplayBubble` method to manually display a chat bubble.

Customization of these bubbles is the same as the customization of the bubbles that are automatically displayed when Players send messages through TextChannels using the [`Class.TextChatService.OnBubbleAdded` callback](#per-bubble-customization).

> **Success:** To generate speech or other text using an LLM, see the `Class.TextGenerator` class.
### NPC bubbles

Display chat bubbles for non-player characters (NPCs) by calling `Class.TextChatService:DisplayBubble(character, message)`, with the NPC character and the message as parameters. These bubbles are customizable using the `Class.TextChatService.OnBubbleAdded` callback just like any other chat bubble.

`Class.TextChatService:DisplayBubble()` only works on client-side scripts, so be sure to use a `Class.Script` with `Class.BaseScript.RunContext|RunContext` set to `Enum.RunContext.Client`, or a `Class.LocalScript` in an [appropriate container](/docs/en-us/projects/data-model.md#client), such as `Class.StarterPlayerScripts`. If you attach a `Class.ProximityPrompt` to an NPC, a script for displaying a chat bubble might look like this:

```lua
local TextChatService = game:GetService("TextChatService")
local Workspace = game:GetService("Workspace")

local prompt = Workspace.SomeNPC.ProximityPrompt
local head = prompt.Parent:WaitForChild("Head")

prompt.Triggered:Connect(function()
	TextChatService:DisplayBubble(head, "Hello world!")
end)
```
