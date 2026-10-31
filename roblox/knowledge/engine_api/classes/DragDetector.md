---
name: DragDetector
last_updated: 2026-10-30T19:55:52Z
inherits:
  - ClickDetector
  - Instance
  - Object
type: class
memory_category: Instances
summary: "Instance which facilitates and encourages interaction with 3D objects in an experience."
---

# Class: DragDetector

> Instance which facilitates and encourages interaction with 3D objects in an
> experience.

## Description

The [DragDetector](/docs/reference/engine/classes/DragDetector.md) instance facilitates and encourages interaction with
3D objects in an experience, such as opening doors and drawers, sliding a part
around, and much more. Key features include:

- Place a [DragDetector](/docs/reference/engine/classes/DragDetector.md) under any [BasePart](/docs/reference/engine/classes/BasePart.md) or [Model](/docs/reference/engine/classes/Model.md) to
  make it draggable via all inputs (mouse, touch, gamepad, and VR), all
  without a single line of code.

- Choose from several [DragStyle](/docs/reference/engine/classes/DragDetector.md) options, define
  how the object responds to motion via
  [ResponseStyle](/docs/reference/engine/classes/DragDetector.md), and optionally apply axis
  or movement limits.

- Scripts can respond to manipulation of dragged objects to drive UI or make
  logical decisions, such as adjusting the light level in a room based on a
  sliding wall switch dimmer.

- Players can manipulate anchored parts or models and they'll stay exactly
  where you put them upon release.

- [DragDetectors](/docs/reference/engine/classes/DragDetector.md) work in Studio as long as you're **not**
  using the **Select**, **Move**, **Scale**, or **Rotate** tools, making it
  easier to test and adjust draggable objects while editing.

See the [3D Drag Detectors](/docs/en-us/ui/3D-drag-detectors.md) guide for
details and usage examples.

## Properties

### Property: DragDetector.ActivatedCursorIcon

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
    "Physics",
    "Input"
  ]
}
```

Sets the cursor icon to display when the mouse is activated over the
parent of this [DragDetector](/docs/reference/engine/classes/DragDetector.md). If this property is left blank, the
detector will use the default icon.

To change the activated cursor icon, set this property to the asset ID of
the image you'd like to use.

### Property: DragDetector.ActivatedCursorIconContent

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
    "Physics",
    "Input"
  ]
}
```

Sets the cursor icon to display when the mouse is activated over the
parent of this [DragDetector](/docs/reference/engine/classes/DragDetector.md). If this property is left blank, the
detector will use the default icon.

To change the activated cursor icon, set this property to the asset ID of
the image you'd like to use. Only asset URIs are supported for this
property.

### Property: DragDetector.ApplyAtCenterOfMass

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
  "category": "Physics Response",
  "capabilities": [
    "Physics",
    "Input"
  ]
}
```

When false (default), constraint force is applied at the point the user
clicks on. When true, force is applied at the object's center of mass.
Only relevant if [ResponseStyle](/docs/reference/engine/classes/DragDetector.md) is
[DragDetectorResponseStyle.Physical](/docs/reference/engine/enums/DragDetectorResponseStyle.md) and the parent object is
unanchored.

### Property: DragDetector.Axis

```json
{
  "type": "Vector3",
  "access": "ReadWrite",
  "security": {
    "read": "None",
    "write": "None"
  },
  "serialization": {
    "can_load": true,
    "can_save": false
  },
  "thread_safety": "ReadSafe",
  "category": "Drag Directions",
  "capabilities": [
    "Physics",
    "Input"
  ]
}
```

The primary axis of motion, expressed relative to the reference frame. For
a [DragStyle](/docs/reference/engine/classes/DragDetector.md) of
[DragDetectorDragStyle.TranslateLine](/docs/reference/engine/enums/DragDetectorDragStyle.md), the direction of translation;
for [DragDetectorDragStyle.TranslatePlane](/docs/reference/engine/enums/DragDetectorDragStyle.md), the normal to the plane
of motion; for [DragDetectorDragStyle.RotateAxis](/docs/reference/engine/enums/DragDetectorDragStyle.md), the axis of 1D
rotation. Changing this value automatically updates
[Orientation](/docs/reference/engine/classes/DragDetector.md) and vice versa.

### Property: DragDetector.DragFrame

```json
{
  "type": "CFrame",
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
    "Physics",
    "Input"
  ]
}
```

If [ReferenceInstance](/docs/reference/engine/classes/DragDetector.md) is set, the
[CFrame](/docs/reference/engine/datatypes/CFrame.md) of the pivot relative to the reference frame; otherwise,
the [CFrame](/docs/reference/engine/datatypes/CFrame.md) of the pivot relative to its frame at the beginning
of the drag.

### Property: DragDetector.DragStyle

```json
{
  "type": "DragDetectorDragStyle",
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
    "Physics",
    "Input"
  ]
}
```

The paradigm used to generate proposed motion, given a stream of cursor
rays. See [DragDetectorDragStyle](/docs/reference/engine/enums/DragDetectorDragStyle.md) for options.

### Property: DragDetector.Enabled

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
    "Physics",
    "Input"
  ]
}
```

