---
name: Tool
last_updated: 2026-10-30T19:55:53Z
inherits:
  - BackpackItem
  - Model
  - PVInstance
  - Instance
  - Object
type: class
memory_category: BaseParts
summary: "An object, such as a weapon, that can be equipped by a Humanoid."
---

# Class: Tool

> An object, such as a weapon, that can be equipped by a [Humanoid](/docs/reference/engine/classes/Humanoid.md).

## Description

A `Tool` is an object that a [Humanoid](/docs/reference/engine/classes/Humanoid.md) object can equip. For players,
they are stored in a [Backpack](/docs/reference/engine/classes/Backpack.md) object parented to a [Player](/docs/reference/engine/classes/Player.md)
object. In-experience, players may have multiple tools which appear as icons
at the bottom of the screen. Equipping a tool moves it from the
[Backpack](/docs/reference/engine/classes/Backpack.md) and into a [Player.Character](/docs/reference/engine/classes/Player.md) model in the
[Workspace](/docs/reference/engine/classes/Workspace.md). By default, tools are held in the right hand and have a
handle in them, which is a [BasePart](/docs/reference/engine/classes/BasePart.md) named `Handle` inside (although
one isn't required if [Tool.RequiresHandle](/docs/reference/engine/classes/Tool.md) is `false`). Tools that are
to be provided to (re)spawning players should be stored in the
[StarterPack](/docs/reference/engine/classes/StarterPack.md).

## Code Samples

**Explode Tool Example**

This code is meant to be placed in a Script within a Tool. It allows a player
to spawn explosions by equipping the tool and clicking on the ground. It does
so by defining a function, `explode`, which creates a non-deadly explosion at
a given point. Then, it defines a function, `onActivated`, that runs when the
tool is activated. Finally, it connects the Activated event of the tool to the
`onActivated` function.

To test this code out, try creating a Tool and put a Part inside it. Name the
Part "Handle". Put a Script inside the Tool next, and paste the code into it.
Finally, put the Tool in the StarterPack.

```lua
local tool = script.Parent

local function explode(point)
	local e = Instance.new("Explosion")
	e.DestroyJointRadiusPercent = 0 -- Make the explosion non-deadly
	e.Position = point
	e.Parent = workspace
end

local function onActivated()
	-- Get the Humanoid that Activated the tool
	local human = tool.Parent.Humanoid
	-- Call explode with the current point the Humanoid is targetting
	explode(human.TargetPoint)
end

tool.Activated:Connect(onActivated)
```

**Sword Tool Example**

This code sample is for a Tool object with a Part named Handle. It detects
when Humanoids other than the current holder hit the handle, and deals some
damage to them. In addition, when the Tool is activated, it triggers a slash
animation in the default character animation scripts. Try out this script by
creating a Tool object in the StarterPack. Put a Part inside it, and name it
Handle. Paste this code into a Script inside the Tool, then try slashing at
another Humanoid!

```lua
local tool = script.Parent

local function onTouch(partOther)
	-- First, try to see if the part we touched was part of a Humanoid
	local humanOther = partOther.Parent:FindFirstChild("Humanoid")
	-- Ignore touches by non-humanoids
	if not humanOther then
		return
	end

	-- Ignore touches by the Humanoid carrying the sword
	if humanOther.Parent == tool.Parent then
		return
	end

	humanOther:TakeDamage(5)
end

-- Trigger a slash animation
local function slash()
	-- Default character scripts will listen for a "toolanim" StringValue
	local value = Instance.new("StringValue")
	value.Name = "toolanim"
	value.Value = "Slash" -- try also: Lunge
	value.Parent = tool
end

tool.Activated:Connect(slash)
tool.Handle.Touched:Connect(onTouch)
```

## Properties

### Property: Tool.CanBeDropped

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
    "Input"
  ]
}
```

The CanBeDropped property controls whether the player can drop the
[Tool](/docs/reference/engine/classes/Tool.md).

If true, when the backspace button is pressed, the tool will be parented
to [Workspace](/docs/reference/engine/classes/Workspace.md) and removed from the player's [Backpack](/docs/reference/engine/classes/Backpack.md). If
false, nothing will happen when backspace is pressed, and the tool will
remain equipped.

### Property: Tool.Enabled

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
  "category": "State",
  "capabilities": [
    "Input"
  ],
  "simulationAccess": true
}
```

