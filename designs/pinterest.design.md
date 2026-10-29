---
version: alpha
name: Pinterest
source: https://www.pinterest.com
date: 2026-05-07
description: Image-centred discovery system with Pinterest Red as a strictly reserved CTA accent, Pin Sans, soft 16px radius, and masonry-style pin cards.
colors:
  primary: "#e60023"
  accent: "#e60023"
  accentPressed: "#cc001f"
  ink: "#000000"
  inkSoft: "#211922"
  text: "#33332e"
  muted: "#62625b"
  mutedSoft: "#91918c"
  border: "#dadad3"
  borderSoft: "#e5e5e0"
  canvas: "#ffffff"
  surfaceSoft: "#fbfbf9"
  surfaceCard: "#f6f6f3"
  surfaceSecondary: "#e5e5e0"
  surfaceSecondaryPressed: "#c8c8c1"
  surfaceDark: "#262622"
  onAccent: "#ffffff"
  onDark: "#ffffff"
  focus: "#435ee5"
  infoBlue: "#2b48d4"
  success: "#103c25"
  successPale: "#c7f0da"
  warning: "#d17711"
  error: "#9e0a0a"
typography:
  display-xl:
    fontFamily: "Pin Sans, Inter, -apple-system, BlinkMacSystemFont, Segoe UI, sans-serif"
    fontSize: 70px
    fontWeight: 600
    lineHeight: 1.1
    letterSpacing: "-1.2px"
  display-lg:
    fontFamily: "Pin Sans, Inter, -apple-system, BlinkMacSystemFont, Segoe UI, sans-serif"
    fontSize: 44px
    fontWeight: 700
    lineHeight: 1.15
    letterSpacing: "-0.8px"
  heading-xl:
    fontFamily: "Pin Sans, Inter, -apple-system, BlinkMacSystemFont, Segoe UI, sans-serif"
    fontSize: 28px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: "-1.2px"
  heading-lg:
    fontFamily: "Pin Sans, Inter, -apple-system, BlinkMacSystemFont, Segoe UI, sans-serif"
    fontSize: 22px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: "0px"
  body-md:
    fontFamily: "Pin Sans, Inter, -apple-system, BlinkMacSystemFont, Segoe UI, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: "0px"
  body-strong:
    fontFamily: "Pin Sans, Inter, -apple-system, BlinkMacSystemFont, Segoe UI, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: "0px"
  body-sm:
    fontFamily: "Pin Sans, Inter, -apple-system, BlinkMacSystemFont, Segoe UI, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: "0px"
  caption:
    fontFamily: "Pin Sans, Inter, -apple-system, BlinkMacSystemFont, Segoe UI, sans-serif"
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1.5
    letterSpacing: "0px"
  button:
    fontFamily: "Pin Sans, Inter, -apple-system, BlinkMacSystemFont, Segoe UI, sans-serif"
    fontSize: 14px
    fontWeight: 700
    lineHeight: 1
    letterSpacing: "0px"
rounded:
  none: 0px
  sm: 8px
  md: 16px
  lg: 32px
  full: 9999px
spacing:
  xxs: 4px
  xs: 6px
  sm: 8px
  md: 12px
  lg: 16px
  xl: 24px
  xxl: 32px
  section: 64px
