---
version: alpha
name: OpenAI
slug: openai
source: https://openai.com/
extractedAt: 2026-05-19
description: "Dark, editorial AI brand system with OpenAI Sans, image-first modular news cards, quiet pill actions, flat translucent surfaces, and precise negative-tracked typography."

colors:
  primary: "#ffffff"
  accent: "#f9f9f9"
  accentHover: "#ececec"
  accentPressed: "#dcdcdc"
  ink: "#ffffff"
  body: "#dcdcdc"
  muted: "#b9b9b9"
  canvas: "#000000"
  surface: "#212121"
  surfaceAlt: "#303030"
  border: "#ffffff1f"
  borderStrong: "#ffffff26"
  link: "#8ad1fd"
  success: "#10a37f"
  warning: "#f5a524"
  error: "#ef4444"
  translucentAction: "#ffffff1f"
  translucentActionHover: "#ffffff29"
  textFaint: "#ffffff99"
  docsCanvas: "#131313"
  chatgptInk: "#0d0d0d"
  ruleDark: "#ffffff0d"
  on-primary: "#000000"
  on-dark: "#ffffff"

typography:
  display: { fontFamily: "OpenAI Sans, Arial, Helvetica, sans-serif", fontSize: 59px, fontWeight: 500, lineHeight: 1.01, letterSpacing: "-0.03em" }
  hero: { fontFamily: "OpenAI Sans, Arial, Helvetica, sans-serif", fontSize: 60px, fontWeight: 500, lineHeight: 1.00, letterSpacing: "-0.03em" }
  headline-lg: { fontFamily: "OpenAI Sans, Arial, Helvetica, sans-serif", fontSize: 46px, fontWeight: 500, lineHeight: 1.16, letterSpacing: "-0.029em" }
  title-lg: { fontFamily: "OpenAI Sans, Arial, Helvetica, sans-serif", fontSize: 30px, fontWeight: 600, lineHeight: 1.40, letterSpacing: "-0.02em" }
  title-md: { fontFamily: "OpenAI Sans, Arial, Helvetica, sans-serif", fontSize: 22px, fontWeight: 500, lineHeight: 1.25, letterSpacing: "-0.01em" }
  title-sm: { fontFamily: "OpenAI Sans, Arial, Helvetica, sans-serif", fontSize: 18px, fontWeight: 600, lineHeight: 1.35, letterSpacing: "-0.01em" }
  body: { fontFamily: "OpenAI Sans, Arial, Helvetica, sans-serif", fontSize: 17px, fontWeight: 400, lineHeight: 1.65, letterSpacing: "-0.01em" }
  body-sm: { fontFamily: "OpenAI Sans, Arial, Helvetica, sans-serif", fontSize: 14px, fontWeight: 400, lineHeight: 1.64, letterSpacing: "-0.01em" }
  label: { fontFamily: "OpenAI Sans, Arial, Helvetica, sans-serif", fontSize: 14px, fontWeight: 500, lineHeight: 1.00, letterSpacing: "0em" }
  button: { fontFamily: "OpenAI Sans, Arial, Helvetica, sans-serif", fontSize: 14px, fontWeight: 500, lineHeight: 1.43, letterSpacing: "0em" }
  caption: { fontFamily: "OpenAI Sans, Arial, Helvetica, sans-serif", fontSize: 13px, fontWeight: 500, lineHeight: 1.00, letterSpacing: "0em" }
  legal: { fontFamily: "OpenAI Sans, Arial, Helvetica, sans-serif", fontSize: 12px, fontWeight: 400, lineHeight: 1.50, letterSpacing: "0em" }
  code: { fontFamily: "ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, monospace", fontSize: 14px, fontWeight: 400, lineHeight: 1.55, letterSpacing: "0em" }

rounded:
  sm: 6px
  md: 8px
  lg: 10px
  xl: 16px
  pill: 9999px

spacing:
  xs: 8px
  sm: 16px
  md: 24px
  lg: 40px
  xl: 64px
  section: 96px

