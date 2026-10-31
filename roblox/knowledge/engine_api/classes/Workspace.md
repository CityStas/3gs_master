---
name: Workspace
last_updated: 2026-10-30T19:55:53Z
inherits:
  - WorldRoot
  - Model
  - PVInstance
  - Instance
  - Object
type: class
memory_category: BaseParts
tags:
  - NotCreatable
  - Service
summary: "`Workspace` houses 3D objects which are rendered to the 3D world. Objects not descending from it will not be rendered or physically interact with the world."
---

# Class: Workspace

> `Workspace` houses 3D objects which are rendered to the 3D world. Objects not
> descending from it will not be rendered or physically interact with the world.

## Description

The core job of [Workspace](/docs/reference/engine/classes/Workspace.md) is to hold objects that exist in the 3D
world, effectively [BaseParts](/docs/reference/engine/classes/BasePart.md) and
[Attachments](/docs/reference/engine/classes/Attachment.md). While such objects are descendant of
[Workspace](/docs/reference/engine/classes/Workspace.md), they will be active. For [BaseParts](/docs/reference/engine/classes/BasePart.md), this
means they will be rendered, and physically interact with other parts and the
world. For [Attachments](/docs/reference/engine/classes/Attachment.md), this means that objects adorned to
them, such as [ParticleEmitters](/docs/reference/engine/classes/ParticleEmitter.md), [Beams](/docs/reference/engine/classes/Beam.md),
and [BillboardGuis](/docs/reference/engine/classes/BillboardGui.md), will render.

Understanding this behavior is important, as it means objects can be removed
from [Workspace](/docs/reference/engine/classes/Workspace.md) when they are not needed. For example, map
[Models](/docs/reference/engine/classes/Model.md) can be removed when a different map is being played on.
Objects that are not immediately needed in the 3D world are generally stored
in [ReplicatedStorage](/docs/reference/engine/classes/ReplicatedStorage.md) or [ServerStorage](/docs/reference/engine/classes/ServerStorage.md).

In its role as the holder of active 3D objects, [Workspace](/docs/reference/engine/classes/Workspace.md) includes a
number of useful functions related to parts, their positions, and joints
between them.

#### Accessing the Workspace

[Workspace](/docs/reference/engine/classes/Workspace.md) can be accessed several ways, all of which are valid.

- `workspace`
- `game:GetService("Workspace")`
- `game.Workspace`

#### Notes

- Objects that require adornment, such as
  [ParticleEmitters](/docs/reference/engine/classes/ParticleEmitter.md) and
  [BillboardGuis](/docs/reference/engine/classes/BillboardGui.md), will be at the
  <Typography noWrap>`(0, 0, 0)`</Typography> position when parented to
  [Workspace](/docs/reference/engine/classes/Workspace.md) without an adornee otherwise being set.
- The [Model:MakeJoints()](/docs/reference/engine/classes/Model.md) and [Model:BreakJoints()](/docs/reference/engine/classes/Model.md) methods
  inherited from the [Model](/docs/reference/engine/classes/Model.md) class are overridden by
  [Workspace:MakeJoints()](/docs/reference/engine/classes/Workspace.md) and [Workspace:BreakJoints()](/docs/reference/engine/classes/Workspace.md) which can
  only be used in plugins.
- It is impossible to delete [Workspace](/docs/reference/engine/classes/Workspace.md).
- [Workspace](/docs/reference/engine/classes/Workspace.md) automatically cleans up [BaseParts](/docs/reference/engine/classes/BasePart.md) that
  fall beneath
  [FallenPartsDestroyHeight](/docs/reference/engine/classes/Workspace.md).
- A client's current [Camera](/docs/reference/engine/classes/Camera.md) object can be accessed using the
  [Workspace.CurrentCamera](/docs/reference/engine/classes/Workspace.md) property.
- The [Terrain](/docs/reference/engine/classes/Terrain.md) object can be accessed using the
  [Workspace.Terrain](/docs/reference/engine/classes/Workspace.md) property.

## Properties

### Property: Workspace.AirDensity

```json
{
  "type": "float",
  "access": "ReadWrite",
  "security": {
    "read": "None",
    "write": "None"
  },
  "serialization": {
    "can_load": true,
    "can_save": true
  },
  "thread_safety": "ReadSafe",
  "category": "AirProperties",
  "capabilities": [
    "Physics",
    "Environment"
  ],
  "simulationAccess": true
}
```

The ground level (**Y** of 0) air density in RMU/stud&sup3; units (see
[Roblox Units](/docs/en-us/physics/units.md)), used to calculate the
aerodynamic force if [Workspace.FluidForces](/docs/reference/engine/classes/Workspace.md) is
[Experimental](/docs/reference/engine/enums/FluidForces.md). The default corresponds to realistic sea
level air density at standard temperature and pressure. Air density decays
as the **Y** altitude increases, reaching 5% of its ground level value at
100,000 studs. Below **Y** of 0, the air density is fixed at the input
value.

### Property: Workspace.AirTurbulenceIntensity

```json
{
  "type": "float",
  "access": "ReadWrite",
  "security": {
    "read": "None",
    "write": "None"
  },
  "serialization": {
    "can_load": true,
    "can_save": true
  },
  "thread_safety": "ReadSafe",
  "category": "AirProperties",
  "capabilities": [
    "Physics",
    "Environment"
  ],
  "simulationAccess": true
}
```

Controls the intensity of turbulence by determining the magnitude of
fluctuations in wind velocities. Ranges from `0` to `1`, with a value of
`0` disabling turbulence and a value of `1` providing the most intense
turbulence. The values of `AirTurbulenceIntensity` roughly correspond to
the following levels:

- `(0, 0.4]`: Low intensity turbulence
- `(0.4, 0.7]`: Moderate intensity turbulence
- `(0.7, 1]`: High intensity turbulence

The magnitude of the fluctuations at a fixed intensity scale linearly with
the magnitude of the global wind, except in the case that the global wind
is zero. When the global wind is zero, the magnitude of the fluctuations
scale exponentially with `AirTurbulenceIntensity`, allowing low and high
intensity turbulence to exist with wind velocities that still average out
to zero.

### Property: Workspace.AllowThirdPartySales

```json
{
  "type": "boolean",
  "access": "ReadWrite",
  "security": {
    "read": "None",
    "write": "None"
  },
  "serialization": {
    "can_load": true,
    "can_save": true
  },
  "thread_safety": "ReadSafe",
  "category": "Behavior",
  "capabilities": [
    "Monetization"
  ]
}
```

This [Workspace](/docs/reference/engine/classes/Workspace.md) property determines whether assets created by other
uses can be sold in the game.

### Property: Workspace.AuthorityMode

```json
{
  "type": "AuthorityMode",
  "access": "ReadWrite",
  "security": {
    "read": "None",
    "write": "None"
  },
  "serialization": {
    "can_load": true,
    "can_save": true
  },
  "thread_safety": "ReadSafe",
  "category": "Server Authority",
  "capabilities": [
    "Basic"
  ]
}
```

Sets the server authority mode. See [AuthorityMode](/docs/reference/engine/enums/AuthorityMode.md) for options.

### Property: Workspace.AvatarUnificationMode

```json
{
  "type": "AvatarUnificationMode",
  "access": "ReadWrite",
  "security": {
    "read": "None",
    "write": "None"
  },
  "serialization": {
    "can_load": true,
    "can_save": true
  },
  "thread_safety": "ReadSafe",
  "category": "Behavior"
}
```

When [AvatarUnificationMode.Enabled](/docs/reference/engine/enums/AvatarUnificationMode.md), R15 avatars can join R6
experiences via the R6 to R15 adapter. R15 characters receive invisible
adapter parts with R6-compatible names welded to their corresponding R15
parts, preserving R6-like scale and movement while enabling R15 features
such as layered clothing and animatable heads. Only relevant when the
experience's avatar type is set to R6.

### Property: Workspace.ClientAnimatorThrottling

```json
{
  "type": "ClientAnimatorThrottlingMode",
  "access": "ReadWrite",
  "security": {
    "read": "None",
    "write": "None"
  },
  "serialization": {
    "can_load": true,
    "can_save": true
  },
  "thread_safety": "ReadSafe",
  "category": "Behavior",
  "capabilities": [
    "Animation"
  ]
}
```

