---
title: "Template head structure"
url: /docs/en-us/art/characters/creating/head-objects
last_updated: 2026-10-30T19:55:33Z
description: "Each Roblox avatar template contains modular separate pieces that must later be combined or removed."
---

# Template head structure

Each avatar character body template includes extra head mesh objects and face armature bones. Separating these objects within the templates allows you to make easier changes to each of these separate objects, as demonstrated during the texturing section of this tutorial.

To avoid validation errors, you must [join](/docs/en-us/art/characters/creating/combine-head-geometry.md) and [remove](/docs/en-us/art/characters/creating/remove-extra-bones.md) these extra objects during the cleanup process prior to exporting.

The extra head mesh objects are the following:

- Head_Geo
- UpperTeeth_Geo
- LowerTeeth_Geo
- Tongue_Geo
- RightLash_Geo
- RightEye_Geo
- LeftLash_Geo
- LeftEye_Geo

![Head-Related Meshes](../../../assets/art/blender-ui/Face-Objects.png)_Extra head-related meshes in Blender's Outliner_

The extra head bone children are the following and may differ between templates:

- Tongue
- LowerTeeth
- UpperTeeth
- LeftEye
- RightEye

![Head-Related Meshes](../../../assets/art/blender-ui/Face-Bones.png)_Extra head-related bones in Blender's Outliner_

While these extra objects exist to aid the creation and modification process, leaving them in your project on final export will cause validation issues when uploading these assets to the Marketplace.
