---
name: unity-assets
description: "Producing and importing art for Unity: the local asset pipeline (asset_image / asset_character / asset_to_3d / asset_generate_pack), where output lands (Assets/Generated/), import settings for sprites and normal maps, glTFast for GLB, generated meshes that are too dense, forward-axis and scale fixes, materials and URP shaders. Use whenever a Unity project needs a texture, sprite, model or material. Русские триггеры: «нужен ассет», «сгенерируй арт», «текстура», «модель», «спрайт», «импорт glb», «материал»."
---

# Assets for Unity

## Local generation first

`ASSET-POLICY.md` applies to Unity exactly as to Three.js and Godot: **generate locally first**,
web assets are a second tier with a recorded license. The `asset_*` tools drive the local
ComfyUI pipeline; the `assets` MCP server is registered for Unity with
`THREE_PROJECT_ASSET_ROOT=Assets/Generated`, so output lands in:

```
<project>/Assets/Generated/images/<name>.png
<project>/Assets/Generated/masks/<name>-nobg.png
<project>/Assets/Generated/3d/<name>.glb
```

One call for the whole pack (`asset_generate_pack`), never one call per asset — each call pays a
ComfyUI start/stop and a 9B model reload on an 8 GB card.

## Import rules that decide how it looks

| File | Default | What you want |
|---|---|---|
| PNG as a sprite | `Default` or `Sprite` depending on the template | **Sprite (2D and UI)**, `spritePixelsPerUnit` set to the intended world size |
| alpha PNG | alpha kept, not premultiplied | `Alpha Is Transparency` on for a cut-out |
| normal map | imported as colour | **Texture Type = Normal map**, sRGB **off** |
| GLB | **not imported at all** | install `com.unity.cloud.gltfast` (see below) |
| GLB without `NORMAL` | renders **black** | `mesh.RecalculateNormals()` |

`spritePixelsPerUnit` is the size knob: 512 px at 100 PPU is 5.12 world units. "The art came out
enormous" is this number, not the generator.

## GLB needs a package

Unity has no built-in glTF importer. `Packages/manifest.json`:

```json
"com.unity.cloud.gltfast": "6.6.0"
```

then **delete `Packages/packages-lock.json`**. Check available versions first:
`curl -s https://packages.unity.com/com.unity.cloud.gltfast | jq '.["dist-tags"]'`.
Exporting **FBX** from Blender avoids the package entirely and is the lower-risk path.

## Generated meshes are too dense

The pipeline's default is ~700 000 faces per model; a game prop wants 5 000–20 000. Cap it at
generation time with `faces_3d` in the pack job (`faces_3d` is the real speed/size lever;
`resolution_3d` is a no-op for this). A 3 M-triangle model instanced a few times will not hold
frame rate.

## Two silent visual bugs

1. **Forward axis.** The model's forward is whatever the generator produced; Unity expects `+Z`.
   Symptom: the character rotates correctly but walks sideways. Fix on the model child (not the
   root the controller rotates):
   ```csharp
   const float ModelYawOffset = 90f;
   model.transform.localRotation = Quaternion.Euler(0f, ModelYawOffset, 0f);
   ```
   Find the offset by looking from `-Z` and `+Z` with `root.rotation = identity` — the face tells
   you. `localBounds` swapping X and Z confirms it applied.
2. **Scale.** A generated GLB has no agreed scale. Set `localScale` against the character height
   (1.6–1.8 units), not by eye.

## No rig, no clips

Image→3D gives a **static mesh** (`skins: 0`, `animations: 0`). An `Animator` on it plays
nothing. Animate the transform procedurally (bob, lean, squash) or rig it in Blender.

## Materials and shaders

- URP vs Built-in vs HDRP are not interchangeable: a Built-in `Standard` material on a URP
  project is **magenta**. Property names differ too — `_BaseColor` (URP) vs `_Color` (Built-in),
  `_BaseMap` vs `_MainTex`.
- `Shader.Find("Universal Render Pipeline/Lit")` for a URP material; a material created in a
  batch run must be saved with `AssetDatabase.CreateAsset` or it dies with the process.
- Shader Graph is a node graph and cannot be authored from C#; a code shader goes under
  `Assets/Shaders/` as ShaderLab/HLSL.

## Full recipes

- `unity_rag_search("generated art into unity")` — the end-to-end path with the importer script.
- `unity_rag_search("import glb from blender")` — glTFast, normals, axis.
- `unity_rag_search("urp materials shaders")` — property names and pipeline rules.
