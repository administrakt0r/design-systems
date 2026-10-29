---
version: alpha
name: GitHub
slug: github
source: "https://github.com/"
extractedAt: "2026-05-31"
description: "Developer-native platform identity built from black-and-white GitHub brand contrast, Mona Sans typography, Primer UI density, green CTAs, blue product links, Octicon language, bordered cards, code surfaces, and contribution-grid patterns."

colors:
  primary: "#1f883d"
  accent: "#0969da"
  accentHover: "#0860ca"
  accentPressed: "#0550ae"
  ink: "#1f2328"
  body: "#59636e"
  muted: "#818b98"
  canvas: "#ffffff"
  surface: "#f6f8fa"
  surfaceAlt: "#f0f3f6"
  border: "#d1d9e0"
  borderStrong: "#818b98"
  link: "#0969da"
  success: "#1a7f37"
  warning: "#9a6700"
  error: "#d1242f"
  brandBlack: "#000000"
  brandWhite: "#ffffff"
  marketingInk: "#0d1117"
  marketingMuted: "#8b949e"
  darkCanvas: "#0d1117"
  darkSurface: "#161b22"
  darkSurfaceAlt: "#21262d"
  darkBorder: "#30363d"
  githubGreen: "#2da44e"
  githubGreenHover: "#2c974b"
  githubGreenPressed: "#298e46"
  githubBlue: "#0969da"
  githubPurple: "#8250df"
  githubPink: "#bf3989"
  githubOrange: "#bc4c00"
  githubYellow: "#bf8700"
  contributionNone: "#ebedf0"
  contributionLow: "#9be9a8"
  contributionMedium: "#40c463"
  contributionHigh: "#30a14e"
  contributionMax: "#216e39"
  codeBg: "#0d1117"
  codeText: "#c9d1d9"
  diffAddBg: "#dafbe1"
  diffDeleteBg: "#ffebe9"
  focusRing: "#0969da"
  on-primary: "#ffffff"
  on-dark: "#ffffff"

typography:
  display: { fontFamily: "Mona Sans, Hubot Sans, -apple-system, BlinkMacSystemFont, Segoe UI, sans-serif", fontSize: 80px, fontWeight: 800, lineHeight: 1.0, letterSpacing: "-0.04em" }
  hero: { fontFamily: "Mona Sans, Hubot Sans, -apple-system, BlinkMacSystemFont, Segoe UI, sans-serif", fontSize: 64px, fontWeight: 800, lineHeight: 1.0, letterSpacing: "-0.035em" }
  headline-lg: { fontFamily: "Mona Sans, Hubot Sans, -apple-system, BlinkMacSystemFont, Segoe UI, sans-serif", fontSize: 48px, fontWeight: 800, lineHeight: 1.08, letterSpacing: "-0.03em" }
  title-lg: { fontFamily: "Mona Sans, -apple-system, BlinkMacSystemFont, Segoe UI, sans-serif", fontSize: 32px, fontWeight: 700, lineHeight: 1.18, letterSpacing: "-0.02em" }
  title-md: { fontFamily: "Mona Sans, -apple-system, BlinkMacSystemFont, Segoe UI, sans-serif", fontSize: 24px, fontWeight: 600, lineHeight: 1.25, letterSpacing: "-0.012em" }
  title-sm: { fontFamily: "Mona Sans, -apple-system, BlinkMacSystemFont, Segoe UI, sans-serif", fontSize: 20px, fontWeight: 600, lineHeight: 1.3, letterSpacing: "-0.006em" }
  body: { fontFamily: "Mona Sans, -apple-system, BlinkMacSystemFont, Segoe UI, sans-serif", fontSize: 16px, fontWeight: 400, lineHeight: 1.5, letterSpacing: "0em" }
  body-lg: { fontFamily: "Mona Sans, -apple-system, BlinkMacSystemFont, Segoe UI, sans-serif", fontSize: 20px, fontWeight: 400, lineHeight: 1.5, letterSpacing: "-0.005em" }
  label: { fontFamily: "Mona Sans, -apple-system, BlinkMacSystemFont, Segoe UI, sans-serif", fontSize: 14px, fontWeight: 600, lineHeight: 1.43, letterSpacing: "0em" }
  button: { fontFamily: "Mona Sans, -apple-system, BlinkMacSystemFont, Segoe UI, sans-serif", fontSize: 14px, fontWeight: 600, lineHeight: 1.43, letterSpacing: "0em" }
  caption: { fontFamily: "Mona Sans, -apple-system, BlinkMacSystemFont, Segoe UI, sans-serif", fontSize: 12px, fontWeight: 400, lineHeight: 1.33, letterSpacing: "0em" }
  legal: { fontFamily: "Mona Sans, -apple-system, BlinkMacSystemFont, Segoe UI, sans-serif", fontSize: 12px, fontWeight: 400, lineHeight: 1.5, letterSpacing: "0em" }
  nav: { fontFamily: "Mona Sans, -apple-system, BlinkMacSystemFont, Segoe UI, sans-serif", fontSize: 16px, fontWeight: 600, lineHeight: 1.5, letterSpacing: "0em" }
  pricing-display: { fontFamily: "Mona Sans, Hubot Sans, -apple-system, BlinkMacSystemFont, Segoe UI, sans-serif", fontSize: 48px, fontWeight: 800, lineHeight: 1.05, letterSpacing: "-0.03em" }
  code: { fontFamily: "ui-monospace, SFMono-Regular, SF Mono, Menlo, Consolas, Liberation Mono, monospace", fontSize: 13px, fontWeight: 400, lineHeight: 1.54, letterSpacing: "0em" }

