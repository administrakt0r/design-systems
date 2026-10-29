---
version: alpha
name: Discord
slug: discord
source: "https://discord.com/"
extractedAt: 2026-05-20
description: "Playful communication brand built on Blurple, oversized ABC Ginto hero headlines, gg sans utility text, pill CTAs, dark utility surfaces, and illustrated mega-navs that make product marketing feel like a game world."

colors:
  primary: "#5865F2"
  accent: "#798DF9"
  accentHover: "#5765F2"
  accentPressed: "#3442DA"
  ink: "#23272A"
  body: "#4F545C"
  muted: "#99AAB5"
  canvas: "#FFFFFF"
  surface: "#F6F6F6"
  surfaceAlt: "#F2F3F5"
  border: "#DDE1E7"
  borderStrong: "#C7CCD1"
  link: "#5865F2"
  success: "#57F287"
  warning: "#FEE75C"
  error: "#ED4245"
  light-blurple: "#E0E3FF"
  nitro-mint: "#15F5BA"
  nitro-pink: "#FF6AEF"
  footerBg: "#5865F2"
  utility-dark: "#202225"
  utility-darker: "#0E0619"
  on-primary: "#FFFFFF"
  on-dark: "#FFFFFF"

typography:
  display:
    fontFamily: "Abcgintodiscordnord, Arial, sans-serif"
    fontSize: 56px
    fontWeight: 800
    lineHeight: 0.96
    letterSpacing: "-0.02em"
  hero:
    fontFamily: "\"Abcgintonord 800\", Arial, sans-serif"
    fontSize: 48px
    fontWeight: 800
    lineHeight: 1.00
    letterSpacing: "-0.01em"
  headline-lg:
    fontFamily: "ABCGintoNormal-Bold, Arial, sans-serif"
    fontSize: 40px
    fontWeight: 700
    lineHeight: 1.20
    letterSpacing: "-0.01em"
  title-lg:
    fontFamily: "ABCGintoNormal-Bold, Arial, sans-serif"
    fontSize: 32px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: "-0.01em"
  title-md:
    fontFamily: "ABCGintoNormal-Bold, Arial, sans-serif"
    fontSize: 24px
    fontWeight: 700
    lineHeight: 1.33
    letterSpacing: "0"
  title-sm:
    fontFamily: "gg sans, sans-serif"
    fontSize: 20px
    fontWeight: 500
    lineHeight: 1.40
    letterSpacing: "0"
  label:
    fontFamily: "gg sans, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.29
    letterSpacing: "0.02em"
  button:
    fontFamily: "gg sans, sans-serif"
    fontSize: 20px
    fontWeight: 500
    lineHeight: 1.20
    letterSpacing: "0"
  body-lg:
    fontFamily: "gg sans, sans-serif"
    fontSize: 20px
    fontWeight: 400
    lineHeight: 1.40
    letterSpacing: "0"
  body:
    fontFamily: "gg sans, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.50
    letterSpacing: "0"
  caption:
    fontFamily: "gg sans, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.29
    letterSpacing: "0"
  legal:
    fontFamily: "gg sans, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.50
    letterSpacing: "0"
  code:
    fontFamily: "Ggsansmono, ui-monospace, monospace"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.40
    letterSpacing: "0"

rounded:
  none: 0px
  sm: 4px
  md: 8px
  lg: 16px
  xl: 28px
  pill: 9999px

spacing:
  xs: 8px
  sm: 12px
  md: 16px
  lg: 24px
  xl: 32px
  section: 80px

