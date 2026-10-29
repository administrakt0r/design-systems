---
version: alpha
name: "Next.js"
slug: "nextjs"
source: "https://nextjs.org/"
extractedAt: "2026-05-21"
description: "Developer-first monochrome system with Geist typography, terminal-coded hero moments, hairline borders, pill controls, and a disciplined split between polished launch marketing and dense utility docs."

colors:
  primary: "#111111"
  accent: "#000000"
  accentHover: "#1f1f1f"
  accentPressed: "#2a2a2a"
  ink: "#000000"
  body: "#171717"
  muted: "#666666"
  canvas: "#ffffff"
  surface: "#ffffff"
  surfaceAlt: "#fafafa"
  border: "#e5e5e5"
  borderStrong: "#d4d4d4"
  link: "#111111"
  success: "#067647"
  warning: "#b54708"
  error: "#b42318"
  terminal-bg: "#111111"
  code-bg: "#f6f6f6"
  code-border: "#ebebeb"
  badge-bg: "#f3f3f3"
  spotlight-ring: "#f0f0f0"
  on-primary: "#ffffff"
  on-dark: "#ffffff"

typography:
  display:
    fontFamily: "Geist, ui-sans-serif, system-ui, sans-serif"
    fontSize: 64px
    fontWeight: 600
    lineHeight: 1.05
    letterSpacing: "-0.05em"
  hero:
    fontFamily: "Geist, ui-sans-serif, system-ui, sans-serif"
    fontSize: 48px
    fontWeight: 600
    lineHeight: 1.08
    letterSpacing: "-0.04em"
  headline-lg:
    fontFamily: "Geist, ui-sans-serif, system-ui, sans-serif"
    fontSize: 32px
    fontWeight: 600
    lineHeight: 1.15
    letterSpacing: "-0.03em"
  title-lg:
    fontFamily: "Geist, ui-sans-serif, system-ui, sans-serif"
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: "-0.025em"
  title-md:
    fontFamily: "Geist, ui-sans-serif, system-ui, sans-serif"
    fontSize: 20px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: "-0.02em"
  title-sm:
    fontFamily: "Geist, ui-sans-serif, system-ui, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.35
    letterSpacing: "-0.01em"
  body:
    fontFamily: "Geist, ui-sans-serif, system-ui, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: "-0.01em"
  label:
    fontFamily: "Geist, ui-sans-serif, system-ui, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: "-0.01em"
  button:
    fontFamily: "Geist, ui-sans-serif, system-ui, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.2
    letterSpacing: "-0.01em"
  caption:
    fontFamily: "Geist, ui-sans-serif, system-ui, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.45
    letterSpacing: "0em"
  legal:
    fontFamily: "Geist, ui-sans-serif, system-ui, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.45
    letterSpacing: "0em"
  code:
    fontFamily: "Geist Mono, ui-monospace, SFMono-Regular, monospace"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.55
    letterSpacing: "0em"
  pricing-display:
    fontFamily: "Geist, ui-sans-serif, system-ui, sans-serif"
    fontSize: 40px
    fontWeight: 600
    lineHeight: 1.1
    letterSpacing: "-0.03em"

rounded:
  sm: 8px
  md: 12px
  lg: 14px
  xl: 20px
  pill: 9999px

spacing:
  xs: 4px
  sm: 8px
  md: 12px
  lg: 16px
  xl: 24px
  section: 96px