rounded:
  sm: 4px
  md: 6px
  lg: 8px
  xl: 12px
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
    { backgroundColor: "{colors.primary}", textColor: "{colors.on-primary}", typography: "{typography.button}", rounded: "{rounded.md}", padding: 8px 16px }
  button-primary-active:
    { backgroundColor: "{colors.githubGreenPressed}", textColor: "{colors.on-primary}", rounded: "{rounded.md}" }
  button-secondary:
    { backgroundColor: "{colors.surface}", textColor: "{colors.ink}", borderColor: "{colors.border}", typography: "{typography.button}", rounded: "{rounded.md}", padding: 7px 16px }
  button-secondary-on-dark:
    { backgroundColor: transparent, textColor: "{colors.on-dark}", borderColor: "rgba(255,255,255,0.35)", typography: "{typography.button}", rounded: "{rounded.md}", padding: 8px 16px }
  button-ghost:
    { backgroundColor: transparent, textColor: "{colors.ink}", typography: "{typography.button}", rounded: "{rounded.md}", padding: 8px 12px }
  button-link:
    { backgroundColor: transparent, textColor: "{colors.link}", typography: "{typography.button}", rounded: "{rounded.sm}", padding: 0px }
  input-search:
    { backgroundColor: "{colors.canvas}", textColor: "{colors.ink}", borderColor: "{colors.border}", typography: "{typography.body}", rounded: "{rounded.md}", padding: 8px 12px }
  nav-marketing:
    { backgroundColor: "{colors.brandBlack}", textColor: "{colors.on-dark}", typography: "{typography.nav}", height: 72px }
  nav-product:
    { backgroundColor: "{colors.canvas}", textColor: "{colors.ink}", borderColor: "{colors.border}", typography: "{typography.label}", height: 64px }
  hero-dark:
    { backgroundColor: "{colors.darkCanvas}", textColor: "{colors.on-dark}", rounded: 0px, padding: 96px 0px }
  hero-light:
    { backgroundColor: "{colors.canvas}", textColor: "{colors.ink}", rounded: 0px, padding: 96px 0px }
  feature-card:
    { backgroundColor: "{colors.canvas}", textColor: "{colors.ink}", borderColor: "{colors.border}", rounded: "{rounded.xl}", padding: 24px }
  dark-feature-card:
    { backgroundColor: "{colors.darkSurface}", textColor: "{colors.on-dark}", borderColor: "{colors.darkBorder}", rounded: "{rounded.xl}", padding: 24px }
  code-panel:
    { backgroundColor: "{colors.codeBg}", textColor: "{colors.codeText}", typography: "{typography.code}", rounded: "{rounded.lg}", padding: 16px }
  repo-card:
    { backgroundColor: "{colors.canvas}", textColor: "{colors.ink}", borderColor: "{colors.border}", rounded: "{rounded.md}", padding: 16px }
  pricing-card:
    { backgroundColor: "{colors.canvas}", textColor: "{colors.ink}", borderColor: "{colors.border}", rounded: "{rounded.xl}", padding: 24px }
  contribution-grid:
    { backgroundColor: "{colors.canvas}", emptyColor: "{colors.contributionNone}", lowColor: "{colors.contributionLow}", mediumColor: "{colors.contributionMedium}", highColor: "{colors.contributionHigh}", maxColor: "{colors.contributionMax}", rounded: "{rounded.sm}" }
  octicon:
    { color: "{colors.body}", size: 16px, strokeWidth: 2px }
  footer:
    { backgroundColor: "{colors.canvas}", textColor: "{colors.body}", borderColor: "{colors.border}", typography: "{typography.caption}", padding: 48px 0px }