components:
  button-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button}"
    rounded: "{rounded.xl}"
    padding: 14px 32px
  button-primary-active:
    backgroundColor: "{colors.accentPressed}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.xl}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button}"
    rounded: "{rounded.xl}"
    padding: 14px 32px
  button-secondary-on-dark:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.label}"
    rounded: "{rounded.pill}"
    padding: 7px 16px
  button-utility-dark:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    typography: "{typography.button}"
    rounded: "{rounded.xl}"
    padding: 12px 32px 15px
  button-utility-outline:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.link}"
    typography: "{typography.label}"
    rounded: "{rounded.sm}"
    padding: 6px 16px
  button-search-pill:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.label}"
    rounded: "{rounded.pill}"
    padding: 8px 20px
  card-feature:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    rounded: "{rounded.md}"
    padding: 40px
  card-surface:
    backgroundColor: "{colors.surfaceAlt}"
    textColor: "{colors.ink}"
    rounded: "{rounded.lg}"
    padding: 24px
  card-elevated-marketing:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
    padding: 26px
  card-nitro-gradient:
    backgroundColor: "{colors.nitro-mint}"
    textColor: "{colors.utility-darker}"
    rounded: "{rounded.md}"
    padding: 30px 20%
  input-search:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body}"
    rounded: "{rounded.pill}"
    padding: 8px 12px
  nav-topbar:
    backgroundColor: "transparent"
    textColor: "{colors.on-dark}"
    typography: "{typography.label}"
    rounded: "{rounded.none}"
    padding: 20px 0px
  nav-dropdown-mega:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    rounded: "{rounded.md}"
    padding: 24px
  footer-dropdown-mobile:
    backgroundColor: "transparent"
    textColor: "{colors.on-primary}"
    typography: "{typography.body}"
    rounded: "{rounded.none}"
    padding: 16px 0px
  pricing-promo-banner:
    backgroundColor: "{colors.utility-darker}"
    textColor: "{colors.on-dark}"
    rounded: "{rounded.lg}"
    padding: 16px 24px
  docs-sidebar:
    backgroundColor: "{colors.utility-darker}"
    textColor: "{colors.on-dark}"
    rounded: "{rounded.md}"
    padding: 16px
---

**Overview**
Discord’s visual identity is recognizably social, playful, and slightly theatrical. The core brand is anchored by `{colors.primary}` Blurple, oversized ABC Ginto headlines, and pill-shaped CTAs that feel more like “join the fun” invitations than conventional SaaS buttons. Even when the layout is simple, the composition is rarely neutral: hero blocks arrive with floating illustrations, deep blue or black atmospheres, and strong center-stage messaging.

There are at least three visible modes. Marketing pages use dramatic hero type, bright brand color, roomy section spacing, and illustrated dropdowns. Nitro pushes that language further with dark cosmic backdrops and neon accents like `{colors.nitro-mint}` and `{colors.nitro-pink}`. Docs shift into a more utility-first interface with darker chrome, smaller radii, and a denser navigational rhythm, but still keep `{colors.primary}` and `gg sans` as connective tissue.

Key Characteristics:
- Lead with `{colors.primary}` as a world-building color, not just a CTA color.
- Pair large, compressed-feeling display type with softer, readable `gg sans` body copy.
- Use `{rounded.xl}` and `{rounded.pill}` heavily for actions, badges, and friendly surfaces.
- Prefer flat color fields and hierarchy through scale before relying on heavy depth.
- Treat navigation as a feature surface with illustrated mega-dropdowns, not a plain menu.
- Keep spacing generous between major sections, with a recurring 16/24/32 rhythm inside components.
- Let marketing feel expressive while docs feel stricter, darker, and more tool-like.

**Colors**
Primary & Action

`primary` `{colors.primary}` `#5865F2` is the unmistakable Discord Blurple. It owns the homepage, primary CTAs, active links, footer background treatments, and the strongest brand recall moments.

`accent` `{colors.accent}` `#798DF9` appears more in the docs and supporting gradient atmospheres than in the main marketing CTA system. It lightens the brand without abandoning the core blue-violet identity.

`accentHover` `{colors.accentHover}` `#5765F2` is the near-state variant that keeps interaction feedback subtle. Discord generally nudges hue and depth rather than radically changing button appearance.

