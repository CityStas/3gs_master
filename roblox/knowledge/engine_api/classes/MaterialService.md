---
name: MaterialService
last_updated: 2026-10-30T19:55:52Z
inherits:
  - Instance
  - Object
type: class
memory_category: Instances
tags:
  - NotCreatable
  - Service
summary: "The game service responsible for managing materials."
---

# Class: MaterialService

> The game service responsible for managing materials.

## Description

MaterialService is the game service responsible for managing materials. It is
the container for global [MaterialVariant](/docs/reference/engine/classes/MaterialVariant.md) instances.
[MaterialVariant](/docs/reference/engine/classes/MaterialVariant.md) can be child or descendant of MaterialService. For
each base Material type, MaterialService internally keeps a set of
MaterialVariant references. [MaterialVariant.Name](/docs/reference/engine/classes/MaterialVariant.md) is the key to access
it. The [MaterialVariant.Name](/docs/reference/engine/classes/MaterialVariant.md) and [MaterialVariant.BaseMaterial](/docs/reference/engine/classes/MaterialVariant.md)
are combined to work as an identifier. If more than one MaterialVariant object
has the same name and BaseMaterial under MaterialService, only one of them can
be used.

MaterialService has some (Material)Name properties. Assigning a
MaterialVariant Name replaces the built-in material with the specified
MaterialVariant. If the MaterialService can't find a matching MaterialVariant,
it falls back to built-in material. Note BaseMaterial should also match, for
example, a MaterialVariant with BaseMaterial Grass can only be assigned to
MaterialService.GrassName, not AsphaltName or any other names. These
properties are not scriptable but can read and write using
[MaterialService:GetBaseMaterialOverride()](/docs/reference/engine/classes/MaterialService.md) and
[MaterialService:SetBaseMaterialOverride()](/docs/reference/engine/classes/MaterialService.md) function.

MaterialService has a [MaterialService.Use2022Materials](/docs/reference/engine/classes/MaterialService.md) property that
switches between legacy materials and new materials introduced in year 2022.
Because legacy and user-generated (new) terrain materials use different
encoding, using legacy terrain materials and MaterialVariant at the same time
has a performance penalty. If your game is using pre-2022 terrain materials,
avoid overriding any built-in materials. Migrate to 2022 materials if
possible.

## Properties

### Property: MaterialService.AsphaltName

```json
{
  "type": "string",
  "access": "ReadOnly",
  "security": {
    "read": "RobloxEngineSecurity",
    "write": "RobloxEngineSecurity"
  },
  "serialization": {
    "can_load": true,
    "can_save": true
  },
  "thread_safety": "ReadSafe",
  "category": "Material Overrides",
  "capabilities": [
    "Material"
  ]
}
```

Specify [MaterialVariant](/docs/reference/engine/classes/MaterialVariant.md) name to override built-in Asphalt. The
Specified MaterialVariant must have [MaterialVariant.BaseMaterial](/docs/reference/engine/classes/MaterialVariant.md)
set to Asphalt. This property is not scriptable; use
[MaterialService:GetBaseMaterialOverride()](/docs/reference/engine/classes/MaterialService.md) and
[MaterialService:SetBaseMaterialOverride()](/docs/reference/engine/classes/MaterialService.md) to access it from
scripts.

### Property: MaterialService.BasaltName

```json
{
  "type": "string",
  "access": "ReadOnly",
  "security": {
    "read": "RobloxEngineSecurity",
    "write": "RobloxEngineSecurity"
  },
  "serialization": {
    "can_load": true,
    "can_save": true
  },
  "thread_safety": "ReadSafe",
  "category": "Material Overrides",
  "capabilities": [
    "Material"
  ]
}
```

Specify [MaterialVariant](/docs/reference/engine/classes/MaterialVariant.md) name to override built-in Basalt. The
Specified MaterialVariant must have [MaterialVariant.BaseMaterial](/docs/reference/engine/classes/MaterialVariant.md)
set to Basalt. This property is not scriptable; use
[MaterialService:GetBaseMaterialOverride()](/docs/reference/engine/classes/MaterialService.md) and
[MaterialService:SetBaseMaterialOverride()](/docs/reference/engine/classes/MaterialService.md) to access it from
scripts.

### Property: MaterialService.BrickName

```json
{
  "type": "string",
  "access": "ReadOnly",
  "security": {
    "read": "RobloxEngineSecurity",
    "write": "RobloxEngineSecurity"
  },
  "serialization": {
    "can_load": true,
    "can_save": true
  },
  "thread_safety": "ReadSafe",
  "category": "Material Overrides",
  "capabilities": [
    "Material"
  ]
}
```

Specify [MaterialVariant](/docs/reference/engine/classes/MaterialVariant.md) name to override built-in Brick. The
Specified MaterialVariant must have [MaterialVariant.BaseMaterial](/docs/reference/engine/classes/MaterialVariant.md)
set to Brick. This property is not scriptable; use
[MaterialService:GetBaseMaterialOverride()](/docs/reference/engine/classes/MaterialService.md) and
[MaterialService:SetBaseMaterialOverride()](/docs/reference/engine/classes/MaterialService.md) to access it from
scripts.

### Property: MaterialService.CardboardName

