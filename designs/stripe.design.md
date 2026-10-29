---
version: alpha
name: Stripe
slug: stripe
source: "https://stripe.com/"
extractedAt: "2026-05-18"
description: "Precision financial-infrastructure identity with violet action color, deep navy ink, angled Stripe geometry, product UI mockups, fine dashed dividers, and dense developer-first modules."

colors:
  primary: "#533afd"
  accent: "#635bff"
  accentHover: "#4032c8"
  accentPressed: "#2e2b8c"
  ink: "#0a2540"
  body: "#425466"
  muted: "#727f96"
  canvas: "#f6f9fc"
  surface: "#ffffff"
  surfaceAlt: "#fafbfd"
  border: "#e7ecf1"
  borderStrong: "#c1c9d2"
  link: "#635bff"
  success: "#09825d"
  warning: "#bb5504"
  error: "#cd3d64"
  brandViolet: "#533afd"
  brandVioletSoft: "#e8e9ff"
  signaturePurple: "#9966ff"
  signatureCyan: "#11efe3"
  signatureMagenta: "#ff5996"
  signatureOrange: "#ff6118"
  superNavy: "#061b31"
  footerBg: "#0a2540"
  docsBlue: "#5469d4"
  docsCanvas: "#f7fafc"
  codeInk: "#1a1f36"
  on-primary: "#ffffff"
  on-dark: "#ffffff"

typography:
  display: { fontFamily: "sohne-var, SF Pro Display, Helvetica Neue, Arial, sans-serif", fontSize: 92px, fontWeight: 400, lineHeight: 0.98, letterSpacing: "-0.04em" }
  hero: { fontFamily: "sohne-var, SF Pro Display, Helvetica Neue, Arial, sans-serif", fontSize: 68px, fontWeight: 400, lineHeight: 1.02, letterSpacing: "-0.035em" }
  headline-lg: { fontFamily: "sohne-var, SF Pro Display, Helvetica Neue, Arial, sans-serif", fontSize: 48px, fontWeight: 400, lineHeight: 1.08, letterSpacing: "-0.03em" }
  title-lg: { fontFamily: "sohne-var, SF Pro Display, Helvetica Neue, Arial, sans-serif", fontSize: 32px, fontWeight: 400, lineHeight: 1.25, letterSpacing: "-0.02em" }
  title-md: { fontFamily: "sohne-var, SF Pro Display, Helvetica Neue, Arial, sans-serif", fontSize: 24px, fontWeight: 400, lineHeight: 1.33, letterSpacing: "-0.01em" }
  title-sm: { fontFamily: "sohne-var, SF Pro Display, Helvetica Neue, Arial, sans-serif", fontSize: 18px, fontWeight: 500, lineHeight: 1.33, letterSpacing: "0em" }
  body: { fontFamily: "sohne-var, Helvetica Neue, Arial, sans-serif", fontSize: 17px, fontWeight: 300, lineHeight: 1.6, letterSpacing: "0.01em" }
  label: { fontFamily: "sohne-var, Helvetica Neue, Arial, sans-serif", fontSize: 13px, fontWeight: 500, lineHeight: 1.62, letterSpacing: "0.015em" }
  button: { fontFamily: "sohne-var, Helvetica Neue, Arial, sans-serif", fontSize: 15px, fontWeight: 500, lineHeight: 1.6, letterSpacing: "0.01em" }
  caption: { fontFamily: "sohne-var, Helvetica Neue, Arial, sans-serif", fontSize: 13px, fontWeight: 300, lineHeight: 1.62, letterSpacing: "0.015em" }
  legal: { fontFamily: "sohne-var, Helvetica Neue, Arial, sans-serif", fontSize: 12px, fontWeight: 300, lineHeight: 1.5, letterSpacing: "0.02em" }
  pricing-display: { fontFamily: "sohne-var, SF Pro Display, Helvetica Neue, Arial, sans-serif", fontSize: 44px, fontWeight: 500, lineHeight: 1.09, letterSpacing: "-0.02em" }
  code: { fontFamily: "SourceCodePro, SFMono-Regular, Consolas, monospace", fontSize: 13px, fontWeight: 500, lineHeight: 1.7, letterSpacing: "0em" }

