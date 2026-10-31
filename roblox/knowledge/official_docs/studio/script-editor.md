---
title: "Script Editor"
url: /docs/en-us/studio/script-editor
last_updated: 2026-10-30T19:55:57Z
description: "Roblox's built-in, fully-featured script editor includes modern conveniences like autocomplete, code highlighting, and multi-cursor editing."
---

# Script Editor

The **Script Editor** in Studio is the primary tool for scripting on Roblox. It's a self-improving environment that can help you write high-impact code, shorten your development time, and iterate on your games. It can improve your scripting experience by:

- Formatting and highlighting syntax in your code.
- Offering ways to [autocomplete](#autocomplete-features) phrases in your code as you type.
- Helping you [navigate code](#code-navigation) by jumping to variable and function declarations.
- Helping you [find and replace](#find-and-replace) code in open scripts or all scripts.
- Providing [real-time feedback](#real-time-feedback) on your code quality and performance.

The Script Editor supports all types of [scripts](/docs/en-us/scripting.md) and opens automatically when you create a new script or double-click an existing script in the [Explorer](/docs/en-us/studio/explorer.md) window.

> **Success:** You can [customize](#editor-settings) the Script Editor to suit your preferences and workflows, including font family/size, formatting behavior, and colors for syntax highlighting. You can also toggle features such as [autocomplete](#autocomplete-features), and [script analysis](#script-analysis).
## Autocomplete features

The Script Editor's autocomplete features generate code-related information that can improve your programming efficiency, such as:

- **Informed suggestions** on how to complete phrases as you type them that are contextual to the game's [data model](/docs/en-us/projects/data-model.md). For example, if you have a `Class.Model` in `Class.Workspace` called **RocketShip**, autocomplete suggests `RocketShip` when you type `workspace.roc` and indicates that it's a `Class.Model`.![Autocomplete showing suggestions based on the game's data model](../assets/studio/script-editor/Autocomplete-Data-Model.png)
  > **Info:** Use the `↑` and `↓` keys to browse the suggestions, then press `Tab` or `Enter` to accept a suggestion and insert the complete phrase.
- **Autofill names** for variables and functions that you declare, helping you avoid pesky typos.![Autocomplete showing suggestions based on a previously declared variable.](../assets/studio/script-editor/Autocomplete-Variable.png)
- **Documentation pop-ups with code samples** that are similar to those on the [Engine API Reference](/docs/en-us/reference/engine.md), giving you context on the API's usage.![Autocomplete showing suggestions based on a Roblox Engine API.](../assets/studio/script-editor/Autocomplete-API.png)
- **On-hover tooltips** that you can customize with your own defined documentation. Place a [block comment](/docs/en-us/luau/comments.md#block-comments) immediately before a function, variable, or other declaration, and the Script Editor shows that comment as a tooltip when you hover over the name later. This also works when the declaration appears inside a type expression, such as `typeof()`:```lua
export type Icon = {
	new: typeof(--[[Constructs an empty icon.]] function(): Icon
		return (nil :: any) :: Icon
	end),
}
```![Autocomplete showing custom documentation.](../assets/studio/script-editor/Autocomplete-CustomDocs.png)
- **On-hover script analysis diagnostics** with information you can use to troubleshoot errors.![Autocomplete showing diagnostic information.](../assets/studio/script-editor/Autocomplete-Diagnostics.png)
- **Function signatures** when you type an argument, providing you a reference for its parameters and return values.![Autocomplete showing function signature](../assets/studio/script-editor/Autocomplete-Signature.png)

## Code navigation

### Go to declaration

You can jump to the declaration of a function or variable by holding `Ctrl` on Windows or `⌘` on Mac when clicking the call, or by right-clicking its call and clicking **Go to Declaration**.

![Go to Declaration workflow on a declared function](../assets/studio/script-editor/Go-To-Declaration.png) ### Script function filter

The **Script Function Filter** displays a list of all functions declared in a script. To open it, press `Alt``F` on Windows or `⌥``F` on Mac. With the list open, you can browse the signatures for each function, filter through them by name, and double-click one to jump to its declaration.

![Script Function Filter showing all functions inside a script](../assets/studio/script-editor/Script-Functions-Filter.png) ## Find and replace

The **Find/Replace** widget lets you find and replace code in an open script. The widget supports matching case, matching the whole word, and searching by regular expressions. To open it, press `Ctrl``F` on Windows or `⌘``F` on Mac.

![Find/Replace widget labeled](../assets/studio/script-editor/Find-Replace-Widget-Labeled.png)
> **Info:** For broader searches, the **Find All / Replace All** window lets you find/replace code across multiple scripts in the game. To open it, press `Ctrl``Shift``F` on Windows or `⌘``Shift``F` on Mac.
## Real-time feedback

### Script Analysis

The **Script Analysis** window, accessible through the **Analysis** button in Studio's **Script** tab toolbar, performs static analysis on your scripts and displays active errors and warnings. For more information on the errors and warnings, see the [Luau linting](https://luau.org/lint) documentation.

![Script with various marked errors](../assets/studio/script-editor/Script-Analysis-1.png)_Script errors underlined in Script Editor_

![Script Analysis window with details on marked errors from script](../assets/studio/script-editor/Script-Analysis-2.png)_Errors explained in Script Analysis window_

### Output

The [Output](/docs/en-us/studio/output.md) window displays errors captured from running scripts, messages from the Roblox engine, messages from calls to `print()`, and errors from calls to `warn()`.

## Code Assist

**Code Assist** is a feature that suggests lines or functions of code as you type, helping you code more efficiently and stay focused. Based on contexts from your comment and code, suggestions will be triggered in two ways:

- **Automatically** when you pause on a line for a few seconds and the AI model has enough context for a suggestion.
- **Manually** with shortcut `Alt``∖` on Windows or `⌥``∖` on Mac.

Press `Tab` to accept a suggestion, or ignore it by continuing to type. Currently, your script needs to contain at least a few lines of code to trigger a suggestion.

> **Warning:****Code Assist** helps automate basic coding tasks so you can focus on creative work, but it does not always suggest perfect code (see [Limitations](#limitations)). It's still your responsibility to review, test, and determine if the code suggestion is contextually appropriate.
### Improve suggestions

To get more accurate and relevant suggestions, it's recommended that you follow clean coding practices, regardless of assistance, and:

- Break down your code into smaller functions.
- Use descriptive script names that capture the overall intent of what each script does. For example, name a script **SyncCustomSounds** instead of just **Sounds**.
- Assign descriptive names for parameters, functions, and scripts. For example, name a part **GreenSphere** instead of simply **grs**, or name a function `generateSphere()` instead of `gen()`. Using named functions versus anonymous functions can also produce better hints.
- Consistently include well-written [comments](/docs/en-us/luau/comments.md) that describe the task you're implementing and what the inputs/outputs should be.
  - Consider including some sample calls with expected results in comments.
  - Suggest how to solve a problem, for instance `-- Use raycast`.
  - Use the exact function or variable name you defined, for example `-- Create 10 greenSphere objects` instead of `-- Create 10 spheres`.
- If you're a novice scripter, start with basic projects such as "make the player jump when they touch the part" or use the tool to generate small code snippets that you can expand upon as your knowledge grows.

### Limitations

The tool helps automate basic coding tasks but it does not always suggest perfect code. Known limitations include:

- Manual triggering does not **always** force-generate a suggestion.
- Suggestions are machine learned from a corpus of code and can thus reflect some limitations of the code they're trained on. For example, suggestions may not use newer APIs in favor of older APIs, or they may use Lua instead of [Luau](/docs/en-us/luau.md).
- The tool may generate incorrect or misleading information that is not useful for your purpose.
- Internal filters attempt to block offensive language, but they're not all-encompassing and there's a possibility the tool may generate offensive or biased information.
- The suggestions may be the same, similar, or different among users, even with the same prompts. Your code, however, will never be shared with others.
- The suggestion may be incomplete due to the limited length of output from the learning models.
- There's a daily cap for the number of suggestions and, once the cap is reached, you will get no suggestions until the next day.

### Code privacy

Currently, Roblox does not use any non-public data to train the learning models. The tool only uses a small subset of free marketplace assets for tuning large language models and the subset has passed various checks for quality and safety filters.

Furthermore, all suggestions are generated **by** the AI model and do not transfer from one user to another. Since your code is not used for model training, it won't be suggested to other users of **Code Assist**, with the one exception of code being posted to free marketplace items.

## Multi-cursor

The Script Editor supports usage of multiple cursors to make edits simultaneously. You can add cursors based on your needs with a mouse click or keyboard shortcut. The initial cursor is called the **primary cursor** and additional cursors are called **secondary cursors**.

- Edits that you make at the primary cursor copy to the secondary cursors. Each edit counts as one action, so undo/redo of an edit applies to all cursors.
- Widgets such as [autocomplete](#autocomplete-features) appear on the primary cursor but not the secondary cursors.
- All of the standard [keyboard shortcuts](#keyboard-shortcuts) for script editing work with multi-cursor editing, including code indentation, toggling comments, and deleting lines.

The following table summarizes multi-cursor workflows and their shortcuts.

| Command | Windows | Mac |
| --- | --- | --- |
| **Add/remove cursor at mouse location** | `Alt` + click | `⌥` + click |
| **Remove most recently added cursor** | `Ctrl``U` | `⌘``U` |
| **Add/modify cursor on mouse drag** | `Alt` + drag | `⌥` + drag |
| **Add cursor above/below** | `Ctrl``Alt``↑` / `Ctrl``Alt``↓` | `⌘``⌥``↑` / `⌘``⌥``↓` |
| **Add cursor to next matching selection** | `Ctrl``D` | `⌘``D` |
| **Add cursor to every matching selection** | `Shift``Alt``L` | `Shift``⌥``L` |
| **Column/block select** | `Shift``Alt` + drag | `Shift``⌥` + drag |
| **Split selections into lines** | `Shift``Alt``I` | `Shift``⌥``I` |

> **Info:** To remove all secondary cursors, exit multi-cursor editing, and return to the primary cursor, press `Esc`.
### Add cursors

You can add cursors with a combination of keyboard shortcuts and mouse maneuvers. Cursors merge if they occupy the same space, such as if you add cursors with arrow keys or delete all the characters between cursors.

#### At mouse location

To add a cursor at your mouse pointer location:

1. Hold `Alt` on Windows or `⌥` on Mac.
2. Click where you want to add the cursor.

#### With mouse drag

You can drag the mouse to add a cursor to a selection, split a multi-line selection into lines, or select columns and blocks of code/whitespace.

#### Drag select

To add a cursor to a selection of code through dragging:

1. Hold `Alt` on Windows or `⌥` on Mac.
2. Click and drag your mouse over the selection of code.

#### Split into lines

To split a multi-line selection into lines and add a cursor at the end of each line, press `Shift``Alt``I` on Windows or `Shift``⌥``I` on Mac.

#### Column/block select

To select columns and blocks of code or whitespace, drag the mouse while holding `Shift``Alt` on Windows or `Shift``⌥` on Mac. As you drag, a cursor will be added on each highlighted line.

#### Above and below primary cursor

To add a cursor directly above or below the primary cursor:

1. Press and hold `Ctrl``Alt` on Windows or `⌘``⌥` on Mac.
2. Press the `↑` or `↓` arrows.

#### To matching selections

You can add cursors to all matches of a selection or to the next/previous match, and optionally toggle whether matches are case-sensitive and/or match the whole word.

#### All matching

To add a cursor to all matches of a selected portion:

1. Select the code that you want to search for matches of.
2. Press `Shift``Alt``L` on Windows or `Shift``⌥``L` on Mac.

#### Next/previous match

To add a cursor to the **next** matching selection:

1. Select the code that you want to search for matches of.
2. Press `Ctrl``D` on Windows or `⌘``D` on Mac.
3. Continue pressing `Ctrl``D` or `⌘``D` until you've selected all the next matches that you want.

There is no default shortcut for adding a cursor to the **previous** matching selection, but you can add your own:

1. Open **File** ⟩ **Advanced** ⟩ **Customize Shortcuts**.
2. In the shortcuts window, locate **Select previous occurrence**.
3. Double-click the action's **Shortcut** field and enter your own custom key combination, such as `Shift``Ctrl``D` to pair alongside "next" matching's default of `Ctrl``D`.
4. Confirm your setting by clicking **OK** in the bottom-right corner of the window.

#### Case or whole word match

For each of the matching-related workflows above, you can match **case** and/or **whole word** as follows:

1. Open the Find/Replace tool (`Ctrl``F` on Windows or `⌘``F` on Mac).
2. Use the toggle buttons to choose if a matched selection should be case-sensitive and/or match the whole word only.

### Remove cursors

You can remove cursors with the following keyboard shortcuts and mouse maneuvers. Alternatively, you can exit multi-cursor editing by pressing `Esc`.

#### At mouse location

To remove a cursor:

1. Press and hold `Alt` on Windows or `⌥` on Mac.
2. Click the cursor you want to remove.

#### Most recently added

To remove the most recently added cursor, press `Ctrl``U` on Windows or `⌘``U` on Mac.

### Copy and paste cursors

Copying a selection of code includes the cursors within it. The behavior of the paste depends on the number of cursors at the source and the number of cursors at the destination:

- If the number of cursors are the same, then each copied cursor pastes to each corresponding destination cursor.
- If the number of cursors are different, then each cursor at the destination receives the entire paste with each copied cursor as a new line.

### On-type formatting

Pressing enter/return will auto-indent each cursor at the new line relative to the previous line. If the previous line starts with an incomplete block, the formatter will try to complete it.

## Editor settings

Many customization options are accessible via the **Script Editor** tab of [Studio Settings](/docs/en-us/studio/setup.md#customization). Commonly modified options include:

| Option | Description |
| --- | --- |
| **Font** | Font face and size for code in the editor. |
| **Tab width** | Number of spaces representing a `Tab` indent. |
| **Indent using spaces** | If enabled, spaces equal to **Tab Width** are inserted with `Tab` press. |
| **Text wrapping** | If enabled, longer lines of code wrap to the next line. |
| **Script Editor color preset** | Color preset for code elements, selection colors, and more. After choosing a preset, you can set specific colors for options like **Selection Color** and **Comment Color**. |

## Keyboard shortcuts

The Script Editor has the following keyboard shortcuts.

#### File and display

| Command | Windows | Mac |
| --- | --- | --- |
| **Close script** | `Ctrl``W` | `⌘``W` |
| **Reopen last closed script** | `Ctrl``Shift``T` | `⌘``Shift``T` |
| **Quick open** | `Ctrl``P` | `⌘``P` |
| **Show script in Explorer** | `Ctrl``Alt``K` | `⌘``⌥``K` |
| **Zoom in** | `Ctrl``=` | `⌘``=` |
| **Zoom out** | `Ctrl``-` | `⌘``-` |
| **Reset script zoom** | `Ctrl``0` | `⌘``0` |

#### Basic editing

| Command | Windows | Mac |
| --- | --- | --- |
| **Cut** | `Ctrl``X` | `⌘``X` |
| **Copy** | `Ctrl``C` | `⌘``C` |
| **Paste** | `Ctrl``V` | `⌘``V` |
| **Undo** | `Ctrl``Z` | `⌘``Z` |
| **Redo** | `Ctrl``Y` | `Shift``⌘``Z` |
| **Select all** | `Ctrl``A` | `⌘``A` |
| **Find** / **Replace** | `Ctrl``F` | `⌘``F` |
| **Find all** / **replace all** | `Ctrl``Shift``F` | `⌘``Shift``F` |
| **Indent** / **unindent** | `Ctrl``]` / `Ctrl``[` | `⌘``]` / `⌘``[` |
| **Toggle comment** | `Ctrl``/` | `⌘``/` |
| **Expand all folds** | `Ctrl``E` | `⌘``E` |
| **Collapse all folds** | `Ctrl``Shift``E` | `⌘``Shift``E` |
| **Delete line** | `Ctrl``Shift``K` | `⌘``Shift``K` |
| **Delete to start of line** | `Ctrl``Shift``Backspace` | `⌘``Delete` |
| **Move line up/down** | `Alt``↑` / `Alt``↓` | `⌥``↑` / `⌥``↓` |
| **Go to declaration** | `Ctrl``F12` | `⌘``F12` |
| **Open script function filter** | `Alt``F` | `⌥``F` |
| **Format selection** | `Alt``Shift``F` | `⌥``Shift``F` |

#### Multi-Cursor

| Command | Windows | Mac |
| --- | --- | --- |
| **Add/remove cursor at mouse location** | `Alt` + click | `⌥` + click |
| **Remove most recently added cursor** | `Ctrl``U` | `⌘``U` |
| **Add/modify cursor on mouse drag** | `Alt` + drag | `⌥` + drag |
| **Add cursor above/below** | `Ctrl``Alt``↑` / `Ctrl``Alt``↓` | `⌘``⌥``↑` / `⌘``⌥``↓` |
| **Add cursor to next matching selection** | `Ctrl``D` | `⌘``D` |
| **Add cursor to every matching selection** | `Shift``Alt``L` | `Shift``⌥``L` |
| **Column/block select** | `Shift``Alt` + drag | `Shift``⌥` + drag |
| **Split selections into lines** | `Shift``Alt``I` | `Shift``⌥``I` |
