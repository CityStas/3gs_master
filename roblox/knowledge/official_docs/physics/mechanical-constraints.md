---
title: "Mechanical constraints"
url: /docs/en-us/physics/mechanical-constraints
last_updated: 2026-10-30T19:55:47Z
description: "Mechanical constraints behave as conceptual mechanical connections such as hinges, springs, and motors."
---

# Mechanical constraints

The physics engine includes the following `Class.Constraint|Constraints` that behave as conceptual mechanical connections, including hinges, springs, ropes, and more. In addition, various [mover constraints](/docs/en-us/physics/mover-constraints.md) are available to exert directional or rotational force upon [assemblies](/docs/en-us/physics/assemblies.md).

[Ball Socket](/docs/en-us/physics/constraints/ball-socket.md)

_`Class.BallSocketConstraint` forces its two attachments into the same position and allows them to freely rotate about all three axes, with optional limits to restrict both tilt and twist_

[Hinge](/docs/en-us/physics/constraints/hinge.md)

_`Class.HingeConstraint` allows its two attachments to rotate about one axis, with optional assigned power for motor or servo behavior_

[Prismatic](/docs/en-us/physics/constraints/prismatic.md)

_`Class.PrismaticConstraint` allows two attachments to slide along one axis but not rotate, with optional assigned power for mechanisms like sliding doors and elevator platforms_

[Cylindrical](/docs/en-us/physics/constraints/cylindrical.md)

_`Class.CylindricalConstraint` allows its attachments to slide along one axis and rotate about another axis, with optional assigned angular and/or linear power_

[Spring](/docs/en-us/physics/constraints/spring.md)

_`Class.SpringConstraint` applies a force on its attachments based on spring and damper behavior, with an optional minimum/maximum length_

[Torsion Spring](/docs/en-us/physics/constraints/torsion-spring.md)

_`Class.TorsionSpringConstraint` applies torque based on a relative angle and relative angular velocity, in an attempt to bring two axes from two parts together_

[Universal](/docs/en-us/physics/constraints/universal.md)

_`Class.UniversalConstraint` ensures two axes on two assemblies remain perpendicular, useful for applications such as vehicle power transmission to rear drive shafts, robotics, and more_

[Rope](/docs/en-us/physics/constraints/rope.md)

_`Class.RopeConstraint` prevents two attachments from separating further than a defined length, with optional behavior as an extending or contracting winch_

[Rod](/docs/en-us/physics/constraints/rod.md)

_`Class.RodConstraint` keeps two attachments separated by a defined length, with optional limits on rotational tilt_

[Plane](/docs/en-us/physics/constraints/plane.md)

_`Class.PlaneConstraint` moves two attachments into a position/orientation along a plane, and both attachments remain free to translate and rotate unless otherwise constrained_

[Weld](/docs/en-us/physics/constraints/weld.md)

_`Class.WeldConstraint` connects two `Class.BasePart|BaseParts` and ensures they stay in the same relative position and orientation to each other, even if they are not touching_

[Rigid](/docs/en-us/physics/constraints/rigid.md)

_`Class.RigidConstraint` connects two `Class.Attachment|Attachments` or `Class.Bone|Bones` and ensures they stay in the same relative position/orientation to each other, even if they are not touching_

[No Collision](/docs/en-us/physics/constraints/no-collision.md)

_`Class.NoCollisionConstraint` prevents collisions between two specific parts, but those parts may still register collisions with the rest of the world_

## Constraint visualization

To accurately visualize constraints in Studio, you can toggle the following from the **View** menu or through the respective shortcut:

- **Show Welds** (`Alt``W` or `⌥``W`) — Show `Class.WeldConstraint|WeldConstraints` separately from the visualization of other constraints.
- **Show Constraint Details** (`Alt``D` or `⌥``D`) — Show complete visual details of non-weld constraints.