components:
  button-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button}"
    rounded: "{rounded.pill}"
    padding: "10px 16px"
  button-primary-active:
    backgroundColor: "{colors.accentPressed}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button}"
    rounded: "{rounded.pill}"
    padding: "10px 16px"
  button-secondary:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.body}"
    typography: "{typography.button}"
    rounded: "{rounded.pill}"
    padding: "10px 16px"
  button-ghost:
    backgroundColor: "transparent"
    textColor: "{colors.body}"
    typography: "{typography.button}"
    rounded: "{rounded.pill}"
    padding: "10px 12px"
  button-icon:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.body}"
    typography: "{typography.button}"
    rounded: "{rounded.pill}"
    padding: "8px 10px"
  nav-header:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.label}"
    rounded: "{rounded.pill}"
    padding: "10px 14px"
  nav-search:
    backgroundColor: "{colors.surfaceAlt}"
    textColor: "{colors.muted}"
    typography: "{typography.label}"
    rounded: "{rounded.pill}"
    padding: "10px 14px"
  hero-terminal:
    backgroundColor: "{colors.terminal-bg}"
    textColor: "{colors.on-dark}"
    typography: "{typography.code}"
    rounded: "{rounded.xl}"
    padding: "20px 20px"
  feature-tile:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.body}"
    typography: "{typography.body}"
    rounded: "{rounded.xl}"
    padding: "24px 24px"
  template-card:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.body}"
    typography: "{typography.body}"
    rounded: "{rounded.lg}"
    padding: "16px 16px"
  testimonial-card:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.body}"
    typography: "{typography.body}"
    rounded: "{rounded.xl}"
    padding: "24px 24px"
  docs-sidebar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.label}"
    rounded: "{rounded.sm}"
    padding: "8px 0px"
  docs-topbar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.label}"
    rounded: "{rounded.pill}"
    padding: "10px 14px"
  input-newsletter:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.body}"
    typography: "{typography.body}"
    rounded: "{rounded.pill}"
    padding: "10px 14px"
  code-inline:
    backgroundColor: "{colors.code-bg}"
    textColor: "{colors.body}"
    typography: "{typography.code}"
    rounded: "{rounded.sm}"
    padding: "2px 6px"
  code-block:
    backgroundColor: "{colors.code-bg}"
    textColor: "{colors.body}"
    typography: "{typography.code}"
    rounded: "{rounded.md}"
    padding: "16px 16px"
  release-pill:
    backgroundColor: "{colors.badge-bg}"
    textColor: "{colors.body}"
    typography: "{typography.label}"
    rounded: "{rounded.pill}"
    padding: "6px 10px"
---

**Overview**

Next.js presents itself with unusual restraint for a modern framework brand. The public site is dominated by black, white, and a narrow gray spectrum, but it does not feel sterile. The energy comes from sharp typographic control, code-adjacent UI modules, tiny radii decisions, and repeated terminal or product-demo motifs that tell you this is a tool for builders, not a lifestyle brand. The homepage uses this language to make engineering competence feel aspirational.

There is a clear split between modes. Marketing pages are spacious, centered, and confidence-heavy: oversized headings, capsule CTAs, demo frames, logo walls, testimonials, and release pills. Docs and learning pages keep the same monochrome palette and type families, but switch into a high-density utility mode with a left rail, prominent search, code blocks, version selectors, and many compact navigation rows. The recognizability comes less from color than from discipline: hairline borders, pill geometry, near-black ink, and the ever-present relationship between prose and code.

Key Characteristics:
- Monochrome-first palette built around `{colors.primary}`, `{colors.canvas}`, and subtle gray borders instead of a saturated signature color.
- `Geist` and `Geist Mono` establish a strong editorial-plus-terminal voice without changing families across modes.
- Large negative tracking on hero headlines creates a compressed, technical confidence rather than a soft brand tone.
- CTAs and utility controls both lean on pill shapes, but the site avoids bubbly playfulness by pairing them with strict spacing and flat surfaces.
- Cards rarely rely on heavy elevation; hierarchy comes from spacing, border contrast, and content density.
- Marketing modules often include product-preview frames, terminal snippets, or code-like demonstrations instead of decorative illustration.
- Docs keep the brand intact by using the same quiet palette while increasing navigation density and reducing gesture-heavy ornament.

**Colors**

Primary & Action

- `{colors.primary}` `#111111`: The main action color for dark CTAs and core emphasis. It appears as the most assertive fill on primary buttons and in dark hero or terminal modules.
- `{colors.accent}` `#000000`: Used where Next.js wants maximum contrast and brand authority, especially around logo marks, headline ink, and terminal panels.
- `{colors.accentHover}` `#1f1f1f`: A slight lightening of the black fill used for hover-like dark states rather than a chromatic shift.
- `{colors.accentPressed}` `#2a2a2a`: Pressed or active dark states stay within the same grayscale family, preserving the understated tone.
- `{colors.link}` `#111111`: Links usually behave like strong body ink rather than bright web-blue links, which keeps the brand feeling product-grade and controlled.

Surfaces

- `{colors.canvas}` `#ffffff`: The dominant page background across homepage, learning pages, and docs. White space is a structural material in this system.
- `{colors.surface}` `#ffffff`: Cards and inputs often remain white and are separated from the page through borders or containment rather than tint shifts.
- `{colors.surfaceAlt}` `#fafafa`: Soft alternate surface for search, code-adjacent containers, and gentle panel separation without introducing obvious color.
- `{colors.code-bg}` `#f6f6f6`: A dedicated code surface that makes snippets and command examples feel intentional, not merely boxed.
- `{colors.badge-bg}` `#f3f3f3`: A light capsule background for small pills, metadata chips, and release labels.

Neutrals & Text

