---
name: Terrain
last_updated: 2026-10-30T19:55:53Z
inherits:
  - BasePart
  - PVInstance
  - Instance
  - Object
type: class
memory_category: Instances
tags:
  - NotCreatable
summary: "`Terrain` lets you to create dynamically morphable environments."
---

# Class: Terrain

> `Terrain` lets you to create dynamically morphable environments.

## Description

The `Terrain` class lets you create dynamically morphable environments. It is
based on a 4&times;4&times;4 grid of cells, where each cell has a number
between `0` and `1` representing how much the geometry should occupy the cell,
and the material of the cell. The occupancy determines how the cell will morph
together with surrounding cells, and the result is the illusion of having no
grid constraint.

For more information, see [Terrain](/docs/en-us/parts/terrain.md).

## Properties

### Property: Terrain.Decoration

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
  "category": "Appearance",
  "capabilities": [
    "Environment"
  ]
}
```

Currently enables or disables animated grass on the
[Grass](/docs/reference/engine/enums/Material.md) terrain material, although future
modifications of this property may control additional decorative features.

### Property: Terrain.GrassLength

```json
{
  "type": "float",
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
    "Environment"
  ]
}
```

Specifies the length of animated grass on the [Grass](/docs/reference/engine/enums/Material.md)
terrain material, assuming [Decoration](/docs/reference/engine/classes/Terrain.md) is
enabled. Valid values are between `0.1` and `1`.

### Property: Terrain.MaterialColors

```json
{
  "type": "BinaryString",
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
    "Environment"
  ]
}
```

`MaterialColors` represents the editor for the **Material Color** feature
and cannot be edited by scripts.

To get the color of a material, use [Terrain:GetMaterialColor()](/docs/reference/engine/classes/Terrain.md). To
set the color of a material, use [Terrain:SetMaterialColor()](/docs/reference/engine/classes/Terrain.md).

### Property: Terrain.MaxExtents

```json
{
  "type": "Region3int16",
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
  "category": "Data",
  "capabilities": [
    "Environment"
  ]
}
```

Displays the boundaries of the largest possible editable region as a
[Region3int16](/docs/reference/engine/datatypes/Region3int16.md). The returned value spans from
`(-32000, -32000, -32000)` to `(32000, 32000, 32000)` in cell coordinates,
where each cell is 4 studs wide. This corresponds to a world-space volume
of -128,000 to 128,000 studs on each axis. The property is read-only.

### Property: Terrain.WaterColor

```json
{
  "type": "Color3",
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
    "Environment"
  ]
}
```

The tint color applied to `Terrain` water. This [Color3](/docs/reference/engine/datatypes/Color3.md) value is
blended with the water's base appearance to shift its overall hue. The
default value is `[0.05, 0.33, 0.36]` (a dark teal).

### Property: Terrain.WaterReflectance

```json
{
  "type": "float",
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
    "Environment"
  ]
}
```

Controls how opaque the reflections on `Terrain` water are, on a scale of
`0` (no reflections) to `1` (fully opaque reflections). The default value
is `1`.

### Property: Terrain.WaterTransparency

```json
{
  "type": "float",
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
    "Environment"
  ]
}
```

The transparency of `Terrain` water, on a scale of `0` (fully opaque) to
`1` (fully transparent). The default value is `0.3`.

### Property: Terrain.WaterWaveSize

```json
{
  "type": "float",
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
    "Environment"
  ]
}
```

Sets the maximum height of `Terrain` water waves in studs. This is
currently constrained to between `0` and `1`.

### Property: Terrain.WaterWaveSpeed

```json
{
  "type": "float",
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
    "Environment"
  ]
}
```

Sets how many times `Terrain` water waves will move up and down per
minute. This is currently constrained to between `0` and `100`.

### Property: Terrain.IsSmooth

```json
{
  "type": "boolean",
  "access": "ReadWrite",
  "security": {
    "read": "None",
    "write": "None"
  },
  "serialization": {
    "can_load": false,
    "can_save": false
  },
  "deprecated": true,
  "thread_safety": "ReadSafe",
  "category": "Data",
  "capabilities": [
    "Environment"
  ]
}
```

> **Deprecated:** The legacy terrain engine has been removed, so this property will always be `true`.

Returns `true` if the game is using the smooth terrain system.

## Methods

### Method: Terrain:CellCenterToWorld

**Signature:** `Terrain:CellCenterToWorld(x: int, y: int, z: int): Vector3`

Returns the world position of the center of the terrain cell at grid
coordinates `(x, y, z)`. Each terrain cell is 4&times;4&times;4 studs, so
this method returns the position of the lower-left-forward corner of the
cell plus an offset of `(2, 2, 2)` studs.

*Security: None · Thread Safety: Unsafe · Capabilities: Environment*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `x` | `int` |  | The X coordinate of the terrain cell in grid space. |
| `y` | `int` |  | The Y coordinate of the terrain cell in grid space. |
| `z` | `int` |  | The Z coordinate of the terrain cell in grid space. |

**Returns:** `Vector3` — The world-space [Vector3](/docs/reference/engine/datatypes/Vector3.md) position at the center of the
specified cell.

### Method: Terrain:CellCornerToWorld

**Signature:** `Terrain:CellCornerToWorld(x: int, y: int, z: int): Vector3`

Returns the world position of the lower-left-forward corner of the terrain
cell at grid coordinates `(x, y, z)`. Each terrain cell is
4&times;4&times;4 studs, so the corner position is
`(x * 4, y * 4, z * 4)`.

*Security: None · Thread Safety: Unsafe · Capabilities: Environment*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `x` | `int` |  | The X coordinate of the terrain cell in grid space. |
| `y` | `int` |  | The Y coordinate of the terrain cell in grid space. |
| `z` | `int` |  | The Z coordinate of the terrain cell in grid space. |

**Returns:** `Vector3` — The world-space [Vector3](/docs/reference/engine/datatypes/Vector3.md) position of the lower-left-forward
corner of the specified cell.

### Method: Terrain:Clear

**Signature:** `Terrain:Clear(): ()`

Clears the entire terrain, removing all material and occupancy data from
every voxel. After calling this method, the `Terrain` object contains no
geometry until new terrain is written via methods such as
[FillBlock()](/docs/reference/engine/classes/Terrain.md) or
[WriteVoxels()](/docs/reference/engine/classes/Terrain.md).

*Security: None · Thread Safety: Unsafe · Capabilities: Environment*

**Returns:** `()`

### Method: Terrain:CopyRegion

**Signature:** `Terrain:CopyRegion(region: Region3int16): TerrainRegion`

Stores a chunk of terrain into a [TerrainRegion](/docs/reference/engine/classes/TerrainRegion.md) object so it can be
loaded back later. Note that [TerrainRegion](/docs/reference/engine/classes/TerrainRegion.md) data does not replicate
between server and client.

*Security: None · Thread Safety: Unsafe · Capabilities: Environment*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `region` | `Region3int16` |  | The [Region3int16](/docs/reference/engine/datatypes/Region3int16.md) defining the area of terrain to copy, in cell coordinates. |

**Returns:** `TerrainRegion` — A [TerrainRegion](/docs/reference/engine/classes/TerrainRegion.md) containing the copied voxel data from the
specified region.

**Terrain:CopyRegion()**

The following code will copy all terrain and clear it. After 5 seconds it will
paste the terrain back.

```lua
local terrainRegion = workspace.Terrain:CopyRegion(workspace.Terrain.MaxExtents)
workspace.Terrain:Clear()

