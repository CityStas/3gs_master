---
name: SpawnLocation
last_updated: 2026-10-30T19:55:53Z
inherits:
  - Part
  - FormFactorPart
  - BasePart
  - PVInstance
  - Instance
  - Object
type: class
memory_category: BaseParts
summary: "SpawnLocations, or \"spawns\" determine where a Player respawns when they die. They can be configured to allow only certain players to use each spawn, using Teams. They also control how ForceFields are set up for newly-spawned players."
---

# Class: SpawnLocation

> [SpawnLocations](/docs/reference/engine/classes/SpawnLocation.md), or "spawns" determine where a
> [Player](/docs/reference/engine/classes/Player.md) respawns when they die. They can be configured to allow only
> certain players to use each spawn, using [Teams](/docs/reference/engine/classes/Team.md). They also control
> how [ForceFields](/docs/reference/engine/classes/ForceField.md) are set up for newly-spawned players.

## Description

SpawnLocations, or "spawns" determine where a [Player](/docs/reference/engine/classes/Player.md) respawns when
they die. They can be configured to allow only certain players to use each
spawn, using [Teams](/docs/reference/engine/classes/Team.md). They also control how
[ForceFields](/docs/reference/engine/classes/ForceField.md) are set up for newly-spawned players.

SpawnLocations can be used as checkpoints, such as in an obstacle course,
using the [SpawnLocation.AllowTeamChangeOnTouch](/docs/reference/engine/classes/SpawnLocation.md) property, so that when
a player touches it, they will change teams to the SpawnLocation's team. In
this case, only the first [Team](/docs/reference/engine/classes/Team.md) should have [Team.AutoAssignable](/docs/reference/engine/classes/Team.md)
set to true, else players will not start at the first checkpoint.

Note if a SpawnLocation is added to the [Workspace](/docs/reference/engine/classes/Workspace.md) in Studio with
[SpawnLocation.Neutral](/docs/reference/engine/classes/SpawnLocation.md) set to false a Team will be created
corresponding to [SpawnLocation.TeamColor](/docs/reference/engine/classes/SpawnLocation.md) if it does not already exist.
This behavior does not occur when spawns are created in-game using a
[Script](/docs/reference/engine/classes/Script.md) or if the properties of the SpawnLocation are changed after
already being added. It is recommended that developers always set up their
teams manually and not rely on this behavior.

## Spawning Rules

There are several rules that come into play for a given SpawnLocation when a
player respawns:

- When [SpawnLocation.Neutral](/docs/reference/engine/classes/SpawnLocation.md) is set to false only
  [Players](/docs/reference/engine/classes/Player.md) with [Player.TeamColor](/docs/reference/engine/classes/Player.md) matching
  [SpawnLocation.TeamColor](/docs/reference/engine/classes/SpawnLocation.md) will respawn above it
- When [SpawnLocation.Neutral](/docs/reference/engine/classes/SpawnLocation.md) is set to true any Player can spawn above
  it regardless of [SpawnLocation.TeamColor](/docs/reference/engine/classes/SpawnLocation.md)
- If multiple eligible spawns are available to a [Player](/docs/reference/engine/classes/Player.md), a random one
  will be chosen
- Players will spawn at different points on top of a SpawnLocation, but
  currently, they may still spawn on top of each other if they spawn right
  after one and other

See also:

- If you'd like to configure how long it takes for a player to respawn, take a
  look at the [RespawnTime](/docs/reference/engine/classes/Players.md) property

## Code Samples

**SpawnLocation Checkpoints**

This sample demonstrates how SpawnLocations can be used to make a checkpoint
system. Typically this would be done Studio and not in Lua, but this example
serves as a comprehensive example of what Team and SpawnLocation properties
need to be used to achieve this setup.

