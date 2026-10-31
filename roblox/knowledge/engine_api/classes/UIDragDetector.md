---
name: UIDragDetector
last_updated: 2026-10-30T19:55:53Z
inherits:
  - UIComponent
  - UIBase
  - Instance
  - Object
type: class
memory_category: Instances
summary: "Instance which facilitates and encourages interaction with UI elements in an experience."
---

# Class: UIDragDetector

> Instance which facilitates and encourages interaction with UI elements in an
> experience.

## Description

The [UIDragDetector](/docs/reference/engine/classes/UIDragDetector.md) instance facilitates and encourages interaction
with 2D user interface elements in an experience, such as sliders and
spinners. Key features include:

- Place a [UIDragDetector](/docs/reference/engine/classes/UIDragDetector.md) under any [GuiObject](/docs/reference/engine/classes/GuiObject.md) instance to make
  it draggable via all inputs without a single line of code.

- Choose from several [DragStyle](/docs/reference/engine/classes/UIDragDetector.md) options,
  define how the object responds to motion via
  [ResponseStyle](/docs/reference/engine/classes/UIDragDetector.md), and optionally apply
  axis, movement limits, or drag boundaries.

- Scripts can respond to manipulation of dragged objects to drive logic
  responses, such as adjusting settings.

- [UIDragDetectors](/docs/reference/engine/classes/UIDragDetector.md) work in Studio as long as you're
  **not** using the **Select**, **Move**, **Scale**, or **Rotate** tools, nor
  certain plugins or Studio's **UI** editor tools.

## Properties

### Property: UIDragDetector.ActivatedCursorIcon

```json
{
  "type": "ContentId",
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
  "category": "Image",
  "capabilities": [
    "UI"
  ]
}
```

Sets the cursor icon to display when the mouse is activated over the
parent of this [UIDragDetector](/docs/reference/engine/classes/UIDragDetector.md). If this property is left blank, the
detector will use the default icon.

To change the activated cursor icon, set this property to the asset ID of
the image you'd like to use.

### Property: UIDragDetector.ActivatedCursorIconContent

```json
{
  "type": "Content",
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
  "category": "Image",
  "capabilities": [
    "UI"
  ]
}
```

Sets the cursor icon to display when the mouse is activated over the
parent of this [UIDragDetector](/docs/reference/engine/classes/UIDragDetector.md). If this property is left blank, the
detector will use the default icon.

To change the activated cursor icon, set this property to the asset ID of
the image you'd like to use. Only asset URIs are supported for this
property.

### Property: UIDragDetector.BoundingBehavior

```json
{
  "type": "UIDragDetectorBoundingBehavior",
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
  "category": "Behavior",
  "capabilities": [
    "UI"
  ]
}
```

Determines bounding behavior of the dragged UI object when the detector's
[BoundingUI](/docs/reference/engine/classes/UIDragDetector.md) is set. See
[UIDragDetectorBoundingBehavior](/docs/reference/engine/enums/UIDragDetectorBoundingBehavior.md) for details on each setting's
behavior.

### Property: UIDragDetector.BoundingUI

```json
{
  "type": "GuiBase2d",
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
  "category": "Behavior",
  "capabilities": [
    "UI"
  ]
}
```

When set, the [UIDragDetector](/docs/reference/engine/classes/UIDragDetector.md) instance will not allow the bounds of
the parent [GuiObject](/docs/reference/engine/classes/GuiObject.md) to be dragged outside the bounds of the
**BoundingUI** instance.

Note that if a portion of the parent [GuiObject](/docs/reference/engine/classes/GuiObject.md) is outside the
**BoundingUI** bounds, the initial input position at drag start and its
relative position during drag will be used for bounding detection until
the entirety of the dragged object is within the bounds, after which the
object will be constrained inside the bounds.

### Property: UIDragDetector.CursorIcon

```json
{
  "type": "ContentId",
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
  "category": "Image",
  "capabilities": [
    "UI"
  ]
}
```

Sets the cursor icon to display when the mouse is hovered over the parent
of this [UIDragDetector](/docs/reference/engine/classes/UIDragDetector.md). If this property is left blank, the
detector will use the default icon.

