---
version: alpha
name: Framer
slug: framer
source: "https://www.framer.com/"
extractedAt: "2026-05-22"
description: "Dark, product-led web-building identity with electric Framer Blue, tight Geist typography, pill actions, compact glassy nav, and screenshot-heavy modules that make publishing feel instant."

colors:
  primary: "#0099ff"
  accent: "#8555ff"
  accentHover: "#33adff"
  accentPressed: "#0077cc"
  ink: "#ffffff"
  body: "#ffffff99"
  muted: "#999999"
  canvas: "#000000"
  surface: "#191919"
  surfaceAlt: "#242424"
  border: "#ffffff1a"
  borderStrong: "#ffffff26"
  link: "#0099ff"
  success: "#24d164"
  warning: "#ffcd36"
  error: "#ff4d4d"
  editor-panel: "#1f1f1f"
  dark-card: "#141414"
  dark-card-raised: "#1c1c1c"
  on-primary: "#ffffff"

typography:
  display:
    fontFamily: "Geist Variable, Geist, Inter, sans-serif"
    fontSize: 96px
    fontWeight: 600
    lineHeight: 1.0
    letterSpacing: "-0.02em"
  hero:
    fontFamily: "Geist Variable, Geist, Inter, sans-serif"
    fontSize: 72px
    fontWeight: 600
    lineHeight: 1.0
    letterSpacing: "-0.02em"
  headline-lg:
    fontFamily: "Geist Variable, Geist, Inter, sans-serif"
    fontSize: 56px
    fontWeight: 600
    lineHeight: 1.05
    letterSpacing: "-0.02em"
  title-lg:
    fontFamily: "Geist Variable, Geist, Inter, sans-serif"
    fontSize: 32px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: "-1px"
  title-md:
    fontFamily: "Geist Variable, Geist, Inter, sans-serif"
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: "-0.5px"
  title-sm:
    fontFamily: "Geist Variable, Geist, Inter, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: "-0.01em"
  body:
    fontFamily: "Inter, Inter Placeholder, Geist, sans-serif"
    fontSize: 15px
    fontWeight: 500
    lineHeight: 1.6
    letterSpacing: "-0.01em"
  label:
    fontFamily: "Inter, Inter Placeholder, Geist, sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.0
    letterSpacing: "-0.01em"
  button:
    fontFamily: "Inter, Inter Placeholder, Geist, sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.0
    letterSpacing: "-0.01em"
  caption:
    fontFamily: "Inter, Inter Placeholder, Geist, sans-serif"
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: "0em"
  code:
    fontFamily: "Geist Mono, JetBrains Mono, monospace"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: "0em"
  pricing-display:
    fontFamily: "Geist Variable, Geist, Inter, sans-serif"
    fontSize: 56px
    fontWeight: 600
    lineHeight: 1.0
    letterSpacing: "-0.02em"

rounded:
  sm: 5px
  md: 8px
  lg: 10px
  xl: 16px
  pill: 9999px

spacing:
  xs: 5px
  sm: 10px
  md: 15px
  lg: 20px
  xl: 40px
  section: 120px