If true, the [DragDetector](/docs/reference/engine/classes/DragDetector.md) responds to user input; if false, it
does not.

### Property: DragDetector.GamepadModeSwitchKeyCode

```json
{
  "type": "KeyCode",
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
  "category": "Mode Switching",
  "capabilities": [
    "Physics",
    "Input"
  ]
}
```

During gamepad input, the [KeyCode](/docs/reference/engine/enums/KeyCode.md) for toggling the secondary mode
of motion. Only applies if the drag detector's
[DragStyle](/docs/reference/engine/classes/DragDetector.md) has both primary and secondary
modes of motion.

### Property: DragDetector.KeyboardModeSwitchKeyCode

```json
{
  "type": "KeyCode",
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
  "category": "Mode Switching",
  "capabilities": [
    "Physics",
    "Input"
  ]
}
```

During keyboard input, the [KeyCode](/docs/reference/engine/enums/KeyCode.md) for toggling the secondary mode
of motion. Only applies if the drag detector's
[DragStyle](/docs/reference/engine/classes/DragDetector.md) has both primary and secondary
modes of motion.

### Property: DragDetector.MaxDragAngle

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
    "Physics",
    "Input"
  ]
}
```

If this is greater than [MinDragAngle](/docs/reference/engine/classes/DragDetector.md),
translation will be clamped within that range.

This is not a constraint; it merely impedes the drag detector's attempts
to generate motion in order to remain within limits. See
[AddConstraintFunction()](/docs/reference/engine/classes/DragDetector.md) to
add custom constraint to a drag.

Only relevant if [DragStyle](/docs/reference/engine/classes/DragDetector.md) is
[DragDetectorDragStyle.RotateAxis](/docs/reference/engine/enums/DragDetectorDragStyle.md).

### Property: DragDetector.MaxDragTranslation

```json
{
  "type": "Vector3",
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
    "Physics",
    "Input"
  ]
}
```

In any dimension, if this is greater than
[MinDragTranslation](/docs/reference/engine/classes/DragDetector.md), translation
will be clamped within that range.

This is not a constraint; it merely impedes the drag detector's attempts
to generate motion in order to remain within limits. See
[AddConstraintFunction()](/docs/reference/engine/classes/DragDetector.md) to
add custom constraint to a drag.

### Property: DragDetector.MaxForce

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
  "category": "Physics Response",
  "capabilities": [
    "Physics",
    "Input"
  ]
}
```

Maximum force applied for the object to reach its goal. Only relevant if
[ResponseStyle](/docs/reference/engine/classes/DragDetector.md) is
[DragDetectorResponseStyle.Physical](/docs/reference/engine/enums/DragDetectorResponseStyle.md) and the parent object is
unanchored.

