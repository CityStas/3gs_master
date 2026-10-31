---
title: "Blender validation tool"
url: /docs/en-us/art/characters/validation-tool
last_updated: 2026-10-30T19:55:35Z
description: "The Avatar Validation Tool checks for common character model issues in Blender."
---

# Blender validation tool

> **Warning:** This tool is no longer in active development. You are free to use the tool for any purpose. The tool may be out of date or incompatible with modern Roblox assets.

The **Avatar Validation Tool** is a supplemental Blender add-on you can use to quickly identify common issues with your character model. This tool checks that your model meets most of Roblox's avatar [technical specifications](/docs/en-us/avatar/character-bodies/specifications.md) and, when possible, attempts to automatically resolve them.

This tool can save you time by checking for common validation specifications before you export your model, but it doesn't provide a comprehensive verification of all aspects of your character model. You should always continually test your character model, including testing your characters [in Studio](/docs/en-us/avatar/character-bodies/test-studio.md) and verifying on your own if your model meets Roblox's [character body specifications](/docs/en-us/avatar/character-bodies/specifications.md).

## Install

> **Warning:** The Validation Tool plugin is compatible with Blender 3.5.1+. You may experience unexpected behavior if using earlier versions of Blender.

To install the Validation Tool in Blender:

1. Download [ValidationTool_Blender.zip](https://github.com/Roblox/avatar/tree/main/Tools/ClothingValidationTool) and save the .zip file locally. Do not open the .zip file.
2. In Blender, navigate to **Edit** > **Preferences**.
3. In Preferences, go to the **Add-Ons** section on the left sidebar.
4. Click the **Install...** button. A file browser displays.
5. Select the downloaded .zip file and click **Install Add-On**.
6. In the Add-Ons section, find the Validation Tool and **enable** the add-on.
7. Return to your workspace and expand the side toolbar in the Viewport to access the add-on.

_Sidebar indicator_

_Expanded sidebar_

## Validate

After installing the plugin, you can begin validating your character models. When validating, results with issues display as red. In some cases, you can apply an automatic fix to checks that have issues. See [Checks and Troubleshooting Steps](#checks-and-troubleshooting) for details on each validation check.

To use the validation tool on your asset:

1. In the Target Armature field, select the **eyedropper**.
2. With the eyedropper active, select your character's **armature object**. This object is often named Joints or Armature.
3. Select **Run All Checks** to go through each individual check. Alternatively, you can click individual buttons to run a specific check.
4. Checks that detect issues display as red and an error output displays at the bottom of the tool.

> **Info:** This validation tool only checks for common validation issues. You should always continually test your character model, including testing your characters [in Studio](/docs/en-us/avatar/character-bodies/test-studio.md) and verifying on your own if your model meets Roblox's [character body specifications](/docs/en-us/avatar/character-bodies/specifications.md).
## Checks and troubleshooting

Each button on the validation tool performs a different check against the expected [character specifications](/docs/en-us/avatar/character-bodies/specifications.md). The following are the specific types of verification each check performs, as well as general troubleshooting steps to resolve discovered issues:

<dl><dt>**Layers**</dt>
<dd>Checks for extra layers in the scene. Automatic fix attempts to remove extra layers.

If the automatic fix fails, manually remove extra layers.</dd>

<dt>**Transforms**</dt>
<dd>Checks that geometry location, rotation, and scale are frozen (`0`,`0`,`0`). Automatic fix button attempts to freeze the transforms. This may cause changes to your rig.

If the automatic fix fails, manually freeze your geometry.</dd>

<dt>**UV**</dt>
<dd>Checks if the body Geometry UVs are within `0`-`1`. You must resolve issues manually by setting your body object UVs within a `0`-`1` range.</dd>

<dt>**Cage UV Modifications**</dt>
<dd>Checks if cage object UVs have incorrect modifications. Automatic fix attempts to resolve UV coordinates.

If automatic fix fails, you may want to use a new template cage.</dd>

<dt>**Asset Size**</dt>
<dd>Checks if the character total size and individual parts are within expected bounds. You must resolve issues manually by resizing your character model or individual parts.</dd>

<dt>**Unused Data**</dt>
<dd>Checks for any unused data in the scene, such as orphan data, or unused materials. Automatic fix attempts to remove extra data.

If automatic fix fails, manually remove unnecessary data and objects.</dd>

<dt>**Keyframes**</dt>
<dd>Checks for any unnecessary keyframes. Keyframes related to facial expressions are expected and ignored. Automatic fix attempts to remove keyframes associated with non-face objects.

 If automatic fix fails, manually remove keyframe data from non-face objects. Do not delete keyframes that also contain facial data.</dd>

<dt>**Attachment Points**</dt>
<dd>Checks that attachment points are parented to the armature and use the correct naming convention. Automatic fix attempts to parent any unexpected attachment points.</dd>

<dt>**Joint Positions**</dt>
<dd>Checks for the following:

- Root and HumanoidRootNode bones exist
- Root bone is at `0`,`0`,`0` world space
- Bones with Left/Right naming conventions are on correct axes.

 Refer to the output messages to manually resolve joint position issues.</dd>

<dt>**FACS Data**</dt>
<dd>Checks for the following FACs data:

- `Neutral Pose` exists as a mapped pose
- Mapped Custom Properties under the Head_Geo exists
- Property name and values correctly set
- Corrective poses must include existing base poses
- Corrective poses do not use more than 3 base poses Refer to the output messages to manually resolve FACS data issues.

</dd>

<dt>**Head Joint Names**</dt>
<dd>Checks for duplicate head bone names, including duplicates with Blender's duplicate affixes .001, .002, .003, and such. Refer to the output messages to manually resolve face joint names.</dd>

<dt>**Intersection**</dt>
<dd>Checks for any intersection between character geometry and cage mesh geometry. The tool switches to Edit mode and highlights areas where potential intersections are detected.</dd>

<dt>**Polygon Data**</dt>
<dd>Checks for common polygon issues:

- Meshes are watertight
- Meshes are within polycount budgets
- Meshes don't use N-Gons Meshes
- Meshes are non-manifold
- Meshes don't have vertex color information

Refer to the output messages to manually resolve any polygon data issues.</dd>

<dt>**Texture Format**</dt>
<dd>Checks that textures match texture requirements, such as resolution size. Users can also select an external image file. Refer to the output messages to manually resolve any texture related issues.</dd>
</dl>