---

**Overview**
GitHub's visual identity is an operating environment for developers before it is a decorative marketing brand. The public site moves between stark black-and-white brand moments, dense Primer UI surfaces, and product screenshots that look like real software instead of illustration. Its most recognizable signals are the Octocat mark, Mona Sans headlines, Octicons, green action buttons, blue links, compact bordered modules, code windows, contribution grids, and a preference for showing repositories, issues, diffs, workflows, and security panels as the proof of the story.

The brand has three visible modes. Marketing pages use {colors.brandBlack}, {colors.brandWhite}, oversized high-weight type, sweeping section rhythm, and dramatic product composites. Product and pricing pages become lighter and more tabular, using {colors.canvas}, {colors.surface}, 1px borders, cards, comparison rows, and restrained CTAs. Docs and product UI are pure Primer: compact typography, blue links, gray surfaces, monospaced code, focus outlines, and predictable application spacing.

Key Characteristics:
- Lead with {colors.ink} or {colors.on-dark} type; avoid generic saturated marketing palettes.
- Use {colors.primary} for committed actions and {colors.link} for navigation, docs, and product links.
- Build identity through real developer artifacts: code panels, repo cards, diffs, Actions timelines, and contribution grids.
- Keep surfaces mostly flat, separated by 1px borders from {colors.border} and modest radius from {rounded.md}.
- Use Octicons as the native icon language, aligned to labels and status metadata.
- Reserve vivid purple, pink, orange, and yellow accents for product storytelling, not base UI chrome.
- Let the grid feel engineered: wide max-width containers, regular gutters, and dense information rows.

**Colors**
Primary & Action

`primary` `{colors.primary}` is the primary committed-action green. It appears on sign-up, trial, and "get started" buttons and should feel practical rather than ornamental.

`githubGreen` `{colors.githubGreen}` is the broader GitHub green family used in button systems and positive product messaging. Its hover and pressed partners keep the CTA readable while preserving the same saturated product tone.

`accent` `{colors.accent}` and `link` `{colors.link}` are GitHub's core blue interaction colors. They carry text links, docs navigation, issue references, repository metadata, and selected product links.

`accentHover` `{colors.accentHover}` and `accentPressed` `{colors.accentPressed}` deepen the blue for hover, active, and focused states. Use them for interaction feedback, not static decoration.

Surfaces

`canvas` `{colors.canvas}` is the default page and card ground in light mode. GitHub often lets white dominate, then uses borders and gray panels to create structure.

`surface` `{colors.surface}` is the familiar Primer gray used for secondary panels, input backgrounds, table headers, and page bands. It makes product UI feel lightweight and scannable.

