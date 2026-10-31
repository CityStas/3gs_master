---
title: "Combine head geometry"
url: /docs/en-us/art/characters/creating/combine-head-geometry
last_updated: 2026-10-30T19:55:33Z
description: "When creating characters in Blender, you must combine the head geometry to a single object."
---

# Combine head geometry

Whenever you are ready to export your model, it's important to clean up your project to ensure that your model is ready to export. This includes the following tasks that ensure the customized template model and all of the avatar components can import into Studio successfully:

- Combining extra head geometry
- Removing extra head bones
- Verifying attachment points
- Final technical checks

> **Error:** Failure to combine head geometry and [remove head bones](/docs/en-us/art/characters/creating/remove-extra-bones.md) will cause issues with validation, as the character will no longer adhere to the expected standard [geometry](/docs/en-us/avatar/character-bodies/specifications.md#body-parts) and [joint hierarchy](/docs/en-us/avatar/character-bodies/specifications.md#rigging).
## Combine head geometry

At this point, you should also combine the separate head and face objects within the single `Head_Geo` object. Some templates don't include some face objects, like lashes. To combine the head and face meshes:

1. In the Outliner, hold `Ctrl`/`⌘` and click the following objects, ending with the `Head_Geo`:
  - `UpperTeeth_Geo`
  - `LowerTeeth_Geo`
  - `Tongue_Geo`
  - `RightLash_Geo`
  - `RightEye_Geo`
  - `LeftLash_Geo`
  - `LeftEye_Geo`
  - `Head_Geo`
  > **Error:** When selecting multiple head objects, make sure that the `Head_Geo` is highlighted as yellow, indicating it as the main object that the others merge into. This correctly preserves the custom properties stored in the head mesh. You can achieve this by selecting the head last in the Outliner.
2. While in **Object** mode, right-click in the viewport and select **Join** from the contextual menu. The objects combine as a single `Head_Geo` object.