To change the cursor icon, set this property to the asset ID of the image
you'd like to use.

### Property: UIDragDetector.CursorIconContent

```json
{
  "type": "Content",
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
  "category": "Image",
  "capabilities": [
    "UI"
  ]
}
```

Sets the cursor icon to display when the mouse is hovered over the parent
of this [UIDragDetector](/docs/reference/engine/classes/UIDragDetector.md). If this property is left blank, the
detector will use the default icon.

To change the cursor icon, set this property to the asset ID of the image
you'd like to use. Only asset URIs are supported for this property.

### Property: UIDragDetector.DragAxis

```json
{
  "type": "Vector2",
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
  "category": "Drag Directions",
  "capabilities": [
    "UI"
  ]
}
```

[Vector2](/docs/reference/engine/datatypes/Vector2.md) value that defines the axis of movement for the dragged
object when [DragStyle](/docs/reference/engine/classes/UIDragDetector.md) is set to
[UIDragDetectorDragStyle.TranslateLine](/docs/reference/engine/enums/UIDragDetectorDragStyle.md). The axis is defined in the
local space of the [UIDragDetector](/docs/reference/engine/classes/UIDragDetector.md) unless
[ReferenceUIInstance](/docs/reference/engine/classes/UIDragDetector.md) is defined,
in which case the axis is defined in that instance's local space.

### Property: UIDragDetector.DragRelativity

```json
{
  "type": "UIDragDetectorDragRelativity",
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
  "category": "Behavior",
  "capabilities": [
    "UI"
  ]
}
```

Only applies if a custom drag function is registered through
[SetDragStyleFunction()](/docs/reference/engine/classes/UIDragDetector.md) or
[AddConstraintFunction()](/docs/reference/engine/classes/UIDragDetector.md).
Sets the paradigm which defines the relativity of the registered
function's inputs/outputs.

For example, returning a [UDim2.fromOffset(1, 0)](/docs/reference/engine/datatypes/UDim2.md) from a
registered function with this property set to
[UIDragDetectorDragRelativity.Absolute](/docs/reference/engine/enums/UIDragDetectorDragRelativity.md) will move the detector's
parent **to** `(1, 0)` in the designated
[DragSpace](/docs/reference/engine/classes/UIDragDetector.md), while returning the same
[UDim2](/docs/reference/engine/datatypes/UDim2.md) with this property set to
[UIDragDetectorDragRelativity.Relative](/docs/reference/engine/enums/UIDragDetectorDragRelativity.md) will move the detector's
parent **by** `(1, 0)` in the designated
[DragSpace](/docs/reference/engine/classes/UIDragDetector.md).

