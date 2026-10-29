---
version: alpha
name: Mailchimp
slug: mailchimp
source: https://mailchimp.com/
extractedAt: 2026-05-17
description: "Warm editorial marketing system with Cavendish Yellow action surfaces, Peppercorn ink, Means Web headlines, Graphik UI, tactile pill CTAs, and flat pricing/product tables."

colors:
  primary: "#FFE01B"
  accent: "#007C89"
  accentHover: "#004E56"
  accentPressed: "#001D28"
  ink: "#231E15"
  body: "#403B3B"
  muted: "#575757"
  canvas: "#FFFFFF"
  surface: "#FFFFFF"
  surfaceAlt: "#F5F5F5"
  border: "#DBD9D2"
  borderStrong: "#BCBAB8"
  link: "#231E15"
  success: "#00C350"
  warning: "#E7B75F"
  error: "#A73205"
  focus: "#4BC4C2"
  peppercorn: "#231E15"
  oyster: "#39352C"
  kale: "#007C89"
  kaleCharred: "#001D28"
  cavendish: "#FFE01B"
  coconut: "#FFFFFF"
  jasmine: "#F5F5F5"
  cornflower: "#D2EBFF"
  cucumber: "#EDFFCC"
  radish: "#FFCCD8"
  yam: "#FFDBCC"
  squash: "#EBE1CD"
  plum: "#B42855"
  plumInk: "#692340"
  plumCream: "#FBEECA"
  on-primary: "#231E15"
  on-dark: "#FFFFFF"

typography:
  display:
    fontFamily: "Means Web, Georgia, Times, Times New Roman, serif"
    fontSize: 64px
    fontWeight: 400
    lineHeight: 1.13
    letterSpacing: "-0.0625rem"
  hero:
    fontFamily: "Means Web, Georgia, Times, Times New Roman, serif"
    fontSize: 64px
    fontWeight: 400
    lineHeight: 1.20
    letterSpacing: "-0.075rem"
  headline-lg:
    fontFamily: "Means Web, Georgia, Times, Times New Roman, serif"
    fontSize: 48px
    fontWeight: 400
    lineHeight: 1.00
    letterSpacing: "-0.0625rem"
  title-lg:
    fontFamily: "Means Web, Georgia, Times, Times New Roman, serif"
    fontSize: 40px
    fontWeight: 400
    lineHeight: 1.20
    letterSpacing: "-0.03125rem"
  title-md:
    fontFamily: "Means Web, Georgia, Times, Times New Roman, serif"
    fontSize: 32px
    fontWeight: 400
    lineHeight: 1.25
    letterSpacing: "0"
  title-sm:
    fontFamily: "Graphik Web, Helvetica Neue, Helvetica, Arial, Verdana, sans-serif"
    fontSize: 24px
    fontWeight: 400
    lineHeight: 1.33
    letterSpacing: "-0.02rem"
  body:
    fontFamily: "Graphik Web, Helvetica Neue, Helvetica, Arial, Verdana, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.75
    letterSpacing: "0"
  label:
    fontFamily: "Graphik Web, Helvetica Neue, Helvetica, Arial, Verdana, sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: "0"
  button:
    fontFamily: "Graphik Web, Helvetica Neue, Helvetica, Arial, Verdana, sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.50
    letterSpacing: "0"
  caption:
    fontFamily: "Graphik Web, Helvetica Neue, Helvetica, Arial, Verdana, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.50
    letterSpacing: "0"
  legal:
    fontFamily: "Graphik Web, Helvetica Neue, Helvetica, Arial, Verdana, sans-serif"
    fontSize: 11px
    fontWeight: 400
    lineHeight: 1.45
    letterSpacing: "0"
  pricing-display:
    fontFamily: "Means Web, Georgia, Times, Times New Roman, serif"
    fontSize: 52px
    fontWeight: 400
    lineHeight: 1.00
    letterSpacing: "-0.0625rem"

rounded:
  sm: 4px
  md: 8px
  lg: 16px
  image: 26px
  pill: 9999px

spacing:
  xs: 4px
  sm: 8px
  md: 16px
  lg: 24px
  xl: 40px
  xxl: 64px
  section: 80px