task.wait(5)

workspace.Terrain:PasteRegion(terrainRegion, workspace.Terrain.MaxExtents.Min, true)
```

### Method: Terrain:CountCells

**Signature:** `Terrain:CountCells(): int`

Returns the approximate number of non-empty cells in the terrain. A cell
is considered non-empty when it has a material other than Air and an
occupancy greater than zero. This count is an approximation and can be
used to quickly gauge how much terrain geometry exists in the place.

*Security: None · Thread Safety: Unsafe · Capabilities: Environment*

**Returns:** `int` — The approximate number of non-empty terrain cells.

### Method: Terrain:FillBall

**Signature:** `Terrain:FillBall(center: Vector3, radius: float, material: Material): ()`

Fills a spherical volume of smooth terrain centered at `center` with the
given `radius` (in studs) and [Material](/docs/reference/engine/enums/Material.md). Voxels within the sphere
are set to full occupancy with the specified material. Existing terrain
inside the sphere is overwritten.

*Security: None · Thread Safety: Unsafe · Capabilities: Environment*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `center` | `Vector3` |  | The position of the center of the terrain ball. |
| `radius` | `float` |  | The radius in studs of the terrain ball. |
| `material` | `Material` |  | The [Material](/docs/reference/engine/enums/Material.md) of the terrain ball. |

**Returns:** `()`

### Method: Terrain:FillBlock

**Signature:** `Terrain:FillBlock(cframe: CFrame, size: Vector3, material: Material): ()`

Fills an oriented rectangular volume of smooth terrain at the position and
rotation specified by `cframe`, with the dimensions given by `size` (in
studs), using the specified [Material](/docs/reference/engine/enums/Material.md). Because the block is oriented
by a [CFrame](/docs/reference/engine/datatypes/CFrame.md), it can be rotated to any angle. Existing terrain
inside the volume is overwritten.

*Security: None · Thread Safety: Unsafe · Capabilities: Environment*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `cframe` | `CFrame` |  | The position and orientation of the terrain block. |
| `size` | `Vector3` |  | The size in studs of the square block (both the height and width). |
| `material` | `Material` |  | The [Material](/docs/reference/engine/enums/Material.md) of the terrain block. |

**Returns:** `()`

### Method: Terrain:FillCylinder

**Signature:** `Terrain:FillCylinder(cframe: CFrame, height: float, radius: float, material: Material): ()`

Fills a cylinder of smooth terrain in a given space. The space is defined
using a [CFrame](/docs/reference/engine/datatypes/CFrame.md), height, and radius.

*Security: None · Thread Safety: Unsafe · Capabilities: Environment*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `cframe` | `CFrame` |  | The position and orientation of the terrain cylinder. |
| `height` | `float` |  | The height in studs of the terrain cylinder. |
| `radius` | `float` |  | The radius in studs of the terrain cylinder. |
| `material` | `Material` |  | The [Material](/docs/reference/engine/enums/Material.md) of the terrain cylinder. |

**Returns:** `()`

### Method: Terrain:FillRegion

**Signature:** `Terrain:FillRegion(region: Region3, resolution: float, material: Material): ()`

Fills an axis-aligned [Region3](/docs/reference/engine/datatypes/Region3.md) volume of smooth terrain with the
specified [Material](/docs/reference/engine/enums/Material.md) at full occupancy. The `resolution` parameter
must be exactly `4`. The region must be aligned to the voxel grid; use
[Region3:ExpandToGrid()](/docs/reference/engine/datatypes/Region3.md) to align a region before calling.

*Security: None · Thread Safety: Unsafe · Capabilities: Environment*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `region` | `Region3` |  | The [Region3](/docs/reference/engine/datatypes/Region3.md) to fill, which must be aligned to the voxel grid. |
| `resolution` | `float` |  | The voxel resolution; must be exactly `4`. |
| `material` | `Material` |  | The [Material](/docs/reference/engine/enums/Material.md) to fill the region with. |

**Returns:** `()`

### Method: Terrain:FillWedge

**Signature:** `Terrain:FillWedge(cframe: CFrame, size: Vector3, material: Material): ()`

This method fills a wedge-shaped volume of [Terrain](/docs/reference/engine/classes/Terrain.md) with the given
[Material](/docs/reference/engine/enums/Material.md) and the area's [CFrame](/docs/reference/engine/datatypes/CFrame.md) and size. The orientation
of the wedge is the same as an equivalent [WedgePart](/docs/reference/engine/classes/WedgePart.md).

*Security: None · Thread Safety: Unsafe · Capabilities: Environment*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `cframe` | `CFrame` |  | The position and orientation of the wedge to fill. |
| `size` | `Vector3` |  | The size of the wedge to fill. |
| `material` | `Material` |  | The material with which the wedge will be filled. |

**Returns:** `()`

### Method: Terrain:GetMaterialColor

**Signature:** `Terrain:GetMaterialColor(material: Material): Color3`

Returns the current [Color3](/docs/reference/engine/datatypes/Color3.md) color for the specified terrain
[Material](/docs/reference/engine/enums/Material.md). This color represents the tint applied to the material's
base texture. Passing [Air](/docs/reference/engine/enums/Material.md) or [Water](/docs/reference/engine/enums/Material.md) throws
an error because those materials do not support custom colors.

*Security: None · Thread Safety: Safe · Capabilities: Environment*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `material` | `Material` |  | The [Material](/docs/reference/engine/enums/Material.md) whose terrain color to retrieve. |

**Returns:** `Color3` — The [Color3](/docs/reference/engine/datatypes/Color3.md) representing the current color tint of the
specified material.

### Method: Terrain:PasteRegion

**Signature:** `Terrain:PasteRegion(region: TerrainRegion, corner: Vector3int16, pasteEmptyCells: boolean): ()`

Applies a chunk of terrain to the `Terrain` object. Note that
[TerrainRegion](/docs/reference/engine/classes/TerrainRegion.md) data does not replicate between server and client.

*Security: None · Thread Safety: Unsafe · Capabilities: Environment*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `region` | `TerrainRegion` |  | The [TerrainRegion](/docs/reference/engine/classes/TerrainRegion.md) to paste, previously obtained from [Terrain:CopyRegion()](/docs/reference/engine/classes/Terrain.md). |
| `corner` | `Vector3int16` |  | The [Vector3int16](/docs/reference/engine/datatypes/Vector3int16.md) cell coordinate at which to place the lower-left-forward corner of the region. |
| `pasteEmptyCells` | `boolean` |  | Whether to overwrite existing terrain with empty (air) cells from the region. |

**Returns:** `()`

**Create, Copy and Paste Terrain**

Creates some terrain, copies it, then pastes it.

```lua
local Terrain = workspace.Terrain

