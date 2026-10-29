---
version: alpha
name: "Disney+"
slug: "disneyplus"
source: "https://www.disneyplus.com/"
extractedAt: "2026-05-21"
description: "Cinematic streaming system built from midnight navy-black stages, crisp Inspire typography, cyan-teal action sparks, poster-led rails, bundle comparison modules, and a distinct shift into lighter Salesforce-style help surfaces."

colors:
  primary: "#3DDEFF"
  accent: "#3DDEFF"
  accentHover: "#66BCFF"
  accentPressed: "#056D85"
  ink: "#040714"
  body: "#B7B8BD"
  muted: "#6F717B"
  canvas: "#17171C"
  surface: "#17171C"
  surfaceAlt: "#25272C"
  border: "#6F717B"
  borderStrong: "#4A4D59"
  link: "#66BCFF"
  success: "#65DCA1"
  warning: "#FFDE66"
  error: "#CA1F16"
  surfaceLow: "#121118"
  surfaceHigh: "#2C2E35"
  heroBackdrop: "#1A1D29"
  bundleTeal: "#124954"
  helpCanvas: "#F6F7F8"
  helpSurface: "#FFFFFF"
  helpBorder: "#ECEBEA"
  helpBrand: "#056D85"
  helpLink: "#0B7AAD"
  legalGold: "#FFDB6E"
  on-primary: "#040714"
  on-dark: "#FAFAFA"

typography:
  display:
    fontFamily: "\"Inspire\", \"Segoe UI\", system-ui, sans-serif"
    fontSize: 72px
    fontWeight: 600
    lineHeight: 1.11
    letterSpacing: "-0.02em"
  hero:
    fontFamily: "\"Inspire\", \"Segoe UI\", system-ui, sans-serif"
    fontSize: 40px
    fontWeight: 600
    lineHeight: 1.30
    letterSpacing: "0em"
  headline-lg:
    fontFamily: "\"Inspire\", \"Segoe UI\", system-ui, sans-serif"
    fontSize: 32px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: "0em"
  headline-md:
    fontFamily: "\"Inspire\", \"Segoe UI\", system-ui, sans-serif"
    fontSize: 28px
    fontWeight: 600
    lineHeight: 1.29
    letterSpacing: "0em"
  title-lg:
    fontFamily: "\"Inspire\", \"Segoe UI\", system-ui, sans-serif"
    fontSize: 24px
    fontWeight: 700
    lineHeight: 1.33
    letterSpacing: "0em"
  title-md:
    fontFamily: "\"Inspire\", \"Segoe UI\", system-ui, sans-serif"
    fontSize: 20px
    fontWeight: 600
    lineHeight: 1.20
    letterSpacing: "0em"
  title-sm:
    fontFamily: "\"Inspire\", \"Segoe UI\", system-ui, sans-serif"
    fontSize: 18px
    fontWeight: 700
    lineHeight: 1.33
    letterSpacing: "0em"
  body:
    fontFamily: "\"Inspire\", \"Segoe UI\", system-ui, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.50
    letterSpacing: "0em"
  body-small:
    fontFamily: "\"Inspire\", \"Segoe UI\", system-ui, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: "0em"
  caption:
    fontFamily: "\"Inspire\", \"Segoe UI\", system-ui, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.33
    letterSpacing: "0em"
  label:
    fontFamily: "\"Inspire\", \"Segoe UI\", system-ui, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.14
    letterSpacing: "0.01em"
  button:
    fontFamily: "\"Inspire\", \"Segoe UI\", system-ui, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: "0.01em"
  utility-button:
    fontFamily: "\"Inspire\", \"Segoe UI\", system-ui, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.15
    letterSpacing: "0em"
  legal:
    fontFamily: "\"Inspire\", \"Segoe UI\", system-ui, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.44
    letterSpacing: "0em"

rounded:
  sm: 4px
  md: 8px
  lg: 12px
  xl: 24px
  pill: 9999px

spacing:
  xs: 4px
  sm: 8px
  md: 16px
  lg: 24px
  xl: 40px
  section: 56px

