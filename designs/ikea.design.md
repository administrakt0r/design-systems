---
version: alpha
name: IKEA Global
description: "Editorial IKEA global design system: democratic living, bold blue/yellow, flat magazine grid, large lifestyle image cards, and friendly Noto IKEA typography."
colors:
  primary: "#FFDB00"
  accent: "#FFDB00"
  accent-hover: "#F7DA06"
  brand-blue: "#0058A3"
  brand-blue-dark: "#003B7D"
  ink: "#111111"
  text: "#111111"
  muted: "#484848"
  muted-soft: "#818181"
  canvas: "#FFFEFB"
  surface: "#FFFFFF"
  surface-soft: "#F5F5F5"
  border: "#DFDFDF"
  border-strong: "#CCCCCC"
  overlay: "#000000"
  footer: "#000000"
  on-dark: "#FFFFFF"
  success: "#0A8A00"
  warning: "#CA5008"
  error: "#E00751"
  card-blue-wash: "#C4DEE8"
  quiz-green: "#8FB62D"
  product-orange: "#FD600E"
  product-pink: "#FF8AB0"
typography:
  display-xl:
    fontFamily: "Noto IKEA, Noto Sans, Roboto, Open Sans, system-ui, sans-serif"
    fontSize: 72px
    fontWeight: 700
    lineHeight: 1.1
    letterSpacing: "-0.04em"
  display-lg:
    fontFamily: "Noto IKEA, Noto Sans, Roboto, Open Sans, system-ui, sans-serif"
    fontSize: 56px
    fontWeight: 700
    lineHeight: 1.08
    letterSpacing: "-0.029em"
  heading-lg:
    fontFamily: "Noto IKEA, Noto Sans, Roboto, Open Sans, system-ui, sans-serif"
    fontSize: 51px
    fontWeight: 700
    lineHeight: 1.08
    letterSpacing: "-1.48px"
  heading-md:
    fontFamily: "Noto IKEA, Noto Sans, Roboto, Open Sans, system-ui, sans-serif"
    fontSize: 32px
    fontWeight: 700
    lineHeight: 1.15
    letterSpacing: "-0.02em"
  heading-sm:
    fontFamily: "Noto IKEA, Noto Sans, Roboto, Open Sans, system-ui, sans-serif"
    fontSize: 24px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: "-0.01em"
  body-md:
    fontFamily: "Noto IKEA, Noto Sans, Roboto, Open Sans, system-ui, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "Noto IKEA, Noto Sans, Roboto, Open Sans, system-ui, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  label:
    fontFamily: "Noto IKEA, Noto Sans, Roboto, Open Sans, system-ui, sans-serif"
    fontSize: 14px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0
rounded:
  none: 0px
  sm: 4px
  md: 8px
  lg: 12px
  xl: 16px
  circle: 9999px
  pill: 9999px
spacing:
  xs: 4px
  sm: 8px
  md: 16px
  lg: 24px
  xl: 32px
  xxl: 48px
  section: 80px
  page-x: 24px
  container: 1232px
components:
  header:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    height: 96px
  nav-link:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    padding: 16px
  button-shopping:
    backgroundColor: "{colors.accent}"
    textColor: "{colors.ink}"
    rounded: "{rounded.md}"
    padding: 16px
    height: 80px
  button-icon-dark:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    rounded: "{rounded.circle}"
    size: 60px
  button-carousel-secondary:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.ink}"
    rounded: "{rounded.circle}"
    size: 48px
  story-card-image:
    backgroundColor: "{colors.overlay}"
    textColor: "{colors.on-dark}"
    rounded: "{rounded.md}"
  story-card-graphic:
    backgroundColor: "{colors.card-blue-wash}"
    textColor: "{colors.ink}"
    rounded: "{rounded.md}"
  designer-section:
    backgroundColor: "{colors.accent}"
    textColor: "{colors.ink}"
    padding: 64px
  designer-card:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.ink}"
    rounded: "{rounded.md}"
    padding: 24px
  search-input:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.ink}"
    rounded: "{rounded.md}"
    padding: 12px 0 12px 42px
    height: 46px
  cookie-dialog:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.ink}"
    rounded: "{rounded.md}"
    padding: 25px
  footer:
    backgroundColor: "{colors.footer}"
    textColor: "{colors.on-dark}"
    padding: 140px 24px 48px
---

# 1. Source

- URL: https://www.ikea.com
- Date: 2026-05-07
- Page: IKEA global homepage, an international corporate and inspiration portal. The page shows story teasers, collections, designer stories, store/shopping entry, and a global footer. This is not the local product shop but an editorial brand surface.

# 2. Brand DNA

## Visual Identity

IKEA Global combines the iconic brand colours yellow and blue with an almost invisible off-white canvas, black typography, and large, emotional home-living images. The page feels democratic, accessible, and practical: real home situations, picnics, hallways, kitchens, textiles, children/family contexts, designers, and brand history — not luxury staging.

