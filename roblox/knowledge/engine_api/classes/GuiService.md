---
name: GuiService
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
summary: "Offers numerous properties and methods for working with GuiObjects, player preferences, and other UI‑related tasks."
---

# Class: GuiService

> Offers numerous properties and methods for working with
> [GuiObjects](/docs/reference/engine/classes/GuiObject.md), player preferences, and other UI‑related tasks.

## Description

`GuiService` offers numerous properties and methods for working with
[GuiObjects](/docs/reference/engine/classes/GuiObject.md), player preferences, and other UI‑related tasks.

## Properties

### Property: GuiService.AutoSelectGuiEnabled

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
  "category": "Data",
  "capabilities": [
    "UI",
    "Input"
  ]
}
```

If activated, the <kbd>Select</kbd> button on a gamepad or
<kbd>Backslash</kbd> will automatically set a GUI as the selected object.
Disabling this means that GUI navigation will still work if
[GuiNavigationEnabled](/docs/reference/engine/classes/GuiService.md) is enabled,
but you will have to set [SelectedObject](/docs/reference/engine/classes/GuiService.md)
manually to start navigation.

### Property: GuiService.GuiNavigationEnabled

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
  "category": "Data",
  "capabilities": [
    "UI",
    "Input"
  ]
}
```

Used to enable and disable the default controller GUI navigation.

### Property: GuiService.MenuIsOpen

```json
{
  "type": "boolean",
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
    "UI"
  ]
}
```

Returns `true` if any menu of [CoreGui](/docs/reference/engine/classes/CoreGui.md) is open.

### Property: GuiService.PreferredTextSize

```json
{
  "type": "PreferredTextSize",
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
    "UI"
  ]
}
```

Gets the player's preferred text size as an [PreferredTextSize](/docs/reference/engine/enums/PreferredTextSize.md) value
of [Medium](/docs/reference/engine/enums/PreferredTextSize.md) (default),
[Large](/docs/reference/engine/enums/PreferredTextSize.md),
[Larger](/docs/reference/engine/enums/PreferredTextSize.md), or
[Largest](/docs/reference/engine/enums/PreferredTextSize.md). This property maps to the
**Text&nbsp;Size** setting available to players from the Roblox and
in‑game **Settings** menus, and it can be combined with
[Object.GetPropertyChangedSignal()](/docs/reference/engine/classes/Object.md) to detect text size setting
changes for purposes of adjusting UI.

When working with UI elements, note the following behaviors:

- Text that is constrained to a minimum and/or maximum size through a
  [UITextSizeConstraint](/docs/reference/engine/classes/UITextSizeConstraint.md) will **not** shrink below or expand above
  the set
  [MinTextSize](/docs/reference/engine/classes/UITextSizeConstraint.md)/[MaxTextSize](/docs/reference/engine/classes/UITextSizeConstraint.md),
  regardless of the player's text size setting.

- When [TextScaled](/docs/reference/engine/classes/TextLabel.md) is enabled for a
  [TextLabel](/docs/reference/engine/classes/TextLabel.md) or
  [TextButton](/docs/reference/engine/classes/TextButton.md), the element's text will
  **not** be scaled by the
  [PreferredTextSize](/docs/reference/engine/classes/GuiService.md) value.

- UI elements with [AutomaticSize](/docs/reference/engine/classes/GuiObject.md) enabled
  will shrink/grow as
  [PreferredTextSize](/docs/reference/engine/classes/GuiService.md)
  decreases/increases (element bounds will resize to fit the resized
  text).

- When [TextWrapped](/docs/reference/engine/classes/TextLabel.md) is enabled for a
  [TextLabel](/docs/reference/engine/classes/TextLabel.md) or
  [TextButton](/docs/reference/engine/classes/TextButton.md), the element's text will wrap
  to additional lines as
  [PreferredTextSize](/docs/reference/engine/classes/GuiService.md) increases, within
  limits of the element's absolute size.