The **Enabled** property relates to whether or not the [Tool](/docs/reference/engine/classes/Tool.md) can be
used. This is useful if you want to prevent a player from using a tool,
but don't want to remove it from their [Backpack](/docs/reference/engine/classes/Backpack.md).

When set to `true`, the player can use the tool. When set to `false`, the
tool is disabled and the player cannot use it; this prevents the tool from
being activated or deactivated by the [Tool:Activate()](/docs/reference/engine/classes/Tool.md) and
[Tool:Deactivate()](/docs/reference/engine/classes/Tool.md) methods, and it prevents the
[Tool.Activated](/docs/reference/engine/classes/Tool.md) and [Tool.Deactivated](/docs/reference/engine/classes/Tool.md) events from firing.

**Superjump Tool**

The code sample below creates [Tool](/docs/reference/engine/classes/Tool.md) in the local player's
[Backpack](/docs/reference/engine/classes/Backpack.md) that increases their [JumpPower](/docs/reference/engine/classes/Humanoid.md)
from `50` to `150` for 5 seconds.

This example uses the tool's [Tool.Enabled](/docs/reference/engine/classes/Tool.md) property as a debounce by
setting the property to `true` when the player jumps and back to `false` after
the 5 second duration.

Unequipping the tool also stops the player from super jumping by changing the
[JumpPower](/docs/reference/engine/classes/Humanoid.md) back to `50`.

```lua
local Players = game:GetService("Players")

local player = Players.LocalPlayer
local character = player.Character or player.CharacterAdded:Wait()
local humanoid = character:WaitForChild("Humanoid")

local tool = Instance.new("Tool")
tool.Name = "SuperJump"
tool.RequiresHandle = false
tool.Parent = player.Backpack

function toolActivated()
	humanoid.JumpPower = 150
	tool.Enabled = false
	task.wait(5)
	tool.Enabled = true
	humanoid.JumpPower = 50
end

tool.Activated:Connect(toolActivated)
tool.Unequipped:Connect(function()
	humanoid.JumpPower = 50
end)
```

### Property: Tool.Grip

```json
{
  "type": "CFrame",
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
  "category": "Transform",
  "capabilities": [
    "Input"
  ],
  "simulationAccess": true
}
```

The `Grip` property stores the tool's "grip" properties as a single
[CFrame](/docs/reference/engine/datatypes/CFrame.md). These properties position how the player holds the tool
and include [GripUp](/docs/reference/engine/classes/Tool.md), [GripRight](/docs/reference/engine/classes/Tool.md),
[GripForward](/docs/reference/engine/classes/Tool.md), and [GripPos](/docs/reference/engine/classes/Tool.md).

**Grip Stick**

The code below insert's a [Tool](/docs/reference/engine/classes/Tool.md) named **Stick** into the local player's
[BackPack](/docs/reference/engine/classes/BackPack.md). When the player activates the tool, the code prints the
values of the tool's grip properties.

```lua
local Players = game:GetService("Players")

local player = Players.LocalPlayer

local tool = Instance.new("Tool")
tool.Name = "Stick"
tool.Parent = player.Backpack

local handle = Instance.new("Part")
handle.Name = "Handle"
handle.Parent = tool
handle.Size = Vector3.new(0.1, 3, 0.1)
handle.Color = Color3.fromRGB(108, 88, 75) -- Brown

tool.Activated:Connect(function()
	print(tool.Grip)
	print(tool.GripUp)
	print(tool.GripRight)
	print(tool.GripForward)
	print(tool.GripPos)
end)
```

### Property: Tool.ManualActivationOnly

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
    "Input"
  ]
}
```

This property controls whether the [Tool](/docs/reference/engine/classes/Tool.md) can be activated without
explicitly executing [Tool:Activate()](/docs/reference/engine/classes/Tool.md) in a script.

When set to `true`, the tool will only fire [Tool.Activated](/docs/reference/engine/classes/Tool.md) when
[Tool:Activate()](/docs/reference/engine/classes/Tool.md) is called. This also suppresses the
[ContextActionService:BindActivate()](/docs/reference/engine/classes/ContextActionService.md) function.

When set to `false`, mouse clicks (when the tool is equipped) will also
fire [Tool.Activated](/docs/reference/engine/classes/Tool.md).

**Sprint Tool**

The code sample below creates [Tool](/docs/reference/engine/classes/Tool.md) in the local player's
[Backpack](/docs/reference/engine/classes/Backpack.md) that increases their [WalkSpeed](/docs/reference/engine/classes/Humanoid.md)
from `16` to `30` for 5 seconds.

This example uses the tool's [Tool.ManualActivationOnly](/docs/reference/engine/classes/Tool.md) property as a
debounce by setting the property to `true` when the player begins sprinting
and to `false` when the player stops sprinting. As a result, when the player
is sprinting, the tool cannot be re-activated.

Unequipping the tool also stops the player from sprinting by changing the
[WalkSpeed](/docs/reference/engine/classes/Humanoid.md) to `16`.

```lua
local Players = game:GetService("Players")