`surfaceAlt` `{colors.surfaceAlt}` is a slightly stronger gray for nested regions, hover rows, and comparison-table subdivisions. Use it where a white card needs another layer without adding a shadow.

`darkCanvas` `{colors.darkCanvas}`, `darkSurface` `{colors.darkSurface}`, and `darkSurfaceAlt` `{colors.darkSurfaceAlt}` create the dark marketing and code environment. They should be paired with {colors.on-dark}, {colors.codeText}, and quiet dark borders.

Neutrals & Text

`ink` `{colors.ink}` is the primary text color for product UI and light pages. It is softer than pure black, so it can support dense UI without harsh contrast.

`body` `{colors.body}` is the paragraph and metadata color. It carries explanatory copy, card descriptions, table text, and subdued labels.

`muted` `{colors.muted}` is for secondary timestamps, captions, placeholder text, and disabled-looking detail. Keep important copy out of this token unless the size is generous.

`border` `{colors.border}` is one of the most important GitHub tokens. It defines cards, tables, inputs, split panes, nav dividers, pricing cards, and repo modules.

`borderStrong` `{colors.borderStrong}` supports heavier separators, disabled borders, and table rules that need more presence.

Semantic

`success` `{colors.success}` appears in checks, merged states, workflow success, and positive status. It should be compact and functional.

`warning` `{colors.warning}` is GitHub's operational amber for review, billing, security, and caution states. Use it with short labels and icon support.

`error` `{colors.error}` is for destructive actions, failed checks, deleted diff context, and critical validation. It should not be used as a decorative red.

Brand-specific signatures

`brandBlack` `{colors.brandBlack}` and `brandWhite` `{colors.brandWhite}` are the clearest GitHub brand pair. They frame home-page hero work, major launches, and moments where the Octocat identity needs to feel iconic.

`githubPurple` `{colors.githubPurple}` and `githubPink` `{colors.githubPink}` support Copilot, AI, and expressive feature storytelling. They should be accents around product scenes, not replacements for the green or blue action system.

`githubBlue` `{colors.githubBlue}` reinforces product navigation, docs links, and repository references. Treat it as GitHub's utility accent, especially in product-native pages.

`githubOrange` `{colors.githubOrange}` and `githubYellow` `{colors.githubYellow}` work best for warnings, package/security emphasis, and small visual annotations. They should appear as badges, icons, or tiny chart accents.

`contributionNone` through `contributionMax` are the contribution-graph greens. They are uniquely GitHub and should be used when visualizing activity, cadence, participation, or developer momentum.

`codeBg` `{colors.codeBg}` and `codeText` `{colors.codeText}` are the code panel defaults for marketing snippets and docs. They create immediate developer recognition when paired with monospaced type.

`diffAddBg` `{colors.diffAddBg}` and `diffDeleteBg` `{colors.diffDeleteBg}` belong to code-review storytelling. Use them when representing pull requests, review history, changed files, or merge confidence.

**Typography**
GitHub uses Mona Sans and Hubot Sans as its brand-facing family, then falls back to the system stack for performance and product consistency. Product UI can feel almost system-native, but marketing pages become recognizably GitHub through very heavy, tightly tracked headlines. Code uses the standard GitHub monospace stack: `ui-monospace`, `SFMono-Regular`, `SF Mono`, `Menlo`, `Consolas`, `Liberation Mono`, and `monospace`.

| Level | Size | Weight | Line height | Letter spacing |
|---|---:|---:|---:|---:|
| display | 80px | 800 | 1.0 | -0.04em |
| hero | 64px | 800 | 1.0 | -0.035em |
| headline-lg | 48px | 800 | 1.08 | -0.03em |
| title-lg | 32px | 700 | 1.18 | -0.02em |
| title-md | 24px | 600 | 1.25 | -0.012em |
| title-sm | 20px | 600 | 1.3 | -0.006em |
| body-lg | 20px | 400 | 1.5 | -0.005em |
| body | 16px | 400 | 1.5 | 0em |
| nav | 16px | 600 | 1.5 | 0em |
| label | 14px | 600 | 1.43 | 0em |
| button | 14px | 600 | 1.43 | 0em |
| caption | 12px | 400 | 1.33 | 0em |
| pricing-display | 48px | 800 | 1.05 | -0.03em |
| code | 13px | 400 | 1.54 | 0em |

