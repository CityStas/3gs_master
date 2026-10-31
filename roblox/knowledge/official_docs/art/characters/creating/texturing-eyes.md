---
title: "Texturing eyes"
url: /docs/en-us/art/characters/creating/texturing-eyes
last_updated: 2026-10-30T19:55:33Z
description: "Use Blender's texture painting tools to apply a custom surface appearance on your character's eyes."
---

# Texturing eyes

You can apply a fully opaque texture to the eyes to achieve a more non-human visual effect for your character. Before editing the eye textures, join the two eye objects to texture them both at the same time. Then texture paint the entire eye, starting with the outer eye, moving to the inner eye, and finishing with the pupil.

To texture your eye mesh objects:

1. If you haven't already, [increase the texture image resolution](/docs/en-us/art/characters/creating/texturing-setup.md#set-texture-resolution).
2. In the Outliner, toggle the **Hide in Viewport** option for the `Head_Geo`, `LowerTeeth_Geo`, `Tongue_Geo`, and `UpperTeeth_Geo`. Leave the eye mesh objects visible.
3. In **Object** mode, hold `Shift` and click on both `LeftEye_Geo` and `RightEye_Geo`, then right-click and select **Join** (`Ctrl``J`; `⌘``J`) from the contextual menu to join the objects. The two objects merge using the name of the last object selected.
4. Switch to the **Texture Paint** tab, then with the **Draw** tool active, set the following brush settings in the tool sidebar for the outer eye shadow.
  1. In **Brush Settings**, set **Radius** to **50px** and **Strength** to **1.0**.
  2. In **Color Picker**, set **Color** to black.
5. Completely paint the eye objects black. This serves as the basis for the outer eye shadow.
6. With the **Draw** tool active, set the following brush settings in the tool sidebar for the outer eye color:
  1. In **Brush Settings**, set **Radius** to **75px** and **Strength** to **1.0**.
  2. In **Color Picker**, set **Color** to a deep yellow.
7. In the **Texture Paint** tab's 2D view window, line up your cursor to the center of the UV map that corresponds to the eye texture. Click 4-6 times on the center of each eye to create an outer eye color over the base shadow.
8. For visibility, enable `Head_Geo` visibility and reorient the camera to a front-facing view.
9. Paint the inner eye color using the following suggestions:
  1. Click the **X Symmetry** button to enable symmetry. Toggle this off if creating asymmetrical assets.
  2. In **Viewport Overlays** settings, enable **Wireframe geometry view**. You can toggle this overlay off when spot checking your visual elements.
  3. Update your brush settings in the tool sidebar for the inner eye:
    1. In **Brush Settings**, set **Radius** to **5px**. You can quickly change this radius as you paint by holding `F`.
    2. In **Color Picker**, set **Color** to red.
  4. Periodically make the head mesh visible to ensure your eye texture works with the rest of the model.
10. Update your brush settings in the tool sidebar for the pupils:
  1. In **Brush Settings**, set Radius to **5px**. You can quickly change this radius as you paint by holding `F`.
  2. In **Color Picker**, set **Color** to a bright red.
11. Using the **Brush** tool, paint the pupils of your model.
12. After completing your texture painting, switch back to **Edit** mode.
13. Hold `Shift`, click on both of your eye objects, press `P`, and select **By Loose Parts** from the contextual menu to separate the two meshes.
14. Rename your remaining mesh to the original `RightEye_Geo` or `LeftEye_Geo` name.