components:
  button-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button}"
    rounded: "{rounded.pill}"
    padding: 12px 24px
    border: "1px solid {colors.ink}"
    shadow: "0 0 0 1px {colors.ink}"
  button-primary-raised:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.pill}"
    transform: "translateY(-6px)"
    shadow: "0 0 0 1px {colors.ink}, 0 6px 0 0 {colors.ink}"
  button-secondary:
    backgroundColor: "transparent"
    textColor: "{colors.ink}"
    typography: "{typography.button}"
    rounded: "{rounded.pill}"
    padding: 12px 24px
    border: "1px solid {colors.ink}"
  button-secondary-on-dark:
    backgroundColor: "transparent"
    textColor: "{colors.on-dark}"
    typography: "{typography.button}"
    rounded: "{rounded.pill}"
    padding: 12px 24px
    border: "1px solid {colors.on-dark}"
  button-arrow:
    backgroundColor: "transparent"
    textColor: "{colors.ink}"
    typography: "{typography.body}"
    rounded: "{rounded.pill}"
    padding: 0px 40px 0px 0px
    indicatorBackground: "{colors.primary}"
  nav-global:
    backgroundColor: "transparent"
    textColor: "{colors.ink}"
    typography: "{typography.label}"
    height: 68px
    padding: 12px 16px
  nav-item:
    backgroundColor: "transparent"
    textColor: "{colors.ink}"
    typography: "{typography.label}"
    rounded: "{rounded.sm}"
    padding: 8px
  section-band:
    backgroundColor: "{colors.coconut}"
    textColor: "{colors.ink}"
    padding: 80px 0px
  section-band-alt:
    backgroundColor: "{colors.jasmine}"
    textColor: "{colors.ink}"
    padding: 64px 0px
  section-band-dark:
    backgroundColor: "{colors.peppercorn}"
    textColor: "{colors.on-dark}"
    padding: 80px 0px
  card-flat:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.ink}"
    border: "1px solid {colors.borderStrong}"
    rounded: "{rounded.md}"
    padding: 8px
    shadow: "none"
  card-editorial:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.ink}"
    rounded: "{rounded.image}"
    padding: 32px
    shadow: "none"
  pricing-table:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.ink}"
    border: "1px solid {colors.borderStrong}"
    rounded: 0px
    padding: 48px 16px 24px
  input-rule:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.ink}"
    typography: "{typography.body}"
    rounded: 0px
    border: "0 0 1px 0 solid {colors.ink}"
    padding: 20px 0px
  badge:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    typography: "{typography.caption}"
    rounded: "{rounded.pill}"
    padding: 1px 7px
  accordion-row:
    backgroundColor: "transparent"
    textColor: "{colors.ink}"
    typography: "{typography.title-sm}"
    rounded: 0px
    padding: 24px 0px
  assistant-toolbar:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.ink}"
    rounded: "{rounded.pill}"
    border: "1px solid rgba(35,30,21,0.5)"
    padding: 11px
  highlight-emphasis:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
    padding: 0.06em 0.18em
  focus-ring:
    outlineColor: "{colors.focus}"
    outlineWidth: 2px
    outlineOffset: 3px
---

**Overview**
Mailchimp's public design language is warm, editorial, and commercially practical. It is recognizable through Cavendish Yellow actions, Peppercorn ink, large Means Web headlines, compact Graphik UI, flat comparison tables, and tactile pill CTAs that lift on hover.

The site has three visual modes. Marketing pages use magazine-like scale, dark bands, rounded media, and yellow emphasis. Utility flows such as pricing, forms, nav, and accordions use Graphik, borders, and squared controls. Brand-expression moments use yellow arrows, underlines, badges, and friendly image or illustration rhythms rather than generic SaaS gradients.

Key Characteristics:
- Use {colors.primary} as action/highlight punctuation, not a blanket background.
- Preserve the Means Web and Graphik Web split.
- Build hierarchy with type, bands, borders, and yellow emphasis before shadow.
- Use {components.button-primary-raised} for the distinctive CTA lift.
- Keep pricing and forms practical with {components.pricing-table} and {components.input-rule}.
- Use {colors.peppercorn}, {colors.oyster}, or {colors.kaleCharred} for dark branded sections.
- Prefer rounded media at {rounded.image}, not rounded page-section cards.

Research Sources:
- Homepage: https://mailchimp.com/
- Feature page: https://mailchimp.com/features/marketing-automation/
- Pricing page: https://mailchimp.com/pricing/marketing/
- Content page: https://mailchimp.com/resources/
- Brand assets: https://mailchimp.com/about/brand-assets/

