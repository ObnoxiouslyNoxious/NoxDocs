# Buttons and Layouts

## Buttons and Layouts

MTF owns the vanilla Main Menu Buttons. The Theme chooses **which Layouts to offer**. MTF handles the sizes, scrolling, hit boxes, hover and focus, the d-pad and mouse wheel. It also handles Buttons that other Mods add late.

---

## Layout Presets

```lua
layouts = {
    { id = "rail",  name = "IGUI_X_LayoutRail",  preset = "keep" },
    { id = "strip", name = "IGUI_X_LayoutStrip", preset = "strip" },
},
defaultLayout = "rail",
```

With **two or more** Layouts, the Menu Theme Settings window gets a **Button Layout** choice. `defaultLayout` is the one used until the Player picks; without it, the first Layout in the list is the default. With no `layouts` at all, the vanilla list is left alone.

| Field | Meaning |
|:---|:---|
| `id` | Unique key for the Layout (saved in the Player's Settings) |
| `name` | Display name, plain text or a translation key. Defaults to the `id` |
| `preset` | One of the presets below. Defaults to `"keep"`. An unknown preset prints a warning and uses `"keep"` |
| `layout` | Instead of a preset, a `function(ctx, buttons)` written by the Theme to place the Buttons itself |
| `cardWidth` | `cards` preset only: design width of one Card (overrides `cards.geometry.baseW`) |
| `cardOrientation` | `cards` preset only: `"vertical"` for a column on the left. Anything else is the horizontal row |
| `alignY` | `function(ctx)` returning a screen y. On a `keep` Layout the vanilla list moves, as a whole, up or down until the vertical centre of its middle visible Button sits at that y. On a vertical `cards` Layout the column of Cards is centred on that y. Return `nil` to leave things where they are. The list is never pushed past the bottom of the screen |
| `alignX` | `keep` Layout: `function(ctx)` returning the x of the list's left edge (where the Button text starts). Never left of the screen edge |
| `shiftY` | `keep` Layout: `function(ctx)` returning a number of pixels to move the vanilla list up (negative) or down from where vanilla puts it. Ignored when `alignY` is set |
| `carouselAlign` | `carousel` preset only: `"centre"` centres the row on the screen width. The default is bottom left, beside the options icon |
| `underLogo` | `cards` preset only: `false` lets a vertical column start at the top margin instead of staying below the Logo, for a Theme whose Logo is centred |

### Presets

| Preset | Result |
|:---|:---|
| `"keep"` | The vanilla list, left as the game draws it |
| `"strip"` | A bar along the bottom with the options as text in a row |
| `"carousel"` | One option shown at a time, with arrows either side |
| `"cards"` | Graphic Cards. A horizontal row by default, a vertical column with `cardOrientation = "vertical"` |

GTA Menu Theme offers all four, with two flavours of Cards:

From `GMT_Theme.lua`:

```lua
	layouts = {
		{ id = "rail", name = "IGUI_GMT_LayoutRail", preset = "keep", alignY = GMT_RailCentreY },
		{ id = "strip", name = "IGUI_GMT_LayoutStrip", preset = "strip" },
		{ id = "carousel", name = "IGUI_GMT_LayoutCarousel", preset = "carousel" },
		{ id = "cards_wide", name = "IGUI_GMT_LayoutCardsWide", preset = "cards", cardWidth = 1228 },
		{ id = "cards_vertical", name = "IGUI_GMT_LayoutCardsVertical", preset = "cards", cardOrientation = "vertical" },
	},
```


In the `rail` Layout above, `alignY` is `GMT_RailCentreY`, a function GTA Menu Theme defines. It returns the vertical centre the list should sit on (a little below the middle of the window), or `nil` when the window is not close to 16:9. `nil` leaves the list where vanilla puts it.

### Placing the Buttons

A Layout function runs when the Layout is first applied and again whenever a Mod adds, removes, shows or hides a Main Menu Button. Players can also hide Buttons themselves in the Menu Theme Settings window (UI tab, see [Settings and Translations](settings-and-translations.md#the-menu-theme-settings-window)); a hidden Button is left out of the list. Use:

```lua
ctx.menu.buttons()                 -- list of { element, id, group = "play"/"system"/"mods", visible }
ctx.menu.moveButton(element, x, y) -- move one button label (the original position is restored on a layout change)
ctx.menu.layoutId()                -- the active layout id
ctx.menu.restoreButtons()          -- put every moved button back where vanilla placed it
```

`hooks.onLayoutChange(ctx, layoutId)` fires when the Layout is first applied to a Main Menu and whenever the choice changes.

### Telling MTF Where the Art Ends

The Strip is centred halfway between the bottom of the Theme's art and the bottom of the screen. Report where the art ends every frame it is laid out:

```lua
ctx.menu.setArtBottom(y)          -- screen y where the art ends
ctx.menu.freeRect()               -- { x, y, w, h } of the screen area not covered by the buttons, or nil
```

`freeRect()` is how a Theme fits a Graphic or a frame into the space the Buttons leave over (GMT fits its frame to the right of the vertical Cards with it).

---

## Highlights

The hover highlight of the vanilla list, the Strip and the Carousel can use the Theme's caption art instead of vanilla's grey box. Set these in `menu`:

| Field | Usage |
|:---|:---|
| `listHighlight` | `"caption"`: the vanilla list's hover highlight is the painted caption bar (`media/ui/cards/captions/<Prefix>_Caption.png`). `"white"`: a solid white box, like the Strip and the Carousel, with the text turning black |
| `stripHighlight` | `"caption"`: the Strip's and the Carousel's hover highlight is the painted caption bar, with the text left as it is |
| `listHighlightTint` | `{ r, g, b }`: tint of the caption art when used as a highlight |
| `listHighlightPad` | Pixels, making the highlight the longest Button text plus this much on each side instead of vanilla's box |

---

## The Button Font

Draw the vanilla Buttons in the Theme's own font. `menu.buttonFont` is a font name, or a **function** that returns the font (and optionally a check texture). A function lets a Player Setting pick the font live:

From `GMT_Theme.lua`:

```lua
local BUTTON_FONTS = {
    inter = { "MainMenu1", "media/fonts/EN/mainfont_0.png" },
    barlow = { "MainMenu2", "media/fonts/EN/mainfont2_0.png" },
}

local function GMT_ButtonFont()
    local choice = MTF_Settings.get("GMT.MenuFont")
    local font = BUTTON_FONTS[choice]
    if not font then
        return nil
    end
    return font[1], font[2]
end
```


Used as:

```lua
menu = { holdUntilReady = true, holdMusic = true, buttonFont = GMT_ButtonFont },
```

`menu.buttonFontCheck` names the font's atlas. MTF only switches when that texture loads, falling back to vanilla instead of drawing nothing if the font file is missing. Ship the fonts in `media/fonts/EN/`. **The font file names are fixed** (`mainfont.fnt` and `mainfont2.fnt`, with their atlases) and cannot be prefixed. See [Files MTF Finds by Name](reference.md#files-mtf-finds-by-name).

---

## Holding the Menu for an Intro

With `menu = { holdUntilReady = true }`, the vanilla Buttons panel and the Theme's Logo stay hidden from the first frame until the Theme releases them. Release both when the intro is done, or the Player has no Main Menu.

```lua
ctx.menu.releaseLogo(1000)     -- show the logo, fading in over 1000 ms
ctx.menu.releaseButtons()      -- show the vanilla buttons (and the options button)
ctx.menu.panelBounds()         -- x, y, w, h of the buttons panel, or nil
ctx.menu.logoReleased()        -- booleans, for the Theme's own state
ctx.menu.buttonsReleased()
```

Release before anything that can fail (such as loading an Image that might be missing). A mistake then can never leave the Main Menu hidden. This is how GTA Menu Theme decides when its Buttons may show:

From `GMT_MainMenuSlideshow.lua`:

```lua
local function tryShowMenuButtons(mainScreen, now)
    if menuButtonsReleased or not currentCtx or not isRootTitleMenu(mainScreen) then
        return
    end
    if not menuButtonsReadyMs then
        menuButtonsReadyMs = now
    end
    if now - menuButtonsReadyMs >= (GMT_Config.MENU_BUTTON_DELAY_MS or 0) then
        menuButtonsReleased = true
        currentCtx.menu.releaseButtons()
    end
end
```


### Once per Launch

Many intros should play on a fresh launch but not each time the Player quits a game back to the Main Menu. A quit to the Main Menu rebuilds Lua, wiping anything kept in memory. MTF keeps a marker in a file instead.

```lua
if ctx.boot.isFirstMenuThisLaunch() then
    ctx.boot.markShown()
    -- start the intro here
end
```

Call `isFirstMenuThisLaunch()` once at the start and store the answer. Do not call it every frame, as it reads a file.

### Detecting a New Menu

Every time the Player returns to the Main Menu there is a new MainScreen. Compare `ctx.screen` with the one seen last to restart per-visit state:

```lua
local run = nil
local function renderBackground(ctx)
    if not run or run.screen ~= ctx.screen then
        run = { screen = ctx.screen, startMs = ctx.now }
    end
    local elapsed = ctx.now - run.startMs
    -- ...
end
```

---

## Menu Holding versus Reveal Style

`holdUntilReady` is a mechanism, with the Theme deciding **when** to release. How the Buttons then appear (fade, slide) is style. See [Logo and Reveal](cards-and-styling.md#logo-and-reveal).

---

## Other Menu Helpers

```lua
ctx.menu.setVersionLineHidden(true)   -- hide the "Version 42.x" line at the bottom of the title screen
```

The click on that line (which copies the git revision) is removed along with its text. It is safe to call every frame and affects the title screen only. Players can also hide the line themselves with **Hide Game Version** in the Menu Theme Settings window.

---