> **Success:** In addition to the above visualization, you can view colored outlines around mechanisms (groups of parts that share simulation step and [network ownership](/docs/en-us/physics/network-ownership.md)) by toggling on **Mechanisms** from the [Visualization Options](/docs/en-us/studio/overview.md#visualization-options) widget in the upper‑right corner of the 3D viewport.
## Create constraints

All mechanical constraints must connect one or two `Class.Attachment|Attachments` or `Class.Bone|Bones`, except for [WeldConstraint](/docs/en-us/physics/constraints/weld.md) and [NoCollisionConstraint](/docs/en-us/physics/constraints/no-collision.md). When connected to `Class.Bone|Bones`, the constraint will use their animated position and orientation.

To create a mechanical constraint, you can either insert one from the **Constraint** picker/button or through the [Explorer](/docs/en-us/studio/explorer.md) window.

#### Constraint Picker

1. In Studio's **Model** tab toolbar, click‑hold over the small corner arrow on a constraint button to open its picker menu, then select the desired constraint.![Constraint pickers indicated in Studio's toolbar](../assets/studio/general/Toolbar-Constraint-Pickers.png)
2. In the 3D viewport, hover over any `Class.Part` or `Class.MeshPart` and click to add a new `Class.Attachment` to the part at the visualized point. Alternatively, hover over and click an existing `Class.Attachment` or `Class.Bone` to use it for the constraint.
3. Most mechanical constraints require a **secondary** attachment in their functionality, so the tool will typically prompt you to repeat the previous step on another `Class.Part`, `Class.MeshPart`, `Class.Attachment`, or `Class.Bone`.![SpringConstraint connecting two attachments on separate blocks. One block is green and the other is blue.](../assets/physics/constraints/Creation-Diagram.jpg)_Completed [SpringConstraint](/docs/en-us/physics/constraints/spring.md) connecting two attachments_

#### Explorer

> **Info:** Note that [WeldConstraint](/docs/en-us/physics/constraints/weld.md) and [NoCollisionConstraint](/docs/en-us/physics/constraints/no-collision.md) do not utilize `Class.Attachment|Attachments` or `Class.Bone|Bones`, so their linking properties in the following steps are **Part0**/**Part1**, not **Attachment0**/**Attachment1**. Similarly, you'll need to select a `Class.Part` or `Class.MeshPart` to complete the link, not an `Class.Attachment` or `Class.Bone`.

1. In the [Explorer](/docs/en-us/studio/explorer.md) hierarchy, hover over the intended parent, click the **⊕** button, and insert the desired constraint from the dropdown menu, such as a [SpringConstraint](/docs/en-us/physics/constraints/spring.md).![New SpringConstraint in Explorer hierarchy.](../assets/studio/explorer/SpringConstraint.png)
2. With the new constraint selected, locate its currently empty **Attachment0** property in the [Properties](/docs/en-us/studio/properties.md) window.![Constraint's Attachment0 property highlighted in the Properties window.](../assets/studio/properties/SpringConstraint-Attachment0-Unassigned.png)
3. Link the **Attachment0** property to an `Class.Attachment` or `Class.Bone` in two consecutive steps:
  1. In the [Properties](/docs/en-us/studio/properties.md) window, click in the **Attachment0** row to reveal the selection cursor.
  2. In the [Explorer](/docs/en-us/studio/explorer.md) hierarchy, click on the target `Class.Attachment` or `Class.Bone`.![Mouse pointer hovering over Attachment0 property in the Properties window.](../assets/physics/constraints/SpringConstraint-Link-Attachment0-1.png)![Target attachment indicated in Explorer hierarchy.](../assets/physics/constraints/SpringConstraint-Link-Attachment0-2.png)
4. Most mechanical constraints require a **secondary** `Class.Attachment` or `Class.Bone` in their functionality. If necessary, repeat the previous step on the **Attachment1** property in the [Properties](/docs/en-us/studio/properties.md) window.

## Physical simulation

To simulate physics while [moving](/docs/en-us/parts.md#move) or [rotating](/docs/en-us/parts.md#rotate) parts, you can switch from **Geometric** mode to **Physical** mode in Studio's toolbar, effectively forcing parts to obey physical limitations. For example, if two parts are attached by a `Class.RopeConstraint` and you drag one part around the scene, the other part will follow as the rope becomes taut.