```lua
local Teams = game:GetService("Teams")

-- create start team (AutoAssignable = true)
local startTeam = Instance.new("Team")
startTeam.Name = "Start"
startTeam.AutoAssignable = true
startTeam.TeamColor = BrickColor.new("White")
startTeam.Parent = Teams

-- create checkpoint teams (Autoassignable = false), ensuring all TeamColors are unique
local team1 = Instance.new("Team")
team1.Name = "Checkpoint 1"
team1.AutoAssignable = false
team1.TeamColor = BrickColor.new("Bright blue")
team1.Parent = Teams

local team2 = Instance.new("Team")
team2.Name = "Checkpoint 2"
team2.AutoAssignable = false
team2.TeamColor = BrickColor.new("Bright green")
team2.Parent = Teams

local team3 = Instance.new("Team")
team3.Name = "Checkpoint 2"
team3.AutoAssignable = false
team3.TeamColor = BrickColor.new("Bright red")
team3.Parent = Teams

-- create spawns
local startSpawn = Instance.new("SpawnLocation")
startSpawn.Anchored = true
startSpawn.Size = Vector3.new(5, 1, 5)
startSpawn.Neutral = false
startSpawn.AllowTeamChangeOnTouch = false
startSpawn.TeamColor = startTeam.TeamColor
startSpawn.BrickColor = startTeam.TeamColor
startSpawn.Parent = game.Workspace

local team1Spawn = Instance.new("SpawnLocation")
team1Spawn.Anchored = true
team1Spawn.Size = Vector3.new(5, 1, 5)
team1Spawn.Neutral = false
team1Spawn.AllowTeamChangeOnTouch = true
team1Spawn.TeamColor = team1.TeamColor
team1Spawn.BrickColor = team1.TeamColor
team1Spawn.Parent = game.Workspace

local team2Spawn = Instance.new("SpawnLocation")
team2Spawn.Anchored = true
team2Spawn.Size = Vector3.new(5, 1, 5)
team2Spawn.Neutral = false
team2Spawn.AllowTeamChangeOnTouch = true
team2Spawn.TeamColor = team2.TeamColor
team2Spawn.BrickColor = team2.TeamColor
team2Spawn.Parent = game.Workspace

local team3Spawn = Instance.new("SpawnLocation")
team3Spawn.Anchored = true
team3Spawn.Size = Vector3.new(5, 1, 5)
team3Spawn.Neutral = false
team3Spawn.AllowTeamChangeOnTouch = true
team3Spawn.TeamColor = team3.TeamColor
team3Spawn.BrickColor = team3.TeamColor
team3Spawn.Parent = game.Workspace

-- position spawns
startSpawn.CFrame = CFrame.new(0, 0.5, 0)
team1Spawn.CFrame = CFrame.new(10, 0.5, 0)
team2Spawn.CFrame = CFrame.new(20, 0.5, 0)
team3Spawn.CFrame = CFrame.new(30, 0.5, 0)
```

## Properties

### Property: SpawnLocation.AllowTeamChangeOnTouch

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
  "category": "Teams",
  "capabilities": [
    "Basic",
    "Players"
  ]
}
```

Allows a [Player](/docs/reference/engine/classes/Player.md) to join the team by touching the
[SpawnLocation](/docs/reference/engine/classes/SpawnLocation.md). When set to true, if a [Player](/docs/reference/engine/classes/Player.md) character
comes into contact with the [SpawnLocation](/docs/reference/engine/classes/SpawnLocation.md), the player's
[Player.TeamColor](/docs/reference/engine/classes/Player.md) will be set to [SpawnLocation.TeamColor](/docs/reference/engine/classes/SpawnLocation.md).
[Player.Neutral](/docs/reference/engine/classes/Player.md) will also be set to [SpawnLocation.Neutral](/docs/reference/engine/classes/SpawnLocation.md)
upon contact, meaning a player can also become neutral by touching a spawn
location.

This will not function when [SpawnLocation.Enabled](/docs/reference/engine/classes/SpawnLocation.md) is set to false.

#### Making Checkpoints

This feature is often used to make checkpoints in obstacle courses or
similar games.

**SpawnLocation Checkpoints**

This sample demonstrates how SpawnLocations can be used to make a checkpoint
system. Typically this would be done Studio and not in Lua, but this example
serves as a comprehensive example of what Team and SpawnLocation properties
need to be used to achieve this setup.

```lua
local Teams = game:GetService("Teams")

-- create start team (AutoAssignable = true)
local startTeam = Instance.new("Team")
startTeam.Name = "Start"
startTeam.AutoAssignable = true
startTeam.TeamColor = BrickColor.new("White")
startTeam.Parent = Teams

-- create checkpoint teams (Autoassignable = false), ensuring all TeamColors are unique
local team1 = Instance.new("Team")
team1.Name = "Checkpoint 1"
team1.AutoAssignable = false
team1.TeamColor = BrickColor.new("Bright blue")
team1.Parent = Teams