Specifies the [ClientAnimatorThrottlingMode](/docs/reference/engine/enums/ClientAnimatorThrottlingMode.md) to use for the local
client.

When enabled, animations on remotely-simulated [Model](/docs/reference/engine/classes/Model.md) instances
will begin to throttle. The throttler calculates throttling intensity
using:

- Visibility of a [Model](/docs/reference/engine/classes/Model.md) in relation to the [Camera](/docs/reference/engine/classes/Camera.md)
- In-game FPS
- Number of active animations

### Property: Workspace.CurrentCamera

```json
{
  "type": "Camera",
  "access": "ReadWrite",
  "security": {
    "read": "None",
    "write": "None"
  },
  "serialization": {
    "can_load": true,
    "can_save": true
  },
  "thread_safety": "ReadSafe",
  "category": "Data",
  "capabilities": [
    "Basic"
  ]
}
```

The [Camera](/docs/reference/engine/classes/Camera.md) object being used by the local player.

#### How to use CurrentCamera

When looking for a client's [Camera](/docs/reference/engine/classes/Camera.md) object, use this property
rather than looking for a child of [Workspace](/docs/reference/engine/classes/Workspace.md) named "Camera".

When you set this property, all other `Camera` objects in the `Workspace`
are destroyed, including the previous `CurrentCamera`. If you set this
property to `nil` or to a camera that is not a descendant of the Workspace
(or the `CurrentCamera` is otherwise destroyed), a new `Camera` will be
created and assigned. Avoid these scenarios, as destroying the camera can
have unintended consequences.

