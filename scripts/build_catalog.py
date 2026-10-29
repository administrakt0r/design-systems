#!/usr/bin/env python3
"""
Catalog Builder
Extracts metadata from all .design.md specifications and produces catalog.json.
"""

import os
import glob
import yaml
import json
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
DESIGNS_DIR = REPO_ROOT / "designs"
OUTPUT_FILE = REPO_ROOT / "catalog.json"

CATEGORIES = {
    # FinTech & Payments
    'stripe': 'FinTech & Payments',
    'wise': 'FinTech & Payments',
    'paypal': 'FinTech & Payments',
    'brex': 'FinTech & Payments',
    'mastercard': 'FinTech & Payments',
    'coinbase': 'FinTech & Payments',
    
    # Developer Platforms & Cloud
    'github': 'Developer Platforms & Cloud',
    'cloudflare': 'Developer Platforms & Cloud',
    'nextjs': 'Developer Platforms & Cloud',
    'framer': 'Developer Platforms & Cloud',
    'raycast': 'Developer Platforms & Cloud',
    'openai': 'Developer Platforms & Cloud',
    
    # Productivity & Collaboration
    'notion': 'Productivity & Collaboration',
    'slack': 'Productivity & Collaboration',
    'clickup': 'Productivity & Collaboration',
    'arc': 'Productivity & Collaboration',
    'strawberry': 'Productivity & Collaboration',
    
    # Entertainment & Media
    'netflix': 'Entertainment & Media',
    'disneyplus': 'Entertainment & Media',
    'medium': 'Entertainment & Media',
    'discord': 'Entertainment & Media',
    
    # E-Commerce & Retail
    'amazon': 'E-Commerce & Retail',
    'apple': 'Hardware & Ecosystem',
    'ikea': 'E-Commerce & Retail',
    'nike': 'E-Commerce & Retail',
    
    # Travel, Lifestyle & Marketing
    'booking': 'Travel & Hospitality',
    'tripadvisor': 'Travel & Hospitality',
    'pinterest': 'Lifestyle & Social',
    'duolingo': 'Education & Gamification',
    'vodafone': 'Telecommunications',
    'mailchimp': 'Marketing & Automation'
}

def main():
    files = sorted(DESIGNS_DIR.glob("*.design.md"))
    catalog = []
    
    for f in files:
        with open(f, "r", encoding="utf-8") as fh:
            content = fh.read()
        if not content.startswith("---"):
            continue
        parts = content.split("---", 2)
        if len(parts) < 3:
            continue
        data = yaml.safe_load(parts[1])
        slug = data.get("slug", f.stem.replace(".design", ""))
        name = data.get("name", slug.capitalize())
        category = CATEGORIES.get(slug, "General & SaaS")
        colors = data.get("colors", {})
        primary = colors.get("primary", colors.get("accent", "#000000"))
        accent = colors.get("accent", colors.get("primary", primary))
        canvas = colors.get("canvas", colors.get("background", "#ffffff"))
        ink = colors.get("ink", colors.get("text", "#000000"))
        
        catalog.append({
            "name": name,
            "slug": slug,
            "category": category,
            "source": data.get("source", ""),
            "description": data.get("description", ""),
            "primaryColor": primary,
            "accentColor": accent,
            "canvasColor": canvas,
            "inkColor": ink,
            "specFile": f"designs/{f.name}",
            "cssFile": f"dist/css/{slug}.css"
        })
        
    catalog.sort(key=lambda x: (x["category"], x["name"]))
    
    with open(OUTPUT_FILE, "w", encoding="utf-8") as out:
        json.dump(catalog, out, indent=2)
        
    print(f"Built catalog with {len(catalog)} design systems.")

if __name__ == "__main__":
    main()
