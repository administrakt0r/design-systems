---
version: alpha
name: Arc
slug: arc
source: "https://arc.net/"
extractedAt: "2026-05-22"
description: "Calm future-browser identity with warm off-white canvases, charcoal editorial type, coral pill actions, oversized product screenshots, soft app-like panels, and privacy-first conversational copy."

colors:
  primary: "#25211f"
  accent: "#ff6b57"
  accentHover: "#ef5c49"
  accentPressed: "#d94f3e"
  ink: "#25211f"
  body: "#4d4642"
  muted: "#7c746f"
  canvas: "#faf4ed"
  surface: "#ffffff"
  surfaceAlt: "#f3eee8"
  border: "#e4ddd5"
  borderStrong: "#cfc5bc"
  link: "#5b50d8"
  success: "#2f9f6a"
  warning: "#d58a28"
  error: "#d84d3f"
  signature-coral: "#ff6b57"
  dia-blue: "#3e63f4"
  browser-purple: "#7b61ff"
  browser-pink: "#f174b7"
  browser-mint: "#60cfa7"
  warm-sand: "#faf4ed"
  warm-stone: "#e9dfd4"
  app-sidebar: "#eee8e1"
  app-chrome: "#f7f2ec"
  footerBg: "#211d1b"
  helpCanvas: "#ffffff"
  helpInk: "#1f1f1f"
  helpBorder: "#dddddd"
  on-primary: "#ffffff"
  on-accent: "#ffffff"
  on-dark: "#ffffff"

typography:
  display: { fontFamily: "Inter, SF Pro Display, Helvetica Neue, Arial, sans-serif", fontSize: 84px, fontWeight: 650, lineHeight: 0.98, letterSpacing: "-0.045em" }
  hero: { fontFamily: "Inter, SF Pro Display, Helvetica Neue, Arial, sans-serif", fontSize: 64px, fontWeight: 650, lineHeight: 1.02, letterSpacing: "-0.04em" }
  headline-lg: { fontFamily: "Inter, SF Pro Display, Helvetica Neue, Arial, sans-serif", fontSize: 48px, fontWeight: 650, lineHeight: 1.08, letterSpacing: "-0.035em" }
  title-lg: { fontFamily: "Inter, SF Pro Display, Helvetica Neue, Arial, sans-serif", fontSize: 36px, fontWeight: 650, lineHeight: 1.15, letterSpacing: "-0.03em" }
  title-md: { fontFamily: "Inter, SF Pro Display, Helvetica Neue, Arial, sans-serif", fontSize: 26px, fontWeight: 650, lineHeight: 1.22, letterSpacing: "-0.02em" }
  title-sm: { fontFamily: "Inter, SF Pro Display, Helvetica Neue, Arial, sans-serif", fontSize: 20px, fontWeight: 650, lineHeight: 1.3, letterSpacing: "-0.015em" }
  body: { fontFamily: "Inter, SF Pro Text, Helvetica Neue, Arial, sans-serif", fontSize: 18px, fontWeight: 400, lineHeight: 1.58, letterSpacing: "-0.005em" }
  body-sm: { fontFamily: "Inter, SF Pro Text, Helvetica Neue, Arial, sans-serif", fontSize: 15px, fontWeight: 400, lineHeight: 1.55, letterSpacing: "0em" }
  label: { fontFamily: "Inter, SF Pro Text, Helvetica Neue, Arial, sans-serif", fontSize: 13px, fontWeight: 650, lineHeight: 1.3, letterSpacing: "0.01em" }
  button: { fontFamily: "Inter, SF Pro Text, Helvetica Neue, Arial, sans-serif", fontSize: 16px, fontWeight: 650, lineHeight: 1.2, letterSpacing: "-0.005em" }
  caption: { fontFamily: "Inter, SF Pro Text, Helvetica Neue, Arial, sans-serif", fontSize: 13px, fontWeight: 400, lineHeight: 1.45, letterSpacing: "0em" }
  legal: { fontFamily: "Inter, SF Pro Text, Helvetica Neue, Arial, sans-serif", fontSize: 12px, fontWeight: 400, lineHeight: 1.5, letterSpacing: "0.01em" }
  editorial-quote: { fontFamily: "Inter, SF Pro Display, Helvetica Neue, Arial, sans-serif", fontSize: 40px, fontWeight: 650, lineHeight: 1.12, letterSpacing: "-0.035em" }
  help-title: { fontFamily: "Arial, Helvetica Neue, sans-serif", fontSize: 34px, fontWeight: 700, lineHeight: 1.18, letterSpacing: "-0.02em" }
  help-body: { fontFamily: "Arial, Helvetica Neue, sans-serif", fontSize: 16px, fontWeight: 400, lineHeight: 1.65, letterSpacing: "0em" }
  code: { fontFamily: "SFMono-Regular, Menlo, Consolas, monospace", fontSize: 13px, fontWeight: 500, lineHeight: 1.5, letterSpacing: "0em" }

