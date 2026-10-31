---
title: "AI Assistant"
url: /docs/en-us/tutorials/curriculums/building/code-with-assistant
last_updated: 2026-10-30T19:55:57Z
description: "Explains how use AI Assistant prompts to add code to your obby."
---

# AI Assistant

**Assistant** is Roblox's AI helper that can help you create and code your games. In this chapter, let's walk through how to open Assistant in Studio, write requests that change part behavior, and playtest your results to see if you need to make any changes to the Assistant's code sample.

## Open Assistant

Assistant is available in the top-right corner of this webpage, as well as directly in Studio. This second placement allows Assistant to directly reference everything that makes up your game, then make suggestions on how you can add or edit 3D objects and scripts for your specific gameplay goals.

![Assistant button indicated on the right side of Studio's mezzanine bar.](../../../assets/tutorials/building-lesson/Mezzanine-Assistant.png) ## Create prompt

Once Assistant is open in Studio, it can reference all of your platforms and add scripts to change their behavior, such as:

- Turning a different color every time a player touches the part.
- Moving upward, waiting for 3 seconds, then moving back to its previous position.
- Reducing the player's health the longer they stay on the part.

To demonstrate how this process works, this section of the tutorial shows you how to work with Assistant to make your first platform sparkle whenever a player jumps onto it.

To create a prompt for this behavior:

1. **OPTIONAL** Rename your first platform so that Assistant knows which part to create a script for.
  1. In the viewport, select your first platform.
  2. In the **Explorer** window, right-click the active object, then select Rename from the contextual menu.
  3. Type `GlitterPart`, then press **Enter**.
2. In the **Assistant** window, navigate to the **Enter request here** input, then type the following: `Add a new script that creates yellow sparkles while GlitterPart is touched`.
  > **Warning:** You can use a different color, but using different words might change the results.
3. Press **Enter**. Assistant starts generating a code sample, then a window displays with a suggested code sample that's similar to the following:```lua
local part = script.Parent
local sparkles = nil
local touchCount = 0

local function createSparkles()
    if not sparkles then
        sparkles = Instance.new("Sparkles")
        sparkles.Color = Color3.new(1, 1, 0) -- Yellow
        sparkles.Parent = part
    end
end

local function removeSparkles()
    if sparkles then
        sparkles:Destroy()
        sparkles = nil
    end
end

part.Touched:Connect(function(hit)
    touchCount = touchCount + 1
    createSparkles()
end)

part.TouchEnded:Connect(function(hit)
    touchCount = touchCount - 1
    if touchCount <= 0 then
        removeSparkles()
        touchCount = 0
    end
end)
```
  > **Info:** Assistant is constantly learning, so it might not always produce the same results for the exact same request.
4. Click **Accept**. As you learn more about coding with Luau, it will be easier to review Assistant's code samples to make sure they work for your use cases.

There is more than one right way to make any particular request, but every word counts. For example, the following chart shows how even slightly different word choices to the original prompt can produce different results.

| **Request Variationn** | **Possible Results** |
| --- | --- |
| `Create yellow sparkles while GlitterPart is touched.` | Assistant might show you the code, but not make a new script. It might also add the code to a random existing script. |
| `Make purple sparkles when the part named GlitterPart is stepped on.` | Assistant might make sparkles before GlitterPart is stepped on, or make only a few sparkles. |
| `Make GlitterPart sparkle` | Instead of adding a script, Assistant will just add a particle emitter (the object which makes sparkles) to GlitterPart. Which can be good if you want it to sparkle at all times. |

The fewer details you provide, the more unpredictable the results. For example, possible results for the prompt Make parts sparkle when you touch them may include:

- The resultant script not working at all.
- Only a single random part working.
- Parts sparkling before they are touched.

If you make a request and do not get the results you want, rephrase the request and try again.

> **Info:** Accidentally accept a suggestion that you didn't want? You can undo the change using one of the following methods: - For non-script changes, press `Ctrl``Z` or `⌘``Z`, depending on your computer. - If Assistant made a script, click on the script's name in the **Explorer** window, then press `Delete`.
## Playtest results

Although Assistant is constantly learning and getting better, it sometimes produces results that are different than you intended. You must always check the results of its suggestions to make sure they work as intended.

To playtest Assistant's results:

1. In the top-left corner of Studio, keep the default **Test** playtest option, then click the **Play** button. Studio enters playtest mode.
2. In the game, jump onto the first platform. If the code sample works correctly, yellow sparkles appear when your character touches the part.
3. When you're done verifying the results, return to the top-left corner of Studio, then click the **Stop** button. Studio exits playtest mode.
4. **OPTIONAL** Return to the Assistant window, then press the thumbs up or thumbs down icon to let Assistant know if the code sample worked as you intended.

Now that you know how to code with Assistant, try creating your own prompts to change how parts behave in your obby. When you're happy with your creation, move onto the next section of the tutorial to test and save your work to Roblox.