local team2 = Instance.new("Team")
team2.Name = "Checkpoint 2"
team2.AutoAssignable = false
team2.TeamColor = BrickColor.new("Bright green")
team2.Parent = Teams

local team3 = Instance.new("Team")
team3.Name = "Checkpoint 2"
team3.AutoAssignable = false
team3.TeamColor = BrickColor.new("Bright red")
team3.Parent = Teams

-- create spawns
local startSpawn = Instance.new("SpawnLocation")
startSpawn.Anchored = true
startSpawn.Size = Vector3.new(5, 1, 5)
startSpawn.Neutral = false
startSpawn.AllowTeamChangeOnTouch = false
startSpawn.TeamColor = startTeam.TeamColor
startSpawn.BrickColor = startTeam.TeamColor
startSpawn.Parent = game.Workspace

local team1Spawn = Instance.new("SpawnLocation")
team1Spawn.Anchored = true
team1Spawn.Size = Vector3.new(5, 1, 5)
team1Spawn.Neutral = false
team1Spawn.AllowTeamChangeOnTouch = true
team1Spawn.TeamColor = team1.TeamColor
team1Spawn.BrickColor = team1.TeamColor
team1Spawn.Parent = game.Workspace

local team2Spawn = Instance.new("SpawnLocation")
team2Spawn.Anchored = true
team2Spawn.Size = Vector3.new(5, 1, 5)
team2Spawn.Neutral = false
team2Spawn.AllowTeamChangeOnTouch = true
team2Spawn.TeamColor = team2.TeamColor
team2Spawn.BrickColor = team2.TeamColor
team2Spawn.Parent = game.Workspace

local team3Spawn = Instance.new("SpawnLocation")
team3Spawn.Anchored = true
team3Spawn.Size = Vector3.new(5, 1, 5)
team3Spawn.Neutral = false
team3Spawn.AllowTeamChangeOnTouch = true
team3Spawn.TeamColor = team3.TeamColor
team3Spawn.BrickColor = team3.TeamColor
team3Spawn.Parent = game.Workspace

-- position spawns
startSpawn.CFrame = CFrame.new(0, 0.5, 0)
team1Spawn.CFrame = CFrame.new(10, 0.5, 0)
team2Spawn.CFrame = CFrame.new(20, 0.5, 0)
team3Spawn.CFrame = CFrame.new(30, 0.5, 0)
```

### Property: SpawnLocation.Duration

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
  "category": "Forcefield",
  "capabilities": [
    "Basic",
    "Players"
  ]
}
```

The length of time, in seconds, that a [ForceField](/docs/reference/engine/classes/ForceField.md) will be applied
to a [Player](/docs/reference/engine/classes/Player.md) character spawning at this [SpawnLocation](/docs/reference/engine/classes/SpawnLocation.md). If
Duration is zero, the [ForceField](/docs/reference/engine/classes/ForceField.md) is never created, and it will not
trigger the [Instance.DescendantAdded](/docs/reference/engine/classes/Instance.md) or
[Instance.ChildAdded](/docs/reference/engine/classes/Instance.md) events.

This default value of this property is 10 seconds.

The duration feature allows developers to easily give
[Players](/docs/reference/engine/classes/Player.md) protection from 'spawn killing' which can be a
frustrating experience for players. Note, [ForceFields](/docs/reference/engine/classes/ForceField.md)
will only protect users from [Explosions](/docs/reference/engine/classes/Explosion.md) and weapons that
use [Humanoid:TakeDamage()](/docs/reference/engine/classes/Humanoid.md) to deal damage or otherwise check for a
[ForceField](/docs/reference/engine/classes/ForceField.md).

**SpawnLocation ForceField**

This sample will create a neutral SpawnLocation in the Workspace that'll give
players spawning a ForceField for 20 seconds.

```lua
local spawnLocation = Instance.new("SpawnLocation")
spawnLocation.Anchored = true
spawnLocation.Size = Vector3.new(5, 1, 5)
spawnLocation.Neutral = true -- anyone can spawn here
spawnLocation.Duration = 20
spawnLocation.Parent = workspace
```

