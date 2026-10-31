---
title: "Assemblies"
url: /docs/en-us/physics/assemblies
last_updated: 2026-10-30T19:55:46Z
description: "Explains physical assemblies and how they behave in Roblox's rigid body physics engine."
---

# Assemblies

An **assembly** is one or more [parts](/docs/en-us/parts.md) welded by a rigid `Class.WeldConstraint|WeldConstraint` or connected through movable joints, like `Class.Motor6D|Motor6Ds`. You can group an assembly of parts in a [model](/docs/en-us/parts/models.md) container to quickly organize the parts and related objects as a single asset.

![A light blue cube against a dark blue background that represents an assembly of 1 part.](../assets/physics/assemblies/Assembly-Example-Block.png)_1 assembly; 1 part_

![A humanoid character model against a dark blue background that represents an assembly of 18 parts.](../assets/physics/assemblies/Assembly-Example-Avatar.png)_1 assembly; 18 parts_

![A pirate that represents an assemble of 179 parts.](../assets/physics/assemblies/Assembly-Example-Ship.png)_1 assembly; 179 parts_

From a physics perspective, an assembly is considered a single **rigid body**, meaning no force can push or pull the connected parts from each other, and they will move as a single unit. All forces applied to a specific `Class.BasePart` are applied to its assembly — for instance, `Class.BasePart:ApplyImpulse()` applies impulse to the assembly at `Class.BasePart.AssemblyCenterOfMass`.

> **Info:** The joints that combine multiple parts into assemblies are only active in the `Class.Workspace` or another `Class.WorldModel` instance. If the parts are stored elsewhere, all of the welds/connections that combine parts into assemblies will be non-functional.
> **Success:** To view colored outlines around parts in order to visualize single rigid body assemblies, toggle on **Assemblies** from the [Visualization Options](/docs/en-us/studio/overview.md#visualization-options) widget in the upper‑right corner of the 3D viewport.
## Assembly properties

The following `Class.BasePart` properties show data regarding its assembly. Their values will be the same for any part in the same assembly, so it doesn't matter which part you use.

| Property | Description |
| --- | --- |
| `Class.BasePart.AssemblyLinearVelocity` | The linear velocity vector of the part's assembly. Setting the velocity directly may lead to unrealistic motion, so usage of a `Class.VectorForce` or `Class.LinearVelocity` constraint is preferred, or `Class.BasePart:ApplyImpulse()` for an instantaneous change in linear velocity. |
| `Class.BasePart.AssemblyAngularVelocity` | The angular velocity vector of the part's assembly. Setting the velocity directly may lead to unrealistic motion, so usage of a `Class.Torque` or `Class.AngularVelocity` constraint is preferred, or `Class.BasePart:ApplyAngularImpulse()` for an instantaneous change in angular velocity. |
| `Class.BasePart.AssemblyCenterOfMass` | A read-only position calculated via the mass and position of all the parts in the assembly. A force applied to the center of mass will not cause angular acceleration, only linear. |
| `Class.BasePart.AssemblyMass` | The sum of the `Class.BasePart.Mass` of all parts in the assembly. If the assembly has an anchored part, the assembly's mass is considered infinite. |
| `Class.BasePart.AssemblyRootPart` | The part automatically chosen to represent the assembly's [root part](#assembly-root-part). |

## Assembly root part

Every assembly has a **root part** indicated by its `Class.BasePart.AssemblyRootPart|AssemblyRootPart` property. This is the part that doesn't move when `Class.Motor6D` transforms are updated, as well as the part used to keep consistent physics replication and network ownership.

You cannot explicitly set the root part, but the following factors affect probability from highest to lowest:

An `Class.BasePart.Anchored|Anchored` part will always be assigned as the root part.

Parts with `Class.BasePart.Massless|Massless` set to **false** (default) take precedence.

Higher `Class.BasePart.RootPriority|RootPriority` values take precedence.

Precedence based on the part's size (largest face area), with multipliers for specific part types. `Class.Seat|Seats` and `Class.VehicleSeat|VehicleSeats` receive the highest multiplier, followed by parts named **HumanoidRootPart**, then parts named **Torso**.

## Anchoring behavior

When one of an assembly's parts is anchored, that part becomes the root part and all of the other parts become implicitly anchored with it. The following sequence illustrates this behavior.

1. Below, four parts are welded together with `Class.WeldConstraint|WeldConstraints` (green bars) to form a single assembly, as indicated by the matching colored outlines._Four parts welded to become a single assembly_
2. If just **one** part in the assembly is anchored, the assembly will not change, other than the root part potentially changing (the anchored part always has the highest [priority](#assembly-root-part) for becoming the root part)._Anchored part (as indicated with an anchor icon) becomes the new root part_
3. If more than one part is anchored, the assembly will **split**. Below, both the left and top parts are anchored, so the original assembly splits into two assemblies as shown by the colored outlines. Also, the `Class.WeldConstraint` between the two assemblies deactivates, since you cannot have an active weld between two anchored assemblies._Two assemblies with anchored parts as their respective root parts_
  > **Warning:** If you want to anchor all parts in an assembly, you only need to anchor the assembly's root part. Anchoring all parts is actually less performant, as it creates more assemblies.
