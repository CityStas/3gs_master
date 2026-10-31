---
name: PhysicsSettings
last_updated: 2026-10-30T19:55:52Z
inherits:
  - Instance
  - Object
type: class
memory_category: Instances
tags:
  - NotCreatable
  - Service
  - NotReplicated
summary: "Lets you view debugging features in Roblox's physics engine, found under the Physics tab in Studio's settings menu."
---

# Class: PhysicsSettings

> Lets you view debugging features in Roblox's physics engine, found under the
> Physics tab in Studio's settings menu.

## Description

The PhysicsSettings is a singleton class, which lets you view debugging
features in Roblox's physics engine. You can find it under the Physics tab in
Studio's settings menu.

## Properties

### Property: PhysicsSettings.AllowSleep

```json
{
  "type": "boolean",
  "access": "ReadOnly",
  "security": {
    "read": "PluginSecurity",
    "write": "PluginSecurity"
  },
  "serialization": {
    "can_load": true,
    "can_save": true
  },
  "thread_safety": "ReadSafe",
  "category": "Performance"
}
```

When set to true, physically simulated objects will stop being simulated
if they have little to no motion for a set period of time.

### Property: PhysicsSettings.AreAnchorsShown

```json
{
  "type": "boolean",
  "access": "ReadOnly",
  "security": {
    "read": "PluginSecurity",
    "write": "PluginSecurity"
  },
  "serialization": {
    "can_load": true,
    "can_save": true
  },
  "thread_safety": "ReadSafe",
  "category": "Display"
}
```

When set to true, parts that are [BasePart.Anchored](/docs/reference/engine/classes/BasePart.md) will show a
gray surface outline on the surface of the part's bounding box that is
currently facing the ground.

### Property: PhysicsSettings.AreAssembliesShown

```json
{
  "type": "boolean",
  "access": "ReadOnly",
  "security": {
    "read": "PluginSecurity",
    "write": "PluginSecurity"
  },
  "serialization": {
    "can_load": true,
    "can_save": true
  },
  "thread_safety": "ReadSafe",
  "category": "Display"
}
```

When set to true, each physics assembly is assigned a unique color and the
[Part](/docs/reference/engine/classes/Part.md) associated with the assembly are outlined with the color.
Parts that are attached together by [JointInstance](/docs/reference/engine/classes/JointInstance.md) will share the
same color.

### Property: PhysicsSettings.AreAssemblyCentersOfMassShown

```json
{
  "type": "boolean",
  "access": "ReadOnly",
  "security": {
    "read": "RobloxScriptSecurity",
    "write": "RobloxScriptSecurity"
  },
  "serialization": {
    "can_load": true,
    "can_save": true
  },
  "thread_safety": "ReadSafe",
  "category": "Display"
}
```

When set to true, shows the center of mass for each physics assembly. This
property must be set in the Physics tab of Studio's settings menu.

### Property: PhysicsSettings.AreAwakePartsHighlighted

```json
{
  "type": "boolean",
  "access": "ReadOnly",
  "security": {
    "read": "PluginSecurity",
    "write": "PluginSecurity"
  },
  "serialization": {
    "can_load": true,
    "can_save": true
  },
  "thread_safety": "ReadSafe",
  "category": "Display"
}
```

When set to true, parts that are actively being physically simulated will
have a red outline.

### Property: PhysicsSettings.AreBodyTypesShown

```json
{
  "type": "boolean",
  "access": "ReadOnly",
  "security": {
    "read": "PluginSecurity",
    "write": "PluginSecurity"
  },
  "serialization": {
    "can_load": true,
    "can_save": true
  },
  "thread_safety": "ReadSafe",
  "category": "Display"
}
```

When set to true, [Part](/docs/reference/engine/classes/Part.md) will be outlined with a specific color,
depending on the state of its root simulation body.

#### Body Types

| Color | Body Type | Description |
| --- | --- | --- |
|  | Real-Time Body | Physics Body that is always simulated in real time, and is never throttled. Used for Humanoids. |
|  | Free-Fall Body | Physics Body that is freely moving with no physical contact. |
|  | Joint Body | Physics Body that is being influenced by a physically simulated joint, such as a Motor or a Hinge. |
|  | Contact Body | Physics Body that is in contact with another physics body. |
|  | Symmetric Contact Body | Physics Body that is experiencing a torquing force, while in contact with another body. |
|  | Vertical Contact Body | Physics Body that is moving very little along the Y plane, while in contact with another body. |

### Property: PhysicsSettings.AreCollisionCostsShown

