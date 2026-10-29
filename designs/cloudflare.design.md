---
version: alpha
name: Cloudflare
slug: cloudflare
source: "https://www.cloudflare.com/"
extractedAt: "2026-05-19"
description: "Internet-infrastructure brand system led by Cloudflare orange, taut grotesk typography, pale technical surfaces, slim borders, tiny radii, and diagrammatic product modules that make networking feel fast, precise, and industrial rather than soft SaaS."

colors:
  primary: "#ff5e1f"
  accent: "#ff7038"
  accentHover: "#ff7038"
  accentPressed: "#d63c01"
  ink: "#171717"
  body: "#262626"
  muted: "#737373"
  canvas: "#ffffff"
  surface: "#fdfdfc"
  surfaceAlt: "#f9f7f6"
  border: "#f0f0f0"
  borderStrong: "#f0e3de"
  link: "#ff5e1f"
  success: "#00bd7d"
  warning: "#ff9910"
  error: "#ff3008"
  footerBg: "#151414"
  footerSurface: "#191817"
  footerInk: "#f0e3de"
  signature-coral: "#ff5e1f"
  signature-coral-bright: "#ff7038"
  product-compute: "#0a95ff"
  product-ai: "#00bd7d"
  product-blue: "#4b73ff"
  warm-hairline: "#f0e3de20"
  on-primary: "#171717"
  on-dark: "#fafafa"

typography:
  display:
    fontFamily: "\"FT Kunst Grotesk\", sans-serif"
    fontSize: 64px
    fontWeight: 500
    lineHeight: 0.99
    letterSpacing: "-0.025em"
  hero:
    fontFamily: "\"FT Kunst Grotesk\", sans-serif"
    fontSize: 56px
    fontWeight: 500
    lineHeight: 0.99
    letterSpacing: "-0.025em"
  headline-lg:
    fontFamily: "\"FT Kunst Grotesk\", sans-serif"
    fontSize: 56px
    fontWeight: 500
    lineHeight: 1
    letterSpacing: "-0.025em"
  title-lg:
    fontFamily: "\"FT Kunst Grotesk\", sans-serif"
    fontSize: 48px
    fontWeight: 500
    lineHeight: 1
    letterSpacing: "-0.025em"
  title-md:
    fontFamily: "\"FT Kunst Grotesk\", sans-serif"
    fontSize: 32px
    fontWeight: 500
    lineHeight: 1
    letterSpacing: "-0.025em"
  title-sm:
    fontFamily: "\"FT Kunst Grotesk\", sans-serif"
    fontSize: 24px
    fontWeight: 500
    lineHeight: 1.2
    letterSpacing: "-0.025em"
  body:
    fontFamily: "\"FT Kunst Grotesk\", sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.2
    letterSpacing: "-0.0025em"
  body-relaxed:
    fontFamily: "\"FT Kunst Grotesk\", sans-serif"
    fontSize: 15px
    fontWeight: 400
    lineHeight: 1.75
    letterSpacing: "-0.0025em"
  label:
    fontFamily: "\"FT Kunst Grotesk\", sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.15
    letterSpacing: "-0.01em"
  button:
    fontFamily: "\"FT Kunst Grotesk\", sans-serif"
    fontSize: 16px
    fontWeight: 500
    lineHeight: 1.2
    letterSpacing: "-0.01em"
  caption:
    fontFamily: "\"FT Kunst Grotesk\", sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: "0em"
  legal:
    fontFamily: "\"FT Kunst Grotesk\", sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: "0em"
  code:
    fontFamily: "\"Apercu Mono Pro\", monospace"
    fontSize: 10px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: "0em"
  docs-display:
    fontFamily: "system-ui, sans-serif"
    fontSize: 42px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: "0em"

rounded:
  sm: 3px
  md: 8px
  lg: 12px
  xl: 16px
  pill: 9999px

spacing:
  xs: 4px
  sm: 8px
  md: 16px
  lg: 24px
  xl: 40px
  section: 96px