`accentPressed` `{colors.accentPressed}` `#3442DA` is the deeper pressed state that gives the primary button tactile certainty. It keeps enough chroma to remain playful even when darkened.

`link` `{colors.link}` `#5865F2` is intentionally the same family as the primary color. Hyperlinks feel like part of the action system, not an unrelated editorial token.

Surfaces

`canvas` `{colors.canvas}` `#FFFFFF` is the dominant light surface across homepage, safety, pricing cards, and many dropdowns. Discord uses white aggressively to make bright accents and illustrations feel cleaner and louder.

`surface` `{colors.surface}` `#F6F6F6` is the default light section fill for alternation bands and softer content modules. It helps reset the eye between heavily illustrated or bright sections.

`surfaceAlt` `{colors.surfaceAlt}` `#F2F3F5` is the slightly cooler utility panel color used for cards and structured informational modules. It reads as product UI adjacent rather than decorative.

`footerBg` `{colors.footerBg}` `#5865F2` turns the footer into a branded slab instead of a quiet legal strip. This is a strong Discord trait: the page rarely fades out into neutrality.

`utility-dark` `{colors.utility-dark}` `#202225` and `utility-darker` `{colors.utility-darker}` `#0E0619` define the darker product and Nitro worlds. They are used for banners, doc chrome, and premium atmospheres where the brand wants to feel immersive instead of airy.

Neutrals & Text

`ink` `{colors.ink}` `#23272A` is the primary dark text and dark-button background. It is softer than pure black but still authoritative.

`body` `{colors.body}` `#4F545C` carries most standard paragraph text. Discord avoids overly low-contrast gray for main copy; body text still feels present and readable.

`muted` `{colors.muted}` `#99AAB5` is for secondary labels, subdued support copy, and low-emphasis metadata. It is visibly muted without becoming washed out.

`border` `{colors.border}` `#DDE1E7` is a quiet structural line for utility elements and cards. It supports separation without making the layout feel grid-heavy.

`borderStrong` `{colors.borderStrong}` `#C7CCD1` is used when a stronger edge or hover differentiation is needed, especially around light surfaces and pressed UI.

Semantic

`success` `{colors.success}` `#57F287` is the modern Discord success green. It is bright, almost luminous, and feels energetic rather than “enterprise safe.”

`warning` `{colors.warning}` `#FEE75C` is a saturated alert yellow. It fits the playful system because it stays cheerful while still signaling caution.

`error` `{colors.error}` `#ED4245` is a vivid action red used in utility contexts. It is cleaner and more direct than a muted editorial crimson.

Brand-specific signatures

`light-blurple` `{colors.light-blurple}` `#E0E3FF` functions as a brand wash and softer companion to Blurple. It appears in brand guidance and helps Discord build light moments that still feel proprietary.

`nitro-mint` `{colors.nitro-mint}` `#15F5BA` is a Nitro-specific high-energy accent. It gives premium surfaces a game-skin quality that differs from standard marketing blue.

`nitro-pink` `{colors.nitro-pink}` `#FF6AEF` is another premium-world signature used to push Nitro into a more neon, collectible visual language. It should be used sparingly and only where that premium mood is intended.

**Typography**
Discord’s typographic system splits cleanly by role. Big public-facing statements lean on ABC Ginto variants and related brand display faces, while body, labels, and product-style text lean on `gg sans`. Docs flatten that split slightly by using `gg sans` more consistently, but the brand voice still comes from the contrast between expressive display and dependable utility text.

