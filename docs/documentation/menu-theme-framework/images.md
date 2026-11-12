# Graphics

## Graphics

MTF offers two ways to put Graphics on the Main Menu:

| Approach | Use it when |
|:---|:---|
| `backgrounds = { ... }` | A Slideshow of Images is enough. MTF cycles and transitions them |
| `render.background = function(ctx)` | The Theme draws everything itself, such as layers, parallax, intros, blends and Video |

---

## Slideshow: `backgrounds`

The Slideshow reads from a list of Image paths. It is used only when the Theme does **not** supply `render.background`. Images are cover-scaled (they fill the screen and are cropped), PNG only.

```lua
backgrounds = {
    "media/ui/backgrounds/bg1.png",
    "media/ui/backgrounds/bg2.png",
},
```

To pick up numbered files automatically:

```lua
backgrounds = MenuThemeFramework.discoverImages("media/ui/backgrounds/bg_%d.png", 20),
```

`discoverImages(pattern, maxCount)` tries `bg_1.png`, `bg_2.png` and so on and stops at the first missing one (or at 99 when `maxCount` is left out). It loads each file it finds. Probe only Images the Theme will show.

Timing and transition come from `Config` and the Player's Slideshow Animation Setting in Menu Theme Settings:

| Key | Default |
|:---|:---|
| `Config.TRANSITION_STYLE` | `"slide"` (Horizontal Slide), `"slidedown"` (Vertical Slide) or `"fade"` |
| `Config.TRANSITION_DURATION_MS` | `350` (each half of a transition) |
| `Config.BACKGROUND_DURATION_MS` | `15000` (how long each Image is shown) |

---

## Drawing: `render`

```lua
render = {
    background = function(ctx) end,   -- before vanilla's menu
    foreground = function(ctx) end,   -- after vanilla's menu, root title menu only
},
```

The Draw Order, every frame:

```text
1. MTF notes any change of screen or size
2. render.background      (the Theme)
3. the Logo               (MTF)
4. the vanilla Main Menu  (the base game: Buttons, panels)
5. render.foreground      (the Theme, Title Menu only)
```