rounded:
  sm: 6px
  md: 10px
  lg: 16px
  xl: 28px
  pill: 9999px

spacing:
  xs: 4px
  sm: 8px
  md: 16px
  lg: 24px
  xl: 48px
  section: 112px

components:
  button-primary:
    backgroundColor: "{colors.accent}"
    textColor: "{colors.on-accent}"
    typography: "{typography.button}"
    rounded: "{rounded.pill}"
    padding: 15px 24px
  button-primary-active:
    backgroundColor: "{colors.accentPressed}"
    textColor: "{colors.on-accent}"
    rounded: "{rounded.pill}"
  button-dark:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button}"
    rounded: "{rounded.pill}"
    padding: 15px 24px
  button-secondary:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.ink}"
    borderColor: "{colors.border}"
    typography: "{typography.button}"
    rounded: "{rounded.pill}"
    padding: 14px 22px
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.label}"
    rounded: "{rounded.pill}"
    padding: 8px 12px
  button-link-arrow:
    backgroundColor: transparent
    textColor: "{colors.link}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: 0px
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.label}"
    height: 72px
  announcement-strip:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.ink}"
    borderColor: "{colors.border}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.pill}"
    padding: 10px 18px
  hero-product-frame:
    backgroundColor: "{colors.app-chrome}"
    textColor: "{colors.ink}"
    rounded: "{rounded.xl}"
    shadow: "0 34px 90px rgba(37,33,31,0.16), 0 8px 28px rgba(37,33,31,0.08)"
    padding: 12px
  browser-sidebar-panel:
    backgroundColor: "{colors.app-sidebar}"
    textColor: "{colors.body}"
    rounded: "{rounded.lg}"
    padding: 16px
  feature-card:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.ink}"
    borderColor: "{colors.border}"
    rounded: "{rounded.xl}"
    shadow: "0 18px 48px rgba(37,33,31,0.08)"
    padding: 32px
  testimonial-card:
    backgroundColor: "{colors.surfaceAlt}"
    textColor: "{colors.ink}"
    rounded: "{rounded.xl}"
    padding: 28px
  editorial-article:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body}"
    rounded: "{rounded.md}"
    padding: 0px
  help-search-input:
    backgroundColor: "{colors.helpCanvas}"
    textColor: "{colors.helpInk}"
    borderColor: "{colors.helpBorder}"
    typography: "{typography.help-body}"
    rounded: "{rounded.md}"
    padding: 14px 16px
  help-article-card:
    backgroundColor: "{colors.helpCanvas}"
    textColor: "{colors.helpInk}"
    borderColor: "{colors.helpBorder}"
    rounded: "{rounded.md}"
    padding: 20px
  footer:
    backgroundColor: "{colors.footerBg}"
    textColor: "{colors.on-dark}"
    typography: "{typography.caption}"
    padding: 64px 0px
---

**Overview**
Arc's public identity is a warm, editorial product system for a browser that wants to feel calmer than the rest of the internet. The homepage uses generous off-white space, dense but friendly charcoal type, large rounded browser screenshots, and pill-shaped download actions to make a technical product feel personal. Its core visual promise is order: the browser itself is shown as a soft-sided home with a sidebar, spaces, profiles, split views, and privacy copy rather than as a generic web window.

