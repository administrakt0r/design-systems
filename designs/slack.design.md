---
version: alpha
name: Slack
slug: slack
source: "https://slack.com/"
extractedAt: "2026-05-18"
description: "Conversational AI work-platform identity built from aubergine action color, Salesforce-derived headline typography, dense rounded product UI screenshots, bento feature modules, and a warm off-white editorial rhythm."

colors:
  primary: "#611F69"
  accent: "#4A154B"
  accentHover: "#481A54"
  accentPressed: "#2E0039"
  ink: "#1D1C1D"
  body: "#454245"
  muted: "#696969"
  canvas: "#FFFFFF"
  surface: "#F5F4F5"
  surfaceAlt: "#F4EDE4"
  border: "#EBEAEB"
  borderStrong: "#DBD9DB"
  link: "#1264A3"
  success: "#007A5A"
  warning: "#F2C744"
  error: "#E01E5A"
  slackBlue: "#36C5F0"
  slackGreen: "#2EB67D"
  slackYellow: "#ECB22E"
  slackRed: "#E01E5A"
  lavenderSurface: "#F9F0FF"
  lavenderTint: "#F9EDFF"
  lavenderBorder: "#EABDFB"
  productBlueSurface: "#E8F5FA"
  productBlueInk: "#0B4C8C"
  aiPurple: "#83388A"
  aiViolet: "#A350AF"
  footerBg: "#1D1C1D"
  on-primary: "#FFFFFF"
  on-dark: "#FFFFFF"
  on-light: "#1D1C1D"

typography:
  display: { fontFamily: "Salesforce-Avant-Garde, Slack-Larsseit, Helvetica Neue, Helvetica, Arial, sans-serif", fontSize: 64px, fontWeight: 700, lineHeight: 1.0, letterSpacing: "-0.02em" }
  hero: { fontFamily: "Salesforce-Avant-Garde, Slack-Larsseit, Helvetica Neue, Helvetica, Arial, sans-serif", fontSize: 56px, fontWeight: 700, lineHeight: 1.05, letterSpacing: "-0.018em" }
  headline-lg: { fontFamily: "Salesforce-Avant-Garde, Slack-Larsseit, Helvetica Neue, Helvetica, Arial, sans-serif", fontSize: 48px, fontWeight: 700, lineHeight: 1.08, letterSpacing: "-0.015em" }
  title-lg: { fontFamily: "Salesforce-Avant-Garde, Slack-Larsseit, Helvetica Neue, Helvetica, Arial, sans-serif", fontSize: 32px, fontWeight: 700, lineHeight: 1.16, letterSpacing: "-0.01em" }
  title-md: { fontFamily: "Salesforce-Sans, Slack-Circular-Pro, Helvetica Neue, Helvetica, Arial, sans-serif", fontSize: 24px, fontWeight: 700, lineHeight: 1.25, letterSpacing: "-0.004em" }
  title-sm: { fontFamily: "Salesforce-Sans, Slack-Circular-Pro, Helvetica Neue, Helvetica, Arial, sans-serif", fontSize: 18px, fontWeight: 700, lineHeight: 1.32, letterSpacing: "0em" }
  body: { fontFamily: "Salesforce-Sans, Slack-Circular-Pro, Helvetica Neue, Helvetica, Arial, sans-serif", fontSize: 18px, fontWeight: 400, lineHeight: 1.5, letterSpacing: "0em" }
  body-sm: { fontFamily: "Salesforce-Sans, Slack-Circular-Pro, Helvetica Neue, Helvetica, Arial, sans-serif", fontSize: 15px, fontWeight: 400, lineHeight: 1.45, letterSpacing: "0em" }
  label: { fontFamily: "Salesforce-Sans, Slack-Circular-Pro, Helvetica Neue, Helvetica, Arial, sans-serif", fontSize: 13px, fontWeight: 700, lineHeight: 1.2, letterSpacing: "0.04em" }
  button: { fontFamily: "Salesforce-Sans, Slack-Circular-Pro, Helvetica Neue, Helvetica, Arial, sans-serif", fontSize: 14px, fontWeight: 700, lineHeight: 1.2, letterSpacing: "0.03em" }
  caption: { fontFamily: "Salesforce-Sans, Slack-Circular-Pro, Helvetica Neue, Helvetica, Arial, sans-serif", fontSize: 13px, fontWeight: 400, lineHeight: 1.45, letterSpacing: "0em" }
  legal: { fontFamily: "Salesforce-Sans, Slack-Circular-Pro, Helvetica Neue, Helvetica, Arial, sans-serif", fontSize: 12px, fontWeight: 400, lineHeight: 1.45, letterSpacing: "0em" }
  code: { fontFamily: "Monaco, Consolas, Liberation Mono, Menlo, monospace", fontSize: 14px, fontWeight: 400, lineHeight: 1.5, letterSpacing: "0em" }