### Property: DragDetector.MaxTorque

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
  "category": "Physics Response",
  "capabilities": [
    "Physics",
    "Input"
  ]
}
```

Maximum torque applied for the object to reach its goal. Only relevant if
[ResponseStyle](/docs/reference/engine/classes/DragDetector.md) is
[DragDetectorResponseStyle.Physical](/docs/reference/engine/enums/DragDetectorResponseStyle.md) and the parent object is
unanchored.

### Property: DragDetector.MinDragAngle

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
    "Physics",
    "Input"
  ]
}
```

If this is less than [MaxDragAngle](/docs/reference/engine/classes/DragDetector.md),
translation will be clamped within that range.

This is not a constraint; it merely impedes the drag detector's attempts
to generate motion in order to remain within limits. See
[AddConstraintFunction()](/docs/reference/engine/classes/DragDetector.md) to
add custom constraint to a drag.

Only relevant if [DragStyle](/docs/reference/engine/classes/DragDetector.md) is
[DragDetectorDragStyle.RotateAxis](/docs/reference/engine/enums/DragDetectorDragStyle.md).

### Property: DragDetector.MinDragTranslation

```json
{
  "type": "Vector3",
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
    "Physics",
    "Input"
  ]
}
```

In any dimension, if this is less than
[MaxDragTranslation](/docs/reference/engine/classes/DragDetector.md), translation
will be clamped within that range.

This is not a constraint; it merely impedes the drag detector's attempts
to generate motion in order to remain within limits. See
[AddConstraintFunction()](/docs/reference/engine/classes/DragDetector.md) to
add custom constraint to a drag.

### Property: DragDetector.Orientation

```json
{
  "type": "Vector3",
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
    "Physics",
    "Input"
  ]
}
```

Specifies the **YXZ** rotation of axes of motion relative to the reference
frame (does not change the orientation of the reference frame itself).
Linear translation and axial rotation will be on this reoriented **Y**
axis, and planar translation in the **XZ** plane. Changing this value
automatically updates [Axis](/docs/reference/engine/classes/DragDetector.md) and vice versa.

### Property: DragDetector.PermissionPolicy

```json
{
  "type": "DragDetectorPermissionPolicy",
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
    "Physics",
    "Input"
  ]
}
```

Controls the permission level for which players can interact with the
[DragDetector](/docs/reference/engine/classes/DragDetector.md). Default is
[DragDetectorPermissionPolicy.Everybody](/docs/reference/engine/enums/DragDetectorPermissionPolicy.md).

### Property: DragDetector.ReferenceInstance

```json
{
  "type": "Instance",
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
  "category": "Data",
  "capabilities": [
    "Physics",
    "Input"
  ]
}
```

An instance whose [CFrame](/docs/reference/engine/datatypes/CFrame.md) is the reference frame for the drag
detector. The [DragFrame](/docs/reference/engine/classes/DragDetector.md) is expressed
relative to this [CFrame](/docs/reference/engine/datatypes/CFrame.md) which may be retrieved via the
[GetReferenceFrame()](/docs/reference/engine/classes/DragDetector.md) method.

If this instance is a [PVInstance](/docs/reference/engine/classes/PVInstance.md), the reference frame will be its
pivot; if an [Attachment](/docs/reference/engine/classes/Attachment.md), then its world [CFrame](/docs/reference/engine/datatypes/CFrame.md). If it
is `nil` or neither of the former, the reference frame will be based on
the pivot of the drag detector's parent [BasePart](/docs/reference/engine/classes/BasePart.md) or [Model](/docs/reference/engine/classes/Model.md).

### Property: DragDetector.ResponseStyle

```json
{
  "type": "DragDetectorResponseStyle",
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
    "Physics",
    "Input"
  ]
}
```

Once the proposed motion has been computed and potentially constrained,
this is the paradigm used to move, or not move, the objects affected by
the [DragDetector](/docs/reference/engine/classes/DragDetector.md). See [DragDetectorResponseStyle](/docs/reference/engine/enums/DragDetectorResponseStyle.md) for
options.

