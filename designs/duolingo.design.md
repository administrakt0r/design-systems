---
version: alpha
name: Duolingo
slug: duolingo-com
source: https://www.duolingo.com
extractedAt: 2026-05-07
description: Playful, gamified learning system with Duo Green, rounded brand fonts, 3D cartoon illustrations, button bottom-edges, and a modular feature rhythm.
colors:
  primary: "#58CC02"
  secondary: "#1CB0F6"
  tertiary: "#FFC800"
  neutral: "#FFFFFF"
  accent: "#58CC02"
  accentHover: "#61E002"
  accentPressed: "#46A302"
  accentShadow: "#58A700"
  ink: "#3C3C3C"
  inkStrong: "#4B4B4B"
  muted: "#777777"
  mutedLight: "#AFAFAF"
  canvas: "#FFFFFF"
  wash: "#DDF4FF"
  surface: "#FFFFFF"
  surfaceAlt: "#F7F7F7"
  border: "#E5E5E5"
  borderStrong: "#DADADA"
  link: "#1CB0F6"
  linkPressed: "#1B99D6"
  navy: "#042C60"
  superNavy: "#100F3E"
  superInk: "#000437"
  footerTextSoft: "#D7FFB8"
  success: "#58CC02"
  warning: "#FFC800"
  error: "#FF4B4B"
  streak: "#FF9600"
  gems: "#CE82FF"
typography:
  display:
    fontFamily: feather, din-round, sans-serif
    fontSize: 64px
    fontWeight: 700
    lineHeight: 1.05
    letterSpacing: "-0.01em"
  headline-lg:
    fontFamily: feather, din-round, sans-serif
    fontSize: 48px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: "-0.005em"
  hero:
    fontFamily: din-round, sans-serif
    fontSize: 32px
    fontWeight: 700
    lineHeight: 1.375
    letterSpacing: "0em"
  body:
    fontFamily: din-round, sans-serif
    fontSize: 17px
    fontWeight: 500
    lineHeight: 24px
  label:
    fontFamily: din-round, sans-serif
    fontSize: 15px
    fontWeight: 700
    lineHeight: 1
    letterSpacing: "0.02em"
rounded:
  sm: 8px
  md: 12px
  lg: 16px
  xl: 24px
  pill: 999px
spacing:
  xs: 8px
  sm: 16px
  md: 24px
  lg: 40px
  xl: 48px
  section: 96px
  super: 185px
layout:
  maxWidth: 988px
  wideWidth: 1090px
  heroColumns: 424px 480px
  featureColumns: 503px 530px
components:
  button-primary:
    backgroundColor: "{colors.accent}"
    textColor: "#FFFFFF"
    rounded: "{rounded.md}"
    height: 50px
    padding: 0 16px
  button-primary-pressed:
    backgroundColor: "{colors.accentPressed}"
    textColor: "#FFFFFF"
    rounded: "{rounded.md}"
    height: 50px
    padding: 0 16px
  button-secondary:
    backgroundColor: "#FFFFFF"
    textColor: "{colors.link}"
    rounded: "{rounded.md}"
    height: 50px
    padding: 0 16px
  app-store-badge:
    backgroundColor: "#FFFFFF"
    textColor: "{colors.inkStrong}"
    rounded: "{rounded.md}"
    height: 63px
    padding: 9.5px 14px
  super-button:
    backgroundColor: "#FFFFFF"
    textColor: "{colors.superInk}"
    rounded: "{rounded.md}"
    height: 50px
    padding: 0 16px
---

# Duolingo Design System Extraction

## 1. Source

- URL: https://www.duolingo.com
- Date: 2026-05-07
- Page: German Duolingo homepage with hero, course carousel, feature sections, app download, Super Duolingo promo, product blocks, final CTA, and green footer.
- Direct technical observation: computed CSS names `din-round, sans-serif` as the base font and `feather, sans-serif` for large green headlines. Visible colours from DOM: `rgb(88, 204, 2)`, `rgb(28, 176, 246)`, `rgb(60, 60, 60)`, `rgb(119, 119, 119)`, `rgb(221, 244, 255)`, `rgb(16, 15, 62)`, `rgb(4, 44, 96)`.

