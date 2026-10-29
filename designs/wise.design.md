---
version: alpha
name: Wise
slug: wise
source: "https://wise.com/"
extractedAt: "2026-05-22"
description: "Transparent money-product system built around vivid Wise Green, deep forest text, pill navigation, compact currency calculators, flag-led selectors, and flat rounded utility surfaces."

colors:
  primary: "#163300"
  accent: "#9FE870"
  accentHover: "#80E142"
  accentPressed: "#65CF21"
  ink: "#0E0F0C"
  body: "#454745"
  muted: "#6A6C6A"
  canvas: "#FFFFFF"
  surface: "#FFFFFF"
  surfaceAlt: "#F1F1ED"
  surfaceTint: "#E2F6D5"
  border: "rgba(14,15,12,0.12157)"
  borderStrong: "#CACFC7"
  link: "#163300"
  success: "#054D28"
  warning: "#FFD11A"
  error: "#CB272F"
  brightGreen: "#9FE870"
  forestGreen: "#163300"
  forestGreenHover: "#0D1F00"
  forestGreenPressed: "#0E0F0C"
  brightBlue: "#A0E1E1"
  brightYellow: "#FFEB69"
  brightOrange: "#FFC091"
  brightPink: "#FFD7EF"
  darkCharcoal: "#21231D"
  darkPurple: "#260A2F"
  darkGold: "#3A341C"
  darkMaroon: "#320707"
  celebrationBg: "#ECF9F9"
  celebrationText: "#0B4C72"
  mapBlue: "#435E89"
  legacyBlue: "#0097C7"
  on-primary: "#FFFFFF"
  on-accent: "#163300"
  on-dark: "#9FE870"

typography:
  display:
    fontFamily: "\"Wise Sans\", \"Inter\", sans-serif"
    fontSize: 64px
    fontWeight: 700
    lineHeight: 1.0
    letterSpacing: "-0.04em"
  hero:
    fontFamily: "\"Wise Sans\", \"Inter\", sans-serif"
    fontSize: 56px
    fontWeight: 700
    lineHeight: 1.05
    letterSpacing: "-0.04em"
  headline-lg:
    fontFamily: "\"Wise Sans\", \"Inter\", sans-serif"
    fontSize: 40px
    fontWeight: 700
    lineHeight: 1.1
    letterSpacing: "-0.03em"
  title-lg:
    fontFamily: "\"Wise Sans\", \"Inter\", sans-serif"
    fontSize: 32px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: "-0.025em"
  title-md:
    fontFamily: "\"Wise Sans\", \"Inter\", sans-serif"
    fontSize: 24px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: "-0.015em"
  title-sm:
    fontFamily: "\"Wise Sans\", \"Inter\", sans-serif"
    fontSize: 20px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: "-0.01em"
  body:
    fontFamily: "\"Inter\", Helvetica, Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: "0em"
  body-lg:
    fontFamily: "\"Inter\", Helvetica, Arial, sans-serif"
    fontSize: 18px
    fontWeight: 400
    lineHeight: 1.55
    letterSpacing: "0em"
  label:
    fontFamily: "\"Inter\", Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: "0em"
  button:
    fontFamily: "\"Inter\", Helvetica, Arial, sans-serif"
    fontSize: 16px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: "0em"
  nav:
    fontFamily: "\"Inter\", Helvetica, Arial, sans-serif"
    fontSize: 15px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: "0em"
  caption:
    fontFamily: "\"Inter\", Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.45
    letterSpacing: "0em"
  legal:
    fontFamily: "\"Inter\", Helvetica, Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: "0em"
  pricing-display:
    fontFamily: "\"Wise Sans\", \"Inter\", sans-serif"
    fontSize: 48px
    fontWeight: 700
    lineHeight: 1.05
    letterSpacing: "-0.03em"

rounded:
  sm: 10px
  md: 16px
  lg: 24px
  xl: 32px
  pill: 9999px

spacing:
  xs: 4px
  sm: 8px
  md: 16px
  lg: 24px
  xl: 32px
  xxl: 56px
  section: 96px