### Property: DragDetector.Responsiveness

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
  "category": "Physics Response",
  "capabilities": [
    "Physics",
    "Input"
  ]
}
```

Higher values cause the object to reach its goal more rapidly. Only
relevant if [ResponseStyle](/docs/reference/engine/classes/DragDetector.md) is
[DragDetectorResponseStyle.Physical](/docs/reference/engine/enums/DragDetectorResponseStyle.md) and the parent object is
unanchored.

### Property: DragDetector.RunLocally

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
    "Physics",
    "Input"
  ]
}
```

If false (default), the client sends replicated signals
([DragStart](/docs/reference/engine/classes/DragDetector.md),
[DragContinue](/docs/reference/engine/classes/DragDetector.md),
[DragEnd](/docs/reference/engine/classes/DragDetector.md)) to the server which processes cursor
rays, makes changes to the data model, and replicates them onwards to
clients.

If true, the client processes those signals itself and does not replicate
them to the server. Client [LocalScripts](/docs/reference/engine/classes/LocalScript.md) may be used to
respond to these events and [RemoteEvents](/docs/reference/engine/classes/RemoteEvent.md) may be used
to send any resulting changes that should be replicated to the server.

### Property: DragDetector.SecondaryAxis

```json
{
  "type": "Vector3",
  "access": "ReadWrite",
  "security": {
    "read": "None",
    "write": "None"
  },
  "serialization": {
    "can_load": true,
    "can_save": false
  },
  "thread_safety": "ReadSafe",
  "category": "Drag Directions",
  "capabilities": [
    "Physics",
    "Input"
  ]
}
```

The secondary axis of the motion. Relates to orientation using the same
paradigm as [Attachments](/docs/reference/engine/classes/Attachment.md).

### Property: DragDetector.TrackballRadialPullFactor

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
    "Physics",
    "Input"
  ]
}
```

When the cursor is outside the trackball, the [DragDetector](/docs/reference/engine/classes/DragDetector.md) can
apply a radial pull rotation that turns the ball as if it were trying to
roll out toward the cursor. This property is a 0 to 1 multiplier for
adding that rotation as a contribution to the total. Only relevant if
[DragStyle](/docs/reference/engine/classes/DragDetector.md) is
[DragDetectorDragStyle.RotateTrackball](/docs/reference/engine/enums/DragDetectorDragStyle.md).

### Property: DragDetector.TrackballRollFactor

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
    "Physics",
    "Input"
  ]
}
```

When the cursor is outside the trackball, the [DragDetector](/docs/reference/engine/classes/DragDetector.md) can
apply a roll rotation that turns the ball as if it were mounted on a vinyl
record facing the viewer. This property is a 0 to 1 multiplier for adding
that roll rotation to the total. Only relevant if
[DragStyle](/docs/reference/engine/classes/DragDetector.md) is
[DragDetectorDragStyle.RotateTrackball](/docs/reference/engine/enums/DragDetectorDragStyle.md).

### Property: DragDetector.VRSwitchKeyCode

```json
{
  "type": "KeyCode",
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
  "category": "Mode Switching",
  "capabilities": [
    "Physics",
    "Input"
  ]
}
```

During VR input, the [KeyCode](/docs/reference/engine/enums/KeyCode.md) for toggling the secondary mode of
motion. Only applies if the drag detector's
[DragStyle](/docs/reference/engine/classes/DragDetector.md) has both primary and secondary
modes of motion.

### Property: DragDetector.WorldAxis

```json
{
  "type": "Vector3",
  "access": "ReadWrite",
  "security": {
    "read": "None",
    "write": "None"
  },
  "serialization": {
    "can_load": true,
    "can_save": false
  },
  "thread_safety": "ReadSafe",
  "category": "Drag Directions",
  "capabilities": [
    "Physics",
    "Input"
  ]
}
```

