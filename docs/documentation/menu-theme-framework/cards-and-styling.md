# Cards and Styling

## Cards and Styling

MTF decides how things work, never how they look. A Theme that declares no style gets a **plain, working Main Menu**, with no Logo slide, Buttons that fade in over 400 ms and Cards that are a Graphic with a caption bar and an instant white outline. Everything else is something the Theme turns on, with plain Style Tables in the same `registerTheme` call.

!!! info "Mistakes Are Reported, Not Fatal"
    Every Style Table is validated once at registration. An unknown field or a value of the wrong type is printed to the console as a warning and ignored. A typo can never break the Main Menu.

---

## GTA Menu Theme Sets All of It

This is the complete style block GMT passes to `registerTheme`. Every field is explained in the tables below.

From `GMT_Theme.lua`:

```lua
	-- GMT's own motion (MTF's defaults are plain: no slide, no fade): the logo slides down into place while it fades in,
	-- and the buttons wait for the layout to settle, then fade in and slide (vertical cards from the left, the rest from below)
	logo = { slide = 0.35, place = GMT_LogoPlace },
	reveal = { waitForLayout = true, settleMs = 100, fadeMs = 1000, slide = "auto" },
	-- GMT's card look (MTF's plain cards have none of this): unselected cards grow to 70% of the way up to full height
	-- (resting at half of it) and widen 1.5x (vertical); photos are dimmed and, with a _g twin, rest in greyscale and fade
	-- to colour; a soft inner shadow, a slanted caption bar end, a white outline that fades in after the growth, and the
	-- slow glide of photo and character on selection
	cards = {
		geometry = { restFraction = 0.5, growFraction = 0.7, expandFactor = 1.5 },
		look = {
			dim = 0.45, greyTwin = true, greyTone = 0.2, captionAlpha = 1, restTextGrey = 0.3, captionSlant = 4 / 15,
			shadow = true, restCaption = { slant = 4 / 15, padX = 44 },
			outline = { delayMs = 250, inMs = 200, outMs = 100, thickness = 3 },
		},
		motion = { smoothMs = 70, colorFadeMs = 2000, drift = true },
		-- the characters standing on the cards (GMT_Cards.lua); MTF draws everything else of a card
		paint = { layers = GMT_Cards.layers },
	},
	strip = { fadeFraction = 0.10, alpha = 0.85 },
	arrows = { idleTone = 0.18, hoverTone = 0.32 },
	-- the settings icon sits much dimmer until the mouse is over it
	optionsButton = { idleAlpha = 0.3 },
```


---

## Logo and Reveal

The Logo and the Buttons can animate in. By default the Logo does not slide and the Buttons fade in over 400 ms.

`reveal` applies only while one of MTF's Layout presets is active. With no `layouts`, the vanilla Buttons appear as the base game draws them.

| Field | Type | Plain default | What it does |
|:---|:---|:---|:---|
| `logo.slide` | number | `0` | How far above its place the Logo starts, as a fraction of its own height, while it fades in (0 = no slide) |
| `logo.place` | function or `false` | `false` (off) | `function(ctx, w, h, uiScale) return x, y end`: where the Logo goes. `false` keeps vanilla's own spot |
| `logo.path` | function or `false` | `false` (off) | `function(ctx)` returning a Logo texture path (for example picked by a Setting), or `nil` for the normal Logo |
| `reveal.waitForLayout` | boolean | `true` | Hold the vanilla Buttons (drawn at zero opacity) until the Layout's geometry has stopped changing. They never show compacted and then grow. This is a mechanism rather than a look, which is why it defaults to on |
| `reveal.settleMs` | number | `100` | How long the geometry must stay unchanged before the Buttons appear (ms) |
| `reveal.maxHoldMs` | number | `6000` | Never hold longer than this, whatever the geometry does (ms) |
| `reveal.ready` | function or `false` | `false` (off) | `function(ctx)` returning `true` once the Buttons may appear. Until then they stay held |
| `reveal.fadeMs` | number | `400` | Fade-in time of the Buttons (ms). 0 = they appear at once |
| `reveal.slide` | string | `"none"` | `"none"`, `"auto"` (vertical Cards slide in from the left, every other Layout from below), `"left"` or `"up"` |
| `reveal.slideXFraction` | number | `0.3` | How far from the left the Buttons start, as a fraction of the panel width (`left` / `auto` with vertical Cards) |
| `reveal.slideYFraction` | number | `0.08` | How far below the Buttons start, as a fraction of the screen height (`up` / `auto`) |