| Level | Font | Size | Weight | Line Height | Letter Spacing |
|---|---|---:|---:|---:|---|
| `display` | `Abcgintodiscordnord, Arial, sans-serif` | 56px | 800 | 0.96 | `-0.02em` |
| `hero` | `"Abcgintonord 800", Arial, sans-serif` | 48px | 800 | 1.00 | `-0.01em` |
| `headline-lg` | `ABCGintoNormal-Bold, Arial, sans-serif` | 40px | 700 | 1.20 | `-0.01em` |
| `title-lg` | `ABCGintoNormal-Bold, Arial, sans-serif` | 32px | 700 | 1.25 | `-0.01em` |
| `title-md` | `ABCGintoNormal-Bold, Arial, sans-serif` | 24px | 700 | 1.33 | `0` |
| `title-sm` | `gg sans, sans-serif` | 20px | 500 | 1.40 | `0` |
| `button` | `gg sans, sans-serif` | 20px | 500 | 1.20 | `0` |
| `body-lg` | `gg sans, sans-serif` | 20px | 400 | 1.40 | `0` |
| `body` | `gg sans, sans-serif` | 16px | 400 | 1.50 | `0` |
| `label` | `gg sans, sans-serif` | 14px | 500 | 1.29 | `0.02em` |
| `caption` | `gg sans, sans-serif` | 14px | 400 | 1.29 | `0` |
| `legal` | `gg sans, sans-serif` | 12px | 400 | 1.50 | `0` |
| `code` | `Ggsansmono, ui-monospace, monospace` | 14px | 400 | 1.40 | `0` |

Principles:
- Use display faces for punchy, compressed, slogan-like statements; they carry Discord’s personality more than the layout does.
- Tighten tracking on large headlines with negative spacing like `-0.01em` to `-0.02em`; Discord’s big type should feel packed and decisive.
- Keep `gg sans` for almost all utility, support, navigation, and product-adjacent copy.
- Hold body text at readable weights; Discord’s friendliness comes from clear copy, not ultra-light text.
- Let type size do the hierarchy work before adding extra decorative treatments or dense borders.

**Layout**
The most reliable spacing cadence is `{spacing.xs}` / `{spacing.md}` / `{spacing.lg}` / `{spacing.xl}`, with larger section jumps around `{spacing.section}` and beyond. Internal card spacing is usually 24px or 40px; button paddings cluster around `7x16`, `14x32`, and `16x32`; section containers observed in CSS include widths around `944px`, `1180px`, `1320px`, `1400px`, and `1540px` depending on campaign complexity. Grid behavior alternates between centered single-column hero stacks and 2- or 3-column informational bands, while mega-nav content uses structured multi-column dropdown panels.

Discord’s whitespace philosophy is generous but not minimalist. The brand likes big breathing room around hero statements and section transitions, yet inside modules it tightens rhythm to 16px and 24px so the page still feels lively. Empty space is used to stage motion, illustration, and type rather than to create an austere editorial mood.

**Elevation & Depth**
Observed shadows are generally soft and short-range: `0 3px 9px rgba(0,0,0,0.10)`, `0 8px 16px rgba(0,0,0,0.10-0.20)`, `0 8px 30px rgba(35,35,35,0.10)`, and compact focus or halo shadows on interactive buttons. The base system is flatter than many SaaS brands; hierarchy usually comes from scale, color blocks, and radius rather than layered neumorphism or glass.

When Discord does add depth, it is purposeful. White marketing cards lift slightly from pale surfaces, dropdown panels float over strong brand backgrounds, and CTAs get shadow reinforcement on hover. Premium Nitro sections replace some literal shadow with contrast, neon accents, and dark atmospheric backgrounds.

**Components**
Buttons

`button-primary` is the canonical Discord CTA: `{colors.primary}` fill, white text, and a soft `{rounded.xl}` or pill silhouette. It appears as the main subscribe, download, or proceed action and should feel bold but welcoming rather than severe.

`button-primary-active` deepens the same hue rather than changing shape. Preserve the same radius and weight so the state feels like a pressed version of the same object.

`button-secondary` is the white pill counterpart used on bright heroes and branded slabs. It relies on contrast reversal, not outline logic, to stand beside the primary action.