**Colors**
Primary & Action:
- {colors.primary} `#FFE01B`: Cavendish Yellow, used for primary CTAs, arrow capsules, headline highlights, pricing indicators, carousel pills, selected states, and checks.
- {colors.accent} `#007C89`: Kale teal, a secondary action/support accent seen in tags and alternate themed flows.
- {colors.accentHover} `#004E56` and {colors.accentPressed} `#001D28`: deeper teal states for hover, pressed, and dark utility moments.
- {colors.link} `#231E15`: links usually remain Peppercorn and signal hover through yellow highlight backgrounds.
- {colors.focus} `#4BC4C2`: focus-ring cyan-teal, distinct from both yellow and dark bands.

Surfaces:
- {colors.canvas} `#FFFFFF` and {colors.surface} `#FFFFFF`: default page and card surfaces.
- {colors.surfaceAlt} `#F5F5F5` and {colors.jasmine} `#F5F5F5`: quiet alternate bands, trial blocks, and low-pressure modules.
- {colors.coconut} `#FFFFFF`: named white brand surface.
- {colors.squash} `#EBE1CD`: warm beige support surface and disabled pricing overlay.
- {colors.cornflower} `#D2EBFF`, {colors.cucumber} `#EDFFCC`, {colors.radish} `#FFCCD8`, and {colors.yam} `#FFDBCC`: pale produce surfaces for content variation.

Neutrals & Text:
- {colors.ink} `#231E15`: Peppercorn, the main text, stroke, link, and CTA-depth color.
- {colors.body} `#403B3B`: softened long-form text.
- {colors.muted} `#575757`: secondary labels and metadata.
- {colors.border} `#DBD9D2`: soft warm divider and disabled fill.
- {colors.borderStrong} `#BCBAB8`: pricing-grid and card border.
- {colors.on-primary} `#231E15`: required text color on yellow CTAs.
- {colors.on-dark} `#FFFFFF`: text on dark Peppercorn, Oyster, Plum, or Charred Kale bands.

Semantic & Signatures:
- {colors.success} `#00C350`: Apple green, reserved for true success status.
- {colors.warning} `#E7B75F`: golden badge/warning emphasis.
- {colors.error} `#A73205`: validation text and error borders.
- {colors.peppercorn} `#231E15`: core dark brand field.
- {colors.oyster} `#39352C`: dark olive-brown alternate section.
- {colors.plum} `#B42855`, {colors.plumInk} `#692340`, and {colors.plumCream} `#FBEECA`: plum-themed campaign palette.

Color Principles:
- Prefer {colors.ink} over pure black for brand UI.
- Keep {colors.primary} dominant in action and emphasis, not general decoration.
- Use dark bands with {colors.on-dark} and yellow punctuation.
- Use pale produce surfaces sparingly to avoid a pastel collage.

**Typography**
Mailchimp's strongest identity move is type contrast: Means Web carries editorial voice; Graphik Web handles product clarity. Public CSS loads Means Web at 300-500 and Graphik Web at 300-600.

| Token | Family | Size | Weight | Line Height | Letter Spacing | Use |
|---|---|---:|---:|---:|---:|---|
| {typography.display} | Means Web | 64px | 400 | 1.13 | -0.0625rem | Display/stat moments |
| {typography.hero} | Means Web | 64px | 400 | 1.20 | -0.075rem | Homepage hero |
| {typography.headline-lg} | Means Web | 48px | 400 | 1.00 | -0.0625rem | Major sections |
| {typography.title-lg} | Means Web | 40px | 400 | 1.20 | -0.03125rem | Feature headings |
| {typography.title-md} | Means Web | 32px | 400 | 1.25 | 0 | Quotes/subheads |
| {typography.title-sm} | Graphik Web | 24px | 400 | 1.33 | -0.02rem | Accordions/UI headings |
| {typography.body} | Graphik Web | 16px | 400 | 1.75 | 0 | Paragraphs/cards |
| {typography.label} | Graphik Web | 13px | 500 | 1.25 | 0 | Nav/compact labels |
| {typography.button} | Graphik Web | 13px | 500 | 1.50 | 0 | CTAs/selectors |
| {typography.caption} | Graphik Web | 13px | 400 | 1.50 | 0 | Metadata/captions |
| {typography.legal} | Graphik Web | 11px | 400 | 1.45 | 0 | Legal/footer |
| {typography.pricing-display} | Means Web | 52px | 400 | 1.00 | -0.0625rem | Prices |