### Property: SpawnLocation.Enabled

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
    "Basic",
    "Players"
  ]
}
```

Sets whether or not the [SpawnLocation](/docs/reference/engine/classes/SpawnLocation.md) is enabled. When disabled
players cannot spawn at the [SpawnLocation](/docs/reference/engine/classes/SpawnLocation.md) and the
[SpawnLocation.AllowTeamChangeOnTouch](/docs/reference/engine/classes/SpawnLocation.md) functionality is disabled.

This property provides the most convenient way of preventing
[Players](/docs/reference/engine/classes/Player.md) from spawning at a spawn.

Note, although team changing on touch using
[SpawnLocation.AllowTeamChangeOnTouch](/docs/reference/engine/classes/SpawnLocation.md) is disabled when Enabled is
set to false, other touched events using [BasePart.Touched](/docs/reference/engine/classes/BasePart.md) will
still fire.

**SpawnLocation Enabled**

The following sample will create a SpawnLocation in the Workspace that will
become semi-transparent when it is disabled.

```lua
local spawnLocation = Instance.new("SpawnLocation")
spawnLocation.Anchored = true
spawnLocation.Size = Vector3.new(5, 1, 5)
spawnLocation.Neutral = true -- anyone can spawn here
spawnLocation.Enabled = true
spawnLocation.Parent = workspace

local function onEnabledChanged()
	spawnLocation.Transparency = spawnLocation.Enabled and 0 or 0.5
end

spawnLocation:GetPropertyChangedSignal("Enabled"):Connect(onEnabledChanged)

task.wait(5)

spawnLocation.Enabled = false -- transparency = 0.5
```

### Property: SpawnLocation.Neutral

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
  "category": "Teams",
  "capabilities": [
    "Basic",
    "Players"
  ]
}
```

Whether or not a spawn is affiliated with a specific team. This means that
any [Player](/docs/reference/engine/classes/Player.md), of any [Team](/docs/reference/engine/classes/Team.md), can spawn on it if this property
is set to true.

If Neutral is set to false, only players whose [Player.TeamColor](/docs/reference/engine/classes/Player.md) is
equal to [SpawnLocation.TeamColor](/docs/reference/engine/classes/SpawnLocation.md) can use the
[SpawnLocation](/docs/reference/engine/classes/SpawnLocation.md).

If [SpawnLocation.AllowTeamChangeOnTouch](/docs/reference/engine/classes/SpawnLocation.md) is true
[Player.Neutral](/docs/reference/engine/classes/Player.md) will be set to this property upon contact with the
spawn.

**SpawnLocation Checkpoints**

This sample demonstrates how SpawnLocations can be used to make a checkpoint
system. Typically this would be done Studio and not in Lua, but this example
serves as a comprehensive example of what Team and SpawnLocation properties
need to be used to achieve this setup.

```lua
local Teams = game:GetService("Teams")

-- create start team (AutoAssignable = true)
local startTeam = Instance.new("Team")
startTeam.Name = "Start"
startTeam.AutoAssignable = true
startTeam.TeamColor = BrickColor.new("White")
startTeam.Parent = Teams

-- create checkpoint teams (Autoassignable = false), ensuring all TeamColors are unique
local team1 = Instance.new("Team")
team1.Name = "Checkpoint 1"
team1.AutoAssignable = false
team1.TeamColor = BrickColor.new("Bright blue")
team1.Parent = Teams

local team2 = Instance.new("Team")
team2.Name = "Checkpoint 2"
team2.AutoAssignable = false
team2.TeamColor = BrickColor.new("Bright green")
team2.Parent = Teams

local team3 = Instance.new("Team")
team3.Name = "Checkpoint 2"
team3.AutoAssignable = false
team3.TeamColor = BrickColor.new("Bright red")
team3.Parent = Teams

-- create spawns
local startSpawn = Instance.new("SpawnLocation")
startSpawn.Anchored = true
startSpawn.Size = Vector3.new(5, 1, 5)
startSpawn.Neutral = false
startSpawn.AllowTeamChangeOnTouch = false
startSpawn.TeamColor = startTeam.TeamColor
startSpawn.BrickColor = startTeam.TeamColor
startSpawn.Parent = game.Workspace

local team1Spawn = Instance.new("SpawnLocation")
team1Spawn.Anchored = true
team1Spawn.Size = Vector3.new(5, 1, 5)
team1Spawn.Neutral = false
team1Spawn.AllowTeamChangeOnTouch = true
team1Spawn.TeamColor = team1.TeamColor
team1Spawn.BrickColor = team1.TeamColor
team1Spawn.Parent = game.Workspace

local team2Spawn = Instance.new("SpawnLocation")
team2Spawn.Anchored = true
team2Spawn.Size = Vector3.new(5, 1, 5)
team2Spawn.Neutral = false
team2Spawn.AllowTeamChangeOnTouch = true
team2Spawn.TeamColor = team2.TeamColor
team2Spawn.BrickColor = team2.TeamColor
team2Spawn.Parent = game.Workspace

local team3Spawn = Instance.new("SpawnLocation")
team3Spawn.Anchored = true
team3Spawn.Size = Vector3.new(5, 1, 5)
team3Spawn.Neutral = false
team3Spawn.AllowTeamChangeOnTouch = true
team3Spawn.TeamColor = team3.TeamColor
team3Spawn.BrickColor = team3.TeamColor
team3Spawn.Parent = game.Workspace

-- position spawns
startSpawn.CFrame = CFrame.new(0, 0.5, 0)
team1Spawn.CFrame = CFrame.new(10, 0.5, 0)
team2Spawn.CFrame = CFrame.new(20, 0.5, 0)
team3Spawn.CFrame = CFrame.new(30, 0.5, 0)
```

