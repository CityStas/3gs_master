---
name: ContextActionService
last_updated: 2026-10-30T19:55:52Z
inherits:
  - Instance
  - Object
type: class
memory_category: Instances
tags:
  - NotCreatable
  - Service
summary: "A service used to bind user input to contextual actions."
---

# Class: ContextActionService

> A service used to bind user input to contextual actions.

## Description

[BindAction](/docs/reference/engine/classes/ContextActionService.md) and the related binding
methods of this service aren't recommended for new work and are planned for
deprecation. Use the
[Input Action System](/docs/en-us/input/input-action-system.md) instead, which is
built for cross-platform input. You create [InputContext](/docs/reference/engine/classes/InputContext.md),
[InputAction](/docs/reference/engine/classes/InputAction.md) and [InputBinding](/docs/reference/engine/classes/InputBinding.md) instances rather than binding
actions from scripts. Each action holds bindings for keyboard, mouse, gamepad
and touch, so the same action works on every platform and responds to
whichever device the player is using, without separate code for each one.

Allows an experience to bind user input to contextual actions, or actions that
are only enabled under some condition or period of time. For example, allowing
a player to open a door only while close by. In code, an action is simply a
string (the name of the action) used by the service to differentiate between
unique actions. The action string is provided to
[BindAction](/docs/reference/engine/classes/ContextActionService.md) and
[UnbindAction](/docs/reference/engine/classes/ContextActionService.md), among other member
functions. If two actions are bound to the same input, the most recently bound
will take priority. When the most recent action is unbound, the one bound
before that takes control again. Since this service deals with user input, you
can only use it in client-side [LocalScripts](/docs/reference/engine/classes/LocalScript.md).

#### Context and Action

A **context** is simply a condition during which a player may perform some
action. Some examples include holding a [Tool](/docs/reference/engine/classes/Tool.md), being
[seated](/docs/reference/engine/classes/Seat.md) in a car or standing near a door. Whatever the case may
be, it is up to your [LocalScripts](/docs/reference/engine/classes/LocalScript.md) to call
[BindAction](/docs/reference/engine/classes/ContextActionService.md) when the context is
entered and [UnbindAction](/docs/reference/engine/classes/ContextActionService.md) when the
context is left.

An **action** is simply some input that can be performed by the player while
in that context. Such an action could open/close some menu, trigger a
secondary tool action or send a request to the server using
[RemoteFunction:InvokeServer()](/docs/reference/engine/classes/RemoteFunction.md). An action is identified by a unique
string as the first parameter of both
[BindAction](/docs/reference/engine/classes/ContextActionService.md) and
[UnbindAction](/docs/reference/engine/classes/ContextActionService.md). The string can be
anything, but it should reflect the **action being performed, not the input
being used**. For example, don't use "KeyH" as an action name - use "CarHorn"
instead. It is best to define your actions as a constant at the top of your
script since you will use it in at least three different places in your code.

#### Binding Actions Contextually

It's better to use ContextActionService's
[BindAction](/docs/reference/engine/classes/ContextActionService.md) than
[UserInputService.InputBegan](/docs/reference/engine/classes/UserInputService.md) for most cases. For
[UserInputService.InputBegan](/docs/reference/engine/classes/UserInputService.md), your connected function would have to
check if the player is in the context of the action being performed. In most
cases, this is harder than just calling a function when a context is entered/
left. For example, if you want to have the `H` key trigger a car horn sound
while the player is sitting in it, the player might type "hello" in chat or
otherwise use the `H` key for something else. It is harder to determine if
something else is using the H key (like chat) - the car might honk when the
player didn't mean to. If you instead use
[BindAction](/docs/reference/engine/classes/ContextActionService.md) and
[UnbindAction](/docs/reference/engine/classes/ContextActionService.md) when the player
enters/leaves the car, [ContextActionService](/docs/reference/engine/classes/ContextActionService.md) will make sure that `H`
key presses trigger the honk action only when it is the most recently bound
action. If something else (like chat) takes control, you won't have to worry
about checking that.

#### Inspecting Bound Actions

To see a list of actions and their bound inputs, you can inspect the "Action
Bindings" tab in the Developer Console (F9 while in game). This shows all
bindings, including those bound by Roblox core scripts and default
camera/control scripts too. This is useful for debugging if your actions are
being bound/unbound at the correct times, or if some other action is stealing
input from your actions. For example, if you are attempting to bind
<kbd>W</kbd><kbd>A</kbd><kbd>S</kbd><kbd>D</kbd>, it may be the case that
default character movement scripts are binding over those same keys.
Similarly, the camera control script can steal right-click input if the script
runs after yours.

#### Keyboardless Input

This service is especially useful for supporting gamepad and touch input. For
gamepad input, you might choose to bind the B button to an action that returns
the user to the previous menu when they enter another menu. For touch,
on-screen touch buttons can be used in place of key presses: these buttons
display only while the action is bound, and the position, text and/or images
of these buttons can be configured through this service. They're somewhat
limited in the amount of customization provided by this service; it's usually
a better idea to make your own on-screen buttons using [ImageButton](/docs/reference/engine/classes/ImageButton.md) or
[TextButton](/docs/reference/engine/classes/TextButton.md).

## Code Samples

**ContextActionService Tool Reload**

This example properly shows how to use ContextActionService in binding user
input to a contextual action. The context is the tool being equipped; the
action is reloading some weapon. Test this code sample by placing it in a
LocalScript parented to a Tool. When the Tool is equipped, a "Reload" action
is bound, and when the Tool is unequipped the "Reload" action is unbound. When
the player presses R with the Tool equipped, the message "Reloading!" will
appear.