components:
  button-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button}"
    rounded: "{rounded.lg}"
    padding: "12px 20px"
  button-primary-active:
    backgroundColor: "{colors.accentPressed}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.lg}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button}"
    rounded: "{rounded.lg}"
    padding: "12px 20px"
  button-ghost:
    backgroundColor: "transparent"
    textColor: "{colors.ink}"
    typography: "{typography.button}"
    rounded: "{rounded.lg}"
    padding: "12px 20px"
  button-dark:
    backgroundColor: "{colors.footerBg}"
    textColor: "{colors.on-dark}"
    typography: "{typography.button}"
    rounded: "{rounded.lg}"
    padding: "12px 20px"
  button-pricing-pill:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.body}"
    typography: "{typography.label}"
    rounded: "{rounded.pill}"
    padding: "6px 12px"
  hero-card:
    backgroundColor: "{colors.canvas}"
    borderColor: "{colors.border}"
    rounded: "{rounded.sm}"
    shadow: "none"
    padding: "24px"
  feature-card:
    backgroundColor: "{colors.surface}"
    borderColor: "{colors.border}"
    rounded: "{rounded.md}"
    shadow: "0 1px 3px rgba(0,0,0,0.08)"
    padding: "24px"
  pricing-card:
    backgroundColor: "{colors.canvas}"
    borderColor: "{colors.border}"
    rounded: "{rounded.sm}"
    shadow: "none"
    padding: "24px"
  pricing-chip:
    backgroundColor: "{colors.surfaceAlt}"
    borderColor: "{colors.borderStrong}"
    rounded: "{rounded.md}"
    padding: "4px 10px"
  nav-shell:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    borderColor: "{colors.border}"
    rounded: "0px"
    padding: "16px 24px"
  nav-dropdown:
    backgroundColor: "{colors.canvas}"
    borderColor: "{colors.border}"
    rounded: "{rounded.md}"
    shadow: "0 1px 3px rgba(0,0,0,0.08)"
    padding: "16px"
  input-default:
    backgroundColor: "{colors.canvas}"
    borderColor: "{colors.border}"
    textColor: "{colors.body}"
    typography: "{typography.body}"
    rounded: "{rounded.md}"
    padding: "10px 14px"
  footer-shell:
    backgroundColor: "{colors.footerBg}"
    textColor: "{colors.footerInk}"
    borderColor: "{colors.warm-hairline}"
    rounded: "0px"
    padding: "48px 24px"
  product-pill:
    backgroundColor: "{colors.surfaceAlt}"
    borderColor: "{colors.borderStrong}"
    textColor: "{colors.body}"
    rounded: "{rounded.pill}"
    padding: "6px 12px"
  network-diagram-module:
    backgroundColor: "{colors.canvas}"
    borderColor: "{colors.primary}"
    rounded: "{rounded.sm}"
    shadow: "none"
    padding: "16px"
---

**Overview**

Cloudflare's visual identity is a mix of industrial infrastructure branding and polished product marketing. The system is led by `{colors.primary}` `#ff5e1f`, but the orange is not used like a soft consumer accent; it is deployed as a sharp operational signal against quiet warm-white surfaces, thin borders, and dense information modules. The result feels fast, exact, engineered, and a little physical, almost like schematics translated into marketing UI.

There are at least three visible modes. The marketing mode is expressive: oversized grotesk headlines, orange keylines, and hero compositions built from product diagrams and modular tiles. The pricing and product mode is more tabular and comparative, using cards, pills, segmented tabs, and fine borders to make complex offerings scannable. The docs mode shifts into a more utility-driven shell with system-facing typography, darker neutrals, search-first navigation, and stronger reading rhythms, but it still inherits the orange accent and disciplined spacing logic.

What makes the brand recognizable is not just the orange. It is the combination of tight headline tracking, small radii, pale surfaces, sparse shadows, and diagram-like product modules that imply network paths, protection layers, and edge locations. Even when the UI is dense, it avoids looking cluttered because the hierarchy comes from scale, contrast, and modular repetition rather than decorative effects.

Key Characteristics:

- Use `{colors.primary}` as a decisive signal color, not a wash across the whole interface.
- Pair big, tightly tracked grotesk headlines with restrained body copy in `{typography.body}`.
- Favor tiny to medium corners such as `{rounded.sm}` and `{rounded.md}` over plush SaaS rounding.
- Build hierarchy with modules, borders, and layout rhythm instead of heavy shadow stacks.
- Let pale warm surfaces and hairline borders create the "technical paper" backdrop.
- Treat product visuals as network schematics: chips, lanes, cards, nodes, and comparative panels.
- Keep dark mode or footer zones dense and warm rather than glossy or neon.

**Colors**

Primary & Action

- `{colors.primary}` `#ff5e1f` is the core Cloudflare orange. It drives primary buttons, important links, highlighted numbers, diagram edges, and key product callouts.
- `{colors.accent}` `#ff7038` is the brighter hover state and secondary orange highlight. It appears where the brand needs a little more energy without changing hue families.
- `{colors.accentPressed}` `#d63c01` is the pressed or dark-accent orange used in active states and darker orange fields. It keeps interactions feeling crisp rather than washed out.
- `{colors.link}` `#ff5e1f` doubles as the text-link color on marketing surfaces, reinforcing that navigation and action belong to the same signal family.

Surfaces

- `{colors.canvas}` `#ffffff` is the default page ground for the marketing site. It gives the system a bright, open field where orange can carry most of the emphasis.
- `{colors.surface}` `#fdfdfc` is a near-white utility surface used for cards, pricing plates, and contained panels that need separation without obvious tint.
- `{colors.surfaceAlt}` `#f9f7f6` is a warmer alternate plane. It supports chips, pricing comparators, and subtle background shifts that feel material rather than gray.
- `{colors.footerBg}` `#151414` is the primary dark surface. It appears in footer and dark-section contexts where the brand becomes denser and more infrastructural.
- `{colors.footerSurface}` `#191817` is a nearby dark step used when dark sections need layering without large tonal jumps.

Neutrals & Text

- `{colors.ink}` `#171717` is the strongest dark text and interface ink. It is used for high-emphasis headings and control labels.
- `{colors.body}` `#262626` is the working text color for paragraphs, data labels, and default UI copy. It is softer than `{colors.ink}` but still firm.
- `{colors.muted}` `#737373` is the subdued neutral for helper text, secondary metadata, and less prominent labels.
- `{colors.border}` `#f0f0f0` is the cool, clean hairline border used on many cards and shells in light contexts.
- `{colors.borderStrong}` `#f0e3de` is the warmer border tone that appears in places where Cloudflare wants a slightly more branded, paper-like edge.
- `{colors.warm-hairline}` `#f0e3de20` is a translucent warm divider used especially in dark regions and subtle separators.
- `{colors.footerInk}` `#f0e3de` keeps text in dark sections warm rather than pure white, which helps the brand avoid harsh contrast.

Semantic

- `{colors.success}` `#00bd7d` appears for AI/product success and positive status accents. It is vivid but narrow in use, functioning as a product lane rather than a replacement brand color.
- `{colors.warning}` `#ff9910` is used sparingly for cautionary or highlighted operational states.
- `{colors.error}` `#ff3008` is a saturated failure or alert red-orange. Its proximity to the brand hue makes it feel native to the system.

Brand-specific signatures

- `{colors.signature-coral}` and `{colors.signature-coral-bright}` formalize the orange pair that makes Cloudflare recognizable at a glance.
- `{colors.product-compute}` `#0a95ff` and `{colors.product-blue}` `#4b73ff` are used as product-lane colors for compute, networking, and docs-side accents. They broaden the system without diluting the orange-led brand.
- `{colors.product-ai}` `#00bd7d` marks AI and smart-platform moments, usually as a lane or badge rather than a full-surface theme.
- `{colors.on-primary}` `#171717` is notable: many orange buttons use dark text instead of white, which preserves edge clarity and keeps the orange bright.
- `{colors.on-dark}` `#fafafa` is reserved for dark backgrounds, but Cloudflare often warms surrounding text with `{colors.footerInk}` to avoid a cold, stark dark mode.

**Typography**

Cloudflare's marketing system uses `"FT Kunst Grotesk", sans-serif` as its main voice, with an alternate override path for `"STK Bureau Sans", sans-serif`. The docs environment shifts closer to system UI typography for reading utility, while code uses `"Apercu Mono Pro", monospace`.

