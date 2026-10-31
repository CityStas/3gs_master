---
title: "Create bundled installers"
url: /docs/en-us/education/support/creating-bundled-installers
last_updated: 2026-10-30T19:55:43Z
description: "Install Roblox Studio on multiple computers for schools or summer camps."
---

# Create bundled installers

For organizations looking to install Roblox Client or Studio on multiple computers, we offer bundled installers. Normally, an installer is used on individual computers, but this can be difficult if you're looking to mass install Roblox, or Roblox Studio on multiple computers.

To help in this process, you can create your own bundled installer, giving you a traditional executable that can be installed on multiple computers. This can then be used in software deployment and imaging tools.

## Create the bundler

The following instructions are applicable to **Windows** computers.

1. Install [Roblox Studio](https://www.roblox.com/create) on your computer.
2. Open the **Command Prompt**. You can do this by clicking the Windows start icon. Then type `CMD` and click on the Command Prompt application.
3. Find the installation of Roblox on your computer. You need the executable of what you'll be creating a bundle for. This will typically be in:`C:\Users\userName\AppData\Local\Roblox\Versions`
  > **Info:** If you have multiple versions, you'll have both Roblox Studio and Client. To find which one includes the executable, open the folders and check for either RobloxStudio.exe or RobloxPlayerLauncher.exe.
4. In the Command Prompt, go to the location of the Roblox executable to use by typing `cd`, then the file path. and then `Enter`. For example:`cd C:\Users\userName\AppData\Local\Roblox\Versions\version-6d02431b656044a6`
5. Depending on the installer you want to create, type the file name, followed by -bundle, like below, and press `Enter`.```bash
RobloxStudioLauncherBeta.exe -bundle
RobloxPlayerLauncher.exe -bundle
```
6. Let the bundler work until it closes.This will create a bundled installer in the same folder as the Roblox executable with a file name such as: `RobloxStudioLauncherBeta_version-6d02431b656044a6.exe`.