```json
{
  "type": "string",
  "access": "ReadOnly",
  "security": {
    "read": "RobloxEngineSecurity",
    "write": "RobloxEngineSecurity"
  },
  "serialization": {
    "can_load": true,
    "can_save": true
  },
  "thread_safety": "ReadSafe",
  "category": "Material Overrides",
  "capabilities": [
    "Material"
  ]
}
```

Specify [MaterialVariant](/docs/reference/engine/classes/MaterialVariant.md) name to override built-in Cardboard. The
Specified MaterialVariant must have [MaterialVariant.BaseMaterial](/docs/reference/engine/classes/MaterialVariant.md)
set to Cardboard. This property is not scriptable; use
[MaterialService:GetBaseMaterialOverride()](/docs/reference/engine/classes/MaterialService.md) and
[MaterialService:SetBaseMaterialOverride()](/docs/reference/engine/classes/MaterialService.md) to access it from
scripts.

### Property: MaterialService.CarpetName

```json
{
  "type": "string",
  "access": "ReadOnly",
  "security": {
    "read": "RobloxEngineSecurity",
    "write": "RobloxEngineSecurity"
  },
  "serialization": {
    "can_load": true,
    "can_save": true
  },
  "thread_safety": "ReadSafe",
  "category": "Material Overrides",
  "capabilities": [
    "Material"
  ]
}
```

Specify [MaterialVariant](/docs/reference/engine/classes/MaterialVariant.md) name to override built-in Carpet. The
Specified MaterialVariant must have [MaterialVariant.BaseMaterial](/docs/reference/engine/classes/MaterialVariant.md)
set to Carpet. This property is not scriptable; use
[MaterialService:GetBaseMaterialOverride()](/docs/reference/engine/classes/MaterialService.md) and
[MaterialService:SetBaseMaterialOverride()](/docs/reference/engine/classes/MaterialService.md) to access it from
scripts.

### Property: MaterialService.CeramicTilesName

```json
{
  "type": "string",
  "access": "ReadOnly",
  "security": {
    "read": "RobloxEngineSecurity",
    "write": "RobloxEngineSecurity"
  },
  "serialization": {
    "can_load": true,
    "can_save": true
  },
  "thread_safety": "ReadSafe",
  "category": "Material Overrides",
  "capabilities": [
    "Material"
  ]
}
```

Specify [MaterialVariant](/docs/reference/engine/classes/MaterialVariant.md) name to override built-in CeramicTiles.
The Specified MaterialVariant must have
[MaterialVariant.BaseMaterial](/docs/reference/engine/classes/MaterialVariant.md) set to CeramicTiles. This property is
not scriptable; use [MaterialService:GetBaseMaterialOverride()](/docs/reference/engine/classes/MaterialService.md) and
[MaterialService:SetBaseMaterialOverride()](/docs/reference/engine/classes/MaterialService.md) to access it from
scripts.

### Property: MaterialService.ClayRoofTilesName

```json
{
  "type": "string",
  "access": "ReadOnly",
  "security": {
    "read": "RobloxEngineSecurity",
    "write": "RobloxEngineSecurity"
  },
  "serialization": {
    "can_load": true,
    "can_save": true
  },
  "thread_safety": "ReadSafe",
  "category": "Material Overrides",
  "capabilities": [
    "Material"
  ]
}
```

Specify [MaterialVariant](/docs/reference/engine/classes/MaterialVariant.md) name to override built-in ClayRoofTiles.
The Specified MaterialVariant must have
[MaterialVariant.BaseMaterial](/docs/reference/engine/classes/MaterialVariant.md) set to ClayRoofTiles. This property
is not scriptable; use [MaterialService:GetBaseMaterialOverride()](/docs/reference/engine/classes/MaterialService.md)
and [MaterialService:SetBaseMaterialOverride()](/docs/reference/engine/classes/MaterialService.md) to access it from
scripts.

### Property: MaterialService.CobblestoneName

```json
{
  "type": "string",
  "access": "ReadOnly",
  "security": {
    "read": "RobloxEngineSecurity",
    "write": "RobloxEngineSecurity"
  },
  "serialization": {
    "can_load": true,
    "can_save": true
  },
  "thread_safety": "ReadSafe",
  "category": "Material Overrides",
  "capabilities": [
    "Material"
  ]
}
```

Specify [MaterialVariant](/docs/reference/engine/classes/MaterialVariant.md) name to override built-in Cobblestone. The
Specified MaterialVariant must have [MaterialVariant.BaseMaterial](/docs/reference/engine/classes/MaterialVariant.md)
set to Cobblestone. This property is not scriptable; use
[MaterialService:GetBaseMaterialOverride()](/docs/reference/engine/classes/MaterialService.md) and
[MaterialService:SetBaseMaterialOverride()](/docs/reference/engine/classes/MaterialService.md) to access it from
scripts.

### Property: MaterialService.ConcreteName

```json
{
  "type": "string",
  "access": "ReadOnly",
  "security": {
    "read": "RobloxEngineSecurity",
    "write": "RobloxEngineSecurity"
  },
  "serialization": {
    "can_load": true,
    "can_save": true
  },
  "thread_safety": "ReadSafe",
  "category": "Material Overrides",
  "capabilities": [
    "Material"
  ]
}
```

