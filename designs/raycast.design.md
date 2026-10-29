---
version: alpha
name: Raycast
slug: raycast
source: https://www.raycast.com/
extractedAt: "2026-05-22"
description: "Dark, command-palette-native productivity identity with red action accents, glossy inset panels, precise 8px rhythm, huge cinematic serif hero type, and macOS-like utility surfaces."

colors:
  primary: "#ff6363"
  accent: "#56c2ff"
  accentHover: "#f28c8c"
  accentPressed: "#d72a2a"
  ink: "#ffffff"
  body: "#9c9c9d"
  muted: "#6a6b6c"
  canvas: "#07080a"
  surface: "#111214"
  surfaceAlt: "#0c0d0f"
  border: "#1b1c1e"
  borderStrong: "#434345"
  link: "#ff6363"
  success: "#59d499"
  warning: "#ff9217"
  error: "#ff6363"
  on-primary: "#ffffff"
  on-dark: "#ffffff"
  grey-50: "#e6e6e6"
  grey-100: "#cdcece"
  grey-200: "#9c9c9d"
  grey-300: "#6a6b6c"
  grey-400: "#434345"
  grey-500: "#2f3031"
  grey-600: "#1b1c1e"
  grey-700: "#111214"
  grey-800: "#0c0d0f"
  grey-900: "#07080a"
  card-border: "rgba(255,255,255,0.06)"
  card-highlight: "rgba(255,255,255,0.10)"
  glass-nav-start: "rgba(17,18,20,0.75)"
  glass-nav-end: "rgba(12,13,15,0.90)"
  danger-surface: "#2c1617"
  danger-border: "#833637"
  code-bg: "rgba(255,99,99,0.15)"
  focus-ring: "rgba(255,255,255,0.50)"
  glow-blue: "#0294fe"
  glow-purple: "#9b4dff"

typography:
  display:
    fontFamily: "Instrument Serif, Georgia, serif"
    fontSize: 168px
    fontWeight: 400
    lineHeight: 1.00
    letterSpacing: "-2px"
  hero:
    fontFamily: "Instrument Serif, Georgia, serif"
    fontSize: 86px
    fontWeight: 400
    lineHeight: 1.00
    letterSpacing: "-2px"
  headline-lg:
    fontFamily: "Inter, Inter Fallback, sans-serif"
    fontSize: 48px
    fontWeight: 600
    lineHeight: 1.06
    letterSpacing: "0.02em"
  title-lg:
    fontFamily: "Inter, Inter Fallback, sans-serif"
    fontSize: 32px
    fontWeight: 600
    lineHeight: 1.50
    letterSpacing: "0em"
  title-md:
    fontFamily: "Inter, Inter Fallback, sans-serif"
    fontSize: 24px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: "0.2px"
  title-sm:
    fontFamily: "Inter, Inter Fallback, sans-serif"
    fontSize: 20px
    fontWeight: 500
    lineHeight: 1.40
    letterSpacing: "0.2px"
  body:
    fontFamily: "Inter, Inter Fallback, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.60
    letterSpacing: "0.2px"
  label:
    fontFamily: "Inter, Inter Fallback, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.60
    letterSpacing: "0.2px"
  button:
    fontFamily: "Inter, Inter Fallback, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.14
    letterSpacing: "0.2px"
  caption:
    fontFamily: "Inter, Inter Fallback, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.23
    letterSpacing: "0.1px"
  legal:
    fontFamily: "Inter, Inter Fallback, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.50
    letterSpacing: "0.4px"
  code:
    fontFamily: "JetBrains Mono, Menlo, Monaco, Courier, monospace"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.50
    letterSpacing: "0em"
  micro-mono:
    fontFamily: "Geist Mono, ui-monospace, SFMono-Regular, monospace"
    fontSize: 10px
    fontWeight: 500
    lineHeight: 1.60
    letterSpacing: "0.2px"

rounded:
  sm: 6px
  md: 8px
  lg: 12px
  xl: 16px
  xxl: 20px
  pill: 9999px

spacing:
  xs: 4px
  sm: 8px
  md: 16px
  lg: 24px
  xl: 32px
  section: 96px