components:
  button-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button}"
    rounded: "{rounded.pill}"
    padding: "12px 20px"
  button-primary-active:
    backgroundColor: "{colors.accentPressed}"
    textColor: "{colors.on-primary}"
  button-secondary:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    rounded: "{rounded.pill}"
    padding: "12px 20px"
  button-ghost:
    backgroundColor: "transparent"
    textColor: "{colors.ink}"
    padding: "10px 15px"
  button-dark-outline:
    backgroundColor: "{colors.surface}"
    borderColor: "{colors.border}"
    padding: "10px 15px"
  nav-pill:
    backgroundColor: "{colors.canvas}"
    borderColor: "{colors.border}"
    padding: "10px"
  hero-product-stage:
    backgroundColor: "{colors.canvas}"
    borderColor: "{colors.border}"
    rounded: "{rounded.xl}"
    shadow: "0px 25px 50px rgba(0,0,0,0.25), 0px 5px 25px rgba(0,0,0,0.5)"
  feature-card:
    backgroundColor: "{colors.dark-card}"
    borderColor: "{colors.border}"
    padding: "20px"
  screenshot-card:
    backgroundColor: "{colors.surfaceAlt}"
    borderColor: "{colors.border}"
    shadow: "0px 10px 20px rgba(0,0,0,0.2), 0px 2px 4px rgba(0,0,0,0.25)"
  editor-panel:
    backgroundColor: "{colors.editor-panel}"
    borderColor: "{colors.border}"
    padding: "10px"
  input-dark:
    backgroundColor: "{colors.surface}"
    borderColor: "{colors.border}"
    padding: "12px 15px"
  pricing-card:
    backgroundColor: "{colors.surface}"
    borderColor: "{colors.border}"
    padding: "30px"
  pricing-table-row:
    backgroundColor: "transparent"
    borderColor: "{colors.border}"
    padding: "15px 0"
  resource-tile:
    backgroundColor: "{colors.dark-card-raised}"
    borderColor: "{colors.border}"
    padding: "10px"
---

**Overview**
Framer's current visual identity is dark, precise, and product-native. The marketing pages use a near-black canvas, crisp white type, electric Framer Blue for action, and large live-product imagery rather than generic illustration. The mood is confident and fast: layouts feel like an extension of the editor itself, with compact control surfaces, screenshot modules, and motion-ready cards doing most of the storytelling.

The brand has two linked modes. The marketing mode is cinematic and high contrast, with oversized type, pill calls to action, and deep product stages. The utility/docs/pricing mode is denser and calmer: the same dark shell, but more table structure, 15px body text, thin white-alpha borders, and cards that feel like app panels. Both modes share a strong black-white-blue axis and a rhythm built around 5px/10px increments.

Key Characteristics:
- Lead with {colors.canvas}, {colors.ink}, and {colors.primary}; the brand is dark-first and action-blue.
- Use tight Geist/Inter typography with negative tracking on headings and compact body copy.
- Prefer pill buttons and compact rounded panels over ornate shapes.
- Let real product screenshots, editor panels, templates, plugins, and CMS/analytics UI become the main visual assets.
- Use thin alpha borders and modest shadows to separate layers on black.
- Keep spacing deliberate: small internal gaps, wider section breathing room, and 1200px content rails.
- Make product modules feel interactive through layered panels, grids, avatars, status dots, and UI chrome.

**Colors**
Primary & Action

`primary` / `framer-blue` is the brand action color. Use {colors.primary} for primary CTAs, active pills, focused controls, product highlights, links, and small UI accents inside dark surfaces.

`accent` is a secondary product accent seen in feature/editor visuals. Use {colors.accent} sparingly for advanced capabilities, AI/editor affordances, and visual contrast beside {colors.primary}; it should not replace the main CTA color.

`accentHover` and `accentPressed` define interaction around blue actions. Hover can brighten the electric feel, while pressed states should become deeper and more saturated so pill buttons still read as active on black.

`link` follows the Framer Blue role. Links should stay clean and unadorned unless inside long-form help content, where a subtle underline on hover is acceptable.

Surfaces

`canvas` is the default page environment. Use {colors.canvas} as the base for homepage, product, pricing, and docs shells; avoid light-page inversions unless recreating a screenshot or embedded content.

`surface` is the primary card and pricing surface. It is just lifted enough from black to support panels, plan cards, and form fields without making the layout feel gray.

`surfaceAlt`, `dark-card`, and `dark-card-raised` create the product-panel family. These are for feature cards, resource tiles, editor chrome, and stacked screenshot frames where multiple dark levels need to remain legible.

`editor-panel` is the app-specific neutral. Use it for inspector panels, toolbar mockups, code blocks, command bars, and UI details that should look native to Framer's builder.

Neutrals & Text

`ink` is the highest-contrast foreground and should carry headlines, prices, nav items, and primary labels.