## Layout Principles

- Modular editorial grid with 1232px content width and 24px outer margin.
- Alternates between 2-column story cards, full-width feature cards, and coloured special tiles.
- Cards are large, flat, slightly rounded, and nearly shadowless.
- Hierarchy is created through image size, overlay, yellow surfaces, and section changes — not decorative effects.
- Header is functional and sparse: logo, few links, shopping/store access.

## Mood / Product Feel

Friendly, practical, family-friendly, editorial, optimistic. The product feel is "a better everyday life at home" rather than a premium showcase. IKEA reads as a global system of home, culture, designers, collections, and affordable solutions.

# 3. Semantic Tokens

- accent: #FFDB00 — IKEA yellow for primary CTA surfaces, designer stories band, shopping anchor.
- ink/text: #111111 — primary text, icons, headlines on light/coloured surfaces.
- canvas/background: #FFFEFB — slightly warm white as page background.
- surface/card: #FFFFFF for dialogs, designer cards, search fields; #F5F5F5 as a neutral soft surface.
- border: #DFDFDF — light dividers and controls; #CCCCCC as a stronger line.
- muted text: #484848 and #818181 for footer secondary links, helper text, meta.
- brand-blue: #0058A3 and #003B7D — primarily in the logo/branding, used selectively as interaction or brand context.
- overlay: rgba(0,0,0,0.55) for image card gradients and readability of white titles.
- success: #0A8A00 — from IKEA semantics/CSS.
- warning: #CA5008 — from IKEA semantics/CSS.
- error: #E00751 — from IKEA semantics/CSS.
- content accents: #C4DEE8, #8FB62D, #FD600E, #FF8AB0 — editorial card colours, not the core CTA system.

# 4. Typography

- Primary family: "Noto IKEA", fallback "Noto Sans", Roboto, Open Sans, system-ui, sans-serif.
- Base size: 16px, regular 400, line-height mostly 1.5.
- Large editorial headlines: bold 700, very tight tracking. Observed: H2 51px, weight 700, line-height 55.08px, letter-spacing −1.48px.
- Display scale from CSS: 40/56/72px and responsively also 64/96/144px as large display tokens. Conservatively 72/56/51/32/24px for the preview.
- Label/teaser: 14–16px, often regular or bold, directly above large card titles.
- Tone: short, active, accessible headlines — "Let's eat out!", "Take the quiz!", "A fresh start", "40 years of the IKEA meatball".

# 5. Layout System

- Max-width: 1232px, centred.
- Page padding: 24px left/right.
- Header height: 96px.
- Main grid: 2 columns on desktop, full width for feature cards, 1 column on mobile.
- Card gaps: approx. 16px.
- Vertical story heights: often 517–604px for large rows.
- Section rhythm: large blocks with approx. 80–140px top/bottom spacing; footer starts with 140px top padding.
- Radius: 8px as the standard for cards, search fields, and shopping accordion; round icon buttons at 50%.
- Elevation: almost no shadows. Depth through image contrast, overlays, and layering. The cookie dialog is the only clear overlay surface.

# 6. Components

1. Sticky/global header: 96px tall, off-white, IKEA logo on the left, few nav links.
2. Skip link: accessibility link, visible/focusable, white background, 20px padding.
3. Top nav link: 16px text, 16px padding, black, no pill background.
4. Go shopping CTA: yellow surface, black text, integrated round arrow.
5. Store selector: yellow accordion/dropdown, 80–100px tall, 8px bottom radius.
6. Image story card: full-bleed photo, 8px radius, dark gradient, white meta/headline.
7. Video story card: image/video tile plus black 60px pause/play button bottom right.
8. Graphic story card: illustration surface in light blue/green/red, black typography.
9. Full-width feature card: 1232px wide story, large headline, strong image.
10. Text-image split card: e.g. GREJSIMOJS, light blue surface with text on the left and product image on the right.
11. Quiz CTA card: bright green/yellow full-surface card, short question/CTA.
12. Designer stories section: large yellow band with headline, intro, and carousel.
13. Designer story card: white card on yellow, designer name plus story title.
14. Carousel controls: round buttons — secondary white/light, primary black.
15. Footer: black corporate block, large inverted logo, link lists.
16. Footer primary links: 20px, white, with dot separators.
17. Footer secondary links: 14px, white/grey, legal links.
18. Cookie dialog: white modal surface, 500px wide, 25px padding, 8px radius.
19. Cookie action buttons: accept, reject, cookie settings as a clear decision group.
20. Search input/store picker input: 46px tall, 8px radius, white, search icon offset 42px.
21. Round icon button: 48–60px, black circle, white icon.
22. Content label: small line above card headline, supporting editorial taxonomy.
23. Overlay text stack: bottom left in cards, category + title.
24. Brand logo lockup: blue/yellow in the header, inverted in the footer.
25. Accordion country picker: yellow store surface with expand/collapse behaviour.

# 7. Brand-specific Product Patterns