- `{colors.ink}` `#000000`: Used for maximum-legibility headlines, logo moments, and dark-on-light brand anchors.
- `{colors.body}` `#171717`: The working text color for paragraphs, medium-emphasis UI labels, and most interface copy.
- `{colors.muted}` `#666666`: Secondary text, help text, low-emphasis navigation items, and placeholder-like search copy.
- `{colors.border}` `#e5e5e5`: The standard divider and control edge. It is critical to the brand because so much hierarchy depends on edges instead of shadow.
- `{colors.borderStrong}` `#d4d4d4`: A firmer boundary for denser modules where the default hairline would disappear.

Semantic

- `{colors.success}` `#067647`: Used conservatively for affirmative system states when needed; Next.js does not make semantic colors a loud part of brand expression.
- `{colors.warning}` `#b54708`: Reserved for cautionary notes, deprecations, or guidance states in utility contexts.
- `{colors.error}` `#b42318`: Error states live in a sober, documentation-friendly red rather than a flashy alarm color.

Brand-specific signatures

- `{colors.terminal-bg}` `#111111`: The terminal-like dark panel is one of the most recognizable non-logo signatures on the site. It reinforces the developer-tool identity more strongly than a colorful accent would.
- `{colors.code-border}` `#ebebeb`: Used to define code modules and quiet frame edges around snippets or demos.
- `{colors.spotlight-ring}` `#f0f0f0`: A very pale outlining tone that supports spotlight or framed demo treatments without visible chrome.

**Typography**

The core families are `Geist, ui-sans-serif, system-ui, sans-serif` for interface and editorial text, and `Geist Mono, ui-monospace, SFMono-Regular, monospace` for commands, inline code, and terminal moments. The system gets most of its brand voice from how these families are used together rather than from variety.

| Level | Token | Family | Size | Weight | Line height | Letter spacing |
|---|---|---|---:|---:|---:|---:|
| Display | `{typography.display}` | Geist | 64px | 600 | 1.05 | -0.05em |
| Hero | `{typography.hero}` | Geist | 48px | 600 | 1.08 | -0.04em |
| Headline Large | `{typography.headline-lg}` | Geist | 32px | 600 | 1.15 | -0.03em |
| Title Large | `{typography.title-lg}` | Geist | 24px | 600 | 1.20 | -0.025em |
| Title Medium | `{typography.title-md}` | Geist | 20px | 600 | 1.25 | -0.02em |
| Title Small | `{typography.title-sm}` | Geist | 16px | 600 | 1.35 | -0.01em |
| Body | `{typography.body}` | Geist | 16px | 400 | 1.60 | -0.01em |
| Label | `{typography.label}` | Geist | 14px | 500 | 1.40 | -0.01em |
| Button | `{typography.button}` | Geist | 14px | 500 | 1.20 | -0.01em |
| Caption | `{typography.caption}` | Geist | 13px | 400 | 1.45 | 0em |
| Legal | `{typography.legal}` | Geist | 12px | 400 | 1.45 | 0em |
| Code | `{typography.code}` | Geist Mono | 14px | 400 | 1.55 | 0em |
| Pricing Display | `{typography.pricing-display}` | Geist | 40px | 600 | 1.10 | -0.03em |

Principles:
- Tight negative tracking is a defining signal on large headings; it makes the brand feel engineered, not airy.
- Weights stay mostly between 400 and 600. Next.js does not rely on extreme black weights to signal importance.
- The same sans family handles both marketing and utility surfaces, which keeps mode shifts coherent.
- Mono is not ornamental. `{typography.code}` appears where the product identity needs to reconnect to the command line or source-level thinking.
- Small text remains clean and quiet; labels and metadata are understated so the layout can carry structure.

**Layout**

The visible spacing rhythm is compact at the component level and generous at the section level. A practical extraction is `{spacing.xs}` 4px, `{spacing.sm}` 8px, `{spacing.md}` 12px, `{spacing.lg}` 16px, `{spacing.xl}` 24px, and `{spacing.section}` 96px. Hero and section wrappers appear to use wide centered containers, typically in the 1200px to 1280px range on desktop, while docs pages allocate a persistent sidebar plus content column rather than a single editorial measure. Grids stay orderly: feature modules use repeated cards or equalized tiles, template listings use image-plus-copy cards, and docs rely on stacked lists with strong alignment rather than masonry or asymmetry.

Whitespace is used surgically. Next.js does not chase luxurious breathing room everywhere; instead, it alternates between broad macro spacing and tightly packed local clusters. That contrast is important: large sections make the brand feel premium, while compact nav rows, search bars, chips, and code blocks keep it unmistakably utilitarian.