```lua
local ContextActionService = game:GetService("ContextActionService")

local ACTION_RELOAD = "Reload"

local tool = script.Parent

local function handleAction(actionName, inputState, _inputObject)
	if actionName == ACTION_RELOAD and inputState == Enum.UserInputState.Begin then
		print("Reloading!")
	end
end

tool.Equipped:Connect(function()
	ContextActionService:BindAction(ACTION_RELOAD, handleAction, true, Enum.KeyCode.R)
end)

tool.Unequipped:Connect(function()
	ContextActionService:UnbindAction(ACTION_RELOAD)
end)
```

## Methods

### Method: ContextActionService:BindAction

**Signature:** `ContextActionService:BindAction(actionName: string, functionToBind: Function, createTouchButton: boolean, inputTypes: Tuple): ()`

Bind an action to user input given an action handling function. Upon a
matching input being performed, the action handler function will be called
with the arguments listed below. Valid input enum items include those
within the following: [KeyCode](/docs/reference/engine/enums/KeyCode.md), [UserInputType](/docs/reference/engine/enums/UserInputType.md) or
[PlayerActions](/docs/reference/engine/enums/PlayerActions.md) . Call this function when a player **enters the
context** in which an action can be performed. When the player leaves the
context, call [UnbindAction()](/docs/reference/engine/classes/ContextActionService.md)
with the same `actionName`.

The code sample below shows how a [Sound](/docs/reference/engine/classes/Sound.md) can be
[played](/docs/reference/engine/classes/Sound.md) while a key (<kbd>H</kbd>), game pad button,
or touch screen button is pressed.

```lua
local ContextActionService = game:GetService("ContextActionService")

-- A car horn sound
local honkSound = Instance.new("Sound", workspace)
honkSound.Looped = true
honkSound.SoundId = "rbxassetid://9120386436"

local function handleAction(actionName, inputState, inputObject)
	if actionName == "HonkHorn" then
		if inputState == Enum.UserInputState.Begin then
			honkSound:Play()
		else
			honkSound:Pause()
		end
	end
end

-- When the player sits in the vehicle:
ContextActionService:BindAction("HonkHorn", handleAction, true, Enum.KeyCode.H, Enum.KeyCode.ButtonY)

-- When the player gets out:
ContextActionService:UnbindAction("HonkHorn")
```

#### Action Handler Parameters

The action handler functions are called with the following parameters:

| # | Type | Description |
| --- | --- | --- |
| 1 | `string` | The same string that was originally passed to [BindAction()](/docs/reference/engine/classes/ContextActionService.md). This allows one function to handle multiple actions at once, if necessary. |
| 2 | [UserInputState](/docs/reference/engine/enums/UserInputState.md) | The state of the input. [Cancel](/docs/reference/engine/enums/UserInputState\.md) is sent if some input was in progress and another action bound over that in-progress input, or if the in-progress bound action was unbound through [UnbindAction()](/docs/reference/engine/classes/ContextActionService.md). |
| 3 | `InputObject` | An object that contains information about the input (varies based on [UserInputType](/docs/reference/engine/enums/UserInputType.md)). The [InputObject](/docs/reference/engine/classes/InputObject.md) sometimes won't match the inputs the action was bound to: when the [Cancel](/docs/reference/engine/enums/UserInputState\.md) state is sent, this object will be [KeyCode.Unknown](/docs/reference/engine/enums/KeyCode.md) and [UserInputType.None](/docs/reference/engine/enums/UserInputType.md). |

#### Action Bindings Stack

Action bindings behave like a stack: if two actions are bound to the same
user input, the **most recently bound** action handler will be used. If an
action handler returns [ContextActionResult.Pass](/docs/reference/engine/enums/ContextActionResult.md), the next most
recently bound action handler will be called, and so on until a handler
sinks the input (by returning `nil` or [ContextActionResult.Sink](/docs/reference/engine/enums/ContextActionResult.md)).
When [UnbindAction](/docs/reference/engine/classes/ContextActionService.md) is called,
the action handler is removed from the stack. This stack behavior can be
overridden using
[BindActionAtPriority](/docs/reference/engine/classes/ContextActionService.md),
where an additional priority parameter after `createTouchButton` may
override the order in which actions are bound (higher before lower).

#### Touch Buttons

In addition to input types, this function's third parameter controls
whether a button is created for
[TouchEnabled](/docs/reference/engine/classes/UserInputService.md) devices. Upon the first
touch button's creation, a [ScreenGui](/docs/reference/engine/classes/ScreenGui.md) named "ContextActionGui" is
added to the [PlayerGui](/docs/reference/engine/classes/PlayerGui.md). Inside the ScreenGui is a [Frame](/docs/reference/engine/classes/Frame.md)
called "ContextButtonFrame" is added. It is in this frame in which
[ImageButtons](/docs/reference/engine/classes/ImageButton.md) for bound actions are parented; you can
use [GetButton()](/docs/reference/engine/classes/ContextActionService.md) to retrieve such
buttons for customization. A maximum of 7 touch buttons can be created
through [BindAction()](/docs/reference/engine/classes/ContextActionService.md).

*Security: None · Thread Safety: Unsafe · Capabilities: Input*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `actionName` | `string` |  | A string representing the action being performed (e.g. "HonkHorn" or "OpenDoor"). |
| `functionToBind` | `Function` |  | The action-handling function, called with the following parameters when the bound inputs are triggered: string (actionName), [UserInputState](/docs/reference/engine/enums/UserInputState.md) and an InputObject. |
| `createTouchButton` | `boolean` |  | Whether a GUI button should be created for the action on touch input devices. |
| `inputTypes` | `Tuple` |  | Any number of [KeyCode](/docs/reference/engine/enums/KeyCode.md) or [UserInputType](/docs/reference/engine/enums/UserInputType.md) representing the inputs to bind to the action. |

**Returns:** `()`

**ContextActionService Tool Reload**

This example properly shows how to use ContextActionService in binding user
input to a contextual action. The context is the tool being equipped; the
action is reloading some weapon. Test this code sample by placing it in a
LocalScript parented to a Tool. When the Tool is equipped, a "Reload" action
is bound, and when the Tool is unequipped the "Reload" action is unbound. When
the player presses R with the Tool equipped, the message "Reloading!" will
appear.