The [Axis](/docs/reference/engine/classes/DragDetector.md) expressed in world space. Relates to
orientation using the same paradigm as [Attachments](/docs/reference/engine/classes/Attachment.md).

### Property: DragDetector.WorldSecondaryAxis

```json
{
  "type": "Vector3",
  "access": "ReadWrite",
  "security": {
    "read": "None",
    "write": "None"
  },
  "serialization": {
    "can_load": true,
    "can_save": false
  },
  "thread_safety": "ReadSafe",
  "category": "Drag Directions",
  "capabilities": [
    "Physics",
    "Input"
  ]
}
```

The [SecondaryAxis](/docs/reference/engine/classes/DragDetector.md) expressed in world
space. Relates to orientation using the same paradigm as
[Attachments](/docs/reference/engine/classes/Attachment.md).

## Methods

### Method: DragDetector:AddConstraintFunction

**Signature:** `DragDetector:AddConstraintFunction(priority: int, function: Function): RBXScriptConnection`

Adds a function to modify or constrain proposed motion. The function takes
an input [CFrame](/docs/reference/engine/datatypes/CFrame.md) of **proposed** motion and returns a
[CFrame](/docs/reference/engine/datatypes/CFrame.md) of **modified** or unmodified motion. Both the input and
output are expressed relative to the reference frame. You can add multiple
functions which will be called in order by `priority`, passing the results
along in a chain.

To remove an added constraint function, call
[Disconnect()](/docs/reference/engine/datatypes/RBXScriptConnection.md) on the returned
connection object.

*Security: None · Thread Safety: Unsafe · Capabilities: Physics, Input*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `priority` | `int` |  | The order of priority for functions added via this method. Higher values take precedence over lower values. |
| `function` | `Function` |  | Function for modifying or constraining proposed motion. This function takes an input [CFrame](/docs/reference/engine/datatypes/CFrame.md) of **proposed** motion and returns a [CFrame](/docs/reference/engine/datatypes/CFrame.md) of **modified** or unmodified motion, both relative to the reference frame. |

**Returns:** `RBXScriptConnection` — Use this connection object to remove the constraint function.

### Method: DragDetector:GetReferenceFrame

**Signature:** `DragDetector:GetReferenceFrame(): CFrame`

Returns the reference [CFrame](/docs/reference/engine/datatypes/CFrame.md) in which motion is expressed; see
the [ReferenceInstance](/docs/reference/engine/classes/DragDetector.md) property for
more details.

*Security: None · Thread Safety: Unsafe · Capabilities: Physics, Input*

**Returns:** `CFrame` — The reference [CFrame](/docs/reference/engine/datatypes/CFrame.md) in which motion is expressed.

### Method: DragDetector:RestartDrag

**Signature:** `DragDetector:RestartDrag(): ()`

May be invoked from a script to restart the drag using new parameters, if
parameters such as [DragStyle](/docs/reference/engine/classes/DragDetector.md),
[Axis](/docs/reference/engine/classes/DragDetector.md), or
[SecondaryAxis](/docs/reference/engine/classes/DragDetector.md) change.

*Security: None · Thread Safety: Unsafe · Capabilities: Physics, Input*

**Returns:** `()`

### Method: DragDetector:SetDragStyleFunction

**Signature:** `DragDetector:SetDragStyleFunction(function: Function): ()`

Passes a function to be used if and only if
[DragStyle](/docs/reference/engine/classes/DragDetector.md) is set to
[DragDetectorDragStyle.Scriptable](/docs/reference/engine/enums/DragDetectorDragStyle.md). The given function is called when
responding to a [DragContinue](/docs/reference/engine/classes/DragDetector.md) signal, it
receives the signal's world space cursor ray with type [Ray](/docs/reference/engine/datatypes/Ray.md), and
it returns a [CFrame](/docs/reference/engine/datatypes/CFrame.md) containing the desired location and
orientation of the pivot in world space.

If the function returns `nil`, the object will not be moved. This is
useful if the script has not yet collected all the information it needs to
give the correct answer, or in temporary cases where you want the object
to stay where it is.

