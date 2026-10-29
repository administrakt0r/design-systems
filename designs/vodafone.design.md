---
version: alpha
name: Vodafone
slug: vodafone
source: https://www.vodafone.com/
extractedAt: 2026-05-18
description: "High-contrast telecom identity built around Vodafone Red, oversized condensed-feeling brand typography, pill CTAs, flat editorial cards, video-led heroes, and repeated connected-world content modules."

colors:
  primary: "#e60000"
  accent: "#e60000"
  accentHover: "#bd0000"
  accentPressed: "#820000"
  ink: "#25282b"
  body: "#25282b"
  muted: "#7e7e7e"
  canvas: "#ffffff"
  surface: "#ffffff"
  surfaceAlt: "#f9f9f9"
  surfaceMuted: "#f2f2f2"
  border: "#bebebe"
  borderStrong: "#4a4d4e"
  link: "#e60000"
  success: "#008a00"
  warning: "#eb6100"
  error: "#bd0000"
  focus: "#0096ad"
  info: "#005ea5"
  telecomTeal: "#00697c"
  enterprisePlum: "#5e2750"
  signalOrange: "#eb6100"
  highlightYellow: "#fecb00"
  financePurple: "#9c2aa0"
  redGradientDeep: "#820000"
  overlayDark: "#00000080"
  overlayLight: "#ffffff80"
  on-primary: "#ffffff"
  on-dark: "#ffffff"

typography:
  display: {fontFamily: "Vodafone, Arial, Helvetica, sans-serif", fontSize: 126px, fontWeight: 800, lineHeight: 0.90, letterSpacing: "-0.008em"}
  display-lg: {fontFamily: "Vodafone, Arial, Helvetica, sans-serif", fontSize: 90px, fontWeight: 800, lineHeight: 0.93, letterSpacing: "0em"}
  headline-lg: {fontFamily: "Vodafone, Arial, Helvetica, sans-serif", fontSize: 32px, fontWeight: 700, lineHeight: 1.25, letterSpacing: "0em"}
  headline-md: {fontFamily: "Vodafone, Arial, Helvetica, sans-serif", fontSize: 24px, fontWeight: 700, lineHeight: 1.25, letterSpacing: "0em"}
  headline-sm: {fontFamily: "Vodafone, Arial, Helvetica, sans-serif", fontSize: 20px, fontWeight: 700, lineHeight: 1.30, letterSpacing: "0em"}
  body-lg: {fontFamily: "Vodafone, Arial, Helvetica, sans-serif", fontSize: 24px, fontWeight: 400, lineHeight: 1.50, letterSpacing: "0em"}
  body: {fontFamily: "Vodafone, Arial, Helvetica, sans-serif", fontSize: 18px, fontWeight: 400, lineHeight: 1.56, letterSpacing: "0em"}
  caption: {fontFamily: "Vodafone, Arial, Helvetica, sans-serif", fontSize: 14px, fontWeight: 400, lineHeight: 1.43, letterSpacing: "0em"}
  label: {fontFamily: "Vodafone, Arial, Helvetica, sans-serif", fontSize: 14px, fontWeight: 400, lineHeight: 1.14, letterSpacing: "0em"}
  button: {fontFamily: "Vodafone, Arial, Helvetica, sans-serif", fontSize: 16px, fontWeight: 800, lineHeight: 1.50, letterSpacing: "0em"}
  nav: {fontFamily: "Vodafone, Arial, Helvetica, sans-serif", fontSize: 18px, fontWeight: 400, lineHeight: 1.33, letterSpacing: "0em"}
  stat: {fontFamily: "Vodafone, Arial, Helvetica, sans-serif", fontSize: 70px, fontWeight: 800, lineHeight: 1.17, letterSpacing: "-0.014em"}

rounded:
  sm: 6px
  md: 12px
  lg: 24px
  xl: 40px
  pill: 9999px

spacing:
  xs: 8px
  sm: 16px
  md: 32px
  lg: 56px
  xl: 96px
  section: 96px