Specify [MaterialVariant](/docs/reference/engine/classes/MaterialVariant.md) name to override built-in Concrete. The
Specified MaterialVariant must have [MaterialVariant.BaseMaterial](/docs/reference/engine/classes/MaterialVariant.md)
set to Concrete. This property is not scriptable; use
[MaterialService:GetBaseMaterialOverride()](/docs/reference/engine/classes/MaterialService.md) and
[MaterialService:SetBaseMaterialOverride()](/docs/reference/engine/classes/MaterialService.md) to access it from
scripts.

### Property: MaterialService.CorrodedMetalName

```json
{
  "type": "string",
  "access": "ReadOnly",
  "security": {
    "read": "RobloxEngineSecurity",
    "write": "RobloxEngineSecurity"
  },
  "serialization": {
    "can_load": true,
    "can_save": true
  },
  "thread_safety": "ReadSafe",
  "category": "Material Overrides",
  "capabilities": [
    "Material"
  ]
}
```

Specify [MaterialVariant](/docs/reference/engine/classes/MaterialVariant.md) name to override built-in CorrodedMetal.
The Specified MaterialVariant must have
[MaterialVariant.BaseMaterial](/docs/reference/engine/classes/MaterialVariant.md) set to CorrodedMetal. This property
is not scriptable; use [MaterialService:GetBaseMaterialOverride()](/docs/reference/engine/classes/MaterialService.md)
and [MaterialService:SetBaseMaterialOverride()](/docs/reference/engine/classes/MaterialService.md) to access it from
scripts.

### Property: MaterialService.CrackedLavaName

```json
{
  "type": "string",
  "access": "ReadOnly",
  "security": {
    "read": "RobloxEngineSecurity",
    "write": "RobloxEngineSecurity"
  },
  "serialization": {
    "can_load": true,
    "can_save": true
  },
  "thread_safety": "ReadSafe",
  "category": "Material Overrides",
  "capabilities": [
    "Material"
  ]
}
```

Specify [MaterialVariant](/docs/reference/engine/classes/MaterialVariant.md) name to override built-in CrackedLava. The
Specified MaterialVariant must have [MaterialVariant.BaseMaterial](/docs/reference/engine/classes/MaterialVariant.md)
set to CrackedLava. This property is not scriptable; use
[MaterialService:GetBaseMaterialOverride()](/docs/reference/engine/classes/MaterialService.md) and
[MaterialService:SetBaseMaterialOverride()](/docs/reference/engine/classes/MaterialService.md) to access it from
scripts.

### Property: MaterialService.DiamondPlateName

```json
{
  "type": "string",
  "access": "ReadOnly",
  "security": {
    "read": "RobloxEngineSecurity",
    "write": "RobloxEngineSecurity"
  },
  "serialization": {
    "can_load": true,
    "can_save": true
  },
  "thread_safety": "ReadSafe",
  "category": "Material Overrides",
  "capabilities": [
    "Material"
  ]
}
```

Specify [MaterialVariant](/docs/reference/engine/classes/MaterialVariant.md) name to override built-in DiamondPlate.
The Specified MaterialVariant must have
[MaterialVariant.BaseMaterial](/docs/reference/engine/classes/MaterialVariant.md) set to DiamondPlate. This property is
not scriptable; use [MaterialService:GetBaseMaterialOverride()](/docs/reference/engine/classes/MaterialService.md) and
[MaterialService:SetBaseMaterialOverride()](/docs/reference/engine/classes/MaterialService.md) to access it from
scripts.

### Property: MaterialService.FabricName

```json
{
  "type": "string",
  "access": "ReadOnly",
  "security": {
    "read": "RobloxEngineSecurity",
    "write": "RobloxEngineSecurity"
  },
  "serialization": {
    "can_load": true,
    "can_save": true
  },
  "thread_safety": "ReadSafe",
  "category": "Material Overrides",
  "capabilities": [
    "Material"
  ]
}
```

Specify [MaterialVariant](/docs/reference/engine/classes/MaterialVariant.md) name to override built-in Fabric. The
Specified MaterialVariant must have [MaterialVariant.BaseMaterial](/docs/reference/engine/classes/MaterialVariant.md)
set to Fabric. This property is not scriptable; use
[MaterialService:GetBaseMaterialOverride()](/docs/reference/engine/classes/MaterialService.md) and
[MaterialService:SetBaseMaterialOverride()](/docs/reference/engine/classes/MaterialService.md) to access it from
scripts.

### Property: MaterialService.FoilName

```json
{
  "type": "string",
  "access": "ReadOnly",
  "security": {
    "read": "RobloxEngineSecurity",
    "write": "RobloxEngineSecurity"
  },
  "serialization": {
    "can_load": true,
    "can_save": true
  },
  "thread_safety": "ReadSafe",
  "category": "Material Overrides",
  "capabilities": [
    "Material"
  ]
}
```

Specify [MaterialVariant](/docs/reference/engine/classes/MaterialVariant.md) name to override built-in Foil. The
Specified MaterialVariant must have [MaterialVariant.BaseMaterial](/docs/reference/engine/classes/MaterialVariant.md)
set to Foil. This property is not scriptable; use
[MaterialService:GetBaseMaterialOverride()](/docs/reference/engine/classes/MaterialService.md) and
[MaterialService:SetBaseMaterialOverride()](/docs/reference/engine/classes/MaterialService.md) to access it from
scripts.

### Property: MaterialService.GlacierName

```json
{
  "type": "string",
  "access": "ReadOnly",
  "security": {
    "read": "RobloxEngineSecurity",
    "write": "RobloxEngineSecurity"
  },
  "serialization": {
    "can_load": true,
    "can_save": true
  },
  "thread_safety": "ReadSafe",
  "category": "Material Overrides",
  "capabilities": [
    "Material"
  ]
}
```

