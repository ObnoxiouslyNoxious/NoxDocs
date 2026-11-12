# Menu Theme Framework

Menu Theme Framework (MTF) is a Lua-only Framework for Build 42 that hosts Main Menu Themes. A Menu Theme Mod registers itself with a single call and the Framework supplies everything else needed to replace the look and sound of the Main Menu, allowing Theme Authors to focus on their Graphics and Music.

---

## Introduction

This is a reference for building a **Main Menu Theme** with Menu Theme Framework. It is written as a Guide. Start at the first page and work through them in order to build a Theme from scratch, or jump straight to the section that holds the information required. Readers new to Lua or modding should start with [First Steps](getting-started.md#first-steps).

MTF decides **how** the Main Menu Theme works (the Hook, the Draw Order, the Buttons, the Audio, the Settings and so on). The Theme decides **how it looks and sounds**. A Theme that declares nothing gets a plain, working Main Menu. Everything beyond that is something the Theme opts into or creates itself.

!!! info "At a Glance"
    Every Theme needs three files at a minimum:

    - **The Theme File** (`media/lua/client/EMT_Theme.lua`): the `registerTheme` call.
    - **The Config File** (`media/lua/shared/EMT_Config.lua`): Image paths, timings and Video.
    - **The Sound Script** (`media/scripts/EMT_Sounds.txt`): one entry per Audio File.

!!! info "Three Themes to Use as Examples"
    - **[Menu Theme Template (MTT)](https://steamcommunity.com/workshop/filedetails/?id=3836836552){target="_blank"}**: A Template shipped inside MTF and also available as a [direct download](https://github.com/ObnoxiouslyNoxious/NoxDocs/releases/download/menu-theme-template/MenuThemeTemplate.zip) with the same files. It provides a working Menu Theme with Audio, Images and Video, intended as the base for a new Menu Theme.
    - **[GTA Menu Theme (GMT)](https://steamcommunity.com/sharedfiles/filedetails/?id=3836840382){target="_blank"}**: A Menu Theme built on Images. It contains a multi-layered parallax Slideshow, an intro sequence, Card Buttons with backgrounds and characters, Music and movement code.
    - **[RDR Menu Theme (RMT)](https://steamcommunity.com/sharedfiles/filedetails/?id=3836837888){target="_blank"}**: A Menu Theme built on Video. It contains Video sources, an intro sequence, synchronised ambient Audio Tracks and Music.

---

## Index

| Page | Contents |
|:---|:---|
| [Getting Started](getting-started.md) | First Steps, the File Tree, `mod.info`, the Config File and Minimal Theme Examples for Image and Video |
| [Audio](audio.md) | Music Tracks, the Sound Script, UI Sounds, Intro Sounds, Volume and Playback |
| [Graphics](images.md) | Backgrounds, Slideshows, Drawing Code, Blend Modes, Logo, Icons and Card Graphics |
| [Video](video.md) | Playing a Bink Video, Paired Video and Audio Playlists, the Fallback Image and the Requirements |
| [Buttons and Layouts](buttons-and-layouts.md) | Layouts (Rail, Strip, Carousel, Cards), Holding and Releasing the Menu, Highlights and Button Fonts |
| [Cards and Styling](cards-and-styling.md) | Every Style Table with its Plain Default and the Painter Slots |
| [Settings and Translations](settings-and-translations.md) | Player Settings for the Theme, the Menu Theme Settings Window, Credits and Translation Keys |
| [Reference](reference.md) | `registerTheme` Fields, the `ctx` Object, Hooks, Helpers and `Config` |
| [Troubleshooting](troubleshooting.md) | Symptoms and Fixes, Debug Output and the Shipping Checklist |
| [Glossary](glossary.md) | The terms these pages use |

---

## MTF Feature, Mechanism & Design Philosophy

MTF controls the Mechanism of each Feature. The Theme controls its Design.

| Feature | MTF Mechanism | Theme Design |
|:---|:---|:---|
| **Menu Hook** | The single Hook, the Draw Order and holding and releasing the Main Menu | How the Background, Logo and Intro look and when they are released |
| **Button Layouts** | Rail, Strip, Carousel and Cards (sizes, scrolling, hit boxes, hover and focus, d-pad and mouse wheel support, late-added Mod Buttons) | Which Layouts to offer and every number in the Style Tables |
| **Button Entrance** | Layout geometry settling before the Buttons are displayed | How the Buttons animate in, such as fading or sliding |
| **Audio and Settings** | Music playback (playlist, fades, resume across a Lua reload), UI Sounds, Settings and the Menu Theme Settings window | Which Tracks to use and the Theme's own Settings |
| **Painter Slots** | Stencils, texture loading, text fitting and the drift helper | What gets drawn in the Slots, such as Graphics, overlays, text, shapes and Video |

Only one Theme can be active at a time. The first Theme to register wins. Any other is ignored and listed in the Menu Theme Settings window as inactive. With no Theme installed, MTF does nothing and the vanilla Main Menu looks and sounds untouched.

---

## Framework Rules

- **Build 42, Lua 5.1 (Kahlua).**
- **Client side only.** The Theme File lives in `media/lua/client/` and its Config File in `media/lua/shared/`.
- **Texture paths** start at `media/` and include the sub-folder and extension (`media/ui/bg1.png`).
- **Images are `.png`.** `.jpg` files can fail to load.
- **The base game gives Lua no shaders, no colour matrices, no true overlay or soft-light blend and no blur.** Bake colour grading into the Images and Video. See [Graphics](images.md).
- **MTF does not catch errors in Theme callbacks.** An error inside a callback repeats every frame. Guard every value that can be `nil`, such as a texture that failed to load.

---
