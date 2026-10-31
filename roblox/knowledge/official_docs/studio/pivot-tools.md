---
title: "Pivot tools"
url: /docs/en-us/studio/pivot-tools
last_updated: 2026-10-30T19:55:57Z
description: "Pivot tools and properties give you full control over the points around which objects rotate and translate."
---

# Pivot tools

The **pivot** tools and related properties give you full control over the points around which objects rotate and translate.

## Interactive Studio tools

The interactive Studio tools are located in the **Model** tab toolbar.

![Pivot tool highlighted in Studio's toolbar.](../assets/studio/general/Toolbar-Pivot.png)

When **Pivot** is toggled on, you can move or rotate the pivot point of a [part](/docs/en-us/parts.md) or [model](/docs/en-us/parts/models.md). Once set, rotation and scaling occur around the pivot point. For more information, see [setting a primary part](/docs/en-us/parts/models.md#set-a-primary-part).

The following diagrams show example pivot locations in relation to object bounds.

#### Center

![A blue cube with its pivot point set in the center of the cube. A green circle represents the object's rotation in relation to its pivot point.](../assets/studio/pivot-tools/Edit-Pivot-Center-A.jpg)

#### Corner

![A blue cube with its pivot point set on a corner of the cube. A green circle represents the object's rotation in relation to its pivot point.](../assets/studio/pivot-tools/Edit-Pivot-Corner-A.jpg)

#### Outside Object Bounds

![A blue cube with its pivot point set on outside of the cube's geometry. A green circle represents the object's rotation in relation to its pivot point.](../assets/studio/pivot-tools/Edit-Pivot-Outside-A.jpg)

When you rotate the pivot of a [model](/docs/en-us/parts/models.md), the bounding box of the model also rotates.

#### Orientation = (0, 90, 0)

![A model of a purple, blue, and red block with its pivot point set on a the edge of the model's bounding box. A green circle represents the object's rotation in relation to its pivot point.](../assets/studio/pivot-tools/Edit-Pivot-Model-A.jpg)

#### Orientation = (0, 135, 0)

#### Orientation = (0, 180, 0)

You can specify a `Class.Model.PrimaryPart|PrimaryPart` for models, which is a `Class.BasePart` within the model that you can use as a positional basis. In terms of pivot points:

1. When you assign a `Class.Model.PrimaryPart|PrimaryPart` to a model, the existing pivot changes to the pivot point of the `Class.Model.PrimaryPart|PrimaryPart`. If you later unassign/clear the `Class.Model.PrimaryPart|PrimaryPart`, the pivot point resets to the **center** of the model's bounding box.
2. If you **delete** the `Class.Model.PrimaryPart|PrimaryPart` from a model, the pivot point remains in the same location and does **not** revert to its previous position. This prevents a sudden "jump" if you delete any parts from the model.

#### Initial Pivot Point

#### A. PrimaryPart Assigned

#### B. PrimaryPart Deleted

### Snap

The **Snap** checkbox, available by click‑holding the small corner arrow on the **Pivot** button, toggles whether the pivot point snaps to **hotspots** such as corners, edges, or centers when you move it with the **Edit Pivot** tool. When snapping is enabled, hotspots display as small magenta points.

_Hotspots on a part_

_Hotspots on a model_

### Reset

The **Reset** button moves the pivot point to the **center** of an object or model's bounding box. This operation is useful after you've changed the composition of a model and wish to place its pivot point at the center of its new bounding box.

![Pivot Reset tool highlighted in Studio's toolbar.](../assets/studio/general/Toolbar-Pivot-Reset.png) ## Pivot properties

In addition to the interactive tools, pivot values can be directly set in the [Properties](/docs/en-us/studio/properties.md) window.

| Property | Description |
| --- | --- |
| **Origin Position** | Current world location of the object based on its pivot point rather than its bounding box. Useful for setting the precise location of a `Class.Model`. |
| **Origin Orientation** | Current orientation of the object based around its pivot point rather than its bounding box. |
| **Pivot Offset Position** | Precise location of the pivot relative to the object.¹ |
| **Pivot Offset Orientation** | Precise pivot orientation.¹ |
| **World Pivot Position** | The precise world location of the pivot for `Class.Model\|Models` without a `Class.Model.PrimaryPart\|PrimaryPart`. If a `Class.Model.PrimaryPart\|PrimaryPart` is set, the model will use **Pivot Offset Position** since the pivot becomes relative to that part.¹ |
| **World Pivot Orientation** | The precise world orientation for `Class.Model\|Models` without a `Class.Model.PrimaryPart\|PrimaryPart`. If a `Class.Model.PrimaryPart\|PrimaryPart` is set, the model will use **Pivot Offset Orientation** since the pivot becomes relative to that part.¹ |

_<sup>1</sup> Changing this property will not move or rotate the object._## Manipulate pivots in scripts

Beyond the Studio tools, pivot points can be accessed and manipulated in scripts.

| Function or Property | Description |
| --- | --- |
| `Class.PVInstance:GetPivot()\|GetPivot()` | Queries the current world location of an object's pivot as a `Datatype.CFrame`. This returns an object's position in 3D space regardless of whether it's an individual part or a `Class.Model`. |
| `Class.PVInstance:PivotTo()\|PivotTo()` | Moves the object such that its pivot will be located at the specified `Datatype.CFrame`. This allows for uniform object movement of both individual parts and models. |
| `Class.BasePart.PivotOffset` | The `Datatype.CFrame` which specifies the pivot offset; effectively the offset of the pivot from the `Datatype.CFrame` of the `Class.BasePart`.² |
| `Class.BasePart.PivotOffset\|Model.WorldPivot` | For `Class.Model\|Models` without a `Class.Model.PrimaryPart\|PrimaryPart`, the `Datatype.CFrame` which specifies the model's pivot in world space. If a `Class.Model.PrimaryPart\|PrimaryPart` is set, the model will use `Class.BasePart.PivotOffset` since the pivot becomes relative to that part.² |

_<sup>2</sup> Changing this property will not move or rotate the object._