Specify [MaterialVariant](/docs/reference/engine/classes/MaterialVariant.md) name to override built-in Glacier. The
Specified MaterialVariant must have [MaterialVariant.BaseMaterial](/docs/reference/engine/classes/MaterialVariant.md)
set to Glacier. This property is not scriptable; use
[MaterialService:GetBaseMaterialOverride()](/docs/reference/engine/classes/MaterialService.md) and
[MaterialService:SetBaseMaterialOverride()](/docs/reference/engine/classes/MaterialService.md) to access it from
scripts.

### Property: MaterialService.GraniteName

```json
{
  "type": "string",
  "access": "ReadOnly",
  "security": {
    "read": "RobloxEngineSecurity",
    "write": "RobloxEngineSecurity"
  },
  "serialization": {
    "can_load": true,
    "can_save": true
  },
  "thread_safety": "ReadSafe",
  "category": "Material Overrides",
  "capabilities": [
    "Material"
  ]
}
```

Specify [MaterialVariant](/docs/reference/engine/classes/MaterialVariant.md) name to override built-in Granite. The
Specified MaterialVariant must have [MaterialVariant.BaseMaterial](/docs/reference/engine/classes/MaterialVariant.md)
set to Granite. This property is not scriptable; use
[MaterialService:GetBaseMaterialOverride()](/docs/reference/engine/classes/MaterialService.md) and
[MaterialService:SetBaseMaterialOverride()](/docs/reference/engine/classes/MaterialService.md) to access it from
scripts.

### Property: MaterialService.GrassName

```json
{
  "type": "string",
  "access": "ReadOnly",
  "security": {
    "read": "RobloxEngineSecurity",
    "write": "RobloxEngineSecurity"
  },
  "serialization": {
    "can_load": true,
    "can_save": true
  },
  "thread_safety": "ReadSafe",
  "category": "Material Overrides",
  "capabilities": [
    "Material"
  ]
}
```

Specify [MaterialVariant](/docs/reference/engine/classes/MaterialVariant.md) name to override built-in Grass. The
Specified MaterialVariant must have [MaterialVariant.BaseMaterial](/docs/reference/engine/classes/MaterialVariant.md)
set to Grass. This property is not scriptable; use
[MaterialService:GetBaseMaterialOverride()](/docs/reference/engine/classes/MaterialService.md) and
[MaterialService:SetBaseMaterialOverride()](/docs/reference/engine/classes/MaterialService.md) to access it from
scripts.

### Property: MaterialService.GroundName

```json
{
  "type": "string",
  "access": "ReadOnly",
  "security": {
    "read": "RobloxEngineSecurity",
    "write": "RobloxEngineSecurity"
  },
  "serialization": {
    "can_load": true,
    "can_save": true
  },
  "thread_safety": "ReadSafe",
  "category": "Material Overrides",
  "capabilities": [
    "Material"
  ]
}
```

Specify [MaterialVariant](/docs/reference/engine/classes/MaterialVariant.md) name to override built-in Ground. The
Specified MaterialVariant must have [MaterialVariant.BaseMaterial](/docs/reference/engine/classes/MaterialVariant.md)
set to Ground. This property is not scriptable; use
[MaterialService:GetBaseMaterialOverride()](/docs/reference/engine/classes/MaterialService.md) and
[MaterialService:SetBaseMaterialOverride()](/docs/reference/engine/classes/MaterialService.md) to access it from
scripts.

### Property: MaterialService.IceName

```json
{
  "type": "string",
  "access": "ReadOnly",
  "security": {
    "read": "RobloxEngineSecurity",
    "write": "RobloxEngineSecurity"
  },
  "serialization": {
    "can_load": true,
    "can_save": true
  },
  "thread_safety": "ReadSafe",
  "category": "Material Overrides",
  "capabilities": [
    "Material"
  ]
}
```

Specify [MaterialVariant](/docs/reference/engine/classes/MaterialVariant.md) name to override built-in Ice. The
Specified MaterialVariant must have [MaterialVariant.BaseMaterial](/docs/reference/engine/classes/MaterialVariant.md)
set to Ice. This property is not scriptable; use
[MaterialService:GetBaseMaterialOverride()](/docs/reference/engine/classes/MaterialService.md) and
[MaterialService:SetBaseMaterialOverride()](/docs/reference/engine/classes/MaterialService.md) to access it from
scripts.

### Property: MaterialService.LeafyGrassName

```json
{
  "type": "string",
  "access": "ReadOnly",
  "security": {
    "read": "RobloxEngineSecurity",
    "write": "RobloxEngineSecurity"
  },
  "serialization": {
    "can_load": true,
    "can_save": true
  },
  "thread_safety": "ReadSafe",
  "category": "Material Overrides",
  "capabilities": [
    "Material"
  ]
}
```

Specify [MaterialVariant](/docs/reference/engine/classes/MaterialVariant.md) name to override built-in LeafyGrass. The
Specified MaterialVariant must have [MaterialVariant.BaseMaterial](/docs/reference/engine/classes/MaterialVariant.md)
set to LeafyGrass. This property is not scriptable; use
[MaterialService:GetBaseMaterialOverride()](/docs/reference/engine/classes/MaterialService.md) and
[MaterialService:SetBaseMaterialOverride()](/docs/reference/engine/classes/MaterialService.md) to access it from
scripts.