- The results returned by [TextService:GetTextSize()](/docs/reference/engine/classes/TextService.md) and
  [TextService:GetTextBoundsAsync()](/docs/reference/engine/classes/TextService.md) honor changes related to
  [PreferredTextSize](/docs/reference/engine/classes/GuiService.md).

**Detect/Apply Changes to Preferred Text Size**

Listens for changes to [GuiService.PreferredTextSize](/docs/reference/engine/classes/GuiService.md) to appropriately
update a UI element's size.

```lua
local GuiService = game:GetService("GuiService")
local TextService = game:GetService("TextService")

local FONT_SIZE = 25
local PADDING = 8

local textLabel = Instance.new("TextLabel")
textLabel.Position = UDim2.new(0.5, 0, 0.5, 0)
textLabel.AnchorPoint = Vector2.new(0.5, 0.5)
textLabel.AutomaticSize = Enum.AutomaticSize.X
textLabel.TextSize = FONT_SIZE + PADDING
textLabel.Text = "Text Label Test"
textLabel.Parent = script.Parent

local function applyAddedTextHeight()
	local finalTextHeight = TextService:GetTextSize("", FONT_SIZE, Enum.Font.BuilderSans, Vector2.new(math.huge, math.huge)).Y
	local addedTextHeight = finalTextHeight - FONT_SIZE
	print("PreferredTextSize adds", addedTextHeight, " to default text size")
	textLabel.Size = UDim2.new(0, 0, 0, FONT_SIZE + addedTextHeight + PADDING)
end
applyAddedTextHeight()

GuiService:GetPropertyChangedSignal("PreferredTextSize"):Connect(applyAddedTextHeight)
```

### Property: GuiService.SelectedObject

```json
{
  "type": "GuiObject",
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
    "UI",
    "Input"
  ]
}
```

Sets the [GuiObject](/docs/reference/engine/classes/GuiObject.md) currently being focused on by the GUI
navigator. This may reset to `nil` if the object is off screen.

This property is changed by the
[SelectionGained](/docs/reference/engine/classes/GuiObject.md) and
[SelectionLost](/docs/reference/engine/classes/GuiObject.md) events. If you would like to
determine when this property changes without tracking these events for all
GUI elements, you can use the [Changed](/docs/reference/engine/classes/Object.md) event.

**Printing When Gamepad Selection Changes**

The code below demonstrates how to handle when the SelectedObject changes. For
instance, this event fires when the Gamepad navigates to another GUI element.

```lua
local GuiService = game:GetService("GuiService")

local function printChanged(value)
	if value == "SelectedObject" then
		print("The SelectedObject changed!")
	end
end

GuiService.Changed:Connect(printChanged)
```

### Property: GuiService.TopbarInset

```json
{
  "type": "Rect",
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
    "UI"
  ]
}
```

Returns a [Rect](/docs/reference/engine/datatypes/Rect.md) object representing the unoccupied area between
the Roblox left-most controls and the edge of the device safe area.

The value is dynamic and can be expected to change based on the visibility
of UI controls such as changing the local player's
[Health](/docs/reference/engine/classes/Humanoid.md) property, usage of
[StarterGui:SetCoreGuiEnabled()](/docs/reference/engine/classes/StarterGui.md), changing the size and position of
Roblox UI Controls, and/or others. For this reason, it's recommend that
you detect and react to changes of this property with
[Object:GetPropertyChangedSignal()](/docs/reference/engine/classes/Object.md).

**Responsive Frame Within Available Top Bar Space**

This code snippet creates a new [ScreenGui](/docs/reference/engine/classes/ScreenGui.md) with a [Frame](/docs/reference/engine/classes/Frame.md) that
automatically adapts its size and position to a top bar space unoccupied by
Roblox UI.

```lua
local GuiService = game:GetService("GuiService")
local Players = game:GetService("Players")

local screenGui = Instance.new("ScreenGui")
screenGui.IgnoreGuiInset = true
screenGui.Parent = Players.LocalPlayer.PlayerGui

local frame = Instance.new("Frame")
frame.BackgroundColor3 = Color3.fromRGB(0, 255, 0)
frame.Parent = screenGui

GuiService:GetPropertyChangedSignal("TopbarInset"):Connect(function()
	local inset = GuiService.TopbarInset
	frame.Size = UDim2.new(0, inset.Width, 0, inset.Height)
	frame.Position = UDim2.new(0, inset.Min.X, 0, inset.Min.Y)
end)
```