rounded:
  sm: 4px
  md: 6px
  lg: 8px
  xl: 16px
  pill: 9999px

spacing:
  xs: 4px
  sm: 8px
  md: 16px
  lg: 24px
  xl: 48px
  section: 96px

components:
  button-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button}"
    rounded: "{rounded.pill}"
    padding: 6px 16px 7px
  button-primary-active:
    backgroundColor: "{colors.accentPressed}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.pill}"
  button-secondary:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.primary}"
    borderColor: "{colors.brandVioletSoft}"
    typography: "{typography.button}"
    rounded: "{rounded.pill}"
    padding: 6px 16px 7px
  button-dark:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    typography: "{typography.button}"
    rounded: "{rounded.pill}"
    padding: 6px 16px 7px
  button-link:
    backgroundColor: transparent
    textColor: "{colors.link}"
    typography: "{typography.button}"
    rounded: "{rounded.pill}"
    padding: 0px
  nav-bar:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.label}"
    height: 64px
  sticky-nav:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.ink}"
    borderColor: "{colors.border}"
    shadow: "0 15px 35px rgba(49,49,93,0.10), 0 5px 15px rgba(0,0,0,0.08)"
  hero-angled-panel:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    rounded: "{rounded.lg}"
    shadow: "0 20px 80px -16px rgba(0,55,112,0.14), 0 10px 60px -16px rgba(0,59,137,0.06)"
  bento-product-card:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.ink}"
    borderColor: "{colors.border}"
    rounded: "{rounded.lg}"
    padding: 24px
  pricing-card:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.ink}"
    borderColor: "{colors.border}"
    rounded: "{rounded.lg}"
    padding: 0px
  pricing-feature-row:
    backgroundColor: "{colors.surfaceAlt}"
    textColor: "{colors.body}"
    borderColor: "{colors.border}"
    padding: 16px 24px
  docs-code-panel:
    backgroundColor: "{colors.codeInk}"
    textColor: "{colors.on-dark}"
    typography: "{typography.code}"
    rounded: "{rounded.lg}"
    padding: 20px 24px
  payment-element-card:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.ink}"
    borderColor: "{colors.border}"
    rounded: "{rounded.lg}"
    padding: 0px
  input-payment:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    borderColor: "{colors.canvas}"
    typography: "{typography.caption}"
    rounded: "{rounded.md}"
    padding: 10px 12px
  segmented-control:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    selectedBackgroundColor: "{colors.accent}"
    selectedTextColor: "{colors.on-primary}"
    typography: "{typography.button}"
    rounded: "{rounded.pill}"
  statistic-tile:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.title-md}"
    padding: 24px 0px
  footer:
    backgroundColor: "{colors.footerBg}"
    textColor: "{colors.on-dark}"
    typography: "{typography.caption}"
    padding: 64px 0px
---

**Overview**
Stripe's public identity is a technical commerce system made approachable through disciplined typography, bright violet action color, and a constant presence of real product interfaces. The brand avoids fluffy SaaS decoration: pages feel engineered, fast, and global, with clear sections, compressed copy, data-heavy claims, and mockups of dashboards, checkout forms, pricing tables, code editors, cards, terminals, and payment elements.

The system has three visible modes. Marketing pages use large Sohne headlines, white or pale blue-gray canvases, slanted Stripe geometry, and vivid accent gradients. Product and pricing pages become more utilitarian, with bordered cards, dashed dividers, compact feature rows, and sticky navigation. Documentation shifts into a denser application mode through Sail tokens: smaller text, blue action color, code panels, side navigation, popovers, and precise focus rings.

Key Characteristics:
- Use {colors.ink} for authoritative headings, never pure black.
- Pair {colors.primary} and {colors.accent} with small pill buttons and inline links.
- Build hierarchy with product UI artifacts, not abstract illustration.
- Favor 1px borders, dashed dividers, and subtle elevation over heavy shadows.
- Use angled or cropped image geometry as a Stripe signature.
- Keep typography compact, lightly tracked in body text, and negatively tracked in hero sizes.
- Let dashboards, pricing grids, and code blocks provide the brand's technical texture.

