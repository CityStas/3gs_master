---
title: "Make mesh watertight"
url: /docs/en-us/art/accessories/creating/watertight
last_updated: 2026-10-30T19:55:32Z
description: "Seal off your geometry to ensure that there are no angles where the interior backfaces of your object are exposed."
---

# Make mesh watertight

With the t-shirt shape finalized, make your mesh **watertight** by "sealing" the holes at the neck, waist, and wrist. A watertight shape ensures that only the top visible surface of the mesh is exposed at any angle. If an asset is not watertight, it may expose backfaces (single-sided faces) that could affect the rendering of your asset and performance when equipped to a character.

_Watertight top view_

_Watertight bottom view_

To make your t-shirt watertight:

1. With **LongSleeve** active, switch to **Edit** mode.
2. Starting with any hole in the mesh, hold `Alt` and click the **last edge** on the mesh. The entire edge highlights.
3. Press `E` to extrude the mesh, then click after a small extrusion is added.
4. With the new edge still selected, right-click and select **Merge Vertices** > **At Center** from the contextual menu.
5. Press `G` to grab the new vertex and reposition it within your t-shirt mesh.
6. Repeat until all the interior-exposing holes of your mesh are closed.

> **Success:** You've completed the modeling section of this tutorial. If desired, download a [reference project](../../../assets/art/reference-files/checkpoint/1_LongSleeve-Modeling-Complete.blend) of this stage and compare it against your work.
>
> There are a lot of techniques to create clothing. Try experimenting with the following techniques, tools, and processes to create additional unique assets: - Making asymmetrical clothing. - Blender's [cloth simulation](https://docs.blender.org/manual/en/latest/physics/cloth/examples.html#using-simulation-to-shape-sculpt-a-mesh) and other sculpting tools. - Various community sewing and fabric techniques for creating clothing on Blender.