```json
{
  "type": "boolean",
  "access": "ReadOnly",
  "security": {
    "read": "RobloxScriptSecurity",
    "write": "RobloxScriptSecurity"
  },
  "serialization": {
    "can_load": true,
    "can_save": true
  },
  "thread_safety": "ReadSafe",
  "category": "Display"
}
```

When set to true, displays collision cost annotations for parts. This
property is not scriptable.

### Property: PhysicsSettings.AreConstraintForcesShownForSelectedOrHoveredInstances

```json
{
  "type": "boolean",
  "access": "ReadOnly",
  "security": {
    "read": "RobloxScriptSecurity",
    "write": "RobloxScriptSecurity"
  },
  "serialization": {
    "can_load": true,
    "can_save": true
  },
  "thread_safety": "ReadSafe",
  "category": "Display"
}
```

When set to true, draws force vectors for constraints on selected or
hovered instances. This property must be set in the Physics tab of
Studio's settings menu.

### Property: PhysicsSettings.AreConstraintTorquesShownForSelectedOrHoveredInstances

```json
{
  "type": "boolean",
  "access": "ReadOnly",
  "security": {
    "read": "RobloxScriptSecurity",
    "write": "RobloxScriptSecurity"
  },
  "serialization": {
    "can_load": true,
    "can_save": true
  },
  "thread_safety": "ReadSafe",
  "category": "Display"
}
```

When set to true, draws torque vectors for constraints on selected or
hovered instances. This property must be set in the Physics tab of
Studio's settings menu.

### Property: PhysicsSettings.AreContactForcesShownForSelectedOrHoveredAssemblies

```json
{
  "type": "boolean",
  "access": "ReadOnly",
  "security": {
    "read": "RobloxScriptSecurity",
    "write": "RobloxScriptSecurity"
  },
  "serialization": {
    "can_load": true,
    "can_save": true
  },
  "thread_safety": "ReadSafe",
  "category": "Display"
}
```

When set to true, draws contact force vectors for selected or hovered
assemblies. This property must be set in the Physics tab of Studio's
settings menu.

### Property: PhysicsSettings.AreContactIslandsShown

```json
{
  "type": "boolean",
  "access": "ReadOnly",
  "security": {
    "read": "PluginSecurity",
    "write": "PluginSecurity"
  },
  "serialization": {
    "can_load": true,
    "can_save": true
  },
  "thread_safety": "ReadSafe",
  "category": "Display"
}
```

When set to true, each contact island will render [SelectionBox](/docs/reference/engine/classes/SelectionBox.md)
adorns on the parts in contact islands, where each contact island is
assigned a random color.

### Property: PhysicsSettings.AreContactPointsShown

```json
{
  "type": "boolean",
  "access": "ReadOnly",
  "security": {
    "read": "PluginSecurity",
    "write": "PluginSecurity"
  },
  "serialization": {
    "can_load": true,
    "can_save": true
  },
  "thread_safety": "ReadSafe",
  "category": "Display"
}
```

When set to true, sphere adorns will be drawn at the contact points of
each part where physics interactions are occurring. Each sphere also has
an arrow drawn in 3D, facing the surface that the contact point is
detecting.

#### Solver Variations

The behavior of this property varies depending on whether Roblox's physics
engine is using the `PGS Physics Solver`, or the `Spring Physics Solver`.

This is controlled by the [Workspace.PGSPhysicsSolverEnabled](/docs/reference/engine/classes/Workspace.md)
property.

##### Spring Physics Solver

When [Workspace.PGSPhysicsSolverEnabled](/docs/reference/engine/classes/Workspace.md) is set to false, the
contact points are color coded as listed below. The length of the arrow
extruding from the sphere depends on how much force the contact point is
exerting, and what the contact type is.

| Color | Contact Type | Description |
| --- | --- | --- |
|  | Normal Contact | Contact point with no special conditions. |
|  | Resting Contact | Contact point that has been active for at least 4 frames. |
|  | Second Pass Contact | Contact point that was made by a kernel joint going through a second pass. Rarely seen. |
|  | Real-Time Contact | Contact point that was made with a real-time physics body. This applies to tripped [Humanoid](/docs/reference/engine/classes/Humanoid.md). |
|  | Joint Contact | Contact point that was made under the context of a physically simulated joint. This applies to Motors and Hinges. |
<b>PGS Physics Solver</b>