**Colors**
Primary & Action

`primary` `{colors.primary}` is the core violet used for primary CTA fills in the newer marketing system. It carries sign-up, selected control, focus, and active product moments.

`accent` `{colors.accent}` is the recognizable Stripe violet seen in links, focus details, active navigation, and gradient stops. Use it when an element needs to read as Stripe-specific without becoming a full filled action.

`accentHover` `{colors.accentHover}` and `accentPressed` `{colors.accentPressed}` deepen the violet family for hover, pressed, and high-contrast selected states. They should be used sparingly because Stripe normally keeps interactions crisp rather than dramatic.

`link` `{colors.link}` is the standard marketing link color. Links often appear as text with a small arrow or chevron, so the color does not need underline treatment by default.

Surfaces

`canvas` `{colors.canvas}` is the pale blue-gray used behind product graphics, UI cards, and section bands. It is one of the most important non-action colors because it makes white cards feel technical instead of generic.

`surface` `{colors.surface}` is the base card, nav, pricing, and form surface. Stripe uses it for clean contrast against {colors.canvas} and for dense UI mockups.

`surfaceAlt` `{colors.surfaceAlt}` is a barely tinted row or subcard fill, especially useful inside pricing cards and product forms. Use it to divide rows without making the interface look heavy.

`footerBg` `{colors.footerBg}` anchors dark sections and end-of-page calls to action. It is also the base color for many dark CTAs.

Neutrals & Text

`ink` `{colors.ink}` is Stripe's deep navy headline and button color. It gives the brand its financial seriousness and should replace generic black in almost every marketing context.

`body` `{colors.body}` is the main paragraph color, softer than {colors.ink} but still readable. It is used for explanatory copy under strong headings.

`muted` `{colors.muted}` supports captions, microcopy, input placeholders, and secondary data. It should not carry critical text unless paired with larger type.

`border` `{colors.border}` is the quiet divider used around cards, payment modules, pricing rows, and input groups. `borderStrong` `{colors.borderStrong}` is reserved for docs-style table lines and stronger application keylines.

Semantic

`success` `{colors.success}` appears in dashboard-like status moments and positive product indicators. Keep it compact and data-like rather than celebratory.

`warning` `{colors.warning}` is the warm amber/brown from Stripe's system palette. Use it for warnings, pricing exceptions, and operational alerts.

`error` `{colors.error}` is a saturated red-pink that aligns with Stripe's broader palette. It belongs in validation, declined payment states, and risk surfaces.

Brand-specific signatures

`signaturePurple` `{colors.signaturePurple}` is the classic purple gradient stop often paired with violet and cyan. Use it in small accents, bars, or graphic modules.

`signatureCyan` `{colors.signatureCyan}` brings the high-energy infrastructure gradient seen in uptime and sticky progress indicators. It works best as a narrow stripe, glow, or data visualization color.

`signatureMagenta` `{colors.signatureMagenta}` and `signatureOrange` `{colors.signatureOrange}` appear in product graphics such as dispute charts and bento overlays. They should be secondary accents, not page-wide themes.

`superNavy` `{colors.superNavy}` is the darker technical surface used for code, popovers, and dramatic dark modules. It supports the developer-first side of the brand.

**Typography**
Stripe uses `sohne-var` for public marketing and UI copy, backed by Apple system display faces and Helvetica/Arial. Code and API examples use `SourceCodePro`, then SFMono/Consolas fallbacks. The docs system uses the same family direction but feels more application-like: smaller, denser, and more constrained.

