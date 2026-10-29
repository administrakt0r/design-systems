#!/usr/bin/env python3
"""
Generate README.md for the design-systems repository.
"""

import json
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
CATALOG_PATH = REPO_ROOT / "catalog.json"
README_PATH = REPO_ROOT / "README.md"

def main():
    with open(CATALOG_PATH, "r", encoding="utf-8") as f:
        catalog = json.load(f)

    # Group by category
    by_cat = {}
    for item in catalog:
        by_cat.setdefault(item["category"], []).append(item)

    cat_order = [
        "FinTech & Payments",
        "Developer Platforms & Cloud",
        "Productivity & Collaboration",
        "Entertainment & Media",
        "E-Commerce & Retail",
        "Hardware & Ecosystem",
        "Travel & Hospitality",
        "Education & Gamification",
        "Lifestyle & Social",
        "Marketing & Automation",
        "Telecommunications"
    ]

    lines = []
    lines.append("# 🎨 Design Systems Catalog")
    lines.append("")
    lines.append("> **31 real-world, production-tested brand design systems** extracted from world-class tech companies, financial institutions, and digital platforms.")
    lines.append("> Standardized as machine-readable `.design.md` token specifications, ready for **AI Coding Assistants** (Claude Code, Antigravity, Cursor, Windsurf, GitHub Copilot) and **Frontend Engineering** (CSS Variables, Tailwind CSS, Design Tokens).")
    lines.append("")
    lines.append("[![Specs](https://img.shields.io/badge/Specs-31%20Brand%20Systems-635bff.svg)](#-index-of-design-systems)")
    lines.append("[![Format](https://img.shields.io/badge/Format-.design.md%20(YAML%20%2B%20Markdown)-1f883d.svg)](#-specification-anatomy-designmd)")
    lines.append("[![CSS Included](https://img.shields.io/badge/CSS-31%20Ready--to--Use%20Stylesheets-0066cc.svg)](#-how-to-use-in-web-development)")
    lines.append("[![License: MIT](https://img.shields.io/badge/License-MIT-gray.svg)](LICENSE)")
    lines.append("")
    lines.append("---")
    lines.append("")
    lines.append("## 🌟 Overview")
    lines.append("")
    lines.append("When building modern web applications or asking AI agents to design interfaces, default styling often converges on generic, purple-gradient SaaS templates with oversized cards and poor contrast.")
    lines.append("")
    lines.append("This repository provides **31 rigorous, high-fidelity design specifications (`.design.md`)** reverse-engineered from world-class products like **Stripe**, **Apple**, **Notion**, **Wise**, **GitHub**, **Raycast**, and **Brex**.")
    lines.append("")
    lines.append("Each specification pairs machine-parseable YAML design tokens with detailed architectural and aesthetic guidelines so you or an AI agent can build or re-theme interfaces with authentic brand personality, proper spatial rhythm, and accessible contrast.")
    lines.append("")
    lines.append("---")
    lines.append("")
    lines.append("## 📂 Repository Structure")
    lines.append("")
    lines.append("```text")
    lines.append("design-systems/")
    lines.append("├── catalog.json              # Machine-readable JSON manifest of all 31 systems")
    lines.append("├── designs/                  # 31 .design.md specifications (YAML tokens + guidelines)")
    lines.append("│   ├── stripe.design.md")
    lines.append("│   ├── apple.design.md")
    lines.append("│   ├── notion.design.md")
    lines.append("│   ├── github.design.md")
    lines.append("│   └── ...")
    lines.append("├── dist/css/                 # Ready-to-import :root CSS custom properties")
    lines.append("│   ├── stripe.css")
    lines.append("│   ├── brex.css")
    lines.append("│   ├── raycast.css")
    lines.append("│   └── ...")
    lines.append("├── scripts/")
    lines.append("│   ├── export_css.py         # Compiles YAML tokens into dist/css/*.css")
    lines.append("│   ├── build_catalog.py      # Generates catalog.json from design specs")
    lines.append("│   └── generate_readme.py    # Builds this README.md")
    lines.append("└── README.md")
    lines.append("```")
    lines.append("")
    lines.append("---")
    lines.append("")
    lines.append("## 📋 Index of Design Systems")
    lines.append("")

    for cat in cat_order:
        items = by_cat.get(cat, [])
        if not items:
            continue
        lines.append(f"### {cat} ({len(items)})")
        lines.append("")
        lines.append("| Brand | Specification | Primary / Accent | Canvas / Ink | Core Aesthetic Summary |")
        lines.append("| :--- | :--- | :--- | :--- | :--- |")
        for it in items:
            name = it["name"]
            slug = it["slug"]
            spec_link = f"[`{slug}.design.md`]({it['specFile']})"
            prim_acc = f"`{it['primaryColor']}` / `{it['accentColor']}`"
            canv_ink = f"`{it['canvasColor']}` / `{it['inkColor']}`"
            desc = it["description"].replace("|", "/")
            if len(desc) > 160:
                desc = desc[:157] + "..."
            lines.append(f"| **{name}** | {spec_link} | {prim_acc} | {canv_ink} | {desc} |")
        lines.append("")

    lines.append("---")
    lines.append("")
    lines.append("## 🤖 How to Use with AI Coding Assistants")
    lines.append("")
    lines.append("AI coding agents (like **Claude Code**, **Antigravity**, **Cursor**, **Windsurf**, or **GitHub Copilot**) produce remarkably superior UI when provided an explicit design system spec.")
    lines.append("")
    lines.append("### 1. Claude Code CLI")
    lines.append("Attach the design spec directly into your prompt command:")
    lines.append("```bash")
    lines.append('claude --file designs/stripe.design.md "Redesign our checkout summary card to match the visual rhythm, border radii, and color tokens defined in stripe.design.md"')
    lines.append("```")
    lines.append("")
    lines.append("### 2. Cursor / Windsurf")
    lines.append("Reference the spec file using `@` in chat or composer:")
    lines.append("```text")
    lines.append("@designs/notion.design.md Transform this settings modal into Notion aesthetic: monochrome canvas, 4px radii, subtle borders, and subdued muted typography.")
    lines.append("```")
    lines.append("")
    lines.append("### 3. Antigravity / Custom System Prompts")
    lines.append("Inject the design tokens or full spec into the system instructions:")
    lines.append("```text")
    lines.append("You are an expert frontend designer. Adhere strictly to the design system rules in designs/wise.design.md:")
    lines.append("- Use Wise Bright Green (#9FE870) exclusively for high-priority CTA actions.")
    lines.append("- Use Forest Green (#163300) for high-contrast ink and dark sections.")
    lines.append("- Apply stadium pills (9999px radius) on primary buttons and chips.")
    lines.append("```")
    lines.append("")
    lines.append("---")
    lines.append("")
    lines.append("## 💻 How to Use in Web Development")
    lines.append("")
    lines.append("### Option A: Pre-compiled CSS Variables")
    lines.append("Every design system has a pre-compiled CSS stylesheet in `dist/css/<slug>.css`. Import it directly:")
    lines.append("")
    lines.append("```html")
    lines.append("<!-- Link Stripe stylesheet -->")
    lines.append('<link rel="stylesheet" href="dist/css/stripe.css">')
    lines.append("```")
    lines.append("")
    lines.append("Use the CSS custom properties in your styles:")
    lines.append("```css")
    lines.append(".btn-primary {")
    lines.append("  background-color: var(--color-primary);")
    lines.append("  color: var(--color-surface);")
    lines.append("  border-radius: var(--radius-sm, 6px);")
    lines.append("  padding: 10px 18px;")
    lines.append("  font-weight: var(--font-weightMedium, 500);")
    lines.append("}")
    lines.append("```")
    lines.append("")
    lines.append("### Option B: Theme Switching via Data Attribute")
    lines.append('Each stylesheet defines both default `:root` and `:root[data-theme="<slug>"]`. You can load multiple and dynamically switch them:')
    lines.append("```html")
    lines.append('<html data-theme="raycast">')
    lines.append("  <!-- Automatically switches to Raycast tokens -->")
    lines.append("</html>")
    lines.append("```")
    lines.append("")
    lines.append("### Option C: Tailwind CSS Configuration")
    lines.append("You can map Tailwind colors directly to CSS variables:")
    lines.append("```javascript")
    lines.append("// tailwind.config.js")
    lines.append("module.exports = {")
    lines.append("  theme: {")
    lines.append("    extend: {")
    lines.append("      colors: {")
    lines.append('        primary: "var(--color-primary)",')
    lines.append('        accent: "var(--color-accent)",')
    lines.append('        canvas: "var(--color-canvas)",')
    lines.append('        surface: "var(--color-surface)",')
    lines.append('        ink: "var(--color-ink)",')
    lines.append('        border: "var(--color-border)",')
    lines.append("      }")
    lines.append("    }")
    lines.append("  }")
    lines.append("};")
    lines.append("```")
    lines.append("")
    lines.append("---")
    lines.append("")
    lines.append("## 🔬 Specification Anatomy (`.design.md`)")
    lines.append("")
    lines.append("Each `.design.md` file follows a standardized schema divided into two sections:")
    lines.append("")
    lines.append("```yaml")
    lines.append("---")
    lines.append("version: alpha")
    lines.append("name: BrandName")
    lines.append("slug: brandname")
    lines.append('source: "https://brand.com/"')
    lines.append('description: "Precise summary of brand aesthetic and spatial behavior"')
    lines.append("colors:")
    lines.append('  primary: "#HEX"')
    lines.append('  accent: "#HEX"')
    lines.append('  canvas: "#HEX"')
    lines.append('  surface: "#HEX"')
    lines.append('  ink: "#HEX"')
    lines.append('  border: "#HEX"')
    lines.append("typography:")
    lines.append('  fontFamily: "FontName, -apple-system, sans-serif"')
    lines.append("  headingWeight: 600")
    lines.append("rounded:")
    lines.append('  sm: "4px"')
    lines.append('  md: "8px"')
    lines.append('  lg: "16px"')
    lines.append("---")
    lines.append("```")
    lines.append("")
    lines.append("Followed by human-readable and agent-executable architectural guidelines:")
    lines.append("- **1. Visual Theme & Atmosphere**: Emotional tone, layout density, whitespace rhythm")
    lines.append("- **2. Color Palette & Roles**: Exact semantic roles for foreground, background, accents, and borders")
    lines.append("- **3. Typography & Hierarchy**: Typeface choices, scale, tracking, line heights")
    lines.append("- **4. Elevation, Depth & Borders**: Shadow rules, frosted glass filters, borders")
    lines.append("- **5. Component Patterns**: Buttons, inputs, navigation, cards, tables, footers")
    lines.append("- **6. Do's and Don'ts**: Anti-patterns to prevent breaking the aesthetic")
    lines.append("")
    lines.append("---")
    lines.append("")
    lines.append("## 🛠️ CLI Utilities")
    lines.append("")
    lines.append("The repository includes Python automation scripts:")
    lines.append("")
    lines.append("- **Rebuild CSS**: `python3 scripts/export_css.py`  ")
    lines.append("  Parses all `.design.md` files and outputs updated stylesheets into `dist/css/`.")
    lines.append("- **Rebuild Catalog**: `python3 scripts/build_catalog.py`  ")
    lines.append("  Extracts metadata and updates `catalog.json`.")
    lines.append("- **Rebuild README**: `python3 scripts/generate_readme.py`  ")
    lines.append("  Regenerates the complete README index table.")
    lines.append("")
    lines.append("---")
    lines.append("")
    lines.append("## ⚖️ Legal & Brand Disclaimer")
    lines.append("")
    lines.append("This repository is an independent educational and design-research reference. All brand names, trademarks, registered trademarks, service marks, and trade dress referenced herein (e.g. Stripe, Apple, Notion, Wise, Brex, GitHub, etc.) are the property of their respective owners.")
    lines.append("")
    lines.append("The token specifications and guidelines are intended solely for learning, aesthetic comparative study, and building compatible themes. No affiliation, endorsement, or sponsorship is implied.")
    lines.append("")
    lines.append("## 📄 License")
    lines.append("")
    lines.append("The documentation format, token extraction scripts, and CSS generation tooling are licensed under the [MIT License](LICENSE).")

    with open(README_PATH, "w", encoding="utf-8") as f:
        f.write("\n".join(lines) + "\n")

    print(f"README.md successfully written to {README_PATH}")

if __name__ == "__main__":
    main()