components:
  button-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button}"
    rounded: "{rounded.md}"
    padding: "12px 32px"
  button-primary-active:
    backgroundColor: "{colors.accentPressed}"
    textColor: "{colors.on-dark}"
    typography: "{typography.button}"
    rounded: "{rounded.md}"
    padding: "12px 32px"
  button-secondary-on-dark:
    backgroundColor: "rgba(0,0,0,0.8)"
    textColor: "{colors.on-dark}"
    typography: "{typography.utility-button}"
    rounded: "{rounded.md}"
    padding: "8px 16px"
  button-help-primary:
    backgroundColor: "{colors.helpBrand}"
    textColor: "{colors.on-dark}"
    typography: "{typography.body}"
    rounded: "{rounded.sm}"
    padding: "16px 20px"
  nav-header:
    backgroundColor: "transparent"
    textColor: "{colors.on-dark}"
    typography: "{typography.utility-button}"
    rounded: "0px"
    padding: "8px 16px"
  hero-stage:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    rounded: "0px"
    padding: "0px 0px"
  collection-rail-card:
    backgroundColor: "transparent"
    textColor: "{colors.on-dark}"
    rounded: "{rounded.sm}"
    padding: "10px 10px"
  flip-info-card:
    backgroundColor: "{colors.surfaceAlt}"
    textColor: "{colors.on-dark}"
    rounded: "{rounded.lg}"
    padding: "40px 16px 20px 16px"
  faq-accordion-row:
    backgroundColor: "{colors.surfaceAlt}"
    textColor: "{colors.on-dark}"
    rounded: "{rounded.xl}"
    padding: "24px 24px"
  pricing-comparison-grid:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.on-dark}"
    rounded: "0px"
    padding: "24px 0px"
  legal-modal:
    backgroundColor: "{colors.surfaceAlt}"
    textColor: "{colors.on-dark}"
    rounded: "{rounded.md}"
    padding: "40px 24px"
  help-article-shell:
    backgroundColor: "{colors.helpSurface}"
    textColor: "{colors.ink}"
    typography: "{typography.body}"
    rounded: "0px"
    padding: "0px 0px"
  help-form-field:
    backgroundColor: "{colors.helpCanvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body}"
    rounded: "{rounded.sm}"
    padding: "12px 16px"
---

**Overview**
Disney+ presents itself as a theater first and a website second. The dominant experience is a dark streaming shell built on `{colors.ink}` and `{colors.canvas}`, where oversized title art, poster rails, and wide hero backgrounds do most of the emotional work. Interface chrome stays disciplined: text is bright but not loud, radii are controlled, and `{colors.primary}` appears as a cool cyan-teal spark rather than a page-wide theme wash. The mood is premium, nocturnal, and franchise-driven, with the UI acting like a frame around media rather than a decorative identity layer.

The brand clearly operates in two visual modes. Marketing and browse surfaces are cinematic and immersive, using dark fields, image-led modules, plan grids, and FAQ slabs. Support surfaces in the Help Center pivot to a lighter utility mode built on `{colors.helpCanvas}` and `{colors.helpSurface}`, with denser article text, smaller radii, and Salesforce-derived form scaffolding. That split is central to the Disney+ system: discovery should feel like entering an entertainment universe, while assistance should feel practical, serviceable, and calm without severing the connection to the core brand.

Key Characteristics:
- Anchor most customer-facing pages in `{colors.ink}` and `{colors.canvas}` so imagery feels illuminated against a theater-dark stage.
- Reserve `{colors.primary}` for commitment moments such as primary CTAs, selection emphasis, and bright focus cues.
- Use restrained radii from `{rounded.sm}` to `{rounded.lg}` so cards feel architectural instead of soft and playful.
- Let posters, logos, and franchise art provide personality while typography and containers stay controlled.
- Build hierarchy through contrast, spacing, sticky positioning, and surface shifts more often than through shadows.
- Treat pricing, bundles, and FAQs as branded product modules, not as generic marketing blocks.
- Shift decisively into `{colors.helpCanvas}` and `{colors.helpSurface}` for support and article workflows.

**Colors**
Primary & Action

`primary` `{colors.primary}` / `#3DDEFF`
This is the signature decision color across Disney+ marketing surfaces. It appears in primary buttons, active utility controls, emphasized links, and select highlights, giving the dark system a cool, technological spark rather than a warm promotional tone.

`accentHover` `{colors.accentHover}` / `#66BCFF`
This lighter cyan-blue is used as a hover lift rather than a second brand hue. It keeps interactive states visible on black without introducing a radically different mood.

