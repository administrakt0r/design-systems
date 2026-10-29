---
version: alpha
name: Notion
source: "https://www.notion.so"
date: "2026-05-07"
description: "Current Notion marketing and product design: dark AI night-shift hero, light modular workspace sections, NotionInter/Lyon Text, blue CTA roles, colourful agent and product cards, flat document-like components."
colors:
  primary: "#097FE8"
  accent: "#097FE8"
  accentHover: "#0075DE"
  accentPressed: "#005BAB"
  ink: "#191918"
  inkStrong: "#000000"
  text: "#171717"
  textMuted: "#737373"
  textSubtle: "#A3A3A3"
  canvas: "#FFFFFF"
  pageDark: "#191918"
  heroNavy: "#02093A"
  surface: "#F6F5F4"
  surfaceSoft: "#F9F9F8"
  surfaceAccentMuted: "#F2F9FF"
  card: "#FFFFFF"
  border: "#E5E5E5"
  borderStrong: "#DFDCD9"
  onDark: "#FFFFFF"
  onDarkMuted: "#D6D6D6"
  blue400: "#62AEF0"
  campaignsBlue: "#455DD3"
  red: "#F64932"
  orange: "#FF6D00"
  orange600: "#DD5B00"
  yellow: "#FFB110"
  teal: "#2A9D99"
  green: "#1AAE39"
  pink: "#FF64C8"
  purple: "#AD6DED"
  brown: "#9C7054"
  success: "#1AAE39"
  warning: "#FF6D00"
  error: "#F64932"
typography:
  displayHero:
    fontFamily: "NotionInter, Inter, -apple-system, BlinkMacSystemFont, Segoe UI, Helvetica, Arial, sans-serif"
    fontSize: 64px
    fontWeight: 700
    lineHeight: 1
    letterSpacing: "-0.117em"
  displayLg:
    fontFamily: "NotionInter, Inter, -apple-system, BlinkMacSystemFont, Segoe UI, Helvetica, Arial, sans-serif"
    fontSize: 54px
    fontWeight: 700
    lineHeight: 1.04
    letterSpacing: "-0.06em"
  titleLg:
    fontFamily: "NotionInter, Inter, -apple-system, BlinkMacSystemFont, Segoe UI, Helvetica, Arial, sans-serif"
    fontSize: 42px
    fontWeight: 600
    lineHeight: 1.14
    letterSpacing: "-0.04em"
  titleMd:
    fontFamily: "NotionInter, Inter, -apple-system, BlinkMacSystemFont, Segoe UI, Helvetica, Arial, sans-serif"
    fontSize: 26px
    fontWeight: 700
    lineHeight: 1.23
    letterSpacing: "-0.015em"
  body:
    fontFamily: "NotionInter, Inter, -apple-system, BlinkMacSystemFont, Segoe UI, Helvetica, Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
  bodySm:
    fontFamily: "NotionInter, Inter, -apple-system, BlinkMacSystemFont, Segoe UI, Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
  nav:
    fontFamily: "NotionInter, Inter, -apple-system, BlinkMacSystemFont, Segoe UI, Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.43
  caption:
    fontFamily: "NotionInter, Inter, -apple-system, BlinkMacSystemFont, Segoe UI, Helvetica, Arial, sans-serif"
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1.33
  quote:
    fontFamily: "Lyon Text, Georgia, YuMincho, Hiragino Mincho ProN, Songti SC, SimSun, serif"
    fontSize: 32px
    fontWeight: 400
    lineHeight: 1.25
  mono:
    fontFamily: "iA Writer Mono, Nitti, Menlo, Courier, monospace"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
rounded:
  xs: 4px
  sm: 5px
  md: 6px
  lg: 12px
  xl: 14px
  xxl: 16px
  round: 9999px
spacing:
  xxs: 4px
  xs: 8px
  sm: 12px
  md: 16px
  lg: 24px
  xl: 32px
  xxl: 48px
  section: 96px
  hero: 120px
