---
title: "UI animation/tweens"
url: /docs/en-us/ui/animation
last_updated: 2026-10-30T19:56:02Z
description: "Explains how to animate GuiObjects using the process of tweening."
---

# UI animation/tweens

In animation, **tweening** is the process of generating intermediate frames between two key points in a sequence. When designing a user interface, you can use tweening to transition a `Class.GuiObject` smoothly from one state to another, such as:

- Smoothly increasing the size of a button when a user selects it.
- Sliding UI menus in and out from the screen edges.
- Gradually animating a health bar between two widths when a user receives a health boost.

## Single-property tweens

### Position

To tween the **position** of a `Class.GuiObject`:

1. Set the `Class.GuiObject.AnchorPoint|AnchorPoint` for the object.
2. Determine `Datatype.UDim2` coordinates for the object's target position, using the **scale** parameters of `Datatype.UDim2` instead of exact pixel values so that the object tweens to the exact center of the screen.
3. Pass a `Datatype.TweenInfo` and the target position to `Class.TweenService:Create()`.
4. Play the tween with `Class.Tween:Play()`.

The following code snippet moves an `Class.ImageLabel` within a `Class.ScreenGui` to the exact center of the screen:

```lua
local TweenService = game:GetService("TweenService")
local Players = game:GetService("Players")

local PlayerGui = Players.LocalPlayer:WaitForChild("PlayerGui")
local ScreenGui = PlayerGui:WaitForChild("ScreenGui")
local object = ScreenGui:WaitForChild("ImageLabel")

object.AnchorPoint = Vector2.new(0.5, 0.5)

local targetPosition = UDim2.new(0.5, 0, 0.5, 0)

local tweenInfo = TweenInfo.new(2)
local tween = TweenService:Create(object, tweenInfo, {Position = targetPosition})

tween:Play()
```

### Size

To tween the **size** of a `Class.GuiObject`:

1. Determine `Datatype.UDim2` coordinates for the object's target size, using the **scale** parameters of `Datatype.UDim2` instead of exact pixel values so that the object tweens to a relative percentage of the screen size.
2. Attach a `Class.UIAspectRatioConstraint` to the object to maintain its designed aspect ratio when tweening.
3. Pass a `Datatype.TweenInfo` and the target size to `Class.TweenService:Create()`.
4. Play the tween with `Class.Tween:Play()`.

The following code snippet scales an `Class.ImageLabel` within a `Class.ScreenGui` to 40% of the screen width or height (whichever is smaller) from the object's center anchor point:

```lua
local TweenService = game:GetService("TweenService")
local Players = game:GetService("Players")

local PlayerGui = Players.LocalPlayer:WaitForChild("PlayerGui")
local ScreenGui = PlayerGui:WaitForChild("ScreenGui")
local object = ScreenGui:WaitForChild("ImageLabel")

object.AnchorPoint = Vector2.new(0.5, 0.5)

local aspectRatioConstraint = Instance.new("UIAspectRatioConstraint")
aspectRatioConstraint.Parent = object

local targetSize = UDim2.new(0.4, 0, 0.4, 0)

local tweenInfo = TweenInfo.new(2)
local tween = TweenService:Create(object, tweenInfo, {Size = targetSize})

tween:Play()
```

### Rotation

To tween the **rotation** of a `Class.GuiObject`:

1. Set the `Class.GuiObject.AnchorPoint|AnchorPoint` for the object to rotate around.
2. Determine the target `Class.GuiObject.Rotation|Rotation` for the object.
3. Pass a `Datatype.TweenInfo` and the target rotation to `Class.TweenService:Create()`.
4. Play the tween with `Class.Tween:Play()`.

```lua
local TweenService = game:GetService("TweenService")
local Players = game:GetService("Players")

local PlayerGui = Players.LocalPlayer:WaitForChild("PlayerGui")
local ScreenGui = PlayerGui:WaitForChild("ScreenGui")
local object = ScreenGui:WaitForChild("ImageLabel")

object.AnchorPoint = Vector2.new(0.5, 0.5)

local targetRotation = 45

local tweenInfo = TweenInfo.new(2)
local tween = TweenService:Create(object, tweenInfo, {Rotation = targetRotation})

tween:Play()
```

### Transparency