rounded:
  sm: 4px
  md: 8px
  lg: 12px
  xl: 16px
  xxl: 24px
  pill: 9999px

spacing:
  xs: 4px
  sm: 8px
  md: 16px
  lg: 24px
  xl: 32px
  xxl: 48px
  section: 96px

shadows:
  subtle: "0 1px 3px #0000001A"
  card: "0 4px 12px #00000014"
  floating: "0 12px 48px #0016391F, 0 2px 10px #0016390A"

components:
  button-primary: { backgroundColor: "{colors.primary}", textColor: "{colors.on-primary}", typography: "{typography.button}", rounded: "{rounded.md}", padding: 16px 28px }
  button-primary-active: { backgroundColor: "{colors.accentPressed}", textColor: "{colors.on-primary}", rounded: "{rounded.md}" }
  button-secondary: { backgroundColor: "{colors.canvas}", textColor: "{colors.primary}", borderColor: "{colors.primary}", typography: "{typography.button}", rounded: "{rounded.md}", padding: 15px 27px }
  button-secondary-on-dark: { backgroundColor: "transparent", textColor: "{colors.on-dark}", borderColor: "{colors.on-dark}", typography: "{typography.button}", rounded: "{rounded.md}", padding: 15px 27px }
  button-ghost: { backgroundColor: "transparent", textColor: "{colors.link}", typography: "{typography.button}", rounded: "{rounded.sm}", padding: 8px 0 }
  arrow-link: { textColor: "{colors.link}", underlineColor: "{colors.link}", typography: "{typography.title-sm}", icon: "right-arrow" }
  hero-band: { backgroundColor: "{colors.canvas}", textColor: "{colors.ink}", padding: 96px 24px 64px }
  aubergine-band: { backgroundColor: "{colors.accent}", textColor: "{colors.on-dark}", padding: 96px 24px }
  product-ui-frame: { backgroundColor: "{colors.canvas}", borderColor: "{colors.border}", rounded: "{rounded.xl}", shadow: "{shadows.card}", padding: 16px }
  feature-bento-card: { backgroundColor: "{colors.canvas}", borderColor: "{colors.border}", rounded: "{rounded.xl}", shadow: "{shadows.subtle}", padding: 24px }
  ai-answer-card: { backgroundColor: "{colors.lavenderSurface}", borderColor: "{colors.lavenderBorder}", rounded: "{rounded.xl}", shadow: "{shadows.subtle}", padding: 24px }
  pricing-plan-card: { backgroundColor: "{colors.canvas}", borderColor: "{colors.borderStrong}", rounded: "{rounded.lg}", shadow: "{shadows.subtle}", padding: 32px }
  stat-card: { backgroundColor: "{colors.canvas}", textColor: "{colors.ink}", rounded: "{rounded.md}", padding: 24px }
  input-search: { backgroundColor: "{colors.canvas}", textColor: "{colors.ink}", borderColor: "{colors.borderStrong}", rounded: "{rounded.pill}", padding: 16px 52px 16px 64px }
  nav-expanded: { backgroundColor: "{colors.canvas}", textColor: "{colors.ink}", borderColor: "{colors.border}", rounded: "{rounded.md}", shadow: "{shadows.card}" }
  footer: { backgroundColor: "{colors.canvas}", textColor: "{colors.body}", borderColor: "{colors.border}" }
---

**Overview**

Slack’s visual identity is a conversational work surface wrapped in warm enterprise confidence. The brand still turns on aubergine, sharp blue links, and the four-color Slack mark, but the current site has moved toward Salesforce-era typography, larger AI-work-platform messaging, dense product UI screenshots, and pale lavender or blue module backgrounds. It feels approachable and practical: not whimsical for its own sake, but human enough that collaboration software does not become sterile.

