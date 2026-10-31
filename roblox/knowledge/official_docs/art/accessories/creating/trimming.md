---
title: "Trim clothing shape"
url: /docs/en-us/art/accessories/creating/trimming
last_updated: 2026-10-30T19:55:32Z
description: "Create the general shape of your clothing item by removing unnecessary sections of your duplicated mesh."
---

# Trim clothing shape

With a clean mesh object to work with, cut the basic shape of the type of clothing item you intend to create and prepare the mesh for additional sculpting detail. In this tutorial, you create a long-sleeve shirt shape by removing the leg, arm, and head sections, smoothing out the mesh to create a flat canvas, and repositioning the mesh onto your temporary mannequin.

_Long-sleeve trimming of the full-body mesh._

## Trim clothing shape

Create the general shape of your t-shirt by trimming sections of your duplicated mannequin mesh.

To trim your clothing shape:

1. Select **LongSleeve**, then switch to **Edit** mode.
2. In the top right corner of the viewport, enable **Wireframe** mode.
3. Click and drag over parts of the mesh that you do not want to include in your shirt, then press `X` and select **Vertices** from the contextual menu to delete these sections of your mesh.
4. Repeat until you reach your desired clothing shape.

## Add and smooth vertices

With the basic shape created, subdivide the surface of your t-shirt to add vertices and smooth out the mesh. This process removes the grid-like surface and allows you to apply more complex sculpting detail later.

_Before applying Subdivision modifier and Shade Smooth_

_After applying Subdivision modifier and Shade Smooth_

To add and smooth your vertices:

1. Switch to **Object** mode.
2. With **LongSleeve** active, navigate to the **Modifier Properties** tab in the Properties Editor.
3. Select **Add Modifier** > **Subdivision Surface**, then click the **Apply** button with the default settings.
4. In the viewport, right-click the object and select **Shade Smooth** from the contextual menu to eliminate the creases on your t-shirt.

## Scale and position

With your base clothing shape created, the next steps are to scale out the t-shirt and reposition it on top of the mannequin.

_Clothing mesh should fit over mannequin after applying a reposition and scale_

To set up and scale your clothing to your mannequin:

1. Switch to **Object** mode, then unhide one of your cage meshes.
2. Using the filter dropdown, enable the **Selectable** toggle, then set your body mesh to unselectable to prevent accidental edits to your mannequin.
3. With **LongSleeve** active, lightly scale and position your asset to rest over the mannequin.
  1. Press `S` and use your mouse to scale. In most cases, the scaling should be a small change.
  2. Press `G` and click to grab your shirt. Make sure the shirt rests loosely over the mannequin; it does not need to fit perfectly at this point.