components:
  button-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button}"
    rounded: "{rounded.pill}"
    padding: 12px 24px
  button-primary-active:
    backgroundColor: "{colors.accentHover}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.pill}"
  button-secondary:
    backgroundColor: "transparent"
    textColor: "{colors.ink}"
    borderColor: "{colors.ink}"
    typography: "{typography.button}"
    rounded: "{rounded.pill}"
    padding: 12px 24px
  button-secondary-on-dark:
    backgroundColor: "transparent"
    textColor: "{colors.on-dark}"
    borderColor: "{colors.on-dark}"
    rounded: "{rounded.pill}"
  button-tertiary:
    backgroundColor: "{colors.surfaceMuted}"
    textColor: "{colors.ink}"
    iconColor: "{colors.primary}"
    rounded: "{rounded.pill}"
  button-text-link:
    backgroundColor: "transparent"
    textColor: "{colors.primary}"
    typography: "{typography.body}"
    underlineColor: "{colors.primary}"
  button-icon:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.pill}"
    size: 48px
  hero-video:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    typography: "{typography.display}"
    overlayColor: "{colors.overlayDark}"
  editorial-image-card:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    rounded: "{rounded.sm}"
    shadow: "none"
  utility-card:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.ink}"
    borderColor: "{colors.border}"
    rounded: "{rounded.sm}"
    padding: 32px
  stat-panel:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.ink}"
    statColor: "{colors.primary}"
    typography: "{typography.stat}"
  content-panel:
    backgroundColor: "{colors.surfaceAlt}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
    padding: 32px
  mega-nav:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.ink}"
    typography: "{typography.nav}"
    borderColor: "{colors.border}"
  search-input:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.ink}"
    borderColor: "{colors.border}"
    focusColor: "{colors.focus}"
    rounded: "{rounded.sm}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    linkColor: "{colors.on-dark}"
  tariff-benefit-card:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.ink}"
    iconColor: "{colors.primary}"
    rounded: "{rounded.md}"
    padding: 32px
---

**Overview**
Vodafone’s global site presents a corporate telecom brand with unusually strong scale contrast: very large brand-font display type sits beside simple body copy, full-bleed video or image panels, and direct pill-shaped actions. The visual identity is not fussy. It relies on Vodafone Red, near-black charcoal, white space, and confident editorial composition rather than ornamental illustration or soft SaaS gradients.

The system has two visible modes. The corporate/editorial site is dramatic, video-led, and statement-driven, with “everyone.connected” language, oversized words, image cards, stats, and dark sections. The Vodafone Business pages are more utility-oriented but still use the same red action language, Vodafone typeface, simple grids, icon-led cards, and rounded containers.

Key Characteristics:

- Use `{colors.primary}` as the immediate brand signal, especially for CTAs, statistics, icons, focus moments, and red gradient hero treatments.
- Pair oversized `{typography.display}` with calm `{typography.body}` copy; Vodafone feels recognizable when the type scale jumps hard.
- Keep components flat: cards, panels, and images use `{rounded.sm}` with little or no shadow.
- Prefer full-bleed video, photography, and editorial image cards over abstract decoration.
- Use pill CTAs from `{components.button-primary}` and secondary outline pills from `{components.button-secondary}`.
- Build around “connected” modules: hero statements, stats, signpost cards, and content blocks that connect people, businesses, continents, and futures.
- Keep navigation practical and content-rich, with mega-menu columns, image signposts, and a dark footer.

**Colors**
Primary & Action:

`primary` / `accent` is Vodafone Red. It is the main action color, brand field, icon accent, statistics color, and the most important recognition cue. It should be used in concentrated blocks rather than tinting every surface.

`accentHover` is the darker red used for hover, active, error, and deeper action states. Use it for pressed CTAs, red overlays, and hover states that need clear feedback while staying unmistakably Vodafone.

`accentPressed` and `redGradientDeep` are the deepest red tones observed in brand gradients. They are appropriate for video overlays, red hero depth, and darkened motion backgrounds, not for everyday text.

Surfaces:

`canvas` and `surface` are white. Vodafone uses white as the default corporate canvas so red, black typography, and editorial images can carry the page.

`surfaceAlt` is a very light near-white used to separate content bands without adding a colored theme. It is useful for quiet business sections and long editorial pages.

`surfaceMuted` is the pale grey utility surface for tertiary buttons, foundation-style cards, and low-emphasis panels.

Neutrals & Text:

`ink` and `body` are the same charcoal. This is the primary text color and dark section background; it is softer than pure black and works well against Vodafone Red.