The marketing pages use three modes. The homepage is editorial and cinematic, with large headlines, product montages, customer proof, and AI modules. Feature pages become more modular, with alternating copy, screenshot frames, and bento grids. Pricing and help pages are more utilitarian: tighter text, cards, tables, pill search, and clear comparison structures. A faithful Slack screen should combine all three modes without losing the signature balance of friendliness and operational density.

Key Characteristics:

- Aubergine action color anchored by {colors.primary} and deeper {colors.accent}.
- Big, confident display type with compact, uppercase-feeling button labels.
- White and off-white canvases interrupted by lavender AI surfaces and pale blue product panels.
- Rounded rectangular screenshots that show actual Slack UI, not abstract SaaS decoration.
- Link-forward navigation with blue arrow links and dense expanded menus.
- Bento-like feature groupings that mix large hero tiles with small proof or capability tiles.
- Calm enterprise spacing: generous sections, but compact interiors inside cards and nav panels.

**Colors**

Primary & Action:

{colors.primary} is the main action color. It appears on primary CTAs, help coachmarks, focus accents, and selected high-intent controls; use it sparingly so the button system keeps authority.

{colors.accent} is the deeper Slack aubergine. It appears in brand backgrounds, logo-adjacent contexts, and dark bands where the brand needs more gravity than the brighter primary action.

{colors.accentHover} and {colors.accentPressed} provide active depth. These should be used for hover and pressed states on aubergine controls, especially when the interface needs a clear tactile response without adding shadows.

{colors.link} is Slack’s canonical text-link blue. It carries arrow links, documentation links, help article links, and secondary navigation actions; avoid replacing it with generic bright blue.

Surfaces:

{colors.canvas} is the dominant page background and card interior. Slack relies on white to make product screenshots and dense copy feel crisp.

{colors.surface} is a light neutral utility surface. Use it for separators, subtle bands, comparison table backgrounds, and low-emphasis containers.

{colors.surfaceAlt} is the warm editorial off-white. It is useful for legacy Slack marketing warmth, customer story areas, and lower-contrast page bands.

{colors.lavenderSurface} and {colors.lavenderTint} are AI-era surfaces. They show up around assistant, answer, and announcement modules, giving Slackbot/Agentforce content a distinctly softer frame.

{colors.productBlueSurface} supports product information panels. Pair it with {colors.productBlueInk} for informational callouts or feature proof that should feel system-like rather than promotional.

Neutrals & Text:

{colors.ink} is the main text color. It should be used for headings, dense body copy, pricing content, and article text.

{colors.body} is the warmer secondary text color. It appears in paragraphs and supporting copy where full black would feel too harsh.

{colors.muted} handles metadata, sublabels, legal copy, and nav descriptions. It keeps Slack’s dense menus readable without over-weighting every item.

{colors.border} is the default divider. Use it for cards, expanded navigation edges, help article separators, and footer structure.

{colors.borderStrong} is the stronger comparison or input border. It works when a field, table, or pricing card needs an edge visible against white.

Semantic:

{colors.success} is the Slack product green used in checkmarks and positive states. It should feel functional, not decorative.

{colors.warning} is a warm yellow used for warning and highlight treatments. Keep it small because large yellow fields quickly stop feeling like Slack’s current marketing system.

{colors.error} is both semantic error and one of the Slack mark colors. In UI, reserve it for errors, alerts, destructive validation, and brand mark compositions.

Brand-specific signatures:

{colors.slackBlue}, {colors.slackGreen}, {colors.slackYellow}, and {colors.slackRed} are the four Slack-mark accents. Use them in tiny moments: icon details, logo-adjacent motifs, product status chips, or illustrative confetti. Do not build whole screens from these accents.

{colors.aiPurple} and {colors.aiViolet} appear in AI loading, shimmer, and answer modules. They are useful for Slackbot intelligence moments but should remain subordinate to aubergine.

{colors.footerBg} is available for dark editorial bands, but the observed expanded footer is mostly white. Use dark footer treatment only when the page already has a strong brand band.

**Typography**

Slack’s current web typography combines Salesforce-branded headline fonts with Slack’s older sans fallbacks. Display and large headings use a heavy geometric voice; body text is compact, readable, and built for product explanations. The type system is assertive in headlines and pragmatic everywhere else.