Principles:
- Keep Means Web at 400; scale and tracking create emphasis.
- Use negative tracking only on large editorial text.
- Use Graphik for scan-heavy UI, navigation, forms, CTAs, and body.
- Let Graphik paragraphs breathe with {typography.body}; avoid cramped SaaS copy.
- Do not substitute Inter/system-ui when brand fidelity matters.

**Layout**
Spacing:
- {spacing.xs}: micro offsets, icon gaps, badge insets.
- {spacing.sm}: nav padding and card gutters.
- {spacing.md}: mobile margins and form grouping.
- {spacing.lg}: headline-to-copy spacing.
- {spacing.xl}: CTA groups and pricing action spacing.
- {spacing.xxl}: medium module padding.
- {spacing.section}: major homepage/product bands.

Layout Behavior:
- Use full-width bands such as {components.section-band}, {components.section-band-alt}, and {components.section-band-dark}.
- Keep inner content near a 1200px max-width on desktop.
- Use two-column editorial splits for product pages and table-like grids for pricing.
- Collapse to one column on mobile with {spacing.md} page margins.
- Preserve left alignment in utility flows, even when marketing modules are centered.

Whitespace Philosophy:
Mailchimp alternates generous editorial breathing room with dense utility modules. Sections may be tall, but CTAs, nav, pricing cells, and forms stay compact and deliberate. Avoid floating cards as page sections; use bands, grids, borders, and rounded media.

**Elevation & Depth**
Mailchimp is mostly flat. Hierarchy comes from type scale, background bands, borders, yellow emphasis, and tactile CTA motion.

Observed Depth:
- {components.button-primary}: 1px Peppercorn outline shadow.
- {components.button-primary-raised}: 6px Peppercorn bottom ledge on hover-like lifted states.
- {components.card-flat} and {components.pricing-table}: no shadow; rely on borders.
- Badges and assistant overlays may use minor shadows, but they are exceptions.

Depth Rules:
- Use button bottom-depth only on primary/secondary CTAs.
- Do not add generic soft shadows to pricing cards, feature cards, or sections.
- Do not use glass, bokeh, or decorative gradients.
- Use {rounded.image} media and {components.highlight-emphasis} instead of atmospheric depth.

**Components**
Buttons:
- {components.button-primary} is the default yellow pill action with dark text and Peppercorn outline. Use {components.button-primary-raised} for hover/lift behavior.
- {components.button-secondary} and {components.button-secondary-on-dark} are outline pills for secondary actions. They should not become grey filled buttons.
- {components.button-arrow} is the editorial text CTA with a yellow arrow capsule; use it below feature copy and content links.

Cards & Containers:
- {components.card-flat} covers pricing selectors, compact plan cards, and utility cards: white fill, 8px radius, strong border, no shadow.
- {components.card-editorial} covers larger image/content blocks with {rounded.image}; use sparingly and avoid nesting.
- {components.section-band}, {components.section-band-alt}, and {components.section-band-dark} are the primary page containers.
- {components.highlight-emphasis} is the yellow headline span or underline-like emphasis.

Inputs & Forms:
- {components.input-rule} is the core form/control model: square corners, practical padding, and rule-based borders.
- Error states use {colors.error}; focus states use {components.focus-ring}.
- Currency, language, and contact-count selects stay compact and utility-oriented, not decorative.

Navigation:
- {components.nav-global} is compact, transparent, 68px tall, and Graphik-led.
- {components.nav-item} is a small transparent text control with slight radius; only CTAs become pills.
- Mobile collapses to a menu button while keeping the trial CTA visible when space allows.

Pricing:
- {components.pricing-table} is the dominant pricing pattern: square cells, clear borders, dense comparison rows.
- Price figures use {typography.pricing-display}; free labels use yellow underline emphasis.
- Recommendations use yellow dots, check circles, progress bars, and selected pills without turning the grid into marketing cards.

Signature Components:
- {components.badge} covers small dark status pills; square warning badges may use {colors.warning}.
- {components.accordion-row} pairs large Graphik labels with yellow circular plus icons.
- {components.assistant-toolbar} is a rounded white product-assistant/search field with translucent Peppercorn border.
- Rounded image modules and yellow arrow CTAs are the recurring marketing/product bridge.