Principles:
- Track display type negatively; GitHub hero type is tight, heavy, and confident.
- Keep product text unshowy: 16px body, 14px labels, and 12px captions are normal Primer territory.
- Let weight create hierarchy before introducing color; headings are often black or white, not rainbow.
- Use code typography as a content layer, not just as decoration.
- Align icons and labels on a compact baseline so navigation and metadata read like real developer tooling.

**Layout**
GitHub pages use a broad responsive container, usually around 1280px for marketing layouts and narrower readable measures for docs and articles. The spacing scale is simple: {spacing.xs} for icon gaps, {spacing.sm} for compact controls, {spacing.md} for card internals, {spacing.lg} for module spacing, {spacing.xl} for large card and grid rhythm, and {spacing.section} for hero or major band padding.

Grid behavior is pragmatic. Marketing pages use 12-column or bento-style layouts with large product visuals spanning multiple columns. Product, pricing, and docs pages switch to table, sidebar, and card grids with dense rows. Cards rarely float far from the page; they sit in a rational system of gutters and keylines.

Common layout measurements:
- Marketing content usually caps around 1280px with generous side padding.
- Docs and editorial reading measures should stay narrower so long technical paragraphs do not sprawl.
- Product UI screenshots can bleed wider than the text column when they are the main proof.
- Card grids normally collapse from 3 or 4 columns to 2 columns and then 1 column.
- Sidebar layouts should preserve navigation hierarchy before preserving decorative art.

Whitespace philosophy: GitHub uses whitespace to make complex developer content navigable, not luxurious. Large empty areas appear around hero statements, but as soon as the page becomes product proof, spacing tightens around screenshots, cards, comparison tables, and documentation blocks.

**Elevation & Depth**
GitHub is mostly flat. Hierarchy comes from contrast, border, typography, spacing, and real product screenshots rather than heavy elevation. In product UI, {colors.border} and {colors.surface} do most of the work.

Use shadows sparingly: a modal, dropdown, hover popover, or marketing screenshot may use a soft shadow such as `0 8px 24px rgba(140,149,159,0.20)`. Feature cards, repo cards, pricing cards, and code panels should usually rely on a 1px border and radius from {rounded.md} or {rounded.xl}.

Dark marketing scenes create depth through layered dark surfaces, glowing code contrast, and product composites. Avoid glassmorphism, frosted panels, and decorative blur unless a live GitHub page shows that exact launch treatment.

**Components**
Buttons

`button-primary` is the green GitHub commitment button. Use it for sign-up, trial, and primary conversion actions; keep it rectangular with {rounded.md}, not pill-shaped.

`button-primary-active` uses the pressed green state for active interaction only. It should not be used as a static secondary shade.

`button-secondary` is a bordered gray or white button for product UI, pricing comparisons, and neutral actions. It pairs with {colors.ink} text and {colors.border} keylines.

`button-secondary-on-dark` is the dark-hero outline button. It lets a secondary CTA sit beside a green or white primary without adding another fill color.

`button-ghost` and `button-link` are for nav, docs, repo actions, and inline flows. The link version should feel like GitHub text navigation, often supported by an arrow or Octicon.

Cards & Containers

`hero-dark` is the iconic GitHub launch and home-page mode: black canvas, white type, green or white action, and product artifacts emerging from the dark.

`hero-light` is used for pricing, docs-adjacent, and utility marketing pages. It feels clearer and more operational, with {colors.ink} headlines and direct comparison structures.

`feature-card` is a white, bordered, rounded card for marketing features, integrations, and product modules. It should contain real UI fragments, diagrams, or concise copy.

`dark-feature-card` sits inside dark marketing bands. Use {colors.darkSurface}, {colors.darkBorder}, and restrained accent marks so the card still feels like GitHub.