`muted` supports secondary labels, captions, metadata, and disabled-feeling copy. It should not replace `{colors.body}` for main paragraphs.

`border` and `borderStrong` define the restrained structural language: thin borders, subtle dividers, and no heavy decorative strokes.

Semantic:

`success` is a direct green for positive status and operational confirmation.

`warning` and `signalOrange` are orange, suitable for alerts, telecom signal warnings, and status emphasis.

`error` reuses dark red. It fits the brand but must be paired with labels or icons because it is visually close to action red.

`focus` is a teal-blue outline used for keyboard and accessibility focus. Preserve this distinction; do not replace focus outlines with red.

Brand-specific signatures:

`telecomTeal`, `enterprisePlum`, `highlightYellow`, and `financePurple` appear as secondary palette colors. Use them sparingly for category systems, data accents, and business/product icon groups.

`overlayDark` and `overlayLight` support legibility on full-bleed photography and video. They should be functional overlays, not decorative glass effects.

**Typography**
Vodafone uses its own “Vodafone” font across display, headings, navigation, body copy, buttons, and stats. Use `Arial, Helvetica, sans-serif` only as fallbacks. The site also loads Inter in some contexts, but the brand variables point to Vodafone for both title and body primitives.

| Level | Size | Weight | Line height | Letter spacing | Use |
|---|---:|---:|---:|---:|---|
| `{typography.display}` | 126px | 800 | 0.90 | -0.008em | Homepage statements, video heroes, giant “connected” language |
| `{typography.display-lg}` | 90px | 800 | 0.93 | 0em | Large page titles and campaign section headers |
| `{typography.headline-lg}` | 32px | 700 | 1.25 | 0em | Section headlines, carousel headings |
| `{typography.headline-md}` | 24px | 700 | 1.25 | 0em | Cards, content modules, business product headings |
| `{typography.headline-sm}` | 20px | 700 | 1.30 | 0em | Labels, small card titles, footer headings |
| `{typography.body-lg}` | 24px | 400 | 1.50 | 0em | Hero supporting copy and lead paragraphs |
| `{typography.body}` | 18px | 400 | 1.56 | 0em | Default paragraphs and product descriptions |
| `{typography.caption}` | 14px | 400 | 1.43 | 0em | Metadata, dates, legal, breadcrumbs |
| `{typography.label}` | 14px | 400 | 1.14 | 0em | Form labels and utility labels |
| `{typography.button}` | 16px | 800 | 1.50 | 0em | CTAs and strong commands |
| `{typography.nav}` | 18px | 400 | 1.33 | 0em | Header navigation and menu items |
| `{typography.stat}` | 70px | 800 | 1.17 | -0.014em | Big numbers and performance highlights |

Principles:

- Push scale. Vodafone’s signature comes from very large display type, not from decorative type treatments.
- Use heavy weights for actions, stats, and hero claims; use regular weight for navigation and body to keep the system readable.
- Keep tracking neutral, with slight negative spacing only on the largest display and stat levels.
- Mix all-caps sparingly. Buttons are uppercase in the corporate CTA style, while prose and section titles stay sentence-like.
- Allow emphasized words inside display headings, especially connected-world phrases, but keep the emphasis typographic rather than colorful.

**Layout**
The layout is based on Bootstrap-like breakpoints and a 12-column grid with 32px gutters at container level. Max-widths step from 540px through 1320px, with major layouts changing at 768px, 992px, 1200px, and 1400px. The spacing scale is compact at the component level, then generous at section scale: `{spacing.xs}` for icon gaps, `{spacing.sm}` for small rhythm, `{spacing.md}` for card interiors, and `{spacing.section}` for large editorial bands.

Whitespace is assertive but not precious. Vodafone pages often let one large message, one image, or one statistic dominate a viewport, then use tight supporting modules below. Business pages are denser, but still preserve clear row gaps and card padding so product categories can be scanned quickly.

**Elevation & Depth**
The core corporate system is flat. Global card and panel shadow variables are effectively `none`, and hierarchy is created through scale, contrast, image cropping, red accents, and section background changes. Use shadows only when a true overlay or modal requires separation.

Observed shadow tokens exist for optional depth, but they are not the visual default. Cards should feel like editorial surfaces or clickable tiles, not floating material objects. Depth on the homepage more often comes from video overlays, image gradients, and large foreground type.

