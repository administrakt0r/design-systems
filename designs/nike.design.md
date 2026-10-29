---
version: alpha
name: Nike.com Retail Editorial
description: Monochrome, image-led performance commerce system with Nike Futura display, Helvetica Now utility typography, full-bleed campaign modules and flat product grids.
colors:
  primary: "#111111"
  secondary: "#707072"
  neutral: "#F5F5F5"
  accent: "#111111"
  accentInverse: "#FFFFFF"
  ink: "#111111"
  canvas: "#FFFFFF"
  canvasMuted: "#F5F5F5"
  surface: "#FFFFFF"
  surfaceMuted: "#F5F5F5"
  surfaceImageFallback: "#E5E5E5"
  border: "#E5E5E5"
  borderStrong: "#CACACB"
  mutedText: "#707072"
  subtleText: "#9E9EA0"
  statusNew: "#9E3500"
  success: "#008A00"
  warning: "#B36B00"
  error: "#D43F21"
typography:
  display-hero:
    fontFamily: Nike Futura ND, Helvetica Now Text Medium, Helvetica, Arial, sans-serif
    fontSize: 76px
    fontWeight: 500
    lineHeight: 1
    letterSpacing: "0em"
  page-title:
    fontFamily: Helvetica Now Text Medium, Helvetica, Arial, sans-serif
    fontSize: 24px
    fontWeight: 500
    lineHeight: 1.3
  section-title:
    fontFamily: Helvetica Now Display Medium, Helvetica, Arial, sans-serif
    fontSize: 24px
    fontWeight: 500
    lineHeight: 1.2
  nav-link:
    fontFamily: Helvetica Now Text Medium, Helvetica, Arial, sans-serif
    fontSize: 16px
    fontWeight: 500
    lineHeight: 1.5
  body:
    fontFamily: Helvetica Now Text, Helvetica, Arial, sans-serif
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.75
  utility:
    fontFamily: Helvetica Now Text Medium, Helvetica, Arial, sans-serif
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1.5
spacing:
  xs: 8px
  sm: 12px
  md: 16px
  lg: 24px
  xl: 36px
  page: 48px
  cardInset: 48px
  section: 80px
rounded:
  none: 0px
  chip: 18px
  pill: 999px
components:
  button-pill-primary:
    backgroundColor: "{colors.accent}"
    textColor: "{colors.accentInverse}"
    rounded: "{rounded.pill}"
    padding: 8px 20px
  button-pill-on-image:
    backgroundColor: "{colors.accentInverse}"
    textColor: "{colors.accent}"
    rounded: "{rounded.pill}"
    padding: 8px 20px
  search-input:
    backgroundColor: "{colors.surfaceMuted}"
    textColor: "{colors.ink}"
    rounded: "{rounded.pill}"
    padding: 6px 18px
  product-card:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    rounded: "{rounded.none}"
    padding: 0px
  image-tile:
    backgroundColor: "{colors.surfaceImageFallback}"
    textColor: "{colors.accentInverse}"
    rounded: "{rounded.none}"
    padding: 48px
---

# Nike.com Design System Extraction

## 1. Source

- URL: https://www.nike.com/de/ and product listing after clicking “New”
- Date: 2026-05-07
- Page: German Nike homepage with global retail navigation, campaign-video-style hero, large editorial card grid, classics carousel, discovery link lists, footer, plus supplementary product listing with sidebar filters and product cards.

## 2. Brand DNA

### Visual Identity

Nike.com is not a colourful UI system — it is a highly disciplined black-and-white retail system that uses campaign imagery as its actual colour. The UI deliberately steps back: white canvas, black swoosh, black navigation, light-grey search/chip surfaces, and pill-shaped CTAs. The only functional accent colour outside the image world is a red-brown status orange for product badges such as “Coming Soon”, “Just In”, and “Now in SNKRS”.

### Layout Principles

- Editorial first: full-width campaign modules and large image cards lead the page.
- Commerce second: product listing remains extremely flat — image area + text, no shadows, no borders.
- Brand anchor at the top: two-tier header with partner icons, utility links, swoosh, main navigation, search, favourites, bag.
- Grid with clean edges: 48px side margin, 12–16px card gaps, 2-column campaign grid, 3-column PLP beside sidebar.
- No decorative container borders: surface and image content define modules.

### Mood / Product Feel

Confident, fast, athletic, direct, but not loud in the UI. The emotion comes from campaign imagery, product photography, and large Nike Futura display typography. UI elements are touch-friendly, reduced, and performance-oriented.

## 3. Semantic Tokens

