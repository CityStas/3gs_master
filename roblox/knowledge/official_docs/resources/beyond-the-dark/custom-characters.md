---
title: "Custom characters"
url: /docs/en-us/resources/beyond-the-dark/custom-characters
last_updated: 2026-10-30T19:55:55Z
description: "Explains the design concepts and systems for characters in Beyond The Dark."
---

# Custom characters

You can import custom meshes to create everything from NPCs to an animated cloth of a sail boat. We used the custom setting of the [Importer](/docs/en-us/studio/importer.md) to bring in more exotic custom characters, like the mysterious black hole creatures and the friendly, if unaware, service droids.

The following sections go over how we used [rigging and skinning](/docs/en-us/art/modeling/rigging.md), [PBR (surface appearance)](/docs/en-us/art/modeling/surface-appearance.md), and VFX to build one of our more complicated characters that we named the "Creature." We wanted it to glow, emit some light, have trails of particle smoke, and a fluid motion that involved skinning a rig with enough joints to create the convincing waves of its tentacles.

![Creature Banner](../../assets/resources/beyond-the-dark/custom-characters/Creature_Banner.png) ## Rig

When we were rigging the Creature, we found it best to model the character in a neutral pose, because that pose is best suited to bending in multiple directions. If we modeled the Creature with its tentacles already curled, it would have led to stretching if we animated the tentacles to bend in the opposite direction. The following screenshots show the Creature in its natural state:

From a neutral pose, we added joints economically, focusing on the areas that needed the most movement. The fewer joints the better, because you'll have to manage them when skinning your character, and you'll have less to control when you animate them. In the previous screenshots, the Creature looks like it has a lot of joints in the center, but the main body only has one joint.

Most of the other joints are towards the tentacles and mandibles. With the tentacles, we wanted a lot of secondary motion, or motion that is layered, to create a convincing effect that they're all moving on their own. However, the center mass of tentacles were so close together that it felt wasteful to make joints for all of them, both on performance and effort to animate. So instead, we treated the center mass as a single large tentacle with smaller "tails" where the tips left the center mass.

![Creature Front, Maya](../../assets/resources/beyond-the-dark/custom-characters/Creature_Front.png)
> **Info:** It sometimes helps to make a "control rig" that saves you from having to animate every joint by hand. You can search for excellent tutorials of control rigs appropriate for your character and corresponding DCC application.

We found the following guidelines useful, so that the character mesh imports correctly into Studio:

- Individual joints and bones must have unique names.
- Meshes must not have the same name as joints and bones.
- Meshes should have no transforms prior to skinning/binding; in other words, transforms should be 0 and scales should be 1.
- Mesh normals should face outward (the model shouldn't look inside-out).
- Skeletons shouldn't have any scale factor; all joints should be [1, 1, 1].

## Skin

When we finished the Creature's skeleton, the next step was to skin the mesh. Skinning can be an arduous task, so to make matters easier, it's best to be familiar with the different initial skinning settings of your DCC application to find the one you like. Since this is an organic character, we skinned it with plenty of falloff on each joint and overlap between them. This way, the bending feels smooth and not sharp. The following screenshots show bad skinning and smooth skinning respectively:

_Bad Skinning_

_Smooth Skinning_

We found the following guidelines produced the best outcomes for skinning:

- Skinning influences (meaning they affect a part of the model when moved) should be a maximum of 4 influences per vertex.
- Joint and mesh names need to be unique, both within each other and between each other.
- Any joint you want to import into Studio must have some influence on the model's skinning, otherwise the engine doesn't import it. Whenever possible, skin your model in its original or "bind" pose.

## Import the mesh to Studio

Importing your custom characters into Studio is one of the more exciting parts of the process, because you get to see your creations in the game you're building!

To import the mesh into Studio:

1. Export the character from the DCC application and ensure the following:
  - All normals, scales, and names are correct.
  - The character has all joint and bone hierarchy and all meshes.
  - Meshes are all under 10,000 triangles for each part of the mesh.
  - Mesh total size isn't over 2000 units in any axis.
  - See [Mesh Requirements](/docs/en-us/avatar/character-bodies/specifications.md) for a complete list of model specifications.![Creature in DCC Tool](../../assets/resources/beyond-the-dark/custom-characters/Creature-In-Maya.png)
2. In the [Importer](/docs/en-us/studio/importer.md), import the custom `.fbx` or `.obj` file.![Creature Imported Into Studio](../../assets/resources/beyond-the-dark/custom-characters/Custom-Import-2.png)

## Make the creature glow

Once the Creature's model was stable and didn't require any more immediate import into Studio, we started putting together the SurfaceAppearance objects, lights, and visual effects. We did this to ensure that the quality of the model was good enough before proceeding to place and edit any one aspect of it.

![Glowing Creature Example](../../assets/resources/beyond-the-dark/custom-characters/Glowing-Creature.png)

We knew we wanted the Creature to be dark, and the focal points to be the eyes and its "grabby" tentacles. High points of contrast tend to attract attention, so having a few strong ones ensure the viewer knows what to focus on. Studio supports neon materials that self-illuminate, so early on we separated the eyes out so they could be their own material from the rest of the character. We did something similar for the tentacles, so they would glow on their tips only.

![Creature Eyes in Studio](../../assets/resources/beyond-the-dark/custom-characters/Creature-Eyes.jpeg)

Neon material doesn't emit actual light, so after some testing, we added separate parts to control placement and direction of light emission. This ensured the lighting was directed in a manner to enhance the glow of the eyes and also project its own source of light.

![Point Light in Studio](../../assets/resources/beyond-the-dark/custom-characters/Light-Emission.jpeg)

Notice that the `SpotLights` add visual flare to the Creature close to other surfaces or a player.

![Creature Light Example](../../assets/resources/beyond-the-dark/custom-characters/Spotlights.png)

In addition, we wanted the Creature's tentacles to emit some particles, so it would leave behind a smoke trail when it moved. Because the tentacles are very long, adding the `Class.ParticleEmitter` to the entire tentacle would make the particles emit from the entire tentacle instead of the tip. To combat this, we used a small part positioned near the end of the tentacle, so we could control the emission size, placement, and direction of the particles.

![Particle Example](../../assets/resources/beyond-the-dark/custom-characters/Particle-Emitter.jpeg) ## Make the VFX follow the character

The skinned character's mesh positions aren't updated when the Creature animates, so we needed a method to make sure the VFX, SFX, and lights all followed the Creature properly. To accomplish this, we created a VFX controller script and used CollectionService to inform the parts that contained the VFX where the creature's bones were and to follow them.

1. We placed the following `Class.LocalScript` in **StarterPlayer** → **StarterPlayerScripts**. This essentially runs the VFX update function.```lua
-- Add this snippet to an existing local script that makes PreSimulation
-- connections

local RunService = game:GetService("RunService")
local vfx = require(workspace.VfxUpdateModule)

RunService.PreSimulation:Connect(vfx.updateVfx)
``````lua
-- This module attached parts to animations so they are updated as the
-- animation plays. It is a workaround for the current limitations
-- with Joints and Bones and will not always be necessary.
--
-- Prereqs:
-- To be included, models need the "AnimatedVfxModel" tag, and a folder
-- of all parts that you want to sync with animation. Each part needs
-- an attribute called "AttachedBoneName" that refers to the name of the
-- bone you want to attach to. Parts should also already be in their
-- correct positions relative to the desired bone.
--
-- To Use:
-- A LocalScript should require this module, then connect
-- VfxUpdateModule.updateVfx to the RunService.PreSimulation event.

local VfxUpdateModule = {}
local CollectionService = game:GetService("CollectionService")

-- SETUP - this should run once on every client.
-- Collect all models with the tag
local vfxModels = CollectionService:GetTagged("AnimatedVfxModel")
local vfxTable = {} -- where we will store all the parts and offsets

-- Assign a table to each model that will hold all vfx parts and offset
for _, model in vfxModels do
 vfxTable[model] = {}
 local vfxParts = model:FindFirstChild("VFX"):GetChildren() -- Find theVFX folder

 -- Find the bone via attribute and calculate the offset for each part.
 for _,part in vfxParts do
   local name = part:GetAttribute("AttachedBoneName")
   local bone = model:FindFirstChild(name, true)
   if bone then
     local offset = (bone.TransformedWorldCFrame:inverse() * part.CFrame)
     vfxTable[model][part] = {bone, offset}
   else
     warn("Vfx part refers to bone that could not be found.")
   end
 end
end
print(vfxTable)

-- UPDATE - This should be linked to every client's RunService.PreSimulation
-- Go through all models, then update all parts on the model to match the bonecframe.
function VfxUpdateModule.updateVfx()
 for model, vfxParts in vfxTable do
   for part, bone in vfxParts do
     part.CFrame = bone[1].TransformedWorldCFrame * bone[2]
   end
 end
end

return VfxUpdateModule
```
2. We created a **VFXUpdateModule** `Class.ModuleScript` to tell any objects tagged appropriately with **AnimatedVfxModel** to update on a play event.
3. We tagged the necessary model groups with **AnimatedVfxModel** using the [Tags](/docs/en-us/studio/properties.md#instance-tags) section of its properties. Using tags allows the **VFXUpdateModule** to know which object to look for as the first VFX child and to apply the update.![VFX In Studio Example](../../assets/resources/beyond-the-dark/custom-characters/In-Studio-VFX.jpeg)
4. Finally, we added an **AttachedBoneName** custom attribute to the part we wanted to animate and added the precise name of the joint we wanted it to follow.

## Texture the creature

Next, we set up the PBR (Physically Based Rendered) texture maps. These powerful bitmaps give the creature the varied sheen and surface variations to make it look like it has a lot of small bumps and imperfections. This visual effect helps sell the appearance of the Creature when it's closer to the player.

![Creature Texturing Comparison](../../assets/resources/beyond-the-dark/custom-characters/Surface-Appearance.png)

Here's how we created the surface appearance texture maps:

1. The texture maps for this character were all on one "sheet" per map. This made the creature more efficient and meant we had to deal with fewer texture maps or `Class.SurfaceAppearance` objects.
2. For areas that needed to glow or be self-illuminated, such as the "grabby tentacles," we also used transparency on the `Class.SurfaceAppearance` to blend with those parts.![Illumination Example](../../assets/resources/beyond-the-dark/custom-characters/Surface-Appearance-Transparency.jpeg) We found it helpful to follow these guidelines when creating surface appearance texture maps:
  - Make sure your maps are no bigger than 1024×1024.
  - Your green channel may need to be flipped depending on the application you worked in.

## Animate the creature

Animating is very subjective and has a personal style. Options include motion capture, hand "key frame" animating in your DCC application, or using Studio's powerful **Animation Editor**.

As we mentioned earlier, we wanted to make sure we had enough joints for fluid motion as well as enough limbs, so the creature animation felt natural and "layered." Layering, also known as secondary motion, is something you see in everyday life — when you throw your arm out, every joint is reacting to the initial impulse from your upper arm, and every joint in your body doesn't move or rest at the same time.

We used this technique to animate the Creature to feel like the limbs were reacting to the movement driven by its body as shown here:

![Creature Animation Example](../../assets/resources/beyond-the-dark/custom-characters/Animation-Example.gif)

If using an external DCC application for animation, we found the following guidelines work best:

- Set frame rates to at least 30 FPS.
- Create your animations with the same character you're applying it to.
- Export your animation data as a separate `.fbx` file.

Because we animated the character outside of Studio, we needed to use the **Animation Editor** to import the animation `.fbx` file. The editor lets you select any avatar with joints or motors and drive them via points in the timeline.

To import an animation:

1. In the toolbar's **Avatar** tab, click **Clip Editor**.
2. Select the rigged character that you want to animate in Roblox. The character should be the same one you are rigging in your external DCC application.
3. Click the **⋯** button in the upper-left section of the editor window, select **Import From FBX Animation**, and locate your exported `.fbx` animation file.![Animation Import Example 2](../../assets/resources/beyond-the-dark/custom-characters/Animation-Import-2.png)
  > **Info:** If you animated at a different frame rate than 30 FPS, you may get a warning about alignment issues. This is because the key frames at different frame rates will not align to the frame count in Studio. You can generate keys at those points in time, or ignore it. Either way you'll be able to export, but aligning allows you better control over editing the frames in Studio.
4. When you're happy with your animation, you can export it to discover the animation ID, which you can then use in Roblox scripts to run them. For example, you can add a `Class.Script` to the model group of the imported character and use the following code to run the animation:![Animation Script Example](../../assets/resources/beyond-the-dark/custom-characters/Script-Example.jpeg)```lua
local animationId = "YOUR_ANIMATION_ID"
local char = script.Parent
local animController = char:FindFirstChildWhichIsA("Humanoid") or char:FindFirstChildOfClass("AnimationController")

local animation = Instance.new("Animation")
animation.AnimationId = "rbxassetid://" .. tostring(animationId)

local animTrack = animController:LoadAnimation(animation)
animTrack:Play(0, 1, 1)
```
  > **Warning:** Check the character after you've closed the **Animation Editor** to ensure that the **AnimSaves** folder was deleted, as its files are only useful during editing.

## Final results

After a few finishing tweaks to colors, light brightnesses, and some more particle effects to give it a stronger halo effect in front of windows, here's the final result in the space station!

![Final Creature Rendering](../../assets/resources/beyond-the-dark/custom-characters/Final-Result.png)
