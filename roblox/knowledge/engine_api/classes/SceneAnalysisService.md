---
name: SceneAnalysisService
last_updated: 2026-10-30T19:55:53Z
inherits:
  - Instance
  - Object
type: class
memory_category: Instances
tags:
  - NotCreatable
  - Service
  - NotReplicated
---

# Class: SceneAnalysisService

## Description

Provides programmatic access to the
[Scene Analysis](/docs/en-us/performance-optimization/scene-analysis.md) tool's
underlying performance data.

## Methods

### Method: SceneAnalysisService:GetAnimationMemoryAsync

**Signature:** `SceneAnalysisService:GetAnimationMemoryAsync(): AnimationMemoryResult`

Returns loaded animation clip memory. The same asset shared by multiple
Animators appears only once, with all owners listed.

#### Root dictionary

| Key        | Type   | Description                                                      |
| ---------- | ------ | ---------------------------------------------------------------- |
| `Name`     | string | Always `"AnimationMemory"`.                                      |
| `Size`     | number | Total loaded clip memory in bytes.                               |
| `Children` | array  | Array of clip entries and optionally an out-of-data model group. |

#### Clip entry

Each child in `Children` is either a clip entry or the "not in data model"
group (see below).

| Key       | Type   | Description                                                 |
| --------- | ------ | ----------------------------------------------------------- |
| `Name`    | string | The asset ID (e.g. `"rbxassetid://111"`).                   |
| `Size`    | number | Clip memory in bytes.                                       |
| `AssetId` | string | The asset ID string (same value as `Name`).                 |
| `Owners`  | array  | Array of owner entries for all Animators playing this clip. |

#### Owner entry

| Key         | Type   | Description                                                                  |
| ----------- | ------ | ---------------------------------------------------------------------------- |
| `Name`      | string | Full path to the owning Animator (e.g. `"Workspace.NPC.Humanoid.Animator"`). |
| `ClassName` | string | Class name of the owner (e.g. `"Animator"`).                                 |

#### "Not in data model" group

Clips from Animators held only by Lua (not parented in the data model) are
collected into a single group entry.

| Key        | Type   | Description                                   |
| ---------- | ------ | --------------------------------------------- |
| `Name`     | string | Always `"Not In DataModel"`.                  |
| `Size`     | number | Sum of clip bytes in this group.              |
| `Children` | array  | Array of clip entries (same schema as above). |

#### Example

```lua
{
  Name = "AnimationMemory",
  Size = 1048576,
  Children = {
    { Name = "rbxassetid://111", Size = 32768, AssetId = "rbxassetid://111",
      Owners = {
        { Name = "Workspace.Player.Humanoid.Animator", ClassName = "Animator" },
    }},
    { Name = "rbxassetid://444", Size = 65536, AssetId = "rbxassetid://444",
      Owners = {
        { Name = "Workspace.NPC1.Humanoid.Animator", ClassName = "Animator" },
        { Name = "Workspace.NPC2.Humanoid.Animator", ClassName = "Animator" },
    }},
    { Name = "Not In DataModel", Size = 32768, Children = {
        { Name = "rbxassetid://555", Size = 32768, AssetId = "rbxassetid://555",
          Owners = {
            { Name = "Animator", ClassName = "Animator" },
        }},
    }},
  }
}
```

*Yields · Security: None · Thread Safety: Unsafe*

**Returns:** `AnimationMemoryResult` — A dictionary tree of loaded animation clip memory, deduplicated by
clip.

### Method: SceneAnalysisService:GetAudioMemoryAsync

**Signature:** `SceneAnalysisService:GetAudioMemoryAsync(): AudioMemoryResult`

Returns loaded audio asset memory, deduplicated by asset ID. Assets whose
owners share the same parent are organized under that parent path —
flattened when there is one child, nested when there are several. Assets
whose owners span different parents appear as shared entries with an
`Owners` array.

#### Root dictionary

| Key        | Type   | Description                                             |
| ---------- | ------ | ------------------------------------------------------- |
| `Name`     | string | Always `"AudioMemory"`.                                 |
| `Size`     | number | Total loaded audio memory in bytes.                     |
| `Children` | array  | Mix of flat entries, parent groups, and shared entries. |

#### Flat asset entry

Emitted when a parent has exactly one audio child.

| Key       | Type   | Description                                          |
| --------- | ------ | ---------------------------------------------------- |
| `Name`    | string | Full instance path (e.g. `"Workspace.Map.BGMusic"`). |
| `Size`    | number | Asset memory in bytes.                               |
| `AssetId` | string | The audio asset ID.                                  |