local player = Players.LocalPlayer
local character = player.Character or player.CharacterAdded:Wait()
local humanoid = character:WaitForChild("Humanoid")

local tool = Instance.new("Tool")
tool.Name = "Sprint"
tool.RequiresHandle = false
tool.Parent = player:WaitForChild("Backpack")

function toolActivated()
	humanoid.WalkSpeed = 30
	tool.ManualActivationOnly = true
	task.wait(5)
	tool.ManualActivationOnly = false
	humanoid.WalkSpeed = 16
end

tool.Activated:Connect(toolActivated)
tool.Unequipped:Connect(function()
	humanoid.WalkSpeed = 16
end)
```

### Property: Tool.RequiresHandle

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
    "Input"
  ]
}
```

This property determines whether a [Tool](/docs/reference/engine/classes/Tool.md) functions without a
handle.

A tool has a handle when it contains a child part named **Handle**. Tools
with handles typically require the player equipping them to hold an object
to use them, for instance weapons. Tools without handles typically don't
require the player equipping them to hold anything to use them, for
instance "fly" or "summon" tools.

When set to `true`, the tool will function only with a handle. When set to
`false`, the tool will function even without a handle.

### Property: Tool.ToolTip

```json
{
  "type": "string",
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
  "category": "Appearance",
  "capabilities": [
    "Input"
  ]
}
```

The ToolTip property controls the message that will be displayed when the
player's [Mouse](/docs/reference/engine/classes/Mouse.md) hovers over the [Tool](/docs/reference/engine/classes/Tool.md) in their
[Backpack](/docs/reference/engine/classes/Backpack.md).

Generally, the value of this property should describe the what the tool is
or its use. For instance, for a shovel tool, you may choose to set the
ToolTip to:

```lua
tool.ToolTip = "Shovel"
```

or

```lua
tool.ToolTip = "Use to dig"
```

or

```lua
tool.ToolTip = "Shovel - Use to dig"
```

### Property: Tool.GripForward *(hidden)*

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
  "category": "Transform",
  "capabilities": [
    "Input"
  ]
}
```

One of the properties that specifies a tool's orientation in a character's
hand. This represents the `R02`, `R12`, and `R22` values of the grip
[CFrame](/docs/reference/engine/datatypes/CFrame.md) rotation matrix.

Other tool properties that control how a character holds a tool include
[Tool.GripUp](/docs/reference/engine/classes/Tool.md), [Tool.GripRight](/docs/reference/engine/classes/Tool.md), and [Tool.GripPos](/docs/reference/engine/classes/Tool.md). All
of these properties are stored in a single [CFrame](/docs/reference/engine/datatypes/CFrame.md) in the
[Tool.Grip](/docs/reference/engine/classes/Tool.md) property.

**Grip Stick**

The code below insert's a [Tool](/docs/reference/engine/classes/Tool.md) named **Stick** into the local player's
[BackPack](/docs/reference/engine/classes/BackPack.md). When the player activates the tool, the code prints the
values of the tool's grip properties.

```lua
local Players = game:GetService("Players")

local player = Players.LocalPlayer

local tool = Instance.new("Tool")
tool.Name = "Stick"
tool.Parent = player.Backpack

local handle = Instance.new("Part")
handle.Name = "Handle"
handle.Parent = tool
handle.Size = Vector3.new(0.1, 3, 0.1)
handle.Color = Color3.fromRGB(108, 88, 75) -- Brown

tool.Activated:Connect(function()
	print(tool.Grip)
	print(tool.GripUp)
	print(tool.GripRight)
	print(tool.GripForward)
	print(tool.GripPos)
end)
```

### Property: Tool.GripPos *(hidden)*

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
  "category": "Transform",
  "capabilities": [
    "Input"
  ]
}
```

