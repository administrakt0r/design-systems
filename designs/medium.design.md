---
version: alpha
name: Medium
source: "https://www.medium.com"
date: "2026-05-07"
description: "Editorial publishing system for reading, writing, membership and story discovery. Extracted from the public Medium homepage via Jina text snapshot and the live hero artwork asset; direct browser rendering was blocked by Cloudflare."
colors:
  primary: "#1A8917"
  accent: "#1A8917"
  accent-hover: "#156D12"
  accent-soft: "#E8F3E8"
  ink: "#191919"
  text: "#242424"
  muted: "#6B6B6B"
  muted-soft: "#757575"
  canvas: "#F7F4ED"
  canvas-alt: "#FFFFFF"
  surface: "#FFFFFF"
  surface-warm: "#F2EFE6"
  border: "#E6E6E6"
  border-strong: "#CFCFCF"
  hero-green: "#34AC45"
  hero-moss: "#48704B"
  success: "#1A8917"
  warning: "#B7791F"
  error: "#C94A4A"
  on-accent: "#FFFFFF"
  on-dark: "#FFFFFF"
typography:
  display-xl:
    fontFamily: "GT Super, Georgia, Cambria, Times New Roman, serif"
    fontSize: 106px
    fontWeight: 400
    lineHeight: 0.92
    letterSpacing: "-0.055em"
  display-lg:
    fontFamily: "GT Super, Georgia, Cambria, Times New Roman, serif"
    fontSize: 72px
    fontWeight: 400
    lineHeight: 0.96
    letterSpacing: "-0.045em"
  headline:
    fontFamily: "GT Super, Georgia, Cambria, Times New Roman, serif"
    fontSize: 44px
    fontWeight: 400
    lineHeight: 1.08
    letterSpacing: "-0.035em"
  title-lg:
    fontFamily: "Sohne, Helvetica Neue, Arial, sans-serif"
    fontSize: 24px
    fontWeight: 500
    lineHeight: 1.22
    letterSpacing: "-0.01em"
  title-md:
    fontFamily: "Sohne, Helvetica Neue, Arial, sans-serif"
    fontSize: 18px
    fontWeight: 500
    lineHeight: 1.35
    letterSpacing: "-0.005em"
  body-lg:
    fontFamily: "Sohne, Helvetica Neue, Arial, sans-serif"
    fontSize: 22px
    fontWeight: 400
    lineHeight: 1.32
    letterSpacing: "-0.012em"
  body-md:
    fontFamily: "Sohne, Helvetica Neue, Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.55
    letterSpacing: 0
  body-sm:
    fontFamily: "Sohne, Helvetica Neue, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.45
    letterSpacing: 0
  meta:
    fontFamily: "Sohne, Helvetica Neue, Arial, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.35
    letterSpacing: 0
  button:
    fontFamily: "Sohne, Helvetica Neue, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1
    letterSpacing: 0
rounded:
  none: 0px
  xs: 2px
  sm: 4px
  md: 8px
  lg: 14px
  xl: 24px
  pill: 9999px
spacing:
  xxs: 4px
  xs: 8px
  sm: 12px
  md: 16px
  lg: 24px
  xl: 32px
  xxl: 48px
  section: 84px
  hero: 112px
components:
  top-nav:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    height: 75px
  button-primary:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    typography: "{typography.button}"
    rounded: "{rounded.pill}"
    padding: 11px 20px
    height: 40px
  button-primary-green:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-accent}"
    typography: "{typography.button}"
    rounded: "{rounded.pill}"
    padding: 9px 16px
    height: 36px
  button-primary-green-hover:
    backgroundColor: "{colors.accent-hover}"
    textColor: "{colors.on-accent}"
    rounded: "{rounded.pill}"
  button-secondary:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.ink}"
    typography: "{typography.button}"
    rounded: "{rounded.pill}"
    padding: 10px 18px
    height: 38px
  button-ghost:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button}"
    rounded: "{rounded.pill}"
    padding: 9px 14px
  hero:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.display-xl}"
    padding: 84px 0
  story-card:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.text}"
    typography: "{typography.body-md}"
    rounded: "{rounded.none}"
    padding: 24px 0
  topic-pill:
    backgroundColor: "{colors.surface-warm}"
    textColor: "{colors.text}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.pill}"
    padding: 8px 14px
  membership-card:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    typography: "{typography.title-md}"
    rounded: "{rounded.lg}"
    padding: 28px
  text-input:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.text}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: 12px 0
    height: 44px
---

## 1. Source