components:
  button-primary:
    backgroundColor: "{colors.accent}"
    textColor: "{colors.onAccent}"
    typography: "{typography.button}"
    rounded: "{rounded.md}"
    padding: 6px 14px
    height: 40px
  button-primary-pressed:
    backgroundColor: "{colors.accentPressed}"
    textColor: "{colors.onAccent}"
    rounded: "{rounded.md}"
  button-secondary:
    backgroundColor: "{colors.surfaceSecondary}"
    textColor: "{colors.ink}"
    typography: "{typography.button}"
    rounded: "{rounded.md}"
    padding: 6px 14px
    height: 40px
  search-bar:
    backgroundColor: "{colors.surfaceCard}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: 11px 15px
    height: 48px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.md}"
    padding: 11px 15px
    height: 48px
  pin-card:
    backgroundColor: "{colors.surfaceCard}"
    textColor: "{colors.ink}"
    rounded: "{rounded.md}"
    padding: 0px
  pin-card-large:
    backgroundColor: "{colors.surfaceCard}"
    textColor: "{colors.ink}"
    rounded: "{rounded.lg}"
    padding: 0px
  modal-card:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.lg}"
    padding: 32px
  filter-chip:
    backgroundColor: "{colors.surfaceCard}"
    textColor: "{colors.ink}"
    typography: "{typography.button}"
    rounded: "{rounded.full}"
    padding: 8px 16px
  filter-chip-active:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.onDark}"
    typography: "{typography.button}"
    rounded: "{rounded.full}"
    padding: 8px 16px
---

## 1. Source

- URL: https://www.pinterest.com
- Date: 2026-05-07
- Page: Public Pinterest homepage in German localisation, observed as a landing page with sticky top navigation, large idea hero, carousel-style pin collage, feature sections, signup form, and cookie modal. Supplemented by existing local Pinterest design.md evidence and live computed styles from the browser.

## 2. Brand DNA

### Visual Identity
Pinterest is an image-centred discovery system. The UI itself is deliberately quiet: white and warm cream surfaces, black typography, almost no shadows, and a single highly saturated accent. Pinterest Red `#e60023` marks the logo, primary CTAs, and conversion points. The actual visual energy does not come from decorative UI but from the pin images: variable heights, soft corners, collage and masonry feel.

### Layout Principles
- A horizontal, sticky top nav with logo on the left, search as the dominant centre control, and CTA cluster on the right.
- Hero as a centred headline plus vertical pin collage with carousel-style image groups.
- Marketing sections alternate between text block and image pattern, often as a 2-column staging.
- Discovery surfaces use tight 8px gutters and natural image aspect ratios.
- Almost all interactive surfaces have 16px or pill radius.

### Mood / Product Feel
Friendly, soft, curated, low-threshold, and visually appealing. Pinterest feels less like a dashboard and more like an inspiration magazine with a search engine. The surface says: search quickly, save, try it out.

## 3. Semantic Tokens

| Role | Token | Value | Meaning |
|---|---|---:|---|
| accent | `--pin-red` | `#e60023` | Logo, signup, login, explore CTA |
| accent pressed | `--pin-red-pressed` | `#cc001f` | Pressed primary button, deep red state |
| ink/text | `--ink` | `#000000` | Headline, button text, primary contrast |
| ink soft | `--ink-soft` | `#211922` | Pinterest-typical warm-black UI text |
| body | `--body` | `#33332e` | Longer copy and section text |
| canvas/background | `--canvas` | `#ffffff` | Main surface, nav, modal, forms |
| canvas soft | `--surface-soft` | `#fbfbf9` | Very light warm page wash surface |
| surface/card | `--surface-card` | `#f6f6f3` | Search bar, pin placeholder, neutral cards |
| secondary surface | `--surface-secondary` | `#e5e5e0` | Register/cookie/secondary buttons |
| border | `--border` | `#dadad3` | Subtle dividers, input borders |
| muted text | `--muted` | `#62625b` | Footer, help text, secondary info |
| disabled | `--muted-soft` | `#91918c` | Placeholder, disabled text |
| focus | `--focus` | `#435ee5` | Blue accessibility focus ring |
| success | `--success` | `#103c25` | Success text, positive system message |
| success bg | `--success-pale` | `#c7f0da` | Success pill background |
| warning | `--warning` | `#d17711` | Cautious status message, editorial accent |
| error | `--error` | `#9e0a0a` | Validation, error text |

## 4. Typography

