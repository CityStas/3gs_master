---
title: "Properties window"
url: /docs/en-us/studio/properties
last_updated: 2026-10-30T19:55:57Z
description: "The Properties window lets you adjust properties of a selected object to change how it looks and behaves."
---

# Properties window

The **Properties** window, accessible from Studio's **Window** menu or **Home** tab toolbar, allows you to adjust certain properties of a selected object to change how the object looks and behaves. Additionally, you can manage [tags](#instance-tags) and configure instance [attributes](#instance-attributes) at the bottom of the window.

![Properties highlighted in Studio's toolbar.](../assets/studio/general/Toolbar-Properties.png)

When you select an object, the window's header bar changes to reflect the object's class and name, and its properties are divided into sections. For example, a `Class.MeshPart` includes sections like **Appearance** and **Transform** which respectively allow you to change its appearance and transform its `Class.BasePart.Size|Size`, `Class.BasePart.CFrame|CFrame`, and origin.

> **Info:** You can collapse or expand any section or subsection by clicking the small arrow to the left of its name. After you expand or collapse a section, it remains expanded or collapsed for other objects of the same class, as well as related objects that share the same property grouping.

Some properties are collapsed by default, but you can expand them by clicking the small arrow next to its name. For instance, `Class.BasePart|BaseParts` contain a `Class.BasePart.Position|Position` property which represents an **X**, **Y**, **Z** coordinate in the 3D world. In Studio, these coordinates can be entered in two ways:

_All three coordinates typed into the parent **Size** field, separated by commas_

_Property expanded and an individual size vector typed into the **X**, **Y**, and **Z** fields_

> **Info:** After you expand or collapse a property, it remains expanded or collapsed for other objects of the same class, as well as related objects that share the same property.
## Property filter

You can filter properties by typing a search query into the **Filter Properties** input near the top of the window. For example, filtering by the letters "velo" finds all properties containing them, such as **AssemblyLinear<u>Velo</u>city** and **AssemblyAngular<u>Velo</u>city**. Quickly access this input by pressing `Ctrl``Shift``P` (Windows) or `⌘``Shift``P` (Mac).

## Instance tags

The **Tags** section allows you to apply specific tags for use with `Class.CollectionService`. Tags are sets of strings applied to instances that replicate from the server to the client. They are also serialized when places are saved.

To add tags to an instance through the **Properties** window:

1. Select the instance, scroll to the **Tags** section, and click the **+** button.
2. In the popup window, enter a new tag name **or** select a tag you've already created for any other instance from the list below the input field. The tag will appear within the **Tags** section.
3. If necessary, you can remove an existing tag by clicking the **×** icon.

## Instance attributes

**Attributes** allow you to customize instances with your own data. They are similar to built-in object properties, but you can create and modify your own attributes for any instance. Key features include:

- Attributes can be created, edited, and deleted directly within Studio or through scripting (see [properties and attributes](/docs/en-us/scripting/attributes.md) for script commands to create, set, get, and delete attributes).
- Attributes and their values are saved with your place and assets.
- Value changes can be viewed in real time and are **replicated** so that clients can access them immediately.

You can store the following types/values in attributes:

- [string](/docs/en-us/luau/strings.md)
- [boolean](/docs/en-us/luau/booleans.md)
- [number](/docs/en-us/luau/numbers.md)
- `Datatype.UDim`

- `Datatype.UDim2`
- `Datatype.BrickColor`
- `Datatype.Color3`
- `Datatype.Vector2`

- `Datatype.Vector3`
- `Datatype.CFrame`
- `Datatype.NumberSequence`
- `Datatype.ColorSequence`

- `Datatype.NumberRange`
- `Datatype.Rect`
- `Datatype.Font`

New attributes can be created and modified in Studio as follows:

1. Select the instance, scroll to the **Attributes** section, and click the **+** button.
2. In the popup window, enter the attribute **Name**, select its **Type**, and click **Save**.
3. The new attribute will appear with a default value that you can change just like any other property.
4. If necessary, you can rename or delete an attribute by clicking the gear icon.

## Configurable defaults

The **configurable defaults** feature allows you to save properties from a selected `Class.Instance` as the new default for that type, reset them as needed, and share them from a local file if desired. Use cases include:

- A default `Class.MeshPart` instance where `Class.BasePart.Anchored|Anchored` is `true`, so that every new `Class.MeshPart` inserted into the 3D workspace is anchored.
- A set of default [mechanical constraints](/docs/en-us/physics/mechanical-constraints.md) with physical behaviors that match the type of mechanisms you're currently building, such as massive vehicles vs. smaller machines with less mass.
- A set of default [light](/docs/en-us/effects/light-sources.md) sources (`Class.PointLight`, `Class.SpotLight`, `Class.SurfaceLight`), each with `Class.Light.Brightness|Brightness` that suits the environment you're designing.

To **set** a specific instance as the default:

1. Select the instance in the 3D viewport or [Explorer](/docs/en-us/studio/explorer.md) hierarchy.
2. From Studio's main **Edit** menu, select **Save as Default [Instance]**. A toast notification will indicate that the default has been updated, and newly inserted instances of that type will match the default properties.
  > **Info:** Instance defaults are saved **locally** on each machine to a `DefaultInstances.rbxm` file, not to your Roblox or group account. The location of this directory can be changed in Studio's settings (`Alt``S` or `⌥``S`) under the **Studio** tab ⟩ **Instance Defaults Dir**.

To **reset** a configurable default instance:

1. Select any instance of that type in the 3D viewport or [Explorer](/docs/en-us/studio/explorer.md) hierarchy.
2. From Studio's main **Edit** menu, select **Reset Default [Instance]**. Existing instances of that type will retain their properties, but newly inserted instances will use Studio's default properties.

> **Warning:** Note the following exceptions and behavioral rules to default instances: - The **positional** instance properties `Class.BasePart.Position`, `Class.BasePart.CFrame`, `Class.PVInstance.Origin`, and `Class.Model.WorldPivot` are **not** affected by default properties, but rather are overridden by Studio insertion rules and workflows. However, `Class.GuiObject.Position` and positional properties for `Class.Attachment|Attachments` (`Class.Attachment.Position|Position`, `Class.Attachment.WorldCFrame|WorldCFrame`, `Class.Attachment.WorldPosition|WorldPosition`) are stored/maintained in configured defaults of those instance types. - Studio's **Group as Model** (`Ctrl``G` or `⌘``G`) and **Group as Folder** (`Ctrl``Alt``G` or `⌘``⌥``G`) actions do **not** use the instance defaults for `Class.Model` or `Class.Folder`, respectively.
