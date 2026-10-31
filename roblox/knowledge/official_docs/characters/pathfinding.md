---
title: "Pathfinding"
url: /docs/en-us/characters/pathfinding
last_updated: 2026-10-30T19:55:38Z
description: "Pathfinding is the process of moving a character or object (agent) along a logical path to reach a destination."
---

# Pathfinding

**Pathfinding** is the process of moving a character or object (agent) along a logical path around obstacles to reach a destination, optionally avoiding hazardous materials or defined regions.

## Navigation visualization

To assist with pathfinding layout and debugging, Studio can render a navigation mesh and [modifier](#pathfinding-modifiers) labels. To enable them, toggle on **Navigation mesh** and **Pathfinding modifiers** from the [Visualization Options](/docs/en-us/studio/overview.md#visualization-options) widget in the upper‑right corner of the 3D viewport.

![A close up view of the 3D viewport with the Visualization Options button indicated in the upper-right corner.](../assets/studio/general/Visualization-Options.png)

#### Navigation Mesh

With **Navigation mesh** enabled, colored areas show where a character might walk or swim. Small arrows indicate areas that a character will attempt to reach by jumping.

![Navigation mesh showing in Studio](../assets/avatar/pathfinding/Navigation-Mesh.jpg)

#### Pathfinding Modifiers

With **Pathfinding modifiers** enabled, text labels indicate specific materials and regions that are taken into consideration when using [pathfinding modifiers](#pathfinding-modifiers).

![Navigation labels showing on navigation mesh](../assets/avatar/pathfinding/Navigation-Labels.jpg)

## Implementation

Although pathfinding can be implemented in various ways through `Class.PathfindingService` and its associated methods such as `Class.PathfindingService:CreatePath()|CreatePath()`, this section uses the following pathfinding script for the player's character.

To test while reading:

1. **IMPORTANT** In the [Explorer](/docs/en-us/studio/explorer.md), select the `Class.StarterPlayer` container. Then, in the [Properties](/docs/en-us/studio/properties.md) window, set both `Class.StarterPlayer.DevComputerMovementMode|DevComputerMovementMode` and `Class.StarterPlayer.DevTouchMovementMode|DevTouchMovementMode` to `Scriptable`.
2. Copy the following code into a `Class.LocalScript` within `Class.StarterCharacterScripts`, or [get this package](https://create.roblox.com/store/asset/95888831676289/Player-Path-Following-Script) and drop it into `Class.StarterCharacterScripts`.```lua
local PathfindingService = game:GetService("PathfindingService")
local Players = game:GetService("Players")
local RunService = game:GetService("RunService")

local DESTINATION = Vector3.new(20, 0.5, 20)
local GROUND_WAIT = 0.01
local VELOCITY_MULTIPLIER = 0.0625

local path = PathfindingService:CreatePath({
	AgentCanClimb = true,
	Costs = {
		Water = 20
	}
})

local character = script.Parent
local humanoid = character:WaitForChild("Humanoid")
local waypoints
local nextWaypointIndex
local blockedConnection
local currentWaypointReachedConnection
local currentWaypointPlaneNormal = Vector3.zero
local currentWaypointPlaneDistance = 0
local pathfinderWorking = false

local function disconnectCurrentWaypointReachedConnection()
	if not currentWaypointReachedConnection then return end
	currentWaypointReachedConnection:Disconnect()
	currentWaypointReachedConnection = nil
end

local function isCurrentWaypointReached()
	if humanoid.FloorMaterial == Enum.Material.Air then
		return false
	end

	local reached = false
	if currentWaypointPlaneNormal ~= Vector3.zero then
		-- Compute the distance from humanoid to destination plane
		local dist = currentWaypointPlaneNormal:Dot(humanoid.RootPart.Position) - currentWaypointPlaneDistance
		-- Compute the component of the humanoid velocity that is towards the plane
		local velocity = -currentWaypointPlaneNormal:Dot(humanoid.RootPart.Velocity)
		-- Compute the threshold from the destination plane based on humanoid velocity
		local threshold = math.max(1.0, VELOCITY_MULTIPLIER * velocity)
		-- Consider waypoint reached if less then threshold in front of the plane
		reached = dist < threshold
	else
		reached = true
	end

	if reached then
		currentWaypointPlaneNormal = Vector3.zero
		currentWaypointPlaneDistance = 0
		moveToNextWaypoint()
	end
end

local function calculateNextWaypointApproach()
	nextWaypointIndex += 1
	if nextWaypointIndex > #waypoints then
		return false
	end
	local currentWaypoint = waypoints[nextWaypointIndex - 1]
	local nextWaypoint = waypoints[nextWaypointIndex]
	-- Build destination plane from next waypoint towards current one
	currentWaypointPlaneNormal = currentWaypoint.Position - nextWaypoint.Position
	-- Set normal perpendicular to Y plane when not climbing up
	if nextWaypoint.Label ~= "Climb" then
		currentWaypointPlaneNormal = Vector3.new(currentWaypointPlaneNormal.X, 0, currentWaypointPlaneNormal.Z)
	end
	if currentWaypointPlaneNormal.Magnitude > 0.000001 then
		currentWaypointPlaneNormal	= currentWaypointPlaneNormal.Unit
		currentWaypointPlaneDistance = currentWaypointPlaneNormal:Dot(nextWaypoint.Position)
	end

	return true
end

local function resetWaypointData()
	humanoid:Move(Vector3.zero)
	currentWaypointPlaneNormal	= Vector3.zero
	currentWaypointPlaneDistance = 0
	disconnectCurrentWaypointReachedConnection()
	pathfinderWorking = false
end

local function waitForGround()
	while humanoid.FloorMaterial == Enum.Material.Air do
		task.wait(GROUND_WAIT)
	end
end

function moveToNextWaypoint()
	if calculateNextWaypointApproach() then
		disconnectCurrentWaypointReachedConnection()
		currentWaypointReachedConnection = RunService.Heartbeat:Connect(isCurrentWaypointReached)
		local nextWaypointPosition = waypoints[nextWaypointIndex].Position
		local nextWaypointAction = waypoints[nextWaypointIndex].Action
		humanoid:Move(nextWaypointPosition - humanoid.RootPart.Position)
		if waypoints[nextWaypointIndex + 1] and waypoints[nextWaypointIndex + 1].Label == "UseBoat" then
			nextWaypointIndex += 1
			-- Call your own customized function to make agent use the boat

		elseif nextWaypointAction == Enum.PathWaypointAction.Jump then
			humanoid:ChangeState(Enum.HumanoidStateType.Jumping)
			while humanoid.FloorMaterial ~= Enum.Material.Air do
				task.wait(GROUND_WAIT)
			end
			humanoid:Move(nextWaypointPosition - humanoid.RootPart.Position)
		end
	else
		resetWaypointData()
	end
end

local function findStartingPoint(waypoints)
	nextWaypointIndex = 1
	while nextWaypointIndex + 1 <= #waypoints do
		local dist = waypoints[nextWaypointIndex + 1].Position - humanoid.RootPart.Position
		dist = Vector3.new(dist.X, 0, dist.Z)
		if dist.magnitude >= 2 then
			return
		end
		nextWaypointIndex += 1
	end
end

local function followPath()
	-- Compute the path
	pathfinderWorking = true
	waitForGround()

	local success, errorMessage = pcall(function()
		path:ComputeAsync(character.PrimaryPart.Position, DESTINATION)
	end)
	if not success or path.Status ~= Enum.PathStatus.Success then
		warn("Path not computed!", errorMessage)
		return
	end

	-- Get the path waypoints
	waypoints = path:GetWaypoints()

	-- Detect if path becomes blocked
	blockedConnection = path.Blocked:Connect(function(blockedWaypointIndex)
		-- Check if the obstacle is further down the path
		if blockedWaypointIndex >= nextWaypointIndex then
			-- Stop detecting path blockage until path is re-computed
			blockedConnection:Disconnect()
			resetWaypointData()
			-- Call function to re-compute new path
			followPath()
		end
	end)

	findStartingPoint(waypoints)
	moveToNextWaypoint()
end

followPath()
```
3. Edit the `DESTINATION` variable (**LINE 5**) to a `Datatype.Vector3` destination within the 3D world that the player character can reach.
4. Proceed through the following sections to learn about path computation and character movement.

### Path creation

Pathfinding is initiated through `Class.PathfindingService` and its `Class.PathfindingService:CreatePath()|CreatePath()` method (**LINES 9–14**). This method accepts an optional table of parameters which fine tune how the character (agent) moves along the path.

| Key | Description | Type | Default |
| --- | --- | --- | --- |
| `AgentRadius` | Agent radius, in studs. Useful for determining the minimum separation from obstacles. | integer | `2` |
| `AgentHeight` | Agent height, in studs. Empty space smaller than this value, like the space under stairs, will be marked as non-traversable. | integer | `5` |
| `AgentCanJump` | Determines whether jumping during pathfinding is allowed. | boolean | `true` |
| `AgentCanClimb` | Determines whether climbing `Class.TrussPart\|TrussParts` during pathfinding is allowed. A climbable path has a `Datatype.PathWaypoint.Label\|Label` named `Climb` and the [cost](#material-costs) for a climbable path is `1` by default. | boolean | `false` |
| `WaypointSpacing` | Spacing between intermediate waypoints in path. If set to `Library.math.huge`, there will be no intermediate waypoints. | number | `4` |
| `Costs` | Table of materials or defined `Class.PathfindingModifier\|PathfindingModifiers` and their cost for traversal. Useful for making the agent prefer certain materials/regions over others. See [modifiers](#pathfinding-modifiers) for details. | table | `nil` |

### Path computation

After you've created a valid path with `Class.PathfindingService:CreatePath()|CreatePath()`, it must be **computed** by calling `Class.Path:ComputeAsync()` with a `Datatype.Vector3` for both the starting point and destination (**LINES 133–139**).

![Path start/end marked across two bridges](../assets/avatar/pathfinding/Path-Start-End.jpg)

Once the `Class.Path` is computed, it will contain a series of **waypoints** that trace the path from start to end. These points can be gathered with the `Class.Path:GetWaypoints()` method (**LINE 142**). The returned array is arranged in order of waypoints from path start to path end.

![Waypoints indicated across computed path](../assets/avatar/pathfinding/Waypoints.jpg)_Waypoints indicated across computed path_

> **Warning:** The pathfinding engine includes specific limitations, and pathfinding computations can fail for various reasons. If your implementation does not behave as expected, see [limitations and failure factors](#limitations-and-failure-factors) for possible causes.
### Path movement

Each `Datatype.PathWaypoint` consists of both a `Datatype.PathWaypoint.Position|Position` (`Datatype.Vector3`) and `Datatype.PathWaypoint.Action|Action` (`Enum.PathWaypointAction|PathWaypointAction`). To move a character containing a `Class.Humanoid`, like a typical Roblox character, the best way is to call `Class.Humanoid:Move()` from waypoint to waypoint and use the script's `isCurrentWaypointReached()` callback (**LINES 32–56**) to detect when the character reaches each waypoint.

> **Warning:** Note that the script waits for the humanoid to be touching the ground before calling the pathfinder. If the path is computed while the character is falling through the air, the pathfinder will try to determine an appropriate start position for the path.
### Blocked paths

Many Roblox worlds are dynamic; parts might move or fall and floors may collapse. This can block a computed path and prevent the character from reaching its destination. To handle this, you can connect the `Class.Path.Blocked` event and re-compute the path around whatever blocked it (**LINES 145–154**).

> **Warning:** Paths may also become blocked somewhere **behind** the agent, such as a pile of rubble falling on a path as the agent runs away, but that doesn't mean the agent should stop moving. The`if blockedWaypointIndex >= nextWaypointIndex` check makes sure that the path is re-computed only if the blocked waypoint is **ahead** of the current waypoint.
## Pathfinding modifiers

By default, `Class.Path:ComputeAsync()` returns the **shortest** path between the starting point and destination, with the exception that it attempts to avoid jumps. This looks unnatural in some situations; for instance, a path may go through swamp water rather than around it simply because the path through the water is geometrically shorter.

![Two paths indicated with the shorter path not necessarily more logical](../assets/avatar/pathfinding/Paths-Shortest-Best.jpg)

To optimize pathfinding even further, you can implement **pathfinding modifiers** to compute smarter paths across various [materials](#material-costs), around defined [regions](#configure-regions), or to [ignore obstacles](#ignore-obstacles).

### Material costs

When working with `Class.Terrain` and `Class.BasePart` materials, you can include a `Costs` table within `Class.PathfindingService:CreatePath()|CreatePath()` to make certain materials more traversable than others. All materials have a default cost of `1` and any material can be defined as non‑traversable by setting its value to `Library.math.huge`.

Keys in the `Costs` table should be **string** names representing `Enum.Material` names, for example `Water` for `Enum.Material.Water` or `CrackedLava` for `Enum.Material.CrackedLava`.

```lua
local PathfindingService = game:GetService("PathfindingService")
local Players = game:GetService("Players")
local RunService = game:GetService("RunService")

local DESTINATION = Vector3.new(20, 0.5, 20)
local GROUND_WAIT = 0.01
local VELOCITY_MULTIPLIER = 0.0625

local path = PathfindingService:CreatePath({
	AgentCanClimb = true,
	Costs = {
		Water = 20, CrackedLava = 100, Slate = 20
	}
})
```

> **Info:** To set a material such as `CrackedLava` as a "last option," assign it a high but finite material cost like `100` or `1000`. Since there's no engine‑enforced upper cap below `Library.math.huge`, the pathfinder will only route through the material if every alternative is more expensive.
### Configure regions

In some cases, [material preference](#material-costs) is not enough. For example, you might want characters to avoid a defined **region**, regardless of the materials underfoot. This can be achieved by adding a `Class.PathfindingModifier` object to a part.

1. Create an `Class.BasePart.Anchored|Anchored` part around the region and set its `Class.BasePart.CanCollide|CanCollide` property to `false`.![Anchored part defining a region to apply a pathfinding modifier to.](../assets/avatar/pathfinding/GeyserBlocker-Block.jpg)
2. Insert a `Class.PathfindingModifier` instance onto the part, locate its `Class.PathfindingModifier.Label|Label` property, and assign a meaningful name like `DangerZone`.![PathfindingModifier instance with Label property set to DangerZone.](../assets/studio/properties/PathfindingModifier-Label.png)
3. Include a matching `DangerZone` key and associated numeric value within the `Costs` table of `Class.PathfindingService:CreatePath()|CreatePath()`. A modifier can be defined as non‑traversable by setting its value to `Library.math.huge`.```lua
local PathfindingService = game:GetService("PathfindingService")
local Players = game:GetService("Players")
local RunService = game:GetService("RunService")

local DESTINATION = Vector3.new(20, 0.5, 20)
local GROUND_WAIT = 0.01
local VELOCITY_MULTIPLIER = 0.0625

local path = PathfindingService:CreatePath({
	AgentCanClimb = true,
	Costs = {
		DangerZone = math.huge, Water = 20, CrackedLava = 20, Slate = 20
	}
})
```

### Ignore obstacles

In some cases, it's useful to pathfind through solid obstacles as if they didn't exist. This lets you compute a path through specific physical blockers, versus the computation failing outright.

1. Create an `Class.BasePart.Anchored|Anchored` part around the object and set its `Class.BasePart.CanCollide|CanCollide` property to `false`.![Anchored part defining a region to apply a pathfinding modifier to.](../assets/avatar/pathfinding/DoorPassThrough-Block.jpg)
2. Insert a `Class.PathfindingModifier` instance onto the part and enable its `Class.PathfindingModifier.PassThrough|PassThrough` property.![PathfindingModifier instance with PassThrough property enabled.](../assets/studio/properties/PathfindingModifier-PassThrough.png) Now, when a path is computed from the zombie NPC to the player character, the path extends beyond the door and you can prompt the zombie to traverse it. Even if the zombie is unable to open the door, it reacts as if it "hears" the character behind the door.![Zombie NPC path passing through the previously blocking door.](../assets/avatar/pathfinding/Zombie-Full-Path.jpg)

## Pathfinding links

Sometimes it's necessary to find a path across a space that cannot be normally traversed, such as across a chasm, and perform a custom action to reach the next waypoint. This can be achieved through the `Class.PathfindingLink` object.

Using the example from above, you can make the agent use a boat.

![PathfindingLink showing how an agent can use a boat.](../assets/avatar/pathfinding/PathfindingLink-Path.jpg)

To create a `Class.PathfindingLink` using this example:

1. **OPTIONAL** Toggle on **Pathfinding links** from the [Visualization Options](/docs/en-us/studio/overview.md#visualization-options) widget in the upper‑right corner of the 3D viewport. This helps with visualization and debugging when implementing pathfinding links.
2. Create two `Class.Attachment|Attachments`, one on the boat's seat and one near the boat's landing point.![Attachments created for pathfinding link's start and end.](../assets/avatar/pathfinding/PathfindingLink-Attachments.jpg)
3. Create a `Class.PathfindingLink` object in the workspace, then assign its `Class.PathfindingLink.Attachment0|Attachment0` and `Class.PathfindingLink.Attachment1|Attachment1` properties to the starting and ending attachments respectively.![Attachment0/Attachment1 properties of a PathfindingLink.](../assets/studio/properties/PathfindingLink-Attachments.png)![PathfindingLink visualized in the 3D world.](../assets/avatar/pathfinding/PathfindingLink-In-World.jpg)
4. Assign a meaningful name like `UseBoat` to its `Class.PathfindingLink.Label|Label` property. This name is used as a flag in the pathfinding script to trigger a custom action when the agent reaches the starting link point.![Label property specified for PathfindingLink.](../assets/studio/properties/PathfindingLink-Label.png)
5. Include a `Costs` table within `Class.PathfindingService:CreatePath()|CreatePath()` containing both a `Water` key and a custom key matching the `Class.PathfindingLink.Label|Label` property name. Assign the custom key a value **lower** than that of `Water`.```lua
local PathfindingService = game:GetService("PathfindingService")
local Players = game:GetService("Players")
local RunService = game:GetService("RunService")

local DESTINATION = Vector3.new(20, 0.5, 20)
local GROUND_WAIT = 0.01
local VELOCITY_MULTIPLIER = 0.0625

local path = PathfindingService:CreatePath({
	AgentCanClimb = true,
	Costs = {
		UseBoat = 2, Water = 20
	}
})
```
6. In the `moveToNextWaypoint()` function (**LINES 93–114**), a custom check for the `Class.PathfindingLink.Label|Label` modifier name can be used to take a different action than `Class.Humanoid:Move()`; in this case, you might call a function to seat the agent in the boat, move the boat across the water, unseat the agent at the boat's landing point, and then continue the agent's path to its final destination.

## Streaming compatibility

In-game [instance streaming](/docs/en-us/workspace/streaming.md) is a powerful feature that dynamically loads and unloads 3D content as a player's character moves around the world. As they explore the 3D space, new subsets of the space stream to their device and some of the existing subsets might stream out.

Consider the following best practices for using `Class.PathfindingService` in streaming-enabled games:

- Streaming can block or unblock a given path as a character moves along it. For example, while a character runs through a forest, a tree might stream in somewhere ahead of them and obstruct the path. To make pathfinding work seamlessly with streaming, it's highly recommended that you use the [handling blocked paths](#blocked-paths) technique and re-compute the path when necessary.
- A common approach in pathfinding is to use the coordinates of existing objects for [computation](#path-computation), such as setting a path destination to the position of an existing `TreasureChest` model in the world. This approach is fully compatible with server-side `Class.Script|Scripts` since the server has full view of the world at all times, but `Class.LocalScript|LocalScripts` and `Class.ModuleScript|ModuleScripts` that run on the client may fail if they attempt to compute a path to an object that's not streamed in. To address this issue, consider setting the destination to the position of a `Class.BasePart` within a [persistent](/docs/en-us/workspace/streaming.md#model-streaming-controls) model. Persistent models load soon after the player joins and they never stream out, so a client-side script can connect to the `Class.Workspace.PersistentLoaded|PersistentLoaded` event and safely access the model for creating waypoints after the event fires.

## Limitations and failure factors

The pathfinding engine includes specific limitations to ensure efficient processing and optimal performance. Additionally, pathfinding [computations](#path-computation) can fail for various reasons as outlined below.

> **Warning:****Path request too long** — The direct line‑of‑sight distance for pathfinding from the start to the finish point must not exceed 3,000 studs.
> **Warning:****Node budget exhausted** — A pathfinding computation may exceed 20,000 nodes well before reaching the distance cap of 3,000 studs, especially when pathfinding in a vast open world or through complex mazes.
> **Warning:****Incompatible agent parameters** — A pathfinding computation will fail if the [creation parameters](#path-creation) cannot resolve. For example, if the destination can **only** be reached by the agent jumping but `AgentCanJump` is `false`, or `AgentHeight` is greater than the height of any traversable path.
> **Warning:****Vertical waypoint limits** — Pathfinding calculations only consider paths within a set vertical boundary. Potential waypoints with a bottom global **Y** coordinate less than `-65,536` studs or greater than `65,536` studs are ignored.