| Role | Token | Value | Usage |
|---|---:|---:|---|
| accent | `--nike-accent` | `#111111` | Primary actions on light background, logo, navigation, titles |
| accent inverse | `--nike-accent-inverse` | `#FFFFFF` | CTA on image surfaces, text on dark campaign images |
| ink/text | `--nike-ink` | `#111111` | Primary text, product name, price, nav |
| canvas/background | `--nike-canvas` | `#FFFFFF` | Page background, header, footer |
| canvas muted | `--nike-canvas-muted` | `#F5F5F5` | Utility bar, search field, chips, controls |
| surface/card | `--nike-surface` | `#FFFFFF` | Flat content surfaces, form panels |
| surface image fallback | `--nike-image-fallback` | `#E5E5E5` | Product image background, lazy-loaded campaign tiles |
| border | `--nike-border` | `#E5E5E5` | Footer dividers, bordered chips, table lines |
| strong border | `--nike-border-strong` | `#CACACB` | Hover/focus on chips and inputs |
| muted text | `--nike-muted` | `#707072` | Footer links, product metadata, placeholder |
| subtle text | `--nike-subtle` | `#9E9EA0` | Disabled controls, small helper text |
| success | `--nike-success` | `#008A00` | Derived for availability/confirmation |
| warning/status | `--nike-status` | `#9E3500` | Observed as product status orange |
| error | `--nike-error` | `#D43F21` | Derived from Nike-like error orange/red |

## 4. Typography

Observed via browser CSS:

- Body: `Helvetica Now Text, Helvetica, Arial, sans-serif`, 16px, 400, 28px line-height.
- Nav and buttons: `Helvetica Now Text Medium`, 16px, 500, 24–28px line-height.
- Utility links: `Helvetica Now Text Medium`, 12px, 500, 18px line-height.
- Section title: `Helvetica Now Display Medium`, 24px, 500, 28.8px line-height.
- Campaign headline: `Nike Futura ND`, 76px, 500, 76px line-height, uppercase.

Hierarchy:

1. Campaign display: 56–76px, uppercase, tight, almost poster-like.
2. Page/section title: 24px medium, sober.
3. Nav/button/product name: 16px medium.
4. Body and product meta: 16px regular, `#707072` for the secondary level.
5. Utility and legal: 12–14px medium/regular.

## 5. Layout System

- Header: utility strip approx. 36px, main header approx. 60px, combined 96px.
- Desktop page gutter: 48px left/right.
- Homepage hero: full-bleed or nearly full-width, text overlay bottom left.
- Campaign grid: 2 columns, 12px column gap, large image surfaces, text inset approx. 48px.
- Promo banner: full-width, 500–600px height, centred text stack.
- Carousel: horizontally scrolling product/classics cards, 3 visible tiles plus clipped overflow.
- PLP: left sidebar approx. 200–240px, product grid 3 columns, image cards square.
- Footer: 4 link columns plus region selector, thin divider at the top.
- Section rhythm in preview: 80px vertical to match the Stripe-like documentation format while staying Nike-flat.

## 6. Components

### Buttons

1. `PillButton / on-image`: white background, black text, 999px radius, 8–10px y, 16–20px x.
2. `PillButton / black`: black background, white text, same dimensions.
3. `TextButton / cancel`: plain text, 16px medium, no border.
4. `IconButton / header`: 36–40px, icon-only, round/hover light grey.
5. `CarouselControl`: 48px circle, light grey, arrow icon, disabled with `#F5F5F5`.
6. `ChipButton`: light-grey pill, 36px height, 16px text.
7. `OutlineChip`: white pill with `#CACACB` border, for related categories.

### Cards

8. `HeroImageOverlay`: full-bleed/video module with kicker, Futura headline, sub-line, CTA bottom left.
9. `CampaignCard`: 50% image card, text bottom left, no radius, no shadow.
10. `PromoBanner`: large image or fallback surface, centred text stack.
11. `ProductTileCarousel`: sneaker image, floating label pill bottom left.
12. `ProductCard`: square product image surface, badge, name, meta, price, no shadow.
13. `PromoTileInGrid`: square campaign card in the product grid, white text and CTA.
14. `TokenCard`: derived for documentation — must remain flat.
15. `FooterColumn`: headline black, links grey, generous line-height.

### Nav

16. `UtilityHeader`: light-grey top bar with Jordan/Converse on the left, store/help/join us/sign in on the right.
17. `MainHeader`: swoosh on the left, central category navigation, search/favourites/bag on the right.
18. `MegaMenuTrigger`: nav link + invisible/ARIA menu trigger; hover presumably opens mega-menu.
19. `AnnouncementBar`: light-grey promo strip with text link.
20. `RegionSelector`: globe icon + “Germany”.

### Hero

21. `CampaignHero`: campaign image with Nike Futura headline “TIERISCH BEQUEM”.
22. `EditorialCaption`: kicker 16px, headline 24px or display, sub-line 16–20px.

### Forms

23. `SearchOverlay`: 100% wide white top surface, approx. 324px height, no backdrop dimming.
24. `SearchInputPill`: 755px wide on desktop, 36px tall, `#F5F5F5`, magnifier on the left, grey placeholder.
25. `PopularSearchChips`: multi-row light-grey chips for “air force 1”, “air max”, “jordan”.
26. `FilterSidebar`: scrollable left area with category links and accordions.
27. `FilterAccordion`: button with chevron, content per region, flat without card border.
28. `SortDropdown`: text button with chevron, no border.
29. `FormField`: derived from search — flat light-grey inputs with black focus ring.

### Modals / Dropdowns

30. `SearchSheet`: observed as dropdown/sheet rather than modal, white, no shadow, no overlay dimming.
31. `SortMenu`: derived from PLP — simple list below text button.
32. `GuidesFooterDropdown`: observed as a legal footer link with chevron.