components:
  button-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button}"
    rounded: "{rounded.pill}"
    padding: 12px 24px 10px
  button-primary-active:
    backgroundColor: "{colors.forestGreenPressed}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.pill}"
  button-accent:
    backgroundColor: "{colors.accent}"
    textColor: "{colors.on-accent}"
    typography: "{typography.button}"
    rounded: "{rounded.pill}"
    padding: 12px 24px 10px
  button-accent-active:
    backgroundColor: "{colors.accentPressed}"
    textColor: "{colors.on-accent}"
    rounded: "{rounded.pill}"
  button-secondary:
    backgroundColor: "{colors.surfaceTint}"
    textColor: "{colors.primary}"
    typography: "{typography.button}"
    rounded: "{rounded.pill}"
    padding: 12px 24px 10px
  button-ghost:
    backgroundColor: "transparent"
    textColor: "{colors.primary}"
    typography: "{typography.nav}"
    rounded: "{rounded.pill}"
    padding: 8px 12px
  button-icon:
    backgroundColor: "{colors.surfaceTint}"
    textColor: "{colors.primary}"
    rounded: "{rounded.pill}"
    size: 40px
  nav-pill:
    backgroundColor: "rgba(255,255,255,0.8)"
    textColor: "{colors.primary}"
    rounded: "{rounded.lg}"
    height: 34px
  nav-dropdown:
    backgroundColor: "{colors.surface}"
    borderColor: "{colors.border}"
    rounded: "{rounded.md}"
    shadow: "0 20px 66px 0 rgba(34,48,73,0.20)"
  currency-calculator:
    backgroundColor: "{colors.surface}"
    borderColor: "{colors.border}"
    rounded: "{rounded.md}"
    padding: 24px
  amount-input:
    backgroundColor: "transparent"
    textColor: "{colors.primary}"
    typography: "{typography.pricing-display}"
    rounded: "{rounded.sm}"
  currency-selector:
    backgroundColor: "{colors.surface}"
    borderColor: "{colors.border}"
    textColor: "{colors.ink}"
    rounded: "{rounded.pill}"
    padding: 8px 12px
  feature-card:
    backgroundColor: "{colors.surface}"
    borderColor: "{colors.border}"
    rounded: "{rounded.md}"
    padding: 24px
  segment-card:
    backgroundColor: "{colors.surfaceAlt}"
    textColor: "{colors.ink}"
    rounded: "{rounded.md}"
    padding: 16px
  pricing-table:
    backgroundColor: "{colors.surface}"
    borderColor: "{colors.border}"
    rounded: "{rounded.md}"
    rowMinHeight: 40px
  prompt-positive:
    backgroundColor: "{colors.surfaceTint}"
    textColor: "{colors.success}"
    rounded: "{rounded.sm}"
    padding: 16px
  alert-celebration:
    backgroundColor: "{colors.celebrationBg}"
    textColor: "{colors.celebrationText}"
    rounded: "{rounded.sm}"
    padding: 4px 8px
  article-container:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    maxWidth: 672px
  footer:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-dark}"
---

**Overview**

Wise's visual identity is built around the idea that money should feel clear, fast, and fair. The system uses a high-recognition pairing of bright green and deep forest green, but the brand does not rely on color alone. It combines compact product controls, large direct headlines, flag-led currency selection, plain-language pricing modules, and rounded pill actions to make financial UI feel approachable without becoming decorative.

There are three visible modes. Marketing pages use large `Wise Sans` headlines, green or forest sections, full-bleed product photography/video, and bold calls to action. Product and pricing pages become denser: calculator panels, currency flags, fee rows, comparison tables, and inline prompts carry the experience. Help Centre pages are the quietest mode, preserving the same typography and rounded buttons while prioritizing readable articles and a simpler sticky nav.

Key Characteristics:

- Use `{colors.accent}` as the unmistakable Wise signal, especially for hero fields, active states, and positive action moments.
- Pair `{colors.primary}` with `{colors.accent}` instead of black-on-green when the interface needs to feel branded.
- Prefer pill controls and compact modules over square SaaS panels.
- Let currency flags, large numeric inputs, and fee breakdown rows do product storytelling.
- Keep shadows rare; most hierarchy comes from color, spacing, borders, and type scale.
- Use direct, plain typographic hierarchy with negative tracking on large `Wise Sans` headings.
- Treat pricing transparency as a visual pattern: rows, dashed dividers, highlighted savings, and clear fee labels.

**Colors**

Primary & Action

`primary` / `{colors.primary}` is Wise's forest action color. It appears in logos, primary text on bright-green themes, links, buttons, calculator amounts, and active navigation.

`accent` / `{colors.accent}` is the signature bright Wise Green. It appears as the main brand field, CTA background in many marketing contexts, active pill color, and a positive highlight surface.

