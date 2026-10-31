---
name: RunService
last_updated: 2026-10-30T19:55:53Z
inherits:
  - Instance
  - Object
type: class
memory_category: Instances
tags:
  - NotCreatable
  - Service
  - NotReplicated
summary: "Service responsible for all runtime activity and progression of time."
---

# Class: RunService

> Service responsible for all runtime activity and progression of time.

## Description

`RunService` contains methods and events for time management as well as for
managing the context in which an experience or script is running. Methods like
[IsClient()](/docs/reference/engine/classes/RunService.md),
[IsServer()](/docs/reference/engine/classes/RunService.md), and
[IsStudio()](/docs/reference/engine/classes/RunService.md) can help you determine under what
context code is running. These methods are useful for
[ModuleScripts](/docs/reference/engine/classes/ModuleScript.md) that may be required by both client and
server scripts. Furthermore, [IsStudio()](/docs/reference/engine/classes/RunService.md) can be
used to add special behaviors for in‑Studio testing.

`RunService` also houses events that allow your code to adhere to the engine's
frame‑by‑frame loop, such as [PreRender](/docs/reference/engine/classes/RunService.md),
[PreAnimation](/docs/reference/engine/classes/RunService.md),
[PreSimulation](/docs/reference/engine/classes/RunService.md),
[PostSimulation](/docs/reference/engine/classes/RunService.md), and
[Heartbeat](/docs/reference/engine/classes/RunService.md). Selecting the proper event to use for
any case is important, so you should read
[Task Scheduler](/docs/en-us/performance-optimization/microprofiler/task-scheduler.md)
to make an informed decision.

##### Context Test Results

| Environment | [IsStudio](/docs/reference/engine/classes/RunService.md) | [IsClient](/docs/reference/engine/classes/RunService.md) | [IsServer](/docs/reference/engine/classes/RunService.md) | [IsEdit](/docs/reference/engine/classes/RunService.md) | [IsRunning](/docs/reference/engine/classes/RunService.md) | [IsRunMode](/docs/reference/engine/classes/RunService.md) |
| --- | --- | --- | --- | --- | --- | --- |
| Live (Client) | `false` | `true` | `false` |  | `true` | `false` |
| Live (Server) | `false` | `false` | `true` |  | `true` | `false` |
| Edit | `true` | `true` | `true` | `true` | `false` | `false` |
| Collaborative Edit | `true` | `true` | `false` | `true` | `false` | `false` |
| Run Mode | `true` | `false` | `true` |  | `true` | `true` |
| Play Mode (Client) | `true` | `true` | `false` |  | `true` | `false` |
| Play Mode (Server) | `true` | `false` | `true` |  | `true` | `false` |
| Team Test (Client) | `true` | `true` | `false` |  | `true` | `false` |
| Team Test (Server) | `true` | `false` | `true` |  | `true` | `false` |
| Luau Execution | `false` | `false` | `true` |  | `false` | `false` |

## Properties

### Property: RunService.RunState

```json
{
  "type": "RunState",
  "access": "ReadOnly",
  "security": {
    "read": "None",
    "write": "PluginSecurity"
  },
  "serialization": {
    "can_load": false,
    "can_save": false
  },
  "thread_safety": "ReadSafe",
  "category": "Data",
  "capabilities": [
    "Basic",
    "PluginOrOpenCloud"
  ]
}
```

An [RunState](/docs/reference/engine/enums/RunState.md) value that reflects whether the game's simulation is
stopped, running, or paused. Reading reports the current state; setting it
transitions the simulation, equivalent to [RunService:Run()](/docs/reference/engine/classes/RunService.md),
[RunService:Pause()](/docs/reference/engine/classes/RunService.md), and [RunService:Stop()](/docs/reference/engine/classes/RunService.md) for the
corresponding states. Defaults to [RunState.Stopped](/docs/reference/engine/enums/RunState.md). Setting this
property requires `Plugin` security.

The state reported here backs the context methods on [RunService](/docs/reference/engine/classes/RunService.md):
it is `Running` when [IsRunning()](/docs/reference/engine/classes/RunService.md) returns
`true`, and `Stopped` when [IsEdit()](/docs/reference/engine/classes/RunService.md) returns
`true`.

## Methods

### Method: RunService:BindToAnimation

**Signature:** `RunService:BindToAnimation(function: Function, frequency?: StepFrequency, priority?: int): RBXScriptConnection`