`accentPressed` `{colors.accentPressed}` / `#056D85`
Pressed and deeper action states drop into this darker teal. It preserves the brand family while signaling firmness, especially in CTAs and Help Center branded buttons.

`link` `{colors.link}` / `#66BCFF`
Marketing links stay in the same cool family as actions, which keeps navigation, inline legal links, and assistive jumps visually related to CTA moments.

`helpBrand` `{colors.helpBrand}` / `#056D85`
In the Help Center this becomes the primary branded button and focus color. It reads more service-oriented than `{colors.primary}` because the light UI needs stronger contrast and less glow.

Surfaces

`ink` `{colors.ink}` / `#040714`
This is the deepest cinematic black-blue in the system. It appears behind hero media and in the broadest atmospheric backgrounds, helping Disney+ feel more like a screen in a dark room than a flat webpage.

`canvas` `{colors.canvas}` / `#17171C`
This is the default dark field for marketing pages, pricing zones, and content groupings. It is dark enough to recede while still allowing adjacent panels to step up or down in value.

`surface` `{colors.surface}` / `#17171C`
The base surface and the canvas are effectively aligned, which reinforces the flat, continuous stage feel of the product.

`surfaceAlt` `{colors.surfaceAlt}` / `#25272C`
This panel color is used for FAQ rows, informational cards, and modal bodies. It creates hierarchy through a surface step rather than through shadow.

`surfaceLow` `{colors.surfaceLow}` / `#121118`
This darker layer supports footers, underlays, and lower-depth containers. It is useful when Disney+ wants extra separation without resorting to borders everywhere.

`surfaceHigh` `{colors.surfaceHigh}` / `#2C2E35`
This higher container tone appears in stronger utility contexts and can outline more data-heavy sections. It stays within the dark family and never becomes a light card.

`bundleTeal` `{colors.bundleTeal}` / `#124954`
This brand-specific teal appears in bundle and explanatory contexts. It gives pricing and educational modules their own emphasis without breaking out of the core dark palette.

`helpCanvas` `{colors.helpCanvas}` / `#F6F7F8`
This is the main Help Center page background. It marks the visual transition from entertainment discovery into support and account clarity.

`helpSurface` `{colors.helpSurface}` / `#FFFFFF`
Help articles, search fields, and form-heavy content sit on white surfaces. That clean utility backdrop is intentionally more conventional than the streaming experience.

Neutrals & Text

`on-dark` `{colors.on-dark}` / `#FAFAFA`
This is the primary text color on dark marketing surfaces. Disney+ uses it for display headlines, CTA text on dark buttons, and the highest priority UI labels.

`body` `{colors.body}` / `#B7B8BD`
Supporting text, descriptions, and metadata sit here. It softens long passages without making them feel faded or secondary to the point of weakness.

`muted` `{colors.muted}` / `#6F717B`
This is the quieter neutral for outlines, smaller metadata, and less important interface information. It is especially useful in a system that relies on low-chroma hierarchy.

`border` `{colors.border}` / `#6F717B`
The standard border tone stays visible on dark surfaces but does not pull too much focus. It is a structure color more than a decoration color.

`borderStrong` `{colors.borderStrong}` / `#4A4D59`
This darker structural line is helpful in comparison grids and dense component groupings. It supports tabular rhythm and sticky headers without introducing bright separators.

Semantic

`success` `{colors.success}` / `#65DCA1`
Success is present in token form and aligns with contemporary streaming-service status language. It is less saturated than gaming greens, which suits the premium tone.

`warning` `{colors.warning}` / `#FFDE66`
Warning appears in legal and cautionary contexts, especially where Disney+ needs to separate notices from normal body copy without using alarming red.

`error` `{colors.error}` / `#CA1F16`
The system includes a clear destructive red for account, form, and service problems. On marketing surfaces it is rare; on utility surfaces it becomes more important.

Brand-specific signatures

`heroBackdrop` `{colors.heroBackdrop}` / `#1A1D29`
This supporting dark blue-black helps large media zones feel layered even when shadows are absent. It is more atmospheric than structural.

`helpLink` `{colors.helpLink}` / `#0B7AAD`
Help Center links use a more conventional service-blue than the main site’s cyan, reinforcing that article navigation belongs to a utility pattern.

`legalGold` `{colors.legalGold}` / `#FFDB6E`
This appears in legal and disclosure-related emphasis, especially where Disney+ needs a caution tone that remains premium rather than urgent.