This property controls the positional offset of the tool's weld matrix. It
is one of several properties used to position how the player character
holds the tool.

Other properties that control how a character holds a tool include
[Tool.GripUp](/docs/reference/engine/classes/Tool.md), [Tool.GripRight](/docs/reference/engine/classes/Tool.md), and [Tool.GripForward](/docs/reference/engine/classes/Tool.md).
All of these properties are stored in a single [CFrame](/docs/reference/engine/datatypes/CFrame.md) in the
[Tool.Grip](/docs/reference/engine/classes/Tool.md) property.

**Grip Stick**

The code below insert's a [Tool](/docs/reference/engine/classes/Tool.md) named **Stick** into the local player's
[BackPack](/docs/reference/engine/classes/BackPack.md). When the player activates the tool, the code prints the
values of the tool's grip properties.

```lua
local Players = game:GetService("Players")

local player = Players.LocalPlayer

local tool = Instance.new("Tool")
tool.Name = "Stick"
tool.Parent = player.Backpack

local handle = Instance.new("Part")
handle.Name = "Handle"
handle.Parent = tool
handle.Size = Vector3.new(0.1, 3, 0.1)
handle.Color = Color3.fromRGB(108, 88, 75) -- Brown

tool.Activated:Connect(function()
	print(tool.Grip)
	print(tool.GripUp)
	print(tool.GripRight)
	print(tool.GripForward)
	print(tool.GripPos)
end)
```

### Property: Tool.GripRight *(hidden)*

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
  "category": "Transform",
  "capabilities": [
    "Input"
  ]
}
```

One of the properties that specifies a tool's orientation in a character's
hand. This represents the `R00`, `R10`, and `R20` values of the grip
[CFrame](/docs/reference/engine/datatypes/CFrame.md) rotation matrix.

Other tool properties that control how a character holds a tool include
[Tool.GripUp](/docs/reference/engine/classes/Tool.md), [Tool.GripForward](/docs/reference/engine/classes/Tool.md), and [Tool.GripPos](/docs/reference/engine/classes/Tool.md).
All of these properties are stored in a single [CFrame](/docs/reference/engine/datatypes/CFrame.md) in the
[Tool.Grip](/docs/reference/engine/classes/Tool.md) property.

**Grip Stick**

The code below insert's a [Tool](/docs/reference/engine/classes/Tool.md) named **Stick** into the local player's
[BackPack](/docs/reference/engine/classes/BackPack.md). When the player activates the tool, the code prints the
values of the tool's grip properties.

```lua
local Players = game:GetService("Players")

local player = Players.LocalPlayer

local tool = Instance.new("Tool")
tool.Name = "Stick"
tool.Parent = player.Backpack

local handle = Instance.new("Part")
handle.Name = "Handle"
handle.Parent = tool
handle.Size = Vector3.new(0.1, 3, 0.1)
handle.Color = Color3.fromRGB(108, 88, 75) -- Brown

tool.Activated:Connect(function()
	print(tool.Grip)
	print(tool.GripUp)
	print(tool.GripRight)
	print(tool.GripForward)
	print(tool.GripPos)
end)
```

### Property: Tool.GripUp *(hidden)*

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
  "category": "Transform",
  "capabilities": [
    "Input"
  ]
}
```

One of the properties that specifies a tool's orientation in a character's
hand. This represents the `R01`, `R11`, and `R21` values of the grip
[CFrame](/docs/reference/engine/datatypes/CFrame.md) rotation matrix.

Other tool properties that control how a character holds a tool include
[Tool.GripRight](/docs/reference/engine/classes/Tool.md), [Tool.GripForward](/docs/reference/engine/classes/Tool.md), and
[Tool.GripPos](/docs/reference/engine/classes/Tool.md). All of these properties are stored in a single
[CFrame](/docs/reference/engine/datatypes/CFrame.md) in the [Tool.Grip](/docs/reference/engine/classes/Tool.md) property.

**Grip Stick**

The code below insert's a [Tool](/docs/reference/engine/classes/Tool.md) named **Stick** into the local player's
[BackPack](/docs/reference/engine/classes/BackPack.md). When the player activates the tool, the code prints the
values of the tool's grip properties.