`logo.place` puts the Logo anywhere:

```lua
logo = { place = function(ctx, w, h, uiScale) return 40 * uiScale, 30 * uiScale end },
```

---

## Cards: Geometry

Sizes and shapes. Used by the `cards` Layouts only.

| Field | Type | Plain default | What it does |
|:---|:---|:---|:---|
| `cards.geometry.baseW` | number | `600` | Design width of one Card (design pixels, scaled with the screen). A Layout's own `cardWidth` replaces it |
| `cards.geometry.baseH` | number | `696` | Design height of one Card |
| `cards.geometry.border` | number | `24` | Width of the black frame around the Graphic |
| `cards.geometry.captionH` | number | `120` | Height of the caption area when it has risen |
| `cards.geometry.heightFraction` | number | `0.196` | Height of a SELECTED Card as a share of the screen height |
| `cards.geometry.restFraction` | number | `1` | How tall an unselected Card is next to that. 1 = the same height |
| `cards.geometry.growFraction` | number | `0` | How far a selected Card grows from resting towards the full height. 0 = it does not grow |
| `cards.geometry.maxStretch` | number | `1.35` | How much wider than `baseW` a Card may grow for a long label |

### Vertical Cards

| Field | Type | Plain default | What it does |
|:---|:---|:---|:---|
| `cards.geometry.visible` | number | `4` | How many Cards are shown at once (the column scrolls past that) |
| `cards.geometry.minCardHeightFraction` | number | `0` | A minimum Card height as a share of the screen height (0 = off). When set, `visible` becomes automatic, showing as many Cards as fit at that height |
| `cards.geometry.refH` | number | `140` | The reference Card height at 1920 wide |
| `cards.geometry.heightFactor` | number | `5` | Card widths are derived from the vanilla Button height times this |
| `cards.geometry.expandFactor` | number | `1` | How much wider a selected Card is than a resting one. 1 = not wider |
| `cards.geometry.maxRestWidthFraction` | number | `0.3` | The widest a selected Card gets, as a share of the screen width |
| `cards.geometry.selWidthFactor` | number | `2.6` | A Card's width as a multiple of its height |
| `cards.geometry.edgeGapFraction` | number | `0.012` | The gap under the Logo and above the Settings Button (share of screen height) |
| `cards.geometry.leftFraction` | number | `0.01` | The left margin of the column (share of screen width) |
| `cards.geometry.arrowFraction` | number | `0.15` | The up and down arrow's width as a share of a resting Card's width |

---

## Cards: Look

| Field | Type | Plain default | What it does |
|:---|:---|:---|:---|
| `cards.look.dim` | number | `1` | Brightness of an unselected Card's Graphic (1 = full brightness) |
| `cards.look.greyTwin` | boolean | `false` (off) | Use the `_g` twin of each Graphic as the resting Graphic, leaving the Card greyscale at rest while the colour Graphic fades in on selection |
| `cards.look.greyTone` | number | `1` | Brightness of that greyscale resting Graphic |
| `cards.look.captionAlpha` | number | `1` | Opacity of the black caption bar |
| `cards.look.captionTint` | table | `{ r = 1, g = 1, b = 1 }` | Multiplied into the painted caption art (a white Graphic tinted black gives a black bar) |
| `cards.look.captionOverhang` | number | `0` | Horizontal Cards: design pixels a selected Card's painted caption bar reaches past the Card on each side |
| `cards.look.restTextGrey` | number | `1` | Vertical Cards: the caption text of an unselected Card (0 = black, 1 = white). It turns white as the Card is selected |
| `cards.look.captionSlant` | number | `0` | Vertical Cards: pixels the end of the caption bar leans per row (0 = square) |
| `cards.look.shadow` | table or `false` | `false` (off) | A soft inner shadow on the Graphic. `true` uses the defaults below. A table overrides fields |
| `cards.look.restCaption` | table or `false` | `false` (off) | Horizontal Cards: show the label on closed Cards too, on a centred black bar whose two ends slant inwards, growing to the full caption strip on selection |
| `cards.look.outline.delayMs` | number | `0` | Wait after the Card has finished growing before the outline starts to fade in |
| `cards.look.outline.inMs` | number | `0` | Outline fade-in (0 = at once) |
| `cards.look.outline.outMs` | number | `0` | Outline fade-out when the Card starts to shrink (0 = at once) |
| `cards.look.outline.thickness` | number | `3` | Outline thickness in design pixels. `outline = false` removes the outline |