*Security: None · Thread Safety: Unsafe · Capabilities: Physics, Input*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `function` | `Function` |  | Function for monitoring [DragContinue](/docs/reference/engine/classes/DragDetector.md) signals. This function receives the signal's world space cursor ray and it returns a [CFrame](/docs/reference/engine/datatypes/CFrame.md) containing the desired location and orientation of the pivot in world space. If this function returns `nil`, the object will not be moved. |

**Returns:** `()`

### Method: DragDetector:SetPermissionPolicyFunction

**Signature:** `DragDetector:SetPermissionPolicyFunction(function: Function): ()`

Passes a function to be used if and only if
[PermissionPolicy](/docs/reference/engine/classes/DragDetector.md) is set to
[DragDetectorPermissionPolicy.Scriptable](/docs/reference/engine/enums/DragDetectorPermissionPolicy.md). The given function accepts
a [Player](/docs/reference/engine/classes/Player.md) parameter for enabling/disabling the detector for a
specific player. It also receives a `part` parameter indicating which
specific [BasePart](/docs/reference/engine/classes/BasePart.md) was clicked, such as one part within a draggable
[Model](/docs/reference/engine/classes/Model.md); this is useful for enabling/disabling the detector based on
that part's [Name](/docs/reference/engine/classes/Instance.md), [Color](/docs/reference/engine/classes/BasePart.md),
[HasTag()](/docs/reference/engine/classes/Instance.md) value, or other details.

*Security: None · Thread Safety: Unsafe · Capabilities: Physics, Input*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `function` | `Function` |  | Function for setting the detector's interactivity. This function accepts a [Player](/docs/reference/engine/classes/Player.md) parameter for enabling/disabling the detector for a specific player. It also receives a `part` parameter indicating which specific [BasePart](/docs/reference/engine/classes/BasePart.md) was clicked, such as one part within a draggable [Model](/docs/reference/engine/classes/Model.md); this is useful for enabling/disabling the detector based on that part's [Name](/docs/reference/engine/classes/Instance.md), [Color](/docs/reference/engine/classes/BasePart.md), [HasTag()](/docs/reference/engine/classes/Instance.md) value, or other details. |

**Returns:** `()`

**Set Permission Policy Function**

Demonstrates [DragDetector:SetPermissionPolicyFunction()](/docs/reference/engine/classes/DragDetector.md).

```lua
local part = Instance.new("Part")
part.Parent = workspace
local dragDetector = Instance.new("DragDetector")
dragDetector.Parent = part
dragDetector.PermissionPolicy = Enum.DragDetectorPermissionPolicy.Scriptable

dragDetector:SetPermissionPolicyFunction(function(player, part)
	if player and player:GetAttribute("IsInTurn") then
		return true
	elseif part and not part:GetAttribute("IsDraggable") then
		return false
	else
		return true
	end
end)
```

## Events

### Event: DragDetector.DragContinue

**Signature:** `DragDetector.DragContinue(playerWhoDragged: Player, cursorRay: Ray, viewFrame: CFrame, vrInputFrame: OptionalCoordinateFrame, isModeSwitchKeyDown: boolean)`

Fires when a user continues dragging the object after
[DragStart](/docs/reference/engine/classes/DragDetector.md) has been initiated.

*Security: None · Capabilities: Physics, Input*

**Parameters:**

