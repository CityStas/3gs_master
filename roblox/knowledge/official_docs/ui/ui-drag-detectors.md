---
title: "UI drag detectors"
url: /docs/en-us/ui/ui-drag-detectors
last_updated: 2026-10-30T19:56:02Z
description: "UI drag detectors facilitate and encourage interaction with 2D user interface elements in a game, such as sliders and spinners."
---

# UI drag detectors

The `Class.UIDragDetector` instance facilitates and encourages interaction with 2D user interface elements in a game, such as sliders, spinners, and more. Key features include:

- Place a `Class.UIDragDetector` under any `Class.GuiObject` instance to make it draggable via all user inputs without a single line of code.
- Choose from several `Class.UIDragDetector.DragStyle|DragStyle` options, define how the object responds to motion via `Class.UIDragDetector.ResponseStyle|ResponseStyle`, and optionally apply axis, movement limits, or drag boundaries.
- Scripts can respond to manipulation of dragged objects to drive logic responses, such as adjusting settings.
- `Class.UIDragDetector|UIDragDetectors` work in Studio's edit and play mode as long as you're **not** using the **Select**, **Move**, **Scale**, or **Rotate** tools, nor certain plugins or Studio's **UI** editor tools.

> **Info:** For drag detectors that manipulate 3D objects in a game, such as opening doors and drawers or sliding a part around, see [3D Drag Detectors](/docs/en-us/ui/3D-drag-detectors.md).
## Make UI elements draggable

To make any `Class.GuiObject` instances draggable, simply add a `Class.UIDragDetector` as a direct descendant.

1. In the [Explorer](/docs/en-us/studio/explorer.md) window, hover over the `Class.GuiObject` instance and click the ⊕ button. A contextual menu displays.
2. From the menu, insert a **UIDragDetector**.
3. By default, the object will now be draggable in the `Class.LayerCollector|LayerCollector` interface.

> **Warning:** Remember that `Class.UIDragDetector|UIDragDetectors` only work in Studio if you're **not** using the **Select**, **Move**, **Scale**, or **Rotate** tools, nor certain plugins or Studio's **UI** editor tools.
## Customize UI drag detectors

### Drag style

`Class.UIDragDetector|UIDragDetectors` map cursor motion to calculate proposed 2D motion and/or rotation. Through the `Class.UIDragDetector.DragStyle|DragStyle` property, you can choose from different mappings to suit your needs. For example, `Enum.UIDragDetectorDragStyle.TranslatePlane` produces translation in the 2D plane of the `Class.LayerCollector`, while `Enum.UIDragDetectorDragStyle.Rotate` normally produces a rotation instead of translation.

| Setting | Description |
| --- | --- |
| `Enum.UIDragDetectorDragStyle.TranslateLine\|TranslateLine` | 1D motion along the detector's `Class.UIDragDetector.DragAxis\|DragAxis`. |
| `Enum.UIDragDetectorDragStyle.TranslatePlane\|TranslatePlane` | 2D motion in the plane of the `Class.LayerCollector`. |
| `Enum.UIDragDetectorDragStyle.Rotate\|Rotate` | By default, rotation about the absolute center position of the detector's parent `Class.GuiObject`. If `Class.UIDragDetector.ReferenceUIInstance\|ReferenceUIInstance` is set, rotation happens about that instance's absolute center position. |
| `Enum.UIDragDetectorDragStyle.Scriptable\|Scriptable` | Calculates desired motion via a custom function provided through `Class.UIDragDetector:SetDragStyleFunction()\|SetDragStyleFunction()`. |

### Drag direction

By default, 2D motion and the associated `Class.UIDragDetector.DragStyle|DragStyle` map to the space of the ancestor `Class.LayerCollector`. However, you may want to change the `Class.UIDragDetector.ReferenceUIInstance|ReferenceUIInstance` or the `Class.UIDragDetector.DragAxis|DragAxis` when building different UI components.

