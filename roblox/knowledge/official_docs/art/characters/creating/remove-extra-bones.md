---
title: "Remove extra bones"
url: /docs/en-us/art/characters/creating/remove-extra-bones
last_updated: 2026-10-30T19:55:33Z
description: "When creating characters in Blender, you must remove the extra head bones included in the template."
---

# Remove extra bones

The helper bones used to help place the head geometries also require removal to validate correctly. While these extra bones do not include any skinning data, do not delete any of the facial animation bones parented within DynamicHead, as these include important skinning data that drives facial animation.

> **Error:** Failure to [combine head geometry](/docs/en-us/art/characters/creating/combine-head-geometry.md) and remove head bones will cause issues with validation, as the character will no longer adhere to the standard [geometry](/docs/en-us/avatar/character-bodies/specifications.md#body-parts) and [joint hierarchy](/docs/en-us/avatar/character-bodies/specifications.md#rigging).

Remove the additional head bones by selecting them and deleting them in edit mode:

1. If required for your template, toggle visibility on your **Armature** object. The bones display in the viewport.
2. In the Outliner, expand the character's armature object and find the **Joints** object that parents the bone structure of the character.
3. Expand the **Joints** object's hierarchy by holding `Shift` and clicking the expansion dropdown.
4. In the viewport, select any bone and switch to **Edit** mode.
5. Under the `Head` joint, hold `Shift` and select all the head child joints except `DynamicHead`.
6. With the extra head bones selected, right-click in the viewport and select **Delete Selected Bones** from the contextual menu.
