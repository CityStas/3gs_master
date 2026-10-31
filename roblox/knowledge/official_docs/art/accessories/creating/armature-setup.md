---
title: "Armature setup"
url: /docs/en-us/art/accessories/creating/armature-setup
last_updated: 2026-10-30T19:55:32Z
description: "Transfer and parent an armature template to your custom clothing Blender project."
---

# Armature setup

**Rigging** is the process that enables the clothing object to move and deform with a Roblox character's rigging armature. In this tutorial, you'll parent the t-shirt to Roblox's provided [standard R15 rig](/docs/en-us/avatar/character-bodies/specifications.md#standard-r15-rigs) and verify the Automatic Skinning Transfer data. After rigging, be sure to test out some basic poses to ensure that your clothes move and stretch correctly with any character body.

_Clothing mesh with no rigging data_

_Clothing mesh with rigging data performing pose tests_

The next two rigging sections cover the following processes:

1. Downloading and appending a standard R15 armature to your project.
2. Parenting the rig with Blender's automatic weights.
3. Testing poses.

## Transfer armature

Roblox provides base rigging armatures that you can import into your own project. While it is possible to create your own rigs, importing a premade rig with the proper configuration saves you time and reduces the potential for error.

To import a standard R15 rig into your file:

1. Download Roblox's [Rig_and_Attachments_Template.blend](../../../assets/modeling/meshes/reference-files/Rig_and_Attachments_Templates.zip), but do not open this project.
2. In your current clothing project, return to **Object** mode.
3. Navigate to **File** > **Append**, and select the saved **Rig_And_Attachments_Template.blend** file. An additional folder structure appears.
4. Select **Armature** > **Armature** and press **Append**. An armature object is added to your workspace.
5. Reorient the armature:
  1. With the armature active, open the **Item tool** sidebar.
  2. Adjust the rotation so the armature is correctly aligned with your mesh.
  3. After alignment, navigate to **Object** > **Apply** > **All Transforms** to freeze your new rotation values.

## Parent armature

With the armature rig in place, you can use Blender's **Parent with Automatic Weights** functionality to quickly set your t-shirt mesh as a child of the armature. This feature also applies vertex weighting, or **skinning**, automatically to your mesh, which can save you significant time over skinning your clothing manually.

To parent the t-shirt to the rig:

1. Select **LongSleeve**, then hold `Shift` and click the **Armature** object. Ensure that the armature object is the last object selected.
2. Right-click in the viewport, then select **Parent** > **With Automatic Weights** from the contextual menu.
