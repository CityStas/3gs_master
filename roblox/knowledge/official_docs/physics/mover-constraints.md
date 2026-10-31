---
title: "Mover constraints"
url: /docs/en-us/physics/mover-constraints
last_updated: 2026-10-30T19:55:47Z
description: "Mover constraints apply force or torque to move one or more assemblies."
---

# Mover constraints

The physics engine includes the following `Class.Constraint|Constraints` that apply force or torque to move one or more assemblies. In addition, various [mechanical constraints](/docs/en-us/physics/mechanical-constraints.md) are available which behave as conceptual mechanical connections, including hinges, springs, ropes, and more.

[Linear Velocity](/docs/en-us/physics/constraints/linear-velocity.md)

_`Class.LinearVelocity` applies force on an assembly to maintain a constant velocity along a 3D vector, line, or 2D plane_

[Angular Velocity](/docs/en-us/physics/constraints/angular-velocity.md)

_`Class.AngularVelocity` applies torque on an assembly to maintain a constant angular velocity_

[Align Position](/docs/en-us/physics/constraints/align-position.md)

_`Class.AlignPosition` applies force to move two attachments together, or to move one attachment to a goal position_

[Align Orientation](/docs/en-us/physics/constraints/align-orientation.md)

_`Class.AlignOrientation` applies torque to align two attachments, or to align one attachment with a goal orientation_

[Vector Force](/docs/en-us/physics/constraints/vector-force.md)

_`Class.VectorForce` applies constant linear force on an assembly_

[Torque](/docs/en-us/physics/constraints/torque.md)

_`Class.Torque` applies constant torque on an assembly from its center of mass_

[Line Force](/docs/en-us/physics/constraints/line-force.md)

_`Class.LineForce` applies force along the theoretical line connecting its two attachments_

[Animation Constraint](/docs/en-us/physics/constraints/animation.md)

_`Class.AnimationConstraint` constrains its `Class.Attachment|Attachments` by an offset transform `Datatype.CFrame`._

## Constraint visualization

To accurately visualize constraints in Studio, you can toggle the following from the **View** menu or through the respective shortcut:

- **Show Welds** (`Alt``W` or `⌥``W`) — Show `Class.WeldConstraint|WeldConstraints` separately from the visualization of other constraints.
- **Show Constraint Details** (`Alt``D` or `⌥``D`) — Show complete visual details of non-weld constraints.

> **Success:** In addition to the above visualization, you can view colored outlines around mechanisms (groups of parts that share simulation step and [network ownership](/docs/en-us/physics/network-ownership.md)) by toggling on **Mechanisms** from the [Visualization Options](/docs/en-us/studio/overview.md#visualization-options) widget in the upper‑right corner of the 3D viewport.
## Create constraints

Mover constraints typically connect one or two `Class.Attachment|Attachments` or `Class.Bone|Bones`. When connected to `Class.Bone|Bones`, the constraint will use their animated position and orientation.

To create a mechanical constraint, you can either insert one from the **Constraint** picker/button or through the [Explorer](/docs/en-us/studio/explorer.md) window.

#### Constraint Picker

1. In Studio's **Model** tab toolbar, click‑hold over the small corner arrow on a constraint button to open its picker menu, then select the desired constraint.![Constraint pickers indicated in Studio's toolbar](../assets/studio/general/Toolbar-Constraint-Pickers.png)
2. In the 3D viewport, hover over any `Class.Part` or `Class.MeshPart` and click to add a new `Class.Attachment` to the part at the visualized point. Alternatively, hover over and click an existing `Class.Attachment` or `Class.Bone` to use it for the constraint.
3. Some mover constraints utilize or support a **secondary** attachment in their functionality, so the tool might prompt you to repeat the previous step on another `Class.Part`, `Class.MeshPart`, or `Class.Attachment`, or `Class.Bone`.![AngularVelocity using one attachment](../assets/physics/constraints/Constraint-AngularVelocity-Labeled.jpg)_[AngularVelocity](/docs/en-us/physics/constraints/angular-velocity.md) using one attachment_![AlignPosition using two attachments](../assets/physics/constraints/Constraint-AlignPosition-Labeled.jpg)_[AlignPosition](/docs/en-us/physics/constraints/align-position.md) using two attachments_

#### Explorer