### Property: UIDragDetector.DragRotation

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
  "category": "Dragged Amount",
  "capabilities": [
    "UI"
  ]
}
```

The rotation performed by the current drag. This value is defined in
degrees relative to the local space of the [UIDragDetector](/docs/reference/engine/classes/UIDragDetector.md) unless
[ReferenceUIInstance](/docs/reference/engine/classes/UIDragDetector.md) is defined,
in which case the rotation is defined in the local space of that instance
and from its positive **X** axis.

This property can be changed while there is no active drag to rotate the
dragged object.

### Property: UIDragDetector.DragSpace

```json
{
  "type": "UIDragDetectorDragSpace",
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
  "category": "Behavior",
  "capabilities": [
    "UI"
  ]
}
```

Only applies if a custom drag function is registered through
[SetDragStyleFunction()](/docs/reference/engine/classes/UIDragDetector.md) or
[AddConstraintFunction()](/docs/reference/engine/classes/UIDragDetector.md).
Sets the paradigm which defines the space of the registered function's
inputs/outputs.

For example, if the detector's parent [GuiObject](/docs/reference/engine/classes/GuiObject.md) is a child of a
parent [GuiObject](/docs/reference/engine/classes/GuiObject.md) that's rotated:

- Returning a [UDim2.fromOffset(1, 0)](/docs/reference/engine/datatypes/UDim2.md) from a registered function
  with this property set to [UIDragDetectorDragSpace.Parent](/docs/reference/engine/enums/UIDragDetectorDragSpace.md) will
  move the detector's parent [GuiObject](/docs/reference/engine/classes/GuiObject.md) to the right by 1 pixel in
  the local space affected by its parent's rotation.

- Returning a [UDim2.fromOffset(1, 0)](/docs/reference/engine/datatypes/UDim2.md) from a registered function
  with this property set to [UIDragDetectorDragSpace.LayerCollector](/docs/reference/engine/enums/UIDragDetectorDragSpace.md)
  will move the detector's parent [GuiObject](/docs/reference/engine/classes/GuiObject.md) to the right by 1
  pixel in the space of the [LayerCollector](/docs/reference/engine/classes/LayerCollector.md).

### Property: UIDragDetector.DragStyle

```json
{
  "type": "UIDragDetectorDragStyle",
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
  "category": "Behavior",
  "capabilities": [
    "UI"
  ]
}
```

The paradigm used to generate proposed motion, given a stream of input
position vectors. See [UIDragDetectorDragStyle](/docs/reference/engine/enums/UIDragDetectorDragStyle.md) for options.

### Property: UIDragDetector.DragUDim2

```json
{
  "type": "UDim2",
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
  "category": "Dragged Amount",
  "capabilities": [
    "UI"
  ]
}
```

The translation performed by the current drag expressed in a
[UDim2](/docs/reference/engine/datatypes/UDim2.md) value. Translation is done through
[Offset](/docs/reference/engine/datatypes/UDim.md) or [Scale](/docs/reference/engine/datatypes/UDim.md) value changes
depending on the [DragRelativity](/docs/reference/engine/classes/UIDragDetector.md)
value, and it is relative to the detector's local space unless a
[ReferenceUIInstance](/docs/reference/engine/classes/UIDragDetector.md) is defined.

This property can be changed while there is no active drag to move the
dragged object.

### Property: UIDragDetector.Enabled

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
  "category": "Behavior",
  "capabilities": [
    "UI"
  ]
}
```

If `true`, the [UIDragDetector](/docs/reference/engine/classes/UIDragDetector.md) responds to user input; if `false`,
it does not.

### Property: UIDragDetector.MaxDragAngle

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
  "category": "Drag Limits",
  "capabilities": [
    "UI"
  ]
}
```

If this property is greater than
[MinDragAngle](/docs/reference/engine/classes/UIDragDetector.md), rotation will be clamped
within the range of [MinDragAngle](/docs/reference/engine/classes/UIDragDetector.md) and
[MaxDragAngle](/docs/reference/engine/classes/UIDragDetector.md). Positive values impede
clockwise rotation while negative values impede counterclockwise rotation.

This is not a constraint; it merely impedes the detector's attempts to
generate motion in order to remain within limits. See
[AddConstraintFunction()](/docs/reference/engine/classes/UIDragDetector.md) to
add custom constraint to a drag.

Only relevant if [DragStyle](/docs/reference/engine/classes/UIDragDetector.md) is
[UIDragDetectorDragStyle.Rotate](/docs/reference/engine/enums/UIDragDetectorDragStyle.md).

### Property: UIDragDetector.MaxDragTranslation

```json
{
  "type": "UDim2",
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
  "category": "Drag Limits",
  "capabilities": [
    "UI"
  ]
}
```

If the corresponding [Offset](/docs/reference/engine/datatypes/UDim.md) and/or
[Scale](/docs/reference/engine/datatypes/UDim.md) values are greater than those of
[MinDragTranslation](/docs/reference/engine/classes/UIDragDetector.md) in all
dimensions, linear/planar translation will be clamped within the range of
[MinDragTranslation](/docs/reference/engine/classes/UIDragDetector.md) and
[MaxDragTranslation](/docs/reference/engine/classes/UIDragDetector.md).

This is not a constraint; it merely impedes the detector's attempts to
generate motion in order to remain within limits. See
[AddConstraintFunction()](/docs/reference/engine/classes/UIDragDetector.md) to
add custom constraint to a drag.

Only relevant if [DragStyle](/docs/reference/engine/classes/UIDragDetector.md) is
[UIDragDetectorDragStyle.TranslateLine](/docs/reference/engine/enums/UIDragDetectorDragStyle.md) or
[UIDragDetectorDragStyle.TranslatePlane](/docs/reference/engine/enums/UIDragDetectorDragStyle.md).

### Property: UIDragDetector.MinDragAngle

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
  "category": "Drag Limits",
  "capabilities": [
    "UI"
  ]
}
```