| Level | Size | Weight | Line-height | Tracking | Use |
|---|---:|---:|---:|---:|---|
| display | 92px | 400 | 0.98 | -0.04em | Large campaign and data-led hero headlines |
| hero | 68px | 400 | 1.02 | -0.035em | Standard homepage and product hero headings |
| headline-lg | 48px | 400 | 1.08 | -0.03em | Major section headers |
| title-lg | 32px | 400 | 1.25 | -0.02em | Feature blocks and card group headings |
| title-md | 24px | 400 | 1.33 | -0.01em | Stats, subheads, and product panels |
| title-sm | 18px | 500 | 1.33 | 0em | Card titles and pricing product names |
| body | 17px | 300 | 1.6 | 0.01em | Marketing paragraphs and section descriptions |
| label | 13px | 500 | 1.62 | 0.015em | Nav, labels, badges, and metadata |
| button | 15px | 500 | 1.6 | 0.01em | CTAs, segmented controls, and inline action links |
| caption | 13px | 300 | 1.62 | 0.015em | Captions, form helper text, small table copy |
| legal | 12px | 300 | 1.5 | 0.02em | Footer, disclaimers, legal notes |
| pricing-display | 44px | 500 | 1.09 | -0.02em | Large price and numeric emphasis |
| code | 13px | 500 | 1.7 | 0em | API examples, snippets, and code editors |

Principles:
- Track large headlines tightly; Stripe's big type is confident and compact, not airy.
- Keep body copy light in weight but generous in line-height so dense claims remain readable.
- Use medium weight for controls and small labels because many UI modules are compact.
- Use tabular numerals for stats, pricing, and infrastructure metrics.
- Split code into {typography.code} immediately; developer content should look native, not styled as prose.

**Layout**
Stripe pages rely on wide responsive grids with a maximum content measure near 1080-1180px and column padding that increases at tablet and desktop breakpoints. Section padding is generous, often around {spacing.section}, while internal card spacing stays practical at {spacing.md} to {spacing.lg}. Product pages use sticky local navigation, horizontal scroll tracks on tablet, and dense grids that collapse to one column on mobile.

The whitespace philosophy is structured rather than luxurious. Stripe gives hero sections enough room for dramatic type and product graphics, then compresses secondary sections into bento cards, stats rows, pricing tables, and side-by-side modules. Empty space usually has a job: revealing a slanted image crop, separating a data module, or making a dense UI mockup legible.

Spacing scale:

| Token | Value | Role |
|---|---:|---|
| {spacing.xs} | 4px | Icon gaps, micro offsets, dashed row rhythm |
| {spacing.sm} | 8px | Text stacks, form field clusters, small card gaps |
| {spacing.md} | 16px | Button groups, mobile card padding, nav gaps |
| {spacing.lg} | 24px | Standard card padding and pricing row padding |
| {spacing.xl} | 48px | Feature grid gaps, card group rhythm |
| {spacing.section} | 96px | Section vertical padding on desktop |

**Elevation & Depth**
Stripe's depth is layered but controlled. Cards often use a 1px {colors.border} keyline with light shadows such as `0 15px 35px rgba(49,49,93,0.10), 0 5px 15px rgba(0,0,0,0.08)`. Larger hero panels use broader blue-tinted shadows that feel infrastructural rather than glossy.

Hierarchy is frequently created through contrast, borders, angled shapes, and product UI composition instead of shadow alone. Pricing cards and payment forms can be nearly flat; bento modules and floating UI screenshots receive more elevation when they need to read as artifacts above the canvas.

**Components**
Buttons

`button-primary` is a compact pill CTA using {colors.primary} with white text. It should feel efficient, with horizontal padding just large enough for a label and arrow.

`button-primary-active` darkens the violet for pressed and selected states. Keep it as a sibling token so interactions do not require nested state definitions.

`button-secondary` is a low-emphasis action for white surfaces, often paired with a primary CTA. It keeps the Stripe violet as text or border rather than filling the whole button.

`button-dark` uses {colors.ink} for CTAs inside light marketing contexts. This is common when the page already has enough violet or when the action needs sober contrast.

`button-link` is the common text CTA style. Pair it with a small arrow and use hover opacity rather than underline-heavy treatment.

Cards & Containers

`hero-angled-panel` represents Stripe's signature product showcase: elevated, pale, and often cropped or skewed by the surrounding composition. Use it for dashboard screenshots, payment flows, and global commerce graphics.

`bento-product-card` is a modular marketing card with product copy and an embedded UI or animated graphic. It should have tight copy, a real product pattern, and a hover that feels like revealing machinery.