- `background` runs on the Main Menu screen and every sub-screen of the Main Menu (the Title Menu and screens opened from it such as New Game, Options or Mods), from the very first frame. It never runs in game. Draw an opaque layer first to hide vanilla's Main Menu background.
- `foreground` runs only on the [Title Menu](glossary.md#title-menu).

### Drawing Toolbox

| Call | Usage |
|:---|:---|
| `ctx.tex(path)` | Cached `getTexture`; returns `nil` if the file is missing |
| `ctx.drawCover(tex, alpha, offsetX, offsetY, r, g, b)` | Cover-scales a texture to fill the screen, optionally offset and tinted |
| `ctx.screen:drawRect(x, y, w, h, a, r, g, b)` | A filled rectangle |
| `ctx.screen:drawTextureScaled(tex, x, y, w, h, a, r, g, b)` | A texture at an exact rectangle |
| `ctx.draw.withBlend(mode, fn)` | Runs `fn` with a GL blend mode, then restores normal blending |
| `ctx.screen:setStencilRect(x, y, w, h)` / `clearStencilRect()` | Clip drawing to a rectangle (useful for reveals) |
| `ctx.now` | A millisecond clock, for animation |

A simple Background with a black underlay and one Image:

```lua
local function renderBackground(ctx)
    ctx.screen:drawRect(0, 0, ctx.width, ctx.height, 1, 0, 0, 0)    -- black underlay
    local img = ctx.tex("media/ui/rdr_a.png")
    if img then
        ctx.drawCover(img, 1)                                       -- alpha 1
    end
end
```

Apply a slow drift using `now`:

```lua
local t = (ctx.now % 20000) / 20000            -- 0..1 over 20 seconds
ctx.drawCover(img, 1, -40 * t, 0)               -- pan 40 px left over the cycle
```

Preload large Images when the Theme File loads. The first frame that needs them then does not stall:

```lua
getTexture("media/ui/bg1.png")
```

GTA Menu Theme keeps a small texture cache of its own Graphics. Repeated lookups then never call the game again:

From `GMT_MainMenuSlideshow.lua`:

```lua
local function loadTexture(path)
    if not path then return nil end
    if textureCache[path] == nil then
        local loadStart = getTimestampMs()
        textureCache[path] = getTexture(path) or false
        local loadMs = getTimestampMs() - loadStart
        if textureCache[path] == false then
            GMT_dprint("failed to load texture: %s (took %dms)", path, loadMs)
        else
            GMT_dprint("loaded texture %s in %dms (t=%d, +%dms since file load)",
                path, loadMs, getTimestampMs(), getTimestampMs() - GMT_fileLoadMs)
        end
    end
    return textureCache[path] or nil
end
```


### Graphics Scaling and Resolution (`ctx.layout`)

The **design area** is the largest 16:9 rectangle that fits the window, centred. On a 16:9 window it is the whole screen. On an ultrawide it is a centred 16:9 region. On a tall window it is limited by width.

| Field | Meaning |
|:---|:---|
| `refW`, `refH` | Design-area size in pixels |
| `originX`, `originY` | Where the design area starts |
| `uiScale` | `refW / Config.LAYOUT_REFERENCE_WIDTH` (default reference 1920: `uiScale` is 1 on a 1080p window) |

```lua
local size = 200 * ctx.layout.uiScale   -- 200 px at 1080p, 400 px at 4K
```

Set `Config.LAYOUT_REFERENCE_WIDTH = 3840` for art drawn for a 4K screen. `Config.LAYOUT_DESIGN_ASPECT` (default `16 / 9`) sets the shape of the design area.

### Blend Modes

`ctx.draw.withBlend(mode, fn)` changes how `fn`'s draws combine with what is already on screen, then restores normal alpha blending.

| Mode | Effect |
|:---|:---|
| `"alpha"` | Normal transparency |
| `"additive"` | Adds light (glows, light leaks) |
| `"multiply"` | Darkens by the layer's colours (grain, vignette, stains) |

RDR Menu Theme lays a wet-plate Graphic over the Video with a multiply blend:

From `RMT_Theme.lua`:

```lua
	if videoPlate then
		local plate = ctx.tex(videoPlate)
		if plate then
			ctx.draw.withBlend("multiply", function()
				ctx.drawCover(plate, 1)
			end)
		end
	end
```


`mode` can also be raw GL enums, `{ src, dst }` for `glBlendFunc`, or `{ srcRGB, dstRGB, srcAlpha, dstAlpha }` for `glBlendFuncSeparate`. Call it only inside a render callback. Keep `fn` to a few draws, as an error inside it skips the restore until the next frame. An unknown mode name prints a warning and draws without a blend change.

### Base Game Limitations

Build 42 gives Lua **no shaders, no colour matrices, no true overlay or soft-light blend and no blur**.

- Bake colour grading into the Images.
- Fake blur with pre-blurred copies cross-faded together (the intro sequences of GTA Menu Theme and RDR Menu Theme do this, as do RDR Menu Theme's Cards).
- Use stencils to reveal or crop.

### Complete Background Example

A black-to-image fade loop with a setting for the cycle length and a held intro, built from the calls above:

```lua
require "MTF_Core"

local IMAGE = "media/ui/emt_background.png"
getTexture(IMAGE)

local run = nil

local function renderBackground(ctx)
    ctx.screen:drawRect(0, 0, ctx.width, ctx.height, 1, 0, 0, 0)

    -- every time the player returns to the menu there is a new MainScreen
    if not run or run.screen ~= ctx.screen then
        run = { screen = ctx.screen, startMs = ctx.now, music = false, logo = false, buttons = false }
    end
    local elapsed = ctx.now - run.startMs

    -- release the menu first, so a missing image can never leave it hidden
    if not run.music then
        run.music = true
        ctx.music.start()
    end
    if not run.logo and elapsed >= 2000 then
        run.logo = true
        ctx.menu.releaseLogo(1000)
    end
    if not run.buttons and elapsed >= 3000 and ctx.isRootTitleMenu() then
        run.buttons = true
        ctx.menu.releaseButtons()
    end

    local img = ctx.tex(IMAGE)
    if not img then
        return
    end
    local cycleMs = ctx.settings.getNumber("CycleSeconds") * 1000
    local t = (elapsed % cycleMs) / cycleMs                 -- 0..1
    local fade = math.min(1, t / 0.1, (1 - t) / 0.1)        -- in over 10%, out over 10%
    ctx.drawCover(img, fade)
end

MenuThemeFramework.registerTheme({
    id = "ExampleMenuTheme",
    name = "IGUI_EMT_Title",
    credits = { { header = "Theme Created by:", rows = { "Your Name" } } },
    music = { { "EMT_MenuTrack_1", "Dusty Road", 162000 } },
    render = { background = renderBackground },
    settings = {
        { key = "CycleSeconds", type = "slider", default = 20, min = 10, max = 60, step = 2, label = "IGUI_EMT_Cycle" },
    },
    menu = { holdUntilReady = true, holdMusic = true },
})
```

---

## Logos

MTF always hides vanilla's own Logo and draws one itself, fading in over `Config.LOGO_FADE_IN_MS`.

- Ship `media/ui/logos/<assetPrefix>_Menu_Logo.png` to use the Theme's own Logo (`assetPrefix` defaults to the Theme's `id`; set `assetPrefix = "EMT"` for `EMT_Menu_Logo.png`). The Player can turn it off with **Replace Main Menu Logo** in the Menu Theme Settings window, which shows MTF's bundled vanilla-style Project Zomboid Logo instead.
- With no Logo file, MTF shows that vanilla-style Logo. Pick which one with `vanillaLogo = "plain"` (default) or `"stroke"` (the black-outlined variant, as GMT uses).
- Size: `Config.LOGO_DISPLAY_HEIGHT` pixels at `LAYOUT_REFERENCE_WIDTH` of design-area width, scaling with the window. If it is `nil`, the Logo texture's own height is used.
- Slide, placement and Logo variants are style, covered in [Logo and Reveal](cards-and-styling.md#logo-and-reveal).

---

## Settings Icon

A Button at the bottom left of the Main Menu opens the Menu Theme Settings window. Ship `media/ui/icons/<assetPrefix>_Options_Icon.png` (240x240 recommended) to replace the bundled icon. It scales with the window and hides when the Player enters a sub-menu. How far it dims when idle is the style field `optionsButton.idleAlpha` (see [Cards and Styling](cards-and-styling.md#the-strip-the-arrows-and-the-settings-button)).

---

## Card Graphics

When the Theme offers a `cards` Layout, each Button shows a Graphic. MTF looks for them in this order:

1. A texture shipped for exactly that Button, by convention name, `media/ui/cards/backgrounds/<assetPrefix>_Card_<BUTTONID>.png`. With `assetPrefix = "EMT"` the Solo Button's Card is `EMT_Card_SOLO.png`. The Button ids, as shown by `ctx.menu.buttons()`, are LATESTSAVE, CREDITS, TUTORIAL, SOLO, OPTIONS, MULTIPLAYER, COOP, MODS, WORKSHOP, EXIT, LOAD.
2. The Theme's own pick, the `cardPhoto` callback.
3. A shipped default, `media/ui/cards/backgrounds/<assetPrefix>_Card_Default.png`. If none is found, the Card has no Graphic.

With the greyscale twin turned on (`cards.look.greyTwin`), MTF looks beside each Graphic for the same name with `_g` before the extension (`bg_solo.png` gives `bg_solo_g.png`). The Card rests in greyscale and the colour Graphic fades in on selection.

`cardPhoto` is a function from the Button id to a texture path, or `nil`:

From `GMT_Theme.lua`:

```lua
    cardPhoto = function(buttonId)
        if GMT_Slideshow and GMT_Slideshow.claimCardBackground then
            return GMT_Slideshow.claimCardBackground(buttonId)
        end
        return nil
    end,
```


GTA Menu Theme ships a pair per Button (`bg_<name>.png`, with a `_g` greyscale twin for the resting state) in `backgrounds/cards/`, plus cut-out characters in `characters/cards/`. It falls back to a random Slideshow Image when a pair is missing.

---

## Memory Usage

Every Image has two costs. Its **file size** sets how large the Workshop download is. Its **video memory** is the space it takes up on the graphics card once loaded.

### Video Memory

The game decodes every texture to 4 bytes per pixel and pads each side up to the next power of two (256, 512, 1024, 2048, 4096 and so on). The padded size is what counts:

| Image size | Stored as | Video memory |
|:---|:---|:---|
| 1024x1024 | 1024x1024 | 4 MB |
| 1920x1080 | 2048x2048 | 16 MB |
| 2048x1024 | 2048x1024 | 8 MB |
| 2560x1440 | 4096x2048 | 32 MB |
| 3640x2048 (GTA Menu Theme's Backgrounds) | 4096x2048 | 32 MB |
| 3840x2160 (4K) | 4096x4096 | 64 MB |

- A side slightly over a power of two doubles that side. 1080 pixels tall costs the same as 2048 tall. 2100 wide costs the same as 4096 wide.
- File compression and colour count do not change video memory. A 3 MB posterized PNG and a 30 MB PNG of the same size take the same space once loaded.
- With the game's Texture Compression option on (the default), the graphics driver usually stores textures smaller than this. How much smaller is up to the driver. Plan for the full figure.
- `ctx.tex` and MTF cache every texture they load, keeping a loaded Image in memory for the rest of the session. Count every Image the Theme loads, including those found by `discoverImages`.

### Recommended Sizes

- **Backgrounds:** 1920x1080 is sharp on a 1080p screen (16 MB each). For 4K screens, up to 4096x2048 costs 32 MB, the same as 2560x1440. Going smaller within the same power of two saves nothing.
- **Cut away empty space.** GTA Menu Theme cropped its character art from 3640x2048 to 1840x2048, halving each from 32 MB to 16 MB. Across its 43 characters that saved about 688 MB.
- **Keep flat Graphics tiny.** A solid colour or a simple gradient can be a very small Image stretched with `drawTextureScaled`. GTA Menu Theme's black frame is 64x36.
- **Keep pools small.** Load only what a phase shows. GTA Menu Theme keeps only 8 of its frames loaded at a time.

### File Size

PNG file size decides the download, not the video memory. Posterizing (reducing an Image to a palette of 256 colours or fewer, saved as an indexed PNG) cuts it sharply. GTA Menu Theme ships 157 Images, most of them 3640x2048, posterized to 64 colours for Backgrounds and characters and 256 colours for Cards. All of them together come to about 153 MB on disk.

- Check posterized Images at full size. Smooth gradients such as skies can show bands at low colour counts. Raise the count for those Images.
- Use `.png` for every Image. `.jpg` files can fail to load.

---
