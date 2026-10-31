---
title: "FACS poses reference"
url: /docs/en-us/avatar/dynamic-heads/facs-poses-reference
last_updated: 2026-10-30T19:55:37Z
description: "The Facial Action Coding System (FACS) ensures that all face animations have a common pose reference and can create similar face animations."
---

# FACS poses reference

The [Facial Action Coding System](https://en.wikipedia.org/wiki/Facial_Action_Coding_System) (FACS) is a comprehensive, anatomically-based system for describing all visually discernible facial movement. This system breaks down all facial expressions into individual types of muscle movement, such as `LeftEyeClosed` or `MouthLeft`. You can [configure](/docs/en-us/art/characters/facial-animation/create-basic-heads.md#pose-the-joints) and store these muscle movements, or **poses**, within the head model through a third-party modeling software, such as [Blender](https://www.blender.org) or [Maya](https://www.autodesk.com/products/maya/overview). When you import the head model into Studio, you can then access and [animate](/docs/en-us/art/characters/facial-animation/animate-heads.md) these poses to create lively facial expressions.

The following is a list of 50 base poses that you can use in Roblox to portray a wide range of face emotions. Except for the first neutral pose, the order of poses you save to your character model doesn't matter since this information is set during the [mapping](/docs/en-us/art/characters/facial-animation/create-basic-heads.md#map-each-pose) process as a custom property.

> **Warning:** If you intend to publish your avatar to the Marketplace, your avatar head must include the required [17 facial base poses](/docs/en-us/avatar/dynamic-heads/specifications.md#facs-poses). Marketplace validation rejects assets that do not include these 17 required base poses.

You can combine multiple FACS base poses together in one animation frame to create complex facial expressions. However, some combinations of poses might collide unless you also add a [corrective](/docs/en-us/art/characters/facial-animation/create-basic-heads.md#combination-poses) to their full default values.

## LeftEyeClosed

> **Warning:** If publishing to the Marketplace, your avatar asset must include this pose.

`Class.FaceControls.LeftEyeClosed|LeftEyeClosed` closes the character's left eyelid.

## RightEyeClosed

> **Warning:** If publishing to the Marketplace, your avatar asset must include this pose.

`Class.FaceControls.RightEyeClosed|RightEyeClosed` closes the character's right eyelid.

## EyesLookDown

> **Warning:** If publishing to the Marketplace, your avatar asset must include this pose.

`Class.FaceControls.EyesLookDown|EyesLookDown` makes the eyes gaze down.

## JawDrop

> **Warning:** If publishing to the Marketplace, your avatar asset must include this pose.

`Class.FaceControls.JawDrop|JawDrop` lowers the jaw downward, opening the mouth.

## Pucker

> **Warning:** If publishing to the Marketplace, your avatar asset must include this pose.

`Class.FaceControls.Pucker|Pucker` makes a kiss-like shape with the mouth.

## LeftLipCornerPuller

> **Warning:** If publishing to the Marketplace, your avatar asset must include this pose.

`Class.FaceControls.LeftLipCornerPuller|LeftLipCornerPuller` raises the corners of the mouth upwards in a smile.

## RightLipCornerPuller

> **Warning:** If publishing to the Marketplace, your avatar asset must include this pose.

`Class.FaceControls.RightLipCornerPuller|RightLipCornerPuller` raises the corners of the mouth upwards in a smile.

## ChinRaiser

> **Warning:** If publishing to the Marketplace, your avatar asset must include this pose.

`Class.FaceControls.ChinRaiser|ChinRaiser` raises the chin up; moves the lower lip upwards.

When you use `Class.FaceControls.ChinRaiser|ChinRaiser` and the character's mouth is closed, the character's lower lip collides with their upper lip. When you need to keep the mouth closed while raising the chin, use [`ChinRaiserUpperLip`](#chinraiserupperlip) and `Class.FaceControls.ChinRaiser|ChinRaiser` together to raise both the lower and upper lip, and avoid a collision. Note that if you use this method, you must set both `Class.FaceControls.ChinRaiser|ChinRaiser` and [`ChinRaiserUpperLip`](#chinraiserupperlip) to the same value so the lips move the same distance upwards.

## ChinRaiserUpperLip

> **Warning:** If publishing to the Marketplace, your avatar asset must include this pose.

`Class.FaceControls.ChinRaiserUpperLip|ChinRaiserUpperLip` raises the upper lip up when ChinRaiser is engaged and it is touching the upper lip.

## LeftCheekRaiser

> **Warning:** If publishing to the Marketplace, your avatar asset must include this pose.

`Class.FaceControls.LeftCheekRaiser|LeftCheekRaiser` squints the character's left eye.

## RightCheekRaiser

> **Warning:** If publishing to the Marketplace, your avatar asset must include this pose.

`Class.FaceControls.RightCheekRaiser|RightCheekRaiser` squints the character's right eye.

## LeftInnerBrowRaiser

> **Warning:** If publishing to the Marketplace, your avatar asset must include this pose.

`Class.FaceControls.LeftInnerBrowRaiser|LeftInnerBrowRaiser` raises the interior half of the character's left brow upwards.

## RightInnerBrowRaiser

> **Warning:** If publishing to the Marketplace, your avatar asset must include this pose.

`Class.FaceControls.RightInnerBrowRaiser|RightInnerBrowRaiser` raises the interior half of the character's right brow upwards.

## LeftLipCornerDown

> **Warning:** If publishing to the Marketplace, your avatar asset must include this pose.

`Class.FaceControls.LeftLipCornerDown|LeftLipCornerDown` lowers the corners of the mouth downwards in a frown.

## RightLipCornerDown

> **Warning:** If publishing to the Marketplace, your avatar asset must include this pose.

`Class.FaceControls.RightLipCornerDown|RightLipCornerDown` lowers the corners of the mouth downwards in a frown.

## LeftLowerLipDepressor

> **Warning:** If publishing to the Marketplace, your avatar asset must include this pose.

`Class.FaceControls.LeftLowerLipDepressor|LeftLowerLipDepressor` lowers the lower lip downwards away from the upper lip, revealing the lower teeth.

## RightLowerLipDepressor

> **Warning:** If publishing to the Marketplace, your avatar asset must include this pose.

`Class.FaceControls.RightLowerLipDepressor|RightLowerLipDepressor` lowers the lower lip down away from the upper lip revealing the lower teeth.

## EyesLookLeft

`Class.FaceControls.EyesLookLeft|EyesLookLeft` makes the eyes gaze left.

## EyesLookRight

`Class.FaceControls.EyesLookRight|EyesLookRight` makes the eyes gaze right.

## EyesLookUp

`Class.FaceControls.EyesLookUp|EyesLookUp` makes the eyes gaze up.

## LeftLipStretcher

`Class.FaceControls.LeftLipStretcher|LeftLipStretcher` stretches the corners of the mouth apart.

## LeftUpperLipRaiser

`Class.FaceControls.LeftUpperLipRaiser|LeftUpperLipRaiser` raises the character's left upper lip away from the lower lip revealing the upper teeth.

## LipsTogether

`Class.FaceControls.LipsTogether|LipsTogether` brings the character's lips together. However, if the character's mouth is closed, their lips are already together and they collide.

This pose's main use case is in connection with the [`JawDrop`](#jawdrop) property. If you set [`JawDrop`](#jawdrop) and `Class.FaceControls.LipsTogether|LipsTogether` to 100% of their default values, the character's lips stay together as the jaw drops.

In addition, if you set [`JawDrop`](#jawdrop) to 100% of its default value, and ease `Class.FaceControls.LipsTogether|LipsTogether` in and out of 100% of its default value, the character's lips open and close.

## RightLipStretcher

`Class.FaceControls.RightLipStretcher|RightLipStretcher` stretches the corners of the mouth apart.

## RightUpperLipRaiser

`Class.FaceControls.RightUpperLipRaiser|RightUpperLipRaiser` raises the right upper lip away from the lower lip, revealing the upper teeth.

## FlatPucker

`Class.FaceControls.FlatPucker|FlatPucker` brings the corners of the mouth inward and presses the lips back against the teeth. This pose is also known as lip tightener.

## Funneler

`Class.FaceControls.Funneler|Funneler` makes an 'O' shape with the mouth.

## LowerLipSuck

`Class.FaceControls.LowerLipSuck|LowerLipSuck` rolls the lower lip up over the teeth.

## LipPresser

`Class.FaceControls.LipPresser|LipPresser` presses the lips together.

## MouthLeft

`Class.FaceControls.MouthLeft|MouthLeft` moves the mouth to the character's left. This property doesn't move the character's jaw, teeth, or tongue, only their mouth. If you want to move those additional facial features, use [`JawLeft`](#jawleft) instead.

## MouthRight

`Class.FaceControls.MouthRight|MouthRight` moves the mouth to the character's right. This property doesn't move the character's jaw, teeth, or tongue to the right, only their mouth. If you want to move those additional facial features, use [`JawRight`](#jawright) instead.

## UpperLipSuck

`Class.FaceControls.UpperLipSuck|UpperLipSuck` rolls the upper lip around the teeth.

## LeftCheekPuff

`Class.FaceControls.LeftCheekPuff|LeftCheekPuff` puffs up the character's left cheek.

## LeftDimpler

`Class.FaceControls.LeftDimpler|LeftDimpler` moves the corners of the left side of the mouth back toward the teeth.

## RightCheekPuff

`Class.FaceControls.RightCheekPuff|RightCheekPuff` puffs up the character's right cheek.

## RightDimpler

`Class.FaceControls.RightDimpler|RightDimpler` moves the corners of the right side of the mouth back toward the teeth.

## JawLeft

`Class.FaceControls.JawLeft|JawLeft` moves the character's jaw, teeth, tongue, and lower lip to their left. If you just want to move the character's mouth to their left, use [`MouthLeft`](#mouthleft) instead.

## JawRight

`Class.FaceControls.JawRight|JawRight` moves the character's jaw, teeth, tongue, and lower lip to their right. If you just want to move the character's mouth to their right, use [`MouthRight`](#mouthright) instead.

## Corrugator

`Class.FaceControls.Corrugator|Corrugator` brings the left and right brows inward together.

## LeftBrowLowerer

`Class.FaceControls.LeftBrowLowerer|LeftBrowLowerer` lowers the character's left brow down.

## LeftOuterBrowRaiser

`Class.FaceControls.LeftOuterBrowRaiser|LeftOuterBrowRaiser` raises the outer part of the character's left brow upwards.

## LeftNoseWrinkler

`Class.FaceControls.LeftNoseWrinkler|LeftNoseWrinkler` raises the character's left nostril, pulls the brow down slightly, and wrinkles the left side of the nose.

## RightBrowLowerer

`Class.FaceControls.RightBrowLowerer|RightBrowLowerer` lowers the character's right brow down.

## RightOuterBrowRaiser

`Class.FaceControls.RightOuterBrowRaiser|RightOuterBrowRaiser` raises the outer part of the character's right brow upwards.

## RightNoseWrinkler

`Class.FaceControls.RightNoseWrinkler|RightNoseWrinkler` raises the character's right nostril, pulls the brow down slightly, and wrinkles the right side of the nose.

## LeftEyeUpperLidRaiser

`Class.FaceControls.LeftEyeUpperLidRaiser|LeftEyeUpperLidRaiser` raises the character's left eyelid upwards to reveal more of the eye white above the iris.

## RightEyeUpperLidRaiser

`Class.FaceControls.RightEyeUpperLidRaiser|RightEyeUpperLidRaiser` raises the character's right eyelid upwards to reveal more of the eye white above the iris.

## TongueDown

`Class.FaceControls.TongueDown|TongueDown` bends the tongue down. This pose is only visible if you combine it with [`TongueOut`](#tongueout), otherwise the tongue only bends down within the character's mouth.

## TongueOut

`Class.FaceControls.TongueOut|TongueOut` sticks the tip of the tongue out of the mouth.

## TongueUp

`Class.FaceControls.TongueUp|TongueUp` bends the tongue up. This pose is only visible if you combine it with [`TongueOut`](#tongueout), otherwise the tongue only bends up within the character's mouth.