components:
  nav-main:
    backgroundColor: "transparent"
    textColor: "{colors.onDark}"
    typography: "{typography.nav}"
    height: 64px
  button-primary:
    backgroundColor: "{colors.accentHover}"
    textColor: "{colors.onDark}"
    typography: "{typography.nav}"
    rounded: "{rounded.md}"
    padding: "8px 14px"
  button-primary-hover:
    backgroundColor: "{colors.accent}"
    textColor: "{colors.onDark}"
  button-primary-active:
    backgroundColor: "{colors.accentPressed}"
    textColor: "{colors.onDark}"
  button-dark-arrow:
    backgroundColor: "{colors.inkStrong}"
    textColor: "{colors.onDark}"
    rounded: "{rounded.round}"
    size: 36px
  card-base:
    backgroundColor: "{colors.card}"
    textColor: "{colors.text}"
    rounded: "{rounded.lg}"
    padding: "{spacing.xl}"
  input-default:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.text}"
    typography: "{typography.body}"
    rounded: "{rounded.md}"
    padding: "10px 12px"
    height: 44px
---

1. Source

- URL: https://www.notion.so, redirected to https://www.notion.com/
- Date: 2026-05-07
- Page: Notion homepage, current messaging "The AI workspace that works for you" with hero "Meet the night shift." and focus on Notion Agents, AI Search, Meeting Notes, Docs, Knowledge Base, Projects, productivity calculator, testimonials, and download cards.
- Basis: live HTML/CSS, browser snapshot, visual inspection of the hero, middle, and footer sections. An existing local Notion design.md specification was used for comparison, but current tokens were adjusted to match the observed notion.so/notion.com page.

2. Brand DNA

Visual Identity

Notion feels like a document-based work product that is intentionally staged more dramatically for the AI-agents campaign: a very dark "night shift" hero with white display typography, blue CTA, and floating agent illustrations meets light, calm workspace sections with flat white cards. The brand stays documentary and minimal, but gains more playful energy through colourful agent icons, coloured product surfaces, and hand-drawn lines.

Core DNA:

- Document/workspace first: cards, tables, lists, checkboxes, tabs, sidebars, and product mockups are the primary visual material.
- AI agents as small helpers: round colourful icons, cartoon agents, sparkles, wires/cables, and carousel motion tell the story "work keeps going".
- Light/dark contrast: the hero is almost night-dark; below it, white/off-white with black headlines dominates.
- Flat rather than glossy: cards are separated mostly by radius, border, colour, and space — not heavy shadows.
- Editorial credibility: testimonials use Lyon Text serif, large quotes, and wide calm cards.

Layout Principles

- Max-width approx. 1180–1280px, generous horizontal gutters.
- Sections start with large, very bold headlines and generous top spacing.
- Product modules are bento-like: 1 large feature, followed by 2- or 3-column grids, occasionally wide cards.
- Repeating card structure: white text header + coloured product stage with abstracted UI layers.
- Navigation and footer areas remain simple so the product modules stand out.

Mood / Product Feel

- Productive, active at night, automating.
- Accessible and friendly, not enterprise-cold.
- Intelligent, but not futuristic-metallic.
- Serious enough for Forbes Cloud 100, playful enough for custom agents.
- Workspace tool with its own handwriting: monochrome base plus colourful Notion database/agent signals.

3. Semantic Tokens

Core Tokens

