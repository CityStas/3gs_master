---
title: "Optimize your game"
url: /docs/en-us/tutorials/curriculums/environmental-art/optimize-your-experience
last_updated: 2026-10-30T19:55:59Z
description: "Explains how to configure your assets and Studio settings to improve frame rate and performance levels."
---

# Optimize your game

**Optimizing your game** is the process of configuring your assets and Studio settings to keep your frame rate and performance levels high for devices with memory and graphics processing unit (GPU) limitations. This process ensures that nearly every user has the same gameplay and visual experience while they're viewing your environment.

Using the [Environment Art - Optimizing](https://www.roblox.com/games/14447845297/Environment-Art-Optimizing) `.rbxl` file as a reference, this section of the environmental art curriculum shows you how to review and configure your place file for optimal graphics, including guidance on:

- Reviewing the physics and rendering parameters of each asset to confirm they preserve memory and engine performance.
- Culling excess texture, geometry, or transparencies that unnecessarily increase the amount of calculations the Roblox Engine must perform to render your assets.

While the Roblox Engine handles most optimization work for you, you can assist in these optimization efforts by utilizing the [Microprofiler](/docs/en-us/performance-optimization/microprofiler.md) to see where it takes more time to render specific frames. Using this information, you can make informed decisions about what assets need your attention in regards to their parameters or excess content. [Scene Analysis](/docs/en-us/performance-optimization/scene-analysis.md) is another powerful tool for checking resource usage.

## Review physics and render parameters

In [Assemble an asset library](/docs/en-us/tutorials/curriculums/environmental-art/assemble-an-asset-library.md), you learned how important it is to set physics and rendering parameters that allow your assets to retain their high visual quality across devices with memory and GPU limitations. However, it's common as you construct your environment to adjust these parameters according to an asset's contextual position and purpose within your game. For example, much of the foliage in the final sample laser tag environment casts shadows despite a performance cost because it adds to the realism of the environment.

When you modify physics and rendering parameters, it's useful near the end of the development process to review all parameters to see where you can optimize a parameter while maintaining aesthetic goals and gameplay requirements. To illustrate, you can disable `Class.BasePart.CastShadow` property for the foliage near the edges of the gameplay area to save on performance without interfering with a user's gameplay or visual experience.

![An outdoor view of the sample laser tag game that casts shadows.](../../../assets/tutorials/environmental-art-curriculum/Section5/ReviewingParameters-Disabled.jpg)_`Class.BasePart.CastShadow` = Disabled_

![An outdoor view of the sample laser tag game that doesn't cast shadows. There is almost no difference in this view, but it improves performance.](../../../assets/tutorials/environmental-art-curriculum/Section5/ReviewingParameters-Enabled.jpg)_`Class.BasePart.CastShadow` = Enabled_

## Cull nonessential content

After you review your physics and rendering parameters, you can review the assets themselves to see where you can cull any nonessential content from the game that doesn't affect your gameplay, such as identical textures with different asset IDs, complex geometry with many vertices, or transparencies that layer on top of each other depending on the camera view. The following sections detail what you can do to review this content, and why it helps optimization efforts.

### Remove duplicate textures

As you transition between developing your assets and constructing your environment, it's common to iterate over meshes or textures as you find what's necessary for your aesthetic goals or gameplay requirements. If you don't convert your assets into [packages](/docs/en-us/projects/assets/packages.md), when you import these iterations into Studio, you're making unique asset IDs that the Roblox Engine needs to reference as it renders your assets within the environment.

For example, if you were to import the following two fire hydrant meshes into Studio separately, even if they are exactly the same in appearance, the Roblox Engine treats them as two objects with unique asset IDs. The more unique calls the engine needs to make, the more of an impact on memory and performance. For this reason, it's important to confirm when you're reusing an asset multiple times, each instance of that asset uses the same asset ID so that the engine only needs to make a single call to render it repeatedly.

![Two of the exact same fire hydrant with unique asset IDs. There is no visual difference but the duplicate asset IDs negatively impacts performance.](../../../assets/tutorials/environmental-art-curriculum/Section5/RemovingTextures-Firehydrants.jpg) ### Optimize geometry

If you find that you need to make more adjustments to increase frame rate across devices, it's useful to see where you can optimize your geometry by either:

- Combining groups of meshes into a single asset.
- Decreasing the polygon count of assets with geometric complexity.

Expanding on this first technique, every unique asset in your game represents a draw call on the GPU in which it sends a signal to the GPU to call information in order for the Roblox Engine to render the asset correctly. The more unique assets you have, the more draw calls the system needs to make. For this reason, if you have a group of meshes that make up a larger component in your game, you can group them together in third-party modeling tools to reduce the need for multiple draw calls.

To illustrate this point, the final sample laser tag environment parents multiple parts and meshes together to create the large towers outside of the building. If you were to combine all of these individual components together, you could make it a single asset with only one asset ID, and reduce the number of draw calls from 8 to 1. However, it's important to note that this technique removes your ability to freely change the visual and physical characteristics of each component, such as its position or material.

For example, in the following image, the left tower remains multiple assets under a `Class.Model` object, and the right tower is a single asset. You can modify each component of the left tower individually, but when you modify the right tower, such as changing its color to black, it affects the entirety of the object. This is why it's important to only consider this technique near the end of your environment's development when you know where you can improve performance without affecting your aesthetic goals.

![A front view of the two towers. The tower on the left includes multiple assets under a single model, while the tower on the right decreases the amount of assets by removing all texture objects.](../../../assets/tutorials/environmental-art-curriculum/Section5/OptimizingGeo-Towers.jpg)

Expanding on the second technique, assets with geometric complexity have more polygons, meaning they have more vertices that the engine needs to calculate as it renders their visual appearance. This means that assets with less complexity and fidelity are less costly to render, leading to an improvement in both performance and memory.

> **Warning:** If you choose to utilize this second technique, after you simplify your geometry in third-party tooling, it's important to remember to update your packages with the new import instead of creating a new asset ID, otherwise the Roblox Engine needs to make two separate calls for each asset ID.
### Delete layered transparencies

To provide a sense of realism to the environment, the final sample laser tag environment includes many meshes with varying levels of transparency, such as the foliage in the outdoor space, glass on the futuristic signage or planter railing. When the camera views multiple semi-transparent objects that are in front or behind each other, the Roblox Engine must render the overlapping pixels multiple times to account for the transparent areas. This process is called high transparency overdraw, and it comes at a significant impact to performance.

For example, consider the following view of a planter in the sample environment. The engine must render the transparent areas of the leaves between the plant closest to the camera to the plant closest to the outdoor area in layers, equating to hundreds of thousands of overdrawn pixels. To alleviate some of this impact, it's important to review the layout of all semi-transparent objects in your environment, and ensure there aren't too many places where there are many layers of overlap, especially in large areas of the screen.

![A Rthro avatar facing a planter with multiple plants with transparency between the leaves.](../../../assets/tutorials/environmental-art-curriculum/Section5/LayeredTransparencies-Left.jpg)

![A side view of the Rthro avatar facing a planter with multiple plants with transparency between the leaves, and example layers of overdrawn pixels are highlighted to show where there is overdrawn in the environment.](../../../assets/tutorials/environmental-art-curriculum/Section5/LayeredTransparencies-Right.jpg)

When you finish reviewing all of your content to ensure it's optimal across devices, your game is now ready for publication!

> **Info:** We're interested in hearing from you about your experience following the Environmental Art Curriculum. If you have any questions, concerns, or additional feedback on the process, please comment on our [Environmental Art Curriculum Q&A](https://devforum.roblox.com/t/feedback-on-environmental-art-curriculum/2592218).