-- Create a simple terrain region
local initialRegion = Region3.new(Vector3.zero, Vector3.one * 10)
Terrain:FillRegion(initialRegion, 4, Enum.Material.Grass)

-- Copy the region
local copyRegion = Region3int16.new(Vector3int16.new(0, 0, 0), Vector3int16.new(10, 10, 10))
local copiedRegion = Terrain:CopyRegion(copyRegion)

-- Define where to paste the region
local newRegionCorner = Vector3int16.new(5, 0, 0)

-- Paste the region
Terrain:PasteRegion(copiedRegion, newRegionCorner, true)
```

### Method: Terrain:ReadVoxelChannels

**Signature:** `Terrain:ReadVoxelChannels(region: Region3, resolution: float, channelIds: Array): Dictionary`

Returns voxel data from a region of terrain, separated by channel. Unlike
[ReadVoxels()](/docs/reference/engine/classes/Terrain.md), this method lets you specify
exactly which channels to read (`SolidMaterial`, `SolidOccupancy`, and/or
`LiquidOccupancy`), and returns a dictionary keyed by channel ID. The
`region` must be aligned to the voxel grid, `resolution` must be `4`, and
the region cannot exceed 4,194,304 voxels.

*Security: None · Thread Safety: Safe · Capabilities: Environment*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `region` | `Region3` |  | Target region to read from. Must be aligned to the voxel grid. Will throw an error if region is too large; limit is currently 4194304 voxels&sup3;. |
| `resolution` | `float` |  | Voxel resolution. Must be 4. |
| `channelIds` | `Array` |  | Array of channel IDs (strings) that need to be accessed from the voxel data. Each channel ID represents a type of data that's stored in voxel. Current supported IDs are `{"SolidMaterial", "SolidOccupancy", "LiquidOccupancy"}`. |

**Returns:** `Dictionary` — Returns voxel data as a dictionary based on the `channelIds` input.
Keys represent each channel ID with their respective value as an array
of 3D data.

- `SolidMaterial` — The [Material](/docs/reference/engine/enums/Material.md) material of the voxel. Note
  that [Water](/docs/reference/engine/enums/Material.md) is not supported anymore; instead, a
  voxel that contains water will have a value of `LiquidOccupancy`.
- `SolidOccupancy` — The occupancy of the voxel's material as
  specified in the `SolidMaterial` channel. This is a value between 0
  (empty) and 1 (full).
- `LiquidOccupancy` — Specifies the occupancy of the
  [Water](/docs/reference/engine/enums/Material.md) material in a voxel as a value between 0 (no
  water) and 1 (full of water). If the `SolidOccupancy` is 1 and the
  `SolidMaterial` is not [Air](/docs/reference/engine/enums/Material.md), this will be 0.

The dictionary also contains a `Size` key with a value representing
the 3D array size of each channel data.

**Terrain:ReadVoxelChannels()**

```lua
local REGION_START = Vector3.new(-20, -20, -20)
local REGION_END = Vector3.new(20, 20, 20)

