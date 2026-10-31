---
title: "Sleep system"
url: /docs/en-us/physics/sleep-system
last_updated: 2026-10-30T19:55:47Z
description: "Explore how the sleep system automatically prevents unnecessary simulation of non-moving parts."
---

# Sleep system

Each [assembly](/docs/en-us/physics/assemblies.md) in the Roblox Engine corresponds to a single **rigid body**. The position and velocity of each rigid body describe where it's located and how fast it's moving, and one of the primary engine tasks is to update the positions and velocities of each assembly.

Assemblies can be connected together with [mechanical constraints](/docs/en-us/physics/mechanical-constraints.md) and [mover constraints](/docs/en-us/physics/mover-constraints.md) to form mechanisms such as cars or airplanes. As the number of assemblies and constraints in a mechanism increases, the time required to simulate the mechanism also increases. Fortunately, this increase is offset when the **sleep system** determines that the engine can skip simulation of non‑moving assemblies.

## Sleep states

Each assembly can be in one of three states: [awake](#awake), [sleeping](#sleeping), or [sleep‑checking](#sleep-checking).

### Awake

An **awake** assembly is moving or accelerating, and is therefore simulated. Assemblies enter this state from situations outlined in [sleeping](#sleeping) and [sleep‑checking](#sleep-checking), as well as [additional wake situations](#additional-wake-situations).

### Sleeping

A **sleeping** assembly is neither moving nor accelerating, and is therefore not simulated.

An assembly is determined to be non-moving by checking its **linear velocity** and **rotational velocity**. If its linear velocity is less than the [Linear Velocity](#threshold-reference) threshold and its rotational velocity is less than the [Rotational Velocity](#threshold-reference) threshold, the assembly is considered to be non-moving.

In some cases, simply checking for non-movement would cause an assembly to incorrectly enter the sleeping state. For example, if a ball is thrown straight up, its velocity approaches zero as it reaches its maximum height, making it a candidate to sleep and never fall back down. To handle such cases, the engine considers an assembly to be accelerating if its **linear acceleration** or **rotational acceleration** are greater than the [Linear Acceleration](#threshold-reference) and [Rotational Acceleration](#threshold-reference) thresholds, respectively, and will prevent the assembly from falling asleep.

> **Info:** If an assembly falls asleep when you expect it to remain awake, it's commonly because the assembly is moving too slowly. In addition to automatic checks outlined in [sleep‑checking](#sleep-checking) and [sleeping](#sleeping), you can forcibly wake up an assembly through the conditions outlined in [additional wake situations](#additional-wake-situations).
### Sleep-checking

A non-moving assembly that shares a constraint with at least one [awake](#awake) neighboring assembly is put into the **sleep-checking** state and is not simulated. On each worldstep, a sleep-checking assembly checks whether:

- Its **linear acceleration** is greater than the [Wake Linear Acceleration](#threshold-reference) threshold.
- Its **rotational acceleration** is greater than the [Wake Rotational Acceleration](#threshold-reference) threshold.
- A neighboring assembly's **linear velocity** is greater than the [Neighbor Linear Velocity](#threshold-reference) threshold.
- A neighboring assembly's **rotational velocity** is greater than the [Neighbor Rotational Velocity](#threshold-reference) threshold.

If any of these conditions is true, or under any of the [additional wake situations](#additional-wake-situations), the sleep-checking assembly enters the [awake](#awake) state.

## Threshold reference

The following table provides the various velocity and acceleration thresholds used to determine if an assembly is moving or accelerating.

| Threshold | Value | State change |
| --- | --- | --- |
| Linear Velocity | 0.33 studs/s | [awake](#awake) ⟩ [sleeping](#sleeping) |
| Rotational Velocity | 0.42 studs/s | [awake](#awake) ⟩ [sleeping](#sleeping) |
| Linear Acceleration | 0.24 studs/s² | [awake](#awake) ⟩ [sleeping](#sleeping) |
| Rotational Acceleration | 0.24 studs/s² | [awake](#awake) ⟩ [sleeping](#sleeping) |
| Neighbor Linear Velocity | 0.48 studs/s | [sleep-checking](#sleep-checking) ⟩ [awake](#awake) |
| Neighbor Rotational Velocity | 0.59 studs/s | [sleep-checking](#sleep-checking) ⟩ [awake](#awake) |
| Wake Linear Acceleration | 16.9 studs/s² | [awake](#awake) ⟩ [sleeping](#sleeping) |
| Wake Rotational Acceleration | 16.9 studs/s² | [awake](#awake) ⟩ [sleeping](#sleeping) |

Rotational velocity and acceleration thresholds reflect the velocity and acceleration of a point located on the assembly bounding sphere (a sphere that contains all of the parts in an assembly) that moves rigidly with the assembly.

> **Info:** For a given angular velocity, the rotational velocity of an assembly is proportional to the assembly bounding sphere radius. This means that larger assemblies can rotate at a lower angular velocity without falling asleep.
## Actuated joints

Sometimes developers want to move parts very slowly using an **actuated joint**, a constraint that applies force or motion to drive connected parts, such as a `Class.HingeConstraint` using a `Enum.ActuatorType.Motor|Motor`. To support these scenarios, assemblies connected to actuated joints use a stricter sleep velocity threshold. This delays when those assemblies fall asleep, allowing slow, controlled motion without the physics system prematurely putting them to sleep.

The following are considered actuated joints:

| Constraint | Configuration | Required nonzero properties |
| --- | --- | --- |
| `Class.AlignOrientation\|AlignOrientation` | `Class.AlignOrientation.RigidityEnabled\|RigidityEnabled` = `false` | <ul><li>`Class.AlignOrientation.MaxAngularVelocity\|MaxAngularVelocity`</li><li>`Class.AlignOrientation.MaxTorque\|MaxTorque`</li><li>`Class.AlignOrientation.Responsiveness\|Responsiveness`</li></ul> |
| `Class.AlignPosition\|AlignPosition` | `Class.AlignPosition.RigidityEnabled\|RigidityEnabled` = `false` | <ul><li>`Class.AlignPosition.MaxVelocity\|MaxVelocity`</li><li>`Class.AlignPosition.Responsiveness\|Responsiveness`</li></ul> |
| `Class.AngularVelocity\|AngularVelocity` | — | <ul><li>`Class.AngularVelocity.AngularVelocity\|AngularVelocity`</li><li>`Class.AngularVelocity.MaxTorque\|MaxTorque`</li></ul> |
| `Class.AnimationConstraint\|AnimationConstraint` | `Class.AnimationConstraint.IsKinematic\|IsKinematic` = `false` | <ul><li>`Class.AnimationConstraint.MaxForce\|MaxForce`</li><li>`Class.AnimationConstraint.MaxTorque\|MaxTorque`</li></ul> |
| `Class.CylindricalConstraint\|CylindricalConstraint` | `Class.CylindricalConstraint.ActuatorType\|ActuatorType` = `Enum.ActuatorType.Motor\|Motor` | <ul><li>`Class.CylindricalConstraint.Velocity\|Velocity`</li><li>`Class.CylindricalConstraint.MotorMaxAcceleration\|MotorMaxAcceleration`</li><li>`Class.CylindricalConstraint.MotorMaxForce\|MotorMaxForce`</li></ul> |
| `Class.CylindricalConstraint.ActuatorType\|ActuatorType` = `Enum.ActuatorType.Servo\|Servo` | <ul><li>`Class.CylindricalConstraint.Speed\|Speed`</li><li>`Class.CylindricalConstraint.ServoMaxForce\|ServoMaxForce`</li><li>`Class.CylindricalConstraint.Responsiveness\|Responsiveness`</li></ul> |
| `Class.CylindricalConstraint\|CylindricalConstraint` | `Class.CylindricalConstraint.AngularActuatorType\|AngularActuatorType` = `Enum.ActuatorType.Motor\|Motor` | <ul><li>`Class.CylindricalConstraint.AngularVelocity\|AngularVelocity`</li><li>`Class.CylindricalConstraint.MotorMaxAngularAcceleration\|MotorMaxAngularAcceleration`</li><li>`Class.CylindricalConstraint.MotorMaxTorque\|MotorMaxTorque`</li></ul> |
| `Class.CylindricalConstraint.AngularActuatorType\|AngularActuatorType` = `Enum.ActuatorType.Servo\|Servo` | <ul><li>`Class.CylindricalConstraint.AngularSpeed\|AngularSpeed`</li><li>`Class.CylindricalConstraint.ServoMaxTorque\|ServoMaxTorque`</li><li>`Class.CylindricalConstraint.Responsiveness\|Responsiveness`</li></ul> |
| `Class.HingeConstraint\|HingeConstraint` | `Class.HingeConstraint.ActuatorType\|ActuatorType` = `Enum.ActuatorType.Motor\|Motor` | <ul><li>`Class.HingeConstraint.AngularVelocity\|AngularVelocity`</li><li>`Class.HingeConstraint.MotorMaxAcceleration\|MotorMaxAcceleration`</li><li>`Class.HingeConstraint.MotorMaxTorque\|MotorMaxTorque`</li></ul> |
| `Class.HingeConstraint.ActuatorType\|ActuatorType` = `Enum.ActuatorType.Servo\|Servo` | <ul><li>`Class.HingeConstraint.AngularSpeed\|AngularSpeed`</li><li>`Class.HingeConstraint.ServoMaxTorque\|ServoMaxTorque`</li><li>`Class.HingeConstraint.Responsiveness\|Responsiveness`</li></ul> |
| `Class.LinearVelocity\|LinearVelocity` | `Class.LinearVelocity.VelocityConstraintMode\|VelocityConstraintMode` = `Enum.VelocityConstraintMode.Line\|Line` | <ul><li>`Class.LinearVelocity.LineVelocity\|LineVelocity`</li><li>If `Class.LinearVelocity.ForceLimitsEnabled\|ForceLimitsEnabled`, also `Class.LinearVelocity.MaxForce\|MaxForce`</li></ul> |
| `Class.LinearVelocity.VelocityConstraintMode\|VelocityConstraintMode` = `Enum.VelocityConstraintMode.Plane\|Plane` | <ul><li>`Class.LinearVelocity.PlaneVelocity\|PlaneVelocity`</li><li>If `Class.LinearVelocity.ForceLimitsEnabled\|ForceLimitsEnabled`:<ul><li>`Enum.ForceLimitMode.Magnitude\|Magnitude`: `Class.LinearVelocity.MaxForce\|MaxForce`</li><li>`Enum.ForceLimitMode.PerAxis\|PerAxis`: `Class.LinearVelocity.MaxPlanarAxesForce\|MaxPlanarAxesForce`</li></ul></li></ul> |
| `Class.LinearVelocity.VelocityConstraintMode\|VelocityConstraintMode` = `Enum.VelocityConstraintMode.Vector\|Vector` | <ul><li>`Class.LinearVelocity.VectorVelocity\|VectorVelocity`</li><li>If `Class.LinearVelocity.ForceLimitsEnabled\|ForceLimitsEnabled`:<ul><li>`Enum.ForceLimitMode.Magnitude\|Magnitude`: `Class.LinearVelocity.MaxForce\|MaxForce`</li><li>`Enum.ForceLimitMode.PerAxis\|PerAxis`: `Class.LinearVelocity.MaxAxesForce\|MaxAxesForce`</li></ul></li></ul> |
| `Class.PrismaticConstraint\|PrismaticConstraint` | `Class.PrismaticConstraint.ActuatorType\|ActuatorType` = `Enum.ActuatorType.Motor\|Motor` | <ul><li>`Class.PrismaticConstraint.Velocity\|Velocity`</li><li>`Class.PrismaticConstraint.MotorMaxAcceleration\|MotorMaxAcceleration`</li><li>`Class.PrismaticConstraint.MotorMaxForce\|MotorMaxForce`</li></ul> |
| `Class.PrismaticConstraint.ActuatorType\|ActuatorType` = `Enum.ActuatorType.Servo\|Servo` | <ul><li>`Class.PrismaticConstraint.Speed\|Speed`</li><li>`Class.PrismaticConstraint.ServoMaxForce\|ServoMaxForce`</li><li>`Class.PrismaticConstraint.Responsiveness\|Responsiveness`</li></ul> |
| `Class.RopeConstraint\|RopeConstraint` | `Class.RopeConstraint.WinchEnabled\|WinchEnabled` = `true` | <ul><li>`Class.RopeConstraint.WinchForce\|WinchForce`</li><li>`Class.RopeConstraint.WinchSpeed\|WinchSpeed`</li></ul> |

## Additional wake situations

In addition to situations outlined in [sleep‑checking](#sleep-checking) and [sleeping](#sleeping), an assembly enters the [awake](#awake) state when:

- It collides with another assembly moving faster than 1 studs/s.
- Any physics-related property of any `Class.BasePart` within the assembly changes, including:
  - `Class.BasePart.Anchored|Anchored`
  - `Class.BasePart.AssemblyLinearVelocity|AssemblyLinearVelocity`/`Class.BasePart.AssemblyAngularVelocity|AssemblyAngularVelocity`
  - `Class.BasePart.CanCollide|CanCollide`/`Class.BasePart.CanTouch|CanTouch`
  - `Class.BasePart.CustomPhysicalProperties|CustomPhysicalProperties`
  - `Class.BasePart.EnableFluidForces|EnableFluidForces`
  - `Class.BasePart.Massless|Massless`
  - `Class.BasePart.RootPriority|RootPriority`
- A non-zero impulse is applied to any `Class.BasePart` within the assembly via `Class.BasePart:ApplyImpulse()|ApplyImpulse()`, `Class.BasePart:ApplyImpulseAtPosition()|ApplyImpulseAtPosition()`, or `Class.BasePart:ApplyAngularImpulse()|ApplyAngularImpulse()`.
- Any physics-related property changes on the `Class.Workspace` that would affect the assembly, including:
  - `Class.Workspace.Gravity|Gravity`
  - `Class.Workspace.FluidForces|FluidForces`
  - `Class.Workspace.GlobalWind|GlobalWind`
  - `Class.Workspace.AirDensity|AirDensity`
- A new `Class.Constraint` is created with an `Class.Attachment` that is parented to a `Class.BasePart` within the assembly.
- Any property changes for a `Class.Constraint` with an `Class.Attachment` that is parented to a `Class.BasePart` within the assembly.
- The `Class.Motor.CurrentAngle|CurrentAngle` property changes for a `Class.Motor` that is connected to a `Class.BasePart` within the assembly.
- The assembly contains a `Class.VehicleSeat` with a seated player character.
- The assembly is within the `Class.Explosion.BlastRadius|BlastRadius` of an `Class.Explosion`.

## Debug visualization

During playtesting, you can visualize assembly sleep states by toggling on **Awake parts** from the [Visualization Options](/docs/en-us/studio/overview.md#visualization-options) widget in the upper‑right corner of the 3D viewport.

![A close up view of the 3D viewport with the Visualization Options button indicated in the upper-right corner.](../assets/studio/general/Visualization-Options.png)

Once enabled, simulated parts will be outlined by their current sleep state, with [awake](#awake) parts outlined in red, [sleep‑checking](#sleep-checking) parts outlined in orange, and [sleeping](#sleeping) parts un‑outlined.

_Simulated parts outlined by the color representing their current sleep state_