`accentHover` and `accentPressed` support tactile green interactions. Use them for hover and pressed states on bright green CTAs, not as extra decorative tones.

`link` / `{colors.link}` stays forest rather than web-blue in the modern Wise theme. This keeps articles and product flows visually tied to the brand.

Surfaces

`canvas` and `surface` are clean white surfaces used for articles, calculator cards, dropdowns, and pricing modules.

`surfaceAlt` is a warm off-white used for softened panels, dropdown group backgrounds, and neutral bands. It should feel practical and paper-like, not creamy or editorial.

`surfaceTint` is a pale green positive surface. It appears in prompts, highlighted table rows, and neutral-positive UI feedback.

`celebrationBg` is a pale cyan celebration surface used for specific prompts and rate/product moments. It is secondary to green and should not become the dominant page theme.

Neutrals & Text

`ink` is the main text color in the personal theme. It is nearly black but slightly warm, matching Wise's utility tone.

`body` and `muted` soften descriptive text, captions, helper copy, and metadata. Avoid lowering contrast too far in calculators or legal/pricing copy.

`border` is an alpha border over the text color. Wise often uses this instead of a fixed gray, so borders inherit the mood of the current theme.

Semantic

`success` is deep green for positive sentiment labels. It is distinct from action green and should be used for status, not primary CTAs.

`warning` is a bright yellow with dark-gold content. Use it sparingly for risk, regulatory, or attention modules.

`error` is a direct red used for validation and negative alerts. Wise pairs it with pale red surfaces rather than heavy red blocks.

Brand-specific Signatures

`brightGreen` and `forestGreen` are the core brand duet. Most Wise-looking compositions need both: one as field or action, the other as text or anchor.

`brightBlue`, `brightYellow`, `brightOrange`, and `brightPink` are supporting brand brights. They appear in illustrations, campaign surfaces, and small product emphasis, not as random dashboard categories.

`darkCharcoal`, `darkPurple`, `darkGold`, and `darkMaroon` are contrast partners for the brights. They keep the palette grounded when a section moves away from green.

`mapBlue` and `legacyBlue` appear in older or utility contexts such as map backgrounds and Help Centre/system surfaces. Use only when matching those patterns.

**Typography**

Wise splits typographic work between `Wise Sans` for display and `Inter` for interface reading. `Wise Sans` gives the brand its blunt, confident headline voice; `Inter` keeps forms, tables, and articles legible at product density.

| Level | Family | Size | Weight | Line Height | Letter Spacing |
|---|---|---:|---:|---:|---:|
| display | `Wise Sans` | 64px | 700 | 1.0 | -0.04em |
| hero | `Wise Sans` | 56px | 700 | 1.05 | -0.04em |
| headline-lg | `Wise Sans` | 40px | 700 | 1.1 | -0.03em |
| title-lg | `Wise Sans` | 32px | 700 | 1.2 | -0.025em |
| title-md | `Wise Sans` | 24px | 700 | 1.25 | -0.015em |
| title-sm | `Wise Sans` | 20px | 700 | 1.3 | -0.01em |
| body-lg | `Inter` | 18px | 400 | 1.55 | 0em |
| body | `Inter` | 16px | 400 | 1.5 | 0em |
| label | `Inter` | 14px | 600 | 1.4 | 0em |
| button | `Inter` | 16px | 700 | 1.2 | 0em |
| nav | `Inter` | 15px | 700 | 1.2 | 0em |
| caption | `Inter` | 14px | 400 | 1.45 | 0em |
| legal | `Inter` | 12px | 400 | 1.5 | 0em |
| pricing-display | `Wise Sans` | 48px | 700 | 1.05 | -0.03em |

Principles:

- Tighten large type with negative tracking; Wise headlines should feel compact and emphatic.
- Keep body and form text on `Inter` with normal tracking for clarity.
- Use weight instead of ornament. Buttons, nav, and row labels are bold but not all-caps.
- Let numbers become display elements in calculators and pricing rows.
- Keep article typography restrained; Help Centre pages should feel like product support, not a magazine.

**Layout**

Wise uses a 4px-root scale with prominent stops at 8, 16, 24, 32, 40, 56, 72, and 96px. Containers commonly max around 1164px on desktop, with 16px mobile gutters, 24px tablet gutters, and 32px desktop gutters. Marketing sections can stretch wider for media, while product modules stay constrained and scannable.

