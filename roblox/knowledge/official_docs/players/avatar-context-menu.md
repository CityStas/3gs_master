---
title: "Avatar Context Menu"
url: /docs/en-us/players/avatar-context-menu
last_updated: 2026-10-30T19:55:47Z
description: "The Avatar Context Menu (ACM) allows users to interact and customize actions with others in their game."
---

# Avatar Context Menu

The **Avatar Context Menu** (ACM) makes it easier for users to interact with each other. When the ACM is enabled in your game, a user can walk up to another user's character and click on them to open a small menu with several default options. The player can send a friend request, begin a private chat, view the user's profile, or wave.

After [enabling](#enable-the-avatar-context-menu) the ACM in your game, you can customize the ACM in the following ways:

- Programmatically [open and close](#open-and-close-the-acm) the ACM for specific users.
- [Add](#add-menu-options) custom options and [remove](#remove-menu-options) existing options to the ACM.
- [Customize the ACM appearance](#customize-menu-appearance) to create a unique user interface.

## Enable the Avatar Context Menu

The Avatar Context Menu must be enabled using the `Class.StarterGui:SetCore()` option "AvatarContextMenuEnabled" in a `Class.LocalScript`. The ACM is best used in games where there is no predefined behavior for clicking on other users.

Use the following code sample to enable the ACM in a `Class.LocalScript`:

```lua
-- Run in a LocalScript, ideally within "StarterPlayerScripts"
local StarterGui = game:GetService("StarterGui")
StarterGui:SetCore("AvatarContextMenuEnabled", true)
```

If you need to detect whether the ACM is enabled, you can use the following code to return a boolean on the current status of the ACM:

```lua
---Returns a boolean indicating if the ACM is currently enabled.
StarterGui:GetCore(AvatarContextMenuEnabled)
```

## Open and close the ACM

Once enabled, you can open and close the ACM programmatically with `Class.StarterGui`.

To programmatically open the ACM, use the following code:

```lua
-- Use StarterGui:SetCore where targetPlayer is a valid Player object
StarterGui:SetCore("AvatarContextMenuTarget", targetPlayer)
```

To programmatically close the ACM, use the following code:

```lua
StarterGui:SetCore("AvatarContextMenuTarget", nil)
```

## Menu options

You can [add](#add-menu-options) and [remove](#remove-menu-options) actions through scripting. By default, the menu has the following options:

| Menu option | Description |
| --- | --- |
| Friend | Sends a friend request to the selected user. |
| Chat | Opens a private conversation with the selected user in the in-game chat. |
| View | Opens a window to inspect the selected user's appearance. |
| Wave | Initiates a wave animation to the selected user. |

Once the ACM is open, the user can scroll and select other users on the character selection carousel. Characters are sorted based on distance to the selected character. The menu only updates when opened and the list of available users will repeat when scrolling.

### Add menu options

Once enabled, game-specific actions can be added to the ACM. For example, a game might allow for trade requests, add-to-party options, or other special interactions.

The following example shows how to add a custom action to the Avatar Context Menu:

```lua
local Players = game:GetService("Players")
local StarterGui = game:GetService("StarterGui")
local player = Players.LocalPlayer

-- Connect a function to a "BindableEvent"
local bindableEvent = Instance.new("BindableEvent")
local function onCustomACMAction(targetPlayer)
	-- At this point, you could call InvokeServer() on a RemoteFunction to alert the server of the selection
	print("ACM event selected by " .. player.Name .. " on " .. targetPlayer.Name)
end
bindableEvent.Event:Connect(onCustomACMAction)

-- Add the ACM option using SetCore() with "AddAvatarContextMenuOption"
local options = {"Custom ACM Action", bindableEvent}
StarterGui:SetCore("AddAvatarContextMenuOption", options)
```

### Remove menu options

You can remove custom and the default Add Friend, Chat, View, and Wave options from the ACM by referencing the custom Action name or the default `Enum.AvatarContextMenuOption` enum.

Use the following code to remove a default and custom menu option:

```lua
-- Remove the "Custom ACM Action" option
StarterGui:SetCore("RemoveAvatarContextMenuOption", "Custom ACM Action")

-- Remove the default "Friend" option by referencing the AvatarContextMenuOption.Friend Enum
StarterGui:SetCore("RemoveAvatarContextMenuOption", Enum.AvatarContextMenuOption.Friend)
```

> **Warning:** You can not make edits to the ACM while it is open. Your code should verify that an action is still relevant in case the action was removed from the menu. For example, if a marketplace area adds an option to send trade requests, you should verify both users are still in the marketplace.
## Customize menu appearance

To change the appearance of the Avatar Context Menu, call `Class.StarterGui:SetCore()` with the option "AvatarContextMenuTheme", providing a table of parameters and values to adjust the menu appearance.

The ACM user interface includes the following sections:

A. Name Tag: The user name of the character being interacted with.

B. Button Frame: Contains all of the ACM buttons.

C. Buttons: Individual buttons for the default or custom ACM actions.

### Appearance parameters

These are the customization parameters with the ACM:

#### Background

| BackgroundColor | A `Datatype.Color3` for the overall background of the ACM (most useful when not using a background image). |
| --- | --- |
| BackgroundTransparency | Transparency value (0–1) for the overall background of the ACM (most useful when not using a background image). |
| BackgroundImage | A valid asset ID of an image for the ACM background. |
| BackgroundImageTransparency | Transparency value (0–1) for the background image. |
| BackgroundImageScaleType | A `Enum.ScaleType` enum for background image scaling. |
| BackgroundImageSliceCenter | A `Datatype.Rect` specifying the center of a nine-slice image when BackgroundImageScaleType is set to `Enum.ScaleType.Slice`. |

#### Name tag

| NameTagColor | A `Datatype.Color3` for the bar showing which player is being interacted with. |
| --- | --- |
| NameUnderlineColor | A `Datatype.Color3` for the thin line between the name tag and action buttons. |

#### Button frame

| ButtonFrameColor | A `Datatype.Color3` for the section (frame) containing the action buttons. |
| --- | --- |
| ButtonFrameTransparency | Transparency value (0–1) for the button frame section. |

#### Button

| ButtonColor | A `Datatype.Color3` for the background of the ACM action buttons. |
| --- | --- |
| ButtonTransparency | Transparency value (0–1) for the background color of the action buttons. |
| ButtonHoverColor | A `Datatype.Color3` for the "hover" state of the action buttons. |
| ButtonHoverTransparency | Transparency value (0–1) for the "hover" color of the action buttons. |
| ButtonUnderlineColor | A `Datatype.Color3` for the thin line which separates each action button. |
| ButtonImage | A valid asset ID of an image for the background of buttons. |
| ButtonImageScaleType | A `Enum.ScaleType` enum for button image scaling. |
| ButtonImageSliceCenter | A `Datatype.Rect` specifying the center of a nine-slice image when ButtonImageScaleType is set to `Enum.ScaleType.Slice`. |

#### Text

| Font | A `Enum.Font` enum value for the name tag and button text. |
| --- | --- |
| TextColor | A `Datatype.Color3` for all text within the ACM. |
| TextScale | A float value to scale the default text sizes of each element. |

#### Various image

| LeaveMenuImage | An asset ID of an image for the ACM close button. |
| --- | --- |
| ScrollLeftImage | An asset ID of an image for the carousel "scroll left" button. |
| ScrollRightImage | A valid asset ID of an image for the carousel "scroll right" button. |

#### Selected character

| SelectedCharacterIndicator | The `Class.MeshPart` which floats above a character's head to indicate they are selected. |
| --- | --- |

#### Size and position

| Size | A `Datatype.UDim2` for the overall size of the ACM. |
| --- | --- |
| MinSize | A `Datatype.Vector2` specifying the minimum size of the ACM. |
| MaxSize | A `Datatype.Vector2` specifying the maximum size of the ACM. |
| AspectRatio | A float value specifying the relative width and height of the ACM. |
| AnchorPoint | The `Class.GuiObject.AnchorPoint\|AnchorPoint` of the ACM. |
| OnScreenPosition | A `Datatype.UDim2` specifying the on-screen position of the ACM (the position where it tweens to when opened). |
| OffScreenPosition | A `Datatype.UDim2` specifying the off-screen position of the ACM (the position where it tweens from/to when opened/closed). |

### Example customization

The following code sample customizes the ACM theme using some basic parameters:

```lua
local StarterGui = game:GetService("StarterGui")

StarterGui:SetCore("AvatarContextMenuTheme", {
	BackgroundImage = "",
	BackgroundTransparency = 0.5,
	BackgroundColor = Color3.fromRGB(111, 145, 242),
	NameTagColor = Color3.fromRGB(0, 0, 200),
	NameUnderlineColor = Color3.fromRGB(213, 233, 255),
	ButtonFrameColor = Color3.fromRGB(15, 24, 65),
	ButtonFrameTransparency = 0.2,
	ButtonUnderlineColor = Color3.fromRGB(213, 233, 255),
	Font = Enum.Font.SciFi
})
```