If this property is less than
[MaxDragAngle](/docs/reference/engine/classes/UIDragDetector.md), rotation will be clamped
within the range of [MinDragAngle](/docs/reference/engine/classes/UIDragDetector.md) and
[MaxDragAngle](/docs/reference/engine/classes/UIDragDetector.md). Positive values impede
clockwise rotation while negative values impede counterclockwise rotation.

This is not a constraint; it merely impedes the detector's attempts to
generate motion in order to remain within limits. See
[AddConstraintFunction()](/docs/reference/engine/classes/UIDragDetector.md) to
add custom constraint to a drag.

Only relevant if [DragStyle](/docs/reference/engine/classes/UIDragDetector.md) is
[UIDragDetectorDragStyle.Rotate](/docs/reference/engine/enums/UIDragDetectorDragStyle.md).

### Property: UIDragDetector.MinDragTranslation

```json
{
  "type": "UDim2",
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
  "category": "Drag Limits",
  "capabilities": [
    "UI"
  ]
}
```

If the corresponding [Offset](/docs/reference/engine/datatypes/UDim.md) and/or
[Scale](/docs/reference/engine/datatypes/UDim.md) values are less than those of
[MaxDragTranslation](/docs/reference/engine/classes/UIDragDetector.md) in all
dimensions, linear/planar translation will be clamped within the range of
[MinDragTranslation](/docs/reference/engine/classes/UIDragDetector.md) and
[MaxDragTranslation](/docs/reference/engine/classes/UIDragDetector.md).

This is not a constraint; it merely impedes the detector's attempts to
generate motion in order to remain within limits. See
[AddConstraintFunction()](/docs/reference/engine/classes/UIDragDetector.md) to
add custom constraint to a drag.

Only relevant if [DragStyle](/docs/reference/engine/classes/UIDragDetector.md) is
[UIDragDetectorDragStyle.TranslateLine](/docs/reference/engine/enums/UIDragDetectorDragStyle.md) or
[UIDragDetectorDragStyle.TranslatePlane](/docs/reference/engine/enums/UIDragDetectorDragStyle.md).

### Property: UIDragDetector.ReferenceUIInstance

```json
{
  "type": "GuiObject",
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
  "category": "Behavior",
  "capabilities": [
    "UI"
  ]
}
```

A [GuiObject](/docs/reference/engine/classes/GuiObject.md) instance whose local space and absolute center
position is the reference space and origin for the detector. Setting this
reference affects properties such as
[DragUDim2](/docs/reference/engine/classes/UIDragDetector.md),
[DragRotation](/docs/reference/engine/classes/UIDragDetector.md), and the behavior of
[DragAxis](/docs/reference/engine/classes/UIDragDetector.md).

### Property: UIDragDetector.ResponseStyle

```json
{
  "type": "UIDragDetectorResponseStyle",
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
  "category": "Behavior",
  "capabilities": [
    "UI"
  ]
}
```

Once the proposed motion has been computed and potentially constrained,
this paradigm is used to deterimine how to move (or not move) the
[GuiObject](/docs/reference/engine/classes/GuiObject.md) affected by the [UIDragDetector](/docs/reference/engine/classes/UIDragDetector.md). See
[UIDragDetectorResponseStyle](/docs/reference/engine/enums/UIDragDetectorResponseStyle.md) for options.

### Property: UIDragDetector.SelectionModeDragSpeed

```json
{
  "type": "UDim2",
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
  "category": "Behavior",
  "capabilities": [
    "UI"
  ]
}
```