Grid behavior is practical: two-column hero layouts on desktop, stacked flows on mobile, and repeated card/table structures that preserve row rhythm. Pricing and calculator components favor fixed minimum heights, visible row separators, and responsive button stacks that become full-width below small breakpoints.

Whitespace is generous around sections but tight inside product modules. The brand does not create luxury whitespace; it creates breathing room around dense financial decisions so amounts, rates, fees, and CTAs remain easy to compare.

**Elevation & Depth**

Wise is mostly flat. Cards, tables, and prompts rely on `{colors.border}`, rounded corners, and surface contrast instead of heavy elevation. This keeps the product honest and avoids making financial information feel hidden behind decorative chrome.

The main observed shadow is used for navigation dropdowns: `0 20px 66px 0 rgba(34,48,73,0.20)`. Use it only for floating overlays, large menus, or modal-like surfaces. Do not apply it to every card.

Depth also comes from motion: dropdowns fade/scale into place, mobile menus slide horizontally, and loading states shimmer subtly. These interactions are short and utilitarian.

**Components**

Buttons

`button-primary` uses `{colors.primary}` with white text for high-contrast committed actions. It should be pill-shaped and compact, with the slight bottom padding adjustment Wise uses to optically center text.

`button-accent` is the signature Wise CTA when the background is dark or neutral. It pairs `{colors.accent}` with `{colors.on-accent}` and should read as confident rather than playful.

`button-secondary` uses pale green surfaces for lower-priority actions such as feedback buttons, inline choices, and secondary CTAs. It keeps the UI branded while reducing urgency.

`button-ghost` is for nav tabs, language controls, and low-friction links. It should remain text-forward, with hover expressed through neutral green-tinted backgrounds.

`button-icon` is circular, usually 40px, and used for menu, close, language, and compact utility controls. Keep icons simple and filled with the current interactive color.

Cards & Containers

`feature-card` is a bordered rounded content unit for benefits, business features, and reusable explanation blocks. It should be plain, readable, and never over-shadowed.

`segment-card` appears in navigation mega menus with media, a short title, body copy, and an arrow link. It is more editorial than product cards but still compact.

`prompt-positive` is a pale green feedback container used to explain savings, next steps, or positive product outcomes. It should be concise and action-adjacent.

`alert-celebration` is a cyan-tinted micro-alert. Use it for celebratory or informational emphasis when green would confuse the action hierarchy.

Inputs & Forms

`currency-calculator` is a core Wise pattern: rounded panel, large amount field, paired currency selectors, flags, fee breakdown, and a decisive CTA. It must feel like the product, not a generic lead form.

`amount-input` uses oversized numeric type and forest color. It is borderless or minimally framed inside the calculator, with the selector carrying most of the visible affordance.

`currency-selector` is flag-led and pill-like. It combines country/currency identity with a chevron, usually within a calculator row or conversion form.

Navigation

`nav-pill` is Wise's compact desktop navigation mode: a translucent or flat pill area with bold 15px labels and rounded active areas. It should not become a tall enterprise navbar.

`nav-dropdown` is one of the few elevated surfaces. It uses rounded 16px corners, a small pointer, grouped links with icons, and the large overlay shadow.

The mobile navigation slides in from the side and turns CTAs into full-width buttons. Large mobile tab labels can reach 40px in pill navigation, giving the menu a strong brand moment.

Pricing

`pricing-table` uses rounded borders, minimum 40px rows, and clear divisions between categories. It favors plain words like "Free", fixed fees, and percentages over visual flourish.

Pricing comparison blocks should highlight transparency: mid-market rate, no hidden fees, clear conversion fee, and row-by-row cost breakdown. Dashed dividers can be used where a calculation is being explained.

Signature Components

The currency calculator is the most important product signature. Always include amount, source/target currency, flag or currency icon, rate/fee explanation, and a CTA when designing a Wise-like money flow.

Flag stacks and currency-pair visuals are another signature. Overlapping circular flags, usually 44-72px, quickly communicate international money movement.

The fee breakdown pattern is central: row labels on the left, numeric values on the right, highlighted savings or rate rows, and explanatory helper text below.

The business plan picker uses rounded pricing cards with feature lists, icon avatars, one-time payment labels, and clear Basic/Advanced comparison. Keep it functional rather than salesy.

Help Centre article pages use a sticky white nav, centered article column, bold `Wise Sans` H1, plain paragraphs, related articles, and simple Yes/No feedback buttons.

