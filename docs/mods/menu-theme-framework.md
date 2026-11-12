# **Menu Theme Framework**

<div class="mod-hero" markdown>

![Menu Theme Framework preview](../assets/img/mods/steam/menu-theme-framework/preview.jpg){ .mod-icon }

<span class="pz-tag">B42</span><span class="pz-tag">SP/MP</span><span class="pz-tag">Framework</span>

[:fontawesome-brands-steam-symbol: Steam Workshop](https://steamcommunity.com/sharedfiles/filedetails/?id=3836836552)

**Recommended Build:** 42.19+

</div>

## Overview

*'Build your own Main Menu Theme with custom Audio, Image and Video. No Java. No Manual Installation.'*

Menu Theme Framework (MTF) hosts compatible Main Menu Theme Mods for Build 42. A Theme registers with MTF, which supplies the Title Menu hook, Button Layouts, Audio playback, Logo handling and a Settings window. MTF has no visible effect until a Theme registers.

The Workshop item also includes the Menu Theme Template as a separate Mod. It is a working example with comments for Theme Authors to copy and adapt.

!!! tip "Creating a Theme?"
    Start with the [Menu Theme Framework Guide](../documentation/menu-theme-framework/index.md) for the file tree, Theme registration, Settings and full API reference.

## Gallery

<div class="gallery-grid" markdown>

</div>

## Features

- **Title Menu Hook:** Themes draw before and after the vanilla Menu Buttons
- **Image and Video Backgrounds:** A Background Slideshow, or custom Video with its own Sound
- **Button Layouts:** The vanilla list, a Strip, a Carousel or Horizontal and Vertical Cards
- **Mouse and Controller Support:** Every Layout works with a Mouse or Controller. X or Square opens Menu Theme Settings
- **Theme Styling:** Cards, the Strip, Arrows, the Logo and Menu transitions are styled through Style Tables
- **Music Playback:** A Theme playlist with fade-in, shuffle and Track selection
- **Replacement UI Sounds:** Custom click, hover and launch Sounds with their own volume control
- **Logo Handling:** The vanilla Logo is hidden and the Theme's Logo shown, with a vanilla-style Logo when a Theme provides none
- **Settings Window:** Display, UI, Audio and Credits tabs, opened from the Title Menu
- **Menu Theme Template:** A bundled working Theme Mod showing registration, Images, Video, Music, Cards and Settings
- **Resolution Support:** Theme elements scale to every aspect ratio, resolution and Font Size
- **No File Replacements:** Lua only, with no changes to vanilla game files and no manual installation
- Translations for all supported Project Zomboid languages

## Mechanics

MTF activates when a Theme calls `MenuThemeFramework.registerTheme`. The first Theme to register controls the Title Menu. Other Themes are listed as ignored in Menu Theme Settings. With no Theme registered, MTF leaves the vanilla Menu unchanged.

MTF wraps the Title Menu's drawing step. A Theme can draw its Background before the vanilla Menu Buttons and draw its overlay after them. MTF manages the chosen Button Layout, Music, UI Sounds, Logo and Settings window.

Music and Video Sound use the game's shared UI Emitter. Random Music plays every Track once in a shuffled order. While Theme Music or Video Sound is playing, MTF silences the game's Music and Sound Effects volume. It restores the live values before the game leaves the Title Menu without changing the Player's saved Audio settings.

While a Theme is active, MTF switches **Do Video Effects** off on the Title Menu and draws a black layer beneath the Theme to prevent the vanilla Menu Video from playing underneath. MTF restores the Player's saved setting before the Options screen, the Select Spawn Location screen and the Game Loading state. If the Player has Do Video Effects turned off, a Theme Video shows its supplied still frame instead.

Background Images scale to cover and centre on the screen. Build 42 gives Lua no access to shader, blur or colour effects. Bake those effects into the Image itself. Themes with custom Bink Video require Build 42.22 or later. Each Video clip uses a separate Sound file because the base game does not play Bink Video audio. Themes can loop one clip or sequence several clips with an optional fade through black.

MTF keeps Settings locally, with a separate `MTF_Settings.txt` file for each Theme under `Zomboid/Lua/MenuThemeFramework/`.

## Installation

### Singleplayer

Subscribe to Menu Theme Framework on Steam Workshop. Enable MTF and a compatible Theme Mod from the Mods screen. MTF on its own leaves the vanilla Menu unchanged.

### Hosted or Dedicated Multiplayer

Menu Theme Framework runs on the Player's client and has no Server code. Enable it locally with a compatible Theme to use the themed Title Menu. The Server has no MTF gameplay logic.

### Mod Identifiers

| Item | Value |
|:---|:---|
| Workshop ID | `3836836552` |
| Framework Mod ID | `ObnoxMenuThemeFrameworkB42` |
| Bundled Template Mod ID | `ObnoxMenuThemeTemplateB42` |

The bundled Menu Theme Template requires Menu Theme Framework. Enable the Template by itself to view its example Theme.

## Configuration

Open **Menu Theme Settings** with the button at the bottom left of the Title Menu or press X on a Controller. The available controls depend on the active Theme.

### Display Settings

| Setting | Default | Range | Description |
|:---|:---|:---|:---|
| Button Layout | Theme-selected | Theme-defined | Select a Layout when the Theme offers two or more |
| Theme Settings | Theme-defined | Theme-defined | Change options supplied by the active Theme |
| Slideshow Animation | Horizontal Slide | Horizontal Slide, Vertical Slide or Fade | Choose how a list of Background Images transitions |
| Replace Main Menu Logo | On | On or Off | Show the Theme Logo when one is provided |
| Hide Game Version | On | On or Off | Show or hide the version text on the Title Menu |

Slideshow Animation appears when MTF is managing the Theme's Background slideshow. Replace Main Menu Logo appears when the Theme provides a convention Logo.
An active Theme can override the Framework default for Slideshow Animation.

### Menu Settings

| Setting | Default | Range | Description |
|:---|:---|:---|:---|
| Show/Hide Menu Buttons | All visible | On or Off per Button | Choose which vanilla Menu Buttons appear |

### Audio Settings

| Setting | Default | Range | Description |
|:---|:---|:---|:---|
| Music Track | Random | Random or a Theme Track | Choose a Track from the active Theme's playlist |
| Music Volume | 30% | 0 to 100% | Set the Theme Music volume |
| Video Sound Volume | 50% | 0 to 100% | Set Video Sound volume when the Theme uses Video Sound |
| UI Sound Volume | 50% | 0 to 100% | Set replacement UI Sound volume, with output gain up to 300% |

Music, Video Sound and UI Sound use the Framework defaults above unless the active Theme supplies Config overrides. Each Theme can set its own Settings defaults and default Button Layout. MTF saves Settings locally for each Theme.

## Works With

- [GTA Menu Theme](gta-menu-theme.md): Uses MTF to provide its GTA-inspired Main Menu Theme
- [RDR Menu Theme](rdr-menu-theme.md): Uses MTF to provide its Red Dead Redemption Main Menu Theme

## Compatibility

| Build | SP | Hosted MP | Dedicated MP |
|:---:|:---:|:---:|:---:|
| 42.19+ | ✅ | ✅ | ✅ |
| 41 | ❌ | ❌ | ❌ |

Themes that provide custom Bink Video need Build 42.22 or later. MTF runs on the client only and contains no server code.

Only one Theme is active at a time. Any other installed Theme is listed as inactive in the Menu Theme Settings window.

!!! success "Is this Mod safe to add to or remove from existing Saves?"
    Yes. It only changes the Title Menu and does not touch Save data.

!!! success "Is this Mod compatible with 'X' Mod?"
    Compatible with Mods that add Main Menu Buttons. Not compatible with Mods that replace the Main Menu's Background, Logo, Music or Video, or restyle or move its Buttons.

!!! success "Does this Mod support 'X' Language?"
    Yes. It has translations for all supported Project Zomboid languages.

## FAQ / Troubleshooting

!!! question "Why Does the Main Menu Look Unchanged?"
    MTF is a Framework, not a Theme. Enable a Theme Mod that requires MTF, such as GTA Menu Theme or RDR Menu Theme.

!!! question "What Happens When More Than One Theme Is Installed?"
    The first Theme to register controls the Title Menu. MTF lists other registered Themes as ignored in Menu Theme Settings.

!!! question "Can a Theme's Video Run on Every Build?"
    No. Custom Bink Video requires Build 42.22 or later. MTF supports Build 42.19 and later. Themes can provide a still frame when Video playback is unavailable or disabled.

!!! question "Where Are Settings Saved?"
    MTF stores Settings locally under `Zomboid/Lua/MenuThemeFramework/`, with a separate `<theme folder>/MTF_Settings.txt` file for each Theme.

## Changelog

[:fontawesome-brands-steam-symbol: View Patch Notes](https://steamcommunity.com/sharedfiles/filedetails/changelog/3836836552)