Defines the maximum drag speed for translation as a combination of
[Scale](/docs/reference/engine/datatypes/UDim.md) and [Offset](/docs/reference/engine/datatypes/UDim.md) of the first
ancestor [ScreenGui](/docs/reference/engine/classes/ScreenGui.md) or [SurfaceGui](/docs/reference/engine/classes/SurfaceGui.md) the
[UIDragDetector](/docs/reference/engine/classes/UIDragDetector.md) belongs to. This value must be positive and any
value below `0` will be clamped to `0`.

### Property: UIDragDetector.SelectionModeRotateSpeed

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
  "category": "Behavior",
  "capabilities": [
    "UI"
  ]
}
```

Defines the maximum angle per second at which the [UIDragDetector](/docs/reference/engine/classes/UIDragDetector.md)
can rotate. This value must be positive and any value below `0` will be
clamped to `0`.

### Property: UIDragDetector.UIDragSpeedAxisMapping

```json
{
  "type": "UIDragSpeedAxisMapping",
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
  "category": "Behavior",
  "capabilities": [
    "UI"
  ]
}
```

[UIDragSpeedAxisMapping](/docs/reference/engine/enums/UIDragSpeedAxisMapping.md) value that determines the **X**/**Y**
dimension dragging speeds.

## Methods

### Method: UIDragDetector:AddConstraintFunction

**Signature:** `UIDragDetector:AddConstraintFunction(priority: int, function: Function): RBXScriptConnection`

Adds a function to modify or constrain proposed motion. The function takes
an input [UDim2](/docs/reference/engine/datatypes/UDim2.md) (position) and float (rotation) of **proposed**
motion and returns a [UDim2](/docs/reference/engine/datatypes/UDim2.md) and float of **modified** or
unmodified motion. You can add multiple functions which will be called in
order by `priority`, passing the results along in a chain.

The input is expressed in the space defined by the
[DragSpace](/docs/reference/engine/classes/UIDragDetector.md) property, either as a delta or
the final desired position/rotation based on the
[DragRelativity](/docs/reference/engine/classes/UIDragDetector.md) property. The output
should be expressed in the same space and relativity, unless overridden by
returning a specified [UIDragDetectorDragRelativity](/docs/reference/engine/enums/UIDragDetectorDragRelativity.md) and
[UIDragDetectorDragSpace](/docs/reference/engine/enums/UIDragDetectorDragSpace.md) as the third and fourth return values.

To remove an added constraint function, call
[Disconnect()](/docs/reference/engine/datatypes/RBXScriptConnection.md) on the returned
connection object.

*Security: None · Thread Safety: Unsafe · Capabilities: UI*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `priority` | `int` |  | The order of priority for functions added via this method. Higher values take precedence over lower values. |
| `function` | `Function` |  | Function for modifying or constraining proposed motion. This function takes in input [UDim2](/docs/reference/engine/datatypes/UDim2.md) and float of **proposed** motion and returns a [UDim2](/docs/reference/engine/datatypes/UDim2.md) and float of **modified** or unmodified motion. It can optionally return an [UIDragDetectorDragRelativity](/docs/reference/engine/enums/UIDragDetectorDragRelativity.md) and [UIDragDetectorDragSpace](/docs/reference/engine/enums/UIDragDetectorDragSpace.md) as the third and fourth return values as output overrides. |

**Returns:** `RBXScriptConnection` — Use this connection object to remove the constraint function.

### Method: UIDragDetector:GetReferencePosition

**Signature:** `UIDragDetector:GetReferencePosition(): UDim2`

When no [ReferenceUIInstance](/docs/reference/engine/classes/UIDragDetector.md) is
set, this function returns the [UDim2](/docs/reference/engine/datatypes/UDim2.md) position of the dragged
object's immediate parent [GuiObject](/docs/reference/engine/classes/GuiObject.md) (if one exists), or else the
[UDim2](/docs/reference/engine/datatypes/UDim2.md) position of the dragged object.

When a [ReferenceUIInstance](/docs/reference/engine/classes/UIDragDetector.md) is
set, this function returns the [UDim2](/docs/reference/engine/datatypes/UDim2.md) position of that reference
instance.

*Security: None · Thread Safety: Unsafe · Capabilities: UI*

**Returns:** `UDim2` — [UDim2](/docs/reference/engine/datatypes/UDim2.md) position of the current drag's reference element.

### Method: UIDragDetector:GetReferenceRotation

**Signature:** `UIDragDetector:GetReferenceRotation(): float`

When no [ReferenceUIInstance](/docs/reference/engine/classes/UIDragDetector.md) is
set, this function returns the rotation of the dragged object's immediate
parent [GuiObject](/docs/reference/engine/classes/GuiObject.md) (if one exists), or else the rotation of the
dragged object.

When a [ReferenceUIInstance](/docs/reference/engine/classes/UIDragDetector.md) is
set, this function returns the rotation of that reference instance.

*Security: None · Thread Safety: Unsafe · Capabilities: UI*

**Returns:** `float` — Rotation of the current drag's reference element.

### Method: UIDragDetector:SetDragStyleFunction

**Signature:** `UIDragDetector:SetDragStyleFunction(function: Function): ()`

Passes a function to be used if and only if
[DragStyle](/docs/reference/engine/classes/UIDragDetector.md) is set to
[UIDragDetectorDragStyle.Scriptable](/docs/reference/engine/enums/UIDragDetectorDragStyle.md). The given function receives the
signal's screen space input position with type [Vector2](/docs/reference/engine/datatypes/Vector2.md), and it
returns a [UDim2](/docs/reference/engine/datatypes/UDim2.md) (position) and float (rotation) containing the
desired motion of the drag. The space of the return values and the
relativity of the motion are determined by the
[DragSpace](/docs/reference/engine/classes/UIDragDetector.md) and
[DragRelativity](/docs/reference/engine/classes/UIDragDetector.md) properties, unless
overridden by returning a specified [UIDragDetectorDragRelativity](/docs/reference/engine/enums/UIDragDetectorDragRelativity.md)
and [UIDragDetectorDragSpace](/docs/reference/engine/enums/UIDragDetectorDragSpace.md) as the third and fourth return values.

If the function returns `nil`, the object will not be moved. This is
useful if the script has not yet collected all the information it needs to
give the correct answer, or in temporary cases where you want the object
to stay where it is.

*Security: None · Thread Safety: Unsafe · Capabilities: UI*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `function` | `Function` |  | Function for monitoring [DragContinue](/docs/reference/engine/classes/UIDragDetector.md) signals. This function receives the signal's screen space input position and returns a [UDim2](/docs/reference/engine/datatypes/UDim2.md) and float containing the desired motion of the drag in the desired space and relativity. If this function returns `nil`, the object will not be moved. |

**Returns:** `()`

## Events

### Event: UIDragDetector.DragContinue

**Signature:** `UIDragDetector.DragContinue(inputPosition: Vector2)`

Fires when a user continues dragging the UI element after
[DragStart](/docs/reference/engine/classes/UIDragDetector.md) has been initiated.

*Security: None · Capabilities: UI*

**Parameters:**

| Name | Type | Description |
|------|------|-------------|
| `inputPosition` | `Vector2` | [Vector2](/docs/reference/engine/datatypes/Vector2.md) representing the current input position. |

### Event: UIDragDetector.DragEnd

**Signature:** `UIDragDetector.DragEnd(inputPosition: Vector2)`

Fires when a user stops dragging the UI element.

*Security: None · Capabilities: UI*

**Parameters:**

| Name | Type | Description |
|------|------|-------------|
| `inputPosition` | `Vector2` | [Vector2](/docs/reference/engine/datatypes/Vector2.md) representing the current input position. |

### Event: UIDragDetector.DragStart

**Signature:** `UIDragDetector.DragStart(inputPosition: Vector2)`

Fires when a user starts dragging the UI element.

*Security: None · Capabilities: UI*

**Parameters:**

| Name | Type | Description |
|------|------|-------------|
| `inputPosition` | `Vector2` | [Vector2](/docs/reference/engine/datatypes/Vector2.md) representing the current input position. |

## Inherited Members

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