#!/usr/bin/env python3
"""
Design Systems CSS Exporter
Converts .design.md YAML frontmatter into ready-to-use CSS custom properties (:root variables).
"""

import os
import sys
import glob
import yaml
import json
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
DESIGNS_DIR = REPO_ROOT / "designs"
DIST_DIR = REPO_ROOT / "dist" / "css"

def parse_design_file(file_path: Path):
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()
    if not content.startswith("---"):
        return None
    parts = content.split("---", 2)
    if len(parts) < 3:
        return None
    data = yaml.safe_load(parts[1])
    return data

def generate_css(data: dict) -> str:
    slug = data.get("slug", "theme")
    name = data.get("name", slug.capitalize())
    description = data.get("description", "")
    
    lines = [
        f"/**",
        f" * Design System: {name} ({slug})",
        f" * Source: {data.get('source', 'N/A')}",
        f" * Description: {description}",
        f" */",
        f"",
        f":root[data-theme=\"{slug}\"],",
        f":root {{",
        f"  /* Colors */",
    ]
    
    colors = data.get("colors", {})
    if isinstance(colors, dict):
        for key, val in colors.items():
            if isinstance(val, str):
                lines.append(f"  --color-{key}: {val};")
            elif isinstance(val, dict):
                for subkey, subval in val.items():
                    lines.append(f"  --color-{key}-{subkey}: {subval};")
    
    typography = data.get("typography", {})
    if isinstance(typography, dict) and typography:
        lines.append(f"")
        lines.append(f"  /* Typography */")
        for key, val in typography.items():
            lines.append(f"  --font-{key}: {val};")
            
    rounded = data.get("rounded", {})
    if isinstance(rounded, dict) and rounded:
        lines.append(f"")
        lines.append(f"  /* Border Radius */")
        for key, val in rounded.items():
            lines.append(f"  --radius-{key}: {val};")

    lines.append(f"}}")
    lines.append("")
    return "\n".join(lines)

def main():
    DIST_DIR.mkdir(parents=True, exist_ok=True)
    files = sorted(DESIGNS_DIR.glob("*.design.md"))
    
    exported = 0
    for f in files:
        data = parse_design_file(f)
        if not data:
            continue
        slug = data.get("slug", f.stem.replace(".design", ""))
        css_content = generate_css(data)
        out_path = DIST_DIR / f"{slug}.css"
        with open(out_path, "w", encoding="utf-8") as out:
            out.write(css_content)
        exported += 1
    
    print(f"Generated CSS for {exported} design systems in {DIST_DIR}")

if __name__ == "__main__":
    main()
