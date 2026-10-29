---
version: alpha
name: Strawberry
slug: strawberry
source: https://strawberrybrowser.com/
extractedAt: 2026-05-31
description: "Warm off-white AI-browser identity with custom Strawberry type, ink-black pill actions, coral micro-markers, rounded cream panels, animated companions, and chat-like browser automation modules."

colors:
  primary: "#252522"
  accent: "#F2805D"
  accentHover: "#E97452"
  accentPressed: "#D96544"
  ink: "#252522"
  body: "#252522"
  muted: "#858481"
  canvas: "#FFFCFA"
  surface: "#FFFEFE"
  surfaceAlt: "#F7F2ED"
  border: "#EFE6DC"
  borderStrong: "#E6DBD1"
  link: "#252522"
  success: "#22C55E"
  warning: "#C8B828"
  error: "#EF4343"
  signature-coral: "#F2805D"
  berry-red: "#ED5A31"
  leaf-gold: "#D6C530"
  golden-olive: "#AD9D25"
  valid-green: "#50AD25"
  feature-blue: "#678FFF"
  feature-lavender: "#ACA0DF"
  subtle-stroke: "#EFEBE7"
  shadow-tint: "#0000000D"
  shadow-tint-strong: "#0000001A"
  on-primary: "#FFFCFA"
  on-dark: "#FFFCFA"

typography:
  display: { fontFamily: "Strawberry Sans, system-ui, -apple-system, sans-serif", fontSize: 72px, fontWeight: 480, lineHeight: 1.1, letterSpacing: "-0.04em" }
  hero: { fontFamily: "Strawberry Sans, system-ui, -apple-system, sans-serif", fontSize: 52.8px, fontWeight: 480, lineHeight: 1.1, letterSpacing: "-0.04em" }
  headline-lg: { fontFamily: "Strawberry Sans, system-ui, -apple-system, sans-serif", fontSize: 56px, fontWeight: 480, lineHeight: 1.1, letterSpacing: "-0.04em" }
  title-lg: { fontFamily: "Strawberry Sans, system-ui, -apple-system, sans-serif", fontSize: 40px, fontWeight: 480, lineHeight: 1.2, letterSpacing: "-0.04em" }
  title-md: { fontFamily: "Strawberry Sans, system-ui, -apple-system, sans-serif", fontSize: 24px, fontWeight: 480, lineHeight: 1.4, letterSpacing: "-0.03em" }
  title-sm: { fontFamily: "Strawberry Sans, system-ui, -apple-system, sans-serif", fontSize: 18px, fontWeight: 500, lineHeight: 1.4, letterSpacing: "-0.03em" }
  body: { fontFamily: "Strawberry Sans, system-ui, -apple-system, sans-serif", fontSize: 16px, fontWeight: 400, lineHeight: 1.6, letterSpacing: "0em" }
  body-lg: { fontFamily: "Strawberry Sans, system-ui, -apple-system, sans-serif", fontSize: 18px, fontWeight: 400, lineHeight: 1.4, letterSpacing: "-0.0075em" }
  label: { fontFamily: "Strawberry Sans, system-ui, -apple-system, sans-serif", fontSize: 14px, fontWeight: 500, lineHeight: 1.4, letterSpacing: "-0.0075em" }
  button: { fontFamily: "Strawberry Sans, system-ui, -apple-system, sans-serif", fontSize: 15px, fontWeight: 500, lineHeight: 1.4, letterSpacing: "0em" }
  nav: { fontFamily: "Strawberry Sans, system-ui, -apple-system, sans-serif", fontSize: 15.32px, fontWeight: 400, lineHeight: 1.2, letterSpacing: "-0.1px" }
  caption: { fontFamily: "Strawberry Sans, system-ui, -apple-system, sans-serif", fontSize: 13px, fontWeight: 400, lineHeight: 1.4, letterSpacing: "-0.0075em" }
  legal: { fontFamily: "Strawberry Sans, system-ui, -apple-system, sans-serif", fontSize: 12px, fontWeight: 400, lineHeight: 1.4, letterSpacing: "0em" }
  pricing-display: { fontFamily: "Strawberry Sans, system-ui, -apple-system, sans-serif", fontSize: 40px, fontWeight: 500, lineHeight: 1.2, letterSpacing: "-0.04em" }
  serif-accent: { fontFamily: "Strawberry Serif, Georgia, serif", fontSize: 40px, fontWeight: 500, lineHeight: 1.1, letterSpacing: "-0.02em" }