- Font note: Live computed style shows `Pin Sans` with system fallbacks: `-apple-system`, `system-ui`, `Segoe UI`, `Roboto`, `Helvetica Neue`, `Arial`, sans-serif. Pin Sans is proprietary; the preview uses Inter/system as a substitute.
- Size logic: strong hero peak at approx. 70px/600, marketing H2 at 44px/700, section/card headings 28px/700, and UI text 16px/400 to 16px/600.
- Weight: Pinterest builds hierarchy strongly through 600/700 rather than many colours.
- Tracking: large headlines tightly set, approx. -1.2px to -0.8px.
- Button text: compact, heavy, 14px/700 or in live nav sometimes 12px, but visually bold through pill form and colour.

## 5. Layout System

- Grid: marketing container approx. 1280px max, desktop 24px to 48px outer margin.
- Masonry: 5–6 columns ultrawide, 4 desktop, 3 tablet, 2 mobile, 1 very narrow. Pin gutter 8px.
- Section rhythm: 64px between main sections, mobile 32–48px.
- Hero: centred headline, below/around it an image collage with varying-height pin tiles.
- Nav: 64px to 80px tall top bar, logo on the left, search flexible in the centre, CTA on the right.
- Forms: signup modal/form as a vertical stack, inputs 48px tall, 16px radius, 11px/15px padding.

## 6. Components

### Buttons
1. Primary CTA: red `#e60023`, white text, 16px radius, approx. 40–48px tall, 6px 14px padding.
2. Primary pressed: `#cc001f`, identical form.
3. Secondary: `#e5e5e0`, black text, 16px radius.
4. Tertiary/ghost: transparent, black text, 16px radius.
5. Cookie secondary: `#e5e5e0`, 16px radius, multi-line labels possible.
6. Icon circle: 40–48px, pill/full radius, for scroll/carousel/close.
7. On-image pill: white, black text, 9999px radius, overlaid on pin image.

### Cards
8. Pin card: full-bleed image, 16px radius, no inner padding, no shadows.
9. Large pin card: 32px radius for hero or feature pins.
10. Category tile: warm cream surface, 16px radius, image group + short search term.
11. Feature card: text + image, 32px padding, mostly flat.
12. Modal card: white, 32px radius, 32px padding, scrim and soft shadow.
13. Dark CTA strip: `#262622`, white text, red CTA.
14. Feed metric/attribution chip: avatar circle + name/followers on or below image.

### Nav
15. Primary nav: sticky, white, logo red, links black, search centred, red signup action.
16. Search bar: 48px tall, `#f6f6f3`, pill radius, magnifier on the left, placeholder in muted grey.
17. Mobile nav: compressed icons, search becomes icon/overlay, signup remains visible.

### Hero
18. Hero headline: "Find your next idea:" with rotating search statements.
19. Carousel dots: round indicators, 25px visible from computed styles.
20. Down-scroll affordance: round coloured button leading into the next section.
21. Pin collage: multiple portrait-oriented tiles as brand keyvisual.

### Forms
22. Signup input: 48px height, 1px `#91918c`, 16px radius, 11px/15px padding.
23. Password field: identical, icon/switch on the right.
24. Continue button in signup: compact red button, 12px label, 12px radius observed.
25. Helper link: small text link, `#2b48d4` or warm black depending on context.
26. Consent modal: title, explanation, link, 3 secondary pill buttons.

### Modals/Dropdowns
27. Cookie modal: centred white card with generous padding, above the hero collage.
28. Signup modal/form: "Welcome to Pinterest", vertical input stack, small legal links.
29. Selection/filter chips: pill chips, active inverted black on white.
30. Footer link columns: small 12–14px links, blue for legal/utility links in observed localisation.

## 7. Brand-specific Product Patterns

