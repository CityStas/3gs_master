---
title: "Play your animation"
url: /docs/en-us/tutorials/curriculums/animator/play-your-animation
last_updated: 2026-10-30T19:55:57Z
description: "Explains how to export and replace a default character animation with your custom animation."
---

# Play your animation

In order to play your animation in your open game, as well as store it for reuse in other projects, you must publish the animation to the cloud. This process creates a unique animationID for your animation that you can reference in scripts, which is especially important if you want to replace any of Roblox's default character animations.

In this chapter, let's go over how to export your animation by publishing it to Roblox, then swap out the template's default walk animation with your own creation.

## Export new animation

If you were to close Studio right now, you would lose all of your work on your animation because your animation doesn't have an **animationID** that Studio can reference for your projects. To fix this, you must export your animation to Roblox so that Studio can connect the animation to your account.

To export your new animation:

1. In the **Animation Editor**, click on the **⋯** and select **Publish to Roblox**. The **Asset Configuration** window displays.
2. In the **Asset Configuration** window, give your animation a name and description, then click the **Save** button. After a few moments, the window confirms your animation was successfully submitted.
3. Copy your animation's animationID by clicking the icon next to the ID. A green "_ID Copied!_" text pop-up displays when you have done this step correctly.
4. Click the **Close** button.

## Replace default animation

Every player character includes a set of **default animations** that play whenever the character performs specific in-game actions, such as running, climbing, or jumping. Roblox provides these animations out-of-the-box for every game without any additional coding effort.

_Default Fall Animation_

_Default Swim Animation_

_Default Climb Animation_

You can swap out default animations with your own custom animations so that they play for every player that joins your game. For this lesson, let's swap out the default walking animation with your swim animation so that you can see how it looks with your avatar as soon as you start playing.

To replace the default walking animation with your custom swimming animation:

1. Find the default walk animation.
  1. In the **Explorer** window, go to the search bar, then type **walk**.
  2. In your search results, click on **WalkAnimationID**.
  > **Warning:** If you don't see the **Explorer** and **Properties** windows, open them from Studio's **Window** menu.
2. In the **Properties** window, click the **Value** field and paste your animation ID by pressing `Ctrl``V` or `⌘``V`, depending on your computer.
  > **Info:****Need to Get the Animation ID?** If your animationID didn't paste into the Value field, you need to get your animation's animationID again. To do this:  1. Go to the [Creator Dashboard](https://create.roblox.com/dashboard/creations).  2. In the horizontal navigation, select **Development Items**, then click the **Animations** button. All animations you have ever published display here.  3. Select your animation. The animation's **Configure** page displays.  4. In the left-hand navigation, click the vertical three dots icon, then select **Copy Asset ID** from the contextual menu.
