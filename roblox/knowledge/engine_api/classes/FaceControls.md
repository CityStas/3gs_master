---
name: FaceControls
last_updated: 2026-10-30T19:55:52Z
inherits:
  - Instance
  - Object
type: class
memory_category: Animation
summary: "The FaceControls object defines a set of properties for controlling the facial expressions of a Dynamic Head."
---

# Class: FaceControls

> The [FaceControls](/docs/reference/engine/classes/FaceControls.md) object defines a set of properties for controlling
> the facial expressions of a Dynamic Head.

## Description

The [FaceControls](/docs/reference/engine/classes/FaceControls.md) object defines a set of properties for controlling
the facial expressions of a character head capable of animation.

The FaceControls properties are based on the Facial Action Coding System
(FACS), a comprehensive system for describing all visually discernible facial
movement based on anatomy. [FaceControls](/docs/reference/engine/classes/FaceControls.md) properties can only be set
between 0 and 1. Different combinations of the [FaceControls](/docs/reference/engine/classes/FaceControls.md) property
values create different facial expressions. Recording multiple facial
expressions over time creates facial animation.

## What is an Animatable Head?

An animatable head is a [MeshPart](/docs/reference/engine/classes/MeshPart.md) that implements a facial rig and is
capable of playing facial animations and triggering facial expressions. A
[FaceControls](/docs/reference/engine/classes/FaceControls.md) object that is a child of a head [MeshPart](/docs/reference/engine/classes/MeshPart.md) can
change the facial expressions of the head.

A head consists of the following three components:

- Skinned MeshPart instance for the head geometry with an internal rig that
  deforms this skinned MeshPart
- FaceControls instance that drives the internal rig when properties such as
  FaceControls.JawDrop are changed.
- Cage [WrapTarget](/docs/reference/engine/classes/WrapTarget.md) instance for tight fitting facial accessories

In a third-party modeling tool, such as Blender or Maya, an artist can create
a joint-driven facial rig, pose the joints to match each of the individual
FACS controls, and save as an FBX. When a head `.FBX` is imported in Studio, a
facs-to-joint mapping is created. This mapping deforms the mesh geometry when
FaceControls properties are changed. The mapping and the facial rig (including
[Bone](/docs/reference/engine/classes/Bone.md) instances) are not exposed to developers and can only be accessed
through the FaceControls instance. The [MeshPart](/docs/reference/engine/classes/MeshPart.md) for a Dynamic Head
looks and behaves the same as a regular [MeshPart](/docs/reference/engine/classes/MeshPart.md) except when a
FaceControls instance is a child of the MeshPart. Editing the properties of
the FaceControls deforms the MeshPart's geometry. These properties are
available to animate in the Animation Editor.

See [Facial animation](/docs/en-us/avatar/dynamic-heads.md) for more
information on usage and creation of an animatable head.

## Animatable Heads in the Marketplace

If you are publishing your head to the Marketplace, your head asset must
include a minimum subset of face controls. Roblox's publishing validation
rejects assets without the following required poses:

- EyesLookDown
- EyesLookLeft
- EyesLookRight
- EyesLookUp
- JawDrop
- LeftEyeClosed
- LeftLipCornerPuller
- LeftLipStretcher
- LeftLowerLipDepressor
- LeftUpperLipRaiser
- LipsTogether
- Pucker
- RightEyeClosed
- RightLipCornerPuller
- RightLipStretcher
- RightLowerLipDepressor
- RightUpperLipRaiser

See
[FACS poses reference](/docs/en-us/avatar/dynamic-heads/facs-poses-reference.md)
for more information on usage and creation of an animatable head.

## Properties

### Property: FaceControls.ChinRaiser

```json
{
  "type": "float",
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
  "category": "Mouth",
  "capabilities": [
    "Animation"
  ]
}
```

Raises the chin up; moves the lower lip upwards

### Property: FaceControls.ChinRaiserUpperLip

```json
{
  "type": "float",
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
  "category": "Mouth",
  "capabilities": [
    "Animation"
  ]
}
```

Moves the upper lip when ChinRaiser is engaged and touching the upper lip

### Property: FaceControls.Corrugator

```json
{
  "type": "float",
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
  "category": "Brows",
  "capabilities": [
    "Animation"
  ]
}
```

Brings the left and right brows inward together

### Property: FaceControls.EyesLookDown

```json
{
  "type": "float",
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
  "category": "Eyes",
  "capabilities": [
    "Animation"
  ]
}
```

Moves gaze down. This is a required pose for avatars.

### Property: FaceControls.EyesLookLeft

```json
{
  "type": "float",
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
  "category": "Eyes",
  "capabilities": [
    "Animation"
  ]
}
```

Moves gaze left. This is a required pose for avatars.

### Property: FaceControls.EyesLookRight

```json
{
  "type": "float",
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
  "category": "Eyes",
  "capabilities": [
    "Animation"
  ]
}
```

Moves gaze right. This is a required pose for avatars.

### Property: FaceControls.EyesLookUp

```json
{
  "type": "float",
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
  "category": "Eyes",
  "capabilities": [
    "Animation"
  ]
}
```