### Property: GuiService.TouchControlsEnabled

```json
{
  "type": "boolean",
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
    "UI",
    "Input"
  ]
}
```

Used to enable and disable touch controls and touch control display UI.
Defaults to `true`.

### Property: GuiService.ViewportDisplaySize

```json
{
  "type": "DisplaySize",
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
    "UI"
  ]
}
```

Read-only property which represents the physical rendering size of the
viewport:

- [DisplaySize.Small](/docs/reference/engine/enums/DisplaySize.md) — Most tablet/mobile/handheld devices
- [DisplaySize.Medium](/docs/reference/engine/enums/DisplaySize.md) — Most laptops and monitors
- [DisplaySize.Large](/docs/reference/engine/enums/DisplaySize.md) — Most TVs or larger

You can listen for changes to this property through the
[GetPropertyChangedSignal()](/docs/reference/engine/classes/Object.md)
method to adapt UI to various display sizes.

**ViewportDisplaySize Changes**

This code snippet listens to [GuiService.ViewportDisplaySize](/docs/reference/engine/classes/GuiService.md) property
change signals to adapt UI to various display sizes.

```lua
local GuiService = game:GetService("GuiService")

local function updateUI()
	if (GuiService.ViewportDisplaySize == Enum.DisplaySize.Small) then
		-- Update UI to small screen
	elseif (GuiService.ViewportDisplaySize == Enum.DisplaySize.Large) then
		-- Update UI to large screen
	else
		-- Update UI to medium/default screen
	end
end

GuiService:GetPropertyChangedSignal("ViewportDisplaySize"):Connect(updateUI)
updateUI()
```

### Property: GuiService.IsModalDialog

```json
{
  "type": "boolean",
  "access": "ReadWrite",
  "security": {
    "read": "None",
    "write": "None"
  },
  "serialization": {
    "can_load": false,
    "can_save": false
  },
  "deprecated": true,
  "thread_safety": "ReadSafe",
  "category": "Data",
  "capabilities": [
    "UI"
  ]
}
```

> **Deprecated:** This item is deprecated. Do not use it for new work.

This property tells whether or not a modal dialog is visible, such as the
game menu or a purchase prompt.

### Property: GuiService.IsWindows

```json
{
  "type": "boolean",
  "access": "ReadWrite",
  "security": {
    "read": "None",
    "write": "None"
  },
  "serialization": {
    "can_load": false,
    "can_save": false
  },
  "deprecated": true,
  "thread_safety": "ReadSafe",
  "category": "Data",
  "capabilities": [
    "UI"
  ]
}
```

> **Deprecated:** This item is deprecated. Do not use it for new work.

The IsWindows property defines if the user is playing on a computer
running Windows.

### Property: GuiService.CoreGuiNavigationEnabled *(hidden)*

```json
{
  "type": "boolean",
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
    "UI",
    "Input"
  ]
}
```

Toggles whether or not objects in the [CoreGui](/docs/reference/engine/classes/CoreGui.md) can be navigated
using a gamepad.

### Property: GuiService.PreferredTransparency *(hidden)*

```json
{
  "type": "float",
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
    "UI"
  ]
}
```

Gets the player's preferred transparency as a number between `0` and `1`.
This property maps to the **Background&nbsp;Transparency** setting
available to players from the Roblox and in‑experience **Settings** menus,
and it can be combined with [Object.GetPropertyChangedSignal()](/docs/reference/engine/classes/Object.md) to
detect transparency setting changes for purposes of adjusting UI.