rounded:
  xs: 4px
  sm: 8px
  md: 12px
  lg: 16px
  xl: 24px
  input: 29px
  bubble: 28px
  pill: 9999px

spacing:
  xs: 4px
  sm: 8px
  md: 16px
  lg: 24px
  xl: 32px
  xxl: 48px
  section: 120px
  container: 1080px
  pageGutter: 29.6px

components:
  button-primary: { backgroundColor: "{colors.primary}", textColor: "{colors.on-primary}", typography: "{typography.button}", rounded: "{rounded.pill}", padding: 12px 32px }
  button-primary-hover: { backgroundColor: "{colors.primary}", textColor: "{colors.on-primary}", rounded: "{rounded.pill}", opacity: 0.9 }
  button-primary-active: { backgroundColor: "{colors.primary}", textColor: "{colors.on-primary}", rounded: "{rounded.pill}", opacity: 0.8 }
  button-secondary: { backgroundColor: "{colors.surfaceAlt}", textColor: "{colors.ink}", borderColor: "{colors.borderStrong}", typography: "{typography.label}", rounded: "{rounded.pill}", padding: 12px 24px }
  button-ghost-nav: { backgroundColor: transparent, textColor: "{colors.muted}", typography: "{typography.nav}", rounded: "{rounded.xs}", padding: 8px 14px }
  button-icon: { backgroundColor: transparent, textColor: "{colors.muted}", rounded: "{rounded.pill}", size: 32px }
  hero-input: { backgroundColor: "{colors.surface}", textColor: "{colors.ink}", borderColor: "{colors.borderStrong}", typography: "{typography.body}", rounded: "{rounded.input}", padding: 14px 14px 12px, shadow: "0 6px 24px {colors.shadow-tint}, 0 0 0 1px {colors.borderStrong}" }
  use-case-card: { backgroundColor: "{colors.surfaceAlt}", textColor: "{colors.ink}", rounded: "{rounded.xl}", padding: 32px }
  testimonial-card: { backgroundColor: "{colors.surfaceAlt}", textColor: "{colors.ink}", rounded: "{rounded.xl}", padding: 16px }
  feature-icon-stack: { backgroundColor: "{colors.canvas}", borderColor: "{colors.surfaceAlt}", rounded: "{rounded.pill}", size: 44px }
  pricing-card: { backgroundColor: "{colors.surfaceAlt}", textColor: "{colors.ink}", rounded: "{rounded.xl}", padding: 32px 24px }
  pricing-card-popular: { backgroundColor: "{colors.surfaceAlt}", textColor: "{colors.ink}", outlineColor: "{colors.signature-coral}", rounded: "{rounded.xl}", outlineWidth: 3px }
  pricing-chip: { backgroundColor: "{colors.signature-coral}", textColor: "{colors.on-primary}", typography: "{typography.button}", rounded: "{rounded.pill}", padding: 5px 16px }
  billing-toggle: { backgroundColor: "{colors.surfaceAlt}", textColor: "{colors.muted}", rounded: "{rounded.md}", padding: 4px }
  billing-toggle-active: { backgroundColor: "{colors.canvas}", textColor: "{colors.ink}", rounded: "{rounded.sm}", shadow: "0 1px 3px {colors.shadow-tint-strong}" }
  chat-bubble-companion: { backgroundColor: "{colors.surfaceAlt}", textColor: "{colors.ink}", typography: "{typography.body-lg}", rounded: "{rounded.bubble}", padding: 15px 26px }
  chat-bubble-user: { backgroundColor: "{colors.primary}", textColor: "{colors.on-primary}", typography: "{typography.body-lg}", rounded: "{rounded.bubble}", padding: 15px 26px }
  nav-header: { backgroundColor: "{colors.canvas}", textColor: "{colors.muted}", height: 64px }
  nav-active-marker: { backgroundColor: "{colors.signature-coral}", size: 6px, shape: diamond }
  beta-badge: { backgroundColor: "{colors.surfaceAlt}", textColor: "{colors.muted}", typography: "{typography.legal}", rounded: "{rounded.xs}", padding: 4px 6px }
  fade-pattern-band: { backgroundColor: "{colors.canvas}", height: 232px }
  companion-video: { backgroundColor: transparent, rounded: 0px, objectFit: contain }