Moves gaze up. This is a required pose for avatars.

### Property: FaceControls.FlatPucker

```json
{
  "type": "float",
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
  "category": "Mouth",
  "capabilities": [
    "Animation"
  ]
}
```

Also known as lip tightener; brings the corners of the mouth inward and
pressing the lips back against the teeth

### Property: FaceControls.Funneler

```json
{
  "type": "float",
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
  "category": "Mouth",
  "capabilities": [
    "Animation"
  ]
}
```

Makes a 'O' shape with the mouth

### Property: FaceControls.JawDrop

```json
{
  "type": "float",
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
  "category": "Jaw",
  "capabilities": [
    "Animation"
  ]
}
```

Lowers the jaw downward opening the mouth. This is a required pose for
avatars.

### Property: FaceControls.JawLeft

```json
{
  "type": "float",
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
  "category": "Jaw",
  "capabilities": [
    "Animation"
  ]
}
```

Moves the mouth and jaw to the character's left. Like all
[FaceControls](/docs/reference/engine/classes/FaceControls.md) properties, this value is clamped between 0 and 1 and
defaults to 0, meaning no displacement. [FaceControls.JawRight](/docs/reference/engine/classes/FaceControls.md)
applies the opposite displacement, moving the mouth and jaw to the
character's right.

### Property: FaceControls.JawRight

```json
{
  "type": "float",
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
  "category": "Jaw",
  "capabilities": [
    "Animation"
  ]
}
```

Moves mouth and jaw to the right (character right)

### Property: FaceControls.LeftBrowLowerer

```json
{
  "type": "float",
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
  "category": "Brows",
  "capabilities": [
    "Animation"
  ]
}
```

Lowers the left brow down

### Property: FaceControls.LeftCheekPuff

```json
{
  "type": "float",
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
  "category": "Mouth",
  "capabilities": [
    "Animation"
  ]
}
```

Puffs up the left cheek

### Property: FaceControls.LeftCheekRaiser

```json
{
  "type": "float",
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
  "category": "Eyes",
  "capabilities": [
    "Animation"
  ]
}
```

Squints the left eye

### Property: FaceControls.LeftDimpler

```json
{
  "type": "float",
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
  "category": "Mouth",
  "capabilities": [
    "Animation"
  ]
}
```

Moves the corners of the mouth back in Z

### Property: FaceControls.LeftEyeClosed

```json
{
  "type": "float",
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
  "category": "Eyes",
  "capabilities": [
    "Animation"
  ]
}
```

Closes the left eyelid. This is a required pose for avatars.

### Property: FaceControls.LeftEyeUpperLidRaiser

```json
{
  "type": "float",
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
  "category": "Eyes",
  "capabilities": [
    "Animation"
  ]
}
```

Raises the left eyelid upwards to reveal more of the eye white above the
iris

### Property: FaceControls.LeftInnerBrowRaiser

```json
{
  "type": "float",
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
  "category": "Brows",
  "capabilities": [
    "Animation"
  ]
}
```

Raises the interior half of the left brow upwards

### Property: FaceControls.LeftLipCornerDown

```json
{
  "type": "float",
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
  "category": "Mouth",
  "capabilities": [
    "Animation"
  ]
}
```

Lowers the corners of the mouth downwards in a frown

### Property: FaceControls.LeftLipCornerPuller

```json
{
  "type": "float",
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
  "category": "Mouth",
  "capabilities": [
    "Animation"
  ]
}
```

Raises the corners of the mouth upwards in a smile. This is a required
pose for avatars.

### Property: FaceControls.LeftLipStretcher

```json
{
  "type": "float",
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
  "category": "Mouth",
  "capabilities": [
    "Animation"
  ]
}
```

Stretches the corners of the mouth apart. This is a required pose for
avatars.

### Property: FaceControls.LeftLowerLipDepressor

```json
{
  "type": "float",
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
  "category": "Mouth",
  "capabilities": [
    "Animation"
  ]
}
```

Lowers the lower lip down away from the upper lip revealing the lower
teeth. This is a required pose for avatars.

### Property: FaceControls.LeftNoseWrinkler

```json
{
  "type": "float",
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
  "category": "Brows",
  "capabilities": [
    "Animation"
  ]
}
```

Raise the left nostril, pulls the brow down slightly, and wrinkles on the
side of the nose

### Property: FaceControls.LeftOuterBrowRaiser

```json
{
  "type": "float",
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
  "category": "Brows",
  "capabilities": [
    "Animation"
  ]
}
```

Raises the outer part of the left brow upwards

### Property: FaceControls.LeftUpperLipRaiser

```json
{
  "type": "float",
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
  "category": "Mouth",
  "capabilities": [
    "Animation"
  ]
}
```

Raises the left upper lip away from the lower lip revealing the upper
teeth. This is a required pose for avatars.

### Property: FaceControls.LipPresser

```json
{
  "type": "float",
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
  "category": "Mouth",
  "capabilities": [
    "Animation"
  ]
}
```

Presses the lips together

### Property: FaceControls.LipsTogether

