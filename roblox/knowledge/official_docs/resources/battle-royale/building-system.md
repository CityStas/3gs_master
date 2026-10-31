---
title: "Building system"
url: /docs/en-us/resources/battle-royale/building-system
last_updated: 2026-10-30T19:55:54Z
description: "Explains the process of creating a building system in the Battle Royale kit."
---

# Building system

Roblox Battle Royale features a building system that lets users build their own structures to reach higher ground for a better shooting angle, or to provide cover during battle. Using a menu, the user can select from a number of different tile types and place them in the world.

![Building Example](../../assets/resources/battle-royale/building-system/Battle-Royale-Building-View.jpeg)

To maintain an orderly and structured system:

- Each tile must connect to another existing tile or to the ground.
- Place all building tiles within a grid coordinated with the 3D world so that tiles connect properly and do not overlap.

## Tile composition

In order for users to build new tiles quickly and easily, the building system needs to understand which tiles are connected to each other and where new tiles can be placed on the grid.

Tiles use 3 components: the [visual asset](#asset) that is used as the tile object, information about the [space the tile occupies](#occupancy) in reference to other world objects, and the [connection points](#connectivity) of a tile which allow additional tiles to connect to available edges.

### Asset

An asset is a `Class.BasePart` (`Class.Part`, `Class.MeshPart`, etc.) placed in `ReplicatedStorage/BuildingSystem/Assets` representing what the tile looks like in the 3D world. This `Class.BasePart` must have two children:

- **ObjectType** — A `Class.StringValue` with a `Value` of the tile type name.
- **StartingRotation** — A `Class.NumberValue` with a `Value` of the tile's starting rotation when a user places it in the world.

### Occupancy

Ensuring that a tile occupies the correct location in a grid system is important and can be done using a bitmask. A bitmask represents the physical space the tile type takes up within a basic section of world space, or cell. Each building system tile/object can occupy any number of faces of a grid cell (front, left, back, right, top, and bottom) and any number of octants in a grid cell. A user can only place a building system object in a cell if all the faces and octants that the object occupies are available in that cell. Occupancy for a building system object is defined as follows:

| Bit index | Meaning |
| --- | --- |
| 0 | Bottom face of cell |
| 1 | Top face of cell |
| 2 | Right face of cell |
| 3 | Back face of cell |
| 4 | Left face of cell |
| 5 | Front face of cell |
| 6 | **+X, –Y, +Z** octant of cell with origin at center of cell |
| 7 | **+X, +Y, +Z** octant of cell with origin at center of cell |
| 8 | **–X, –Y, +Z** octant of cell with origin at center of cell |
| 9 | **–X, +Y, +Z** octant of cell with origin at center of cell |
| 10 | **–X, –Y, –Z** octant of cell with origin at center of cell |
| 11 | **–X, +Y, –Z** octant of cell with origin at center of cell |
| 12 | **+X, –Y, –Z** octant of cell with origin at center of cell |
| 13 | **+X, +Y, –Z** octant of cell with origin at center of cell |

### Connectivity

Tiles need to connect to each other to create a structure. You can use a bitmask which represents what portions of the cell's faces/edges the tile type touches. A building system tile/object's connectivity is represented by a series of connection points, bits, on the surface of a cell. They arrange in the following way on the faces of the cell:

![Octant Cube Diagram](../../assets/resources/battle-royale/building-system/Octant-Cube.png)

A building system object is considered connected to another building system object in the grid if they share at least 2 connectivity points on the surface of a cell.

## Create new tile types

To create a new tile type:

1. Place the asset in `ReplicatedStorage/BuildingSystem/Assets`. Remember that it must contain `ObjectType` and `StartingRotation` children as defined above.![Battle Royale Weapon Example](../../assets/resources/battle-royale/building-system/Battle-Royale-New-Tile-1.png)
2. Define the [Occupancy](#occupancy) and [Connectivity](#connectivity) for your new tile type in `ReplicatedStorage/BuildingSystem/Libraries/Grid/ObjectTypeConfigurations`:![Battle Royale Weapon Example](../../assets/resources/battle-royale/building-system/Battle-Royale-New-Tile-2.png)

For example, the **Wall** tile type is expressed as follows:

```lua
ObjectTypeConfigurations.Wall = {
	ASSET_OFFSET_FROM_CENTER = Vector3.new(0, 0, -CELL_DIMENSIONS.Z / 2),
	CONNECTIVITY = 0xFF8000, -- 0b 111 111 111 000 000 000 000 000
	OCCUPANCY = 0x20, -- 0b 00 00 00 00 1 0 0 0 0 0
}
```

## Work with terrain

If you would like to create a map with free-form [terrain](/docs/en-us/parts/terrain.md) that lines up perfectly with the building system, we recommend that you use the **heightmap import** system as outlined in [Environmental Terrain](/docs/en-us/parts/terrain.md) and that you observe the following details:

- Terrain in Roblox is represented by a three dimensional array of voxels, each of which occupies a cube of 4×4×4 studs in the world. Because of this, Roblox Battle Royale uses a grid cell size of 20×16×20 studs, with wall tiles that are 20×16×1 studs and floor/ceiling tiles that are 20×1×20 studs in size. This allows building tiles and terrain to line up properly.
- Each pixel in your heightmap image should represent one terrain voxel in the **X/Z** plane, so a 5×5 area in pixels represents one building system grid cell that occupies a 20×20 stud area.
- In your heightmap image, make sure the red channel or grey channel value for each pixel is divisible by the height of your building system grid cell so that the floor tiles sit nicely on top of the terrain.
- When you import your heightmap, set:```lua
Position (X, Y, Z) = 0, 0, 0
Size (X, Y, Z) = heightmap_width × 4, 256, heightmap_length × 4
```