### Property: SpawnLocation.TeamColor

```json
{
  "type": "BrickColor",
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
  "category": "Teams",
  "capabilities": [
    "Basic",
    "Players"
  ]
}
```

The TeamColor property sets what team the [SpawnLocation](/docs/reference/engine/classes/SpawnLocation.md) is
affiliated to. If [SpawnLocation.Neutral](/docs/reference/engine/classes/SpawnLocation.md) property is false, only
[Players](/docs/reference/engine/classes/Player.md) with the same [Player.TeamColor](/docs/reference/engine/classes/Player.md) as the
spawn's TeamColor will be able to spawn there.

If [SpawnLocation.AllowTeamChangeOnTouch](/docs/reference/engine/classes/SpawnLocation.md) is true
[Player.Neutral](/docs/reference/engine/classes/Player.md) will be set to this property upon contact with the
spawn.

**SpawnLocation Checkpoints**

This sample demonstrates how SpawnLocations can be used to make a checkpoint
system. Typically this would be done Studio and not in Lua, but this example
serves as a comprehensive example of what Team and SpawnLocation properties
need to be used to achieve this setup.

```lua
local Teams = game:GetService("Teams")

-- create start team (AutoAssignable = true)
local startTeam = Instance.new("Team")
startTeam.Name = "Start"
startTeam.AutoAssignable = true
startTeam.TeamColor = BrickColor.new("White")
startTeam.Parent = Teams

-- create checkpoint teams (Autoassignable = false), ensuring all TeamColors are unique
local team1 = Instance.new("Team")
team1.Name = "Checkpoint 1"
team1.AutoAssignable = false
team1.TeamColor = BrickColor.new("Bright blue")
team1.Parent = Teams

local team2 = Instance.new("Team")
team2.Name = "Checkpoint 2"
team2.AutoAssignable = false
team2.TeamColor = BrickColor.new("Bright green")
team2.Parent = Teams

local team3 = Instance.new("Team")
team3.Name = "Checkpoint 2"
team3.AutoAssignable = false
team3.TeamColor = BrickColor.new("Bright red")
team3.Parent = Teams

-- create spawns
local startSpawn = Instance.new("SpawnLocation")
startSpawn.Anchored = true
startSpawn.Size = Vector3.new(5, 1, 5)
startSpawn.Neutral = false
startSpawn.AllowTeamChangeOnTouch = false
startSpawn.TeamColor = startTeam.TeamColor
startSpawn.BrickColor = startTeam.TeamColor
startSpawn.Parent = game.Workspace

local team1Spawn = Instance.new("SpawnLocation")
team1Spawn.Anchored = true
team1Spawn.Size = Vector3.new(5, 1, 5)
team1Spawn.Neutral = false
team1Spawn.AllowTeamChangeOnTouch = true
team1Spawn.TeamColor = team1.TeamColor
team1Spawn.BrickColor = team1.TeamColor
team1Spawn.Parent = game.Workspace

local team2Spawn = Instance.new("SpawnLocation")
team2Spawn.Anchored = true
team2Spawn.Size = Vector3.new(5, 1, 5)
team2Spawn.Neutral = false
team2Spawn.AllowTeamChangeOnTouch = true
team2Spawn.TeamColor = team2.TeamColor
team2Spawn.BrickColor = team2.TeamColor
team2Spawn.Parent = game.Workspace

local team3Spawn = Instance.new("SpawnLocation")
team3Spawn.Anchored = true
team3Spawn.Size = Vector3.new(5, 1, 5)
team3Spawn.Neutral = false
team3Spawn.AllowTeamChangeOnTouch = true
team3Spawn.TeamColor = team3.TeamColor
team3Spawn.BrickColor = team3.TeamColor
team3Spawn.Parent = game.Workspace

-- position spawns
startSpawn.CFrame = CFrame.new(0, 0.5, 0)
team1Spawn.CFrame = CFrame.new(10, 0.5, 0)
team2Spawn.CFrame = CFrame.new(20, 0.5, 0)
team3Spawn.CFrame = CFrame.new(30, 0.5, 0)
```

