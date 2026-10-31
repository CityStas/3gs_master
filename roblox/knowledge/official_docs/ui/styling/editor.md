---
title: "Style Editor"
url: /docs/en-us/ui/styling/editor
last_updated: 2026-10-30T19:56:02Z
description: "Explore the built-in Style Editor, a comprehensive tool that allows you to create, manage, and apply UI styles for Roblox games."
---

# Style Editor

The built-in **Style Editor** is a comprehensive tool that allows you to create, manage, and apply UI styles for Roblox games through a combination of [tokens](#style-tokens), [design sheets](#design-sheets), [style rules](#style-rules), and [themes](#style-themes).

Access the **Style Editor** via the **UI** tab.

![Style Editor tool indicated in UI tab of Studio toolbar](../../assets/studio/general/Toolbar-Style-Editor.png)

Once open, click the **Create Design** button to generate a base style set.

![Create Design button in opening dialog of Style Editor.](../../assets/ui/ui-styling/SE-Create-Design-Entry.png)
> **Warning:** Creating a design style set through the Style Editor generates a **BaseStyleSheet** inside a **Design** folder within `Class.ReplicatedStorage`. This base sheet syncs specific engine‑level defaults like the `Datatype.Color3` default of`[163, 162, 165]` with defaults that come from insertion workflows in Studio. It's highly recommended that you do **not** delete or attempt to modify the base style sheet — instead, build tokens and style rules around a design sheet to match your UI goals.
>
> Additionally, a **StyleSheet** sheet is generated in the **Design** folder which contains a `Class.StyleDerive` to the base style sheet. If you choose to remove that `Class.StyleDerive`, unstyled values for `Class.GuiObject|GuiObjects` may become unexpected values, for example a default `Class.GuiObject.Size|Size` of`0, 0, 0, 0`.
## Style tokens

Style **tokens**, defined through [attributes](/docs/en-us/studio/properties.md#instance-attributes) of a token `Class.StyleSheet`, represent UI property variables that can be used across styles and components; for example, there could be a common color for a `Class.Frame.BackgroundColor3`, `Class.TextLabel.TextColor3`, and `Class.UIStroke.Color`. Tokens are comparable to [CSS variables](/docs/en-us/ui/styling/css-comparisons.md#variables).

> **Success:** Although not required for UI styling, tokens are highly recommended for extensible UI design and style updates over time. You should begin by creating the following tokens to understand how they tie into other aspects of universal styling.

1. Create a new token style sheet:
  1. In the left column of the Style Editor, hover over **Tokens**, click the **⊕**, and select **New Token StyleSheet**.
  2. Rename the new sheet to `TokenSheet`.![New token sheet created in the Style Editor.](../../assets/ui/ui-styling/SE-TokenSheet-New.png)
2. With the new token sheet selected, create several tokens by clicking **Add a Token…** in the main panel. These tokens will be used throughout this guide for both [rules](#style-rules) and [themes](#style-themes).![Token addition field in the Style Editor.](../../assets/ui/ui-styling/SE-TokenSheet-Add-Token.png) | Token Name | Type | Value |
| --- | --- | --- | | `Gold` | `Datatype.Color3` | `#ffcc00` | | `Magenta` | `Datatype.Color3` | `#ff0099` | | `Orange` | `Datatype.Color3` | `#dd6030` | | `Oswald` | `Datatype.Font` | `Oswald` | | `Rad20` | `Datatype.UDim` | `0, 20` | | `RectL` | `Datatype.UDim2` | `0, 300, 0, 160` | | `SquareL` | `Datatype.UDim2` | `0, 200, 0, 200` | | `Text24` | number | `24` | | `Text32` | number | `32` |![Tokens added to TokenSheet in Style Editor.](../../assets/ui/ui-styling/SE-TokenSheet-Tokens.png)

## Design sheets

A design style sheet aggregates [style rules](#style-rules) and can be linked to `Class.DataModel` trees to apply style properties to UI instances. Only one `Class.StyleSheet` can apply to a given tree, although you can use [themes](#style-themes) to swap related styles across your UI, a concept covered later in this guide.

A prepopulated design sheet named **StyleSheet** is created via the **Create Design** button. It contains class rules for common UI objects such as `Class.Frame` and `Class.TextLabel`. It also contains two `Class.StyleDerive` instances which derive (inherit) [tokens](#style-tokens) and styles from the base style sheet for use in your custom styling configurations.

![Initial configuration of design sheet in Style Editor.](../../assets/ui/ui-styling/SE-Initial-Config.png)

Once you have a design sheet, you can set up a test [on‑screen container](/docs/en-us/ui/on-screen-containers.md) to use with the Style Editor, or an [in‑game container](/docs/en-us/ui/in-experience-containers.md) if desired.

1. Hover over `Class.StarterGui` in the [Explorer](/docs/en-us/studio/explorer.md) and insert a `Class.ScreenGui`.
2. Confirm that a new `Class.StyleLink` instance appears under the `Class.ScreenGui` with its `Class.StyleLink.StyleSheet|StyleSheet` property set to the **StyleSheet** design sheet.
  > **Info:** If the `Class.StyleLink` is not created, you can quickly create one by selecting the `Class.ScreenGui` in the [Explorer](/docs/en-us/studio/explorer.md) as well as the **StyleSheet** design sheet in the left column of the Style Editor. Then, click the **Insert StyleLink** button in the upper‑right section of the editor's main panel.

## Style rules

Style **rules** apply to every instance that matches the rule's `Class.StyleRule.Selector|Selector` definition to match characteristics such as class name, instance tag, and hierarchy relationships. At a high level, instance matching and modification via a rule's `Class.StyleRule.Selector|Selector` definition operates through:

- Roblox [class](#class-rule) selectors which target all instances of a given UI class, for example `Class.Frame`, `Class.ImageLabel`, `Class.TextButton`, etc.
- Instance [tag](#tag-rule) selectors that target specific UI objects [tagged](/docs/en-us/studio/properties.md#instance-tags) through `Class.CollectionService`.
- Instance [modifiers](#ui-modifier) applied through phantom `Class.UIComponent|UIComponents` such as `Class.UICorner` or `Class.UIStroke`.
- `Class.GuiObject` [state](#state-rule) selectors which correspond to one of the four `Enum.GuiState` enum values such as `Enum.GuiState.Hover|Hover`.
- Instance name selection according to the value of the UI object's `Class.Instance.Name`.

### Class rule

A style **class** selector targets all instances of a given UI class. The following rule setup styles all `Class.Frame|Frames` with a uniform background color and size.

1. In the left column of the Style Editor, select **Frame** in the **UI Elements** branch.![Default class style in the Style Editor.](../../assets/ui/ui-styling/SE-Class-Rule-New-Class.png)
2. Link two previously created [style tokens](#style-tokens) to two `Class.Frame` properties: | Property | Style Token |
| --- | --- | | `Class.Frame.BackgroundColor3\|BackgroundColor3` | `$Magenta` | | `Class.Frame.Size\|Size` | `$SquareL` |
  1. Click **Add a Property…** in the main panel and select the necessary property. Note that you can type keywords to more quickly find properties in the dropdown menu.
  2. Instead of entering a static value, click the **⋮** button and select **Link Token**.
  3. Click the `$` which appears in the value field and select the proper associated token.![Token linking workflow diagrammed in the Style Editor.](../../assets/ui/ui-styling/SE-Class-Rule-Configure.png)![Class rule configured with tokens in the Style Editor.](../../assets/ui/ui-styling/SE-Class-Rule-Tokens.png)
3. Insert a new `Class.Frame` into the `Class.ScreenGui` you previously [created and linked](#design-sheets). The styles you defined should automatically apply to it.![Final styled class rule in the Style Editor.](../../assets/ui/ui-styling/SE-Class-Rule-Result.png)

### Tag rule

Instance **tag** selectors target specific UI objects [tagged](/docs/en-us/studio/properties.md#instance-tags) through `Class.CollectionService`. The following rule setup styles a `Class.TextButton` tagged as `ButtonPrimary` with a custom background color, font, and text size.

1. In the left column of the Style Editor, hover over the **StyleSheet** sheet, click the **⋮** button, and navigate through to **New** ⟩ **Tag**.![Creation of tag rule in the Style Editor.](../../assets/ui/ui-styling/SE-Tag-Rule-New.png)
2. Rename the new tag rule `.ButtonPrimary` (note the leading `.`).![Tag rule renamed in the Style Editor.](../../assets/ui/ui-styling/SE-Tag-Rule-Renamed.png)
3. Link three previously created [style tokens](#style-tokens) to three `Class.TextButton` properties: | Property | Style Token |
| --- | --- | | `Class.TextButton.BackgroundColor3\|BackgroundColor3` | `$Gold` | | `Class.TextButton.FontFace\|FontFace` | `$Oswald` | | `Class.TextButton.TextSize\|TextSize` | `$Text32` |
  1. Click **Add a Property…** in the main panel and select the necessary property. Remember that you can type keywords to more quickly find properties in the dropdown menu.
  2. Instead of entering a static value, click the **⋮** button and select **Link Token**.
  3. Click the `$` which appears in the value field and select the proper associated token.![Token linking workflow diagrammed in the Style Editor.](../../assets/ui/ui-styling/SE-Tag-Rule-Configure.png)![Tag rule configured with tokens in the Style Editor.](../../assets/ui/ui-styling/SE-Tag-Rule-Tokens.png)
4. Insert a new `Class.TextButton` into the `Class.ScreenGui` you previously [created and linked](#design-sheets) and [tag](/docs/en-us/studio/properties.md#instance-tags) it as `ButtonPrimary`. A convenient shortcut is as follows:
  1. Make sure the new `Class.TextButton` is selected in the [Explorer](/docs/en-us/studio/explorer.md).
  2. With the **.ButtonPrimary** tag rule selected in the left column of the Style Editor, click **Apply Tag** in the main panel. The styles you defined should automatically apply to the button.![Tag linking workflow diagrammed in the Style Editor.](../../assets/ui/ui-styling/SE-Tag-Rule-Apply-Tag.png)![Final styled tag rule in the Style Editor.](../../assets/ui/ui-styling/SE-Tag-Rule-Result.png)

### UI modifier

Instance modifier selectors apply phantom `Class.UIComponent|UIComponents` such as `Class.UICorner` or `Class.UIStroke` to further style an object. The following rule setup styles a `Class.TextLabel` with a custom text size and rounded corners.

1. In the left column of the Style Editor, select **TextLabel** in the **UI Elements** branch.![Default class style in the Style Editor.](../../assets/ui/ui-styling/SE-Modifier-Rule-New-Class.png)
2. Link a previously created [style token](#style-tokens) to the `Class.TextLabel.TextSize|TextSize` property:
  1. Click **Add a Property…** in the main panel and select the `Class.TextLabel.TextSize|TextSize` property. Remember that you can type keywords to more quickly find properties in the dropdown menu.
  2. Instead of entering a static value, click the **⋮** button and select **Link Token**.
  3. Click the `$` which appears in the value field and select the `$Text32` token.![Token linking workflow diagrammed in the Style Editor.](../../assets/ui/ui-styling/SE-Modifier-Rule-Configure.png)![Class rule configured with tokens in the Style Editor.](../../assets/ui/ui-styling/SE-Modifier-Rule-Tokens.png)

A **pseudo instance** is required to configure and apply rounded corners to other elements. To create one:

1. In the left column, hover over **TextLabel**, click the **⋮** button, and navigate through to **New** ⟩ **Pseudo Instance** ⟩ **UICorner**.![Creation of a pseudo instance in the Style Editor.](../../assets/ui/ui-styling/SE-Modifier-Rule-Pseudo-Instance-New.png) A new **UICorner** pseudo instance appears under the **TextLabel** element in the left column.![Resulting pseudo instance in the Style Editor.](../../assets/ui/ui-styling/SE-Modifier-Rule-Pseudo-Instance-Created.png)
2. With the new **UICorner** instance selected in the left column, link a previously created [style token](#style-tokens) to the `Class.UICorner.CornerRadius|CornerRadius` property:
  1. Click **Add a Property…** in the main panel and select the `Class.UICorner.CornerRadius|CornerRadius` property.
  2. Instead of entering a static value, click the **⋮** button and select **Link Token**.
  3. Click the `$` which appears in the value field and select the `$Rad20` token.![Pseudo instance configured with tokens in the Style Editor.](../../assets/ui/ui-styling/SE-Modifier-Rule-Pseudo-Instance-Tokens.png)
3. Insert a new `Class.TextLabel` into the `Class.ScreenGui` you previously [created and linked](#design-sheets). The styles you defined should automatically apply to it.![Final styled modifier rule in the Style Editor.](../../assets/ui/ui-styling/SE-Modifier-Rule-Result.png)

### State rule

`Class.GuiObject` **state** selectors correspond to one of the four `Enum.GuiState|GuiState` enum values such as `Enum.GuiState|Hover`, letting you automatically configure style changes for interactive states. The following rule setup creates a hover state of `-4` degrees rotation for all `Class.ImageButton|ImageButtons`.

1. In the left column of the Style Editor, select **ImageButton** in the **UI Elements** branch.![Default class style in the Style Editor.](../../assets/ui/ui-styling/SE-State-Rule-New-Class.png)
2. Click the **⋮** button and navigate through to **New** ⟩ **GuiState** ⟩ **Hover**.![Creation of state rule in the Style Editor.](../../assets/ui/ui-styling/SE-State-Rule-New.png) A new **Hover** state modifier instance appears under the **ImageButton** element in the left column.![Resulting state rule in the Style Editor.](../../assets/ui/ui-styling/SE-State-Rule-Created.png)
3. With the new **Hover** modifier selected in the left column, click **Add a Property…** in the main panel and select `Class.ImageButton.Rotation|Rotation`. Remember that you can type keywords to more quickly find properties in the dropdown menu.
4. Enter `-4` in the property's value field.![State rule configured with tokens in the Style Editor.](../../assets/ui/ui-styling/SE-State-Rule-Tokens.png)
5. Insert a new `Class.ImageButton` into the `Class.ScreenGui` you previously [created and linked](#design-sheets). When you hover over the button in the viewport, it should rotate 4 degrees counterclockwise.![Final styled state rule in the Style Editor.](../../assets/ui/ui-styling/SE-State-Rule-Result.png)

## Style queries

Style **queries**, similar to [CSS container and media queries](/docs/en-us/ui/styling/css-comparisons.md#queries), allow you to apply conditional logic to your UI based on container size, input type, or other factors. The Style Editor provides a streamlined workflow to create both the query logic (conditions) and the resulting styles as a unified set.

### Built-in queries

Some `Class.StyleQuery` conditions are very common, such as changing properties based on the `Class.GuiService.ViewportDisplaySize|ViewportDisplaySize`. To simplify this, the Style Editor includes **built‑in** queries which allow you to create conditional rules without needing a pseudo or real instance of a `Class.StyleQuery`; instead, you simply use a query rule with a predefined selector like `ViewportDisplaySizeSmall`.

The following steps demonstrate how to generate built‑in queries for a `Class.TextLabel` to handle `Enum.DisplaySize.Small|Small`, `Enum.DisplaySize.Medium|Medium`, and `Enum.DisplaySize.Large|Large` viewport sizes.

1. In the left column of the Style Editor, hover over **TextLabel**, click the **⋮** button, and navigate through to **New** ⟩ **StyleQuery** ⟩ **Builtin** ⟩ **ViewportDisplaySize**.![Creation of a built-in StyleQuery in the Style Editor.](../../assets/ui/ui-styling/SE-Query-New-Builtin.png) This creates a **Queries** folder under the **TextLabel** rule containing three query rules:
  - **@ViewportDisplaySizeLarge** — Define properties that apply when the viewport is `Enum.DisplaySize.Large|Large`.
  - **@ViewportDisplaySizeMedium** — Define properties that apply when the viewport is `Enum.DisplaySize.Medium|Medium`.
  - **@ViewportDisplaySizeSmall** — Define properties that apply when the viewport is `Enum.DisplaySize.Small|Small`.![Hierarchy of a StyleQuery within a class rule.](../../assets/ui/ui-styling/SE-Query-Builtin-Hierarchy.png)
2. Click **Add a Property…** under each query rule and set the specific `Class.TextLabel.Text|Text` string that should display when that query is active: | Query Rule | Property | Value |
| --- | --- | --- | | **@ViewportDisplaySizeLarge** | `Class.TextLabel.Text\|Text` | `Large Text` | | **@ViewportDisplaySizeMedium** | `Class.TextLabel.Text\|Text` | `Medium Text` | | **@ViewportDisplaySizeSmall** | `Class.TextLabel.Text\|Text` | `Small Text` |
3. To verify the queries, use the [Device Emulator](/docs/en-us/studio/testing-modes.md#device-emulation) to test how the UI responds to different resolutions across three distinct devices:
  1. Insert a new `Class.TextLabel` into the `Class.ScreenGui`.
  2. Change the **Device** in the [Device Emulator](/docs/en-us/studio/testing-modes.md#device-emulation) to see the text change in real time. | Size | Example Emulations |
| --- | --- | | `Enum.DisplaySize.Large\|Large` | **PS5**, **PS4**, **Xbox One** | | `Enum.DisplaySize.Medium\|Medium` | **Average Laptop**, **HD 720** | | `Enum.DisplaySize.Small\|Small` | **iPhone XR**, **iPad 7th Generation** |

### Custom query

You can add a style query to any existing rule to create responsive UI that adapts to its container. The following setup configures a `Class.TextLabel` to automatically change its appearance only when it expands to a width of 400 pixels or more.

1. In the left column of the Style Editor, hover over **TextLabel**, click the **⋮** button, and navigate through to **New** ⟩ **StyleQuery** ⟩ **Custom**.![Creation of a custom StyleQuery in the Style Editor.](../../assets/ui/ui-styling/SE-Query-New-Custom.png) This action creates a **Queries** folder under the **TextLabel** rule containing two linked items:
  - **::StyleQuery** pseudo-instance rule where you define the **Conditions**.
  - **@StyleQuery** rule where you define the **Properties** to apply when those conditions are met.![Hierarchy of a StyleQuery within a class rule.](../../assets/ui/ui-styling/SE-Query-Custom-Hierarchy.png)
2. Select the parent **TextLabel** rule in the main panel and define the following default properties: | Property | Value |
| --- | --- | | `Class.TextLabel.BackgroundColor3\|BackgroundColor3` | `$Magenta` | | `Class.TextLabel.Text\|Text` | `Default Text` |
3. Select the **::StyleQuery** rule in the main panel, click **Add a Condition…**, and configure the following: | Condition | Value |
| --- | --- | | `MinSize` | `400, 0` |
  > **Info:** See `Class.StyleQuery.IsActive` as a reference for other conditions available through the **::StyleQuery** rule.
4. Select the **@StyleQuery** rule in the main panel and set the properties that should apply when the query is active: | Property | Value |
| --- | --- | | `Class.TextLabel.BackgroundColor3\|BackgroundColor3` | `$Gold` | | `Class.TextLabel.Text\|Text` | `Large Text` |

To verify the query, you can manually resize a `Class.TextLabel` in the viewport.

1. Insert a new `Class.TextLabel` into the `Class.ScreenGui`.
2. Adjust its width to see the style swap in real-time. #### 0–400 Pixel Width While the `Class.TextLabel` width is smaller, the `MinSize` condition is not met and the label uses its default background color and text.![TextLabel appearing magenta with 'Default Text' on a phone viewport.](../../assets/ui/ui-styling/SE-Query-Test-Small.png) #### Over 400 Pixel Width As you drag the `Class.TextLabel` wider than 400 pixels, the query becomes active and the `@StyleQuery` immediately overrides the base style.![TextLabel appearing gold with 'Large Text' on the same phone viewport.](../../assets/ui/ui-styling/SE-Query-Test-Large.png)

> **Info:** While manual resizing is a quick way to check responsive logic, you can also use Studio's built‑in emulation tools for more precise testing: - Use the [Device Emulator](/docs/en-us/studio/testing-modes.md#device-emulation) to test how your UI responds to specific screen resolutions and `Class.GuiService.ViewportDisplaySize|ViewportDisplaySize` conditions. - Use the [Controller Emulator](/docs/en-us/studio/testing-modes.md#controller-simulation) to verify `Class.UserInputService.PreferredInput|PreferredInput` logic, such as switching styles when a gamepad is detected.
## Style transitions

Style **transitions**, comparable to [CSS transitions](/docs/en-us/ui/styling/css-comparisons.md#transitions), let you tween property values over a set duration.

### Default

To tween many UI properties with the same parameters, you can set a default transition that applies to **all** properties unless another transition is explicitly set for a specific property.

1. Select **TextButton** in the **UI Elements** branch and then, in the main panel, add three new properties with the following values: | Property | Value |
| --- | --- | | `Class.TextButton.AutoButtonColor\|AutoButtonColor` | `false` | | `Class.TextButton.BackgroundColor3\|BackgroundColor3` | `#335FFF` | | `Class.TextButton.Rotation\|Rotation` | `0` |![Class style in the Style Editor.](../../assets/ui/ui-styling/SE-Transition-Rule-New-Class.png)
2. Hover over the parent **TextButton** row, click the ⋮ button, and navigate through to **Insert** ⟩ **Transition**.![Add default transition to a rule in the Style Editor.](../../assets/ui/ui-styling/SE-Transition-Rule-Add-Default-Transition.png) A default transition of `1, Quad, Out, 0` inserts directly under the **TextButton** rule, indicating a transition of 1 second, easing style `Enum.EasingStyle.Quad|Quad`, easing direction `Enum.EasingDirection.Out|Out`, and no delay.![Default transition highlighted in the Style Editor.](../../assets/ui/ui-styling/SE-Transition-Rule-Default-Transition-Added.png)
3. Hover over the parent **TextButton** row, click the **⋮** button, and navigate through to **New** ⟩ **GuiState** ⟩ **Hover**.![Creation of state rule in the Style Editor.](../../assets/ui/ui-styling/SE-Transition-Rule-Default-New-State.png)
4. For the new **Hover** modifier, add two new properties as the **targets** for the hover state. | Property | Value |
| --- | --- | | `Class.TextButton.BackgroundColor3\|BackgroundColor3` | `#33AAFF` | | `Class.TextButton.Rotation\|Rotation` | `-5` |![Properties on hover state rule in the Style Editor.](../../assets/ui/ui-styling/SE-Transition-Rule-State-Properties.png)
5. Insert a new `Class.TextButton` into the `Class.ScreenGui` you previously [created and linked](#design-sheets). When you hover over the button in the viewport, it should gradually brighten and rotate 5 degrees counterclockwise.![Final styled state rule in the Style Editor.](../../assets/ui/ui-styling/SE-Transition-Rule-Result.png)

### Token-linked

To reuse transition behaviors across multiple rules, you can define **tokens** representing the `Datatype.TweenInfo` data type. The following rule setup creates a hover state to transition all `Class.TextButton|TextButtons` to/from -5 degrees rotation and a lighter background color.

1. If you haven't already, create a [token style sheet](#style-tokens) named `TokenSheet`.![New token sheet created in the Style Editor.](../../assets/ui/ui-styling/SE-TokenSheet-New.png)
2. With the new token sheet selected, create two new tokens by clicking **Add a Token…** in the main panel. | Token Name | Type | Tween Parameters |
| --- | --- | --- | | `CubicOut` | `Datatype.TweenInfo` | <ul><li>`Duration` = `1.25`</li><li>`EasingStyle` = `Cubic`</li><li>`EasingDirection` = `Out`</li><li>`Delay` = `0`</li></ul> | | `QuadInOut` | `Datatype.TweenInfo` | <ul><li>`Duration` = `0.5`</li><li>`EasingStyle` = `Quad`</li><li>`EasingDirection` = `InOut`</li><li>`Delay` = `0`</li></ul> |![Tokens added to TokenSheet in Style Editor.](../../assets/ui/ui-styling/SE-Transition-Rule-Tokens-Defined.png)
3. Select **TextButton** in the **UI Elements** branch and then, in the main panel, add three new properties with the following values: | Property | Value |
| --- | --- | | `Class.TextButton.AutoButtonColor\|AutoButtonColor` | `false` | | `Class.TextButton.BackgroundColor3\|BackgroundColor3` | `#335FFF` | | `Class.TextButton.Rotation\|Rotation` | `0` |![Class style in the Style Editor.](../../assets/ui/ui-styling/SE-Transition-Rule-New-Class.png)
4. For each new property except for `Class.TextButton.AutoButtonColor|AutoButtonColor`, hover over its row, click the **⋮** button, and select **Insert** ⟩ **Transition**.![Add transition to a property in the Style Editor.](../../assets/ui/ui-styling/SE-Transition-Rule-Add-Transition.png)
5. Hover over the new **Transition** row under each property, click the **⋮** button, and select **Link Token**. Then, instead of entering a static value, click the `$` which appears in the value field and select the proper transition token.![Token linking workflow diagrammed in the Style Editor.](../../assets/ui/ui-styling/SE-Transition-Rule-Tokens-Link.png) | Property Transition | Transition Token |
| --- | --- | | `Class.TextButton.BackgroundColor3\|BackgroundColor3` | `$CubicOut` | | `Class.TextButton.Size\|Size` | `$QuadInOut` |![Transition tokens linked in the Style Editor.](../../assets/ui/ui-styling/SE-Transition-Rule-Tokens-Linked.png)
6. Hover over the parent **TextButton** row, click the **⋮** button, and navigate through to **New** ⟩ **GuiState** ⟩ **Hover**.![Creation of state rule in the Style Editor.](../../assets/ui/ui-styling/SE-Transition-Rule-New-State.png)
7. For the new **Hover** modifier, add two new properties as the **targets** for the hover state. | Property | Value |
| --- | --- | | `Class.TextButton.BackgroundColor3\|BackgroundColor3` | `#33AAFF` | | `Class.TextButton.Rotation\|Rotation` | `-5` |![Properties on hover state rule in the Style Editor.](../../assets/ui/ui-styling/SE-Transition-Rule-State-Properties.png)
8. Insert a new `Class.TextButton` into the `Class.ScreenGui` you previously [created and linked](#design-sheets). When you hover over the button in the viewport, it should gradually brighten and rotate 5 degrees counterclockwise.![Final styled state rule in the Style Editor.](../../assets/ui/ui-styling/SE-Transition-Rule-Result.png)

## Style themes

Style **themes** consist of sets of specific tokens that can be swapped, for example color tokens that define a "light" and "dark" theme.

### Theme creation

For extensibility, themes are organized into folders. While a single folder may suffice for most purposes, you're free to organize themes in folders like "colors" or "fonts" if desired.

1. Create a new theme folder:
  1. In the left column of the Style Editor, hover over **Themes**, click the **⊕**, and select **New Theme**.
  2. Rename the new **Folder** item to **General**.![New themes folder created in the Style Editor.](../../assets/ui/ui-styling/SE-Themes-New-Folder.png)
2. Create a new theme style sheet:
  1. Hover over the new **General** folder, click the **⋮** button, and select **New Theme StyleSheet**.
  2. Rename it to **ThemeA**.![New theme created in the Style Editor.](../../assets/ui/ui-styling/SE-Themes-New-Theme.png)

### Theme tokens

Once a theme is constructed, you can link its tokens to various UI object properties such as the `Class.TextButton.BackgroundColor3|BackgroundColor3` of a `Class.TextButton`. Theme sheets must use a common set of tokens to work correctly.

With **ThemeA** selected in the left column of the Style Editor:

1. Link three previously created [style tokens](#style-tokens) to three new theme tokens: | Theme Token | Style Token |
| --- | --- | | `BackColor` | `$Gold` | | `ButtonFont` | `$Oswald` | | `ButtonTextSize` | `$Text32` |
  1. Click **Add a Token…** in the main panel and enter the theme token's name.
  2. Click the `$` which appears in the value field and select the associated style token.![Theme configured with tokens in the Style Editor.](../../assets/ui/ui-styling/SE-Themes-ThemeA-Tokens.png)
2. In the left column of the Style Editor, select **TextButton** in the **UI Elements** branch.![Default class style in the Style Editor.](../../assets/ui/ui-styling/SE-Themes-New-Class.png)
3. Link the theme's tokens to three new `Class.TextButton` properties: | Property | Theme Token |
| --- | --- | | `Class.TextButton.BackgroundColor3\|BackgroundColor3` | `$BackColor` | | `Class.TextButton.FontFace\|FontFace` | `$ButtonFont` | | `Class.TextButton.TextSize\|TextSize` | `$ButtonTextSize` |
  1. Click **Add a Property…** in the main panel and select the necessary property.
  2. Instead of entering a static value, click the **⋮** button and select **Link Token**.
  3. Click the `$` which appears in the value field and select the proper theme token.![Token linking workflow diagrammed in the Style Editor.](../../assets/ui/ui-styling/SE-Themes-Theme-Configure.png)
  > **Warning:** When linking the theme's tokens, look for **$[Token] in ThemeA** in the hover‑over to know the token is coming from the **theme** and not from the global token sheet (remember that the theme already derives the global tokens).![Class rule configured with theme tokens in the Style Editor.](../../assets/ui/ui-styling/SE-Themes-Class-Tokens.png)

### Theme duplication

Once you have a theme generally established, you can **duplicate** it and change various tokens to define a unique theme style.

1. In the left column of the Style Editor, hover over the **ThemeA** theme, click the **⋮** button, and select **Duplicate**.
2. Rename the duplicated theme to **ThemeB**.![Theme duplicated in the Style Editor.](../../assets/ui/ui-styling/SE-Themes-Duplicated-Theme.png)
3. Link two of the theme's tokens to two different style tokens: | Theme Token | Style Token |
| --- | --- | | `BackColor` | `$Magenta` | | `ButtonTextSize` | `$Text24` |
  1. To the right of the property's value field, click the **⋮** button and select **Unlink Token**.
  2. Click **⋮** again and select **Link Token**.
  3. In its value field, click the `$` and select the new associated style token.![Theme configured with tokens in the Style Editor.](../../assets/ui/ui-styling/SE-Themes-ThemeB-Tokens.png)

### Theme swapping

Once you have [multiple themes](#theme-duplication), you can swap between them via the theme's folder, or via a script as outlined in `Class.StyleSheet:SetDerives()|SetDerives()`.

1. In the left column of the Style Editor, select the **General** folder in the **Themes** branch.
2. In the main panel, swap between the themes using the radio buttons. #### ThemeA![ThemeA swapped in the Style Editor.](../../assets/ui/ui-styling/SE-Themes-Swapping-ThemeA.png) #### ThemeB![ThemeB swapped in the Style Editor.](../../assets/ui/ui-styling/SE-Themes-Swapping-ThemeB.png)