Multiple properties control UI transparency, depending on the object type. You can tween each of these properties individually or combined through a [multi-property tween](#multi-property-tweens). Alternatively, you can tween an object's overall transparency by placing it inside a `Class.CanvasGroup` and tweening the group's `Class.CanvasGroup.GroupTransparency|GroupTransparency`.

| UI Object | Properties |
| --- | --- |
| `Class.Frame` | `Class.GuiObject.BackgroundTransparency\|BackgroundTransparency` |
| `Class.TextLabel` | `Class.GuiObject.BackgroundTransparency\|BackgroundTransparency`, `Class.TextLabel.TextTransparency\|TextTransparency`, `Class.TextLabel.TextStrokeTransparency\|TextStrokeTransparency` |
| `Class.TextButton` | `Class.GuiObject.BackgroundTransparency\|BackgroundTransparency`, `Class.TextButton.TextTransparency\|TextTransparency`, `Class.TextButton.TextStrokeTransparency\|TextStrokeTransparency` |
| `Class.ImageLabel` | `Class.GuiObject.BackgroundTransparency\|BackgroundTransparency`, `Class.ImageLabel.ImageTransparency\|ImageTransparency` |
| `Class.ImageButton` | `Class.GuiObject.BackgroundTransparency\|BackgroundTransparency`, `Class.ImageButton.ImageTransparency\|ImageTransparency` |

> **Info:** As a modern alternative to `Class.TextLabel.TextStrokeTransparency` and `Class.TextButton.TextStrokeTransparency`, you can tween stroke transparency on a `Class.UIStroke` object as outlined in [Stroke](#stroke).

```lua
local TweenService = game:GetService("TweenService")
local Players = game:GetService("Players")

local PlayerGui = Players.LocalPlayer:WaitForChild("PlayerGui")
local ScreenGui = PlayerGui:WaitForChild("ScreenGui")
local object = ScreenGui:WaitForChild("ImageLabel")

local targetTransparency = 0.8

local tweenInfo = TweenInfo.new(2)
local tween = TweenService:Create(object, tweenInfo, {ImageTransparency = targetTransparency})

tween:Play()
```

```lua
local TweenService = game:GetService("TweenService")
local Players = game:GetService("Players")

local PlayerGui = Players.LocalPlayer:WaitForChild("PlayerGui")
local ScreenGui = PlayerGui:WaitForChild("ScreenGui")
local canvasGroup = ScreenGui:WaitForChild("CanvasGroup")

local targetTransparency = 0.8

local tweenInfo = TweenInfo.new(2)
local tween = TweenService:Create(canvasGroup, tweenInfo, {GroupTransparency = targetTransparency})

tween:Play()
```

### Color

Multiple properties control UI color, depending on the object type. You can tween each of these properties individually or combined through a [multi-property tween](#multi-property-tweens). Alternatively, you can tween an object's overall color by placing it inside a `Class.CanvasGroup` and tweening the group's `Class.CanvasGroup.GroupColor3|GroupColor3`.

| UI Object | Properties |
| --- | --- |
| `Class.Frame` | `Class.GuiObject.BackgroundColor3\|BackgroundColor3`, `Class.GuiObject.BorderColor3\|BorderColor3` |
| `Class.TextLabel` | `Class.GuiObject.BackgroundColor3\|BackgroundColor3`, `Class.GuiObject.BorderColor3\|BorderColor3`, `Class.TextLabel.TextColor3\|TextColor3`, `Class.TextLabel.TextStrokeColor3\|TextStrokeColor3` |
| `Class.TextButton` | `Class.GuiObject.BackgroundColor3\|BackgroundColor3`, `Class.GuiObject.BorderColor3\|BorderColor3`, `Class.TextButton.TextColor3\|TextColor3`, `Class.TextButton.TextStrokeColor3\|TextStrokeColor3` |
| `Class.ImageLabel` | `Class.GuiObject.BackgroundColor3\|BackgroundColor3`, `Class.GuiObject.BorderColor3\|BorderColor3`, `Class.ImageLabel.ImageColor3\|ImageColor3` |
| `Class.ImageButton` | `Class.GuiObject.BackgroundColor3\|BackgroundColor3`, `Class.GuiObject.BorderColor3\|BorderColor3`, `Class.ImageButton.ImageColor3\|ImageColor3` |

> **Info:** As a modern alternative to `Class.GuiObject.BorderColor3`, `Class.TextLabel.TextStrokeColor3`, and `Class.TextButton.TextStrokeColor3`, you can tween stroke color on a `Class.UIStroke` object as outlined in [Stroke](#stroke).

```lua
local TweenService = game:GetService("TweenService")
local Players = game:GetService("Players")

local PlayerGui = Players.LocalPlayer:WaitForChild("PlayerGui")
local ScreenGui = PlayerGui:WaitForChild("ScreenGui")
local object = ScreenGui:WaitForChild("ImageLabel")

local targetColor = Color3.fromRGB(255, 0, 0)

local tweenInfo = TweenInfo.new(2)
local tween = TweenService:Create(object, tweenInfo, {ImageColor3 = targetColor})

tween:Play()
```

```lua
local TweenService = game:GetService("TweenService")
local Players = game:GetService("Players")

local PlayerGui = Players.LocalPlayer:WaitForChild("PlayerGui")
local ScreenGui = PlayerGui:WaitForChild("ScreenGui")
local canvasGroup = ScreenGui:WaitForChild("CanvasGroup")

local targetColor = Color3.fromRGB(255, 0, 0)

local tweenInfo = TweenInfo.new(2)
local tween = TweenService:Create(canvasGroup, tweenInfo, {GroupColor3 = targetColor})

tween:Play()
```

### Stroke

Multiple properties control UI borders, depending on the object type.

| UI object | Properties |
| --- | --- |
| `Class.Frame` | `Class.GuiObject.BorderSizePixel\|BorderSizePixel`, `Class.GuiObject.BorderColor3\|BorderColor3` |
| `Class.TextLabel` | `Class.GuiObject.BorderSizePixel\|BorderSizePixel`, `Class.GuiObject.BorderColor3\|BorderColor3`, `Class.TextLabel.TextStrokeColor3\|TextStrokeColor3`, `Class.TextLabel.TextStrokeTransparency\|TextStrokeTransparency` |
| `Class.TextButton` | `Class.GuiObject.BorderSizePixel\|BorderSizePixel`, `Class.GuiObject.BorderColor3\|BorderColor3`, `Class.TextButton.TextStrokeColor3\|TextStrokeColor3`, `Class.TextButton.TextStrokeTransparency\|TextStrokeTransparency` |
| `Class.ImageLabel` | `Class.GuiObject.BorderSizePixel\|BorderSizePixel`, `Class.GuiObject.BorderColor3\|BorderColor3` |
| `Class.ImageButton` | `Class.GuiObject.BorderSizePixel\|BorderSizePixel`, `Class.GuiObject.BorderColor3\|BorderColor3` |

Alternatively, you can apply a `Class.UIStroke` child and tween its thickness, color, and/or transparency.

| UI Object | Properties |
| --- | --- |
| `Class.UIStroke` | `Class.UIStroke.Color\|Color`, `Class.UIStroke.Thickness\|Thickness`, `Class.UIStroke.Transparency\|Transparency` |

```lua
local TweenService = game:GetService("TweenService")
local Players = game:GetService("Players")

local PlayerGui = Players.LocalPlayer:WaitForChild("PlayerGui")
local ScreenGui = PlayerGui:WaitForChild("ScreenGui")
local object = ScreenGui:WaitForChild("TextLabel")

local stroke = Instance.new("UIStroke")
stroke.Color = Color3.fromRGB(255, 255, 255)
stroke.Thickness = 5
stroke.Parent = object

local targetColor = Color3.fromRGB(255, 0, 0)
local targetThickness = 10

local tweenInfo = TweenInfo.new(2)
local tween = TweenService:Create(stroke, tweenInfo, {Color = targetColor, Thickness = targetThickness})

tween:Play()
```

## Multi-property tweens

You can combine any of the [single-property tweens](#single-property-tweens) into more complex tweens by passing multiple target properties to `Class.TweenService:Create()`, for example **position + rotation** or **size + transparency**.

```lua
local TweenService = game:GetService("TweenService")
local Players = game:GetService("Players")

local PlayerGui = Players.LocalPlayer:WaitForChild("PlayerGui")
local ScreenGui = PlayerGui:WaitForChild("ScreenGui")
local object = ScreenGui:WaitForChild("ImageLabel")

object.AnchorPoint = Vector2.new(0.5, 0.5)

local targetPosition = UDim2.new(0.5, 0, 0.5, 0)
local targetRotation = 45

local tweenInfo = TweenInfo.new(2)
local tween = TweenService:Create(object, tweenInfo, {Position = targetPosition, Rotation = targetRotation})

tween:Play()
```

```lua
local TweenService = game:GetService("TweenService")
local Players = game:GetService("Players")

local PlayerGui = Players.LocalPlayer:WaitForChild("PlayerGui")
local ScreenGui = PlayerGui:WaitForChild("ScreenGui")
local object = ScreenGui:WaitForChild("ImageLabel")

object.AnchorPoint = Vector2.new(0.5, 0.5)

local aspectRatioConstraint = Instance.new("UIAspectRatioConstraint")
aspectRatioConstraint.Parent = object

local targetSize = UDim2.new(0.4, 0, 0.4, 0)
local targetTransparency = 0.8

local tweenInfo = TweenInfo.new(2)
local tween = TweenService:Create(object, tweenInfo, {Size = targetSize, ImageTransparency = targetTransparency})

tween:Play()
```

## Tween sequences

You can chain UI animations to occur one after another by playing subsequent tweens upon the previous tween's `Class.TweenBase.Completed|Completed` event. For example, the following script moves an object to the center of the screen, then rotates it by 45°.

```lua
local TweenService = game:GetService("TweenService")
local Players = game:GetService("Players")

local PlayerGui = Players.LocalPlayer:WaitForChild("PlayerGui")
local ScreenGui = PlayerGui:WaitForChild("ScreenGui")
local object = ScreenGui:WaitForChild("ImageLabel")

object.AnchorPoint = Vector2.new(0.5, 0.5)

local targetPosition = UDim2.new(0.5, 0, 0.5, 0)
local targetRotation = 45

local tweenInfo = TweenInfo.new(2)
local positionTween = TweenService:Create(object, tweenInfo, {Position = targetPosition})
local rotationTween = TweenService:Create(object, tweenInfo, {Rotation = targetRotation})

-- Initially play position tween
positionTween:Play()

-- Play rotation tween upon completion of position tween
positionTween.Completed:Connect(function()
	rotationTween:Play()
end)
```

## Style transitions

UI objects can also be animated through **style transitions**, comparable to [CSS transitions](/docs/en-us/ui/styling/css-comparisons.md#transitions), where one or more UI properties are tweened through `Class.StyleRule` definitions. See the [Style Editor](/docs/en-us/ui/styling/editor.md#style-transitions) guide for details.

![Final styled state rule in the Style Editor.](../assets/ui/ui-styling/SE-Transition-Rule-Result.png) ## Easing options

Using the easing options of `Datatype.TweenInfo`, you can control the easing **style** and **direction** of UI animations.

### Style

`Enum.EasingStyle` sets the rate of interpolation from start to end. By default, easing style is set to `Enum.EasingStyle.Quad`.

| Style | Description |
| --- | --- |
| **Linear** | Moves at a constant speed. |
| **Sine** | Speed is determined by a sine wave for a gentle easing motion. |
| **Quad** | Similar to **Sine** but with a slightly sharper curve based on quadratic interpolation. |
| **Cubic** | Similar to **Quad** but with a slightly sharper curve based on cubic interpolation. |
| **Quart** | Similar to **Cubic** but with an even sharper curve based on quartic interpolation. |
| **Quint** | Similar to **Quart** but with an even sharper curve based on quintic interpolation. |
| **Exponential** | The sharpest curve based on exponential interpolation. |
| **Circular** | Follows a circular arc, such that acceleration is more sudden and deceleration more gradual versus **Quint** or **Exponential**. |
| **Back** | Slightly overshoots the target, then backs into place. |
| **Bounce** | Bounces backwards multiple times after reaching the target, before eventually settling. |
| **Elastic** | Moves as if attached to a rubber band, overshooting the target several times. |

#### EasingDirection = In

![Graphs of EasingStyle variations with an 'In' EasingDirection.](../assets/engine-api/enums/EasingStyle/Easing-Styles-In.png)

#### EasingDirection = Out

![Graphs of EasingStyle variations with an 'Out' EasingDirection.](../assets/engine-api/enums/EasingStyle/Easing-Styles-Out.png)

#### EasingDirection = InOut

![Graphs of EasingStyle variations with an 'InOut' EasingDirection.](../assets/engine-api/enums/EasingStyle/Easing-Styles-InOut.png)

```lua
local tweenInfo = TweenInfo.new(2, Enum.EasingStyle.Cubic)
local tween = TweenService:Create(object, tweenInfo, {Rotation = 45})
```

### Direction

`Enum.EasingDirection` defines how the [easing style](#style) interpolation applies to an object, with a default of **Out**. Note that a tween with **Linear** easing style is not affected, as linear interpolation is constant from start to end.

| Direction | Description |
| --- | --- |
| **In** | The easing style applies in a forward direction. |
| **Out** | The easing style applies in a reverse direction. |
| **InOut** | The easing style applies forward for the first half and in reverse for the second half. |

```lua
local tweenInfo = TweenInfo.new(2, Enum.EasingStyle.Cubic, Enum.EasingDirection.InOut)
local tween = TweenService:Create(object, tweenInfo, {Rotation = 45})
```

## Typewriter effect on text

You can easily enhance text-based UI, such as cutscene banners, player instructions, and prompts, with animated effects. The "typewriter" effect is ideal for `Class.TextLabel|TextLabels` that tell a story, output NPC conversations, etc.

1. Create a new `Class.ModuleScript` within **ReplicatedStorage**.
2. Rename the new script **AnimateUI**.
3. Paste the following code into the script:```lua
local LocalizationService = game:GetService("LocalizationService")
local Players = game:GetService("Players")

local SOURCE_LOCALE = "en"
local translator = nil

local AnimateUI = {}

function AnimateUI.loadTranslator()
	pcall(function()
		translator = LocalizationService:GetTranslatorForPlayerAsync(Players.LocalPlayer)
	end)
	if not translator then
		pcall(function()
			translator = LocalizationService:GetTranslatorForLocaleAsync(SOURCE_LOCALE)
		end)
	end
end

function AnimateUI.typeWrite(guiObject, text, delayBetweenChars)
	guiObject.Visible = true
	guiObject.AutoLocalize = false
	local displayText = text

	-- Translate text if possible
	if translator then
		displayText = translator:Translate(guiObject, text)
	end

	-- Replace line break tags so grapheme loop will not miss those characters
	displayText = displayText:gsub("<br%s*/>", "\n")
 	-- Remove RichText tags since char-by-char animation will break the tags
	displayText = displayText:gsub("<[^<>]->", "")

	-- Set translated/modified text on parent
	guiObject.Text = displayText

	local index = 0
	for first, last in utf8.graphemes(displayText) do
		index += 1
		guiObject.MaxVisibleGraphemes = index
		task.wait(delayBetweenChars)
	end
end

return AnimateUI
```
  > **Info:** If your game's **source language** is not English (`"en"`), change the locale code for `SOURCE_LOCALE` to match the source language in [localization settings](/docs/en-us/production/localization.md#localization-settings).
4. Create a `Class.TextLabel` in a suitable location, such as within a `Class.ScreenGui` parented to `Class.StarterGui`.
5. Insert a new `Class.LocalScript` as a direct child of the label and paste in the following code. Note that each message is output by calling `AnimateUI.typeWrite()` with parameters for the parent object, the string to output, and the delay between characters.```lua
local ReplicatedStorage = game:GetService("ReplicatedStorage")

local AnimateUI = require(ReplicatedStorage:WaitForChild("AnimateUI"))

local label = script.Parent

-- Load translator if game is localized
--AnimateUI.loadTranslator()

local message1 = [[Beyond this door is the<br /><font size="46" color="rgb(255,50,25)">Great Zorgoth...</font> <font size="40">🗡</font>]]
AnimateUI.typeWrite(label, message1, 0.05)

task.wait(1)

local message2 = [[...who rules this dungeon <font color="rgb(255,200,50)">unchallenged!</font> <font size="30">😈</font>]]
AnimateUI.typeWrite(label, message2, 0.05)
```