| Role | Token | Value | Observation / Usage |
|---|---|---:|---|
| accent | --accent | #097FE8 | Primary CTA/action colour on the current page, buttons, badge/text accents. |
| accent hover | --accent-hover | #0075DE | CSS variable for focus/hover/link accent. |
| accent pressed | --accent-pressed | #005BAB | Active button/pressed state. |
| ink/text | --ink | #191918 | Notion warm black, body/footer and light sections. |
| strong text | --ink-strong | #000000 | Very strong headlines, arrow buttons. |
| text | --text | #000000E6 | CSS-observed primary text rgba(0,0,0,.9). |
| muted text | --text-muted | #0000008A | Secondary text, descriptions, disabled UI. |
| subtle text | --text-subtle | #00000059 | Labels, weaker metadata. |
| canvas/background | --canvas | #FFFFFF | Main page surface and cards. |
| dark page / footer body base | --page-dark | #191918 | Body background at page edge and dark base. |
| hero background | --hero-navy | #02093A | Dark AI/night hero. |
| surface/card wash | --surface | #F6F5F4 | Light sections, ghost hover, result surfaces. |
| surface soft | --surface-soft | #F9F9F8 | Very subtle card/section surface. |
| accent soft | --surface-accent-muted | #F2F9FF | Soft blue button/badge background. |
| surface/card | --card | #FFFFFF | Standard cards, testimonials, calculator. |
| border | --border | #0000001A | 1px hairlines, card borders, checkboxes. |
| border strong | --border-strong | #DFDCD9 | Inputs, stronger dividers. |
| on dark | --on-dark | #FFFFFF | Text on hero and dark custom agent card. |
| on dark muted | --on-dark-muted | #FFFFFFBF | Sub-headline on dark hero. |

Product and Campaign Colours

| Role | Value | Usage |
|---|---:|---|
| agent blue | #455DD3 | Campaign/agent blue, hero illustrations. |
| light blue | #62AEF0 | AI Meeting Notes, UI layers, agent icon. |
| link blue | #0075DE | Inline links such as language switcher and pricing link. |
| red/search | #F64932 | Enterprise Search, error, alert agent. |
| orange | #FF6D00 | Agents, warning, Notion agent visuals. |
| orange deep | #DD5B00 | Stronger warning/product accents. |
| yellow | #FFB110 | Agent/assistant card, highlights. |
| teal | #2A9D99 | Docs product surface. |
| green/success | #1AAE39 | Success, reporting agent, activating signals. |
| pink | #FF64C8 | Agent/AI accent, mascot. |
| purple | #AD6DED | Agent/AI accent, decorative badges. |
| brown/projects | #9C7054 | Projects product surface, warm management patterns. |
| success | #1AAE39 | Positive status, activated/successful states. |
| warning | #FF6D00 | Warning, orange agents, price/tool indicators. |
| error | #F64932 | Errors, security alerts, danger states. |