There are three visible modes. The marketing mode is cinematic and product-led, with oversized headlines, warm canvases, and app screenshots treated like hero objects. The content/blog/FAQ mode is more editorial, carrying long-form copy with the same conversational tone and roomy vertical rhythm. The Help Center mode is utilitarian and more Zendesk-like: white surfaces, standard article typography, search/input patterns, breadcrumbs, related-article cards, and practical screenshots.

Key Characteristics:
- Lead with {colors.canvas} and {colors.ink}; Arc should feel warm, quiet, and readable before it feels colorful.
- Use {colors.accent} for the main download or try action, especially in pill buttons.
- Treat product UI as the primary visual asset: browser windows, sidebars, spaces, pinned tabs, split views, and theme panels.
- Keep corners large on product frames and cards; {rounded.xl} is part of the brand's tactile software mood.
- Use short, human copy with big editorial headings rather than dense feature matrices.
- Let color appear as theme-like accents inside browser mockups, not as decorative gradients detached from product behavior.
- Maintain a privacy and calmness tone: generous whitespace, low border contrast, soft depth, and restrained navigation.

**Colors**
Primary & Action

`primary` `{colors.primary}` is the near-charcoal used for core text, dark buttons, and high-authority interface moments. It gives Arc's warm pages enough seriousness to balance the playful browser concept.

`accent` `{colors.accent}` is the signature coral action color used for the strongest download-style CTA. It should appear as a confident, friendly action color rather than a broad background wash.

`accentHover` `{colors.accentHover}` and `accentPressed` `{colors.accentPressed}` are interaction states for the coral family. Use them only on active controls so the base page remains calm.

`link` `{colors.link}` is a cool violet-blue link accent used where text actions need to stand apart from coral purchase/download actions. It pairs well with arrow links and privacy or docs references.

Surfaces

`canvas` `{colors.canvas}` is Arc's warm off-white stage. It is the default marketing background and should carry most page sections, especially around hero copy and product screenshots.

`surface` `{colors.surface}` is the clean white card and panel color. It works best when layered over {colors.canvas} with either a quiet border or soft shadow.

`surfaceAlt` `{colors.surfaceAlt}` is a warmer inset surface for testimonials, muted modules, and secondary panels. It should feel like paper or app chrome, not a disabled gray.

`app-sidebar` `{colors.app-sidebar}` and `app-chrome` `{colors.app-chrome}` represent the browser's own product surfaces. Use them for mock sidebars, tab rails, address areas, and product frames.

Neutrals & Text

`ink` `{colors.ink}` is the default headline and navigation color. Avoid pure black; Arc's writing is direct, but the visual system is intentionally softened.

`body` `{colors.body}` carries explanatory paragraphs and product descriptions. It should contrast clearly on {colors.canvas} while leaving the heavier authority to {colors.ink}.

`muted` `{colors.muted}` supports metadata, captions, bylines, and secondary nav links. Use it for "Updated" labels, testimonial handles, helper text, and footer sublinks.

`border` `{colors.border}` is the standard quiet line for cards, inputs, and navigation separation. `borderStrong` `{colors.borderStrong}` is reserved for table-like help content, dense product diagrams, or strong panel boundaries.

Semantic

`success` `{colors.success}` is suitable for secure, synced, complete, or privacy-safe statuses. Keep it small and UI-like.

`warning` `{colors.warning}` fits notice banners, product availability caveats, or migration messages. It should be used with neutral text rather than as a saturated alert panel.

`error` `{colors.error}` handles destructive states, invalid form fields, and unavailable downloads. It should remain rare in marketing screens.

Brand-specific signatures

`signature-coral` `{colors.signature-coral}` repeats the main action color and is Arc's strongest warm brand accent. Use it for CTA emphasis, small badges, or key product states.

`browser-purple` `{colors.browser-purple}`, `browser-pink` `{colors.browser-pink}`, and `browser-mint` `{colors.browser-mint}` describe Arc's theme-like product colors. They belong inside browser previews, space icons, sidebar themes, and small accents rather than across full marketing sections.