---

**Overview**

Strawberry is warm, compact, and deliberately product-native. The site does not look like a generic AI landing page: it feels like a browser interface crossed with a friendly assistant layer. The foundation is a pale cream canvas, custom soft grotesque typography, ink-black controls, and tiny coral signals that behave like a brand punctuation mark. The marketing pages use generous whitespace, but the actual component language is functional: prompt boxes, chat bubbles, companion figures, pricing cards, app icons, and migration flows.

The visual identity has two main modes. The marketing mode is calm and spacious, using centered display type, animated ambient grids, and broad rounded panels. The utility mode is closer to an operating surface: pill buttons, compact menus, circular icon buttons, app chips, stacked favicons, and speech bubbles. Both modes share the same warm palette and the same reduced contrast philosophy, so Strawberry feels soft without becoming decorative.

Key Characteristics:

- Custom `Strawberry Sans` drives nearly every text level, with `Strawberry Serif` available as a restrained accent.
- The canvas uses `{colors.canvas}` instead of pure white, making the product feel local, warm, and low-glare.
- Primary actions are ink pills, not colorful buttons; coral is saved for brand marks, active dots, chips, and feature glyphs.
- Panels use `{colors.surfaceAlt}` and `{rounded.xl}`, creating broad, friendly blocks with minimal border noise.
- The hero centers on an oversized prompt input, animated companions, and a fading ambient grid rather than a static screenshot.
- Interactive surfaces use opacity and subtle scaling instead of heavy color shifts.
- Chat bubbles and companion videos are signature product modules, not decorative add-ons.

**Colors**

Primary & Action:

`{colors.primary}` is the main action color and the same value as `{colors.ink}`. It appears on download CTAs, send buttons, pricing buttons, chat replies, and footer wordmarks. Use it for decisive actions where Strawberry needs confidence.

`{colors.accent}` is the signature coral. It appears in logo fruit, navigation active diamonds, pricing emphasis, and custom feature marks. It should punctuate the interface, not flood it.

`{colors.accentHover}` and `{colors.accentPressed}` are conservative derived states for coral chips or active markers. The source site more often changes opacity than hue, so these should be used sparingly.

Surfaces:

`{colors.canvas}` is the page background and header color. It is the default environment for marketing sections, documentation pages, and footer layouts.

`{colors.surface}` is the near-white elevated surface used by the hero message input and context menus. It should appear when an object needs to feel interactive and slightly closer than the page.

`{colors.surfaceAlt}` is the warm cream used for cards, CTAs, pricing plans, mobile menu separators, toggles, and companion bubbles. This is the main block color.

Neutrals & Text:

`{colors.ink}` is the dominant text and action color. It is almost black but slightly warm, which keeps the brand from feeling stark.

`{colors.body}` is equivalent to the primary text tone. Use opacity or `{colors.muted}` for hierarchy rather than introducing extra grays.

`{colors.muted}` represents the observed secondary text treatment. It is used for descriptions, navigation labels, footer headings, and helper copy.

`{colors.border}` and `{colors.borderStrong}` create very quiet separation. Borders usually support surfaces instead of outlining every component.

Semantic:

`{colors.success}` appears directly in the yearly billing badge. Keep it for positive savings, readiness, and confirmation.

`{colors.warning}` maps to the leaf/golden brand family and can support caution or highlighted status without leaving the palette.

`{colors.error}` is the destructive token from the global CSS. It is available for validation and destructive UI, but it is not a marketing color.

Brand-Specific Signatures:

`{colors.berry-red}` and `{colors.leaf-gold}` come from the Strawberry logo. Use them in identity marks and small illustrative details.

`{colors.golden-olive}` is used as an accent-green/olive value in the CSS. It pairs with the leaf mark and geometric feature tags.

`{colors.feature-blue}` and `{colors.feature-lavender}` appear in pricing feature markers. They are small taxonomy colors, not large backgrounds.

**Typography**

Strawberry uses `Strawberry Sans` as its primary variable face across headings, body, buttons, navigation, and product UI. `Strawberry Serif` is loaded at weight 500 but was not prominent in the observed pages; treat it as an optional editorial accent rather than the default headline family.

