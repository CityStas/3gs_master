---
title: "Create a sparkler"
url: /docs/en-us/education/build-it-play-it-mansion-of-wonder/creating-a-sparkler
last_updated: 2026-10-30T19:55:41Z
description: "Learn how to attach a particle emitter to a player-carried tool in Roblox Studio. Once you are finished, Earn the fourth set of rewards in Roblox's Build It Play It Mansion of Wonders -- the Head Slime avatar item and Glimmer and Gumption badge."
---

# Create a sparkler

You've learned the basics of particles, now apply those skills to design a sparkler that can be carried around by people. Just like blasts, the particles can be customized for different effects, like magical stars or raging flames.

In addition to the properties covered in the Build It, Play It challenge, this tutorial will use color gradients which allows particles to change colors over time, like from blue to yellow as seen in the video. The sparklers can be used with the Mansion of Wonder template or any other game you've created.

## Find a tool

For this tutorial, sparklers are **tools** with attached particle effects. In Roblox, tools are items players equip; if you've played a game with a sword or gun, it's likely you've used tools before.

To start, add the pre-made sparkler set into your existing game. You'll then choose one and customize its particle emitter.

1. Start by pressing the **Add to Inventory** button in the following component. This adds the set into your Inventory, which is accessed in the Toolbox. #### Sparkler Set Click the button to get a set of sparklers for the tutorial.
2. In Studio, find the **Toolbox**. If it's not visible, open it from the **Window** menu.
3. Select the **Inventory** tab.
4. Make sure the left dropdown is set to **My Models**, then find and click on **Sparkler Set**. This will add the parts into your game.

## Create the particle

Each sparkler comes with a customizable particle emitter. Follow the steps to find the particle, change its texture, and then create the color gradient.

1. Select one of the pre-made tools. In the **Explorer** window, find the highlighted part. Then, click the **>** arrows to expand until you find **Attachment** and select **SparklerParticle**.
2. Change the **Texture** property. Some texture ID's are included below._5860841663__5857851812__5857851618__6711256324__5833235272__6772783963__5833323391__5857892330__5857892405__5857931724__5857851618__5860841737_ When finished, a tool may look like the example below.
3. Find the **Color** property and click anywhere in the row next to its name. Then, press the **...** to open the Color Sequence editor. You'll learn how to edit the color in the next section.

## Create a color gradient

Each **arrow** on the color sequence represents a different color. Colors can be changed, added, removed, or moved around. Use a combination of techniques to create a color gradient, like the example below.

### Change a color

Under the color sequence, select an **arrow**. Then, click the **Color** button to open the color picker and set a new color. Note that arrows are yellow when selected.

### Add or remove colors

To add a color, click on the color sequence. This adds a new arrow that can be clicked. To remove a color, click on an arrow and click the **Delete** button on the screen.

### Move colors

To move a color, click on any arrow other than the start or end arrows and drag it to a new area.

### Improve the particle

After creating a color gradient, use your knowledge from the previous lessons to change properties like **Size** and **Speed** to get the particular effect you want.

## Finish the sparkler

So players can have the sparkler when the game starts, you'll need to move it to the StarterPack. This folder holds all items a player receives when they join.

1. In the **Explorer** window, find the **tool** of your choice, such as the **Staff Sparkler** or **Torch Sparkler**. Right-click on that tool and select **Cut**. This copies the staff to your clipboard, but also deletes it from the folder.
2. Scroll down in the **Explorer** window until you find the **StarterPack**. Right-click on it and select **Paste Into** to add the tool.
3. Playtest project, and select the sparkler from your backpack by pressing `1` on your keyboard. Note that you can repeat this process to make more sparklers.
  > **Info:** Each sparkler has a name that's shown to players in the game. To rename a sparkler, in the **Explorer** window, right click on the tool and select **Rename**.

## Challenge checkpoint

You got your animation ready! Celebrate your new skills by getting the **Head Slime** avatar item and **Glimmer and Gumption** badge.

1. **Copy** the following code: `Glimmer`
2. Click the **Enter World** button below to open the **Mansion of Wonder** game.
3. When you are playing game, interact with Freddie the fox character, then click **REDEEM CODE**. Use the code from step 1 to get your item.
