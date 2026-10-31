---
title: "Create player tools"
url: /docs/en-us/tutorials/use-case-tutorials/scripting/intermediate-scripting/create-player-tools
last_updated: 2026-10-30T19:56:01Z
description: "The process for creating and customizing Tools that players can equip and use."
---

# Create player tools

Tools are a simple way to manage items that the player can hold in their hand and use in-game. They can range from weapons such as swords to food items.

In this tutorial, you'll learn how to create a tool in the shape of a laser blaster that will play sound effects when equipped or activated.

## Create the tool

The `Class.Tool` object is the basis of any tool in Roblox, so you'll need to create one. It's easier to change how tools look by adding objects such as Parts and MeshParts to the tool in the workspace where they are visible.

1. Insert a **Tool** into the workspace and name it **Blaster**.
2. Insert a `Class.MeshPart` into the tool.
3. Set the **MeshId** property to `rbxassetid://92656610`.
4. Set the **TextureId** property to `rbxassetid://92658105`.
5. The tool needs a part named **Handle** for the player to hold. Change the name of the MeshPart to **Handle**.

> **Warning:** If you don't include a part named **Handle** in the tool, it will drop to the ground when a player tries to equip it.
## Store the tool

Tools can be kept in the 3D world as **collectable tools** or given to all players as **starter tools**.

### Collectable tool

The blaster is currently a child of **Workspace** so it will be collectable. A player can pick up the tool by touching it, causing it to become a child of the character model; the tool will then be equipped and placed in their hotbar.

During gameplay, unequipped tools are stored within the player's hierarchy in the Backpack and then moved to their character model when equipped. Any tool that becomes a child of a character will be automatically equipped.

_Tripmine Unequipped_

_Tripmine Equipped_

### Starter tool

Storing a tool in `Class.StarterPack` will place it in a player's `Class.Backpack` when they join or respawn.

1. Move the **Blaster** to **StarterPack** in the **Explorer**.
2. Play the game to test the tool. Click on the hotbar at the bottom of the screen or press **1** on the keyboard to equip the tool.

## Tool properties

### Position / orientation

A tool's position and orientation can be changed using the **grip** properties. **GripPos** changes the position of the grip, whereas **GripForward**, **GripRight** and **GripUp** affect the rotation.

Currently the player is holding the center of the blaster instead of the grip.

1. Set the **GripPos** property of the tool to **0, -0.4, 1.1**.
2. [Initiate a playtest](/docs/en-us/studio/testing-modes.md#playtesting) to test the tool. Notice how the tool is now being gripped in a different position._Before__After_

### Hotbar icon

By default, the tool **name** will be displayed on the hotbar icon. It's good practice to change the icon to be an image of the tool. Set the **TextureId** property of the tool to `rbxassetid://92628145`.

_Before_

_After_

### Tooltip

A **tooltip** is a small text description that appears when the mouse hovers over a tool in the hotbar. They typically include the name of the tool and/or a brief description of its function. Change the **ToolTip** property to **Blaster**.

## Use scripts with tools

A tool has three key events you can connect to: `Class.Tool.Equipped|Equipped`, `Class.Tool.Unequipped|Unequipped` and `Class.Tool.Activated|Activated`.

| Event | Description |
| --- | --- |
| **`Class.Tool.Equipped\|Equipped`** | Fired when a tool is equipped by the player, for example when a tool is selected in the hotbar. |
| **`Class.Tool.Unequipped\|Unequipped`** | Fired when a tool is unequipped by the player, for example when a tool is deselected in the hotbar. |
| **`Class.Tool.Activated\|Activated`** | Fired when a tool is activated by the player, for example when a player left-clicks. |

These methods only work in `Class.LocalScript|LocalScripts` because only the player's device knows when input happens, such as a mouse button being clicked or a screen being touched.

## Add the sounds

To see these events in action, you can play a sound when they fire. First, you'll need to create Sound objects to use for this.

1. Insert two `Class.Sound` objects into the **Handle**.
2. Rename one sound **Equip** and set its SoundId property to `rbxassetid://282906960`.
3. Rename the other sound **Activate** and set its SoundId property to `rbxassetid://130113322`.

## Add the code

The example code below plays the **Equip** sound when the tool is equipped and the **Fire** sound when activated.

1. Insert a **LocalScript** into the tool and name it **ToolController**.
2. Insert the following lines of code into the script.```lua
local tool = script.Parent

local function toolEquipped()
	tool.Handle.Equip:Play()
end

local function toolActivated()
	tool.Handle.Activate:Play()
end

tool.Equipped:Connect(toolEquipped)
tool.Activated:Connect(toolActivated)
```
3. Test the blaster sound effects by equipping and clicking to activate the tool.

Now you know how to create and script a basic tool, try creating other simple tools such as a flashlight or speaker.