components:
  button-primary:
    backgroundColor: "{colors.grey-50}"
    textColor: "{colors.grey-500}"
    typography: "{typography.button}"
    rounded: "{rounded.md}"
    padding: 8px 12px
  button-primary-active:
    backgroundColor: "{colors.grey-100}"
    textColor: "{colors.grey-500}"
    rounded: "{rounded.md}"
  button-dark:
    backgroundColor: "linear-gradient(180deg, rgba(255,255,255,0.03), rgba(255,255,255,0.10))"
    textColor: "{colors.on-dark}"
    typography: "{typography.button}"
    rounded: "{rounded.md}"
    padding: 8px 12px
  button-danger:
    backgroundColor: "{colors.danger-surface}"
    textColor: "{colors.primary}"
    typography: "{typography.button}"
    rounded: "{rounded.md}"
    padding: 8px 12px
  nav-glass:
    backgroundColor: "linear-gradient(137deg, {colors.glass-nav-start} 4.87%, {colors.glass-nav-end} 75.88%)"
    textColor: "{colors.body}"
    rounded: "{rounded.xl}"
    padding: 16px 32px
  card-dark:
    backgroundColor: "linear-gradient(137deg, {colors.surface} 4.87%, {colors.surfaceAlt} 75.88%)"
    textColor: "{colors.ink}"
    rounded: "{rounded.lg}"
    padding: 24px
  cta-card:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.ink}"
    rounded: "{rounded.md}"
    padding: 24px
  search-modal:
    backgroundColor: "radial-gradient(100% 100% at 50% 0, {colors.grey-800} 0, {colors.grey-700} 150%)"
    textColor: "{colors.ink}"
    rounded: "{rounded.md}"
    padding: 16px
  command-row:
    backgroundColor: "rgba(255,255,255,0.00)"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
    padding: 8px 16px
  input-dark:
    backgroundColor: "transparent"
    textColor: "{colors.ink}"
    rounded: "{rounded.md}"
    padding: 16px
  pricing-card:
    backgroundColor: "linear-gradient(137deg, {colors.surface} 4.87%, {colors.surfaceAlt} 75.88%)"
    textColor: "{colors.ink}"
    rounded: "{rounded.lg}"
    padding: 32px
  hotkey-key:
    backgroundColor: "radial-gradient(100% 100% at 50% 0, {colors.grey-800} 0, {colors.grey-700} 100%)"
    textColor: "{colors.body}"
    typography: "{typography.caption}"
    rounded: "{rounded.sm}"
    padding: 0px 5px
  app-window-peek:
    backgroundColor: "{colors.surfaceAlt}"
    textColor: "{colors.ink}"
    rounded: "{rounded.md}"
    padding: 0px
---

**Overview**
Raycast’s visual system is a dark productivity interface turned into a marketing language. It borrows directly from the command palette: compact rows, shortcut keys, floating search panels, inset borders, small metadata, and dense utility modules. The brand feels fast, precise, technical, and slightly cinematic rather than corporate.

The most distinctive mode is the homepage hero, where oversized serif display type and blurred/masked duplicates create a dramatic “Raycast” title above a glowing app-window peek. Product and pricing pages shift into a calmer utility mode: Inter-led type, dark cards, red action accents, sparse blue links, and white hairline borders. Docs/manual content is more editorial but keeps the same dark background, monospace code treatment, and red link grammar.

Key Characteristics:

- Dark canvas first: build from `{colors.canvas}` and layer only a few brighter surfaces.
- Red is the core action and brand accent; use `{colors.primary}` sparingly but decisively.
- Cards feel like dark metal: subtle gradients, 1px translucent borders, and inset top highlights.
- Typography is compact and exact, except for the homepage’s enormous serif wordmark-style hero.
- Interaction patterns echo Raycast itself: command rows, hotkeys, search modals, app icons, and floating windows.
- Spacing uses an 8px rhythm with 4px half-steps for dense controls.
- Motion is small and functional: scale on press, arrow nudges, fade-up entrances, and carousel progress.

**Colors**
Primary & Action:

`{colors.primary}` `#ff6363` is Raycast’s signature red. It appears in links, danger messaging, highlights, code chips, log-out states, and feature emphasis, but not as a full-page wash.

`{colors.accent}` `#56c2ff` is the secondary link and “new/system” blue. Use it for informational links and occasional product metadata, never as the main CTA color.

`{colors.accentHover}` and `{colors.accentPressed}` are derived interaction stops for red controls. They keep the red family warm and avoid drifting into generic saturated scarlet.

Surfaces:

`{colors.canvas}` is the site foundation. Use it for page backgrounds, footer bases, and negative space around all product modules.

`{colors.surface}` and `{colors.surfaceAlt}` create Raycast’s standard dark panel gradient. Most cards, nav, app tiles, and poster modules blend these two values at a diagonal or radial angle.

`{colors.card-border}` and `{colors.card-highlight}` define the quiet edge language. The border is usually translucent white, while highlights sit as inset top lines.

Neutrals & Text:

`{colors.ink}` is reserved for headings, selected rows, primary labels, and white-on-dark buttons.

`{colors.body}` is the default secondary text and nav link color. It should feel readable but deliberately lower contrast than headings.

`{colors.muted}`, `{colors.grey-400}`, and `{colors.grey-500}` are for disabled text, icon chrome, keycaps, and supporting metadata.

Semantic:

`{colors.success}` appears in success flash messages and completion states with a transparent green background.

`{colors.warning}` appears in beta tags and warm status labels, usually over a low-alpha orange surface.

`{colors.error}` shares the brand red. Error states should pair it with `{colors.danger-surface}` and `{colors.danger-border}` so errors still feel native to the dark UI.

Brand-specific signatures:

`{colors.glass-nav-start}` and `{colors.glass-nav-end}` describe the fixed navbar’s translucent dark gradient. Pair them with blur and an inset highlight.

`{colors.code-bg}` supports inline code and red-tinted chips. It should stay translucent so code feels embedded, not pill-like.

`{colors.glow-blue}`, `{colors.glow-purple}`, and `{colors.primary}` form the rare multicolor glow used around newsletter submit focus states and special AI/product moments.

**Typography**
Raycast uses Inter for nearly all marketing and utility UI, JetBrains Mono for code, Geist Mono for small version labels and compact technical tags, and a serif display face on the flagship homepage hero. If Instrument Serif is unavailable, use Georgia for the same high-contrast editorial gesture, but keep it only for the top-level brand moment.

| Level | Size | Weight | Line Height | Letter Spacing |
| --- | ---: | ---: | ---: | --- |
| `{typography.display}` | 168px | 400 | 1.00 | -2px |
| `{typography.hero}` | 86px | 400 | 1.00 | -2px |
| `{typography.headline-lg}` | 48px | 600 | 1.06 | 0.02em |
| `{typography.title-lg}` | 32px | 600 | 1.50 | 0em |
| `{typography.title-md}` | 24px | 500 | 1.25 | 0.2px |
| `{typography.title-sm}` | 20px | 500 | 1.40 | 0.2px |
| `{typography.body}` | 16px | 400 | 1.60 | 0.2px |
| `{typography.label}` | 14px | 500 | 1.60 | 0.2px |
| `{typography.button}` | 14px | 500 | 1.14 | 0.2px |
| `{typography.caption}` | 13px | 400 | 1.23 | 0.1px |
| `{typography.legal}` | 12px | 400 | 1.50 | 0.4px |
| `{typography.code}` | 12px | 400 | 1.50 | 0em |
| `{typography.micro-mono}` | 10px | 500 | 1.60 | 0.2px |

Principles:

- Keep most UI type at 12-16px; Raycast’s density is part of the product memory.
- Use medium weights often. Labels, buttons, card headings, and nav items usually sit at 500.
- Track small text slightly positive with `0.1px` or `0.2px`; reserve negative tracking for the huge serif hero only.
- Use monospace as product evidence: versions, code, hotkeys, and command-line-like snippets.
- Avoid oversized SaaS headings inside cards. Card titles usually stay at `{typography.title-sm}` or smaller.