```lua
local ContextActionService = game:GetService("ContextActionService")

local ACTION_RELOAD = "Reload"

local tool = script.Parent

local function handleAction(actionName, inputState, _inputObject)
	if actionName == ACTION_RELOAD and inputState == Enum.UserInputState.Begin then
		print("Reloading!")
	end
end

tool.Equipped:Connect(function()
	ContextActionService:BindAction(ACTION_RELOAD, handleAction, true, Enum.KeyCode.R)
end)

tool.Unequipped:Connect(function()
	ContextActionService:UnbindAction(ACTION_RELOAD)
end)
```

**General Action Handler**

This code sample uses ContextActionService to bind an action named
"BoundAction" to a general action handler function on the `F` key. Place this
in a LocalScript inside StarterPlayerScripts and press `F` to see the message
"Handling action: BoundAction".

```lua
local ContextActionService = game:GetService("ContextActionService")

local function handleAction(actionName, inputState, inputObj)
	if inputState == Enum.UserInputState.Begin then
		print("Handling action: " .. actionName)
		print(inputObj.UserInputType)
	end

	-- Since this function does not return anything, this handler will
	-- "sink" the input and no other action handlers will be called after
	-- this one.
end

ContextActionService:BindAction("BoundAction", handleAction, false, Enum.KeyCode.F)
```

**Stacked Action Handlers**

This code sample demonstrates how BindAction acts like a stack. It binds two
actions, FirstAction (`Z`, `X`, and `C` keys) and SecondAction (`Z` and `X`
keys) to two action handling functions. The second one will pass on a certain
input (the `X` key).

Both actions use the `Z` and `X` keys, however the second handler will pass
input only if `X` is pressed. So, when `X` is pressed, the second handler is
called and then the first. The first action is also bound to the `C` key, and
can be triggered even though the other two inputs are "covered" by the second
action.

Test this code out by pasting it into a LocalScript within
StarterPlayerScripts, then pressing `Z`, `X` and `C`. Observe which action
handlers are called with what actions.

```lua
local ContextActionService = game:GetService("ContextActionService")

-- Define an action handler for FirstAction
local function actionHandlerOne(actionName, inputState, _inputObj)
	if inputState == Enum.UserInputState.Begin then
		print("Action Handler One: " .. actionName)
	end
	-- This action handler returns nil, so it is assumed that
	-- it properly handles the action.
end

-- Binding the action FirstAction (it's on the bottom of the stack)
ContextActionService:BindAction("FirstAction", actionHandlerOne, false, Enum.KeyCode.Z, Enum.KeyCode.X, Enum.KeyCode.C)

-- Define an action handler for SecondAction
local function actionHandlerTwo(actionName, inputState, inputObj)
	if inputState == Enum.UserInputState.Begin then
		print("Action Handler Two: " .. actionName)
	end

	if inputObj.KeyCode == Enum.KeyCode.X then
		return Enum.ContextActionResult.Pass
	else
		-- Returning nil implicitly Sinks inputs
		return Enum.ContextActionResult.Sink
	end
end

-- Binding SecondAction over the first action (since it bound more recently, it is on the top of the stack)
-- Note that SecondAction uses the same keys as
ContextActionService:BindAction("SecondAction", actionHandlerTwo, false, Enum.KeyCode.Z, Enum.KeyCode.X)
```

### Method: ContextActionService:BindActionAtPriority

**Signature:** `ContextActionService:BindActionAtPriority(actionName: string, functionToBind: Function, createTouchButton: boolean, priorityLevel: int, inputTypes: Tuple): ()`

BindActionAtPriority behaves like
[BindAction](/docs/reference/engine/classes/ContextActionService.md) but also allows a
priority to be assigned to the bound action. If multiple actions are bound
to the same input, the higher priority function is called regardless of
the order in which the actions were bound. In other words, this function
overrides the normal "stack" behavior of BindAction.

*Security: None · Thread Safety: Unsafe · Capabilities: Input*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `actionName` | `string` |  | A string representing the action being performed (e.g. "HonkHorn" or "OpenDoor"). |
| `functionToBind` | `Function` |  | The action-handling function, called with the following parameters when the bound inputs are triggered: string (actionName), [UserInputState](/docs/reference/engine/enums/UserInputState.md) and an InputObject. |
| `createTouchButton` | `boolean` |  | Whether a GUI button should be created for the action on touch input devices. |
| `priorityLevel` | `int` |  | The priority level at which the action should be bound (higher considered before lower). |
| `inputTypes` | `Tuple` |  | Any number of Enum.KeyCode or Enum.UserInputType representing the inputs to bind to the action. |

**Returns:** `()`

**ContextActionService BindAction Priorities**

This code sample demonstrates how
[ContextActionService:BindActionAtPriority()](/docs/reference/engine/classes/ContextActionService.md) can be used to bind
actions out of order yet still have the same priority levels. Normally,
[BindAction()](/docs/reference/engine/classes/ContextActionService.md) would operate on order
(last bound action has highest priority), but priority levels override this.
You can test this code by pasting it into a `Script` with `RunContext` =
`Client` in `ReplicatedStorage`.