1. Masonry as the primary component: pins are not forced into standardised cards with copy. The image itself is the card.
2. Single-red conversion logic: red is not decoration but almost exclusively action and brand.
3. Search-first navigation: search is not a small header field but the central product control.
4. Idea sentence machine in the hero: "Find your next idea:" plus rotating search suggestions conveys discovery rather than a static brand line.
5. Full-bleed pin geometry: no card chrome overload, no shadow, just image + radius.
6. Overlay pills on images: labels such as search terms or categories sit as white pills on photos.
7. Warm neutral chrome: `#f6f6f3` and `#e5e5e0` take the volume out of the UI surface.
8. Signup gate at the end of the page: the marketing story leads into a form, not just a footer.
9. Mixed editorial/product modes: home feels magazine-like, search feels like an image index; both use the same tokens.
10. Radius vocabulary as recognition: 16px/32px/full dominates more strongly than shadows or lines.

## 8. Motion / Interaction

- Hero carousel rotates between idea terms and image groups, visible through dots and slide structure.
- Scroll buttons connect sections vertically and create a guided landing page.
- Primary buttons have a pressed state in deeper red `#cc001f`.
- Secondary buttons press from `#e5e5e0` to `#c8c8c1`.
- Search focus: surface switches to white with border, focus ring may be blue `#435ee5`.
- Modal interaction: cookie/signup sits above scrim, page behind remains visible as context.
- No pronounced card shadows or hover lifts observed; Pinterest relies on image content and clickability.

## 9. Implementation Notes

### Concrete CSS Tokens
```css
:root {
  --pin-red: #e60023;
  --pin-red-pressed: #cc001f;
  --ink: #000000;
  --ink-soft: #211922;
  --body: #33332e;
  --muted: #62625b;
  --muted-soft: #91918c;
  --border: #dadad3;
  --canvas: #ffffff;
  --surface-soft: #fbfbf9;
  --surface-card: #f6f6f3;
  --surface-secondary: #e5e5e0;
  --surface-secondary-pressed: #c8c8c1;
  --surface-dark: #262622;
  --focus: #435ee5;
  --r-md: 16px;
  --r-lg: 32px;
  --r-full: 9999px;
  --space-section: 64px;
}
```

### Component Structure
- `PinterestSystemPage`
  - `StickyNav`
  - `HeroIdeaCarousel`
  - `MetaStrip`
  - `TokenSection`
  - `MasonryPreview`
  - `ComponentGallery`
  - `SignupModalDemo`
  - `FormStates`
  - `SpacingRadiusElevationDocs`
  - `ExtractedComponentTokens`

### Do
- Use pin images or abstract coloured image surfaces as the main visual.
- Use red sparingly and always action-related.
- Keep cards flat and full-bleed.
- Use 16px radius as the default component language.
- Place search prominently at the centre.

### Don't
- No generic SaaS gradients.
- No glass/blur decoration for cards.
- No square buttons.
- No red surface fireworks outside of logo/CTA.
- No shadow elevation for every element.

## 10. Accuracy Check

### Directly Observed
- Live URL redirected to `https://de.pinterest.com/`.
- Header with Pinterest logo, Explore, search field, links, Log in, and Sign up.
- Computed styles: font stack starts with `Pin Sans`; primary button `rgb(230, 0, 35)` = `#e60023`; secondary button `rgb(229,229,224)` = `#e5e5e0`; text `rgb(33,25,34)` = `#211922`; inputs 48px tall, 16px radius, 1px `#91918c` border; hero H2 70px/600.
- Visible homepage with large hero idea, pin collage, scroll buttons, signup form, cookie modal.

### Derived
- Complete masonry breakpoints, filter chip active state, and some semantic tokens were supplemented from existing local Pinterest design.md evidence and common Pinterest web patterns.
- Preview uses abstract gradients/colour surfaces instead of real Pinterest image assets to remain reproducible and licence-safe.

### Uncertain
- Authenticated feed, board detail pages, and pin detail modal were not investigated live.
- Mobile behaviour is derived from system logic and existing evidence, not verified in a mobile screenshot.
- Proprietary Pin Sans metrics can only be approximated; Inter/system is the safe substitute family.

Source: www.designmd-store.com