| Level | Size | Weight | Line Height | Letter Spacing |
|---|---:|---:|---:|---:|
| `{typography.display}` | 72px | 480 | 1.1 | -0.04em |
| `{typography.hero}` | 52.8px | 480 | 1.1 | -0.04em |
| `{typography.headline-lg}` | 56px | 480 | 1.1 | -0.04em |
| `{typography.title-lg}` | 40px | 480 | 1.2 | -0.04em |
| `{typography.title-md}` | 24px | 480 | 1.4 | -0.03em |
| `{typography.title-sm}` | 18px | 500 | 1.4 | -0.03em |
| `{typography.body-lg}` | 18px | 400 | 1.4 | -0.0075em |
| `{typography.body}` | 16px | 400 | 1.6 | 0em |
| `{typography.label}` | 14px | 500 | 1.4 | -0.0075em |
| `{typography.button}` | 15px | 500 | 1.4 | 0em |
| `{typography.nav}` | 15.32px | 400 | 1.2 | -0.1px |
| `{typography.caption}` | 13px | 400 | 1.4 | -0.0075em |
| `{typography.pricing-display}` | 40px | 500 | 1.2 | -0.04em |

Principles:

- Use medium-light heading weights around 480; Strawberry avoids the blunt heaviness common in SaaS hero type.
- Apply negative tracking to all headings, especially display and pricing numbers.
- Keep body copy loose and readable with 1.4 to 1.6 line-height.
- Use 500 weight for controls, tags, and plan names rather than full bold.
- Let muted color do more hierarchy work than type size changes.

**Layout**

The primary container maxes out at `{spacing.container}` with mobile gutters of `{spacing.pageGutter}` and desktop gutters near 20px. Layouts are centered and shallow: hero content stacks vertically, use-case cards form a 3-column grid on desktop, pricing plans form 4 columns at large widths, and FAQ/pricing support areas split into 2 columns only when space allows.

Spacing follows a soft 4/8 rhythm: `{spacing.xs}`, `{spacing.sm}`, `{spacing.md}`, `{spacing.lg}`, `{spacing.xl}`, and `{spacing.xxl}`. Larger sections expand to about `{spacing.section}` on desktop, while cards usually sit at 16px, 24px, or 32px internal padding.

Whitespace philosophy: leave large cream fields around hero and CTA moments, then compress product modules into dense rounded groups. Strawberry should feel calm at the page level and practical inside each component.

Section rhythm:

- Start hero sections with centered copy and a product module within the first viewport.
- Use 48px to 72px between a section heading and dense card grids.
- Use 12px to 20px grid gaps for repeated cards, keeping the cards visually close enough to read as one product set.
- Switch to full-width cream bands when the section is instructional or CTA-driven.
- Keep footer columns compact and low-contrast, with the logo and copyright given more breathing room than link groups.

**Elevation & Depth**

Strawberry is mostly flat. Depth appears when an element behaves like a product surface: the hero input, context menu, and billing toggle active state use quiet shadows. Cards usually rely on `{colors.surfaceAlt}`, spacing, radius, and typography instead of shadows.

The canonical elevated shadow is `0 6px 24px {colors.shadow-tint}` with a 1px border-like ring from `{colors.borderStrong}`. Smaller controls use `0 1px 3px {colors.shadow-tint-strong}`. Avoid deep drop shadows, glass panels, and glossy gradients.

**Components**

Buttons:

`button-primary` is an ink-black pill with cream text. It appears as Download, pricing CTA, contact CTA, and card links. The hover state reduces opacity, preserving the ink identity.

`button-secondary` is a cream pill with ink text and a subtle border. It fits account actions, mobile secondary actions, and quiet choices.

`button-ghost-nav` is text-first and low contrast until hover. The coral diamond from `nav-active-marker` supplies recognition.

`button-icon` is circular, 32px, and mostly transparent. It becomes visible through hover fill or ink send-state color.

Use arrow motion on link-like buttons. The observed card and FAQ arrows translate only a few pixels, so the interaction should feel like a nudge rather than a slide.

Use button text economically. Strawberry favors direct labels such as Download, Get Intern, Get Full-Time, and See how, with context provided by surrounding copy.

Cards & Containers:

`hero-input` is the most important product surface: wide, pill-rounded, near-white, softly shadowed, and animated. It should look like a browser command bar, not a generic newsletter input.

`use-case-card` uses `{colors.surfaceAlt}` with `{rounded.xl}` and no visible shadow. Its stacked favicon strip gives each card product specificity.

