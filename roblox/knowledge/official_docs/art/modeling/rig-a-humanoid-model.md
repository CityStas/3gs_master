---
title: "Rig a humanoid model"
url: /docs/en-us/art/modeling/rig-a-humanoid-model
last_updated: 2026-10-30T19:55:36Z
description: "Explains the process for rigging a humanoid R15 model in Blender."
---

# Rig a humanoid model

An R15 humanoid character model, such as those that make up user avatar characters, is made up of 15 individual mesh objects. Similar to rigging a simple mesh, you can bind or parent a group of meshes to an internal rig. Models made up of multiple meshes require additional steps to rig in a third-party modeling tool such as [Blender](https://www.blender.org) or [Maya](https://www.autodesk.com/products/maya/overview).

This advanced guide covers the process of rigging a humanoid model in Blender using a provided template and humanoid model. This rigging step is required before [skinning the humanoid model](/docs/en-us/art/modeling/skin-a-humanoid-model.md). You should be familiar with [rigging a basic model](/docs/en-us/art/modeling/rig-a-simple-mesh.md) before continuing.

To rig a humanoid model in Blender:

- [Import a character model](#import-model) into a template file to easily access a premade [standard R15 rig](/docs/en-us/avatar/character-bodies/specifications.md#standard-r15-rigs).
- [Create, size, and position bones](#set-bones-and-armature) symmetrically for a humanoid character.
- [Parent](#parent-armature) multiple meshes to a single armature to bind the skeleton rig.
- [Assign full influence](#assign-meshes-to-bones) to each mesh object and bone by assigning influences.

> **Info:** This guide uses a downloadable [Rig and Attachment Template Blender Project](../../assets/modeling/meshes/reference-files/Rig_and_Attachments_Templates.zip), a reference [Lola Character model](../../assets/modeling/meshes/reference-files/lola-base-model.fbx), and [Blender version 3.0](https://www.blender.org/download/releases/3-0/). If you are using another version of Blender, there may be minor differences in UI and settings.
## Set up Blender

To begin creating a humanoid rigged mesh, first set up the following in your Blender project:

- [Import](#import-model) the Lola character model in the Mannequin Template Blender project.
- Set up your [Viewport visualizations](#viewport-visualizations) to optimize the rigging process.

### Import model

When rigging a model, make sure the character model you are using follows Studio's [Avatar character specifications](/docs/en-us/avatar/character-bodies/specifications.md). For this guide, import a [Lola reference model](../../assets/modeling/meshes/reference-files/lola-base-model.fbx) into the mannequin template project.

To import your model:

1. In Blender, navigate to **File** > **Open** and select `Rig_and_Attachments_Template.blend`.
2. Navigate to **File** > **Import** > **FBX (.fbx)** and import the reference Lola model file.
3. If required, scale the model to roughly match the scale of the armature bone structure. You can select all the mesh geometries in the Outliner and press `G` to reposition and `S` to scale the mesh objects by dragging your mouse.

### Viewport visualizations

For better visualization and access to your bone objects, set your bone objects to always be displayed in front of the Viewport.

To set the bone visualization:

1. In the **Viewport**, click on any of the bones in your armature.
2. In the **Properties Editor** panel, select the **Object Data Properties** tab.
3. Expand **Viewport Display**, navigate to the **Show** property, then enable **In Front**.

At any point during the skinning process, you can also toggle one of the various material previews options in the top right of your 3D Viewport to change the visualization of your character model, such as enabling X-ray or texture view.

## Set bones and armature

In this guide, set up X-Axis Mirroring to make symmetrical changes to the left and right bones before repositioning the bones to the imported model. Try to maintain symmetry whenever possible when rigging a model.

> **Warning:** If modifying bones or creating a new bone structure, it's important to ensure it follows the standardized bone hierarchy and naming conventions for either a [standard](/docs/en-us/avatar/character-bodies/specifications.md#standard-r15-rigs) or [advanced](/docs/en-us/avatar/character-bodies/specifications.md#advanced-r15-rigs) R15 rigging armature for avatar character models.
### Enable x-axis mirror

The X-Axis Mirror setting allows you to maintain symmetry with your left and right bones by mirroring changes to their positions. To reduce issues with posing and animating, it is important to retain symmetry with your bone structure whenever possible.

To set up X-Axis Mirror:

1. In **Object Mode**, select your **armature** by clicking on any bone.
2. Switch to **Edit Mode** (`Tab`).
3. In the Viewport's right sidebar, extend the Tool panel and enable **X-Axis Mirror**.

### Position bones

With the model added to the project, you can reposition the bones provided in the template to match the character structure. In most cases, each bone should be positioned in the center of their corresponding mesh objects, such as the Head bone being centered within the Head_Geo mesh object.

Bone positioning may differ based on use-case and may need to be revisited after weight painting and testing if a certain pose or animation doesn't work as intended.

To position your individual bones:

1. In Object Mode, click on the **bone** you intend to reposition to highlight it.
2. From the Mode dropdown, switch to **Edit Mode**.
3. Click on the **tip** of the bone so that the tip is highlighted and press `G`. The top of the bone moves with your cursor.
4. Pull this bone to align with the interior center of the model, then click to set the bone's position.
5. Click and hold your mouse's scroll wheel or use one of the various perspective views to verify that the bone is within the mesh object.

### Parent armature

After you position the bone structure, you need to parent the bone armature to the model. You must parent all 15 mesh objects to one armature.

For this example, the mesh objects are parented to the armature with Empty Groups to illustrate the vertex group assignment and weight painting process in the following [Skin a humanoid model](/docs/en-us/art/modeling/skin-a-humanoid-model.md) guide.

To parent the model to the armature:

1. Switch to **Object Mode**.
2. In the Outliner, filter your mesh objects by typing **"geo"** in the search bar.
3. Select all of the mesh objects in the Outliner by holding `Shift` and clicking on the first and last mesh objects.
4. With the meshes highlighted, hold `Shift` and click on the Armature object in the Viewport or Outliner.
5. Right click in the Viewport and select **Parent** > **With Empty Groups**.

## Assign meshes to bones

Now that you have connected your armature to the mesh object, you can assign the vertices of your individual limbs to be fully influenced by one corresponding bone. After this process is completed, the model will be ready for skinning. See [Skin a humanoid model](/docs/en-us/art/modeling/skin-a-humanoid-model.md) for instructions on applying multiple bone influences to a mesh.

> **Warning:** The **Root** and **HumanoidRootNode** parent bones in a humanoid rig should not have any influences applied to them. Any added influences are dropped when importing into Studio.

To assign full influence to the head mesh:

1. In **Object Mode**, click on the **head mesh object** to highlight it.
2. Switch to **Edit Mode**.
3. Select all the vertices of your mesh object by pressing `A`.
4. After all the head vertices are highlighted, navigate to the **Object Properties** panel on the right side of the screen.
5. In the **Vertex Group** section of the panel, select the name of the bone you want to assign the Head geometry to and click **Assign**.

You can quickly iterate through all of your mesh objects in this mode by selecting the next mesh object in the Outliner and assigning it to the appropriate Vertex Group. For this guide, **assign all of your character's mesh objects to their appropriate bone**.

To quickly assign vertex groups to the rest of the body meshes:

1. In the **Outliner** panel, **click** the dot next to the object you intend to edit. The dot switches to the active edit icon when pressed.
2. If the vertices are not highlighted, press `A` to select all vertices.
3. In the **Object Properties** panel > **Vertex Groups** section, select the appropriate vertex group and click **Assign**. You can use the search bar to find the specific vertex group name.

## Test

You can test and pose bones and their assigned mesh objects in Pose Mode. It is important to test your model after applying or editing any influences.

To navigate to Pose mode and test your poses:

1. In **Object Mode**, select any part of your model.
2. Click on the Mode dropdown, then switch to **Pose** mode.
3. Hold `Shift` and click the bone you want to test to highlight it, then press `R` to test the rotation.
4. Press `Alt``A` (`⌥``A`) to deselect the current bone, then reselect and test another bone.

> **Info:** To reset the rotation of a selected bone to neutral, press `Alt`+`R`. While rotating, you can also press your mouse's scroll wheel to change the axes of your rotation.

At this stage, if all of your mesh objects are influenced by their corresponding bones, you can [export](/docs/en-us/art/modeling/export-requirements.md) this rigged model as an `.fbx` for use in Studio or continue on to the next stage of [Skin a humanoid model](/docs/en-us/art/modeling/skin-a-humanoid-model.md).