| Setting | Description | Default |
| --- | --- | --- |
| `Class.UIDragDetector.ReferenceUIInstance\|ReferenceUIInstance` | A `Class.GuiObject` instance whose local space and absolute center position is the reference space and origin for the detector. Setting this reference affects properties such as `Class.UIDragDetector.DragUDim2\|DragUDim2`, `Class.UIDragDetector.DragRotation\|DragRotation`, and the behavior of `Class.UIDragDetector.DragAxis\|DragAxis`. | `nil` |
| `Class.UIDragDetector.DragAxis\|DragAxis` | `Datatype.Vector2` value that defines the axis of movement for the dragged object when `Class.UIDragDetector.DragStyle\|DragStyle` is set to `Enum.UIDragDetectorDragStyle.TranslateLine`. The axis is defined in the local space of the `Class.UIDragDetector` unless `Class.UIDragDetector.ReferenceUIInstance\|ReferenceUIInstance` is defined, in which case the axis is defined in that instance's local space. | (1, 0) |

### Response to motion

The `Class.UIDragDetector.ResponseStyle` property specifies how an object's position value is changed by the proposed motion. The custom response styles let you use the resulting `Class.UIDragDetector.DragUDim2` and `Class.UIDragDetector.DragRotation` values as desired, without having the detector's parent execute the proposed motion.

| Setting | Description |
| --- | --- |
| `Enum.UIDragDetectorResponseStyle.Offset\|Offset` | Move by the `Datatype.UDim.Offset\|Offset` values of the detector's parent's `Class.GuiObject.Position` value. This is the setting by default. |
| `Enum.UIDragDetectorResponseStyle.Scale\|Scale` | Move by the `Datatype.UDim.Scale\|Scale` values of the detector's parent's `Class.GuiObject.Position` value. |
| `Enum.UIDragDetectorResponseStyle.CustomOffset\|CustomOffset` | The UI element will not move at all, but the `Datatype.UDim.Offset\|Offset` values of the detector's `Class.UIDragDetector.DragUDim2\|DragUDim2` will still be updated and the detector's events will still fire, allowing you to respond to drag manipulation however you'd like. |
| `Enum.UIDragDetectorResponseStyle.CustomScale\|CustomScale` | The UI element will not move at all, but the `Datatype.UDim.Scale\|Scale` values of the detector's `Class.UIDragDetector.DragUDim2\|DragUDim2` will still be updated and the detector's events will still fire, allowing you to respond to drag manipulation however you'd like. |

### Translation & rotation limits

By default, there are no limits to 2D motion behind the inherent restrictions of the `Class.UIDragDetector.DragStyle|DragStyle`. Limits for both minimum and maximum translations and rotations can be declared with the following properties if desired. Additionally, you can define how the dragged object is constrained within the bounds of a specified `Class.GuiObject` such as a `Class.Frame`.

| Properties | Description | Default |
| --- | --- | --- |
| `Class.UIDragDetector.MinDragTranslation\|MinDragTranslation`<br> `Class.UIDragDetector.MaxDragTranslation\|MaxDragTranslation` | Limits to drag translation in each dimension, defined by a `Datatype.UDim2` value. If `Class.UIDragDetector.MaxDragTranslation\|MaxDragTranslation` is greater than `Class.UIDragDetector.MinDragTranslation\|MinDragTranslation`, translation will be clamped within that range. | {0, 0}, {0, 0} |
| `Class.UIDragDetector.MinDragAngle\|MinDragAngle`<br> `Class.UIDragDetector.MaxDragAngle\|MaxDragAngle` | Only relevant if `Class.UIDragDetector.DragStyle\|DragStyle` is set to `Enum.UIDragDetectorDragStyle.Rotate`, or if the functions set through `Class.UIDragDetector:SetDragStyleFunction()\|SetDragStyleFunction()` or `Class.UIDragDetector:AddConstraintFunction()\|AddConstraintFunction()` defines a rotation value. If `Class.UIDragDetector.MaxDragAngle\|MaxDragAngle` is greater than `Class.UIDragDetector.MinDragAngle\|MinDragAngle`, rotation will be clamped within that range. | 0 |
| `Class.UIDragDetector.BoundingBehavior\|BoundingBehavior` | Determines the `Class.UIDragDetector` instance's bounding behavior when its `Class.UIDragDetector.BoundingUI\|BoundingUI` is set. Setting this to `Enum.UIDragDetectorBoundingBehavior.EntireObject\|EntireObject` bounds the entire dragged UI within the `Class.UIDragDetector.BoundingUI\|BoundingUI`, while setting it to `Enum.UIDragDetectorBoundingBehavior.HitPoint\|HitPoint` bounds the dragged UI only by the exact hit/grab point and its respective position after translation/rotation. As a convenience, the default of `Enum.UIDragDetectorBoundingBehavior.Automatic\|Automatic` mimics the `Enum.UIDragDetectorBoundingBehavior.EntireObject\|EntireObject` behavior for a UI object that's entirely contained by the `Class.UIDragDetector.BoundingUI\|BoundingUI`, or else `Enum.UIDragDetectorBoundingBehavior.HitPoint\|HitPoint` for a UI object that's partially outside the `Class.UIDragDetector.BoundingUI\|BoundingUI`. | `Enum.UIDragDetectorBoundingBehavior.Automatic\|Automatic` |