`dia-blue` `{colors.dia-blue}` is present in the current Arc ecosystem through the Dia promotion. Use it only for Dia-related cross-promotion, not as Arc's default action color.

`footerBg` `{colors.footerBg}` closes pages with a warm dark anchor. It should use {colors.on-dark} text and muted link groups rather than bright, high-energy panels.

**Typography**
Arc's marketing typography is best approximated with `Inter` and system Apple fonts. The live site renders in a clean grotesk style with large, tightly tracked display headlines, compact labels, and readable editorial body copy. The Help Center diverges into a more utilitarian support-site stack, so it receives separate help tokens.

| Level | Size | Weight | Line-height | Letter-spacing | Use |
|---|---:|---:|---:|---:|---|
| `display` | 84px | 650 | 0.98 | -0.045em | Very large homepage claims and first-screen brand statements. |
| `hero` | 64px | 650 | 1.02 | -0.04em | Standard hero headlines and major campaign headings. |
| `headline-lg` | 48px | 650 | 1.08 | -0.035em | Feature section headings and strong editorial blocks. |
| `title-lg` | 36px | 650 | 1.15 | -0.03em | FAQ titles, article titles, and large card headings. |
| `title-md` | 26px | 650 | 1.22 | -0.02em | Feature-card titles and module headings. |
| `title-sm` | 20px | 650 | 1.3 | -0.015em | Compact product labels, card headings, and sidebar titles. |
| `body` | 18px | 400 | 1.58 | -0.005em | Marketing paragraphs and editorial page copy. |
| `body-sm` | 15px | 400 | 1.55 | 0em | Nav support text, card descriptions, and secondary copy. |
| `label` | 13px | 650 | 1.3 | 0.01em | Nav items, metadata, badges, and section labels. |
| `button` | 16px | 650 | 1.2 | -0.005em | Primary and secondary CTA labels. |
| `caption` | 13px | 400 | 1.45 | 0em | Handles, dates, image captions, and footer links. |
| `legal` | 12px | 400 | 1.5 | 0.01em | Legal, security, and fine-print text. |
| `editorial-quote` | 40px | 650 | 1.12 | -0.035em | Pull quotes and press-style testimonial moments. |
| `help-title` | 34px | 700 | 1.18 | -0.02em | Help Center article headings. |
| `help-body` | 16px | 400 | 1.65 | 0em | Help Center article paragraphs and instructions. |
| `code` | 13px | 500 | 1.5 | 0em | Keyboard shortcuts, commands, and technical snippets. |

Principles:
- Track large type tightly; Arc headlines should look composed and editorial, not loose or corporate.
- Use semibold rather than extreme bold for marketing headings; the warmth comes from shape and spacing, not heavy type.
- Keep body copy comfortable and conversational with generous line-height.
- Split marketing and support typography: polished product pages use the Arc voice, while help pages prioritize skimmable utility.
- Use monospace only for shortcuts and commands such as `Command-T`, never as a decorative brand texture.

**Layout**
Arc pages use broad centered compositions with a maximum content width around 1120-1240px for marketing sections and a narrower 720-820px reading width for FAQ or blog articles. Hero sections usually stack copy above or beside a large product image, but the product screenshot must remain the visual anchor. Navigation is shallow and relaxed: a compact top bar, simple product/resource links, and prominent download actions.

Spacing scale: {spacing.xs} for tiny icon gaps, {spacing.sm} for label/icon relationships, {spacing.md} for control interiors, {spacing.lg} for card content rhythm, {spacing.xl} for module separation, and {spacing.section} for full marketing sections. Mobile sections can compress to 56-72px vertical padding while preserving clear separation between text, actions, and screenshots.

Whitespace philosophy: Arc uses whitespace as an expression of calm. Do not fill every row with feature cards. Let hero copy breathe, let screenshots sit with room around their shadows, and use low-contrast surfaces to create hierarchy without visual noise.