```lua
local ContextActionService = game:GetService("ContextActionService")

local INPUT_KEY1 = Enum.KeyCode.Q
local INPUT_KEY2 = Enum.KeyCode.E

local function handleThrow(actionName: string, inputState: Enum.UserInputState, inputObject: InputObject)
	if inputState ~= Enum.UserInputState.Begin then
		return Enum.ContextActionResult.Pass
	end
	print(`Action [{actionName}] occurred. KeyCode [{inputObject.KeyCode}] pressed.`)

	return Enum.ContextActionResult.Sink
end

local function handlePunch(actionName: string, inputState: Enum.UserInputState, inputObject: InputObject)
	if inputState ~= Enum.UserInputState.Begin then
		return Enum.ContextActionResult.Pass
	end
	print(`Action [{actionName}] occurred. KeyCode [{inputObject.KeyCode}] pressed.`)

	return Enum.ContextActionResult.Sink
end

-- Without specifying priority, the most recently bound action is called first,
-- so pressing INPUT_KEY1 prints "Punch" and then sinks the input.
ContextActionService:BindAction("DefaultThrow", handleThrow, false, INPUT_KEY1)
ContextActionService:BindAction("DefaultPunch", handlePunch, false, INPUT_KEY1)

-- Here we bind both functions in the same order as above, but with explicitly swapped priorities.
-- That is, we give "Throw" a higher priority of 2 so it will be called first,
-- despite "Punch" still being bound more recently.
-- Pressing INPUT_KEY2 prints "Throw" and then sinks the input.
ContextActionService:BindActionAtPriority("PriorityThrow", handleThrow, false, 2, INPUT_KEY2)
ContextActionService:BindActionAtPriority("PriorityPunch", handlePunch, false, 1, INPUT_KEY2)
```

### Method: ContextActionService:BindActivate

**Signature:** `ContextActionService:BindActivate(userInputTypeForActivation: UserInputType, keyCodesForActivation: Tuple): ()`

Bind a [KeyCode](/docs/reference/engine/enums/KeyCode.md) that can be used with a [UserInputType](/docs/reference/engine/enums/UserInputType.md) to
activate [ClickDetector](/docs/reference/engine/classes/ClickDetector.md) events, [Tools](/docs/reference/engine/classes/Tool.md), and
[GuiButtons](/docs/reference/engine/classes/GuiButton.md). When the given key/button is pressed, it
fires the [Mouse.Button1Down](/docs/reference/engine/classes/Mouse.md) event on the mouse sent to
[Tool.Equipped](/docs/reference/engine/classes/Tool.md). This in turn fires the [Tool.Activated](/docs/reference/engine/classes/Tool.md) event
if [Tool.ManualActivationOnly](/docs/reference/engine/classes/Tool.md) is not set to true. For gamepad
input, this function is called by the default control scripts in order to
bind the ButtonR2 [KeyCode](/docs/reference/engine/enums/KeyCode.md).

Note that the [UserInputType](/docs/reference/engine/enums/UserInputType.md) specified must be `Keyboard` or
`Gamepad1` through `Gamepad8` in order to be valid.

*Security: None · Thread Safety: Unsafe · Capabilities: Input*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `userInputTypeForActivation` | `UserInputType` |  | Must be Keyboard or Gamepad1 through Gamepad8. |
| `keyCodesForActivation` | `Tuple` |  | Any number of [KeyCode](/docs/reference/engine/enums/KeyCode.md) values that trigger [Tool](/docs/reference/engine/classes/Tool.md) activation for the specified [UserInputType](/docs/reference/engine/enums/UserInputType.md). |

**Returns:** `()`

### Method: ContextActionService:GetAllBoundActionInfo

**Signature:** `ContextActionService:GetAllBoundActionInfo(): Dictionary`

GetAllBoundActioninfo returns a table which maps all actions' names (those
originally passed to [BindAction](/docs/reference/engine/classes/ContextActionService.md))
to a table returned by
[GetBoundActionInfo](/docs/reference/engine/classes/ContextActionService.md) when
called with the action name itself. Using this function, you can inspect
all presently bound actions. This is useful when debugging their priority
levels or stack orders.

*Security: None · Thread Safety: Unsafe · Capabilities: Input*

**Returns:** `Dictionary` — A dictionary mapping each bound action name to its info table.

### Method: ContextActionService:GetBoundActionInfo

**Signature:** `ContextActionService:GetBoundActionInfo(actionName: string): Dictionary`

GetBoundActionInfo returns a table with the following keys describing a
bound action given its name. To get the same information for all actions
at once, use
[GetAllBoundActionInfo](/docs/reference/engine/classes/ContextActionService.md).

| Name | Type | Description |
| --- | --- | --- |
| `stackOrder` | number | Describes the index of the action on the stack (increasing) |
| `priorityLevel`* | number | Describes the [priority](/docs/reference/engine/classes/ContextActionService.md) level of the action |
| `createTouchButton` | bool | Describes whether a touch button should be created on [TouchEnabled](/docs/reference/engine/classes/UserInputService.md) devices |
| `inputTypes` | table | The input types passed to [BindAction](/docs/reference/engine/classes/ContextActionService.md) for which this action will trigger |
| `description`† | string | The description of action set by [SetDescription](/docs/reference/engine/classes/ContextActionService.md) |
| `title`† | string | The title of the action set by [SetTitle](/docs/reference/engine/classes/ContextActionService.md) |
| `image`† | string | The image of the action's touch button set by [SetImage](/docs/reference/engine/classes/ContextActionService.md) |

\* Priority level will still be included even if
[BindActionAtPriority](/docs/reference/engine/classes/ContextActionService.md)
wasn't used - by default it will be 2000.

† Indicates that this field will be `nil` if the associated method was not
called for the given action.

*Security: None · Thread Safety: Unsafe · Capabilities: Input*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `actionName` | `string` |  | The name of the action originally passed to BindAction. |

**Returns:** `Dictionary` — A dictionary with keys describing the bound action, including
stackOrder, priorityLevel, createTouchButton, inputTypes, description,
title, and image.

### Method: ContextActionService:GetButton

**Signature:** `ContextActionService:GetButton(actionName: string): Instance`

GetButton returns the [ImageButton](/docs/reference/engine/classes/ImageButton.md) created by
[BindAction](/docs/reference/engine/classes/ContextActionService.md) if its third
parameter was true and the device is
[TouchEnabled](/docs/reference/engine/classes/UserInputService.md). The only parameter to
this function must match exactly the name of the action originally sent to
BindAction.