components:
  button-primary: { backgroundColor: "{colors.primary}", textColor: "{colors.on-primary}", typography: "{typography.button}", rounded: "{rounded.pill}", padding: 0px 20px, minHeight: 36px }
  button-primary-active: { backgroundColor: "{colors.accentPressed}", textColor: "{colors.on-primary}", rounded: "{rounded.pill}" }
  button-secondary: { backgroundColor: "{colors.translucentAction}", textColor: "{colors.on-dark}", typography: "{typography.caption}", rounded: "{rounded.pill}", padding: 8px 16px }
  button-secondary-hover: { backgroundColor: "{colors.translucentActionHover}", textColor: "{colors.on-dark}", rounded: "{rounded.pill}" }
  button-outline-dark: { backgroundColor: "{colors.canvas}", textColor: "{colors.on-dark}", borderColor: "{colors.borderStrong}", typography: "{typography.button}", rounded: "{rounded.pill}", padding: 0px 12px, minHeight: 36px }
  button-ghost: { backgroundColor: transparent, textColor: "{colors.ink}", typography: "{typography.body}", rounded: 0px, padding: 0px }
  button-icon: { backgroundColor: transparent, textColor: "{colors.textFaint}", rounded: "{rounded.pill}", width: 40px, height: 40px }
  nav-global: { backgroundColor: transparent, textColor: "{colors.ink}", typography: "{typography.body}", height: 64px }
  card-media-news: { backgroundColor: transparent, textColor: "{colors.ink}", rounded: "{rounded.sm}", mediaAspectRatio: "1 / 1", gap: "{spacing.sm}" }
  card-cta-translucent: { backgroundColor: "{colors.translucentAction}", textColor: "{colors.ink}", rounded: "{rounded.sm}", padding: "{spacing.xs}", borderColor: transparent }
  card-docs: { backgroundColor: "{colors.surface}", textColor: "{colors.body}", rounded: "{rounded.lg}", padding: 20px, borderColor: "{colors.border}" }
  pricing-plan-card: { backgroundColor: transparent, textColor: "{colors.ink}", rounded: 0px, padding: 0px, borderColor: "{colors.ruleDark}" }
  pricing-feature-table: { backgroundColor: transparent, textColor: "{colors.ink}", rounded: 0px, borderColor: "{colors.ruleDark}" }
  input-chat-composer: { backgroundColor: transparent, textColor: "{colors.ink}", typography: "{typography.body-sm}", rounded: 0px, minHeight: 72px }
  input-search-pill: { backgroundColor: "{colors.surface}", textColor: "{colors.muted}", typography: "{typography.body-sm}", rounded: "{rounded.pill}", padding: 8px 16px, borderColor: "{colors.border}" }
  footer-link-grid: { backgroundColor: "{colors.canvas}", textColor: "{colors.body}", typography: "{typography.body-sm}", gap: "{spacing.md}" }
  article-feed-row: { backgroundColor: transparent, textColor: "{colors.ink}", rounded: 0px, borderColor: "{colors.ruleDark}" }
  model-showcase-band: { backgroundColor: "{colors.canvas}", textColor: "{colors.ink}", rounded: 0px, padding: "{spacing.section}" }
---

**Overview**

OpenAI's public visual system is a restrained, dark editorial interface built around large-scale imagery, black canvases, white type, and quiet pill actions. It avoids loud brand color blocking; recognition comes from the near-monochrome palette, precise OpenAI Sans typesetting, square media grids with slightly softened corners, and a calm rhythm of modular news, research, product, and story surfaces.

The brand has three visible modes. The corporate and marketing mode on `openai.com` is cinematic and editorial: dark background, generous whitespace, image-led cards, and headline sections. The ChatGPT pricing mode is still dark but more utilitarian, using plan columns, comparison tables, FAQ rows, and high-contrast pill buttons. The developer mode is denser and more product-documentation oriented, with charcoal cards, 8-10px radii, muted gray copy, compact nav pills, and search controls.

Key Characteristics:

- Dark-first canvas using {colors.canvas} or {colors.docsCanvas} as the base.
- White and gray type hierarchy rather than saturated brand color.
- OpenAI Sans everywhere, with tight negative tracking on most text.
- Pill CTAs for actions, paired with flat ghost navigation.
- Image-first editorial cards with minimal framing and 6px media radii.
- Flat depth: hierarchy is made through contrast, scale, opacity, and spacing.
- Product-specific modules include chat composer hero, pricing matrix, docs cards, and news/research feeds.

**Colors**

Primary & Action:

- primary: "#ffffff" is the dominant action fill on dark pages. It appears in global CTAs such as "Try ChatGPT" and creates a clear black-on-white pill.
- accent: "#f9f9f9" is used as the softer white action fill in the ChatGPT commerce layer. It keeps CTAs bright without feeling pure optical white in dense plan grids.
- accentHover: "#ececec" supports subtle hover response for white pills. Use it sparingly; OpenAI interactions tend to be quiet.
- accentPressed: "#dcdcdc" is the pressed/active white-family action state. It also matches the primary docs text color.
- link: "#8ad1fd" appears as the rare saturated link color. It should remain an accent, not a general palette driver.

Surfaces:

- canvas: "#000000" is the default marketing and commerce background. It gives the brand its stark, gallery-like presence.
- docsCanvas: "#131313" is the slightly lifted documentation background. It softens the developer experience without leaving the dark system.
- surface: "#212121" is the main charcoal card/search surface on developer pages. It works for contained docs panels and compact inputs.
- surfaceAlt: "#303030" is the active nav/tab surface in developer contexts. Use it to show selection inside otherwise dark navigation.
- translucentAction: "#ffffff1f" is the signature translucent surface for secondary pills and CTA cards. It creates visibility without adding a new hue.
- translucentActionHover: "#ffffff29" is the hover lift for those translucent components.

Neutrals & Text:

- ink: "#ffffff" is the highest-emphasis text on black. It is used for nav, hero headings, plan names, and action labels.
- body: "#dcdcdc" is the primary long-form text in docs surfaces. It is less glaring than pure white and works well on {colors.docsCanvas}.
- muted: "#b9b9b9" is secondary copy and metadata. It appears in developer descriptions and should carry explanatory text, not critical actions.
- textFaint: "#ffffff99" is used for subdued controls such as disabled icon buttons and tertiary chrome.
- chatgptInk: "#0d0d0d" is black text on bright ChatGPT buttons. It gives CTAs strong contrast against {colors.accent}.

Semantic:

- success: "#10a37f" is a conservative OpenAI-adjacent green for confirmations. It was not dominant in the sampled marketing pages, so use it only for product status.
- warning: "#f5a524" is reserved for warnings and cautionary inline states. Do not turn it into a brand accent.
- error: "#ef4444" is reserved for destructive or failed states. Keep it functional and sparse.
- border: "#ffffff1f" is the light-on-dark card and search control border.
- borderStrong: "#ffffff26" is the more visible outline used on dark outline buttons.
- ruleDark: "#ffffff0d" is the very faint divider color used by pricing and FAQ structures.

Brand-specific signatures:

- The monochrome pairing of {colors.canvas}, {colors.ink}, and {colors.translucentAction} is more important than any single hue.
- The developer signature uses {colors.docsCanvas}, {colors.surface}, {colors.surfaceAlt}, and {colors.muted} for a compact technical workspace.
- The pricing signature keeps cards almost unboxed, relying on column rhythm, fine rules, and pill buttons instead of heavy panels.

**Typography**

Font families:

- Primary: `OpenAI Sans, Arial, Helvetica, sans-serif`.
- Code: `ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, monospace`.
- Fallback behavior should preserve geometric neutrality and compact spacing; avoid expressive display faces.

