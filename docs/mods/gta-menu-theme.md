# **GTA Menu Theme**

<div class="mod-hero" markdown>

![GTA Menu Theme preview](../assets/img/mods/steam/gta-menu-theme/preview.jpg){ .mod-icon }

<span class="pz-tag">B42</span><span class="pz-tag">SP/MP</span>

[:fontawesome-brands-steam-symbol: Steam Workshop](https://steamcommunity.com/sharedfiles/filedetails/?id=3836840382)

**Recommended Build:** 42.19+

</div>

## Overview

*'Bring Liberty to Louisville on your way to Leonida'*

GTA Menu Theme brings Music, Graphics and Menu styling inspired by the Grand Theft Auto series to Project Zomboid. A layered Slideshow places moving Backgrounds and Characters inside cut-out Frames composed from the Project Zomboid Map.

It requires [Menu Theme Framework (MTF)](../documentation/menu-theme-framework/index.md). The Theme runs on the Main Menu and its sub-screens. Its Music and Graphics stop when game loading begins.

## Gallery

<div class="gallery-grid" markdown>
</div>

## Features

- **Menu Music:** Choose from 11 handpicked Tracks from GTA III, Vice City, San Andreas, Liberty City Stories, Chinatown Wars, GTA IV and GTA V. Random mode plays the Tracks in shuffled order. Select one Track to loop it
- **Parallax Slideshow:** View 40+ Background and Character pairs inside cut-out Frames based on the Project Zomboid Map
- **Slideshow Animation:** Choose Horizontal Slide, Vertical Slide or Fade
- **Button Layouts:** Select Zomboid, Strip, Carousel, Horizontal Cards or Vertical Cards. All five Layouts support Mouse and Controller input. Use the Scroll Wheel to move through Cards and Carousel options
- **Menu Font:** Choose Barlow, Inter or the classic Zomboid Menu Font. If a selected Font does not support the current language, the game default Font is used
- **Menu Button Visibility:** Hide Main Menu options that are not needed. Exit remains visible
- **GTA Logo:** Replace the default Main Menu Logo with the optional GTA themed Logo
- **Intro Sequence:** Play a short intro once each time the game launches, or skip it from Menu Theme Settings
- **Hide Game Version:** Hide the game version line at the bottom of the Main Menu
- **Client-side Theme:** Change the Main Menu without adding Server code or modifying vanilla game files

## Mechanics

GTA Menu Theme registers with MTF. The Framework manages the Theme Settings window, Music controls and Main Menu Button Layouts. Only one Menu Theme can be active at a time through MTF.

The Slideshow layers Backgrounds, Character art and map cut-out Frames. The default animation moves each Slide horizontally. Vertical Slide and Fade are also available. The intro sequence plays once per game launch unless Skip Intro Sequence is on.

The Theme appears on the Main Menu and its sub-screens, including Solo, Multiplayer, Mods and Options. Music and Graphics stop when the game loading state begins. GTA Menu Theme runs on each Player's client and contains no Server code.

## Installation

Subscribe to Menu Theme Framework and GTA Menu Theme on Steam Workshop. Enable both from the Mods screen. In Multiplayer, enable both on each client that needs the themed Main Menu. The Theme is client-side and does not require Server-side code.

The Workshop IDs below can be added to a Server mod list when a host wants to distribute these client-side Mods through Steam Workshop. Server installation is optional.

```ini
Mods=ObnoxMenuThemeFrameworkB42;ObnoxGTAMenuThemeB42
WorkshopItems=3836836552;3836840382
```

## Configuration

Open **Menu Theme Settings** from the button at the bottom-left of the Main Menu. The window groups controls under Display, Audio, UI and Credits.

### Theme Display Settings

| Setting | Default | Range | Description |
|:---|:---|:---|:---|
| Slideshow Animation | Horizontal Slide | Horizontal Slide, Vertical Slide or Fade | Changes how the Slideshow moves between Scenes |
| Menu Font | Barlow | Barlow, Inter or Zomboid | Sets the Main Menu Button Font. Unsupported language scripts use the game default Font |
| Skip Intro Sequence | Off | On or Off | Skips the intro sequence at game launch when enabled |

### Main Menu Display Settings

| Setting | Default | Range | Description |
|:---|:---|:---|:---|
| Replace Main Menu Logo | On | On or Off | Replaces the vanilla Main Menu Logo with the GTA Logo |
| Hide Game Version | On | On or Off | Shows or hides the game version line |
| Button Layout | Horizontal Cards | Zomboid, Strip, Carousel, Horizontal Cards or Vertical Cards | Changes the position and style of the Main Menu Buttons |

### Audio Settings

| Setting | Default | Range | Description |
|:---|:---|:---|:---|
| Music Track | Random | Random or one of 11 Tracks | Random plays the Tracks in shuffled order. Selecting a Track plays it repeatedly |
| Music Volume | 30% | 0 to 100% | Sets the Main Menu Music volume |
| UI Sound Volume | 50% | 0 to 100% | Sets the Menu interface Sound volume |

The available Tracks are:

- IV - Loading Theme
- IV - Pause Theme
- SA - Main Theme
- V - Main Theme
- V - Loading Theme
- III - Main Theme
- LCS - Main Theme
- Vice - Main Theme
- SA - C.R.A.S.H Theme
- CW - Xin Shan's Theme
- V - No Happy Endings

### Menu Button Visibility

| Setting | Default | Range | Description |
|:---|:---|:---|:---|
| Main Menu Buttons | All shown | Show or Hide, except Exit | Hide Latest Save, Singleplayer, Load, Tutorial, Multiplayer, Co-op, Options, Mods, Workshop or Credits |

## Works With

| Mod | What It Adds |
|:---|:---|
| [Menu Theme Framework](../documentation/menu-theme-framework/index.md) | Required Framework for registering and displaying the Theme. MTF supplies the Settings window, Music controls and Button Layouts |

## Compatibility

| Build | SP | Hosted MP | Dedicated MP |
|:---:|:---:|:---:|:---:|
| 42.19+ | ✅ | ✅ | ✅ |
| 41 | ❌ | ❌ | ❌ |

!!! success "Does it require another Mod?"
    Yes. Menu Theme Framework is required

!!! success "Can it be added or removed from an existing Save?"
    Yes. It changes only client-side Main Menu Audio and Graphics. It stops at game loading, adds no gameplay data and does not modify vanilla game files

!!! success "Can it run with another Menu Theme?"
    Only one Theme is active at a time through MTF

!!! success "Can it run with other Mods that modify the Main Menu?"
    No. Other Mods that modify the Main Menu are listed as incompatible

!!! success "Does it support all resolutions and controllers?"
    Yes. It supports all Aspect Ratios, Resolutions and Font Sizes plus Controller input

!!! success "Does this Mod support 'X' Language?"
    Yes. It has translations for all supported Project Zomboid languages. Fonts that lack characters for a language fall back to the game default Font

## FAQ / Troubleshooting

!!! question "How Can the Main Menu Music Be Changed?"
    Open **Menu Theme Settings**, choose the **Audio** tab and select **Random** or one of the 11 Tracks. Random shuffles the playlist. A single Track repeats.

!!! question "How Can the Intro Be Skipped?"
    Open **Menu Theme Settings**, choose the **Display** tab and enable **Skip Intro Sequence**.

!!! question "Why Is Only One Menu Theme Active?"
    MTF runs one active Menu Theme at a time. The **Display** tab in **Menu Theme Settings** holds the Theme options and Button Layout.

!!! question "Does GTA Menu Theme Change Gameplay?"
    No. The Theme changes the Main Menu and its sub-screens. Its Music and Graphics stop when game loading begins.

## Credits

- Music remixes kindly provided by [1DERER1](https://www.youtube.com/@1DERER1)
- Special thanks to [RedChili - PZ Survivor Studio](https://pz-icon-maker.vercel.app/) and [Scrubblie](https://twitch.tv/scrubblie)

This is an unofficial fan-made Theme. It is not affiliated with or endorsed by Rockstar Games or Take-Two Interactive.

## Changelog

[:fontawesome-brands-steam-symbol: View Patch Notes](https://steamcommunity.com/sharedfiles/filedetails/changelog/3836840382)