When [Workspace.PGSPhysicsSolverEnabled](/docs/reference/engine/classes/Workspace.md) is set to true, the contact
points are always colored **RED**, and the length of the arrow will always
be 1 stud. There are no special conditions tracked, because the PGS solver
does not keep specific lookup tables for the states listed in the Spring
Solver.

| Color | Contact Type | Description |
| --- | --- | --- |
|  | Normal Contact | Contact point with no special conditions. |

### Property: PhysicsSettings.AreGravityForcesShownForSelectedOrHoveredAssemblies

```json
{
  "type": "boolean",
  "access": "ReadOnly",
  "security": {
    "read": "RobloxScriptSecurity",
    "write": "RobloxScriptSecurity"
  },
  "serialization": {
    "can_load": true,
    "can_save": true
  },
  "thread_safety": "ReadSafe",
  "category": "Display"
}
```

When set to true, draws gravity force vectors for selected or hovered
assemblies. This property must be set in the Physics tab of Studio's
settings menu.

### Property: PhysicsSettings.AreJointCoordinatesShown

```json
{
  "type": "boolean",
  "access": "ReadOnly",
  "security": {
    "read": "PluginSecurity",
    "write": "PluginSecurity"
  },
  "serialization": {
    "can_load": true,
    "can_save": true
  },
  "thread_safety": "ReadSafe",
  "category": "Display"
}
```

When set to true, XYZ axes are rendered at the [BasePart.CFrame](/docs/reference/engine/classes/BasePart.md) of
every part.

### Property: PhysicsSettings.AreMagnitudesShownForDrawnForcesAndTorques

```json
{
  "type": "boolean",
  "access": "ReadOnly",
  "security": {
    "read": "RobloxScriptSecurity",
    "write": "RobloxScriptSecurity"
  },
  "serialization": {
    "can_load": true,
    "can_save": true
  },
  "thread_safety": "ReadSafe",
  "category": "Display"
}
```

When set to true, displays magnitude labels alongside drawn force and
torque vectors. This property must be set in the Physics tab of Studio's
settings menu.

### Property: PhysicsSettings.AreMechanismsShown

```json
{
  "type": "boolean",
  "access": "ReadOnly",
  "security": {
    "read": "PluginSecurity",
    "write": "PluginSecurity"
  },
  "serialization": {
    "can_load": true,
    "can_save": true
  },
  "thread_safety": "ReadSafe",
  "category": "Display"
}
```

When set to true, every individual mechanism of parts is given a unique
color.

### Property: PhysicsSettings.AreModelCoordsShown

```json
{
  "type": "boolean",
  "access": "ReadOnly",
  "security": {
    "read": "PluginSecurity",
    "write": "PluginSecurity"
  },
  "serialization": {
    "can_load": true,
    "can_save": true
  },
  "thread_safety": "ReadSafe",
  "category": "Display"
}
```

An ancient property that hasn't work correctly since late 2007. It's
supposed to render an XYZ axis on the root part of a [Model](/docs/reference/engine/classes/Model.md), but
the axis rendering component doesn't work correctly.

### Property: PhysicsSettings.AreNonAnchorsShown

```json
{
  "type": "boolean",
  "access": "ReadOnly",
  "security": {
    "read": "PluginSecurity",
    "write": "PluginSecurity"
  },
  "serialization": {
    "can_load": true,
    "can_save": true
  },
  "thread_safety": "ReadSafe",
  "category": "Display"
}
```

When set to true, parts that are not [BasePart.Anchored](/docs/reference/engine/classes/BasePart.md) will be
highlighted. This property must be set in the Physics tab of Studio's
settings menu.

### Property: PhysicsSettings.AreOwnersShown

```json
{
  "type": "boolean",
  "access": "ReadOnly",
  "security": {
    "read": "PluginSecurity",
    "write": "PluginSecurity"
  },
  "serialization": {
    "can_load": true,
    "can_save": true
  },
  "thread_safety": "ReadSafe",
  "category": "Display"
}
```

When set to true, each player's character is outlined with a unique color,
and each part that the player has network ownership over is outlined with
the same color.

### Property: PhysicsSettings.ArePartCoordsShown

```json
{
  "type": "boolean",
  "access": "ReadOnly",
  "security": {
    "read": "PluginSecurity",
    "write": "PluginSecurity"
  },
  "serialization": {
    "can_load": true,
    "can_save": true
  },
  "thread_safety": "ReadSafe",
  "category": "Display"
}
```

An ancient property that hasn't worked correctly since late 2007. It's
supposed to render a large XYZ axis in the center of each
[BasePart](/docs/reference/engine/classes/BasePart.md), but the axis rendering component doesn't work correctly.

