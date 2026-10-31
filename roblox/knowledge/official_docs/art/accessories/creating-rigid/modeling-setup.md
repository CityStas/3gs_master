---
title: "Box modeling"
url: /docs/en-us/art/accessories/creating-rigid/modeling-setup
last_updated: 2026-10-30T19:55:32Z
description: "Create your basic rigid accessory model in Blender."
---

# Box modeling

![A screenshot of blender showing the final 3d shape of a treasure chest in the viewport](../../../assets/art/accessories/creating-rigid/Modeling-Complete.png)

**Modeling** is the process of creating and shaping the 3D geometry of an object. **Box modeling** is a fundamental technique in 3D modeling combining basic shapes and steps to create a more complex object.

The following instructions are based off of the [Box Modeling 101 staff article](https://devforum.roblox.com/t/modeling-101-in-blender-box-modeling/2963814). The original article includes additional information, as well as Blender setup instructions, best practices, and advanced modeling examples that are not included in this accessory tutorial.

> **Warning:** Whether you are using an existing shape or creating your own 3D object, it's important to consider [technical requirements](/docs/en-us/avatar/rigid-accessories/specifications.md), such as keeping your geometry within a polycount budget, and [policy requirements](/docs/en-us/marketplace/marketplace-policy.md), such as ensuring your design does not infringe on other creator's IP both within and outside of the Roblox ecosystem.
## General shape

In a new Blender file, delete everything except the starter cube, then create the basic shape of the treasure chest.

1. In a new project, select all non-cube objects and press `X` to delete.
2. Convert the cube into a rectangle.
  1. Select the cube and press `S` for scale.
  2. Press `Y` to lock scaling to the Y axis.
  3. Drag with the mouse to create a rectangle.
3. Create the top of the treasure chest.
  1. Switch to **Edit** mode, then press `3` to switch to face selection.
  2. Select the top face of the box and press `E` to activate the **Extrude** tool.
  3. Drag your mouse to extrude the lid. Extend the lid to about half the height of the main body.

## Rounded lid

Create the rounded lid shape using segmentation:

1. Press `2` to switch to edge selection.
2. Holding `Shift`, click the top front and back edges of your chest.
3. With both edges selected, press `Ctrl``B`/`⌘``B` to activate the **Bevel** tool.
4. Navigate to the contextual menu at the bottom right, then set the number of segments to `6` and enable **Clamp Overlap**.

### Merge vertices

Sometimes tools like the **Bevel** tool may move vertices very close to each other without merging them. Use the **Merge Vertices** function to ensure that your object shares vertices wherever possible.

1. Press `1` to switch to vertex selection, then press `A` to select all vertices of your object.
2. Right-click anywhere in the viewport, then select **Merge Vertices by Distance** from the contextual menu.
3. In the pop-up modal, set the distance to `.01`.

## Side insets

Create the left and right insets of your chest:

1. Press `3` to switch to face selection.
2. Holding `Shift`, click both sides of your shape. This selects both the left and right faces.
3. Press `I` to activate the **Inset** tool. Drag the mouse to adjust the amount of inset for the new face to about the size of your bevel segments.
4. With your new insets selected, right-click anywhere in the viewport, then select **Extrude Along Normals** from the contextual menu.
5. Use the mouse to drag and adjust the distance of extrusion into the chest.

## Front insets

Create the front and back insets of your chest by creating new lines and then extruding your faces between those lines.

### Vertical loop cuts

To create your vertical loop cuts:

1. Press `2` to switch to edge selection, then press `A` to select the entire chest.
2. Use `Ctrl``R`/`⌘``R` to create a loop cut.
3. Using your mouse, hover over the object until the highlighted cut is vertical, then click to confirm.
4. In the contextual menu, set the number of cuts to `2`.
5. With the new lines selected, press `S` to scale and `Y` to scale within the Y axis.
6. Use the mouse to drag the lines until they nearly reach the edges of your chest, then click to confirm.

### Horizontal loop cuts

To create your horizontal loop cuts:

1. Select the chest, and press `Ctrl``R`/`⌘``R` to loop cut, then click to confirm a horizontal cut.
2. In the contextual menu, set the number of cuts to `2`.
3. To straighten each line across your object:
  1. Click one of your new lines.
  2. Press `S` for scale.
  3. Press `Z` to scale within the Z axis.
  4. Press `0` to set the scale value to `0` across the Z axis.
  5. Repeat for the other line.
4. Position the top line near the top below the segmentations.
5. Position the bottom line near the bottom.
6. Enable **Magnet Snapping** so the bottom line merges with the existing vertices and lines from the side insets.

### Extrusions

Create the extrusions for the front, top, and back of the chest.

1. Press `3` to switch to face selection.
2. Hold `Alt`/`⌥` and click on your front faces to select the front, top, and back faces.
3. With the faces selected, hold `Shift` and click on the metal borders to deselect them. The front and back faces, and the top segmentations, should remain selected.
4. Right-click anywhere in the viewport, then select **Extrude Faces Along Normals** from the contextual menu.
5. Drag the mouse to extrude the faces about the same width as the metal borders.

## Complete border

The chest is almost ready, but is still missing the continuous metal border across the top edge. Remove the existing faces and add new geometry to the treasure chest.

### Delete faces

Delete the faces of the top side metal borders:

1. Starting on any side, hold `Shift` and click the three faces of the top metal border.
2. Press `X` to delete.
3. Repeat this process for the other side.

### Add faces

Add new faces to the sides that complete the geometry of the treasure chest box.

1. Press `2` to switch to edge selection.
2. Starting with any side, hold `Shift` and click the two top corner edges of the missing face.
3. Right-click anywhere in the viewport, then select **New Face from Edges** from the contextual menu to create a top face.
4. Repeat steps 2-3 with the bottom corner edges to create a bottom face.
5. On the other side of the chest, repeat steps 2-4 to complete the metal border.

> **Success:** You've completed the modeling section of this tutorial. If desired, download a [reference version](../../../assets/art/accessories/creating-rigid/Chest-Modeling-Complete.blend) of this stage of the project for comparison.
>
> This tutorial represents an extremely basic overview of the 3D modeling process. Tools like Blender offer many features, workflows, and techniques to create unique and complex models. Check out Blender's official and community tutorials for additional instructional content.