| Level | Size | Weight | Line Height | Letter Spacing |
|---|---:|---:|---:|---:|
| display | 59px | 500 | 1.01 | -0.03em |
| hero | 60px | 500 | 1.00 | -0.03em |
| headline-lg | 46px | 500 | 1.16 | -0.029em |
| title-lg | 30px | 600 | 1.40 | -0.02em |
| title-md | 22px | 500 | 1.25 | -0.01em |
| title-sm | 18px | 600 | 1.35 | -0.01em |
| body | 17px | 400 | 1.65 | -0.01em |
| body-sm | 14px | 400 | 1.64 | -0.01em |
| label | 14px | 500 | 1.00 | 0em |
| button | 14px | 500 | 1.43 | 0em |
| caption | 13px | 500 | 1.00 | 0em |
| legal | 12px | 400 | 1.50 | 0em |
| code | 14px | 400 | 1.55 | 0em |

Principles:

- Use medium weight for large marketing headings; avoid heavy black display weights.
- Apply negative tracking to headings and most body text, especially at 17px and above.
- Keep button and caption tracking neutral; actions feel cleaner without extra compression.
- Let line height open up body copy. OpenAI pages read calmly because paragraphs are airy against the dark canvas.
- Use code typography only in developer/product examples, never as decoration.

**Layout**

The spacing scale is compact at the component level and broad at the section level: {spacing.xs} for card insets, {spacing.sm} for text-media gaps, {spacing.md} for layout gutters, {spacing.lg} for grouped modules, {spacing.xl} for major subsections, and {spacing.section} for page bands.

Marketing pages use a wide container around 1180-1265px with 24px desktop side gutters. Developer pages use a tighter reading grid around 1072px with 16px side padding. Hero text often caps near 800px, producing a short, confident line length rather than full-width copy. Cards usually form 3-column desktop grids, collapse to 2 columns at tablet widths, and become single-column feeds on mobile.

Whitespace philosophy: leave black space visible. OpenAI does not fill every row with containers; it lets media, type, and faint dividers breathe. When building new screens, prefer fewer larger sections with confident gaps over dense boxed dashboards unless the context is explicitly developer documentation or pricing comparison.

**Elevation & Depth**

Observed shadows are essentially absent: most sampled components report `box-shadow: none`. Depth is created by color contrast, opacity, image scale, and border/rule weight rather than stacked material layers.

Use no elevation for default cards. For dark containers, rely on {colors.surface} against {colors.docsCanvas} plus {colors.border}. For marketing and pricing sections, let transparent cards sit directly on {colors.canvas}; introduce {colors.ruleDark} dividers only when tabular scanning requires structure.

**Components**

Buttons:

- `button-primary` is a compact white pill with black text. It appears in global CTAs and pricing/signup actions, using {colors.primary}, {colors.on-primary}, and {rounded.pill}.
- `button-primary-active` darkens the white fill to {colors.accentPressed}. It should feel tactile but not animated or glossy.
- `button-secondary` uses {colors.translucentAction} on dark backgrounds. It works for secondary links, skip links, and quiet supporting actions.
- `button-secondary-hover` increases opacity to {colors.translucentActionHover}. The state should remain flat.
- `button-outline-dark` is a black pill with a faint white border. It appears in ChatGPT commerce contexts where multiple CTAs must sit side by side.
- `button-ghost` is the default navigation behavior: text-only, no fill, no radius, and no visual chrome until interaction.
- `button-icon` is a 40px circular control for carousel and utility actions. Use muted white at rest and avoid enclosing it in a separate card.

Cards & Containers:

- `card-media-news` is an image-led editorial card. The media is usually square or fixed-ratio, with minimal corner softening and text below or adjacent.
- `card-cta-translucent` is a dark marketing CTA card using a translucent white fill and 8px inset. It is useful for API use-case tiles.
- `card-docs` is the developer card: charcoal fill, 10px radius, 20px padding, and a faint border. It is more visibly boxed than marketing cards because developer pages need scan-friendly modules.
- `article-feed-row` is a flat feed item separated by space or faint rules. It supports news, research, stories, and blog entries without heavy card chrome.
- `model-showcase-band` is a full-width dark product band. It should use scale, media, and headline copy rather than decorative gradient backdrops.

Inputs & Forms:

- `input-chat-composer` is the homepage’s product-specific hero pattern: a transparent text area with a minimum 72px height that evokes ChatGPT directly. It should feel like a real prompt surface, not a generic newsletter form.
- `input-search-pill` is the developer search control. It uses {colors.surface}, {colors.muted}, {rounded.pill}, and a faint border to create a compact command/search affordance.

Navigation:

- `nav-global` is a 64px transparent header over the dark page. Links use {typography.body}, white text, and minimal decoration.
- `footer-link-grid` is a dense link directory on {colors.canvas}. It organizes many brand areas with small type, muted text, and clear column spacing rather than visual boxes.

Pricing:

- `pricing-plan-card` is intentionally low-chrome. Plan names and CTAs carry the hierarchy while columns remain mostly transparent.
- `pricing-feature-table` uses faint rules and repeated plan labels. It should remain readable, not ornamental; avoid filling every cell with a card.

Signature Components:

- The chat composer hero is the strongest product-brand bridge. It brings the ChatGPT interaction model directly into a marketing homepage.
- The editorial feed grid is OpenAI’s recurring content pattern: image thumbnail, category/date metadata, concise title, and little else.
- The developer resource card combines technical density with soft charcoal surfaces, creating a distinct mode from the more cinematic corporate pages.

Component audit notes:

- Global header links are visually calm: no filled tabs, no underline system, and no large logo lockup dominating the page.

- Product pages use feature cards only when the card contains a concrete use case or model capability; otherwise content sits directly on the black canvas.

- The homepage prompt area should be treated as a branded product module, not as a decorative search box.

- News and story cards need real imagery, because the monochrome system depends on content photography and generated/product art for variety.

- Pricing cards should preserve column comparison behavior even on smaller screens; do not convert every feature into a separate decorative tile.

- Developer cards can be denser than marketing cards, but they still use generous internal padding and muted copy rather than data-table clutter.

- Footer navigation is intentionally comprehensive and quiet; keep it small, structured, and text-led.

**Do's and Don'ts**

Do:

- Use {colors.canvas} or {colors.docsCanvas} as the base before adding any content.
- Set major headings in {typography.display} or {typography.headline-lg} with negative tracking.
- Use {colors.primary} on {colors.canvas} for the main CTA pill.
- Keep secondary actions in {colors.translucentAction}, not saturated accent colors.
- Build editorial modules with square or fixed-ratio imagery and {rounded.sm}.
- Separate pricing and FAQ content with {colors.ruleDark} instead of heavy card borders.
- Use {colors.surface} and {rounded.lg} for docs cards and search, where utility needs visible containment.

Don't:

- Do not introduce multicolor gradients, glass blur, or glowing shadows; they are not part of the observed system.
- Do not replace OpenAI Sans with a quirky display face or serif headline.
- Do not make buttons large rounded rectangles when a compact {rounded.pill} action is appropriate.
- Do not use saturated blue as the primary brand color; {colors.link} is only a link accent.
- Do not over-card marketing layouts; many OpenAI content blocks are transparent on black.
- Do not use heavy borders above {colors.borderStrong}; the system prefers faint rules.
- Do not center every section in a landing-page style. Use editorial grids and feed rows where content is the product.

**Responsive Behavior**

| Breakpoint | Width | Behavior |
|---|---:|---|
| compact | 0-479px | Single-column feeds, collapsed nav, full-width CTAs |
| mobile | 480-767px | Larger tap targets, stacked pricing cards, reduced hero scale |
| tablet | 768-1023px | 2-column card grids, medium hero headlines, persistent gutters |
| desktop | 1024-1279px | 3-column editorial/product grids, 64px nav, 24px side gutters |
| wide | 1280px+ | Max-width containers, hero copy capped near 800px |

Touch targets should be at least 36px for compact pill buttons and 40px for icon buttons. On mobile, increase vertical hit area to 44px when controls appear in nav, pricing, or FAQ rows.

Collapsing strategy:

- Collapse global nav into a minimal menu while keeping the primary account/action visible where possible.
- Stack pricing plan cards before the comparison matrix; keep CTAs close to each plan name.
- Convert 3-column editorial grids into a single scrolling feed with consistent media ratios.
- Preserve negative tracking but reduce display sizes rather than scaling with viewport width.
- Keep imagery inspectable; crop deliberately and avoid dark overlays unless needed for legibility.