**Elevation & Depth**
Arc is not flat in the strict sense; it uses depth to make the browser feel like a physical, carefully designed object. The strongest elevation belongs to product frames, especially large browser screenshots, using soft wide shadows such as `0 34px 90px rgba(37,33,31,0.16), 0 8px 28px rgba(37,33,31,0.08)`.

Cards use gentler shadows such as `0 18px 48px rgba(37,33,31,0.08)` or a single {colors.border} keyline. Avoid glassmorphism, neon glow, and exaggerated floating layers. Hierarchy should come from scale, spacing, and product imagery first, then from shadows.

**Components**
Buttons

`button-primary` is the coral pill CTA for download or trial actions. It should appear in short pairs or alone, with enough padding to feel touch-friendly and intentional.

`button-primary-active` is the pressed state of the coral CTA. It deepens color without changing shape, size, or typography.

`button-dark` is the charcoal CTA used when coral would compete with a screenshot or when the action needs a quieter premium tone. It works on warm light canvases and white surfaces.

`button-secondary` is a white pill with a quiet border for paired download choices, platform alternatives, or lower-priority actions. It must look sibling-like to `button-primary`, not like a generic outline button.

`button-ghost` is for top navigation and small utility links. It keeps the same pill geometry but removes visible chrome until interaction.

`button-link-arrow` is an inline text action, typically for privacy, documentation, or learn-more moments. Pair it with a right arrow and do not wrap it in a card.

Cards & Containers

`hero-product-frame` is the signature product screenshot container. It uses {colors.app-chrome}, {rounded.xl}, and the strongest Arc shadow to make the browser window feel substantial.

`browser-sidebar-panel` represents Arc's left-side organization metaphor. Use it for spaces, pinned tabs, profiles, folders, and themed sidebar demos.

`feature-card` is a rounded white panel for product benefits. It should include one clear title, one short paragraph, and either a product screenshot crop or small UI detail.

`testimonial-card` is a warm inset quote surface. It should be text-forward, with a handle or source in {typography.caption}, and should not become a heavily bordered review widget.

`editorial-article` is the long-form content container for blog and FAQ-style pages. It is usually unframed on {colors.canvas}, relying on readable measure and heading rhythm.

Inputs & Forms

`help-search-input` is the main Help Center search/control pattern. It is white, bordered, medium-radius, and utilitarian; keep it more practical than marketing CTAs.

Help forms should use {typography.help-body}, {colors.helpInk}, and {colors.helpBorder}. Error, warning, and success states may use semantic tokens but should remain compact.

Navigation

`nav-bar` is a warm, low-profile top navigation with compact labels and a height around 72px. It should feel like a product header, not an enterprise mega-nav.

`announcement-strip` is used for current cross-product notices, such as the Dia message on the homepage. It is pill-shaped, compact, and should sit above hero content without overpowering it.

`footer` is a dark warm endpoint with grouped links. It should be calmer than the hero and avoid large promotional graphics.

Pricing

No active Arc pricing page was found during extraction. If a pricing module is needed, derive it from `feature-card`, `button-primary`, and `button-secondary` rather than inventing a heavy SaaS pricing table.

Signature Components

Arc's most brand-specific module is the browser-home composition: a large rounded window, a visible sidebar, theme-tinted spaces, and content panes that show Split View, privacy, or organization. This pattern should be used whenever a screen needs to say "Arc" immediately.

The spaces/profiles pattern is another signature: small colored icons or pills grouped in a sidebar to imply different contexts such as work, study, hobbies, and personal browsing. Use {colors.browser-purple}, {colors.browser-pink}, and {colors.browser-mint} as small theme accents inside that structure.

The privacy-comfort module pairs plain-language copy with quiet surfaces, not security theater. Use the link-arrow component for "Learn more about privacy in Arc" style actions.

**Do's and Don'ts**
Do:
- Use {colors.canvas} as the default stage for marketing pages and reserve {colors.surface} for panels.
- Make the first viewport product-led with `hero-product-frame` or a real browser screenshot.
- Use {colors.accent} for one dominant download action per cluster.
- Keep primary controls pill-shaped with {rounded.pill} and {typography.button}.
- Build feature explanations around Arc product metaphors: Spaces, Profiles, Split View, Themes, Little Arc, and privacy.
- Use {typography.display} or {typography.hero} with tight tracking for big claims.
- Let card shadows stay soft and warm, using Arc's product-object depth rather than dramatic elevation.