`body` is soft white text used for descriptive copy. It keeps large dark sections from becoming too stark while still passing comfortably on {colors.canvas}.

`muted` is for lower-priority labels, metadata, card captions, and inactive states. It should not be used for core instructions or key plan limits.

`border` and `borderStrong` are white-alpha dividers. Framer rarely uses heavy strokes; borders should feel like light catching an edge of glass or metal.

Semantic

`success` is reserved for completed states, check marks, availability, and positive billing/hosting signals. Use it as a small token, not a dominant surface.

`warning` appears in product-style accents and caution states. Use {colors.warning} in compact badges, usage warnings, or editor-style indicators.

`error` is for destructive or failed states. Keep it direct and restrained; Framer's visual system does not lean on big red alert panels.

Brand-specific signatures

`border` is a structural material. It appears as borders, separators, subtle fills, and inset outlines across dark cards.

`body` supports overlays and image treatments as soft white copy. Use it to preserve readable hierarchy over media or dark screenshot stages without blurring the asset.

`warning` is also an observed supporting accent in product/demo visuals. Use it only inside illustrative UI modules, never as the primary brand action.

**Typography**
Framer uses Geist Variable/Geist for its most recognizable display voice, with Inter/Inter Placeholder also present across generated text and interface copy. The type is geometric, clean, and compact. Large headings are tightly tracked and often sit at a 1.0 to 1.05 line-height, while body text lands at 15px with a generous 1.6 line-height for readability on dark.

| Level | Size | Weight | Line Height | Letter Spacing | Role |
|---|---:|---:|---:|---:|---|
| display | 96px | 600 | 1.0 | -0.02em | Hero-scale launch statements |
| hero | 72px | 600 | 1.0 | -0.02em | Standard page hero headings |
| headline-lg | 56px | 600 | 1.05 | -0.02em | Section headlines and pricing display |
| title-lg | 32px | 600 | 1.25 | -1px | Feature headers and card leads |
| title-md | 24px | 600 | 1.25 | -0.5px | Plan names and module titles |
| title-sm | 18px | 600 | 1.3 | -0.01em | Card titles and FAQ prompts |
| body | 15px | 500 | 1.6 | -0.01em | Core explanatory copy |
| label | 13px | 500 | 1.0 | -0.01em | Nav, metadata, pills, plan labels |
| button | 15px | 600 | 1.0 | -0.01em | Button text |
| caption | 12px | 500 | 1.25 | 0em | Badges, helper text, compact captions |
| code | 13px | 500 | 1.4 | 0em | Snippets, command bars, technical UI |
| pricing-display | 56px | 600 | 1.0 | -0.02em | Plan prices and large numeric values |

Principles:
- Track headings negatively; the Framer voice gets sharper as type gets larger.
- Keep weights mostly 500-600. Heavy weights appear in font assets, but the visible system is not bulky.
- Use 15px as the default product-marketing body size; resist inflating normal copy to 18px unless it is a short hero subhead.
- Preserve short line heights in buttons, labels, and nav so controls feel compact and app-like.
- Use mono fonts only for code, command bars, and editor-flavored details, not for general brand copy.

**Layout**
Framer pages sit on a 1200px max content rail with responsive side gutters of roughly 40px on tablet and 20px on mobile. Internal component rhythm is compact: 5px, 10px, 15px, and 20px recur constantly in gaps, padding, and small control clusters. Larger page composition opens up at 40px, 60px, and 120px for section rhythm.

Grid behavior is modular rather than magazine-like. Marketing sections use two to four columns of feature cards, resource tiles, screenshots, or pricing plans, then collapse into stacked single-column modules under mobile widths. Product stages often use fixed-aspect screenshots centered in the rail, with surrounding controls and small cards aligned to a strict editor-like grid.

Whitespace philosophy: use black space as a premium material. Framer does not fill every viewport with decorations; it lets strong headings, product UI, and crisp panels breathe. The whitespace should feel like a dark canvas around a design tool, not an empty landing page.