**Components**
Buttons:

`{components.button-primary}` is the main Vodafone action: red fill, white text, heavy button typography, and a pill silhouette. It appears in hero actions, business contact prompts, and strong content CTAs.

`{components.button-primary-active}` darkens the red for hover, focus, and active states. Use it to show interactivity without changing shape or adding shadow.

`{components.button-secondary}` is an outline pill for lower-priority actions on light surfaces. It uses charcoal text and border, then can invert to dark fill on hover.

`{components.button-secondary-on-dark}` is the dark-section counterpart: transparent, white outline, white text, and red icon accents when needed. It should remain visibly secondary beside red primary actions.

`{components.button-tertiary}` is a quiet grey pill used for less-prominent utility commands. Its red icon is the cue that it is still part of the Vodafone action family.

`{components.button-text-link}` is an inline CTA with a red underline that animates or expands on hover. Use it in editorial cards and article lists where a pill button would feel too heavy.

`{components.button-icon}` covers search, video play/pause, close, and back-to-top controls. It should be circular or pill-round, with enough size for touch and a simple glyph.

Cards & Containers:

`{components.hero-video}` is the dominant brand module: full-bleed media, dark overlay, enormous display type, and a short supporting paragraph. It creates instant Vodafone recognition.

`{components.editorial-image-card}` is a dark image signpost with text over photography, small category labels, and a whole-card link. It appears in navigation, news, and “latest” sections.

`{components.utility-card}` is the business/product card: white surface, light border, simple icon, heading, and paragraph. It is practical and grid-friendly, not decorative.

`{components.stat-panel}` turns numbers into brand moments. The number uses `{typography.stat}` and typically red or white depending on section mode.

`{components.content-panel}` is a restrained light panel for explanatory business content, investor modules, or support blocks. It should keep `{rounded.sm}` and use layout spacing rather than shadow for separation.

Inputs & Forms:

`{components.search-input}` is the clearest observed form pattern: a large search field in the header, Vodafone font, white surface, and teal focus treatment. Keep fields rectangular with small radius and visible focus.

Forms should not overuse red borders because red already carries action and error. Use `{colors.focus}` for keyboard focus and `{colors.error}` only for validation failures with text.

Navigation:

`{components.mega-nav}` uses a white header surface, charcoal links, regular-weight navigation typography, deep dropdown columns, and image signposts. Mega-menu links have generous vertical padding and use icons sparingly for disclosure.

The mobile navigation collapses into a hierarchical drawer. Keep link rows tall, plain, and content-first; the Vodafone personality comes from clear structure and imagery, not animated ornament.

`{components.footer}` is dark, information-heavy, and practical. It combines accordion-like link groups, regional site lists, investor/share-price modules, legal copy, and white links.

Pricing:

`{components.tariff-benefit-card}` appears on the Vodafone Business Global Tariffs page as benefit tiles such as roaming, commercial simplicity, adaptive data plans, and flexible usage. It functions more like a product-benefit grid than a price table.

No global consumer price cards were observed on `vodafone.com`; individual markets likely handle plan pricing locally. For global business pages, model pricing-adjacent content as tariff explainers, benefit grids, and contact-led conversion.

Signature Components:

Connected-world heroes use giant phrases like “everyone.connected” and section titles for people, businesses, continents, and futures. Recreate the rhythm with `{typography.display}`, concise copy, and one strong media surface.

Mega trend modules use background text, red-accented headings, video/image blocks, and expandable CTAs. They should feel like editorial reports, with prominent section titles and measured prose.

Latest-news signposts use image cards, dates, categories, and headline typography. Keep the cards image-led and avoid generic white blog-card styling.

**Do's and Don'ts**
Do:

- Use `{colors.primary}` as the first visual signal on actions, stats, icons, and selected editorial accents.
- Set hero claims in `{typography.display}` or `{typography.display-lg}` with short, direct language.
- Keep cards flat with `{rounded.sm}` and use image contrast or layout placement for hierarchy.
- Pair dark sections with `{colors.on-dark}` text and red actions, especially for media-led modules.
- Use `{components.button-primary}` for the main CTA and `{components.button-secondary}` for alternative paths.
- Use `{colors.focus}` for focus outlines so accessibility states are distinct from red action states.
- Build business sections with icon-led `{components.utility-card}` or `{components.tariff-benefit-card}` grids.
- Let photography and video fill their containers with `object-fit: cover` and purposeful cropping.

