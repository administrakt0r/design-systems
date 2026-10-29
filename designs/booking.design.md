---
version: alpha
name: Booking.com
domain: booking.com
source: "https://www.booking.com"
date: "2026-05-07"
description: "Booking.com homepage: high-conversion travel commerce system with full-bleed brand blue, a yellow search frame, modular property cards, destination image cards, review badges, Genius promos, and dense link/footer ecosystems."
colors:
  primary: "#006CE4"
  accent: "#006CE4"
  accentHover: "#0057B8"
  brandBlue: "#003B95"
  brandBlueDark: "#00224F"
  searchYellow: "#FFB700"
  geniusBlue: "#003B95"
  ink: "#1A1A1A"
  mutedText: "#595959"
  canvas: "#FFFFFF"
  background: "#F5F5F5"
  surface: "#FFFFFF"
  surfaceAlt: "#FAFAFA"
  border: "#E7E7E7"
  borderStrong: "#BDBDBD"
  success: "#008234"
  warning: "#FFB700"
  error: "#D4111E"
typography:
  display:
    fontFamily: "Avenir Next, system-ui, -apple-system, Segoe UI, Roboto, Helvetica, Arial, sans-serif"
    fontSize: 48px
    fontWeight: 700
    lineHeight: 1.08
    letterSpacing: "-0.02em"
  h1:
    fontFamily: "Avenir Next, system-ui, -apple-system, Segoe UI, Roboto, Helvetica, Arial, sans-serif"
    fontSize: 24px
    fontWeight: 700
    lineHeight: 32px
  h2:
    fontFamily: "Avenir Next, system-ui, -apple-system, Segoe UI, Roboto, Helvetica, Arial, sans-serif"
    fontSize: 24px
    fontWeight: 700
    lineHeight: 32px
  h3:
    fontFamily: "system-ui, -apple-system, Segoe UI, Roboto, Helvetica, Arial, sans-serif"
    fontSize: 16px
    fontWeight: 700
    lineHeight: 24px
  body:
    fontFamily: "system-ui, -apple-system, Segoe UI, Roboto, Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 20px
  bodyLarge:
    fontFamily: "system-ui, -apple-system, Segoe UI, Roboto, Helvetica, Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 24px
  meta:
    fontFamily: "system-ui, -apple-system, Segoe UI, Roboto, Helvetica, Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 18px
rounded:
  sm: 4px
  md: 8px
  card: 12px
  lg: 16px
  pill: 9999px
  circle: 999px
spacing:
  xs: 4px
  sm: 8px
  md: 12px
  lg: 16px
  xl: 24px
  xxl: 32px
  section: 48px
  page: 32px
  maxWidth: 1128px
shadows:
  search: "0 2px 8px rgba(26, 26, 26, 0.16)"
  cardHover: "0 2px 8px rgba(26, 26, 26, 0.16)"
  popover: "0 8px 24px rgba(26, 26, 26, 0.18)"
  floating: "0 2px 4px rgba(26, 26, 26, 0.16)"
components:
  button-primary:
    backgroundColor: "{colors.accent}"
    textColor: "#FFFFFF"
    rounded: "{rounded.sm}"
    padding: 12px
  button-primary-hover:
    backgroundColor: "{colors.accentHover}"
    textColor: "#FFFFFF"
    rounded: "{rounded.sm}"
    padding: 12px
  button-on-blue:
    backgroundColor: "#FFFFFF"
    textColor: "{colors.accent}"
    rounded: "{rounded.sm}"
    padding: 8px
  search-container:
    backgroundColor: "{colors.searchYellow}"
    textColor: "{colors.ink}"
    rounded: "{rounded.md}"
    padding: 4px
  property-card:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.ink}"
    rounded: "{rounded.md}"
    padding: 0px
---

## 1. Source

- URL: https://www.booking.com
- Date: 2026-05-07
- Page description: Public Booking.com homepage with header, product navigation, hero search, why-Booking cards, offers, destination cards, property carousels, Genius promo, link lists, and footer.

## 2. Brand DNA

### Visual Identity
Booking.com combines a very clear travel-commerce identity with maximum conversion readability: at the top, a calm, full-bleed dark blue as a trust surface; below it, a yellow-framed search module as the primary interaction anchor. The rest of the page is white, modular, card-based, and strongly information-oriented.