**Do's and Don'ts**

Do:

- Use `{colors.accent}` and `{colors.primary}` together in first-viewport compositions.
- Build money flows around `currency-calculator`, not around generic email-capture forms.
- Use `{rounded.pill}` for CTAs, nav tabs, selectors, and icon buttons.
- Keep pricing rows explicit with `pricing-table`, row dividers, and right-aligned values.
- Use `Wise Sans` only where the message needs brand confidence; use `Inter` for dense product reading.
- Let flags, currency codes, rates, and fees carry visual distinctiveness.
- Use the dropdown shadow only for overlays like `nav-dropdown`.
- Stack buttons full-width on mobile with at least 48px touch height.

Don't:

- Do not replace Wise Green with generic fintech blue for primary actions.
- Do not use heavy card shadows or glass effects on product modules.
- Do not square off buttons; Wise actions should use `{rounded.pill}` or large rounded corners.
- Do not make decorative gradients the main brand expression.
- Do not use all-caps labels for pricing or navigation; Wise stays sentence-case and direct.
- Do not hide fees inside collapsed or decorative elements when a row explanation is expected.
- Do not overuse supporting brights like `{colors.brightPink}` or `{colors.brightOrange}` as category colors.
- Do not stretch article text wider than the readable article column.

**Responsive Behavior**

| Breakpoint | Width | Behavior |
|---|---:|---|
| compact | 320px | Preserve logo/menu, reduce CTA padding, stack all actions. |
| mobile | 576px | 16px gutters, single-column cards, full-width button stacks. |
| tablet | 768px | 24-32px gutters, two-column media can begin, calculators remain prominent. |
| laptop | 992px | Nav can expose more items; product layouts can use side-by-side modules. |
| desktop | 1200px | Full pill navigation, dropdown menus, max-width container around 1164px. |
| wide | 1440px+ | Increase content breathing room; keep product controls constrained. |

Touch targets should be at least 40px for compact controls and 48px for primary mobile CTAs. Icon buttons should remain circular and not shrink below 40px except in the narrowest nav fallback.

Collapsing strategy:

- Stack calculator fields vertically on mobile while preserving amount-first hierarchy.
- Convert CTA groups to full-width vertical stacks below small breakpoints.
- Collapse desktop navigation into a slide-in menu below 1200px.
- Hide excess flag-grid items at mobile and tablet widths.
- Keep pricing rows readable by stacking descriptions above values if horizontal space is tight.

Image behavior should be real and product-relevant: cards, people using Wise, flags, app screens, maps, or currency visuals. Hero media may overflow horizontally for impact, but it must stay anchored to the product story and avoid generic finance stock imagery.

**Iteration Guide**

1. Check that the first screen uses the `{colors.accent}` plus `{colors.primary}` pairing somewhere meaningful.
2. Confirm all main CTAs use `{rounded.pill}` and button text uses `{typography.button}`.
3. Verify large headings use `Wise Sans`, negative letter spacing, and a compact line height.
4. Audit money-related screens for a visible calculator, currency selector, rate, fee, and CTA.
5. Inspect pricing modules for row clarity: no hidden fees, no ambiguous labels, right-aligned values.
6. Remove unnecessary shadows; only dropdowns, modals, and floating menus should use the large Wise shadow.
7. Test mobile at 320px and 576px: buttons stack, nav slides, text does not overflow pills.
8. Make sure supporting brights are accents, not a replacement for the green/forest system.

**Known Gaps**

Observed directly: homepage, Wise Business, Wise pricing, and a Help Centre article were fetched on 2026-05-22. CSS token extraction confirmed the modern personal theme colors, forest and bright-green modes, font families, size scale, radii, navigation behavior, dropdown shadow, and many component class patterns.

Derived: the largest display sizes in this file are inferred from token scale, class usage, and rendered page hierarchy rather than a single exposed named CSS token. Component padding values are based on observed CSS snippets and Wise button conventions, with minor optical rounding.

Uncertain: Wise likely runs experiments by locale, product, and visitor state. Some pages still expose older blue utility tokens, while the main Wise brand uses the green system. Treat blue tokens as legacy/support-context values unless a specific Wise page clearly uses them.

Not fully captured: animation curves, every icon size, all dark-mode permutations, and proprietary illustration/photo rules. The extraction is strongest for color, typography, spacing, nav, buttons, calculators, pricing rows, and Help Centre article structure.