`pricing-card` is a bordered container with sectioned rows and no decorative excess. It uses {colors.border}, {colors.surface}, and occasional dashed dividers to make pricing feel exact.

`pricing-feature-row` is the internal pricing row: pale surface, compact text, and strict separation. It should support comparison and scanning before brand expression.

`docs-code-panel` is the developer surface: dark ink background, monospaced code, and restrained syntax accents. Use it whenever the design needs Stripe's API-first credibility.

Inputs & Forms

`payment-element-card` is the branded checkout module. It uses a white card, {colors.border}, 8px radius, stacked payment rows, and compact form fields.

`input-payment` is a filled pale input with small type and minimal border contrast. Stripe inputs often feel embedded in a payment object rather than like isolated form controls.

`segmented-control` is a pill-based mode switch. Active states use {colors.accent} and white text; inactive states rely on opacity and clean typography.

Navigation

`nav-bar` is transparent over the hero and uses compact labels. It should be visually quiet so the hero and product graphic carry the first impression.

`sticky-nav` appears on product pages and documentation-like flows. It uses white surface, subtle shadow, and sometimes a thin multi-color progress stripe to show page position.

Pricing

`pricing-card` and `pricing-feature-row` should be used together. The visual logic is a spreadsheet softened into a card: exact rows, clear product names, tight metadata, and CTAs that do not overpower numbers.

Signature Components

`statistic-tile` is a data-first block for metrics like volume, uptime, currencies, and subscriptions. Use tabular numerals, {colors.ink}, and minimal framing.

`footer` is a dense link and CTA area. It can use {colors.footerBg} for dark endings or light canvas for directory-like footer navigation, depending on page mode.

**Do's and Don'ts**
Do:
- Use {colors.ink} for primary headings and CTAs when violet would feel too promotional.
- Place {colors.primary} on compact pill buttons, selected segments, and focused action states.
- Build product sections around UI artifacts: checkout cards, pricing grids, code editors, stats, and dashboards.
- Use {colors.canvas} behind white cards to create Stripe's pale technical atmosphere.
- Use 1px {colors.border} and dashed dividers inside pricing and feature rows.
- Apply {typography.code} to every API snippet or terminal-like panel.
- Crop imagery into angled or Stripe-logo-like geometry when using customer stories or hero visuals.
- Keep shadows blue-tinted and subtle; reserve large elevation for floating product panels.

Don't:
- Do not replace {colors.ink} with pure black; it loses Stripe's navy financial tone.
- Do not make page-wide purple gradients; Stripe uses gradients as narrow accents or graphic energy.
- Do not use oversized rounded cards beyond {rounded.lg} unless the element is a pill control.
- Do not decorate with abstract blobs when a real product UI module could explain the feature.
- Do not center all content in generic SaaS hero layouts; pair copy with product evidence.
- Do not use heavy box shadows on pricing cards; use {colors.border} and row structure.
- Do not loosen headline tracking; keep hero text tight with {typography.hero} or {typography.display}.
- Do not turn documentation screens into marketing pages; keep code, side nav, and dense hierarchy visible.

**Responsive Behavior**
Breakpoints:

| Name | Width | Behavior |
|---|---:|---|
| compact | 0px | Single column, compressed hero type, mobile nav, full-width CTAs |
| phone-wide | 500px | Payment cards and CTAs gain more horizontal breathing room |
| tablet | 600px | Two-column pricing rows begin; sticky nav becomes horizontal scroll |
| content | 640px | Marketing grid spans expand from 4 to 8 columns |
| desktop | 900px | Product pages switch to multi-column layouts and persistent nav affordances |
| wide | 1112px | Complex graphics, compliance cards, and dashboard mockups reach full composition |

Touch targets should be at least 44px for primary mobile actions, even when the visual button remains a compact pill. Smaller desktop controls can be 32-36px high if they are not primary touch targets.

Collapsing strategy:
- Collapse bento and pricing grids to one column before reducing internal type below readable sizes.
- Convert sticky nav into horizontal scroll with masked edges at tablet widths.
- Hide secondary enterprise/product metadata when it competes with the main card content.
- Keep payment forms proportional; stack fields before shrinking labels or placeholders.
- Preserve product screenshots and code panels as recognizable artifacts, even if cropped.

