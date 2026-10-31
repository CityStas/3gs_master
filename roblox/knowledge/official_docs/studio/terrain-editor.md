---
title: "Terrain Editor"
url: /docs/en-us/studio/terrain-editor
last_updated: 2026-10-30T19:55:57Z
description: "The Terrain Editor tools generate and sculpt realistic terrain environments such as mountains, bodies of water, grass-covered hills, or a flat desert."
---

# Terrain Editor

The **Terrain Editor**, accessible from Studio's **Home** tab or **Window** ⟩ **3D** menu, lets you generate and manipulate [environmental terrain](/docs/en-us/parts/terrain.md) through its [Create](#create-tab) and [Edit](#edit-tab) toolsets.

![Terrain Editor indicated in Studio's toolbar](../assets/studio/general/Toolbar-Terrain-Editor.png)
> **Success:** For detailed instructions on working with terrain, see the [environmental terrain](/docs/en-us/parts/terrain.md) guide. To paint up to 62 custom materials onto terrain, see [Custom terrain materials](/docs/en-us/parts/custom-terrain-materials.md).
## Create tab

The **Create** tab includes the [Import](#import), [Generate](#generate), and [Clear](#clear) tools.

### Import

The **Import** tool imports a [heightmap](/docs/en-us/parts/terrain.md#heightmaps-and-colormaps) and optional [colormap](/docs/en-us/parts/terrain.md#heightmaps-and-colormaps) and applies them to a selected region.

![Import tool indicated in Create tab of Terrain Editor](../assets/studio/terrain-editor/Create-Tab-Import.png)

![Example heightmap image](../assets/modeling/terrain/Terrain-Heightmap.png)_Heightmap_

![Example colormap image](../assets/modeling/terrain/Terrain-Colormap.png)_Colormap_

![Terrain generated from the example heightmap and colormap](../assets/modeling/terrain/Terrain-Colormap-Result.jpg)_Generated terrain_

| Selection settings |
| --- |
| Size, position, and snapping options as outlined for the [Select](#select) tool. |
| Heightmap settings |
| **Heightmap** | Imports a heightmap from a local image file. |
| **Colormap** | Imports a colormap from a local image file to use alongside a heightmap. |
| **Default Material** | Specifies one consistent material to apply across all of the generated terrain. This is overridden by materials based on the colormap, if imported. |

### Generate

The **Generate** tool procedurally generates terrain within a selected region. This is useful if you want to create a large map and then fine-tune terrain details using the [Edit](#edit-tab) tab tools.

![Generate tool indicated in Create tab of Terrain Editor](../assets/studio/terrain-editor/Create-Tab-Generate.png)

| Selection settings |
| --- |
| Size, position, and snapping options as outlined for the [Select](#select) tool. |
| Biome settings |
| **Biomes** | Includes the selected biomes in the generated terrain. |
| **Blending** | Adjusts how the biomes blend into one another, with higher values a bit smoother. |
| **Caves** | Includes caves in the generated terrain. |
| **Biome Size** | Sets the size of the biomes within the overall terrain size. |
| **Seed** | A number that Studio generates to determine the shape of the terrain. When you change this number, Studio generates a new terrain with the same settings. |

### Clear

The **Clear** tool reveals a button that clears all terrain within the entire place.

![Clear tool indicated in Create tab of Terrain Editor](../assets/studio/terrain-editor/Create-Tab-Clear.png) ## Edit tab

The **Edit** tab includes the [Select](#select), [Transform](#transform), [Fill](#fill), [Sea Level](#sea-level), [Draw](#draw), [Sculpt](#sculpt), [Smooth](#smooth), [Paint](#paint), and [Flatten](#flatten) tools.

### Select

The **Select** tool is a universal tool for selecting rectangular regions of terrain. With the tool enabled, select a region by clicking and dragging in the 3D viewport, reposition it with the **move** draggers, and edit its size with the **scale** handles. Alternatively, enter values into the tool's **X**/**Y**/**Z** inputs to set a specific position and size.

![Select tool indicated in Edit tab of Terrain Editor](../assets/studio/terrain-editor/Edit-Tab-Select.png)

| Selection settings |
| --- |
| **Size** | Sets specific **X**/**Y**/**Z** values for the selection's size, in studs. |
| **Position** | Sets specific **X**/**Y**/**Z** values for the selection's position. |
| **Snap to Voxels** | Snaps the selection bounds to the nearest voxel. |

![Move draggers and scale handles on a selected region](../assets/studio/terrain-editor/Select-Region-Labeled.jpg)_Move draggers and scale handles on a selected region_

Studio also supports the following keyboard and mouse shortcuts, assuming the **Select** tool is active and nothing is selected in the [Explorer](/docs/en-us/studio/explorer.md) hierarchy.

| Windows | Mac | Action |
| --- | --- | --- |
| `Ctrl``C` | `⌘``C` | Copy terrain within the selected region to the clipboard. |
| `Ctrl``V` | `⌘``V` | Paste terrain that has been copied to the clipboard and swap to the [Transform](#transform) tool so that the new terrain can be transformed. |
| `Ctrl``X` | `⌘``X` | Cut terrain within the selected region to the clipboard. |
| `Ctrl``D` | `⌘``D` | Duplicate terrain within the selected region and swap to the [Transform](#transform) tool so that the new terrain can be transformed. |
| `Delete` | `Delete` | Delete terrain within the selected region. |
| `Shift` | `Shift` | When held down while dragging any **scale** handle, scales the region proportionally across all other axes. |
| `Ctrl` | `⌘` | When held down while dragging any **scale** handle, scales the region equally in both the positive and negative direction along that axis. |

### Transform

The **Transform** tool manipulates entire [selected](#select) regions to a new position, size, or orientation. With the tool enabled, transform a selected region with the **move** draggers, **rotate** rings, and **scale** handles. Alternatively, enter values into the tool's **X**/**Y**/**Z** inputs to set a specific position, size, and rotation.

![Transform tool indicated in Edit tab of Terrain Editor](../assets/studio/terrain-editor/Edit-Tab-Transform.png)

| Transform settings |
| --- |
| **Size** | Sets specific **X**/**Y**/**Z** values for the selection's size in studs. |
| **Position** | Sets specific **X**/**Y**/**Z** values for the selection's position. |
| **Rotation** | Sets specific **X**/**Y**/**Z** values for the selection's rotation in degrees. |
| **Merge Empty** | When enabled, air voxels in the selection will overwrite existing voxels at the destination. |
| **Live Edit** | When enabled, terrain is constantly updated while being transformed. To view only a wireframe preview of the transformation, disable live edit mode and then, while transforming, press `Enter`/`Return` or click the **Apply** button to apply the changes. |
| **Snap to Voxels** | Snaps the selection bounds to the nearest voxel. |

![Move draggers, rotate rings, and scale handles on a selected region](../assets/studio/terrain-editor/Transform-Region-Labeled.jpg)_Move draggers, rotate rings, and scale handles on a selected region_

> **Warning:** Before rotating a region with the visual **rotate** rings, check the rotation snapping setting in Studio's toolbar. Disable rotation snapping entirely for free-form rotation.
> **Info:** Similar to [selecting](#select) a region, holding `Shift` while dragging any **scale** handle scales the region proportionally across all other axes, and holding `Ctrl` or `⌘` while dragging scales the region equally in both the positive and negative direction along that axis.
### Fill

The **Fill** tool fills an entire [selected](#select) region with a specific material, or replaces all material within the region with another material.

![Fill tool indicated in Edit tab of Terrain Editor](../assets/studio/terrain-editor/Edit-Tab-Fill.png)

| Selection settings |
| --- |
| Size, position, and snapping options as outlined for the [Select](#select) tool. |
| Material settings |
| **Fill Mode** | Toggles the tool between **Fill** and **Replace** mode. |
| **Source Material** | In **Fill** mode, the desired fill material. In **Replace** mode, the material to replace. |
| **Target Material** | In **Replace** mode, the material to replace the source material with. |

![Region filled with Salt material](../assets/studio/terrain-editor/Fill-Region.jpg)_Selected region filled with Salt material_

### Sea Level

The **Sea Level** tool lets you create a consistent water level or remove all water within a region.

![Sea Level tool indicated in Edit tab of Terrain Editor](../assets/studio/terrain-editor/Edit-Tab-Sea-Level.png)

| Sea level settings |
| --- |
| **Size** | Sets specific **X**/**Y**/**Z** values for the selection's size in studs. |
| **Position** | Sets specific **X**/**Y**/**Z** values for the selection's position. |
| **Snap to Voxels** | Snaps the selection bounds to the nearest voxel. |

### Draw

The **Draw** tool **adds** or **subtracts** terrain using the brush. This tool functions in a dual mode where holding down `Ctrl` or `⌘` toggles on "subtract" mode instead of the default "add" mode. Additionally, holding down `Shift` temporarily activates the [Smooth](#smooth) tool.

![Draw tool indicated in Edit tab of Terrain Editor](../assets/studio/terrain-editor/Edit-Tab-Draw.png)

| Brush settings |
| --- |
| **Brush Mode** | Toggles the tool between **Add** and **Subtract** mode. Also toggled by holding down `Ctrl` or `⌘`. |
| **Brush Shape** | Sets the brush shape to either a **sphere**, **box**, or **cylinder**.<br>![Brush shape icons in the Terrain Editor](../assets/studio/terrain-editor/Brush-Shape-Icons.png) |
| **Brush Size** | Sets the brush size from 1 to 64. If you choose a brush shape of **box** or **cylinder**, a **Height** slider/input also appears to adjust the brush height proportionally or independently of the base size. |
| **Pivot Position** | Sets the vertical pivot point of the brush to either the bottom, center, or top of where the brush connects with existing terrain. |
| **Snapping** | Whether snapping is off or to the nearest voxel. |
| **Plane Lock** | Toggles whether to enable a visual plane which the brush locks to. In **Auto** mode, the plane tilts and rotates with the camera. In **Manual** mode, the **Edit Plane** option appears, letting you set a specific position/orientation through the visual draggers or **X**/**Y**/**Z** inputs. |
| **Ignore Water** | Ignores water when adding or subtracting terrain. |
| **Ignore Parts** | Ignores [parts](/docs/en-us/parts.md) in regards to brush placement while moving the mouse pointer across part surfaces. |
| Material settings |
| **Auto Material** | Uses the same terrain material in the brush's vicinity when adding new terrain. |
| **Source Material** | Sets the [material](/docs/en-us/parts/terrain.md#terrain-materials) for **Add** mode. |

### Sculpt

The **Sculpt** tool **adds** or **subtracts** terrain using the brush. Unlike the [Draw](#draw) tool, this tool includes a **strength** slider/input to allow for more gentle manipulation of terrain. This tool functions in a dual mode where holding down `Ctrl` or `⌘` toggles on "subtract" mode instead of the default "add" mode, and holding down `Shift` temporarily activates the [Smooth](#smooth) tool.

![Sculpt tool indicated in Edit tab of Terrain Editor](../assets/studio/terrain-editor/Edit-Tab-Sculpt.png)

| Option | Description |
| --- | --- |
| **Brush Mode** | Toggles the tool between **Add** and **Subtract** mode. Also toggled by holding down `Ctrl` or `⌘`. |
| **Brush Shape** | Sets the brush shape to either a **sphere**, **box**, or **cylinder**.<br>![Brush shape icons in the Terrain Editor](../assets/studio/terrain-editor/Brush-Shape-Icons.png) |
| **Brush Size** | Sets the brush size from 1 to 64. If you choose a brush shape of **box** or **cylinder**, a **Height** slider/input also appears to adjust the brush height proportionally or independently of the base size. |
| **Strength** | Sets the brush strength from 0.1 to 1. |
| **Plane Lock** | Toggles whether to enable a visual plane which the brush locks to. In **Auto** mode, the plane tilts and rotates with the camera. In **Manual** mode, the **Edit Plane** option appears, letting you set a specific position/orientation through the visual draggers or **X**/**Y**/**Z** inputs. |
| **Ignore Water** | Ignores water when adding or subtracting terrain. |
| **Ignore Parts** | Ignores [parts](/docs/en-us/parts.md) in regards to brush placement while moving the mouse pointer across part surfaces. |
| **Auto Material** | Uses the same terrain material in the brush's vicinity when adding new terrain. |
| **Source Material** | Sets the [material](/docs/en-us/parts/terrain.md#terrain-materials) for **Add** mode. |

### Smooth

The **Smooth** tool smoothes out abrupt edges in terrain using the brush. This tool can be used in standalone mode, or you can toggle it on by holding `Shift` while using the [Draw](#draw) or [Sculpt](#sculpt) tools.

![Smooth tool indicated in Edit tab of Terrain Editor](../assets/studio/terrain-editor/Edit-Tab-Smooth.png)

| Option | Description |
| --- | --- |
| **Brush Shape** | Sets the brush shape to either a **sphere**, **box**, or **cylinder**.<br>![Brush shape icons in the Terrain Editor](../assets/studio/terrain-editor/Brush-Shape-Icons.png) |
| **Brush Size** | Sets the brush size from 1 to 64. If you choose a brush shape of **box** or **cylinder**, a **Height** slider/input also appears to adjust the brush height proportionally or independently of the base size. |
| **Strength** | Sets the brush strength from 0.1 to 1. |
| **Pivot Position** | Sets the vertical pivot point of the brush to either the bottom, center, or top of where the brush connects with existing terrain. |
| **Snapping** | Whether snapping is off or to the nearest voxel. |
| **Plane Lock** | Toggles whether to enable a visual plane which the brush locks to. In **Auto** mode, the plane tilts and rotates with the camera. In **Manual** mode, the **Edit Plane** option appears, letting you set a specific position/orientation through the visual draggers or **X**/**Y**/**Z** inputs. |
| **Ignore Water** | Ignores water when smoothing terrain. |
| **Ignore Parts** | Ignores [parts](/docs/en-us/parts.md) in regards to brush placement while moving the mouse pointer across part surfaces. |

### Paint

The **Paint** tool, using the brush, **paints** a terrain [material](/docs/en-us/parts/terrain.md#terrain-materials) over an existing material or **replaces** one material with another material.

![Paint tool indicated in Edit tab of Terrain Editor](../assets/studio/terrain-editor/Edit-Tab-Paint.png)

| Option | Description |
| --- | --- |
| **Brush Shape** | Sets the brush shape to either a **sphere**, **box**, or **cylinder**.<br>![Brush shape icons in the Terrain Editor](../assets/studio/terrain-editor/Brush-Shape-Icons.png) |
| **Brush Size** | Sets the brush size from 1 to 64. If you choose a brush shape of **box** or **cylinder**, a **Height** slider/input also appears to adjust the brush height proportionally or independently of the base size. |
| **Pivot Position** | Sets the vertical pivot point of the brush to either the bottom, center, or top of where the brush connects with existing terrain. |
| **Snapping** | Whether snapping is off or to the nearest voxel. |
| **Plane Lock** | Toggles whether to enable a visual plane which the brush locks to. In **Auto** mode, the plane tilts and rotates with the camera. In **Manual** mode, the **Edit Plane** option appears, letting you set a specific position/orientation through the visual draggers or **X**/**Y**/**Z** inputs. |
| **Ignore Water** | Ignores water when flattening terrain. |
| **Ignore Parts** | Ignores [parts](/docs/en-us/parts.md) in regards to brush placement while moving the mouse pointer across part surfaces. |
| **Material Mode** | Toggles the tool between **Paint** and **Replace** mode. In **Paint** mode, choose the desired painting material from the tool's picker tiles. In **Replace** mode, choose both the **source** material to replace and the **target** material to replace it with. |

### Flatten

The **Flatten** tool flattens terrain to a consistent level across a visualized plane. By default, the tool lowers terrain above the plane **and** raises terrain below to the plane, but you can opt to selectively lower **or** raise through the tool's **Flatten Mode** option.

![Flatten tool indicated in Edit tab of Terrain Editor](../assets/studio/terrain-editor/Edit-Tab-Flatten.png)

| Option | Description |
| --- | --- |
| **Brush Shape** | Sets the brush shape to either a **sphere**, **box**, or **cylinder**.<br>![Brush shape icons in the Terrain Editor](../assets/studio/terrain-editor/Brush-Shape-Icons.png) |
| **Flatten Mode** | **Erode to Flat**¹ flattens terrain above the plane. **Grow to Flat**² fills in terrain below the plane. **Flatten All**³ removes terrain above the plane and fills in terrain below the plane.<br>![Flatten Mode icons in the Terrain Editor](../assets/studio/terrain-editor/Flatten-Mode-Icons.png) |
| **Brush Size** | Sets the brush size from 1 to 64. If you choose a brush shape of **box** or **cylinder**, a **Height** slider/input also appears to adjust the brush height proportionally or independently of the base size. |
| **Strength** | Sets the brush strength from 0.1 to 1. |
| **Pivot Position** | Sets the vertical pivot point of the brush to either the bottom, center, or top of where the brush connects with existing terrain. |
| **Snapping** | Whether snapping is off or to the nearest voxel. |
| **Flatten Plane** | If set to **Fixed**, flattens terrain to a fixed visual plane in **Y** world space. |
| **Ignore Water** | Ignores water when flattening terrain. |
| **Ignore Parts** | Ignores [parts](/docs/en-us/parts.md) in regards to brush placement while moving the mouse pointer across part surfaces. |

## Studio shortcuts

For tools which use the **brush** ([Draw](#draw), [Sculpt](#sculpt), [Smooth](#smooth), [Flatten](#flatten), [Paint](#paint)), Studio supports the following keyboard and mouse shortcuts.

| Windows | Mac | Action |
| --- | --- | --- |
| `Ctrl` | `⌘` | When held down while using the [Draw](#draw) and [Sculpt](#sculpt) tools, toggles on the alternate brush mode. For example, toggles on "subtract" mode instead of the default "add" mode. |
| `Shift` | `Shift` | When held down while using the [Draw](#draw) and [Sculpt](#sculpt) tools, temporarily activates the [Smooth](#smooth) tool. |
| `B` | `B` | When held down while dragging the mouse or using the scroll wheel, adjusts the brush's **base size**. |
| `Ctrl``B` | `⌘``B` | When held down while dragging the mouse or using the scroll wheel, adjusts the brush's **height**. Only applies if the brush's shape is set to **box** or **cylinder**. |
| `Shift``B` | `Shift``B` | When held down while dragging the mouse or using the scroll wheel, adjusts the brush's **strength**. Only applies when using the [Sculpt](#sculpt), [Smooth](#smooth), or [Flatten](#flatten) tool. |
| `Alt` | `⌥` | When held down on mouse click, shows the material picker. |