## Inherited Members

### From [Part](/docs/reference/engine/classes/Part.md)

- **Property `Shape`** (`PartType`): Sets the overall shape of the object.

### From [FormFactorPart](/docs/reference/engine/classes/FormFactorPart.md)

- **Property `FormFactor`** (`FormFactor`):  *(deprecated)*
- **Property `formFactor`** (`FormFactor`):  *(deprecated, hidden)*

### From [BasePart](/docs/reference/engine/classes/BasePart.md)

- **Property `Anchored`** (`boolean`): Determines whether a part is immovable by physics.
- **Property `AssemblyAngularVelocity`** (`Vector3`): The angular velocity of the part's assembly.
- **Property `AssemblyCenterOfMass`** (`Vector3`): The center of mass of the part's assembly in world space.
- **Property `AssemblyLinearVelocity`** (`Vector3`): The linear velocity of the part's assembly.
- **Property `AssemblyMass`** (`float`): The total mass of the part's assembly.
- **Property `AssemblyRootPart`** (`BasePart`): A reference to the root part of the assembly.
- **Property `AudioCanCollide`** (`boolean`): Determines whether the part will physically interact with audio
- **Property `BackParamA`** (`float`): Determines the first parameter for the SurfaceType on the Back face of a *(deprecated, hidden)*
- **Property `BackParamB`** (`float`): Determines the second parameter for the SurfaceType on the Back face of a *(deprecated, hidden)*
- **Property `BackSurface`** (`SurfaceType`): Determines the type of surface for the back face of a part.
- **Property `BackSurfaceInput`** (`InputType`): Determines the kind of input for the Back face of a part. *(deprecated, hidden)*
- **Property `BottomParamA`** (`float`): Determines the first parameter for the SurfaceType on the Bottom face of a *(deprecated, hidden)*
- **Property `BottomParamB`** (`float`): Determines the second parameter for the SurfaceType on the Bottom face of *(deprecated, hidden)*
- **Property `BottomSurface`** (`SurfaceType`): Determines the type of surface for the bottom face of a part.
- **Property `BottomSurfaceInput`** (`InputType`): Determines the kind of input for the Bottom face of a part. *(deprecated, hidden)*
- **Property `BrickColor`** (`BrickColor`): Determines the color of a part.
- **Property `brickColor`** (`BrickColor`):  *(deprecated)*
- **Property `CanCollide`** (`boolean`): Determines whether a part may collide with other parts.
- **Property `CanQuery`** (`boolean`): Determines whether the part is considered during spatial query operations.
- **Property `CanTouch`** (`boolean`): Determines if Touched and
- **Property `CastShadow`** (`boolean`): Determines whether or not a part casts a shadow.
- **Property `CenterOfMass`** (`Vector3`): Describes the local position of a part's center of mass, relative to its
- **Property `CFrame`** (`CFrame`): Determines the position and orientation of the BasePart in the
- **Property `CollisionGroup`** (`string`): Describes the name of a part's collision group.
- **Property `CollisionGroupId`** (`int`): Describes the automatically set ID number of a part's collision group. *(deprecated)*
- **Property `Color`** (`Color3`): Determines the color of a part.
- **Property `CurrentPhysicalProperties`** (`PhysicalProperties`): Indicates the current physical properties of the part.
- **Property `CustomPhysicalProperties`** (`PhysicalProperties`): Determines several physical properties of a part.
- **Property `Elasticity`** (`float`): Used to control the Elasticity of the part, but it no longer does *(deprecated, hidden)*
- **Property `EnableFluidForces`** (`boolean`): Used to enable or disable aerodynamic forces on parts and assemblies.
- **Property `ExtentsCFrame`** (`CFrame`): The CFrame of the physical extents of the BasePart.
- **Property `ExtentsSize`** (`Vector3`): The actual physical size of the BasePart as regarded by the
- **Property `Friction`** (`float`): Used to control the Friction of the part, but now it no longer does *(deprecated, hidden)*
- **Property `FrontParamA`** (`float`): Determines the first parameter for the SurfaceType on the Front face of a *(deprecated, hidden)*
- **Property `FrontParamB`** (`float`): Determines the second parameter for the SurfaceType on the Front face of a *(deprecated, hidden)*
- **Property `FrontSurface`** (`SurfaceType`): Determines the type of surface for the front face of a part.
- **Property `FrontSurfaceInput`** (`InputType`): Determines the kind of input for the Front face of a part (-Z direction). *(deprecated, hidden)*
- **Property `LeftParamA`** (`float`): Determines the first parameter for the SurfaceType on the Left face of a *(deprecated, hidden)*
- **Property `LeftParamB`** (`float`): Determines the second parameter for the SurfaceType on the Left face of a *(deprecated, hidden)*
- **Property `LeftSurface`** (`SurfaceType`): Determines the type of surface for the left face of a part.
- **Property `LeftSurfaceInput`** (`InputType`): Determines the kind of input for the Left face of a part. *(deprecated, hidden)*
- **Property `LocalTransparencyModifier`** (`float`): Determines a multiplier for BasePart.Transparency that is only *(hidden)*
- **Property `Locked`** (`boolean`): Determines whether a part is selectable in Studio.
- **Property `Mass`** (`float`): Describes the mass of the part, the product of its density and volume.
- **Property `Massless`** (`boolean`): Determines whether the part contributes to the total mass or inertia of
- **Property `Material`** (`Material`): Determines the texture and default physical properties of a part.
- **Property `MaterialVariant`** (`string`): The name of MaterialVariant.
- **Property `Orientation`** (`Vector3`): Describes the rotation of the part in the world. *(hidden)*
- **Property `PivotOffset`** (`CFrame`): Specifies the offset of the part's pivot from its CFrame.
- **Property `Position`** (`Vector3`): Describes the position of the part in the world. *(hidden)*
- **Property `ReceiveAge`** (`float`): Time since last recorded physics update. *(hidden)*
- **Property `Reflectance`** (`float`): Determines how much a part reflects the skybox.
- **Property `ResizeableFaces`** (`Faces`): Describes the faces on which a part may be resized.
- **Property `ResizeIncrement`** (`int`): Describes the smallest change in size allowable by the
- **Property `RightParamA`** (`float`): Determines the first parameter for the SurfaceType on the Right face of a *(deprecated, hidden)*
- **Property `RightParamB`** (`float`): Determines the second parameter for the SurfaceType on the Right face of a *(deprecated, hidden)*
- **Property `RightSurface`** (`SurfaceType`): Determines the type of surface for the right face of a part.
- **Property `RightSurfaceInput`** (`InputType`): Determines the kind of input for the Right face of a part (-X direction). *(deprecated, hidden)*
- **Property `RootPriority`** (`int`): The main rule in determining the root part of an assembly.
- **Property `Rotation`** (`Vector3`): The rotation of the part in degrees for the three axes.
- **Property `RotVelocity`** (`Vector3`): Determines a part's change in orientation over time. *(deprecated, hidden)*
- **Property `Size`** (`Vector3`): Determines the dimensions of a part (length, height, width).
- **Property `SpecificGravity`** (`float`): The ratio of the part's density to the density of water determined by the *(deprecated)*
- **Property `TopParamA`** (`float`): Determines the first parameter for the SurfaceType on the Top face of a *(deprecated, hidden)*
- **Property `TopParamB`** (`float`): Determines the second parameter for the SurfaceType on the Top face of a *(deprecated, hidden)*
- **Property `TopSurface`** (`SurfaceType`): Determines the type of surface for the top face of a part.
- **Property `TopSurfaceInput`** (`InputType`): Determines the kind of input for the Top face of a part (+Y direction). *(deprecated, hidden)*
- **Property `Transparency`** (`float`): Determines how much a part can be seen through (the inverse of part
- **Property `Velocity`** (`Vector3`): Determines a part's change in position over time. *(deprecated, hidden)*
- **Method `AngularAccelerationToTorque(angAcceleration: Vector3, angVelocity?: Vector3): Vector3`**: Returns the torque needed to achieve a given angular acceleration on this
- **Method `ApplyAngularImpulse(impulse: Vector3): ()`**: Apply an angular impulse to the assembly.
- **Method `ApplyImpulse(impulse: Vector3): ()`**: Apply an impulse to the assembly at the assembly's
- **Method `ApplyImpulseAtPosition(impulse: Vector3, position: Vector3): ()`**: Apply an impulse to the assembly at specified position.
- **Method `BindToCollisionSummaries(callback: Function): RBXScriptConnection`**: Subscribes to detailed per-frame contact data for the collisions this part
- **Method `BreakJoints(): ()`**: Breaks any surface connection with any adjacent part, including *(deprecated)*
- **Method `breakJoints(): ()`**:  *(deprecated)*
- **Method `CanCollideWith(part: BasePart): boolean`**: Returns whether the parts can collide with each other.
- **Method `CanSetNetworkOwnership(): Tuple`**: Checks whether you can set a part's network ownership.
- **Method `GetClosestPointOnSurface(position: Vector3): Vector3`**: Returns the closest point on the part's surface to the given point.
- **Method `GetConnectedParts(recursive?: boolean): List<BasePart>`**: Returns a table of parts connected to the object by any kind of rigid
- **Method `GetJoints(): Instances`**: Returns all Joints or Constraints connected to this part that are active
- **Method `GetMass(): float`**: Returns the value of the Mass property.
- **Method `getMass(): float`**:  *(deprecated)*
- **Method `GetNetworkOwner(): Instance`**: Returns the current player who is the network owner of this part, or `nil`
- **Method `GetNetworkOwnershipAuto(): boolean`**: Returns true if the game engine automatically decides the network owner
- **Method `GetNoCollisionConstraints(): Instances`**: Returns the enabled NoCollisionConstraint objects currently
- **Method `GetRenderCFrame(): CFrame`**: OBSOLETE. Returns a CFrame describing where the part is being rendered at. *(deprecated)*
- **Method `GetRootPart(): Instance`**: Returns the base part of an assembly of parts. *(deprecated)*
- **Method `GetTouchingParts(): Instances`**: Returns a table of all BasePart.CanCollide true parts that
- **Method `GetVelocityAtPosition(position: Vector3): Vector3`**: Returns the linear velocity of the part's assembly at the given position
- **Method `IntersectAsync(parts: Instances, collisionfidelity?: CollisionFidelity, renderFidelity?: RenderFidelity): Instance`**: Creates a new IntersectOperation from the overlapping geometry of
- **Method `IsGrounded(): boolean`**: Returns true if the object is connected to a part that will hold it in
- **Method `MakeJoints(): ()`**: Creates a joint on any side of the object that has a surface ID that can *(deprecated)*
- **Method `makeJoints(): ()`**:  *(deprecated)*
- **Method `Resize(normalId: NormalId, deltaAmount: int): boolean`**: Changes the size of an object just like using the Studio resize tool.
- **Method `resize(normalId: NormalId, deltaAmount: int): boolean`**:  *(deprecated)*
- **Method `SetNetworkOwner(playerInstance?: Player): ()`**: Sets the given player as network owner for this and all connected parts.
- **Method `SetNetworkOwnershipAuto(): ()`**: Lets the game engine dynamically decide who will handle the part's physics
- **Method `SubtractAsync(parts: Instances, collisionfidelity?: CollisionFidelity, renderFidelity?: RenderFidelity): Instance`**: Creates a new UnionOperation from the part, minus the geometry
- **Method `TorqueToAngularAcceleration(torque: Vector3, angVelocity?: Vector3): Vector3`**: Returns the angular acceleration that would result from applying a given
- **Method `UnionAsync(parts: Instances, collisionfidelity?: CollisionFidelity, renderFidelity?: RenderFidelity): Instance`**: Creates a new UnionOperation from the part, plus the geometry
- **Event `LocalSimulationTouched`**: Fires on the local client when another part comes in contact with this *(deprecated)*
- **Event `OutfitChanged`**: Fires when the part's appearance changes due to a Shirt. *(deprecated)*
- **Event `StoppedTouching`**: Fires on the local client when a part stops touching another part. *(deprecated)*
- **Event `Touched`**: Fires when a part touches another part as a result of physical movement.
- **Event `TouchEnded`**: Fires when a part stops touching another part as a result of physical

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