#### Parent group

Emitted when a parent has multiple audio children.

| Key        | Type   | Description                                                        |
| ---------- | ------ | ------------------------------------------------------------------ |
| `Name`     | string | Parent path (e.g. `"Workspace.Map.SFX"`).                          |
| `Size`     | number | Sum of child asset bytes.                                          |
| `Children` | array  | Array of flat asset entries (each with `Name`, `Size`, `AssetId`). |

#### Shared asset entry

Emitted when an asset's owners are under different parents.

| Key       | Type   | Description                                 |
| --------- | ------ | ------------------------------------------- |
| `Name`    | string | The asset ID.                               |
| `Size`    | number | Asset memory in bytes.                      |
| `AssetId` | string | The asset ID string (same value as `Name`). |
| `Owners`  | array  | Array of owner entries.                     |

#### Owner entry

| Key         | Type   | Description                                            |
| ----------- | ------ | ------------------------------------------------------ |
| `Name`      | string | Full instance path (e.g. `"Workspace.Zone1.Ambient"`). |
| `ClassName` | string | `"Sound"` or `"AudioPlayer"`.                          |

#### Example

```lua
{
  Name = "AudioMemory",
  Size = 5242880,
  Children = {
    -- Single audio under unique parent (flat)
    { Name = "Workspace.Map.BGMusic", Size = 2097152,
      AssetId = "rbxassetid://111" },

    -- Multiple audio under same parent (grouped)
    { Name = "Workspace.Map.SFX", Size = 1048576, Children = {
        { Name = "Workspace.Map.SFX.Explosion", Size = 524288, AssetId = "rbxassetid://222" },
        { Name = "Workspace.Map.SFX.Gunshot",   Size = 524288, AssetId = "rbxassetid://333" },
    }},

    -- Shared asset (owners in different locations)
    { Name = "rbxassetid://444", Size = 2097152, AssetId = "rbxassetid://444",
      Owners = {
        { Name = "Workspace.Zone1.Ambient", ClassName = "Sound" },
        { Name = "Workspace.Zone2.Ambient", ClassName = "Sound" },
    }},
  }
}
```

*Yields · Security: None · Thread Safety: Unsafe*

**Returns:** `AudioMemoryResult` — A dictionary tree of loaded audio asset memory, deduplicated by asset
ID.

### Method: SceneAnalysisService:GetInstanceCompositionAsync

**Signature:** `SceneAnalysisService:GetInstanceCompositionAsync(): InstanceCompositionResult`

Returns instance counts by category and class from the data model tree.
Scans descendants of Workspace, Players, Lighting, MaterialService,
ReplicatedFirst, ReplicatedStorage, ServerScriptService, ServerStorage,
StarterGui, StarterPack, StarterPlayer, Teams, SoundService, and
TextChatService. Each instance is classified into one of the categories
below based on its class hierarchy.

#### Root dictionary

| Key        | Type   | Description                                       |
| ---------- | ------ | ------------------------------------------------- |
| `Name`     | string | Always `"InstanceComposition"`.                   |
| `Size`     | number | Total instance count across all scanned services. |
| `Children` | array  | Array of category entries.                        |

#### Category entry

| Key        | Type   | Description                       |
| ---------- | ------ | --------------------------------- |
| `Name`     | string | Category name (see table below).  |
| `Size`     | number | Total instances in this category. |
| `Children` | array  | Array of class entries.           |

#### Class entry (leaf)

| Key    | Type   | Description                                            |
| ------ | ------ | ------------------------------------------------------ |
| `Name` | string | The class name (e.g. `"Part"`, `"Script"`, `"Frame"`). |
| `Size` | number | Number of instances of this class.                     |

#### Categories

