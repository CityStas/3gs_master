---
title: "2D paths"
url: /docs/en-us/ui/2D-paths
last_updated: 2026-10-30T19:56:01Z
description: "The Path2D instance, along with its API methods and properties, lets you implement 2D splines and 2D curved lines."
---

# 2D paths

The `Class.Path2D` instance, along with its API methods and properties, lets you implement 2D splines and 2D curved lines, useful for UI effects like path‑based animations and graph editors.

## Create a 2D path

To add a `Class.Path2D` to the screen or an in-game object:

1. In the [Explorer](/docs/en-us/studio/explorer.md) window, insert a `Class.Path2D` instance under a visible `Class.ScreenGui` or `Class.SurfaceGui` (it does not need to be a direct child).![Path2D instance parented to a ScreenGui in the Explorer hierarchy.](../assets/studio/explorer/StarterGui-ScreenGui-Path2D.png)
2. Select the new `Class.Path2D` to reveal the in-viewport tooling widget. By default, the **Add Point** tool is selected.![Add Point tool indicated in the 2D path editor widget.](../assets/ui/2D-paths/Widget-Add-Point.png)
3. Begin clicking on the screen to add a series of **control points** to form a path. The initial path will likely be imprecise but you can [fine‑tune](#move-points) the position of any control point later.![Diagram illustrating an example path created using the Add Point tool to connect a series of points.](../assets/ui/2D-paths/Path-Example-Create-Basic.png)
  > **Info:** If you drag the mouse after clicking, [tangents](#control-point-tangents) will be created on that point. Tangents can also be procedurally [added](#add-tangents) to any control point.
4. When finished, click the widget's **Done** button or press `Enter`.

## Modify control points

With a `Class.Path2D` selected in the [Explorer](/docs/en-us/studio/explorer.md) hierarchy, you can modify its individual control points as well as their [tangents](#control-point-tangents).

### Move points

To move an individual control point on a path, enable the **Select** tool (`V`) and then click‑and‑drag it to a new position.

![Select tool indicated in the 2D path editor widget.](../assets/ui/2D-paths/Widget-Select.png)![Diagram illustrating how a path control point is moved to a new position by clicking and dragging with the Select tool enabled.](../assets/ui/2D-paths/Path-Example-Move-Point.png)

For very specific positioning, select the control point and then, in the [Properties](/docs/en-us/studio/properties.md) window, set a new position for the point's `Class.Path2D.SelectedControlPointData|SelectedControlPointData` property (`Datatype.UDim2`).

![SelectedControlPointData property of a Path2D instance indicated in the Properties window.](../assets/studio/properties/Path2D-SelectedControlPointData.png)

Note that a point's position is not absolute, but rather **relative** to the path's parent container. For example, compare a control point 30% from left and 20% from top for a path inside a `Class.ScreenGui`, versus an identical path placed inside a `Class.Frame` located in the upper‑right corner of the `Class.ScreenGui`.

![Diagram illustrating how the positions of path control points are relative to their parent container.](../assets/ui/2D-paths/Control-Point-Relativity.png) ### Add points

New control points can be added to a `Class.Path2D` either between two existing points or from either end point using the **Add Point** tool (`P`).

![Add Point tool indicated in the 2D path editor widget.](../assets/ui/2D-paths/Widget-Add-Point.png)

![Diagram illustrating how a control point is added between two existing points using the Add Point tool.](../assets/ui/2D-paths/Path-Example-Add-Point-Between.png)_Hover anywhere over the path and click to add a control point between two existing points_

![Diagram illustrating how a control point is added to the end of a path using the Add Point tool.](../assets/ui/2D-paths/Path-Example-Add-Point-From-End.png)_Click on an end point and then click again to add a control point from that end_

> **Info:** Remember that if you drag the mouse after clicking to add a new control point, [tangents](#control-point-tangents) will be created on that point.
### Delete points

To delete a control point, hover over and right‑click it, then select **Delete Point** from the contextual popup menu.

![Diagram illustrating how a path control point is deleted by right-clicking it and selecting Delete Point.](../assets/ui/2D-paths/Path-Example-Delete-Point.png) ### Control point tangents

Control point **tangents** let you create and adjust curves on a path.

![Diagram illustrating a curved path with several tangent control points.](../assets/ui/2D-paths/Tangents.png) #### Add tangents

To add tangents to any control point that doesn't already have tangents:

1. Enable the **Add Tangent** tool in the tooling widget.![Add Tangent tool indicated in the 2D path editor widget.](../assets/ui/2D-paths/Widget-Add-Tangent.png)
2. Hover over the desired control point, then click to add two [mirrored](#break-and-mirror) tangents (optionally drag after clicking to [adjust](#adjust-tangents) the new tangents).![Diagram illustrating how a path control point with tangents is created with the Add Tangent tool.](../assets/ui/2D-paths/Path-Example-Add-Tangent.png)

#### Adjust tangents

To adjust existing tangents for an individual control point:

1. Enable the **Select** tool (`V`).![Select tool indicated in the 2D path editor widget.](../assets/ui/2D-paths/Widget-Select.png)
2. Hover over a tangent marker (not the control point), then click‑and‑drag it to a new position. If the tangents are mirrored, the paired tangent point will move in unison.![Diagram illustrating how the tangents of a control point are adjusted with the Select tool enabled.](../assets/ui/2D-paths/Path-Example-Adjust-Tangent.png)

To manually set a specific `Datatype.UDim2` position for a tangent:

1. Enable the **Select** tool (`V`) and select the control point. In the [Properties](/docs/en-us/studio/properties.md) window, expand the `Class.Path2D.SelectedControlPointData|SelectedControlPointData` field to expose the `Datatype.Path2DControlPoint.LeftTangent|LeftTangent` and `Datatype.Path2DControlPoint.RightTangent|RightTangent` properties.![LeftTangent and RightTangent properties of a Path2D control point indicated in the Properties window.](../assets/studio/properties/Path2D-SelectedControlPointData-Expanded.png)
2. Set the position for `Datatype.Path2DControlPoint.LeftTangent|LeftTangent` and/or `Datatype.Path2DControlPoint.RightTangent|RightTangent`. Note that this will [break the mirrored behavior](#break-and-mirror) of the tangents.

#### Delete tangents

To delete both tangents from a control point, hover over and right-click that point, then select **Clear Tangents** from the contextual popup menu.

![Diagram illustrating how both tangents of a control point are cleared by right-clicking it and selecting Clear Tangents.](../assets/ui/2D-paths/Path-Example-Clear-Tangents.png)

To delete just one of the tangents (left or right), hover over and right‑click that tangent's marker, then select **Delete Tangent**.

![Diagram illustrating how one tangent of a control point is deleted by right-clicking it and selecting Delete Tangent.](../assets/ui/2D-paths/Path-Example-Delete-Tangent.png) #### Break and mirror

By default, tangents mirror each other. When you [drag to adjust](#adjust-tangents) one tangent marker, the paired tangent point will move in unison.

![Diagram illustrating how the tangents of a control point are adjusted with the Select tool enabled.](../assets/ui/2D-paths/Path-Example-Adjust-Tangent.png)

To "break" the tangents so that each can be moved independently of the other, hover over and right‑click the associated control point, then select **Break Tangents** from the contextual menu. Once broken, you can move each tangent marker without affecting the other.

![Diagram illustrating how the tangents of a control point are broken by right-clicking it and selecting Break Tangents.](../assets/ui/2D-paths/Path-Example-Break-Tangents.png)
> **Info:** To re-establish mirror behavior, hover over and right‑click the associated control point, then select **Mirror Tangents** from the contextual menu. Note that you will **not** see an immediate change in the path after re‑establishing mirror behavior, as the system cannot predict which tangent point you want to begin mirroring. Mirror behavior will resume only once you [drag to adjust](#adjust-tangents) one of the tangent markers.
## Path visual properties

You can customize the visual appearance of a `Class.Path2D` with the following properties:

| Property | Description |
| --- | --- |
| `Class.Path2D.Color3\|Color3` | Sets the color of the path line. |
| `Class.Path2D.Thickness\|Thickness` | Sets the thickness of the path line, in pixels. |
| `Class.Path2D.Visible\|Visible` | Make the path visible or not in both edit and runtime. |
| `Class.Path2D.ZIndex\|ZIndex` | Order in which a path renders relative to other GUIs. |

![Diagram illustrating a path with Thickness of 2 and Color3 of (125, 125, 125).](../assets/ui/2D-paths/Path-Example-Thin-Grey.png)_Thickness = 2Color3 = (125, 125, 125)_

![Diagram illustrating a path with Thickness of 10 and Color3 of (225, 0, 50).](../assets/ui/2D-paths/Path-Example-Thick-Red.png)_Thickness = 10Color3 = (225, 0, 50)_

![Diagram illustrating a path layered in front of another using the ZIndex property.](../assets/ui/2D-paths/Path-Example-ZIndex-Layering.png)_ZIndex layering_

## Path scripting

Scripting is useful for several path-related workflows. The following examples use methods such as `Class.Path2D:GetControlPoints()|GetControlPoints()` which returns a table of `Datatype.Path2DControlPoint|Path2DControlPoints` and `Class.Path2D:GetPositionOnCurveArcLength()|GetPositionOnCurveArcLength()` which returns the `Datatype.UDim2` position at a given `t` value along the spline.

```lua
local parent = script.Parent
local path = parent:FindFirstChildWhichIsA("Path2D")

local function arrangeChildren()
	local segmentCount = #path:GetControlPoints()
	local objectsToArrange = {}

	for _, child in parent:GetChildren() do
		if child:IsA("GuiObject") then
			table.insert(objectsToArrange, child)
		end
	end

	for idx, child in objectsToArrange do
		local t = idx / (#objectsToArrange + 1)
		child.Position = path:GetPositionOnCurveArcLength(t)
	end
end

-- Initially arrange child UI objects across path
arrangeChildren()

-- Listen for children being added/removed to adjust arrangement
parent.ChildAdded:Connect(arrangeChildren)
parent.ChildRemoved:Connect(arrangeChildren)
```

```lua
local Tweenservice = game:GetService("TweenService")

local parent = script.Parent
local path = parent:FindFirstChildWhichIsA("Path2D")
local objectToAnimate = parent:FindFirstChildWhichIsA("GuiObject")

local TWEEN_DURATION = 4
local TWEEN_EASING_STYLE = Enum.EasingStyle.Cubic
local TWEEN_EASING_DIRECTION = Enum.EasingDirection.InOut

local pathSampleValue = Instance.new("NumberValue")
local tweenInfo = TweenInfo.new(TWEEN_DURATION, TWEEN_EASING_STYLE, TWEEN_EASING_DIRECTION, 0, true, 2)
local tween = Tweenservice:Create(pathSampleValue, tweenInfo, {Value = 1})

local function onSampleValueChanged()
	objectToAnimate.Position = path:GetPositionOnCurveArcLength(pathSampleValue.Value)
end
pathSampleValue.Changed:Connect(onSampleValueChanged)

tween:Play()
```

## Generation details

A path is generated using a cubic Bézier spline. The mathematical function for the spline is given as follows, where P 0 \textbf{P}_0P0​ and P 3 \textbf{P}_3P3​ are the positional points, and P 1 \textbf{P}_1P1​ and P 2 \textbf{P}_2P2​ are the control points.

B ( t) = ( 1 − t) 3 P 0 + 3 ( 1 − t) 2 t P 1 + 3 ( 1 − t) t 2 P 2 + t 3 P 3 \textbf{B}(t) = \left(1-t\right)^{3}\textbf{P}_0+3\left(1-t\right)^{2}t \textbf{P}_1+3\left(1-t\right)t^{2}\textbf{P}_2+t^{3}\textbf{P}_3B(t)=(1−t)3P0​+3(1−t)2tP1​+3(1−t)t2P2​+t3P3​

For each section between two `Datatype.Path2DControlPoint|Path2DControlPoints`, P 0 \textbf{P}_0P0​ represents the position of the first control point, P 1 \textbf{P}_1P1​ represents the first control point's position plus its right tangent, P 2 \textbf{P}_2P2​ represents the second control point's position plus its left tangent, and P 3 \textbf{P}_3P3​ represents the position of the second control point.