If no such action was bound or if a button was not created, this function
returns `nil`.

*Yields · Security: None · Thread Safety: Unsafe · Capabilities: Input*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `actionName` | `string` |  | The name of the action originally passed to BindAction. |

**Returns:** `Instance` — An ImageButton created by BindAction.

### Method: ContextActionService:GetCurrentLocalToolIcon

**Signature:** `ContextActionService:GetCurrentLocalToolIcon(): string`

GetCurrentLocalToolIcon will return the [BackpackItem.TextureId](/docs/reference/engine/classes/BackpackItem.md) of
a [Tool](/docs/reference/engine/classes/Tool.md) currently [equipped](/docs/reference/engine/classes/Tool.md) by the
[Player](/docs/reference/engine/classes/Player.md), or `nil` if there is no such Tool or if the player lacks a
[Character](/docs/reference/engine/classes/Player.md).

*Security: None · Thread Safety: Unsafe · Capabilities: Input*

**Returns:** `string` — A content string from the Tool's TextureId, or `nil` if one could not
be found.

### Method: ContextActionService:SetDescription

**Signature:** `ContextActionService:SetDescription(actionName: string, description: string): ()`

SetDescription will set the description of an action bound by
[BindAction](/docs/reference/engine/classes/ContextActionService.md). In a list of
available actions, this would be text that describes the given action.

Although the name may suggest that this method is related to the family of
functions that customize a touch button for actions that create them
([SetTitle](/docs/reference/engine/classes/ContextActionService.md),
[SetImage](/docs/reference/engine/classes/ContextActionService.md) and
[SetPosition](/docs/reference/engine/classes/ContextActionService.md)), this method does
not affect such a button. This method merely sets a text description of an
action, and nothing more.

*Security: None · Thread Safety: Unsafe · Capabilities: Input*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `actionName` | `string` |  | The name of the action originally passed to BindAction. |
| `description` | `string` |  | A text description of the action, such as "Honk the car's horn" or "Open the inventory". |

**Returns:** `()`

**ContextActionService Touch Button**

This code sample demonstrates binding an "Inspect" action to a touch button
created automatically by `ContextActionService`. The button is customized
using [SetImage()](/docs/reference/engine/classes/ContextActionService.md),
[SetTitle()](/docs/reference/engine/classes/ContextActionService.md),
[SetDescription()](/docs/reference/engine/classes/ContextActionService.md) and
[SetPosition()](/docs/reference/engine/classes/ContextActionService.md). The button is
further customized by using
[GetButton()](/docs/reference/engine/classes/ContextActionService.md) to get a reference to the
`ImageButton` itself and tinting it green by setting
[ImageButton.ImageColor3](/docs/reference/engine/classes/ImageButton.md).

Paste this code into a `LocalScript` placed within `StarterPlayerScripts` to
test it. In Studio, be sure to toggle the touch device emulator in order for
the button to actually be created.

```lua
local ContextActionService = game:GetService("ContextActionService")

local ACTION_INSPECT = "Inspect"
local INPUT_INSPECT = Enum.KeyCode.E
local IMAGE_INSPECT = "rbxassetid://1826746856" -- Image of a speech bubble with ? in it

local function handleAction(actionName, inputState, _inputObject)
	if actionName == ACTION_INSPECT and inputState == Enum.UserInputState.End then
		print("Inspecting")
	end
end

-- For touch devices, a button is created on-screen automatically via the 3rd parameter
ContextActionService:BindAction(ACTION_INSPECT, handleAction, true, INPUT_INSPECT)
-- We can use these functions to customize the button:
ContextActionService:SetImage(ACTION_INSPECT, IMAGE_INSPECT)
ContextActionService:SetTitle(ACTION_INSPECT, "Look")
ContextActionService:SetDescription(ACTION_INSPECT, "Inspect something.")
ContextActionService:SetPosition(ACTION_INSPECT, UDim2.new(0, 0, 0, 0))
-- We can manipulate the button directly using ContextActionService:GetButton
local imgButton = ContextActionService:GetButton(ACTION_INSPECT)
if imgButton then -- Remember: non-touch devices won't return anything!
	imgButton.ImageColor3 = Color3.new(0.5, 1, 0.5) -- Tint the ImageButton green
end
```

**Expected output:** When run on a touch-enabled device, a green-tinted button will appear. The message "Inspecting" will be printed when the button is pressed then released, or when the E key is pressed.

### Method: ContextActionService:SetImage

**Signature:** `ContextActionService:SetImage(actionName: string, image: string): ()`

This method sets the image shown on a touch button created by
[BindAction()](/docs/reference/engine/classes/ContextActionService.md). Specifically, it
sets the [ImageLabel.Image](/docs/reference/engine/classes/ImageLabel.md) property of the [ImageLabel](/docs/reference/engine/classes/ImageLabel.md)
within the [ImageButton](/docs/reference/engine/classes/ImageButton.md) that would be returned by
[GetButton](/docs/reference/engine/classes/ContextActionService.md). If no such bound
action exists (e.g. nothing is returned by GetButton), this function does
nothing and throws no error.

This function is part of a family of methods that customize the touch
button of an action. Others in this family include
[SetPosition](/docs/reference/engine/classes/ContextActionService.md) and
[SetTitle](/docs/reference/engine/classes/ContextActionService.md).

*Security: None · Thread Safety: Unsafe · Capabilities: Input*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `actionName` | `string` |  | The name of the action originally passed to BindAction. |
| `image` | `string` |  | The value to which the Image property should be set. |

**Returns:** `()`

**ContextActionService Touch Button**

