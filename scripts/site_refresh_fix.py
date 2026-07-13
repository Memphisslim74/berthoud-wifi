#!/usr/bin/env python3
"""Post-processing fixes for the generated Berthoud WiFi refresh."""

import json
import re
from pathlib import Path

from bs4 import BeautifulSoup

ROOT = Path(__file__).resolve().parents[1]
HERO_IMAGE = "https://images.unsplash.com/photo-1497366754035-f200968a6e72?auto=format&fit=crop&w=1800&q=82"
BRAND_CSS = "/assets/css/brand-refresh.css?v=18"

COPY_FIXES = {
    "View All Solutions": "View all solutions",
    "Learn More": "Learn more",
    "Contact Us": "Contact us",
}

CSS_MARKER = "/* v18 unified controls and Turnstile */"
CSS_OVERRIDES = r'''
/* v18 unified controls and Turnstile */
:root{--button-radius:5px}
.btn,button.btn,input[type="submit"].btn,input[type="button"].btn{
  border-radius:var(--button-radius)!important;
  min-height:44px;
  padding:12px 18px;
  line-height:1.1;
  white-space:nowrap;
  flex:0 0 auto;
  width:auto;
  max-width:max-content;
}
.site-header .nav-links .btn{min-height:38px;padding:10px 15px}
.menu-btn{border-radius:var(--button-radius)!important}
.hero-actions{align-items:center}
.hero-actions .btn{min-width:0}
.cta>div{min-width:0}
.cta>.btn,.content-cta>.btn{min-width:132px;align-self:center}
.form-actions .btn{min-width:150px}
.btn:disabled{cursor:not-allowed;opacity:.58;transform:none!important}
.turnstile-field{gap:8px;margin-top:2px}
.turnstile-field[hidden]{display:none!important}
.turnstile-widget{min-height:65px;max-width:100%;color:var(--body-text);font-size:.92rem;line-height:1.55}
.turnstile-field.is-error{padding:14px;border:1px solid #D7A691;border-radius:7px;background:var(--accent-clay-soft)}
.turnstile-note{margin:0;color:var(--body-text);font-size:.78rem}
@media(max-width:700px){
  .cta>.btn,.content-cta>.btn{width:100%;max-width:280px;align-self:flex-start}
  .form-actions .btn{width:100%;max-width:none}
}
'''


def schema_key(data):
    if not isinstance(data, dict):
        return None
    schema_type = data.get("@type")
    if isinstance(schema_type, list):
        schema_type = ",".join(sorted(str(item) for item in schema_type))
    if schema_type == "FAQPage":
        return "FAQPage"
    if schema_type == "WebSite":
        return f"WebSite:{data.get('@id', data.get('url', ''))}"
    if schema_type in {"LocalBusiness", "ProfessionalService", "Organization"}:
        return f"Business:{data.get('@id', data.get('name', 'Berthoud WiFi'))}"
    return None


def dedupe_jsonld(soup: BeautifulSoup) -> None:
    seen = set()
    for script in list(soup.find_all("script", type="application/ld+json")):
        try:
            data = json.loads(script.string or script.get_text())
        except Exception:
            continue
        key = schema_key(data)
        if key and key in seen:
            script.decompose()
        elif key:
            seen.add(key)