## 2. Brand DNA

### Visual Identity
Duolingo is a friendly learning game, not just a learning platform. The website combines an almost empty-feeling white canvas with extremely saturated cartoon accents. The brand is carried primarily through Duo Green, mascot logic, reward objects, rounded letterforms, and large illustrations. Classic SaaS UI elegance steps back in favour of gamification, cuteness, optimism, and instant accessibility.

### Layout Principles
- Generous, centred max-width of approx. 988px.
- Hero as a 2-column module with illustration on the left and CTA on the right.
- Below it, a horizontal language/course carousel as compact product navigation.
- Feature sections alternate text/image direction and remain borderless.
- App download section breaks the grid in favour of a centred atmosphere block with floating devices.
- Super Duolingo uses a dark full-bleed contrast block.
- Final CTA transitions visually into the green footer landscape.

### Mood / Product Feel
Playful, motivating, freely accessible, rewarding, harmless, optimistic. The product feel is "daily learning as a small game": short lessons, streaks, hearts, coins, progress, friendly reminders.

## 3. Semantic Tokens

| Role | Token | Value | Usage |
|---|---:|---:|---|
| accent | `--duo-green` | `#58CC02` | Primary CTA, headlines, footer, success |
| accent pressed | `--duo-green-dark` | `#46A302` | Pressed buttons, shadow edge |
| accent shadow | `--duo-green-shadow` | `#58A700` | Duolingo 3D bottom-edge on buttons |
| ink/text | `--ink` | `#3C3C3C` | Default text, interface labels |
| strong ink | `--ink-strong` | `#4B4B4B` | Hero headline |
| canvas/background | `--canvas` | `#FFFFFF` | Main page surface |
| wash | `--wash-blue` | `#DDF4FF` | Subtle atmospheric background surfaces |
| surface/card | `--surface` | `#FFFFFF` | Buttons, badges, cards |
| border | `--border` | `#E5E5E5` | Course strip, secondary buttons, dividers |
| strong border | `--border-strong` | `#DADADA` | Secondary button bottom edge |
| muted text | `--muted` | `#777777` | Paragraphs, course labels |
| muted light | `--muted-light` | `#AFAFAF` | Language dropdown in header |
| link | `--link-blue` | `#1CB0F6` | Secondary CTA text, text links |
| link pressed | `--link-blue-dark` | `#1B99D6` | Active link buttons |
| navy | `--navy` | `#042C60` | App section headline |
| super bg | `--super-navy` | `#100F3E` | Premium/Super Duolingo section |
| footer soft | `--footer-soft` | `#D7FFB8` | Footer links |
| success | `--success` | `#58CC02` | Correct, progress, check |
| warning | `--warning` | `#FFC800` | Coins, rewards |
| error | `--error` | `#FF4B4B` | Errors, heart loss |
| streak | `--streak` | `#FF9600` | Flame, streak |

## 4. Typography

- Base font: `din-round, sans-serif`, observed on body, buttons, navigation, and body text.
- Headline font: `feather, sans-serif`, observed on large green headlines and the app headline.
- Hero H1: 32px, 700, dark grey, centred, approx. 480px wide.
- Feature H2: 48px, 700, green, generous line-height, deliberately short lines.
- App H1: 64px, 700, `#042C60`, centred.
- Body: 17px, 500, 24px line-height, grey `#777777`, narrow reading width of approx. 473px.
- Buttons: 15px, 700, uppercase, compact, high contrast.
- Language/course strip: 17px, grey, uppercase labels with flags/icons.

## 5. Layout System