| Level | Size | Weight | Line Height | Letter Spacing | Use |
|---|---:|---:|---:|---:|---|
| {typography.display} | 64px | 700 | 1.0 | -0.02em | First-screen brand statements and major campaign lines |
| {typography.hero} | 56px | 700 | 1.05 | -0.018em | Standard hero H1 when product UI shares the viewport |
| {typography.headline-lg} | 48px | 700 | 1.08 | -0.015em | Section leads and major proof blocks |
| {typography.title-lg} | 32px | 700 | 1.16 | -0.01em | Feature headings, pricing headings, content hubs |
| {typography.title-md} | 24px | 700 | 1.25 | -0.004em | Card titles, article headings, module titles |
| {typography.title-sm} | 18px | 700 | 1.32 | 0em | Feature list titles and link headings |
| {typography.body} | 18px | 400 | 1.5 | 0em | Marketing body copy and explanatory paragraphs |
| {typography.body-sm} | 15px | 400 | 1.45 | 0em | Help text, nav sublabels, compact cards |
| {typography.label} | 13px | 700 | 1.2 | 0.04em | Eyebrows, categories, table labels |
| {typography.button} | 14px | 700 | 1.2 | 0.03em | CTAs and compact command labels |
| {typography.caption} | 13px | 400 | 1.45 | 0em | Metadata, footnotes, small descriptions |
| {typography.legal} | 12px | 400 | 1.45 | 0em | Legal notes and source attributions |
| {typography.code} | 14px | 400 | 1.5 | 0em | Developer snippets or API references |

Principles:

- Track display text slightly tight; Slack headlines look confident because they are large, heavy, and compact.
- Keep body text open and readable; do not copy display tracking into paragraphs.
- Use strong weight jumps instead of many intermediate weights. Slack relies on 400 and 700 more than delicate typography.
- Buttons should feel like labels, not sentences: short, bold, and slightly tracked.
- Article/help pages should reduce scale and increase density while retaining {colors.ink}, {colors.link}, and clear dividers.

**Layout**

Slack’s spacing scale is simple: {spacing.sm} and {spacing.md} inside dense UI, {spacing.lg} and {spacing.xl} inside cards, and {spacing.section} between major marketing bands. Product screenshots and content blocks often sit inside centered containers around 1080-1280px wide, with copy columns constrained closer to 480-560px for readability. Feature grids move from one column on mobile to two columns at tablet and four-column bento arrangements on desktop.

Page rhythm alternates between broad white space and information-dense modules. The whitespace philosophy is generous at section boundaries but economical inside components: nav flyouts, pricing cards, help articles, and product UI frames all pack content tightly with clear typographic hierarchy. When designing Slack-like layouts, avoid decorative emptiness; every large gap should either frame a major headline, reveal a product screenshot, or separate proof from explanation.

**Elevation & Depth**

Slack is mostly flat with selective tactile depth. {shadows.subtle} is enough for help answer cards, small product modules, and pricing cards; {shadows.card} can lift a screenshot or dropdown; {shadows.floating} belongs to chat widgets and temporary overlays. Depth should clarify layering, not create a glossy SaaS showroom.

Hierarchy often comes from color fields, typography, grid size, and screenshot scale rather than heavy shadow. A large white card on a lavender surface, a dense product UI frame, or a blue arrow link often communicates structure more accurately than deep elevation.

**Components**

Buttons:

`button-primary` is the highest-intent Slack action. It uses {colors.primary}, white text, bold uppercase-feeling type, and a moderate {rounded.md} corner; use it for “Get started,” “Request demo,” and plan actions.

`button-primary-active` darkens to {colors.accentPressed}. It should feel pressed and decisive, not animated or glossy.

`button-secondary` is a white button with aubergine text and border. It often sits beside primary actions, especially where Slack wants two equally visible paths such as “Get started” and “Find your plan.”

`button-secondary-on-dark` is the inverse outline for aubergine or dark bands. Keep the border white and the label concise so the button remains legible on saturated backgrounds.

`button-ghost` is for low-friction navigation. It should behave more like a textual control than a button block.

`arrow-link` is a signature Slack link pattern. It pairs {colors.link} with a right-arrow cue and often appears under feature copy, in cards, and across help/resource modules.

Cards & Containers:

`hero-band` is the default marketing stage. It should be white, spacious, and paired with product UI or recognizable customer proof, not abstract illustration alone.

`aubergine-band` is the brand-strength section. Use it for closing CTAs, bold proof, or brand moments where white type can sit confidently on deep Slack color.

`product-ui-frame` holds screenshots or reconstructed Slack UI. It needs {rounded.xl}, a light border, and modest shadow so product content feels tangible but not skeuomorphic.

`feature-bento-card` is Slack’s modular capability unit. It should support uneven grid spans, compact copy, and product imagery without turning every tile into a marketing card.

`ai-answer-card` is the Slackbot/AI module. Use lavender surfaces, a soft border, small icon/avatar elements, and tight copy that resembles a helpful answer rather than a generic promo card.

`stat-card` is simple and evidence-driven. It works best with one large number, one short label, and enough whitespace to make the metric scan quickly.

Inputs & Forms:

`input-search` is the most distinctive form pattern observed in help and AI surfaces. It uses pill geometry, large left icon/avatar space, and dense placeholder text; keep it taller than ordinary form fields.

Standard inputs should use {colors.canvas}, {colors.borderStrong}, and {rounded.sm} or {rounded.md}. Slack forms look practical, not soft or playful.

Navigation:

`nav-expanded` is dense and structured. It uses white background, grouped columns, uppercase category labels, muted sublabels, and compact links. The goal is fast scanning across product taxonomy.

Primary nav links are plain, dark, and compact. Dropdown triggers should not look like full buttons unless they are high-intent CTAs.

`footer` is content-heavy and mostly white in the observed pages. It relies on columns, legal links, and muted text rather than a large decorative footer block.

Pricing:

`pricing-plan-card` organizes plan comparison through bordered white cards, bold plan names, short descriptions, price or contact emphasis, and stacked feature lists. Highlight differences with border, heading, and CTA hierarchy rather than dramatic color fills.

Pricing pages also use announcement banners and pill-like plan selectors. Keep these visually lighter than the plan cards so the comparison remains the main object.

Signature Components:

Slack product screenshots are first-class brand assets. They should show channels, messages, huddles, lists, workflows, canvases, Slackbot answers, or integrations in recognizable UI frames.

The screenshot frame should feel like a captured workspace. Include sidebars, message rows, app chips, avatars, or workflow steps; a blank dashboard rectangle will not read as Slack.

AI modules use answer-card structure, shimmer-like purple accents, avatar or sparkle details, and copy that implies action from conversation.

AI answers should look compact and useful. Prefer a short generated response, a small source cue, and one obvious next action over a large promotional panel.

Feature tile grids use mixed heights and spans. Large tiles introduce a category; smaller tiles act like capability shortcuts.

Tiles may carry icons, short headings, and product thumbnails, but they should not all have identical height on desktop. Slack’s feature pages use uneven spans to create a working rhythm.

Expanded menus are part of the brand experience. They expose Slack’s taxonomy through multi-column groups: Collaboration, Project Management, Platform, Intelligence, Admin & Security, and related resource calls.

Customer proof modules pair real company names, quotes, video thumbnails, and statistics. They should feel editorial and credible, not like generic logo strips.

Comparison tables should be quiet and scannable. Use {colors.border}, checkmark rows, muted explanatory copy, and one strong CTA per plan area.

Help-center modules should prioritize search. The search field, suggested topic pills, article links, and support chatbot entry points are the visual grammar of Slack documentation.

**Do's and Don'ts**

Do:

- Use {colors.primary} for decisive CTAs and keep competing action colors out of the same cluster.
- Pair large {typography.hero} or {typography.headline-lg} text with real product UI frames.
- Use {colors.link} for arrow links and help/documentation navigation.
- Build feature pages from mixed bento cards, not uniform three-card rows only.
- Use lavender AI surfaces for Slackbot, Agentforce, answers, and search-assist moments.
- Keep nav flyouts dense with muted sublabels and clear category labels.
- Let pricing cards stay white and bordered so plan comparison feels operational.
- Use Slack’s four mark colors only as small accents unless rendering the logo itself.

Don't:

- Do not replace aubergine with generic purple gradients; Slack’s action identity depends on {colors.primary} and {colors.accent}.
- Do not make every card heavily shadowed; most Slack depth is {shadows.subtle}.
- Do not use rounded pill buttons for every CTA; primary marketing buttons use moderate {rounded.md}, while search and topic chips use {rounded.pill}.
- Do not create abstract SaaS blob illustrations in place of product screenshots.
- Do not stretch body copy across full-width containers; keep text columns constrained.
- Do not turn help/article pages into oversized marketing pages; they should use compact {typography.body-sm} and clear links.
- Do not flood a screen with Slack Blue, Green, Yellow, and Red; they are brand accents, not layout colors.
- Do not hide product complexity too much; Slack’s visual language is recognizable because dense conversations, lists, and workflows are visible.

**Responsive Behavior**

| Breakpoint | Width | Behavior |
|---|---:|---|
| Compact mobile | 0-479px | Single-column flow, stacked CTAs, simplified nav, cropped or scaled product media |
| Mobile | 480-767px | One-column feature sections, large touch targets, screenshot frames below copy |
| Tablet | 768-1023px | Two-column grids begin, hero media and copy rebalance, nav condenses |
| Small desktop | 1024-1279px | Expanded bento layouts, desktop nav, product images beside copy |
| Wide desktop | 1280px+ | Maximum content containers, four-column feature grids, stronger hero composition |

Touch targets should be at least 44px high. Buttons commonly exceed this through 16px vertical padding, and search inputs are taller with icon space.

Collapsing strategy:

- Stack hero copy above or before product imagery on mobile.
- Collapse bento grids to one column, then two columns, then mixed four-column spans.
- Convert expanded navigation into mobile panels with grouped lists.
- Keep paired CTAs stacked or full-width on narrow screens.
- Preserve product screenshot legibility by cropping less important edges before shrinking text below readability.

Image behavior:

Product imagery should remain real and inspectable. Use responsive widths, fixed aspect-ratio frames, and modest rounding. Avoid dark overlays on screenshots unless text is not placed over the image.

Screenshots can crop peripheral UI on mobile, but message text, channel names, and primary action labels should remain legible. If the UI becomes decorative noise, replace it with a tighter crop rather than scaling it down further.

**Iteration Guide**

1. Check the first viewport: it should combine {typography.hero}, clear CTA hierarchy, and a visible Slack product or brand signal.
2. Verify the action palette: primary actions use {colors.primary}; text links use {colors.link}; Slack mark colors are only accents.
3. Audit card geometry: product and AI cards should use {rounded.xl}; CTAs should use {rounded.md}; search fields should use {rounded.pill}.
4. Inspect typography: headings should be heavy and slightly tight, while paragraphs remain readable at {typography.body} or {typography.body-sm}.
5. Confirm density: navs, pricing cards, and help modules should contain useful details, not oversized empty panels.
6. Test responsive grids: feature bento layouts must collapse cleanly from mixed desktop spans into readable mobile cards.
7. Review screenshots: at least one major visual should show Slack-like channels, messages, workflows, lists, huddles, AI answers, or integrations.
8. Recheck contrast: white text on {colors.primary} and {colors.accent} is acceptable; muted text should not be used over lavender or dark bands without adjustment.

**Known Gaps**

Observed directly: homepage content and structure, features page structure, pricing page structure, help article page structure, live CSS color values, font-face names, breakpoints, button classes, arrow-link styling, borders, shadows, card radii, search-pill behavior, expanded navigation groups, and AI/help card patterns.

Derived conservatively: the exact type scale in this file is normalized from observed CSS and rendered page behavior. Slack’s CSS uses many responsive and locale-specific overrides, so the YAML expresses a practical design-system scale rather than every page-specific exception.

Uncertain: exact production font availability can vary by locale, CDN bundle, and Salesforce/Slack page generation. The safest implementation is to use the declared Salesforce and Slack font family names with system fallbacks. Some homepage hero effects use radial color washes in CSS, but they are not treated as core tokens because they are campaign-specific rather than universal Slack identity.

Also uncertain: internal Slack application UI has its own mature design system that differs from marketing pages. This extraction is for slack.com and adjacent help/pricing/content experiences, not a complete clone of the logged-in Slack product.

Evidence pages researched:

- Homepage: `https://slack.com/`
- Feature page: `https://slack.com/features`
- Pricing page: `https://slack.com/pricing`
- Help/content page: `https://slack.com/help/articles/115004071768-What-is-Slack`