**Layout**
The core spacing scale is 4, 8, 12, 16, 24, 32, 40, 48, 64, 80, 96, 168, and 224px. The design system’s public tokens favor `{spacing.xs}` through `{spacing.xl}`, with `{spacing.section}` for large blocks. Containers commonly max at 1204px, with smaller editorial/content widths around 746px and 1064px.

The navbar is fixed, centered, and constrained to the main container. Desktop nav is 76px tall; mobile is 58px. Main grids collapse early and keep generous side padding of 16-32px. Product cards often use 24px internal padding, while pricing and richer panels use 32px.

Whitespace philosophy: Raycast alternates dense product UI inside modules with very open page-level spacing. Let panels be compact, but give sections enough vertical room to feel deliberate. The page should never become a flat grid of equal cards; it needs dark air around precise UI artifacts.

**Elevation & Depth**
Raycast uses depth through light-catching edges more than heavy shadows. Standard panels use a 1px translucent border plus `inset 0 1px 0 rgba(255,255,255,0.10)`. Floating nav and dropdowns add blur and a slightly brighter inset edge.

Use stronger shadows only for app-window moments: search modals, hero media, and product peeks. Acceptable values include soft white glows like `0 0 140px rgba(255,255,255,0.20)` and dark modal depth like `0 4px 40px 8px rgba(0,0,0,0.40)`.

Hierarchy comes from contrast, placement, cropping, masks, and motion. Avoid broad material-style drop shadows; Raycast depth is glossy, controlled, and mostly internal.

**Components**
Buttons:

`{components.button-primary}` is a light button on dark canvas. It is used for “Download” and high-priority conversion moments, with grey text over a near-white fill and a pressed state that darkens to `{colors.grey-100}`.

`{components.button-dark}` is the standard secondary/action button. It uses a translucent white gradient, white text, and an inset border so it reads as a native dark control.

`{components.button-danger}` is for destructive or account actions. It pairs `{colors.primary}` text with `{colors.danger-surface}` and a red-brown border, keeping danger states inside the brand’s dark palette.

Cards & Containers:

`{components.card-dark}` is the default marketing/product card. It should use a diagonal dark gradient, 1px translucent border, and inset highlight.

`{components.cta-card}` is a compact promotional panel. It may include a clipped graphic, 24px padding, a 16px semibold title, and a 14px muted description.

`{components.search-modal}` is Raycast’s most product-specific container. It is a centered floating command palette with a radial dark gradient, 500px max width, separated input row, and list results below.

Inputs & Forms:

`{components.input-dark}` is transparent over a dark modal or footer form. Use white text, no heavy border, and a single low-contrast divider when needed.

Newsletter submit buttons may use a focused multicolor conic glow from `{colors.glow-blue}`, `{colors.primary}`, and `{colors.glow-purple}`. Keep this rare; it is an interaction flourish, not a background system.

Navigation:

`{components.nav-glass}` is fixed, centered, blurred, and compact. Links use `{typography.label}`, `{colors.body}`, and turn white on hover.

Mobile navigation expands the same glass container vertically. The toggle is a 24px hamburger that rotates into a close icon with thin white lines.

Pricing:

`{components.pricing-card}` follows the card-dark language but increases padding and structured comparison density. Pricing pages use compact 24px hero headings rather than the oversized homepage serif.

The enterprise link is a soft horizontal callout: 15px medium type, 16px 24px padding, translucent white background, and a small arrow nudge on hover.

Signature Components:

`{components.command-row}` is the native Raycast row pattern: icon, primary text, muted secondary text, accessory, and a translucent hover/focus fill.

`{components.hotkey-key}` is the keyboard grammar. It uses a dark radial surface, 20px minimum height, small mono or system type, and subtle inset treatment.

`{components.app-window-peek}` is the masked product-window preview. It should appear clipped from the bottom/top with rounded upper corners, not as a generic screenshot card.

**Do's and Don'ts**
Do:

- Build pages on `{colors.canvas}` and reserve pure white areas only for buttons or media content.
- Use `{components.card-dark}` with inset highlights for product modules and feature tiles.
- Use `{colors.primary}` for links, code accents, error states, and signature emphasis.
- Keep controls compact with `{typography.button}` and 36-42px heights.
- Pair app icons, hotkeys, command rows, or window peeks with product claims.
- Use 24px or 32px internal padding for substantial cards.
- Animate hover states with small transforms such as `scale(0.98)` on active and 3px arrow nudges.

