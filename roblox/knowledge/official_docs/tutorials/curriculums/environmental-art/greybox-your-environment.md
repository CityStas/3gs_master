---
title: "Greybox your environment"
url: /docs/en-us/tutorials/curriculums/environmental-art/greybox-your-environment
last_updated: 2026-10-30T19:55:59Z
description: "Explains how to greybox the laser tag environment using basic parts."
---

# Greybox your environment

**Greyboxing your environment**, also known as massing out or blocking your environment, is the process of adding simple shapes to the 3D space to figure out how users will experience gameplay before investing time into polishing assets. This process is crucial for finding issues in the layout of playable areas, such as difficult regions to traverse, unfair advantages from certain vantage points, or assets with disproportionate scale to the user's character.

Using the [Environment Art - Greyboxing](https://www.roblox.com/games/14447721254/Environment-Art-Greyboxing) `.rbxl` file as a reference, this section of the environmental art curriculum shows you how to greybox a standard three lane map layout for a team-based first-person laser tag shooter game, including step-by-step instructions on:

- Creating playable areas that encourage strategic combat for multiple playstyles.
- Applying placeholder materials that help inform users of their position and orientation.
- Testing the layout to ensure it's fun and doesn't include playability issues.

After you complete this section, you will learn how to develop high-quality assets to replace or convert the greybox environment, and meet your game's design requirements.

![An angled top-down view of the final greybox environment with placeholder materials to mark unique sections of the map.](../../../assets/tutorials/environmental-art-curriculum/Section1/PlaceholderMaterials.jpg) ## Three lane map layout

The **three lane map layout** is a first-person shooter map layout that includes a spawn zone for each team on opposite sides of the map, three primary lanes that each team can use to travel to either spawn zone, and cross lanes that allow for users to travel from one primary lane to another. This type of map layout is a common layout for first-person shooter games because it quickly places users into combat zones as soon as they join a match, and it allows for a variety of playstyles depending on which primary lane users choose to follow.

The following sections explain each component of the three lane map layout, including considerations of how each component works together to create intentional gameplay interactions within first-person shooter games.

### Spawn zones

**Spawn zones** are areas of the map where users either join their team at the start of a match, or rejoin the gameplay after their health reaches zero. At minimum, each team needs to have a central spawn zone when users first join the game. Many developers place these central spawn zones at opposite ends of their maps to allow users time to navigate the game at the start of the match before seeing the enemy team.

![A top-down view of the baseplate with each team's spawn zone highlighted on opposite sides of the map.](../../../assets/tutorials/environmental-art-curriculum/Section1/ThreeLaneLayout-SpawnZones.jpg)

In addition, many team-based first-person shooter games also include spawn zones throughout the map that users can randomly respawn at once their health reaches zero. The placement of these decentralized spawn zones can significantly increase the game's difficulty, especially when you place spawn zones near areas with heavy combat. To keep the gameplay simple, the sample laser tag greybox environment only includes one central spawn zone for each team.

### Primary lanes

**Primary lanes** are paths that extend the length of the map from one spawn zone to another. The three lane map layout includes three primary lanes, and how developers conceptualize them is often dependent on the overall environmental context of the game. For example, because the sample laser tag map has both an indoor and outdoor environment, the names of the primary lanes are as follows:

- **Interior** - The innermost lane that's furthest from the entrance of the building.
- **Middle** - The lane that's in-between the interior and exterior primary lanes.
- **Exterior** - The lane closest to the entrance of the building that's partially indoors and outdoors.

For most first-person shooter games using the three lane map layout, the middle primary lane intersects with areas of the map that contain the most combat because users traveling the middle primary lane can be attacked from both the interior or exterior primary lanes, while users traveling the interior or exterior primary lanes can only be attacked from the middle primary lane.

![A top-down view of the baseplate with three primary lanes highlighted between each team's spawn zone on opposite sides of the map.](../../../assets/tutorials/environmental-art-curriculum/Section1/ThreeLaneLayout-PrimaryLanes.jpg) ### Cross lanes

**Cross lanes** are paths that intersect all of the primary lanes, extending from the interior to the exterior primary lane. These are the paths that users can use to travel from one primary lane to another, and they often contain minimal obstructions to help users take cover from enemy fire. This is because coverless zones create transitory spaces that encourage users to not stay in one place for too long without it being dangerous.

![A top-down view of the baseplate with three primary lanes between each team's spawn zone on opposite sides of the map, as well as five cross lanes that intersect with the primary lanes.](../../../assets/tutorials/environmental-art-curriculum/Section1/ThreeLaneLayout-CrossLanes.jpg)

Similar to the reason why the most combat occurs around the middle primary lane, areas where cross lanes intersect with the middle primary lane, or **combat pockets**, contain the most combat because they allow users traveling from the interior or exterior lanes to access and shoot into the middle lane, and users traveling the middle lane can shoot in the direction of either the interior or exterior lane.

![A top-down view of the baseplate with three primary lanes between each team's spawn zone on opposite sides of the map, as well as five cross lanes that intersect with the primary lanes. The intersections between the primary and cross lanes are highlighted.](../../../assets/tutorials/environmental-art-curriculum/Section1/ThreeLaneLayout-IntersectingPoints.jpg)

Building a three lane map layout with these combat pockets in mind allows you to segment the distance from spawn zones, and create intentional spaces where users have to interact with each other. This encourages users to engage in rapid gameplay and quickly become familiar with the map as they jump between primary lanes using cross lanes.

## Create playable areas

Now that you are familiar with three lane map layouts, it's time to learn how to create the playable areas for the sample laser tag greybox environment that follows a three lane map layout. As you follow these instructions that exactly recreate the geometry within the sample [Environment Art - Greyboxing](https://www.roblox.com/games/14447721254/Environment-Art-Greyboxing) `.rbxl` file, you will start to see how it all works together to make up two spawn zones, three primary lanes, and five cross lanes that mirror across the middle of the map when you look at it from a top-down view.

![A top-down view of the final greybox geometry with three primary lanes between each team's spawn zone on opposite sides of the map, as well as five cross lanes that intersect with the primary lanes. The intersections between the primary and cross lanes are highlighted.](../../../assets/tutorials/environmental-art-curriculum/Section1/CreatingPlayableAreas-Intro1.jpg)
> **Info:** The following instructions provide two different instructional paths: you can either insert parts to represent your own unique laser tag environment, or you can insert parts in a way that exactly recreates the greybox environment within the sample [Environment Art - Greyboxing](https://www.roblox.com/games/14447721254/Environment-Art-Greyboxing) place file.

If you adjust the geometry to meet the specifications of your own game, note that the sample file keeps every doorway and hallway at least 10 studs wide, and every wall at least 10 studs tall. These parameters ensure that two users are able to pass through hallways and doorways concurrently, no one is able to jump over walls with Roblox's default jump height of 5 studs, and that the camera can safely maneuver the map without interfering with geometry.

![In a doorway, two lizard avatars are stacked on top of each other on the left, and two blocky avatars are stacked on top of each other on the right. This demonstrates that only two characters can pass each other in a doorway, and they cannot jump higher than the walls.](../../../assets/tutorials/environmental-art-curriculum/Section1/CreatingPlayableAreas-Intro2.png) ### Floor geometry

The first step in creating the laser tag greybox environment is to create the geometry for each of the following floors:

- **Main Floor** – Spans the length of one spawn zone to another.
- **Mezzanine Floor** – Spans half of the middle combat pocket, and provides a rise in elevation.
- **Outdoor Floor** – Spans the outdoor space, and provides a drop in elevation.

To help visualize the geometry of each floor you are creating for the game, reference the following image that marks the main floor in yellow, the mezzanine floor in red, and the outdoor floor in blue.

![A top-down view of the final greybox environment with placeholder materials to mark the main, mezzanine, and outdoor floors.](../../../assets/tutorials/environmental-art-curriculum/Section1/Floor-Intro.jpg)

It's important to have spaces in the game with peaks and valleys because it allows you to control sight lines and engagement distances throughout the game outside of horizontal movement. For example, if the entire playable space was a single floor with no change in elevation, every user would be able to interact with each other as long as there wasn't a wall in the way, meaning there is little ability for the user to develop a strategy outside of not being seen from other users. However, with peaks and valleys, you can decide where users can see each other.

In addition, a rise in elevation creates both a physical and emotional sense of ascension, allowing users with a high ground to have a bird's eye view of the battlefield in order to get a better sense of where to travel next. When they're ready to move on, the drop in elevation creates both a physical and emotional sense of descension, pushing users to make quick decisions to maneuver around enemy lines of sight and achieve their goals.

#### Create your own

To create your own floor geometry:

1. Open Roblox Studio with a **Baseplate** template.
2. Navigate to Studio's **Home** or **Model** tab toolbar, then set [transform snapping](/docs/en-us/parts.md#transform-parts) to **5 studs** and **90°**. This allows you to equally position all greybox geometry on or away from each other in 5 stud increments.
3. Using **block** parts, create symmetrical left and right surfaces for the **main floor** of your building. This geometry represents the length of your playable interior, and its symmetry denotes the center of the map.![An angled top-down view of the main floor greybox geometry highlighted in yellow.](../../../assets/tutorials/environmental-art-curriculum/Section1/GeneralFloor-1.jpg)
4. Using **block** parts, create symmetrical left and right surfaces for the **mezzanine floor** of your building. This geometry represents the highest ground on the map.![An angled top-down view of both the main and mezzanine floors. The mezzanine floor greybox geometry is highlighted in yellow.](../../../assets/tutorials/environmental-art-curriculum/Section1/Floor-3.jpg)
5. Using **wedge** parts, create a **rise in elevation** between the main and mezzanine floors. This geometry breaks the lines of sight for players traveling the interior primary lane, or the cross lane in the middle of the map.![An angled top-down view of both the main, mezzanine floor, and rise in elevation parts. The rise in elevation greybox geometry is highlighted in yellow.](../../../assets/tutorials/environmental-art-curriculum/Section1/Floor-4.jpg)
6. Using **wedge** parts, create a **drop in elevation** between the main and outdoor floor. This geometry is your exterior primary lane, and it descends to the lowest point on the map.![An angled top-down view of both the main, mezzanine floor, and rise and drop in elevation parts. The drop in elevation greybox geometry is highlighted in yellow.](../../../assets/tutorials/environmental-art-curriculum/Section1/Floor-5.jpg)
7. Anchor all of your parts.

#### Recreate the sample

To exactly recreate the floor geometry within the sample [Environment Art - Greyboxing](https://www.roblox.com/games/14447721254/Environment-Art-Greyboxing) place file:

1. Open Roblox Studio with a **Baseplate** template.
2. Navigate to Studio's **Home** or **Model** tab toolbar, then set [transform snapping](/docs/en-us/parts.md#transform-parts) to **5 studs** and **90°**. This allows you to equally position all greybox geometry on or away from each other in 5 stud increments.
3. Add and configure a **block** part for the left-side surface of the **main floor**. You can use this same process for each step as you create all of the playable areas.
  1. In the **Explorer** window, select the block, then in the **Properties** window,
    1. Set **Size** to `105, 1, 185`.
    2. Set **CFrame.Position** to `-77.5, 4.5, 252.5`.![An angled top-down view of the left-side of the main floor greybox geometry highlighted in yellow.](../../../assets/tutorials/environmental-art-curriculum/Section1/Floor-1.jpg)
4. Add and configure the following **block** parts for the **main floor**: | Part | Size | CFrame.Position |
| --- | --- | --- | | Right-side floor | `105, 1, 185` | `-77.5, 4.5, 67.5` | | Middle left-side floor | `20, 10, 50` | `-15, 0, 185` | | Middle right-side floor | `20, 10, 50` | `-15, 0, 135` |![An angled top-down view of the main floor geometry. The right-side and middle portion of the main floor greybox geometry is highlighted in yellow.](../../../assets/tutorials/environmental-art-curriculum/Section1/Floor-2.jpg)
5. Add and configure the following **block** parts for the **mezzanine floor**: | Part | Size | CFrame.Position |
| --- | --- | --- | | Left-side floor | `70, 5, 35` | `-110, 7.5, 177.5` | | Right-side floor | `70, 5, 35` | `-110, 7.5, 142.5` | | Left-side ledge | `10, 5, 10` | `-70, 7.5, 165` | | Right-side ledge | `10, 5, 10` | `-70, 7.5, 155` | | Ledge wall | `1, 3, 20` | `-65.5, 11.5, 160` |![An angled top-down view of both the main and mezzanine floors. The mezzanine floor greybox geometry is highlighted in yellow.](../../../assets/tutorials/environmental-art-curriculum/Section1/Floor-3.jpg)
6. Add and configure the following **wedge** parts for the **rise in elevation** between the main and mezzanine floor: | Part | Size | CFrame.Position | CFrame.Orientation |
| --- | --- | --- | --- | | Left-side elevation | `15, 5, 10` | `-102.5, 7.5, 200` | `0, 180, 0` | | Right-side elevation | `15, 5, 10` | `-102.5, 7.5, 120` | `0, 0, 0` | | Middle left-side elevation | `15, 5, 10` | `-70, 7.5, 177.5` | `0, -90, 0` | | Middle right-side elevation | `15, 5, 10` | `-70, 7.5, 142.5` | `0, -90, 0` |![An angled top-down view of both the main, mezzanine floor, and rise in elevation parts. The rise in elevation greybox geometry is highlighted in yellow.](../../../assets/tutorials/environmental-art-curriculum/Section1/Floor-4.jpg)
7. Add and configure the following **wedge** part for the **drop in elevation** between the main and outdoor floor with a **Size** of `270, 11, 45`, **CFrame.Position** of `-2.5, -0.5, 160`, and a **CFrame.Orientation** of `0, -90, 0`.![An angled top-down view of both the main, mezzanine floor, and rise and drop in elevation parts. The drop in elevation greybox geometry is highlighted in yellow.](../../../assets/tutorials/environmental-art-curriculum/Section1/Floor-5.jpg)
8. Anchor all of these floor parts.

### Perimeter wall geometry

The second step in creating the laser tag greybox environment is to create the geometry for perimeter walls of the building. This provides boundaries for the interior gameplay of the game, as well as guidance to users on where they can go to engage with one another.

To help visualize the geometry of the perimeter walls of the building you are creating for the game, reference the following image that marks them in yellow.

![A top-down view of the final greybox environment with the perimeter wall geometry highlighted in yellow.](../../../assets/tutorials/environmental-art-curriculum/Section1/Perimeter-Intro.jpg)

#### Create your own

To create your own perimeter wall geometry:

1. Using **block** parts, create a **perimeter boundary** around your main floor except for the edge that opens to the exterior primary lane. This geometry prevents players from leaving your playable area while allowing them to enter and exit the building.![An angled top-down view of the floor and perimeter walls. The perimeter wall geometry is highlighted in yellow.](../../../assets/tutorials/environmental-art-curriculum/Section1/GeneralPerimeter-1.jpg)
2. Anchor these parts.

#### Recreate the sample

To exactly recreate the perimeter wall geometry within the sample [Environment Art - Greyboxing](https://www.roblox.com/games/14447721254/Environment-Art-Greyboxing) place file:

1. Add and configure the following **block** parts for the **top** perimeter walls: | Part | Size | CFrame.Position |
| --- | --- | --- | | Top-left wall | `30, 30, 185` | `-140, 20, 282.5` | | Top-middle wall | `10, 30, 60` | `-150, 20, 160` | | Top-right wall | `30, 30, 185` | `-140, 20, 37.5` |![An angled top-down view of the floor and top perimeter walls. The top perimeter wall geometry is highlighted in yellow.](../../../assets/tutorials/environmental-art-curriculum/Section1/Perimeter-1.jpg)
2. Add and configure the following **block** parts for the **side** perimeter walls: | Part | Size | CFrame.Position |
| --- | --- | --- | | Left wall | `105, 30, 35` | `-72.5, 20, 357.5` | | Right wall | `105, 30, 35` | `-72.5, 20, -37.5` |![An angled top-down view of the floor, top perimeter walls, and side perimeter walls. The side perimeter wall geometry is highlighted in yellow.](../../../assets/tutorials/environmental-art-curriculum/Section1/Perimeter-2.jpg)
3. Add and configure the following **block** parts for the **bottom left** perimeter walls: | Part | Size | CFrame.Position |
| --- | --- | --- | | Left wall | `20, 20, 40` | `-34, 15, 320` | | Middle wall | `12, 45, 15` | `-29, 24.5, 297.5` | | Right wall | `5, 35, 5` | `-27.5, 19.5, 287.5` |![An angled top-down view of the floor, top perimeter walls, side perimeter walls, and bottom-left perimeter walls. The bottom-left perimeter wall geometry is highlighted in yellow.](../../../assets/tutorials/environmental-art-curriculum/Section1/Perimeter-3.jpg)
4. Add and configure the following **block** parts for the **bottom right** perimeter walls: | Part | Size | CFrame.Position |
| --- | --- | --- | | Left wall | `5, 35, 5` | `-27.5, 19.5, 32.5` | | Middle wall | `12, 45, 15` | `-29, 24.5, 22.5` | | Right wall | `20, 20, 40` | `-35, 15, 0` |![An angled top-down view of the floor, top perimeter walls, side perimeter walls, bottom perimeter walls. The bottom-right perimeter wall geometry is highlighted in yellow.](../../../assets/tutorials/environmental-art-curriculum/Section1/Perimeter-4.jpg)
5. Anchor all of these perimeter wall parts.

### Spawn zone geometry

The third step in creating the laser tag greybox environment is to create the geometry to contain each team's spawn zone. For games that only contain centralized spawn zones, sectioning them off into their own rooms lets users acclimate to the game when they first join the match, and it provides them cover from enemy fire when they rejoin the match after their health reaches zero.

There are two spawn zones in the [Environment Art - Greyboxing](https://www.roblox.com/games/14447721254/Environment-Art-Greyboxing) `.rbxl` file, one for each team a user can join, and they're located at opposite ends of the map. Each spawn zone has two exit points users can choose to enter the main gameplay area, which allows for quick access to two primary lanes, and provides cover from enemy fire from users within the cross lane near the spawn zone. Having two exit points is important because a single exit point would result in a bottleneck of users trying to enter or exit the spawn zone, and three spawn zones wouldn't provide enough cover from enemy fire after the start of the match.

![An angled top-down view of a spawn zone with arrows pointing toward the two exit points and all paths users can take away from the spawn zone.](../../../assets/tutorials/environmental-art-curriculum/Section1/SpawnZone-ExitPoints.jpg)

To help visualize the geometry of the spawn zone areas you are creating for the game, reference the following image that marks them in yellow.

![A top-down view of the final greybox environment with the spawn zone wall geometry highlighted in yellow.](../../../assets/tutorials/environmental-art-curriculum/Section1/SpawnZone-Intro.jpg)

#### Create your own

To create your own spawn zone geometry:

1. Using **block** parts, segment symmetrical sections on the far left and right of the map for each team's **spawn zon**e with two exit points.![An angled top-down view of the floor, perimeter, and spawn zone walls. The spawn zone wall geometry is highlighted in yellow.](../../../assets/tutorials/environmental-art-curriculum/Section1/GeneralSpawnZone-1.jpg)
2. Anchor these parts.

#### Recreate the Sample

To exactly recreate the spawn zone geometry within the sample [Environment Art - Greyboxing](https://www.roblox.com/games/14447721254/Environment-Art-Greyboxing) place file:

1. Add and configure the following **block** parts for the additional **spawn zone walls**: | Part | Size | CFrame.Position |
| --- | --- | --- | | Left spawn zone wall | `15, 15, 45` | `-117.5, 12.5, 317.5` | | Right spawn zone wall | `15, 15, 45` | `-117.5, 12.5, 2.5` |![An angled top-down view of the floor, perimeter, and top spawn zone walls. The top spawn zone wall geometry is highlighted in yellow.](../../../assets/tutorials/environmental-art-curriculum/Section1/SpawnZone-1.jpg)
2. Add and configure the following **block** parts for the left spawn zone's **doorways**: | Part | Size | CFrame.Position |
| --- | --- | --- | | Left spawn, top wall | `10, 15, 5` | `-105, 12.5, 297.5` | | Left spawn, top door | `10, 5, 5` | `-95, 17.5, 297.5` | | Left spawn, middle wall | `25, 15, 5` | `-77.5, 12.5, 297.5` | | Left spawn, bottom door | `10, 5, 5` | `-60, 17.5, 297.5` | | Left spawn, bottom wall | `20, 15, 5` | `-45, 12.5, 297.5` |![An angled top-down view of the floor, perimeter, top spawn zone walls, and left spawn zone walls. The left spawn zone wall geometry is highlighted in yellow.](../../../assets/tutorials/environmental-art-curriculum/Section1/SpawnZone-2.jpg)
3. Add and configure the following **block** parts for the right spawn zone's **doorways**: | Part | Size | CFrame.Position |
| --- | --- | --- | | Right spawn top wall | `10, 15, 5` | `-105, 12.5, 22.5` | | Right spawn, top door | `10, 5, 5` | `-95, 17.5, 22.5` | | Right spawn, middle wall | `25, 15, 5` | `-77.5, 12.5, 22.5` | | Right spawn, bottom door | `10, 5, 5` | `-60, 17.5, 22.5` | | Right spawn, bottom wall | `20, 15, 5` | `-45, 12.5, 22.5` |![An angled top-down view of the floor, perimeter, all spawn zone walls. The right spawn zone wall geometry is highlighted in yellow.](../../../assets/tutorials/environmental-art-curriculum/Section1/SpawnZone-3.jpg)
4. Anchor all of these spawn zone parts.

### Combat pockets geometry

The fourth step in creating the laser tag greybox environment is to create the geometry for combat pockets in the interior of the building. This geometry makes up the majority of the playable areas in the game because combat pockets arise from the intersections of primary lane and cross lanes, which span the entirety of the building.

The instructions in this section refer to this geometry as three separate combat pockets according to their location on a top-view of the map: the left combat pocket, the middle combat pocket, and the right combat pocket. Most combat pockets include a maximum of three entrance or exit points to refrain from giving users choice overload as they're navigating the space.

![A top-down view of the final greybox environment with the left, middle, and right combat pockets highlighted.](../../../assets/tutorials/environmental-art-curriculum/Section1/CombatPockets-Intro1.jpg)

To help visualize geometry of the combat pockets you are creating for the game, reference the following image that marks them in yellow.

![A top-down view of the final greybox environment with the combat pocket geometry highlighted in yellow.](../../../assets/tutorials/environmental-art-curriculum/Section1/CombatPockets-Intro2.jpg)

#### Create your own

To create your own combat pockets geometry:

1. Using **block** parts, create a **left combat pocket** with two exit points that allow players to traverse the middle lane, and one exit point that opens to the interior primary lane. This geometry must have space on either side of the combat pocket to allow for cross lanes, and block player entry from the exterior primary lane.![An angled top-down view of the floor, perimeter, spawn zone walls, and left combat pocket. The left combat pocket geometry is highlighted in yellow.](../../../assets/tutorials/environmental-art-curriculum/Section1/CombatPockets-1.jpg)
2. Using **block** parts, create and position a symmetrical copy of this combat pocket near the other team's spawn zone. This geometry represents your **right combat pocket**.![An angled top-down view of the floor, perimeter, spawn zone walls, left combat pocket, and right combat pocket. The right combat pocket geometry is highlighted in yellow.](../../../assets/tutorials/environmental-art-curriculum/Section1/GeneralCombatPockets-2.jpg)
3. Using **block** parts, create a **middle combat pocket** with two exit points that allow players to traverse the middle lane, one exit point that opens to the interior primary lane, and open space along the edge that flows into the exterior primary lane.![An angled top-down view of the floor, perimeter, spawn zone walls, left combat pocket, middle combat pocket, and right combat pocket. The middle combat pocket geometry is highlighted in yellow.](../../../assets/tutorials/environmental-art-curriculum/Section1/GeneralCombatPockets-3.jpg)
4. **OPTIONAL** Using **block** parts, create **hallway additions** to the middle combat pocket to break up sight lines across the interior primary lane.![An angled top-down view of the floor, perimeter, spawn zone walls, left combat pocket, middle combat pocket, right combat pocket, and hallway addition walls. The hallway addition geometry is highlighted in yellow.](../../../assets/tutorials/environmental-art-curriculum/Section1/GeneralCombatPockets-4.jpg)
5. Anchor these parts.

#### Recreate the sample

To exactly recreate the combat pockets geometry within the sample [Environment Art - Greyboxing](https://www.roblox.com/games/14447721254/Environment-Art-Greyboxing) place file:

1. Add and configure the following **block** parts for the **left combat pocket**. | Part | Size | CFrame.Position |
| --- | --- | --- | | Top hallway extension | `10, 15, 15` | `-100, 12.5, 272.5` | | Top doorway, left wall | `5, 15, 15` | `-92.5, 12.5, 262.5` | | Top doorway, overhang | `5, 5, 10` | `-92.5, 17.5, 250` | | Top doorway, right wall | `5, 15, 20` | `-92.5, 12.5, 235` | | Left doorway, top wall | `20, 15, 5` | `-85, 12.5, 272.5` | | Left doorway, overhang | `10, 5, 5` | `-70, 17.5, 272.5` | | Left doorway, bottom wall | `20, 15, 5` | `-55, 12.5, 272.5` | | Right doorway, top wall | `15, 15, 10` | `-82.5, 12.5, 230` | | Right doorway, overhang | `10, 5, 10` | `-70, 17.5, 230` | | Right doorway, bottom wall | `20, 15, 10` | `-55, 12.5, 230` | | Bottom wall | `10, 15, 35` | `-50, 12.5, 252.5` |![An angled top-down view of the floor, perimeter, spawn zone walls, and left combat pocket. The left combat pocket geometry is highlighted in yellow.](../../../assets/tutorials/environmental-art-curriculum/Section1/CombatPockets-1.jpg)
2. Add and configure the following **block** parts for the **top hallway addition** to the middle combat pocket that breaks up sight lines across the interior primary lane: | Part | Size | CFrame.Position |
| --- | --- | --- | | Left hallway extension | `15, 20, 45` | `-117.5, 15, 212.5` | | Right hallway extension | `15, 20, 45` | `-117.5, 15, 107.5` | | Left hallway | `5, 20, 45` | `-92.5, 15, 187.5` | | Right hallway | `5, 20, 45` | `-92.5, 15, 132.5` | | Top hallway entrance, left wall | `15, 15, 5` | `-102.5, 17.5, 172.5` | | Top hallway entrance, left wall on entrance | `5, 15, 10` | `-112.5, 17.5, 170` | | Top hallway entrance, right wall | `15, 15, 5` | `-102.5, 17.5, 147.5` | | Top hallway entrance, right wall on entrance | `5, 15, 10` | `-112.5, 17.5, 150` | | Door overhang | `5, 5, 10` | `-92.5, 22.5, 160` |![An angled top-down view of the floor, perimeter, spawn zone walls, left combat pocket, and top hallway addition walls. The top hallway addition wall geometry is highlighted in yellow.](../../../assets/tutorials/environmental-art-curriculum/Section1/CombatPockets-2.jpg)
3. Add and configure the following **block** parts for the **middle room** of the middle combat pocket: | Part | Size | CFrame.Position |
| --- | --- | --- | | Left wall that extends into the hallway | `10, 20, 25` | `-85, 15, 197.5` | | Right wall that extends into the hallway | `10, 20, 25` | `-85, 15, 122.5` | | Left doorway, top wall | `25, 20, 15` | `-67.5, 15, 192.5` | | Left doorway, overhang | `10, 10, 15` | `-50, 20, 192.5` | | Left doorway, bottom wall | `5, 20, 15` | `-42.5, 15, 192.5` | | Right doorway, top wall | `25, 20, 15` | `-67.5, 15, 127.5` | | Right doorway, overhang | `10, 10, 15` | `-50, 20, 127.5` | | Right doorway, bottom wall | `5, 20, 15` | `-42.5, 15, 127.5` |![An angled top-down view of the floor, perimeter, spawn zone walls, left combat pocket, top hallway addition walls, and the middle room of the middle combat pocket. The middle room of the middle combat pocket geometry is highlighted in yellow.](../../../assets/tutorials/environmental-art-curriculum/Section1/CombatPockets-3.jpg)
4. Add and configure the following **block** parts for the **right combat pocket**: | Part | Size | CFrame.Position |
| --- | --- | --- | | Top hallway extension | `10, 15, 15` | `-100, 12.5, 47.5` | | Top doorway, left wall | `5, 15, 20` | `-92.5, 12.5, 85` | | Top doorway, overhang | `5, 5, 10` | `-92.5, 17.5, 70` | | Top doorway, right wall | `5, 15, 15` | `-92.5, 12.5, 57.5` | | Left doorway, top wall | `15, 15, 10` | `-82.5, 12.5, 90` | | Left doorway, overhang | `10, 5, 10` | `-70, 17.5, 90` | | Left doorway, bottom wall | `20, 15, 10` | `-55, 12.5, 90` | | Right doorway, top wall | `20, 15, 5` | `-85, 12.5, 47.5` | | Right doorway, overhang | `10, 5, 5` | `-70, 17.5, 47.5` | | Right doorway, bottom wall | `20, 15, 5` | `-55, 12.5, 47.5` | | Bottom wall | `10, 15, 35` | `-50, 12.5, 67.5` |![An angled top-down view of the floor, perimeter, spawn zone walls, left combat pocket, top hallway addition walls, middle combat pocket, and right combat pocket. The right combat pocket geometry is highlighted in yellow.](../../../assets/tutorials/environmental-art-curriculum/Section1/CombatPockets-4.jpg)
5. Anchor all of these combat pocket parts.

### Exterior geometry

The final step in creating the laser tag greybox environment is to create the placeholder exterior assets that create interesting composition for the outdoor space, as well as minimal cover for users traveling the exterior primary lane. This area of the game is important because while it comes with risk due to the minimal cover from enemy fire, it also provides users a quick route to the enemy team's spawn zone.

To help visualize the geometry of the exterior assets you are creating for the game, reference the following image that marks them in yellow.

![A top-down view of the final greybox environment with the exterior geometry highlighted in yellow.](../../../assets/tutorials/environmental-art-curriculum/Section1/Exterior-Intro.jpg)

#### Create your own

To create your own exterior geometry:

1. Using **block** parts, create symmetrical **obstacles** along the exterior primary lane. For example, the sample greybox environment adds parts to block lines of sight that will later become towers, pillars, and planters.![An angled top-down view of the floor, perimeter, spawn zone walls, combat pockets, and exterior geometry. The exterior geometry is highlighted in yellow.](../../../assets/tutorials/environmental-art-curriculum/Section1/GeneralExterior-1.jpg)
2. Anchor these parts.

#### Recreate the sample

To exactly recreate the exterior geometry within the sample [Environment Art - Greyboxing](https://www.roblox.com/games/14447721254/Environment-Art-Greyboxing) place file:

1. Add and configure the following **block** parts for the **left tower**: | Part | Size | CFrame.Position |
| --- | --- | --- | | Left wall | `15, 25, 5` | `-32.5, 22.5, 192.5` | | Right wall | `15, 40, 10` | `-32.5, 30, 185` | | Bottom ledge | `20, 5, 15` | `-30, 7.5, 187.5` |![An angled top-down view of the floor, perimeter, spawn zone walls, combat pockets, and left tower geometry. The left tower geometry is highlighted in yellow.](../../../assets/tutorials/environmental-art-curriculum/Section1/Exterior-1.jpg)
2. Add and configure the following **block** parts for the **right tower**: | Part | Size | CFrame.Position |
| --- | --- | --- | | Left wall | `15, 40, 10` | `-32.5, 30, 135` | | Right wall | `15, 25, 5` | `-32.5, 22.5, 127.5` | | Bottom ledge | `20, 5, 15` | `-30, 7.5, 132.5` |![An angled top-down view of the floor, perimeter, spawn zone walls, combat pockets, left tower, and right tower geometry. The right tower geometry is highlighted in yellow.](../../../assets/tutorials/environmental-art-curriculum/Section1/Exterior-2.jpg)
3. Add and configure the following **block** parts for the **obstacles** to the left of the towers: | Part | Size | CFrame.Position |
| --- | --- | --- | | Left obstacle | `20, 10, 5` | `-15, 5, 262.5` | | Middle obstacle | `15, 30, 5` | `-22.5, 15, 237.5` | | Right obstacle | `10, 10, 15` | `-5, 5, 202.5` |![An angled top-down view of the floor, perimeter, spawn zone walls, combat pockets, left tower, right tower, and obstacle geometry to the left of the left tower. The obstacle geometry to the left of the left tower are highlighted in yellow.](../../../assets/tutorials/environmental-art-curriculum/Section1/Exterior-3.jpg)
4. Add and configure the following **block** parts for the **obstacles** to the right of the towers: | Part | Size | CFrame.Position |
| --- | --- | --- | | Left obstacle | `10, 10, 15` | `-5, 5, 117.5` | | Middle obstacle | `15, 30, 5` | `-22.5, 15, 82.5` | | Right obstacle | `20, 10, 5` | `-15, 5, 57.5` |![An angled top-down view of the floor, perimeter, spawn zone walls, combat pockets, left tower, right tower, and obstacle geometry to the left and right of the towers. The obstacle geometry to the right of the right tower are highlighted in yellow.](../../../assets/tutorials/environmental-art-curriculum/Section1/Exterior-4.jpg)
5. Add and configure the following **block** parts for the **obstacles** between the towers: | Part | Size | CFrame.Position |
| --- | --- | --- | | Top obstacle | `10, 5, 5` | `-50, 7.5, 160` | | Middle obstacle | `20, 10, 10` | `-35, 10, 160` | | Bottom obstacle | `10, 10, 30` | `0, 5, 160` |![An angled top-down view of the floor, perimeter, spawn zone walls, combat pockets, left tower, right tower, and obstacle geometry. The obstacle geometry between the towers are highlighted in yellow.](../../../assets/tutorials/environmental-art-curriculum/Section1/Exterior-5.jpg)
6. Anchor all of these tower parts.

## Apply placeholder materials

Now that you have your placeholder geometry in place, it's time to apply placeholder materials to the map in key areas to help orient users to where they are in the game. The sample [Environment Art - Greyboxing](https://www.roblox.com/games/14447721254/Environment-Art-Greyboxing) `.rbxl` file uses the following color map, but you can use can use any color to achieve the same purpose:

- **Deep Orange for top perimeter walls** – Informs users where they are in relation to the back of the building.
- **Persimmon for all left-side floors** – Informs users where they are in relation to the right-side of the building.
- **Lapis for all right-side floors** – Informs users where they are in relation to the left-side of the building.
- **Bright Green for the exterior elevation** – Informs users where they are in relation to outside of the building.

Applying materials to these specific key areas is important because no matter where a user is in the game, as long as they can see at least one of these colors, they can quickly deduce their approximate location within the overall map, as well as where they are in relation to a spawn zone.

For example, if the following user is on the "red" team, when they're walking on the red floor with the yellow wall to their right, they know that they're in the interior primary lane and moving toward their spawn zone. Conversely, if they're walking on the lapis floor with the yellow wall to their left, they know they're in the interior lane and moving toward the enemy team's spawn zone.

![A Rthro avatar standing on a red floor with a yellow wall to their right. This color configuration informs the user that they're in the interior primary lane and moving toward the red spawn zone.](../../../assets/tutorials/environmental-art-curriculum/Section1/Placeholder-Left.jpg)

![A Rthro avatar standing on a blue floor with a yellow wall to their left. This color configuration informs the user that they're in the interior primary lane and moving toward the blue spawn zone.](../../../assets/tutorials/environmental-art-curriculum/Section1/Placeholder-Right.jpg)

To apply placeholder materials:

1. Select the top perimeter walls and the top hallway editions, then set their `Class.Part.Color` to `255, 176, 0`.
2. Select the left-side floor parts, then set their `Class.Part.Color` to `255, 89, 89`.
3. Select the right-side floor parts, then set their `Class.Part.Color` to `16, 42, 220`.
4. Select the part for the elevation between the ground and first floor, then set their `Class.Part.Color` to `75, 151, 75`.

![An angled top-down view of the final greybox environment with placeholder materials to mark unique sections of the map.](../../../assets/tutorials/environmental-art-curriculum/Section1/PlaceholderMaterials.jpg) ## Playtest your layout

It's important to continuously playtest the layout of your environment **at nearly every step of the development process** so you can ensure the game is both fun and functional, and you can catch small issues before they turn into much larger problems the further you are in the process. As you playtest, ask yourself the following questions:

- Are there advantages or disadvantages to either team?
- Are users able to successfully orient themselves and understand their location at any point on the map?
- Are there any areas on the map that overwhelm users with too many choices?
- What am I enjoying or getting frustrated about the layout or gameplay?
- Will this make users feel the way I want them to when they're in this area?
- Is there any part of the map that I can bypass and still achieve my goals?

To playtest, select one of the following simulation modes from the mezzanine's dropdown menu and click the **Play** button to begin.

![Test option in the testing modes dropdown of Studio's mezzanine.](../../../assets/studio/general/Mezzanine-Testing-Mode-Test.png)

| Mode | Shortcut | Description |
| --- | --- | --- |
| **Test** | `F5` | Starts simulating the game, inserting your avatar at either a `Class.SpawnLocation` or coordinates of around`(0, 100, 0)`. |
| **Test Here** |  | Starts simulating the game, inserting your avatar in front of the camera's current position. |
| **Run** | `F8` | Starts simulating the game but does not insert your avatar. The simulation begins at the current camera position and you can navigate around using the Studio camera controls. |

While playtesting, you can use the same controls as a default Roblox game. Once you are happy with the overall layout of your game, you can move on to creating polishing assets that will replace the greybox geometry in accordance with your art style.
