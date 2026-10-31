---
title: "Connect the beam"
url: /docs/en-us/education/build-it-play-it-mansion-of-wonder/connect-the-beam
last_updated: 2026-10-30T19:55:41Z
description: "Learn how to connect a beam effect in Roblox Studio, and to configure its properties to customize it to your game's needs. Part of the Build It Play It Mansion of Wonders series."
---

# Connect the beam

Now that you've made the attachments, it's time to connect them to the beam so that a texture can be shown.

1. Under **TestPlayer**, select the **TutorialBeam**. In the **Properties** window, find **Attachment0**. Click the empty box to the right of the property. Then, in the **Explorer** window, find **TestPlayer** and click on **PlayerAttachment**.
2. In the **TutorialBeam** properties, set **Attachment1** to the attachment you created in **GoalPart1**, the **GoalAttachment**.

## Adjust the beam

By default, a beam doesn't always face the camera. This may lead to situations where players are unable to see a beam from different angles. This can be fixed by turning on a property called **FaceCamera**.

_FaceCamera Off_

_FaceCamera On_

1. Make the beam visible at any position by going into the beam's properties and enabling **FaceCamera**. Once finished, you should see a white beam between the player and goal, regardless of camera angle.

## Make the tutorial arrows

The image displayed along the beam can be customized by changing its 2D texture. In addition, beams have a variety of visual options, such as texture, color, motion that can be modified.

1. To stream arrows along the beam like in the example, copy `5886559421` and paste it into the beam's **Texture** property.
  > **Info:** Custom textures can be any image that you have. Learn how to upload them in the [Asset Manager](/docs/en-us/projects/assets/manager.md) article.
2. Right now, the arrow's texture is stretched. Set **TextureMode** to **Static** to make the arrow repeat at its original size.
  > **Warning:** If the arrow doesn't point the correct direction, attachments may be swapped. Make sure that Attachment0 connects to PlayerAttachment and Attachment1 to GoalAttachment. Alternatively, if you're using a custom texture, you may need to mirror the image in a photo-editing program.
3. Modify beam properties like **Color**, **LightEmission**, and **TextureSpeed** to design something that feels eye-catching and appealing. Below is just one example.

### Tips for color choices

**Color** is one opportunity for improving a first time user experience. For example, contrasting or saturated colors get more attention, making it easier to inform players where to look on their screen.

Additionally, as you design, consider [accessibility](/docs/en-us/production/publishing/accessibility.md) for your players. Some players may struggle to see certain color combinations, making it important that colors appeal to the broadest audience.
