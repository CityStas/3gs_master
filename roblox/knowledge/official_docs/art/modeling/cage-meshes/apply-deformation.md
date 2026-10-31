---
title: "Apply deformation"
url: /docs/en-us/art/modeling/cage-meshes/apply-deformation
last_updated: 2026-10-30T19:55:35Z
description: "Deform a caged mesh onto a target shape with a WrapLayer, the basis of layered accessories."
---

# Apply deformation

Once a target caged mesh and a layered caged mesh are imported into your experience, you can apply a deformation by parenting both `Class.MeshPart|MeshParts` within a `Class.Model` and adding a `Class.WeldConstraint`.

![A grey twisted target, a red-and-white checker cube, and the checker cube reshaped to match the twisted target, in Studio.](../../../assets/modeling/cage-meshes/Apply-Deformation-Hero.png) ## Deform a mesh

Download the reference files to follow along. The Blender project contains every shape, and each `.fbx` imports as a ready-made target or layered mesh with its cages.

| **File** | **Description** |
| --- | --- |
| [Cage-Mesh-Examples.blend](../../../assets/modeling/meshes/reference-files/Cage-Mesh-Examples.blend) | A Blender project containing every target and layered mesh in this guide, with their cages. |
| [Cube_Target.fbx](../../../assets/modeling/meshes/reference-files/Cube_Target.fbx) | A cube target, ready to import as a `Class.MeshPart` with a `Class.WrapTarget`. |
| [Sphere_Target.fbx](../../../assets/modeling/meshes/reference-files/Sphere_Target.fbx) | A sphere target, ready to import as a `Class.MeshPart` with a `Class.WrapTarget`. |
| [Cube-Flattened_Target.fbx](../../../assets/modeling/meshes/reference-files/Cube-Flattened_Target.fbx) | A flattened cube target, ready to import as a `Class.MeshPart` with a `Class.WrapTarget`. |
| [Layered-Mesh1.fbx](../../../assets/modeling/meshes/reference-files/Layered-Mesh1.fbx) | A layered mesh with inner and outer cages, ready to import as a `Class.MeshPart` with a `Class.WrapLayer`. |
| [Layered-Mesh2.fbx](../../../assets/modeling/meshes/reference-files/Layered-Mesh2.fbx) | A second layered mesh, ready to import as a `Class.MeshPart` with a `Class.WrapLayer`. |

1. Ensure that your workspace includes two 3D objects: a target `Class.MeshPart` and a layered `Class.MeshPart`.
  1. Confirm the target has a `Class.WrapTarget` and the deforming mesh has a `Class.WrapLayer`.![The Studio Explorer showing the target MeshPart with a child WrapTarget object.](../../../assets/modeling/cage-meshes/WrapTarget-Explorer.png)_Target: a `Class.WrapTarget`_![The Studio Explorer showing the layered MeshPart with a child WrapLayer object.](../../../assets/modeling/cage-meshes/WrapLayer-Explorer.png)_Deforming mesh: a `Class.WrapLayer`_
  2. (Optional) If testing or applying multiple deformations, make a copy of your layered mesh to ensure you have an original copy later.
2. In the Explorer, parent both target and layered `Class.MeshPart|MeshParts` in one `Class.Model`.![The Studio Explorer showing the target and layered MeshParts grouped in one Model.](../../../assets/modeling/cage-meshes/Group-And-Align.png)
3. Add a `Class.WeldConstraint` to the layered `Class.MeshPart`, then:
  1. Set `Part0` to the layered mesh.
  2. Set `Part1` to the target mesh.![The WeldConstraint properties with Part0 set to the layered mesh and Part1 set to the target.](../../../assets/modeling/cage-meshes/WeldConstraint-First-Layer.png)
4. In the Properties window, change `Class.WrapLayer.Order` from the default value to another number, such as `2` or `5`.
  1. Changing this property triggers the deformation in the 3D workspace so the layered mesh reshapes to match the shape of the target.
  2. If the order is incorrect with other layers, such as a T-shirt wrapping over a sweater, you can change this property at any time.![The WrapLayer properties with the Order property set.](../../../assets/modeling/cage-meshes/WrapLayer-Order-Property.png)