Image behavior:

Use real product, customer, or interface imagery whenever possible. Crop images with strong geometry, including slanted frames and parallelogram-like compositions, but avoid dark blurry stock treatments. Product graphics may overflow their containers on desktop and become clipped previews on mobile.

**Iteration Guide**
1. Check that primary actions use {colors.primary} or {colors.ink}, with white text and pill radius from {rounded.pill}.
2. Confirm headings use {typography.hero} or smaller tight-tracked levels; no loose tracking on large type.
3. Inspect every major section for a real Stripe-like artifact: pricing row, payment form, dashboard, code panel, stat, or terminal device.
4. Verify that cards use {rounded.lg}, {colors.border}, and restrained shadows rather than generic floating-card styling.
5. Look for {colors.canvas} behind white UI modules; pure white pages without pale structure feel under-specified.
6. Audit pricing modules for dashed or fine dividers, compact row copy, and exact numeric alignment.
7. Ensure docs or developer sections use {typography.code}, dark panels, and application-like density.
8. On mobile, test that sticky navigation, CTAs, and payment modules remain usable without shrinking below 44px touch targets.

**Known Gaps**
Observed directly: homepage structure, Payments product page structure, Pricing page modules, docs CSS, public font-face declarations, Sail color tokens, HDS action tokens, card borders, payment element styling, segmented controls, sticky nav behavior, and pricing card rows were fetched from Stripe pages and stylesheets on 2026-05-18.

Research pages inspected:

| Page | URL | Strongest evidence gathered |
|---|---|---|
| Homepage | `https://stripe.com/` | Hero hierarchy, global commerce positioning, bento product rhythm, stats, customer story imagery, footer structure |
| Product | `https://stripe.com/payments` | Payment Element card, sticky nav, segmented controls, code editor, uptime gradient, compliance and checkout modules |
| Pricing | `https://stripe.com/pricing` | Product cards, pricing rows, badges, dashed dividers, feature groups, enterprise package cards |
| Docs | `https://docs.stripe.com/` | Sail palette, docs typography, code surfaces, popover shadows, pressable controls, focus rings |

Confidence by category:

| Category | Confidence | Notes |
|---|---|---|
| Colors | High | Public CSS exposed canonical Sail and HDS colors plus repeated marketing hex values |
| Typography families | High | `sohne-var` and `SourceCodePro` font-face declarations were observed directly |
| Typography scale | Medium | Exact values vary responsively, so tokens capture representative desktop anchors |
| Spacing | Medium | Component padding is directly observed; section-level rhythm is normalized from multiple pages |
| Radius | High | 4px, 6px, 8px, 16.5px, and pill controls recur across CSS |
| Elevation | High | HDS and Sail shadows are visible in CSS and reused in docs/product surfaces |
| Product patterns | High | Payment, pricing, docs, sticky nav, and code editor modules were all present in fetched assets |

Evidence boundaries:

- Treat {colors.primary} as the modern HDS action fill and {colors.accent} as the familiar Stripe marketing violet.
- Treat {colors.docsBlue} as docs/application-specific, not as the main public CTA color.
- Treat {colors.signatureCyan}, {colors.signaturePurple}, {colors.signatureMagenta}, and {colors.signatureOrange} as accents for graphics and charts.
- Treat {rounded.pill} as mandatory for compact CTAs but not for cards.
- Treat {typography.display} as a large-screen anchor; responsive implementations should step down quickly on mobile.

Derived: several type sizes are normalized into practical design tokens from observed CSS patterns and visible hierarchy rather than copied from one global token table. Marketing pages use responsive fluid typography, so fixed pixel values here are representative anchors for AI generation rather than exact values at every viewport.

Uncertain: some homepage modules are generated from minified CSS and region-specific content, so a few page-level spacing values and exact max widths are approximated. Stripe also evolves visual campaigns frequently; the core tokens here emphasize stable brand behavior across marketing, product, pricing, and docs rather than a single hero treatment.
