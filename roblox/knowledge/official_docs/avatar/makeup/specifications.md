---
title: "Makeup specifications"
url: /docs/en-us/avatar/makeup/specifications
last_updated: 2026-10-30T19:55:37Z
description: "Makeup is a cosmetic look made up of multiple facial textures and optional eyebrow and eyelashes."
---

# Makeup specifications

Makeup requires a specific set of components and configuration standards to ensure it displays properly on avatar faces of all shapes and sizes. Before you start the export process, verify that your makeup meets the following specifications and guidelines for proper Studio compatibility.

When you're ready to export your makeup, reference all [export setting requirements](/docs/en-us/avatar/makeup/reassign-textures.md) for Blender and Maya.

> **Info:** **For other types of 3D models:**- [General mesh](/docs/en-us/art/modeling/specifications.md) specifications. - [Rigid accessory](/docs/en-us/avatar/rigid-accessories/specifications.md) specifications. - [Layered accessory](/docs/en-us/avatar/layered-accessories/specifications.md) specifications.
## General

If you are following the best practice [creation process](/docs/en-us/avatar/makeup.md#creation-process), ensure that your template file submission includes the following objects that are correctly configured and named in their respective third-party modeling software:

- A **head mesh object** and associated **cage mesh object**.
  - These two objects must include the prefix "TransferTarget_" in their name.
- **TransferTexture mesh objects** for each region: `Eyes`, `Face`, `Lips`.
  - These three objects must follow the following naming conventions.
    - `TransferTexture_Eyes_01`
    - `TransferTexture_Lips_01`
    - `TransferTexture_Face_01`
    - Any for multiple regions, increment the affix number: `TransferTexture_Face_02`
- Optional [eyebrows and eyelashes](#eyebrows-and-eyelashes).

> **Warning:** The [provided Roblox makeup template head](https://github.com/Roblox/avatar/tree/main/Makeup) should already be properly configured with the correct objects and naming conventions. To prevent issues with import, avoid renaming or deleting the data model of the template head when creating your own makeup.
## Decals and textures

All accessory textures must meet Roblox's [texture specifications](/docs/en-us/art/modeling/texture-specifications.md), but makeup textures include two additional considerations:

- There is a 4K texture limit for [in-game](/docs/en-us/avatar/in-experience-creation.md) makeup creation.
- There is a 1K texture limit for makeup that you upload to the [Marketplace](https://www.roblox.com/catalog).

For additional information on PBR textures, see [PBR textures](/docs/en-us/art/modeling/surface-appearance.md).

## Eyebrows and eyelashes

Eyebrows and eyelashes are optional layered accessories for makeup looks. If you choose to include them in your creations, they must meet all [layered accessory requirements](/docs/en-us/avatar/layered-accessories/specifications.md), notably:

- **Cage data** - Eyebrows and eyelashes each require their own inner and outer cage.
  - Eyebrows and eyelashes can also take advantage of automatic skinning, specifically with [special skinning joints](/docs/en-us/avatar/automatic-skinning-transfer.md#special-skinning-transfer-joints).
- **Geometry size** - Eye accessories can't exceed the [maximum dimensions](/docs/en-us/avatar/layered-accessories/specifications.md) for their asset type.
- **Budgets** - Eye accessories can't exceed 4k triangles each.