`button-secondary-on-dark` is the smaller white utility pill used in headers and contextual placements. It keeps the friendliness of the broader button language while shrinking into navigation scale.

`button-utility-dark` is the dark counterpart for places where the background is light and the action needs extra authority. It is still rounded and friendly, never sharp or enterprise-boxy.

`button-utility-outline` is a rarer, more utilitarian style seen in lighter product or brand-management contexts. Its small radius makes it feel more interface-like than campaign-like.

`button-search-pill` belongs to search and compact action contexts. The circular or pill enclosure around a single icon is a Discord pattern that keeps utility controls consistent with the broader rounded system.

Cards & Containers

`card-feature` is the main light marketing card: white fill, moderate radius, roomy padding, and only light shadowing if any. It supports explanatory content without overpowering the surrounding illustration system.

`card-surface` uses `{colors.surfaceAlt}` to signal structured information rather than spotlight content. This is common for safety hubs, feature summaries, and calm utility modules.

`card-elevated-marketing` is a smaller lifted unit with tighter radius and a more noticeable shadow. It is used where Discord wants a card to feel collectible or hoverable.

`card-nitro-gradient` is a signature premium move: a colorful gradient or high-chroma fill inside a soft rounded container. It should read like a premium perk tile, not a default card style.

Inputs & Forms

`input-search` stays clean and straightforward: white field, soft border, readable `gg sans`, and often paired with a rounded blue action button. Inputs are not a major decorative playground for Discord.

Navigation

`nav-topbar` is deceptively simple at first glance, but the distinct pattern is the rich dropdown system beneath it. Primary links are text-forward, medium-weight, and spaced evenly inside a tall horizontal bar.

`nav-dropdown-mega` is one of Discord’s clearest signature components. Dropdowns are multi-column, generously padded, and decorated with illustrative characters or objects that extend the brand story right inside navigation.

`footer-dropdown-mobile` mirrors the navigation hierarchy in a mobile-friendly accordion form. Discord does not change language radically between desktop and mobile; it mainly changes density and disclosure behavior.

Pricing

`pricing-promo-banner` is the Nitro-specific announcement strip that sits above the main navigation on pricing pages. It uses a dark premium background with a bright CTA to create urgency without leaving the brand family.

Signature Components

`docs-sidebar` represents Discord’s documentation mode: darker chrome, denser navigation, smaller corner language, and a more tool-like posture while still retaining `{colors.primary}` accents and `gg sans`.

The Nitro hero pattern is also signature even though it is not a single tokenized component. It combines oversized italicized or emphatic headings, dark atmospheric surfaces, floating character art, and premium accent colors to create a “game perk unlock” mood rather than a normal pricing header.

**Do's and Don'ts**
Do's

- Use `{colors.primary}` as the dominant action and brand field before introducing secondary accent colors.
- Pair `{typography.display}` or `{typography.hero}` with `{typography.body-lg}` to recreate Discord’s high-low type contrast.
- Keep primary CTAs rounded to `{rounded.xl}` or `{rounded.pill}` so actions feel soft and social.
- Alternate `{colors.canvas}` and `{colors.surface}` section bands to preserve Discord’s clear marketing rhythm.
- Use `{spacing.lg}` and `{spacing.xl}` inside cards instead of cramming text into dense blocks.
- Reserve `{colors.nitro-mint}` and `{colors.nitro-pink}` for premium or celebratory moments, not baseline navigation.
- Let mega-navigation feel illustrative and content-rich rather than reducing it to plain text lists.

Don'ts

- Don’t replace `{colors.primary}` with a generic SaaS blue; the exact Blurple family is part of the brand memory.
- Don’t flatten all corners to `{rounded.sm}`; Discord’s action language depends on rounded pills and soft capsules.
- Don’t set long body copy in ABC Ginto display faces; keep utility reading in `{typography.body}` or `{typography.body-lg}`.
- Don’t use heavy glass, blur cards, or luxury gradients on standard marketing sections where Discord is mostly flat and solid.
- Don’t turn the nav into a minimal monochrome bar; the dropdown illustration system is part of the brand identity.
- Don’t over-muted body copy past `{colors.body}` and `{colors.muted}`; Discord still reads clearly and directly.
- Don’t use premium Nitro accents across ordinary docs or safety content; it dilutes the base product language.