### Property: PhysicsSettings.AreRegionsShown

```json
{
  "type": "boolean",
  "access": "ReadOnly",
  "security": {
    "read": "PluginSecurity",
    "write": "PluginSecurity"
  },
  "serialization": {
    "can_load": true,
    "can_save": true
  },
  "thread_safety": "ReadSafe",
  "category": "Display"
}
```

When set to true, a cylinder is drawn around each player's character,
representing their [Player.SimulationRadius](/docs/reference/engine/classes/Player.md). Each physically
simulated object will check to see which player is closest to that object,
and if they are within the player's simulation radius. If both conditions
are met, that player will becomes the network owner of that object.

### Property: PhysicsSettings.AreSolverIslandsShown

```json
{
  "type": "boolean",
  "access": "ReadOnly",
  "security": {
    "read": "RobloxScriptSecurity",
    "write": "RobloxScriptSecurity"
  },
  "serialization": {
    "can_load": true,
    "can_save": true
  },
  "thread_safety": "ReadSafe",
  "category": "Display"
}
```

When set to true, each solver island is highlighted with a unique color.
This property must be set in the Physics tab of Studio's settings menu.

### Property: PhysicsSettings.AreTerrainReplicationRegionsShown

```json
{
  "type": "boolean",
  "access": "ReadOnly",
  "security": {
    "read": "PluginSecurity",
    "write": "PluginSecurity"
  },
  "serialization": {
    "can_load": true,
    "can_save": true
  },
  "thread_safety": "ReadSafe",
  "category": "Display"
}
```

When set to true, shows terrain replication streaming regions. This
property is not scriptable.

### Property: PhysicsSettings.AreTimestepsShown

```json
{
  "type": "boolean",
  "access": "ReadOnly",
  "security": {
    "read": "RobloxScriptSecurity",
    "write": "RobloxScriptSecurity"
  },
  "serialization": {
    "can_load": true,
    "can_save": true
  },
  "thread_safety": "ReadSafe",
  "category": "Display"
}
```

When set to true, shows physics timestep information for assemblies. This
property is not scriptable.

### Property: PhysicsSettings.AreUnalignedPartsShown

```json
{
  "type": "boolean",
  "access": "ReadOnly",
  "security": {
    "read": "PluginSecurity",
    "write": "PluginSecurity"
  },
  "serialization": {
    "can_load": true,
    "can_save": true
  },
  "thread_safety": "ReadSafe",
  "category": "Display"
}
```

When set to true, parts that aren't aligned on the 1x1x1 grid will be
outlined yellow.

### Property: PhysicsSettings.AreWorldCoordsShown

```json
{
  "type": "boolean",
  "access": "ReadOnly",
  "security": {
    "read": "PluginSecurity",
    "write": "PluginSecurity"
  },
  "serialization": {
    "can_load": true,
    "can_save": true
  },
  "thread_safety": "ReadSafe",
  "category": "Display"
}
```

An ancient property that hasn't worked correctly since late 2007. It's
supposed to render a large XYZ axis in the center of the world, but the
axis rendering component doesn't work correctly.

### Property: PhysicsSettings.DisableCSGv2

```json
{
  "type": "boolean",
  "access": "ReadOnly",
  "security": {
    "read": "PluginSecurity",
    "write": "PluginSecurity"
  },
  "serialization": {
    "can_load": true,
    "can_save": true
  },
  "thread_safety": "ReadSafe",
  "category": "Display"
}
```

When set to true, Roblox will fall back to using its legacy CSG solver
when performing solid model operations.

### Property: PhysicsSettings.DisableCSGv3ForPlugins

```json
{
  "type": "boolean",
  "access": "ReadOnly",
  "security": {
    "read": "PluginSecurity",
    "write": "PluginSecurity"
  },
  "serialization": {
    "can_load": true,
    "can_save": true
  },
  "thread_safety": "ReadSafe",
  "category": "Display"
}
```

When set to true, disables CSGv3 for plugin solid modeling operations.
This property must be set in the Physics tab of Studio's settings menu.

### Property: PhysicsSettings.DrawConstraintsNetForce

```json
{
  "type": "boolean",
  "access": "ReadOnly",
  "security": {
    "read": "RobloxScriptSecurity",
    "write": "RobloxScriptSecurity"
  },
  "serialization": {
    "can_load": true,
    "can_save": true
  },
  "thread_safety": "ReadSafe",
  "category": "Display"
}
```

When set to true, draws the net force from all constraints on selected or
hovered assemblies. This property must be set in the Physics tab of
Studio's settings menu.