Sub-tables that can be given instead of `true`:

| Field | Type | Plain default | What it does |
|:---|:---|:---|:---|
| `cards.look.shadow.depth` | number | `0.08` | How far in the shadow reaches, as a fraction of the Card's design height |
| `cards.look.shadow.strength` | number | `0.3` | Black opacity at the edge |
| `cards.look.shadow.plateau` | number | `0.3` | Share of the depth over which it holds full strength before it fades |
| `cards.look.shadow.bands` | number | `14` | How many rings the depth is cut into (more = smoother) |
| `cards.look.restCaption.slant` | number | `0.2667` | Pixels each end of the bar leans per row (shorter at the top) |
| `cards.look.restCaption.padX` | number | `24` | Space either side of the text on a closed Card, in design pixels |

---

## Cards: Motion

| Field | Type | Plain default | What it does |
|:---|:---|:---|:---|
| `cards.motion.smoothMs` | number | `1` | Time constant of the grow smoothing (larger = softer, 1 = at once) |
| `cards.motion.colorFadeMs` | number | `0` | Grey to colour cross-fade time (0 = at once) |
| `cards.motion.drift` | table or `false` | `false` (off) | The Graphic glides to a random new place on selection. `true` uses the defaults below |

Sub-table that can be given instead of `true`:

| Field | Type | Plain default | What it does |
|:---|:---|:---|:---|
| `cards.motion.drift.zoom` | number | `1.06` | How much larger the Graphic is drawn, keeping its edges hidden while it glides |
| `cards.motion.drift.fill` | number | `0.9` | How much of the spare margin the glide uses |
| `cards.motion.drift.charFactor` | number | `1.8` | How many times as far a character layer moves (the opposite way, for a parallax) |
| `cards.motion.drift.fadeMs` | number | `800` | How long the glide takes to build up on selection and ease out on deselection |

---

## The Strip, the Arrows and the Settings Button

The Strip bar, the arrows and the Settings icon are found by name and folder: `<Prefix>_Strip.png`, `<Prefix>_Arrow_H.png` and `<Prefix>_Arrow_V.png` in `media/ui/layout/`, with `<Prefix>_Options_Icon.png` in `media/ui/icons/`. The Card caption bar is `<Prefix>_Caption.png` in `media/ui/cards/captions/`. See [Files MTF Finds by Name](reference.md#files-mtf-finds-by-name) for the full list.

| Field | Type | Plain default | What it does |
|:---|:---|:---|:---|
| `strip.fadeFraction` | number | `0` | How much of each end of the Strip art fades out (share of its width) |
| `strip.alpha` | number | `1` | Opacity of the plain black bar drawn when there is no Strip art |
| `arrows.idleTone` | number | `1` | The scroll arrows' colour when idle (0 = black, 1 = the art's own colour) |
| `arrows.hoverTone` | number | `1` | The scroll arrows' colour when hovered |
| `optionsButton.idleAlpha` | number | `0.85` | Opacity of the Settings Button at the bottom left when the mouse is not over it (hovered, it is fully opaque) |

---

## Painter Slots

When numbers are not enough, give MTF a function and it draws that piece instead of its plain one. MTF still owns the Card's size, growth, hit box, hover, focus and input. Each Slot is called as `fn(ctx, card)` every frame the Card is drawn.

