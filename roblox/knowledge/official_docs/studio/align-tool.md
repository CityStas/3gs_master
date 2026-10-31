---
title: "Align tool"
url: /docs/en-us/studio/align-tool
last_updated: 2026-10-30T19:55:57Z
description: "The Align tool lets you align objects or groups of objects along the X, Y, or Z axes."
---

# Align tool

The **Align** tool, accessible from Studio's **Model** tab toolbar or the **Window** ⟩ **3D** menu, lets you align objects or groups of objects along the **X**, **Y**, or **Z** axes.

![Align tool highlighted in Studio's toolbar.](../assets/studio/general/Toolbar-Align.png)

Primary benefits include:

- Aligning the center or edge of multiple objects in one action.
- Aligning entire `Class.Model|Models` or parts within them relative to other parts, all while keeping the model intact.
- Dynamically previewing the point of alignment before confirming.

## Mode

You can set the alignment mode to either **Min**, **Center**, or **Max**.

![The Min icon in the toolbar.](../assets/studio/align-tool/Icon-Min.png)

_Min_

![The Center icon in the toolbar.](../assets/studio/align-tool/Icon-Center.png)

_Center_

![The Max icon in the toolbar.](../assets/studio/align-tool/Icon-Max.png)

_Max_

#### Min

![An angled side view of a small red cube, large blue cube, and a small purple cube that are aligned with the Min button on the world Z axis. A translucent orange rectangle represents where the objects align in context to each other.](../assets/studio/align-tool/Mode-Min.jpg)

#### Center

![An angled side view of a small red cube, large blue cube, and a small purple cube that are aligned with the Center button on the world Z axis. A translucent orange rectangle represents where the objects align in context to each other.](../assets/studio/align-tool/Mode-Center.jpg)

#### Max

![An angled side view of a small red cube, large blue cube, and a small purple cube that are aligned with the Max button on the world Z axis. A translucent orange rectangle represents where the objects align in context to each other.](../assets/studio/align-tool/Mode-Max.jpg)

## Align In

The **World** or **Local** option specifies which relative coordinates to align on. This is especially useful for aligning parts which don't share the same orientation or rotation.

The **X**, **Y**, and **Z** checkboxes let you select which axes to align on. Note that you can select multiple axes in a single alignment operation.

#### Before Alignment

![An angled side view of a small red cube, large blue cube, and a small purple cube that are unaligned.](../assets/studio/align-tool/Align-In-Before.jpg)

#### Max / World Z

![An angled side view of a small red cube, large blue cube, and a small purple cube that are aligned with the Max button on the world Z axis. A translucent orange rectangle represents where the objects align in context to each other.](../assets/studio/align-tool/Align-In-World-Z.jpg)

#### Max / Local Z

![An angled side view of a small red cube, large blue cube, and a small purple cube that are aligned with the Max button on their local Z axis. A translucent orange rectangle represents where the objects align in context to each other.](../assets/studio/align-tool/Align-In-Local-Z.jpg)

## Relative To

An alignment operation can be relative to either the **Selection Bounds** or the **Active Object**.

### Selection Bounds

**Selection Bounds** aligns the selected objects relative to the bounding box around them.

#### Before Alignment

![An angled side view of a small red cube, large blue cube, and a small purple cube that are unaligned. A translucent red rectangle represents where the objects' collective bounding box.](../assets/studio/align-tool/Relative-To-Selection-Bounds-Before.jpg)

#### Min / World X

![An angled side view of a small red cube, large blue cube, and a small purple cube that are aligned with the Min button on the world X axis relative to their collective bounding box. A translucent red rectangle represents where the objects' collective bounding box.](../assets/studio/align-tool/Relative-To-Selection-Bounds-Min-X.jpg)

#### Max / World X

![An angled side view of a small red cube, large blue cube, and a small purple cube that are aligned with the Max button on the world X axis relative to their collective bounding box. A translucent red rectangle represents where the objects' collective bounding box.](../assets/studio/align-tool/Relative-To-Selection-Bounds-Max-X.jpg)

### Active Object

**Active Object** aligns the objects relative to the **last selected object**. This object is outlined in orange and it will not move during the operation. While parts are selected, you can switch the active object by clicking on a different object.

#### Before Alignment

![An angled side view of a small red cube, large blue cube, and a small purple cube that are unaligned. The large blue cube has a yellow outline to represent that it's the active object.](../assets/studio/align-tool/Relative-To-Active-Object-Before.jpg)

#### Min / World X

![An angled side view of a small red cube, large blue cube, and a small purple cube that are aligned with the Min button on the world X axis relative to the active object. The large blue cube has a yellow outline to represent that it's the active object.](../assets/studio/align-tool/Relative-To-Active-Object-Min-X.jpg)

#### Max / World X

![An angled side view of a small red cube, large blue cube, and a small purple cube that are aligned with the Max button on the world X axis relative to the active object. The large blue cube has a yellow outline to represent that it's the active object.](../assets/studio/align-tool/Relative-To-Active-Object-Max-X.jpg)