### Property: PhysicsSettings.DrawContactsNetForce

```json
{
  "type": "boolean",
  "access": "ReadOnly",
  "security": {
    "read": "RobloxScriptSecurity",
    "write": "RobloxScriptSecurity"
  },
  "serialization": {
    "can_load": true,
    "can_save": true
  },
  "thread_safety": "ReadSafe",
  "category": "Display"
}
```

When set to true, draws the net force from all contacts on selected or
hovered assemblies. This property must be set in the Physics tab of
Studio's settings menu.

### Property: PhysicsSettings.DrawShapecast

```json
{
  "type": "boolean",
  "access": "ReadOnly",
  "security": {
    "read": "PluginSecurity",
    "write": "PluginSecurity"
  },
  "serialization": {
    "can_load": true,
    "can_save": true
  },
  "thread_safety": "ReadSafe",
  "category": "Display"
}
```

When set to true, draws the swept volume and hit result of every
[WorldRoot:Shapecast()](/docs/reference/engine/classes/WorldRoot.md), [WorldRoot:Blockcast()](/docs/reference/engine/classes/WorldRoot.md), and
[WorldRoot:Spherecast()](/docs/reference/engine/classes/WorldRoot.md) query. Each cast is drawn with its shape at
the start of the cast and where it stopped, faint copies of the shape
along the path it traveled, the travel direction, and the contact point of
the hit. Casts that hit something are drawn in green and casts that miss
are drawn in red.

### Property: PhysicsSettings.DrawTotalNetForce

```json
{
  "type": "boolean",
  "access": "ReadOnly",
  "security": {
    "read": "RobloxScriptSecurity",
    "write": "RobloxScriptSecurity"
  },
  "serialization": {
    "can_load": true,
    "can_save": true
  },
  "thread_safety": "ReadSafe",
  "category": "Display"
}
```

When set to true, draws the total net force on selected or hovered
assemblies. This property must be set in the Physics tab of Studio's
settings menu.

### Property: PhysicsSettings.EnableForceVisualizationSmoothing

```json
{
  "type": "boolean",
  "access": "ReadOnly",
  "security": {
    "read": "RobloxScriptSecurity",
    "write": "RobloxScriptSecurity"
  },
  "serialization": {
    "can_load": true,
    "can_save": true
  },
  "thread_safety": "ReadSafe",
  "category": "Display"
}
```

When set to true, enables temporal smoothing for force and torque
visualizations. This property must be set in the Physics tab of Studio's
settings menu.

### Property: PhysicsSettings.FluidForceDrawScale

```json
{
  "type": "float",
  "access": "ReadOnly",
  "security": {
    "read": "RobloxScriptSecurity",
    "write": "RobloxScriptSecurity"
  },
  "serialization": {
    "can_load": true,
    "can_save": true
  },
  "thread_safety": "ReadSafe",
  "category": "Display"
}
```

Sets the scale of arrows drawn for aerodynamic force visualization. The
default value is 1.0; smaller values draw smaller arrows and vice versa.
The default value is a good starting point for a wide range of aerodynamic
mechanisms.

### Property: PhysicsSettings.ForceDrawScale

```json
{
  "type": "float",
  "access": "ReadOnly",
  "security": {
    "read": "RobloxScriptSecurity",
    "write": "RobloxScriptSecurity"
  },
  "serialization": {
    "can_load": true,
    "can_save": true
  },
  "thread_safety": "ReadSafe",
  "category": "Display"
}
```

Sets the scale of arrows drawn for force visualization. This property is
not scriptable.

### Property: PhysicsSettings.ForceVisualizationSmoothingSteps

```json
{
  "type": "int",
  "access": "ReadOnly",
  "security": {
    "read": "RobloxScriptSecurity",
    "write": "RobloxScriptSecurity"
  },
  "serialization": {
    "can_load": true,
    "can_save": true
  },
  "thread_safety": "ReadSafe",
  "category": "Display"
}
```

Controls the number of frames used for force visualization smoothing. This
property must be set in the Physics tab of Studio's settings menu.

### Property: PhysicsSettings.IsInterpolationThrottleShown

```json
{
  "type": "boolean",
  "access": "ReadOnly",
  "security": {
    "read": "PluginSecurity",
    "write": "PluginSecurity"
  },
  "serialization": {
    "can_load": true,
    "can_save": true
  },
  "thread_safety": "ReadSafe",
  "category": "Display"
}
```

When set to true, shows physics interpolation throttle information. This
property is not scriptable.

