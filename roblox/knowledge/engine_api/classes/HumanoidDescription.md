---
name: HumanoidDescription
last_updated: 2026-10-30T19:55:52Z
inherits:
  - Instance
  - Object
type: class
memory_category: Instances
summary: "Describes the appearance of a Humanoid character including body parts, accessories, colors, scales, animations, and emotes."
---

# Class: HumanoidDescription

> Describes the appearance of a Humanoid character including body parts,
> accessories, colors, scales, animations, and emotes.

## Description

**HumanoidDescription** is an object that stores a description of a
[Humanoid](/docs/reference/engine/classes/Humanoid.md) for R6 and
[R15 rigs](/docs/en-us/avatar/character-bodies/specifications.md#rigging). It can
be [applied](/docs/reference/engine/classes/Humanoid.md) in order to set a rig's
scaling, clothing ([Shirt](/docs/reference/engine/classes/Shirt.md), [Pants](/docs/reference/engine/classes/Pants.md), [ShirtGraphic](/docs/reference/engine/classes/ShirtGraphic.md)),
[Accessories](/docs/reference/engine/classes/Accessory.md), [Animations](/docs/reference/engine/classes/Animation.md) and
[BodyColors](/docs/reference/engine/classes/BodyColors.md).

You can get a HumanoidDescription by using the following functions:

- [Players:GetHumanoidDescriptionFromUserIdAsync()](/docs/reference/engine/classes/Players.md), for an outfit
  currently being worn by a user on Roblox.
- [Players:GetHumanoidDescriptionFromOutfitIdAsync()](/docs/reference/engine/classes/Players.md), for an outfit
  created by a user on Roblox.
- You can create a Humanoid rig model from a HumanoidDescription through
  [Players:CreateHumanoidModelFromDescriptionAsync()](/docs/reference/engine/classes/Players.md).

See also:

- [HumanoidDescription System](/docs/en-us/characters/appearance.md#humanoiddescription),
  for more information on [HumanoidDescription](/docs/reference/engine/classes/HumanoidDescription.md).

## Properties

### Property: HumanoidDescription.AccessoryBlob

```json
{
  "type": "string",
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
  "category": "Accessories",
  "capabilities": [
    "AvatarAppearance"
  ]
}
```

A JSON formatted array of Layered clothing where each table in the entry
in the array describes an accessory's AssetId, AccessoryType, Order, and
(optionally) Puffiness as key-value pairs. This can be edited in the
properties windows for the [HumanoidDescription](/docs/reference/engine/classes/HumanoidDescription.md).

To make changes from Luau (which is recommended over editing the JSON
directly), use [HumanoidDescription:SetAccessories()](/docs/reference/engine/classes/HumanoidDescription.md) and
[HumanoidDescription:GetAccessories()](/docs/reference/engine/classes/HumanoidDescription.md). These methods can also be
enabled to work with rigid accessories by setting IncludeRigidAccessories
parameters to true.

### Property: HumanoidDescription.BackAccessory

```json
{
  "type": "string",
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
  "category": "Accessories",
  "capabilities": [
    "AvatarAppearance"
  ]
}
```

**BackAccessory** is a comma-separated list of asset IDs that determine
what accessories should be added when the description is
[applied](/docs/reference/engine/classes/Humanoid.md). The list cannot contain
duplicates.

An error is thrown if you try to apply a new description which shares any
assets with the existing description but a different accessory property.

See also:

- [HumanoidDescription System](/docs/en-us/characters/appearance.md#humanoiddescription),
  for more information on [HumanoidDescription](/docs/reference/engine/classes/HumanoidDescription.md).
- [FaceAccessory](/docs/reference/engine/classes/HumanoidDescription.md),
  [FrontAccessory](/docs/reference/engine/classes/HumanoidDescription.md),
  [HairAccessory](/docs/reference/engine/classes/HumanoidDescription.md),
  [HatAccessory](/docs/reference/engine/classes/HumanoidDescription.md),
  [NeckAccessory](/docs/reference/engine/classes/HumanoidDescription.md),
  [ShouldersAccessory](/docs/reference/engine/classes/HumanoidDescription.md) and
  [WaistAccessory](/docs/reference/engine/classes/HumanoidDescription.md), which are
  similar properties that apply accessories like this one

### Property: HumanoidDescription.BodyTypeScale

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
  "category": "Scale",
  "capabilities": [
    "AvatarAppearance"
  ]
}
```

**BodyTypeScale** determines the factor by which the shape of a
[Humanoid](/docs/reference/engine/classes/Humanoid.md) is interpolated from the standard R15 body shape (0) to a
taller and more slender body type (1). Values outside the range of 0 to 1
are clamped. When the description is applied through
[Humanoid:ApplyDescriptionAsync()](/docs/reference/engine/classes/Humanoid.md), this value maps to a
**BodyTypeScale** [NumberValue](/docs/reference/engine/classes/NumberValue.md) within the [Humanoid](/docs/reference/engine/classes/Humanoid.md).

Note that when the value of this property is 0, the
[ProportionScale](/docs/reference/engine/classes/HumanoidDescription.md) property has
no effect.

#### See Also

- [HumanoidDescription System](/docs/en-us/characters/appearance.md#humanoiddescription),
  for more information on [HumanoidDescription](/docs/reference/engine/classes/HumanoidDescription.md).
- [ProportionScale](/docs/reference/engine/classes/HumanoidDescription.md), which also
  affects rig proportions when this property is non-zero
- [WidthScale](/docs/reference/engine/classes/HumanoidDescription.md),
  [HeightScale](/docs/reference/engine/classes/HumanoidDescription.md) and
  [DepthScale](/docs/reference/engine/classes/HumanoidDescription.md), which provide finer
  control over the dimensions of a rig
- [HeadScale](/docs/reference/engine/classes/HumanoidDescription.md), which provides specific
  control over the scale of the rig's head

### Property: HumanoidDescription.ClimbAnimation

```json
{
  "type": "int64",
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
  "category": "Animation",
  "capabilities": [
    "AvatarAppearance"
  ]
}
```

When this description is [applied](/docs/reference/engine/classes/Humanoid.md)
to a [Humanoid](/docs/reference/engine/classes/Humanoid.md), **ClimbAnimation** determines the
[Animation.AnimationId](/docs/reference/engine/classes/Animation.md) to play when its
[state](/docs/reference/engine/classes/Humanoid.md) is [Climbing](/docs/reference/engine/enums/HumanoidStateType.md).

See also:

- [FallAnimation](/docs/reference/engine/classes/HumanoidDescription.md),
  [IdleAnimation](/docs/reference/engine/classes/HumanoidDescription.md),
  [JumpAnimation](/docs/reference/engine/classes/HumanoidDescription.md),
  [RunAnimation](/docs/reference/engine/classes/HumanoidDescription.md),
  [SwimAnimation](/docs/reference/engine/classes/HumanoidDescription.md) and
  [WalkAnimation](/docs/reference/engine/classes/HumanoidDescription.md), which are
  similar properties that determine animations to play on the rig

### Property: HumanoidDescription.DepthScale

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
  "category": "Scale",
  "capabilities": [
    "AvatarAppearance"
  ]
}
```

**DepthScale** determines by what factor the depth (back-to-front
distance) of a [Humanoid](/docs/reference/engine/classes/Humanoid.md) is scaled, as well as all accessories not
attached to its head. When the description is applied through
[Humanoid:ApplyDescriptionAsync()](/docs/reference/engine/classes/Humanoid.md), this value maps to a
**BodyDepthScale** [NumberValue](/docs/reference/engine/classes/NumberValue.md) within the Humanoid.

#### See Also

- [HumanoidDescription System](/docs/en-us/characters/appearance.md#humanoiddescription),
  for more information on [HumanoidDescription](/docs/reference/engine/classes/HumanoidDescription.md).
- [BodyTypeScale](/docs/reference/engine/classes/HumanoidDescription.md) and
  [ProportionScale](/docs/reference/engine/classes/HumanoidDescription.md), which can
  provide more realistic rig proportions
- [WidthScale](/docs/reference/engine/classes/HumanoidDescription.md) and
  [HeightScale](/docs/reference/engine/classes/HumanoidDescription.md)

### Property: HumanoidDescription.Face

```json
{
  "type": "int64",
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
  "category": "Body Parts",
  "capabilities": [
    "AvatarAppearance"
  ]
}
```

**Face** determines the asset ID of the Face to be
[applied](/docs/reference/engine/classes/Humanoid.md) to a [Humanoid](/docs/reference/engine/classes/Humanoid.md).
The type of the asset ID provided **must be for a Face** type asset and
not a Decal or Image type asset.

The actual face texture is rendered using a [Decal](/docs/reference/engine/classes/Decal.md) in the Head
named "face" or "Face".

See also:

- [HumanoidDescription System](/docs/en-us/characters/appearance.md#humanoiddescription),
  for more information on [HumanoidDescription](/docs/reference/engine/classes/HumanoidDescription.md).
- [GraphicTShirt](/docs/reference/engine/classes/HumanoidDescription.md),
  [Shirt](/docs/reference/engine/classes/HumanoidDescription.md) and
  [Pants](/docs/reference/engine/classes/HumanoidDescription.md), which also apply textures to a
  rig
- [Head](/docs/reference/engine/classes/HumanoidDescription.md), which can change the mesh of the
  head
- [FaceAccessory](/docs/reference/engine/classes/HumanoidDescription.md), which can apply
  one or more [Accessory](/docs/reference/engine/classes/Accessory.md) objects to the face

### Property: HumanoidDescription.FaceAccessory

```json
{
  "type": "string",
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
  "category": "Accessories",
  "capabilities": [
    "AvatarAppearance"
  ]
}
```

**FaceAccessory** is a comma-separated list of asset IDs that determine
what accessories should be added when the description is
[applied](/docs/reference/engine/classes/Humanoid.md), usually those attached
to the front of its face (such as glasses). The list does not contain
duplicates.

An error is thrown if you try to apply a new description which shares any
assets with the existing description but a different accessory property.

See also:

- [HumanoidDescription System](/docs/en-us/characters/appearance.md#humanoiddescription),
  for more information on [HumanoidDescription](/docs/reference/engine/classes/HumanoidDescription.md).
- [BackAccessory](/docs/reference/engine/classes/HumanoidDescription.md),
  [FrontAccessory](/docs/reference/engine/classes/HumanoidDescription.md),
  [HairAccessory](/docs/reference/engine/classes/HumanoidDescription.md),
  [HatAccessory](/docs/reference/engine/classes/HumanoidDescription.md),
  [NeckAccessory](/docs/reference/engine/classes/HumanoidDescription.md),
  [ShouldersAccessory](/docs/reference/engine/classes/HumanoidDescription.md) and
  [WaistAccessory](/docs/reference/engine/classes/HumanoidDescription.md), which are
  similar properties that apply accessories like this one
- [Face](/docs/reference/engine/classes/HumanoidDescription.md), a property that determines what
  Face texture is used on the head

### Property: HumanoidDescription.FallAnimation

```json
{
  "type": "int64",
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
  "category": "Animation",
  "capabilities": [
    "AvatarAppearance"
  ]
}
```

When this description is [applied](/docs/reference/engine/classes/Humanoid.md)
to a [Humanoid](/docs/reference/engine/classes/Humanoid.md), **FallAnimation** determines the
[Animation.AnimationId](/docs/reference/engine/classes/Animation.md) to play when its
[state](/docs/reference/engine/classes/Humanoid.md) is [Freefall](/docs/reference/engine/enums/HumanoidStateType.md).

See also:

- [HumanoidDescription System](/docs/en-us/characters/appearance.md#humanoiddescription),
  for more information on [HumanoidDescription](/docs/reference/engine/classes/HumanoidDescription.md).
- [ClimbAnimation](/docs/reference/engine/classes/HumanoidDescription.md),
  [IdleAnimation](/docs/reference/engine/classes/HumanoidDescription.md),
  [JumpAnimation](/docs/reference/engine/classes/HumanoidDescription.md),
  [RunAnimation](/docs/reference/engine/classes/HumanoidDescription.md),
  [SwimAnimation](/docs/reference/engine/classes/HumanoidDescription.md) and
  [WalkAnimation](/docs/reference/engine/classes/HumanoidDescription.md), which are
  similar properties that determine animations to play on the rig

### Property: HumanoidDescription.FrontAccessory

```json
{
  "type": "string",
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
  "category": "Accessories",
  "capabilities": [
    "AvatarAppearance"
  ]
}
```

**FrontAccessory** is a comma-separated list of asset IDs that determine
what accessories should be added when the description is
[applied](/docs/reference/engine/classes/Humanoid.md), usually those attached
to front of its torso (such as medals or ties). The list does not contain
duplicates.

An error is thrown if you try to apply a new description which shares any
assets with the existing description but a different accessory property.

See also:

- [HumanoidDescription System](/docs/en-us/characters/appearance.md#humanoiddescription),
  for more information on [HumanoidDescription](/docs/reference/engine/classes/HumanoidDescription.md).
- [BackAccessory](/docs/reference/engine/classes/HumanoidDescription.md),
  [FaceAccessory](/docs/reference/engine/classes/HumanoidDescription.md),
  [HairAccessory](/docs/reference/engine/classes/HumanoidDescription.md),
  [HatAccessory](/docs/reference/engine/classes/HumanoidDescription.md),
  [NeckAccessory](/docs/reference/engine/classes/HumanoidDescription.md),
  [ShouldersAccessory](/docs/reference/engine/classes/HumanoidDescription.md) and
  [WaistAccessory](/docs/reference/engine/classes/HumanoidDescription.md), which are
  similar properties that apply accessories like this one

### Property: HumanoidDescription.GraphicTShirt

```json
{
  "type": "int64",
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
  "category": "Clothes",
  "capabilities": [
    "AvatarAppearance"
  ]
}
```

**GraphicTShirt** determines the [Graphic](/docs/reference/engine/classes/ShirtGraphic.md) used
by a [ShirtGraphic](/docs/reference/engine/classes/ShirtGraphic.md) instance when
[Humanoid:ApplyDescriptionAsync()](/docs/reference/engine/classes/Humanoid.md) is called on a [Humanoid](/docs/reference/engine/classes/Humanoid.md).
The asset type must be for a **T‑Shirt**, not a **Decal** or **Image**.

#### See Also

- [HumanoidDescription System](/docs/en-us/characters/appearance.md#humanoiddescription),
  for more information on [HumanoidDescription](/docs/reference/engine/classes/HumanoidDescription.md).
- [Shirt](/docs/reference/engine/classes/HumanoidDescription.md), which can provide the same
  functionality in addition to providing textures for the entire torso and
  arms
- [TorsoColor](/docs/reference/engine/classes/HumanoidDescription.md), which can change the
  color of the torso underneath the t-shirt texture

### Property: HumanoidDescription.HairAccessory

```json
{
  "type": "string",
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
  "category": "Accessories",
  "capabilities": [
    "AvatarAppearance"
  ]
}
```

**HairAccessory** is a comma-separated list of asset IDs that determine
what accessories should be added when the description is
[applied](/docs/reference/engine/classes/Humanoid.md), usually those attached
to its head resembling hair. The list does not contain duplicates.

An error is thrown if you try to apply a new description which shares any
assets with the existing description but a different accessory property.

See also:

- [HumanoidDescription System](/docs/en-us/characters/appearance.md#humanoiddescription),
  for more information on [HumanoidDescription](/docs/reference/engine/classes/HumanoidDescription.md).
- [BackAccessory](/docs/reference/engine/classes/HumanoidDescription.md),
  [FaceAccessory](/docs/reference/engine/classes/HumanoidDescription.md),
  [FrontAccessory](/docs/reference/engine/classes/HumanoidDescription.md),
  [HatAccessory](/docs/reference/engine/classes/HumanoidDescription.md),
  [NeckAccessory](/docs/reference/engine/classes/HumanoidDescription.md),
  [ShouldersAccessory](/docs/reference/engine/classes/HumanoidDescription.md) and
  [WaistAccessory](/docs/reference/engine/classes/HumanoidDescription.md), which are
  similar properties that apply accessories like this one

### Property: HumanoidDescription.HatAccessory

```json
{
  "type": "string",
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
  "category": "Accessories",
  "capabilities": [
    "AvatarAppearance"
  ]
}
```

**HatAccessory** is a comma-separated list of asset IDs that determine
what accessories should be added when the description is
[applied](/docs/reference/engine/classes/Humanoid.md), usually those attached
to its head. The list does not contain duplicates.

An error is thrown if you try to apply a new description which shares any
assets with the existing description but a different accessory property.

See also:

- [HumanoidDescription System](/docs/en-us/characters/appearance.md#humanoiddescription),
  for more information on [HumanoidDescription](/docs/reference/engine/classes/HumanoidDescription.md).
- [BackAccessory](/docs/reference/engine/classes/HumanoidDescription.md),
  [FaceAccessory](/docs/reference/engine/classes/HumanoidDescription.md),
  [FrontAccessory](/docs/reference/engine/classes/HumanoidDescription.md),
  [HairAccessory](/docs/reference/engine/classes/HumanoidDescription.md),
  [NeckAccessory](/docs/reference/engine/classes/HumanoidDescription.md),
  [ShouldersAccessory](/docs/reference/engine/classes/HumanoidDescription.md) and
  [WaistAccessory](/docs/reference/engine/classes/HumanoidDescription.md), which are
  similar properties that apply accessories like this one

### Property: HumanoidDescription.Head

```json
{
  "type": "int64",
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
  "category": "Body Parts",
  "capabilities": [
    "AvatarAppearance"
  ]
}
```

**Head** determines the asset ID of the Head to be
[applied](/docs/reference/engine/classes/Humanoid.md) to a [Humanoid](/docs/reference/engine/classes/Humanoid.md).

See also:

- [HumanoidDescription System](/docs/en-us/characters/appearance.md#humanoiddescription),
  for more information on [HumanoidDescription](/docs/reference/engine/classes/HumanoidDescription.md).
- [Torso](/docs/reference/engine/classes/HumanoidDescription.md),
  [RightArm](/docs/reference/engine/classes/HumanoidDescription.md),
  [LeftArm](/docs/reference/engine/classes/HumanoidDescription.md),
  [RightLeg](/docs/reference/engine/classes/HumanoidDescription.md) and
  [LeftLeg](/docs/reference/engine/classes/HumanoidDescription.md), which are similar
  properties that also control body part
- [HeadColor](/docs/reference/engine/classes/HumanoidDescription.md), which controls the
  color of this limb
- [HatAccessory](/docs/reference/engine/classes/HumanoidDescription.md),
  [HairAccessory](/docs/reference/engine/classes/HumanoidDescription.md) and
  [FaceAccessory](/docs/reference/engine/classes/HumanoidDescription.md), which all can
  apply [Accessory](/docs/reference/engine/classes/Accessory.md) objects which are joined to the head

### Property: HumanoidDescription.HeadColor

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
    "can_save": false
  },
  "thread_safety": "ReadSafe",
  "category": "Body Colors",
  "capabilities": [
    "AvatarAppearance"
  ]
}
```

**HeadColor** determines the [BodyColors.HeadColor3](/docs/reference/engine/classes/BodyColors.md) and
[BodyColors.HeadColor](/docs/reference/engine/classes/BodyColors.md) of a [Humanoid](/docs/reference/engine/classes/Humanoid.md) when the description is
[applied](/docs/reference/engine/classes/Humanoid.md).

See also:

- [HumanoidDescription System](/docs/en-us/characters/appearance.md#humanoiddescription),
  for more information on [HumanoidDescription](/docs/reference/engine/classes/HumanoidDescription.md).
- [TorsoColor](/docs/reference/engine/classes/HumanoidDescription.md),
  [LeftArmColor](/docs/reference/engine/classes/HumanoidDescription.md),
  [RightArmColor](/docs/reference/engine/classes/HumanoidDescription.md),
  [LeftLegColor](/docs/reference/engine/classes/HumanoidDescription.md), and
  [RightLegColor](/docs/reference/engine/classes/HumanoidDescription.md), which are
  similar properties that also control body colors
- [Head](/docs/reference/engine/classes/HumanoidDescription.md), which controls the mesh used for
  the head
- [Face](/docs/reference/engine/classes/HumanoidDescription.md), which applies a texture to the
  front of the head

### Property: HumanoidDescription.HeadScale

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
  "category": "Scale",
  "capabilities": [
    "AvatarAppearance"
  ]
}
```

**HeadScale** determines by what factor the **Head** object of a
[Humanoid](/docs/reference/engine/classes/Humanoid.md) is scaled, as well as any accessories attached to it
(such as those specified by
[HatAccessory](/docs/reference/engine/classes/HumanoidDescription.md) and
[HairAccessory](/docs/reference/engine/classes/HumanoidDescription.md)). When the
description is applied through [Humanoid:ApplyDescriptionAsync()](/docs/reference/engine/classes/Humanoid.md),
this value maps to a **HeadScale** [NumberValue](/docs/reference/engine/classes/NumberValue.md) within the
[Humanoid](/docs/reference/engine/classes/Humanoid.md).

#### See Also

- [HumanoidDescription System](/docs/en-us/characters/appearance.md#humanoiddescription),
  for more information on [HumanoidDescription](/docs/reference/engine/classes/HumanoidDescription.md).
- [BodyTypeScale](/docs/reference/engine/classes/HumanoidDescription.md) and
  [ProportionScale](/docs/reference/engine/classes/HumanoidDescription.md), which can
  provide realistic rig proportions
- [WidthScale](/docs/reference/engine/classes/HumanoidDescription.md),
  [HeightScale](/docs/reference/engine/classes/HumanoidDescription.md) and
  [DepthScale](/docs/reference/engine/classes/HumanoidDescription.md), which provide finer
  control over other dimensions of a rig

### Property: HumanoidDescription.HeightScale

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
  "category": "Scale",
  "capabilities": [
    "AvatarAppearance"
  ]
}
```

**HeightScale** determines by what factor the height (top-to-bottom
distance) of a [Humanoid](/docs/reference/engine/classes/Humanoid.md) is scaled, as well as all accessories not
attached to its head. When the description is applied through
[Humanoid:ApplyDescriptionAsync()](/docs/reference/engine/classes/Humanoid.md), this value maps to a
**BodyHeightScale** [NumberValue](/docs/reference/engine/classes/NumberValue.md) within the [Humanoid](/docs/reference/engine/classes/Humanoid.md).

#### See Also

- [HumanoidDescription System](/docs/en-us/characters/appearance.md#humanoiddescription),
  for more information on [HumanoidDescription](/docs/reference/engine/classes/HumanoidDescription.md).
- [BodyTypeScale](/docs/reference/engine/classes/HumanoidDescription.md) and
  [ProportionScale](/docs/reference/engine/classes/HumanoidDescription.md), which can
  provide more realistic rig proportions
- [WidthScale](/docs/reference/engine/classes/HumanoidDescription.md) and
  [DepthScale](/docs/reference/engine/classes/HumanoidDescription.md)

### Property: HumanoidDescription.IdleAnimation

```json
{
  "type": "int64",
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
  "category": "Animation",
  "capabilities": [
    "AvatarAppearance"
  ]
}
```

When this description is [applied](/docs/reference/engine/classes/Humanoid.md)
to a [Humanoid](/docs/reference/engine/classes/Humanoid.md), **IdleAnimation** determines the
[Animation.AnimationId](/docs/reference/engine/classes/Animation.md) to play when its
[state](/docs/reference/engine/classes/Humanoid.md) is [Running](/docs/reference/engine/enums/HumanoidStateType.md) at a
speed near zero.

See also:

- [HumanoidDescription System](/docs/en-us/characters/appearance.md#humanoiddescription),
  for more information on [HumanoidDescription](/docs/reference/engine/classes/HumanoidDescription.md).
- [ClimbAnimation](/docs/reference/engine/classes/HumanoidDescription.md),
  [FallAnimation](/docs/reference/engine/classes/HumanoidDescription.md),
  [JumpAnimation](/docs/reference/engine/classes/HumanoidDescription.md),
  [RunAnimation](/docs/reference/engine/classes/HumanoidDescription.md),
  [SwimAnimation](/docs/reference/engine/classes/HumanoidDescription.md) and
  [WalkAnimation](/docs/reference/engine/classes/HumanoidDescription.md), which are
  similar properties that determine animations to play on the rig

### Property: HumanoidDescription.JumpAnimation

```json
{
  "type": "int64",
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
  "category": "Animation",
  "capabilities": [
    "AvatarAppearance"
  ]
}
```

When this description is [applied](/docs/reference/engine/classes/Humanoid.md)
to a [Humanoid](/docs/reference/engine/classes/Humanoid.md), **JumpAnimation** determines the
[Animation.AnimationId](/docs/reference/engine/classes/Animation.md) to play when its
[state](/docs/reference/engine/classes/Humanoid.md) is [Jumping](/docs/reference/engine/enums/HumanoidStateType.md).

See also:

- [HumanoidDescription System](/docs/en-us/characters/appearance.md#humanoiddescription),
  for more information on [HumanoidDescription](/docs/reference/engine/classes/HumanoidDescription.md).
- [ClimbAnimation](/docs/reference/engine/classes/HumanoidDescription.md),
  [FallAnimation](/docs/reference/engine/classes/HumanoidDescription.md),
  [IdleAnimation](/docs/reference/engine/classes/HumanoidDescription.md),
  [RunAnimation](/docs/reference/engine/classes/HumanoidDescription.md),
  [SwimAnimation](/docs/reference/engine/classes/HumanoidDescription.md) and
  [WalkAnimation](/docs/reference/engine/classes/HumanoidDescription.md), which are
  similar properties that determine animations to play on the rig

### Property: HumanoidDescription.LeftArm

```json
{
  "type": "int64",
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
  "category": "Body Parts",
  "capabilities": [
    "AvatarAppearance"
  ]
}
```

**LeftArm** determines the asset ID of the LeftArm to be
[applied](/docs/reference/engine/classes/Humanoid.md) to a [Humanoid](/docs/reference/engine/classes/Humanoid.md).

See also:

- [HumanoidDescription System](/docs/en-us/characters/appearance.md#humanoiddescription),
  for more information on [HumanoidDescription](/docs/reference/engine/classes/HumanoidDescription.md).
- [Head](/docs/reference/engine/classes/HumanoidDescription.md),
  [Torso](/docs/reference/engine/classes/HumanoidDescription.md),
  [RightArm](/docs/reference/engine/classes/HumanoidDescription.md),
  [RightLeg](/docs/reference/engine/classes/HumanoidDescription.md) and
  [LeftLeg](/docs/reference/engine/classes/HumanoidDescription.md), which are similar
  properties that also control body part
- [LeftArmColor](/docs/reference/engine/classes/HumanoidDescription.md), which controls
  the color of this limb

### Property: HumanoidDescription.LeftArmColor

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
    "can_save": false
  },
  "thread_safety": "ReadSafe",
  "category": "Body Colors",
  "capabilities": [
    "AvatarAppearance"
  ]
}
```

**LeftArmColor** determines the [BodyColors.LeftArmColor3](/docs/reference/engine/classes/BodyColors.md) and
[BodyColors.LeftArmColor](/docs/reference/engine/classes/BodyColors.md) of a [Humanoid](/docs/reference/engine/classes/Humanoid.md) when the description
is [applied](/docs/reference/engine/classes/Humanoid.md). For R15 and Rthro
rigs, this property controls both the upper, lower, and hand parts of the
left arm.

See also:

- [HumanoidDescription System](/docs/en-us/characters/appearance.md#humanoiddescription),
  for more information on [HumanoidDescription](/docs/reference/engine/classes/HumanoidDescription.md).
- [HeadColor](/docs/reference/engine/classes/HumanoidDescription.md),
  [TorsoColor](/docs/reference/engine/classes/HumanoidDescription.md),
  [RightArmColor](/docs/reference/engine/classes/HumanoidDescription.md),
  [LeftLegColor](/docs/reference/engine/classes/HumanoidDescription.md), and
  [RightLegColor](/docs/reference/engine/classes/HumanoidDescription.md), which are
  similar properties that also control body colors
- [LeftArm](/docs/reference/engine/classes/HumanoidDescription.md), which controls the mesh
  used for this limb
- [Shirt](/docs/reference/engine/classes/HumanoidDescription.md), which can apply a texture to
  this limb

### Property: HumanoidDescription.LeftLeg

```json
{
  "type": "int64",
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
  "category": "Body Parts",
  "capabilities": [
    "AvatarAppearance"
  ]
}
```

**LeftLeg** determines the asset ID of the LeftLeg to be
[applied](/docs/reference/engine/classes/Humanoid.md) to a [Humanoid](/docs/reference/engine/classes/Humanoid.md).

See also:

- [HumanoidDescription System](/docs/en-us/characters/appearance.md#humanoiddescription),
  for more information on [HumanoidDescription](/docs/reference/engine/classes/HumanoidDescription.md).
- [Head](/docs/reference/engine/classes/HumanoidDescription.md),
  [Torso](/docs/reference/engine/classes/HumanoidDescription.md),
  [RightArm](/docs/reference/engine/classes/HumanoidDescription.md),
  [LeftArm](/docs/reference/engine/classes/HumanoidDescription.md), and
  [RightLeg](/docs/reference/engine/classes/HumanoidDescription.md), which are similar
  properties that also control body part
- [LeftLegColor](/docs/reference/engine/classes/HumanoidDescription.md), which controls
  the color of this limb

### Property: HumanoidDescription.LeftLegColor

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
    "can_save": false
  },
  "thread_safety": "ReadSafe",
  "category": "Body Colors",
  "capabilities": [
    "AvatarAppearance"
  ]
}
```

**LeftLegColor** determines the [BodyColors.LeftLegColor3](/docs/reference/engine/classes/BodyColors.md) and
[BodyColors.LeftLegColor](/docs/reference/engine/classes/BodyColors.md) of a [Humanoid](/docs/reference/engine/classes/Humanoid.md) when the description
is [applied](/docs/reference/engine/classes/Humanoid.md). For R15 and Rthro
rigs, this property controls both the upper, lower, and foot parts of the
left leg.

See also:

- [HumanoidDescription System](/docs/en-us/characters/appearance.md#humanoiddescription),
  for more information on [HumanoidDescription](/docs/reference/engine/classes/HumanoidDescription.md).
- [HeadColor](/docs/reference/engine/classes/HumanoidDescription.md),
  [TorsoColor](/docs/reference/engine/classes/HumanoidDescription.md),
  [LeftArmColor](/docs/reference/engine/classes/HumanoidDescription.md),
  [RightArmColor](/docs/reference/engine/classes/HumanoidDescription.md), and
  [RightLegColor](/docs/reference/engine/classes/HumanoidDescription.md), which are
  similar properties that also control body colors
- [LeftLeg](/docs/reference/engine/classes/HumanoidDescription.md), which controls the mesh
  used for this limb
- [Pants](/docs/reference/engine/classes/HumanoidDescription.md), which can apply a texture to
  this limb

### Property: HumanoidDescription.MoodAnimation

```json
{
  "type": "int64",
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
  "category": "Animation",
  "capabilities": [
    "AvatarAppearance"
  ]
}
```

When this description is [applied](/docs/reference/engine/classes/Humanoid.md)
to a [Humanoid](/docs/reference/engine/classes/Humanoid.md), this property sets the asset ID of the mood
animation to apply. The asset ID must be for a Mood animation asset.
Defaults to `0`, in which case the character's face uses its neutral rest
pose.

A mood animation applies a static facial pose to a character with a
Dynamic Head, giving the face a characteristic expression (such as a
smile) that persists while the head is otherwise idle.

See also:

- [HumanoidDescription System](/docs/en-us/characters/appearance.md#humanoiddescription),
  for more information on [HumanoidDescription](/docs/reference/engine/classes/HumanoidDescription.md).
- [StaticFacialAnimation](/docs/reference/engine/classes/HumanoidDescription.md),
  which disables animated facial movement so that a Dynamic Head displays
  a static mood pose instead

### Property: HumanoidDescription.NeckAccessory

```json
{
  "type": "string",
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
  "category": "Accessories",
  "capabilities": [
    "AvatarAppearance"
  ]
}
```

**NeckAccessory** is a comma-separated list of asset IDs that determine
what accessories should be added when the description is
[applied](/docs/reference/engine/classes/Humanoid.md), usually those attached
to its neck (such as scarves or necklaces). The list does not contain
duplicates.

Any accessory can used in this property, even if it is meant to go in a
different accessory spot. For example, an accessory meant to go on your
back (such as a cape) could be included in
[HairAccessory](/docs/reference/engine/classes/HumanoidDescription.md). An error is
thrown if you try to apply a new description which shares any assets with
the existing description but a different accessory property.

See also:

- [HumanoidDescription System](/docs/en-us/characters/appearance.md#humanoiddescription),
  for more information on [HumanoidDescription](/docs/reference/engine/classes/HumanoidDescription.md).
- [BackAccessory](/docs/reference/engine/classes/HumanoidDescription.md),
  [FaceAccessory](/docs/reference/engine/classes/HumanoidDescription.md),
  [FrontAccessory](/docs/reference/engine/classes/HumanoidDescription.md),
  [HairAccessory](/docs/reference/engine/classes/HumanoidDescription.md),
  [HatAccessory](/docs/reference/engine/classes/HumanoidDescription.md),
  [ShouldersAccessory](/docs/reference/engine/classes/HumanoidDescription.md) and
  [WaistAccessory](/docs/reference/engine/classes/HumanoidDescription.md), which are
  similar properties that apply accessories like this one

### Property: HumanoidDescription.Pants

```json
{
  "type": "int64",
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
  "category": "Clothes",
  "capabilities": [
    "AvatarAppearance"
  ]
}
```

**Pants** determines the [PantsTemplate](/docs/reference/engine/classes/Pants.md) used by
a [Pants](/docs/reference/engine/classes/Pants.md) instance when [Humanoid:ApplyDescriptionAsync()](/docs/reference/engine/classes/Humanoid.md) is
called on a [Humanoid](/docs/reference/engine/classes/Humanoid.md). The asset type must be for **Pants**, not a
**Decal** or **Image**.

#### See Also

- [HumanoidDescription System](/docs/en-us/characters/appearance.md#humanoiddescription),
  for more information on [HumanoidDescription](/docs/reference/engine/classes/HumanoidDescription.md).
- [Shirt](/docs/reference/engine/classes/HumanoidDescription.md), a similar property which
  applies to a [Shirt](/docs/reference/engine/classes/Shirt.md) object
- [TorsoColor](/docs/reference/engine/classes/HumanoidDescription.md),
  [LeftLegColor](/docs/reference/engine/classes/HumanoidDescription.md) and
  [RightLegColor](/docs/reference/engine/classes/HumanoidDescription.md), which can
  change the color of the body parts underneath the pants texture

### Property: HumanoidDescription.ProportionScale

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
  "category": "Scale",
  "capabilities": [
    "AvatarAppearance"
  ]
}
```

**ProportionScale** determines how wide (0) or narrow (1) a
[Humanoid](/docs/reference/engine/classes/Humanoid.md) rig is. Values outside the range of 0 to 1 are clamped.
When the description is applied through
[Humanoid:ApplyDescriptionAsync()](/docs/reference/engine/classes/Humanoid.md), this value maps to a
**BodyProportionScale** [NumberValue](/docs/reference/engine/classes/NumberValue.md) within the [Humanoid](/docs/reference/engine/classes/Humanoid.md).

Note that when the value of
[BodyTypeScale](/docs/reference/engine/classes/HumanoidDescription.md) is 0, this
property has no effect.

#### See Also

- [HumanoidDescription System](/docs/en-us/characters/appearance.md#humanoiddescription),
  for more information on [HumanoidDescription](/docs/reference/engine/classes/HumanoidDescription.md).
- [BodyTypeScale](/docs/reference/engine/classes/HumanoidDescription.md), which also
  affects rig proportions
- [WidthScale](/docs/reference/engine/classes/HumanoidDescription.md),
  [HeightScale](/docs/reference/engine/classes/HumanoidDescription.md) and
  [DepthScale](/docs/reference/engine/classes/HumanoidDescription.md), which provide finer
  control over the dimensions of a rig
- [HeadScale](/docs/reference/engine/classes/HumanoidDescription.md), which provides specific
  control over the scale of the rig's head

### Property: HumanoidDescription.RightArm

```json
{
  "type": "int64",
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
  "category": "Body Parts",
  "capabilities": [
    "AvatarAppearance"
  ]
}
```

**RightArm** determines the asset ID of the RightArm to be
[applied](/docs/reference/engine/classes/Humanoid.md) to a [Humanoid](/docs/reference/engine/classes/Humanoid.md).

See also:

- [HumanoidDescription System](/docs/en-us/characters/appearance.md#humanoiddescription),
  for more information on [HumanoidDescription](/docs/reference/engine/classes/HumanoidDescription.md).
- [Head](/docs/reference/engine/classes/HumanoidDescription.md),
  [Torso](/docs/reference/engine/classes/HumanoidDescription.md),
  [LeftArm](/docs/reference/engine/classes/HumanoidDescription.md),
  [RightLeg](/docs/reference/engine/classes/HumanoidDescription.md) and
  [LeftLeg](/docs/reference/engine/classes/HumanoidDescription.md), which are similar
  properties that also control body part
- [RightArmColor](/docs/reference/engine/classes/HumanoidDescription.md), which controls
  the color of this limb

### Property: HumanoidDescription.RightArmColor

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
    "can_save": false
  },
  "thread_safety": "ReadSafe",
  "category": "Body Colors",
  "capabilities": [
    "AvatarAppearance"
  ]
}
```

**RightArmColor** determines the [BodyColors.RightArmColor3](/docs/reference/engine/classes/BodyColors.md) and
[BodyColors.RightArmColor](/docs/reference/engine/classes/BodyColors.md) of a [Humanoid](/docs/reference/engine/classes/Humanoid.md) when the
description is [applied](/docs/reference/engine/classes/Humanoid.md). For R15
and Rthro rigs, this property controls both the upper, lower, and hand
parts of the right arm.

See also:

- [HumanoidDescription System](/docs/en-us/characters/appearance.md#humanoiddescription),
  for more information on [HumanoidDescription](/docs/reference/engine/classes/HumanoidDescription.md).
- [HeadColor](/docs/reference/engine/classes/HumanoidDescription.md),
  [TorsoColor](/docs/reference/engine/classes/HumanoidDescription.md),
  [LeftArmColor](/docs/reference/engine/classes/HumanoidDescription.md),
  [LeftLegColor](/docs/reference/engine/classes/HumanoidDescription.md), and
  [RightLegColor](/docs/reference/engine/classes/HumanoidDescription.md), which are
  similar properties that also control body colors
- [RightArm](/docs/reference/engine/classes/HumanoidDescription.md), which controls the mesh
  used for this limb
- [Shirt](/docs/reference/engine/classes/HumanoidDescription.md), which can apply a texture to
  this limb

### Property: HumanoidDescription.RightLeg

```json
{
  "type": "int64",
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
  "category": "Body Parts",
  "capabilities": [
    "AvatarAppearance"
  ]
}
```

**RightLeg** determines the asset ID of the RightLeg to be
[applied](/docs/reference/engine/classes/Humanoid.md) to a [Humanoid](/docs/reference/engine/classes/Humanoid.md).

See also:

- [HumanoidDescription System](/docs/en-us/characters/appearance.md#humanoiddescription),
  for more information on [HumanoidDescription](/docs/reference/engine/classes/HumanoidDescription.md).
- [Head](/docs/reference/engine/classes/HumanoidDescription.md),
  [Torso](/docs/reference/engine/classes/HumanoidDescription.md),
  [RightArm](/docs/reference/engine/classes/HumanoidDescription.md),
  [LeftArm](/docs/reference/engine/classes/HumanoidDescription.md) and
  [LeftLeg](/docs/reference/engine/classes/HumanoidDescription.md), which are similar
  properties that also control body part
- [RightLegColor](/docs/reference/engine/classes/HumanoidDescription.md), which controls
  the color of this limb

### Property: HumanoidDescription.RightLegColor

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
    "can_save": false
  },
  "thread_safety": "ReadSafe",
  "category": "Body Colors",
  "capabilities": [
    "AvatarAppearance"
  ]
}
```

**RightLegColor** determines the [BodyColors.RightLegColor3](/docs/reference/engine/classes/BodyColors.md) and
[BodyColors.RightLegColor](/docs/reference/engine/classes/BodyColors.md) of a [Humanoid](/docs/reference/engine/classes/Humanoid.md) when the
description is [applied](/docs/reference/engine/classes/Humanoid.md). For R15
and Rthro rigs, this property controls both the upper, lower, and foot
parts of the right leg.

See also:

- [HumanoidDescription System](/docs/en-us/characters/appearance.md#humanoiddescription),
  for more information on [HumanoidDescription](/docs/reference/engine/classes/HumanoidDescription.md).
- [HeadColor](/docs/reference/engine/classes/HumanoidDescription.md),
  [TorsoColor](/docs/reference/engine/classes/HumanoidDescription.md),
  [LeftArmColor](/docs/reference/engine/classes/HumanoidDescription.md),
  [RightArmColor](/docs/reference/engine/classes/HumanoidDescription.md), and
  [LeftLegColor](/docs/reference/engine/classes/HumanoidDescription.md), which are similar
  properties that also control body colors
- [RightLeg](/docs/reference/engine/classes/HumanoidDescription.md), which controls the mesh
  used for this limb
- [Pants](/docs/reference/engine/classes/HumanoidDescription.md), which can apply a texture to
  this limb

### Property: HumanoidDescription.RunAnimation

```json
{
  "type": "int64",
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
  "category": "Animation",
  "capabilities": [
    "AvatarAppearance"
  ]
}
```

When this description is [applied](/docs/reference/engine/classes/Humanoid.md)
to a [Humanoid](/docs/reference/engine/classes/Humanoid.md), **RunAnimation** determines the
[Animation.AnimationId](/docs/reference/engine/classes/Animation.md) to play when its
[state](/docs/reference/engine/classes/Humanoid.md) is [Running](/docs/reference/engine/enums/HumanoidStateType.md) at a
moderate speed.

See also:

- [HumanoidDescription System](/docs/en-us/characters/appearance.md#humanoiddescription),
  for more information on [HumanoidDescription](/docs/reference/engine/classes/HumanoidDescription.md).
- [ClimbAnimation](/docs/reference/engine/classes/HumanoidDescription.md),
  [FallAnimation](/docs/reference/engine/classes/HumanoidDescription.md),
  [IdleAnimation](/docs/reference/engine/classes/HumanoidDescription.md),
  [JumpAnimation](/docs/reference/engine/classes/HumanoidDescription.md),
  [SwimAnimation](/docs/reference/engine/classes/HumanoidDescription.md) and
  [WalkAnimation](/docs/reference/engine/classes/HumanoidDescription.md), which are
  similar properties that determine animations to play on the rig

### Property: HumanoidDescription.Shirt

```json
{
  "type": "int64",
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
  "category": "Clothes",
  "capabilities": [
    "AvatarAppearance"
  ]
}
```

**Shirt** determines the [ShirtTemplate](/docs/reference/engine/classes/Shirt.md) used by
a [Shirt](/docs/reference/engine/classes/Shirt.md) instance when [Humanoid:ApplyDescriptionAsync()](/docs/reference/engine/classes/Humanoid.md) is
called on a [Humanoid](/docs/reference/engine/classes/Humanoid.md). The asset type must be for **Shirt**, not a
**Decal** or **Image**.

#### See Also

- [HumanoidDescription System](/docs/en-us/characters/appearance.md#humanoiddescription),
  for more information on [HumanoidDescription](/docs/reference/engine/classes/HumanoidDescription.md).
- [Pants](/docs/reference/engine/classes/HumanoidDescription.md), a similar property which
  applies to a [Pants](/docs/reference/engine/classes/Pants.md) object
- [GraphicTShirt](/docs/reference/engine/classes/HumanoidDescription.md), a similar
  property which applies to a [ShirtGraphic](/docs/reference/engine/classes/ShirtGraphic.md) object
- [TorsoColor](/docs/reference/engine/classes/HumanoidDescription.md),
  [LeftArmColor](/docs/reference/engine/classes/HumanoidDescription.md) and
  [RightArmColor](/docs/reference/engine/classes/HumanoidDescription.md), which can
  change the color of the body parts underneath the shirt texture

### Property: HumanoidDescription.ShouldersAccessory

```json
{
  "type": "string",
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
  "category": "Accessories",
  "capabilities": [
    "AvatarAppearance"
  ]
}
```

**ShouldersAccessory** is a comma-separated list of asset IDs that
determine what accessories should be added when the description is
[applied](/docs/reference/engine/classes/Humanoid.md), usually those attached
to its shoulders (such as shoulder-mounted critters). The list does not
contain duplicates.

An error is thrown if you try to apply a new description which shares any
assets with the existing description but a different accessory property.

See also:

- [HumanoidDescription System](/docs/en-us/characters/appearance.md#humanoiddescription),
  for more information on [HumanoidDescription](/docs/reference/engine/classes/HumanoidDescription.md).
- [BackAccessory](/docs/reference/engine/classes/HumanoidDescription.md),
  [FaceAccessory](/docs/reference/engine/classes/HumanoidDescription.md),
  [FrontAccessory](/docs/reference/engine/classes/HumanoidDescription.md),
  [HairAccessory](/docs/reference/engine/classes/HumanoidDescription.md),
  [HatAccessory](/docs/reference/engine/classes/HumanoidDescription.md),
  [NeckAccessory](/docs/reference/engine/classes/HumanoidDescription.md) and
  [WaistAccessory](/docs/reference/engine/classes/HumanoidDescription.md), which are
  similar properties that apply accessories like this one

### Property: HumanoidDescription.StaticFacialAnimation

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
  "category": "Animation",
  "capabilities": [
    "AvatarAppearance"
  ]
}
```

**StaticFacialAnimation** controls whether facial animations play when
this description is applied to a [Humanoid](/docs/reference/engine/classes/Humanoid.md) with a Dynamic Head.
When set to `true`, the head displays a static mood pose without any
animated facial movement, achieving visual parity with classic face
decals.

Even with `StaticFacialAnimation` set to `true`,
[MoodAnimation](/docs/reference/engine/classes/HumanoidDescription.md) still applies a
static pose to give the face its characteristic expression. Setting
`StaticFacialAnimation` to `true` is different from setting
`MoodAnimation` to `0`, which would result in the Dynamic Head's neutral
rest pose.

This is a per-description setting and does not affect other descriptions
or the user's avatar globally.

See also:

- [HumanoidDescription System](/docs/en-us/characters/appearance.md#humanoiddescription),
  for more information on [HumanoidDescription](/docs/reference/engine/classes/HumanoidDescription.md).

### Property: HumanoidDescription.SwimAnimation

```json
{
  "type": "int64",
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
  "category": "Animation",
  "capabilities": [
    "AvatarAppearance"
  ]
}
```

When this description is [applied](/docs/reference/engine/classes/Humanoid.md)
to a [Humanoid](/docs/reference/engine/classes/Humanoid.md), **SwimAnimation** determines the
[Animation.AnimationId](/docs/reference/engine/classes/Animation.md) to play when its
[state](/docs/reference/engine/classes/Humanoid.md) is [Swimming](/docs/reference/engine/enums/HumanoidStateType.md)

See also:

- [HumanoidDescription System](/docs/en-us/characters/appearance.md#humanoiddescription),
  for more information on [HumanoidDescription](/docs/reference/engine/classes/HumanoidDescription.md).
- [ClimbAnimation](/docs/reference/engine/classes/HumanoidDescription.md),
  [FallAnimation](/docs/reference/engine/classes/HumanoidDescription.md),
  [IdleAnimation](/docs/reference/engine/classes/HumanoidDescription.md),
  [JumpAnimation](/docs/reference/engine/classes/HumanoidDescription.md),
  [RunAnimation](/docs/reference/engine/classes/HumanoidDescription.md) and
  [WalkAnimation](/docs/reference/engine/classes/HumanoidDescription.md), which are
  similar properties that determine animations to play on the rig

### Property: HumanoidDescription.Torso

```json
{
  "type": "int64",
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
  "category": "Body Parts",
  "capabilities": [
    "AvatarAppearance"
  ]
}
```

**Torso** determines the asset ID of the Torso to be
[applied](/docs/reference/engine/classes/Humanoid.md) to a [Humanoid](/docs/reference/engine/classes/Humanoid.md).

See also:

- [HumanoidDescription System](/docs/en-us/characters/appearance.md#humanoiddescription),
  for more information on [HumanoidDescription](/docs/reference/engine/classes/HumanoidDescription.md).
- [Head](/docs/reference/engine/classes/HumanoidDescription.md),
  [RightArm](/docs/reference/engine/classes/HumanoidDescription.md),
  [LeftArm](/docs/reference/engine/classes/HumanoidDescription.md),
  [RightLeg](/docs/reference/engine/classes/HumanoidDescription.md) and
  [LeftLeg](/docs/reference/engine/classes/HumanoidDescription.md), which are similar
  properties that also control body part
- [TorsoColor](/docs/reference/engine/classes/HumanoidDescription.md), which controls the
  color of this limb

### Property: HumanoidDescription.TorsoColor

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
    "can_save": false
  },
  "thread_safety": "ReadSafe",
  "category": "Body Colors",
  "capabilities": [
    "AvatarAppearance"
  ]
}
```

**TorsoColor** determines the [BodyColors.TorsoColor3](/docs/reference/engine/classes/BodyColors.md) and
[BodyColors.TorsoColor](/docs/reference/engine/classes/BodyColors.md) of a [Humanoid](/docs/reference/engine/classes/Humanoid.md) when the description
is [applied](/docs/reference/engine/classes/Humanoid.md). For R15 and Rthro
rigs, this property controls both the upper and lower parts of the torso.

See also:

- [HumanoidDescription System](/docs/en-us/characters/appearance.md#humanoiddescription),
  for more information on [HumanoidDescription](/docs/reference/engine/classes/HumanoidDescription.md).
- [HeadColor](/docs/reference/engine/classes/HumanoidDescription.md),
  [TorsoColor](/docs/reference/engine/classes/HumanoidDescription.md),
  [LeftArmColor](/docs/reference/engine/classes/HumanoidDescription.md),
  [RightArmColor](/docs/reference/engine/classes/HumanoidDescription.md),
  [LeftLegColor](/docs/reference/engine/classes/HumanoidDescription.md), and
  [RightLegColor](/docs/reference/engine/classes/HumanoidDescription.md), which are
  similar properties that also control body colors
- [Torso](/docs/reference/engine/classes/HumanoidDescription.md), which controls the mesh used
  for this body part
- [GraphicTShirt](/docs/reference/engine/classes/HumanoidDescription.md) and
  [Shirt](/docs/reference/engine/classes/HumanoidDescription.md), which can apply a texture to
  this body part

### Property: HumanoidDescription.UseAvatarSettings

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
  "category": "Data",
  "capabilities": [
    "AvatarAppearance"
  ]
}
```

When true, `Humanoid:ApplyDescriptionAsync` or
`Players:CreateHumanoidModelFromDescriptionAsync` will also apply the
Avatar Settings set for the universe to the model.

### Property: HumanoidDescription.WaistAccessory

```json
{
  "type": "string",
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
  "category": "Accessories",
  "capabilities": [
    "AvatarAppearance"
  ]
}
```

**WaistAccessory** is a comma-separated list of asset IDs that determine
what accessories should be added when the description is
[applied](/docs/reference/engine/classes/Humanoid.md), usually those attached
to its waist (such as belts). The list does not contain duplicates.

An error is thrown if you try to apply a new description which shares any
assets with the existing description but a different accessory property.

See also:

- [HumanoidDescription System](/docs/en-us/characters/appearance.md#humanoiddescription),
  for more information on [HumanoidDescription](/docs/reference/engine/classes/HumanoidDescription.md).
- [BackAccessory](/docs/reference/engine/classes/HumanoidDescription.md),
  [FaceAccessory](/docs/reference/engine/classes/HumanoidDescription.md),
  [FrontAccessory](/docs/reference/engine/classes/HumanoidDescription.md),
  [HairAccessory](/docs/reference/engine/classes/HumanoidDescription.md),
  [HatAccessory](/docs/reference/engine/classes/HumanoidDescription.md),
  [NeckAccessory](/docs/reference/engine/classes/HumanoidDescription.md) and
  [ShouldersAccessory](/docs/reference/engine/classes/HumanoidDescription.md), which
  are similar properties that apply accessories like this one

### Property: HumanoidDescription.WalkAnimation

```json
{
  "type": "int64",
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
  "category": "Animation",
  "capabilities": [
    "AvatarAppearance"
  ]
}
```

When this description is [applied](/docs/reference/engine/classes/Humanoid.md)
to a [Humanoid](/docs/reference/engine/classes/Humanoid.md), **WalkAnimation** determines the
[Animation.AnimationId](/docs/reference/engine/classes/Animation.md) to play when its
[state](/docs/reference/engine/classes/Humanoid.md) is [Running](/docs/reference/engine/enums/HumanoidStateType.md) at a
low speed

See also:

- [HumanoidDescription System](/docs/en-us/characters/appearance.md#humanoiddescription),
  for more information on [HumanoidDescription](/docs/reference/engine/classes/HumanoidDescription.md).
- [ClimbAnimation](/docs/reference/engine/classes/HumanoidDescription.md),
  [FallAnimation](/docs/reference/engine/classes/HumanoidDescription.md),
  [IdleAnimation](/docs/reference/engine/classes/HumanoidDescription.md),
  [JumpAnimation](/docs/reference/engine/classes/HumanoidDescription.md),
  [RunAnimation](/docs/reference/engine/classes/HumanoidDescription.md) and
  [SwimAnimation](/docs/reference/engine/classes/HumanoidDescription.md), which are
  similar properties that determine animations to play on the rig

### Property: HumanoidDescription.WidthScale

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
  "category": "Scale",
  "capabilities": [
    "AvatarAppearance"
  ]
}
```

**WidthScale** determines by what factor the width (left-to-right
distance) of a [Humanoid](/docs/reference/engine/classes/Humanoid.md) is scaled, as well as all accessories not
attached to its head. When the description is applied through
[Humanoid:ApplyDescriptionAsync()](/docs/reference/engine/classes/Humanoid.md), this value maps to a
**BodyWidthScale** [NumberValue](/docs/reference/engine/classes/NumberValue.md) within the [Humanoid](/docs/reference/engine/classes/Humanoid.md).

#### See Also

- [HumanoidDescription System](/docs/en-us/characters/appearance.md#humanoiddescription),
  for more information on [HumanoidDescription](/docs/reference/engine/classes/HumanoidDescription.md).
- [BodyTypeScale](/docs/reference/engine/classes/HumanoidDescription.md) and
  [ProportionScale](/docs/reference/engine/classes/HumanoidDescription.md), which can
  provide more realistic rig proportions
- [HeightScale](/docs/reference/engine/classes/HumanoidDescription.md) and
  [DepthScale](/docs/reference/engine/classes/HumanoidDescription.md)

## Methods

### Method: HumanoidDescription:AddEmote

**Signature:** `HumanoidDescription:AddEmote(name: string, assetId: int64): ()`

**AddEmote** will add an Emote asset to the description given a name and
its asset ID. The asset ID must be for an "Emote" asset (see
[Featured emotes](https://www.roblox.com/catalog?Category=0&Subcategory=39)
in the Catalog).

You can add multiple emotes of the same name. All emotes of the same name
can be removed using
[RemoveEmote](/docs/reference/engine/classes/HumanoidDescription.md). If an emote with
the same ID is added under the same name,
[EmotesChanged](/docs/reference/engine/classes/HumanoidDescription.md) fires.

See also:

- [HumanoidDescription System](/docs/en-us/characters/appearance.md#humanoiddescription),
  for more information on [HumanoidDescription](/docs/reference/engine/classes/HumanoidDescription.md).
- [GetEmotes](/docs/reference/engine/classes/HumanoidDescription.md), which can be used to
  retrieve the emotes that have been added by this function
- [SetEmotes](/docs/reference/engine/classes/HumanoidDescription.md) and
  [RemoveEmote](/docs/reference/engine/classes/HumanoidDescription.md), which also
  manipulate what emotes have been added
- [EmotesChanged](/docs/reference/engine/classes/HumanoidDescription.md), which fires
  after this function is called

*Security: None · Thread Safety: Unsafe · Capabilities: AvatarAppearance*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `name` | `string` |  | A string that identifies what emote is being added. Example: `"Salute"`. |
| `assetId` | `int64` |  | An emote asset ID. |

**Returns:** `()`

### Method: HumanoidDescription:GetAccessories

**Signature:** `HumanoidDescription:GetAccessories(includeRigidAccessories: boolean): List<AccessoriesInfo>`

Returns a table of an avatar's current accessories. If the second
parameter (includeRigidAccessories) is true then the returned table will
also include entries for rigid accessories from the rigid accessory
properties.

*Security: None · Thread Safety: Unsafe · Capabilities: AvatarAppearance*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `includeRigidAccessories` | `boolean` |  | Set to true if rigid accessories from the rigid accessory properties should also be included in the return array. False means only include layered clothing accessories from the AccessoryBlob. |

**Returns:** `List<AccessoriesInfo>` — Returns an array where each entry specifies for an individual
accessory the AccessoryType, AssetId, IsLayered, Order and Puffiness.

**Get Accessories**

This code sample prints out all the asset IDs and types of the accessories in
the HumanoidDescription.

```lua
local includeRigidAccessories = true
local accessoriesTable =
	game:GetService("Players"):GetHumanoidDescriptionFromUserIdAsync(1):GetAccessories(includeRigidAccessories)
for _, accessoryInfo in ipairs(accessoriesTable) do
	print(tostring(accessoryInfo.AssetId) .. " " .. tostring(accessoryInfo.AccessoryType))
end
```

**Expected output:** When run, all the asset IDs and types are printed out for the accessories in the HumanoidDescription.

### Method: HumanoidDescription:GetEmotes

**Signature:** `HumanoidDescription:GetEmotes(): Dictionary`

**GetEmotes** returns a dictionary of emotes that have been
[added](/docs/reference/engine/classes/HumanoidDescription.md) or
[set](/docs/reference/engine/classes/HumanoidDescription.md) to this description. The keys
of this dictionary are the names of the emotes, and the values are a
non-empty array of emote IDs for that name.

#### Example

```lua
local hd = Instance.new("HumanoidDescription")
hd:AddEmote("Salute", 3360689775)
local emotes = hd:GetEmotes()
for name, ids in emotes do
    print(("The emote %s has %d ids:"):format(name, #ids))
    for _, id in ids do
        print(id)
    end
end
```

See also:

- [HumanoidDescription System](/docs/en-us/characters/appearance.md#humanoiddescription),
  for more information on [HumanoidDescription](/docs/reference/engine/classes/HumanoidDescription.md).
- [SetEmotes](/docs/reference/engine/classes/HumanoidDescription.md) and
  [AddEmote](/docs/reference/engine/classes/HumanoidDescription.md), which can add emotes
  that may be returned by this function
- [EmotesChanged](/docs/reference/engine/classes/HumanoidDescription.md), which fires
  with the value returned this function after it may have changed

*Security: None · Thread Safety: Unsafe · Capabilities: AvatarAppearance*

**Returns:** `Dictionary` — A dictionary of emotes where the key is the emote name and the value
is an array of emote asset IDs. Example:

```lua
{
    Salute = {3360689775},
    Agree = {4849487550},
    Disagree = {4849495710}
}
```

.

### Method: HumanoidDescription:GetEquippedEmotes

**Signature:** `HumanoidDescription:GetEquippedEmotes(): Array`

**GetEquippedEmotes** returns an array of tables which indicate the `Name`
and `Slot` of each equipped emote as it was set by
[SetEquippedEmotes](/docs/reference/engine/classes/HumanoidDescription.md).

#### Example

```lua
local hd = Instance.new("HumanoidDescription")
hd:SetEmotes({Salute = {3360689775}, Agree = {4849487550}})
hd:SetEquippedEmotes({"Salute", "Agree"})
-- Iterate over the equipped emotes:
for _, t in hd:GetEquippedEmotes() do
    print(("In slot %d: emote %s is equipped"):format(t.Slot, t.Name))
end
```

See also:

- [HumanoidDescription System](/docs/en-us/characters/appearance.md#humanoiddescription),
  for more information on [HumanoidDescription](/docs/reference/engine/classes/HumanoidDescription.md).
- [SetEquippedEmotes](/docs/reference/engine/classes/HumanoidDescription.md), which
  sets the currently equipped emotes and changes what this function
  returns
- [EquippedEmotesChanged](/docs/reference/engine/classes/HumanoidDescription.md),
  which fires when the function returned by this value may have changed

*Security: None · Thread Safety: Unsafe · Capabilities: AvatarAppearance*

**Returns:** `Array` — An array of tables describing the name and slot which each emote is
equipped. Example:

```lua
{
    {Slot = 3, Name = "Salute"},
    {Slot = 2, Name = "Agree"},
    {Slot = 1, Name = "Disagree"},
}
```

.

### Method: HumanoidDescription:RemoveEmote

**Signature:** `HumanoidDescription:RemoveEmote(name: string): ()`

**RemoveEmote** removes all emotes from the description that have been
[added](/docs/reference/engine/classes/HumanoidDescription.md) or
[set](/docs/reference/engine/classes/HumanoidDescription.md) under the given name. If there
are no added emotes with the given name, no error is thrown and
[EmotesChanged](/docs/reference/engine/classes/HumanoidDescription.md) **does not** fire.

See also:

- [HumanoidDescription System](/docs/en-us/characters/appearance.md#humanoiddescription),
  for more information on [HumanoidDescription](/docs/reference/engine/classes/HumanoidDescription.md).
- [SetEmotes](/docs/reference/engine/classes/HumanoidDescription.md) and
  [AddEmote](/docs/reference/engine/classes/HumanoidDescription.md), which can add emotes
  that may be removed
- [GetEmotes](/docs/reference/engine/classes/HumanoidDescription.md), which can retrieve a
  dictionary of emotes that may be removed

*Security: None · Thread Safety: Unsafe · Capabilities: AvatarAppearance*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `name` | `string` |  | The name of the emote as it was [set](/docs/reference/engine/classes/HumanoidDescription.md) or [added](/docs/reference/engine/classes/HumanoidDescription.md). |

**Returns:** `()`

### Method: HumanoidDescription:SetAccessories

**Signature:** `HumanoidDescription:SetAccessories(accessories: Array, includeRigidAccessories: boolean): ()`

Accepts a table that sets the accessories and related properties for an
avatar. If the second parameter (includeRigidAccessories) is true, then
this function can also be used to set the rigid accessories in the rigid
accessory properties. In this case any table entry that does not have an
Order will be considered a rigid accessory and put in the appropriate
property according to the AccessoryType.

*Security: None · Thread Safety: Unsafe · Capabilities: AvatarAppearance*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `accessories` | `Array` |  | Each entry specifies for an individual accessory the AccessoryType, AssetId, IsLayered, Order and Puffiness. |
| `includeRigidAccessories` | `boolean` |  | Set to true if rigid accessories are also included in the passed in array (they would have to not specify Order). |

**Returns:** `()`

**Set Accessories**

This code sample adds two accessories to a HumanoidDescription.

```lua
local humanoidDescription = Instance.new("HumanoidDescription")
local originalSpecifications = {
	{
		Order = 1,
		AssetId = 123456789,
		Puffiness = 0.5,
		AccessoryType = Enum.AccessoryType.Sweater,
	},
}
humanoidDescription:SetAccessories(originalSpecifications, true)

local updatedSpecifications = humanoidDescription:GetAccessories(false)
local newIndividualSpecification = {
	Order = 2,
	AssetId = 987654321,
	Puffiness = 0.7,
	AccessoryType = Enum.AccessoryType.Jacket,
	IsLayered = true,
}
updatedSpecifications[#updatedSpecifications + 1] = newIndividualSpecification
humanoidDescription:SetAccessories(updatedSpecifications, true)
```

**Expected output:** When run, the HumanoidDescription will have two accessories.

### Method: HumanoidDescription:SetEmotes

**Signature:** `HumanoidDescription:SetEmotes(emotes: Dictionary): ()`

**SetEmotes** sets all of the emotes on this description given a table
similar to that returned by
[GetEmotes](/docs/reference/engine/classes/HumanoidDescription.md). It fires
[EmotesChanged](/docs/reference/engine/classes/HumanoidDescription.md)

#### Example

```lua
local emotes = {
    Salute = {3360689775}, -- Syntax note: can also use ["Salute"] = ...
    Agree = {4849487550},
    Disagree = {4849495710}
}
local hd = Instance.new("HumanoidDescription")
hd:SetEmotes(emotes)
```

See also:

- [HumanoidDescription System](/docs/en-us/characters/appearance.md#humanoiddescription),
  for more information on [HumanoidDescription](/docs/reference/engine/classes/HumanoidDescription.md).
- [AddEmote](/docs/reference/engine/classes/HumanoidDescription.md) and
  [RemoveEmote](/docs/reference/engine/classes/HumanoidDescription.md) which can modify
  the added emotes on an individual level
- [EmotesChanged](/docs/reference/engine/classes/HumanoidDescription.md), which fires
  when this function is called

*Security: None · Thread Safety: Unsafe · Capabilities: AvatarAppearance*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `emotes` | `Dictionary` |  | A dictionary of emotes where the key is the emote name and the value is an array of emote asset IDs. Example:  ```lua {     Salute = {3360689775},     Agree = {4849487550},     Disagree = {4849495710} } ```  . |

**Returns:** `()`

### Method: HumanoidDescription:SetEquippedEmotes

**Signature:** `HumanoidDescription:SetEquippedEmotes(equippedEmotes: Array): ()`

**SetEquippedEmotes** sets the currently equipped emotes given an array of
emote names as they were passed to
[AddEmote](/docs/reference/engine/classes/HumanoidDescription.md) or
[SetEmotes](/docs/reference/engine/classes/HumanoidDescription.md). It can also take an
array of tables similar to that returned by
[GetEquippedEmotes](/docs/reference/engine/classes/HumanoidDescription.md). Calling
this function fires
[EquippedEmotesChanged](/docs/reference/engine/classes/HumanoidDescription.md).

#### Example

```lua
local hd = Instance.new("HumanoidDescription")
hd:SetEmotes({Salute = {3360689775}, Agree = {4849487550}})
-- Can provide either an array of strings... (index is slot number)
hd:SetEquippedEmotes({"Salute", "Agree"})
-- ...or an array of tables as returned by GetEquippedEmotes (Slot and Name keys set)
hd:SetEquippedEmotes({{Slot = 1, Name = "Salute"}, {Slot = 2, Name = "Agree"}})
```

See also:

- [HumanoidDescription System](/docs/en-us/characters/appearance.md#humanoiddescription),
  for more information on [HumanoidDescription](/docs/reference/engine/classes/HumanoidDescription.md).
- [GetEquippedEmotes](/docs/reference/engine/classes/HumanoidDescription.md), which
  returns a value describing the equipped emotes set by this function
- [EquippedEmotesChanged](/docs/reference/engine/classes/HumanoidDescription.md),
  which fires when this function is called

*Security: None · Thread Safety: Unsafe · Capabilities: AvatarAppearance*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `equippedEmotes` | `Array` |  | An array of emote names. Example:  ```lua { "Disagree", "Agree", "Salute" } ```  &ndash; OR &ndash; An array of tables describing the name and slot which each emote is equipped. Example:  ```lua {     {Slot = 3, Name = "Salute"},     {Slot = 2, Name = "Agree"},     {Slot = 1, Name = "Disagree"}, } ```  . |

**Returns:** `()`

## Events

### Event: HumanoidDescription.EmotesChanged

**Signature:** `HumanoidDescription.EmotesChanged(newEmotes: Dictionary)`

**EmotesChanged** fires when emotes are
[added](/docs/reference/engine/classes/HumanoidDescription.md),
[removed](/docs/reference/engine/classes/HumanoidDescription.md) or
[set](/docs/reference/engine/classes/HumanoidDescription.md) on the description. The event
fires with the new emote table as returned by
[GetEmotes](/docs/reference/engine/classes/HumanoidDescription.md).

If [AddEmote](/docs/reference/engine/classes/HumanoidDescription.md) is called with the same
name and ID as an existing emote, this event fires.

See also:

- [HumanoidDescription System](/docs/en-us/characters/appearance.md#humanoiddescription),
  for more information on [HumanoidDescription](/docs/reference/engine/classes/HumanoidDescription.md).
- [AddEmote](/docs/reference/engine/classes/HumanoidDescription.md),
  [RemoveEmote](/docs/reference/engine/classes/HumanoidDescription.md) and
  [HumanoidDescription:SetEmotes()](/docs/reference/engine/classes/HumanoidDescription.md), which can cause this event to
  be fired

*Security: None · Capabilities: AvatarAppearance*

**Parameters:**

| Name | Type | Description |
|------|------|-------------|
| `newEmotes` | `Dictionary` | A dictionary of emotes where the key is the emote name and the value is an array of emote asset IDs. Example:  ```lua {     Salute = {3360689775},     Agree = {4849487550},     Disagree = {4849495710} } ```  . |

### Event: HumanoidDescription.EquippedEmotesChanged

**Signature:** `HumanoidDescription.EquippedEmotesChanged(newEquippedEmotes: Array)`

**EquippedEmotesChanged** fires when the equipped emotes are set on this
description using
[SetEquippedEmotes](/docs/reference/engine/classes/HumanoidDescription.md). It
provides the new equipped emotes in a table like that returned by
[GetEquippedEmotes](/docs/reference/engine/classes/HumanoidDescription.md).

#### Example

```lua
local hd = Instance.new("HumanoidDescription")
hd.EquippedEmotesChanged:Connect(function(equippedEmotes)
    print(("We have %d emotes equipped"):format(#equippedEmotes))
    for _, t in equippedEmotes do
        print(("In slot %d: emote %s is equipped"):format(t.Slot, t.Name))
    end
end)
hd:SetEquippedEmotes({"Salute", "Agree"}) --> We have 2 emotes equipped
```

See also:

- [HumanoidDescription System](/docs/en-us/characters/appearance.md#humanoiddescription),
  for more information on [HumanoidDescription](/docs/reference/engine/classes/HumanoidDescription.md).
- [SetEquippedEmotes](/docs/reference/engine/classes/HumanoidDescription.md), which
  fires this event
- [GetEquippedEmotes](/docs/reference/engine/classes/HumanoidDescription.md), which
  can be used to query the currently equipped emotes without this event
  firing

*Security: None · Capabilities: AvatarAppearance*

**Parameters:**

| Name | Type | Description |
|------|------|-------------|
| `newEquippedEmotes` | `Array` | An array of tables describing the name and slot which each emote is equipped. Example:  ```lua {     {Slot = 3, Name = "Salute"},     {Slot = 2, Name = "Agree"},     {Slot = 1, Name = "Disagree"}, } ```  . |

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