| Token | Family | Size | Weight | Line-height | Letter-spacing |
|---|---|---:|---:|---:|---:|
| `{typography.display}` | FT Kunst Grotesk | 64px | 500 | 0.99 | -0.025em |
| `{typography.hero}` | FT Kunst Grotesk | 56px | 500 | 0.99 | -0.025em |
| `{typography.headline-lg}` | FT Kunst Grotesk | 56px | 500 | 1.00 | -0.025em |
| `{typography.title-lg}` | FT Kunst Grotesk | 48px | 500 | 1.00 | -0.025em |
| `{typography.title-md}` | FT Kunst Grotesk | 32px | 500 | 1.00 | -0.025em |
| `{typography.title-sm}` | FT Kunst Grotesk | 24px | 500 | 1.20 | -0.025em |
| `{typography.body}` | FT Kunst Grotesk | 16px | 400 | 1.20 | -0.0025em |
| `{typography.body-relaxed}` | FT Kunst Grotesk | 15px | 400 | 1.75 | -0.0025em |
| `{typography.label}` | FT Kunst Grotesk | 14px | 500 | 1.15 | -0.01em |
| `{typography.button}` | FT Kunst Grotesk | 16px | 500 | 1.20 | -0.01em |
| `{typography.caption}` | FT Kunst Grotesk | 13px | 400 | 1.50 | 0em |
| `{typography.legal}` | FT Kunst Grotesk | 12px | 400 | 1.50 | 0em |
| `{typography.code}` | Apercu Mono Pro | 10px | 700 | 1.30 | 0em |
| `{typography.docs-display}` | system-ui | 42px | 600 | 1.20 | 0em |

Principles:

- Track display copy tightly. The recurring `-0.025em` is central to the brand's compressed, infrastructural tone.
- Keep headline weights moderate rather than black. Most large titles sit at `500`, which feels precise instead of loud.
- Split reading modes by context: grotesk for brand marketing, system UI for docs, mono for compact technical labels.
- Let body copy breathe through line-height shifts, not big size jumps. Marketing body is compact, editorial and docs copy becomes more relaxed.
- Use medium-weight labels and buttons to sharpen controls without resorting to all-caps branding everywhere.

**Layout**

The visible spacing scale centers on `{spacing.xs}` `4px`, `{spacing.sm}` `8px`, `{spacing.md}` `16px`, `{spacing.lg}` `24px`, and `{spacing.xl}` `40px`, with major section padding around `{spacing.section}` `96px` on desktop. Repeated utility classes and modules suggest a max-width around `1200px` for standard content regions, while some hero blocks stretch wider to approximately `1080px` for headline content. Grid behavior is modular: single-column on small screens, then quick transitions into two-, three-, or twelve-column arrangements for feature and pricing surfaces.

Whitespace is disciplined rather than luxurious. Cloudflare does not rely on huge empty voids; instead it uses consistent gutters, repeated card padding, and strong block segmentation to make dense information readable. Even large hero sections tend to be structured as grouped modules, lanes, and plates rather than free-floating copy.

**Elevation & Depth**

Cloudflare is mostly flat. The dominant depth model is border-led rather than shadow-led, and many marketing cards use `shadow: none` or only a minimal `0 1px 3px rgba(0,0,0,0.08)` treatment. This keeps the interface feeling engineered and diagrammatic instead of tactile or app-store glossy.

When depth appears, it is subtle and usually serves containment, not drama. Hierarchy comes from orange keylines, alternating pale surfaces, scale changes, and nested modules. Dark sections and animated product visuals sometimes add glow-like effects around orange beams or activity states, but those are product storytelling devices, not general UI chrome.

**Components**

Buttons

- `{components.button-primary}` is a warm orange CTA with dark text, medium weight typography, and a rounded rectangle shape. It appears in the global nav, hero CTAs, and pricing actions where Cloudflare wants a decisive but still technical call to action.
- `{components.button-primary-active}` deepens the orange rather than switching hue. The darker active state reinforces firmness and keeps interaction feedback within the brand range.
- `{components.button-secondary}` is usually a white or pale-surface companion with dark text and the same general geometry as the primary button. It is used beside primary CTAs so comparison happens through fill, not shape.
- `{components.button-ghost}` strips the fill away and relies on typography plus layout position. It works best in nav and contextual action clusters where Cloudflare wants low-friction secondary movement.
- `{components.button-dark}` appears in dark sections and footer-like zones. It preserves the same general proportions while switching to `{colors.on-dark}` to keep continuity across visual modes.
- `{components.button-pricing-pill}` is a smaller capsule used for category selection, plan segmentation, or compact control states. This is more utility chip than hero CTA.

