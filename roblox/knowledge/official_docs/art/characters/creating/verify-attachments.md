---
title: "Verify attachment placement"
url: /docs/en-us/art/characters/creating/verify-attachments
last_updated: 2026-10-30T19:55:33Z
description: "When creating characters in Blender, the character model requires minor attachment adjustments to be Studio-ready."
---

# Verify attachment placement

Attachment points are non-rendered objects of your avatar where rigid accessories attach to. Each template includes the required attachments at their expected locations ending with **_Att**. Before exporting, it's important to verify the attachment position and, if necessary, adjust the location if you made any changes to the shape of your model.

_Original template attachment positions_

_Attachments after adjustment_

Center attachment points at their respective locations. Each attachment should overlap approximately halfway with the character's mesh.

This tutorial only changes the head of your model, so you only need to adjust the **Hat**, **Hair** and **FaceFront** attachments. To enable visibility and verify your head attachment point:

1. If you haven't already, enable [disabled objects](/docs/en-us/art/characters/creating.md#disabled-objects) in your Outliner.
2. In the Outliner, find the `Joints` parent object.
3. Hold `Shift` and click the **Hide** icon for the `Joints` object to hide everything.
4. Expand the `Joints` object's hierarchy and unhide `Head_Geo`, `Hat_Att`, `Hair_Att`, and `FaceFront_Att`.
  1. If required, disable **Disable In Viewport** next to the _Att objects.
5. In the viewport, verify the placement of the attachments. The goblin's head is shorter than the starting template, so the attachments require minor vertical adjustment.
6. Select the attachments, then switch to **Edit** mode.
7. Using the **Grab** tool, position the attachments vertically along the y-axis until they are about halfway embedded in the head.