`repo-card` is a product-native module representing repositories, issues, packages, or projects. It should include metadata rows, icons, language dots, stars, checks, or timestamps where appropriate.

`code-panel` is central to the brand. Use dark background, monospace text, small syntax accents, and enough padding to read like a real code window.

Repo-like containers should prefer short rows and explicit metadata over big generic descriptions. A viewer should be able to recognize the object type immediately from its icon, title, status, and secondary text.

Code, terminal, and diff modules can be cropped as marketing artifacts, but the crop should keep meaningful line numbers, command prompts, or status labels. Abstract code texture alone is weaker than real UI evidence.

Inputs & Forms

`input-search` represents GitHub's search and form fields. It uses {colors.canvas}, {colors.border}, {rounded.md}, and 16px body type, with a clear {colors.focusRing} state.

Forms should be compact and direct. Labels sit close to fields, helper text uses {typography.caption}, and validation uses semantic colors plus text rather than color alone.

Navigation

`nav-marketing` is dark, high-contrast, and brand-forward. It often carries the Octocat mark, product menu groups, search, sign-in, and sign-up.

`nav-product` is lighter and utility-driven. It uses keylines, compact labels, tabs, breadcrumbs, and search behavior aligned to Primer.

`octicon` is the native icon component. Use Octicons for repos, branches, issues, pull requests, checks, code, stars, security, packages, and workflow concepts.

Pricing

`pricing-card` is a bordered comparison container with strong plan names, pricing-display numbers, and dense feature lists. It should feel like a product decision table, not a lifestyle card.

Pricing layouts need clear free/team/enterprise separation, consistent checkmarks, and restrained CTA hierarchy. Green is for the desired commitment; bordered buttons support secondary plan paths.

Signature Components

`contribution-grid` is one of GitHub's most recognizable visual patterns. Use it for activity, consistency, community, or work history, with square cells and the green intensity ramp.

Repository, code, diff, Actions, and security modules should look like slices of the product. The more a marketing page can use authentic UI structure, the more GitHub it feels.

AI and Copilot sections can use {colors.githubPurple} and {colors.githubPink} accents, but the surrounding UI should still be Primer-based: code panels, chat-like surfaces, repo context, and clear buttons.

Actions storytelling should include checks, job rows, status dots, terminal logs, and compact timestamps. Keep the visual logic operational, because GitHub's automation story is about confidence and traceability.

Security storytelling should use alerts, shield icons, dependency rows, and review status rather than generic lock imagery. It should feel like a maintained repository surface.

**Do's and Don'ts**
Do:
- Use {colors.brandBlack} and {colors.brandWhite} for high-impact GitHub hero moments.
- Use {colors.primary} for primary CTAs and keep them at {rounded.md}.
- Use {colors.link} for docs, product references, issue links, and inline navigation.
- Separate dense modules with {colors.border} before reaching for shadows.
- Place Octicons beside repository, code, workflow, and security labels.
- Show real developer artifacts: code, pull requests, diffs, checks, and contribution patterns.
- Use {typography.code} for snippets and commands, even in marketing contexts.
- Use the contribution-grid colors only as square activity cells or close derivatives.

Don't:
- Do not turn GitHub into a soft pastel SaaS palette; the base system is black, white, gray, green, and blue.
- Do not make primary CTAs pill-shaped; {rounded.md} is the safer GitHub button radius.
- Do not use large decorative gradients as the only hero visual; product UI should carry the brand.
- Do not replace Octicons with generic line icons when a GitHub concept exists.
- Do not use heavy drop shadows on repo cards, pricing cards, or docs panels.
- Do not make body copy lighter than {colors.body} on white for important content.
- Do not use {colors.githubPurple} as the universal accent; reserve it for Copilot or launch storytelling.
- Do not round cards beyond {rounded.xl} unless matching a specific screenshot treatment.