**Elevation & Depth**

The depth model is almost flat. Observed hierarchy is created primarily through border lines, surface changes like `{colors.surfaceAlt}`, and the juxtaposition of white canvases against dark demo panels such as `{components.hero-terminal}`. If shadows appear, they are subtle enough to function as optical separation rather than expressive brand signatures. A conservative reconstruction is to treat cards and controls as mostly shadowless, with optional low-strength shadows only for floating search or demo frames.

This matters because Next.js communicates seriousness through restraint. Instead of stacking multiple shadow layers, it uses content framing, radii, and density to tell you what matters. The result feels closer to a polished developer tool than a conventional SaaS marketing page.

**Components**

Buttons

- `{components.button-primary}` is the canonical Next.js CTA: dark fill, white text, pill radius, and compact horizontal padding. It appears in top-level actions like "Get Started" and reads as confident without being loud.
- `{components.button-primary-active}` should stay inside the grayscale family. Do not add blue or glow-based active states; the pressed effect comes from a small value shift, not a stylistic flourish.
- `{components.button-secondary}` carries the same capsule silhouette as primary buttons but swaps emphasis for containment. It is useful beside the primary CTA when both actions need equal geometry but unequal weight.
- `{components.button-ghost}` is how utility links become button-like without visual bulk. It works best in navigation bars, feature toggles, and lightweight adjacent actions.
- `{components.button-icon}` follows the same flat, rounded control logic. Keep icon buttons small, centered, and border- or surface-defined rather than chromatically expressive.

Cards & Containers

- `{components.hero-terminal}` is a signature pattern, not just a dark card. It turns the framework into an executable object by visually echoing a terminal or code console, which is one of the strongest brand-specific modules on the site.
- `{components.feature-tile}` handles the "What's in Next.js?" style of modular explanation. These tiles are orderly, lightly framed, and content-led; they should feel like product capabilities arranged into a grid, not lifestyle cards.
- `{components.template-card}` is smaller and more merchandising-oriented, usually pairing a thumbnail with a short title and summary. It keeps the same disciplined border/radius language but with tighter spacing.
- `{components.testimonial-card}` uses generous padding and quiet structure to let the quote carry the weight. Even social proof stays monochrome and composed.
- `{components.code-block}` and `{components.code-inline}` are part of the core identity because they normalize code as a first-class visual asset. Their backgrounds should be light, clean, and never skeuomorphic.

Inputs & Forms

- `{components.input-newsletter}` is a pill-shaped text field aligned with the rest of the control family. Input styling should feel almost invisible until focus, relying on border clarity and quiet background shifts.
- Docs and learning flows suggest forms that prioritize readability over decorative affordances. Placeholder text should live in `{colors.muted}`, and helper copy should stay in `{typography.caption}`.

Navigation

- `{components.nav-header}` represents the main top navigation language: light background, dark text, compact vertical height, and chip-like containment when needed.
- `{components.nav-search}` is a major recurring pattern because search is central across docs and content. The search field feels like a quiet capsule rather than a boxed enterprise widget.
- `{components.docs-topbar}` adapts the same control language to documentation context with version switching, feedback links, and search access clustered tightly.
- `{components.docs-sidebar}` is intentionally dense and low-drama. The sidebar's visual logic comes from indentation, active row emphasis, and type contrast, not card treatment.

Pricing

- No standalone pricing page was observed on `nextjs.org` during this extraction. Use `{typography.pricing-display}` only if you need to adapt the system to plan or enterprise packaging, and keep it subordinate to the existing monochrome marketing language.

Signature Components

- `{components.release-pill}` captures the small release or metadata capsule used to surface versioned announcements like Next.js 16. It is subtle, neutral, and built for product news rather than promotional urgency.
- The homepage repeatedly uses product-preview frames and capability modules that pair terse labels with technical summaries. When recreating that pattern, favor tight headings, short explanatory lines, and bordered frames over illustration-led storytelling.
- Logo walls and customer proof rows are part of the system's trust language. Keep them monochrome, evenly spaced, and secondary to product explanation.

**Do's and Don'ts**

Do's

- Use `{colors.primary}` and `{components.button-primary}` for the single strongest CTA in a section, then step down to `{components.button-secondary}` for adjacent actions.
- Pair `{typography.display}` or `{typography.hero}` with strong negative tracking so headings feel compressed and technical rather than roomy and editorial-soft.
- Reuse `{components.hero-terminal}` when a module should feel executable, inspectable, or source-driven.
- Let `{colors.border}` and `{colors.borderStrong}` do most of the separation work before introducing any shadow.
- Keep search, filters, and small controls within the pill family defined by `{rounded.pill}` to preserve the site's control vocabulary.
- Use `{typography.code}` with `{colors.code-bg}` for commands, filenames, and API-facing fragments instead of styling them like normal body copy.
- Alternate large section spacing with compact inner clusters so the page feels premium at a macro level and tool-like at a micro level.