local function printRegion(terrain, region)
	local channelOutput = terrain:ReadVoxelChannels(region, 4, { "SolidOccupancy", "SolidMaterial", "LiquidOccupancy" })
	local size = channelOutput.Size
	for x = 1, size.X do
		for y = 1, size.Y do
			for z = 1, size.Z do
				print(
					("(%2i, %2i, %2i): %.2f %s %.2f"):format(
						x,
						y,
						z,
						channelOutput.SolidOccupancy[x][y][z],
						channelOutput.SolidMaterial[x][y][z].Name,
						channelOutput.LiquidOccupancy[x][y][z]
					)
				)
			end
		end
	end
end

local region = Region3.new(REGION_START, REGION_END)
printRegion(workspace.Terrain, region)
```

### Method: Terrain:ReadVoxels

**Signature:** `Terrain:ReadVoxels(region: Region3, resolution: float): Tuple`

Returns the voxel data for a region of smooth terrain as two 3D arrays:
`materials` (an array of [Material](/docs/reference/engine/enums/Material.md) values) and `occupancies` (an
array of numbers between `0` and `1`). The `region` must be aligned to the
voxel grid, `resolution` must be `4`, and the region cannot exceed
4,194,304 voxels. For more granular channel control, see
[ReadVoxelChannels()](/docs/reference/engine/classes/Terrain.md).

*Security: None · Thread Safety: Safe · Capabilities: Environment*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `region` | `Region3` |  | Target region to read from. Must be aligned to the voxel grid. Will throw an error if region is too large. The limit is currently 4194304 voxels&sup3;. |
| `resolution` | `float` |  | Voxel resolution. Must be `4`. |

**Returns:** `Tuple` — Returns raw voxel data as two 3D arrays.

- `materials` - 3D array of [Material](/docs/reference/engine/enums/Material.md) from the target area. Also
  contains a Size field, equal to the dimensions of the nested arrays.
- `occupancies` - 3D array of occupancy values from the target area.
  Also contains a Size field, equal to the dimensions of the nested
  arrays.

**Terrain:ReadVoxels()**

```lua
local REGION_START = Vector3.new(-20, -20, -20)
local REGION_END = Vector3.new(20, 20, 20)

local function printRegion(terrain, region)
	local materials, occupancies = terrain:ReadVoxels(region, 4)

	local size = materials.Size -- Same as occupancies.Size

	for x = 1, size.X, 1 do
		for y = 1, size.Y, 1 do
			for z = 1, size.Z, 1 do
				print(("(%2i, %2i, %2i): %.2f %s"):format(x, y, z, occupancies[x][y][z], materials[x][y][z].Name))
			end
		end
	end
end

local region = Region3.new(REGION_START, REGION_END)

printRegion(workspace.Terrain, region)
```

### Method: Terrain:ReplaceMaterial

**Signature:** `Terrain:ReplaceMaterial(region: Region3, resolution: float, sourceMaterial: Material, targetMaterial: Material): ()`

ReplaceMaterial replaces terrain of a certain [Material](/docs/reference/engine/enums/Material.md) within a
[Region3](/docs/reference/engine/datatypes/Region3.md) with another material. Essentially, it is a
find-and-replace operation on [Terrain](/docs/reference/engine/classes/Terrain.md) materials.

When calling this method, the `resolution` parameter must be exactly `4`.
Additionally, `region` must be aligned to the terrain materials grid, such
that the components of the region's minimum and maximum points must be
divisible by `4`. Use [Region3:ExpandToGrid()](/docs/reference/engine/datatypes/Region3.md) to make a region
compatible with this function.

*Security: None · Thread Safety: Unsafe · Capabilities: Environment*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `region` | `Region3` |  | The region in which the replacement operation will occur. |
| `resolution` | `float` |  | The resolution at which the replacement operation will take place; at the moment this must be exactly `4`. |
| `sourceMaterial` | `Material` |  | The old material that shall be replaced. |
| `targetMaterial` | `Material` |  | The new material. |

**Returns:** `()`

**Terrain:ReplaceMaterial**

This code sample demonstrates the usage of [Terrain:ReplaceMaterial()](/docs/reference/engine/classes/Terrain.md)
by replacing grass near the game origin with asphalt.

```lua
local terrain = workspace.Terrain
local region = Region3.new(Vector3.new(-20, -20, -20), Vector3.new(20, 20, 20))
local resolution = 4
local materialToReplace = Enum.Material.Grass
local replacementMaterial = Enum.Material.Asphalt