Don't:

- Do not turn Vodafone into a soft pastel or monochrome red interface; white, charcoal, and disciplined red are essential.
- Do not add glassmorphism, floating glow, or decorative shadow to flat editorial cards.
- Do not make every heading red; reserve `{colors.primary}` for action, stats, icons, and key brand fields.
- Do not use rounded card corners larger than `{rounded.sm}` unless building a pill CTA or brand video control.
- Do not replace Vodafone’s heavy CTA typography with light or lowercase button labels.
- Do not use generic SaaS split heroes when a full-bleed media hero would carry the Vodafone identity better.
- Do not use red as a focus-only color; preserve `{colors.focus}` for keyboard visibility.
- Do not invent a global price-card pattern; use tariff and benefit modules unless local market evidence is available.

**Responsive Behavior**
| Breakpoint | Width | Behavior |
|---|---:|---|
| xs | 0px | Single-column content, mobile nav drawer, stacked cards |
| sm | 576px | Narrow container, larger touch spacing, simple two-up where safe |
| md | 768px | Tablet layouts, larger radius tokens, image/text modules begin pairing |
| lg | 992px | Multi-column editorial sections and wider business grids |
| xl | 1200px | Desktop mega-navigation, full display scale, complex grid modules |
| xxl | 1400px | 1320px max container and full editorial spacing |

Touch targets should be at least 44px, with icon buttons preferably 48px. Pill CTAs need enough horizontal padding to keep their strong shape visible on mobile.

Collapsing strategy:

- Collapse mega-navigation into a drawer below desktop and keep menu levels explicit.
- Stack utility cards to one column on mobile, two columns on tablet, and three or four columns on desktop depending on content.
- Reduce hero display size through responsive clamps, but keep the display-to-body contrast dramatic.
- Preserve image aspect ratios; do not let image cards shrink into shallow strips.
- Move CTA groups below supporting copy on mobile and keep primary action first.

Images should use full-width containers, cover cropping, and dark overlays when text sits on top. Editorial images should reveal the actual subject where possible; avoid abstract stock-like replacements.

**Iteration Guide**
1. Check the first viewport: does it show either Vodafone Red, a strong Vodafone wordmark/navigation cue, or a full-bleed media hero with `{typography.display}`?
2. Audit CTAs: every primary action should match `{components.button-primary}` and every lower-priority action should use a secondary, tertiary, or text-link pattern.
3. Inspect type scale: hero and stat type must be visibly larger than card headings; if everything feels the same size, the system is not Vodafone enough.
4. Verify card depth: cards should use `{rounded.sm}`, flat surfaces, and image/content contrast rather than ornamental shadows.
5. Test red discipline: `{colors.primary}` should stand out because it is selective, not because the whole page is tinted red.
6. Check accessibility states: focus outlines should use `{colors.focus}` and be visible on light and dark sections.
7. Review business/product screens: product groupings should use icon-led cards, benefit grids, and contact-led conversion instead of invented pricing tiers.
8. Validate responsive behavior: mobile should stack cleanly, keep touch targets above 44px, and preserve large Vodafone display moments.

**Known Gaps**
Observed directly: the global homepage, the Internet of Things / mega trends product-feature page, a Vodafone Business Global Tariffs page, and a current news/content page. The global variables CSS provided strong evidence for colors, typography, spacing ramps, radii, theme modes, shadows, and CTA states.

Derived: fixed pixel typography values are desktop approximations from Vodafone’s responsive CSS clamps. The actual site scales fluidly, so generated experiences should use the listed sizes as target maxima and preserve the relative hierarchy.

Uncertain: exact local-market consumer pricing cards were not available on `vodafone.com`; Vodafone routes device offers and account pricing to local country sites. The pricing section therefore documents the global business tariff pattern, not consumer plan purchase UI.

Also uncertain: some Vodafone Business pages are built with a separate Next.js/styled-components stack. They share the same fonts, red actions, grids, and card logic, but exact component class names and runtime styles are more opaque than the corporate CSS.
