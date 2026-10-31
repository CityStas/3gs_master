---
title: "Global wind"
url: /docs/en-us/environment/global-wind
last_updated: 2026-10-30T19:55:43Z
description: "The global wind vector sets the direction and strength that wind blows through a game, affecting terrain grass, dynamic clouds, and particles."
---

# Global wind

The `Class.Workspace.GlobalWind|GlobalWind` vector sets the direction and strength that wind blows through a game, affecting [terrain grass](/docs/en-us/parts/terrain.md#grass-animation) and [dynamic clouds](/docs/en-us/environment/clouds.md). You can set it as a [constant vector](#global-wind-vector), or adjust it through [scripting](#scripted-effects) to create cyclical gusts of wind. Additionally, you can influence [particles](#particle-influence) to follow the global wind vector.

## Global wind vector

Global wind is controlled through The `Class.Workspace.GlobalWind|GlobalWind` vector is a property of `Class.Workspace` and you can edit it directly in Studio, or set it through [scripting](#scripted-effects).

To set the global wind vector in Studio:

1. In the **Explorer** window, select the top-level `Class.Workspace` service.![Workspace object shown in Explorer window of Studio](../assets/studio/explorer/Workspace.png)
2. In the **Properties** window, locate the `Class.Workspace.GlobalWind|GlobalWind` property and set an **X**, **Y**, and **Z** value for its direction and strength.![GlobalWind property shown in Properties window of Studio](../assets/studio/properties/Workspace-GlobalWind.png)

> **Info:** Note that the speed of [animated grass](/docs/en-us/parts/terrain.md#grass-animation) — but not its vector direction — will be reduced if the player has toggled on the **Reduce Motion** [accessibility](/docs/en-us/production/publishing/accessibility.md#reduced-motion) setting from the Roblox or in-game **Settings** menu.
## Particle Influence

Particles emitted by a `Class.ParticleEmitter` will follow the global wind vector as long as the emitter's `Class.ParticleEmitter.WindAffectsDrag|WindAffectsDrag` property is enabled and its `Class.ParticleEmitter.Drag|Drag` property is greater than `0`, which is useful for [simulating rain](/docs/en-us/effects/particle-emitters.md#simulate-rain). `Class.Fire` and `Class.Smoke` instances follow the wind vector by default.

![Drag and WindAffectsDrag properties shown in Properties window of Studio](../assets/studio/properties/ParticleEmitter-WindAffectsDrag.png) ## Wind direction widget

To make it easier to tune global wind, you can use the **Wind Direction** widget, accessible from Studio's **View** menu. The widget lets you visualize how wind is blowing using a wind sock model, and you can dynamically set the wind's **Speed**, **Yaw**, and **Pitch** by clicking the desired aspect name and sliding the slider along the bottom, or you can adjust yaw or pitch by manipulating the green ring and blue arrow on the animated portion. You can also click and drag the widget to reposition it anywhere in the 3D viewport.

![Wind Direction widget showing in 3D viewport of Studio](../assets/lighting-and-effects/aero-fluid-dynamics/Wind-Direction-Widget.jpg) ## Scripted effects

Scripting of the `Class.Workspace.GlobalWind|GlobalWind` property opens up a whole range of possibilities. For example, you can use the following code sample to cause cyclical gusts of wind that ease in and out using the `Library.math.sin()` function.

```lua
local gustCycleDelay = 5  -- Max duration between gust cycles in seconds
local gustCycleDuration = 3.5  -- Duration of each gust cycle in seconds

-- During each gust cycle, a portion of "gust" will be added to "baseWind" in a ramped fashion
local baseWind = Vector3.new(5, 0, 2)  -- Base wind speed and direction
local gust = Vector3.new(25, 0, 10)  -- Gust speed and direction
local gustIntervals = 100  -- Number of iterations used to calculate each gust interval
local dg = gustCycleDuration / gustIntervals
local dgf = dg / gustCycleDuration

-- Set global wind to base wind initially
workspace.GlobalWind = baseWind

-- Wait delay amount before starting gusts
task.wait(gustCycleDelay)

while true do
	for i = 1, gustIntervals do
		local f = math.sin(math.pi * dgf * i)  -- Use sin() function to ramp gust
		workspace.GlobalWind = baseWind + f * gust  -- Set global wind to base wind + gust
		task.wait(dg)
	end
	workspace.GlobalWind = baseWind  -- Reset global wind to base wind at end of gust cycle
	task.wait(math.random() * gustCycleDelay)  -- Wait a random fraction of delay before next gust cycle
end
```
