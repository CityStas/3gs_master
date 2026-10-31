---
title: "Rigging and skinning"
url: /docs/en-us/art/modeling/rigging
last_updated: 2026-10-30T19:55:36Z
description: "Rigging and skinning is a modeling process that connects an armature to a mesh, allowing it to be animated or posed in Studio."
---

# Rigging and skinning

**Rigging** is the process of connecting a mesh with an internal poseable skeleton rig and bone structure. Rigged meshes allow mesh surfaces to rotate and move where internal bones are placed within the model during the modeling process. Rigging is often performed in conjunction with **skinning**, creating a natural looking stretch and bend when models are animated or repositioned. You can create rigged meshes with third-party software such as [Blender](https://www.blender.org) or [Maya](https://www.autodesk.com/products/maya/overview).

_A normal model can only rotate on its pivot point._

_A rigged model (or mesh) can rotate with any bone of its associated rig._

_A rigged model with no skinning data._

_A skinned model that bends organically with the bone rotation._

See the following resources to learn the basics and intermediate steps required to skin models in Blender:

- [Rig a simple mesh](/docs/en-us/art/modeling/rig-a-simple-mesh.md)
- [Skin a simple mesh](/docs/en-us/art/modeling/skin-a-simple-mesh.md)
- [Rig a humanoid model](/docs/en-us/art/modeling/rig-a-humanoid-model.md)
- [Skin a humanoid model](/docs/en-us/art/modeling/skin-a-humanoid-model.md)

## Rigs and bones

The **rig**, or bone structure, within a rigged mesh creates additional poseable points for the 3D model in Studio. By rotating or moving the bones of a mesh, the parts of the mesh assigned to those bones can move independently from the rest of the mesh. The assignment of influence between meshes and bones, such as a **LowerLeftArm** bone driving the movement of the **LowerLeftArm** geometry, is set in a third-party application like Blender or Maya. When imported into Studio, Roblox saves this influence assignment data to the `Class.MeshPart` asset data.

Once you successfully [import](/docs/en-us/parts/meshes.md#import-meshes) a rigged mesh model into Studio, Studio represents this rig structure with `Class.Bone` instances that you can then pose and animate. You can view bones in Studio by enabling **Show Constraint Details** from the **View** menu, or when you are using the [Animation Editor](/docs/en-us/animation/editor.md).

> **Info:** When `Class.Bone` objects are used in animation, they affect the appearance of the parts but don't change the physical shape in cases such as [collision detection](/docs/en-us/workspace/collisions.md).

![A translucent humanoid outline, showing various sphere points where the constraints exist.](../../assets/modeling/skinned-meshes/Rig-Constraint-Details.jpg)_Constraint Details enabled_

![A translucent humanoid outline, showing 15 pink bones objects over various limbs.](../../assets/modeling/skinned-meshes/Rig-Bone-Visualization.jpg)_When using the Animation Editor_

## Types of rigs

Rigged models use a naming convention starting with "R" and ending with the number of individual meshes that make up the model. This is used to quickly identify the type and number of meshes that a model has. Although R6 and R15 models are common, a model can be of varying subjects, sizes and can have any number of individual meshes, such as a R5, R20, or R200.

- **R1** refers to a single mesh that is rigged, or associated with an internal skeleton structure. Many models, such as a tree or accessory item, are good candidates to be made into an R1 model. Even NPC humanoid characters can be created as R1 models, but they will not be able to take full advantage of the animation and humanoid options available for R15 characters. See [Rig a simple mesh](/docs/en-us/art/modeling/rig-a-simple-mesh.md) for instructions on turning a basic mesh into an R1 model in Blender.
- **R15** typically refers to humanoid models used as player or avatar characters. An R15 model is made up of 15 specific meshes that are parented to a single [R15 rig](/docs/en-us/avatar/character-bodies/specifications.md#rigging). An R15 character model often includes skinning data to allow the model to bend and pose naturally. Roblox uses the R15 standard for all avatars, and requires the [technical specifications](/docs/en-us/avatar/character-bodies/specifications.md) to ensure universal behavior and quality. See [Rig a humanoid model](/docs/en-us/art/modeling/rig-a-humanoid-model.md) for instructions on turning a character model into an R15 humanoid model in Blender.