### Property: MaterialService.LeatherName

```json
{
  "type": "string",
  "access": "ReadOnly",
  "security": {
    "read": "RobloxEngineSecurity",
    "write": "RobloxEngineSecurity"
  },
  "serialization": {
    "can_load": true,
    "can_save": true
  },
  "thread_safety": "ReadSafe",
  "category": "Material Overrides",
  "capabilities": [
    "Material"
  ]
}
```

Specify [MaterialVariant](/docs/reference/engine/classes/MaterialVariant.md) name to override built-in Leather. The
Specified MaterialVariant must have [MaterialVariant.BaseMaterial](/docs/reference/engine/classes/MaterialVariant.md)
set to Leather. This property is not scriptable; use
[MaterialService:GetBaseMaterialOverride()](/docs/reference/engine/classes/MaterialService.md) and
[MaterialService:SetBaseMaterialOverride()](/docs/reference/engine/classes/MaterialService.md) to access it from
scripts.

### Property: MaterialService.LimestoneName

```json
{
  "type": "string",
  "access": "ReadOnly",
  "security": {
    "read": "RobloxEngineSecurity",
    "write": "RobloxEngineSecurity"
  },
  "serialization": {
    "can_load": true,
    "can_save": true
  },
  "thread_safety": "ReadSafe",
  "category": "Material Overrides",
  "capabilities": [
    "Material"
  ]
}
```

Specify [MaterialVariant](/docs/reference/engine/classes/MaterialVariant.md) name to override built-in Limestone. The
Specified MaterialVariant must have [MaterialVariant.BaseMaterial](/docs/reference/engine/classes/MaterialVariant.md)
set to Limestone. This property is not scriptable; use
[MaterialService:GetBaseMaterialOverride()](/docs/reference/engine/classes/MaterialService.md) and
[MaterialService:SetBaseMaterialOverride()](/docs/reference/engine/classes/MaterialService.md) to access it from
scripts.

### Property: MaterialService.MarbleName

```json
{
  "type": "string",
  "access": "ReadOnly",
  "security": {
    "read": "RobloxEngineSecurity",
    "write": "RobloxEngineSecurity"
  },
  "serialization": {
    "can_load": true,
    "can_save": true
  },
  "thread_safety": "ReadSafe",
  "category": "Material Overrides",
  "capabilities": [
    "Material"
  ]
}
```

Specify [MaterialVariant](/docs/reference/engine/classes/MaterialVariant.md) name to override built-in Marble. The
Specified MaterialVariant must have [MaterialVariant.BaseMaterial](/docs/reference/engine/classes/MaterialVariant.md)
set to Marble. This property is not scriptable; use
[MaterialService:GetBaseMaterialOverride()](/docs/reference/engine/classes/MaterialService.md) and
[MaterialService:SetBaseMaterialOverride()](/docs/reference/engine/classes/MaterialService.md) to access it from
scripts.

### Property: MaterialService.MetalName

```json
{
  "type": "string",
  "access": "ReadOnly",
  "security": {
    "read": "RobloxEngineSecurity",
    "write": "RobloxEngineSecurity"
  },
  "serialization": {
    "can_load": true,
    "can_save": true
  },
  "thread_safety": "ReadSafe",
  "category": "Material Overrides",
  "capabilities": [
    "Material"
  ]
}
```

Specify [MaterialVariant](/docs/reference/engine/classes/MaterialVariant.md) name to override built-in Metal. The
Specified MaterialVariant must have [MaterialVariant.BaseMaterial](/docs/reference/engine/classes/MaterialVariant.md)
set to Metal. This property is not scriptable; use
[MaterialService:GetBaseMaterialOverride()](/docs/reference/engine/classes/MaterialService.md) and
[MaterialService:SetBaseMaterialOverride()](/docs/reference/engine/classes/MaterialService.md) to access it from
scripts.

### Property: MaterialService.MudName

```json
{
  "type": "string",
  "access": "ReadOnly",
  "security": {
    "read": "RobloxEngineSecurity",
    "write": "RobloxEngineSecurity"
  },
  "serialization": {
    "can_load": true,
    "can_save": true
  },
  "thread_safety": "ReadSafe",
  "category": "Material Overrides",
  "capabilities": [
    "Material"
  ]
}
```

Specify [MaterialVariant](/docs/reference/engine/classes/MaterialVariant.md) name to override built-in Mud. The
Specified MaterialVariant must have [MaterialVariant.BaseMaterial](/docs/reference/engine/classes/MaterialVariant.md)
set to Mud. This property is not scriptable; use
[MaterialService:GetBaseMaterialOverride()](/docs/reference/engine/classes/MaterialService.md) and
[MaterialService:SetBaseMaterialOverride()](/docs/reference/engine/classes/MaterialService.md) to access it from
scripts.

### Property: MaterialService.PavementName

```json
{
  "type": "string",
  "access": "ReadOnly",
  "security": {
    "read": "RobloxEngineSecurity",
    "write": "RobloxEngineSecurity"
  },
  "serialization": {
    "can_load": true,
    "can_save": true
  },
  "thread_safety": "ReadSafe",
  "category": "Material Overrides",
  "capabilities": [
    "Material"
  ]
}
```