**Do's and Don'ts**
Do:
- Use {colors.primary} for CTAs, arrows, selected pills, and headline emphasis.
- Pair Means headlines with Graphik UI/body text.
- Use {components.button-primary-raised} for primary CTA hover behavior.
- Use {colors.peppercorn} for dark bands and CTA depth.
- Use {components.pricing-table} for plan comparison.
- Use {components.input-rule} for forms and selectors.
- Use {rounded.image} for marketing media.
- Use {colors.borderStrong} for pricing and card separation.

Don't:
- Do not use white text on {components.button-primary}.
- Do not replace Cavendish Yellow with orange or generic gold.
- Do not add soft SaaS shadows to {components.card-flat} or {components.pricing-table}.
- Do not round forms into pill inputs.
- Do not bold Means Web headlines.
- Do not make every module a card.
- Do not use blue as the primary action color; teal is secondary.
- Do not add gradients, glass, bokeh, or decorative blobs.

**Responsive Behavior**
Breakpoints:

| Name | Width | Behavior |
|---|---:|---|
| mobile-sm | 0px | Single column, compact nav, 16px margins |
| mobile-lg | 576px | Type begins stepping up; cards stack |
| tablet | 600px | CTA groups can align; modals gain full radius |
| desktop-sm | 992px | Feature grids and pricing tables expand |
| desktop-md | 1200px | Wide editorial sections stabilize |
| desktop-lg | 1422px | Display sizes cap; bands feel spacious |

Touch Targets:
- Nav CTAs should be at least 44px tall.
- Dense utility buttons can be 35px only in constrained pricing/consent contexts.
- Round icon controls should be visually 40px with a 44px target.
- Accordion rows should keep generous vertical rhythm.

Collapsing Strategy:
- Collapse desktop nav into menu controls.
- Stack editorial two-column sections into one column.
- Preserve table borders when pricing turns into cards or scroll regions.
- Keep CTAs attached to their text block.
- Reduce {spacing.section} to {spacing.xl} or {spacing.xxl} on smaller screens.

Image Behavior:
- Preserve {rounded.image} on desktop marketing images.
- On mobile mosaics, round only the exposed top/bottom image corners as needed.
- Avoid decorative shadows and aggressive crops.
- Keep screenshots and illustrations crisp against white, Jasmine, or Peppercorn bands.

**Iteration Guide**
1. Confirm the first viewport has Means headline scale or a clear utility module plus a {colors.primary} action.
2. Check every primary CTA against {components.button-primary} and lifted states against {components.button-primary-raised}.
3. Verify the Means/Graphik split across headings, body, nav, pricing, and forms.
4. Ensure page structure uses bands, not nested cards.
5. Check pricing against {components.pricing-table}: borders, square cells, and Means price figures.
6. Check forms against {components.input-rule}: square, rule-based, focused with {components.focus-ring}.
7. Confirm dark sections use {colors.on-dark} and avoid low-contrast muted text.
8. Verify {colors.primary} appears as punctuation, not uncontrolled page fill.
9. Remove generic gradients, glass, blue CTAs, and soft card shadows.
10. Test mobile stacking so CTAs remain near their copy and image corners remain intentional.

**Known Gaps**
Observed directly:
- Homepage, feature page, pricing page, resources page, and brand assets page were researched.
- CSS exposed Means Web, Graphik Web, Cavendish/Peppercorn palette classes, CTA motion, focus rings, forms, pricing selectors, badges, and assistant-toolbar selectors.
- Pricing table/card behavior, nav CTAs, dark feature bands, accordions, and hero typography were sampled from live pages.

Derived conservatively:
- Semantic status colors use observed palette/form values, not a complete logged-in product token table.
- Component names are normalized DESIGN.md names, not internal Mailchimp class names.
- Max-width guidance is inferred from observed desktop layouts around 1200px.
- Assistant-toolbar behavior is based on public CSS, not an authenticated product session.

Uncertain:
- Logged-in product UI details, complete motion timings, and all A/B tested modules were not exhaustively accessible.
- Localized redirects may change text wrapping compared with US English pages.
- Some palette classes were visible in CSS but not dominant in sampled pages.
- Recheck the live site for pixel-critical work because Mailchimp changes commercial pages often.
