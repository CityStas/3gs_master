---
title: "Proximity prompts"
url: /docs/en-us/ui/proximity-prompts
last_updated: 2026-10-30T19:56:02Z
description: "Proximity Prompts allow users to trigger actions when they approach objects in the 3D space."
---

# Proximity prompts

`Class.ProximityPrompt` objects encourage user interaction to trigger an action when they approach in-game objects such as doors, light switches, and buttons. Using this object, you can:

- Indicate what objects a user can interact with in the game.
- Display the action a user can take on the object, then trigger the action through user input such as pressing or holding a key.
- Display the correct input for all input types, such a keyboard, gamepad, and touchscreen keys.

> **Info:** See the [Dungeon Delve](https://www.roblox.com/games/6074153281/Dungeon-Delve) sample place for the fully working proximity prompt examples shown in the video above.
## Create proximity prompts

You must parent proximity prompts to the part, model, or attachment that you want a user to interact with. To add a proximity prompt to a `Class.BasePart`, `Class.Model`, or `Class.Attachment` object:

1. In the [Explorer](/docs/en-us/studio/explorer.md) window, hover over the `Class.BasePart`, `Class.Model`, or `Class.Attachment` and click the ⊕ button. A contextual menu displays.
2. From the menu, insert a **ProximityPrompt**.![Explorer hierarchy showing a ProximityPrompt parented to an Attachment](../assets/ui/proximity-prompt/ProximityPrompt-New.png)

## Customize proximity prompts

You can customize a proximity prompt based on how you want it to [appear](#appearance), when you want it to be [visible](#visibility), and what you want a user to do to [trigger the action](#interactivity).

### Appearance

Proximity prompts need to communicate three things:

- The **object** that a user can interact with.
- The **action** that triggers when they interact with the proximity prompt.
- The **key** that a user must press or hold.

You can specify these through the following properties:

- `Class.ProximityPrompt.ObjectText|ObjectText` An optional name for the object a user can interact with.
- `Class.ProximityPrompt.ActionText|ActionText` An optional name for the action a user will trigger.
- `Class.ProximityPrompt.KeyboardKeyCode|KeyboardKeyCode` The keyboard key a user must press or hold to trigger the action.
- `Class.ProximityPrompt.GamepadKeyCode|GamepadKeyCode` The gamepad key a user must press or hold to trigger the action.![Diagram indicating basic elements of a ProximityPrompt](../assets/ui/proximity-prompt/Prompt-Diagram.png)

### Visibility

You can control when the proximity prompt is visible through its `Class.ProximityPrompt.MaxActivationDistance|MaxActivationDistance`, `Class.ProximityPrompt.RequiresLineOfSight|RequiresLineOfSight`, and `Class.ProximityPrompt.Exclusivity|Exclusivity` properties.

#### MaxActivationDistance

The `Class.ProximityPrompt.MaxActivationDistance|MaxActivationDistance` property allows you to define the range from around the `Class.ProximityPrompt` object that activates the visibility of the proximity prompt. Once a user's character enters that range, the proximity prompt becomes visible.

![Diagram indicating how a character's distance from a ProximityPrompt object affects whether the prompt appears on screen](../assets/ui/proximity-prompt/MaxActivationDistance.jpg) #### RequiresLineOfSight

The `Class.ProximityPrompt.RequiresLineOfSight|RequiresLineOfSight` property activates the visibility of the proximity prompt when there's a clear path from the **camera** to the `Class.ProximityPrompt` object. By default, this property is set to true.

#### Exclusivity

If a user's character is within range of multiple proximity prompts, each proximity prompt's visibility depends on which proximity prompt the camera is pointing at, as well as each proximity prompt's `Class.ProximityPrompt|Exclusivity` property value.

#### OnePerButton

![ProximityPrompt objects set to exclusivity of OnePerButton](../assets/ui/proximity-prompt/Exclusivity-OnePerButton.jpg)_Only one proximity prompt is visible per input keycode. If multiple in-range proximity prompts use different keycodes, they are all visible. However, if multiple in-range proximity prompts use the same keycode, only one proximity prompt is visible at any given time, depending on the camera's view direction._

#### OneGlobally

![ProximityPrompt objects set to exclusivity of OneGlobally](../assets/ui/proximity-prompt/Exclusivity-OneGlobally.jpg)_If multiple proximity prompts are set to this exclusivity, only one prompt is visible at any given time, regardless of the character's proximity or the prompt's keycode. The camera's view direction determines which proximity prompt is visible, useful for minimizing prompt distraction when there are several in an area._

#### AlwaysShow

![ProximityPrompt objects set to exclusivity of AlwaysShow](../assets/ui/proximity-prompt/Exclusivity-AlwaysShow.jpg)_Proximity prompts are always visible when in range, assuming no other factors prevent them from being visible. Be cautious when using this setup, as all visible prompts using the same keycode will trigger on a player's input of that keycode._

### Interactivity

You can customize how a user interacts with a proximity prompt through its `Class.ProximityPrompt.HoldDuration|HoldDuration` and `Class.ProximityPrompt.ClickablePrompt|ClickablePrompt` properties.

#### HoldDuration

The `Class.ProximityPrompt.HoldDuration|HoldDuration` property determines how many seconds a user has to press a key before the proximity prompt's action triggers. If this property has a value of `0`, the proximity prompt's action triggers immediately.

#### ClickablePrompt

The `Class.ProximityPrompt.ClickablePrompt|ClickablePrompt` property specifies if a user can click on a proximity prompt to trigger its action. When set to **true**, a user can interact with the proximity prompt by directly clicking the proximity prompt **or** by pressing the specified key. When set to **false**, a user can only interact with the proximity prompt by pressing the specified key.

> **Warning:** Note that if a user is using a phone or a tablet, they can always interact with the proximity prompt by directly clicking the proximity prompt regardless of the `Class.ProximityPrompt.ClickablePrompt|ClickablePrompt` property's value.
## Script proximity prompts

You can connect to proximity prompt events either on the `Class.ProximityPrompt` object itself or globally through `Class.ProximityPromptService`. The `Class.ProximityPromptService` allows you to manage all proximity prompt behavior from one location, preventing any need for duplicate code in your game.

| Event | Description |
| --- | --- |
| `Class.ProximityPromptService.PromptTriggered\|PromptTriggered` | Fires when a player interacts with a proximity prompt (after the duration for a prompt with non-zero `Class.ProximityPrompt.HoldDuration\|HoldDuration`). |
| `Class.ProximityPromptService.PromptTriggerEnded\|PromptTriggerEnded` | Triggers when the player stops interacting with a proximity prompt. |
| `Class.ProximityPromptService.PromptButtonHoldBegan\|PromptButtonHoldBegan` | Fires when a player begins interacting with a proximity prompt with a non-zero `Class.ProximityPrompt.HoldDuration\|HoldDuration` value. |
| `Class.ProximityPromptService.PromptButtonHoldEnded\|PromptButtonHoldEnded` | Fires when a player stops interacting with a proximity prompt with a non-zero `Class.ProximityPrompt.HoldDuration\|HoldDuration` value. |
| `Class.ProximityPromptService.PromptShown\|PromptShown` | Triggers in `Class.LocalScript\|LocalScripts` when a proximity prompt is made visible. |
| `Class.ProximityPromptService.PromptHidden\|PromptHidden` | Triggers in `Class.LocalScript\|LocalScripts` when a prompt is hidden. |

The following code sample includes a basic framework for using `Class.ProximityPromptService`:

```lua
local ProximityPromptService = game:GetService("ProximityPromptService")

-- Detect when prompt is triggered
local function onPromptTriggered(promptObject, player)

end

-- Detect when prompt hold begins
local function onPromptHoldBegan(promptObject, player)

end

-- Detect when prompt hold ends
local function onPromptHoldEnded(promptObject, player)

end

-- Connect prompt events to handling functions
ProximityPromptService.PromptTriggered:Connect(onPromptTriggered)
ProximityPromptService.PromptButtonHoldBegan:Connect(onPromptHoldBegan)
ProximityPromptService.PromptButtonHoldEnded:Connect(onPromptHoldEnded)
```