A value of `1` (default) indicates the player prefers the default
background transparency, while a value of `0` indicates the player prefers
fully opaque (non‑transparent) background transparency for improved
readability and contrast. Multiplying a UI element's
[BackgroundTransparency](/docs/reference/engine/classes/GuiObject.md) with
[PreferredTransparency](/docs/reference/engine/classes/GuiService.md) is the
recommended approach, such that backgrounds become more opaque as
[PreferredTransparency](/docs/reference/engine/classes/GuiService.md) approaches
`0`.

**Detect/Apply Changes to Preferred Transparency**

Listens for changes to [GuiService.PreferredTransparency](/docs/reference/engine/classes/GuiService.md) to adjust the
background opacity of UI objects tagged with `TransparentBack` through
[CollectionService](/docs/reference/engine/classes/CollectionService.md).

```lua
local GuiService = game:GetService("GuiService")
local CollectionService = game:GetService("CollectionService")

local TAG = "TransparentBack"

local transparentBackObjects = {}

local function onInstanceAdded(object)
	if object.BackgroundTransparency then
		local defaultTransparency = object.BackgroundTransparency
		transparentBackObjects[object] = defaultTransparency
		object.BackgroundTransparency = defaultTransparency * GuiService.PreferredTransparency
	end
end

local function onInstanceRemoved(object)
	transparentBackObjects[object] = nil
end

-- Store initial tagged instances
for _, object in CollectionService:GetTagged(TAG) do
	onInstanceAdded(object)
end

-- Detect when tagged instance is added or removed
CollectionService:GetInstanceAddedSignal(TAG):Connect(onInstanceAdded)
CollectionService:GetInstanceRemovedSignal(TAG):Connect(onInstanceRemoved)

-- When in-game setting is changed, adjust tagged instances
GuiService:GetPropertyChangedSignal("PreferredTransparency"):Connect(function()
	for object, defaultTransparency in transparentBackObjects do
		object.BackgroundTransparency = defaultTransparency * GuiService.PreferredTransparency
	end
end)
```

### Property: GuiService.ReducedMotionEnabled *(hidden)*

```json
{
  "type": "boolean",
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
    "UI"
  ]
}
```

