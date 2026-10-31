---
title: "Test character bodies"
url: /docs/en-us/avatar/character-bodies/test
last_updated: 2026-10-30T19:55:37Z
description: "Verify the important aspects of your character model in Blender and in Studio."
---

# Test character bodies

To ensure your character bodies for avatars can move, interact with objects in the 3D space, and wear cosmetics, clothing, and accessories, it's important to periodically test their components in both your third-party modeling tool and in Studio as you iterate on their design. By testing often, you can save yourself a lot of time in having to rework time-intensive processes like rigging, skinning, and caging.

Whether you are using a [template character](/docs/en-us/avatar/resources.md#templates) or [project file](/docs/en-us/avatar/resources.md#project-files) as a basis for your character body, reference the following tables for common tests and resources you can use throughout the creation process to comprehensively quality check each component of your character models.

#### Blender Tests

> **Info:** You can apply the following workflows with any 3D modeling software, though certain interfaces and instructions may differ between platforms. For more information, see [Test character bodies in Blender](/docs/en-us/avatar/character-bodies/test-blender.md).

| Component | Testing recommendations |
| --- | --- |
| <br>**Body Parts** | When modeling, confirm that your character's geometry follows Roblox's [geometry specifications](/docs/en-us/avatar/character-bodies/specifications.md#geometry). |
| <br>**Textures** | When texturing, confirm that your character's textures follow Roblox's [texture specifications](/docs/en-us/avatar/character-bodies/specifications.md#textures). |
| <br>**Rigging** | Use Blender's [posing tools](/docs/en-us/avatar/character-bodies/test-blender.md#skinning-data) to check the rigging and skinning quality of your character's body.<br> |
| <br>**Face Animation** | Confirm that your character's [FACS data](/docs/en-us/avatar/character-bodies/test-blender.md#facial-animation-data) is present and correctly configured. |
| <br>**Cage Mesh** | Manually verify that your cage meshes completely and tightly cover your character model and follow Roblox's [outer cage specifications](/docs/en-us/avatar/character-bodies/specifications.md#outer-cages). |
| <br>**Attachments** | Manually verify that your attachment points are correctly positioned and follow Roblox's [attachment specifications](/docs/en-us/avatar/character-bodies/specifications.md#attachments). |

#### Studio Tests

> **Info:** Roblox provides an uncopylocked testing place file that includes quick access to various environments and testing features. For more information, see [Test character bodies in Studio](/docs/en-us/avatar/character-bodies/test-studio.md).

| Component | Testing recommendations |
| --- | --- |
| <br>**Body Parts** | Test how your character's body parts [move and animate](/docs/en-us/avatar/character-bodies/test-studio.md#movement-and-animation) in the 3D space. |
| <br>**Textures** | Test how your character looks in [various lighting environments and skin tone colors](/docs/en-us/avatar/character-bodies/test-studio.md#lighting-and-color). |
| <br>**Rigging** | Use [animations and testing environments](/docs/en-us/avatar/character-bodies/test-studio.md#movement-and-animation) to verify your character's rigging, skinning, and movement quality. |
| <br>**Face Animation** | [Cycle through various facial animations](/docs/en-us/avatar/character-bodies/test-studio.md#movement-and-animation) to ensure your character can perform common expressions. |
| <br>**Cage Mesh** | [Equip various clothing items](/docs/en-us/avatar/character-bodies/test-studio.md#clothing-and-accessories) to check for fit and for any unexpected cosmetic issues. |
| <br>**Attachments** | [Equip various accessory items](/docs/en-us/avatar/character-bodies/test-studio.md#clothing-and-accessories) to verify rigid accessory placement and orientation. |