- URL: https://www.medium.com
- Date: 2026-05-07
- Description: Public Medium homepage: navigation to Our story, Membership, Write, Sign in, and Get started; hero with headline "Human stories & ideas", sub-line "A place to read, write, and deepen your understanding", CTA "Start reading", and a large green editorial illustration.
- Note on extraction: Direct browser rendering was blocked by Cloudflare. Directly observed were a Jina markdown snapshot of the homepage and the linked hero image from miro.medium.com. Colour and typography tokens are derived from this evidence plus known Medium web conventions and are marked in the Accuracy Check.

## 2. Brand DNA

### Visual Identity
Medium feels like a digital literary and essay newspaper: warm paper, black editorial ink, generous open space, a single green action accent, and an expressive, almost risograph-like illustration. The system is deliberately not "SaaS-glossy". It aims to convey trust, calm, authorship, and editorial depth.

### Layout Principles
- Homepage as an editorial poster: narrow navigation, very large serif headline, clear horizontal dividers.
- Two-tone tension: warm paper canvas against black text and green CTA/artwork accents.
- Content UI is mostly flat: lines, lists, typography, and rhythm instead of shadows.
- Story and feed patterns prioritise author, title, brief metadata, topic, and reading time.

### Mood / Product Feel
Calm, human, literary, cultured, accessible. Medium does not feel like a dashboard — it feels like a publishing house with a simple publishing layer.

## 3. Semantic Tokens

- accent: #1A8917 — Medium green for primary product actions: Follow, Publish, Start reading.
- accent-hover: #156D12 — darker green for hover and pressed.
- ink/text: #191919 / #242424 — near-black editorial ink for logo, headlines, story titles.
- canvas/background: #F7F4ED — warm paper background of the homepage.
- surface/card: #FFFFFF — story surfaces, popovers, forms, feed lists.
- surface-warm: #F2EFE6 — topic pills and light editorial boxes.
- border: #E6E6E6 — hairlines, header border, separation between story rows.
- border-strong: #CFCFCF — active tabs, search/field borders.
- muted text: #6B6B6B / #757575 — author meta, footer, secondary navigation.
- hero-green: #34AC45 — bright green from the hero illustration.
- hero-moss: #48704B — muted moss background from the hero image.
- success: #1A8917; warning: #B7791F; error: #C94A4A — derived for system states, not prominently observed on the homepage.

## 4. Typography

Medium clearly separates brand voice and product UI:

- Display: GT Super-style serif, fallback Georgia/Cambria. Very large, tightly set, with a slight literary contrast. Hero approx. 100–110px on desktop, line-height below 1.
- Story/product UI: Sohne-style grotesque, fallback Helvetica Neue/Arial. Calm, neutral, excellent legibility.
- Hierarchy: hero enormous and serif; subhead large but sans; story titles mostly 18–24px; meta 13–14px; navigation 14px.
- Weight: favours 400 and 500 over heavy bold weights. Medium's presence comes from scale and whitespace, not heaviness.

## 5. Layout System

- Max-width: homepage hero approx. 1192px; documentation/feed container 1120–1200px.
- Grid: hero 2 columns, text on the left approx. 56%, artwork on the right approx. 44%; stacked on mobile.
- Rhythm: large sections 80–112px vertical, header 75px, story rows 24px padding.
- Lines: horizontal 1px borders structure the header, hero end, and footer.
- Radius: product UI uses pills for CTAs/topics, but story lists remain square/line-based.
- Elevation: minimal. Avoid shadows; very soft and sparing on popovers.

## 6. Components

1. Top navigation: warm canvas, 75px height, black wordmark on the left, links on the right, border at the bottom.
2. Wordmark: black Medium logo, flat, no background surface.
3. Nav links: 14px sans, #242424, subtle hover with underline or darker ink.
4. Get started CTA: green pill or black pill depending on context, 36–40px tall.
5. Sign in link: text-based, unobtrusive.
6. Hero headline: enormous serif, tight letter-spacing, line break "Human / stories & ideas".
7. Hero subhead: 22–24px sans, max. 430px wide.
8. Hero CTA: black or green pill with "Start reading".
9. Hero artwork panel: asymmetric green collage, organic flower, geometric lines, speckles.
10. Footer link row: small text links, muted, strongly reduced.
11. Story feed row: title, description, author, reading time, topic, bookmark icon.
12. Author chip: avatar circle, name, publication note, follow link.
13. Topic pill: warm-grey pill, 8/14px padding, 9999 radius.
14. Reading time meta: 13px muted, dot separation.
15. Bookmark icon button: transparent icon button, 32–36px hit box.
16. Clap/response action: monochrome icon + count, muted to active.
17. Membership card: dark or warm box with serif headline and CTA.
18. Search input: very minimal, line or soft border, green focus.
19. Email signup field: 44px tall, text-based, with a pill button beside it.
20. Publish composer bar: white surface, bottom/top border, green publish pill.
21. Tag selector: pill group with warm surface and active border.
22. Dropdown/menu: white surface, 1px border, very light shadow, 8–14px radius.
23. Paywall/membership notice: short editorial callout, accent CTA, minimal decoration.
24. Recommendation module: list layout, compact story titles, small metadata.
25. Footer: no large social icons — only text-based utility links.