```lua
local Players = game:GetService("Players")

local player = Players.LocalPlayer

local tool = Instance.new("Tool")
tool.Name = "Stick"
tool.Parent = player.Backpack

local handle = Instance.new("Part")
handle.Name = "Handle"
handle.Parent = tool
handle.Size = Vector3.new(0.1, 3, 0.1)
handle.Color = Color3.fromRGB(108, 88, 75) -- Brown

tool.Activated:Connect(function()
	print(tool.Grip)
	print(tool.GripUp)
	print(tool.GripRight)
	print(tool.GripForward)
	print(tool.GripPos)
end)
```

## Methods

### Method: Tool:Activate

**Signature:** `Tool:Activate(): ()`

This function simulates activation of the [Tool](/docs/reference/engine/classes/Tool.md). The tool must be
equipped for this function to work.

*Security: None · Thread Safety: Unsafe · Capabilities: Input*

**Returns:** `()`

**Invisibility Tool**

The code below creates a [Tool](/docs/reference/engine/classes/Tool.md) in the local player's [Backpack](/docs/reference/engine/classes/Backpack.md)
that turns the player invisible when activated and visible when deactivated.

When equipped, the script simulates the tool being activated and turns the
player invisible for 3 seconds and then simulates the tool being deactivated.
Holding the left mouse button down turns the player invisible for up to 3
seconds, with a cooldown period of 1 second, or until the player releases
their left mouse button.

```lua
local Players = game:GetService("Players")

local player = Players.LocalPlayer
local character = player.Character

local tool = Instance.new("Tool")
tool.Name = "Invisibility Tool"
tool.RequiresHandle = false
tool.Parent = player.Backpack

local invisible = false

local function toolActivated()
	if invisible then
		return
	end
	invisible = true

	for _, bodypart in pairs(character:GetChildren()) do
		if bodypart:IsA("MeshPart") or bodypart:IsA("Part") then
			bodypart.Transparency = 1
		end
	end

	task.wait(3)
	tool:Deactivate()
	task.wait(1)
	invisible = false
end

local function toolDeactivated()
	if not invisible then
		return
	end
	for _, bodypart in pairs(character:GetChildren()) do
		if bodypart.Name ~= "HumanoidRootPart" then
			if bodypart:IsA("MeshPart") or bodypart:IsA("Part") then
				bodypart.Transparency = 0
			end
		end
	end
end

local function toolEquipped()
	tool:Activate()
end

tool.Equipped:Connect(toolEquipped)
tool.Activated:Connect(toolActivated)
tool.Deactivated:Connect(toolDeactivated)
tool.Unequipped:Connect(toolDeactivated)
```

### Method: Tool:Deactivate

**Signature:** `Tool:Deactivate(): ()`

This function simulates deactivation of the [Tool](/docs/reference/engine/classes/Tool.md). The tool must be
equipped for this function to work.

*Security: None · Thread Safety: Unsafe · Capabilities: Input*

**Returns:** `()`

**Invisibility Tool**

The code below creates a [Tool](/docs/reference/engine/classes/Tool.md) in the local player's [Backpack](/docs/reference/engine/classes/Backpack.md)
that turns the player invisible when activated and visible when deactivated.

When equipped, the script simulates the tool being activated and turns the
player invisible for 3 seconds and then simulates the tool being deactivated.
Holding the left mouse button down turns the player invisible for up to 3
seconds, with a cooldown period of 1 second, or until the player releases
their left mouse button.

```lua
local Players = game:GetService("Players")

local player = Players.LocalPlayer
local character = player.Character

local tool = Instance.new("Tool")
tool.Name = "Invisibility Tool"
tool.RequiresHandle = false
tool.Parent = player.Backpack

local invisible = false

local function toolActivated()
	if invisible then
		return
	end
	invisible = true

	for _, bodypart in pairs(character:GetChildren()) do
		if bodypart:IsA("MeshPart") or bodypart:IsA("Part") then
			bodypart.Transparency = 1
		end
	end

	task.wait(3)
	tool:Deactivate()
	task.wait(1)
	invisible = false
end

local function toolDeactivated()
	if not invisible then
		return
	end
	for _, bodypart in pairs(character:GetChildren()) do
		if bodypart.Name ~= "HumanoidRootPart" then
			if bodypart:IsA("MeshPart") or bodypart:IsA("Part") then
				bodypart.Transparency = 0
			end
		end
	end
end

local function toolEquipped()
	tool:Activate()
end

tool.Equipped:Connect(toolEquipped)
tool.Activated:Connect(toolActivated)
tool.Deactivated:Connect(toolDeactivated)
tool.Unequipped:Connect(toolDeactivated)
```