### Layout Principles
- Centred max-width of approx. 1128px.
- Header and hero as a wide brand surface.
- Search sits at the transition between blue and content, feeling like an embedded control panel.
- Product modules follow a repeatable section rhythm: section title, short subtext, horizontal cards or image grid.
- Interaction is always visible: blue buttons, blue links, yellow search frame, scores as blue badges.

### Mood / Product Feel
Pragmatic, trustworthy, transactional, fast. Less lifestyle magazine than Airbnb — more search engine and marketplace. The page feels like "find, compare, book".

## 3. Semantic Tokens

- accent: #006CE4 — primary CTA and link colour, search button, register/sign-in text.
- ink/text: #1A1A1A — primary text, card content, labels.
- canvas/background: #FFFFFF as main canvas, #F5F5F5 for slightly offset panels.
- surface/card: #FFFFFF — nearly all cards, popovers, form fields.
- border: #E7E7E7 — light card and footer dividers; #BDBDBD for stronger UI separation.
- muted text: #595959 — metadata, descriptions, link lists.
- brandBlue: #003B95 — header, hero, Genius label, rating badge context.
- searchYellow/warning: #FFB700 — search frame, strong attention signal, Booking-specific conversion signal.
- success: #008234 — derived for positive availability/confirmation.
- error: #D4111E — observed as the red system/warning colour in CSS colours.

## 4. Typography

- Font note: computed CSS shows system-ui for body and "Avenir Next" for H1/H2, with system-ui fallbacks.
- Size logic: body 14/20px, large controls 16/24px, section headings 24/32px, hero can reach up to 48px depending on viewport.
- Weight: 400 for body text, 500 for controls and tabs, 700 for headings, card titles, and important product data.
- Hierarchy: headlines and section titles are bold; cards use compact titles plus grey meta; price and score information is visually compressed but high-contrast.

## 5. Layout System

- Grid: centred container, approx. 1128px max-width.
- Section rhythm: 32–48px vertical, 16–24px card gaps.
- Responsive pattern: desktop with 4-card row, destinations as 2+3 grid, footer as 5 columns; mobile should switch to horizontal scroll areas or a 1-column stack.
- Search layout: compound control with 4 segments; container yellow, individual fields white, 4px gaps, search CTA on the right.
- Card layout: image-heavy property cards 220–260px wide, photo on top, content on bottom, heart overlay, rating + reviews, price at the bottom.

## 6. Components

1. Brand header on #003B95 with white logo.
2. Utility nav buttons: USD, language, support, list your property.
3. Account buttons: white buttons on blue header with #006CE4 text.
4. Product nav pills with icons; active tab as a white 1px outline pill.
5. Hero headline and sub-headline on brand blue.
6. Destination combobox with icon and placeholder.
7. Date range trigger with calendar icon.
8. Occupancy trigger with adults/children/rooms text.
9. Primary search button in #006CE4.
10. Add-flights checkbox directly below the search.
11. Datepicker popover with calendar/flexible tabs and month grid.
12. Occupancy popover with stepper/slider rows and done button.
13. Why Booking.com benefit cards with illustration, title, description.
14. Offer promo card with Visa/Genius illustration and learn-more CTA.
15. Destination image cards with dark overlay, white place title, flag.
16. Property cards with photo, type, Genius/Preferred labels, title, location.
17. Favourite heart button as a round white floating control.
18. Rating badge: dark blue, white score, next to text and review count.
19. Carousel navigation as round floating arrow buttons.
20. Property type links/tiles: hotels, apartments, resorts, villas, etc.
21. Explore-destination links with property count.
22. Genius promo sign-in card with primary sign-in button and register link.
23. Traveller tabs: active category as a blue outline pill.
24. Dense link grid for cities/countries/properties.
25. Footer with support/discover/terms/partners/about columns.
26. Cookie dialog and sign-in save modal: white cards, clear CTAs, close button.

## 7. Brand-specific Product Patterns

