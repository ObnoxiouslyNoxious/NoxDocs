# Reference

## Reference

Every `registerTheme` field, the `ctx` object, the Hooks, the helper functions, the files MTF finds by name and every `Config` value, in one place.

---

## `registerTheme`

```lua
MenuThemeFramework.registerTheme({ ... })
```

Returns `true` on success, `false` if the table is invalid or another Theme already owns MTF. Registering again with the **same** `id` (a Lua reload) replaces the Theme (see [Reloading While Working](troubleshooting.md#reloading-while-working)).

| Field | Type | Required | Covered in |
|:---|:---|:---|:---|
| `id` | string | **yes** | below |
| `name` | string | no | below |
| `assetPrefix` | string | no | below |
| `settingsFolder` | string | no | below |
| `modId` | string | no | below |
| `config` | table of `Config` keys | no | [`MenuThemeFramework.Config`](#menuthemeframeworkconfig) |
| `video` | `{ mode, clips, fadeMs }` | no | [Video](video.md) |
| `vanillaLogo` | `"plain"` or `"stroke"` | no | [Graphics](images.md#logos) |
| `cardPhoto` | `function(buttonId)` | no | [Graphics](images.md#card-graphics) |
| `credits`, `creditsFooter` | list | no | [Settings and Translations](settings-and-translations.md#credits) |
| `backgrounds` | list of paths | no | [Graphics](images.md) |
| `music` | list | no | [Audio](audio.md#music) |
| `musicKindSetting` | string (a Setting `key`) | no | [Audio](audio.md#track-kinds-and-repeat-one) |
| `musicRepeatOne` | boolean | no | [Audio](audio.md#track-kinds-and-repeat-one) |
| `render` | `{ background, foreground }` | no | [Graphics](images.md#drawing-render) |
| `hooks` | table of callbacks | no | below |
| `settings` | list | no | [Settings and Translations](settings-and-translations.md#player-settings) |
| `layouts`, `defaultLayout` | list, string | no | [Buttons and Layouts](buttons-and-layouts.md) |
| `menu` | table | no | below |
| `logo`, `reveal`, `cards`, `strip`, `arrows`, `optionsButton` | Style Tables | no | [Cards and Styling](cards-and-styling.md) |

### Every Field at Once

A commented outline of a Theme that sets every field. Only `id` is required.

```lua
MenuThemeFramework.registerTheme({
    id = "ExampleMenuTheme",                 -- required, unique
    name = "IGUI_EMT_Title",                 -- window title (plain text or a translation key)
    assetPrefix = "EMT",                     -- prefix of the files MTF finds by name
    settingsFolder = "ExampleMenuTheme",     -- folder for this Theme's saved files
    modId = "ExampleMenuThemeB42",           -- mod.info id: the window shows the Mod's icon
    config = { MUSIC_VOLUME = 0.3 },         -- MenuThemeFramework.Config values for this Theme

    backgrounds = { "media/ui/backgrounds/bg1.png" },   -- built-in Slideshow (ignored with render.background)
    render = {
        background = function(ctx) end,      -- before the vanilla Main Menu
        foreground = function(ctx) end,      -- after it, Title Menu only
    },
    vanillaLogo = "plain",                   -- or "stroke", used when no Logo file is shipped
    cardPhoto = function(buttonId) return nil end,

    music = { { "EMT_MenuTrack_1", "Dusty Road", 162000, "song" } },
    musicKindSetting = "MusicType",
    musicRepeatOne = false,
    video = { mode = "random", fadeMs = 0, clips = { } },

    settings = { },                          -- see Settings and Translations
    credits = { { header = "Theme Created by:", rows = { "Your Name" } } },
    creditsFooter = { },

    layouts = { { id = "rail", name = "IGUI_EMT_LayoutRail", preset = "keep" } },
    defaultLayout = "rail",

    menu = {
        holdUntilReady = false,
        holdMusic = false,
        disableVideoEffects = true,
        buttonFont = nil,
        buttonFontCheck = nil,
        listHighlight = nil,                 -- "caption" or "white"
        stripHighlight = nil,                -- "caption"
        listHighlightTint = nil,             -- { r, g, b }
        listHighlightPad = nil,              -- pixels
    },
    hooks = {
        onEnter = function(ctx) end,
        onLeave = function(ctx) end,
        onResize = function(ctx) end,
        onFrontEndChange = function(ctx, isRoot) end,
        onLayoutChange = function(ctx, layoutId) end,
    },

    logo = { }, reveal = { }, cards = { }, strip = { }, arrows = { }, optionsButton = { },   -- Style Tables
})
```

### `id`

A unique string. It names the Theme's Settings (`<id>.<key>`), its once-per-launch marker and, unless `assetPrefix` is set, its convention files (see [Files MTF Finds by Name](#files-mtf-finds-by-name)). Use letters, digits and underscores.

### `name`

The Menu Theme Settings window title, shown upper case. Plain text or a translation key.

### `assetPrefix`, `settingsFolder` and `modId`

| Field | Meaning |
|:---|:---|
| `assetPrefix` | The prefix of the Theme's convention art files (`EMT_Menu_Logo.png` and so on). Default: the Theme's `id`. A short, unique prefix reduces the risk of two Themes colliding on a file name |
| `settingsFolder` | The folder, inside `Zomboid/Lua/MenuThemeFramework`, that holds this Theme's own saved files (Settings, Music resume point, Video state, boot marker). Default: the Theme's `id` |
| `modId` | The id in the Theme's `mod.info`. The Menu Theme Settings window shows the Mod's icon under its title |

### `menu`

| Field | Meaning |
|:---|:---|
| `holdUntilReady` | Hide the vanilla Buttons and the Theme's Logo until the Theme releases them ([Buttons and Layouts](buttons-and-layouts.md#holding-the-menu-for-an-intro)) |
| `holdMusic` | Do not start the first Track until `ctx.music.start()` ([Audio](audio.md#setting-a-music-delay-holdmusic)) |
| `disableVideoEffects` | `false` keeps the vanilla Main Menu Video and its layers visible. By default MTF stops the vanilla Main Menu Video for every Theme ([Video](video.md#zomboids-menu-video)) |
| `buttonFont` | A font name, or `function(ctx)` returning the font and optionally its atlas ([Buttons and Layouts](buttons-and-layouts.md#the-button-font)) |
| `buttonFontCheck` | The font's atlas. The font is only applied if it loads |
| `listHighlight` | `"caption"` or `"white"`: the vanilla list's hover highlight ([Buttons and Layouts](buttons-and-layouts.md#highlights)) |
| `stripHighlight` | `"caption"`: the Strip's and the Carousel's hover highlight |
| `listHighlightTint` | `{ r, g, b }` tint of the caption art used as a highlight |
| `listHighlightPad` | Pixels either side of the longest Button text for the highlight |

### `hooks`

Each receives `ctx`.

| Hook | When |
|:---|:---|
| `onEnter(ctx)` | The Main Menu is entered |
| `onLeave(ctx)` | The Player leaves the Main Menu for a game |
| `onResize(ctx)` | The window size changed |
| `onFrontEndChange(ctx, isRoot)` | The Player moved between the Title Menu (`true`) and a child screen (`false`) |
| `onLayoutChange(ctx, layoutId)` | A Layout was first applied to a Main Menu, or the choice changed |

---

## The `ctx` Object

One table, reused all session and refreshed before every callback. Treat it as read-only.

| Field | Meaning |
|:---|:---|
| `ctx.screen` | The MainScreen (use its `drawRect`, `drawTextureScaled` and so on) |
| `ctx.width`, `ctx.height` | Window size in pixels |
| `ctx.now` | A millisecond clock (for timing and animation) |
| `ctx.entered` | Whether the Main Menu has been entered |
| `ctx.layout` | `refW`, `refH`, `originX`, `originY`, `uiScale` ([Graphics](images.md#graphics-scaling-and-resolution-ctxlayout)) |
| `ctx.tex(path)` | Cached `getTexture`; `nil` if the file is missing |
| `ctx.drawCover(tex, alpha, offsetX, offsetY, r, g, b)` | Cover-scales a texture over the screen |
| `ctx.coverFrame(focusY, screenFocus, refW, refH)` | Cover-scales a 1920x1080 canvas with row `focusY` at `screenFocus` of the screen height; returns `x, y, scale` ([Video](video.md#video-with-overlay)) |
| `ctx.draw.withBlend(mode, fn)` | Runs `fn` with a GL blend mode, then restores normal blending |
| `ctx.video.draw(filename, srcW, srcH, alpha, offsetX, offsetY, fit, anchor, freeze, still)` | Plays a Bink Video cover-scaled or, with `fit = "cropped"`, scaled to the screen width. `fit` may also be a `{ x, y, w, h }` rect ([Video](video.md#render-draw-ctxvideodraw)) |
| `ctx.video.play(opts)` | Plays the Theme's paired Video and Sound clips as a random, ordered or shuffled playlist. `opts` defaults to the Theme's `video` table ([Video](video.md#paired-video-audio-ctxvideoplay)) |
| `ctx.video.stop()` | Stops the playlist and its Sound and closes the Video |
| `ctx.settings.get / getNumber / getBoolean(key)` | Read a Setting |
| `ctx.isRootTitleMenu()` | True on the Title Menu |
| `ctx.music.start / skip / currentTrack` | Music control ([Audio](audio.md#setting-a-music-delay-holdmusic)) |
| `ctx.boot.isFirstMenuThisLaunch / markShown` | The once-per-launch marker |
| `ctx.dprint(fmt, ...)` | Debug print, only when `Config.DEBUG` is true |

### `ctx.menu`

| Call | Meaning |
|:---|:---|
| `releaseLogo(fadeMs)` | Show the Logo, fading in |
| `releaseButtons()` | Show the vanilla Buttons and the Settings Button |
| `logoReleased()`, `buttonsReleased()` | Booleans for the Theme's own state |
| `panelBounds()` | `x, y, w, h` of the Buttons panel, or `nil` |
| `buttons()` | The list of Main Menu Buttons (`element`, `id`, `group`, `visible`) |
| `moveButton(element, x, y)` | Move one Button label |
| `restoreButtons()` | Put every moved Button back where vanilla placed it |
| `layoutId()` | The active Layout id |
| `freeRect()` | The screen area the Buttons leave free |
| `setArtBottom(y)` | Report where the Theme's art ends (centres the Strip) |
| `setVersionLineHidden(hidden)` | Hide the vanilla "Version 42.x" line on the title screen |

---

## Files MTF Finds by Name

Most paths are the Theme's to choose, as anything given to MTF as a path (`backgrounds`, Music, Video, `cardPhoto`) is used exactly as written. The files below are different. MTF finds them **by name and folder**, making these names required.

`<Prefix>` is the Theme's `assetPrefix` or its `id`, as MTF tries both (see [`assetPrefix`](#assetprefix-settingsfolder-and-modid)). Each is tried as written, in upper case and in lower case, letting both `EMT_Menu_Logo.png` and `emt_menu_logo.png` load. The words can be `Capitalised_Words`, `lower_words` or `UPPER_WORDS`. Other mixes are not found.

| Art | Folder | File name | Notes |
|:---|:---|:---|:---|
| Main Menu Logo | `media/ui/logos/` | `<Prefix>_Menu_Logo.png` | Shown when **Replace Main Menu Logo** is on |
| Settings Button icon | `media/ui/icons/` | `<Prefix>_Options_Icon.png` | 240x240. A bundled icon is used if absent |
| Strip bar | `media/ui/layout/` | `<Prefix>_Strip.png` | A plain black bar if absent |
| Scroll arrow | `media/ui/layout/` | `<Prefix>_Arrow_H.png` | Facing left, 64x64 or 128x128 |
| Vertical Cards arrow | `media/ui/layout/` | `<Prefix>_Arrow_V.png` | Wide and short, facing up, 256x64 |
| Card Graphic | `media/ui/cards/backgrounds/` | `<Prefix>_Card_<BUTTONID>.png` | One per Button, for example `EMT_Card_SOLO.png` |
| Default Card Graphic | `media/ui/cards/backgrounds/` | `<Prefix>_Card_Default.png` | Used by any Card with no Graphic of its own |
| Card greyscale twin | Beside the Graphic | The Graphic's name with `_g` before the extension | Only with `cards.look.greyTwin` |
| Card caption bar | `media/ui/cards/captions/` | `<Prefix>_Caption.png`, or `<Prefix>_Caption_Left.png`, `_Middle.png` and `_Right.png` | One Graphic, or all three at the same height |
| Video fallback still | `media/videos/` | `<video file>.png`, for example `emt_loop.bik.png` | Unless the clip sets `still` |
| Button fonts | `media/fonts/EN/` | `mainfont.fnt` and `mainfont2.fnt` with their atlases | See below |
| Translations | `common/media/lua/shared/Translate/<LANG>/` | `IG_UI.json` | The folder and file name are the game's |

The convention art above must be `.png` and keep its extension. If a file is not in its folder, MTF also tries `media/ui/cards/` (for Card Graphics and caption bars) and then `media/ui/` itself. A Theme may keep everything flat.

**Fonts cannot be prefixed.** The game only lets a Mod replace font files it already has. The fixed names are `mainfont.fnt` (the `MainMenu1` slot) and `mainfont2.fnt` (`MainMenu2`), each with its atlas (`mainfont_0.png`, `mainfont2_0.png`). They come in five size tiers, one per Font Size option, in `media/fonts/EN/` (smallest) and `media/fonts/EN/1x` to `4x`. A path is shared by every Mod that ships it. If two Mods ship `mainfont.fnt`, the one that loads last wins, whichever Theme is active.

---

## Helper Functions

| Function | Use |
|:---|:---|
| `MenuThemeFramework.isRootTitleMenu(screen)` | True on the Title Menu only (false on New Game, Mods, spawn selection, character creation). The screen argument is optional |
| `MenuThemeFramework.hasTheme()` | Whether a Theme is registered |
| `MenuThemeFramework.discoverImages(pattern, maxCount)` | Probe numbered Images (`maxCount` defaults to 99) |
| `MenuThemeFramework.conventionTexture(suffix)` | Path of the convention file with that name (see [Files MTF Finds by Name](#files-mtf-finds-by-name)) if shipped, else `nil` |
| `MenuThemeFramework.themeStyle()` | The resolved Style Tables (read-only), with the Theme's values merged over the plain defaults |
| `MenuThemeFramework.cardDrift(card, coverW, coverH, factor)` | Drift offset for a Card layer |
| `MenuThemeFramework.fitText(text, font, maxW, maxH)` | Fits a label into a box using a smaller font, two lines, then an ellipsis |
| `MenuThemeFramework.playClickSound()` / `playHoverSound()` / `playLaunchSound()` | MTF's replacement UI Sounds |

---

## `MenuThemeFramework.Config`

Pass the Theme's own values as `config = { ... }` in `registerTheme`. MTF applies them only when the Theme is the active one. Writing to `MenuThemeFramework.Config` directly would also change another Theme's values. Defaults shown.

| Key | Default | What it does |
|:---|:---|:---|
| `TRANSITION_STYLE` | `"slide"` | Built-in Slideshow transition: `"slide"` (Horizontal Slide), `"slidedown"` (Vertical Slide) or `"fade"`. Only a starting default, as the Player's choice wins |
| `TRANSITION_DURATION_MS` | `350` | Length of each half of a transition (out, then in) |
| `BACKGROUND_DURATION_MS` | `15000` | How long each built-in Background shows |
| `MUSIC_FADE_IN_MS` | `3000` | Fade-in of a Track when it starts |
| `MUSIC_VOLUME` | `0.3` | Default Music volume, 0 to 1 (the Player can change it) |
| `VIDEO_VOLUME` | `0.5` | Default volume of a Video clip's paired Sound, 0 to 1 (the Player has a slider for it) |
| `VIDEO_COVER_FADE_MS` | `1000` | How long a clip's black cover takes to fade away once the Video has started (0 = at once) |
| `VIDEO_COVER_FRAMES` | `12` | The Video counts as started after it has been drawn playing for this many frames... |
| `VIDEO_COVER_MIN_MS` | `400` | ...and at least this long |
| `VIDEO_COVER_STILL_FRAMES` | `30` | With no Video playing (the Player has Video Effects off) the still counts as ready after this many frames |
| `VIDEO_COVER_MAX_MS` | `4000` | The cover is never held longer than this |
| `VIDEO_BOUNDARY_HOLD_MS` | `150` | How long the screen stays fully black after the next Video opens, between chained clips with `fadeMs` |
| `VIDEO_FADE_IN_MS` | `3000` | How long a Video clip's paired Sound takes to fade in when the Main Menu opens, in milliseconds (0 = none). It does not fade again at each clip restart |
| `LOGO_FADE_IN_MS` | `1000` | Logo fade-in |
| `LOGO_DISPLAY_HEIGHT` | `nil` | Logo height in pixels at the reference width; `nil` = the texture's own height |
| `LAYOUT_DESIGN_ASPECT` | `16 / 9` | Shape of the design area (see [Graphics Scaling and Resolution](images.md#graphics-scaling-and-resolution-ctxlayout)) |
| `LAYOUT_REFERENCE_WIDTH` | `1920` | Design-area width that sizes are authored for. Set 3840 for art drawn for 4K |
| `UI_SOUND_VOLUME` | `1.5` | Default loudness (a gain) of the Main Menu click, hover and launch Sounds |
| `UI_SOUND_MAX_GAIN` | `3` | The Settings slider's 100% is this gain (3.0 = three times the recorded file) |
| `BLEND_RESTORE` | `{ 770, 771 }` | GL blend function restored after `ctx.draw.withBlend` (leave alone) |

`MUSIC_VOLUME`, `VIDEO_VOLUME`, `UI_SOUND_VOLUME` and `TRANSITION_STYLE` are only starting defaults. Once a Player changes them in the Menu Theme Settings window, the Player's values apply.

`DEBUG` (default `false`) is not read from `config`. Set `MenuThemeFramework.Config.DEBUG = true` directly while developing. Ship it as `false` (see [Troubleshooting](troubleshooting.md#debugging)).

---