**Elevation & Depth**
Framer's depth is restrained and practical. The most common separation is a 1px white-alpha border, often {colors.border}, paired with a dark surface one step above the canvas. Shadows appear most strongly around screenshot stages and floating product panels, where values like `0px 25px 50px rgba(0,0,0,0.25), 0px 5px 25px rgba(0,0,0,0.5)` create a dense black-on-black lift.

Small UI panels use tighter shadows such as `0px 2px 4px rgba(0,0,0,0.15)` plus a subtle edge line. Avoid bright glows except for rare blue product highlights. Hierarchy should come from scale, contrast, border alpha, and authentic product imagery more than from decorative depth.

**Components**
Buttons

`button-primary` is a Framer Blue pill. It should be the clearest path to start, publish, upgrade, or launch; keep it compact, high contrast, and horizontally padded.

`button-primary-active` is the pressed or selected version of the same action. Use the deeper blue so it remains connected to {colors.primary} without looking disabled.

`button-secondary` is a white pill on dark. It works for paired hero actions such as AI start flows or secondary conversion moments where Framer wants equal visibility without duplicating blue.

`button-ghost` is a text-first pill used in nav, menus, and low-pressure actions. It should feel integrated with the dark header rather than floating as a separate button.

`button-dark-outline` is for utility actions on cards and tables. It uses dark fill plus {colors.border}, making it suitable for pricing, docs, and editor-like surfaces.

Cards & Containers

`hero-product-stage` is the large cinematic screenshot container. It frames real interface imagery, template previews, or product demos with rounded corners, dark shadow, and a thin border.

`feature-card` is the standard explanatory module. It combines compact padding, dark fill, short titles, muted copy, and usually a product visual or icon-like screenshot detail.

`screenshot-card` is a raised card for website previews, editor captures, or CMS/analytics panels. It should prioritize asset clarity over decorative framing.

`editor-panel` recreates the Framer app surface. Use it for inspector controls, command bars, layer panels, property fields, and any feature explanation that benefits from feeling embedded in the product.

`resource-tile` is the community marketplace pattern used for templates, plugins, and components. It pairs a preview image with short metadata and a compact action, often in horizontally scrolling or dense grid contexts.

Inputs & Forms

`input-dark` is the default form field. It uses a dark fill, white text, alpha border, and 10px radius; keep labels small and helper text muted.

Forms should be sparse. Framer's marketing pages avoid heavy form UI, so use single-line fields, compact stacked groups, and button adjacency rather than large boxed form sections.

Navigation

`nav-pill` is the signature header shell. It appears as a dark rounded capsule with compact spacing, white text, and subtle borders, often floating visually above the page content.

Navigation links should be short, centered vertically, and calm. Dropdowns or product menus should use the same panel logic as `editor-panel`, with thin dividers and small labels.

Pricing

`pricing-card` presents each plan as a dark rounded panel with clear hierarchy: plan name, price, short fit statement, compact features, and a pill action.

`pricing-table-row` is the comparison rhythm. Rows should use thin dividers, small type, and restrained check/empty indicators; avoid colorful comparison charts that compete with the blue action system.

Signature Components

Product UI collage is central to Framer. Build signature sections from layered editor panels, website previews, avatars, CMS tables, analytics graphs, plugin cards, and template tiles.

Community resource rails are also distinctive. Templates, Plugins, and Components appear as real marketplace objects, so tiles should show concrete previews and concise labels rather than abstract illustrations.

Feature proof modules should look publishable. When explaining design, CMS, localization, analytics, or SEO, use screenshot-like frames and interface fragments so the brand reads as a working web builder.

**Do's and Don'ts**
Do:
- Use {colors.canvas} as the default page background and reserve light surfaces for embedded screenshot content.
- Make primary actions {colors.primary} pills with {typography.button} and {rounded.pill}.
- Set major headlines in {typography.display}, {typography.hero}, or {typography.headline-lg} with tight negative tracking.
- Use {colors.border} for card edges, table rows, dropdowns, and nav shells instead of heavy strokes.
- Build feature sections around `hero-product-stage`, `screenshot-card`, and `editor-panel` patterns.
- Keep component padding on the 10px/15px/20px rhythm so the UI feels native to Framer.
- Use real product, template, plugin, or website-preview imagery whenever a visual module is needed.
- Pair large black whitespace with concise copy; let product surfaces carry the detail.