Cards & Containers

- `{components.hero-card}` is the baseline story module: white ground, hairline border, tiny corner, and zero drama. It lets diagrams, metrics, and labels do the expressive work.
- `{components.feature-card}` adds a little more separation through `{colors.surface}` and a restrained shadow. It is still crisp, but more contained for educational or explainer content.
- `{components.pricing-card}` is intentionally austere because pricing tables already carry a lot of information. The system avoids plush card styling so value comparison remains the focus.
- `{components.pricing-chip}` is the compact feature or tag unit inside pricing contexts. Warm borders keep it from feeling generic gray.

Inputs & Forms

- `{components.input-default}` follows the same pattern as the broader system: light surface, subtle border, medium-tight radius, no heavy inset styling. Inputs are utilitarian and do not become expressive brand moments.
- Search and lightweight filters in docs reinforce this restrained approach. Interaction is communicated via border and background shift more than fill-heavy focus treatments.

Navigation

- `{components.nav-shell}` is a clean horizontal frame with direct typography and strong CTA placement. The nav's personality comes from content density and orange action emphasis, not ornamental background treatment.
- `{components.nav-dropdown}` turns product and solution categories into structured panels with light borders and compact spacing. These dropdowns read like product maps or control centers rather than lifestyle menus.
- `{components.footer-shell}` flips the palette into warm dark mode while keeping the same modular logic. Dense link columns and quiet dividers make the footer feel infrastructural.

Pricing

- `{components.pricing-card}` and `{components.button-pricing-pill}` are core to Cloudflare's comparison mode. The pricing system depends on segmented tabs, side-by-side plan panels, and compact badges that break large product matrices into scannable chunks.
- `{components.pricing-chip}` is especially important because Cloudflare sells technical capability, not only tiers. Small bordered chips help summarize features without becoming colorful badges everywhere.

Signature Components

- `{components.product-pill}` packages product families and attributes into slim rounded chips. These reinforce the catalog-like nature of Cloudflare's platform.
- `{components.network-diagram-module}` is the most brand-specific pattern. Across homepage and product storytelling, Cloudflare uses bordered rectangles, linked nodes, beam lines, chips, and layered mini-panels to visualize traffic flow, protection, routing, and edge execution.
- Diagram clusters often combine `{rounded.sm}` corners, orange edge details, and pale blocks. That geometry is a key reason generated work can look authentically Cloudflare rather than broadly "enterprise SaaS."

**Do's and Don'ts**

Do's

- Use `{colors.primary}` for the single most important action in a region, then let `{colors.canvas}` and `{colors.surface}` carry everything else.
- Set major marketing headlines in `{typography.display}` or `{typography.hero}` with the tight tracking intact.
- Prefer `{rounded.sm}` and `{rounded.md}` on cards and modules so layouts stay technical and compact.
- Separate dense content with `{colors.border}` or `{colors.borderStrong}` before reaching for shadow.
- Build product storytelling with `{components.network-diagram-module}` patterns: nodes, chips, flow lanes, and bordered plates.
- Use `{components.button-pricing-pill}` and `{components.pricing-chip}` for segmentation and taxonomy instead of oversized tabs.
- Warm dark sections with `{colors.footerBg}` and `{colors.footerInk}` rather than pure black and stark white.

Don'ts

