---
title: "Inverse Kinematics"
url: /docs/en-us/animation/inverse-kinematics
last_updated: 2026-10-30T19:55:32Z
description: "Inverse Kinematics is a technique in computer animation to make characters move and interact with their environment."
---

# Inverse Kinematics

[Inverse Kinematics](https://en.wikipedia.org/wiki/Inverse_kinematics) (IK) is a common technique in computer animation to efficiently make characters move and interact realistically with their environment. The process of creating a realistic movement for a character often requires many iterations and minor adjustments of the various joints. With IK, you can pose and animate multiple character parts by posing or adjusting a single object.

This animation technique can provide solutions to the following examples:

_Grab and pose a character's hand while automatically adjusting the related limbs, such as the wrist, elbow, and shoulder._

_Make a character's feet interact realistically on different surfaces and slopes._

_Grab and move a single target object to quickly create realistic interactions with your character and props._

## IKControl

You can use an `Class.IKControl` to procedurally add IK to your character rigs outside of the **Animation Editor**. Studio allows you to programmatically apply IK to all characters to create realistic movement and interactions in your game.

When adding an `Class.IKControl`, set the [required properties](#required-properties) correctly to avoid unexpected and unnatural animation results. As with all animation, [test your IKControls](#test-ikcontrols) to ensure that you achieve the desired behavior.

### Required properties

When adding a `Class.IKControl` to your character's `Class.Humanoid` or `Class.AnimationController`, you must set the following required properties to enable IK:

| Property | Description |
| --- | --- |
| `Class.IKControl.Type\|Type` | Specifies the behavior type of the IK control. See `Enum.IKControlType` for the list of behavior options. Common behavior types are `Position` or `Transform`. |
| `Class.IKControl.EndEffector\|EndEffector` | A `Class.BasePart` or `Class.Bone` in your character rig that tracks toward the `Class.IKControl.Target\|Target`. For example, you can set a **LeftHand** bone as a `Class.IKControl.EndEffector\|EndEffector` to reach a doorknob object set as the `Class.IKControl.Target\|Target`. |
| `Class.IKControl.Target\|Target` | The object the `Class.IKControl.EndEffector\|EndEffector` reaches or points toward. A `Class.IKControl.Target\|Target` can be any object with a world position. |
| `Class.IKControl.ChainRoot\|ChainRoot` | Defines the chain of `Class.BasePart\|BaseParts` or `Class.Bone\|Bones` that the `Class.IKControl` affects. All connected parts between the `Class.IKControl.ChainRoot\|ChainRoot` and the `Class.IKControl.EndEffector\|EndEffector` are affected by the `Class.IKControl` using the behavior type defined. <br><br> For example, if your character's **LeftHand** is set as the `Class.IKControl.Target\|Target`, you can apply IK to the entire left arm by setting `Class.IKControl.ChainRoot\|ChainRoot` to the **LeftUpperArm**. To apply IK just to the parts below the elbow, set `Class.IKControl.ChainRoot\|ChainRoot` to the **LeftLowerArm**. |

### Test IKControls

You can add and edit `Class.IKControl` programmatically or directly through the **Explorer**. You can even add and make changes to `Class.IKControl` during a Play test to quickly check how various properties affect a character's movements.

To quickly test your `Class.IKControl` using an `Class.Attachment` as a target:

1. From Studio's mezzanine, [initiate a playtest](/docs/en-us/studio/testing-modes.md#playtesting).
2. In the **Explorer** window, navigate to **Workspace** → your user's `Class.Model`. This `Class.Model` instance is named as your current Roblox account.
3. Click the **⊕** icon next to your character model's `HumanoidRootPart` and add an **Attachment**.
4. Select the **Attachment** and use the **Move** tool to position the object in front of your character in the viewport.
5. In the **Explorer** window, select the **⊕** icon next to your character's `Class.Humanoid` and add an **IKControl**.
6. Select the `Class.IKControl` and set the following property values in the **Properties** window:
  1. **Type**: Select `Transform` from the dropdown.
  2. **EndEffector**: Select your model's **LeftHand** `Class.MeshPart` in the **Explorer**.
  3. **Target**: Select the newly created **Attachment** object in the **Explorer**.
  4. **ChainRoot**: Select your model's **LeftUpperArm** `Class.MeshPart` in the **Explorer**._IKControl Properties__Explorer - Character Model_ Your character's left arm should now reach for the target `Class.Attachment`. You can experiment with moving the `Class.Attachment` or editing the `Class.IKControl` properties to achieve different results.

### Add constraints

You can use `Class.Constraint|Constraints` to restrict how joints can move when reaching its target. Constraints can ensure joints like the elbows and knees bend naturally, or to make the mechanical joints rotate in a specific orientation.

_Elbow bending unnaturally_

_Elbow bending correctly_

To add constraints to your character using `Class.IKControl`, your `Class.IKControl` and constraint must meet the following conditions:

- The attachments referenced in the constraint's `Class.Constraint.Attachment0|Attachment0`/`Class.Constraint.Attachment1|Attachment1` properties attaches to the same parts as the `Class.Motor6D` `Class.Motor6D.Part0|Part0`/`Class.Motor6D.Part1|Part1`.
- The relative positions of `Class.Constraint.Attachment0|Attachment0`/`Class.Constraint.Attachment1|Attachment1` must equal the corresponding positions of the `Class.Motor6D` `Class.Motor6D.C0|C0`/`Class.Motor6D.C1|C1` CFrames.
- The constraint and the IKControl share the same parent `Class.Model`.

The following instructions describe the process of adding a `Class.HingeConstraint` to restrict the rotation of a character's elbow and adding a `Class.BallSocketConstraint` to the wrist to limit the rotation angle.

#### Elbow

Characters with [R15 rigs](/docs/en-us/avatar/character-bodies/specifications.md#rigging) already include attachments in their joints that you can use to apply the elbow constraint. For the elbow, both the LeftUpperArm and the LeftLowerArm include a `LeftElbowRigAttachment`. Along with adding a constraint, you also need to add additional child attachments to each part's `LeftElbowRigAttachment` to specify which axis the elbow can rotate about.

To add the `Class.HingeConstraint` and child attachments:

1. In the **Explorer** window, locate your model's **LeftLowerArm** and click the **⊕ button**.
2. Add a **HingeConstraint** with the name `LeftElbowConstraint`.
3. In the **Explorer** window, navigate to the **LeftUpperArm.LeftElbowRigAttachment** and add an attachment:
  1. Click the **⊕ button** to add an **Attachment** with the name `LeftElbowConstraintAttachment0`.
  2. In the viewport, select the attachment and use the **Rotate tool** to rotate the attachment so the yellow **PrimaryAxis** is the axis of your elbow's expected rotation.
  3. Set the **LeftElbowConstraint.Attachment0** property to this new attachment.
4. In the **Explorer** window, navigate to your model's **LeftLowerArm.LeftElbowRigAttachment** add an attachment:
  1. Click the **⊕ button** and add an **Attachment** with the name `LeftElbowConstraintAttachment1`.
  2. Set the **LeftUpperArm.LeftElbowConstraint.Attachment1** property to this new attachment.
  3. Copy the **LeftElbowConstraintAttachment0.CFrameOrientation** property and paste it as the **LeftElbowConstraint.Attachment1.CFrameOrientation** value.

> **Error:** If you see a red arrow on the constraint's visualization, that means your attachment orientations are violating the hinge constraint. Go back and make sure the **LeftElbowConstraintAttachment1** has the same orientation as the **LeftElbowConstraintAttachment0**.

Test your IKControl to verify the elbow only rotates about its hinge axis:

#### Wrists

Even with the elbow constraint, the IKControl can still produce unrealistic poses with the wrists.

_The wrist bends unnaturally at certain orientations_

You can improve this by adding a `Class.BallSocketConstraint` to limit the rotation of the wrist. While this is similar to the process for adding a `Class.HingeConstraint` to the elbow, you can use the `Class.BallSocketConstraint.LimitsEnabled|LimitsEnabled` property on this constraint to further control the range of motion of the wrist.

To add a `Class.BallSocketConstraint` for the wrist:

1. In the **Explorer** window, locate your model's **LeftHand** and click the **⊕ button**.
  1. Add a **BallSocketConstraint** with the name `LeftWristConstraint`.
2. Locate your model's **LeftLowerArm.LeftWristRigAttachment** and add an attachment:
  1. Click the **⊕ button** and add an **Attachment** with the name `LeftWristConstraintAttachment0`.
  2. In the viewport, select the attachment and use the **Rotate tool** to rotate the attachment so the yellow PrimaryAxis points toward the model's fingertips.
  3. Set the **LeftWristConstraint.Attachment0** property to the new `LeftWristConstraintAttachment0`.
3. Locate your model's **LeftHand.LeftWristRigAttachment** and add an attachment:
  1. Click the **⊕ button** and add an **Attachment** with the name `LeftWristConstraintAttachment1`.
  2. Copy the **LeftWristConstraintAttachment0.CFrameOrientation** property and paste it as the **LeftWristConstraintAttachment1.CFrameOrientation** property.
  3. Set the **LeftWristConstraint.Attachment1** property to this new **LeftWristConstraintAttachment1**.
4. In the **Explorer** window, select the **LeftWristConstraint**.
5. In the **Properties** window, set the following:
  1. Enable **LimitsEnabled**.
  2. Set **UpperAngle** to `80`. This controls how much the constraint's axis can rotate, and 80 degrees is approximately how much the wrist should be able to bend.
6. Depending on your character you may want to tweak the direction the cone is pointing in. You can do this by using the **Rotate tool** to rotate the constraint's **Attachment0**.

When selecting the **LeftWristConstraint**, a green cone appears visualizing the wrist's range of motion.

With the constraint set up, test the IKControl with the hand pointing down in front of the character and the wrist should rotate and bend more realistically.