### Property: PhysicsSettings.IsReceiveAgeShown

```json
{
  "type": "boolean",
  "access": "ReadOnly",
  "security": {
    "read": "PluginSecurity",
    "write": "PluginSecurity"
  },
  "serialization": {
    "can_load": true,
    "can_save": true
  },
  "thread_safety": "ReadSafe",
  "category": "Display"
}
```

This property is supposed to show the [BasePart.ReceiveAge](/docs/reference/engine/classes/BasePart.md) of a
part, but it does not work correctly.

### Property: PhysicsSettings.IsTreeShown

```json
{
  "type": "boolean",
  "access": "ReadOnly",
  "security": {
    "read": "PluginSecurity",
    "write": "PluginSecurity"
  },
  "serialization": {
    "can_load": true,
    "can_save": true
  },
  "thread_safety": "ReadSafe",
  "category": "Display"
}
```

When set to true, the joint connections of each part, and the states of
their underlying primitive components are visualized as a spanning tree.

##### Spanning Tree Table

There are several visualizations made available when this property is set
to true:

| Color | Adorn Type | Description |
| --- | --- | --- |
|  | Box | Root Primitive of a Mechanism that is currently anchored, or connected to an anchored primitive. See [BasePart:IsGrounded()](/docs/reference/engine/classes/BasePart.md). |
|  | Box | Root Primitive of a Mechanism that is free to be physically simulated. |
|  | Box | Root Primitive of a Mechanism that has moving components. |
|  | Sphere | Root Primitive of an Assembly. |
|  | Line | Connection between two Primitives that share the same Assembly. |
|  | Line | Connection between two Primitives. |

### Property: PhysicsSettings.PhysicsEnvironmentalThrottle

```json
{
  "type": "EnviromentalPhysicsThrottle",
  "access": "ReadOnly",
  "security": {
    "read": "PluginSecurity",
    "write": "PluginSecurity"
  },
  "serialization": {
    "can_load": true,
    "can_save": true
  },
  "thread_safety": "ReadSafe",
  "category": "Performance"
}
```

Controls the throttle rate of Roblox's physics engine. By default, the
physics engine will adjust the physics environment throttle depending on
how much work the physics engine is doing, and the current framerate. See
the enum page for [EnviromentalPhysicsThrottle](/docs/reference/engine/enums/EnviromentalPhysicsThrottle.md) for more information.

### Property: PhysicsSettings.ShowDecompositionGeometry

```json
{
  "type": "boolean",
  "access": "ReadOnly",
  "security": {
    "read": "PluginSecurity",
    "write": "PluginSecurity"
  },
  "serialization": {
    "can_load": true,
    "can_save": true
  },
  "thread_safety": "ReadSafe",
  "category": "Display"
}
```

When set to true, the underlying collision geometry for
[PartOperation](/docs/reference/engine/classes/PartOperation.md) and [MeshPart](/docs/reference/engine/classes/MeshPart.md) is rendered.

### Property: PhysicsSettings.ShowFluidForcesForSelectedOrHoveredMechanisms

```json
{
  "type": "boolean",
  "access": "ReadOnly",
  "security": {
    "read": "RobloxScriptSecurity",
    "write": "RobloxScriptSecurity"
  },
  "serialization": {
    "can_load": true,
    "can_save": true
  },
  "thread_safety": "ReadSafe",
  "category": "Display"
}
```

When set to true, enables aerodynamic visualization for selected or
hovered mechanisms in Studio's play and run modes. This visualization
shows aerodynamic force, torque, and center of pressure for the hovered or
selected mechanisms.

### Property: PhysicsSettings.ShowInstanceNamesForDrawnForcesAndTorques

```json
{
  "type": "boolean",
  "access": "ReadOnly",
  "security": {
    "read": "RobloxScriptSecurity",
    "write": "RobloxScriptSecurity"
  },
  "serialization": {
    "can_load": true,
    "can_save": true
  },
  "thread_safety": "ReadSafe",
  "category": "Display"
}
```

When set to true, displays instance names alongside drawn force and torque
vectors. This property must be set in the Physics tab of Studio's settings
menu.

### Property: PhysicsSettings.SolverConvergenceMetricType

```json
{
  "type": "SolverConvergenceMetricType",
  "access": "ReadOnly",
  "security": {
    "read": "RobloxScriptSecurity",
    "write": "RobloxScriptSecurity"
  },
  "serialization": {
    "can_load": true,
    "can_save": true
  },
  "thread_safety": "ReadSafe",
  "category": "Display"
}
```