```json
{
  "type": "float",
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
  "category": "Mouth",
  "capabilities": [
    "Animation"
  ]
}
```

Brings the lips together relative to JawDrop. This is a required pose for
avatars.

### Property: FaceControls.LowerLipSuck

```json
{
  "type": "float",
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
  "category": "Mouth",
  "capabilities": [
    "Animation"
  ]
}
```

Rolls the lower lip up over the teeth

### Property: FaceControls.MouthLeft

```json
{
  "type": "float",
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
  "category": "Mouth",
  "capabilities": [
    "Animation"
  ]
}
```

Moves the mouth left

### Property: FaceControls.MouthRight

```json
{
  "type": "float",
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
  "category": "Mouth",
  "capabilities": [
    "Animation"
  ]
}
```

Moves the mouth right

### Property: FaceControls.Pucker

```json
{
  "type": "float",
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
  "category": "Mouth",
  "capabilities": [
    "Animation"
  ]
}
```

Makes a kiss-like shape with the mouth. This is a required pose for
avatars.

### Property: FaceControls.RightBrowLowerer

```json
{
  "type": "float",
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
  "category": "Brows",
  "capabilities": [
    "Animation"
  ]
}
```

Lowers the right brow down

### Property: FaceControls.RightCheekPuff

```json
{
  "type": "float",
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
  "category": "Mouth",
  "capabilities": [
    "Animation"
  ]
}
```

Puffs up the right cheek

### Property: FaceControls.RightCheekRaiser

```json
{
  "type": "float",
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
  "category": "Eyes",
  "capabilities": [
    "Animation"
  ]
}
```

Squints the right eye

### Property: FaceControls.RightDimpler

```json
{
  "type": "float",
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
  "category": "Mouth",
  "capabilities": [
    "Animation"
  ]
}
```

Moves the corners of the mouth back in Z

### Property: FaceControls.RightEyeClosed

```json
{
  "type": "float",
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
  "category": "Eyes",
  "capabilities": [
    "Animation"
  ]
}
```

Closes the right eyelid. This is a required pose for avatars.

### Property: FaceControls.RightEyeUpperLidRaiser

```json
{
  "type": "float",
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
  "category": "Eyes",
  "capabilities": [
    "Animation"
  ]
}
```

Raises the right eyelid upwards to reveal more of the eye white above the
iris

### Property: FaceControls.RightInnerBrowRaiser

```json
{
  "type": "float",
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
  "category": "Brows",
  "capabilities": [
    "Animation"
  ]
}
```

Raises the interior half of the right brow upwards

### Property: FaceControls.RightLipCornerDown

```json
{
  "type": "float",
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
  "category": "Mouth",
  "capabilities": [
    "Animation"
  ]
}
```

Lowers the corners of the mouth downwards in a frown

### Property: FaceControls.RightLipCornerPuller

```json
{
  "type": "float",
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
  "category": "Mouth",
  "capabilities": [
    "Animation"
  ]
}
```

Raises the corners of the mouth upwards in a smile. This is a required
pose for avatars.

### Property: FaceControls.RightLipStretcher

```json
{
  "type": "float",
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
  "category": "Mouth",
  "capabilities": [
    "Animation"
  ]
}
```

Stretches the corners of the mouth apart. This is a required pose for
avatars.

### Property: FaceControls.RightLowerLipDepressor

```json
{
  "type": "float",
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
  "category": "Mouth",
  "capabilities": [
    "Animation"
  ]
}
```

Lowers the lower lip down away from the upper lip revealing the lower
teeth. This is a required pose for avatars.

### Property: FaceControls.RightNoseWrinkler

```json
{
  "type": "float",
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
  "category": "Brows",
  "capabilities": [
    "Animation"
  ]
}
```

Raises the right nostril, pulls the brow down slightly, and wrinkles on
the side of the nose

### Property: FaceControls.RightOuterBrowRaiser

```json
{
  "type": "float",
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
  "category": "Brows",
  "capabilities": [
    "Animation"
  ]
}
```

Raises the outer part of the right brow upwards

### Property: FaceControls.RightUpperLipRaiser

```json
{
  "type": "float",
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
  "category": "Mouth",
  "capabilities": [
    "Animation"
  ]
}
```

Raises the right upper lip away from the lower lip revealing the upper
teeth. This is a required pose for avatars.

### Property: FaceControls.TongueDown

```json
{
  "type": "float",
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
  "category": "Tongue",
  "capabilities": [
    "Animation"
  ]
}
```

Bends the tongue down

### Property: FaceControls.TongueOut

```json
{
  "type": "float",
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
  "category": "Tongue",
  "capabilities": [
    "Animation"
  ]
}
```

Extends the tip of the tongue out of the mouth

### Property: FaceControls.TongueUp

```json
{
  "type": "float",
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
  "category": "Tongue",
  "capabilities": [
    "Animation"
  ]
}
```

Bends the tongue up

### Property: FaceControls.UpperLipSuck

```json
{
  "type": "float",
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
  "category": "Mouth",
  "capabilities": [
    "Animation"
  ]
}
```

Rolls the upper lip around the teeth

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