def fix_html(path: Path) -> None:
    soup = BeautifulSoup(path.read_text(encoding="utf-8"), "lxml")
    if not soup.head:
        return

    icon = soup.head.find(
        "link",
        rel=lambda value: value and "icon" in value if isinstance(value, list) else value == "icon",
    )
    if icon:
        icon["href"] = "/favicon.png?v=17"
        icon["type"] = "image/png"
        icon["sizes"] = "256x256"
    else:
        soup.head.append(
            soup.new_tag(
                "link",
                rel="icon",
                href="/favicon.png?v=17",
                type="image/png",
                sizes="256x256",
            )
        )

    touch = soup.head.find(
        "link",
        rel=lambda value: value and "apple-touch-icon" in value
        if isinstance(value, list)
        else value == "apple-touch-icon",
    )
    if touch is None:
        soup.head.append(
            soup.new_tag(
                "link",
                rel="apple-touch-icon",
                href="/apple-touch-icon.png?v=17",
                sizes="180x180",
            )
        )
    else:
        touch["href"] = "/apple-touch-icon.png?v=17"
        touch["sizes"] = "180x180"

    brand_stylesheet = soup.head.find(
        "link",
        rel="stylesheet",
        href=lambda value: value and value.startswith("/assets/css/brand-refresh.css"),
    )
    if brand_stylesheet:
        brand_stylesheet["href"] = BRAND_CSS
    else:
        soup.head.append(soup.new_tag("link", rel="stylesheet", href=BRAND_CSS))

    gtag_loaders = soup.find_all(
        "script", src=lambda value: value and "googletagmanager.com/gtag/js" in value
    )
    for duplicate in gtag_loaders[1:]:
        duplicate.decompose()

    dedupe_jsonld(soup)
    relative = path.relative_to(ROOT).as_posix()

    if relative == "index.html":
        preload = soup.head.find("link", rel="preload", href=HERO_IMAGE)
        if preload is None:
            preload = soup.new_tag("link", rel="preload", href=HERO_IMAGE)
            preload["as"] = "image"
            preload["fetchpriority"] = "high"
            soup.head.append(preload)

    if relative == "contact.html":
        preconnect = soup.head.find(
            "link", rel="preconnect", href="https://challenges.cloudflare.com"
        )
        if preconnect is None:
            soup.head.append(
                soup.new_tag(
                    "link", rel="preconnect", href="https://challenges.cloudflare.com"
                )
            )

    for img in soup.select(".site-header .brand img"):
        img["loading"] = "eager"
        img["fetchpriority"] = "low"
    for img in soup.select(".site-footer .brand img"):
        img["loading"] = "lazy"
        img.attrs.pop("fetchpriority", None)

    if relative != "contact.html":
        for script in soup.find_all("script", src="/assets/js/contact-form.js"):
            script.decompose()

    for node in soup.find_all(string=True):
        if node.parent and node.parent.name in {"script", "style"}:
            continue
        text = str(node)
        new = text
        for old, replacement in COPY_FIXES.items():
            new = new.replace(old, replacement)
        if new != text:
            node.replace_with(new)

    path.write_text("<!doctype html>\n" + str(soup.html), encoding="utf-8")


def fix_css() -> None:
    path = ROOT / "assets" / "css" / "brand-refresh.css"
    if not path.exists():
        return
    text = path.read_text(encoding="utf-8")
    text = text.replace(
        "/* Berthoud WiFi v17 design system:",
        "/* Berthoud WiFi v18 design system:",
    )
    if CSS_MARKER in text:
        text = text.split(CSS_MARKER, 1)[0].rstrip()
    path.write_text(text.rstrip() + "\n" + CSS_OVERRIDES.lstrip(), encoding="utf-8")


def fix_headers() -> None:
    path = ROOT / "_headers"
    if not path.exists():
        return
    text = path.read_text(encoding="utf-8")
    csp = (
        "  Content-Security-Policy: default-src 'self'; "
        "img-src 'self' data: https:; "
        "style-src 'self' 'unsafe-inline' https://fonts.googleapis.com; "
        "script-src 'self' 'unsafe-inline' https://www.googletagmanager.com "
        "https://www.google-analytics.com https://challenges.cloudflare.com; "
        "font-src 'self' data: https://fonts.gstatic.com; "
        "connect-src 'self' https://www.google-analytics.com "
        "https://region1.google-analytics.com; "
        "frame-src https://challenges.cloudflare.com; "
        "frame-ancestors 'self'; base-uri 'self'; form-action 'self' mailto:;"
    )
    if "Content-Security-Policy:" in text:
        text = re.sub(
            r"^\s*Content-Security-Policy:.*$", csp, text, flags=re.MULTILINE
        )
    else:
        text = text.rstrip() + "\n" + csp + "\n"
    path.write_text(text, encoding="utf-8")


def main() -> None:
    fix_css()
    fix_headers()
    for html in ROOT.rglob("*.html"):
        if any(part.startswith(".") for part in html.relative_to(ROOT).parts):
            continue
        fix_html(html)


if __name__ == "__main__":
    main()