- IKEA editorial mosaic: the homepage is not a generic feed but an asymmetric story mosaic of home living, collections, history, food, outdoor, and designer culture.
- Yellow commerce island: the shopping entry point is a yellow, dedicated tile/accordion zone — not just a small button.
- Democratic lifestyle cards: products always shown in everyday situations, not as sterile product tiles.
- Dark gradient story titles: white headline on photo with a strong bottom overlay, optimised for widely varying home images.
- Collection naming rhythm: product/collection titles in uppercase or Swedish-inflected names as a visual brand mark — e.g. OMMJÄNGE, STOCKHOLM, SOLUPPGÅNG.
- Designer carousel on yellow: designer storytelling gets IKEA yellow as its own stage.
- Flat utility UI: controls are functional, round, and high-contrast; no complex shadows or glassmorphism.
- Corporate black footer: after colourful inspiration, a radical black global footer with a large logo follows.
- Accessibility visible by default: skip link and clear cookie decisions are visibly part of the UI architecture.

# 8. Motion / Interaction

- Header remains visible when scrolling as a global orientation point, effectively sticky.
- Entire story cards are clickable; cursor/link surfaces cover the full card.
- Video tile uses a round pause button bottom right, likely a play/pause toggle.
- Designer stories uses a horizontal carousel with round back/next buttons.
- Store selection is an accordion/dropdown in the yellow shopping area.
- Cookie dialog offers accept, reject, and settings; modal/overlay-style.
- Expected hover behaviour: nav links underline/darken, card images zoom minimally or intensify the overlay, round buttons invert/lighten. Not fully observed — marked as derived.

# 9. Implementation Notes

## CSS Tokens

```css
:root {
  --ikea-yellow: #FFDB00;
  --ikea-blue: #0058A3;
  --ikea-blue-dark: #003B7D;
  --ink: #111111;
  --canvas: #FFFEFB;
  --surface: #FFFFFF;
  --surface-soft: #F5F5F5;
  --border: #DFDFDF;
  --muted: #484848;
  --overlay: rgba(0,0,0,.55);
  --radius-card: 8px;
  --container: 1232px;
  --gap: 16px;
  --font: "Noto IKEA", "Noto Sans", Roboto, "Open Sans", system-ui, sans-serif;
}
```

## Component Structure

- `IkeaHeader`: Logo, nav, shopping/store picker slot.
- `StoryGrid`: rows with `StoryCard` variants `image`, `video`, `graphic`, `split`, `fullWidth`, `quiz`.
- `StoryCard`: `media`, `overlay`, `eyebrow`, `title`, optional `control`.
- `ShoppingIsland`: yellow CTA surface plus store accordion.
- `DesignerCarousel`: yellow section, intro on the left, `DesignerCard` list on the right, `CarouselControls`.
- `ConsentDialog`: clear three-part actions.
- `IkeaFooter`: black footer with large logo and link groups.

## Do

- Use yellow at large scale and sparingly: CTA/section, not for every minor element.
- Keep cards flat, large, and image-led.
- Use 8px radius and almost no shadows.
- Write short, direct headlines with a friendly tone.
- Use real home/product contexts, not abstract SaaS illustrations.
- Use black round icon buttons as the clear interaction pattern.

## Don't

- No generic SaaS gradients, glassmorphism, or neon glows.
- Do not use blue as the primary surface everywhere — on ikea.com, yellow/off-white dominates; blue is primarily the logo/brand anchor.
- No premium luxury typography or serif display fonts.
- Do not add shadows to every element — IKEA Global is deliberately flat.
- No small product-shop cards as the main pattern when the analysed global page shows an editorial mosaic.

# 10. Accuracy Check

## Directly Observed

- URL, title, and meta description.
- Body font: "Noto IKEA", "Noto Sans", Roboto, "Open Sans", system-ui, sans-serif.
- Canvas #FFFEFB, text #111111, yellow #FFDB00, blue #0058A3, footer #000000.
- Header height 96px, container width 1232px, card rows 517–604px.
- H2: 51px, 700, line-height 55.08px, letter-spacing −1.48px.
- Buttons: yellow store/shopping accordion, black 60px round video button, carousel buttons.
- Inputs: 46px tall, white, 8px radius, 42px icon padding.
- Footer: black block, 140px top padding, link lists, and large logo.
- Story grid with image cards, video, illustration cards, yellow designer stories section.

## Derived

- Full spacing scale from observed values and IKEA CSS tokens.
- Hover and focus behaviour where not checked in tool state.
- Some demo components in the preview abstract copyright-protected photos as colour/pattern cards.
- Product patterns generalised from visible teasers and image alt texts.

## Uncertain

- Exact local shop components from ikea.com/de or other countries were not analysed — this extraction applies to ikea.com Global.
- Exact cookie button styles could only be partially observed, as the consent state/overlay is dynamic.
- Exact image hover animations are not fully verified.

Source: www.designmd-store.com
