---
title: "Use animations"
url: /docs/en-us/animation/using
last_updated: 2026-10-30T19:55:32Z
description: "Explains the process of playing animations through scripts, and replacing default animations."
---

# Use animations

Once you have [created an animation](/docs/en-us/animation/editor.md), you need to use scripts to include them in your game. You can either [play animations manually](#play-animations-from-scripts) from scripts or [replace default animations](#replace-default-animations) for player characters.

## Play animations from scripts

In some cases, you'll need to play an animation directly from inside a script, such as when a user presses a certain key or picks up a special item.

### Humanoids

To play an animation on a rig containing a `Class.Humanoid` object, such as typical playable characters, follow this basic pattern:

1. Ensure that the local player's `Class.Humanoid` contains an `Class.Animator` object.
2. Create a new `Class.Animation` instance with the proper `Class.Animation.AnimationId|AnimationId`.
3. Load the animation via `Class.Animator:LoadAnimation()` to create an `Class.AnimationTrack`.
4. Play the track with `Class.AnimationTrack:Play()`.

For example, the following `Class.LocalScript`, when placed in `Class.StarterPlayerScripts`, loads a "kick" animation onto the player's character and plays it. The script also utilizes the `Class.AnimationTrack:GetMarkerReachedSignal()|GetMarkerReachedSignal()` method to detect when a specific [animation event](/docs/en-us/animation/events.md) occurs.

```lua
local Players = game:GetService("Players")

local player = Players.LocalPlayer
local character = player.Character or player.CharacterAdded:Wait()

-- Ensure that the character's humanoid contains an "Animator" object
local humanoid = character:WaitForChild("Humanoid")
local animator = humanoid:WaitForChild("Animator")

-- Create a new "Animation" instance and assign an animation asset ID
local kickAnimation = Instance.new("Animation")
kickAnimation.AnimationId = "rbxassetid://2515090838"

-- Load the animation onto the animator
local kickAnimationTrack = animator:LoadAnimation(kickAnimation)

-- If a named event was defined for the animation, connect it to "GetMarkerReachedSignal()"
kickAnimationTrack:GetMarkerReachedSignal("KickEnd"):Connect(function(paramString)
	print(paramString)
end)

task.wait(4)

-- Play the animation track
kickAnimationTrack:Play()
```

### Non-humanoids

To play animations on rigs that do **not** contain a `Class.Humanoid`, you must create an `Class.AnimationController` with a child `Class.Animator`. For example, the following `Class.Script` (assumed to be a direct child of the rig) loads a "kick" animation and plays it.

```lua
local rig = script.Parent

-- Create a new "Animation" instance and assign an animation asset ID
local kickAnimation = Instance.new("Animation")
kickAnimation.AnimationId = "rbxassetid://2515090838"

-- Create a new "AnimationController" and "Animator"
local animationController = Instance.new("AnimationController")
animationController.Parent = rig

local animator = Instance.new("Animator")
animator.Parent = animationController

-- Load the animation onto the animator
local kickAnimationTrack = animator:LoadAnimation(kickAnimation)

-- If a named event was defined for the animation, connect it to "GetMarkerReachedSignal()"
kickAnimationTrack:GetMarkerReachedSignal("KickEnd"):Connect(function(paramString)
	print(paramString)
end)

task.wait(4)

-- Play the animation track
kickAnimationTrack:Play()
```

## Replace default animations

By default, Roblox player characters include common animations like running, climbing, swimming, and jumping. You can replace these [default animations](#default-character-animations) with animations from the [catalog](#catalog-animations) or with your own [custom](/docs/en-us/animation/editor.md) animations.

1. Obtain the **asset ID** of the new animation as follows:
  - For a custom animation built with the [Animation Editor](/docs/en-us/animation/editor.md), follow the [export](/docs/en-us/animation/editor.md#exporting-an-animation) instructions.
  - Copy an appropriate ID from the [catalog animation reference](#catalog-animations) below. For example, to replace the default run animation with the [Ninja Run](https://www.roblox.com/catalog/658830056/Ninja-Run) variant, use `656118852`.
2. In the [Explorer](/docs/en-us/studio/explorer.md) window, add a new `Class.Script` to **ServerScriptService**.
  1. Hover over **ServerScriptService** and click the ⊕ button.
  2. From the contextual menu, insert a **Script**.
3. In the new script, paste the following code:```lua
local Players = game:GetService("Players")

local function onCharacterAdded(character)
	-- Get animator on humanoid
	local humanoid = character:WaitForChild("Humanoid")
	local animator = humanoid:WaitForChild("Animator")

	-- Stop all animation tracks
	for _, playingTrack in animator:GetPlayingAnimationTracks() do
		playingTrack:Stop(0)
	end

	local animateScript = character:WaitForChild("Animate")
	--animateScript.run.RunAnim.AnimationId = "rbxassetid://"
	--animateScript.walk.WalkAnim.AnimationId = "rbxassetid://"
	--animateScript.jump.JumpAnim.AnimationId = "rbxassetid://"
	--animateScript.idle.Animation1.AnimationId = "rbxassetid://"
	--animateScript.idle.Animation2.AnimationId = "rbxassetid://"
	--animateScript.fall.FallAnim.AnimationId = "rbxassetid://"
	--animateScript.swim.Swim.AnimationId = "rbxassetid://"
	--animateScript.swimidle.SwimIdle.AnimationId = "rbxassetid://"
	--animateScript.climb.ClimbAnim.AnimationId = "rbxassetid://"
end

local function onPlayerAdded(player)
	player.CharacterAppearanceLoaded:Connect(onCharacterAdded)
end

Players.PlayerAdded:Connect(onPlayerAdded)
```
4. For each line that references a [default character animation](#default-character-animations), uncomment it and paste the replacement ID after `rbxassetid://`. For example, to change the default run animation to the [Ninja Run](https://www.roblox.com/catalog/658830056/Ninja-Run) variant:```lua
local Players = game:GetService("Players")

local function onCharacterAdded(character)
	-- Get animator on humanoid
	local humanoid = character:WaitForChild("Humanoid")
	local animator = humanoid:WaitForChild("Animator")

	-- Stop all animation tracks
	for _, playingTrack in animator:GetPlayingAnimationTracks() do
		playingTrack:Stop(0)
	end

	local animateScript = character:WaitForChild("Animate")
	animateScript.run.RunAnim.AnimationId = "rbxassetid://656118852"
	--animateScript.walk.WalkAnim.AnimationId = "rbxassetid://"
	--animateScript.jump.JumpAnim.AnimationId = "rbxassetid://"
	--animateScript.idle.Animation1.AnimationId = "rbxassetid://"
	--animateScript.idle.Animation2.AnimationId = "rbxassetid://"
	--animateScript.fall.FallAnim.AnimationId = "rbxassetid://"
	--animateScript.swim.Swim.AnimationId = "rbxassetid://"
	--animateScript.swimidle.SwimIdle.AnimationId = "rbxassetid://"
	--animateScript.climb.ClimbAnim.AnimationId = "rbxassetid://"
end

local function onPlayerAdded(player)
	player.CharacterAppearanceLoaded:Connect(onCharacterAdded)
end

Players.PlayerAdded:Connect(onPlayerAdded)
```

## Set animation weights

You can use multiple animations for the same action. For example, there are two `idle` variations in the code sample for [replacing default animations](#replace-default-animations).

When multiple animations exist for a character state, the **Animate** script randomly chooses which one to play, but you can influence the outcome by setting the animation's `Weight` value under the following formula:

- **animation weight / total weight of all state animations**

In the following example, `idle.Animation1` will play ⅓ of the time the character is idle, while `idle.Animation2` will play ⅔ of the time.

```lua
	animateScript.idle.Animation1.AnimationId = "rbxassetid://656117400"
	animateScript.idle.Animation2.AnimationId = "rbxassetid://656118341"
	animateScript.idle.Animation1.Weight.Value = 5
	animateScript.idle.Animation2.Weight.Value = 10
```

## Animation references

### Default character animations

The following table contains all of the default character animations that you can [replace](#replace-default-animations) with [catalog](#catalog-animations) animations or your own [custom](/docs/en-us/animation/editor.md) animations. Note that **Idle** has two variations which you can [weight](#set-animation-weights) to play more or less frequently.

| Character action | Animate script reference |
| --- | --- |
| **Run** | `animateScript.run.RunAnim.AnimationId` |
| **Walk** | `animateScript.walk.WalkAnim.AnimationId` |
| **Jump** | `animateScript.jump.JumpAnim.AnimationId` |
| **Idle** | `animateScript.idle.Animation1.AnimationId`<br> `animateScript.idle.Animation2.AnimationId` |
| **Fall** | `animateScript.fall.FallAnim.AnimationId` |
| **Swim** | `animateScript.swim.Swim.AnimationId` |
| **Swim (Idle)** | `animateScript.swimidle.SwimIdle.AnimationId` |
| **Climb** | `animateScript.climb.ClimbAnim.AnimationId` |

### Catalog animations

When using avatar animation bundles to [replace default animations](#replace-default-animations), use the following references for the respective asset IDs. For example, if you want to apply the [Ninja Jump](https://www.roblox.com/catalog/658832070/Ninja-Jump) animation, use `656117878`. Note that **Idle** has multiple variations.

| [**Astronaut**](https://www.roblox.com/bundles/34/Astronaut-Animation-Pack) | **Run**<br>891636393**Walk**<br>891636393**Jump**<br>891627522**Idle**<br>891621366, 891633237, 1047759695**Fall**<br>891617961**Swim**<br>891639666**Swim (Idle)**<br>891663592**Climb**<br>891609353 |
| --- | --- |
| [**Bubbly**](https://www.roblox.com/bundles/39/Bubbly-Animation-Package) | **Run**<br>910025107**Walk**<br>910034870**Jump**<br>910016857**Idle**<br>910004836, 910009958, 1018536639**Fall**<br>910001910**Swim**<br>910028158**Swim (Idle)**<br>910030921**Climb**<br>909997997 |
| [**Cartoony**](https://www.roblox.com/bundles/56/Cartoony-Animation-Package) | **Run**<br>742638842**Walk**<br>742640026**Jump**<br>742637942**Idle**<br>742637544, 742638445, 885477856**Fall**<br>742637151**Swim**<br>742639220**Swim (Idle)**<br>742639812**Climb**<br>742636889 |
| [**Elder**](https://www.roblox.com/bundles/48/Elder-Animation-Package) | **Run**<br>845386501**Walk**<br>845403856**Jump**<br>845398858**Idle**<br>845397899, 845400520, 901160519**Fall**<br>845396048**Swim**<br>845401742**Swim (Idle)**<br>845403127**Climb**<br>845392038 |
| [**Knight**](https://www.roblox.com/bundles/68/Knight-Animation-Package) | **Run**<br>657564596**Walk**<br>657552124**Jump**<br>658409194**Idle**<br>657595757, 657568135, 885499184**Fall**<br>657600338**Swim**<br>657560551**Swim (Idle)**<br>657557095**Climb**<br>658360781 |
| [**Levitation**](https://www.roblox.com/bundles/79/Levitation-Animation-Pack) | **Run**<br>616010382**Walk**<br>616013216**Jump**<br>616008936**Idle**<br>616006778, 616008087, 886862142**Fall**<br>616005863**Swim**<br>616011509**Swim (Idle)**<br>616012453**Climb**<br>616003713 |
| [**Mage**](https://www.roblox.com/bundles/63/Mage-Animation-Package) | **Run**<br>707861613**Walk**<br>707897309**Jump**<br>707853694**Idle**<br>707742142, 707855907, 885508740**Fall**<br>707829716**Swim**<br>707876443**Swim (Idle)**<br>707894699**Climb**<br>707826056 |
| [**Ninja**](https://www.roblox.com/bundles/75/Ninja-Animation-Package) | **Run**<br>656118852**Walk**<br>656121766**Jump**<br>656117878**Idle**<br>656117400, 656118341, 886742569**Fall**<br>656115606**Swim**<br>656119721**Swim (Idle)**<br>656121397**Climb**<br>656114359 |
| [**Pirate**](https://www.roblox.com/bundles/55/Pirate-Animation-Package) | **Run**<br>750783738**Walk**<br>750785693**Jump**<br>750782230**Idle**<br>750781874, 750782770, 885515365**Fall**<br>750780242**Swim**<br>750784579**Swim (Idle)**<br>750785176**Climb**<br>750779899 |
| [**Robot**](https://www.roblox.com/bundles/82/Robot-Animation-Pack) | **Run**<br>616091570**Walk**<br>616095330**Jump**<br>616090535**Idle**<br>616088211, 616089559, 885531463**Fall**<br>616087089**Swim**<br>616092998**Swim (Idle)**<br>616094091**Climb**<br>616086039 |
| [**Rthro**](https://www.roblox.com/bundles/356/Rthro-Animation-Package) | **Run**<br>2510198475**Walk**<br>2510202577**Jump**<br>2510197830**Idle**<br>2510197257, 2510196951, 3711062489**Fall**<br>2510195892**Swim**<br>2510199791**Swim (Idle)**<br>2510201162**Climb**<br>2510192778 |
| [**Stylish**](https://www.roblox.com/bundles/83/Stylish-Animation-Pack) | **Run**<br>616140816**Walk**<br>616146177**Jump**<br>616139451**Idle**<br>616136790, 616138447, 886888594**Fall**<br>616134815**Swim**<br>616143378**Swim (Idle)**<br>616144772**Climb**<br>616133594 |
| [**Superhero**](https://www.roblox.com/bundles/81/Superhero-Animation-Pack) | **Run**<br>616117076**Walk**<br>616122287**Jump**<br>616115533**Idle**<br>616111295, 616113536, 885535855**Fall**<br>616108001**Swim**<br>616119360**Swim (Idle)**<br>616120861**Climb**<br>616104706 |
| [**Toy**](https://www.roblox.com/bundles/43/Toy-Animation-Pack) | **Run**<br>782842708**Walk**<br>782843345**Jump**<br>782847020**Idle**<br>782841498, 782845736, 980952228**Fall**<br>782846423**Swim**<br>782844582**Swim (Idle)**<br>782845186**Climb**<br>782843869 |
| [**Vampire**](https://www.roblox.com/bundles/33/Vampire-Animation-Pack) | **Run**<br>1083462077**Walk**<br>1083473930**Jump**<br>1083455352**Idle**<br>1083445855, 1083450166, 1088037547**Fall**<br>1083443587**Swim**<br>1083464683**Swim (Idle)**<br>1083467779**Climb**<br>1083439238 |
| [**Werewolf**](https://www.roblox.com/bundles/32/Werewolf-Animation-Pack) | **Run**<br>1083216690**Walk**<br>1083178339**Jump**<br>1083218792**Idle**<br>1083195517, 1083214717, 1099492820**Fall**<br>1083189019**Swim**<br>1083222527**Swim (Idle)**<br>1083225406**Climb**<br>1083182000 |
| [**Zombie**](https://www.roblox.com/bundles/80/Zombie-Animation-Pack) | **Run**<br>616163682**Walk**<br>616168032**Jump**<br>616161997**Idle**<br>616158929, 616160636, 885545458**Fall**<br>616157476**Swim**<br>616165109**Swim (Idle)**<br>616166655**Climb**<br>616156119 |