This code sample demonstrates binding an "Inspect" action to a touch button
created automatically by `ContextActionService`. The button is customized
using [SetImage()](/docs/reference/engine/classes/ContextActionService.md),
[SetTitle()](/docs/reference/engine/classes/ContextActionService.md),
[SetDescription()](/docs/reference/engine/classes/ContextActionService.md) and
[SetPosition()](/docs/reference/engine/classes/ContextActionService.md). The button is
further customized by using
[GetButton()](/docs/reference/engine/classes/ContextActionService.md) to get a reference to the
`ImageButton` itself and tinting it green by setting
[ImageButton.ImageColor3](/docs/reference/engine/classes/ImageButton.md).

Paste this code into a `LocalScript` placed within `StarterPlayerScripts` to
test it. In Studio, be sure to toggle the touch device emulator in order for
the button to actually be created.

```lua
local ContextActionService = game:GetService("ContextActionService")

local ACTION_INSPECT = "Inspect"
local INPUT_INSPECT = Enum.KeyCode.E
local IMAGE_INSPECT = "rbxassetid://1826746856" -- Image of a speech bubble with ? in it

local function handleAction(actionName, inputState, _inputObject)
	if actionName == ACTION_INSPECT and inputState == Enum.UserInputState.End then
		print("Inspecting")
	end
end

-- For touch devices, a button is created on-screen automatically via the 3rd parameter
ContextActionService:BindAction(ACTION_INSPECT, handleAction, true, INPUT_INSPECT)
-- We can use these functions to customize the button:
ContextActionService:SetImage(ACTION_INSPECT, IMAGE_INSPECT)
ContextActionService:SetTitle(ACTION_INSPECT, "Look")
ContextActionService:SetDescription(ACTION_INSPECT, "Inspect something.")
ContextActionService:SetPosition(ACTION_INSPECT, UDim2.new(0, 0, 0, 0))
-- We can manipulate the button directly using ContextActionService:GetButton
local imgButton = ContextActionService:GetButton(ACTION_INSPECT)
if imgButton then -- Remember: non-touch devices won't return anything!
	imgButton.ImageColor3 = Color3.new(0.5, 1, 0.5) -- Tint the ImageButton green
end
```

**Expected output:** When run on a touch-enabled device, a green-tinted button will appear. The message "Inspecting" will be printed when the button is pressed then released, or when the E key is pressed.

### Method: ContextActionService:SetPosition

**Signature:** `ContextActionService:SetPosition(actionName: string, position: UDim2): ()`

This method sets the position of a touch button created by
[BindAction()](/docs/reference/engine/classes/ContextActionService.md). Specifically, it
sets the [GuiObject.Position](/docs/reference/engine/classes/GuiObject.md) property of the [ImageButton](/docs/reference/engine/classes/ImageButton.md)
that would be returned by
[GetButton](/docs/reference/engine/classes/ContextActionService.md). If no such bound
action exists (e.g. nothing is returned by GetButton), this function does
nothing and throws no error.

This function is part of a family of methods that customize the touch
button of an action. Others in this family include
[SetImage](/docs/reference/engine/classes/ContextActionService.md) and
[SetTitle](/docs/reference/engine/classes/ContextActionService.md).

*Security: None · Thread Safety: Unsafe · Capabilities: Input*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `actionName` | `string` |  | The name of the action originally passed to BindAction. |
| `position` | `UDim2` |  | The position within the ContextButtonFrame. |

**Returns:** `()`

**ContextActionService Touch Button**

This code sample demonstrates binding an "Inspect" action to a touch button
created automatically by `ContextActionService`. The button is customized
using [SetImage()](/docs/reference/engine/classes/ContextActionService.md),
[SetTitle()](/docs/reference/engine/classes/ContextActionService.md),
[SetDescription()](/docs/reference/engine/classes/ContextActionService.md) and
[SetPosition()](/docs/reference/engine/classes/ContextActionService.md). The button is
further customized by using
[GetButton()](/docs/reference/engine/classes/ContextActionService.md) to get a reference to the
`ImageButton` itself and tinting it green by setting
[ImageButton.ImageColor3](/docs/reference/engine/classes/ImageButton.md).

Paste this code into a `LocalScript` placed within `StarterPlayerScripts` to
test it. In Studio, be sure to toggle the touch device emulator in order for
the button to actually be created.

```lua
local ContextActionService = game:GetService("ContextActionService")

local ACTION_INSPECT = "Inspect"
local INPUT_INSPECT = Enum.KeyCode.E
local IMAGE_INSPECT = "rbxassetid://1826746856" -- Image of a speech bubble with ? in it

local function handleAction(actionName, inputState, _inputObject)
	if actionName == ACTION_INSPECT and inputState == Enum.UserInputState.End then
		print("Inspecting")
	end
end

-- For touch devices, a button is created on-screen automatically via the 3rd parameter
ContextActionService:BindAction(ACTION_INSPECT, handleAction, true, INPUT_INSPECT)
-- We can use these functions to customize the button:
ContextActionService:SetImage(ACTION_INSPECT, IMAGE_INSPECT)
ContextActionService:SetTitle(ACTION_INSPECT, "Look")
ContextActionService:SetDescription(ACTION_INSPECT, "Inspect something.")
ContextActionService:SetPosition(ACTION_INSPECT, UDim2.new(0, 0, 0, 0))
-- We can manipulate the button directly using ContextActionService:GetButton
local imgButton = ContextActionService:GetButton(ACTION_INSPECT)
if imgButton then -- Remember: non-touch devices won't return anything!
	imgButton.ImageColor3 = Color3.new(0.5, 1, 0.5) -- Tint the ImageButton green
end
```

**Expected output:** When run on a touch-enabled device, a green-tinted button will appear. The message "Inspecting" will be printed when the button is pressed then released, or when the E key is pressed.

### Method: ContextActionService:SetTitle

**Signature:** `ContextActionService:SetTitle(actionName: string, title: string): ()`