Don't:

- Do not turn the whole interface red; `{colors.primary}` is an accent, not a surface.
- Do not use bright blue as the main CTA; `{colors.accent}` is informational and secondary.
- Do not replace inset borders with broad material shadows on standard cards.
- Do not use rounded pill buttons everywhere; most controls use `{rounded.md}`.
- Do not set dense card headings in `{typography.display}` or giant SaaS hero scales.
- Do not flatten command rows into generic list items; include icon, accessory, and hover fill.
- Do not use beige, pastel, or light-mode surfaces as the dominant page mood.
- Do not invent glassmorphism beyond the fixed nav, search overlay, and floating menus.

**Responsive Behavior**
| Breakpoint | Width | Behavior |
| --- | ---: | --- |
| compact | 375px | Scale hero/media and hotkey showcases down; keep 16px page padding. |
| phone-wide | 480px | Increase hero image, title, and product preview sizes. |
| tablet | 720px | Move many stacked cards into multi-column layouts; grid gap usually 24px. |
| content | 768px | Desktop-like hero spacing begins; larger window peeks and section padding. |
| nav-desktop | 880px | Navbar becomes horizontal, 76px tall, logo/actions split to edges. |
| wide | 1064px | Full nav labels, two-column product layouts, and sidebars appear. |

Touch targets should stay at least 36px for buttons and 40px for icon-only controls, even when visual content is small. Command rows may be 32-40px high if they are part of a dense desktop-only palette.

Collapsing strategy:

- Stack marketing grids vertically before shrinking internal card content too far.
- Keep nav inside the same glass container and expand its height on mobile.
- Hide secondary desktop-only metadata before removing primary action buttons.
- Preserve product screenshots and window peeks with masks instead of cropping arbitrary centers.
- Let horizontal app-icon rows scroll or mask at edges rather than wrapping into noisy mosaics.

Images should be real product UI, app icons, or generated feature artwork. Use masks, radial fades, and cropped peeks to integrate images into the dark canvas.

**Iteration Guide**
1. Check the base page: the background must read as `{colors.canvas}`, not charcoal blue or pure black.
2. Audit every card for Raycast edges: 1px translucent border plus inset highlight should appear on core panels.
3. Verify primary actions: main conversion buttons should use the light `{components.button-primary}` pattern or the dark secondary pattern, not red-filled generic buttons.
4. Scan type density: most UI text should sit between `{typography.caption}` and `{typography.body}`; only the hero may use `{typography.display}`.
5. Look for product-native evidence: at least one command row, hotkey, app icon grid, search palette, or window peek should anchor product pages.
6. Test red usage: `{colors.primary}` should appear as accents and links, with enough contrast against dark surfaces.
7. Review spacing rhythm: card padding should resolve to 16, 24, or 32px; page sections should use 80-96px or larger.
8. Check mobile: nav collapses at 880px, content stacks before 720px, and text never overlaps masked imagery.

**Known Gaps**
Observed directly: homepage, AI feature page, pricing page, and manual billing page content were fetched on 2026-05-22. CSS chunks exposed the root colors, spacing, radii, font stacks, nav, buttons, search modal, footer, markdown, pricing hero, cards, hotkeys, and product showcase patterns.

Derived: the YAML normalizes some exact CSS variables into DESIGN.md roles. For example, `{colors.primary}` maps to Raycast’s `--red-dark`, while `{colors.surface}` and `{colors.surfaceAlt}` map to the recurring gradient stops used in cards and nav.

Uncertain: the homepage serif font is referenced through compiled classes and appears as an Instrument-style serif in the CSS naming pattern, but the exact public font token was not fully available in the extracted chunk preview. Use the specified serif stack conservatively only for brand-scale hero text.

Docs/manual pages are built on a separate docs surface but retain Raycast’s red links, dark canvas, Inter/mono content, and markdown styles. Treat docs-specific table and article formatting as a content-mode extension, not the primary marketing design system.