Controls which metric is used for solver convergence visualization. This
property is not scriptable.

### Property: PhysicsSettings.SolverConvergenceVisualizationMode

```json
{
  "type": "SolverConvergenceVisualizationMode",
  "access": "ReadOnly",
  "security": {
    "read": "RobloxScriptSecurity",
    "write": "RobloxScriptSecurity"
  },
  "serialization": {
    "can_load": true,
    "can_save": true
  },
  "thread_safety": "ReadSafe",
  "category": "Display"
}
```

Controls the visualization mode for solver convergence. This property is
not scriptable.

### Property: PhysicsSettings.ThrottleAdjustTime

```json
{
  "type": "double",
  "access": "ReadOnly",
  "security": {
    "read": "PluginSecurity",
    "write": "PluginSecurity"
  },
  "serialization": {
    "can_load": true,
    "can_save": true
  },
  "thread_safety": "ReadSafe",
  "category": "Performance"
}
```

If the [PhysicsSettings.PhysicsEnvironmentalThrottle](/docs/reference/engine/classes/PhysicsSettings.md) is set to
`DefaultAuto`, this specifies the maximum time that the physics
environmental throttle has to wait before it is allowed to automatically
change.

### Property: PhysicsSettings.TorqueDrawScale

```json
{
  "type": "float",
  "access": "ReadOnly",
  "security": {
    "read": "RobloxScriptSecurity",
    "write": "RobloxScriptSecurity"
  },
  "serialization": {
    "can_load": true,
    "can_save": true
  },
  "thread_safety": "ReadSafe",
  "category": "Display"
}
```

Sets the scale of arrows drawn for torque visualization. This property is
not scriptable.

### Property: PhysicsSettings.UseCSGv2

```json
{
  "type": "boolean",
  "access": "ReadOnly",
  "security": {
    "read": "PluginSecurity",
    "write": "PluginSecurity"
  },
  "serialization": {
    "can_load": true,
    "can_save": true
  },
  "thread_safety": "ReadSafe",
  "category": "Display"
}
```

If set to true, version 2 of Roblox's CSG solver will be used instead of
version 1.

### Property: PhysicsSettings.ForceCSGv2 *(hidden)*

```json
{
  "type": "boolean",
  "access": "ReadOnly",
  "security": {
    "read": "PluginSecurity",
    "write": "PluginSecurity"
  },
  "serialization": {
    "can_load": true,
    "can_save": true
  },
  "thread_safety": "ReadSafe",
  "category": "Display"
}
```

When set to true, forces the use of CSGv2 for solid modeling operations.
This property must be set in the Physics tab of Studio's settings menu.

## Inherited Members

### From [Instance](/docs/reference/engine/classes/Instance.md)