terrain:ReplaceMaterial(region, resolution, materialToReplace, replacementMaterial)
```

### Method: Terrain:SetMaterialColor

**Signature:** `Terrain:SetMaterialColor(material: Material, value: Color3): ()`

Sets current terrain material color for specified terrain material.
Terrain material will shift its base color toward specified color.

*Security: None · Thread Safety: Unsafe · Capabilities: Environment*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `material` | `Material` |  | The [Material](/docs/reference/engine/enums/Material.md) whose terrain color to change. |
| `value` | `Color3` |  | The [Color3](/docs/reference/engine/datatypes/Color3.md) to apply as the new color tint for the material. |

**Returns:** `()`

### Method: Terrain:WorldToCell

**Signature:** `Terrain:WorldToCell(position: Vector3): Vector3`

Returns the grid cell location that contains the point `position`.

*Security: None · Thread Safety: Unsafe · Capabilities: Environment*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `position` | `Vector3` |  | The world-space [Vector3](/docs/reference/engine/datatypes/Vector3.md) to convert to a cell coordinate. |

**Returns:** `Vector3` — A [Vector3](/docs/reference/engine/datatypes/Vector3.md) representing the grid cell coordinates containing
the given position.

### Method: Terrain:WorldToCellPreferEmpty

**Signature:** `Terrain:WorldToCellPreferEmpty(position: Vector3): Vector3`

Returns the grid cell location that contains the point `position`,
preferring empty grid cells when position is on a grid edge.

*Security: None · Thread Safety: Unsafe · Capabilities: Environment*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `position` | `Vector3` |  | The world-space [Vector3](/docs/reference/engine/datatypes/Vector3.md) to convert to a cell coordinate. |

**Returns:** `Vector3` — A [Vector3](/docs/reference/engine/datatypes/Vector3.md) representing the grid cell coordinates, biased
toward an empty (air) neighbor when the position lies on a cell
boundary.

### Method: Terrain:WorldToCellPreferSolid

**Signature:** `Terrain:WorldToCellPreferSolid(position: Vector3): Vector3`

Returns the grid cell location that contains the point position,
preferring non-empty grid cells when position is on a grid edge.

*Security: None · Thread Safety: Unsafe · Capabilities: Environment*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `position` | `Vector3` |  | The world-space [Vector3](/docs/reference/engine/datatypes/Vector3.md) to convert to a cell coordinate. |

**Returns:** `Vector3` — A [Vector3](/docs/reference/engine/datatypes/Vector3.md) representing the grid cell coordinates, biased
toward a non-empty (solid) neighbor when the position lies on a cell
boundary.

### Method: Terrain:WriteVoxelChannels

**Signature:** `Terrain:WriteVoxelChannels(region: Region3, resolution: float, channels: Dictionary): ()`

Sets a region of terrain using a dictionary of per-channel voxel data, the
inverse of [ReadVoxelChannels()](/docs/reference/engine/classes/Terrain.md). The
`channels` dictionary maps channel ID strings (`SolidMaterial`,
`SolidOccupancy`, and/or `LiquidOccupancy`) to their respective 3D data
arrays. You may write one or more channels in a single call. The `region`
must be aligned to the voxel grid, `resolution` must be `4`, and the
region cannot exceed 4,194,304 voxels.

*Security: None · Thread Safety: Unsafe · Capabilities: Environment*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `region` | `Region3` |  | Target region to write to. Must be aligned to the voxel grid. Will throw an error if region is too large; limit is currently 4194304 voxels&sup3;. |
| `resolution` | `float` |  | Voxel resolution. Must be `4`. |
| `channels` | `Dictionary` |  | Dictionary of voxel data similar to the return value of [ReadVoxelChannels()](/docs/reference/engine/classes/Terrain.md). Keys represent each channel ID with their respective value as an array of 3D data. The dictionary can support single or multiple channel inputs.  - `SolidMaterial` — The [Material](/docs/reference/engine/enums/Material.md) material of the voxel. Note   that [Water](/docs/reference/engine/enums/Material.md) is not supported anymore; instead, a   voxel that contains only water should be entered as   `SolidMaterial = Enum.Material.Air, LiquidOccupancy = x`, where `x`   is a number between `0` (exclusive) and `1` (inclusive). - `SolidOccupancy` — The occupancy of the voxel's material as   specified in the `SolidMaterial` channel. This should be a value   between `0` (empty) and `1` (full). - `LiquidOccupancy` — Specifies the occupancy of the   [Water](/docs/reference/engine/enums/Material.md) material in a voxel as a value between `0` (no   water) and `1` (full of water). If the `SolidOccupancy` is 1 and the   `SolidMaterial` is not [Air](/docs/reference/engine/enums/Material.md), this will be `0`. |

**Returns:** `()`

**Terrain:WriteVoxelChannels()**

```lua
local region = Region3.new(Vector3.new(0, 0, 0), Vector3.new(64, 32, 64))