Returns `true` if the player has enabled reduced motion, indicating that
they want motion effects and animations to be reduced or completely
removed. This property maps to the **Reduce&nbsp;Motion** toggle available
from the Roblox and in‑experience **Settings** menus. See
[accessibility guidelines](/docs/en-us/production/publishing/accessibility.md#reduced-motion)
for usage recommendations.

## Methods

### Method: GuiService:CloseInspectMenu

**Signature:** `GuiService:CloseInspectMenu(): ()`

This method closes the
[Avatar Inspect Menu](/docs/en-us/players/avatar-inspect-menu.md), if open,
when run from a [LocalScript](/docs/reference/engine/classes/LocalScript.md).

#### See Also

- [InspectPlayerFromHumanoidDescription()](/docs/reference/engine/classes/GuiService.md)
  which allows the avatar inspection menu to appear showing the assets
  listed in a [HumanoidDescription](/docs/reference/engine/classes/HumanoidDescription.md) object.

- [InspectPlayerFromUserId()](/docs/reference/engine/classes/GuiService.md)
  which allows the avatar inspection menu to appear showing the user that
  has the given [UserId](/docs/reference/engine/classes/Player.md).

*Security: None · Thread Safety: Unsafe · Capabilities: UI*

**Returns:** `()`

### Method: GuiService:DismissNotification

**Signature:** `GuiService:DismissNotification(notificationId: string): boolean`

Dismisses the notification identified by `notificationId`, which is the
string returned when the notification was created with
[SendNotification()](/docs/reference/engine/classes/GuiService.md). If the
notification was created with an `OnDismiss` callback, that callback is
invoked. Returns `true` when a matching notification is found and
dismissed, or `false` when no active notification has the given
`notificationId`.

*Security: None · Thread Safety: Unsafe · Capabilities: UI*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `notificationId` | `string` |  | The identifier returned by [SendNotification()](/docs/reference/engine/classes/GuiService.md) for the notification to dismiss. |

**Returns:** `boolean` — `true` if a matching notification was found and dismissed; `false` if
no active notification has the given `notificationId`.

### Method: GuiService:GetEmotesMenuOpen

**Signature:** `GuiService:GetEmotesMenuOpen(): boolean`

Returns a boolean indicating whether or not the player emotes menu is
open. You can open or close the emotes menu by calling the
[SetEmotesMenuOpen()](/docs/reference/engine/classes/GuiService.md) method.

*Security: None · Thread Safety: Unsafe · Capabilities: UI*

**Returns:** `boolean` — Whether the emotes menu is open.

### Method: GuiService:GetGameplayPausedNotificationEnabled

**Signature:** `GuiService:GetGameplayPausedNotificationEnabled(): boolean`

This method returns whether or not the [Player.GameplayPaused](/docs/reference/engine/classes/Player.md)
notification has been disabled through
[SetGameplayPausedNotificationEnabled()](/docs/reference/engine/classes/GuiService.md).

See also [Workspace.StreamingIntegrityMode](/docs/reference/engine/classes/Workspace.md) and
[StreamingIntegrityMode](/docs/reference/engine/enums/StreamingIntegrityMode.md) for more details on when gameplay is paused.

*Security: None · Thread Safety: Unsafe · Capabilities: UI*

**Returns:** `boolean` — Whether or not the [Player.GameplayPaused](/docs/reference/engine/classes/Player.md) notification has been
disabled.

### Method: GuiService:GetGuiInset

**Signature:** `GuiService:GetGuiInset(): Tuple`

Returns two [Vector2](/docs/reference/engine/datatypes/Vector2.md) values representing the inset of user GUIs
in pixels, from the top‑left corner of the screen and the bottom‑right
corner of the screen respectively.

Note that the inset values supplied by this method only take effect on
[ScreenGuis](/docs/reference/engine/classes/ScreenGui.md) that have their
[IgnoreGuiInset](/docs/reference/engine/classes/ScreenGui.md) property set to `false`.

*Security: None · Thread Safety: Unsafe · Capabilities: UI*

**Returns:** `Tuple` — A tuple of two [Vector2](/docs/reference/engine/datatypes/Vector2.md) values describing the current
specified GUI inset.

**Get Gui Inset**

Demonstrates [GuiService:GetGuiInset()](/docs/reference/engine/classes/GuiService.md).

```lua
local GuiService = game:GetService("GuiService")

local screenAreaTopLeft, screenAreaBottomRight = GuiService:GetGuiInset()
print(screenAreaTopLeft, screenAreaBottomRight)
```

### Method: GuiService:GetInsetArea

**Signature:** `GuiService:GetInsetArea(screenInsets: ScreenInsets): Rect`

Takes an [ScreenInsets](/docs/reference/engine/enums/ScreenInsets.md) value and returns a [Rect](/docs/reference/engine/datatypes/Rect.md)
describing the inset region relative to the
[CoreUISafeInsets](/docs/reference/engine/enums/ScreenInsets.md) area, effectively
the usable rectangle for a particular [ScreenInsets](/docs/reference/engine/enums/ScreenInsets.md) area.

On a mobile device screen, for example, querying
`GetInsetArea(Enum.ScreenInsets.None)` may return a result such as
`-59, -58, 792, 334`, meaning the usable rectangle for
[ScreenInsets.None](/docs/reference/engine/enums/ScreenInsets.md) has a top‑left corner `59` pixels left and `58`
pixels up from the top‑left corner of the core UI area, and a bottom‑right
corner `792` pixels right and `334` pixels down from the top‑left corner
of the core UI area.

*Security: None · Thread Safety: Unsafe · Capabilities: UI*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `screenInsets` | `ScreenInsets` |  | The [ScreenInsets](/docs/reference/engine/enums/ScreenInsets.md) value indicating which inset area to query. |

**Returns:** `Rect` — A [Rect](/docs/reference/engine/datatypes/Rect.md) of the usable region for the specified
[ScreenInsets](/docs/reference/engine/enums/ScreenInsets.md) area.

**Get Inset Area**

Demonstrates [GuiService:GetInsetArea()](/docs/reference/engine/classes/GuiService.md).

```lua
local GuiService = game:GetService("GuiService")

local noneRect = GuiService:GetInsetArea(Enum.ScreenInsets.None)
print(noneRect) --> -59, -58, 792, 334

local deviceSafeRect = GuiService:GetInsetArea(Enum.ScreenInsets.DeviceSafeInsets)
print(deviceSafeRect) --> 0, -58, 733, 313

local coreUISafeRect = GuiService:GetInsetArea(Enum.ScreenInsets.CoreUISafeInsets)
print(coreUISafeRect) --> 0, 0, 733, 313

local topbarSafeRect = GuiService:GetInsetArea(Enum.ScreenInsets.TopbarSafeInsets)
print(topbarSafeRect) --> 164, -58, 733, 0
```

### Method: GuiService:GetInspectMenuEnabled

**Signature:** `GuiService:GetInspectMenuEnabled(): boolean`

This method returns whether the
[Avatar Inspect Menu](/docs/en-us/players/avatar-inspect-menu.md) is
currently enabled. The feature is enabled by default and can be disabled
using the
[SetInspectMenuEnabled()](/docs/reference/engine/classes/GuiService.md) method.

*Security: None · Thread Safety: Unsafe · Capabilities: UI*

**Returns:** `boolean` — Whether the avatar inspection menu is enabled.

### Method: GuiService:InspectPlayerFromHumanoidDescription

**Signature:** `GuiService:InspectPlayerFromHumanoidDescription(humanoidDescription: Instance, name: string): ()`

This method allows the
[Avatar Inspect Menu](/docs/en-us/players/avatar-inspect-menu.md) to appear
showing the assets listed in a [HumanoidDescription](/docs/reference/engine/classes/HumanoidDescription.md) object. This
allows further customization with what is shown in the inspection menu
when players inspect other players in your experience.

See also
[InspectPlayerFromUserId()](/docs/reference/engine/classes/GuiService.md)
which allows the avatar inspection menu to appear showing the user that
has the given [UserId](/docs/reference/engine/classes/Player.md).

*Security: None · Thread Safety: Unsafe · Capabilities: UI, AvatarAppearance*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `humanoidDescription` | `Instance` |  | A [HumanoidDescription](/docs/reference/engine/classes/HumanoidDescription.md) object that contains the assets to show in the inspection menu. |
| `name` | `string` |  | The name of the player being inspected to show in the menu. |

**Returns:** `()`

**Opening an Inspect Menu with a HumanoidDescription**

This example demonstrates how to show an Inspect Menu containing two items
([Midnight Antlers][1] and [Mid-Summer Starry Wings][2]), for a player named
`MyPlayer` using `GuiService:InspectPlayerFromHumanoidDescription`.

[1]: https://www.roblox.com/catalog/3339374070/Midnight-Rune-Antlers
[2]: https://www.roblox.com/catalog/3339363671/Mid-Summer-Starry-Wings

```lua
local GuiService = game:GetService("GuiService")

local humanoidDescription = Instance.new("HumanoidDescription")
humanoidDescription.HatAccessory = "3339374070"
humanoidDescription.BackAccessory = "3339363671"

GuiService:InspectPlayerFromHumanoidDescription(humanoidDescription, "MyPlayer")
```

### Method: GuiService:InspectPlayerFromUserId

**Signature:** `GuiService:InspectPlayerFromUserId(userId: User): ()`

This method allows the
[Avatar Inspect Menu](/docs/en-us/players/avatar-inspect-menu.md) to appear
showing the user that has the given [UserId](/docs/reference/engine/classes/Player.md). This is
especially useful when you want to inspect players who aren't in the
current experience.

See also
[InspectPlayerFromHumanoidDescription()](/docs/reference/engine/classes/GuiService.md)
which allows you to bring up the avatar inspection menu showing the assets
listed in a [HumanoidDescription](/docs/reference/engine/classes/HumanoidDescription.md) object.

*Security: None · Thread Safety: Unsafe · Capabilities: UI, AvatarAppearance*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `userId` | `User` |  | The [UserId](/docs/reference/engine/classes/Player.md) of the player to inspect. |

**Returns:** `()`

**Opening the Inspect Menu for a UserId**

The code sample below demonstrates how to use
[GuiService:InspectPlayerFromUserId()](/docs/reference/engine/classes/GuiService.md) to open the `Inspect Menu` for
the Roblox user with the ID [772462][1].

[1]: https://www.roblox.com/users/772462/profile

```lua
local GuiService = game:GetService("GuiService")
GuiService:InspectPlayerFromUserId(772462)
```

### Method: GuiService:IsTenFootInterface

**Signature:** `GuiService:IsTenFootInterface(): boolean`

Returns `true` if the client is using the ten foot interface, a special
version of Roblox's UI exclusive to consoles.

Note that you should **not** use this property in an attempt to verify if
the player is on a console or not. Instead, consider reading
[ViewportDisplaySize](/docs/reference/engine/classes/GuiService.md). This method is
hardcoded to return `true` whenever the client runs on a console,
regardless of how the player is actually interacting with the device,
making it an unreliable proxy for rendering context.

*Security: None · Thread Safety: Unsafe · Capabilities: UI*

**Returns:** `boolean` — `true` if the client is using the ten foot interface (console UI
mode); `false` otherwise.

### Method: GuiService:Select

**Signature:** `GuiService:Select(selectionParent: Instance): ()`

When called on an instance `selectionParent` that is the [PlayerGui](/docs/reference/engine/classes/PlayerGui.md)
or a descendant of it, the engine searches all available selectable,
visible and on-screen [GuiObjects](/docs/reference/engine/classes/GuiObject.md) that are descendants of
`selectionParent` and sets the
[SelectedObject](/docs/reference/engine/classes/GuiService.md) to the [GuiObject](/docs/reference/engine/classes/GuiObject.md)
with the smallest [SelectionOrder](/docs/reference/engine/classes/GuiObject.md).

*Security: None · Thread Safety: Unsafe · Capabilities: UI*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `selectionParent` | `Instance` |  | The parent of selection whose descendants are searched. |

**Returns:** `()`

### Method: GuiService:SendNotification

**Signature:** `GuiService:SendNotification(notificationInfo: Dictionary): string`

Displays a notification built from the `notificationInfo` dictionary using
Roblox's native notification UI, and returns a unique identifier string
for the notification. The following fields of `notificationInfo` are
recognized:

| Field | Type | Description |
| --- | --- | --- |
| `Title` | `string` | The notification's title text. |
| `Text` | `string` | The notification's body text. |
| `Icon` | `string` | An image asset to display with the notification. |
| `Buttons` | `{[ButtonInfo]}` | An array of button definitions. Each entry is a table with a `Text` (`string`), a `ButtonType` ([NotificationButtonType](/docs/reference/engine/enums/NotificationButtonType.md)), and an `OnActivated` (`function`) callback invoked when the button is pressed. |
| `OnDisplay` | `function` | Invoked when the notification is shown. |
| `OnDismiss` | `function` | Invoked when the notification is dismissed. |

The returned identifier can be passed to
[DismissNotification()](/docs/reference/engine/classes/GuiService.md) to dismiss
the notification programmatically; an empty string is returned if the
notification could not be queued.

*Security: None · Thread Safety: Unsafe · Capabilities: UI*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `notificationInfo` | `Dictionary` |  | A dictionary describing the notification. Recognized fields are `Title` (string), `Text` (string), `Icon` (string), `Buttons` (an array of button tables, each with a `Text` string, a `ButtonType` [NotificationButtonType](/docs/reference/engine/enums/NotificationButtonType.md) value, and an `OnActivated` callback), and `OnDisplay`/`OnDismiss` callback functions. |

**Returns:** `string` — A unique identifier string for the notification, which can be passed
to [DismissNotification()](/docs/reference/engine/classes/GuiService.md).
Returns an empty string if the notification could not be queued.

### Method: GuiService:SetEmotesMenuOpen

**Signature:** `GuiService:SetEmotesMenuOpen(isOpen: boolean): ()`

Opens or closes the player emotes menu.

*Security: None · Thread Safety: Unsafe · Capabilities: UI*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `isOpen` | `boolean` |  | Whether to open (`true`) or close (`false`) the emotes menu. |

**Returns:** `()`

### Method: GuiService:SetGameplayPausedNotificationEnabled

**Signature:** `GuiService:SetGameplayPausedNotificationEnabled(enabled: boolean): ()`

This method lets you disable the built-in notification when a player's
gameplay is paused. You can then add in your own UI and customize it.

You can query whether the notification is enabled by calling the
[GetGameplayPausedNotificationEnabled()](/docs/reference/engine/classes/GuiService.md)
method.

See also [Workspace.StreamingIntegrityMode](/docs/reference/engine/classes/Workspace.md) and
[StreamingIntegrityMode](/docs/reference/engine/enums/StreamingIntegrityMode.md) for more details on when gameplay is paused.

*Security: None · Thread Safety: Unsafe · Capabilities: UI*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `enabled` | `boolean` |  | Whether or not the built-in notification GUI is disabled. |

**Returns:** `()`

### Method: GuiService:SetInspectMenuEnabled

**Signature:** `GuiService:SetInspectMenuEnabled(enabled: boolean): ()`

This method allows you to enable or disable the
[Avatar Inspect Menu](/docs/en-us/players/avatar-inspect-menu.md). The
feature is enabled by default.

*Security: None · Thread Safety: Unsafe · Capabilities: UI*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `enabled` | `boolean` |  | A boolean indicating whether to enable or disable the menu. |

**Returns:** `()`

### Method: GuiService:AddSelectionParent

**Signature:** `GuiService:AddSelectionParent(selectionName: string, selectionParent: Instance): ()`

Creates a selection group where gamepad GUI navigation will only consider
selectable objects that are within the group (children of
`selectionParent`). An example is when you have a menu pop open and there
are other selectable objects on the screen, possibly from previous menus,
but you want the user to only be able to select GUI objects in the new
menu.

*Security: None · Thread Safety: Unsafe · Capabilities: UI*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `selectionName` | `string` |  | A unique name identifying this selection group. |
| `selectionParent` | `Instance` |  | The [GuiObject](/docs/reference/engine/classes/GuiObject.md) whose selectable descendants form the navigation group. |

**Returns:** `()`

### Method: GuiService:AddSelectionTuple

**Signature:** `GuiService:AddSelectionTuple(selectionName: string, selections: Tuple): ()`

Functions similarly to [GuiService:AddSelectionParent()](/docs/reference/engine/classes/GuiService.md), but you
can give it a tuple of [GuiObject](/docs/reference/engine/classes/GuiObject.md) that you want to be contained in
the group.

*Security: None · Thread Safety: Unsafe · Capabilities: UI*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `selectionName` | `string` |  | The name of the added selection. |
| `selections` | `Tuple` |  | The selection(s) added. |

**Returns:** `()`

### Method: GuiService:RemoveSelectionGroup

**Signature:** `GuiService:RemoveSelectionGroup(selectionName: string): ()`

Removes a group that was created with
[AddSelectionParent()](/docs/reference/engine/classes/GuiService.md) or
[AddSelectionTuple()](/docs/reference/engine/classes/GuiService.md).

*Security: None · Thread Safety: Unsafe · Capabilities: UI*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `selectionName` | `string` |  | The name of the selection group to remove. |

**Returns:** `()`

## Events

### Event: GuiService.MenuClosed

**Signature:** `GuiService.MenuClosed()`

Fires when the user **closes** the Roblox [CoreGui](/docs/reference/engine/classes/CoreGui.md) escape menu.

*Security: None · Capabilities: UI*

### Event: GuiService.MenuOpened

**Signature:** `GuiService.MenuOpened()`

Fires when the user **opens** the Roblox [CoreGui](/docs/reference/engine/classes/CoreGui.md) escape menu.

*Security: None · Capabilities: UI*

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