# 🎨 Design Systems Catalog

> **31 real-world, production-tested brand design systems** extracted from world-class tech companies, financial institutions, and digital platforms.
> Standardized as machine-readable `.design.md` token specifications, ready for **AI Coding Assistants** (Claude Code, Antigravity, Cursor, Windsurf, GitHub Copilot) and **Frontend Engineering** (CSS Variables, Tailwind CSS, Design Tokens).

[![Specs](https://img.shields.io/badge/Specs-31%20Brand%20Systems-635bff.svg)](#-index-of-design-systems)
[![Format](https://img.shields.io/badge/Format-.design.md%20(YAML%20%2B%20Markdown)-1f883d.svg)](#-specification-anatomy-designmd)
[![CSS Included](https://img.shields.io/badge/CSS-31%20Ready--to--Use%20Stylesheets-0066cc.svg)](#-how-to-use-in-web-development)
[![License: MIT](https://img.shields.io/badge/License-MIT-gray.svg)](LICENSE)

---

## 🌟 Overview

When building modern web applications or asking AI agents to design interfaces, default styling often converges on generic, purple-gradient SaaS templates with oversized cards and poor contrast.

This repository provides **31 rigorous, high-fidelity design specifications (`.design.md`)** reverse-engineered from world-class products like **Stripe**, **Apple**, **Notion**, **Wise**, **GitHub**, **Raycast**, and **Brex**.

Each specification pairs machine-parseable YAML design tokens with detailed architectural and aesthetic guidelines so you or an AI agent can build or re-theme interfaces with authentic brand personality, proper spatial rhythm, and accessible contrast.

---

## 📂 Repository Structure

```text
design-systems/
├── catalog.json              # Machine-readable JSON manifest of all 31 systems
├── designs/                  # 31 .design.md specifications (YAML tokens + guidelines)
│   ├── stripe.design.md
│   ├── apple.design.md
│   ├── notion.design.md
│   ├── github.design.md
│   └── ...
├── dist/css/                 # Ready-to-import :root CSS custom properties
│   ├── stripe.css
│   ├── brex.css
│   ├── raycast.css
│   └── ...
├── scripts/
│   ├── export_css.py         # Compiles YAML tokens into dist/css/*.css
│   ├── build_catalog.py      # Generates catalog.json from design specs
│   └── generate_readme.py    # Builds this README.md
└── README.md
```

---

## 📋 Index of Design Systems

### FinTech & Payments (6)

| Brand | Specification | Primary / Accent | Canvas / Ink | Core Aesthetic Summary |
| :--- | :--- | :--- | :--- | :--- |
| **Brex** | [`brex.design.md`](designs/brex.design.md) | `#FF5900` / `#FF5900` | `#FCFCFD` / `#15191E` | Precise intelligent-finance system with Brex orange actions, tight Inter typography, white modular product cards, muted enterprise neutrals, and screenshot-l... |
| **Coinbase** | [`coinbase.design.md`](designs/coinbase.design.md) | `#0052ff` / `#0052ff` | `#ffffff` / `#0a0b0d` | An institutional-grade crypto exchange whose marketing surfaces read like a quietly-confident financial-services brand. The base canvas is pure white; Coinba... |
| **Mastercard** | [`mastercard.design.md`](designs/mastercard.design.md) | `#141413` / `#CF4500` | `#F3F0EE` / `#141413` | Warm editorial magazine aesthetic built from soft stone and signal orange, extreme stadium pill border radiuses, circular orbit imagery, and MarkForMC typogr... |
| **PayPal** | [`paypal.design.md`](designs/paypal.design.md) | `#003087` / `#0070E0` | `#FFFFFF` / `#001435` | Trust-first payments identity with assertive PayPal blues, black-and-white clarity, pill-shaped commerce CTAs, compact geometric typography, and modular pay,... |
| **Stripe** | [`stripe.design.md`](designs/stripe.design.md) | `#533afd` / `#635bff` | `#f6f9fc` / `#0a2540` | Precision financial-infrastructure identity with violet action color, deep navy ink, angled Stripe geometry, product UI mockups, fine dashed dividers, and de... |
| **Wise** | [`wise.design.md`](designs/wise.design.md) | `#163300` / `#9FE870` | `#FFFFFF` / `#0E0F0C` | Transparent money-product system built around vivid Wise Green, deep forest text, pill navigation, compact currency calculators, flag-led selectors, and flat... |

### Developer Platforms & Cloud (6)

| Brand | Specification | Primary / Accent | Canvas / Ink | Core Aesthetic Summary |
| :--- | :--- | :--- | :--- | :--- |
| **Cloudflare** | [`cloudflare.design.md`](designs/cloudflare.design.md) | `#ff5e1f` / `#ff7038` | `#ffffff` / `#171717` | Internet-infrastructure brand system led by Cloudflare orange, taut grotesk typography, pale technical surfaces, slim borders, tiny radii, and diagrammatic p... |
| **Framer** | [`framer.design.md`](designs/framer.design.md) | `#0099ff` / `#8555ff` | `#000000` / `#ffffff` | Dark, product-led web-building identity with electric Framer Blue, tight Geist typography, pill actions, compact glassy nav, and screenshot-heavy modules tha... |
| **GitHub** | [`github.design.md`](designs/github.design.md) | `#1f883d` / `#0969da` | `#ffffff` / `#1f2328` | Developer-native platform identity built from black-and-white GitHub brand contrast, Mona Sans typography, Primer UI density, green CTAs, blue product links,... |
| **Next.js** | [`nextjs.design.md`](designs/nextjs.design.md) | `#111111` / `#000000` | `#ffffff` / `#000000` | Developer-first monochrome system with Geist typography, terminal-coded hero moments, hairline borders, pill controls, and a disciplined split between polish... |
| **OpenAI** | [`openai.design.md`](designs/openai.design.md) | `#ffffff` / `#f9f9f9` | `#000000` / `#ffffff` | Dark, editorial AI brand system with OpenAI Sans, image-first modular news cards, quiet pill actions, flat translucent surfaces, and precise negative-tracked... |
| **Raycast** | [`raycast.design.md`](designs/raycast.design.md) | `#ff6363` / `#56c2ff` | `#07080a` / `#ffffff` | Dark, command-palette-native productivity identity with red action accents, glossy inset panels, precise 8px rhythm, huge cinematic serif hero type, and macO... |

### Productivity & Collaboration (5)

| Brand | Specification | Primary / Accent | Canvas / Ink | Core Aesthetic Summary |
| :--- | :--- | :--- | :--- | :--- |
| **Arc** | [`arc.design.md`](designs/arc.design.md) | `#25211f` / `#ff6b57` | `#faf4ed` / `#25211f` | Calm future-browser identity with warm off-white canvases, charcoal editorial type, coral pill actions, oversized product screenshots, soft app-like panels, ... |
| **ClickUp** | [`clickup.design.md`](designs/clickup.design.md) | `#202020` / `#7612FA` | `#FFFFFF` / `#090C1D` | Dense AI-work SaaS identity with ink-black CTAs, ClickUp's four-color gradient logo system, rounded modular app cards, mono product labels, and a high-volume... |
| **Notion** | [`notion.design.md`](designs/notion.design.md) | `#097FE8` / `#097FE8` | `#FFFFFF` / `#191918` | Current Notion marketing and product design: dark AI night-shift hero, light modular workspace sections, NotionInter/Lyon Text, blue CTA roles, colourful age... |
| **Slack** | [`slack.design.md`](designs/slack.design.md) | `#611F69` / `#4A154B` | `#FFFFFF` / `#1D1C1D` | Conversational AI work-platform identity built from aubergine action color, Salesforce-derived headline typography, dense rounded product UI screenshots, ben... |
| **Strawberry** | [`strawberry.design.md`](designs/strawberry.design.md) | `#252522` / `#F2805D` | `#FFFCFA` / `#252522` | Warm off-white AI-browser identity with custom Strawberry type, ink-black pill actions, coral micro-markers, rounded cream panels, animated companions, and c... |

### Entertainment & Media (4)

| Brand | Specification | Primary / Accent | Canvas / Ink | Core Aesthetic Summary |
| :--- | :--- | :--- | :--- | :--- |
| **Discord** | [`discord.design.md`](designs/discord.design.md) | `#5865F2` / `#798DF9` | `#FFFFFF` / `#23272A` | Playful communication brand built on Blurple, oversized ABC Ginto hero headlines, gg sans utility text, pill CTAs, dark utility surfaces, and illustrated meg... |
| **Disney+** | [`disneyplus.design.md`](designs/disneyplus.design.md) | `#3DDEFF` / `#3DDEFF` | `#17171C` / `#040714` | Cinematic streaming system built from midnight navy-black stages, crisp Inspire typography, cyan-teal action sparks, poster-led rails, bundle comparison modu... |
| **Medium** | [`medium.design.md`](designs/medium.design.md) | `#1A8917` / `#1A8917` | `#F7F4ED` / `#191919` | Editorial publishing system for reading, writing, membership and story discovery. Extracted from the public Medium homepage via Jina text snapshot and the li... |
| **Netflix** | [`netflix.design.md`](designs/netflix.design.md) | `#E50914` / `#E50914` | `#000000` / `#000000` | Cinematic subscription product system built around black stages, assertive Netflix red actions, dense poster-led rows, heavy sans headlines, and a split betw... |

### E-Commerce & Retail (3)

| Brand | Specification | Primary / Accent | Canvas / Ink | Core Aesthetic Summary |
| :--- | :--- | :--- | :--- | :--- |
| **Amazon Commerce System** | [`amazon.design.md`](designs/amazon.design.md) | `#0F1111` / `#FF9900` | `#E3E6E6` / `#0F1111` | Functional, conversion-oriented marketplace design with a dark utility header, dominant search bar, light-grey commerce canvas, and modular product/category ... |
| **IKEA Global** | [`ikea.design.md`](designs/ikea.design.md) | `#FFDB00` / `#FFDB00` | `#FFFEFB` / `#111111` | Editorial IKEA global design system: democratic living, bold blue/yellow, flat magazine grid, large lifestyle image cards, and friendly Noto IKEA typography. |
| **Nike.com Retail Editorial** | [`nike.design.md`](designs/nike.design.md) | `#111111` / `#111111` | `#FFFFFF` / `#111111` | Monochrome, image-led performance commerce system with Nike Futura display, Helvetica Now utility typography, full-bleed campaign modules and flat product gr... |

### Hardware & Ecosystem (1)

| Brand | Specification | Primary / Accent | Canvas / Ink | Core Aesthetic Summary |
| :--- | :--- | :--- | :--- | :--- |
| **Apple** | [`apple.design.md`](designs/apple.design.md) | `#0066cc` / `#0066cc` | `#ffffff` / `#1d1d1f` | A photography-first interface that turns marketing into a museum gallery. Edge-to-edge product tiles alternate light and dark canvases, framed by SF Pro Disp... |

### Travel & Hospitality (2)

| Brand | Specification | Primary / Accent | Canvas / Ink | Core Aesthetic Summary |
| :--- | :--- | :--- | :--- | :--- |
| **Booking.com** | [`booking.design.md`](designs/booking.design.md) | `#006CE4` / `#006CE4` | `#FFFFFF` / `#1A1A1A` | Booking.com homepage: high-conversion travel commerce system with full-bleed brand blue, a yellow search frame, modular property cards, destination image car... |
| **Tripadvisor** | [`tripadvisor.design.md`](designs/tripadvisor.design.md) | `#002B11` / `#00EB5B` | `#FFFFFF` / `#002B11` | Travel marketplace system with deep Trip Green ink, neon Trip Brand search actions, pill-shaped controls, dense photo-led recommendation cards, rating bubble... |

### Lifestyle & Social (1)

| Brand | Specification | Primary / Accent | Canvas / Ink | Core Aesthetic Summary |
| :--- | :--- | :--- | :--- | :--- |
| **Pinterest** | [`pinterest.design.md`](designs/pinterest.design.md) | `#e60023` / `#e60023` | `#ffffff` / `#000000` | Image-centred discovery system with Pinterest Red as a strictly reserved CTA accent, Pin Sans, soft 16px radius, and masonry-style pin cards. |

### Marketing & Automation (1)

| Brand | Specification | Primary / Accent | Canvas / Ink | Core Aesthetic Summary |
| :--- | :--- | :--- | :--- | :--- |
| **Mailchimp** | [`mailchimp.design.md`](designs/mailchimp.design.md) | `#FFE01B` / `#007C89` | `#FFFFFF` / `#231E15` | Warm editorial marketing system with Cavendish Yellow action surfaces, Peppercorn ink, Means Web headlines, Graphik UI, tactile pill CTAs, and flat pricing/p... |

### Telecommunications (1)

| Brand | Specification | Primary / Accent | Canvas / Ink | Core Aesthetic Summary |
| :--- | :--- | :--- | :--- | :--- |
| **Vodafone** | [`vodafone.design.md`](designs/vodafone.design.md) | `#e60000` / `#e60000` | `#ffffff` / `#25282b` | High-contrast telecom identity built around Vodafone Red, oversized condensed-feeling brand typography, pill CTAs, flat editorial cards, video-led heroes, an... |

---

## 🤖 How to Use with AI Coding Assistants

AI coding agents (like **Claude Code**, **Antigravity**, **Cursor**, **Windsurf**, or **GitHub Copilot**) produce remarkably superior UI when provided an explicit design system spec.

### 1. Claude Code CLI
Attach the design spec directly into your prompt command:
```bash
claude --file designs/stripe.design.md "Redesign our checkout summary card to match the visual rhythm, border radii, and color tokens defined in stripe.design.md"
```

### 2. Cursor / Windsurf
Reference the spec file using `@` in chat or composer:
```text
@designs/notion.design.md Transform this settings modal into Notion aesthetic: monochrome canvas, 4px radii, subtle borders, and subdued muted typography.
```

### 3. Antigravity / Custom System Prompts
Inject the design tokens or full spec into the system instructions:
```text
You are an expert frontend designer. Adhere strictly to the design system rules in designs/wise.design.md:
- Use Wise Bright Green (#9FE870) exclusively for high-priority CTA actions.
- Use Forest Green (#163300) for high-contrast ink and dark sections.
- Apply stadium pills (9999px radius) on primary buttons and chips.
```

---

## 💻 How to Use in Web Development

### Option A: Pre-compiled CSS Variables
Every design system has a pre-compiled CSS stylesheet in `dist/css/<slug>.css`. Import it directly:

```html
<!-- Link Stripe stylesheet -->
<link rel="stylesheet" href="dist/css/stripe.css">
```

Use the CSS custom properties in your styles:
```css
.btn-primary {
  background-color: var(--color-primary);
  color: var(--color-surface);
  border-radius: var(--radius-sm, 6px);
  padding: 10px 18px;
  font-weight: var(--font-weightMedium, 500);
}
```

### Option B: Theme Switching via Data Attribute
Each stylesheet defines both default `:root` and `:root[data-theme="<slug>"]`. You can load multiple and dynamically switch them:
```html
<html data-theme="raycast">
  <!-- Automatically switches to Raycast tokens -->
</html>
```

### Option C: Tailwind CSS Configuration
You can map Tailwind colors directly to CSS variables:
```javascript
// tailwind.config.js
module.exports = {
  theme: {
    extend: {
      colors: {
        primary: "var(--color-primary)",
        accent: "var(--color-accent)",
        canvas: "var(--color-canvas)",
        surface: "var(--color-surface)",
        ink: "var(--color-ink)",
        border: "var(--color-border)",
      }
    }
  }
};
```

---

## 🔬 Specification Anatomy (`.design.md`)

Each `.design.md` file follows a standardized schema divided into two sections:

```yaml
---
version: alpha
name: BrandName
slug: brandname
source: "https://brand.com/"
description: "Precise summary of brand aesthetic and spatial behavior"
colors:
  primary: "#HEX"
  accent: "#HEX"
  canvas: "#HEX"
  surface: "#HEX"
  ink: "#HEX"
  border: "#HEX"
typography:
  fontFamily: "FontName, -apple-system, sans-serif"
  headingWeight: 600
rounded:
  sm: "4px"
  md: "8px"
  lg: "16px"
---
```

Followed by human-readable and agent-executable architectural guidelines:
- **1. Visual Theme & Atmosphere**: Emotional tone, layout density, whitespace rhythm
- **2. Color Palette & Roles**: Exact semantic roles for foreground, background, accents, and borders
- **3. Typography & Hierarchy**: Typeface choices, scale, tracking, line heights
- **4. Elevation, Depth & Borders**: Shadow rules, frosted glass filters, borders
- **5. Component Patterns**: Buttons, inputs, navigation, cards, tables, footers
- **6. Do's and Don'ts**: Anti-patterns to prevent breaking the aesthetic

---

## 🛠️ CLI Utilities

The repository includes Python automation scripts:

- **Rebuild CSS**: `python3 scripts/export_css.py`  
  Parses all `.design.md` files and outputs updated stylesheets into `dist/css/`.
- **Rebuild Catalog**: `python3 scripts/build_catalog.py`  
  Extracts metadata and updates `catalog.json`.
- **Rebuild README**: `python3 scripts/generate_readme.py`  
  Regenerates the complete README index table.

---

## ⚖️ Legal & Brand Disclaimer

This repository is an independent educational and design-research reference. All brand names, trademarks, registered trademarks, service marks, and trade dress referenced herein (e.g. Stripe, Apple, Notion, Wise, Brex, GitHub, etc.) are the property of their respective owners.

The token specifications and guidelines are intended solely for learning, aesthetic comparative study, and building compatible themes. No affiliation, endorsement, or sponsorship is implied.

## 📄 License

The documentation format, token extraction scripts, and CSS generation tooling are licensed under the [MIT License](LICENSE).