**Responsive Behavior**
| Breakpoint | Range | Notes |
|---|---|---|
| `xs` | `0-479px` | Mobile-first collapse, full-width stacks, burger nav |
| `sm` | `480-767px` | Large phone / small tablet, simplified hero media |
| `md` | `768-991px` | Tablet landscape, reduced multi-column layouts |
| `lg` | `992-1279px` | Desktop baseline, full navigation and dropdowns |
| `xl` | `1280-1539px` | Wide desktop, larger content containers |
| `xxl` | `1540px+` | Campaign-wide layouts and roomy hero staging |

Touch targets trend toward at least the mid-40px range, with many CTA heights landing around 50px or above. This keeps the pill button language usable on touch devices without changing visual character.

Collapsing strategy:
- Collapse top nav into a burger menu below desktop thresholds visible in the CSS media queries.
- Stack hero content into a single centered column before shrinking headline drama too aggressively.
- Reduce multi-column cards from 3-up to 2-up to 1-up while preserving large section spacing.
- Convert footer link groups into dropdown toggles on smaller screens rather than dumping a long static list.
- Hide or simplify decorative illustrations before sacrificing CTA clarity or headline legibility.

Images stay responsive and often switch from side-by-side scenic composition to centered supporting art. Large branded illustrations are important, but Discord generally treats them as flexible atmosphere, not as fixed editorial crops.

**Iteration Guide**
1. Check the first impression: does the screen clearly feel powered by `{colors.primary}` and not by a generic blue or neutral palette?
2. Audit headline DNA against `{typography.display}` or `{typography.hero}`; if the heading looks merely bold instead of tightly tracked and theatrical, it is off-brand.
3. Verify CTAs use `{rounded.xl}` or `{rounded.pill}` and not small corporate rectangles.
4. Confirm supporting copy sits in `{typography.body}` or `{typography.body-lg}` with `{colors.body}` rather than under-contrasted gray.
5. Review section rhythm: major blocks should breathe at roughly `{spacing.section}`, with 24px to 32px internal cadence inside cards and modules.
6. Inspect navigation: if dropdowns feel plain, add the content grouping and illustrative richness implied by `nav-dropdown-mega`.
7. For premium screens, make sure Nitro accents like `{colors.nitro-mint}` are used as accents around the base Discord system, not as a total palette replacement.
8. Compare depth cues: if the design depends on strong shadows to create hierarchy, reduce them and restore hierarchy through type, color, and spacing.

**Known Gaps**
This extraction is strongest where values were directly observed in live Discord surfaces on 2026-05-20: the homepage, Nitro page, Safety page, and Developer Docs page. Core color values like `{colors.primary}`, `{colors.light-blurple}`, the docs dark background family, and `gg sans` usage are directly evidenced. Several button, card, radius, and shadow values were also pulled from live CSS rules.

Some system values are synthesized from repeated patterns rather than from a single canonical token file. In particular, the typography hierarchy merges multiple observed headline classes into a usable normalized scale, and a few border tokens were inferred from repeated light gray edges. The docs surface also uses a Mintlify shell with Discord-specific overrides, so its density and some utility colors reflect a platform plus brand combination rather than a standalone first-party token source.

The pricing page exists as the Nitro page rather than a conventional comparison table, so “Pricing” here is interpreted as premium-product merchandising rather than card-by-card price plan UI. Where a component name in this file sounds more systematic than Discord’s raw class naming, that is intentional normalization for DESIGN.md usefulness, not evidence that Discord itself publishes the same semantic token names.