### Speed adjustments

Through `Class.UIDragDetector.SelectionModeDragSpeed|SelectionModeDragSpeed` and `Class.UIDragDetector.SelectionModeRotateSpeed|SelectionModeRotateSpeed`, you can fine‑tune the maximum drag/rotate speeds for a detector. Furthermore, through `Class.UIDragDetector.UIDragSpeedAxisMapping|UIDragSpeedAxisMapping`, you can fine‑tune the **X**/**Y** dimension dragging speeds, based on the detector's `Class.UIDragDetector.SelectionModeDragSpeed|SelectionModeDragSpeed`.

| Property | Description |
| --- | --- |
| `Class.UIDragDetector.SelectionModeDragSpeed\|SelectionModeDragSpeed` | Defines the maximum drag speed for translation as a combination of `Datatype.UDim.Scale\|Scale` and `Datatype.UDim.Offset\|Offset` of the first ancestor `Class.ScreenGui` or `Class.SurfaceGui` the `Class.UIDragDetector` belongs to. |
| `Class.UIDragDetector.SelectionModeRotateSpeed\|SelectionModeRotateSpeed` | Defines the maximum angle per second at which the `Class.UIDragDetector` can rotate. |
| `Class.UIDragDetector.UIDragSpeedAxisMapping\|UIDragSpeedAxisMapping` | Determines the **X**/**Y** dimension dragging speeds, based on the detector's `Class.UIDragDetector.SelectionModeDragSpeed\|SelectionModeDragSpeed`. The default is `Enum.UIDragSpeedAxisMapping.XY\|XY`, meaning the **X** and **Y** axis speeds are based off the **X** and **Y** `Datatype.UDim.Scale\|Scale`/`Datatype.UDim.Offset\|Offset` values respectively.<br><br>Alternatives are `Enum.UIDragSpeedAxisMapping\|XX` and `Enum.UIDragSpeedAxisMapping\|YY`, meaning both the **X** and **Y** axis speeds are based off the **X** (`Enum.UIDragSpeedAxisMapping\|XX`) or **Y** (`Enum.UIDragSpeedAxisMapping\|YY`) axis for `Datatype.UDim.Scale\|Scale`, while the `Datatype.UDim.Offset\|Offset` values still apply to their respective axis. For example, if the first ancestor `Class.ScreenGui` is sized 800×600 and `Class.UIDragDetector.SelectionModeDragSpeed\|SelectionModeDragSpeed` is`{0.1, 10}, {0.1, 20}`, a setting of `Enum.UIDragSpeedAxisMapping\|XX` results in an **X**/**Y** drag speed of `80+10`/`80+20`, while `Enum.UIDragSpeedAxisMapping\|YY` results in `60+10`/`60+20` (note the `Datatype.UDim.Offset\|Offset` values remain the same in both cases). |

## Script responses to clicking and dragging