## 7. Brand-specific Product Patterns

- Campaign images are navigation: hero and cards are not just advertising — they are the primary entry points into product worlds.
- CTA buttons are almost always pills and often white on image, so they remain stable across changing campaign imagery.
- Nike Futura ND is reserved for expressive campaign headlines, not regular UI.
- Product listing refuses typical card decoration: no shadows, no borders, no quick-buy in the visible grid.
- Status is typographic, not a badge capsule: orange text above the product name instead of a coloured pill.
- Promo tiles interrupt the product grid and retain the same image overlay language as the homepage.
- Search is its own top sheet: prominent, but without a dark modal backdrop.
- Category discovery is solved as a footer/link-list system, not as colourful marketing tiles.
- Carousel overflow shows exploration: third/fourth tile clipped, arrow controls top right.
- Header is two-tiered: partner ecosystem on top, Nike commerce below.

## 8. Motion / Interaction

Directly recognisable or plausible from observed states:

- Header nav opens mega-menus on hover/click.
- Search expands to a white top sheet with search suggestions and “Cancel”.
- Search chips and CTAs use a slight hover darkening: white button likely `#E5E5E5`, black buttons `#707072`.
- Icon buttons receive light-grey circular surfaces on hover.
- Carousel arrows scroll horizontally; disabled state is lighter.
- Filter toggle shows/hides the sidebar.
- Filter accordions expand, sort dropdown opens a list.
- Product cards are fully clickable; hover likely shows alternative product images/colour options — not definitively observed in the screenshot.
- Focus states should use black or dark grey as a ring, because Nike has no coloured UI accent system.

## 9. Implementation Notes

### Concrete CSS Tokens

```css
:root {
  --nike-ink: #111111;
  --nike-white: #ffffff;
  --nike-canvas-muted: #f5f5f5;
  --nike-image-fallback: #e5e5e5;
  --nike-border: #e5e5e5;
  --nike-border-strong: #cacacb;
  --nike-muted: #707072;
  --nike-subtle: #9e9ea0;
  --nike-status: #9e3500;
  --nike-success: #008a00;
  --nike-error: #d43f21;
  --font-text: "Helvetica Now Text", Helvetica, Arial, sans-serif;
  --font-medium: "Helvetica Now Text Medium", Helvetica, Arial, sans-serif;
  --font-display: "Nike Futura ND", "Helvetica Now Text Medium", Helvetica, Arial, sans-serif;
  --gutter: 48px;
  --gap-card: 12px;
  --inset-card: 48px;
  --radius-pill: 999px;
}
```

### Component Structure

- `NikeHeader` with `UtilityHeader`, `MainHeader`, `SearchTrigger`, `CommerceIcons`.
- Keep `CampaignHero` and `CampaignGrid` separate but share the same overlay component.
- `ProductListingLayout` with `FilterSidebar`, `ListingToolbar`, `ProductGrid`, `ProductCard`, `GridPromoTile`.
- `SearchSheet` as a top-level overlay directly below body, not as a centred modal.
- `DiscoveryFooter` with `CategoryColumns`, `FooterColumns`, `LegalFooter`.

### Do

- Allow generous whitespace.
- Make image surfaces large and keep UI surfaces flat.
- Use the display font only for campaign headlines.
- Apply monochrome contrast consistently.
- Use CTAs as compact pills.
- Build product cards without box shadows.

### Don't

- Do not introduce colourful accent gradients.
- No generic SaaS shadows or glass effects.
- Do not force card radii onto campaign/product cards — Nike uses hard image edges.
- Do not render product status as a Bootstrap-style badge; the observed pattern is coloured text.
- Do not centre search as a dark modal — Nike uses a white top sheet.

## 10. Accuracy Check

### Directly Observed

- URL redirected to `/de/`.
- Fonts via CSS: Helvetica Now Text, Helvetica Now Text Medium, Helvetica Now Display Medium, Nike Futura ND.
- Body 16px/28px, hero H3 76px/76px, H2 24px/28.8px, utility 12px/18px.
- Colours `#111111`, `#FFFFFF`, `#F5F5F5`, `#E5E5E5`, `#707072` observed visually and via CSS/RGB.
- Header structure, search sheet, popular search chips, homepage hero, campaign cards, classics carousel, link lists, footer.
- PLP title, filter sidebar, filter toggle, sorting, product grid, product cards, promo tile, related category chips.

### Derived

- Success/warning/error tokens — they did not appear as form states on the visible homepage.
- Sort dropdown content and filter accordion details based on visible controls.
- Hover transitions and product card hover — only resting states were visible.
- Exact mega-menu design — clicking “New” led to the listing page rather than opening a mega-menu.

### Uncertain

- Exact shadow values: Nike appears mostly shadowless; if menus use internal shadows they were not visible in the screenshot.
- Some light-grey campaign surfaces may have been lazy-load fallbacks — do not treat their contrast as the final creative state.
- Exact swoosh SVG dimensions and mobile breakpoints were not fully investigated.

Source: www.designmd-store.com