local RESOLUTION = 4
local OCC_EPSILON = 1 / 256

local function generateRandomTerrainInRegion(regionInput)
	local region = regionInput:ExpandToGrid(4)
	local size = region.Size / 4
	local solidMaterials = {}
	local solidOccupancies = {}
	local waterOcc = {}

	for x = 1, size.X do
		table.insert(solidMaterials, {})
		table.insert(solidOccupancies, {})
		table.insert(waterOcc, {})

		for y = 1, size.Y do
			table.insert(solidMaterials[x], {})
			table.insert(solidOccupancies[x], {})
			table.insert(waterOcc[x], {})

			for z = 1, size.Z do
				local mat = if math.random() < 0.5 then Enum.Material.Air else Enum.Material.Sand
				local occ = 0
				local water = math.random()
				if mat == Enum.Material.Sand then
					occ = math.random() / 2 + 0.5
					if occ > 1 - OCC_EPSILON then
						water = 0 -- Solids cannot contain water
					end
				else
					occ = 0
				end
				table.insert(solidMaterials[x][y], mat)
				table.insert(solidOccupancies[x][y], occ)
				table.insert(waterOcc[x][y], water)
			end
		end
	end
	return { SolidMaterial = solidMaterials, SolidOccupancy = solidOccupancies, LiquidOccupancy = waterOcc }
end

local regionContent = generateRandomTerrainInRegion(region)
workspace.Terrain:WriteVoxelChannels(region, 4, regionContent)
```

### Method: Terrain:WriteVoxels

**Signature:** `Terrain:WriteVoxels(region: Region3, resolution: float, materials: Array, occupancy: Array): ()`

Sets a region of smooth terrain from two 3D arrays: `materials` (an array
of [Material](/docs/reference/engine/enums/Material.md) values) and `occupancy` (an array of numbers between
`0` and `1`). Both arrays must have dimensions that exactly match the
target region in voxels. The `region` must be aligned to the voxel grid,
`resolution` must be `4`, and the region cannot exceed 4,194,304 voxels.
For more granular channel control, see
[WriteVoxelChannels()](/docs/reference/engine/classes/Terrain.md).

*Security: None · Thread Safety: Unsafe · Capabilities: Environment*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `region` | `Region3` |  | Target region to write to. Must be aligned to the voxel grid. Will throw an error if region is too large. |
| `resolution` | `float` |  | Voxel resolution. Must be `4`. |
| `materials` | `Array` |  | 3D array of [Material](/docs/reference/engine/enums/Material.md). Dimensions must exactly match the size of the target region in voxels. |
| `occupancy` | `Array` |  | 3D array of voxel occupancies (number between `0` and `1`). Dimensions must exactly match the size of the target region in voxels. |

**Returns:** `()`

**Terrain:WriteVoxels()**

```lua
local terrain = workspace.Terrain
local resolution = 4
local region = Region3.new(Vector3.new(0, 0, 0), Vector3.new(16, 28, 20)):ExpandToGrid(resolution)
local materials = {
	{
		{
			Enum.Material.CrackedLava,
			Enum.Material.CrackedLava,
			Enum.Material.CrackedLava,
			Enum.Material.CrackedLava,
			Enum.Material.CrackedLava,
		},
		{ Enum.Material.Rock, Enum.Material.Rock, Enum.Material.Rock, Enum.Material.Rock, Enum.Material.Rock },
		{ Enum.Material.Rock, Enum.Material.Rock, Enum.Material.Rock, Enum.Material.Rock, Enum.Material.Rock },
		{ Enum.Material.Sand, Enum.Material.Sand, Enum.Material.Sand, Enum.Material.Sand, Enum.Material.Sand },
		{ Enum.Material.Sand, Enum.Material.Sand, Enum.Material.Sand, Enum.Material.Sand, Enum.Material.Sand },
		{ Enum.Material.Mud, Enum.Material.Mud, Enum.Material.Mud, Enum.Material.Mud, Enum.Material.Mud },
		{ Enum.Material.Air, Enum.Material.Air, Enum.Material.Air, Enum.Material.Air, Enum.Material.Air },
	},
	{
		{
			Enum.Material.CrackedLava,
			Enum.Material.CrackedLava,
			Enum.Material.CrackedLava,
			Enum.Material.CrackedLava,
			Enum.Material.CrackedLava,
		},
		{ Enum.Material.Rock, Enum.Material.Rock, Enum.Material.Rock, Enum.Material.Rock, Enum.Material.Rock },
		{ Enum.Material.Rock, Enum.Material.Rock, Enum.Material.Rock, Enum.Material.Rock, Enum.Material.Rock },
		{ Enum.Material.Sand, Enum.Material.Sand, Enum.Material.Sand, Enum.Material.Sand, Enum.Material.Sand },
		{ Enum.Material.Sand, Enum.Material.Sand, Enum.Material.Sand, Enum.Material.Sand, Enum.Material.Sand },
		{ Enum.Material.Mud, Enum.Material.Snow, Enum.Material.Snow, Enum.Material.Snow, Enum.Material.Mud },
		{ Enum.Material.Air, Enum.Material.Snow, Enum.Material.Snow, Enum.Material.Snow, Enum.Material.Air },
	},
	{
		{
			Enum.Material.CrackedLava,
			Enum.Material.Sand,
			Enum.Material.Sand,
			Enum.Material.Sand,
			Enum.Material.CrackedLava,
		},
		{ Enum.Material.Rock, Enum.Material.Rock, Enum.Material.Rock, Enum.Material.Rock, Enum.Material.Rock },
		{ Enum.Material.Rock, Enum.Material.Rock, Enum.Material.Rock, Enum.Material.Rock, Enum.Material.Rock },
		{ Enum.Material.Sand, Enum.Material.Sand, Enum.Material.Sand, Enum.Material.Sand, Enum.Material.Sand },
		{ Enum.Material.Sand, Enum.Material.Sand, Enum.Material.Sand, Enum.Material.Sand, Enum.Material.Sand },
		{ Enum.Material.Mud, Enum.Material.Snow, Enum.Material.Snow, Enum.Material.Snow, Enum.Material.Mud },
		{ Enum.Material.Air, Enum.Material.Snow, Enum.Material.Snow, Enum.Material.Snow, Enum.Material.Air },
	},
	{
		{
			Enum.Material.CrackedLava,
			Enum.Material.CrackedLava,
			Enum.Material.CrackedLava,
			Enum.Material.CrackedLava,
			Enum.Material.CrackedLava,
		},
		{ Enum.Material.Rock, Enum.Material.Rock, Enum.Material.Rock, Enum.Material.Rock, Enum.Material.Rock },
		{ Enum.Material.Rock, Enum.Material.Rock, Enum.Material.Rock, Enum.Material.Rock, Enum.Material.Rock },
		{ Enum.Material.Sand, Enum.Material.Sand, Enum.Material.Sand, Enum.Material.Sand, Enum.Material.Sand },
		{ Enum.Material.Sand, Enum.Material.Sand, Enum.Material.Sand, Enum.Material.Sand, Enum.Material.Sand },
		{ Enum.Material.Mud, Enum.Material.Mud, Enum.Material.Mud, Enum.Material.Mud, Enum.Material.Mud },
		{ Enum.Material.Air, Enum.Material.Air, Enum.Material.Air, Enum.Material.Air, Enum.Material.Air },
	},
}
local occupancies = {
	{
		{ 1, 1, 1, 1, 1 },
		{ 1, 1, 1, 1, 1 },
		{ 1, 1, 1, 1, 1 },
		{ 1, 1, 1, 1, 1 },
		{ 1, 1, 1, 1, 1 },
		{ 0.5, 0.5, 0.5, 0.5, 0.5 },
		{ 0, 0, 0, 0, 0 },
	},
	{
		{ 1, 1, 1, 1, 1 },
		{ 1, 1, 1, 1, 1 },
		{ 1, 1, 1, 1, 1 },
		{ 1, 1, 1, 1, 1 },
		{ 1, 1, 1, 1, 1 },
		{ 0.5, 1, 1, 1, 0.5 },
		{ 0, 1, 1, 1, 0 },
	},
	{
		{ 1, 1, 1, 1, 1 },
		{ 1, 1, 1, 1, 1 },
		{ 1, 1, 1, 1, 1 },
		{ 1, 1, 1, 1, 1 },
		{ 1, 1, 1, 1, 1 },
		{ 0.5, 1, 1, 1, 0.5 },
		{ 0, 1, 1, 1, 0 },
	},
	{
		{ 1, 1, 1, 1, 1 },
		{ 1, 1, 1, 1, 1 },
		{ 1, 1, 1, 1, 1 },
		{ 1, 1, 1, 1, 1 },
		{ 1, 1, 1, 1, 1 },
		{ 0.5, 0.5, 0.5, 0.5, 0.5 },
		{ 0, 0, 0, 0, 0 },
	},
}

