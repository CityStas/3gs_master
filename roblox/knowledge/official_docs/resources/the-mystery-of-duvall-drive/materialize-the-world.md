---
title: "Materialize the world"
url: /docs/en-us/resources/the-mystery-of-duvall-drive/materialize-the-world
last_updated: 2026-10-30T19:55:56Z
description: "Explains the use of materials and textures in The Mystery of Duvall Drive."
---

# Materialize the world

We use [materials](/docs/en-us/parts/materials.md) and [surface appearance](/docs/en-us/art/modeling/surface-appearance.md) objects to create an immersive and realistic indoor and outdoor environment. Without materials, this scene could still have some interesting depth, silhouettes, and lighting, but with our materials and texture systems, we can really bring the room to life and add a dimension of realism to the world.

These [physically-based rendering](/docs/en-us/art/modeling/surface-appearance.md) (PBR) materials are what makes surfaces like wood look, react, and reflect the way wood does in the real world. In this section, we will go over some of the decisions and processes we went through to create the palette of materials used in the demo. As in the [Beyond the Dark](/docs/en-us/resources/beyond-the-dark.md) demo, we wanted a realistic look and feel for our materials and we achieved it through a few different approaches.

You can break down the process of building all our textures and materials into three areas:

- Surface appearance objects for 1:1 or unique materials for meshes, such as a marble statue.
- Surface appearance objects for shared trim maps for `Class.MeshPart|MeshParts`, such as repeatable wood trim details on furniture.
- [Material variants](/docs/en-us/parts/materials.md#custom-materials) for shared materials on Parts or terrain, such as flagstone replacing cobblestone for both fireplaces and ground.

## Plan, reuse, and budgets

When starting any project, give some thought about material art direction for consistency and reuse. Every platform and device has a limit on the amount of memory you can use for textures so some upfront planning goes a long way to help keep a handle on the number of textures in your game.

When considering the look and feel of the game, we deliberately chose to go with a craftsman style house to ensure we could reuse a handful of materials over a wide array of assets, from small picture frames and furniture to large architectural elements.

_Here are some of the reference images we collected for the Craftsman Style._

Distilled down to its basics, [American Craftsman](https://en.wikipedia.org/wiki/American_Craftsman) characteristics include simple, clean lines and natural wood tones, letting the wood and artistry of the carpenter take center stage. These characteristics allow us to use one set of wood trim texture maps for furniture and architectural elements in the house and also allow us to keep our models fairly low poly. With this in mind, we set out to create the trim map texture set you see below.

_Wood Trim Texture Set_

## Surface appearance and trim maps

Trim maps are simple repeatable textures that can be applied to a wide variety of assets. Trim maps do a lot of heavy lifting in games and fill the gap between completely tiling textures and creating a 1:1 texture set that you would get from painting an object in a program like [Substance Painter](https://www.adobe.com/products/substance3d-painter) or using [photogrammetry](/docs/en-us/resources/the-mystery-of-duvall-drive/construct-the-house.md#photogrammetry). The wood material shown previously was set up as a trim map which means that it could be reused on many different meshes, each mesh taking advantage of the same trim textures just by laying out its UVs creatively.

_Tiling Texture_

_Trim Texture_

_1-1 Texture_

When using trim map texture sets for use across a large variety of scales and objects, try to keep your textures fairly clean and free of details that would be easily recognizable as repeating.

_Example of too much detail_

_Cleaner textures work best_

For an example of over-detail, say we wanted to add some grime to our BaseColor map. Look how quickly you start to notice the unrealistic direction of textures and stretched UVs.

_Notice how the extra detail of stain on the furniture on the left stands out for repetition and incorrect direction compared to the cleaner set on the right._

If an asset really needs heavy staining, wear, and/or dirt buildup it would be better to use a 1:1 map unique for that specific mesh. For additional information on working with trim maps, see the [Create trim sheets](/docs/en-us/resources/beyond-the-dark/building-architecture.md#create-trim-sheets) section in the Beyond the Dark documentation.

You can package a single Surface Appearance node with these trim maps and apply the trim to all of the assets shown below.

_Just some of the many assets that used the same Wood Trim Surface Appearance Node._

Tinting is another way to make your Surface Appearance nodes and Material Variants go further. By adding an alpha mask to your `Class.SurfaceAppearance.ColorMap` and setting the `Class.SurfaceAppearance.AlphaMode` to **Overlay**, you can use `Datatype.BrickColor` or `Datatype.Color3` to tint your objects for visual variation.

_These 4 color variations are all utilizing the same Packaged Surface Appearance node._

Alpha masks, regardless of how they are created, are merged in your `Class.SurfaceAppearance.ColorMap`, changing it from a standard RGB texture to an RGBA. You can play around with values and levels in your alpha mask to get the desired level of tinting, but with a little finesse you can achieve some great results.

_BaseColor RGB_

In this leather example, we just blended the height map with some scratches and wear marks to create our alpha mask.

_Height Map_

_Scratches and wear marks_

These two maps were then sent to an Alpha Merge Node to create the final RGBA used in the Overlay Surface Appearance Node.

_Final Alpha texture. White pixels don't apply tint and only show the Base Color RGB map. Black pixels tint and only show the flat BrickColor/Color with a gradient in between the two._

_Example of the BaseColor and Alpha being merged via the Alpha Merge Node in Substance Designer._

_Examples of the RGBA in combination with Mesh Color on white, brown, red, and blue meshes._

_Same example only showing the ColorMap and Mesh Color._

## Texture sizes

Along with heavily reusing textures, you can apply other techniques to keep your texture memory usage down. You can reduce texture sizes based on usage. For example, you can often drop the resolution of your Surface Appearance object's `Class.SurfaceAppearance.ColorMap`, `Class.SurfaceAppearance.RoughnessMap`, and `Class.SurfaceAppearance.MetalnessMap` down by 1 or 2 times without losing any visual fidelity. Many times the `Class.SurfaceAppearance.MetalnessMap` can be left blank, which results in a pure black/non-metallic surface.

_This leather trim texture set consists of a normal map at 1024, a base color map at 512, a roughness map at 256, and no metalness map._

In [Substance Designer](https://www.adobe.com/products/substance3d-designer), the easiest way to resize outputs is to add a [Transformation 2D node](https://substance3d.adobe.com/documentation/sddoc/transformation-2d-172825332.html) just before your final output node and adjust the **Output Size** within the Base Parameters section for that node.

_Transform 2D Node with adjusted Output Size._

_Final Surface on couch meshes._

It generally takes several iterations of resizing the various maps in your texture set and visually inspecting the asset in Studio to get them to a spot where they hold up well enough across the variously sized assets. Using this process, you can settle on the smallest texture sizes you feel you can get away with without losing the visual quality needed for the art direction of your game.

With these few techniques you can keep your texture budget under control and still have a beautiful experience.

> **Warning:** When importing custom meshes into Studio, base textures included with your model may be imported with your mesh and automatically applied as a textureID. This can become a problem when importing multiple meshes with the same base texture applied. Each import can create a new version of the same texture map and bloat your texture memory.
>
> When a packaged Surface Appearance is applied for reuse, make sure to delete the textureID within the properties of the mesh to prevent this issue. This is a known behavior and Roblox is looking into improving this flow.
## Base materials

Since we used [parts](/docs/en-us/parts.md), [terrain](/docs/en-us/parts/terrain.md), and [meshes](/docs/en-us/parts/meshes.md) side-by-side in this demo we chose to utilize the default [built-in materials](/docs/en-us/parts/materials.md#asset-ids-for-built-in-materials), [Material Variants](/docs/en-us/parts/materials.md#custom-materials), and the newly released [Material Manager](/docs/en-us/parts/materials.md#material-manager) tool to ensure our various parts and terrain surfaces match the look and feel of our PBR-textured meshes.

Base materials are available for use as-is or to modify as a new variant. In many cases, the wood base materials serve us very well and only require adjusting the color to match our textured meshes.

_Example of a mesh in the foreground using a Surface Appearance node and CSG (constructive solid geometry) objects built in Studio with Parts and using the standard Wood material colored to match._

## Material variants

Since the game includes an outdoor environment during a downpour, we knew we wanted our ground to feel wet and muddy to match our stormy pacific northwest art direction. We accomplished this by creating a handful of new [Custom Materials](/docs/en-us/parts/materials.md#custom-materials) using [Material Variants](/docs/en-us/parts/materials.md#create-a-custom-material-in-the-explorer) that we could override the base materials with. We use them to paint down things like mulch, large and small gravel, mud, as well as a shallow puddled version of each.

Material Variants allow the user to redefine textures that are used for any given default material, adding a lot of opportunities to customize materials used in terrain and parts.

_Image of the backyard and use of wet Material Variants._

Material Variants are also used to create wet and dry versions of our materials. This is helpful for surfaces such as concrete and our flag stone hardscape that would be dry under cover of the porch roof and wet when exposed to the rain out in the yard.

Creating a Material Variant can be done inside the [Material Manager](/docs/en-us/parts/materials.md#material-manager). As the name suggests, the Material Manager also allows you to manage both default and material variants in one place.

Once the Material Manager is open you will click the Circle Plus button in the upper left of the window to edit and add a new Variant. When adding a name, it's a good idea to add a suffix of _MV after your name so you can easily pick out the new material variant from the default materials.

Choose a **Base Material** that most closely relates to your new material. You can think of the Base Material field as the **Physical Properties** of the material, which affects things like friction, density, weight, hit effects, and footstep sounds.

_Notice that the Metalness map was left blank since it was not needed._

Why create a Material Variant? Material Variants that override a Base Material inherit all properties of that material, except for the visuals. This means your material variant will inherit the physical behaviors of the default material, such as density. It also means future additions, like adding unique acoustics to concrete, will automatically be inherited. In this case, we want to create a new wet concrete variant that inherits nearly all the properties of the concrete material.

If the Base Material relates to the **Physical Properties** then the Texture Maps are our **Visual Properties**. **Texture Maps** tell the renderer how light should interact with the material through our PBR rendering pipeline. The Base Material field also defines what default material is overwritten with the new visual properties. In this case, we are proceeding to overwrite the **Concrete** base material.

Now that we have created our new "Concrete_Wet_MV" we need to override the default Concrete material with it so that we can use it in our scene. To do that just click on your new MV and click on the **Set Override** toggle.

_Notice that the default Concrete material changes to the new Concrete_Wet_MV when the Set Override is toggled._

> **Warning:** Material Variants can be applied on a per-part/meshpart basis, so you can make an unlimited amount of custom materials simultaneously used on parts. Terrain requires using overrides for customization, and you're limited to overriding the 22 built-in materials.

Now everything that uses Concrete in your scene will now be using the new override, including any concrete that you might have painted down on your terrain. The only exception to this is parts that have a specifically listed "material variant" on that object.

_Example of Material Variant Overrides being used on terrain and parts._

To allow our terrain to have a variety of surfaces, including both wet and with puddles, we ended up overriding about 10 of the default materials. This was necessary for the rain soaked look we were going for on our final terrain.

_Before Material Variant Override._

_After Material Variant Override._

Using all the material options and tools at hand, the possibilities of what you can create are limitless. With a little forethought and planning upfront, you can create awe inspiring materials all while keeping your game textures under budget.

_Shot of the backyard showing the variation in the terrain materials._