Specify [MaterialVariant](/docs/reference/engine/classes/MaterialVariant.md) name to override built-in Pavement. The
Specified MaterialVariant must have [MaterialVariant.BaseMaterial](/docs/reference/engine/classes/MaterialVariant.md)
set to Pavement. This property is not scriptable; use
[MaterialService:GetBaseMaterialOverride()](/docs/reference/engine/classes/MaterialService.md) and
[MaterialService:SetBaseMaterialOverride()](/docs/reference/engine/classes/MaterialService.md) to access it from
scripts.

### Property: MaterialService.PebbleName

```json
{
  "type": "string",
  "access": "ReadOnly",
  "security": {
    "read": "RobloxEngineSecurity",
    "write": "RobloxEngineSecurity"
  },
  "serialization": {
    "can_load": true,
    "can_save": true
  },
  "thread_safety": "ReadSafe",
  "category": "Material Overrides",
  "capabilities": [
    "Material"
  ]
}
```

Specify [MaterialVariant](/docs/reference/engine/classes/MaterialVariant.md) name to override built-in Pebble. The
Specified MaterialVariant must have [MaterialVariant.BaseMaterial](/docs/reference/engine/classes/MaterialVariant.md)
set to Pebble. This property is not scriptable; use
[MaterialService:GetBaseMaterialOverride()](/docs/reference/engine/classes/MaterialService.md) and
[MaterialService:SetBaseMaterialOverride()](/docs/reference/engine/classes/MaterialService.md) to access it from
scripts.

### Property: MaterialService.PlasterName

```json
{
  "type": "string",
  "access": "ReadOnly",
  "security": {
    "read": "RobloxEngineSecurity",
    "write": "RobloxEngineSecurity"
  },
  "serialization": {
    "can_load": true,
    "can_save": true
  },
  "thread_safety": "ReadSafe",
  "category": "Material Overrides",
  "capabilities": [
    "Material"
  ]
}
```

Specify [MaterialVariant](/docs/reference/engine/classes/MaterialVariant.md) name to override built-in Plaster. The
Specified MaterialVariant must have [MaterialVariant.BaseMaterial](/docs/reference/engine/classes/MaterialVariant.md)
set to Plaster. This property is not scriptable; use
[MaterialService:GetBaseMaterialOverride()](/docs/reference/engine/classes/MaterialService.md) and
[MaterialService:SetBaseMaterialOverride()](/docs/reference/engine/classes/MaterialService.md) to access it from
scripts.

### Property: MaterialService.PlasticName

```json
{
  "type": "string",
  "access": "ReadOnly",
  "security": {
    "read": "RobloxEngineSecurity",
    "write": "RobloxEngineSecurity"
  },
  "serialization": {
    "can_load": true,
    "can_save": true
  },
  "thread_safety": "ReadSafe",
  "category": "Material Overrides",
  "capabilities": [
    "Material"
  ]
}
```

Specify [MaterialVariant](/docs/reference/engine/classes/MaterialVariant.md) name to override built-in Plastic. The
Specified MaterialVariant must have [MaterialVariant.BaseMaterial](/docs/reference/engine/classes/MaterialVariant.md)
set to Plastic. This property is not scriptable; use
[MaterialService:GetBaseMaterialOverride()](/docs/reference/engine/classes/MaterialService.md) and
[MaterialService:SetBaseMaterialOverride()](/docs/reference/engine/classes/MaterialService.md) to access it from
scripts.

### Property: MaterialService.RockName

```json
{
  "type": "string",
  "access": "ReadOnly",
  "security": {
    "read": "RobloxEngineSecurity",
    "write": "RobloxEngineSecurity"
  },
  "serialization": {
    "can_load": true,
    "can_save": true
  },
  "thread_safety": "ReadSafe",
  "category": "Material Overrides",
  "capabilities": [
    "Material"
  ]
}
```

Specify [MaterialVariant](/docs/reference/engine/classes/MaterialVariant.md) name to override built-in Rock. The
Specified MaterialVariant must have [MaterialVariant.BaseMaterial](/docs/reference/engine/classes/MaterialVariant.md)
set to Rock. This property is not scriptable; use
[MaterialService:GetBaseMaterialOverride()](/docs/reference/engine/classes/MaterialService.md) and
[MaterialService:SetBaseMaterialOverride()](/docs/reference/engine/classes/MaterialService.md) to access it from
scripts.

### Property: MaterialService.RoofShinglesName

```json
{
  "type": "string",
  "access": "ReadOnly",
  "security": {
    "read": "RobloxEngineSecurity",
    "write": "RobloxEngineSecurity"
  },
  "serialization": {
    "can_load": true,
    "can_save": true
  },
  "thread_safety": "ReadSafe",
  "category": "Material Overrides",
  "capabilities": [
    "Material"
  ]
}
```

Specify [MaterialVariant](/docs/reference/engine/classes/MaterialVariant.md) name to override built-in RoofShingles.
The Specified MaterialVariant must have
[MaterialVariant.BaseMaterial](/docs/reference/engine/classes/MaterialVariant.md) set to RoofShingles. This property is
not scriptable; use [MaterialService:GetBaseMaterialOverride()](/docs/reference/engine/classes/MaterialService.md) and
[MaterialService:SetBaseMaterialOverride()](/docs/reference/engine/classes/MaterialService.md) to access it from
scripts.

### Property: MaterialService.RubberName

