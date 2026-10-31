---
title: "Character body reference files"
url: /docs/en-us/avatar/character-bodies/project-files
last_updated: 2026-10-30T19:55:37Z
description: "Download various project files and reference files for character bodies."
---

# Character body reference files

The following project files and templates are specifically helpful when creating a character body for an avatar. For a comprehensive list of Roblox's official downloadable content for avatars, such as rigid and layered accessory templates, see [Resources](/docs/en-us/avatar/resources.md).

## Project files

The following `.fbx`, `.blend`, and `.ma` project files are available to use as examples, boilerplate, or as a reference for your own custom character bodies for avatars:

#### Models

**Advanced R15 rigs**

The following [advanced R15 rigs](/docs/en-us/avatar/character-bodies/specifications.md#advanced-r15-rigs) include additional bones or joints for a higher level of realism with articulated hands, shoulders, and spine movements.

| **File name** | **Description** |
| --- | --- |
| [Mannequin-HigherFidelity.zip](../../assets/art/reference-files/Mannequin-HigherFidelity.zip) | A comprehensive `.zip` folder of a AA avatar-ready character body, including a dynamic head, fingers, layered accessories, and 2K PBR textures. |
| [Robuta-HigherFidelity.zip](../../assets/art/reference-files/Robuta-HigherFidelity.zip) | A comprehensive `.zip` folder of an anime-style, avatar-ready character body, including a dynamic head, fingers, rigid and layered accessories, and 2K PBR textures. |
| [HipToBeSquare-HigherFidelity.zip](../../assets/art/reference-files/HipToBeSquare-HigherFidelity.zip) | A comprehensive `.zip` folder of a blocky-style, avatar-ready character body, including a dynamic head, fingers, rigid and layered accessories, and color, roughness, and metal PBR textures. |
| [Roxie-HigherFidelity.zip](../../assets/art/reference-files/Roxie-HigherFidelity.zip) | A comprehensive `.zip` folder of an avatar-ready character with an [Rthro Normal](/docs/en-us/avatar/character-bodies/specifications.md#normal) body, including a dynamic head, fingers, rigid and layered accessories, and PBR textures. When you import this model, set **Rig Scale** to **Rthro Narrow**. |

**Standard R15 rigs**

The following [standard R15 rigs](/docs/en-us/avatar/character-bodies/specifications.md#standard-r15-rigs) include the standard amount of bones or joints.

| **File name** | **Description** |
| --- | --- |
| [Lola.fbx](../../assets/modeling/skinned-meshes/Lola.fbx) | A skinned character with a [standard R15 rig](/docs/en-us/avatar/character-bodies/specifications.md#standard-r15-rigs) created from the [Skin a humanoid model](/docs/en-us/art/modeling/skin-a-humanoid-model.md) guide. Since this reference model doesn't yet have [inner and outer cage mesh data](/docs/en-us/avatar/character-bodies/specifications.md#inner-and-outer-cages), this model can't equip layered accessories. |
| [Fish-Person.zip](../../assets/avatar/dynamic-heads/reference-files/Fish-Person.zip) | A rigged and skinned humanoid character model with a full body cage, facial animation rig, and associated PBR texture maps. |
| [BlockyCharacter.fbx](../../assets/avatar/dynamic-heads/reference-files/BlockyCharacter.fbx) | A Blocky character model with an [animatable head](/docs/en-us/avatar/dynamic-heads.md) and a full body cage. |
| [GoblinCharacter.zip](../../assets/avatar/dynamic-heads/reference-files/GoblinCharacter.zip) | A Goblin character model with an [animatable head](/docs/en-us/avatar/dynamic-heads.md) and a full body cage. |
| [ClassicMannequin.fbx](../../assets/art/reference-files/ClassicMannequin.fbx) | A [classic](/docs/en-us/avatar/character-bodies/specifications.md#classic) body type blank mannequin to use in Studio or your modeling application. |
| [ClassicMannequin_With-Cages](../../assets/art/reference-files/ClassicMannequin_With-Cages.fbx) | A [classic](/docs/en-us/avatar/character-bodies/specifications.md#classic) body type blank mannequin with **body cages** to use in Studio or your modeling application for clothing design. Due to unconfigured cage objects, this file may not import correctly into Studio until modified. |
| [RthroMannequin.fbx](../../assets/art/reference-files/RthroMannequin.fbx) | An [Rthro Normal](/docs/en-us/avatar/character-bodies/specifications.md#normal) body type blank mannequin to use in Studio or your modeling application. |
| [RthroMannequin_With-Cages.fbx](../../assets/art/reference-files/RthroMannequin_With-Cages.fbx) | An [Rthro Normal](/docs/en-us/avatar/character-bodies/specifications.md#normal) body type blank mannequin with **body cages** to use in Studio or your modeling application for clothing design to use in Studio or your modeling application. Due to unconfigured cage objects, this file may not import correctly into Studio until modified. |
| [RthroSlenderMannequin.fbx](../../assets/art/reference-files/RthroSlenderMannequin.fbx) | An [Rthro Slender](/docs/en-us/avatar/character-bodies/specifications.md#slender) body type blank mannequin to use in Studio or your modeling application. |
| [RthroSlenderMannequin_With-Cages.fbx](../../assets/art/reference-files/RthroSlenderMannequin_With-Cages.fbx) | An [Rthro Slender](/docs/en-us/avatar/character-bodies/specifications.md#slender) body type blank mannequin with **body cages** to use in Studio or your modeling application to use in Studio or your modeling application for clothing design. Due to unconfigured cage objects, this file may not import correctly into Studio until modified. |

#### Blender

| **File** | **Description** |
| --- | --- |
| [Rig_and_Attachments_Template.blend](../../assets/modeling/meshes/reference-files/Rig_and_Attachments_Templates.zip) | Starting rigging armature template for Blender. Contains a [standard R15 rig](/docs/en-us/avatar/character-bodies/specifications.md#standard-r15-rigs) with correct naming conventions and attachment points. Use this template for rigging character bodies and layered accessories. |
| [Body_Cage_Template.blend](../../assets/modeling/meshes/reference-files/Body_Cage_Templates.zip) | Starting template for Blender, includes individual cages for each of the character's 15 humanoid body parts. Use this template for caging your character bodies.<br> <br> > **Info:** To save time, edit the full-body `std_cage_deformable` mesh to automatically apply vertex changes to the individual body part meshes. When importing the `.fbx` into Studio, you can remove this helper mesh. |
| [Combined-Template.blend](../../assets/modeling/meshes/reference-files/Combined_Templates.zip) | Template file containing all content from previous templates, includes a rigging armature, body cages, and attachment points. Use this template to rig and cage character bodies and accessories. |

#### Maya

| **File** | **Description** |
| --- | --- |
| [Rig_and_Attachments_Template.ma](../../assets/modeling/meshes/reference-files/Rig_and_Attachments_Templates.zip) | Starting rigging armature template for Maya. Contains a [standard R15 rig](/docs/en-us/avatar/character-bodies/specifications.md#standard-r15-rigs) with correct naming conventions and attachment points. Use this template for creating character bodies and layered accessories. |
| [Body_Cage_Template.ma](../../assets/modeling/meshes/reference-files/Body_Cage_Templates.zip) | Starting template for Maya, includes individual cages for each of the character's 15 humanoid body parts. Use this template for caging your character bodies.<br> <br> > **Info:** To save time, edit the full-body `std_cage_deformable` mesh to automatically apply vertex changes to the individual body part meshes. When importing the `.fbx` into Studio, you can remove this helper mesh. |
| [Combined-Template.ma](../../assets/modeling/meshes/reference-files/Combined_Templates.zip) | Template file containing all content from previous templates, includes a rigging armature, body cages, and attachment points. Use this template to rig and cage character bodies and accessories. |

#### General

> **Warning:** The following `.fbx` files were exported from Maya for use in modeling applications. If you are using Blender or Maya in your workflow, use the specific template files for those programs instead of the following files.

| **File** | **Description** |
| --- | --- |
| [Rig_and_Attachments_Template.fbx](../../assets/modeling/meshes/reference-files/Rig_and_Attachments_Templates.zip) | Starting rigging armature template for general modeling software. Contains a [standard R15 rig](/docs/en-us/avatar/character-bodies/specifications.md#standard-r15-rigs) with correct naming conventions and attachment points. Use this template for creating character bodies and layered accessories. |
| [Body_Cage_Template.fbx](../../assets/modeling/meshes/reference-files/Body_Cage_Templates.zip) | Starting template for general modeling software, includes individual cages for each of the character's 15 humanoid body parts. Use this template for caging your character bodies.<br> <br> > **Info:** To save time, edit the full-body `std_cage_deformable` mesh to automatically apply vertex changes to the individual body part meshes. When importing the `.fbx` into Studio, you can remove this helper mesh. |

## Templates

If you are creating custom character body models, you can choose from a variety of starting templates that best match your final design to save time on creating the [avatar components](/docs/en-us/avatar/character-bodies.md#character-body-components). For important information on using these template files, see [Create with templates](/docs/en-us/art/characters/creating.md#template-files).

Each `.zip` contains a `.blend`, `.fbx`, and PBR texture `.png` files for that template model. If using Blender or following the [template creation guides](/docs/en-us/art/characters/creating.md), use the `.blend` project.

> **Warning:** If you are using Roblox's avatar template files, you must perform the [cleanup steps](/docs/en-us/art/characters/creating/combine-head-geometry.md) in order for the assets to properly validate before publishing to the Marketplace.

#### Head Shapes

_ Round_

Female: [RoundFemale.zip](../../assets/art/reference-files/RoundFemale.zip)  Male: [RoundMale.zip](../../assets/art/reference-files/RoundMale.zip)

_ Square_

Female: [SquareFemale.zip](../../assets/art/reference-files/SquareFemale.zip)  Male: [SquareMale.zip](../../assets/art/reference-files/SquareMale.zip)

_ Muzzle_

Female: [MuzzleFemale.zip](../../assets/art/reference-files/MuzzleFemale.zip)  Male: [MuzzleMale.zip](../../assets/art/reference-files/MuzzleMale.zip)

#### Realistic

_ Realistic_

Female: [SemiRealisticFemale.zip](../../assets/art/reference-files/SemiRealisticFemale.zip)  Male: [SemiRealisticMale.zip](../../assets/art/reference-files/SemiRealisticMale.zip)

#### Anime

_ Anime_

Female: [AnimeFemale.zip](../../assets/art/reference-files/AnimeFemale.zip)  Male: [AnimeMale.zip](../../assets/art/reference-files/AnimeMale.zip)

#### Stylized

_ Stylized_

Single body: [Stylized.zip](../../assets/art/reference-files/StylizedHuman.zip)

#### Caricature

_ Caricature_

Single body: [Caricature.zip](../../assets/art/reference-files/Caricature.zip)