**Typography**
Disney+ uses the proprietary `Inspire` family across both marketing and support surfaces, with `Segoe UI`, `system-ui`, and `sans-serif` as practical fallbacks. The family is asked to do nearly everything: display, hero, body, labels, buttons, and legal copy. That unified voice is important to the brand. Even when the Help Center becomes visually lighter and more utility-driven, it still sounds like Disney+ because the type system does not split into a separate editorial personality.

| Role | Size | Weight | Line Height | Letter Spacing | Family |
|---|---:|---:|---:|---:|---|
| `display` | 72px | 600 | 1.11 | -0.02em | Inspire |
| `hero` | 40px | 600 | 1.30 | 0em | Inspire |
| `headline-lg` | 32px | 600 | 1.25 | 0em | Inspire |
| `headline-md` | 28px | 600 | 1.29 | 0em | Inspire |
| `title-lg` | 24px | 700 | 1.33 | 0em | Inspire |
| `title-md` | 20px | 600 | 1.20 | 0em | Inspire |
| `title-sm` | 18px | 700 | 1.33 | 0em | Inspire |
| `button` | 18px | 600 | 1.33 | 0.01em | Inspire |
| `body` | 16px | 400 | 1.50 | 0em | Inspire |
| `body-small` | 14px | 400 | 1.43 | 0em | Inspire |
| `label` | 14px | 600 | 1.14 | 0.01em | Inspire |
| `utility-button` | 13px | 400 | 1.15 | 0em | Inspire |
| `caption` | 12px | 400 | 1.33 | 0em | Inspire |
| `legal` | 12px | 400 | 1.44 | 0em | Inspire |

Principles:
- Keep tracking mostly neutral; the only strong compression is in `{typography.display}` where `"-0.02em"` tightens hero language into a more premium silhouette.
- Use weight economically. Disney+ relies on 600 and 700 for hierarchy, but it does not escalate into aggressively black or hyper-condensed display behavior.
- Let line-height stay generous in body text and legal text so disclosures remain readable against dark surfaces.
- Avoid a family split between marketing and support; the consistency of `Inspire` is part of the brand bridge between entertainment and service.
- Treat uppercase as a utility signal, mainly in small buttons, labels, and compact navigation, not in large editorial headings.

**Layout**
The spacing rhythm clusters around `{spacing.sm}` 8px, `{spacing.md}` 16px, `{spacing.lg}` 24px, `{spacing.xl}` 40px, and `{spacing.section}` 56px, with observed intermediate layout values such as 20px, 28px, 32px, 48px, 56px, 72px, and 80px in the marketing CSS. Responsive breakpoints observed across the marketing shell include 480px, 768px, 1024px, and 1366px, with image and content widths stepping through roughly 441, 769, 1025, 1291, and 1600px media tiers. Grid behavior favors full-width hero zones, horizontally scrollable rails on smaller screens, and multi-column comparison structures at larger sizes. The Help Center separately caps major content widths around 1330px.

Disney+ whitespace is not airy in the lifestyle-brand sense; it is cinematic. Space exists to isolate title art, separate rows, and keep offer stacks legible against dark backgrounds. The result is a broad, staged rhythm rather than a dense SaaS dashboard. When the UI becomes service-oriented, spacing tightens, but it still avoids clutter through clean column widths and consistent field gaps.

**Elevation & Depth**
Disney+ is primarily a flat-surface system. Most hierarchy comes from alternating dark values such as `{colors.canvas}`, `{colors.surfaceAlt}`, and `{colors.surfaceLow}`, plus border treatment and oversized imagery. Observed form controls and many cards explicitly avoid shadows, and the main browse experience rarely uses tactile card lift.

Where depth does appear, it is more atmospheric than physical. Hero media layers against darker backdrops, sticky regions pin to the viewport, and FAQ or modal surfaces step upward through value rather than box-shadow. The brand therefore reads as screen-based and composited, not paper-like. In practice, if a design needs more prominence, Disney+ typically reaches for a brighter image, stronger border, or more isolated section spacing before it adds shadow.

**Components**
Buttons

`button-primary`
This is the clearest conversion moment in the system: bright `{colors.primary}` with dark text using `{typography.button}` and `{rounded.md}`. It should feel rare and intentional, because Disney+ preserves the impact of cyan by not using it as a background everywhere.