Don't:
- Do not replace {colors.canvas} with cold gray or pure white across the whole marketing page.
- Do not use {colors.dia-blue} as Arc's primary CTA unless the module is specifically promoting Dia.
- Do not create abstract gradients or decorative blobs; show browser UI instead.
- Do not square off product frames; avoid radii below {rounded.lg} for signature containers.
- Do not make dense SaaS dashboards the default visual metaphor; Arc's UI is a browser home, not an analytics tool.
- Do not set long body copy in {typography.display}; keep editorial reading in {typography.body}.
- Do not stack many bordered cards when one large product screenshot and a short heading can carry the idea.

**Responsive Behavior**
| Breakpoint | Width | Behavior |
|---|---:|---|
| `xs` | 360px | Single-column content, full-width buttons, product frames cropped conservatively. |
| `sm` | 640px | Two-button CTA rows may stay side by side if labels fit; screenshots remain below copy. |
| `md` | 768px | Feature cards can form two-column grids; nav may collapse to a compact menu. |
| `lg` | 1024px | Full hero rhythm, wide product frames, and multi-column testimonials are allowed. |
| `xl` | 1280px | Maximum content width locks; whitespace expands around hero and screenshots. |

Touch targets should be at least 44px high, with primary CTAs closer to 48-52px. Icon-only controls inside browser mockups can be smaller visually, but interactive versions still need accessible hit areas.

Collapsing strategy:
- Collapse navigation into a minimal menu before labels wrap or crowd the download action.
- Stack hero text above product screenshots on mobile and keep the screenshot recognizable, not overly cropped.
- Turn feature-card grids into a single column with {spacing.lg} gaps.
- Preserve the sidebar metaphor inside screenshots by scaling the whole frame rather than hiding the sidebar.
- Keep announcement-strip text short; on mobile it may wrap once but should not become a paragraph.

Images should use real Arc product screenshots or faithful UI mockups. Maintain rounded outer corners, soft shadows, and enough resolution that sidebar labels and browser panes feel tangible.

**Iteration Guide**
1. Check the page background first: if the main marketing canvas is not {colors.canvas}, the screen will likely miss Arc's warmth.
2. Audit the first viewport for a product signal: a browser frame, sidebar, spaces, or download CTA should appear immediately.
3. Confirm the main CTA uses {colors.accent}, {rounded.pill}, and {typography.button}; secondary actions should not compete with it.
4. Review headline tracking and weight: large type should use negative letter-spacing and semibold weight, not extra-bold generic SaaS type.
5. Inspect cards and containers for radius: signature panels should use {rounded.xl} or at least {rounded.lg}.
6. Look for unsupported decoration. Remove ornamental gradients, glass panels, and background shapes that are not tied to product UI.
7. Test mobile screenshots: the Arc sidebar or browser-home idea must remain understandable at 360px.
8. For support pages, switch to help tokens and keep the interface practical with `help-search-input` and `help-article-card`.

**Known Gaps**
Observed directly: the homepage structure and copy, FAQ page, Arc Search blog article, and Help Center Spaces documentation were reviewed. These sources confirmed the brand's warm marketing tone, product-led hero, download CTAs, FAQ/editorial copy, help-center article mode, product concepts, and footer/resource structure.

Derived: exact token values for colors, shadows, radii, and typography were approximated from live page appearance, visible assets, and common system font behavior. Arc does not publish a complete public design-token package on these pages, so this file normalizes the observed system into reusable tokens.

Uncertain: the precise production font name, exact CSS variable names, some responsive breakpoints, and every interactive state are not guaranteed. Pricing-specific components are intentionally absent because no active Arc pricing page was found during extraction.

Research pages used: `https://arc.net/`, `https://arc.net/faq`, `https://arc.net/blog/arc-search`, and `https://resources.arc.net/hc/en-us/articles/19228064149143-Spaces-Distinct-Browsing-Areas`.