- Do not flood whole screens with `{colors.primary}`; Cloudflare uses orange as a signal, not as a blanket background.
- Do not replace `{typography.display}` with ultra-bold geometric sans styles; the brand voice depends on medium-weight grotesk tension.
- Do not round containers beyond `{rounded.lg}` for standard marketing UI; big soft pills quickly break the industrial feel.
- Do not stack large blurred shadows under cards; most Cloudflare hierarchy is flat and border-led.
- Do not turn all metadata into colorful badges. Save `{colors.product-compute}`, `{colors.product-blue}`, and `{colors.product-ai}` for real product-lane meaning.
- Do not use cool gray-only dividers where `{colors.borderStrong}` would better preserve the warm paper-like undertone.
- Do not make docs screens visually identical to marketing pages; the docs mode should remain more utilitarian and search-oriented.

**Responsive Behavior**

| Breakpoint | Approx. width | Behavior |
|---|---:|---|
| `xs` | 0px | Single-column stack, compressed hero modules |
| `sm` | 640px | Buttons begin wrapping into stable CTA rows |
| `md` | 768px | Multi-column cards and pricing blocks start appearing |
| `lg` | 1024px | Global nav and richer product matrices settle into desktop layout |
| `xl` | 1280px | Standard marketing max-widths and full comparison structures |
| `2xl` | 1536px | Wide hero compositions and diagram breathing room |

Touch targets should stay at or above `44px` height even when the visual chrome is small. Cloudflare's controls can look compact, but tappable areas should remain generous beneath the disciplined styling.

Collapsing strategy:

- Collapse pricing comparisons from full matrices into stacked plan cards before shrinking typography.
- Turn multi-column feature regions into one-column modular plates while preserving each plate's internal padding.
- Reduce hero diagrams by removing peripheral decorative modules first, not by shrinking key labels below body-legibility.
- Keep CTA pairs intact by wrapping them to a second line rather than converting them into tiny adjacent buttons.
- Simplify nav exploration into drawers or accordions, but preserve the categorized product-map logic.

Images and diagrams should scale responsively with `max-width: 100%` and usually maintain contained framing rather than aggressive crop. Product visuals are informative modules, so preserving internal labels and node relationships matters more than edge-to-edge drama.

**Iteration Guide**

1. Check whether the primary action really deserves `{colors.primary}`. If multiple orange buttons compete in one region, the screen will stop feeling Cloudflare.
2. Audit the headline voice against `{typography.display}` or `{typography.hero}`. If tracking loosens or weights jump too heavy, the brand tone becomes generic enterprise.
3. Review every card corner against `{rounded.sm}`, `{rounded.md}`, and `{rounded.lg}`. If the UI starts looking pillowy, pull the radii back.
4. Remove gratuitous shadow and see whether `{colors.border}` plus surface contrast can carry the hierarchy instead. Usually it can.
5. Inspect neutral balance: body copy should sit in `{colors.body}`, not maximum black, and dark sections should lean on `{colors.footerInk}` rather than pure white everywhere.
6. Verify that dense product areas use `{components.product-pill}`, `{components.pricing-chip}`, or `{components.network-diagram-module}` patterns instead of generic icon cards.
7. Compare spacing rhythm against `{spacing.md}`, `{spacing.lg}`, and `{spacing.section}`. Cloudflare feels structured when modules repeat disciplined padding values.

**Known Gaps**

This extraction is strong on directly observed brand patterns from the live homepage, a live product page, the live pricing page, and a live Cloudflare docs page fetched on 2026-05-19. The orange family, dark footer palette, main font stack, alternate font override path, mono font, several type tokens, surface relationships, radii, and multiple component patterns were observed directly in delivered HTML and bundled CSS.

Some values are normalized for DESIGN.md usefulness rather than copied one-for-one from every variant in the production site. Cloudflare's shipped CSS contains multiple contextual theme branches, including dark mode, product-lane colors, docs-side theme tokens, and internal Kumo variables. Where many neighboring values existed, I selected the most stable public-facing roles rather than exhaustively listing every variant.

The docs experience clearly uses a different shell and token namespace from the marketing site, likely from a docs framework layer. Its exact typography and semantic colors are partially derived from the delivered docs CSS and partially summarized at the role level so the final file remains one coherent design system reference instead of two unrelated token dumps.

I did not treat transient animation glows, experimental campaign visuals, or every product-specific subtheme as core brand tokens unless they repeated across pages. If a future task needs a deeper extraction of only Cloudflare Docs or only the dashboard/product-app side, that should be documented as a separate mode-specific system.