```json
{
  "type": "string",
  "access": "ReadOnly",
  "security": {
    "read": "RobloxEngineSecurity",
    "write": "RobloxEngineSecurity"
  },
  "serialization": {
    "can_load": true,
    "can_save": true
  },
  "thread_safety": "ReadSafe",
  "category": "Material Overrides",
  "capabilities": [
    "Material"
  ]
}
```

Specify [MaterialVariant](/docs/reference/engine/classes/MaterialVariant.md) name to override built-in Rubber. The
Specified MaterialVariant must have [MaterialVariant.BaseMaterial](/docs/reference/engine/classes/MaterialVariant.md)
set to Rubber. This property is not scriptable; use
[MaterialService:GetBaseMaterialOverride()](/docs/reference/engine/classes/MaterialService.md) and
[MaterialService:SetBaseMaterialOverride()](/docs/reference/engine/classes/MaterialService.md) to access it from
scripts.

### Property: MaterialService.SaltName

```json
{
  "type": "string",
  "access": "ReadOnly",
  "security": {
    "read": "RobloxEngineSecurity",
    "write": "RobloxEngineSecurity"
  },
  "serialization": {
    "can_load": true,
    "can_save": true
  },
  "thread_safety": "ReadSafe",
  "category": "Material Overrides",
  "capabilities": [
    "Material"
  ]
}
```

Specify [MaterialVariant](/docs/reference/engine/classes/MaterialVariant.md) name to override built-in Salt. The
Specified MaterialVariant must have [MaterialVariant.BaseMaterial](/docs/reference/engine/classes/MaterialVariant.md)
set to Salt. This property is not scriptable; use
[MaterialService:GetBaseMaterialOverride()](/docs/reference/engine/classes/MaterialService.md) and
[MaterialService:SetBaseMaterialOverride()](/docs/reference/engine/classes/MaterialService.md) to access it from
scripts.

### Property: MaterialService.SandName

```json
{
  "type": "string",
  "access": "ReadOnly",
  "security": {
    "read": "RobloxEngineSecurity",
    "write": "RobloxEngineSecurity"
  },
  "serialization": {
    "can_load": true,
    "can_save": true
  },
  "thread_safety": "ReadSafe",
  "category": "Material Overrides",
  "capabilities": [
    "Material"
  ]
}
```

Specify [MaterialVariant](/docs/reference/engine/classes/MaterialVariant.md) name to override built-in Sand. The
Specified MaterialVariant must have [MaterialVariant.BaseMaterial](/docs/reference/engine/classes/MaterialVariant.md)
set to Sand. This property is not scriptable; use
[MaterialService:GetBaseMaterialOverride()](/docs/reference/engine/classes/MaterialService.md) and
[MaterialService:SetBaseMaterialOverride()](/docs/reference/engine/classes/MaterialService.md) to access it from
scripts.

### Property: MaterialService.SandstoneName

```json
{
  "type": "string",
  "access": "ReadOnly",
  "security": {
    "read": "RobloxEngineSecurity",
    "write": "RobloxEngineSecurity"
  },
  "serialization": {
    "can_load": true,
    "can_save": true
  },
  "thread_safety": "ReadSafe",
  "category": "Material Overrides",
  "capabilities": [
    "Material"
  ]
}
```

Specify [MaterialVariant](/docs/reference/engine/classes/MaterialVariant.md) name to override built-in Sandstone. The
Specified MaterialVariant must have [MaterialVariant.BaseMaterial](/docs/reference/engine/classes/MaterialVariant.md)
set to Sandstone. This property is not scriptable; use
[MaterialService:GetBaseMaterialOverride()](/docs/reference/engine/classes/MaterialService.md) and
[MaterialService:SetBaseMaterialOverride()](/docs/reference/engine/classes/MaterialService.md) to access it from
scripts.

### Property: MaterialService.SlateName

```json
{
  "type": "string",
  "access": "ReadOnly",
  "security": {
    "read": "RobloxEngineSecurity",
    "write": "RobloxEngineSecurity"
  },
  "serialization": {
    "can_load": true,
    "can_save": true
  },
  "thread_safety": "ReadSafe",
  "category": "Material Overrides",
  "capabilities": [
    "Material"
  ]
}
```

Specify [MaterialVariant](/docs/reference/engine/classes/MaterialVariant.md) name to override built-in Slate. The
Specified MaterialVariant must have [MaterialVariant.BaseMaterial](/docs/reference/engine/classes/MaterialVariant.md)
set to Slate. This property is not scriptable; use
[MaterialService:GetBaseMaterialOverride()](/docs/reference/engine/classes/MaterialService.md) and
[MaterialService:SetBaseMaterialOverride()](/docs/reference/engine/classes/MaterialService.md) to access it from
scripts.

### Property: MaterialService.SmoothPlasticName

```json
{
  "type": "string",
  "access": "ReadOnly",
  "security": {
    "read": "RobloxEngineSecurity",
    "write": "RobloxEngineSecurity"
  },
  "serialization": {
    "can_load": true,
    "can_save": true
  },
  "thread_safety": "ReadSafe",
  "category": "Material Overrides",
  "capabilities": [
    "Material"
  ]
}
```

