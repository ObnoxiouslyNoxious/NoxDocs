# Getting Started

## Getting Started

This Guide calls its example Theme 'Example Menu Theme', with EMT as its Abbreviation/Prefix. Any names work. Sections that need a set name say so.

---

## First Steps

This section assumes no Lua or modding experience. It turns Menu Theme Template (MTT) into a first Theme without writing any code. The rest of the documentation assumes the reader can read and edit Lua.

1. **Find the Mods folder.** Mods in development live in the Zomboid folder, under `Zomboid/Workshop/<ModName>/Contents/mods/<ModName>/`. On Windows the Zomboid folder is `C:\Users\<Name>\Zomboid`.
2. **Get the Template.** Subscribe to [Menu Theme Framework](https://steamcommunity.com/sharedfiles/filedetails/?id=3836836552){target="_blank"} on the Steam Workshop, as every Theme needs it to run. Menu Theme Template comes in two forms with identical contents. Use either the `MenuThemeTemplate` folder inside the MTF download (`Steam/steamapps/workshop/content/108600/3836836552/mods/`), copied into `Zomboid/Workshop/` in the layout shown in [The File Tree](#the-file-tree), or the **[Menu Theme Template zip](https://github.com/ObnoxiouslyNoxious/NoxDocs/releases/download/menu-theme-template/MenuThemeTemplate.zip)**, which unzips straight into `Zomboid/Workshop/`.
3. **Rename it.** Change the folder name, then `name` and `id` in both `mod.info` files. Do this before enabling it, as until then it shares its `id` with the Template inside MTF. Keep the `require=ObnoxMenuThemeFrameworkB42` line. Replace the `MTT` prefix in every file name and inside the files with a new Prefix, such as `EMT`.
4. **Swap in new Images and Music.** Put new Images in `media/ui/backgrounds/` and new `.ogg` files in `media/sounds/`. Either keep the Template's file names or change the paths in the Config File (`EMT_Config.lua`) and the Sound Script (`EMT_Sounds.txt`).
5. **Enable it.** Start the game, open **Mods**, enable Menu Theme Framework and the new Mod, then accept. The game reloads Lua and returns to the Main Menu.
6. **Check the result.** The new Images and Music should play, with the Menu Theme Settings Button at the bottom left of the screen.
7. **If nothing changes,** open `Zomboid/console.txt` and look for lines starting `[MTF][WARNING]` or `[MTF][ERROR]`. They name the file or setting at fault. See [Troubleshooting](troubleshooting.md).

---

## The File Tree

This is the File Tree of a Menu Theme Mod. At a minimum it needs two Lua files (the Theme File `EMT_Theme.lua` and the Config File `EMT_Config.lua`), the two `mod.info` files, the Sound Script, an Image and an Audio File. Everything under `ui/` is optional and found by name or by the path given.

```text
ExampleMenuTheme/
└── Contents/
    └── mods/
        └── ExampleMenuTheme/
            ├── mod.info
            ├── poster.png
            ├── icon.png
            ├── common/
            │   └── media/
            │       └── lua/
            │           └── shared/
            │               └── Translate/
            │                   └── EN/
            │                       └── IG_UI.json     Translations (Optional)
            └── 42/
                ├── mod.info                           Identical to the root mod.info
                └── media/
                    ├── lua/
                    │   ├── client/
                    │   │   └── EMT_Theme.lua          The Theme (the registerTheme call)
                    │   └── shared/
                    │       └── EMT_Config.lua         The Theme's Config (Images, Timings, Video)
                    ├── scripts/
                    │   └── EMT_Sounds.txt             Sound definitions for the Music
                    ├── sounds/
                    │   └── EMT_MenuTrack_1.ogg        The Music
                    ├── videos/
                    │   ├── emt_intro.bik              Optional: a Bink Video (see Video)
                    │   └── emt_intro.bik.png          Optional: its fallback still Image (the Video's file name plus .png)
                    ├── fonts/
                    │   └── EN/                        Optional: a Button font (the file names are fixed, see Buttons and Layouts)
                    └── ui/
                        ├── logos/
                        │   └── EMT_Menu_Logo.png      Optional, found by name
                        ├── icons/
                        │   └── EMT_Options_Icon.png   Optional, found by name (240x240)
                        └── backgrounds/               The Images
```

The File Tree of GTA Menu Theme:

```text
GTAMenuTheme/
└── Contents/
    └── mods/
        └── GTAMenuTheme/
            ├── mod.info
            ├── poster.png
            ├── icon.png
            ├── common/
            │   └── media/
            │       └── lua/
            │           └── shared/
            │               └── Translate/   IG_UI.json for each language
            └── 42/
                ├── mod.info
                ├── poster.png
                ├── icon.png
                └── media/
                    ├── fonts/
                    │   └── EN/              The two button fonts (1x to 4x)
                    ├── lua/
                    │   ├── client/          GMT_Theme.lua, GMT_Cards.lua, GMT_MainMenuSlideshow.lua ...
                    │   └── shared/          GMT_Config.lua ...
                    ├── scripts/
                    │   └── GMT_Sounds.txt   Every sound the Theme defines
                    ├── sounds/              GMT_Song_*.ogg (the Music), GMT_LogoAudio.ogg and GMT_ZomboidIntroAudio.ogg
                    └── ui/
                        ├── backgrounds/
                        ├── cards/
                        ├── characters/
                        ├── frames/
                        ├── layout/
                        └── logos/
```

!!! info "Notes"
    - The Theme File goes in `media/lua/client/` and the Config File in `media/lua/shared/` (see [Framework Rules](index.md#framework-rules)).
    - Keep the values (Image paths, timings, Video) in the Config File and `require` it from the Theme File, as GTA Menu Theme, RDR Menu Theme and Menu Theme Template do.
    - Keep `42/mod.info` identical to the root `mod.info`.
    - Texture paths start at `media/` and must include the extension. They go straight to `getTexture()` unchanged.
    - Avoid plain file names such as `Theme.lua` or `Config.lua`. A Prefix reduces the chance of a file name collision with another Mod.
    - A few files must use a set name and folder, such as the Logo, the Settings icon, Card Graphics and the Button fonts. Each section marks them. [Reference](reference.md#files-mtf-finds-by-name) lists them all.
    - Before uploading, run the [shipping checklist](troubleshooting.md#before-uploading).

---

## `mod.info`

Both copies, in the root folder and in `42/`:

```ini
name=Example Menu Theme
id=ExampleMenuThemeB42
description=An Example for Menu Theme Framework.
poster=poster.png
author=MenuThemeAuthor
icon=icon.png
require=ObnoxMenuThemeFrameworkB42
loadAfter=ObnoxMenuThemeFrameworkB42
versionMin=42.19.0
modversion=1.0.0
```

---

## Minimal Theme Examples

Below are two minimal Themes, one built on Images and one built on Video. Each is complete. MTF itself only needs an `id`, a `name` and something to draw.

### Image Theme

A Slideshow of Images and one Music Track. MTF cycles the Images, cover-scaled, with a slide transition.

`media/lua/shared/EMT_Config.lua`:

```lua
EMT_Config = {}

EMT_Config.BG_IMAGES = {
    "media/ui/backgrounds/bg1.png",
    "media/ui/backgrounds/bg2.png",
}
```

`media/lua/client/EMT_Theme.lua`:

```lua
require "MTF_Core"
require "EMT_Config"

MenuThemeFramework.registerTheme({
    id = "ExampleMenuTheme",
    name = "Example Menu Theme",
    credits = {
        { header = "Theme Created by:", rows = { "Your Name" } },
    },
    backgrounds = EMT_Config.BG_IMAGES,
    music = {
        { "EMT_MenuTrack_1", "Dusty Road", 162000 },
    },
})
```

`media/scripts/EMT_Sounds.txt`:

```text
module Base
{
    sound EMT_MenuTrack_1
    {
        category = Ambient,
        master = Primary,
        loop = true,
        volume = 1.0,
        is3D = false,
        clip
        {
            file = media/sounds/EMT_MenuTrack_1.ogg,
        }
    }
}
```

With the Mod enabled, the Main Menu shows the two Images in turn with the Track playing.

!!! warning "Avoid Putting Comments in a Sound Script"
    A comment can silently stop Sounds registering. Keep Sound Scripts bare, exactly as above.

### Video Theme

A looping Video with its own Sound. The Video and its Sound are declared as a pair in the Config File.

`media/lua/shared/EMT_Config.lua`:

```lua
EMT_Config = {}

EMT_Config.VIDEO = {
    mode = "random",
    clips = {
        {
            video = "EMT_Menu_Clip.bik",
            still = "media/videos/EMT_Menu_Clip.bik.png",
            sound = "EMT_Menu_Clip",
            width = 1920,
            height = 1080,
        },
    },
}
```

`media/lua/client/EMT_Theme.lua`:

```lua
require "MTF_Core"
require "EMT_Config"

MenuThemeFramework.registerTheme({
    id = "ExampleMenuTheme",
    name = "Example Menu Theme",
    credits = {
        { header = "Theme Created by:", rows = { "Your Name" } },
    },
    video = EMT_Config.VIDEO,
    render = {
        background = function(ctx)
            ctx.screen:drawRect(0, 0, ctx.width, ctx.height, 1, 0, 0, 0)
            ctx.video.play()
        end,
    },
})
```

`media/scripts/EMT_Sounds.txt`:

```text
module Base
{
    sound EMT_Menu_Clip
    {
        category = Ambient,
        master = Primary,
        loop = true,
        volume = 1.0,
        is3D = false,
        clip
        {
            file = media/sounds/EMT_Menu_Clip.ogg,
        }
    }
}
```

The Video goes in `media/videos/` as `EMT_Menu_Clip.bik`, along with its fallback still Image `EMT_Menu_Clip.bik.png`. The fallback Image is shown when the Player has Video Effects disabled. The Sound goes in `media/sounds/` as `EMT_Menu_Clip.ogg`. Custom Video needs Build 42.22 or later. On older builds MTF shows the still Image while the Sound plays. See [Video](video.md) for the requirements.

---
