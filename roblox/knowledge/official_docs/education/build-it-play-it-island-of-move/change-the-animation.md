---
title: "Change the animation"
url: /docs/en-us/education/build-it-play-it-island-of-move/change-the-animation
last_updated: 2026-10-30T19:55:41Z
description: "Part of the Roblox Build It, Play It Challenge - Island of Move. Swap the default walk animation with your own."
---

# Change the animation

The template has a pre-built setting for what animation to use when players run. To change the animation, you'll need to replace the default animation with yours.

## Change the animation ID

Now that you have the animation ID, you can enter it in your game. Then, Studio will know what animation to play.

1. Make sure the **Explorer** and **Properties** windows are open.
  > **Warning:** If you don't see the windows on the right, open them from Studio's **Window** menu.
2. To find the walk setting,
  1. Go to the **Explorer** window, then in the **search bar**, type "walk".
  2. Click on **WalkAnimationID**.
3. In the **Properties** window, click the **Value** field and paste the animation ID by pressing `Ctrl``V` or `⌘``V`.
  > **Warning:****Need to Get the Animation ID?** If nothing was pasted, or another line of text was used, you'll need to get the animation ID again.  1. Go to the [Creator Dashboard](https://create.roblox.com/dashboard/creations).  2. In the horizontal navigation, select **Development Items**, then click the **Animations** button. All animations you have ever published display here.  3. Select your animation. The animation's **Configure** page displays.  4. In the left-hand navigation, click the vertical three dots icon, then select **Copy Asset ID** from the contextual menu.

## Test and check

After swapping the animation, play the game to see your creation.

1. Press the **Play** Button.
2. Use the `WASD` keys to walk around and see the animation play.
  > **Warning:** If you make updates to the animation, remember to **Save** it in the **Animation Editor**.

## Troubleshooting tips

**Issue:** Animation is spotty, skips, or looks glitchy.

- Make sure that the first and last poses are the same. Right-click on the diamond for the first pose and copy it. Then, paste that pose at the end of the timeline.
- Check that the figure stays inside the white grid when selected. If not, it may go through walls or the ground.

**Issue:** Animation isn't the one that you were working on.

- Check that you've published the animation through the Animation Editor.
- Find in the Explorer an object named WalkAnimationID. Make sure its Value is only a number.