Through [event signals](#event-signals), property changes, `Enum.UIDragDetectorDragStyle.Scriptable|Scriptable` drag style, and custom functions, scripts can respond to the manipulation of dragged UI elements to drive various settings or make logical decisions, such as sliders that adjust music and sound effect volume separately.

> **Warning:** For user-initiated script responses like [Event Signals](#event-signals) and [Scripted Drag Style](#scripted-drag-style), you'll most commonly need to put your script code inside a `Class.LocalScript`, or a `Class.Script` with `Class.BaseScript.RunContext|RunContext` set to `Enum.RunContext.Client|Client`.
### Event signals

Through the following event signals, you can detect when a user starts, continues, and ends dragging an object.

| Event | Description |
| --- | --- |
| `Class.UIDragDetector.DragStart\|DragStart` | Fires when a user starts dragging the object. |
| `Class.UIDragDetector.DragContinue\|DragContinue` | Fires when a user continues dragging the object after `Class.UIDragDetector.DragStart\|DragStart` has been initiated. |
| `Class.UIDragDetector.DragEnd\|DragEnd` | Fires when a user stops dragging the object. |

The following slider designates its container as the `Class.UIDragDetector.BoundingUI|BoundingUI` to limit its movement within the container area, allowing the scale‑based `Enum.UIDragDetectorDragStyle|TranslateLine` drag to be limited to the full width of the container without extra scripting.

> **Note:** To test this example, download the [`TransparencySlider.rbxm`](../assets/ui/ui-drag-detectors/TransparencySlider.rbxm) file, right‑click `Class.StarterGui` in the [Explorer](/docs/en-us/studio/explorer.md) window, select **Insert** ⟩ **Import Roblox Model**, and choose the downloaded file.

```lua
-- Hierarchy is SliderContainer ⟩ Handle ⟩ UIDragDetector ⟩ (this script)
local sliderContainer = script.Parent.Parent.Parent
local handle = sliderContainer:FindFirstChild("Handle")
local uiDragDetector = handle:FindFirstChildWhichIsA("UIDragDetector")

uiDragDetector.ResponseStyle = Enum.UIDragDetectorResponseStyle.Scale  -- Set dragging by scale
uiDragDetector.DragStyle = Enum.UIDragDetectorDragStyle.TranslateLine  -- Restricts dragging to line
uiDragDetector.BoundingUI = sliderContainer

-- Initially set container transparency to X scale value of handle
sliderContainer.BackgroundTransparency = 1 - handle.Position.X.Scale

-- Expand handle border to indicate grab start
uiDragDetector.DragStart:Connect(function(inputPosition)
	handle:FindFirstChildWhichIsA("UIStroke").Thickness = 6
end)

-- Change transparency by how much it dragged in scale
uiDragDetector.DragContinue:Connect(function(inputPosition)
	sliderContainer.BackgroundTransparency = 1 - handle.Position.X.Scale
end)

-- Revert handle border to indicate grab end
uiDragDetector.DragEnd:Connect(function(inputPosition)
	handle:FindFirstChildWhichIsA("UIStroke").Thickness = 4
end)
```

### Position & rotation changes

In addition to [event signals](#event-signals), you can monitor changes to the detector's `Class.UIDragDetector.DragUDim2|DragUDim2` and/or `Class.UIDragDetector.DragRotation|DragRotation` properties directly.

The following detector has its `Class.UIDragDetector.DragStyle|DragStyle` set to `Enum.UIDragDetectorDragStyle|Rotate`, allowing users to drag the handle around the hue rotator ring, all while detecting changes to drag rotation through `Class.Instance:GetPropertyChangedSignal()`.

> **Note:** To test this example, download the [`HueRotator.rbxm`](../assets/ui/ui-drag-detectors/HueRotator.rbxm) file, right‑click `Class.StarterGui` in the [Explorer](/docs/en-us/studio/explorer.md) window, select **Insert** ⟩ **Import Roblox Model**, and choose the downloaded file.

```lua
local handle = script.Parent.Parent  -- UI element to drag
local uiDragDetector = handle:FindFirstChildWhichIsA("UIDragDetector")

uiDragDetector.DragStyle = Enum.UIDragDetectorDragStyle.Rotate  -- Set drag style to rotate

local function changeHue()
	local currAngle = (math.fmod(handle.Rotation, 360)) / 360
	if currAngle < 0 then
		currAngle += 1
	end
	handle.BackgroundColor3 = Color3.fromHSV(currAngle, 1, 1)
end

-- Initially set hue to handle rotation
changeHue()

-- Connect function to GetPropertyChangedSignal() of the detector's drag rotation
uiDragDetector:GetPropertyChangedSignal("DragRotation"):Connect(changeHue)
```

### Scripted drag style

If you set a detector's `Class.UIDragDetector.DragStyle` to `Enum.UIDragDetectorDragStyle.Scriptable`, you can provide your own function that takes in a `Datatype.Vector2` of the input position and returns a `Datatype.UDim2` (position) and a float (rotation). The detector will update the object to the computed position/rotation based off of the returns, the `Class.UIDragDetector.DragSpace|DragSpace` property, and the `Class.UIDragDetector.DragRelativity|DragRelativity` property.

By default, the returned `Datatype.UDim2` and float will be the **final** desired position/rotation in the local space of the detector's parent. Existing translation/rotation limits will still apply, as will boundary limits imposed by a specified `Class.UIDragDetector.BoundingUI|BoundingUI` instance.

The following example drags a UI element following a sine wave computed by the change in **X** coordinate input. Note that the detector's `Class.UIDragDetector.DragSpace|DragSpace` is set to `Enum.UIDragDetectorDragSpace.Relative`.

```lua
local frame = script.Parent  -- UI element to drag
local uiDragDetector = frame:FindFirstChildWhichIsA("UIDragDetector")

local initialXValue = 0
local maxHeightChange = 200
local pixelsPerRadian = 75  -- Lower this value to increase frequency

uiDragDetector.DragStart:Connect(function(inputPosition)
	initialXValue = inputPosition.X
end)

local function computeSinWaveCoordinate(inputPosition)
	local deltaX = inputPosition.X - initialXValue
	-- Negative Y delta so that it goes "up" on the screen with positive Y change
	local deltaY = -math.sin(deltaX / pixelsPerRadian) * maxHeightChange
	return UDim2.fromOffset(deltaX, deltaY)
end

uiDragDetector:SetDragStyleFunction(computeSinWaveCoordinate)
```

### Custom constraint function

`Class.UIDragDetector|UIDragDetectors` do not have built-in motion rules about grids and snapping, but you can register custom constraint functions to edit the detector's `Class.UIDragDetector.DragUDim2` and `Class.UIDragDetector.DragRotation` before they are applied. For example, you can keep motion on a grid by rounding positions to specific increments, or define allowed areas of motion. Note that this is applied **before** any existing translation/rotation limits.

> **Info:** Multiple constraint functions can be registered and they will be called in the order of their priority value passed in upon registration, from least to greatest.

The following example utilizes a constraint function that clamps the planar drag into an **X**/**Y** grid based on the number of rows and columns. Note that the detector's `Class.UIDragDetector.ResponseStyle|ResponseStyle` is set to `Enum.UIDragDetectorResponseStyle.Scale` and its `Class.UIDragDetector.BoundingUI|BoundingUI` is set to the grid container.

> **Note:** To test this example, download the [`GridDrag.rbxm`](../assets/ui/ui-drag-detectors/GridDrag.rbxm) file, right‑click `Class.StarterGui` in the [Explorer](/docs/en-us/studio/explorer.md) window, select **Insert** ⟩ **Import Roblox Model**, and choose the downloaded file.

```lua
-- Hierarchy is GridContainer ⟩ Handle ⟩ UIDragDetector ⟩ (this script)
local gridContainer = script.Parent.Parent.Parent
local handle = gridContainer:FindFirstChild("Handle")  -- UI element to drag
local uiDragDetector = handle:FindFirstChildWhichIsA("UIDragDetector")

uiDragDetector.ResponseStyle = Enum.UIDragDetectorResponseStyle.Scale  -- Set dragging by scale
uiDragDetector.DragRelativity = Enum.UIDragDetectorDragRelativity.Relative
uiDragDetector.BoundingUI = gridContainer

local NUM_COLUMNS = 10
local NUM_ROWS = 5

local xScaleIncrement = 1 / NUM_COLUMNS
local yScaleIncrement = 1 / NUM_ROWS
local initialParentPosition = uiDragDetector.Parent.Position

uiDragDetector.DragStart:Connect(function()
	initialParentPosition = uiDragDetector.Parent.Position
end)

local function dragToGridOnly(proposedPosition, proposedRotation)
	local griddedXScale = math.round(proposedPosition.X.Scale / xScaleIncrement) * xScaleIncrement
	local griddedYScale = math.round(proposedPosition.Y.Scale / yScaleIncrement) * yScaleIncrement

	return UDim2.fromScale(griddedXScale, griddedYScale), proposedRotation
end

uiDragDetector:AddConstraintFunction(1, dragToGridOnly)
```