- **Property `Archivable`** (`boolean`): Determines if an Instance and its descendants can be cloned using
- **Property `archivable`** (`boolean`):  *(deprecated, hidden)*
- **Property `Capabilities`** (`SecurityCapabilities`): The set of capabilities allowed to be used for scripts inside this
- **Property `IsInSandbox`** (`boolean`): Indicates whether the instance is inside a sandboxed container.
- **Property `Name`** (`string`): A non-unique identifier of the Instance.
- **Property `Parent`** (`Instance`): Determines the hierarchical parent of the Instance.
- **Property `PredictionMode`** (`PredictionMode`): Reflects the client-side prediction mode applied to the instance under
- **Property `RobloxLocked`** (`boolean`): A deprecated property that used to protect CoreGui objects. *(hidden)*
- **Property `Sandboxed`** (`boolean`): When enabled, the instance can only access abilities in its `Capabilities`
- **Property `UniqueId`** (`UniqueId`): A unique identifier for the instance.
- **Method `AddTag(tag: string): ()`**: Applies a tag to the instance.
- **Method `children(): Instances`**: Returns an array of the object's children. *(deprecated)*
- **Method `ClearAllChildren(): ()`**: This method destroys all of an instance's children.
- **Method `Clone(): Instance`**: Create a copy of an instance and all its descendants, ignoring instances
- **Method `clone(): Instance`**:  *(deprecated)*
- **Method `Destroy(): ()`**: Sets the Instance.Parent property to `nil`, locks the
- **Method `destroy(): ()`**:  *(deprecated)*
- **Method `FindFirstAncestor(name: string): Instance?`**: Returns the first ancestor of the Instance whose
- **Method `FindFirstAncestorOfClass(className: string): Instance?`**: Returns the first ancestor of the Instance whose
- **Method `FindFirstAncestorWhichIsA(className: string): Instance?`**: Returns the first ancestor of the Instance for whom
- **Method `FindFirstChild(name: string, recursive?: boolean): Instance?`**: Returns the first child of the Instance found with the given name.
- **Method `findFirstChild(name: string, recursive?: boolean): Instance`**:  *(deprecated)*
- **Method `FindFirstChildOfClass(className: string): Instance?`**: Returns the first child of the Instance whose
- **Method `FindFirstChildWhichIsA(className: string, recursive?: boolean): Instance?`**: Returns the first child of the Instance for whom
- **Method `FindFirstDescendant(name: string): Instance?`**: Returns the first descendant found with the given Instance.Name.
- **Method `GetActor(): Actor?`**: Returns the Actor associated with the Instance, if any.
- **Method `GetAttribute(attribute: string): Variant`**: Returns the value which has been assigned to the given attribute name.
- **Method `GetAttributeChangedSignal(attribute: string): RBXScriptSignal`**: Returns an event that fires when the given attribute changes.
- **Method `GetAttributes(): Dictionary`**: Returns a dictionary of the instance's attributes.
- **Method `GetChildren(): Instances`**: Returns an array containing all of the instance's children.
- **Method `getChildren(): Instances`**:  *(deprecated)*
- **Method `GetDebugId(scopeLength?: int): string`**: Returns a coded string of the debug ID used internally by Roblox.
- **Method `GetDescendants(): Instances`**: Returns an array containing all of the descendants of the instance.
- **Method `GetFullName(): string`**: Returns a string describing the instance's ancestry.
- **Method `GetStyled(name: string, selector: string?): Variant`**: Returns the styled or explicitly modified value of the specified property,
- **Method `GetStyledPropertyChangedSignal(property: string): RBXScriptSignal`**: Returns an event that fires when the given style property changes on the
- **Method `GetTags(): Array`**: Gets an array of all tags applied to the instance.
- **Method `HasTag(tag: string): boolean`**: Check whether the instance has a given tag.
- **Method `IsAncestorOf(descendant: Instance): boolean`**: Returns true if an Instance is an ancestor of the given
- **Method `IsDescendantOf(ancestor: Instance): boolean`**: Returns `true` if an Instance is a descendant of the given
- **Method `isDescendantOf(ancestor: Instance): boolean`**:  *(deprecated)*
- **Method `IsPropertyModified(property: string): boolean`**: Returns `true` if the value stored in the specified property is not equal
- **Method `QueryDescendants(selector: string): Instances`**: Returns an array containing all descendants of the instance that match the
- **Method `Remove(): ()`**: Sets the object's `Parent` to `nil`, and does the same for all its *(deprecated)*
- **Method `remove(): ()`**:  *(deprecated)*
- **Method `RemoveTag(tag: string): ()`**: Removes a tag from the instance.
- **Method `ResetPropertyToDefault(property: string): ()`**: Resets a property to its default value.
- **Method `SetAttribute(attribute: string, value: Variant): ()`**: Sets the attribute with the given name to the given value.
- **Method `WaitForChild(childName: string, timeOut: double): Instance`**: Returns the child of the Instance with the given name. If the
- **Event `AncestryChanged`**: Fires when the Instance.Parent property of this object or one of
- **Event `AttributeChanged`**: Fires whenever an attribute is changed on the Instance.
- **Event `ChildAdded`**: Fires after an object is parented to this Instance.
- **Event `childAdded`**:  *(deprecated)*
- **Event `ChildRemoved`**: Fires after a child is removed from this Instance.
- **Event `DescendantAdded`**: Fires after a descendant is added to the Instance.
- **Event `DescendantRemoving`**: Fires immediately before a descendant of the Instance is removed.
- **Event `Destroying`**: Fires immediately before (or is deferred until after) the instance is
- **Event `StyledPropertiesChanged`**: Fires whenever any style property is changed on the instance, including

### From [Object](/docs/reference/engine/classes/Object.md)

- **Property `ClassName`** (`string`): A read-only string representing the class this Object belongs to.
- **Property `className`** (`string`):  *(deprecated)*
- **Method `GetPropertyChangedSignal(property: string): RBXScriptSignal`**: Get an event that fires when a given property of the object changes.
- **Method `IsA(className: string): boolean`**: Returns true if an object's class matches or inherits from a given class.
- **Method `isA(className: string): boolean`**:  *(deprecated)*
- **Event `Changed`**: Fires immediately after a property of the object changes, with some