### The Four Card Slots (`cards.paint`)

| Slot | Replaces | MTF has set |
|:---|:---|:---|
| `photo` | the Graphic and its inner shadow | the stencil to `card.window` |
| `layers` | (nothing, drawn **above** the Graphic) | the stencil to `card.clip` (the window plus the Card's top border) |
| `caption` | the caption bar and the label | no stencil |
| `frame` | the selected Card's outline | no stencil |

### The `card` Object

Read-only.

| Field | Meaning |
|:---|:---|
| `element` | The label to draw on, with `card.element:drawRect(...)`, `drawTextureScaled(...)`, `drawText(...)` |
| `id`, `label` | The Button id and its text |
| `vertical` | `true` for the vertical column |
| `w`, `h`, `border`, `scale` | Current size, frame width, design scale |
| `hover` | 0..1, smoothed |
| `colour` | 0..1, the grey to colour fade |
| `photo`, `photoGrey` | The two textures |
| `window` | The Graphic window rectangle |
| `anchor` | The SELECTED-size window the Graphic is laid out for |
| `clip` | The window plus the Card's top border |
| `drift` | `{ amount, angle }` for the glide |
| `now` | Millisecond clock |

`MenuThemeFramework.cardDrift(card, coverW, coverH, factor)` returns the drift offset for a layer that should glide with the Graphic. A larger, negative factor gives a parallax. `MenuThemeFramework.fitText(text, font, maxW, maxH)` fits a label into a box (a smaller font, two lines, then an ellipsis), as MTF's own captions do.

### A Real `layers` Painter

GTA Menu Theme stands a cut-out character on every Card in the `layers` Slot. This is the start of that function. The rest places and scales the character:

From `GMT_Cards.lua`:

```lua
--- The `cards.paint.layers` slot (see GMT_Theme.lua): draws the card's character. MTF has already set the stencil to
--- card.clip (the photo window plus the card's top border), so the character is cropped by the card.
function GMT_Cards.layers(ctx, card)
    local hover = card.hover
    if hover <= 0 then
        return
    end
    local char = characterFor(card.id)
    if not char then
        return
    end
    local cw, ch = char.tex:getWidth(), char.tex:getHeight()
    if cw <= 0 or ch <= 0 then
        return
    end
    local vertical = card.vertical
    -- the SELECTED-size window the character is laid out for
    local left, top, selWinW, selWinH = card.anchor.x, card.anchor.y, card.anchor.w, card.anchor.h

    local centreLo, centreHi, driftXScale, sizeFactor, raise
    if vertical then
        centreLo = VERTICAL_ZONE_START + VERTICAL_HALF_WIDTH
        centreHi = 1 - VERTICAL_HALF_WIDTH - RIGHT_PAD
        driftXScale, sizeFactor, raise = 1, VERTICAL_SCALE, RAISE
    else
        centreLo, centreHi, driftXScale = MIDDLE_LO, MIDDLE_HI, 1
```


It is passed in like this:

```lua
cards = {
    paint = { layers = GMT_Cards.layers },
},
```

### The Strip, the Carousel and the Arrows

They take Painter Slots the same way.

| Setting | Replaces | The function receives |
|:---|:---|:---|
| `strip.paint.bar` | the Strip's bar | `bar = { screen, x, y, w, h, alpha }` (draw with `bar.screen:drawRect(...)`) |
| `strip.paint.option` | every option of the Strip AND the Carousel | `option = { element, id, label, font, w, h, hover, pad, focused, promptTexture, carousel }` |
| `arrows.paint` | every scroll arrow of every Layout | `arrow = { element, direction, vertical, w, h, enabled, hover, tone, alpha }` |

MTF still places, sizes, scrolls and clicks them. It also still runs the option's tooltip. `option.promptTexture` is the controller Button Graphic for the focused option. Draw it wherever suits the Theme's look (or not at all).

!!! warning "Guard Every nil Value"
    A Painter Slot that errors will error every frame, as MTF does not catch errors in it. Check for missing textures before using them.

---