| Name | Type | Description |
|------|------|-------------|
| `playerWhoDragged` | `Player` | The [Player](/docs/reference/engine/classes/Player.md) who initiated the drag through [DragStart](/docs/reference/engine/classes/DragDetector.md) and is now continuing the drag. |
| `cursorRay` | `Ray` | [Ray](/docs/reference/engine/datatypes/Ray.md) emanating from the cursor, aimed into the scene. |
| `viewFrame` | `CFrame` | [CFrame](/docs/reference/engine/datatypes/CFrame.md) of the user's [Camera](/docs/reference/engine/classes/Camera.md). |
| `vrInputFrame` | `OptionalCoordinateFrame` | If using a VR input device, the [CFrame](/docs/reference/engine/datatypes/CFrame.md) of the hand holding the cursor/pointer/controller. |
| `isModeSwitchKeyDown` | `boolean` | If the drag detector's [DragStyle](/docs/reference/engine/classes/DragDetector.md) has both primary and secondary modes of motion, this parameter indicates whether the user is pressing the modifier input defined through [KeyboardModeSwitchKeyCode](/docs/reference/engine/classes/DragDetector.md), [GamepadModeSwitchKeyCode](/docs/reference/engine/classes/DragDetector.md), or [VRSwitchKeyCode](/docs/reference/engine/classes/DragDetector.md). |

### Event: DragDetector.DragEnd

**Signature:** `DragDetector.DragEnd(playerWhoDragged: Player)`

Fires when a user stops dragging the object.

*Security: None · Capabilities: Physics, Input*

**Parameters:**

| Name | Type | Description |
|------|------|-------------|
| `playerWhoDragged` | `Player` | The [Player](/docs/reference/engine/classes/Player.md) who initiated the drag through [DragStart](/docs/reference/engine/classes/DragDetector.md) and has now ended (released) the drag. |

### Event: DragDetector.DragStart

**Signature:** `DragDetector.DragStart(playerWhoDragged: Player, cursorRay: Ray, viewFrame: CFrame, hitFrame: CFrame, clickedPart: BasePart, vrInputFrame: OptionalCoordinateFrame, isModeSwitchKeyDown: boolean)`

Fires when a user starts dragging the object.

*Security: None · Capabilities: Physics, Input*

**Parameters:**

| Name | Type | Description |
|------|------|-------------|
| `playerWhoDragged` | `Player` | [Player](/docs/reference/engine/classes/Player.md) who initiated the drag. |
| `cursorRay` | `Ray` | [Ray](/docs/reference/engine/datatypes/Ray.md) emanating from the cursor, aimed into the scene. |
| `viewFrame` | `CFrame` | [CFrame](/docs/reference/engine/datatypes/CFrame.md) of the user's [Camera](/docs/reference/engine/classes/Camera.md). |
| `hitFrame` | `CFrame` | The hit frame of the cursor raycast that initiated the drag. |
| `clickedPart` | `BasePart` | The part that was hit by the cursor raycast that initiated the drag. |
| `vrInputFrame` | `OptionalCoordinateFrame` | If using a VR input device, the [CFrame](/docs/reference/engine/datatypes/CFrame.md) of the hand holding the cursor/pointer/controller. |
| `isModeSwitchKeyDown` | `boolean` | If the drag detector's [DragStyle](/docs/reference/engine/classes/DragDetector.md) has both primary and secondary modes of motion, this parameter indicates whether the user is pressing the modifier input defined through [KeyboardModeSwitchKeyCode](/docs/reference/engine/classes/DragDetector.md), [GamepadModeSwitchKeyCode](/docs/reference/engine/classes/DragDetector.md), or [VRSwitchKeyCode](/docs/reference/engine/classes/DragDetector.md). |

## Inherited Members

### From [ClickDetector](/docs/reference/engine/classes/ClickDetector.md)

- **Property `CursorIcon`** (`ContentId`): Sets the cursor icon to display when the mouse is hovered over the parent
- **Property `CursorIconContent`** (`Content`): Sets the cursor icon to display when the mouse is hovered over the parent
- **Property `MaxActivationDistance`** (`float`): Maximum distance between a character and the ClickDetector or
- **Event `MouseClick`**: Fires when a player interacts with the parent of a ClickDetector
- **Event `mouseClick`**:  *(deprecated)*
- **Event `MouseHoverEnter`**: Fires when the parent of a ClickDetector or DragDetector
- **Event `MouseHoverLeave`**: Fires when a player's cursor hovers off the parent of a
- **Event `RightMouseClick`**: Fires when a player right clicks their mouse cursor on a

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