1. In the [Explorer](/docs/en-us/studio/explorer.md) hierarchy, hover over the intended parent, click the **⊕** button, and insert the desired constraint from the dropdown menu, such as a [LinearVelocity](/docs/en-us/physics/constraints/linear-velocity.md) constraint.![New LinearVelocity in Explorer window.](../assets/studio/explorer/LinearVelocity.png)
2. With the new constraint selected, locate its currently empty **Attachment0** property in the [Properties](/docs/en-us/studio/properties.md) window.![Constraint's Attachment0 property highlighted in Properties window.](../assets/studio/properties/LinearVelocity-Attachment0-Unassigned.png)
3. Link the **Attachment0** property to an `Class.Attachment` or `Class.Bone` in two consecutive steps:
  1. In the [Properties](/docs/en-us/studio/properties.md) window, click in the **Attachment0** row to reveal the selection cursor.
  2. In the [Explorer](/docs/en-us/studio/explorer.md) hierarchy, click on the target `Class.Attachment` or `Class.Bone`.![Mouse pointer hovering over Attachment0 property in Properties window.](../assets/physics/constraints/LinearVelocity-Link-Attachment0-1.png)![Target attachment indicated in Explorer window.](../assets/physics/constraints/LinearVelocity-Link-Attachment0-2.png)
4. Some mover constraints use or support a **secondary** `Class.Attachment` or `Class.Bone` in their functionality. If necessary, repeat the previous step on the **Attachment1** property in the **Properties** window. For instance:
  - By default, [AlignPosition](/docs/en-us/physics/constraints/align-position.md) and [AlignOrientation](/docs/en-us/physics/constraints/align-orientation.md) align their primary attachment (**Attachment0**) with a secondary attachment (**Attachment1**).
  - [LineForce](/docs/en-us/physics/constraints/line-force.md) **requires** two attachments to apply force along the theoretical line connecting them.

## Physical simulation

To simulate physics while [moving](/docs/en-us/parts.md#move) or [rotating](/docs/en-us/parts.md#rotate) parts, you can switch from **Geometric** mode to **Physical** mode in Studio's toolbar, effectively forcing parts to obey physical limitations. For example, if two parts are attached by a `Class.RopeConstraint` and you drag one part around the scene, the other part will follow as the rope becomes taut.

## Legacy mover conversion

If your game relies on legacy `Class.BodyMover`‑based constraints, review the following notes when converting to modern mover constraints.

**`BodyPosition`  ⟩  `AlignPosition`**

`Class.AlignPosition` satisfies the majority of use cases covered by the deprecated `Class.BodyPosition` mover. To sync with how the legacy mover treated each component independently and allowed a different force along each dimension, the `Class.AlignPosition.ForceLimitMode|ForceLimitMode` property of `Class.AlignPosition` allows the constraint to operate in `Enum.ForceLimitMode|Magnitude` mode or `Enum.ForceLimitMode|PerAxis` mode:

- In `Enum.ForceLimitMode|Magnitude` mode, the existing behavior is preserved and `Class.AlignPosition.MaxForce|MaxForce` is interpreted as a magnitude.
- In `Enum.ForceLimitMode|PerAxis` mode, the force along each axis can be specified independently. Because the maximum force is specified as a vector, the reference frame of the force can also be specified through the `Class.AlignPosition.ForceRelativeTo|ForceRelativeTo` property with `Enum.ActuatorRelativeTo|World`, `Enum.ActuatorRelativeTo|Attachment0`, and `Enum.ActuatorRelativeTo|Attachment1` options. Additionally, the formulation for the internal controller is modified to match that of `Class.BodyPosition`.

**`BodyGyro`  ⟩  `AlignOrientation`**

`Class.AlignOrientation` satisfies the majority of use cases covered by the deprecated `Class.BodyGyro` mover. The `Class.AlignOrientation.AlignType|AlignType` modes of `Class.AlignOrientation` provide sufficient freedom for most applications and the combination of multiple constraints can replicate the vector torque limit. Additionally, the `Enum.AlignType|PrimaryAxisLookAt` mode forces the primary axis of the constraint's first attachment (`Class.AlignOrientation.Attachment0|Attachment0`) to always point towards the second attachment (`Class.AlignOrientation.Attachment1|Attachment1`), making it a lot easier to add things such as motion tracking security cameras or guided missiles.

**`BodyVelocity`  ⟩  `LinearVelocity`**

`Class.LinearVelocity` satisfies the majority of use cases covered by the deprecated `Class.BodyVelocity` mover. Although the legacy mover allows for a `Class.BodyVelocity.MaxForce|MaxForce` vector, the typical application of that vector force was to zero a particular component, allowing the constraint to be disabled along that dimension. `Class.LinearVelocity` achieves a similar effect by operating in distinct `Class.LinearVelocity.VelocityConstraintMode|VelocityConstraintMode` modes that corresponded to one (`Enum.VelocityConstraintMode|Line`), two (`Enum.VelocityConstraintMode|Plane`), and three (`Enum.VelocityConstraintMode|Vector`) dimensions.

Additionally, the `Class.LinearVelocity.ForceLimitMode|ForceLimitMode` property with the option of `Enum.ForceLimitMode|PerAxis` accommodates any applications of the vector force with all non‑zero components, such as an increase in the force along a single axis to counteract gravity.

**`BodyAngularVelocity`  ⟩  `AngularVelocity`**

Although `Class.AngularVelocity` has some discrepancies with the deprecated `Class.BodyAngularVelocity` mover, specific cases related to those discrepancies have not been highlighted by the community, nor internally.

As a separate improvement, `Class.AngularVelocity` works with `Class.Attachment|Attachments` and the `Class.AngularVelocity.RelativeTo|RelativeTo` property lets you specify the `Datatype.CFrame` in which the force is specified, for example `Enum.ActuatorRelativeTo|World` or `Enum.ActuatorRelativeTo|Attachment1`.

**`BodyForce`/`BodyThrust`  ⟩  `VectorForce`**

`Class.VectorForce` satisfies all use cases offered by the deprecated `Class.BodyForce` and `Class.BodyThrust` movers. The modern constraint works with `Class.Attachment|Attachments` and its `Class.VectorForce.RelativeTo|RelativeTo` property lets you apply force to a relative offset from center, similar to how `Class.BodyThrust.Location` worked.

**`RocketPropulsion`  ⟩  `LineForce`/`AlignOrientation`**

A combination of `Class.LineForce` and `Class.AlignOrientation` satisfies the majority of use cases covered by the deprecated `Class.RocketPropulsion` mover. In the example of a guided missile, `Class.LineForce` can be used to control the "follow target" behavior of `Class.RocketPropulsion` while `Class.AlignOrientation` and its `Class.AlignOrientation.LookAtPosition|LookAtPosition` property can be used to control the "face target" behavior.