Note: On the current homepage, blue (#097FE8/#0075DE) is semantically the strongest CTA/action colour. Older Notion extracts with a purple CTA are more typical of earlier campaigns or other page states.

4. Typography

Font Notes

- Sans: NotionInter, Inter, -apple-system, BlinkMacSystemFont, Segoe UI, Helvetica, Arial, sans-serif.
- Serif: Lyon Text, Georgia, YuMincho, Hiragino Mincho ProN, Songti SC, SimSun, serif. Observed in quote/testimonial moments.
- Mono: iA Writer Mono, Nitti, Menlo, Courier, monospace. Derived from CSS for code/developer/terminal-adjacent surfaces.

Size Logic

| Level | Value | Weight | Line-height | Role |
|---|---:|---:|---:|---|
| Hero Display | 64px desktop observed | 700 | 1.0 | "Meet the night shift." |
| Global Heading LG | 54px / 3.375rem | 700 | 3.5rem | Large section headlines. |
| Sans 700 | 42px / 2.625rem | 600-700 | 3rem | Primary title in card/article context. |
| Sans 600 | 32px / 2rem | 600-700 | 2.5rem | Large card/subsection titles. |
| Sans 500 | 26px / 1.625rem | 700 | 2rem | Quote/card titles, secondary headlines. |
| Body | 16px | 400 | 24px | Body, product text, UI content. |
| Nav/Button | 14px | 500 | 20px | Navigation, buttons, footer links. |
| Caption | 12px | 500 | 16px | Labels, dropdown groups, meta. |
| Quote | 32px Serif | 400 | 40px | Large testimonial voice. |

Hierarchy

- Display headlines are massive, tightly set, and mostly black or white.
- Body text is significantly smaller and grey/semi-transparent so cards remain calm.
- UI components use 14–16px, rarely larger.
- The testimonial quote deliberately uses serif type to create editorial quality and credibility.
- Navigation and footer are compact, almost document-like.

5. Layout System

Grid

- Desktop container: approx. 1180–1280px maximum width.
- Gutters: 24–32px, mobile 16–20px.
- Main pattern: 12-column thinking, implemented as 1-up hero, 2-up cards, 3-up/5-up use-case tiles, 6-column footer.
- Feature card grids: one large 1-up card, then 2-up cards; later 2-up plus a wide projects card.
- Testimonials: 1 wide main card, then a 3×2 grid of small quote cards.
- Download: 2-column layout, large card on the left, 2 smaller stacked cards on the right.

Max-Width and Section Rhythm

- Hero: full-width dark band, content centred; mockup wide below the headline.
- Sections: 80–120px vertical spacing between main blocks.
- Card-internal padding: 24–48px depending on size.
- Calculator/testimonial/download sections use generous whitespace so controls do not feel cramped.

Spacing Scale

- 4px micro unit.
- 8px small spacing in controls.
- 12px list/checkbox/label spacing.
- 16px standard component spacing.
- 24px card and grid gaps.
- 32px larger inner spacing.
- 48px large card/hero inner spacing.
- 96–120px section/hero rhythm.

6. Components

Buttons

1. Primary CTA Button
- Blue #097FE8, white text, 14px/500, radius 6px, height approx. 36–40px, padding 8–14px.
- Usage: "Get Notion free", "Download for Mac".
- Hover/Active: #0075DE / #005BAB.

2. Secondary CTA on Dark
- Dark blue/transparent on hero, white text, fine light border or dark button contrast.
- Usage: "Request a demo" in the hero.

3. Text Link Button
- Transparent background, link blue #0075DE, right-pointing arrow.
- Usage: "See pricing plans", "Read the full story", language switcher.

4. Black Circular Arrow Button
- Black circle, white arrow, approx. 36–44px diameter.
- Recurring card CTA in carousel, feature cards, and product cards.

5. Carousel Next Button
- White or light round button at the edge of a product stage, dark icon.
- Appears floating but without strong shadows.

6. Pause/Play Control
- Small round button bottom right in the carousel, play/pause icon, controls video/auto-animation.

7. Download Button
- Blue, compact rectangular button, with Apple icon for Mac download.

8. Cookie Buttons
- Cookie bar with "Accept all", "Reject all", "More options". Overlay-like, higher z-index, clear button hierarchy.

Cards

9. Hero Product Mockup Card
- Wide desktop window with Notion UI, browser/app chrome, tabs/toolbar, and embedded board/agent workspace.
- Radius 12–16px, distinct soft shadow/glow against the dark hero.

10. Custom Agents Carousel Card
- Split in two: white text and tab area on the left, coloured demo stage on the right.
- Radius 12px, flat border, generous inner padding.

11. Agent Tab Row
- List of four clickable agent types, each with icon + title + description, active row more prominent.
- Fine dividers between rows.

12. Chat Answer Card
- Foreground chatbox above a greyed-out Notion table, white background, soft shadow.
- Contains user avatar, assistant icon, question text, and answer.

13. Use-Case Tile
- Small white card with border, icon on top, bold title, arrow.
- 5-up row on desktop, one dark navy variant for "Create your own Custom Agent".

14. Feature Product Card Large
- White header area plus coloured visual stage.
- Examples: Notion Agent, Enterprise Search, AI Meeting Notes, Docs, Knowledge Base, Projects.
- Radius 12px, click target is the entire card.

15. Tinted Product Stage
- Large colour field within the card: yellow/orange/red/blue/teal/brown.
- Abstracted UI layers with transparency instead of real screenshots.

16. Testimonial Hero Card
- Large white card on a light grey section, large Lyon Text quote, link and play icon.

17. Testimonial Mini Card
- 3×2 grid, quote/claim with arrow, generous padding, minimal decoration.

18. Trust Metric Item
- Small horizontal claim items with icon and text, grey/black, social proof strip.

19. Download Main Card
- Large light card for Notion Desktop/App, icon, title, description, blue download button, and pale mockup surface.

20. Download Product Card
- Smaller cards for Notion Mail and Calendar, icon, copy, button, pale product visuals on the right.

Nav

21. Top Language Banner
- Slim strip: "View this page in your preferred language." + link "Switch to German".
- Light/neutral text, minimal intrusion into the layout.

22. Main Navigation
- 64px tall, Notion logo on the left, dropdown links Product/AI/Solutions/Resources, static links Enterprise/Pricing/Request a demo, Login and CTA on the right.
- On the hero against a dark background, labels white/light grey.

23. Mega Dropdown
- White panel with product links, subtitles, small icons, and bottom promo rows.
- Product dropdown shows: Notion, Calendar, Mail, AI, Agents, AI Meeting Notes, Enterprise Search, Knowledge Base, Docs, Projects, Integrations, Security.

Hero

24. Night Shift Hero
- Full-width dark navy, centred headline/sub-headline/buttons.
- Floating agent icons, hand-drawn lines, spotlight/glow, large product mockup.

Forms

25. Calculator Checkbox
- Small square checkboxes; active: blue with white tick; inactive: white surface with grey outline.

26. Team Size Number Input
- Numeric input/stepper with value 10, fine border, column label.

27. Search/Input Pattern
- Derived from Enterprise Search and CSS: 44px height, white or surface-accent-muted, radius 6px, border #DFDCD9, focus #097FE8.

28. Footer Language Select
- Compact dropdown button with globe/language icon and chevron.

Modals/Dropdowns

29. Cookie Consent Overlay
- Overlay/modal banner, lower than cards, with multiple button actions.

30. Nav Dropdown Panel
- Mega-menu as a popover below the nav, white background, column/list layout, 14px text, subtle hover surfaces.

7. Brand-specific Product Patterns

1. Night-shift AI narrative
- The hero is not a generic SaaS hero. It tells the story that agents work at night: dark background, "Meet the night shift", floating small agents, cables/wires, product window as control centre.

2. Agents as UI characters
- Notion uses colourful small figures/badges for agents. They are round, friendly, slightly cartoon-like, and appear in the hero, carousel, use-case tiles, and dark custom agent card.

3. Product mockup in card instead of pure illustration
- Almost every large visual surface is either a real Notion UI mockup or an abstracted version of one: tables, chat, sidebars, cards, UI layers.

4. Black circular arrow as card CTA
- Recurring, specific pattern: not blue links in cards, but a black circle with a white arrow. This makes product cards clearly clickable and keeps the card visually monochrome in the header area.

5. White header zone plus coloured stage
- Feature cards have calm product copy at the top/left and a large coloured stage with UI layers. The colour signals the product family: Search red, Meeting Notes blue, Docs teal, Projects brown.

6. Calculator as ROI argument, not a form
- The "More productivity. Fewer tools." calculator is a product component with checkboxes, price labels, and savings output. It connects Notion design with business value.

7. Serif quote moment
- The brand is otherwise sans/workspace. The large testimonial deliberately switches to Lyon Text to create an editorial, credible moment.

8. Trust logos below the product mockup
- Social proof sits directly below the hero mockup, not in a separate generic logo wall. This makes the product screen appear as the reason for trust.

9. Mega-dropdown as product map
- The product dropdown is not a simple menu. It is a condensed information architecture map of the product family with subtexts and promo notes.

10. Flat database colours
- Colourful surfaces are vivid but not glossy. They evoke Notion database properties and status colours.

8. Motion / Interaction

Observed

- Hero contains video/product mockup with play button.
- Custom Agents Carousel has tabs, next-slide button, and play/pause control.
- Feature cards are fully clickable and have an arrow CTA.
- Calculator checkboxes update savings dynamically.
- Number input/stepper changes team size.
- Nav dropdowns open mega-menus.
- Cookie banner opens accept/reject/more options.

Derived Interaction Tokens

- Transitions: 150–200ms ease-out for hover, dropdown, button colour changes.
- Hover button: blue from #097FE8 to #0075DE, active to #005BAB.
- Card hover: no strong shadow; rather strengthen border/background slightly or move the arrow button.
- Carousel motion: horizontal slide/fade transition, 300–500ms, pause control must display state.
- Dropdown: 120–180ms fade/translateY, white surface, subtle shadow or border.
- Focus: 2px outline/border in #097FE8, not purple.

9. Implementation Notes

Concrete CSS Tokens

```css
:root {
  --notion-accent: #097FE8;
  --notion-accent-hover: #0075DE;
  --notion-accent-active: #005BAB;
  --notion-ink: #191918;
  --notion-text: #000000E6;
  --notion-muted: #0000008A;
  --notion-subtle: #00000059;
  --notion-canvas: #FFFFFF;
  --notion-surface: #F6F5F4;
  --notion-surface-soft: #F9F9F8;
  --notion-border: #0000001A;
  --notion-border-strong: #DFDCD9;
  --notion-hero-navy: #02093A;
  --notion-red: #F64932;
  --notion-orange: #FF6D00;
  --notion-yellow: #FFB110;
  --notion-blue-400: #62AEF0;
  --notion-teal: #2A9D99;
  --notion-green: #1AAE39;
  --notion-pink: #FF64C8;
  --notion-purple: #AD6DED;
  --notion-brown: #9C7054;

  --font-sans: NotionInter, Inter, -apple-system, BlinkMacSystemFont, "Segoe UI", Helvetica, Arial, sans-serif;
  --font-serif: "Lyon Text", Georgia, YuMincho, "Hiragino Mincho ProN", serif;
  --font-mono: "iA Writer Mono", Nitti, Menlo, Courier, monospace;

  --radius-sm: 5px;
  --radius-md: 6px;
  --radius-card: 12px;
  --radius-large: 16px;
  --radius-round: 9999px;

  --space-1: 4px;
  --space-2: 8px;
  --space-3: 12px;
  --space-4: 16px;
  --space-6: 24px;
  --space-8: 32px;
  --space-12: 48px;
  --section: 96px;

  --shadow-subtle: 0 1px 2px rgba(0,0,0,.06);
  --shadow-card: 0 8px 24px rgba(0,0,0,.08);
  --shadow-hero-mockup: 0 24px 64px rgba(0,0,0,.35);
  --transition-fast: 160ms ease-out;
}
```

Component Structure

```text
Page
  LanguageBanner
  HeaderNav
    Logo
    NavDropdownButton(Product/AI/Solutions/Resources)
    NavLink(Enterprise/Pricing/RequestDemo)
    NavActions(Login, PrimaryCTA)
    MegaDropdown
  HeroNightShift
    DecorativeAgentNetwork
    HeroCopy
    CTAGroup
    ProductMockupVideoCard
    TrustLogoStrip
  CustomAgentsSection
    AgentCarousel
      AgentTabList
      DemoStage(ChatOverTable)
      CarouselControls
    AgentUseCaseTiles
  ProductBentoSection
    FeatureCard(NotionAgent, yellow/orange)
    FeatureCard(EnterpriseSearch, red)
    FeatureCard(AIMeetingNotes, blue)
    FeatureCard(Docs, teal)
    FeatureCard(KnowledgeBase, blue)
    FeatureCard(Projects, brown)
  ProductivityCalculator
    ToolCheckboxGrid
    ResultPanel(TeamSize, MonthlySavings, AnnualSavings)
  Testimonials
    HeroQuoteCard
    TestimonialGrid
    TrustMetricStrip
  TryForFree
    DownloadMainCard
    DownloadProductCard(Mail)
    DownloadProductCard(Calendar)
  Footer
    BrandColumn
    SocialLinks
    LanguageSelect
    LinkColumns
```

Do

- Use #097FE8 as the current action/CTA accent.
- Keep base surfaces monochrome: white, #F6F5F4, #191918.
- Apply colour by product context: red for Search/Security, blue for Notes/AI, teal for Docs, brown for Projects, orange/yellow for agents.
- Use NotionInter for almost everything and Lyon Text only for quotes/editorial voices.
- Build product visuals as real UI layers: tables, cards, sidebar, chat, checkboxes — not abstract gradient blobs alone.
- Use round black arrow buttons in feature cards.
- Use flat borders instead of shadows everywhere.

Don't

- No generic Stripe/Linear gradient look.
- Do not make all buttons pill-shaped; Notion buttons are compact rectangles with a small to medium radius.
- Do not force purple as the current primary CTA when the homepage uses blue.
- No heavy glassmorphism effects on light cards.
- Do not just swap logos/colours: Notion requires sidebar, document, database, chat, and agent patterns.
- No decorative illustrations without a product reference. Even colourful surfaces must suggest UI layers.

Stripe-style Documentation Sections for a Preview

1. Sticky Navigation: dark hero context + mega-dropdown demo.
2. Hero: night-shift story with product mockup and agent network.
3. Meta Strip: "AI workspace", "Agents", "Search", "Docs/Projects".
4. Colors: Semantic Tokens plus product colours.
5. Typography: NotionInter and Lyon Text live.
6. Buttons: Primary, secondary-on-dark, text-link, circular arrow, disabled, focus.
7. Cards: Hero mockup, carousel, use-case tile, feature card, testimonial, download.
8. Product Patterns: Agent carousel, calculator, feature bento, mega-dropdown.
9. Forms: Checkbox grid, number input, search field, select, cookie controls.
10. Spacing/Radius/Elevation: flat borders plus hero mockup shadow.
11. Extracted Component Tokens: Header, Hero, Cards, Calculator, Footer.

10. Accuracy Check

Directly Observed

- URL redirects to notion.com; title: "The AI workspace that works for you. | Notion".
- Hero text: "Meet the night shift.".
- Hero sub-text: "Notion agents keep work moving 24/7. They capture knowledge, answer questions, and push projects forward-all while you sleep."
- CTA text: "Get Notion free", "Request a demo".
- Nav: Product, AI, Solutions, Resources, Enterprise, Pricing, Request a demo, Log in, Get Notion free.
- Product dropdown content: Notion, Notion Calendar, Notion Mail, Notion AI, Agents, AI Meeting Notes, Enterprise Search, Knowledge Base, Docs, Projects, Integrations, Security.
- Main sections: Keep work moving 24/7; See what Custom Agents can do; Ask your on-demand assistants; Bring all your work together; More productivity. Fewer tools; Trusted by teams that ship; Try for free; Footer.
- Components: Carousel tabs, play/pause, next slide, agent use-case tiles, feature cards, productivity calculator, checkboxes, number input, testimonial cards, download cards, footer language select, cookie banner.
- CSS fonts: NotionInter, Lyon Text, iA Writer Mono.
- CSS/computed colours: #097FE8, #0075DE, #005BAB, #191918, #F6F5F4, #F9F9F8, #DFDCD9, #A39E98, #78736F, #F64932, #FF6D00, #FFB110, #2A9D99, #1AAE39, #FF64C8, #AD6DED.
- Computed hero H1: 64px, 700, white, NotionInter.
- Article cards: white background, radius 12px, flat shadows.

Derived

- Exact desktop max-width approx. 1180–1280px.
- Hero navy #02093A from CSS/pixel colours, not guaranteed as the only solid value.
- Hover and motion timings 150–200ms/300–500ms are derived from typical web behaviour, not directly measured.
- Some component shadow levels are implementation values estimated from visual depth.
- Search/input pattern is derived from CSS variables and visible product patterns, not observed as a separate form field in the hero.

Uncertain

- The concrete visual representation may vary depending on A/B test, language, region, cookie state, and login state.
- Older local Notion designs sometimes use purple CTA roles; this extraction prioritises the currently observed homepage with blue CTA.
- Decorative agent illustrations are visually observed, but exact SVG colours and path geometries were not fully isolated from the assets.
- Mobile breakpoints were not tested live; responsive behaviour is derived from layout structure and common Notion patterns.

Source: www.designmd-store.com