## 7. Brand-specific Product Patterns

- Editorial poster hero: one large typographic statement plus artwork, not a SaaS screenshot.
- Read-write-membership triad: navigation and CTAs present reading, writing, and membership as equally valid product paths.
- Story row grammar: author first, then title, then few meta elements. The product trusts text hierarchy over card chrome.
- Warm paper canvas: Medium uses no cold SaaS grey palette — it uses a paper colour that slows reading down in a good way.
- Green as action language: green is not decorative gradient but action-oriented — Start, Follow, Publish, Join.
- Illustration as editorial artifact: the hero image is raw, organic, poster-like — not a generic 3D blob.
- Minimal depth rule: visible structure comes from borders and spacing, not shadows.

## 8. Motion / Interaction

- Buttons: 120–180ms background-color and color; green darkens, black buttons lighten slightly.
- Links: subtle underline or colour change, no strong animations.
- Header: may be sticky; on the Medium homepage typically a clear border and unchanged canvas.
- Cards/rows: story rows stay calm; hover may slightly darken titles/icons but no card-lift effects.
- Forms: focus with a green ring/border, no glow.
- Dropdowns: short opacity/translateY transition, 120ms.

## 9. Implementation Notes

### Concrete CSS Tokens

```css
:root {
  --md-accent: #1A8917;
  --md-accent-hover: #156D12;
  --md-ink: #191919;
  --md-text: #242424;
  --md-muted: #6B6B6B;
  --md-canvas: #F7F4ED;
  --md-surface: #FFFFFF;
  --md-surface-warm: #F2EFE6;
  --md-border: #E6E6E6;
  --md-hero-green: #34AC45;
  --md-hero-moss: #48704B;
  --md-serif: "GT Super", Georgia, Cambria, "Times New Roman", serif;
  --md-sans: "Sohne", "Helvetica Neue", Arial, sans-serif;
  --md-radius-pill: 9999px;
  --md-section: 84px;
}
```

### Component Structure

- `MediumShell`: Sticky nav, main, footer.
- `EditorialHero`: Serif headline, sans subhead, CTA, abstract artwork container.
- `StoryRow`: author meta, title, excerpt, topic pill, reading time, bookmark.
- `TopicRail`: scrollable pill list.
- `MembershipCallout`: dark or warm editorial box.
- `ComposerBar`: publish controls with green action.
- `MinimalForm`: input/textarea/select with green focus border.

### Do

- Use large serif typography as the brand anchor.
- Use warm canvas instead of pure white for homepage/marketing surfaces.
- Treat borders and whitespace as more important than shadows.
- Use CTA green sparingly and semantically.
- Keep story lists text-heavy, calm, and scannable.

### Don't

- No generic gradient heroes or 3D SaaS mockups.
- No heavy shadows around story cards.
- No over-bolded headlines.
- Do not use green for arbitrary decoration.
- Do not round everything — story lists remain editorial-square.

## 10. Accuracy Check

### Directly Observed

- URL and page title: "Medium: Read and write stories."
- Navigation: Sitemap, Our story, Membership, Write, Sign in, Get started.
- Hero text: "Human stories & ideas" and "A place to read, write, and deepen your understanding".
- CTA: "Start reading".
- Footer links: About, Help, Terms, Privacy, Status, Careers, Press, Blog, Rules, Text to speech.
- Hero image: green collage with flower, moss background, black lines/speckles. Colour sampling: approx. #48704B and #34AC45.

### Derived

- Exact typeface names GT Super and Sohne as Medium-typical web fonts; fallbacks are robust.
- Medium green #1A8917 as the primary UI action value.
- Story feed components, author chips, topic pills, bookmark/clap actions derived from Medium product patterns.
- State tokens success/warning/error.

### Uncertain

- Exact live CSS values of the current homepage could not be extracted directly from the rendered page due to Cloudflare.
- Whether the homepage CTA is currently rendered in black or green may vary by test/region; both variants are modelled in the system.
- Exact breakpoints and header sticky behaviour are approximated.

Source: www.designmd-store.com
