# Glossary

## Glossary

The terms these pages use, in alphabetical order. Pages link a term here the first time they use it.

---

## Terms

### Base Game

Project Zomboid as it ships, without Mods. "The base game" also stands for behaviour that comes from the game's own code rather than from MTF or a Theme.

### Config

A Lua table of values. **MTF's Config** is `MenuThemeFramework.Config` (timings, volumes, sizes; see [Reference](reference.md#menuthemeframeworkconfig)). **A Theme's Config File** (`EMT_Config.lua`) is the Theme's own table of Image paths, timings and Video, kept apart from the Theme File.

### Convention File

A file MTF finds by its name and folder instead of a path, such as `EMT_Menu_Logo.png`. See [Files MTF Finds by Name](reference.md#files-mtf-finds-by-name).

### Cover-Scaled

Scaled, keeping its shape, until it fills the whole screen. Anything that overflows is cropped. The opposite of fitting the whole Image inside the screen.

### `ctx`

The table MTF passes to every Theme callback. It holds the screen, its size, a clock and every MTF call a Theme can make. See [The `ctx` Object](reference.md#the-ctx-object).

### Design Area

The largest 16:9 rectangle that fits the window, centred. Sizes in the Style Tables are given in design pixels at a 1920-wide design area and scale with it. See [Graphics Scaling and Resolution](images.md#graphics-scaling-and-resolution-ctxlayout).

### Draw Order

The order MTF and the base game draw each frame, starting with the Theme's Background, then the Logo, the vanilla Main Menu and finally the Theme's foreground. See [Drawing](images.md#drawing-render).

### Fallback Still

The `.png` shown in place of a Video when the Video cannot play (an older build, or Video Effects off).

### Hold and Release

With `menu.holdUntilReady`, the Buttons and Logo stay hidden (held) until the Theme releases them. See [Holding the Menu for an Intro](buttons-and-layouts.md#holding-the-menu-for-an-intro).

### Layout

How the Main Menu Buttons are arranged, as the vanilla list (`keep`), a Strip, a Carousel or Cards. A Theme offers one or more and the Player picks. See [Buttons and Layouts](buttons-and-layouts.md).

### Lua Reload

The game rebuilding its Lua environment, for example after accepting the Mods screen or quitting a game to the Main Menu. Anything a Theme keeps only in memory is lost.

### Paired Clip

A Video and a Sound declared together in the Theme's `video` table, started and restarted together by `ctx.video.play`. See [Video](video.md#paired-video-audio-ctxvideoplay).

### Painter Slot

A function a Theme gives MTF to draw one piece of a Card, the Strip or an arrow in its own way. MTF still owns the size, input and behaviour. See [Painter Slots](cards-and-styling.md#painter-slots).

### Prefix

The Theme's short Abbreviation used at the start of its files and translation keys (`EMT` in this Guide). Set as `assetPrefix`.

### Reveal

How the Buttons appear once shown, waiting for the Layout to settle and then fading or sliding in. See [Logo and Reveal](cards-and-styling.md#logo-and-reveal).

### Style Table

One of the tables (`logo`, `reveal`, `cards`, `strip`, `arrows`, `optionsButton`) that set how MTF's pieces look. See [Cards and Styling](cards-and-styling.md).

### Theme Author

The person making a Menu Theme.

### Title Menu

The first screen of the Main Menu, with the main list of Buttons. Screens opened from it (New Game, Options, Mods and so on) are sub-screens. Some MTF behaviour runs only on the Title Menu (also called the root title menu).

### Vanilla

The base game's own version of something, such as the vanilla Logo or the vanilla Main Menu Video.

---
