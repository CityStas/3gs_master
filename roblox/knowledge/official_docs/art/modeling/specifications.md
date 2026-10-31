---
title: "General specifications"
url: /docs/en-us/art/modeling/specifications
last_updated: 2026-10-30T19:55:36Z
description: "Lists the specific technical requirements for custom models created outside of Studio."
---

# General specifications

Roblox supports a wide variety of mesh configurations created from third-party software such as [Blender](https://www.blender.org) or [Maya](https://www.autodesk.com/products/maya/overview).

Check that your model meets the following modeling specifications and guidelines before exporting to ensure Studio compatibility. Specific types of assets, like characters and accessories, have additional specifications:

> **Warning:** **If creating other types of 3D models:**- For rigid accessories, see [accessory specifications](/docs/en-us/avatar/rigid-accessories/specifications.md) and [accessory export settings](/docs/en-us/avatar/rigid-accessories/export.md). - For layered accessories, see [layered accessory specifications](/docs/en-us/avatar/layered-accessories/specifications.md) and [layered export settings](/docs/en-us/avatar/layered-accessories/export.md). - For avatar characters, see [avatar specifications](/docs/en-us/avatar/character-bodies/specifications.md) and [avatar export settings](/docs/en-us/avatar/character-bodies/export.md).

When ready to export, see the [export settings](/docs/en-us/art/modeling/export-requirements.md) for mesh export settings for Blender and Maya.

> **Info:** If you meet certain account requirements, you can sell your custom meshes as accessories on the Marketplace. See [Rigid accessories](/docs/en-us/avatar/rigid-accessories.md) for an overview on the creation process for these types of accessories.
## Geometry

See the following specifications for general geometry:

- **Budgets** - Individual meshes can not exceed 20,000 triangles. Avatar items have their own individual budget requirements for [character bodies](/docs/en-us/avatar/character-bodies/specifications.md), [rigid accessories](/docs/en-us/avatar/rigid-accessories/specifications.md), and [layered accessories](/docs/en-us/avatar/layered-accessories/specifications.md).
- **Watertight** - All geometry must be watertight without exposed holes or backfaces.
- **No N-gons** - Meshes must be in quads where possible.
- **Volume** - Meshes cannot be 0 thickness and must have some volume.

## Rigging and skinning

Roblox supports third-party meshes with an internal rig, or skeleton structure that can be used as additional articulation points in your model. For more information on the specific standards for R15 rigs, see [Character body specifications - Rigging](/docs/en-us/avatar/character-bodies/specifications.md#rigging).

![A cartoon-ish low polygon model of a puffer fish.](../../assets/animation/importing-custom-3d-rigs/Rig-Custom-Puffer-Blender.png)_Generic rig model._

![The Outliner in Blender of the puffer fish model, showing the armature bone structure.](../../assets/animation/importing-custom-3d-rigs/Rig-Hierarchy-Custom-Blender-Bones.png)_Generic rig bone structure (Blender)._

See the following requirements for general rigging and skinning:

- **Transformations** - All bones (Blender) or joints (Maya) must be frozen and have scale values set to `1`, `1`, `1` and rotation values set to `0`, `0`, `0`.
- **Symmetry** - When possible, maintain symmetry when applying influences to a rig
- **Root joint** - The root bone or joint should always be set to `0`, `0`, `0`.
- **Max influences** - A vertex can not be influenced by more than 4 bones or joints.
- **No Root influences** - Do not apply influences to the Root bone or joint.

## Textures

- Roblox supports basic color textures and modern [PBR textures](/docs/en-us/art/modeling/surface-appearance.md).
- For instructions on assigning texture images to natively import with your mesh, see [Assign textures in modeling tools](/docs/en-us/art/modeling/assign-textures.md).
- For technical requirements and best practices when generating individual texture images, see [Texture specifications](/docs/en-us/art/modeling/texture-specifications.md).

## Animations

An animation can be included on any `.fbx` mesh export. For information on prepping a character animation from a modeling software for export, see [Export animations from Maya](/docs/en-us/art/characters/export-avatar-animations-from-maya.md).

See the following requirements for assets with animation:

- **Single track animation** - Only a single animation track can be exported with a mesh or model. If you want to export multiple animations, you need to create separate exports for each animation you want to import.

## Inner and outer cages

Inner and Outer cages are non-rendered meshes that Roblox uses to define the inner and outer surfaces of a mesh using a `Class.WrapLayer` or `Class.WrapTarget` instance. These cages are most often used with characters and accessories, though you can use cage meshes for any mesh object.

> **Warning:** Character models must include an outer cage in order to properly equip layered accessories. For more information, see [Character body specifications](/docs/en-us/avatar/character-bodies/specifications.md).

For general use, see the following requirements for adding inner and outer cage meshes to your model:

- **Naming conventions** - The inner and outer cage must be named after the primary mesh object with **_InnerCage** and **_OuterCage** affixed.![The Outliner in Blender showing two mesh objects called Tshirt_InnerCage and Tshirt_OuterCage.](../../assets/accessories/lc-blender-selecting-cage-in-outlier.png)
- **Outer cage** - Models, such as a playable character, that aren't expected to deform but are the target of meshes that will stretch over it, only require an outer cage.
  - For more information on applying and implementing cages on non-Humanoid targets, see [layered accessories on non-R15](/docs/en-us/characters/appearance.md#layered-accessories-on-non-r15).
- **Vertices and UV map** - Don't delete vertices or alter the UVs on the Inner or Outer Cages as this can cause errors when importing in Studio or when equipping onto a character.
- **Symmetry and consistency** - Keep each face (the space between vertices) consistently sized and retain symmetry wherever possible. Use symmetry tools in your modeling software whenever possible.