`testimonial-card` is similar but tighter, using 16px padding and occasional squared lower corners for a lightly tiled rhythm.

`feature-icon-stack` overlaps circular app icons with cream borders. This overlap pattern is central to the migration and use-case visuals.

Cream cards should not float alone on the canvas unless they belong to a repeated set. When a section needs a single large panel, use the wider `migrate-wrap`, `trust-wrap`, or CTA panel pattern.

When using testimonial cards, allow subtle variation through squared lower corners. This creates a hand-placed grid while keeping the dominant 24px rounding intact.

Inputs & Forms:

The main input pattern is the chat/prompt field. Use a large rounded container, internal bottom bar, muted placeholder opacity, plus and send icon buttons, and app tags inline with text.

Context menus are compact `{colors.surface}` panels with `{rounded.md}`, small rows, 13px text, and very low black hover fills.

App chips inside prompt text should be inline and sized to the current text, with 1em icons and small rounded app logos. They should read as inserted context, not as separate badges.

The send button is the only icon button that becomes a filled ink circle by default. Other icon buttons should stay quiet until hover or active state.

Navigation:

`nav-header` is fixed, 64px tall, and the same color as the canvas. The logo sits left, links center on desktop, and account/download actions right.

Active or hovered nav items use `nav-active-marker`, a tiny coral diamond placed below desktop links or to the left of mobile links. This marker is a key Strawberry signature.

The beta badge is intentionally tiny and muted. Keep it close to the logo, uppercase, and compact so it supports the brand status without competing with navigation.

Mobile navigation uses scale through type size rather than decorative backgrounds. Large muted links, cream canvas, and the coral marker are enough.

Pricing:

`pricing-card` is a cream plan block with 24px radius and dense vertical content. Plan names use 18 to 22px semi-bold type, while prices use the tracked `{typography.pricing-display}` style.

`pricing-card-popular` adds a 3px coral outline and floating `pricing-chip`. It should still feel like the same card family rather than a separate promotional banner.

`billing-toggle` is a cream segmented control with a white active segment and tiny shadow. The savings badge uses `{colors.success}` and should remain small.

Feature bullets use geometric marks rather than check icons. Preserve the circle, square, rhombus, and triangle vocabulary because it makes the plan tables feel branded.

Companion groups in pricing cards are centered, overlapping, and sometimes vertically offset. They communicate plan scale more warmly than numeric feature density alone.

Signature Components:

`chat-bubble-companion` and `chat-bubble-user` form the FAQ pattern. The companion bubble is cream and left-aligned; the user answer is ink, right-aligned, and animates from a slightly scaled state.

`companion-video` is a transparent, cropped animated character module. It should sit partly below hero content or inside pricing illustrations without a card frame.

`fade-pattern-band` uses repeated fade-pattern assets to soften transitions into CTA panels. Treat it as a background texture, never as a foreground illustration.

The ambient grid belongs behind the hero and should be partially masked by `{colors.canvas}`. It is a quiet systems cue, not a visible cyber-grid motif.

The migration flow uses circular browser nodes, vertical arrows, a Strawberry node, and a companion node. Use it when explaining "bring your browser data, then add AI" workflows.

**Do's and Don'ts**

Do:

- Use `{colors.canvas}` as the page base and reserve `{colors.surface}` for interactive elevated product surfaces.
- Build primary CTAs with `{colors.primary}`, `{colors.on-primary}`, and `{rounded.pill}`.
- Use `{colors.signature-coral}` only for markers, chips, outlines, and identity details.
- Keep major cards on `{colors.surfaceAlt}` with `{rounded.xl}` and little or no shadow.
- Apply negative tracking from `{typography.display}` and `{typography.title-lg}` to preserve the soft compact word shape.
- Use stacked circular favicons or companion visuals when representing automation workflows.
- Animate gently with opacity, small translate, or small scale changes.

Don't:

- Do not make coral the main CTA fill; the source CTA language is ink-first.
- Do not replace the warm canvas with pure white or cold gray.
- Do not introduce blue-purple gradients, glass blur, or glossy SaaS shadows.
- Do not square off main cards below `{rounded.lg}` except for intentional testimonial tile corners.
- Do not use heavy 700+ weights for hero or section headings.
- Do not outline every card; let cream surfaces and spacing define hierarchy.
- Do not use generic chatbot widgets when a Strawberry screen should use wide prompt bars or speech bubbles.

