---
title: "SLIM"
url: /docs/en-us/workspace/streaming/slim
last_updated: 2026-10-30T19:56:03Z
description: "SLIM (Scalable Lightweight Interactive Models) automatically generates optimized, cloud-transcoded representations of models and avatars for improved performance and visual quality."
---

# SLIM

**SLIM** (Scalable Lightweight Interactive Models) is an automatic optimization system that generates lightweight, optimized representations of `Class.Model|Models` and platform avatars using cloud-based transcoding (converting assets into more efficient formats). When enabled, SLIM combines multiple parts into fewer draw calls (rendering commands sent to the GPU) and generates multiple levels of detail, allowing the engine to intelligently select the best representation based on distance, device capability, and available resources.

_Without SLIM — streamed-out models are invisible_

_With SLIM — optimized stand-ins remain visible_

SLIM provides three key benefits:

- **Visual quality** — Distant models appear more detailed than the legacy model level‑of‑detail system, maintaining closer fidelity to the original.
- **Consistent transitions** — All parts within a model switch detail levels simultaneously, eliminating jarring per-part transitions.
- **Performance** — Composite meshes dramatically reduce draw calls, triangle counts, and memory usage, enabling richer scenes across all device tiers.

Explore SLIM in these published games:

_[**City People Cars SLIM Template**](https://www.roblox.com/games/135885449743134/CPC-Slim-Template) — World models with SLIM enabled_

_[**SLIM Platform Avatars**](https://www.roblox.com/games/81704282913046/SLIM-Platform-Avatars) — 200 animated avatars rendered with SLIM_

## Prerequisites

SLIM requires the following:

1. `Class.Workspace.StreamingEnabled|StreamingEnabled` must be enabled on the `Class.Workspace` object. See also [streaming properties](/docs/en-us/workspace/streaming/techniques.md#streaming-properties) for related recommended settings.
2. The place must be **saved to Roblox** (not a local `.rbxl` file), as SLIM uses cloud transcoding to generate optimized assets. If you're testing locally, publish the place and then enable SLIM.
3. [Team Create](/docs/en-us/projects/collaboration.md) must be enabled for the game, as SLIM relies on associated properties for cloud asset generation.

## Technical behavior

When you publish or playtest a game with SLIM-enabled models, the engine uploads model data to a cloud service that generates optimized composite meshes with multiple levels of detail. At runtime, clients fetch these assets from the CDN and the engine selects the appropriate detail level based on distance and device capability, classifying each SLIM model into rendering zones based on distance from the camera:

![Diagram showing the four SLIM rendering zones, colored sky blue, teal, yellow, and vermilion, radiating from a player character.](../../assets/optimization/streaming/SLIM-Zones.jpg)

| Range | Data Model State | Rendering |
| --- | --- | --- |
| `rgb(86,180,233)` | Full instances streamed in. | Traditional part-by-part rendering. |
| `rgb(0,158,115)` | Full instances streamed in. | The engine renders the SLIM composite when more efficient. |
| `rgb(240,228,66)` | Instances streamed out. Only a minimal placeholder exists in the `Class.DataModel`, not the full model hierarchy. | SLIM composite rendering. |
| `rgb(213,94,0)` | Minimal placeholder in the `Class.DataModel`. | Not rendered. |

## SLIM for models

SLIM works best on models that represent **static world geometry** — buildings, props, vehicles, terrain features, and other environment objects that don't change at/during runtime. Adding or removing parts, changing materials, or modifying geometry at runtime prevents SLIM from rendering the model correctly. See [model structure](/docs/en-us/workspace/streaming/techniques.md#model-structure) for general model structure guidance and [limitations](#limitations) for the full list of exclusions.

To enable SLIM on a model, set its `Class.Model.LevelOfDetail|LevelOfDetail` property to `Enum.ModelLevelOfDetail.SLIM|SLIM` in the [Properties](/docs/en-us/studio/properties.md) window.

![The Properties window with the LevelOfDetail property set to SLIM.](../../assets/studio/properties/Model-LevelOfDetail-SLIM.png)

When SLIM is set on a model, the engine:

1. Serializes the model's rendering-relevant properties (geometry, materials, textures, transforms) into a compact representation. Supported instance types within the model include `Class.Part`, `Class.MeshPart`, `Class.Decal`, `Class.Texture`, `Class.SurfaceAppearance`, `Class.PartOperation`, `Class.NegateOperation`, and `Class.SpecialMesh`.
2. Uploads this data to the cloud transcoding service on first publish or play.
3. The cloud service generates a composited mesh with multiple levels of detail, removing hidden internal geometry and optimizing textures.
4. At runtime, clients fetch the optimized SLIM asset and render it when the engine streams out the original model or when SLIM is more efficient than the full model.

> **Info:** Initial SLIM generation might take a few moments for complex models. The cloud service processes assets in the background, so if a model doesn't appear as SLIM immediately after enabling, wait 1–2 minutes and rejoin; the transcoded asset persists on the CDN and the client fetches it on the next session.

** Converting from Streaming Mesh**

If your game uses the legacy `Enum.ModelLevelOfDetail.StreamingMesh|StreamingMesh` setting for `Class.Model.LevelOfDetail`, you can convert individual models by selecting them and changing the property in the [Properties](/docs/en-us/studio/properties.md) window, or you can batch-convert multiple models at once using a script like the following in the [Command Bar](/docs/en-us/studio/overview.md#command-bar). Note that some models which worked with `Enum.ModelLevelOfDetail.StreamingMesh|StreamingMesh` might need adjustments for SLIM, particularly those with overlapping parts or complex `Class.PartOperation` hierarchies.

```lua
for _, descendant in workspace:GetDescendants() do
    if descendant:IsA("Model") and descendant.LevelOfDetail ==
        Enum.ModelLevelOfDetail.StreamingMesh then
        descendant.LevelOfDetail = Enum.ModelLevelOfDetail.SLIM
    end
end
```

## SLIM for avatars

Platform avatars outside of the currently streamed area are not visible by default. Enabling SLIM avatars renders [standard](/docs/en-us/avatar/character-bodies/specifications.md) player characters — regardless of how many accessories or clothing layers they have — as lightweight, animated stand‑ins that maintain visual fidelity at a fraction of the rendering cost.

#### Audience in Far Distance

> **Success:** **SLIM Enabled****~170,000 triangles****~4,000 client instances**

> **Error:** **SLIM Disabled****~2,600,000 triangles****~60,000 client instances**

#### Audience in Near Proximity

> **Success:** **SLIM Enabled****~100,000 triangles****~31,000 client instances**

> **Error:** **SLIM Disabled****~670,000 triangles****~60,000 client instances**

The key SLIM-specific property for avatars is `Class.Workspace.EnableSLIMAvatars` which should be set to `Enum.RolloutState.Enabled|Enabled` in the **Properties** window, alongside `Class.Model.LevelOfDetail|LevelOfDetail` set to `Enum.ModelLevelOfDetail.SLIM|SLIM` on your non‑avatar world models.

![The Properties window with the EnableSLIMAvatars property set to Enabled.](../../assets/studio/properties/Workspace-EnableSLIMAvatars.png)

With `Class.Workspace.EnableSLIMAvatars|EnableSLIMAvatars` enabled, the engine:

- Renders a SLIM version when an actual avatar model streams out.
- Swaps between SLIM and full-resolution representations based on available resources, even inside the streaming radius.
- Throttles SLIM animations based on scene importance and available bandwidth.

> **Success:** **Supported Avatars**- R15 avatars with a body, dynamic head, [standard](/docs/en-us/avatar/character-bodies/specifications.md#standard-r15-rigs) or [advanced](/docs/en-us/avatar/character-bodies/specifications.md#advanced-r15-rigs) R15 rig, and rigid/layered accessories. - Avatar changes made between the `Class.Player.CharacterAdded|CharacterAdded` event and `Class.Player.CharacterAppearanceLoaded|CharacterAppearanceLoaded` event. - Avatars defined by `StarterHumanoid` or `StarterCharacter` under the `Class.StarterPlayer` service.
> **Error:** **Excluded Avatars**- R6 avatars. - NPC characters (even those with a standard or advanced R15 rig). - Avatars with custom proportions, body scaling, or experience-applied avatar settings. - Avatar changes made after the `Class.Player.CharacterAppearanceLoaded|CharacterAppearanceLoaded` event (equipping tools, accessory changes, `Class.Highlight` additions, etc.). - Avatar changes made by `Class.StarterCharacterScripts`.

** Testing SLIM Avatars**

Unlike [model SLIM](#slim-for-models) which you can test alone by moving far from a model until it streams out, SLIM avatars require multiple players in the game to observe. Use one of these [testing modes](/docs/en-us/studio/testing-modes.md) to test SLIM avatars:

- [Team Test](/docs/en-us/studio/testing-modes.md#collaborative-testing) — Join with friends or alternate accounts to see SLIM avatars at distance.
- [Server and Clients](/docs/en-us/studio/testing-modes.md#multi-client-simulation) — Launch two or more client windows where each client displays avatar copies that the others render as SLIM when at distance.

Note that avatars must have been transcoded in a SLIM-enabled game before they appear as SLIM. If avatars don't render as SLIM in your first test, rejoin the game after a moment to allow transcoding to complete.

## Limitations

| Limitation | Details |
| --- | --- |
| **Streaming required** | SLIM only functions with `Class.Workspace.StreamingEnabled\|StreamingEnabled` set to `true`. Without streaming, SLIM‑eligible models fall back to traditional level‑of‑detail rendering. |
| **Static models only** | [Model SLIM](#slim-for-models) does not support models modified at runtime (parts added/removed, properties changed) or models that play animations. |
| **Humanoid instances** | The engine excludes models containing a `Class.Humanoid` from static [model SLIM](#slim-for-models) processing. Use [SLIM avatars](#slim-for-avatars) for animated player characters. |
| **Avatar restrictions** | [SLIM avatars](#slim-for-avatars) only support R15 player characters. R6 rigs, NPCs, and avatars with custom proportions fall back to default rendering. |
| **Cloud dependency** | The cloud service generates and stores SLIM assets on the CDN. Offline or local testing without a published place does not produce SLIM results. |
| **Zero-scale models** | The engine excludes models with a `Class.Model.Scale\|Scale` of `0` from SLIM processing. |
| **Platform availability** | On platforms where SLIM is not yet supported, models set to `Enum.ModelLevelOfDetail.SLIM\|SLIM` fall back to `Enum.ModelLevelOfDetail.Disabled\|Disabled`. |

## Debugging

To better understand the status of SLIM models, Roblox provides several **debug tint modes** in the **DebugVisualizations** ⟩ **SlimTintMode** dropdown of the [Developer Console](/docs/en-us/studio/developer-console.md). Note that this menu is only available to creators who have **Edit** permissions for the game.

There are multiple tint modes to select from. See `Enum.SlimTintMode` for the color mappings of each mode.

#### LOD

`Enum.SlimTintMode.LOD|LOD` colors each mesh by its current level of detail using a blue-to-red heatmap. Blue indicates the lowest detail and warmer colors indicate higher detail.

#### Data Model State

`Enum.SlimTintMode.DataModelState|DataModelState` colors meshes by streaming state of the `Class.DataModel`. Teal indicates the high-fidelity zone where the `Class.DataModel` is present; yellow indicates the low-fidelity zone where the `Class.DataModel` is absent.

You can also see SLIM debug visualizations in Studio by selecting a tint mode from the [Visualization Options](/docs/en-us/studio/overview.md#visualization-options) menu:

![A close up view of the 3D viewport with the Visualization Options button indicated in the upper-right corner.](../../assets/studio/general/Visualization-Options.png)

In addition to the `Enum.SlimTintMode.LOD|LOD`/`Enum.SlimTintMode.DataModelState|DataModelState` tint modes, Studio offers the `Enum.SlimTintMode.TranscoderStatus|TranscoderStatus` tint mode. While editing, only this tint mode is available in the visualization options menu; while playing, all the tint modes are available. See `Enum.SlimTranscoderStatus` for the color mappings of each status.

## Troubleshooting

** SLIM model not appearing**

- Verify that `Class.Workspace.StreamingEnabled|StreamingEnabled` is `true`.
- Confirm the place is published to Roblox and [Team Create](/docs/en-us/projects/collaboration.md) is enabled.
- Check that `Class.Model.LevelOfDetail|LevelOfDetail` is set to `Enum.ModelLevelOfDetail.SLIM|SLIM` for the model.
- Wait 1–2 minutes after first publish for cloud transcoding to complete, then rejoin.
- Ensure the model doesn't contain a `Class.Humanoid` instance.

** Solid modeling operations not rendering correctly in SLIM**

`Class.PartOperation` instances for [solid modeling](/docs/en-us/parts/solid-modeling.md) (unions, intersections, negations) might not render correctly in some SLIM models. If a union appears missing or distorted in the SLIM representation, try separating the affected `Class.PartOperation` into its own model or simplifying the CSG operation.

** Z-fighting or flickering on SLIM models**

Z-fighting can occur when parts in the original model have overlapping or coplanar faces. To resolve:

- Move overlapping parts slightly apart (even `0.01` studs is sufficient).
- Avoid perfectly flush surfaces between adjacent parts in the same model.

** Texture or UV shifts on SLIM models**

SLIM regenerates UV mappings (how textures are projected onto 3D surfaces) during transcoding. Default Roblox materials might show slightly different tiling patterns compared to the original. To mitigate:

- Use custom textures via `Class.SurfaceAppearance` for important surfaces.
- Group visually related parts into the same model to ensure consistent texturing.

** SLIM avatars not rendering**

- Verify `Class.Workspace.EnableSLIMAvatars` is set to `Enum.RolloutState.Enabled|Enabled`.
- Test with multiple clients using [Server and Clients](/docs/en-us/studio/testing-modes.md#multi-client-simulation) test mode (requires at least 2 clients).
- Ensure the avatar uses a [standard](/docs/en-us/avatar/character-bodies/specifications.md#standard-r15-rigs) or [advanced](/docs/en-us/avatar/character-bodies/specifications.md#advanced-r15-rigs) R15 rig without custom proportions.
- Confirm the game doesn't modify the avatar after the `Class.Player.CharacterAppearanceLoaded` event.

** Visual glitches on animated SLIM avatars**

Full-body or finger animations might occasionally show visual artifacts due to bone replication timing. This is a known issue being actively improved. If the issue is severe, verify that animation scripts aren't modifying bone transforms outside of the standard animation pipeline.

** Inaccurate triangle count in rendering stats**

The rendering stats panel might report incorrect triangle counts when SLIM avatars are enabled. This is a known reporting bug and does not affect actual rendering performance.
