---
title: "Construct your world"
url: /docs/en-us/tutorials/curriculums/environmental-art/construct-your-world
last_updated: 2026-10-30T19:55:59Z
description: "Explains how to utilize your asset library, configure additional elements of the 3D space to bring your world to life."
---

# Construct your world

**Constructing your world**, also known as worldbuilding, is the process of decorating the environment with polished assets from your asset library, then adding and configuring additional elements of the 3D space to bring your world to life. This exciting step of the workflow is where you get to see all of your vision and hard work come together into a cohesive environment that is complete and ready for publication.

Using the [Environment Art - Constructing](https://www.roblox.com/games/14447826396/Environment-Art-Constructing) `.rbxl` file as a reference, this section of the environmental art curriculum shows you how to use and apply your high quality assets and custom materials to your greybox geometry in a way that differentiates each distinct area of the team-based first-person laser tag shooter game, including step-by-step instructions on:

- Applying your asset library to the building's architecture and outdoor space to provide users information about the overall world.
- Sculpting terrain with your custom tileable textures to create the overall island that the building rests on.
- Containing the playable areas to ensure users remain in combat without falling off the island.
- Configuring special effects and lighting sources to enrich the 3D space with movement, warmth, and realism.

After you complete this section, you will learn how to review and configure your content to ensure your game has optimal performance across devices.

> **Info:** The instructions in this section of the tutorial show you how to **exactly** recreate the sample final environment using the [Environment Art Asset Library](https://www.roblox.com/library/14447738661/Environment-Art-Asset-Library), which takes about 90 minutes or less from start to finish. If you don't want to use the provided coordinates, you can adjust the geometry however you need to meet the specifications of your own game, or use the sample itself for the rest of the tutorial.
## Apply your asset library

The first step in constructing your environment is to apply your asset library to the 3D space, and this process often falls into one of the following categories of work:

- Applying your asset library directly onto the greybox geometry to exactly match the original design.
- Converting the greybox geometry into something else entirely that still respects the intention behind the original design.
- Converting the greybox geometry into something else while also applying your asset library to the new object to maintain cohesion throughout the environment.

The process between greyboxing and constructing your environment with your asset library hardly ever looks like a straight line from your original design to the final art. Iteration between each step and across steps is normal and almost always necessary in the development process as you find new ways to improve the user's experience in your world. For example, the guidance in the **Floors** section converts the original floor greybox geometry into new divisions in order to better orient users to where they are in the building.

As you follow these instructions that exactly recreate the final environment within the sample [Environment Art - Constructing](https://www.roblox.com/games/14447826396/Environment-Art-Constructing) `.rbxl` file, observe how each step works together to add character to the environment, and provide users information about the overall world. **You can adjust any part of the process to meet the specifications of your own game**, as your environment may have different needs according to the world that you're creating.

### Floors

The original greybox design for floors was to divide the building into two halves, one for each team. This was useful to help visualize each half as its own space for its respective team, and to delineate the center of the map. However, as you begin to construct your environment, you may find that walls can fulfill this purpose more effectively, and that floors are more useful to help orient users to where they are in relation to the exterior of the building.

For example, the final sample laser tag environment uses new floor pieces with unique materials to inform users whether they're navigating somewhere inside the building, or approaching its outdoor space. When a user is inside of the building, they walk on surfaces with the **GlossyTiles** `Class.MaterialVariant`, and when they're walking in the middle courtyard or under the overhang pieces you will make later in this tutorial, they walk on surfaces with the **Concrete_Tiles_A** `Class.MaterialVariant`. You can find both of these materials in the sample [Environment Art Asset Library](https://www.roblox.com/library/14447738661/Environment-Art-Asset-Library).

While this technique replaces and converts the original greybox geometry, it still respects the intention behind the original design to create peaks and valleys that control sight lines and engagement distances throughout the game outside of horizontal movement. This means that users retain all physical and emotional senses of ascension and descension while also having the benefit of knowing where they are in the 3D space.

#### Create your own

To apply your own asset library to the floors:

1. Using **block** parts, create symmetrical surfaces for your indoor floors.
2. Using **wedge** parts, create a **rise in elevation** between the main and mezzanine floors on the inside of your building.
3. Select these indoor parts, then in the **Properties** window, set **Color**, **Material**, and/or **MaterialVariant** to values that apply a distinct visual treatment from other surfaces in your environment. This allows players to always know they are within the building.
4. Using **block** parts, create symmetrical surfaces for your **outdoor floors**.
5. Using **wedge** parts, create a **rise in elevation** between the main and mezzanine floors on the outside of your building.
6. Using **block** or **wedge** parts, create a drop in elevation between the main and outdoor floors on the outside of your building.
7. Select these outdoor parts, then in the **Properties** window, set **Color**, **Material**, and/or **MaterialVariant** to values that apply a distinct visual treatment from other surfaces in your environment. This allows players to always know they are outside of the building.
8. Anchor all of these floor parts.

#### Recreate the sample

To exactly recreate the floors within the sample [Environment Art - Constructing](https://www.roblox.com/games/14447826396/Environment-Art-Constructing) place file:

1. Add and configure the following **block** parts for the indoor floors: | Part | Size | CFrame.Position |
| --- | --- | --- | | Left-side top area | `57.5, 6, 142` | `-123.75, 2, 281` | | Left-side bottom area | `64, 6, 164.5` | `-63, 2, 269.75` | | Middle top area | `53, 6, 60` | `-119.5, 7, 160` | | Right-side top area | `57.5, 6, 142` | `-123.75, 2, 48.5` | | Right-side bottom area | `64, 5, 162.5` | `-63, 2.5, 51.25` |
2. Select these parts, then in the **Properties** window,
  1. Set **Color** to `248, 248, 248`.
  2. Set **Material** to **Concrete**.
  3. Set **MaterialVariant** to **GlossyTiles**.
3. Add and configure the following **block** parts for the outdoor floors: | Part | Size | CFrame.Position |
| --- | --- | --- | | Middle top area | `13, 6, 64` | `-86.5, 7, 158` | | Middle middle area | `29, 1, 55` | `-45.5, 4.5, 160` | | Middle bottom area | `18, 11, 100` | `-14, -0.5, 160` |
4. Select these parts, then in the **Properties** window,
  1. Set **Color** to `233, 218, 218`.
  2. Set **Material** to **Concrete**.
  3. Set **MaterialVariant** to **Concrete_Tiles_A**.
5. Add and configure the following **FloorRamp** modular assets for the elevation between floors: | Size | CFrame.Position | CFrame.Orientation | MaterialVariant |
| --- | --- | --- | --- | | `14, 6, 20` | `-102.5, 7, 200` | `0, 0, 0` | `GlossyTiles` | | `14, 6, 20` | `-102.5, 7, 120` | `0, 180, 0` | `GlossyTiles` | | `50, 6, 20` | `-70, 7, 160` | `0, 90, 0` | `Concrete_Tiles_A` |
6. Add and configure the following **block** parts for the stairs leading down into the outdoor space: | Part | Size | CFrame.Position |
| --- | --- | --- | | Top step | `8, 1, 260` | `-27, 4.5, 160` | | Left-side step one | `3, 1, 74` | `-14.5, 0.5, 250.75` | | Left-side step two | `3, 1, 74` | `-17, 1.5, 250.75` | | Left-side step three | `3, 1, 74` | `-19.5, 2.5, 250.75` | | Left-side step four | `3, 1, 74` | `-22, 3.5, 250.75` | | Right-side step one | `3, 1, 74` | `-14.5, 0.5, 72` | | Right-side step two | `3, 1, 74` | `-17, 1.5, 72` | | Right-side step three | `3, 1, 74` | `-19.5, 2.5, 72` | | Right-side step four | `3, 1, 74` | `-22, 3.5, 72` |
7. Select these parts, then in the **Properties** window,
  1. Set **Color** to `233, 218, 218`.
  2. Set **Material** to **Concrete**.
  3. Set **MaterialVariant** to **Concrete_Tiles_A**.
8. Anchor all of these parts and modular assets.

### Spawn zones

The original greybox design for spawn zones was to create an area at opposite ends of their map for users to join their respective team when the match starts. The placement of these spawn zones allows users to have a safe location at the start of the match that's far away from enemy fire.

The final sample laser tag environment keeps the intent of this design while also adding a color theme: **mint** for the team that assembles on the left side of the map, and **carnation pink** for the team that assembles on the right side of the map. You will continue to use this same color scheme throughout this section of the tutorial to differentiate areas of the map near each team's respective spawn zone.

#### Create your own

To apply your own asset library to the spawn zones:

1. Add and configure any applicable **wall**, **corner**, and **door frame** modular assets to the inside of your **left spawn zone**.
2. Select your wall components, then in the **Properties** window, set **Color** to a **unique** hue. You will continue to use this color throughout the rest of the map to orient players to their location relative to this team's color theme.
3. Repeat this process for your **right spawn zone**.
4. Anchor all of these spawn zone assets.

#### Recreate the sample

To exactly recreate the spawn zones within the sample [Environment Art - Constructing](https://www.roblox.com/games/14447826396/Environment-Art-Constructing) place file:

1. Add and configure the following **modular** assets for the left spawn zone: | Asset Name | CFrame.Position | CFrame.Orientation |
| --- | --- | --- | | WallCornerInner | `-110, 5, 335` | `0, 180, 0` | | WallLarge | `-110, 5, 320` | `0, 0, 0` | | WallLarge | `-110, 5, 305` | `0, 0, 0` | | WallCornerInner | `-105, 5, 300` | `0, 0, 0` | | DoorFrame | `-85, 5, 300` | `0, -90, 0` | | WallLarge | `-70, 5, 300` | `0, -90, 0` | | DoorFrame | `-50, 5, 300` | `0, -90, 0` | | WallCornerInner | `-45, 5, 305` | `0, -90, 0` | | WallLarge | `-45, 5, 320` | `0, 180, 0` | | WallLarge | `-45, 5, 335` | `0, 180, 0` | | WallCornerInner | `-50, 5, 340` | `0, 180, 0` | | WallLarge | `-65, 5, 340` | `0, 90, 0` | | WallLarge | `-80, 5, 340` | `0, 90, 0` | | WallLarge | `-95, 5, 340` | `0, 90, 0` | | WallMid | `-105, 5, 340` | `0, 90, 0` |
2. Select the wall component of these assets, then in the **Properties** window, set **Color** to `88, 218, 171`.
3. Add and configure the following **modular** assets for the right spawn zone: | Asset Name | CFrame.Position | CFrame.Orientation |
| --- | --- | --- | | WallCornerInner | `-110, 5, 15` | `0, 90, 0` | | WallLarge | `-110, 5, -0` | `0, 0, 0` | | WallLarge | `-110, 5, -15` | `0, 0, 0` | | WallCornerInner | `-105, 5, -20` | `0, 0, 0` | | WallLarge | `-90, 5, -20` | `0, -90, 0` | | WallLarge | `-75, 5, -20` | `0, -90, 0` | | WallLarge | `-60, 5, -20` | `0, -90, 0` | | WallMid | `-50, 5, -20` | `0, -90, 0` | | WallCornerInner | `-45, 5, -15` | `0, -90, 0` | | WallLarge | `-45, 5, -0` | `0, 180, 0` | | WallLarge | `-45, 5, 15` | `0, 180, 0` | | WallCornerInner | `-50, 5, 20` | `0, 180, 0` | | DoorFrame | `-70, 5, 20` | `0, 90, 0` | | WallLarge | `-85, 5, 20` | `0, 90, 0` | | WallLarge | `-105, 5, 20` | `0, 90, 0` |
4. Select the wall component of these assets, then in the **Properties** window, set **Color** to `255, 170, 255`.
5. Anchor all of these modular assets.

### Combat pockets

The original greybox design for the combat pockets was to create intentional spaces for combat where the map's primary lanes intersect with the cross lanes. In addition, the original greybox design required that each combat pocket needed to only include three entrance or exit points at most to refrain from giving users choice overload as they're navigating the space.

The final sample laser tag environment applies the sample [Environment Art Asset Library](https://www.roblox.com/library/14447738661/Environment-Art-Asset-Library) directly onto the greybox geometry to exactly match the original design while also using the color theme introduced in the previous section to differentiate areas of the map near each team's respective spawn zone. Using these colors and the floor material, users can quickly orient themselves to where they are no matter where they are around the building, respecting the original intention behind the greybox design for the building's floors.

In addition, the technique in this section also applies props from the sample asset library to left and right combat pockets in order to add character to the environment and provide believability that it has life on its own even if users weren't present. This process, also called **set dressing**, provides users both direct and indirect information about the world they're visiting. For example, the signage and foliage props in this section reinforce the sample art style from [Develop Polishing Assets](/docs/en-us/tutorials/curriculums/environmental-art/develop-polished-assets.md), and inform users that they're in a high-tech environment that still prioritizes organic life.

#### Create your own

To apply your own asset library to the combat pockets:

1. Add and configure any applicable props or **wall**, **corner**, **door frame**, and **door** modular assets to the inside and outside of your **left combat pocket**.
2. Select your wall components on the outside of your left combat pocket, then in the **Properties** window, set **Color** to the **same** hue as the left spawn zone's color theme. This allows players to orient themselves relative to this team's color theme as they are navigating primary and cross lanes.
3. Select your wall components on the inside of your left combat pocket, then in the **Properties** window, set **Color** to a **unique** hue. This allows players to orient themselves when they are within the combat pocket and looking through exit points.
4. Repeat this process for your **middle combat pocket** and **right combat pocket**.
5. Anchor all of these combat pocket assets.

#### Recreate the sample

To exactly recreate the combat pockets within the sample [Environment Art - Constructing](https://www.roblox.com/games/14447826396/Environment-Art-Constructing) place file:

To apply your asset library to the combat pockets:

1. Add and configure the following **modular** assets for the left combat pocket's exterior: | Asset Name | CFrame.Position | CFrame.Orientation |
| --- | --- | --- | | WallCornerOuter | `-105, 5, 280` | `0, -90, 0` | | WallLarge | `-105, 5, 280` | `0, 180, 0` | | WallCornerOuter | `-105, 5, 265` | `0, 180, 0` | | WallSmall | `-105, 5, 265` | `0, 90, 0` | | WallCornerInner | `-100, 5, 265` | `0, 180, 0` | | Door | `-95, 5, 260` | `0, 180, 0` | | DoorFrame | `-95, 5, 260` | `0, -180, 0` | | WallLarge | `-95, 5, 240` | `0, 180, 0` | | WallCornerOuter | `-95, 5, 225` | `0, 180, 0` | | WallLarge | `-95, 5, 225` | `0, 90, 0` | | DoorFrame | `-80, 5, 225` | `0, 90, 0` | | WallLarge | `-60, 5, 225` | `0, 90, 0` | | WallCornerOuter | `-45, 5, 225` | `0, 90, 0` | | WallSmall | `-45, 5, 225` | `0, 0, 0` | | WallLarge | `-45, 5, 230` | `0, 0, 0` | | WallLarge | `-45, 5, 245` | `0, 0, 0` | | WallLarge | `-45, 5, 260` | `0, 0, 0` | | WallCornerOuter | `-45, 5, 275` | `0, 0, 0` | | WallMid | `-45, 5, 275` | `0, -90, 0` | | WallSmall | `-55, 5, 275` | `0, -90, 0` | | DoorFrame | `-60, 5, 275` | `0, -90, 0` | | WallMid | `-80, 5, 275` | `0, -90, 0` | | WallCornerInner | `-90, 5, 275` | `0, 0, 0` | | WallCornerOuter | `-95, 5, 280` | `0, 0, 0` | | WallMid | `-95, 5, 280` | `0, -90, 0` |
2. Select the wall component of these assets, then in the **Properties** window, set **Color** to `88, 218, 171`.
3. Add and configure the following **prop** assets for the left combat pocket's exterior: | Asset Name | CFrame.Position | CFrame.Orientation |
| --- | --- | --- | | Extinguisher | `-44, 10, 254.5` | `0, 0, 0` | | WallHanging | `-44, 12.5, 248.5` | `0, 0, 0` | | WallConsoleA | `-44, 5.5, 233` | `0, 0, 0` | | Extinguisher | `-96, 10, 242` | `0, 0, 0` |
4. Add and configure the following **modular** assets for the left combat pocket's interior: | Asset Name | CFrame.Position | CFrame.Orientation |
| --- | --- | --- | | WallCornerInner | `-90, 5, 265` | `0, 90, 0` | | WallSmall | `-90, 5, 260` | `0, 0, 0` | | DoorFrame | `-90, 5, 240` | `0, 0, 0` | | WallCornerInner | `-85, 5, 235` | `0, 0, 0` | | WallSmall | `-80, 5, 235` | `0, -90, 0` | | DoorFrame | `-60, 5, 235` | `0, -90, 0` | | WallCornerInner | `-55, 5, 240` | `0, -90, 0` | | WallLarge | `-55, 5, 255` | `0, 180, 0` | | WallMid | `-55, 5, 265` | `0, 180, 0` | | WallCornerInner | `-60, 5, 270` | `0, 180, 0` | | DoorFrame | `-80, 5, 270` | `0, 90, 0` | | WallSmall | `-85, 5, 270` | `0, 90, 0` |
5. Select the wall component of these assets, then in the **Properties** window,
  1. Set **Color** to `211, 190, 150`.
  2. Set **MaterialVariant** to **MetalPanels**.
6. Add a **PlanterSmall** prop asset for a piece of cover at a **CFrame.Position** of `-67.5, 5, 252.5` and a **CFrame.Orientation** of `0, 90, 0`. You can add foliage assets from the asset library to the top of the planter to add more organic life to the building.
7. Add and configure the following **modular** assets for the middle combat pocket's exterior: | Asset Name | CFrame.Position | CFrame.Orientation |
| --- | --- | --- | | WallSmall | `-40, 5, 195` | `0, 0, 0` | | WallCornerOuter | `-40, 5, 200` | `0, 0, 0` | | DoorFrame | `-40, 5, 200` | `0, -90, 0` | | WallLarge | `-60, 5, 200` | `0, -90, 0` | | WallCornerInner | `-75, 5, 200` | `0, 0, 0` | | WallSmall | `-80, 5, 205` | `0, 0, 0` | | WallCornerOuter | `-80, 5, 210` | `0, 0, 0` | | WallLarge | `-80, 5, 210` | `0, -90, 0` | | WallCornerOuter | `-95, 5, 210` | `0, -90, 0` | | WallRiseA | `-95, 5, 210` | `0, 180, 0` | | WallMid | `-95, 10, 190` | `0, 180, 0` | | WallCornerInner | `-95, 10, 180` | `0, -90, 0` | | WallLarge | `-100, 10, 175` | `0, -90, 0` | | WallCornerOuter | `-115, 10, 175` | `0, -90, 0` | | WallSmall | `-115, 10, 175` | `0, 180, 0` | | DoorFrame | `-115, 10, 170` | `0, 180, 0` | | WallSmall | `-115, 10, 150` | `0, 180, 0` | | WallCornerOuter | `-115, 10, 145` | `0, 180, 0` | | WallLarge | `-115, 10, 145` | `0, 90, 0` | | WallCornerInner | `-100, 10, 145` | `0, 180, 0` | | WallMid | `-95, 10, 140` | `0, 180, 0` | | WallRiseB | `-95, 5, 110` | `0, -180, 0` | | WallCornerOuter | `-95, 5, 110` | `0, 180, 0` | | WallLarge | `-95, 5, 110` | `0, 90, 0` | | WallCornerOuter | `-80, 5, 110` | `0, 90, 0` | | WallSmall | `-80, 5, 110` | `0, 0, 0` | | WallCornerInner | `-80, 5, 115` | `0, 90, 0` | | WallLarge | `-75, 5, 120` | `0, 90, 0` | | DoorFrame | `-60, 5, 120` | `0, 90, 0` | | WallCornerOuter | `-40, 5, 120` | `0, 90, 0` | | WallSmall | `-40, 5, 120` | `0, 0, 0` |
8. Select the wall component of these assets, then in the **Properties** window,
  1. Set **Color** to `181, 173, 156`.
  2. Set **MaterialVariant** to **Concrete_Ribbed_A**.
9. Add and configure the following **modular** assets for the middle combat pocket's interior: | Asset Name | CFrame.Position | CFrame.Orientation |
| --- | --- | --- | | DoorFrame | `-60, 5, 185` | `0, 90, 0` | | WallRiseB | `-60, 5, 185` | `0, 90, 0` | | WallSmall | `-85, 10, 185` | `0, 90, 0` | | WallCornerInner | `-90, 10, 180` | `0, 90, 0` | | WallMid | `-90, 10, 170` | `0, 0, 0` | | DoorFrame | `-90, 10, 150` | `0, 0, 0` | | WallMid | `-90, 10, 140` | `0, 0, 0` | | WallCornerInner | `-85, 10, 135` | `0, 0, 0` | | WallSmall | `-80, 10, 135` | `0, -90, 0` | | WallRiseA | `-60, 5, 135` | `0, -90, 0` | | DoorFrame | `-40, 5, 135` | `0, -90, 0` | | ExtTrimAShort | `-65, 5, 151` | `0, 90, 0` | | ExtTrimAShort | `-75, 5, 169` | `0, -90, 0` | | ExtTrimAMid | `-65, 5, 169` | `0, 0, 0` | | ExtTrimAMid | `-65, 10, 167` | `0, 0, 0` | | ExtTrimACorner | `-65, 5, 169` | `0, 0, 0` | | ExtTrimACorner | `-65, 5, 151` | `0, 90, 0` | | DoorFramePlug | `-40, 5, 200` | `0, -90, 0` | | DoorFramePlug | `-60, 5, 185` | `0, 90, 0` | | DoorFramePlug | `-100, 10, 170` | `0, 180, 0` | | DoorFramePlug | `-105, 10, 170` | `0, 180, 0` | | DoorFramePlug | `-110, 10, 170` | `0, 180, 0` | | DoorFramePlug | `-105, 10, 150` | `0, 0, 0` | | DoorFramePlug | `-60, 5, 120` | `0, 90, 0` | | DoorFramePlug | `-40, 5, 135` | `0, -90, 0` |
10. Select the wall component of these assets, then in the **Properties** window,
  1. Set **Color** to `181, 173, 156`.
  2. Set **MaterialVariant** to **Concrete_Ribbed_A**.
11. Add and configure the following **modular** assets for the right combat pocket's exterior: | Asset Name | CFrame.Position | CFrame.Orientation |
| --- | --- | --- | | WallCornerOuter | `-95, 5, 95` | `0, -90, 0` | | WallLarge | `-95, 5, 95` | `0, 180, 0` | | DoorFrame | `-95, 5, 80` | `0, 180, 0` | | WallCornerInner | `-95, 5, 60` | `0, -90, 0` | | WallSmall | `-100, 5, 55` | `0, -90, 0` | | WallCornerOuter | `-105, 5, 55` | `0, -90, 0` | | WallLarge | `-105, 5, 55` | `0, 180, 0` | | WallCornerOuter | `-105, 5, 40` | `0, 180, 0` | | WallMid | `-105, 5, 40` | `0, 90, 0` | | WallCornerOuter | `-95, 5, 40` | `0, 90, 0` | | WallCornerInner | `-95, 5, 40` | `0, 90, 0` | | WallMid | `-90, 5, 45` | `0, 90, 0` | | DoorFrame | `-80, 5, 45` | `0, 90, 0` | | WallLarge | `-60, 5, 45` | `0, 90, 0` | | WallCornerOuter | `-45, 5, 45` | `0, 90, 0` | | WallSmall | `-45, 5, 45` | `0, 0, 0` | | WallLarge | `-45, 5, 50` | `0, 0, 0` | | WallLarge | `-45, 5, 65` | `0, 0, 0` | | WallLarge | `-45, 5, 80` | `0, 0, 0` | | WallCornerOuter | `-45, 5, 95` | `0, 0, 0` | | WallMid | `-45, 5, 95` | `0, -90, 0` | | WallSmall | `-55, 5, 95` | `0, -90, 0` | | DoorFrame | `-60, 5, 95` | `0, -90, 0` | | WallLarge | `-80, 5, 95` | `0, -90, 0` |
12. Select the wall component of these assets, then in the **Properties** window, set **Color** to `255, 170, 255`.
13. Add and configure the following **prop** assets for the right combat pocket's exterior: | Asset Name | CFrame.Position | CFrame.Orientation |
| --- | --- | --- | | Extinguisher | `-44, 10, 75.5` | `0, 0, 0` | | WallHanging | `-44, 5.5, 88` | `0, 0, 0` | | WallConsoleA | `-44, 12.5, 70.5` | `0, 0, 0` | | Extinguisher | `-96, 10, 62` | `0, 180, 0` |
14. Add and configure the following **modular** assets for the right combat pocket's interior: | Asset Name | CFrame.Position | CFrame.Orientation |
| --- | --- | --- | | WallCornerInner | `-90, 5, 80` | `0, 90, 0` | | DoorFrame | `-90, 5, 60` | `0, 0, 0` | | WallSmall | `-90, 5, 55` | `0, 0, 0` | | WallCornerInner | `-85, 5, 50` | `0, 0, 0` | | WallSmall | `-80, 5, 50` | `0, -90, 0` | | DoorFrame | `-60, 5, 50` | `0, -90, 0` | | WallCornerInner | `-55, 5, 55` | `0, -90, 0` | | WallLarge | `-55, 5, 70` | `0, 180, 0` | | WallMid | `-55, 5, 80` | `0, 180, 0` | | WallCornerInner | `-60, 5, 85` | `0, 180, 0` | | DoorFrame | `-80, 5, 85` | `0, 90, 0` | | WallSmall | `-85, 5, 85` | `0, 90, 0` |
15. Select the wall component of these assets, then in the **Properties** window,
  1. Set **Color** to `255, 170, 255`.
  2. Set **MaterialVariant** to **MetalPanels**.
16. Add a **PlanterSmall** prop asset for a piece of cover at a **CFrame.Position** of `-67.5, 5, 67.5` and a **CFrame.Orientation** of `0, 90, 0`. You can add foliage assets from the asset library to the top of the planter to add more organic life to the building.
17. Anchor all of these prop and modular assets.

### Perimeter hallways

By applying your asset library to the exterior of the combat pockets in the previous section, most cross lanes now include polished assets aside from the hallways that make up the perimeter of the building. In addition to using the same color scheme from previous sections, the final sample laser tag environment also uses wall assets with their default orange color to inform users where they are in relation to the back of the building.

For example, using the point-of-view in the following image, users immediately have the following information to orient themselves to where they are within the building:

- The **ribbed concrete** informs users that if they move left, then they will enter the middle combat pocket.
- The **yellow wall** informs users that if they move forward, then they will reach the back of the building and the interior primary lane.
- The **pink wall** informs users that if they move right, then they will enter the right combat pocket, and that they are nearest the right side of the map.

Aside from this technique that applies the sample [Environment Art Asset Library](https://www.roblox.com/library/14447738661/Environment-Art-Asset-Library) directly onto the greybox geometry for the walls to exactly match the original design, it also adds geometry in the form of crate prop assets in order to provide users cover from enemy fire as they navigate the interior primary lane. This design iteration still respects the intention to break up sight lights and engagement distances with protruding hallway spaces and elevation changes.

#### Create your own

To apply your own asset library to the perimeter hallways:

1. Add and configure any applicable prop or **wall**, **corner**, and **door frame** modular assets to the perimeter hallways on the **left-side** of the building.
2. Select your wall components, then in the **Properties** window, set **Color** to the **same** hue as the left spawn zone's color theme.
3. Add and configure any applicable prop or **wall**, **corner**, and **door frame** modular assets to the perimeter hallways at the **back** of the building.
4. Select your wall components, then in the **Properties** window, set **Color** to a **unique** hue. This allows players to orient themselves relative to where they are in relation to the interior primary lane. The sample game keeps these assets their default color.
5. Add and configure any applicable prop or **wall**, **corner**, and **door frame** modular assets to the perimeter hallways on the right-side of the building.
6. Select your wall components, then in the **Properties** window, set **Color** to the same hue as the right spawn zone's color theme.
7. Anchor all of these perimeter hallway assets.

#### Recreate the sample

To exactly recreate the perimeter hallways within the sample [Environment Art - Constructing](https://www.roblox.com/games/14447826396/Environment-Art-Constructing) place file:

1. Add and configure the following **modular** assets for the perimeter hallways on the left-side of the building: | Asset Name | CFrame.Position | CFrame.Orientation |
| --- | --- | --- | | WallLarge | `-50, 5, 295` | `0, 90, 0` | | DoorFrame | `-70, 5, 295` | `0, 90, 0` | | WallLarge | `-85, 5, 295` | `0, 90, 0` | | DoorFrame | `-105, 5, 295` | `0, 90, 0` | | WallLarge | `-120, 5, 295` | `0, 90, 0` |
2. Select the wall component of these assets, then in the **Properties** window, set **Color** to `255, 170, 255`.
3. Add and configure the following **modular** assets for the perimeter hallways at the back of the building: | Asset Name | CFrame.Position | CFrame.Orientation |
| --- | --- | --- | | WallCornerInner | `-125, 5, 290` | `0, 90, 0` | | WallLarge | `-125, 5, 275` | `0, 0, 0` | | WallLarge | `-125, 5, 260` | `0, 0, 0` | | WallLarge | `-125, 5, 245` | `0, 0, 0` | | WallSmall | `-125, 5, 240` | `0, 0, 0` | | WallCornerInner | `-120, 5, 235` | `0, 0, 0` | | WallMid | `-110, 5, 235` | `0, -90, 0` | | WallCornerOuter | `-110, 5, 235` | `0, 0, 0` | | WallLarge | `-110, 5, 220` | `0, 0, 0` | | WallMid | `-110, 5, 210` | `0, 0, 0` | | WallRiseB | `-110, 5, 210` | `0, 0, 0` | | WallCornerOuter | `-110, 10, 190` | `0, 90, 0` | | WallLarge | `-125, 10, 190` | `0, 90, 0` | | WallLarge | `-140, 10, 190` | `0, 90, 0` | | WallCornerInner | `-145, 10, 185` | `0, 90, 0` | | WallSmall | `-145, 10, 180` | `0, 0, 0` | | WallLarge | `-145, 10, 165` | `0, 0, 0` | | WallLarge | `-145, 10, 150` | `0, 0, 0` | | WallLarge | `-145, 10, 135` | `0, 0, 0` | | WallCornerInner | `-140, 10, 130` | `0, 0, 0` | | WallLarge | `-125, 10, 130` | `0, -90, 0` | | WallLarge | `-110, 10, 130` | `0, -90, 0` | | WallCornerOuter | `-110, 10, 130` | `0, 0, 0` | | WallRiseA | `-110, 5, 110` | `0, 0, 0` | | WallMid | `-110, 5, 100` | `0, 0, 0` | | WallLarge | `-110, 5, 85` | `0, 0, 0` | | WallCornerOuter | `-110, 5, 85` | `0, 90, 0` | | WallMid | `-120, 5, 85` | `0, 90, 0` | | WallCornerInner | `-125, 5, 80` | `0, 90, 0` | | WallLarge | `-125, 5, 65` | `0, 0, 0` | | WallLarge | `-125, 5, 50` | `0, 0, 0` | | WallLarge | `-125, 5, 35` | `0, 0, 0` | | WallSmall | `-125, 5, 30` | `0, 0, 0` | | WallCornerInner | `-120, 5, 25` | `0, 0, 0` |
4. Add and configure the following **prop** assets for the perimeter hallways at the back of the building: | Asset Name | CFrame.Position | CFrame.Orientation |
| --- | --- | --- | | SecurityCamera | `-120, 20, 290` | `0, 0, 0` | | WallHanging | `-124, 13, 287.5` | `0, 0, 0` | | CrateMedium | `-120, 5, 260` | `0, -180, 0` | | CrateSmall | `-110, 5, 250` | `0, 135, 0` | | WallHanging | `-109, 13, 217.5` | `0, 0, 0` | | WallHanging | `-109, 13, 103` | `0, 0, 0` | | CrateSmall | `-110, 5, 70` | `0, 135, 0` | | CrateMedium | `-120, 5, 65` | `0, -180, 0` | | WallHanging | `-124, 13, 37.5` | `0, 0, 0` | | SecurityCamera | `-120, 20, 30` | `0, -90, 0` |
5. Add and configure the following assets for the perimeter hallways on the right-side of the building: | Part | Size | CFrame.Position |
| --- | --- | --- | | WallLarge | `-105, 5, 25` | `0, -90, 0` | | DoorFrame | `-85, 5, 25` | `0, -90, 0` | | WallLarge | `-70, 5, 25` | `0, -90, 0` | | DoorFrame | `-50, 5, 25` | `0, -90, 0` | | WallLarge | `-35, 5, 25` | `0, -90, 0` |
6. Select the wall component of these assets, then in the **Properties** window, set **Color** to `255, 170, 255`.
7. Anchor all of these prop and modular assets.

### Doors

The final sample laser tag environment applies doors directly onto the greybox geometry to exactly match the original design, however, not all entrance or exit points have door assets. You may find that the requirements of your own game require more or less doors, depending on how you want to control combat within your combat pockets. More doors often leads to longer wait times before users enter or exit a combat pocket, but less doors may open up unwanted lines of sight.

For this reason, it's recommended to playtest with multiple variations to experiment different play styles. In fact, you may experiment with placing door assets into your combat pockets that only open to users from one side of the door, or not at all.

#### Create your own

To apply your own asset library to the doors:

1. Add and configure any **door** modular assets to the doorways of your combat pockets.
2. **OPTIONAL** Anchor all of these door assets.

#### Recreate the sample

To exactly recreate the doors within the sample [Environment Art - Constructing](https://www.roblox.com/games/14447826396/Environment-Art-Constructing) place file:

1. Add and configure the following **Door** assets for the left combat pocket: | CFrame.Position | CFrame.Orientation |
| --- | --- | | `-60, 5, 275` | `0, -90, 0` | | `-95, 5, 260` | `0, 180, 0` |
2. Add and configure the following **Door** assets for the right combat pocket:

| CFrame.Position | CFrame.Orientation |
| --- | --- |
| `-90, 5, 60` | `0, 0, 0` |
| `-80, 5, 45` | `0, 90, 0` |

### Exterior assets

The original greybox design for exterior assets was to set placeholder positions for objects that provide cover from enemy fire while users navigate the exterior primary lane. This was useful to help visualize what would help users as they ascend or descend stairs, cross the middle combat pocket, or otherwise exist in the outdoor space, but as you construct your environment, you can improve this design by providing different uses for these cover objects.

The following sections provide guidance on how to convert these initial placeholder assets into aesthetically pleasing objects that follow your game's art style, and keep the intent behind the original design.

#### Towers

The first exterior assets you can convert for the outdoor space are the two towers right outside of the middle combat pocket that intersect with the exterior primary lane. The technique in this section not only creates objects that are aesthetically pleasing to the eye, but it also creates objects that provide users a sense of scale in their environment. Every other object so far is about the size of the user's character **except** for these towers, which can lead to intrigue in the story behind the architecture or overall island that the building rests on.

#### Create your own

To apply your own asset library to the towers:

1. Using **block** parts, create a tower that is much larger than the player to provide a sense of scale in the environment.
2. Apply unique colors and materials to different block parts according to the art style of your game.
3. Duplicate this tower, then position it to a symmetrical location on your map.
4. Anchor all of these parts.

#### Recreate the sample

To exactly recreate the towers within the sample [Environment Art - Constructing](https://www.roblox.com/games/14447826396/Environment-Art-Constructing) place file:

1. Add and configure the following **block** parts for the left tower: | Part | Size | CFrame.Position | Color | Material | MaterialVariant |
| --- | --- | --- | --- | --- | --- | | Large Spire | `16, 98, 11` | `-32, 58, 186.5` | `248, 248, 248` | `Concrete` | `Concrete_Board_Formed_A` | | Middle Spire | `17.369, 77.734, 3.42` | `-32, 72, 186.5` | `181, 173, 156` | `Concrete` | `Concrete_Board_Formed_A` | | Bottom wide spire | `13, 75, 15` | `-31.5, 42.5, 186.5` | `181, 173, 156` | `Concrete` | `Concrete_Ribbed_A` | | Top Wide Spire | `17.288, 4, 15` | `-33.5, 83, 186.5` | `181, 173, 156` | `Concrete` | `Concrete_Ribbed_A` | | Base | `21, 5, 15` | `-29.5, 7.5, 186.5` | `181, 173, 156` | `Sand` | `MossStones` |
2. Group everything into a model, then duplicate the model.
3. Move the duplicate tower to a **CFrame.Position** of `-30.572, 57.93, 133.5`.
4. Anchor both of these models.

#### Columns

The second exterior assets you can convert for the outdoor space are the two columns that hold up the overhang pieces you will make later in this tutorial. Similar to the towers, the technique in this section not only creates objects that are aesthetically pleasing to the eye, but it also provides further visual cues to users about where they are in the overall environment. For example, each column has either mint or carnation pink detailing to inform users if they are closest to either their own or their enemy's spawn zone.

#### Create your own

1. Using **block** and **wedge** parts, create a column that will hold the roof of your building.
2. Apply unique colors and materials to different parts according to the art style of your game.
3. Duplicate this column, then position it to a symmetrical location on your map.
4. **OPTIONAL** Change the color of one part in each column to match each team's respective color theme.
5. Anchor all of these parts.

#### Recreate the Sample

To exactly recreate the columns within the sample [Environment Art - Constructing](https://www.roblox.com/games/14447826396/Environment-Art-Constructing) place file:

1. Add and configure the following **block** parts for the left column: | Part | Size | CFrame.Position | CFrame.Orientation | Color | Material | MaterialVariant |
| --- | --- | --- | --- | --- | --- | --- | | Top wall | `15, 20, 5` | `-22.5, 20, 238.5` | `0, 0, 0` | `248, 248, 248` | `Concrete` | `Concrete_Ribbed_A` | | Bottom wall | `15, 9, 5` | `-22.5, 5.5, 238.5` | `0, 0, 0` | `181, 173, 156` | `Concrete` | `Concrete_Ribbed_A` | | Base top | `6.483, 1, 6.583` | `-27.304, 5.298, 238.498` | `0, 0, 0` | `181, 173, 156` | `Concrete` | `Concrete_Ribbed_A` | | Base bottom | `6.483, 1.5, 19.652` | `-15.154, 1.479, 238.5` | `-21.622, -90, 0` | `181, 173, 156` | `Concrete` | `Concrete_Tie_Holes_A` | | Color detail | `1.734, 18.179, 6` | `-22.547, 23.597, 238.4` | `0, -180, 62` | `103, 255, 199` | `Concrete` | `<None>` |
2. Add and configure the following **wedge** part for the top of the left column: | Size | CFrame.Position | CFrame.Orientation | Color | Material | MaterialVariant |
| --- | --- | --- | --- | --- | --- | | `7, 11, 21` | `-18.5, 25.5, 238.5` | `0, -90, 180` | `248, 248, 248` | `Concrete` | `Concrete_Board_Formed_A` |
3. Group everything into a model, then duplicate the model.
4. Move the duplicate column to a **CFrame.Position** of `-18.169, 14.081, 81.5` and a **CFrame.Orientation** of `0, -90, 180`.
5. Select the mint **block** part, then in the **Properties** window, set the **Color** property to `255, 170, 255` to match the color theme of the team on the right of the map.
6. Anchor both of these models.

#### Planters

The final exterior assets you can convert for the outdoor space are the eight planters that extend along the entirety of the exterior primary lane. Using [solid modeling](/docs/en-us/parts/solid-modeling.md) operations, you can negate and join parts together to form the base of each planter, then apply your asset library using different materials, foliage, and/or trim asset configurations so that each one feels unique in the 3D space.

To apply your asset library to the left-most planter:

1. Add and configure the following **block** parts for the left-most planter: | Part | Size | CFrame.Position |
| --- | --- | --- | | Planter exterior | `20, 11, 5` | `-15, 4.5, 257.5` | | Divot | `18.5, 1, 4` | `-15, 9.75, 257.5` |
2. Select the divot part.
3. Navigate to Studio's **Model** tab toolbar, then click the **Negate** button. The part turns translucent.
4. Select both the negated part and the planter exterior part.
5. In Studio's **Model** tab toolbar, click the **Union** button. The negated part is cut out from the overlapping planter exterior part.
6. Select the union, then in the **Properties** window,
  1. Set **Color** to `181, 173, 156`.
  2. Set **Material** to **Concrete**.
  3. Set **MaterialVariant** to **Concrete_Board_Formed_A**.
  4. Enable **UsePartColor**.
7. Add and configure the following **block** parts for the dirt and edging of the planter: | Part | Size | CFrame.Position | CFrame.Orientation | Color | Material | MaterialVariant |
| --- | --- | --- | --- | --- | --- | --- | | Dirt | `19, 0.5, 4` | `-15, 9.25, 257.5` | `0, 0, 0` | `248, 248, 248` | `LeafyGrass` | `Moss_Lumpy_Stones_A` | | Top planter edging | `1.652, 1, 6.483` | `-24.838, 5.298, 257.741` | `0, 0, 0` | `181, 173, 156` | `Concrete` | `Concrete_Tie_Holes_A` | | Bottom planter edging | `6.483, 1.5, 19.652` | `-15.154, 1.479, 257.758` | `0, 0, -21.62` | `181, 173, 156` | `Concrete` | `Concrete_Tie_Holes_A` |
8. Add foliage assets to the top of the planter to the top of the planter to add more organic life to the outdoor space.
9. Anchor all of these parts and foliage assets.

Now that you know how to use the solid modeling tools, you can experiment in creating types of planters with different exteriors, materials, plant variety, and trim pieces. For example, the other variations of planters within the final sample laser tag environment either make an 'L' shape, or they layer **block** parts and white trim together to provide higher cover in the middle of the map.

### Roof

The original greybox design didn't include a roof to the building because it would have prevented you from seeing your progress as you designed and constructed your three lane map layout. However, now that the interior of the building is complete outside of configuring its light sources, you can apply your asset library to new geometry to finish the building and provide users shelter from the outdoor space.

The roof of the building is one of the most complex assets in the final sample laser tag environment because it includes multiple layers that must fit together with each other and with the interior geometry. The following instructions walk you through how to construct each layer, starting with the top-most geometry to the final layer of trim that surrounds the perimeter of the roof.

#### Skylights

The first, top-most layer of the roof is the skylight geometry. The purpose of this layer is to provide outdoor light into interior combat areas.

#### Create your own

To apply your own asset library to the skylights:

1. Add and configure any **skylight** modular assets to the ceiling of your building. This allows global lighting into combat areas, and provides a richer sense of immersion for players.
2. Using **block** parts, create glass for some of your skylights.
  1. Add and position a **block** part into a skylight.
  2. Select the part, then in the **Properties** window,
    1. Set **Color** to `105, 162, 172`.
    2. Set **Material** to **Neon**.
    3. Set **Transparency** to `0.6`.
3. Anchor all of these skylight assets.

#### Recreate the sample

To exactly recreate the skylights within the sample [Environment Art - Constructing](https://www.roblox.com/games/14447826396/Environment-Art-Constructing) place file:

1. Add and configure the following **modular** assets for the left skylight: | Asset Name | CFrame.Position | CFrame.Orientation |
| --- | --- | --- | | SkylightCornerInner | `-60, 20, 265` | `0, 180, 0` | | SkylightCornerInner | `-85, 20, 240` | `0, 0, 0` | | SkylightCornerInner | `-60, 20, 240` | `0, -90, 0` | | SkylightCornerInner | `-85, 20, 265` | `0, 90, 0` | | SkylightSmall | `-70, 20, 240` | `0, -90, 0` | | SkylightSmall | `-85, 20, 250` | `0, 0, 0` | | SkylightSmall | `-75, 20, 265` | `0, 90, 0` | | SkylightSmall | `-60, 20, 255` | `0, 180, 0` |
2. Add and configure the following **modular** assets for the top-left skylight: | Asset Name | CFrame.Position | CFrame.Orientation |
| --- | --- | --- | | SkylightCornerInner | `-120, 20, 280` | `0, 90, 0` | | SkylightCornerInner | `-110, 20, 280` | `0, 180, 0` | | SkylightCornerInner | `-120, 20, 240` | `0, 0, 0` | | SkylightCornerInner | `-110, 20, 240` | `0, -90, 0` | | SkylightLarge | `-110, 20, 252.5` | `0, 180, 0` | | SkylightLarge | `-120, 20, 245` | `0, 0, 0` | | SkylightLarge | `-120, 20, 260` | `0, 0, 0` | | SkylightLarge | `-110, 20, 260` | `0, 180, 0` | | SkylightLarge | `-120, 20, 267.5` | `0, 0, 0` | | SkylightLarge | `-120, 20, 252.5` | `0, 0, 0` | | SkylightLarge | `-110, 20, 267.5` | `0, 180, 0` | | SkylightLarge | `-110, 20, 275` | `0, 180, 0` |
3. Add and configure the following **modular** assets for the middle skylight: | Asset Name | CFrame.Position | CFrame.Orientation |
| --- | --- | --- | | SkylightCornerInner | `-120, 25, 140` | `0, -90, 0` | | SkylightCornerInner | `-140, 25, 140` | `0, 0, 0` | | SkylightCornerInner | `-120, 25, 180` | `0, 180, 0` | | SkylightCornerInner | `-140, 25, 180` | `0, 90, 0` | | SkylightLarge | `-120, 25, 170` | `0, 180, 0` | | SkylightLarge | `-140, 25, 150` | `0, 0, 0` | | SkylightSmall | `-120, 25, 155` | `0, 180, 0` | | SkylightSmall | `-140, 25, 165` | `0, 0, 0` |
4. Add and configure the following **modular** assets for the top-right skylight: | Asset Name | CFrame.Position | CFrame.Orientation |
| --- | --- | --- | | SkylightCornerInner | `-110, 20, 40` | `0, -90, 0` | | SkylightCornerInner | `-120, 20, 80` | `0, 90, 0` | | SkylightCornerInner | `-110, 20, 80` | `0, 180, 0` | | SkylightCornerInner | `-120, 20, 40` | `0, 0, 0` | | SkylightLarge | `-110, 20, 67.5` | `0, 180, 0` | | SkylightLarge | `-110, 20, 60` | `0, 180, 0` | | SkylightLarge | `-110, 20, 75` | `0, 180, 0` | | SkylightLarge | `-120, 20, 52.5` | `0, 0, 0` | | SkylightLarge | `-110, 20, 52.5` | `0, 180, 0` | | SkylightLarge | `-120, 20, 60` | `0, 0, 0` | | SkylightLarge | `-120, 20, 67.5` | `0, 0, 0` | | SkylightLarge | `-120, 20, 45` | `0, 0, 0` |
5. Add and configure the following **modular** assets for the right skylight: | Asset Name | CFrame.Position | CFrame.Orientation |
| --- | --- | --- | | SkylightCornerInner | `-85, 20, 80` | `0, 90, 0` | | SkylightCornerInner | `-60, 20, 80` | `0, 180, 0` | | SkylightCornerInner | `-85, 20, 55` | `0, 0, 0` | | SkylightCornerInner | `-60, 20, 55` | `0, -90, 0` | | SkylightSmall | `-70, 20, 55` | `0, -90, 0` | | SkylightSmall | `-85, 20, 65` | `0, 0, 0` | | SkylightSmall | `-75, 20, 80` | `0, 90, 0` | | SkylightSmall | `-60, 20, 70` | `0, 180, 0` |
6. Add and configure the following **block** parts for the skylight glass for the two skylights near the back of the building: | Part | Size | CFrame.Position |
| --- | --- | --- | | Left glass | `10, 1.574, 39` | `-115, 21.395, 260.5` | | Right glass | `10, 1.574, 39` | `-115, 21.395, 60.5` |
7. Select these two parts, then in the **Properties** window:
  1. Set **Color** to `105, 162, 172`.
  2. Set **Material** to **Neon**.
  3. Set **Transparency** to `0.6`.
8. Anchor all of these parts and modular assets.
9. **OPTIONAL** You can add foliage assets around the left, middle, and right skylights for more visual variety when users navigate through the building, and to add a pop of color to the ceiling.

#### Ceiling

The second layer of the roof is the ceiling geometry that users see at the top of their view as they navigate the interior of the building. The purpose of this layer is to fill the open areas between the top trim of each wall asset.

#### Create your own

To apply your own asset library to the ceiling of the roof:

1. Using **block** and **wedge** parts, fill in the open space around your skylights.
2. Select these parts, then in the **Properties** window, set **Color**, **Material**, and/or **MaterialVariant** to values that apply a distinct visual treatment from other surfaces in your environment. This helps players orient themselves when they are moving their camera quickly.
3. Anchor all of these ceiling assets.

#### Recreate the sample

To exactly recreate the ceiling within the sample [Environment Art - Constructing](https://www.roblox.com/games/14447826396/Environment-Art-Constructing) place file:

1. Add and configure the following **block** parts for the fill: | Size | CFrame.Position |
| --- | --- | | `55, 1, 30` | `-77.5, 20.5, 320` | | `30, 1, 5` | `-105, 20.5, 287.5` | | `10, 1, 5` | `-115, 20.5, 282.5` | | `50, 1, 10` | `-65, 20.5, 285` | | `10, 1, 85` | `-35, 20.5, 247.5` | | `10, 1, 20` | `-105, 20.5, 250` | | `5, 1, 35` | `-102.5, 20.5, 222.5` | | `25, 1, 5` | `-87.5, 20.5, 217.5` | | `35, 1, 15` | `-57.5, 20.5, 212.5` | | `5, 1, 10` | `-32.5, 20.5, 200` | | `5, 1, 15` | `-102.5, 25.5, 187.5` | | `35, 1, 5` | `-122.5, 25.5, 182.5` | | `35, 1, 5` | `-122.5, 25.5, 137.5` | | `5, 1, 15` | `-102.5, 25.5, 132.5` | | `5, 1, 35` | `-102.5, 20.5, 97.5` | | `25, 1, 5` | `-87.5, 20.5, 102.5` | | `35, 1, 15` | `-57.5, 20.5, 107.5` | | `10, 1, 85` | `-35, 20.5, 72.5` | | `5, 1, 10` | `-32.5, 20.5, 120.5` | | `10, 1, 20` | `-105, 20.5, 70` | | `10, 1, 5` | `-115, 20.5, 37.5` | | `30, 1, 5` | `-105, 20.5, 32.5` | | `50, 1, 10` | `-65, 20.5, 35` | | `55, 1, 30` | `-77.5, 20.5, 0` |
2. Add and configure the following **wedge** parts for the elevated ceiling: | Size | CFrame.Position | CFrame.Orientation |
| --- | --- | --- | | `5, 5, 10` | `-102.5, 22.5, 200` | `0, 0, 180` | | `5, 5, 10` | `-102.5, 22.5, 120` | `0, 180, 180` |
3. Select all of these ceiling parts, then in the **Properties** window:
  1. Set **Color** to `248, 248, 248`.
  2. Set **MaterialVariant** to **MetalPanels**.
4. Anchor all of these parts.

#### Top roof

The third layer of the roof is the top roof geometry. The purpose of this layer is to provide bulk to the outermost roof area that users see as they look at the building from the outdoor space. It also adds a sense of depth to the skylights, making the building look more complete from the inside and out.

#### Create your own

To apply your own asset library to the top of the roof:

1. Using **block** and **wedge** parts, add in a thick layer to cover the ceiling without hiding your skylights. This surface is what players can see when they are looking at the building from the outdoor space.
2. Select these parts, then in the **Properties** window, set **Color**, **Material**, and/or **MaterialVariant** to values that apply a visual treatment according to the art style of your game.
3. Anchor all of these top roof assets.

#### Recreate the sample

To exactly recreate the top of the roof within the sample [Environment Art - Constructing](https://www.roblox.com/games/14447826396/Environment-Art-Constructing) place file:

1. Add and configure the following **block** parts for the top roof on the left of the map: | Size | CFrame.Position |
| --- | --- | | `126, 15, 90` | `-92, 28.5, 325` | | `35, 15, 40` | `-137.5, 28.5, 260` | | `25, 15, 40` | `-97.5, 28.5, 260` | | `35, 15, 15` | `-72.5, 28.5, 272.5` | | `25, 15, 75` | `-42.5, 28.5, 242.5` | | `100, 15, 35` | `-105, 28.5, 222.5` | | `65, 15, 10` | `-62.5, 28.5, 200` |
2. Add and configure the following **block** parts for the top roof on the top middle of the map: | Size | CFrame.Position |
| --- | --- | | `15, 10, 90` | `-147.5, 31, 160` | | `20, 10, 25` | `-130, 31, 192.5` | | `20, 10, 25` | `-130, 31, 127.5` | | `26, 10, 90` | `-107, 31, 160` |
3. Add and configure the following **block** parts for the top roof on the right of the map: | Size | CFrame.Position |
| --- | --- | | `100, 15, 35` | `-105, 28.5, 97.5` | | `65, 15, 10` | `-62.5, 28.5, 120` | | `35, 15, 40` | `-137.5, 28.5, 60` | | `25, 15, 40` | `-97.5, 28.5, 60` | | `35, 15, 15` | `-72.5, 28.5, 47.5` | | `25, 15, 75` | `-42.5, 28.5, 77.5` | | `126, 15, 90` | `-92, 28.5, -5` |
4. Select all of these top roof parts, then in the **Properties** window:
  1. Set **Color** to `181, 173, 156`.
  2. Set **Material** to **Concrete**.
  3. Set **MaterialVariant** to **Concrete_Tie_Holes_A**.
5. Add and configure the following **block** parts for the top roof on the lower middle of the map: | Size | CFrame.Position |
| --- | --- | | `54, 5, 15` | `-67, 28.5, 187.5` | | `9, 5, 40` | `-89.5, 28.5, 160` | | `54, 5, 15` | `-67, 28.5, 132.5` |
6. Select all of these top roof parts, then in the **Properties** window, then set **Material** to **Concrete**.
7. Add and configure the following **block** parts for the top roof on the sides of the middle of the map: | Size | CFrame.Position |
| --- | --- | | `25, 5, 15` | `-52.5, 23.5, 187.5` | | `25, 5, 15` | `-52.5, 23.5, 132.5` |
8. Add and configure the following **wedge** parts for the top roof on the sides of the middle of the map: | Size | CFrame.Position | CFrame.Orientation |
| --- | --- | --- | | `15, 5, 10` | `-70, 23.5, 187.5` | `0, 90, 180` | | `15, 5, 10` | `-70, 23.5, 132.5` | `0, 90, 180` |
9. Select all of these top roof parts, then in the **Properties** window:
  1. Set **Color** to `248, 248, 248`.
  2. Set **MaterialVariant** to **MetalPanels**.
10. Anchor all of these parts.

#### Overhang

The fourth layer of the roof is the overhang geometry that the column assets hold up in order for the building to be structurally sound. The purpose of this layer is to provide an aesthetically pleasing awning space for users navigating the exterior primary lane.

#### Create your own

To apply your own asset library to the overhang of the roof:

1. Using **block** and **wedge** parts, add in a thick overhang for your columns to hold up. This surface provides players partial cover from the sun while they are navigating the exterior primary lane.
2. Select these parts, then in the **Properties** window, set **Color**, **Material**, and/or **MaterialVariant** to values that apply a visual treatment according to the art style of your game.
3. Anchor all of these overhang parts.

#### Recreate the sample

To exactly recreate the overhang within the sample [Environment Art - Constructing](https://www.roblox.com/games/14447826396/Environment-Art-Constructing) place file:

1. Add and configure the following **block** parts for the overhang on the left of the map: | Size | CFrame.Position | Color | Material | MaterialVariant |
| --- | --- | --- | --- | --- | | `16, 5, 90` | `-16, 38.5, 240` | `181, 173, 156` | `Concrete` | `Concrete_Board_Formed_A` | | `21, 5, 90` | `-18.5, 33.5, 240` | `181, 173, 156` | `Concrete` | `Concrete_Tie_Holes_A` | | `1, 16, 91` | `-29.5, 28, 239.5` | `181, 173, 156` | `Concrete` | `Concrete_Board_Formed_A` | | `0.5, 0.9, 91` | `-30, 20.4, 239.5` | `91, 93, 105` | `Metal` | `<None>` |
2. Add and configure the following **wedge** parts for the overhang on the left of the map: | Size | CFrame.Position | CFrame.Orientation | Color | Material | MaterialVariant |
| --- | --- | --- | --- | --- | --- | | `2, 11, 21` | `-18.5, 25.5, 278` | `0, -90, 180` | `248, 248, 248` | `Concrete` | `Concrete_Board_Formed_A` | | `88, 10, 20` | `-19, 26, 240` | `0, -90, 180` | `181, 173, 156` | `Concrete` | `Concrete_Board_Formed_A` | | `2, 11, 21` | `-18.5, 25.5, 202` | `0, -90, 180` | `248, 248, 248` | `Concrete` | `Concrete_Board_Formed_A` |
3. Add and configure the following **block** parts for the overhang on the right of the map: | Size | CFrame.Position | Color | Material | MaterialVariant |
| --- | --- | --- | --- | --- | | `12, 5, 90` | `-14, 38.5, 80` | `181, 173, 156` | `Concrete` | `Concrete_Board_Formed_A` | | `21, 5, 90` | `-18.5, 33.5, 80` | `181, 173, 156` | `Concrete` | `Concrete_Board_Formed_A` | | `1, 16, 91` | `-29.5, 28, 80.5` | `181, 173, 156` | `Concrete` | `<None>` | | `0.5, 0.9, 91` | `-30, 20.4, 80.5` | `91, 93, 105` | `Metal` | `<None>` |
4. Add and configure the following **wedge** parts for the overhang on the right of the map: | Size | CFrame.Position | CFrame.Orientation | Color | Material | MaterialVariant |
| --- | --- | --- | --- | --- | --- | | `2, 11, 21` | `-18.5, 25.5, 118` | `0, -90, 180` | `255, 255, 255` | `Concrete` | `Concrete_Board_Formed_A` | | `88, 10, 20` | `-19, 26, 80` | `0, -90, 180` | `181, 173, 156` | `Concrete` | `Concrete_Board_Formed_A` | | `2, 11, 21` | `-18.5, 25.5, 42` | `0, -90, 180` | `255, 255, 255` | `Concrete` | `Concrete_Board_Formed_A` |
5. Anchor all of these parts.

#### Trim

The final layer of the roof is the trim geometry that surrounds the perimeter of the roof. The purpose of this layer is to provide visual cohesion between each previous layer from users looking at the room from the outdoor space.

#### Create your own

To apply your own asset library to the trim of the roof:

1. Add and configure **trim** modular assets along the overhang of your roof.
2. Select these parts, then in the **Properties** window, set **Color**, **Material**, and/or **MaterialVariant** to values that apply a visual treatment according to the art style of your game.
3. Anchor all of these overhang parts.

#### Recreate the sample

To exactly recreate the trim of the roof within the sample [Environment Art - Constructing](https://www.roblox.com/games/14447826396/Environment-Art-Constructing) place file:

1. Add and configure the following **modular** assets for the top-most trim: | Asset Name | CFrame.Position | CFrame.Orientation |
| --- | --- | --- | | ExtTrimBLong | `-48, 37, 285` | `0, -90, 0` | | ExtTrimBLong | `-8, 37, 285` | `0, 0, 0` | | ExtTrimBLong | `-8, 37, 240` | `0, 0, 0` | | ExtTrimBLong | `-8, 37, 195` | `0, 90, 0` | | ExtTrimBLong | `-48, 37, 195` | `0, 90, 0` | | ExtTrimBLong | `-89, 37, 195` | `0, 0, 0` | | ExtTrimBLong | `-89, 37, 160` | `0, 0, 0` | | ExtTrimBLong | `-88, 37, 125` | `0, -90, 0` | | ExtTrimBLong | `-48, 37, 125` | `0, -90, 0` | | ExtTrimBLong | `-8, 37, 125` | `0, 0, 0` | | ExtTrimBLong | `-8, 37, 80` | `0, 0, 0` | | ExtTrimBLong | `-8, 37, 35` | `0, 90, 0` | | ExtTrimBCorner | `-8, 37, 285` | `0, 0, 0` | | ExtTrimBCorner | `-8, 37, 195` | `0, 90, 0` | | ExtTrimBCorner | `-8, 37, 125` | `0, 0, 0` | | ExtTrimBCorner | `-8, 37, 35` | `0, 90, 0` |
2. Select these trim assets, then in the **Properties** window, set **Color** to `248, 248, 248`.
3. Add and configure the following **modular** assets for the bottom-most trim: | Asset Name | CFrame.Position | CFrame.Orientation |
| --- | --- | --- | | ExtTrimALong | `-48, 31, 285` | `0, -90, 0` | | ExtTrimALong | `-8, 31, 285` | `0, 0, 0` | | ExtTrimAShort | `-8, 31, 245` | `0, 0, 0` | | ExtTrimALong | `-8, 31, 235` | `0, 0, 0` | | ExtTrimALong | `-8, 31, 195` | `0, 90, 0` | | ExtTrimALong | `-48, 31, 195` | `0, 90, 0` | | ExtTrimALong | `-88, 31, 195` | `-88, 31, 195` | | ExtTrimALong | `-88, 31, 125` | `0, -90, 0` | | ExtTrimALong | `-48, 31, 125` | `0, -90, 0` | | ExtTrimALong | `-8, 31, 125` | `0, 0, 0` | | ExtTrimAShort | `-8, 31, 85` | `0, 0, 0` | | ExtTrimALong | `-8, 31, 75` | `0, 0, 0` | | ExtTrimALong | `-8, 31, 35` | `0, 90, 0` | | ExtTrimBCorner | `-8, 31, 285` | `0, 0, 0` | | ExtTrimBCorner | `-8, 31, 195` | `0, 90, 0` | | ExtTrimBCorner | `-8, 31, 125` | `0, 0, 0` | | ExtTrimBCorner | `-8, 31, 35` | `0, 90, 0` |
4. Add and configure the following **modular** assets for the trim in the middle of the roof: | Asset Name | CFrame.Position | CFrame.Orientation |
| --- | --- | --- | | ExtTrimAShort | `-24, 26, 195` | `0, 90, 0` | | ExtTrimAMid | `-24, 26, 194` | `0, 0, 0` | | ExtTrimALong | `-24, 26, 179` | `0, 90, 0` | | ExtTrimAMid | `-64, 26, 179` | `0, 90, 0` | | ExtTrimALong | `-85, 26, 178` | `0, 0, 0` | | ExtTrimAMid | `-84, 26, 141` | `0, -90, 0` | | ExtTrimALong | `-64, 26, 141` | `0, -90, 0` | | ExtTrimAMid | `-24, 26, 141` | `0, 0, 0` | | ExtTrimAShort | `-24, 26, 126` | `0, 90, 0` | | ExtTrimACorner | `-24, 26, 194` | `0, 0, 0` | | ExtTrimACorner | `-24, 26, 179` | `0, 90, 0` | | ExtTrimACorner | `-84, 26, 178` | `0, -90, 0` | | ExtTrimACorner | `-84, 26, 142` | `0, 180, 0` | | ExtTrimACorner | `-24, 26, 141` | `0, 0, 0` | | ExtTrimACorner | `-24, 26, 126` | `0, 90, 0` |
5. Select these trim assets, then in the **Properties** window, set **Color** to `255, 170, 0`.
6. Anchor all of these trim assets.

## Delete excess geometry

Now that your building is complete, it's time to delete the underlying greybox geometry and the baseplate. This process removes excess polygons that users will never see nor interact with, which quickly improves memory and performance for devices with memory and graphics processing unit (GPU) limitations. In addition, removing the baseplate also allows the building to float in the sky, which is good preparation for you to sculpt terrain for the outdoor space in the next section.

To delete excess geometry:

1. In the **Explorer** window, delete all greybox geometry from the first section of this tutorial.
2. Delete the baseplate object.

## Sculpt terrain

Right now your environment is mostly architectural aside from foliage in your planters. However, following the sample art style from [Develop Polished Assets](/docs/en-us/tutorials/curriculums/environmental-art/develop-polished-assets.md), the 3D space should contain a healthy mix of futuristic technology and lush greenery to inform users that the world values technological advances, but not at the expense of the earth.

Using the [Terrain Editor](/docs/en-us/parts/terrain.md), you can quickly generate and sculpt detailed and realistic terrain to bring organic life to the outdoor space. Because you set material overrides as you created your custom materials in [Assemble an Asset Library](/docs/en-us/tutorials/curriculums/environmental-art/assemble-an-asset-library.md), you can also utilize your tileable textures through **Terrain Editor** brushes to add moss, flowers, and stone paths that are cohesive with the rest of your environment.

> **Info:** Sculpting terrain is an art form, and it's difficult to exactly recreate brush strokes and subtle material edits. As long as your terrain meets the needs of your own game, it's normal and expected for your environment to look and feel different from the sample laser tag environment.

#### Create your own

To apply your own terrain to the outdoor area:

1. From the toolbar's **Home** tab, click **Terrain**. The [Terrain Editor](/docs/en-us/studio/terrain-editor.md) window opens.
2. Navigate to the **Edit** tab, then click the **Draw** button.
3. In the **Brush Settings** section, customize your brush according to the material you want to add to your map. For example, the sample starts this process with the settings in the following image.
4. In the **Materials Settings** section, select a material for the **unplayable area**, such as water or cracked lava, then in the viewport, draw where you want your playable area to end. This material communicates where the map ends for the outdoor space.
5. Navigate back to the **Materials Settings** section, select a material for the **playable area**, such as grass, pavement, or wood planks, then in the viewport, draw where you want your playable area to start. This material communicates where the map starts for the outdoor space
6. Navigate back to the **Terrain Editor**, then select the **Paint** tool.
7. In the **Brush Settings** section, customize your brush according to the material you want to add to your map, and select a new material.
8. In the viewport, draw along the exterior lane. This material communicates the primary path players can take as they are navigating the outdoor space.
9. **(Optiona)** Add and configure any applicable props to the outdoor space for visual variation.

#### Recreate the sample

To recreate the terrain within the sample [Environment Art - Constructing](https://www.roblox.com/games/14447826396/Environment-Art-Constructing) place file:

1. From the toolbar's **Home** tab, click **Terrain**. The [Terrain Editor](/docs/en-us/studio/terrain-editor.md) window opens.
2. Navigate to the **Edit** tab, then click the **Draw** button.
3. In the **Brush Settings** section,
  1. Set **Brush Mode** to **Add**.
  2. Set the brush shape to the cylinder shape.
  3. Set **Base Size** to `16`.
  4. Set **Height** to `5`.
  5. Set **Pivot Position** to **Top**.
  6. Set **Plane Lock** to **Manual**.
  7. In the **Edit Plane** setting,
    1. Click the **Edit** button.
    2. Set **Position** to `0, -1, 0`.
    3. Click the **Apply** button.
4. In the **Material Settings** section, select the **Water** material, then in the viewport, draw a crescent shaped pool around the building.
5. Navigate back to the **Brush Settings** section, then
  1. Set **Base Size** to `10`.
  2. Set **Height** to `10`.
  3. Set **Ignore Parts** to **True/Enabled**.
  4. In the **Edit Plane** setting,
    1. Click the **Edit** button.
    2. Set **Position** to `0, 0, 0`.
    3. Click the **Apply** button.
6. In the **Material Settings** section, select the **Slate** material, then in the viewport, draw another crescent shape that separates the pool from the architecture, and then a thin boundary around the outside of the pool.
7. Navigate back to the **Terrain Editor**, then select the **Paint** tool.
8. In the **Brush Settings** section,
  1. Set the brush shape to the cylinder shape.
  2. Set **Base Size** to `3`.
  3. Set **Pivot Position** to **Top**.
  4. Set **Plane Lock** to **Off**.
9. In the **Material Settings** section, alternate between your **Mud**, **Leafy Grass**, **Ground**, **Sand**, **Salt**, **Slate**, and **Snow** custom materials, then in the viewport, draw on the remaining area.
10. Using your asset library,
  1. Add a **FloatingIsland** asset with a `Datatype.CFrame.Position` of `201.726, -14.315, 183.5` for a spawn area users join before they separate into teams.
  2. Intersperse rock assets with varying `Class.MeshPart.Size` and `Datatype.CFrame.Orientation` values along the border of the playable area.
  3. Intersperse foliage assets around the outdoor space to add more organic life to the outdoor space.

## Contain the playable area

If you playtest your game and navigate off the island, your character will fall until they reach the project's `Class.Workspace.FallenPartsDestroyHeight` and respawn back in your team's spawn zone. To ensure that users cannot fall off the island, or join the match too early from the floating area spawn zone before they separate into teams, you must contain the playable area with an invisible barrier.

The values in this section are highly dependent on the terrain within the final sample laser tag environment. It's recommended to playtest and verify that there are no gaps in the barrier according to the custom terrain within your own game.

#### Create your own

To contain the playable area in your game:

1. Using **block** parts, surround the playable area in your outdoor area. It's important to ensure these parts are tall enough to block players from jumping over your barrier, and that there are no cracks they can slip through and fall off the edge of your map.
2. Select these parts, then in the **Properties** window,
  1. Set **Transparency** to `1`.
  2. Disable **CanCollide**.
  3. Enable **Anchored**.

#### Recreate the sample

To exactly recreate the containment of the playable area within the sample [Environment Art - Constructing](https://www.roblox.com/games/14447826396/Environment-Art-Constructing) place file:

1. Add and configure the following **block** parts to surround the playable area. The top containment part in the following image is semi-transparent for visual reference. | Size | CFrame.Position | CFrame.Orientation |
| --- | --- | --- | | `69, 71, 17` | `12.5, 23, -47.5` | `0, 0, 0` | | `89, 71, 22` | `39, 23, -18` | `0, -45, 0` | | `83, 71, 22` | `70.5, 23, 46` | `0, -90, 0` | | `54, 71, 42` | `93, 23, 95` | `0, -50, 0` | | `129, 71, 85` | `137, 23, 179` | `0, -90, 0` | | `155, 71, 22` | `55, 23, 292` | `0, -135, 0` | | `29, 71, 22` | `-7.5, 23, 337` | `0, 180, 0` | | `34, 71, 6` | `182, 23, 165` | `0, -135, 0` | | `34, 71, 6` | `196.5, 23, 157` | `0, 180, 0` | | `34, 71, 6` | `212.5, 23, 160` | `0, 135, 0` | | `34, 71, 6` | `224, 23, 181` | `0, -90, 0` | | `34, 71, 6` | `216, 23, 198` | `0, -135, 0` | | `34, 71, 6` | `195, 23, 203` | `0, 180, 0` | | `34, 71, 6` | `181, 23, 194` | `0, 135, 0` | | `379, 32, 389` | `41, 42, 153` | `0, 180, 0` |
2. Select these parts, then in the **Properties** window,
  1. Set **Transparency** to `1`.
  2. Disable **CanCollide**.
  3. Enable **Anchored**.

## Configure special effects

Your building's architecture and outdoor space are nearly complete with assets from your asset library, but you may have noticed either consciously or unconsciously that the overall environment feels static. This is because realistic environments include movement from many different sources, whether that's from clouds crawling through the sky, wind brushing through greenery, or life forms navigating the space.

You can mimic realistic environments by configuring special effects that add dynamic movement to your environment, and provoke emotion from users. This process often makes worlds feel more alive, supporting a deep sense of immersion while people access your game.

### Background clouds

The first type of special effect the final sample laser tag environment uses to add movement to the 3D space is an effect called dynamic clouds. [Dynamic clouds](/docs/en-us/environment/clouds.md) are realistic clouds that drift slowly across the sky, and they are useful for creating movement that feels far away from the user while still present in the environment. You can adjust their appearance through the `Class.Clouds` object to create unique atmospheres, and customize their direction and speed through global wind.

_Without dynamic clouds_

_With default dynamic clouds_

#### Create your own

To add and configure your own dynamic clouds in the background:

1. In the **Explorer** window, add a **Clouds** object to the **Terrain** object.
  1. Hover over the **Terrain** object and click the **⊕** button. A contextual menu displays.
  2. From the contextual menu, insert a **Clouds** object.
2. Select the **Clouds** object, then in the **Properties** window,
  1. Set **Cover** to a value between `0` (no clouds) and `1` (full cloud cover).
  2. Set **Density** to a value between `0` (light, translucent clouds) and `1` (heavy, dark clouds).
  3. Set **Color** to a material color of cloud particles according to the art style of your game.

#### Recreate the sample

To add and configure dynamic clouds in the background:

1. In the **Explorer** window, add a **Clouds object** to the **Terrain** object.
  1. Hover over the **Terrain** object and click the **⊕** button. A contextual menu displays.
  2. From the contextual menu, insert a **Clouds** object.
2. Select the **Clouds** object, then in the **Properties** window,
  1. Set **Cover** to `0.625`.
  2. Set **Density** to `0.5`.
  3. Set **Color** to `143, 143, 143`.

### Foreground clouds

The second type of special effect the final sample laser tag environment uses to add movement to the 3D space is an effect called particle emitters. [Particle emitters](/docs/en-us/effects/particle-emitters.md) emit 2D images, or particles, that look and behave for the duration of their lifetime according to the particle emitter's set properties, and they are useful for creating movement that feels and often is close to the user.

Particle emitters have many properties you can adjust to achieve both subtle and bold effects. The following instructions show you how to exactly recreate the foreground clouds within the sample [Environment Art - Constructing](https://www.roblox.com/games/14447826396/Environment-Art-Constructing) place file, but you can modify any property for the needs of your own game. It's recommended to keep these clouds large and with a gentle motion between the gameplay space and the static background.

To add and configure foreground clouds:

1. Add a **block** part to a position where you want users to see a floating cloud.
2. Select this **block** part, then in the **Properties** window,
  1. Set **Transparency** to `1`.
  2. Disable **CanCollide**.
  3. Enable **Anchored**.
3. Create a particle emitter within this part.
  1. In the **Explorer** window, hover over the **block** part and click the **⊕** button. A contextual menu displays.
  2. From the contextual menu, insert a **ParticleEmitter**. The particle emitter immediately emits particles within the part's area.
4. Select this particle emitter, then in the **Properties** window,
  1. Set **Color** to a color sequence that looks like the following image.
  2. Set **LightEmission** to `0.3` to blend the colors of the texture and its environment.
  3. Set **LightInfluence** to `0.2` to allow environment light to have a subtle effect on the color of particles.
  4. Set **Orientation** to **FacingCameraWorldUp** so particles always emit up toward the sky.
  5. Set **Size** to `100` to create large clouds.
  6. Set **Squash** to `-0.25` to shrink particles horizontally.
  7. Set **Texture** to an image of a cloud. The sample uses `rbxassetid://10714362544`.
  8. Set **Transparency** to a number sequence that looks like the following image.
  9. Set **Lifetime** to `30` to fade out particles at 30 seconds.
  10. Set **Rate** to `0.25` to emit particles slowly.
  11. Set **Acceleration** to `0, -0.8, 0` to impact particle speed over their lifetime.
  12. Set **Drag** to `0.1` to make particles look their speed over time.
  13. Enable **LockedToPart** to keep particles close to the particle emitter.
5. Repeat this process, moving cloud particle emitters throughout the environment.

In addition, you can layer multiple particle emitters together to give clouds more depth. For example, in the final sample laser tag environment, foreground clouds layer an additional particle emitter with a **Color** property of `248, 248, 248`, **Texture** property of `rbxassetid://10714433747`, and a **Rate** property of `0.1`. You can find both of these particle emitters in the sample [Environment Art Asset Library](https://www.roblox.com/library/14447738661/Environment-Art-Asset-Library).

### Dust particles

Particle emitters are such a versatile type of special effect because they offer so many properties you can customize to create interesting visual effects, such as glowing portals, green billowing smoke, or vibrant explosions. The final sample laser tag environment uses particle emitters again in this section to create floating dust particles that surround the user as they navigate the outdoor space.

Similar to the foreground clouds steps, the following instructions show you how to exactly recreate the dust particles within the sample [Environment Art - Constructing](https://www.roblox.com/games/14447826396/Environment-Art-Constructing) place file, but you can modify any property for the needs of your own game. It's recommended to keep particle speed slow to only provide micro motion within the environment.

To add and configure dust particles for the outdoor space:

1. Add a **block** part to the environment that covers the entire island.
2. Select this **block** part, then in the **Properties** window,
  1. Set **Transparency** to `1`.
  2. Disable **CanCollide**.
  3. Enable **Anchored**.
3. Create a particle emitter within this part.
  1. In the **Explorer** window, hover over the **block** part and click the **⊕** button. A contextual menu displays.
  2. From the contextual menu, insert a **ParticleEmitter**. The particle emitter immediately emits particles within the part's area.
4. Select this particle emitter, then in the **Properties** window,
  1. Set **Color** to `192, 241, 255` to give the particles a light blue hue.
  2. Set **Size** to a number sequence that looks like the following image.
  3. Set **Texture** to a dust mote image. The sample uses `rbxassetid://14302399641`.
  4. Set **Transparency** to a number sequence that looks like the following image.
  5. Set **ZOffset** to `-5` to move particles away from the camera.
  6. Set **Lifetime** to `1, 10` to set the minimum and maximum age of a particle to 1 and 10 seconds, respectively.
  7. Set **Rate** to `50000` to create many particles for your environment.
  8. Set **RotSpeed** to `-60` to create a range of speeds for newly emitted particles.
  9. Set **Speed** to `1, 5` to set the minimum and maximum speed of a particle to 1 and 5 studs per second, respectively.
  10. Set **Acceleration** to `1, -1, 1` to impact particle speed over its lifetime.
  11. Enable **LockedToPart** to keep particles close to the particle emitter.

## Configure lighting sources

Now that your environment has movement, the final step in constructing your environment is to configure lighting sources. Studio offers two high-level types of lighting sources:

- **Global lighting** - Produces lighting for the entire outdoor environment.
- **Local lighting** - Produces lighting around where you place them within your game.

Both lighting sources are important to consider because your game has both an indoor and outdoor environment that impact the user's ability to see what is happening around them while they're in combat.

### Global lighting

Global lighting is the luminescence from either the sun or moon in a game. By adjusting a couple of key default properties in the `Class.Lighting` service, you can dramatically change how that light appears to users, as well as how it interacts with any other object you place in the game.

Studio begins every game with `Enum.LightingStyle|Soft` lighting which renders a flatter look with softer lights and shadows. However, to enhance the environment and equip your local light sources to produce precise shadows and illumination, such as the lighting in the hallways and above the signage, you must enable `Enum.LightingStyle|Realistic` lighting. This allows both your global and local lighting to work together and provide more realistic and immersive visuals.

For example, the `Enum.LightingStyle|Realistic` lighting style automatically detects when a user is either in an interior or exterior space, then it responds by enabling the appropriate lighting model. This means that reflections are able to reflect off the floor and ceiling within the building, providing a richer visual game as users navigate through combat pockets.

#### Create your own

To configure your own global lighting:

1. In the **Explorer** window, select the **Lighting** service, then in the **Properties** window, set its properties to values that reflect the art style of your game. For more information on these properties, see [Global lighting](/docs/en-us/environment/lighting.md).
2. In the **Explorer** window, select the **Lighting** service's child **Atmosphere** object, then in the **Properties** window, set its properties to values that reflect the art style of your game. For more information on these properties, see [Atmospheric effects](/docs/en-us/environment/atmosphere.md).
3. **OPTIONAL** Apply one or more customizable filters, such as bloom, depth‑of‑field, or sun rays. For more information on these properties, see [Post-processing effects](/docs/en-us/environment/post-processing-effects.md).

#### Recreate the sample

To exactly recreate the global lighting configuration within the sample [Environment Art - Constructing](https://www.roblox.com/games/14447826396/Environment-Art-Constructing) place file:

1. In the **Explorer** window, select the **Lighting** service, then in the **Properties** window,
  1. Set **Ambient** to `26, 34, 36`.
  2. Set **OutdoorAmbient** to `26, 34, 36`.
  3. Set **LightingStyle** to **Realistic**.
  4. Set **ShadowSoftness** to `0.15`.
  5. Set **GeographicLatitude** to `-18`.
  6. Set **TimeOfDay** to `-15:16:23`.
2. In the **Explorer** window, select the **Lighting** service's child **Atmosphere** object, then in the **Properties** window,
  1. Set **Density** to `0.285`.
  2. Set **Offset** to `0.65`.
  3. Set **Decay** to `254, 254, 254`
  4. Set **Glare** to `0.3`.
  5. Set **Haze** to `2`.
3. In the **Explorer** window, select the **Lighting** service's child **Bloom** object, then in the **Properties** window,
  1. Set **Intensity** to `1.5`.
  2. Set **Size** to `56`.
4. In the **Explorer** window, select the **Lighting** service's child **DepthOfField** object, then in the **Properties** window, set **FarIntensity** to `0.05`.

### Local lighting

Local lighting is the luminescence from local [light sources](/docs/en-us/effects/light-sources.md) in your game, such as `Class.SpotLight`, `Class.SurfaceLight`, and `Class.PointLight` objects. It's important to analyze the needs of your game to know which type of local light source to use. For example, the final sample laser tag environment needs lighting to help users see the different areas inside of the building while they're in combat, as well as lighting to differentiate the different spawn zone areas.

Local light sources create points of reference and directionality for users. For example, the sample uses surface lights to inform users if they are navigating the perimeter or are near the blue-green or pink spawn zone, and spotlights to highlight doorways.

> **Info:** Applying light sources is an art form, and it takes time to figure out what lighting configurations work to meet the needs of your game. It's normal and expected for your lighting to look and feel different from the final sample laser tag environment.

#### Create your own

To configure your own local lighting:

1. Add and configure glowing lights around the perimeter hallways that provide orientation cues to users navigating around the building.
  1. Add and position a **block** part near the top of one of your perimeter hallways, then in the **Properties** window,
    1. Set **Color** to a bright color.
    2. Set **Material** to **Neon**.
    3. Enable **Anchored**.
  2. In the **Explorer** window, add a **SurfaceLight** object to the part.
    1. Hover over the part and click the **⊕** button. A contextual menu displays.
    2. From the contextual menu, insert a **SurfaceLight** object.
  3. Select the **SurfaceLight** object, then in the **Properties** window,
    1. Set **Color** to a bright color.
    2. Set **Face** to the direction you want the light to shine.
    3. Set **Range** to a value that reflects how far you want your light to reach.
  4. Repeat this process, positioning and orienting parts to complete the glowing perimeter lights.
2. Add and configure small hallway interior lights that illuminate cross lanes.
  1. Add and position a **block** part near the top of one of your cross lane hallways, then in the **Properties** window,
    1. Set **Color** to a bright color.
    2. Set **Material** to **Neon**.
    3. Enable **Anchored**.
  2. In the **Explorer** window, add a **SpotLight** object to the part.
    1. Hover over the part and click the **⊕** button. A contextual menu displays.
    2. From the contextual menu, insert a **SpotLight** object.
  3. Select the **SpotLight** object, then in the **Properties** window,
    1. Set **Angle** to a value that reflects the angle you want your light to shine.
    2. Set **Face** to the direction you want the light to shine.
    3. Set **Range** to a value that reflects how far you want your light to reach.
  4. Repeat this process, positioning and orienting parts above doors and hallways until you are happy with the interior lighting.
3. Add and configure the spawn zone lights.
  1. Add a **block** part that is the size of your left spawn zone, and position it above the spawn zone's ceiling.
  2. In the **Properties** window,
    1. Set **Color** to the color theme of the team on the left of the map.
    2. Set **Material** to **Neon**.
    3. Enable **Anchored**.
  1. Repeat this process for the right spawn zone.
  1. **OPTIONAL** Add and anchor light fixtures around the interior and exterior of the building from your own asset library.

#### Recreate the sample

To exactly recreate the local lighting configuration within the sample [Environment Art - Constructing](https://www.roblox.com/games/14447826396/Environment-Art-Constructing) place file:

1. Add and configure the glowing perimeter lights.
  1. Add a **block** part for one of the glowing perimeter lights, then in the **Properties** window,
    1. Set **Color** to `199, 166, 147`.
    2. Set **Material** to **Neon**.
    3. Set **Size** to `89.254, 1, 1`.
    4. Set **CFrame.Position** to `-78.297, 21, 293.439`.
    5. Enable **Anchored**.
  2. In the **Explorer** window, add a **SurfaceLight** object to the part.
    1. Hover over the **block** part and click the **⊕** button. A contextual menu displays.
    2. From the contextual menu, insert a **SurfaceLight** object.
  3. Select the **SurfaceLight** object, then in the **Properties** window,
    1. Set **Color** to `211, 190, 150`.
    2. Set **Face** to **Bottom**.
    3. Set **Range** to `21`.
  4. Repeat this process, positioning and orienting parts to complete the glowing perimeter lights.
2. Add and configure the small hallway interior lights.
  1. Add a **block** part for one of the small hallway interior lights, then in the **Properties** window,
    1. Set **Color** to `163, 162, 165`.
    2. Set **Material** to **Neon**.
    3. Set **Size** to `0.25, 0.25, 1`.
    4. Set **CFrame.Position** to `-53.962, 19.936, 291.932`.
    5. Enable **Anchored**.
  2. In the **Explorer** window, add a **SpotLight** object to the part.
    1. Hover over the **block** part and click the **⊕** button. A contextual menu displays.
    2. From the contextual menu, insert a **SpotLight** object.
  3. Select the **SpotLight** object, then in the **Properties** window,
    1. Set **Angle** to `135`.
    2. Set **Face** to **Bottom**.
    3. Set **Range** to `20`.
  4. Repeat this process, positioning and orienting parts above doors and hallways until you are happy with the interior lighting.
3. Add and configure the spawn zone lights.
  1. Add a **block** part for the left spawn zone, then in the **Properties** window,
    1. Set **Color** to `88, 218, 171`.
    2. Set **Material** to **Neon**.
    3. Set **Size** to `62.5, 1, 37.5`.
    4. Set **CFrame.Position** to `-77, 20.6, 321`.
    5. Enable **Anchored**.
  1. Add a **block** part for the right spawn zone, then in the **Properties** window,
    1. Set **Color** to `255, 170, 255`.
    2. Set **Material** to **Neon**.
    3. Set **Size** to `62.5, 1, 37.5`.
    4. Set **CFrame.Position** to `-77, 20.6, 1`.
    5. Enable **Anchored**.
4. **OPTIONAL** Using the sample [Environment Art Asset Library](https://www.roblox.com/library/14447738661/Environment-Art-Asset-Library), add and anchor light fixtures around the interior and exterior of the building. For example, the final sample laser tag environment uses **LightFixtureTall**, **LightFixtureShort**, **TouchScreenA**, and **Roblox Sign** lighting fixtures to complete the environment.

Once you are happy with the look and feel of your environment, you can move on to configure your assets and Studio settings to keep your frame rate and performance levels high for low-end devices. This process ensures that nearly every user has the same gameplay and visual experience while they're viewing your environment.