`button-primary-active`
The active variant deepens into `{colors.accentPressed}` and flips to light text. This keeps state changes within the same chromatic family while making commitment feel more final.

`button-secondary-on-dark`
This is the dark utility button seen in login and supporting actions. The `rgba(0,0,0,0.8)` fill, border treatment, and smaller `{typography.utility-button}` keep it functional without competing with the primary CTA.

`button-help-primary`
Support pages use a flatter branded teal button with `{rounded.sm}` and body-sized text. It belongs to a service workflow, so it is less theatrical than the marketing CTA.

Cards & Containers

`hero-stage`
The hero stage is less a card than a full-width canvas. It uses image masking, title art, and dark underlays to set mood, with text centered or aligned according to campaign composition.

`collection-rail-card`
Poster cards are compact, image-first, and minimally embellished. Their main job is to preserve cover art clarity and consistent row rhythm.

`flip-info-card`
Observed on feature and bundle pages, these dark rounded cards package explanatory content into more interactive, comparison-like modules. They are one of the clearer Disney+ product-specific patterns because they turn plan education into a branded content block instead of a generic text card.

`faq-accordion-row`
FAQ rows are broad, dark, and generously padded, using `{rounded.xl}` more than the rest of the system. This is one of the few places where Disney+ allows a softer shape, likely to make repeated disclosure blocks feel easier to scan.

`legal-modal`
Modal disclosures use `{colors.surfaceAlt}` and dense legal copy. The visual language stays within the dark shell but tightens typographic hierarchy to prioritize clarity over spectacle.

Inputs & Forms

`help-form-field`
Help Center fields use `{colors.helpCanvas}`, `{rounded.sm}`, and a straightforward border. This is a clear utility pattern, intentionally closer to enterprise support tooling than to the entertainment shell.

`help-article-shell`
The article shell is the dominant support container: white surfaces, dark text, and generous line-height. It signals “read and resolve” rather than “browse and stream.”

Navigation

`nav-header`
Top navigation is sparse and image-led, with a transparent initial state over hero content and compact uppercase utilities. The logo carries much of the brand signal while supporting actions stay visually restrained.

Pricing

`pricing-comparison-grid`
The pricing grid is one of the most important Disney+ product patterns. It organizes plan differentiation, sticky headers, badges, and offer toggles within a dark matrix, allowing the brand to compare complex bundles without abandoning the cinematic shell.

Signature Components

The most distinctive Disney+ modules are not generic marketing cards but bundle stacks, flip education cards, poster rails, and FAQ slabs. Together they create a recognizable streaming-commerce grammar: watch, compare, choose, confirm, and only then pivot into help.

**Do's and Don'ts**
Do's

- Use `{colors.ink}` and `{colors.canvas}` as the default backdrop for any screen meant to feel like the core streaming product.
- Reserve `{colors.primary}` for strong intent moments such as `button-primary`, active plan states, and high-priority interaction cues.
- Pair `{typography.display}` or `{typography.hero}` with generous dark space so title art and headlines feel staged rather than crowded.
- Use `{rounded.sm}`, `{rounded.md}`, and `{rounded.lg}` for most UI; let `{rounded.xl}` appear mainly in broad FAQ or disclosure containers.
- Build comparison and bundle layouts with `pricing-comparison-grid` logic instead of generic pricing cards.
- Shift to `{colors.helpCanvas}` and `{colors.helpSurface}` when the experience becomes support-heavy, form-heavy, or article-driven.
- Let poster imagery or franchise logos carry emotional tone while text and containers remain disciplined.

Don'ts

- Do not flood backgrounds with `{colors.primary}`; Disney+ uses cyan as punctuation, not as a full-page brand wash.
- Do not replace dark stage surfaces with bright white cards in marketing flows unless the UI is intentionally entering the Help Center mode.
- Do not round everything to pills or soft 20px consumer-app corners; that breaks the architectural feel established by `{rounded.md}` and `{rounded.lg}`.
- Do not depend on heavy drop shadows to create hierarchy; prefer `{colors.surfaceAlt}`, `{colors.surfaceLow}`, borders, and spacing.
- Do not mix playful or handwritten typography with `{typography.display}` and `{typography.body}`; the brand voice is clean, calm, and screen-native.
- Do not turn bundle education into plain text columns when `flip-info-card` and `pricing-comparison-grid` patterns are more brand-accurate.
- Do not use `{colors.helpLink}` or Help Center whites as the main expression for entertainment browse pages.