- Header height: approx. 72px, white, minimal, logo on the left, language dropdown on the right.
- Max-width: approx. 988px for main content, 1090px for course navigation.
- Hero: approx. 520px tall, padding 48px 0, 424px illustration plus 480px CTA column.
- Feature section: approx. 530px block height, text column approx. 503px, illustration column approx. 530px.
- Section rhythm: feature group with 96px vertical padding.
- Super block: full width, 900px height, 185px vertical padding inside.
- Buttons: often 330px wide in the hero and secondary CTAs, 50px tall.
- Forms/controls should follow this rhythm: 50px height, 12px radius, strong bottom edge.

## 6. Components

### Buttons
1. Primary CTA: green, white text, 12px radius, 50px height, 4px darker bottom edge.
2. Primary hover: slightly lighter green, bottom edge stays dark.
3. Primary pressed: `translateY(4px)`, bottom edge disappears.
4. Secondary CTA: white, blue text, grey border/bottom edge.
5. Secondary hover: very light blue wash, blue border.
6. Super CTA: white on dark navy, dark text, same 3D edge.
7. App store badge: white, 63px tall, icon plus two-line text.
8. Icon round button: round arrows for the course carousel, grey outline.

### Cards / Surfaces
9. Lesson path card: rounded light card with progress bar and round level nodes.
10. Leaderboard card: ranking with avatar circles, XP numbers, green highlight.
11. Streak card: flame icon, day counter, orange/yellow accents.
12. Reward card: coins, badge, positive green checkmark.
13. Skill tile: small, round learning tile with icon, shadow edge.
14. Product card: borderless 2-column section with illustration and text.
15. Super card: dark violet-blue premium card with gradient heart/infinity.
16. App device card: floating smartphone with blue UI surface.
17. Test certificate badge: green round seal with white Duo silhouette.
18. ABC learning card: child-like book/block card with large icons.
19. Footer link column: green surface, white heading, soft-green links.
20. Language chip: flag/icon plus uppercase course label in a horizontal rail.
21. Progress module: green progress bar with a soft track.
22. Error feedback card: red error line, still rounded and friendly in form.
23. Empty state: Duo icon, short motivating copy, primary CTA.
24. Modal shell: white, 24px radius, 4px border edge, centred Duo icon.

### Nav
- Minimal header without a flood of links.
- Logo link on the left, language dropdown on the right in light-grey uppercase text.
- Course carousel directly below the hero with dividers top/bottom, arrows, and flags.

### Hero
- Illustration with Duo and learning objects on the left.
- Right column: large dark headline, primary CTA, secondary login.
- No complex background — the illustration supplies the energy.

### Forms
- Input height 50px, 12px radius, `#E5E5E5` border plus 3D bottom edge.
- Focus: blue ring/border `#1CB0F6`, subtle light-blue background.
- Error: red text `#FF4B4B`, border red, small friendly error message.
- Checkbox/radio: large, round, green in the active state.

### Modals/Dropdowns
- Language dropdown: uppercase trigger in `#AFAFAF`, dropdown as a white card with rounded corners and a list of languages.
- Login/start modal (derived): centred dialog, Duo icon on top, 330px button width, strong vertical button list.

## 7. Brand-specific Product Patterns

1. Duo as an emotional trust anchor: the mascot replaces abstract SaaS symbolism.
2. Gamification rail: languages, levels, streaks, coins, hearts, and checkmarks are not decorative — they are product semantics.
3. Button with a physical bottom edge: the CTA feels like a game button.
4. Alternating learning arguments: every product claim is explained with a playful app/learning image.
5. Super Duolingo as its own mode: dark full-bleed block with neon gradient instead of standard green branding.
6. Footer as a landscape: the conversion section transitions into a green hills/footer world.
7. Learning courses as flag chips: internationality is shown through horizontal, scannable course labels.
8. No photographic aesthetic: people are abstracted as figures/characters.
9. Friendly errors: even error and warning states should feel playful, rounded, and non-aggressive.
10. Motivation before function: UI patterns show progress, reward, and habit more prominently than feature lists.