| Category           | Representative Types                                                                 |
| ------------------ | ------------------------------------------------------------------------------------ |
| 3D Objects         | BasePart, Model, Camera                                                              |
| Physics            | Attachment, Constraint, JointInstance, WeldConstraint, ControllerManager, SensorBase |
| UI                 | GuiBase, BasePlayerGui, UIBase, ProximityPrompt, ClickDetector, TextChannel          |
| Lights             | Light                                                                                |
| PostProcessing     | PostEffect, Highlight, Atmosphere, Sky, Clouds                                       |
| Scripts            | LuaSourceContainer, BindableEvent, RemoteEvent, RemoteFunction                       |
| Audio              | Sound, SoundEffect, AudioPlayer, Wire, SoundGroup, AudioEmitter                      |
| Animation          | Animator, AnimationController, Animation, KeyframeSequence, IKControl                |
| Values             | ValueBase                                                                            |
| Character          | CharacterAppearance, Humanoid, HumanoidDescription, BaseWrap, FaceControls           |
| Textures           | FaceInstance, SurfaceAppearance, MaterialVariant                                     |
| Meshes             | DataModelMesh                                                                        |
| Particles          | ParticleEmitter, Fire, Trail, Beam, Explosion                                        |
| Services & Storage | Player, Folder, Configuration                                                        |
| Misc               | Tool, Backpack, Team, ForceField, PathfindingModifier, PackageLink, HapticEffect     |
| Unclassified       | Anything not matching the above                                                      |

#### Example

```lua
{
  Name = "InstanceComposition",
  Size = 12450,
  Children = {
    { Name = "3D Objects", Size = 5200, Children = {
        { Name = "Part", Size = 3100 },
        { Name = "MeshPart", Size = 1800 },
        { Name = "Model", Size = 300 },
    }},
    { Name = "UI", Size = 2100, Children = {
        { Name = "Frame", Size = 900 },
        { Name = "TextLabel", Size = 700 },
        { Name = "UIListLayout", Size = 500 },
    }},
  }
}
```

*Yields · Security: None · Thread Safety: Unsafe*

**Returns:** `InstanceCompositionResult` — A dictionary tree of instance counts grouped by category and class
name.

### Method: SceneAnalysisService:GetScriptMemoryAsync

**Signature:** `SceneAnalysisService:GetScriptMemoryAsync(): ScriptMemoryResult`

Returns per-script Luau VM heap memory usage in bytes. Scripts are grouped
first by their containing service (derived from the first segment of the
dotted path), then split into `"ModuleScripts"` and `"Scripts"` subgroups
based on the instance's class.

#### Root dictionary

| Key        | Type   | Description                        |
| ---------- | ------ | ---------------------------------- |
| `Name`     | string | Always `"ScriptMemory"`.           |
| `Size`     | number | Total Luau VM memory in bytes.     |
| `Children` | array  | Array of service category entries. |

#### Service category entry

| Key        | Type   | Description                                                                  |
| ---------- | ------ | ---------------------------------------------------------------------------- |
| `Name`     | string | Service name (e.g. `"ServerScriptService"`, `"ReplicatedStorage"`).          |
| `Size`     | number | Sum of all script memory in this service, in bytes.                          |
| `Children` | array  | One or two script-type group entries (`"ModuleScripts"` and/or `"Scripts"`). |

#### Script-type group entry

| Key        | Type   | Description                                        |
| ---------- | ------ | -------------------------------------------------- |
| `Name`     | string | Either `"ModuleScripts"` or `"Scripts"`.           |
| `Size`     | number | Sum of memory for scripts in this group, in bytes. |
| `Children` | array  | Array of individual script entries.                |

#### Script entry (leaf)

| Key    | Type   | Description                                                            |
| ------ | ------ | ---------------------------------------------------------------------- |
| `Name` | string | Dotted path to the script (e.g. `"ServerScriptService.Shared.Utils"`). |
| `Size` | number | Heap memory used by this script, in bytes.                             |

#### Example

```lua
{
  Name = "ScriptMemory",
  Size = 8388608,
  Children = {
    { Name = "ServerScriptService", Size = 524288, Children = {
        { Name = "ModuleScripts", Size = 409600, Children = {
            { Name = "ServerScriptService.Shared.Utils", Size = 204800 },
            { Name = "ServerScriptService.Shared.Config", Size = 204800 },
        }},
        { Name = "Scripts", Size = 114688, Children = {
            { Name = "ServerScriptService.MainScript", Size = 114688 },
        }},
    }},
    { Name = "ReplicatedStorage", Size = 262144, Children = {
        { Name = "ModuleScripts", Size = 262144, Children = {
            { Name = "ReplicatedStorage.SharedModule", Size = 262144 },
        }},
    }},
  }
}
```

*Yields · Security: None · Thread Safety: Unsafe*

**Returns:** `ScriptMemoryResult` — A dictionary tree of per-script Luau VM heap memory grouped by service
and script type.

### Method: SceneAnalysisService:GetTriangleCompositionAsync

**Signature:** `SceneAnalysisService:GetTriangleCompositionAsync(): TriangleCompositionResult`

