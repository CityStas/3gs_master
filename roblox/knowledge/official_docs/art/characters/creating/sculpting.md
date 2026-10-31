---
title: "Sculpt the head"
url: /docs/en-us/art/characters/creating/sculpting
last_updated: 2026-10-30T19:55:33Z
description: "Use Blender's sculpting tools to make unique changes to the shape of your character."
---

# Sculpt the head

After reviewing the modeling best practices and sculpting tips, you can begin sculpting your avatar character body. This tutorial demonstrates sculpting changes to the [RoundMale template](../../../assets/art/reference-files/RoundMale.zip), creating a goblin-like character.

The sculpting instructions utilize the following Sculpting tools:

- **Grab** - Selects and pulls a group of vertices.
- **Smooth** - Eliminates irregularities in the area of the brush's influence.
- **Flatten** - Averages out the vertices within the brush's influence on a common plane.
- **Elastic Deform** - Similar to Grab, but adds an organic stretch and elasticity to the neighboring vertices.

> **Info:** You can use Blender's other sculpting tools, though it's important to use a tool that aligns with the [Non-Destructive Modeling](/docs/en-us/art/characters/creating/modeling-best-practices.md#non-destructive-modeling) concepts to preserve the vertices of the model.

To begin sculpting the head:

1. With the template project opened, hide the other Geo objects to isolate the head mesh.
2. Select the `Head_Geo` mesh object and switch to **Sculpting** mode.
3. At the top right of the viewport:
  1. Enable **X-Axis symmetry**.
  2. Enable **Wireframe** mode.
4. Using the **Mask** tool, paint over the mouth and eyes where you do not want to sculpt unexpectedly.
5. With the **Grab** and **Smooth** tools, make the following edits to your template head:
  1. Reshape the head, flattening and enlarging the top.
  2. Elongate the ears.
    1. Expand the surface near the ear to broaden the base
    2. Grab and extend each ear, ensuring it connects smoothly to the base and vertices remain proportionally spaced when possible.
    3. Try the **Flatten** tool to straighten and align a region.
    4. Try the **Elastic Deform** tool to stretch and pull multiple vertices.
  3. Extend the bridge of the nose and expand the size of the brow.
  4. Broaden the chin so it prominently protrudes.
6. Perform a refinement pass to add final details, polish, and accentuate your main features, such as:
  - Adding details in the outer and inner ears
  - Adding more detail to chin and cheeks
  - Improving edge lines and spacing in areas with crowded vertices

> **Success:** For a comparison reference, you can download [this version of the tutorial project with sculpting completed](../../../assets/art/reference-files/checkpoint/1_Goblin-sculpted.blend).