SetTitle will set the text shown on a touch button created by
[BindAction](/docs/reference/engine/classes/ContextActionService.md). Specifically, this
sets the [TextLabel.Text](/docs/reference/engine/classes/TextLabel.md) property of a [TextLabel](/docs/reference/engine/classes/TextLabel.md) within the
[ImageButton](/docs/reference/engine/classes/ImageButton.md) that would be returned by
[GetButton](/docs/reference/engine/classes/ContextActionService.md). If no such bound
action exists (e.g. nothing is returned by GetButton), this function does
nothing and throws no error.

This function is part of a family of methods that customize the touch
button of an action. Others in this family include
[SetImage](/docs/reference/engine/classes/ContextActionService.md) and
[SetPosition](/docs/reference/engine/classes/ContextActionService.md).

*Security: None · Thread Safety: Unsafe · Capabilities: Input*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `actionName` | `string` |  | The name of the action originally passed to BindAction. |
| `title` | `string` |  | The text to display on the button. |

**Returns:** `()`

**ContextActionService Touch Button**

This code sample demonstrates binding an "Inspect" action to a touch button
created automatically by `ContextActionService`. The button is customized
using [SetImage()](/docs/reference/engine/classes/ContextActionService.md),
[SetTitle()](/docs/reference/engine/classes/ContextActionService.md),
[SetDescription()](/docs/reference/engine/classes/ContextActionService.md) and
[SetPosition()](/docs/reference/engine/classes/ContextActionService.md). The button is
further customized by using
[GetButton()](/docs/reference/engine/classes/ContextActionService.md) to get a reference to the
`ImageButton` itself and tinting it green by setting
[ImageButton.ImageColor3](/docs/reference/engine/classes/ImageButton.md).

Paste this code into a `LocalScript` placed within `StarterPlayerScripts` to
test it. In Studio, be sure to toggle the touch device emulator in order for
the button to actually be created.

```lua
local ContextActionService = game:GetService("ContextActionService")

local ACTION_INSPECT = "Inspect"
local INPUT_INSPECT = Enum.KeyCode.E
local IMAGE_INSPECT = "rbxassetid://1826746856" -- Image of a speech bubble with ? in it

local function handleAction(actionName, inputState, _inputObject)
	if actionName == ACTION_INSPECT and inputState == Enum.UserInputState.End then
		print("Inspecting")
	end
end

-- For touch devices, a button is created on-screen automatically via the 3rd parameter
ContextActionService:BindAction(ACTION_INSPECT, handleAction, true, INPUT_INSPECT)
-- We can use these functions to customize the button:
ContextActionService:SetImage(ACTION_INSPECT, IMAGE_INSPECT)
ContextActionService:SetTitle(ACTION_INSPECT, "Look")
ContextActionService:SetDescription(ACTION_INSPECT, "Inspect something.")
ContextActionService:SetPosition(ACTION_INSPECT, UDim2.new(0, 0, 0, 0))
-- We can manipulate the button directly using ContextActionService:GetButton
local imgButton = ContextActionService:GetButton(ACTION_INSPECT)
if imgButton then -- Remember: non-touch devices won't return anything!
	imgButton.ImageColor3 = Color3.new(0.5, 1, 0.5) -- Tint the ImageButton green
end
```

**Expected output:** When run on a touch-enabled device, a green-tinted button will appear. The message "Inspecting" will be printed when the button is pressed then released, or when the E key is pressed.

### Method: ContextActionService:UnbindAction

**Signature:** `ContextActionService:UnbindAction(actionName: string): ()`

UnbindAction will unbind an action by name from user inputs so that the
action handler function will no longer be called. Call this function when
the context for some action is no longer applicable, such as closing a
user interface, exiting a car or [unequipping](/docs/reference/engine/classes/Tool.md) a
[Tool](/docs/reference/engine/classes/Tool.md). See [BindAction](/docs/reference/engine/classes/ContextActionService.md) for
more information on how bound actions operate.

This function **will not** throw an error if there is no such action bound
with the given string. Using
[GetAllBoundActionInfo](/docs/reference/engine/classes/ContextActionService.md)
or the Developer Console's "Action Bindings" tab, you can find out what
actions are presently bound.

*Security: None · Thread Safety: Unsafe · Capabilities: Input*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `actionName` | `string` |  | The name of the action to unbind, as originally passed to BindAction. |

**Returns:** `()`

**ContextActionService Tool Reload**

This example properly shows how to use ContextActionService in binding user
input to a contextual action. The context is the tool being equipped; the
action is reloading some weapon. Test this code sample by placing it in a
LocalScript parented to a Tool. When the Tool is equipped, a "Reload" action
is bound, and when the Tool is unequipped the "Reload" action is unbound. When
the player presses R with the Tool equipped, the message "Reloading!" will
appear.

```lua
local ContextActionService = game:GetService("ContextActionService")

local ACTION_RELOAD = "Reload"

local tool = script.Parent

local function handleAction(actionName, inputState, _inputObject)
	if actionName == ACTION_RELOAD and inputState == Enum.UserInputState.Begin then
		print("Reloading!")
	end
end

tool.Equipped:Connect(function()
	ContextActionService:BindAction(ACTION_RELOAD, handleAction, true, Enum.KeyCode.R)
end)

tool.Unequipped:Connect(function()
	ContextActionService:UnbindAction(ACTION_RELOAD)
end)
```

### Method: ContextActionService:UnbindActivate

**Signature:** `ContextActionService:UnbindActivate(userInputTypeForActivation: UserInputType, keyCodeForActivation?: KeyCode): ()`

UnbindActivate unbinds an [KeyCode](/docs/reference/engine/enums/KeyCode.md) used with an [UserInputType](/docs/reference/engine/enums/UserInputType.md)
for activating a [Tool](/docs/reference/engine/classes/Tool.md) (or a [HopperBin](/docs/reference/engine/classes/HopperBin.md)) using
[BindActivate](/docs/reference/engine/classes/ContextActionService.md). This function
essentially undoes the action performed by that function.