Don'ts

- Do not introduce a bright accent color for primary interaction; Next.js recognition depends on monochrome confidence, not chromatic branding.
- Do not swap `{rounded.pill}` for sharp rectangular buttons on marketing surfaces; it breaks one of the system's few soft geometric signatures.
- Do not apply deep card shadows to `{components.feature-tile}` or `{components.template-card}`; use borders and spacing instead.
- Do not loosen headline tracking or increase line height on `{typography.display}` too far, or the voice stops feeling engineered.
- Do not treat links as default browser blue when `{colors.link}` is meant to keep navigation and inline actions inside the neutral ink system.
- Do not make docs navigation feel card-heavy or colorful; `{components.docs-sidebar}` should stay dense, quiet, and scan-first.
- Do not decorate code blocks with gradients, fake terminal chrome, or neon syntax framing unless the source page explicitly shows it.

**Responsive Behavior**

| Breakpoint | Width | Typical shift |
|---|---:|---|
| xs | 0px | Single-column stacking, full-width controls |
| sm | 640px | Slightly wider copy measure, chips can wrap more gracefully |
| md | 768px | Two-column modules begin, navigation gains horizontal space |
| lg | 1024px | Full marketing layouts, richer demo framing, wider content tracks |
| xl | 1280px | Standard desktop max-width for homepage sections |
| 2xl | 1440px | Wider showcase treatment without dramatically increasing text measure |

Touch targets should stay at or above roughly 40px high, with pill buttons and search controls feeling comfortable rather than tiny. The design language survives mobile well because it depends on typography, borders, and capsules more than on intricate multi-column ornament.

Collapsing strategy:
- Collapse multi-column feature grids into a single ordered stack before shrinking card padding aggressively.
- Preserve `{components.nav-search}` prominence on mobile, even if other top-nav items move behind a menu.
- Move supporting chips, metadata, or version controls beneath headings rather than forcing cramped inline layouts.
- Keep `{components.hero-terminal}` readable by reducing line length before reducing font size too far.
- Let docs sidebars become overlays or accordion navigation instead of trying to preserve a compressed permanent rail.

Images and product previews should scale fluidly within rounded frames. Avoid edge-to-edge cropping that removes the clean border language or makes demos feel ornamental rather than functional.

**Iteration Guide**

1. Check that the page reads monochrome-first. If a saturated accent competes with `{colors.primary}` or `{colors.terminal-bg}`, the screen is drifting away from Next.js.
2. Audit hero type against `{typography.display}` or `{typography.hero}` and verify the tracking still feels compressed, not airy.
3. Inspect control geometry: if primary actions, search, and nav chips do not share the capsule logic of `{rounded.pill}`, normalize them.
4. Review separation methods. If you are using shadow before `{colors.border}` and whitespace, flatten the layout.
5. Look for at least one code- or product-execution signal such as `{components.hero-terminal}`, `{components.code-block}`, or a framed product preview.
6. Verify text hierarchy uses weight and spacing more than color. Most labels should stay in `{colors.body}` or `{colors.muted}` rather than introducing new hues.
7. Compare card families. `{components.feature-tile}`, `{components.template-card}`, and `{components.testimonial-card}` should feel related even when their densities differ.
8. Test the docs or utility mode separately from marketing mode and confirm both still feel like the same system because they share type, border, and control tokens.

**Known Gaps**

This extraction is strongest on layout patterns, component families, navigation density, and the overall black-white-gray visual system because those traits were directly observable across the homepage, docs index, installation page, forms guide, learning page, and the `Next.js 16` blog/release content. The existence of a pricing page was specifically checked, and no standalone pricing destination on `nextjs.org` was found during research.

Typography family choice is high-confidence: the site is widely associated with `Geist` and `Geist Mono`, and the visible tone strongly matches that usage. Exact pixel values for every heading size, control height, radius, and semantic color were conservatively derived from the observed visual language rather than extracted from live CSS, because direct stylesheet access was not available in this environment.

Shadow behavior was treated as minimal by design. That is consistent with the observed brand, but any tiny shadow values used in implementation may differ from the flat reconstruction here. Semantic colors for success, warning, and error are included to complete the token system, yet they are not a prominent part of the public brand pages and should be treated as the least certain values in this file.