## 8. Motion / Interaction

Directly visible: hover is not measurable in the static screenshot, but the button construction implies typical Duolingo interaction.

- Buttons: hover slightly lighter, active presses down 4px and loses the bottom edge.
- Course carousel: horizontal scrolling with arrow buttons.
- Dropdown: language selection opens a list/popover.
- Floating illustrations: should gently float or appear with a soft parallax effect if animated.
- Focus states: clear blue outline for secondary controls, green outline for the primary positive action.
- Microcopy/feedback: small pop-bounces on success, streak, and reward.

## 9. Implementation Notes

### CSS Tokens

```css
:root {
  --duo-green: #58CC02;
  --duo-green-dark: #46A302;
  --duo-green-shadow: #58A700;
  --ink: #3C3C3C;
  --ink-strong: #4B4B4B;
  --muted: #777777;
  --muted-light: #AFAFAF;
  --canvas: #FFFFFF;
  --wash-blue: #DDF4FF;
  --surface: #FFFFFF;
  --border: #E5E5E5;
  --border-strong: #DADADA;
  --link-blue: #1CB0F6;
  --link-blue-dark: #1B99D6;
  --navy: #042C60;
  --super-navy: #100F3E;
  --warning: #FFC800;
  --error: #FF4B4B;
  --streak: #FF9600;
  --radius-control: 12px;
  --max: 988px;
}
```

### Component Structure

- `Header`: Logo, LanguageDropdown.
- `Hero`: IllustrationCluster, HeroCopy, CTAStack.
- `CourseRail`: ArrowButton, CourseChip[]
- `FeatureSection`: IllustrationPanel, TextPanel, optional Button.
- `AtmosphereDownload`: FloatingDevice[], StoreBadge[].
- `SuperPromo`: SuperCard, GradientLogo, SuperButton.
- `ProductBlock`: ProductIllustration, ProductCopy, SecondaryButton.
- `FinalCTA`: RewardDecorations, PrimaryButton, FooterBridge.
- `Footer`: LinkColumn[], LanguageLinks.

### Do

- Use rounded shapes, saturated accents, and generous whitespace.
- Let illustrations explain product mechanics.
- Keep buttons physical and tactile with a bottom edge.
- Use green for primary actions and blue for secondary navigation/links.
- Write CTAs in short, bold uppercase.

### Don't

- Do not turn it into a generic SaaS gradient template.
- No thin, elegant corporate typography instead of the rounded learning-game font.
- No heavy shadows on feature sections — the page is mostly flat.
- Do not make every surface green; green is the accent plus footer, whitespace is equally important.
- Do not use photography or realistic depictions of people.

## 10. Accuracy Check

### Directly Observed
- URL, German text, hero, course strip, feature sections, app download, Super Duolingo, English Test, Schools, ABC, final CTA, footer.
- Computed colours and fonts: `din-round`, `feather`, `#58CC02`, `#1CB0F6`, `#3C3C3C`, `#777777`, `#DDF4FF`, `#100F3E`, `#042C60`, `#E5E5E5`.
- Button height 50px, radius 12px, hero CTA width 330px, content width 988px, feature H2 48px, app H1 64px, body 17px/24px.

### Derived
- Exact hover/pressed motion from the typical Duolingo button model and the visible 3D bottom edge.
- Product-internal cards such as lesson path, streak card, reward card, and error card as design-system-compliant demo components — not all visible on the landing page.
- Modal/form specification derived from observed control tokens and Duolingo product logic.

### Uncertain
- Exact proprietary font files and licence terms cannot be derived from the screenshot.
- Exact icon assets/illustration files are rebuilt in the preview, not copied.
- Live animations were not fully triggered; motion is partially derived from component semantics.

Source: www.designmd-store.com
