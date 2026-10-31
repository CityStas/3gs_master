---
title: "Moods"
url: /docs/en-us/art/characters/facial-animation/moods
last_updated: 2026-10-30T19:55:35Z
description: "Moods are a type of facial animation that loop indefinitely, allowing users to express persistent facial emotion."
---

# Moods

A **mood** is a type of facial animation for [dynamic heads](/docs/en-us/avatar/dynamic-heads.md) that loops indefinitely, allowing users to express themselves and react to others with a persistent facial emotion. Moods play simultaneously with other character [default animations](/docs/en-us/animation/using.md#default-character-animations), such as walking, climbing, and swimming, and if the default animation has a facial animation, the default animation blends with the character's mood.

_Default mood_

_Open mouth mood_

> **Info:** A mood is a type of facial animation, but not all facial animations are moods. While a mood refers to a specific animation slot that belongs to each character, a facial animation refers to **any** animation that modifies the face channels.
## Create moods

If you have a character model with an animatable head, you can create any mood animation you can think of using the [Face Animation Editor](/docs/en-us/art/characters/facial-animation/animate-heads.md#use-the-face-animation-editor). If you don't want to use the [Blocky](../../../assets/avatar/dynamic-heads/reference-files/BlockyCharacter.fbx) or [Goblin](../../../assets/avatar/dynamic-heads/reference-files/GoblinCharacter.zip) reference character models, you can create or modify an existing model to support animated heads in a third-party modeling software, such as Blender or Maya. For information on how to create an animatable head, see [Create basic heads](/docs/en-us/art/characters/facial-animation/create-basic-heads.md).

To create a mood:

1. Add a character model with an animatable head to the viewport.
2. Open the **Face Animation Editor**.
  1. From the toolbar's **Avatar** tab, click **Clip Editor**. The [Animation Editor](/docs/en-us/animation/editor.md) window displays.
  2. In the viewport, select your character model with an animatable head.
  3. In the editor's [track list](/docs/en-us/animation/editor.md#interface), click the **Face** button. The **Face Animation Editor** displays to the left of the track list.
3. In the **Face Animation Editor**, adjust sliders for the facial parts you want to manipulate. Animation tracks for each facial part you manipulate automatically display in the track list along with keyframes for your current position in the timeline. The character's face also updates in the viewport.
  - To undo a step on a slider, press `Ctrl``Z` (`⌘``Z`).
  - To redo a step on a slider, press `Ctrl``Y` (`⌘``Y`).
  - To reset a slider to its default value, right click on the slider. A contextual menu displays. Select **Reset Selected**.
4. When you are finished creating your animation, navigate to the **Media and Playback Controls** and click the **…** button. A pop-up menu displays.
5. Select **Save** or **Save As** to save the mood animation. The animation displays in the **Explorer** window as a child of the **AnimSaves** object (itself a child of the rig).
6. **OPTIONAL** To assign an asset ID to your mood animation and save it to the [Toolbox](/docs/en-us/projects/assets/toolbox.md) to use across your games,
  1. In the **Explorer** window, right-click on your new mood animation. A contextual menu displays.
  2. Select **Save to Roblox**. The **Asset Configuration** window displays.
  3. Fill in the following fields:
    - **Title**: A name for your plugin.
    - **Description**: A description that describes what a potential user should expect the plugin to do.
    - **Creator**: The creator you'd like to attribute as the creator of the plugin.
  4. Click the **Submit** button. After a moment, the Asset Configuration dialog displays your mood's `Class.Animation.AnimationID` that you can use to set the mood to characters within your games.

## Set moods

Every character with an animatable head has a child **Animate** `Class.LocalScript` with a child **mood** `Class.StringValue` that contains the mood animation that plays on the character's head. The mood animation's default `Class.Animation.AnimationID` plays a smiling animation, but you can change the character's mood to something else by either directly editing the `Class.Animation.AnimationID` within the mood `Class.StringValue`, or using the `Class.HumanoidDescription` system.

> **Warning:** The code for playing moods doesn't occur in the **Animate** `Class.LocalScript`, but in a hidden, internal Roblox script. While you can't edit this internal script, the **mood** `Class.StringValue` allows you to interact with it in order to customize moods within your games.
### Edit AnimationIds

You can set a specific mood for each character within your game by editing their mood's `Class.Animation.AnimationID` whenever a user triggers an event. For example, the following `Class.Script` edits any previously set mood to an animation that [opens the character's mouth](https://www.roblox.com/library/7715145252/moods-11-FaceAnimation) as soon as the user enters the game:

```lua
local Players = game:GetService("Players")

local function onCharacterAdded(character)
	local humanoid = character:WaitForChild("Humanoid")
	local animateScript = character:WaitForChild("Animate")
	animateScript.mood.Animation1.AnimationId = "rbxassetid://7715145252" -- Mood
end

local function onPlayerAdded(player)
	player.CharacterAppearanceLoaded:Connect(onCharacterAdded)
end

Players.PlayerAdded:Connect(onPlayerAdded)
```

### Use the HumanoidDescription

You can also use the `Class.HumanoidDescription` system to find user characters and edit their `Class.Animation.AnimationID|AnimationIDs` for any default animation. For example, the following `Class.Script` edits any previously set mood to an animation that gives the character a [half-smile](https://www.roblox.com/catalog/10725833199/Chiseled-Good-Looks-Mood) on the left-side of their face whenever their character is idling:

```lua
local humanoid = player.Character and player.Character:FindFirstChildWhichIsA("Humanoid")
if humanoid then
	local descriptionClone = humanoid:GetAppliedDescription()
	descriptionClone.IdleAnimation = 10725833199
	-- Apply modified "descriptionClone" to humanoid
	humanoid:ApplyDescription(descriptionClone)
end
```

## Disable moods

To disable moods from your game, you can delete the mood object underneath the **Animate** `Class.LocalScript`. For example, the following `Class.Script` removes every character's **mood** `Class.StringValue` as soon as they join the game:

```lua
local Players = game:GetService("Players")

local function onCharacterAdded(character)
	local humanoid = character:WaitForChild("Humanoid")
	local animateScript = character:WaitForChild("Animate")
	animateScript.mood:Destroy()
end

local function onPlayerAdded(player)
	player.CharacterAppearanceLoaded:Connect(onCharacterAdded)
end

Players.PlayerAdded:Connect(onPlayerAdded)
```