**Responsive Behavior**

| Breakpoint | Width | Behavior |
|---|---:|---|
| Compact | 400px | Hide complex migration flow if it cannot fit cleanly. |
| Mobile | 480px | Hero type moves from 42.4px toward 52.8px and keeps tight tracking. |
| Tablet | 768px | Cards can move to 2 columns; desktop companion extras become visible. |
| Desktop | 1024px | Header switches to full nav; pricing becomes 4 columns; large section spacing appears. |
| Wide | 1280px | Maintain 1080px content max; do not stretch text or cards indefinitely. |

Touch targets should stay at least 32px for icon buttons and 44px for primary mobile actions. Mobile navigation becomes a full-screen cream sheet below the 64px header, with large 22px links and coral left markers.

Collapsing strategy:

- Stack hero, pricing, FAQ, and migration layouts into single columns before reducing internal padding too far.
- Keep the hero input wider than the content text, even if it slightly overhangs on mobile as observed.
- Convert use-case grids from 3 columns to 2 columns, then 1 column.
- Preserve companion visuals where possible, but hide secondary companions before crowding the prompt.
- Keep company logo marquees masked at the edges and reduce logo width on mobile.

Images and videos should use `object-fit: contain`. Companion videos remain transparent and unframed; screenshots or illustrations sit inside cream panels only when the surrounding section is already a panel.

Image behavior:

- Keep companion videos visually independent from card frames.
- Let browser/app icons sit in circles with cream borders.
- Mask logo marquees at both edges so the scroll feels continuous.
- Use product illustrations in cream panels for trust and migration sections.
- Avoid dark, cropped, or photographic hero imagery; the product module is the hero visual.

**Iteration Guide**

1. Check the page background first: it should read as `{colors.canvas}`, not white, gray, or beige-heavy.
2. Verify all primary CTAs use `{components.button-primary}` and are pill-shaped with ink fill.
3. Audit heading weights and tracking against `{typography.display}` and `{typography.title-lg}`; remove heavy bolds.
4. Confirm cards use `{colors.surfaceAlt}` plus `{rounded.xl}` and avoid unnecessary border/shadow stacking.
5. Look for a Strawberry-specific product pattern: prompt input, speech bubbles, companion video, favicon stack, or coral diamond marker.
6. Ensure coral appears as punctuation only; if it dominates a hero or section, reduce it.
7. Check responsive grids at 768px and 1024px so cards do not squeeze below readable widths.
8. Review motion: use opacity, small vertical movement, and subtle scale; avoid dramatic parallax or spin effects.

9. Inspect navigation hover states and confirm the coral diamond is present but tiny.
10. Test pricing cards with long plan descriptions; text should wrap without changing the 24px card radius.
11. Check FAQ bubbles for left/right alignment and tail direction before approving.
12. Confirm mobile layouts keep touch targets large while preserving the warm, low-contrast palette.

**Known Gaps**

Observed directly: homepage, pricing page, getting-started use case page, tutorial content, delivered HTML, CSS variables, font-face declarations, button styles, navigation behavior, hero prompt input, pricing cards, FAQ bubbles, company marquee, testimonial cards, and companion video containers.

Research coverage:

- Homepage: hero, prompt input, company marquee, use-case cards, migration flow, testimonials, FAQ, and CTA.
- Pricing: billing toggle, plan cards, popular outline, geometric feature marks, credit explanation, FAQ, testimonials, and CTA.
- Use-case content: long-form editorial layout, real task examples, trust/safety copy, and plain-language companion framing.
- Tutorial content: docs-style hierarchy, metadata rows, concept lists, comparison copy, and footer behavior.

Derived: hover and pressed color tokens for coral actions are conservative derivations because the source mostly uses opacity changes. `{colors.muted}` is a blended representation of the observed alpha secondary text over the warm canvas.

Uncertain: `Strawberry Serif` is loaded but not strongly used in the observed surfaces, so the `serif-accent` token should be treated as available but optional. Some product imagery and companion colors are video/image assets rather than CSS tokens, so this file documents placement and component behavior more strongly than exact illustration palettes.

Extraction should be considered strongest for marketing/product UI structure, colors, typography, pricing, navigation, cards, prompt input, and FAQ patterns. It is less certain for future app-internal screens that may use additional tokens not exposed on the public site.