terrain:WriteVoxels(region, resolution, materials, occupancies)
```

### Method: Terrain:AutowedgeCell

**Signature:** `Terrain:AutowedgeCell(x: int, y: int, z: int): boolean`

> **Deprecated:** This item is a deprecated function of a legacy [Terrain](/docs/reference/engine/classes/Terrain.md) engine that has been removed. Do not use it for new work.

Obsolete function which no longer does anything.

*Security: None · Thread Safety: Unsafe · Capabilities: Environment*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `x` | `int` |  | The X coordinate of the terrain cell. |
| `y` | `int` |  | The Y coordinate of the terrain cell. |
| `z` | `int` |  | The Z coordinate of the terrain cell. |

**Returns:** `boolean` — Always returns `true`; the function no longer performs any operation.

### Method: Terrain:AutowedgeCells

**Signature:** `Terrain:AutowedgeCells(region: Region3int16): ()`

> **Deprecated:** This item is a deprecated function of a legacy [Terrain](/docs/reference/engine/classes/Terrain.md) engine that has been removed. Do not use it for new work.

Obsolete function which no longer does anything. It was part of the legacy
terrain engine that has since been removed, so calling it on a region has
no effect.

*Security: None · Thread Safety: Unsafe · Capabilities: Environment*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `region` | `Region3int16` |  | The [Region3int16](/docs/reference/engine/datatypes/Region3int16.md) specifying the region of terrain cells to process. |

**Returns:** `()`

### Method: Terrain:ConvertToSmooth

**Signature:** `Terrain:ConvertToSmooth(): ()`

> **Deprecated:** Since all places now automatically use the new terrain engine, this method is obsolete.

Transforms the legacy terrain engine into the new terrain engine. All
places now automatically use the new terrain engine, so this method is
obsolete.

*Security: PluginSecurity · Thread Safety: Unsafe · Capabilities: Environment*

**Returns:** `()`

### Method: Terrain:GetCell

**Signature:** `Terrain:GetCell(x: int, y: int, z: int): Tuple`

> **Deprecated:** This item is a deprecated function of a legacy [Terrain](/docs/reference/engine/classes/Terrain.md) engine that has been removed. Do not use it for new work.

Returns the closest cell material from the legacy terrain engine that
matches the smooth terrain voxel specified.

*Security: None · Thread Safety: Unsafe · Capabilities: Environment*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `x` | `int` |  | The X coordinate of the terrain cell. |
| `y` | `int` |  | The Y coordinate of the terrain cell. |
| `z` | `int` |  | The Z coordinate of the terrain cell. |

**Returns:** `Tuple` — A tuple containing the legacy cell material, block type, and
orientation of the specified cell.

### Method: Terrain:GetWaterCell

**Signature:** `Terrain:GetWaterCell(x: int, y: int, z: int): Tuple`

> **Deprecated:** This item is a deprecated function of a legacy [Terrain](/docs/reference/engine/classes/Terrain.md) engine that has been removed. Do not use it for new work.

Returns `true` if the cell is a water cell.

*Security: None · Thread Safety: Unsafe · Capabilities: Environment*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `x` | `int` |  | The X coordinate of the terrain cell. |
| `y` | `int` |  | The Y coordinate of the terrain cell. |
| `z` | `int` |  | The Z coordinate of the terrain cell. |

**Returns:** `Tuple` — A tuple containing whether the cell has water, the water force, and
the water direction.

### Method: Terrain:SetCell

**Signature:** `Terrain:SetCell(x: int, y: int, z: int, material: CellMaterial, block: CellBlock, orientation: CellOrientation): ()`

> **Deprecated:** This item is a deprecated function of a legacy [Terrain](/docs/reference/engine/classes/Terrain.md) engine that has been removed. Do not use it for new work.

Sets the occupancy of the specified terrain voxel to `1` and sets its
material to the closest smooth terrain material that matches the cell
material.

*Security: None · Thread Safety: Unsafe · Capabilities: Environment*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `x` | `int` |  | The X coordinate of the terrain cell. |
| `y` | `int` |  | The Y coordinate of the terrain cell. |
| `z` | `int` |  | The Z coordinate of the terrain cell. |
| `material` | `CellMaterial` |  | The [CellMaterial](/docs/reference/engine/enums/CellMaterial.md) to set for the cell. |
| `block` | `CellBlock` |  | The [CellBlock](/docs/reference/engine/enums/CellBlock.md) shape type for the cell. |
| `orientation` | `CellOrientation` |  | The [CellOrientation](/docs/reference/engine/enums/CellOrientation.md) rotation for the cell. |

**Returns:** `()`

### Method: Terrain:SetCells

**Signature:** `Terrain:SetCells(region: Region3int16, material: CellMaterial, block: CellBlock, orientation: CellOrientation): ()`

> **Deprecated:** This item is a deprecated function of a legacy [Terrain](/docs/reference/engine/classes/Terrain.md) engine that has been removed. Do not use it for new work.

Sets the occupancy of all terrain voxels in the specified region to `1`
and sets their materials to the closest smooth terrain material that
matches the cell material.

*Security: None · Thread Safety: Unsafe · Capabilities: Environment*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `region` | `Region3int16` |  | The [Region3int16](/docs/reference/engine/datatypes/Region3int16.md) specifying the area of terrain cells to set. |
| `material` | `CellMaterial` |  | The [CellMaterial](/docs/reference/engine/enums/CellMaterial.md) to apply to all cells in the region. |
| `block` | `CellBlock` |  | The [CellBlock](/docs/reference/engine/enums/CellBlock.md) shape type to apply to all cells in the region. |
| `orientation` | `CellOrientation` |  | The [CellOrientation](/docs/reference/engine/enums/CellOrientation.md) rotation to apply to all cells in the region. |

**Returns:** `()`

### Method: Terrain:SetWaterCell

**Signature:** `Terrain:SetWaterCell(x: int, y: int, z: int, force: WaterForce, direction: WaterDirection): ()`

> **Deprecated:** This item is a deprecated function of a legacy [Terrain](/docs/reference/engine/classes/Terrain.md) engine that has been removed. Do not use it for new work.

Sets the specified terrain voxel's material to water and sets its
occupancy to `1`.

*Security: None · Thread Safety: Unsafe · Capabilities: Environment*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `x` | `int` |  | The X coordinate of the terrain cell. |
| `y` | `int` |  | The Y coordinate of the terrain cell. |
| `z` | `int` |  | The Z coordinate of the terrain cell. |
| `force` | `WaterForce` |  | The [WaterForce](/docs/reference/engine/enums/WaterForce.md) value representing the water force in the cell. |
| `direction` | `WaterDirection` |  | The [WaterDirection](/docs/reference/engine/enums/WaterDirection.md) value representing the water flow direction. |

**Returns:** `()`

## Inherited Members

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