## Events

### Event: Tool.Activated

**Signature:** `Tool.Activated()`

This event fires when the player clicks while the [Tool](/docs/reference/engine/classes/Tool.md) is
equipped. It is **not** fired if the <kbd>Ctrl</kbd> key is pressed during
the click.

This event is typically used to perform an action when the player uses the
tool, for instance to launch a rocket from a rocket launcher weapon tool.

The below code, when placed in a [LocalScript](/docs/reference/engine/classes/LocalScript.md), creates a tool in
the local player's [Backpack](/docs/reference/engine/classes/Backpack.md) and prints "Tool activated" when the
player clicks while the created tool is equipped.

*Security: None · Capabilities: Input*

**Activated**

Demonstrates [Tool.Activated](/docs/reference/engine/classes/Tool.md).

```lua
local Players = game:GetService("Players")

local tool = Instance.new("Tool")
tool.RequiresHandle = false
tool.Parent = Players.LocalPlayer.Backpack

function onActivation()
	print("Tool activated")
end

tool.Activated:Connect(onActivation)
```

### Event: Tool.Deactivated

**Signature:** `Tool.Deactivated()`

This event fires when the player releases their click while the
[Tool](/docs/reference/engine/classes/Tool.md) is equipped and activated. It is typically used to perform an
action when the player stops using a tool.

The below code, when placed in a [LocalScript](/docs/reference/engine/classes/LocalScript.md), creates a tool in
the local player's [Backpack](/docs/reference/engine/classes/Backpack.md) and prints "Tool deactivated" when the
player releases their click while the tool is equipped and activated.

*Security: None · Capabilities: Input*

**Deactivated**

Demonstrates [Tool.Deactivated](/docs/reference/engine/classes/Tool.md).

```lua
local Players = game:GetService("Players")

local tool = Instance.new("Tool")
tool.RequiresHandle = false
tool.Parent = Players.LocalPlayer.Backpack

function toolDeactivated()
	print("Tool deactivated")
end

tool.Deactivated:Connect(toolDeactivated)
```

### Event: Tool.Equipped

**Signature:** `Tool.Equipped(mouse: Mouse)`

This event fires when a player equips the [Tool](/docs/reference/engine/classes/Tool.md) (takes it out of
their [Backpack](/docs/reference/engine/classes/Backpack.md)).

The opposite of this event, [Tool.Unequipped](/docs/reference/engine/classes/Tool.md), can be used to
determine when the player unequips the tool by putting it in their
backpack.

Note that this event does **not** fire when [Tool.RequiresHandle](/docs/reference/engine/classes/Tool.md) is
enabled and no handle is present.

*Security: None · Capabilities: Input*

**Parameters:**

| Name | Type | Description |
|------|------|-------------|
| `mouse` | `Mouse` | The player's mouse. |

**Print when a Player Equips a Tool**

The example shown below will print "A tool was equipped" each time the tool is
equipped by the player. Please note that the below example assumes that you've
already defined what "Tool" is.

```lua
local Tool = script.Parent

local function onEquipped(_mouse)
	print("The tool was equipped")
end

Tool.Equipped:Connect(onEquipped)
```

### Event: Tool.Unequipped

**Signature:** `Tool.Unequipped()`

This event fires when a player unequips the [Tool](/docs/reference/engine/classes/Tool.md) (puts it in their
[Backpack](/docs/reference/engine/classes/Backpack.md)).

The opposite of this event, [Tool.Equipped](/docs/reference/engine/classes/Tool.md), can be used to
determine when the player equips the tool by taking it out of their
backpack.

Note that this event does **not** fire when [Tool.RequiresHandle](/docs/reference/engine/classes/Tool.md) is
enabled and no handle is present.

*Security: None · Capabilities: Input*

## Inherited Members

### From [BackpackItem](/docs/reference/engine/classes/BackpackItem.md)

- **Property `TextureContent`** (`Content`): The texture icon that is displayed for a tool in the player's backpack.
- **Property `TextureId`** (`ContentId`): The texture icon that is displayed for a tool in the player's backpack.

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