- Yellow search shell: the most distinctive Booking-specific pattern is the #FFB700 frame around the compound search. It is not just colour — it prioritises the booking process.
- Blue trust header: the blue surface bundles logo, product navigation, and hero so that search logically sits as the next action below it.
- Rating badge grammar: score as a small blue rectangle, next to a qualitative label and review count. This enables rapid comparison.
- Genius layer: blue Genius logo, sign-in-save-money modal, Genius Rewards Visa, and Genius promo link loyalty to the visual brand.
- Marketplace carousel cards: property cards are data-rich but consistent — type, trust badges, name, location, score, reviews, price.
- Destination discovery grid: image cards use photography and dark overlays, not illustrative marketing graphics.
- Dense travel taxonomy: footer and link lists are SEO/discovery-oriented, showing many categories without decorative distraction.

## 8. Motion / Interaction

- Hover: primary blue buttons darken towards #0057B8; cards receive a light shadow or border contrast.
- Search interactions: destination opens autosuggest; date opens a large calendar popover; occupancy opens a popover with steppers/sliders and a pet toggle.
- Carousel: round next/previous controls move property and category lists horizontally.
- Focus: interactive fields should use a clear blue ring.
- Modal/dropdown: white surfaces with popover shadow, 8px radius, high z-index.

## 9. Implementation Notes

### CSS-Token
```css
:root {
  --booking-brand-blue: #003B95;
  --booking-brand-blue-dark: #00224F;
  --booking-action: #006CE4;
  --booking-action-hover: #0057B8;
  --booking-search-yellow: #FFB700;
  --booking-ink: #1A1A1A;
  --booking-muted: #595959;
  --booking-canvas: #FFFFFF;
  --booking-bg: #F5F5F5;
  --booking-border: #E7E7E7;
  --booking-radius-sm: 4px;
  --booking-radius-md: 8px;
  --booking-radius-pill: 9999px;
  --booking-container: 1128px;
}
```

### Component Structure
- `Header` with `TopUtilityNav`, `ProductNav`, `HeroIntro`.
- `SearchShell` with `SearchSegment`, `DateRangeButton`, `OccupancyButton`, `SearchCTA`, `AddFlightsCheckbox`.
- `Section` component with title, optional subtitle, action slot.
- `PropertyCarousel` with `PropertyCard`, `RatingBadge`, `FavoriteButton`, `CarouselArrow`.
- `DestinationGrid` with `ImageOverlayCard`.
- `LoyaltyPromo`, `OfferCard`, `LinkTaxonomy`, `FooterColumns`.

### Do
- Use #003B95 at large scale only for header/hero/trust surfaces.
- Use #FFB700 exclusively as the search/attention frame, not as an arbitrary accent colour.
- Keep cards and form fields white, compact, and data-dense.
- Preserve the score-badge grammar exactly: blue block, white score, text beside it.

### Don't
- Do not transform into generic SaaS gradients.
- Do not add excessive shadows or glass effects — Booking is functional and mostly flat.
- Do not present the search as a simple search input; it is a multi-segment booking panel.
- Do not remove the footer/link density — it is part of Booking's product DNA.

## 10. Accuracy Check

### Directly Observed
- Header #003B95, white account buttons, product nav pills.
- Search with #FFB700 shell, white segments, and blue search button.
- Body #1A1A1A, muted #595959, links/CTA #006CE4, border #E7E7E7.
- Computed font: body system-ui, headings Avenir Next/system-ui.
- Datepicker popover with calendar/flexible tabs and month grid.
- Occupancy popover with adults/children/rooms and pets toggle.
- Property cards, heart buttons, rating badges, Genius/Preferred labels.
- Destination image cards, offers card, Genius promo, footer columns.

### Derived
- Hover #0057B8 from Booking action-hover convention and standard button darkening.
- Success #008234 as a positive system colour, as it was not prominently visible on the homepage.
- Individual sizes for desktop preview where computed values were viewport-dependent.

### Uncertain
- Exact internal BUI token names were not visible as CSS custom properties.
- Some images/carousel areas were partially empty or lazy-loaded in the browser screenshot; patterns were derived from visible text, card structure, and loaded regions.
- Motion durations were not measured; short 120–180ms transitions are recommended, consistent with the functional UI.

Source: www.designmd-store.com