*Security: None · Thread Safety: Unsafe · Capabilities: Input*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `userInputTypeForActivation` | `UserInputType` |  | The same UserInputType originally sent to BindActivate. |
| `keyCodeForActivation` | `KeyCode` | `None` | The same KeyCode originally sent to BindActivate. |

**Returns:** `()`

### Method: ContextActionService:UnbindAllActions

**Signature:** `ContextActionService:UnbindAllActions(): ()`

Removes all functions bound. No actionNames will remain. All touch buttons
will be removed. If a button was manipulated manually there is no
guarantee it will be cleaned up.

*Security: None · Thread Safety: Unsafe · Capabilities: Input*

**Returns:** `()`

### Method: ContextActionService:BindActionToInputTypes

**Signature:** `ContextActionService:BindActionToInputTypes(actionName: string, functionToBind: Function, createTouchButton: boolean, inputTypes: Tuple): ()`

> **Deprecated:** This item has been superseded by [ContextActionService:BindAction()](/docs/reference/engine/classes/ContextActionService.md) which should be used in all new work.

This function binds _functionToBind_ to input events such as key presses,
mouse movement, or controller input. The specific input types the engine
listens for are listed as parameters of BindAction. Whenever a player uses
any of these input types, the Roblox Engine calls "functionToBind".
BindAction sets the priorityLevel via [ContextActionPriority](/docs/reference/engine/enums/ContextActionPriority.md) to
Default.Value, which is 2000. Use [ContextActionService:GetButton()](/docs/reference/engine/classes/ContextActionService.md)
to control the priority of bound events.

In addition to input types, BindAction has a createTouchButton parameter.
When this is set to true it creates an [ImageButton](/docs/reference/engine/classes/ImageButton.md) on any device
with a touchscreen. A [ScreenGui](/docs/reference/engine/classes/ScreenGui.md) is also created to put the context
buttons into named ContextActionGui and is parented to [PlayerGui](/docs/reference/engine/classes/PlayerGui.md).
The created ImageButton is parented to this ContextActionGui. GetButton
can be used to retrieve the button that was created.

If an input has more than one function bound to it, each function will be
placed on a stack. A stack obeys the principle of last in first out. So
the first object placed on the stack will be on the top. The next object
placed on the stack becomes the top and the previous object moves one
position down (like a stack of books). When the input is triggered, the
function at the top of the stack is called. If the function returns
[ContextActionResult](/docs/reference/engine/enums/ContextActionResult.md).Pass this will continue down the stack. To
remove a function from being called by all input that it was bound by use
[ContextActionService:UnbindAction()](/docs/reference/engine/classes/ContextActionService.md).

BindAction allows control over whether or not a bound action should be
processed by other actions on the stack using [ContextActionResult](/docs/reference/engine/enums/ContextActionResult.md).
If [ContextActionResult.Pass](/docs/reference/engine/enums/ContextActionResult.md) is returned in the callback function,
every action below it in the stack (last function called gets executed
first) will get a chance to process it. Anything other than Pass will be
treated as [ContextActionResult.Sink](/docs/reference/engine/enums/ContextActionResult.md), including `nil`. It will also
sink if the callback is yielded.

*Security: None · Thread Safety: Unsafe · Capabilities: Input*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `actionName` | `string` |  |  |
| `functionToBind` | `Function` |  |  |
| `createTouchButton` | `boolean` |  |  |
| `inputTypes` | `Tuple` |  |  |

**Returns:** `()`

## Events

### Event: ContextActionService.LocalToolEquipped

**Signature:** `ContextActionService.LocalToolEquipped(toolEquipped: Instance)`

Fires when a [Tool](/docs/reference/engine/classes/Tool.md) is added as a child of the local player's
[Character](/docs/reference/engine/classes/Player.md) model, which occurs when the player
equips the tool. The `toolEquipped` parameter is the [Tool](/docs/reference/engine/classes/Tool.md) instance
that was equipped.

This event fires only for [Tool](/docs/reference/engine/classes/Tool.md) children added to the character, so
it does not fire for non-Tool children. The connection is re-established
each time the player's character respawns.

This event is useful for updating contextual action bindings when a tool
is equipped. For example, you can call
[BindAction](/docs/reference/engine/classes/ContextActionService.md) inside a handler
connected to this event to set up tool-specific input, then call
[UnbindAction](/docs/reference/engine/classes/ContextActionService.md) in the
corresponding [ContextActionService.LocalToolUnequipped](/docs/reference/engine/classes/ContextActionService.md) handler.

*Security: None · Capabilities: Input*

**Parameters:**

| Name | Type | Description |
|------|------|-------------|
| `toolEquipped` | `Instance` | The [Tool](/docs/reference/engine/classes/Tool.md) instance that was equipped. |

### Event: ContextActionService.LocalToolUnequipped

**Signature:** `ContextActionService.LocalToolUnequipped(toolUnequipped: Instance)`

Fires when a [Tool](/docs/reference/engine/classes/Tool.md) is removed from the local player's
[Character](/docs/reference/engine/classes/Player.md) model, which occurs when the player
unequips the tool. The `toolUnequipped` parameter is the [Tool](/docs/reference/engine/classes/Tool.md)
instance that was unequipped.

This event fires only for [Tool](/docs/reference/engine/classes/Tool.md) children removed from the
character, so it does not fire for non-Tool children. The connection is
re-established each time the player's character respawns.

This event is useful for tearing down contextual action bindings when a
tool is unequipped. For example, you can call
[UnbindAction](/docs/reference/engine/classes/ContextActionService.md) inside a handler
connected to this event to remove tool-specific input that was bound in
the corresponding [ContextActionService.LocalToolEquipped](/docs/reference/engine/classes/ContextActionService.md) handler.

*Security: None · Capabilities: Input*

**Parameters:**

| Name | Type | Description |
|------|------|-------------|
| `toolUnequipped` | `Instance` | The [Tool](/docs/reference/engine/classes/Tool.md) instance that was unequipped. |

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