Don't:
- Do not turn Framer into a light SaaS template; {colors.canvas} is foundational.
- Do not replace {colors.primary} with purple, orange, or green for main CTAs.
- Do not use beige, pastel, or multicolor illustration palettes for core marketing sections.
- Do not make large rounded blobs, glass orbs, or decorative gradients that are not tied to product imagery.
- Do not over-round cards beyond {rounded.xl}; reserve {rounded.pill} for buttons, avatars, and compact pills.
- Do not use heavy drop shadows on every card; most hierarchy should come from border alpha and surface level.
- Do not center long paragraphs under every heading; Framer copy is short, direct, and product-led.
- Do not show generic device mockups when an actual editor panel or website screenshot would be more on-brand.

**Responsive Behavior**
| Breakpoint | Width | Behavior |
|---|---:|---|
| mobile-sm | 390px | Single-column content, 20px gutters, stacked CTAs |
| mobile | 810px | Collapse grids, reduce hero type, hide complex nav behind menu |
| tablet | 1200px | Two-column feature grids, 40px gutters, compact nav retained |
| desktop | 1440px | 1200px content rail, multi-column pricing and resource grids |
| wide | 1920px | Center rail remains stable; product stages may scale but should not fill edge-to-edge |

Touch targets should be at least 44px high for buttons, menu items, and pricing actions. Pills can look visually compact, but their clickable area should remain generous.

Collapsing strategy:
- Stack pricing cards before shrinking their internal content too far.
- Collapse multi-column feature cards into one column with the image above or below text.
- Keep the nav pill compact on tablet, then move links into a dark panel menu on mobile.
- Crop screenshot stages carefully; preserve the recognizable editor chrome and primary product detail.
- Reduce hero display size before reducing CTA size; actions must stay tappable.

Image behavior: product screenshots should remain sharp, centered, and framed with rounded dark containers. Avoid aggressive blur or dark overlays that hide the actual interface, because Framer's credibility comes from showing the tool and the sites it creates.

**Iteration Guide**
1. Check the background first: the page should read from {colors.canvas}, not from gray, blue, or a gradient.
2. Verify the action hierarchy: one dominant {colors.primary} CTA per section, with secondary actions as white or ghost pills.
3. Audit heading type: large headlines should use Geist-like geometry, 600 weight, tight tracking, and near-solid line-height.
4. Inspect card edges: panels should use {colors.border} or {colors.borderStrong}, not thick opaque borders.
5. Confirm product specificity: every major visual should resemble Framer output, the editor, templates, CMS, plugins, analytics, or publishing workflows.
6. Test spacing rhythm: internal gaps should land on 5px/10px/15px/20px, with section rhythm opening up to 60px/120px.
7. Review shadows: reserve deep shadows for screenshot stages and floating product UI; flatten ordinary feature cards.
8. Validate mobile: pricing, resource grids, and feature modules should stack cleanly while preserving 44px touch targets.

**Known Gaps**
Observed directly: the homepage, `/design/` feature page, `/pricing/` page, and a help/docs article were fetched on May 22, 2026. Repeated CSS values confirmed the dominant color set, common font families, frequent type sizes, line heights, border radii, spacing values, and shadow styles.

Derived: semantic token names, hover/pressed colors, and some component abstractions were normalized from recurring raw CSS values and visual patterns. The source uses generated Framer class names and token IDs, so this document maps them into stable design-system roles.

Uncertain: exact responsive type ramps, all animation timings, and every stateful component variant were not fully reconstructable from static HTML alone. The guidance is conservative: it preserves the observed black/white/blue identity, compact pill controls, thin alpha borders, and product-screenshot language without inventing unrelated decorative effects.
