---
name: WrapLayerDebugMode
last_updated: 2026-10-30T19:55:54Z
type: enum
summary: "The Studio-only property for quickly visualizing and debugging meshes with inner cage and outer cages."
---

# WrapLayerDebugMode

The Studio-only property for quickly visualizing and debugging meshes with
inner cage and outer cages.

**Type:** enum

## Description

The Studio-only property for quickly visualizing and debugging meshes with
inner and outer cages.

This debug visualization only works when the WrapLayer is active and does not
work if WrapLayer is not active or incorrectly configured.

## Items

| Name | Value | Description |
|------|-------|-------------|
| `None` | 0 | This debug rendering mode does nothing. This is the default value. |
| `BoundCage` | 1 | This debug mode visualizes corresponding cage mesh vertices bound to an underlying [WrapTarget](/docs/reference/engine/classes/WrapTarget.md). In order to find corresponding vertices between different cages, the Wrap Deformer algorithm uses UV matching. As long as your [WrapLayer](/docs/reference/engine/classes/WrapLayer.md) cage mesh share the same UV layout as [WrapTarget](/docs/reference/engine/classes/WrapTarget.md), its vertices will be marked as "bound". |
| `LayerCage` | 2 | This debug mode shows the resulting layer mesh as a whole. The deformer will use vertex locations from the previous layer for all unbound vertices. |
| `BoundCageAndLinks` | 3 | The same as BoundCage but also visualizes how bound vertices were moved. You can use this mode to identify where they belong on a previous layer and where they are located on the current layer. |
| `Reference` | 4 | This debug mode shows the original inner cage mesh as it was created. |
| `Rbf` | 5 | This debug mode visualizes the internal RBF solver state. You can estimate the wrap deformer's expected behavior by looking at this state. All renderable mesh vertices move from a "big sphere" to a "small sphere" along a corresponding line connecting two spheres. |
| `OuterCage` | 6 | This debug mode shows the original outer cage mesh as it was created. |
| `ReferenceMeshAfterMorph` | 7 | Renders the layer's outer cage after the morph step that aligns it to the previous layer's outer cage surface, prior to HSR processing. |
| `HSROuterDetail` | 8 | Interactive mode that highlights the render-mesh triangle under the cursor and draws the corresponding outer cage vertices on the layer above using HSR association data. |
| `HSROuter` | 9 | Highlights outer cage vertices that HSR associates with visible render-mesh faces. |
| `HSRInner` | 10 | Highlights inner cage vertices that Hidden Surface Removal (HSR) classifies as occluded by the clothing layer above, drawn at the previous layer's outer-cage positions. |
| `HSRInnerReverse` | 11 | Highlights inner cage vertices that HSR classifies as visible (not occluded), the complement of [WrapLayerDebugMode.HSRInner](/docs/reference/engine/enums/WrapLayerDebugMode.md). |
| `LayerCageFittedToBase` | 12 | Renders the layer's outer cage at positions from fitting it to the base body mesh (rest pose), shown as spheres and wireframe edges. |
| `LayerCageFittedToPrev` | 13 | Renders the layer's outer cage at positions from fitting it to the previous layer's deformed shape, shown as spheres and wireframe edges. |
| `PreWrapDeformerOuterCage` | 14 | Draws each outer cage vertex that moved during deformation as a sphere at its pre-deformation position connected by a line to its post-deformation position. |
| `SkinningTransfer` | 15 | Visualizes per-vertex skinning weight transfer for the layer mesh, drawing lines from each mesh vertex to its influencing skeleton joints. |