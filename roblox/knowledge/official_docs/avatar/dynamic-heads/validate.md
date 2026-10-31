---
title: "Dynamic head validation"
url: /docs/en-us/avatar/dynamic-heads/validate
last_updated: 2026-10-30T19:55:37Z
description: "In-depth details on how Roblox validates head assets"
---

# Dynamic head validation

> **Info:** This content is for creators who intend to create dynamic heads designated for the Marketplace, or any character heads that support assets from the Marketplace.

Roblox runs a rigorous validation to ensure each asset that you upload to the Marketplace is compatible with all other assets on the Marketplace. For dynamic heads, validation primarily ensures that the head asset includes:

- A correctly **configured outer cage** to wear clothing and accessories.
- Correctly configured **facial animation poses** to perform basic universal expressions, such as blinking and smiling.

The primary validation check for dynamic heads [uses the cage to detect facial animation](#facial-animation-detection). See below for a reference of how validation processes, as well as [common issues](#common-issues).

> **Warning:** Validation also checks for other issues, such as poor caging or missing required FACS poses. For more information, see [common issues](#common-issues).
> **Info:**[Avatar Setup](/docs/en-us/avatar-setup.md) automatically generates components for your avatar characters, **including the head cage and facial animation** required for the Marketplace. You can save time by submitting character models without avatar components into Avatar Setup, then modifying the output. If necessary, you can download your output as a `.gltf`, then adjust the FACS or cage data in your third-party modeling tool.
>
> For issues or feedback regarding Avatar Setup, submit a [bug report](https://devforum.roblox.com/c/bug-reports/10).
## Facial animation detection

One of the primary dynamic head validation checks verifies if your head asset has **visually discernible** animations. To achieve this, the validation tool uses the head cage to "project" [facial landmarks](#landmark-projection) onto your base mesh.

After these landmarks are created, validation [tests various face animation poses](#test-face-animations) to ensure that these landmarks move and deform appropriately. Validation succeeds when it detects appropriate movement of the landmarks for eyes closed, mouth open, and basic happy/sad expressions.

Failure to either assign landmarks onto the base mesh, or failure to deform landmarks appropriately can occur for several reasons. For more information, see [common issues](#common-issues).

### Landmark projection

Validation uses the head cage to project landmarks onto the head mesh. This helps Roblox establish where the eyes and mouth are and helps guide the facial animation test.

_Cage mesh: Specific vertices of the cage mark eyes and mouth._

_Roblox validation projects these points onto the head mesh._

_ Head mesh: All landmarks projected from cage mesh to head mesh._

> **Success:** Once validation verifies that projection is successful and all landmarks established onto the head mesh, it can move onto testing facial animations.
### Test face animations

Now that the validation system knows where to check for the eyes and mouth, the validation checks for facial animations to ensure that the following basic actions are possible:

- Left and right eyes can close
- Mouth can open
- Basic happy and sad expressions

> **Info:** For a full list of the minimum FACS poses your dynamic heads need to pass validation, see [Dynamic head specifications - FACS poses](/docs/en-us/avatar/dynamic-heads/specifications.md#facs-poses).

The validation looks for the **relative change in the landmarks**. For example, when testing for right eye closing (FACS pose: `RightEyeClosed`), validation checks if the landmarks move from their original neutral state accordingly.

_> **Success:** Face mesh with all projected landmarks applied from cage._

_> **Success:** Validation verifies that the right eye can close based off of displacement of landmarks._

## Common issues

Validation checks for several aspects of your head asset. If you are receiving an error related to dynamic head animation, use the following table for potential culprits:

| Issue | Potential fixes |
| --- | --- |
| The validation tool is **unable to successfully apply landmarks**.<br><br>See [Unable to project landmarks](#unable-to-project-landmarks). | - Verify that the **cage landmark vertices are positioned directly over the corresponding areas of the face**.<br><br>- Verify that the **cage is not intersecting with the head mesh**. Landmark projection expects the cage to be over the head mesh.<br><br>- **Check for any gaps, holes, or difficult surfaces** of the face where landmarks can fail to project. |
| The validation tool is able to apply landmarks, but **can not detect animation**.<br><br>See [Animations not displacing landmarks](#animations-not-displacing-landmarks). | - Verify that **landmarks are on the areas of the eyes and mouth that move during animation**.<br><br>- Verify that the **cage is not intersecting with the head mesh**. Landmark projection expects the cage to be over the head mesh.<br><br>- **If using separate meshes for eyeballs and mouthbags**, ensure that your landmarks are applied to the head mesh, not the eyeballs or mouthbag. This can be achieved by slightly widening the area where your cages project landmarks. |
| The validation tool doesn't detect [FACS animations](#animation-data-missing). | - Your head doesn't include FACS animation. Verify that your head includes FACS poses and mapping. |

### Unable to project landmarks

If validation is unable to apply the projection correctly onto the surface of the head, the validation fails. This often occurs if your **cage extends beyond your head mesh**, or if your head mesh has a **hole or gap** that prevents the application of the landmark. See the following examples:

_> **Error:** Cage **extends too far beyond the mesh** and the validation is unable to apply 3 landmarks to the base mesh._

_> **Error:** Base mesh has a **hollow gap** in the design, preventing validation from applying 3 landmarks to denote the eye area._

> **Success:** In both cases, adjusting the cage to allow the proper projection of landmarks to the base mesh would resolve this issue.
### Animations not displacing landmarks

In the case where landmarks are correctly applied to the base mesh and the base mesh includes FACS data, it's possible that the facial animations do not displace the landmarks enough to pass validation. See the following example:

_> **Warning:** Landmarks successfully established on base mesh, but are not near the expected regions._

_> **Error:** When testing animations, validation doesn't detect the expected change to the landmark regions._

> **Success:** In the example case, adjusting the cage to allow the proper projection of landmarks at the appropriate areas would resolve this issue.

There may also be cases where the landmarks are correct, but the animation itself does not alter the projected landscapes enough to pass validation. In these cases, fixing the animation and/or optimizing the cage could help the validation properly identify the facial animation.

### Animation data missing

Heads require [17 specific FACS poses](/docs/en-us/avatar/dynamic-heads/specifications.md#facs-poses) that are used to test the 5 basic actions. Regardless of landmarks or other FACS animations, validation immediately fails if the minimum 17 poses were not detected.

For information on how to pose and map dynamic heads, see [Create basic dynamic heads](/docs/en-us/art/characters/facial-animation/create-basic-heads.md).

## Working with non-humanoids

Some character models, typically non-humanoids, have unnatural or missing eyes and mouths. The most common case of this is the classic blocky features.

In this case, the cage still applies the expected landscapes to the head surface, and Roblox validates if facial animations correctly displace the facial animations.

_The cage for a blocky character applies landmarks to the surface of the head._

_Ensure that the landmarks are applied in areas where animation can effectively move the landmarks._

_Validation checks the displacement of the landmarks to verify facial animation. Make sure that your [FACS animations](/docs/en-us/avatar/dynamic-heads/specifications.md#facs-poses) properly affect the region where landmarks are applied._

In cases where eyes and mouths might be missing, the validation still projects landmarks and expects facial animation in those areas.

_Although this character doesn't have eyes or mouth, the cage still attempts to project landmarks for those features._

_In this example, the cage landmarks apply to the surface of this eye-less character head._

_Validation checks the displacement of the landmarks to verify facial animation. Make sure that your [FACS animations](/docs/en-us/avatar/dynamic-heads/specifications.md#facs-poses) properly affect the regions where the landmarks are applied._
