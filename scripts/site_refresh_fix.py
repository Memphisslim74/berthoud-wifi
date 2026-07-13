#!/usr/bin/env python3
"""Small post-processing fixes for the generated Berthoud WiFi refresh."""

from pathlib import Path
from bs4 import BeautifulSoup

ROOT = Path(__file__).resolve().parents[1]
HERO_IMAGE = "https://images.unsplash.com/photo-1497366754035-f200968a6e72?auto=format&fit=crop&w=1800&q=82"

COPY_FIXES = {
    "View All Solutions": "View all solutions",
    "Learn More": "Learn more",
    "Contact Us": "Contact us",
}


def fix_html(path: Path) -> None:
    soup = BeautifulSoup(path.read_text(encoding="utf-8"), "lxml")
    if not soup.head:
        return

    # Ensure the newly generated icon is not hidden behind the prior cache-busting version.
    icon = soup.head.find("link", rel=lambda value: value and "icon" in value if isinstance(value, list) else value == "icon")
    if icon:
        icon["href"] = "/favicon.png?v=17"
        icon["type"] = "image/png"
        icon["sizes"] = "256x256"
    else:
        icon = soup.new_tag("link", rel="icon", href="/favicon.png?v=17", type="image/png", sizes="256x256")
        soup.head.append(icon)

    touch = soup.head.find("link", rel=lambda value: value and "apple-touch-icon" in value if isinstance(value, list) else value == "apple-touch-icon")
    if touch is None:
        touch = soup.new_tag("link", rel="apple-touch-icon", href="/apple-touch-icon.png?v=17", sizes="180x180")
        soup.head.append(touch)
    else:
        touch["href"] = "/apple-touch-icon.png?v=17"
        touch["sizes"] = "180x180"

    # Only load the GA library once. The config block remains in the head.
    gtag_loaders = soup.find_all("script", src=lambda value: value and "googletagmanager.com/gtag/js" in value)
    for duplicate in gtag_loaders[1:]:
        duplicate.decompose()

    # Preload the full-bleed hero background on the homepage because CSS backgrounds
    # cannot receive fetchpriority directly.
    if path.relative_to(ROOT).as_posix() == "index.html":
        preload = soup.head.find("link", rel="preload", href=HERO_IMAGE)
        if preload is None:
            preload = soup.new_tag("link", rel="preload", href=HERO_IMAGE)
            preload["as"] = "image"
            preload["fetchpriority"] = "high"
            soup.head.append(preload)

    # Keep the visible header mark eager; defer the footer copy.
    for img in soup.select(".site-header .brand img"):
        img["loading"] = "eager"
        img["fetchpriority"] = "low"
    for img in soup.select(".site-footer .brand img"):
        img["loading"] = "lazy"
        img.attrs.pop("fetchpriority", None)

    # Contact form JavaScript is only needed on the actual contact page.
    if path.relative_to(ROOT).as_posix() != "contact.html":
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


def main() -> None:
    for html in ROOT.rglob("*.html"):
        if any(part.startswith(".") for part in html.relative_to(ROOT).parts):
            continue
        fix_html(html)


if __name__ == "__main__":
    main()
