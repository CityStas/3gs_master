---
title: "Environmental terrain"
url: /docs/en-us/parts/terrain
last_updated: 2026-10-30T19:55:46Z
description: "Explore how to generate and sculpt realistic terrain environments such as mountains, bodies of water, grass-covered hills, or a flat desert."
---

# Environmental terrain

Studio's [Terrain Editor](/docs/en-us/studio/terrain-editor.md) lets you generate and sculpt detailed and realistic terrain environments such as mountains, bodies of water, grass-covered hills, or a flat desert. Terrain is made up of grids of **voxels** which are 4×4×4 stud regions in the 3D world with a set material.

![Terrain Editor indicated in Studio's toolbar](../assets/studio/general/Toolbar-Terrain-Editor.png)![Desert terrain with mountains in the distance](../assets/modeling/terrain/Showcase.jpg)

Using the editor tools, you can easily [generate](#generate-terrain) and edit terrain either at a [voxel](#detailed-editing) or [region](#large-scale-editing) level with the option of importing a [heightmap](#heightmaps-and-colormaps) and [colormap](#heightmaps-and-colormaps). For more precise, dynamic, or procedural terrain editing, you can also [script](#scripting) terrain creation.

## Terrain materials

The following default materials are available for terrain. You can also paint [custom terrain materials](/docs/en-us/parts/custom-terrain-materials.md) after you enable **Expanded Terrain**, or apply [custom materials](/docs/en-us/parts/materials.md#custom-materials) as overrides. Materials affect both the shape and appearance of terrain in the world; for example, [animated grass](#grass-animation) renders only on the `Enum.Material.Grass|Grass` material and the `Enum.Material.Water|Water` material [ripples and shimmers](#water-appearance) with a subtle motion.

![Appearance of Asphalt material](../assets/modeling/terrain/Material-Asphalt.jpg)_Asphalt_

![Appearance of Basalt material](../assets/modeling/terrain/Material-Basalt.jpg)_Basalt_

![Appearance of Brick material](../assets/modeling/terrain/Material-Brick.jpg)_Brick_

![Appearance of Cobblestone material](../assets/modeling/terrain/Material-Cobblestone.jpg)_Cobblestone_

![Appearance of Concrete material](../assets/modeling/terrain/Material-Concrete.jpg)_Concrete_

![Appearance of Cracked Lava material](../assets/modeling/terrain/Material-Cracked-Lava.jpg)_Cracked Lava_

![Appearance of Glacier material](../assets/modeling/terrain/Material-Glacier.jpg)_Glacier_

![Appearance of Grass material](../assets/modeling/terrain/Material-Grass.jpg)_Grass_

![Appearance of Ground material](../assets/modeling/terrain/Material-Ground.jpg)_Ground_

![Appearance of Ice material](../assets/modeling/terrain/Material-Ice.jpg)_Ice_

![Appearance of Leafy Grass material](../assets/modeling/terrain/Material-Leafy-Grass.jpg)_Leafy Grass_

![Appearance of Limestone material](../assets/modeling/terrain/Material-Limestone.jpg)_Limestone_

![Appearance of Mud material](../assets/modeling/terrain/Material-Mud.jpg)_Mud_

![Appearance of Pavement material](../assets/modeling/terrain/Material-Pavement.jpg)_Pavement_

![Appearance of Rock material](../assets/modeling/terrain/Material-Rock.jpg)_Rock_

![Appearance of Salt material](../assets/modeling/terrain/Material-Salt.jpg)_Salt_

![Appearance of Sand material](../assets/modeling/terrain/Material-Sand.jpg)_Sand_

![Appearance of Sandstone material](../assets/modeling/terrain/Material-Sandstone.jpg)_Sandstone_

![Appearance of Slate material](../assets/modeling/terrain/Material-Slate.jpg)_Slate_

![Appearance of Snow material](../assets/modeling/terrain/Material-Snow.jpg)_Snow_

![Appearance of Water material](../assets/modeling/terrain/Material-Water.jpg)_Water_

![Appearance of Wood Planks material](../assets/modeling/terrain/Material-Wood-Planks.jpg)_Wood Planks_

![Air material icon (no visual appearance)](../assets/modeling/terrain/Material-Air.png)_Air_

### Water appearance

By default, terrain water ripples, oscillates, and shimmers with a subtle motion.

To customize the color and motion of water:

1. In the **Explorer** window, navigate to the `Class.Workspace`, then select the `Class.Terrain` object.![Terrain object shown in Explorer window of Studio](../assets/studio/explorer/Workspace-Terrain.png)
2. In the **Properties** window, customize the appearance of water through the following properties: | Property | Description |
| --- | --- | | `Class.Terrain.WaterColor\|WaterColor` | Adjusts the overall hue of all terrain water in the game. | | `Class.Terrain.WaterReflectance\|WaterReflectance` | Adjusts how much water surfaces reflect the sky and surrounding objects from a value of 1 (high) to 0 (none). | | `Class.Terrain.WaterTransparency\|WaterTransparency` | Adjusts how transparent water is from a value of 1 (clear) to 0 (opaque). | | `Class.Terrain.WaterWaveSize\|WaterWaveSize` | Adjusts the size of waves from a value of 1 (large) to 0 (none). | | `Class.Terrain.WaterWaveSpeed\|WaterWaveSpeed` | Adjusts the speed of waves from a value of 100 (turbulent) to 0 (still). |

> **Info:** Some water properties are only visible while playtesting. To preview all properties while editing, open [Studio Settings](/docs/en-us/studio/setup.md#customization), search for **Editor Quality Level**, and set it to the highest level.
### Grass animation

While most materials are static, you can add animated blades of grass to the `Enum.Material.Grass|Grass` terrain material. By default, grass sways gently in a simulated wind, and you can adjust the direction/strength of its animation through [global wind](/docs/en-us/environment/global-wind.md).

> **Info:** Note that the speed of animated grass — but not its vector direction — will be reduced if the player has toggled on the **Reduce Motion** [accessibility](/docs/en-us/production/publishing/accessibility.md#reduced-motion) setting from the Roblox or in-game **Settings** menu.

To add animated grass to the `Enum.Material.Grass|Grass` material:

1. In the **Explorer** window, navigate to the `Class.Workspace`, then select the `Class.Terrain` object.![Terrain object shown in Explorer window of Studio](../assets/studio/explorer/Workspace-Terrain.png)
2. In the **Properties** window, toggle on the `Class.Terrain.Decoration|Decoration` property.![Decoration property of Terrain object in Properties window of Studio](../assets/studio/properties/Terrain-Decoration.png)
3. Adjust the grass length by entering a value between `0.1` and `1` for the `Class.Terrain.GrassLength|GrassLength` property.![GrassLength property of Terrain object in Properties window of Studio](../assets/studio/properties/Terrain-GrassLength.png)![GrassLength comparison depicted on rolling grassland hills.](../assets/modeling/terrain/Terrain-GrassLength.jpg)
4. Adjust the direction and strength of its animation through [global wind](/docs/en-us/environment/global-wind.md).

### Custom terrain colors

Each terrain material is assigned a default color, but you can customize any material's color to better fit your game.

#### Default

![Default terrain colors used in desert landscape](../assets/modeling/terrain/Showcase.jpg)

#### Fantasy

![Custom terrain colors applied for fantasy landscape](../assets/modeling/terrain/Custom-Colors-Fantasy.jpg)

#### Tundra

![Custom terrain colors applied for tundra landscape](../assets/modeling/terrain/Custom-Colors-Tundra.jpg)

To customize any material color other than water:

1. In the **Explorer** window, navigate to the `Class.Workspace`, then select the `Class.Terrain` object.![Terrain object shown in Explorer window of Studio](../assets/studio/explorer/Workspace-Terrain.png)
2. In the **Properties** window, expand `Class.Terrain.MaterialColors|MaterialColors`. All materials display with their RGB code.![MaterialColors property shown in Properties window of Studio](../assets/studio/properties/Terrain-MaterialColors-Expand.png)
3. For any material, either input a new RGB code or click the color box to open the [colors popup](/docs/en-us/parts.md#color).

## Generate terrain

Using the following tools and methods, you can generate large areas of terrain procedurally through tooling or scripting, or automatically based on a heightmap and colormap.

### Generate tool

The **Generate** tool allows you to procedurally generate terrain in seconds. This is useful if you want to create a large map and fine-tune [terrain details](#detailed-editing).

1. In the editor window, navigate to the **Create** tab and select the **Generate** tool.![Generate tool indicated in Create tab of Terrain Editor](../assets/studio/terrain-editor/Create-Tab-Generate.png)
2. In the 3D viewport, move/resize the **selection region** in which to generate terrain. Alternatively, expand the tool's **Selection Settings** and enter values into the **X**/**Y**/**Z** inputs to set a specific size and position.
3. In the tool's **Biome Settings** section, choose the following biomes to include in the new terrain:
  - Arctic
  - Dunes
  - Canyons
  - Lavascape
  - Water
  - Mountains
  - Hills
  - Plains
  - Marsh
4. Click the **Generate** button.

### Heightmaps and colormaps

A **heightmap** is a 2D representation of a 3D terrain map, as viewed directly from above. Brighter areas of a heightmap result in higher terrain, like mountains, while darker areas result in lower regions, like valleys.

An optional **colormap**, along with a heightmap, converts colors to terrain materials using a **color key**.

![Example heightmap image](../assets/modeling/terrain/Terrain-Heightmap.png)_Heightmap_

![Example colormap image](../assets/modeling/terrain/Terrain-Colormap.png)_Colormap_

![Terrain generated from the example heightmap and colormap](../assets/modeling/terrain/Terrain-Colormap-Result.jpg)_Generated terrain_

1 pixel in a heightmap represents 4 studs in Studio, and Studio supports a maximum of 4096×4096 pixels in either `.jpg` or `.png` format.

To import a heightmap and optional colormap:

1. In the editor window, navigate to the **Create** tab and select the **Import** tool.![Import tool indicated in Create tab of Terrain Editor](../assets/studio/terrain-editor/Create-Tab-Import.png)
2. In the tool's **Map Settings** section, click the import button and choose the image you want to import as a heightmap.
3. In the tool's **Material Settings** section, select a terrain material or, alternatively, upload a colormap. #### Material To apply one consistent material across all of the generated terrain, select the **Material** tab and pick a terrain material. #### Colormap To apply a colormap, click the **Colormap** tab, click its import button, and choose the file to import. Colors on the image should match the following RGB/hex values and use hard edges, since anti‑aliasing or edge smoothing may create pixel colors outside the expected value ranges. The following table describes color mapping to a corresponding material. If your colormap contains a color that's not in the table, Studio chooses the closest matching material; for this reason, it is best to download the [`RobloxColorMapIndex`](../assets/modeling/terrain/RobloxColorMapIndex.png) file and directly sample its colors, or type the exact RGB/hex values into the color picker of your image editing application. | Material | RGB Value | Hex Value | Color |
| --- | --- | --- | --- | | `Enum.Material.Air\|Air` | `[255, 255, 255]` | `FFFFFF` | `rgb(255,255,255)` | | `Enum.Material.Asphalt\|Asphalt` | `[115, 123, 107]` | `737B6B` | `rgb(115,123,107)` | | `Enum.Material.Basalt\|Basalt` | `[30, 30, 37]` | `1E1E25` | `rgb(30,30,37)` | | `Enum.Material.Brick\|Brick` | `[138, 86, 62]` | `8A563E` | `rgb(138,86,62)` | | `Enum.Material.Cobblestone\|Cobblestone` | `[132, 123, 90]` | `847B5A` | `rgb(132,123,90)` | | `Enum.Material.Concrete\|Concrete` | `[127, 102, 63]` | `7F663F` | `rgb(127,102,63)` | | `Enum.Material.CrackedLava\|CrackedLava` | `[232, 156, 74]` | `E89C4A` | `rgb(232,156,74)` | | `Enum.Material.Glacier\|Glacier` | `[101, 176, 234]` | `65B0EA` | `rgb(101,176,234)` | | `Enum.Material.Grass\|Grass` | `[106, 127, 63]` | `6A7F3F` | `rgb(106,127,63)` | | `Enum.Material.Ground\|Ground` | `[102, 92, 59]` | `665C3B` | `rgb(102,92,59)` | | `Enum.Material.Ice\|Ice` | `[129, 194, 224]` | `81C2E0` | `rgb(129,194,224)` | | `Enum.Material.LeafyGrass\|LeafyGrass` | `[115, 132, 74]` | `73844A` | `rgb(115,132,74)` | | `Enum.Material.Limestone\|Limestone` | `[206, 173, 148]` | `CEAD94` | `rgb(206,173,148)` | | `Enum.Material.Mud\|Mud` | `[58, 46, 36]` | `3A2E24` | `rgb(58,46,36)` | | `Enum.Material.Pavement\|Pavement` | `[148, 148, 140]` | `94948C` | `rgb(148,148,140)` | | `Enum.Material.Rock\|Rock` | `[102, 108, 111]` | `666C6F` | `rgb(102,108,111)` | | `Enum.Material.Salt\|Salt` | `[198, 189, 181]` | `C6BDB5` | `rgb(198,189,181)` | | `Enum.Material.Sand\|Sand` | `[143, 126, 95]` | `8F7E5F` | `rgb(143,126,95)` | | `Enum.Material.Sandstone\|Sandstone` | `[137, 90, 71]` | `895A47` | `rgb(137,90,71)` | | `Enum.Material.Slate\|Slate` | `[63, 127, 107]` | `3F7F6B` | `rgb(63,127,107)` | | `Enum.Material.Snow\|Snow` | `[195, 199, 218]` | `C3C7DA` | `rgb(195,199,218)` | | `Enum.Material.WoodPlanks\|WoodPlanks` | `[139, 109, 79]` | `8B6D4F` | `rgb(139,109,79)` | | `Enum.Material.Water\|Water` | `[12, 84, 92]` | `0C545C` | `rgb(12,84,92)` |
4. In the 3D viewport, move/resize the **selection region** in which to generate terrain. Alternatively, enter values into the **Select** tool fields to set a more specific position and size.
  > **Info:** Minimum and maximum terrain heights depend on the darkest and lightest areas of the heightmap image in relation to the **Y** size (height) of the selection region. For instance, if you choose a height of 128, pure black areas are 64 studs below the center position and pure white areas are 64 studs above the center position.
5. Click the **Generate** button.

### Scripting

You can script terrain generation using the `Class.Terrain` class. For example, to create terrain with grass material that fills a volume, you can use methods such as `Class.Terrain:FillBall()|FillBall()`, `Class.Terrain:FillBlock()|FillBlock()`, `Class.Terrain:FillCylinder()|FillCylinder()`, `Class.Terrain:FillRegion()|FillRegion()`, or `Class.Terrain:FillWedge()|FillWedge()`.

```lua
local Workspace = game:GetService("Workspace")

Workspace.Terrain:FillBlock(CFrame.new(0, 0, 0), Vector3.new(4, 4, 4), Enum.Material.Grass)
```

## Large-scale editing

The editor's **Edit** tab contains tools for large-scale editing.

### Select regions

The **Select** tool is the universal tool for selecting rectangular regions of terrain.

![Select tool indicated in Edit tab of Terrain Editor](../assets/studio/terrain-editor/Edit-Tab-Select.png)

Select a region by clicking and dragging in the 3D viewport, reposition it with the **move** draggers, and edit its size with the **scale** handles. Alternatively, enter values into the tool's **X**/**Y**/**Z** inputs to set a specific position and size.

![Move draggers and scale handles on a selected region](../assets/studio/terrain-editor/Select-Region-Labeled.jpg)_Move draggers and scale handles on a selected region_

Studio also supports the following keyboard and mouse shortcuts, assuming the Select tool is active and nothing is selected in the **Explorer** window.

| Windows | Mac | Action |
| --- | --- | --- |
| `Ctrl``C` | `⌘``C` | Copy terrain within the selected region to the clipboard. |
| `Ctrl``V` | `⌘``V` | Paste terrain that has been copied to the clipboard and swap to the Transform tool so that the new terrain can be transformed. |
| `Ctrl``X` | `⌘``X` | Cut terrain within the selected region to the clipboard. |
| `Ctrl``D` | `⌘``D` | Duplicate terrain within the selected region and swap to the Transform tool so that the new terrain can be transformed. |
| `Delete` | `Delete` | Delete terrain within the selected region. |
| `Shift` | `Shift` | When held down while dragging any **scale** handle, scales the region proportionally across all other axes. |
| `Ctrl` | `⌘` | When held down while dragging any **scale** handle, scales the region equally in both the positive and negative direction along that axis. |

### Transform regions

The **Transform** tool lets you manipulate entire selected regions to a new position, size, or orientation.

To transform a region:

1. Select a region and then activate the **Transform** tool. Note that the tool will be automatically activated if you paste or duplicate terrain.![Transform tool indicated in Edit tab of Terrain Editor](../assets/studio/terrain-editor/Edit-Tab-Transform.png)
2. In the 3D viewport, transform the region with the **move** draggers, **rotate** rings, and **scale** handles. Alternatively, enter values into the tool's **X**/**Y**/**Z** inputs to set a specific position, size, and rotation.![Move draggers, scale handles, and rotate rings on the Y axis of a selected region](../assets/studio/terrain-editor/Transform-Region-Labeled.jpg)
  > **Info:** Holding `Shift` while dragging any **scale** handle scales the region proportionally across all other axes, and holding `Ctrl` or `⌘` while dragging scales the region equally in both the positive and negative direction along that axis.
>
> Holding `Shift` while dragging any **rotate** ring toggles between rotation snapping or free‑form rotation.
  > **Success:** By default, this tool uses **Live Edit** mode to constantly update terrain as you transform it. To view only a wireframe preview of the terrain as you transform it, disable live edit mode and then, while transforming, press `Enter`/`Return` or click the **Apply** button to apply the changes.

### Fill and replace regions

The **Fill** tool lets you fill an entire selected region with a specific material, or replace all material within the region with another material.

1. Select a region, then activate the **Fill** tool.![Fill tool indicated in Edit tab of Terrain Editor](../assets/studio/terrain-editor/Edit-Tab-Fill.png)
2. In the tool's **Material Settings** section:
  - To fill the region with a specific material, select **Fill** and choose the desired material.
  - To replace all terrain of one material with another material, select **Replace**, then choose a **source** material and **target** material.
3. Click the **Apply** button or press `Enter`/`Return`.![Region filled with Salt material](../assets/studio/terrain-editor/Fill-Region.jpg)_Selected region filled with Salt material_

### Set sea level

The **Sea Level** tool lets you create a consistent water level or remove all water within a region.

1. Activate the **Sea Level** tool.![Sea Level tool indicated in Edit tab of Terrain Editor](../assets/studio/terrain-editor/Edit-Tab-Sea-Level.png)
2. Select the intended region by clicking and dragging the **move** draggers and **scale** handles in the 3D viewport. Alternatively, enter values into the tool's **X**/**Y**/**Z** inputs to set a specific position and size.
3. Click the **Evaporate** button to remove water inside the selected region, or click the **Create** button to fill the selected region with water.

## Detailed editing

The **Edit** tab also contains tools for precision editing using a "brush" tool to draw, sculpt, smooth, flatten, or paint terrain.

![Detailed editing tools indicated in Edit tab of Terrain Editor](../assets/studio/terrain-editor/Edit-Tab-Detail-Tools.png)

Each tool lets you choose from a **sphere**, **box**, or **cylinder** brush shape and a base size between 1–64 studs.

![Brush shape and size controls in the Terrain Editor](../assets/studio/terrain-editor/Brush-Shape-Size.png)

For tools which use the brush, Studio supports the following keyboard and mouse shortcuts.

| Windows | Mac | Action |
| --- | --- | --- |
| `Ctrl` | `⌘` | When held down while using the [Draw](/docs/en-us/studio/terrain-editor.md#draw) and [Sculpt](/docs/en-us/studio/terrain-editor.md#sculpt) tools, toggles on the alternate brush mode. For example, toggles on "subtract" mode instead of the default "add" mode. |
| `Shift` | `Shift` | When held down while using the [Draw](/docs/en-us/studio/terrain-editor.md#draw) and [Sculpt](/docs/en-us/studio/terrain-editor.md#sculpt) tools, temporarily activates the [Smooth](/docs/en-us/studio/terrain-editor.md#smooth) tool. |
| `B` | `B` | When held down while dragging the mouse or using the scroll wheel, adjusts the brush's **base size**. |
| `Ctrl``B` | `⌘``B` | When held down while dragging the mouse or using the scroll wheel, adjusts the brush's **height**. Only applies if the brush's shape is set to **box** or **cylinder**. |
| `Shift``B` | `Shift``B` | When held down while dragging the mouse or using the scroll wheel, adjusts the brush's **strength**. Only applies when using the [Sculpt](/docs/en-us/studio/terrain-editor.md#sculpt), [Smooth](/docs/en-us/studio/terrain-editor.md#smooth), or [Flatten](/docs/en-us/studio/terrain-editor.md#flatten) tool. |
| `Alt` | `⌥` | When held down on mouse click, shows the material picker. |

### Draw

The **Draw** tool **adds** or **subtracts** terrain using the brush. This tool functions in a dual mode where holding down `Ctrl` or `⌘` toggles on "subtract" mode instead of the default "add" mode. Additionally, holding down `Shift` temporarily activates the [Smooth](/docs/en-us/studio/terrain-editor.md#smooth) tool.

### Sculpt

The **Sculpt** tool **adds** or **subtracts** terrain using the brush. Unlike the Draw tool, this tool includes a **strength** slider to allow for more gentle manipulation of terrain.

Similar to the Draw tool, the Sculpt tool functions in a dual mode where holding down `Ctrl` or `⌘` toggles on "subtract" mode instead of the default "add" mode. Additionally, holding down `Shift` temporarily activates the Smooth tool.

### Smooth

The **Smooth** tool smoothes out abrupt edges in terrain using the brush. This tool can be used in standalone mode, or you can toggle it on by holding `Shift` while using the Draw or Sculpt tools.

### Flatten

The **Flatten** tool flattens terrain to a consistent level across a visualized plane. By default, the tool lowers terrain above the plane **and** raises terrain below to the plane, but you can opt to selectively lower **or** raise through the tool's **Flatten Mode** option.

### Paint

The **Paint** tool, using the brush, **paints** a terrain material over an existing material or **replaces** one material with another material.