For more information, see
[Script the camera](/docs/en-us/workspace/camera.md#script-the-camera).

### Property: Workspace.DistributedGameTime

```json
{
  "type": "double",
  "access": "ReadWrite",
  "security": {
    "read": "None",
    "write": "None"
  },
  "serialization": {
    "can_load": true,
    "can_save": true
  },
  "thread_safety": "ReadSafe",
  "category": "Data",
  "capabilities": [
    "Basic"
  ]
}
```

The amount of time, in seconds, that the game has been running.

Despite the title, this value is currently not 'Distributed' across the
client and the server. Instead, on the server it represents how long the
server has been running. On the client, it represents how long the client
has been connected to the server.

Developers should not rely on the above behavior, and it is possible this
property will be synchronized across clients and the server in the future.

Those looking for the time since the program started running should use
the 'time' function instead. See below for a comparison between
DistributedGameTime and its alternatives.

**Distributed Game Time**

Demonstrates [Workspace.DistributedGameTime](/docs/reference/engine/classes/Workspace.md).

```lua
local Workspace = game:GetService("Workspace")

print(Workspace.DistributedGameTime) -- Time the game started running
print(os.time()) -- Time since epoch (1 January 1970, 00:00:00) UTC
print(tick()) -- Time since epoch (1 January 1970, 00:00:00) system time
print(time()) -- Time the game started running
print(elapsedTime()) -- Time since Roblox started running
```

### Property: Workspace.EnableSLIMAvatars

```json
{
  "type": "RolloutState",
  "access": "ReadWrite",
  "security": {
    "read": "None",
    "write": "None"
  },
  "serialization": {
    "can_load": true,
    "can_save": true
  },
  "thread_safety": "ReadSafe",
  "category": "Streaming",
  "capabilities": [
    "Players"
  ]
}
```

This [RolloutState](/docs/reference/engine/enums/RolloutState.md) property controls whether a
[SLIM](/docs/reference/engine/enums/ModelLevelOfDetail.md) model is generated for avatar characters in
the experience. When enabled and instance streaming is active, avatars
render using SLIM in the same way that setting [Model.LevelOfDetail](/docs/reference/engine/classes/Model.md)
to [SLIM](/docs/reference/engine/enums/ModelLevelOfDetail.md) works for other models.

When set to [Enabled](/docs/reference/engine/enums/RolloutState.md), avatars use SLIM rendering. When
set to [Disabled](/docs/reference/engine/enums/RolloutState.md), avatars use the traditional rendering
approach. [Default](/docs/reference/engine/enums/RolloutState.md) follows the current engine-wide
rollout state.

This property cannot be set through developer-facing Luau and must be set
in Studio through the Properties window, Command Bar, or a plugin.

### Property: Workspace.FallenPartsDestroyHeight

```json
{
  "type": "float",
  "access": "ReadWrite",
  "security": {
    "read": "None",
    "write": "None"
  },
  "serialization": {
    "can_load": true,
    "can_save": true
  },
  "thread_safety": "ReadSafe",
  "category": "Behavior",
  "capabilities": [
    "Basic"
  ]
}
```

This property determines the height at which the engine automatically
removes falling [BaseParts](/docs/reference/engine/classes/BasePart.md) and their ancestor
[Models](/docs/reference/engine/classes/Model.md) from [Workspace](/docs/reference/engine/classes/Workspace.md) by parenting them to `nil`.
This is to prevent parts that have fallen off the map from continuing to
fall forever.

If a part removed due to this behavior is the last part in a
[Model](/docs/reference/engine/classes/Model.md), that model will also be removed. This applies to all model
ancestors of the part.

This property is clamped between -50,000 and 50,000 because
[BaseParts](/docs/reference/engine/classes/BasePart.md) do not simulate or render properly at a great
distance from the origin due to floating point inaccuracies.

This property can be read by scripts, but can only be set by plugins, the
command bar, or the properties window in Studio.

### Property: Workspace.FallHeightEnabled

```json
{
  "type": "boolean",
  "access": "ReadWrite",
  "security": {
    "read": "None",
    "write": "None"
  },
  "serialization": {
    "can_load": true,
    "can_save": true
  },
  "thread_safety": "ReadSafe",
  "category": "Behavior",
  "capabilities": [
    "Basic"
  ]
}
```

When `false`, the kill plane defined by
[Workspace.FallenPartsDestroyHeight](/docs/reference/engine/classes/Workspace.md) is disabled and falling parts
are not automatically removed. Defaults to `true`.

This property can be read by scripts but can only be set by plugins, the
command bar, or the properties window in Studio.

### Property: Workspace.FluidForces

```json
{
  "type": "FluidForces",
  "access": "ReadWrite",
  "security": {
    "read": "None",
    "write": "None"
  },
  "serialization": {
    "can_load": true,
    "can_save": true
  },
  "thread_safety": "ReadSafe",
  "category": "Behavior"
}
```

With this property enabled, the physics engine computes aerodynamic forces
on [BaseParts](/docs/reference/engine/classes/BasePart.md) whose
[EnableFluidForces](/docs/reference/engine/classes/BasePart.md) property is true. The
default, [Default](/docs/reference/engine/enums/FluidForces.md), disables aerodynamic forces. Note
that this property cannot be set through developer-facing Luau and instead
must be toggled in Studio.

### Property: Workspace.GlobalWind

```json
{
  "type": "Vector3",
  "access": "ReadWrite",
  "security": {
    "read": "None",
    "write": "None"
  },
  "serialization": {
    "can_load": true,
    "can_save": true
  },
  "thread_safety": "ReadSafe",
  "category": "AirProperties",
  "capabilities": [
    "Basic"
  ],
  "simulationAccess": true
}
```

This property specifies the direction and strength that wind blows through
the experience, affecting terrain grass, dynamic clouds, and particles.
See the [Global Wind](/docs/en-us/environment/global-wind.md) article for
details.

### Property: Workspace.Gravity

```json
{
  "type": "float",
  "access": "ReadWrite",
  "security": {
    "read": "None",
    "write": "None"
  },
  "serialization": {
    "can_load": true,
    "can_save": true
  },
  "thread_safety": "ReadSafe",
  "category": "Behavior",
  "capabilities": [
    "Basic"
  ],
  "simulationAccess": true
}
```

Determines the acceleration due to gravity applied to falling
[BaseParts](/docs/reference/engine/classes/BasePart.md). This value is measured in studs per second
squared and by default is set to 196.2 studs/second<sup>2</sup>. By
changing this value, developers can simulate the effects of lower or
higher gravity in game.

**Low Gravity Button**

This script creates a touch pad in the workspace that, when touched, will
reduce the game's gravity. Activating the pad again will switch back to normal
gravity.

```lua
local MOON_GRAVITY_RATIO = 1.62 / 9.81
local DEFAULT_GRAVITY = 196.2
local MOON_GRAVITY = DEFAULT_GRAVITY * MOON_GRAVITY_RATIO

-- Create a touch pad
local pad = Instance.new("Part")
pad.Size = Vector3.new(5, 1, 5)
pad.Position = Vector3.new(0, 0.5, 0)
pad.Anchored = true
pad.BrickColor = BrickColor.new("Bright green")
pad.Parent = workspace

-- Listen for pad touch
local enabled = false
local debounce = false

local function onPadTouched(_hit)
	if not debounce then
		debounce = true

		enabled = not enabled
		workspace.Gravity = enabled and MOON_GRAVITY or DEFAULT_GRAVITY

		pad.BrickColor = enabled and BrickColor.new("Bright red") or BrickColor.new("Bright green")

		task.wait(1)
		debounce = false
	end
end

pad.Touched:Connect(onPadTouched)
```

### Property: Workspace.IKControlConstraintSupport

```json
{
  "type": "IKControlConstraintSupport",
  "access": "ReadWrite",
  "security": {
    "read": "None",
    "write": "None"
  },
  "serialization": {
    "can_load": true,
    "can_save": true
  },
  "thread_safety": "ReadSafe",
  "category": "Behavior"
}
```

Enables support for constraints for IKControls. The `Default` value is the
same as `Enabled`. If disabled, IKControls ignore physics constraints. See
[IKControl](/docs/reference/engine/classes/IKControl.md) for additional details.

### Property: Workspace.ImprovedAnimationConstraint

```json
{
  "type": "RolloutState",
  "access": "ReadWrite",
  "security": {
    "read": "None",
    "write": "None"
  },
  "serialization": {
    "can_load": true,
    "can_save": true
  },
  "thread_safety": "ReadSafe",
  "category": "Behavior"
}
```

When enabled, [AnimationConstraints](/docs/reference/engine/classes/AnimationConstraint.md) use
separate strength and damping settings for linear and angular motion.
[Default](/docs/reference/engine/enums/RolloutState.md) follows the default for this feature.

### Property: Workspace.ImprovedPhysicsReplication

```json
{
  "type": "RolloutState",
  "access": "ReadWrite",
  "security": {
    "read": "None",
    "write": "None"
  },
  "serialization": {
    "can_load": true,
    "can_save": true
  },
  "thread_safety": "ReadSafe",
  "category": "Behavior"
}
```

When enabled, the experience uses the improved physics replication path.
[Default](/docs/reference/engine/enums/RolloutState.md) follows the default for this feature.

### Property: Workspace.InsertPoint

```json
{
  "type": "Vector3",
  "access": "ReadWrite",
  "security": {
    "read": "None",
    "write": "None"
  },
  "serialization": {
    "can_load": false,
    "can_save": false
  },
  "thread_safety": "ReadSafe",
  "category": "Data"
}
```

Stores the world-space position used when inserting new objects into the
workspace via the Studio IDE.

### Property: Workspace.LayeredClothingCacheOptimizations

```json
{
  "type": "RolloutState",
  "access": "ReadWrite",
  "security": {
    "read": "None",
    "write": "None"
  },
  "serialization": {
    "can_load": true,
    "can_save": true
  },
  "thread_safety": "ReadSafe",
  "category": "Behavior",
  "capabilities": [
    "AvatarAppearance"
  ]
}
```

Controls whether the engine caches layered clothing rendering data to
improve performance for experiences with many characters wearing layered
clothing. [Default](/docs/reference/engine/enums/RolloutState.md) follows the current engine-wide
rollout state.

### Property: Workspace.LuauTypeCheckMode

```json
{
  "type": "LuauTypeCheckMode",
  "access": "ReadWrite",
  "security": {
    "read": "None",
    "write": "None"
  },
  "serialization": {
    "can_load": true,
    "can_save": true
  },
  "thread_safety": "ReadSafe",
  "category": "Scripting",
  "capabilities": [
    "PluginOrOpenCloud"
  ]
}
```

Controls the Luau type checking mode applied to scripts in the experience.
See [LuauTypeCheckMode](/docs/reference/engine/enums/LuauTypeCheckMode.md) for the available modes.

### Property: Workspace.MeshPartHeadsAndAccessories

```json
{
  "type": "MeshPartHeadsAndAccessories",
  "access": "ReadWrite",
  "security": {
    "read": "None",
    "write": "None"
  },
  "serialization": {
    "can_load": true,
    "can_save": true
  },
  "thread_safety": "ReadSafe",
  "category": "Behavior"
}
```

Sets whether character Heads and Accessories should be downloaded as
[MeshParts](/docs/reference/engine/classes/MeshPart.md). The `Default` value is the same as `Enabled`.
If this feature is enabled, built-in avatars will use
[MeshParts](/docs/reference/engine/classes/MeshPart.md) for the character's head and accessories.

### Property: Workspace.MeshStreamingAndImprovedLods

```json
{
  "type": "RolloutState",
  "access": "ReadWrite",
  "security": {
    "read": "None",
    "write": "None"
  },
  "serialization": {
    "can_load": true,
    "can_save": true
  },
  "thread_safety": "ReadSafe",
  "category": "Behavior"
}
```

This [RolloutState](/docs/reference/engine/enums/RolloutState.md) property determines whether the experience uses
the new mesh streaming and Wild Mesh Simplifier LOD system. When set to
[Enabled](/docs/reference/engine/enums/RolloutState.md), mesh requests fetch the lowest quality LOD
first and stream in higher detail over time. When set to
[Disabled](/docs/reference/engine/enums/RolloutState.md), the legacy mesh loading behavior is used.
[Default](/docs/reference/engine/enums/RolloutState.md) follows the current engine-wide rollout state.

### Property: Workspace.ModelStreamingBehavior

```json
{
  "type": "ModelStreamingBehavior",
  "access": "ReadWrite",
  "security": {
    "read": "None",
    "write": "None"
  },
  "serialization": {
    "can_load": true,
    "can_save": true
  },
  "thread_safety": "ReadSafe",
  "category": "Streaming"
}
```

This [ModelStreamingBehavior](/docs/reference/engine/enums/ModelStreamingBehavior.md) property controls how
[Models](/docs/reference/engine/classes/Model.md) are replicated in experiences when instance streaming
is enabled.

### Property: Workspace.NextGenerationReplication

```json
{
  "type": "RolloutState",
  "access": "ReadWrite",
  "security": {
    "read": "None",
    "write": "None"
  },
  "serialization": {
    "can_load": true,
    "can_save": true
  },
  "thread_safety": "ReadSafe",
  "category": "Behavior"
}
```

When `true`, enables an alternate replication system that alters and
improves how properties are replicated under the hood; note that when
`true`, you should not rely on the ordering of property replication and
remote events.

### Property: Workspace.NextGenerationReplicationAlias

```json
{
  "type": "RolloutState",
  "access": "ReadOnly",
  "security": {
    "read": "RobloxEngineSecurity",
    "write": "RobloxEngineSecurity"
  },
  "serialization": {
    "can_load": false,
    "can_save": false
  },
  "thread_safety": "ReadSafe",
  "category": "Server Authority"
}
```

### Property: Workspace.PathfindingUseImprovedSearch

```json
{
  "type": "PathfindingUseImprovedSearch",
  "access": "ReadWrite",
  "security": {
    "read": "None",
    "write": "None"
  },
  "serialization": {
    "can_load": true,
    "can_save": true
  },
  "thread_safety": "ReadSafe",
  "category": "Behavior"
}
```

When [Enabled](/docs/reference/engine/enums/PathfindingUseImprovedSearch.md),
[PathfindingService](/docs/reference/engine/classes/PathfindingService.md) uses an improved pathfinding algorithm.
[Default](/docs/reference/engine/enums/PathfindingUseImprovedSearch.md) follows the current
engine-wide rollout state.

### Property: Workspace.PhysicsSteppingMethod

```json
{
  "type": "PhysicsSteppingMethod",
  "access": "ReadWrite",
  "security": {
    "read": "None",
    "write": "None"
  },
  "serialization": {
    "can_load": true,
    "can_save": true
  },
  "thread_safety": "ReadSafe",
  "category": "Behavior"
}
```

Sets how the solver will advance the physics simulation forward in time.
This option cannot be set through developer-facing Luau and must be set
from the **PhysicsSteppingMethod** property of **Workspace** within
Studio. See
[Adaptive Timestepping](/docs/en-us/physics/adaptive-timestepping.md) for
details.

Note that when assemblies of different simulation rates become connected
via [Constraints](/docs/reference/engine/classes/Constraint.md) or collisions, the combined mechanism
will default to the highest simulation rate for stability.

### Property: Workspace.PlayerCharacterDestroyBehavior

```json
{
  "type": "PlayerCharacterDestroyBehavior",
  "access": "ReadWrite",
  "security": {
    "read": "None",
    "write": "None"
  },
  "serialization": {
    "can_load": true,
    "can_save": true
  },
  "thread_safety": "ReadSafe",
  "category": "Behavior"
}
```

When enabled, the engine automatically calls `Destroy()` on a player's old
character when it is replaced (for example, on respawn) and on the
[Player](/docs/reference/engine/classes/Player.md) object itself when the player leaves the server.

### Property: Workspace.PlayerScriptsUseInputActionSystem

```json
{
  "type": "RolloutState",
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
  "category": "Behavior"
}
```

Controls whether the built-in player scripts are updated to use the
[Input Action System](/docs/en-us/input/input-action-system.md). When
enabled, the player scripts live under [StarterPlayer](/docs/reference/engine/classes/StarterPlayer.md) (controlled
by [StarterPlayer.CreateDefaultPlayerModule](/docs/reference/engine/classes/StarterPlayer.md)) and the server is able
to process player inputs.

### Property: Workspace.PlayerScriptsUseInputActionSystemAlias

```json
{
  "type": "RolloutState",
  "access": "ReadOnly",
  "security": {
    "read": "RobloxEngineSecurity",
    "write": "RobloxEngineSecurity"
  },
  "serialization": {
    "can_load": false,
    "can_save": false
  },
  "thread_safety": "ReadSafe",
  "category": "Server Authority"
}
```

### Property: Workspace.PredictiveStreamingMode

```json
{
  "type": "PredictiveStreamingMode",
  "access": "ReadWrite",
  "security": {
    "read": "None",
    "write": "None"
  },
  "serialization": {
    "can_load": true,
    "can_save": true
  },
  "thread_safety": "ReadSafe",
  "category": "Streaming",
  "capabilities": [
    "PluginOrOpenCloud"
  ]
}
```

When enabled, the engine can prepare content for anticipated changes to a
player's replication focus. This includes movement along likely paths,
predicted spawn locations, and large changes in focus position.
[Default](/docs/reference/engine/enums/PredictiveStreamingMode.md) currently behaves like
[Disabled](/docs/reference/engine/enums/PredictiveStreamingMode.md).

### Property: Workspace.RejectCharacterDeletions

```json
{
  "type": "RejectCharacterDeletions",
  "access": "ReadWrite",
  "security": {
    "read": "None",
    "write": "None"
  },
  "serialization": {
    "can_load": true,
    "can_save": true
  },
  "thread_safety": "ReadSafe",
  "category": "Networking"
}
```

When enabled, the server ignores client requests to delete player
[character](/docs/reference/engine/classes/Model.md) objects from the workspace, preventing exploits
that attempt to abuse this replication path.
[Default](/docs/reference/engine/enums/RejectCharacterDeletions.md) is currently equivalent to
`Enabled`.

### Property: Workspace.RenderingCacheOptimizations

```json
{
  "type": "RenderingCacheOptimizationMode",
  "access": "ReadWrite",
  "security": {
    "read": "None",
    "write": "None"
  },
  "serialization": {
    "can_load": true,
    "can_save": true
  },
  "thread_safety": "ReadSafe",
  "category": "Behavior",
  "capabilities": [
    "Physics"
  ]
}
```

Controls whether the engine caches rendering state data to reduce
redundant per-frame work. When enabled, the renderer can skip recomputing
state for static objects, improving frame rates in scenes with many parts.

### Property: Workspace.ReplicateInstanceDestroySetting

```json
{
  "type": "ReplicateInstanceDestroySetting",
  "access": "ReadWrite",
  "security": {
    "read": "None",
    "write": "None"
  },
  "serialization": {
    "can_load": true,
    "can_save": true
  },
  "thread_safety": "ReadSafe",
  "category": "Behavior"
}
```

Determines the replication behavior when `Instance:Destroy()` is called on
the server. When [Enabled](/docs/reference/engine/enums/ReplicateInstanceDestroySetting.md), the
engine uses improved replication semantics for instance destruction.

### Property: Workspace.Retargeting

```json
{
  "type": "AnimatorRetargetingMode",
  "access": "ReadWrite",
  "security": {
    "read": "None",
    "write": "None"
  },
  "serialization": {
    "can_load": true,
    "can_save": true
  },
  "thread_safety": "ReadSafe",
  "category": "Behavior",
  "capabilities": [
    "Animation"
  ]
}
```

Sets the animation retargeting mode. Retargeting adapts animations to
character rigs of different proportions, allowing a single animation to
play correctly on characters of varying sizes and shapes.

### Property: Workspace.SandboxedInstanceMode

```json
{
  "type": "SandboxedInstanceMode",
  "access": "ReadWrite",
  "security": {
    "read": "None",
    "write": "None"
  },
  "serialization": {
    "can_load": true,
    "can_save": true
  },
  "thread_safety": "ReadSafe",
  "category": "Permissions"
}
```

When set to [Experimental](/docs/reference/engine/enums/SandboxedInstanceMode.md), the engine enables
sandboxed instance mode, which lets you use script capabilities.

### Property: Workspace.SignalBehavior

```json
{
  "type": "SignalBehavior",
  "access": "ReadWrite",
  "security": {
    "read": "None",
    "write": "None"
  },
  "serialization": {
    "can_load": false,
    "can_save": false
  },
  "thread_safety": "ReadSafe",
  "category": "Behavior"
}
```

This property determines whether event handlers will be resumed
immediately when the event fires, or deferred and then resumed at a later
resumption point. Resumption points currently include:

- Input processing (resumes once per input to be processed, see
  [UserInputService](/docs/reference/engine/classes/UserInputService.md))
- [RunService.PreRender](/docs/reference/engine/classes/RunService.md)
- Legacy waiting script resumption such as `wait()`, `spawn()`, and
  `delay()`
- [RunService.PreAnimation](/docs/reference/engine/classes/RunService.md)
- [RunService.PreSimulation](/docs/reference/engine/classes/RunService.md)
- [RunService.PostSimulation](/docs/reference/engine/classes/RunService.md)
- Waiting script resumption such as [task.wait()](/docs/reference/engine/globals/task.md),
  [task.spawn()](/docs/reference/engine/globals/task.md), and [task.delay()](/docs/reference/engine/globals/task.md)
- [RunService.Heartbeat](/docs/reference/engine/classes/RunService.md)
- [DataModel.BindToClose](/docs/reference/engine/classes/DataModel.md)

For more information, see
[Deferred Events](/docs/en-us/scripting/events/deferred.md).

### Property: Workspace.SignalBehaviorAlias

```json
{
  "type": "SignalBehavior",
  "access": "ReadOnly",
  "security": {
    "read": "RobloxEngineSecurity",
    "write": "RobloxEngineSecurity"
  },
  "serialization": {
    "can_load": false,
    "can_save": false
  },
  "thread_safety": "ReadSafe",
  "category": "Server Authority"
}
```

### Property: Workspace.StreamingEnabled

```json
{
  "type": "boolean",
  "access": "ReadWrite",
  "security": {
    "read": "None",
    "write": "None"
  },
  "serialization": {
    "can_load": true,
    "can_save": true
  },
  "thread_safety": "ReadSafe",
  "category": "Streaming"
}
```

This property determines whether in-experience content streaming is
enabled for the place. This property is not scriptable and therefore must
be set on the `Workspace` object in Studio.

#### See also

- [Workspace.StreamingMinRadius](/docs/reference/engine/classes/Workspace.md)
- [Workspace.StreamingTargetRadius](/docs/reference/engine/classes/Workspace.md)
- [Workspace.StreamingIntegrityMode](/docs/reference/engine/classes/Workspace.md)

### Property: Workspace.StreamingEnabledAlias

```json
{
  "type": "boolean",
  "access": "ReadOnly",
  "security": {
    "read": "RobloxEngineSecurity",
    "write": "RobloxEngineSecurity"
  },
  "serialization": {
    "can_load": false,
    "can_save": false
  },
  "thread_safety": "ReadSafe",
  "category": "Server Authority"
}
```

### Property: Workspace.StreamingIntegrityMode

```json
{
  "type": "StreamingIntegrityMode",
  "access": "ReadWrite",
  "security": {
    "read": "None",
    "write": "None"
  },
  "serialization": {
    "can_load": true,
    "can_save": true
  },
  "thread_safety": "ReadSafe",
  "category": "Streaming",
  "capabilities": [
    "PluginOrOpenCloud"
  ]
}
```

If instance [streaming](/docs/en-us/workspace/streaming.md) is enabled,
an experience may behave in unintended ways if a player's character moves
into a region of the world that has not been streamed to their client. The
streaming integrity feature offers a way to avoid those potentially
problematic situations.

### Property: Workspace.StreamingMinRadius

```json
{
  "type": "int",
  "access": "ReadWrite",
  "security": {
    "read": "None",
    "write": "None"
  },
  "serialization": {
    "can_load": true,
    "can_save": true
  },
  "thread_safety": "ReadSafe",
  "category": "Streaming",
  "capabilities": [
    "PluginOrOpenCloud"
  ]
}
```

This property indicates the radius around the player's character or the
current [ReplicationFocus](/docs/reference/engine/classes/Player.md) in which content
will be streamed in at the highest priority. Defaults to 64 studs.

Care should be taken when increasing the default minimum radius since
doing so will require more memory and more server bandwidth at the expense
of other components.

#### See also

- [Workspace.StreamingEnabled](/docs/reference/engine/classes/Workspace.md) which controls whether content
  streaming is enabled
- [Workspace.StreamingTargetRadius](/docs/reference/engine/classes/Workspace.md)
- [Workspace.StreamingIntegrityMode](/docs/reference/engine/classes/Workspace.md)

### Property: Workspace.StreamingTargetRadius

```json
{
  "type": "int",
  "access": "ReadWrite",
  "security": {
    "read": "None",
    "write": "None"
  },
  "serialization": {
    "can_load": true,
    "can_save": true
  },
  "thread_safety": "ReadSafe",
  "category": "Streaming",
  "capabilities": [
    "PluginOrOpenCloud"
  ]
}
```

This property controls the maximum distance away from the player's
character or the current [ReplicationFocus](/docs/reference/engine/classes/Player.md)
in which content will be streamed in. Defaults to 1024 studs.

Note that the engine is allowed to retain previously loaded content beyond
the target radius, memory permitting.

#### See also

- [Workspace.StreamingEnabled](/docs/reference/engine/classes/Workspace.md) which controls whether content
  streaming is enabled
- [Workspace.StreamingMinRadius](/docs/reference/engine/classes/Workspace.md)
- [Workspace.StreamingIntegrityMode](/docs/reference/engine/classes/Workspace.md)

### Property: Workspace.StreamOutBehavior

```json
{
  "type": "StreamOutBehavior",
  "access": "ReadWrite",
  "security": {
    "read": "None",
    "write": "None"
  },
  "serialization": {
    "can_load": true,
    "can_save": true
  },
  "thread_safety": "ReadSafe",
  "category": "Streaming",
  "capabilities": [
    "PluginOrOpenCloud"
  ]
}
```

This property controls where content will be unloaded from the
[ReplicationFocus](/docs/reference/engine/classes/Player.md) based on device memory
conditions, or based on the streaming radius.

#### See also

- [Workspace.StreamingEnabled](/docs/reference/engine/classes/Workspace.md) which controls whether content
  streaming is enabled
- [Workspace.StreamingMinRadius](/docs/reference/engine/classes/Workspace.md)
- [Workspace.StreamingTargetRadius](/docs/reference/engine/classes/Workspace.md)
- [Workspace.StreamingIntegrityMode](/docs/reference/engine/classes/Workspace.md)

### Property: Workspace.Terrain

```json
{
  "type": "Terrain",
  "access": "ReadWrite",
  "security": {
    "read": "None",
    "write": "None"
  },
  "serialization": {
    "can_load": false,
    "can_save": false
  },
  "thread_safety": "ReadSafe",
  "category": "Behavior"
}
```

This property is a reference to the [Terrain](/docs/reference/engine/classes/Terrain.md) object parented to the
[Workspace](/docs/reference/engine/classes/Workspace.md).

![Terrain object within the Workspace hierarchy](/assets/studio/explorer/Workspace-Terrain.png)

See [Environmental Terrain](/docs/en-us/parts/terrain.md) for more
information.

### Property: Workspace.TouchesUseCollisionGroups

```json
{
  "type": "boolean",
  "access": "ReadWrite",
  "security": {
    "read": "None",
    "write": "None"
  },
  "serialization": {
    "can_load": true,
    "can_save": true
  },
  "thread_safety": "ReadSafe",
  "category": "Behavior"
}
```

This property determines whether [parts](/docs/reference/engine/classes/BasePart.md) in different
groups set to not collide will ignore collisions and touch events. By
default, the value of this property is set to `false`.

When this property is enabled, parts in different groups set to not
collide will also ignore the [CanTouch](/docs/reference/engine/classes/BasePart.md) property,
similar to how [BasePart.CanCollide](/docs/reference/engine/classes/BasePart.md) is ignored. For more
information on the behavior of CanTouch, please visit its property page.

### Property: Workspace.UseFixedSimulation

```json
{
  "type": "RolloutState",
  "access": "ReadWrite",
  "security": {
    "read": "None",
    "write": "None"
  },
  "serialization": {
    "can_load": true,
    "can_save": true
  },
  "thread_safety": "ReadSafe",
  "category": "Behavior"
}
```

When `true`, enables [RunService:BindToSimulation()](/docs/reference/engine/classes/RunService.md) which calls a
function at a fixed frequency. Also updates physics stepping logic such
that character controller updates and joint transforms are performed at a
fixed frequency rather than once per frame, as well as makes the
[RobloxGlobals.time()](/docs/reference/engine/globals/RobloxGlobals.md) function return the fixed stepped frame
time.

### Property: Workspace.UseFixedSimulationAlias

```json
{
  "type": "RolloutState",
  "access": "ReadOnly",
  "security": {
    "read": "RobloxEngineSecurity",
    "write": "RobloxEngineSecurity"
  },
  "serialization": {
    "can_load": false,
    "can_save": false
  },
  "thread_safety": "ReadSafe",
  "category": "Server Authority"
}
```

### Property: Workspace.UseNewLuauTypeSolver

```json
{
  "type": "RolloutState",
  "access": "ReadWrite",
  "security": {
    "read": "None",
    "write": "None"
  },
  "serialization": {
    "can_load": true,
    "can_save": true
  },
  "thread_safety": "ReadSafe",
  "category": "Scripting"
}
```

This [RolloutState](/docs/reference/engine/enums/RolloutState.md) property controls whether the new Luau type
solver is used for type inference and type checking in scripts. The new
type solver provides improved accuracy and performance for type analysis.
Note that [Workspace.LuauTypeCheckMode](/docs/reference/engine/classes/Workspace.md) controls the mode (strict,
nonstrict, etc.) while this property controls which solver implementation
is active. [Default](/docs/reference/engine/enums/RolloutState.md) follows the current engine-wide
rollout state.

### Property: Workspace.FilteringEnabled *(hidden)*

```json
{
  "type": "boolean",
  "access": "ReadOnly",
  "security": {
    "read": "None",
    "write": "PluginSecurity"
  },
  "serialization": {
    "can_load": false,
    "can_save": false
  },
  "deprecated": true,
  "thread_safety": "ReadSafe",
  "category": "Behavior",
  "capabilities": [
    "Basic"
  ]
}
```

> **Deprecated:** This property is discontinued.

This property is discontinued and no longer takes effect.

### Property: Workspace.InterpolationThrottling *(hidden)*

```json
{
  "type": "InterpolationThrottlingMode",
  "access": "ReadOnly",
  "security": {
    "read": "None",
    "write": "PluginSecurity"
  },
  "serialization": {
    "can_load": false,
    "can_save": false
  },
  "deprecated": true,
  "thread_safety": "ReadSafe",
  "category": "Behavior",
  "capabilities": [
    "Physics"
  ]
}
```

> **Deprecated:** This property should not be used for new work.

This property has `Physics` read security and `Plugin` write security. It
is hidden in the Studio Properties window. Do not use it for new work.

## Methods

### Method: Workspace:ApplyRecommendedStreamingSettings

**Signature:** `Workspace:ApplyRecommendedStreamingSettings(): boolean`

Applies the current recommended instance streaming settings to the
[Workspace](/docs/reference/engine/classes/Workspace.md). Only settings that differ from their recommended values
are changed.

*Security: PluginSecurity · Thread Safety: Unsafe*

**Returns:** `boolean` — `true` if one or more streaming properties were changed; `false` if
every value already matched its recommended setting.

### Method: Workspace:GetNumAwakeParts

**Signature:** `Workspace:GetNumAwakeParts(): int`

Returns the number of [BaseParts](/docs/reference/engine/classes/BasePart.md) that are deemed
physically active, due to being recently under the influence of physics.

This function provides a measure of how many [BaseParts](/docs/reference/engine/classes/BasePart.md)
are being influenced by, or recently under the influence of, physical
forces.

```
local Workspace = game:GetService("Workspace")

print(Workspace:GetNumAwakeParts())
```

In order to ensure good performance, the engine sets
[BaseParts](/docs/reference/engine/classes/BasePart.md) in which physics are not being applied to a
"sleeping" state. [BaseParts](/docs/reference/engine/classes/BasePart.md) with
[BasePart.Anchored](/docs/reference/engine/classes/BasePart.md) set to `true`, for example, will always be
sleeping as physics doesn't apply to them. When a force is applied to a
non‑anchored [BasePart](/docs/reference/engine/classes/BasePart.md), an "awake" state will be applied. Whilst a
[BasePart](/docs/reference/engine/classes/BasePart.md) is awake, the physics engine will perform continuous
calculations to ensure physical forces interact correctly with the part.
Once the [BasePart](/docs/reference/engine/classes/BasePart.md) is no longer subject to physical forces, it will
revert to a "sleeping" state.

*Security: None · Thread Safety: Safe · Capabilities: Basic*

**Returns:** `int` — The number of awake parts.

### Method: Workspace:GetPhysicsThrottling

**Signature:** `Workspace:GetPhysicsThrottling(): int`

Returns an integer, between `0` and `100`, representing the percentage of
real time that physics simulation is currently being throttled to. Physics
throttling occurs when the physics engine detects it cannot keep up with
the game in real time. When physics is being throttled, it will update
less frequently causing [BaseParts](/docs/reference/engine/classes/BasePart.md) to appear to move
slower.

Objects associated with [Humanoids](/docs/reference/engine/classes/Humanoid.md) are exempt from physics
throttling.

#### See also

- [Workspace:SetPhysicsThrottleEnabled()](/docs/reference/engine/classes/Workspace.md).

*Security: None · Thread Safety: Safe · Capabilities: Basic*

**Returns:** `int` — The percentage of real time that physics simulation is currently being
throttled to.

### Method: Workspace:GetRealPhysicsFPS

**Signature:** `Workspace:GetRealPhysicsFPS(): double`

Returns the number of frames per second that physics is currently being
simulated at.

#### Using GetRealPhysicsFPS to combat exploiters

A common use of this function is to detect if exploiters are increasing
their local physics frame rate to move faster. This is generally done by
comparing the result returned by a client's GetRealPhysicsFPS to a maximum
that will not be breached in normal circumstances (usually 65 or 70). If
this limit is breached, developers can use the [Player:Kick()](/docs/reference/engine/classes/Player.md)
function to remove that [Player](/docs/reference/engine/classes/Player.md) from the game. It is important to
remember that, although this practice may be effective sometimes,
client-side anti-exploiter measures are never 100% reliable.

*Security: None · Thread Safety: Safe · Capabilities: Basic*

**Returns:** `double` — Returns the number of frames per second that physics is currently
being simulated at.

**Workspace:GetRealPhysicsFPS**

Speed exploiters commonly increase their local physics FPS in order to
increase their character speed. This can be detected from a LocalScript by
checking if the player's physics FPS is over the maximum:

```lua
local Players = game:GetService("Players")

local player = Players.LocalPlayer

while task.wait(1) do
	if workspace:GetRealPhysicsFPS() > 65 then
		player:Kick()
	end
end
```

### Method: Workspace:GetServerTimeNow

**Signature:** `Workspace:GetServerTimeNow(): double`

This method returns the client's best approximation of the current time on
the server. It is useful for creating synchronized experiences, as every
client will get roughly the same results regardless of their timezone or
local clock.

This method returns a Unix timestamp, similar to [os.time()](/docs/reference/engine/globals/os.md),
that you can use with [os.date()](/docs/reference/engine/globals/os.md) or
[DateTime.fromUnixTimestamp()](/docs/reference/engine/datatypes/DateTime.md). The timestamp is smoothed so
that:

- It is monotonic; its value will never decrease.
- It moves at the same rate as the local clock to within 0.6%.

This method is useful for making sure an event starts at the right
real-world time and for periodic adjustments to keep a series of events in
sync. For benchmarking or other use cases that require higher precision,
consider [os.clock()](/docs/reference/engine/globals/os.md).

This method relies on the server, so calling it from a client that isn't
connected will throw an error. Also note that this method is not suitable
for things like timed rewards, as it is not secure compared to tracking
such timers on the server.

#### See also

- [DistributedGameTime](/docs/reference/engine/classes/Workspace.md), a game-time
  clock
- [os.time()](/docs/reference/engine/globals/os.md)
- [DateTime](/docs/reference/engine/datatypes/DateTime.md)

*Security: None · Thread Safety: Safe · Capabilities: Basic*

**Returns:** `double` — The estimated Unix timestamp on the server.

### Method: Workspace:JoinToOutsiders

**Signature:** `Workspace:JoinToOutsiders(objects: Instances, jointType: JointCreationMode): ()`

This function creates joints between the specified [Parts](/docs/reference/engine/classes/BasePart.md)
and any touching parts depending on the parts' surfaces and the specified
joint creation mode.

This function creates joints between the specified Parts and any planar
touching surfaces, depending on the parts' surfaces and the specified
joint creation mode.

- Glue, Studs, Inlets, Universal, Weld, and Smooth surfaces will all
  create Weld instances.
- Spheres will not surface-weld to anything. The rounded sides of
  cylinders will not surface-weld, but the flat end sides will.
- Hinge and Motor surfaces will still create [Rotate](/docs/reference/engine/classes/Rotate.md) and
  [RotateP](/docs/reference/engine/classes/RotateP.md) joint instances, regardless of part shape.

The first parameter is an array of [BaseParts](/docs/reference/engine/classes/BasePart.md). Joints will
only be created between the parts in the array and not in the array.
Joints will not be created between the parts in the array.

The second parameter is a [JointCreationMode](/docs/reference/engine/enums/JointCreationMode.md) that determines how
joints will be created. Passing in either enum value,
[Enum.JointCreationMode.All](/docs/reference/engine/enums/JointCreationMode.md) or
[Enum.JointCreationMode.Surface](/docs/reference/engine/enums/JointCreationMode.md), has the same
behavior which equates to Join Always

This function is used by the Roblox Studio **Move** tool when the user
finishes moving a selection. In conjunction with
[Plugin:GetJoinMode()](/docs/reference/engine/classes/Plugin.md) and [Workspace:UnjoinFromOutsiders()](/docs/reference/engine/classes/Workspace.md)
it can be used to retain join functionality when developing custom studio
build tools. See the snippets below for an example.

```lua
local Workspace = game:GetService("Workspace")

-- Finished moving a selection; make joints
local function finishedMovingParts(parts)
	local joinMode = Plugin:GetJoinMode()
	Workspace:JoinToOutsiders(parts, joinMode)
end
```

```lua
local Workspace = game:GetService("Workspace")

-- Started moving a selection; break joints
local function startMovingParts(parts)
	Workspace:UnjoinFromOutsiders(parts)
end
```

*Security: None · Thread Safety: Unsafe · Capabilities: Physics*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `objects` | `Instances` |  | An array of [BaseParts](/docs/reference/engine/classes/BasePart.md) for whom joints are to be made. |
| `jointType` | `JointCreationMode` |  | The [JointCreationMode](/docs/reference/engine/enums/JointCreationMode.md) to be used. Passing in [Enum.JointCreationMode.All](/docs/reference/engine/enums/JointCreationMode.md) or [Enum.JointCreationMode.Surface](/docs/reference/engine/enums/JointCreationMode.md) has the same behavior which equates to Join Always. |

**Returns:** `()`

### Method: Workspace:PGSIsEnabled

**Signature:** `Workspace:PGSIsEnabled(): boolean`

Returns `true` if the game has the PGS Physics solver enabled.

As [Workspace.PGSPhysicsSolverEnabled](/docs/reference/engine/classes/Workspace.md) cannot be accessed by
scripts, the PGSIsEnabled function allows developers to tell which physics
solver the game is using.

*Security: None · Thread Safety: Unsafe · Capabilities: Basic*

**Returns:** `boolean` — True if the PGS solver is enabled.

### Method: Workspace:UnjoinFromOutsiders

**Signature:** `Workspace:UnjoinFromOutsiders(objects: Instances): ()`

Breaks all joints between the specified [BaseParts](/docs/reference/engine/classes/BasePart.md) and
other [BaseParts](/docs/reference/engine/classes/BasePart.md).

This function requires an array of [BaseParts](/docs/reference/engine/classes/BasePart.md). Note,
joints will not be broken between these [BaseParts](/docs/reference/engine/classes/BasePart.md) (each
other), only between these [BaseParts](/docs/reference/engine/classes/BasePart.md) and other
[BaseParts](/docs/reference/engine/classes/BasePart.md) not in the array.

This function is used by the Roblox Studio **Move** tool when the user
starts moving a selection. In conjunction with
[Plugin:GetJoinMode()](/docs/reference/engine/classes/Plugin.md) and [Workspace:JoinToOutsiders()](/docs/reference/engine/classes/Workspace.md) it
can be used to retain join functionality when developing custom Studio
build tools. See the snippets below for an example.

```
local Workspace = game:GetService("Workspace")

-- Finished moving a selection; make joints
local function finishedMovingParts(parts)
	local joinMode = Plugin:GetJoinMode()
	Workspace:JoinToOutsiders(parts, joinMode)
end
```

```
local Workspace = game:GetService("Workspace")

-- Started moving a selection; break joints
local function startMovingParts(parts)
	Workspace:UnjoinFromOutsiders(parts)
end
```

*Security: None · Thread Safety: Unsafe · Capabilities: Physics*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `objects` | `Instances` |  | An array of [BaseParts](/docs/reference/engine/classes/BasePart.md) for whom joints are to be broken. |

**Returns:** `()`

### Method: Workspace:ZoomToExtents

**Signature:** `Workspace:ZoomToExtents(): ()`

Positions and zooms the [Workspace.CurrentCamera](/docs/reference/engine/classes/Workspace.md) to show the extent
of [BaseParts](/docs/reference/engine/classes/BasePart.md) currently in the [Workspace](/docs/reference/engine/classes/Workspace.md). It
exhibits similar behavior to the "focus" command but it shows the extents
of the [Workspace](/docs/reference/engine/classes/Workspace.md) rather than the currently selected object.

This function cannot be used in developer-facing Luau but will function in
the Command Bar or plugins.

*Security: PluginSecurity · Thread Safety: Unsafe*

**Returns:** `()`

### Method: Workspace:BreakJoints

**Signature:** `Workspace:BreakJoints(objects: Instances): ()`

> **Deprecated:** This method is deprecated. Do not use it for new work.

Goes through all [BaseParts](/docs/reference/engine/classes/BasePart.md) given, breaking any joints
connected to these parts. This function will break any of the following
types of joints:

- [JointInstances](/docs/reference/engine/classes/JointInstance.md) such as [Welds](/docs/reference/engine/classes/Weld.md)
- [WeldConstraints](/docs/reference/engine/classes/WeldConstraint.md)

Unlike [Model:MakeJoints()](/docs/reference/engine/classes/Model.md), this function requires an array of
[BaseParts](/docs/reference/engine/classes/BasePart.md) as a parameter. This array is given as follows:

```lua
local Workspace = game:GetService("Workspace")

Workspace:BreakJoints({part1, part2, part3})
```

Note, this function cannot be used in developer-facing Luau and will only
function in plugins.

*Security: PluginSecurity · Thread Safety: Unsafe*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `objects` | `Instances` |  | An array of [BaseParts](/docs/reference/engine/classes/BasePart.md) for whom joints are to be broken. |

**Returns:** `()`

### Method: Workspace:MakeJoints

**Signature:** `Workspace:MakeJoints(objects: Instances): ()`

> **Deprecated:** This method is deprecated. Do not use it for new work.

**Deprecated**

SurfaceType based joining is deprecated, do not use MakeJoints for new
projects. [WeldConstraints](/docs/reference/engine/classes/WeldConstraint.md) and
[HingeConstraints](/docs/reference/engine/classes/HingeConstraint.md) should be used instead.

Goes through all [Parts](/docs/reference/engine/classes/BasePart.md) given. If any part's side has a
[SurfaceType](/docs/reference/engine/enums/SurfaceType.md) that can make a joint it will create a joint with any
adjacent parts.

Joints will be created between the specified Parts and any planar touching
surfaces, depending on the parts' surfaces.

- Smooth surfaces will not create joints
- Glue surfaces will create a [Glue](/docs/reference/engine/classes/Glue.md) joint
- Weld will create a [Weld](/docs/reference/engine/classes/Weld.md) joint with any surface except for
  Unjoinable
- Studs, Inlet, or Universal will each create a [Snap](/docs/reference/engine/classes/Snap.md) joint with
  either of other the other two surfaces (e.g. Studs with Inlet and
  Universal)
- Hinge and Motor surfaces create [Rotate](/docs/reference/engine/classes/Rotate.md) and [RotateV](/docs/reference/engine/classes/RotateV.md) joint
  instances

Unlike [Model:MakeJoints()](/docs/reference/engine/classes/Model.md), this function requires an array of
parts as a parameter. This array is given as follows:

```
local Workspace = game:GetService("Workspace")

Workspace:MakeJoints({part1, part2, part3})
```

Joints are broken if enough force is applied to them due to an
[Explosion](/docs/reference/engine/classes/Explosion.md), unless a [ForceField](/docs/reference/engine/classes/ForceField.md) object is parented to the
[BasePart](/docs/reference/engine/classes/BasePart.md) or ancestor [Model](/docs/reference/engine/classes/Model.md). For this reason, they are
often used to make simple destructible buildings and other models.

*Security: PluginSecurity · Thread Safety: Unsafe*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `objects` | `Instances` |  | An array of [parts](/docs/reference/engine/classes/BasePart.md) for whom joints are to be made. |

**Returns:** `()`

## Events

### Event: Workspace.PersistentLoaded

**Signature:** `Workspace.PersistentLoaded(player: Player)`

This event fires every time a player has been sent all current persistent
models and part-less atomic models. The `player` parameter indicates which
player has received all applicable instances.

Note that experience loading happens before persistent loading, and firing
of the [DataModel.Loaded](/docs/reference/engine/classes/DataModel.md) event does not indicate that all
persistent models are present.

*Security: None*

**Parameters:**

| Name | Type | Description |
|------|------|-------------|
| `player` | `Player` | The player who has received all current persistent models and part-less atomic models. |

## Inherited Members

### From [WorldRoot](/docs/reference/engine/classes/WorldRoot.md)

- **Method `ArePartsTouchingOthers(partList: Instances, overlapIgnored?: float): boolean`**: Returns true if any of the given BasePart are touching any other
- **Method `Blockcast(cframe: CFrame, size: Vector3, direction: Vector3, params?: RaycastParams): RaycastResult?`**: Casts a block shape in a given direction and returns a
- **Method `BulkMoveTo(partList: Instances, cframeList: Array, eventMode?: BulkMoveMode): ()`**: Moves an array of BaseParts to an array of
- **Method `CollisionGroupsAreCollidable(name1: string, name2: string): boolean`**: Returns whether the two groups will collide in this world.
- **Method `CollisionGroupSetCollidable(name1: string, name2: string, collidable: boolean): ()`**: Sets the collision status between two groups in this world.
- **Method `FindPartOnRay(ray: Ray, ignoreDescendantsInstance?: Instance, terrainCellsAreCubes?: boolean, ignoreWater?: boolean): Tuple`**: Returns the first BasePart or Terrain cell intersecting *(deprecated)*
- **Method `findPartOnRay(ray: Ray, ignoreDescendantsInstance?: Instance, terrainCellsAreCubes?: boolean, ignoreWater?: boolean): Tuple`**:  *(deprecated)*
- **Method `FindPartOnRayWithIgnoreList(ray: Ray, ignoreDescendantsTable: Instances, terrainCellsAreCubes?: boolean, ignoreWater?: boolean): Tuple`**: Returns the first BasePart or Terrain cell intersecting *(deprecated)*
- **Method `FindPartOnRayWithWhitelist(ray: Ray, whitelistDescendantsTable: Instances, ignoreWater?: boolean): Tuple`**: Returns the first BasePart or Terrain cell intersecting *(deprecated)*
- **Method `FindPartsInRegion3(region: Region3, ignoreDescendantsInstance?: Instance, maxParts?: int): List<BasePart>`**: Returns an array of BaseParts in the given *(deprecated)*
- **Method `findPartsInRegion3(region: Region3, ignoreDescendantsInstance?: Instance, maxParts?: int): List<BasePart>`**:  *(deprecated)*
- **Method `FindPartsInRegion3WithIgnoreList(region: Region3, ignoreDescendantsTable: Instances, maxParts?: int): List<BasePart>`**: Returns an array of BaseParts in the given *(deprecated)*
- **Method `FindPartsInRegion3WithWhiteList(region: Region3, whitelistDescendantsTable: Instances, maxParts?: int): List<BasePart>`**: Returns an array of BaseParts in the given *(deprecated)*
- **Method `GetMaxCollisionGroups(): int`**: Returns the maximum number of collision groups in this world.
- **Method `GetPartBoundsInBox(cframe: CFrame, size: Vector3, overlapParams?: OverlapParams): List<BasePart>`**: Returns an array of parts whose **bounding boxes** overlap a given box.
- **Method `GetPartBoundsInRadius(position: Vector3, radius: float, overlapParams?: OverlapParams): List<BasePart>`**: Returns an array of parts whose **bounding boxes** overlap a given sphere.
- **Method `GetPartsInPart(part: BasePart, overlapParams?: OverlapParams): List<BasePart>`**: Returns an array of parts whose occupied space is shared with the given
- **Method `GetRegisteredCollisionGroups(): Array`**: Returns a table with info on all of this world's collision groups.
- **Method `IKMoveTo(part: BasePart, target: CFrame, translateStiffness?: float, rotateStiffness?: float, collisionsMode?: IKCollisionsMode): ()`**: Moves the specified part to the specified location via inverse kinematics
- **Method `IsCollisionGroupRegistered(name: string): boolean`**: Checks if a collision group is registered in this world.
- **Method `IsRegion3Empty(region: Region3, ignoreDescendentsInstance?: Instance): boolean`**: Returns a bool indicating whether there are no BaseParts *(deprecated)*
- **Method `IsRegion3EmptyWithIgnoreList(region: Region3, ignoreDescendentsTable: Instances): boolean`**: Returns a boolean indicating whether there are no *(deprecated)*
- **Method `Raycast(origin: Vector3, direction: Vector3, raycastParams?: RaycastParams): RaycastResult?`**: Casts a ray using an origin, direction, and optional
- **Method `RegisterCollisionGroup(name: string): ()`**: Registers a new collision group in this world with the given name.
- **Method `RenameCollisionGroup(from: string, to: string): ()`**: Renames specified collision group in this world.
- **Method `Shapecast(part: BasePart, direction: Vector3, params?: RaycastParams, cframeOverride?: CFrame?, sizeOverride?: Vector3?): RaycastResult?`**: Casts the shape of a given BasePart in a direction and returns a
- **Method `Spherecast(position: Vector3, radius: float, direction: Vector3, params?: RaycastParams): RaycastResult?`**: Casts a spherical shape in a given direction and returns a
- **Method `StepPhysics(dt: float, parts?: Instances): ()`**: Advances the simulation for parts in the world forward based on a
- **Method `UnregisterCollisionGroup(name: string): ()`**: Unregisters the collision group for the given name in this world.

### From [Model](/docs/reference/engine/classes/Model.md)

- **Property `LevelOfDetail`** (`ModelLevelOfDetail`): Sets the level of detail on the model for experiences with instance
- **Property `ModelStreamingMode`** (`ModelStreamingMode`): Controls the model streaming behavior on Models when
- **Property `PrimaryPart`** (`BasePart`): The primary part of the Model, or `nil` if not explicitly set.
- **Property `Scale`** (`float`): Editor-only property used to scale the model around its pivot. Setting
- **Property `WorldPivot`** (`CFrame`): Determines where the pivot of a Model which does **not** have a
- **Method `AddPersistentPlayer(playerInstance?: Player): ()`**: Sets this model to be persistent for the specified player.
- **Method `BreakJoints(): ()`**: Breaks connections between `BaseParts`, including surface connections with *(deprecated)*
- **Method `breakJoints(): ()`**:  *(deprecated)*
- **Method `GetBoundingBox(): Tuple`**: Returns a description of a volume that contains all parts of a Model.
- **Method `GetExtentsSize(): Vector3`**: Returns the size of the smallest bounding box that contains all of the
- **Method `GetModelCFrame(): CFrame`**: This value historically returned the CFrame of a central position in the *(deprecated)*
- **Method `GetModelSize(): Vector3`**: Returns the Vector3 size of the Model. *(deprecated)*
- **Method `GetPersistentPlayers(): List<Player>`**: Returns all the Player objects that this model object is
- **Method `GetPrimaryPartCFrame(): CFrame`**: Returns the CFrame of the model's Model.PrimaryPart. *(deprecated)*
- **Method `GetScale(): float`**: Returns the canonical scale of the model, which defaults to 1 for newly
- **Method `MakeJoints(): ()`**: Goes through all BaseParts in the Model. If any *(deprecated)*
- **Method `makeJoints(): ()`**:  *(deprecated)*
- **Method `move(location: Vector3): ()`**:  *(deprecated)*
- **Method `MoveTo(position: Vector3): ()`**: Moves the PrimaryPart to the given position. If
- **Method `moveTo(location: Vector3): ()`**:  *(deprecated)*
- **Method `RemovePersistentPlayer(playerInstance?: Player): ()`**: Makes this model no longer persistent for the specified player.
- **Method `ResetOrientationToIdentity(): ()`**: Resets the rotation of the model's parts to the previously set identity *(deprecated)*
- **Method `ScaleTo(newScaleFactor: float): ()`**: Sets the scale factor of the model, adjusting the sizing and location of
- **Method `SetIdentityOrientation(): ()`**: Sets the identity rotation of the given model, allowing you to reset the *(deprecated)*
- **Method `SetPrimaryPartCFrame(cframe: CFrame): ()`**: Sets the BasePart.CFrame of the model's Model.PrimaryPart. *(deprecated)*
- **Method `TranslateBy(delta: Vector3): ()`**: Shifts a Model by the given Vector3 offset, preserving

### From [PVInstance](/docs/reference/engine/classes/PVInstance.md)

- **Property `Origin`** (`CFrame`): Editor-only property that reads and sets the world CFrame of
- **Property `Pivot Offset`** (`CFrame`): Editor-only property that displays and edits the pivot's CFrame
- **Method `GetPivot(): CFrame`**: Gets the pivot of a PVInstance.
- **Method `PivotTo(targetCFrame: CFrame): ()`**: Transforms the PVInstance along with all of its descendant

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