**Responsive Behavior**
| Breakpoint | Width | Observed Behavior |
|---|---:|---|
| `xs` | 0-440px | Hero art crops aggressively, rails become horizontally scrollable, buttons tighten, legal text stacks. |
| `sm` | 441-768px | Mobile and small-tablet layouts preserve full-width sections and stacked offers. |
| `md` | 769-1024px | More multi-column pricing and image layouts appear; hero copy gains width. |
| `lg` | 1025-1365px | Desktop comparison structures, wider logo art, and more stable rail groupings activate. |
| `xl` | 1366-1599px | Full desktop presentation with larger media crops and more generous section rhythm. |
| `xxl` | 1600px+ | Large-screen hero and media assets use higher-width art variants and broader spacing. |

Touch targets should stay at least 40px high in compact utilities and closer to 48-50px for primary actions, matching the observed login and CTA patterns.

Collapsing strategy:
- Collapse pricing comparisons from full tables into stacked or horizontally navigable plan modules before sacrificing label clarity.
- Convert multi-card rails into swipeable rows on small screens instead of shrinking poster art below recognition.
- Keep hero copy above or centered over media rather than forcing side-by-side layouts too early.
- Tighten padding before reducing type sizes; the Disney+ feel depends more on dark stage rhythm than on oversized copy alone.
- In help flows, stack fields vertically and preserve `{rounded.sm}` field clarity rather than building dense inline forms.

Image behavior:
Hero art uses breakpoint-specific crops and wide responsive sources, often with centered object treatment on large screens and more vertical emphasis on smaller ones. Poster and logo assets should remain crisp, high-contrast, and visually dominant, since Disney+ relies heavily on image recognition as part of the interface identity.

**Iteration Guide**
1. Check the first impression of the screen with the logo hidden. If it no longer reads as a dark streaming environment, push the page back toward `{colors.ink}`, `{colors.canvas}`, and poster-led composition.
2. Audit every use of `{colors.primary}`. If cyan appears on more than the core CTA, selection, or link emphasis moments, the screen is probably over-branded.
3. Validate type hierarchy against `{typography.display}`, `{typography.hero}`, and `{typography.body}`. Disney+ should feel clean and premium, not noisy or editorially eclectic.
4. Review corner usage. If most modules are rounder than `{rounded.lg}`, the result is drifting away from Disney+ and toward a softer consumer app language.
5. Inspect depth. If hierarchy depends on stacked shadows instead of surface contrast between `{colors.canvas}` and `{colors.surfaceAlt}`, flatten the design.
6. For pricing or subscription flows, confirm that the layout behaves like `pricing-comparison-grid` rather than generic promo cards. Disney+ bundle logic is a signature system pattern.
7. For informational or support-heavy moments, verify whether the UI should switch into `{colors.helpCanvas}` and `{colors.helpSurface}`. Keeping everything in the cinematic shell can hurt accuracy.
8. Re-check CTA contrast and button semantics. `button-primary` should remain high-contrast and visually singular, while `button-secondary-on-dark` stays quieter and more utility-driven.

**Known Gaps**
Directly observed:
- Marketing color tokens, core dark surfaces, breakpoints, and the `Inspire` family were observed in fetched Disney+ HTML and CSS.
- Help Center colors, typography, button sizes, field radii, and content width were directly visible in the Help article pages.
- Product patterns such as poster rails, bundle comparisons, FAQ accordions, modals, and login button treatment were visible in the homepage and bundle page markup.

Derived:
- Some semantic token names such as `bundleTeal`, `heroBackdrop`, and `legalGold` are naming abstractions over observed colors rather than literal Disney token labels.
- The spacing scale is synthesized from repeated layout values and utility classes rather than from a single published token table.
- Component names such as `flip-info-card` and `pricing-comparison-grid` are system-friendly labels created to capture repeated UI behavior.

Uncertain:
- Exact hover and pressed values for every marketing control are not uniformly exposed as human-readable design tokens in the downloaded assets.
- Some content modules are campaign-specific and may shift with current promotions, so the structural pattern is more stable than the exact art direction of any one landing page.
- Disney+ likely has additional signed-in product patterns and app-native modules not visible in the public marketing and Help Center pages reviewed here.