Image behavior: use real product, people, research, or story imagery. Maintain square or stable aspect-ratio crops for cards, and allow hero/product media to span wide bands when it is the main subject.

Responsive audit notes:

- On compact screens, reduce hero type before reducing side padding below readable gutters.

- Keep the first CTA reachable near the top of pricing and product pages.

- Preserve the 64px desktop nav height only when the full nav is visible; mobile nav may become more compact if tap targets remain at least 44px.

- Keep docs cards readable at one column before introducing horizontal scroll.

- Comparison tables may scroll horizontally on mobile, but the plan names and current section label should remain easy to recover.

- Avoid hiding imagery entirely on mobile; crop or reorder it so the editorial character survives.

- Maintain visible black space between modules; do not let stacked mobile sections become a continuous wall of cards.

- Keep footer groups stacked and scannable, with link density reduced only after primary navigation is already simplified.

**Iteration Guide**

1. Check the canvas first: the screen should begin from {colors.canvas} or {colors.docsCanvas}, not a generic gray or blue SaaS background.
2. Audit typography: headings should use {typography.display} or {typography.headline-lg}, weight 500-600, and negative tracking.
3. Inspect CTAs: primary actions should be compact {rounded.pill} buttons with {colors.primary} and {colors.on-primary}.
4. Review secondary controls: use {colors.translucentAction} or ghost text, not outlined neon or saturated fills.
5. Scan cards: marketing cards should be image-first and flat; developer cards may use {colors.surface}, {rounded.lg}, and {colors.border}.
6. Test pricing density: plan columns and feature tables should rely on faint {colors.ruleDark} dividers and readable type, not heavy boxes.
7. Verify imagery: editorial pages need actual media assets, square crops, and minimal decoration.
8. Confirm restraint: remove shadows, gradients, extra hues, and oversized UI chrome unless directly justified by the sampled OpenAI pattern.

**Known Gaps**

Observed directly: homepage, API/product page, ChatGPT pricing page, and developer content page were inspected for rendered typography, colors, radii, buttons, cards, inputs, navigation, and surface behavior. The sampled pages consistently showed OpenAI Sans, black/dark canvases, white and gray text, pill CTAs, flat shadows, 6-10px card radii, and faint borders.

Page evidence:

- Homepage: global nav, ChatGPT-like composer hero, recent news, stories, research feed, business feed, footer link grid.

- API/product page: dark hero, 59px H1, 46px H2s, translucent CTA/use-case cards, white primary CTA, square media rhythm.

- Pricing page: dark commerce mode, 60px H1, 29px plan titles, compact 36px pill CTAs, transparent plan columns, FAQ rows.

- Developer page: {colors.docsCanvas} background, {colors.surface} cards, 10px radii, muted secondary text, compact search pill, dense resource links.

Extraction confidence:

- High confidence: color roles, typography family, large type scale, button radii, dark-first layout, flat depth.

- Medium confidence: exact hover states, breakpoint thresholds, and table behavior outside the sampled viewport.

- Low confidence: semantic status colors, because public marketing surfaces did not expose enough success/warning/error UI.

Derived: semantic colors for success, warning, and error are conservative product-system assumptions because the sampled public marketing pages did not foreground those states. Breakpoints are inferred from observed grid/container behavior and common responsive thresholds rather than extracted from a full stylesheet export.

Uncertain: some pages localized automatically during inspection, but visual values were still measured from rendered CSS. The platform docs URL redirected to a sparse platform shell in one fetch, so the developer content page was used as the content/docs sample. Exact hover/pressed states were inferred from nearby token behavior and opacity variants rather than exhaustive interaction testing on every component.

Use this file as an implementation guide, not a legal brand manual.

When precision matters, re-sample the live page at the target viewport before final production.

When a component is not represented here, prefer the existing principles: dark canvas, OpenAI Sans, flat surfaces, faint rules, compact pills, and restrained color.