**Responsive Behavior**
| Breakpoint | Width | Behavior |
|---|---:|---|
| compact | 320px | Single column, collapsed nav, full-width CTAs, simplified screenshots |
| phone | 480px | Preserve readable code with horizontal scroll or cropped panels |
| tablet | 768px | Two-column cards may appear; nav remains condensed where needed |
| laptop | 1012px | Product sidebars, pricing columns, and multi-card rows become stable |
| desktop | 1280px | Full marketing grid, wide hero composites, and comparison tables |
| wide | 1440px | Keep content capped; expand background art and product composites only |

Touch targets should be at least 44px tall on mobile, even when desktop buttons use compact Primer sizing. Inputs and nav controls need visible focus states and enough horizontal padding for thumb use.

Collapsing strategy:
- Collapse marketing navigation into a menu while preserving sign-in and sign-up priority.
- Stack hero copy above product visuals; do not let code panels become unreadably tiny.
- Convert pricing columns to stacked cards with plan CTAs repeated per card.
- Keep code panels horizontally scrollable when line wrapping would destroy syntax meaning.
- Turn dense comparison tables into grouped feature sections with clear headings.

Images and screenshots should remain semantically exact. Use real product UI crops, repository panels, terminal/code scenes, and workflow diagrams. Avoid generic developer stock photos unless the page is explicitly editorial.

For mobile, keep the GitHub mark, primary CTA, and menu access visible before secondary nav groups. Marketing product composites may crop horizontally, but critical UI labels should remain readable or be replaced by a simplified mobile-specific crop.

**Iteration Guide**
1. Check whether the first viewport clearly reads as GitHub through {colors.brandBlack}, {colors.brandWhite}, Mona Sans weight, Octocat or Octicon language, and real product UI.
2. Verify every CTA: primary actions use {colors.primary}, secondary actions use borders, and inline navigation uses {colors.link}.
3. Audit card construction: most cards should have {colors.canvas}, {colors.border}, and {rounded.md} or {rounded.xl}, with minimal shadow.
4. Confirm typography hierarchy: display and hero levels are tight and heavy, while product labels remain compact at 14px.
5. Look for at least one authentic developer artifact on feature screens: repo card, code panel, diff, issue, pull request, workflow, or contribution grid.
6. Ensure dark sections use {colors.darkCanvas} and {colors.darkSurface} rather than generic navy or purple backgrounds.
7. Test mobile screenshots and code panels so they crop, scroll, or stack without shrinking below useful reading size.
8. Review accent colors: purple, pink, orange, and yellow should support product stories or semantic states, not replace the main interaction system.

**Known Gaps**
Observed directly: GitHub homepage, Actions feature page, pricing page, GitHub Docs, Primer Brand, Primer Product UI, and the GitHub Brand Toolkit were used to triangulate the visual system. The strongest observations are color roles, Primer surface behavior, navigation density, code panels, pricing-card logic, and contribution-grid usage.

Coverage notes:
- Homepage and feature pages informed the marketing, dark-hero, and product-composite guidance.
- Pricing and docs informed the comparison-card, form, table, and compact navigation guidance.

Derived: Exact token names and component groupings in this file are normalized for the DESIGN.md format rather than copied one-to-one from Primer. Some marketing hero sizes are approximated from current GitHub page behavior and Primer Brand scale because responsive typography changes by viewport.

Uncertain: GitHub.com frequently changes launch imagery, Copilot treatments, and home-page hero compositions. The core system remains stable, but campaign-specific gradients, illustrations, and screenshot assemblies should be rechecked for any exact recreation.

Also uncertain: exact production typography can vary by page bundle, user agent, and rollout. The values here prioritize GitHub Brand and Primer behavior over page-specific experiments.

Sources: [GitHub homepage](https://github.com/), [GitHub Actions](https://github.com/features/actions), [GitHub pricing](https://github.com/pricing), [GitHub Docs](https://docs.github.com/), [Primer Product UI](https://primer.style/product/), [Primer Brand](https://primer.style/brand/), [GitHub Brand Toolkit](https://brand.github.com/).