5. (Optional) The deformation is retained after it computes, so you can delete the duplicated layered mesh and the `Class.WeldConstraint` and reset `Class.WrapLayer.Order`, leaving a single deformed mesh. This is useful to simplify your workspace when applying multiple deformations.![A grey cube target beside the checker layered mesh deformed onto it, in Studio.](../../../assets/modeling/cage-meshes/Basic-Deformation.png)
6. Experiment further. Try deforming the reference layered meshes onto the other target shapes, or [deform multiple meshes onto a single target](#deform-multiple-meshes-to-a-single-target).

## Deform multiple meshes to a single target

You can continue to add layered meshes to a target by repeating the process of adding a layered mesh and a weld. Every time a layered mesh is added to a target, Roblox recalculates the surface of the mesh, allowing you to continually add to your target mesh.

> **Warning:** Every mesh you layer onto a target must share the same UV layout as the target. Roblox pairs each layer to the target by UV, so mismatched UVs won't deform correctly.

1. With your existing deformed mesh in the workspace, add a new layered `Class.MeshPart` into your `Class.Model`.![The Studio Explorer showing a second layered MeshPart added to the Model alongside the first.](../../../assets/modeling/cage-meshes/Add-Second-WrapLayer.png)
2. Add a `Class.WeldConstraint` to the new layered `Class.MeshPart`, then:
  1. Set `Part0` to the original layered mesh.
  2. Set `Part1` to the new layered mesh.![The WeldConstraint properties with Part0 set to the first layered mesh and Part1 set to the second.](../../../assets/modeling/cage-meshes/WeldConstraint-Second-Layer.png)
3. Change `Class.WrapLayer.Order` in the Properties window. Changing this property triggers the deformation, and the mesh reshapes to match the target. Each layer's `Class.WrapLayer.Order` determines which one renders on top.![The second layer rendering on top of the first in Studio.](../../../assets/modeling/cage-meshes/Ordering-Example-1.png)_The first layer's `Class.WrapLayer.Order` is `1` and the second layer's is `2`, so the second layer renders on top._![The first layer rendering on top of the second in Studio.](../../../assets/modeling/cage-meshes/Ordering-Example-2.png)_Updating the first layer's `Class.WrapLayer.Order` to `2`, and setting the second layer to `1`, brings the first layer on top._

## Deform an accessory on an avatar

All Roblox avatars share the same standard body cage. Because cages pair by UV, an accessory caged to that shared layout fits every avatar body. Note that the example meshes in this guide use their own cages, so they aren't compatible with Roblox's standard body cage.

![Head and upper-torso cage meshes shown as wireframes on an avatar.](../../../assets/art/avatar/Cage-Mesh-Visual.png)_Head and Upper Torso cage mesh objects (wireframe)_

![The Explorer showing cage objects on each of the 15 avatar body parts.](../../../assets/art/avatar/Cage-Mesh-Data-Model.png)_Cage objects must exist for each of the 15 body parts_

When creating avatar characters and avatar accessories, a similar process of layering applies to a `Class.Humanoid` character's body cages, and the layered accessory pipeline composes the layered mesh automatically. This allows fitting across body types and transferring skinning data through `Class.WrapLayer.AutoSkin`.

> **Warning:** If you are creating your own custom non-Marketplace characters that utilize a unique cage / UV solution, see [Layered accessories on non-R15](/docs/en-us/characters/appearance.md#layered-accessories-on-non-r15).

For an overview of creating your first layered accessory, see the following video:

For the full avatar workflow, see [Layered accessories](/docs/en-us/avatar/layered-accessories.md), the [Accessory Fitting Tool](/docs/en-us/avatar/accessory-fitting-tool.md), and [Automatic Skinning Transfer](/docs/en-us/avatar/automatic-skinning-transfer.md).
