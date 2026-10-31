---
title: "Work with parts"
url: /docs/en-us/tutorials/curriculums/building/work-with-parts
last_updated: 2026-10-30T19:55:58Z
description: "Explains how to insert and customize parts for your obby."
---

# Work with parts

**Parts** are basic 3D shapes that Roblox provides out-of-the-box for building in the 3D space. In this chapter, let's explore how to insert parts of all shapes and sizes, change their position and rotation for your obby, then anchor them in the air so that they don't fall due to Studio's gravity.

## Insert parts

There are five different part shapes that you can insert from the toolbar to build environments in your games: **block**, **sphere**, **cylinder**, **wedge**, and **corner wedge**. While you can join these part shapes together in unique ways to form more complex shapes, this lesson focuses on keeping the shapes as-is for your obby's platforms.

![A single Block part.](../../../assets/modeling/parts/Basic-Part-Block.png)_ Block_

![A single Sphere part.](../../../assets/modeling/parts/Basic-Part-Sphere.png)_ Sphere_

![A single Cylinder part.](../../../assets/modeling/parts/Basic-Part-Cylinder.png)_ Cylinder_

![A single Wedge part.](../../../assets/modeling/parts/Basic-Part-Wedge.png)_ Wedge_

![A single Corner Wedge part.](../../../assets/modeling/parts/Basic-Part-Corner-Wedge.png)_ Corner Wedge_

To insert a part for your first platform:

1. **OPTIONAL** When you insert parts, they appear at the exact center of your camera view. Select the **START** platform, then press `F` to focus the camera on this part so your additional platforms insert near the start of the obby.
  > **Info:** If you want more control over where the part inserts into the 3D space, use your mouse to zoom in and center your view where you want to insert your part.
2. In the **Home** or **Model** tab's toolbar, click the small arrow next to the **Part** inserter tool to reveal the dropdown.![A close-up view of the part picker.](../../../assets/tutorials/building-lesson/part-picker.png)
3. From the dropdown menu, select the part shape you want for your first platform. The part displays at the exact center of your camera view.
4. Using this process, insert additional shape types until you have as many platforms as you want for your obby.

## Customize course

Now that you have platforms for your obby, it's time to customize their position, size, and rotation to create a jumping puzzle for the start of your obby. To do this, you will use three different object tools:

- **Move** — Changes your object's **position**.
- **Scale** — Changes your object's **size**.
- **Rotate** — Changes your object's **orientation**.

Each of these tools includes visual handles you can use to move, scale, or rotate your object using Studio's coordinate system for the 3D space. When you click and drag one of the handles, the object moves, scales, or rotates, respectively.

![Move draggers shown on part in 3D viewport.](../../../assets/modeling/parts/Transform-Move-SM.png)_Move tool handles_

![Scale draggers shown on part in 3D viewport.](../../../assets/modeling/parts/Transform-Scale-SM.png)_Scale tool handles_

![Rotate draggers shown on part in 3D viewport.](../../../assets/modeling/parts/Transform-Rotate-SM.png)_Rotate tool handles_

To customize your course for your obby's starting jumping puzzle:

1. Change the **position** of your first platform.
  1. In the viewport, click on the part shape that you want for your first platform.
  2. In the toolbar, select the **Move** tool. A set of handles display around the part.![Move tool highlighted.](../../../assets/education/general/Move-Tool.png)
  3. Click and drag one of the handles until your part is at a good jump distance away from where players join the game.
    > **Info:** Keep in mind that the jump distance between platforms is important. If you make it too difficult from the start, players may quit instead of continuing to play.
2. Change the **size** of your first platform.
  1. In the toolbar, select the **Scale** tool. A set of handles display around the part.![Scale tool highlighted.](../../../assets/education/general/Scale-Tool.png)
  2. Click and drag one of the handles until your part is a different size.
3. Change the **orientation** of your first platform.
  1. In the toolbar, select the **Rotate** tool. A set of handles display around the part.![Rotate tool highlighted.](../../../assets/education/general/Rotate-Tool.png)
  2. Click and drag one of the handles until your part has a different rotation.
4. Using the following camera controls, check your part's position and orientation from multiple angles to make sure that players would be able to jump to the first platform. | **Action** | **Control** |
| --- | --- | | **Move** | `W` `A` `S` `D` | | **Rotate** | Hold the right mouse button to rotate around the selected object. | | **Zoom** | Use your mouse's scroll wheel. | | **Focus** | Press `F` to focus on a the selected object. |
  > **Info:** If the camera doesn't move, click anywhere in the viewport, then try again.
5. Repeat this process for the rest of your platforms.

## Anchor platforms

If you were to playtest your game now, all of your new platforms would immediately fall and disappear. This is because the Roblox engine simulates gravity as soon as the game runs, allowing the physical force to push objects down.

To make sure your platforms stay at their set position and orientation when the game runs, you must anchor them within the 3D space using the **Anchor** tool. In addition to preventing gravity from pushing the platforms down, anchoring your platforms ensures they will stay in place when players and other objects bump into them.

To anchor your platforms:

1. While holding the `Shift` key, select all of your new parts.
2. In the **Home** or **Model** tab, toggle on **Anchor**.![Anchor tool highlighted.](../../../assets/education/general/Anchor-Tool.png)

Now that you have all of the platforms in place for your obby's jumping puzzle, it's time to add code with AI Assistant to modify part behavior.