Specify [MaterialVariant](/docs/reference/engine/classes/MaterialVariant.md) name to override built-in SmoothPlastic.
The Specified MaterialVariant must have
[MaterialVariant.BaseMaterial](/docs/reference/engine/classes/MaterialVariant.md) set to SmoothPlastic. This property
is not scriptable; use [MaterialService:GetBaseMaterialOverride()](/docs/reference/engine/classes/MaterialService.md)
and [MaterialService:SetBaseMaterialOverride()](/docs/reference/engine/classes/MaterialService.md) to access it from
scripts.

### Property: MaterialService.SnowName

```json
{
  "type": "string",
  "access": "ReadOnly",
  "security": {
    "read": "RobloxEngineSecurity",
    "write": "RobloxEngineSecurity"
  },
  "serialization": {
    "can_load": true,
    "can_save": true
  },
  "thread_safety": "ReadSafe",
  "category": "Material Overrides",
  "capabilities": [
    "Material"
  ]
}
```

Specify [MaterialVariant](/docs/reference/engine/classes/MaterialVariant.md) name to override built-in Snow. The
Specified MaterialVariant must have [MaterialVariant.BaseMaterial](/docs/reference/engine/classes/MaterialVariant.md)
set to Snow. This property is not scriptable; use
[MaterialService:GetBaseMaterialOverride()](/docs/reference/engine/classes/MaterialService.md) and
[MaterialService:SetBaseMaterialOverride()](/docs/reference/engine/classes/MaterialService.md) to access it from
scripts.

### Property: MaterialService.Use2022Materials

```json
{
  "type": "boolean",
  "access": "ReadOnly",
  "security": {
    "read": "RobloxScriptSecurity",
    "write": "RobloxScriptSecurity"
  },
  "serialization": {
    "can_load": false,
    "can_save": false
  },
  "thread_safety": "ReadSafe",
  "category": "Material Pack",
  "capabilities": [
    "Material"
  ]
}
```

When it's false, built-in materials use the material pack before 2022.
When it's true, built-in materials use the material pack released in 2022.

### Property: MaterialService.WoodName

```json
{
  "type": "string",
  "access": "ReadOnly",
  "security": {
    "read": "RobloxEngineSecurity",
    "write": "RobloxEngineSecurity"
  },
  "serialization": {
    "can_load": true,
    "can_save": true
  },
  "thread_safety": "ReadSafe",
  "category": "Material Overrides",
  "capabilities": [
    "Material"
  ]
}
```

Specify [MaterialVariant](/docs/reference/engine/classes/MaterialVariant.md) name to override built-in Wood. The
Specified MaterialVariant must have [MaterialVariant.BaseMaterial](/docs/reference/engine/classes/MaterialVariant.md)
set to Wood. This property is not scriptable; use
[MaterialService:GetBaseMaterialOverride()](/docs/reference/engine/classes/MaterialService.md) and
[MaterialService:SetBaseMaterialOverride()](/docs/reference/engine/classes/MaterialService.md) to access it from
scripts.

### Property: MaterialService.WoodPlanksName

```json
{
  "type": "string",
  "access": "ReadOnly",
  "security": {
    "read": "RobloxEngineSecurity",
    "write": "RobloxEngineSecurity"
  },
  "serialization": {
    "can_load": true,
    "can_save": true
  },
  "thread_safety": "ReadSafe",
  "category": "Material Overrides",
  "capabilities": [
    "Material"
  ]
}
```

Specify [MaterialVariant](/docs/reference/engine/classes/MaterialVariant.md) name to override built-in WoodPlanks. The
Specified MaterialVariant must have [MaterialVariant.BaseMaterial](/docs/reference/engine/classes/MaterialVariant.md)
set to WoodPlanks. This property is not scriptable; use
[MaterialService:GetBaseMaterialOverride()](/docs/reference/engine/classes/MaterialService.md) and
[MaterialService:SetBaseMaterialOverride()](/docs/reference/engine/classes/MaterialService.md) to access it from
scripts.

## Methods

### Method: MaterialService:GetBaseMaterialOverride

**Signature:** `MaterialService:GetBaseMaterialOverride(material: Material): string`

Get the override [MaterialVariant](/docs/reference/engine/classes/MaterialVariant.md) name of specified Material type.

*Security: None · Thread Safety: Unsafe · Capabilities: Material*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `material` | `Material` |  | Material type to be fetched. |

**Returns:** `string` — MaterialVariant name currently set as override.

### Method: MaterialService:GetMaterialVariant

**Signature:** `MaterialService:GetMaterialVariant(material: Material, name: string): MaterialVariant`

Get the effective MaterialVariant reference given a MaterialVariant name
and BaseMaterial. This MaterialVariant must be a descendant of
MaterialService. Returns `nil` if no matching instance exists.

*Security: None · Thread Safety: Unsafe · Capabilities: Material*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `material` | `Material` |  | BaseMaterial of MaterialVariant. |
| `name` | `string` |  | Name of MaterialVariant. |

**Returns:** `MaterialVariant` — A MaterialVariant instance that matches parameters.

### Method: MaterialService:SetBaseMaterialOverride

**Signature:** `MaterialService:SetBaseMaterialOverride(material: Material, name: string): ()`

Set a [MaterialVariant](/docs/reference/engine/classes/MaterialVariant.md) name that overrides a built-in material.

*Security: None · Thread Safety: Unsafe · Capabilities: Material*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `material` | `Material` |  | The Material type to be changed. |
| `name` | `string` |  | Name of the MaterialVariant object. |

**Returns:** `()`

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