`BindToAnimation()` binds a custom function to be called at a fixed
frequency which is independent of the frame rate. When
[Workspace.UseFixedSimulation](/docs/reference/engine/classes/Workspace.md) is enabled, these functions are
invoked before Animators update, making this the fixed-frequency
counterpart to [PreAnimation](/docs/reference/engine/classes/RunService.md). When fixed
simulation is disabled, they instead run immediately before
[BindToSimulation()](/docs/reference/engine/classes/RunService.md) callbacks, so no
pre-animation ordering should be assumed. In the server authority model,
bound functions will also get called when the client needs to resimulate.

Like [BindToSimulation()](/docs/reference/engine/classes/RunService.md), the bound
function is meant for physics controllers and prediction, so an error will
trigger if you read or write from unsynchronized properties or call an
unsynchronized method. This error is meant to help guide you in writing a
pure, synchronized simulation.

To synchronize inaccessible properties, you should store the relevant data
in [attributes](/docs/en-us/studio/properties.md#instance-attributes) and
update the relevant property in
[PostSimulation](/docs/reference/engine/classes/RunService.md) or
[RenderStepped](/docs/reference/engine/classes/RunService.md) by reading from attributes.
This will leverage attribute synchronization to keep the property fully
synchronized through the rollback mechanism.

*Security: None · Thread Safety: Unsafe · Capabilities: Basic*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `function` | `Function` |  | The function to call. This function will be passed one parameter called `deltaTime`, which shows the elapsed time since the callback's previous invocation. |
| `frequency` | `StepFrequency` | `Hz30` | Optional [StepFrequency](/docs/reference/engine/enums/StepFrequency.md) value indicating the frequency at which to call the bound function. Defaults to [StepFrequency.Hz30](/docs/reference/engine/enums/StepFrequency.md). |
| `priority` | `int` | `2000` | Optional priority of the binding as an integer; it determines the order in which bound functions are called within a simulation step. Lower numbers are called first. If two bindings have the same priority, the order between them is unspecified. Defaults to 2000. |

**Returns:** `RBXScriptConnection` — A [RBXScriptConnection](/docs/reference/engine/datatypes/RBXScriptConnection.md) that can be disconnected to
unregister the callback.

### Method: RunService:BindToAnimationParallel

**Signature:** `RunService:BindToAnimationParallel(function: Function, frequency?: StepFrequency, priority?: int): RBXScriptConnection`

`BindToAnimationParallel()` is the parallel counterpart to
[BindToAnimation()](/docs/reference/engine/classes/RunService.md). The calling script
must be a descendant of an [Actor](/docs/reference/engine/classes/Actor.md). A [ModuleScript](/docs/reference/engine/classes/ModuleScript.md) may also
register the callback when its current instantiation was required by a
script associated with an [Actor](/docs/reference/engine/classes/Actor.md). Each fixed animation phase runs
its serial bindings first, then runs due parallel bindings concurrently
across [Actor](/docs/reference/engine/classes/Actor.md) VMs; `priority` orders callbacks within one VM but
does not define an order between different VMs.

The callback has the same simulation restrictions as
[BindToAnimation()](/docs/reference/engine/classes/RunService.md). Calling
[task.synchronize()](/docs/reference/engine/globals/task.md) resumes the callback in serial execution
within the same fixed-step phase. A later [task.synchronize()](/docs/reference/engine/globals/task.md)
returns it to parallel execution. The engine finishes these continuations
before advancing beyond the phase.

*Security: None · Thread Safety: Unsafe · Capabilities: Basic*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `function` | `Function` |  | The function to call. This function receives a `deltaTime` parameter containing the elapsed time since its previous invocation. |
| `frequency` | `StepFrequency` | `Hz30` | Optional [StepFrequency](/docs/reference/engine/enums/StepFrequency.md) value indicating how often to call the bound function. Defaults to [StepFrequency.Hz30](/docs/reference/engine/enums/StepFrequency.md). |
| `priority` | `int` | `2000` | Optional binding priority. Lower numbers run first within the same [Actor](/docs/reference/engine/classes/Actor.md) VM. Defaults to `2000`. |

**Returns:** `RBXScriptConnection` — A [RBXScriptConnection](/docs/reference/engine/datatypes/RBXScriptConnection.md) that can be disconnected to
unregister the callback.

### Method: RunService:BindToRenderStep

**Signature:** `RunService:BindToRenderStep(name: string, priority: int, function: Function): ()`

The `BindToRenderStep()` function binds a custom function to be called at
a specific time during the render step. There are three main arguments:
`name`, `priority`, and what `function` to call.

As it is linked to the client's rendering process, `BindToRenderStep()`
can only be called on the client.

##### Name

The `name` parameter is a label for the binding and can be used with
[RunService:UnbindFromRenderStep()](/docs/reference/engine/classes/RunService.md) if the binding is no longer
needed.

```lua
local RunService = game:GetService("RunService")

local function functionToBind() end

-- Bind the function above to the binding named "tempBinding"
RunService:BindToRenderStep("tempBinding", 1, functionToBind)
-- Unbind the function bound to "tempBinding"
RunService:UnbindFromRenderStep("tempBinding")
```

##### Priority

The `priority` of the binding is an integer; it determines when during the
render step to call the custom function. The lower this number, the sooner
the custom function will be called. If two bindings have the same
priority, the engine will randomly pick one to run first. The default
control scripts run with these specific priorities:

- Player Input: `100`
- Camera Controls: `200` For convenience; the [RenderPriority](/docs/reference/engine/enums/RenderPriority.md) enum
  can be used to determine the integer value to set a binding. For
  example, to make a binding right before the default camera update,
  simply subtract `1` from the camera priority level.

When using [RenderPriority](/docs/reference/engine/enums/RenderPriority.md), remember to use `.Value` at the end of
the desired enum. [RunService:BindToRenderStep()](/docs/reference/engine/classes/RunService.md) will not work if
just the enum is used on its own.

```lua
local RunService = game:GetService("RunService")

local function beforeCamera(delta)
	-- Code in here will run before the default camera script
end

RunService:BindToRenderStep("Before camera", Enum.RenderPriority.Camera.Value - 1, beforeCamera)
```

##### Custom Function and Delta Time

The last argument (`function`) is the custom function to call. This
function will be passed one parameter called `deltaTime` which shows how
much time passed between the beginning of the previous render step and the
beginning of the current render step.

All rendering updates will wait until the code in the render step
finishes. Make sure that any code called by `BindToRenderStep()` runs
quickly and efficiently; if code takes too long, the experience visuals
will be choppy.

*Security: None · Thread Safety: Unsafe · Capabilities: Basic*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `name` | `string` |  | Label for the binding which can be used with [Unbind](/docs/reference/engine/classes/RunService.md) if the binding is no longer needed. |
| `priority` | `int` |  | Priority of the binding as an integer; it determines when during the render step to call the custom function. The lower this number, the sooner the custom function will be called. If two bindings have the same priority, the engine will randomly pick one to run first. |
| `function` | `Function` |  | The custom function being bound. |

**Returns:** `()`

**Frame Moving in Circle**

This code sample moves a GuiObject in a circle within its parent object using
RunService's BindToRenderStep. It defines a parametric equation in a function
to help with positioning the GuiObject.

To try this code out, put a ScreenGui in the StarterGui. Inside the ScreenGui,
insert a Frame with a LocalScript. Paste this code into the LocalScript, then
play the game. Watch the Frame travel counterclockwise within.

```lua
local RunService = game:GetService("RunService")

-- How fast the frame ought to move
local SPEED = 2

local frame = script.Parent
frame.AnchorPoint = Vector2.new(0.5, 0.5)

-- A simple parametric equation of a circle
-- centered at (0.5, 0.5) with radius (0.5)
local function circle(t)
	return 0.5 + math.cos(t) * 0.5, 0.5 + math.sin(t) * 0.5
end

-- Keep track of the current time
local currentTime = 0
local function onRenderStep(deltaTime)
	-- Update the current time
	currentTime = currentTime + deltaTime * SPEED
	-- ...and the frame's position
	local x, y = circle(currentTime)
	frame.Position = UDim2.new(x, 0, y, 0)
end

-- This is just a visual effect, so use the "Last" priority
RunService:BindToRenderStep("FrameCircle", Enum.RenderPriority.Last.Value, onRenderStep)
--RunService.RenderStepped:Connect(onRenderStep) -- Also works, but not recommended
```

**RunService Custom Function**

This example shows how to bind a simple function to the render step. All this
function does is print how much time passed between the last render step and
the current one. Note that this code will need to be in a `LocalScript` to
run.

```lua
local RunService = game:GetService("RunService")

local function checkDelta(deltaTime)
	print("Time since last render step:", deltaTime)
end

RunService:BindToRenderStep("Check delta", Enum.RenderPriority.First.Value, checkDelta)
```

**Bind and Unbind a Function**

This example uses the `RunService` to bind and unbind a function named
`printHello`. First, we bind the function to the RenderStep so that fires
every _step_. Then, after we wait 5 seconds (`wait(5)`), we unbind the
function.

```lua
local RunService = game:GetService("RunService")

-- Step 1: Declare the function and a name
local NAME = "Print Hello"
local function printHello()
	print("Hello")
end

-- Step 2: Bind the function
RunService:BindToRenderStep(NAME, Enum.RenderPriority.First.Value, printHello)

-- Step 3: Unbind the function
RunService:UnbindFromRenderStep(NAME)
```

### Method: RunService:BindToSimulation

**Signature:** `RunService:BindToSimulation(function: Function, frequency?: StepFrequency, priority?: int): RBXScriptConnection`

`BindToSimulation()` binds a custom function to be called at a fixed
frequency which is independent of the frame rate. In the server authority
model, bound functions will also get called when the client needs to
resimulate. This method is only available when
[Workspace.UseFixedSimulation](/docs/reference/engine/classes/Workspace.md) is enabled.

Note that since the bound function is meant for physics controllers and
prediction, an error will trigger if you read or write from unsynchronized
properties or call an unsynchronized method. This error is meant to help
guide you in writing a pure, synchronized simulation.

To synchronize inaccessible properties, you should store the relevant data
in [attributes](/docs/en-us/studio/properties.md#instance-attributes) and
update the relevant property in
[PostSimulation](/docs/reference/engine/classes/RunService.md) or
[RenderStepped](/docs/reference/engine/classes/RunService.md) by reading from attributes.
This will leverage attribute synchronization to keep the property fully
synchronized through the rollback mechanism.

*Security: None · Thread Safety: Unsafe · Capabilities: Basic*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `function` | `Function` |  | The function to call. This function will be passed one parameter called `deltaTime` which shows how much time passed between the beginning of the previous simulation step and the beginning of the current simulation step. |
| `frequency` | `StepFrequency` | `Hz30` | Optional [StepFrequency](/docs/reference/engine/enums/StepFrequency.md) value indicating the frequency at which to call the bound function. If not provided, the default frequency will be used. |
| `priority` | `int` | `2000` | Optional priority of the binding as an integer; it determines the order in which bound functions are called within a simulation step. Lower numbers are called first. If two bindings have the same priority, the order between them is unspecified. Defaults to 2000. |

**Returns:** `RBXScriptConnection` — An [RBXScriptConnection](/docs/reference/engine/datatypes/RBXScriptConnection.md) that can be disconnected to unbind
the function from the simulation step.

**Synchronizing a Part's Color Property**

```lua
local RunService = game:GetService("RunService")
local Workspace = game:GetService("Workspace")

local somePart:BasePart = Workspace:WaitForChild("Part")

RunService:BindToSimulation(function(deltaTime: number)
	local syncdColor = Color3.fromHSV(math.fmod(time(), 1.0), 1.0, 1.0)
	somePart:SetAttribute("SyncdColor", syncdColor)
end)

RunService.RenderStepped:Connect(function(deltaTime: number) 
	local syncdColor = somePart:GetAttribute("SyncdColor")
	somePart.Color = syncdColor
end)
```

### Method: RunService:BindToSimulationParallel

**Signature:** `RunService:BindToSimulationParallel(function: Function, frequency?: StepFrequency, priority?: int): RBXScriptConnection`

`BindToSimulationParallel()` is the parallel counterpart to
[BindToSimulation()](/docs/reference/engine/classes/RunService.md). The calling
script must be a descendant of an [Actor](/docs/reference/engine/classes/Actor.md). A [ModuleScript](/docs/reference/engine/classes/ModuleScript.md)
may also register the callback when its current instantiation was required
by a script associated with an [Actor](/docs/reference/engine/classes/Actor.md). Each fixed simulation phase
runs its serial bindings first, then runs due parallel bindings
concurrently across [Actor](/docs/reference/engine/classes/Actor.md) VMs; `priority` orders callbacks within
one VM but does not define an order between different VMs.

The callback has the same restrictions on unsynchronized properties and
methods as [BindToSimulation()](/docs/reference/engine/classes/RunService.md).
Calling [task.synchronize()](/docs/reference/engine/globals/task.md) resumes the callback in serial
execution within the same fixed-step phase. A later
[task.desynchronize()](/docs/reference/engine/globals/task.md) returns it to parallel execution. The
engine finishes these continuations before advancing beyond the phase.

*Security: None · Thread Safety: Unsafe · Capabilities: Basic*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `function` | `Function` |  | The function to call. This function receives a `deltaTime` parameter containing the elapsed time since its previous invocation. |
| `frequency` | `StepFrequency` | `Hz30` | Optional [StepFrequency](/docs/reference/engine/enums/StepFrequency.md) value indicating how often to call the bound function. Defaults to [StepFrequency.Hz30](/docs/reference/engine/enums/StepFrequency.md). |
| `priority` | `int` | `2000` | Optional binding priority. Lower numbers run first within the same [Actor](/docs/reference/engine/classes/Actor.md) VM. Defaults to `2000`. |

**Returns:** `RBXScriptConnection` — A [RBXScriptConnection](/docs/reference/engine/datatypes/RBXScriptConnection.md) that can be disconnected to
unregister the callback.

### Method: RunService:GetPredictionStatus

**Signature:** `RunService:GetPredictionStatus(context: Instance): PredictionStatus`

Clients can use this method to check the [PredictionStatus](/docs/reference/engine/enums/PredictionStatus.md) of a
specific context instance, useful for debugging scripts affecting multiple
instances (vehicle controllers, custom physics, etc.) where some might be
predicted and others might not. This method is also useful for debugging
and observing the effects of [PredictionMode.Automatic](/docs/reference/engine/enums/PredictionMode.md) prediction
mode.

*Security: None · Thread Safety: Unsafe · Capabilities: Basic · Simulation Access: true*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `context` | `Instance` |  | The [Instance](/docs/reference/engine/classes/Instance.md) for which to check prediction status. |

**Returns:** `PredictionStatus` — The [PredictionStatus](/docs/reference/engine/enums/PredictionStatus.md) of the given instance, indicating whether
it is predicted, authoritative, or not participating in prediction.

### Method: RunService:IsClient

**Signature:** `RunService:IsClient(): boolean`

If the code that invoked this method is running in a client context (in a
[LocalScript](/docs/reference/engine/classes/LocalScript.md), in a [ModuleScript](/docs/reference/engine/classes/ModuleScript.md) required by a
[LocalScript](/docs/reference/engine/classes/LocalScript.md), or in a [Script](/docs/reference/engine/classes/Script.md) with
[RunContext](/docs/reference/engine/classes/BaseScript.md) set to [RunContext.Client](/docs/reference/engine/enums/RunContext.md)),
this method will return `true`. In all other cases, this method will
return `false`.

If this method returns `true`, the current environment can access
client‑only features like [RunService.PreRender](/docs/reference/engine/classes/RunService.md) or
[Players.LocalPlayer](/docs/reference/engine/classes/Players.md).

*Security: None · Thread Safety: Safe · Capabilities: Basic*

**Returns:** `boolean` — Whether the current environment is running the client.

### Method: RunService:IsEdit

**Signature:** `RunService:IsEdit(): boolean`

This method returns whether the current environment is in "edit" mode, for
example in Studio when the experience is not running.

`IsEdit()` will return the inverse of
[IsRunning()](/docs/reference/engine/classes/RunService.md), except when the simulation has
been paused, in which case both methods will return `false`.

*Security: None · Thread Safety: Safe · Capabilities: Basic, PluginOrOpenCloud*

**Returns:** `boolean` — Whether the current environment is in "edit" mode.

### Method: RunService:IsResimulating

**Signature:** `RunService:IsResimulating(): boolean`

Returns `true` if the engine is currently replaying simulation steps after
detecting a misprediction in the server authority model; returns `false`
otherwise. When the server's authoritative state diverges from the
client's predicted state, the client rolls back and rapidly resimulates
all affected steps within a single frame. During that resimulation pass,
[BindToSimulation()](/docs/reference/engine/classes/RunService.md) callbacks and
property-changed signals fire again for each replayed step, which can
cause unwanted side effects such as duplicate sound playback or redundant
network requests.

*Security: None · Thread Safety: Safe · Capabilities: Basic · Simulation Access: true*

**Returns:** `boolean` — Whether the engine is currently resimulating.

### Method: RunService:IsRunMode

**Signature:** `RunService:IsRunMode(): boolean`

This method returns whether a **Run** playtest has been initiated in
Studio. It will continue to return `true` if the simulation has been
paused using the **Pause** button; however, once it has been stopped using
the **Stop** button, it will revert to returning `false`. Note that Studio
only enters "run" mode when a **Run** playtest (without the user's player
character) is initiated. Also note that this method will return `false` if
the simulation was started using [RunService:Run()](/docs/reference/engine/classes/RunService.md).

*Security: None · Thread Safety: Safe · Capabilities: Basic*

**Returns:** `boolean` — Whether a **Run** playtest has been initiated in Studio.

### Method: RunService:IsRunning

**Signature:** `RunService:IsRunning(): boolean`

Returns whether the experience is currently running. `IsRunning()` will
always return the inverse of [IsEdit()](/docs/reference/engine/classes/RunService.md) except
when the simulation has been paused, in which case both methods will
return `false`.

*Security: None · Thread Safety: Unsafe · Capabilities: Basic*

**Returns:** `boolean` — Whether the experience is currently running.

### Method: RunService:IsServer

**Signature:** `RunService:IsServer(): boolean`

This method returns whether the current environment is running on the
server. If the code that invoked this method is running in a server
context (in a [Script](/docs/reference/engine/classes/Script.md) with [RunContext](/docs/reference/engine/classes/BaseScript.md)
set to [RunContext.Server](/docs/reference/engine/enums/RunContext.md) or [RunContext.Legacy](/docs/reference/engine/enums/RunContext.md), or in a
[ModuleScript](/docs/reference/engine/classes/ModuleScript.md) required by a [Script](/docs/reference/engine/classes/Script.md)), this method will
return `true`. In all other cases, this method will return `false`.

If this function returns true, then the current environment can access
server‑only features like [ServerStorage](/docs/reference/engine/classes/ServerStorage.md) or
[ServerScriptService](/docs/reference/engine/classes/ServerScriptService.md).

*Security: None · Thread Safety: Safe · Capabilities: Basic*

**Returns:** `boolean` — Whether the current environment is running on the server.

### Method: RunService:IsStudio

**Signature:** `RunService:IsStudio(): boolean`

This method returns whether the current environment is running in Studio.
It can be used to wrap code that should only execute when testing in
Studio.

*Security: None · Thread Safety: Safe · Capabilities: Basic*

**Returns:** `boolean` — Whether the current environment is running in Studio.

### Method: RunService:Pause

**Signature:** `RunService:Pause(): ()`

This method pauses the experience's simulation if it is running,
suspending physics and scripts. When the simulation is paused,
[IsRunning()](/docs/reference/engine/classes/RunService.md) will return `false`.

*Security: PluginSecurity · Thread Safety: Unsafe · Capabilities: Basic*

**Returns:** `()`

### Method: RunService:Run

**Signature:** `RunService:Run(): ()`

This method runs the experience's simulation (physics and scripts). When
the simulation is running, [IsRunning()](/docs/reference/engine/classes/RunService.md) will
return `true`. However, [IsRunMode()](/docs/reference/engine/classes/RunService.md) will
only return `true` if the simulation was started using the **Run** button
in Studio.

*Security: PluginSecurity · Thread Safety: Unsafe · Capabilities: Basic*

**Returns:** `()`

### Method: RunService:SetPredictionMode

**Signature:** `RunService:SetPredictionMode(context: Instance, mode: PredictionMode): ()`

Sets the prediction mode for an [Instance](/docs/reference/engine/classes/Instance.md) (`context`) to an
[PredictionMode](/docs/reference/engine/enums/PredictionMode.md) value. Mismatches between the physics properties or
attributes for predicted instances will cause a rollback and resimulation
on the client. Can only be called on the client.

*Security: None · Thread Safety: Unsafe · Capabilities: Basic*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `context` | `Instance` |  | The [Instance](/docs/reference/engine/classes/Instance.md) for which to set the prediction mode. |
| `mode` | `PredictionMode` |  | The [PredictionMode](/docs/reference/engine/enums/PredictionMode.md) to set for the context instance. |

**Returns:** `()`

### Method: RunService:Stop

**Signature:** `RunService:Stop(): ()`

This method stops the experience's simulation if it is running. When the
simulation is stopped, [IsRunning()](/docs/reference/engine/classes/RunService.md) will
return `false` and [IsEdit()](/docs/reference/engine/classes/RunService.md) will return
`true`.

In contrast to the **Stop** button in Studio, calling this method will not
restore the experience to the state it was in prior to the simulation
being run. This means any changes made to the experience by the physics
simulation and scripts will persist after the simulation has ended.

*Security: PluginSecurity · Thread Safety: Unsafe · Capabilities: Basic*

**Returns:** `()`

### Method: RunService:UnbindFromRenderStep

**Signature:** `RunService:UnbindFromRenderStep(name: string): ()`

Given a name of a function sent to
[BindToRenderStep()](/docs/reference/engine/classes/RunService.md), this method will
unbind the function from being called during
[PreRender](/docs/reference/engine/classes/RunService.md). This is used to unbind bound
functions once they are no longer needed, or when they no longer need to
fire every step.

If there is no bound function by the given name, this method takes no
action and continues without raising an error.

*Security: None · Thread Safety: Unsafe · Capabilities: Basic*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `name` | `string` |  | The name of the function being unbound. |

**Returns:** `()`

### Method: RunService:Reset

**Signature:** `RunService:Reset(): ()`

> **Deprecated:** This item is deprecated and should not be used in new work.

The Reset function resets the current game to a waypoint set when Run was
called. This method should only be used after Run was called.

*Security: PluginSecurity · Thread Safety: Unsafe · Capabilities: Basic*

**Returns:** `()`

## Events

### Event: RunService.Heartbeat

**Signature:** `RunService.Heartbeat(deltaTime: double)`

The `Heartbeat` event fires every frame, after the physics simulation has
completed. The `deltaTime` argument indicates the time that has elapsed
since the previous frame.

This event is when most scripts run. It occurs at the end of each frame
and it's also when any waiting scripts are executed, such as those
scheduled with the [task](/docs/reference/engine/globals/task.md) library. `Heartbeat` is commonly used
for periodic tasks, such as updating core game systems like health
regeneration.

Following this step, the engine sends property updates and events to the
server or clients which are later received as part of the
[replication](/docs/en-us/projects/client-server.md#replication) receive
step.

*Security: None · Capabilities: Basic*

**Parameters:**

| Name | Type | Description |
|------|------|-------------|
| `deltaTime` | `double` | The time (in seconds) that has elapsed since the previous frame. |

### Event: RunService.Misprediction

**Signature:** `RunService.Misprediction(time: double, instances: Array, stats: Dictionary)`

With server authority enabled, the Misprediction event fires when a
received server state differs from the predicted state.

Use this event to build debugging tools that inspect misprediction data
programmatically. For example, a plugin could listen for this event and
track which instances are frequently mispredicting, what properties are
diverging, and by how much.

##### Instances Array

Each entry in the `instances` array is a table with the following
structure:

| Field | Type | Description |
| --- | --- | --- |
| `Instance` | `Instance` | The instance that was mispredicted. |
| `Properties` | `dictionary?` | Properties that were mispredicted. Each key is a property name mapping to a table with the client's `Predicted` and owner's/server's `Authoritative` values as captured on the step when the client first mispredicted the owner's value. Only present if there are property mismatches. |
| `Attributes` | `dictionary?` | Attributes that were mispredicted. Each key is a property name mapping to a table with the client's `Predicted` and owner's/server's `Authoritative` values as captured on the step when the client first mispredicted the owner's value. Only present if there are attribute mismatches. |

##### Stats Dictionary

The `stats` dictionary contains the following fields:

| Field | Type | Description |
| --- | --- | --- |
| `ResimulationTime` | number | The time spent during resimulation (or the amount of time rolled back). |

##### Code Sample

*Security: None · Capabilities: Basic, PluginOrOpenCloud*

**Parameters:**

| Name | Type | Description |
|------|------|-------------|
| `time` | `double` | The time (in seconds) from the start of simulation at which the client's predicted state first diverged from the server's authoritative state. |
| `instances` | `Array` | An array of tables, each describing an [Instance](/docs/reference/engine/classes/Instance.md) that was mispredicted. See below for the structure of each entry. |
| `stats` | `Dictionary` | A dictionary of statistics about the misprediction. See below for the structure. |

**Misprediction**

Demonstrates [RunService:Misprediction()](/docs/reference/engine/classes/RunService.md).

```lua
local RunService = game:GetService("RunService")

RunService.Misprediction:Connect(function(time, instances, stats)
	print(`Misprediction at t={time}, resim={stats.ResimulationTime}s`)

	for _, entry in instances do
		print(`  Instance: {entry.Instance:GetFullName()}`)

		if entry.Properties then
			for name, values in entry.Properties do
				print(`    Property '{name}': predicted={values.Predicted}, authoritative={values.Authoritative}`)
			end
		end

		if entry.Attributes then
			for name, values in entry.Attributes do
				print(`    Attribute '{name}': predicted={values.Predicted}, authoritative={values.Authoritative}`)
			end
		end
	end
end)
```

### Event: RunService.PostSimulation

**Signature:** `RunService.PostSimulation(deltaTimeSim: double)`

The `PostSimulation` event fires every frame, after the physics simulation
has completed. The `deltaTimeSim` argument indicates the time that the
current frame has stepped the physics simulation, not accounting for
physics throttling. This may deviate from the actual time between frames
in Studio edit mode or when framerate is very low.

This event is useful for making final adjustments to the outcome of the
simulation. Following this phase, the engine triggers the
[Heartbeat](/docs/reference/engine/classes/RunService.md) event.

*Security: None · Capabilities: Basic*

**Parameters:**

| Name | Type | Description |
|------|------|-------------|
| `deltaTimeSim` | `double` | The time (in seconds) that the current frame has stepped the physics simulation, not accounting for physics throttling. |

### Event: RunService.PreAnimation

**Signature:** `RunService.PreAnimation(deltaTimeSim: double)`

The `PreAnimation` event fires every frame, prior to the physics
simulation but after rendering. The `deltaTimeSim` argument indicates the
time that the current frame has stepped animations.

This event is useful for modifying animation objects, such as adjusting
their speed or priority. Once the `PreAnimation` event is complete, the
engine proceeds to run these animations, updating the joint transforms
which will later be used to update objects during the physics simulation.

After animations are stepped, the engine triggers the
[PreSimulation](/docs/reference/engine/classes/RunService.md) event.

*Security: None · Capabilities: Basic*

**Parameters:**

| Name | Type | Description |
|------|------|-------------|
| `deltaTimeSim` | `double` | The time (in seconds) that the current frame has stepped animations. |

### Event: RunService.PreRender

**Signature:** `RunService.PreRender(deltaTimeRender: double)`

The `PreRender` event (replacement for
[RenderStepped](/docs/reference/engine/classes/RunService.md)) fires every frame, prior
to the frame being rendered. The `deltaTimeRender` argument indicates the
time that has elapsed since the previous frame.

This event allows you to run code and update the world before it's drawn
on a player's screen. This is useful for last‑minute adjustments such as
changing object positions, updating animations, or preparing visual
effects, but it should be used sparingly as the engine cannot start to
render the frame until code running in this event has finished executing.

As `PreRender` is client-side, it can only be used in a
[LocalScript](/docs/reference/engine/classes/LocalScript.md), in a [ModuleScript](/docs/reference/engine/classes/ModuleScript.md) required by a
[LocalScript](/docs/reference/engine/classes/LocalScript.md), or in a [Script](/docs/reference/engine/classes/Script.md) with
[RunContext](/docs/reference/engine/classes/BaseScript.md) set to [RunContext.Client](/docs/reference/engine/enums/RunContext.md).

*Security: None · Capabilities: Basic*

**Parameters:**

| Name | Type | Description |
|------|------|-------------|
| `deltaTimeRender` | `double` | The time (in seconds) that has elapsed since the previous frame. |

### Event: RunService.PreSimulation

**Signature:** `RunService.PreSimulation(deltaTimeSim: double)`

The `PreSimulation` event (replacement for
[Stepped](/docs/reference/engine/classes/RunService.md)) fires every frame, prior to the
physics simulation. The `deltaTimeSim` argument indicates the time that
the current frame will step the physics simulation, not accounting for
physics throttling. This may deviate from the actual time between frames
in Studio edit mode or when framerate is very low.

This event is useful for adjusting properties like velocity or forces just
before they're applied as part of the simulation. The simulation then
runs, potentially multiple times, as the physics solver runs at a higher
frequency than other engine systems. Once this is complete, the
[PostSimulation](/docs/reference/engine/classes/RunService.md) event is fired.

*Security: None · Capabilities: Basic*

**Parameters:**

| Name | Type | Description |
|------|------|-------------|
| `deltaTimeSim` | `double` | The time (in seconds) that the current frame will step the physics simulation, not accounting for physics throttling. |

### Event: RunService.RenderStepped

**Signature:** `RunService.RenderStepped(deltaTime: double)`

Fires every frame, prior to the frame being rendered.

##### Migration Note

This event has been superseded by [PreRender](/docs/reference/engine/classes/RunService.md)
which should be used for new work.

*Security: None · Capabilities: Basic*

**Parameters:**

| Name | Type | Description |
|------|------|-------------|
| `deltaTime` | `double` | The time (in seconds) that has elapsed since the previous frame. |

### Event: RunService.Rollback

**Signature:** `RunService.Rollback(time: double)`

When server authority is enabled, the `Rollback` event fires after the
engine detects a misprediction and rolls back all eligible state
(properties, attributes, and related physics and animation state), but
before the engine resimulates the rolled-back steps.

Use this event to update state in your place that wouldn't otherwise be
rolled back after a misprediction. For example, if you maintain gameplay
state that can't be stored in a property or attribute with simulation
access, you can listen for this event, compare the rolled-back-to step
against your farthest-reached step, and rewind your custom state
accordingly.

*Security: None · Capabilities: Basic*

**Parameters:**

| Name | Type | Description |
|------|------|-------------|
| `time` | `double` | The time (in seconds) that we are rolling back to. |

**Rollback**

Demonstrates [RunService:Rollback()](/docs/reference/engine/classes/RunService.md).

```lua
local RunService = game:GetService("RunService")

local stateHistory = {} -- your custom state tracked per fixed step

RunService.Rollback:Connect(function(time)
	-- Discard any custom state newer than the rolled-back-to step
	-- and restore the state at that step before resimulation begins
	for step, _ in stateHistory do
		if step > time then
			stateHistory[step] = nil
		end
	end
end)
```

### Event: RunService.Stepped

**Signature:** `RunService.Stepped(time: double, deltaTime: double)`

Fires every frame, prior to the physics simulation.

##### Migration Note

This event has been superseded by
[PreSimulation](/docs/reference/engine/classes/RunService.md) which should be used for
new work.

*Security: None · Capabilities: Basic*

**Parameters:**

| Name | Type | Description |
|------|------|-------------|
| `time` | `double` | The duration (in seconds) that [RunService](/docs/reference/engine/classes/RunService.md) has been running for. |
| `deltaTime` | `double` | The time (in seconds) that has elapsed since the previous frame. |

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