Returns triangle and draw call counts by render pass, sourced from
`StatsService` performance data. Unlike other queries, this uses a `Sizes`
dictionary (with `Triangles` and `Drawcalls` keys) instead of a single
`Size` field. Render pass entries with zero triangles and zero draw calls
are omitted.

#### Root dictionary

| Key        | Type       | Description                                                            |
| ---------- | ---------- | ---------------------------------------------------------------------- |
| `Name`     | string     | Always `"TriangleComposition"`.                                        |
| `Sizes`    | dictionary | `{ Triangles: number, Drawcalls: number }` — totals across all passes. |
| `Children` | array      | Array of render pass entries.                                          |

#### Render pass entry (leaf)

| Key     | Type       | Description                                               |
| ------- | ---------- | --------------------------------------------------------- |
| `Name`  | string     | Render pass type (see table below).                       |
| `Sizes` | dictionary | `{ Triangles: number, Drawcalls: number }` for this pass. |

#### Render pass types

| Name               | Description                    |
| ------------------ | ------------------------------ |
| Opaque             | Opaque geometry                |
| Transparent        | Transparent geometry           |
| Terrain            | Voxel/smooth terrain           |
| Grass              | Terrain grass decoration       |
| UI                 | Screen-space UI                |
| Decal              | Decal rendering                |
| Cloud              | Volumetric clouds              |
| GenericPostProcess | Generic post-processing        |
| SSAO               | Screen-space ambient occlusion |
| DOF                | Depth of field                 |
| Particles          | Particle systems               |
| Sky                | Skybox                         |
| Shadows            | Shadow map rendering           |
| Undefined          | Uncategorized                  |

#### Example

```lua
{
  Name = "TriangleComposition",
  Sizes = { Triangles = 245000, Drawcalls = 1200 },
  Children = {
    { Name = "Opaque",      Sizes = { Triangles = 180000, Drawcalls = 800 } },
    { Name = "Transparent", Sizes = { Triangles = 25000,  Drawcalls = 150 } },
    { Name = "Shadows",     Sizes = { Triangles = 30000,  Drawcalls = 200 } },
    { Name = "UI",          Sizes = { Triangles = 10000,  Drawcalls = 50  } },
  }
}
```

*Yields · Security: None · Thread Safety: Unsafe*

**Returns:** `TriangleCompositionResult` — A dictionary tree of triangle and draw call counts broken down by
render pass type.

### Method: SceneAnalysisService:GetUnparentedInstancesAsync

**Signature:** `SceneAnalysisService:GetUnparentedInstancesAsync(): UnparentedInstancesResult`

Returns instances held by Luau but no longer in the data model, grouped by
host script. Each unparented instance is traced back to the script that
holds the reference.

Unparented instances that are flagged for garbage collection but not yet
deleted are temporarily shown with a parent of `Unknown`. This is a side
effect of how garbage collection is intended to work and not indicative of
any problems.

#### Root dictionary

| Key        | Type   | Description                          |
| ---------- | ------ | ------------------------------------ |
| `Name`     | string | Always `"UnparentedInstances"`.      |
| `Size`     | number | Total count of unparented instances. |
| `Children` | array  | Array of host script entries.        |

#### Host script entry

| Key        | Type   | Description                                                                                 |
| ---------- | ------ | ------------------------------------------------------------------------------------------- |
| `Name`     | string | Script path (e.g. `"ServerScriptService.Gameplay.Combat"`) or `"(unknown)"` if untraceable. |
| `Size`     | number | Count of unparented instances held by this script.                                          |
| `Children` | array  | Array of class entries.                                                                     |

#### Class entry (leaf)

| Key    | Type   | Description                                                                  |
| ------ | ------ | ---------------------------------------------------------------------------- |
| `Name` | string | Class name of the unparented instance (e.g. `"Part"`, `"Frame"`, `"Sound"`). |
| `Size` | number | Count of unparented instances of this class from this host script.           |

#### Example

```lua
{
  Name = "UnparentedInstances",
  Size = 47,
  Children = {
    { Name = "ServerScriptService.Gameplay.Combat", Size = 30, Children = {
        { Name = "Part", Size = 22 },
        { Name = "Attachment", Size = 8 },
    }},
    { Name = "(unknown)", Size = 17, Children = {
        { Name = "Frame", Size = 12 },
        { Name = "Sound", Size = 5 },
    }},
  }
}
```

*Yields · Security: None · Thread Safety: Unsafe*

**Returns:** `UnparentedInstancesResult` — A dictionary tree of unparented instances grouped by the host script
holding the reference.

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