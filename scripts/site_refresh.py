#!/usr/bin/env python3
"""One-time Berthoud WiFi SEO, performance, contact, and design-system refresh."""

from __future__ import annotations

import json
import re
from datetime import date
from pathlib import Path
from typing import Any

from bs4 import BeautifulSoup, NavigableString, Tag
from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parents[1]
PHONE_DISPLAY = "720-209-3130"
PHONE_E164 = "+17202093130"
EMAIL = "hello@berthoudwifi.com"
FACEBOOK = "https://www.facebook.com/profile.php?id=61591527285692"
LINKEDIN = "https://www.linkedin.com/company/berthoud-wifi/"
SITE_URL = "https://berthoudwifi.com"
LOGO_PATH = "/assets/images/berthoud-wifi-logo-flat.png"
SOCIAL_IMAGE_PATH = "/assets/images/berthoud-wifi-social-card.png"
TODAY = date.today().isoformat()

INK = "#16233B"
BODY = "#5B6472"
BLUE = "#1958C4"
CLAY = "#BC5B2E"
TINT = "#F4F6F9"
BORDER = "#E7E9EE"

PHOTO_ROOT = ROOT / "assets" / "images"


def font(size: int, bold: bool = False) -> ImageFont.FreeTypeFont:
    names = [
        "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf" if bold else "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
        "/usr/share/fonts/truetype/liberation2/LiberationSans-Bold.ttf" if bold else "/usr/share/fonts/truetype/liberation2/LiberationSans-Regular.ttf",
    ]
    for name in names:
        p = Path(name)
        if p.exists():
            return ImageFont.truetype(str(p), size=size)
    return ImageFont.load_default()


def centered_text(draw: ImageDraw.ImageDraw, xy: tuple[int, int], text: str, fnt: ImageFont.ImageFont, fill: str) -> None:
    box = draw.textbbox((0, 0), text, font=fnt)
    width = box[2] - box[0]
    draw.text((xy[0] - width / 2, xy[1]), text, font=fnt, fill=fill)


def make_logo() -> None:
    out = PHOTO_ROOT / "berthoud-wifi-logo-flat.png"
    out.parent.mkdir(parents=True, exist_ok=True)
    size = 1024
    im = Image.new("RGBA", (size, size), (0, 0, 0, 0))
    d = ImageDraw.Draw(im)
    d.ellipse((38, 38, 986, 986), fill="white", outline=INK, width=34)

    # Mountain silhouette.
    mountain = [(145, 430), (285, 260), (372, 360), (500, 190), (650, 385), (742, 292), (880, 440), (880, 510), (145, 510)]
    d.polygon(mountain, fill=INK)
    d.polygon([(245, 308), (285, 260), (320, 326), (285, 305)], fill="white")
    d.polygon([(435, 280), (500, 190), (568, 295), (503, 258)], fill="white")

    # Water tower integrated into the horizon.
    d.rounded_rectangle((725, 336, 812, 390), radius=14, fill="white", outline=INK, width=9)
    d.line((743, 390, 733, 472), fill=INK, width=12)
    d.line((794, 390, 805, 472), fill=INK, width=12)
    d.line((738, 430, 800, 430), fill=INK, width=9)

    # WiFi mark.
    d.arc((316, 420, 708, 730), start=210, end=330, fill=BLUE, width=34)
    d.arc((376, 492, 648, 704), start=210, end=330, fill=BLUE, width=34)
    d.ellipse((488, 628, 536, 676), fill=BLUE)

    centered_text(d, (512, 718), "BERTHOUD", font(72, True), INK)
    centered_text(d, (512, 800), "WIFI", font(78, True), INK)
    centered_text(d, (512, 888), "NORTHERN COLORADO", font(29, True), BODY)
    im.save(out, optimize=True)

    # Favicon and touch icon are generated from the mark rather than the full old portrait badge.
    for name, px in (("favicon.png", 256), ("apple-touch-icon.png", 180)):
        resized = im.resize((px, px), Image.Resampling.LANCZOS)
        resized.save(ROOT / name, optimize=True)


def make_social_card() -> None:
    out = PHOTO_ROOT / "berthoud-wifi-social-card.png"
    im = Image.new("RGB", (1200, 630), TINT)
    d = ImageDraw.Draw(im)
    d.rectangle((0, 0, 1200, 16), fill=BLUE)
    d.rectangle((0, 594, 1200, 630), fill=INK)

    logo = Image.open(PHOTO_ROOT / "berthoud-wifi-logo-flat.png").convert("RGBA").resize((390, 390), Image.Resampling.LANCZOS)
    im.paste(logo, (52, 105), logo)

    d.text((500, 120), "PROFESSIONAL", font=font(35, True), fill=BLUE)
    d.text((500, 173), "UniFi systems", font=font(67, True), fill=INK)
    d.text((500, 270), "for homes, businesses,", font=font(38, False), fill=BODY)
    d.text((500, 322), "and larger properties.", font=font(38, False), fill=BODY)
    d.rounded_rectangle((500, 405, 1085, 472), radius=9, fill=CLAY)
    d.text((535, 420), "WiFi  •  Networking  •  Cameras  •  Fiber", font=font(24, True), fill="white")
    d.text((500, 520), "Berthoud & Northern Colorado", font=font(28, True), fill=INK)
    im.save(out, optimize=True)


def is_photo(path: Path, image: Image.Image) -> bool:
    if path.suffix.lower() in {".jpg", ".jpeg"}:
        return True
    if path.suffix.lower() != ".png":
        return False
    if any(x in path.name.lower() for x in ("logo", "favicon", "icon", "badge", "apple-touch")):
        return False
    if image.width < 500 or image.height < 300:
        return False
    return image.mode not in {"RGBA", "LA"} or image.getextrema()[-1] == (255, 255)


def optimize_images() -> dict[str, dict[str, Any]]:
    mapping: dict[str, dict[str, Any]] = {}
    if not PHOTO_ROOT.exists():
        return mapping

    for path in PHOTO_ROOT.rglob("*"):
        if not path.is_file() or path.suffix.lower() not in {".jpg", ".jpeg", ".png", ".webp"}:
            continue
        if "-480" in path.stem or "-800" in path.stem or "-1200" in path.stem:
            continue
        try:
            with Image.open(path) as img:
                img.load()
                width, height = img.size
                rel = "/" + path.relative_to(ROOT).as_posix()
                info: dict[str, Any] = {"width": width, "height": height, "src": rel, "srcset": []}

                if is_photo(path, img):
                    target = path.with_suffix(".webp")
                    rgb = img.convert("RGB")
                    rgb.save(target, "WEBP", quality=80, method=6)
                    info["src"] = "/" + target.relative_to(ROOT).as_posix()

                    variants = []
                    for target_width in (480, 800, 1200):
                        if width <= target_width * 1.08:
                            continue
                        target_height = round(height * target_width / width)
                        resized = rgb.resize((target_width, target_height), Image.Resampling.LANCZOS)
                        variant = target.with_name(f"{target.stem}-{target_width}.webp")
                        resized.save(variant, "WEBP", quality=78, method=6)
                        variants.append(("/" + variant.relative_to(ROOT).as_posix(), target_width))
                    variants.append((info["src"], width))
                    info["srcset"] = variants

                mapping[rel] = info
                mapping[info["src"]] = info
        except Exception as exc:
            print(f"Skipping image {path}: {exc}")
    return mapping


def update_css_image_urls(mapping: dict[str, dict[str, Any]]) -> None:
    for css in (ROOT / "assets" / "css").glob("*.css"):
        text = css.read_text(encoding="utf-8")
        for old, info in mapping.items():
            new = info["src"]
            if old != new:
                text = text.replace(old, new).replace(old.lstrip("/"), new.lstrip("/"))
        # Remove the retired red palette from the rendered system.
        replacements = {
            "#c93b3b": CLAY,
            "#C93B3B": CLAY,
            "#a72626": "#934521",
            "#9f2525": "#934521",
            "#fff1f1": "#FDF3ED",
            "#fff7f7": "#FDF7F3",
            "rgba(201,59,59": "rgba(188,91,46",
            "var(--red-soft)": "var(--accent-clay-soft)",
            "var(--red)": "var(--accent-clay)",
        }
        for old, new in replacements.items():
            text = text.replace(old, new)
        css.write_text(text, encoding="utf-8")


def ensure_meta(soup: BeautifulSoup, *, name: str | None = None, prop: str | None = None, content: str) -> Tag:
    attrs = {"name": name} if name else {"property": prop}
    tag = soup.head.find("meta", attrs=attrs)
    if tag is None:
        tag = soup.new_tag("meta")
        tag.attrs.update(attrs)
        soup.head.append(tag)
    tag["content"] = content
    return tag


def ensure_link(soup: BeautifulSoup, rel: str, href: str, **attrs: str) -> Tag:
    tag = soup.head.find("link", rel=lambda value: value and rel in value if isinstance(value, list) else value == rel, href=href)
    if tag is None:
        tag = soup.new_tag("link", rel=rel, href=href)
        soup.head.append(tag)
    for key, value in attrs.items():
        tag[key.replace("_", "-")] = value
    return tag


def type_contains(value: Any, expected: str) -> bool:
    if isinstance(value, list):
        return expected in value
    return value == expected


def enrich_schema(node: Any) -> None:
    if isinstance(node, list):
        for item in node:
            enrich_schema(item)
        return
    if not isinstance(node, dict):
        return

    schema_type = node.get("@type")
    if any(type_contains(schema_type, kind) for kind in ("LocalBusiness", "ProfessionalService", "Organization")):
        node.setdefault("@id", f"{SITE_URL}/#business")
        node["name"] = "Berthoud WiFi"
        node["url"] = f"{SITE_URL}/"
        node["telephone"] = PHONE_E164
        node["email"] = EMAIL
        node["logo"] = f"{SITE_URL}{LOGO_PATH}"
        node["image"] = f"{SITE_URL}{SOCIAL_IMAGE_PATH}"
        node["sameAs"] = [FACEBOOK, LINKEDIN]
        node["contactPoint"] = {
            "@type": "ContactPoint",
            "telephone": PHONE_E164,
            "email": EMAIL,
            "contactType": "customer service",
            "areaServed": "US-CO",
            "availableLanguage": "English",
        }
    for value in node.values():
        enrich_schema(value)


def add_homepage_faq_schema(soup: BeautifulSoup) -> None:
    if any("FAQPage" in script.get_text() for script in soup.find_all("script", type="application/ld+json")):
        return
    entries = []
    for details in soup.select(".faq details"):
        summary = details.find("summary")
        answer = details.find("p")
        if summary and answer:
            entries.append({
                "@type": "Question",
                "name": summary.get_text(" ", strip=True),
                "acceptedAnswer": {"@type": "Answer", "text": answer.get_text(" ", strip=True)},
            })
    if not entries:
        return
    script = soup.new_tag("script", type="application/ld+json")
    script.string = json.dumps({"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": entries}, separators=(",", ":"))
    soup.head.append(script)


def add_website_schema(soup: BeautifulSoup) -> None:
    if any('"WebSite"' in script.get_text() for script in soup.find_all("script", type="application/ld+json")):
        return
    script = soup.new_tag("script", type="application/ld+json")
    script.string = json.dumps({
        "@context": "https://schema.org",
        "@type": "WebSite",
        "@id": f"{SITE_URL}/#website",
        "url": f"{SITE_URL}/",
        "name": "Berthoud WiFi",
        "publisher": {"@id": f"{SITE_URL}/#business"},
        "inLanguage": "en-US",
    }, separators=(",", ":"))
    soup.head.append(script)


def update_navigation(soup: BeautifulSoup) -> None:
    for brand in soup.select("a.brand"):
        image = brand.find("img")
        if image:
            image["src"] = LOGO_PATH
            image["alt"] = "Berthoud WiFi"
            image["width"] = "1024"
            image["height"] = "1024"

    nav = soup.select_one(".site-header .nav-links")
    if nav and not nav.select_one(".nav-phone"):
        phone = soup.new_tag("a", href=f"tel:{PHONE_E164}")
        phone["class"] = ["nav-phone"]
        phone["aria-label"] = f"Call Berthoud WiFi at {PHONE_DISPLAY}"
        icon = soup.new_tag("span")
        icon["aria-hidden"] = "true"
        icon.string = "☎"
        phone.append(icon)
        phone.append(NavigableString(PHONE_DISPLAY))
        cta = nav.select_one(".btn-primary")
        if cta:
            cta.insert_before(phone)
        else:
            nav.append(phone)


def update_footer(soup: BeautifulSoup) -> None:
    footer = soup.select_one(".site-footer")
    if not footer:
        return
    for img in footer.select(".brand img"):
        img["src"] = LOGO_PATH
        img["alt"] = "Berthoud WiFi"
        img["width"] = "1024"
        img["height"] = "1024"
    if footer.select_one(".footer-contact"):
        return
    first_col = footer.select_one(".footer-grid > div")
    if not first_col:
        return
    contact = soup.new_tag("div")
    contact["class"] = ["footer-contact"]
    contact.append(BeautifulSoup(
        f'<a href="tel:{PHONE_E164}"><span aria-hidden="true">☎</span>{PHONE_DISPLAY}</a>'
        f'<a href="mailto:{EMAIL}">{EMAIL}</a>'
        f'<span class="footer-social"><a href="{FACEBOOK}" target="_blank" rel="noopener noreferrer">Facebook</a>'
        f'<a href="{LINKEDIN}" target="_blank" rel="noopener noreferrer">LinkedIn</a></span>',
        "html.parser",
    ))
    first_col.append(contact)


def update_contact_page(soup: BeautifulSoup) -> None:
    if soup.select_one(".direct-contact"):
        return
    target = soup.select_one(".contact-layout > div") or soup.select_one("main .container")
    if not target:
        return
    card = BeautifulSoup(
        f'<div class="direct-contact" aria-label="Direct contact options">'
        f'<h2>Talk with Berthoud WiFi</h2>'
        f'<p><a href="tel:{PHONE_E164}">Call {PHONE_DISPLAY}</a></p>'
        f'<p><a href="mailto:{EMAIL}">{EMAIL}</a></p>'
        f'<p class="direct-social"><a href="{FACEBOOK}" target="_blank" rel="noopener noreferrer">Facebook</a> · '
        f'<a href="{LINKEDIN}" target="_blank" rel="noopener noreferrer">LinkedIn</a></p>'
        f'</div>',
        "html.parser",
    )
    target.append(card)


def replace_copy(soup: BeautifulSoup) -> None:
    replacements = {
        "Request a Quote": "Get a quote",
        "Request a quote": "Get a quote",
        "Get a Quote": "Get a quote",
        "See How Installation Works": "See how installs work",
        "Explore Rural Connectivity": "Explore rural connectivity",
        "View All Services": "View all services",
    }
    for node in soup.find_all(string=True):
        if node.parent and node.parent.name in {"script", "style"}:
            continue
        text = str(node)
        new = text
        for old, replacement in replacements.items():
            new = new.replace(old, replacement)
        if new != text:
            node.replace_with(new)


def apply_image_attributes(soup: BeautifulSoup, mapping: dict[str, dict[str, Any]]) -> None:
    first_lcp_done = False
    for img in soup.find_all("img"):
        src = img.get("src", "")
        info = mapping.get(src)
        if info:
            img["src"] = info["src"]
            img["width"] = str(info["width"])
            img["height"] = str(info["height"])
            if info.get("srcset"):
                img["srcset"] = ", ".join(f"{url} {width}w" for url, width in info["srcset"])
                img["sizes"] = "(max-width: 700px) 100vw, (max-width: 1100px) 50vw, 760px"
        elif src == LOGO_PATH or "logo" in src.lower():
            img.setdefault("width", "1024")
            img.setdefault("height", "1024")

        img["decoding"] = "async"
        ancestor_classes = " ".join(" ".join(parent.get("class", [])) for parent in img.parents if isinstance(parent, Tag))
        likely_lcp = any(key in ancestor_classes for key in ("home-hero", "authority-hero", "inner-hero", "page-hero", "featured-post"))
        if likely_lcp and not first_lcp_done:
            img["loading"] = "eager"
            img["fetchpriority"] = "high"
            first_lcp_done = True
        else:
            img["loading"] = "lazy"
            img.attrs.pop("fetchpriority", None)


def update_html(path: Path, mapping: dict[str, dict[str, Any]]) -> None:
    raw = path.read_text(encoding="utf-8")
    soup = BeautifulSoup(raw, "lxml")
    if not soup.head:
        return
    soup.html["lang"] = "en-US"

    # Design fonts and override stylesheet.
    ensure_link(soup, "preconnect", "https://fonts.googleapis.com")
    ensure_link(soup, "preconnect", "https://fonts.gstatic.com", crossorigin="anonymous")
    ensure_link(soup, "stylesheet", "https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,600;9..144,700&family=Inter:wght@400;500;600&display=swap")
    ensure_link(soup, "stylesheet", "/assets/css/brand-refresh.css?v=17")
    ensure_link(soup, "sitemap", "/sitemap.xml", type="application/xml")

    title = soup.title.get_text(strip=True) if soup.title else "Berthoud WiFi"
    desc_tag = soup.head.find("meta", attrs={"name": "description"})
    description = desc_tag.get("content", "Professional UniFi WiFi and networking services across Northern Colorado.") if desc_tag else "Professional UniFi WiFi and networking services across Northern Colorado."
    canonical = soup.head.find("link", rel="canonical")
    canonical_url = canonical.get("href") if canonical else f"{SITE_URL}/"

    title_map = {
        "Industry Network Solutions": "Industry Network Solutions in Northern Colorado | Berthoud WiFi",
        "Network Solutions | Berthoud WiFi": "Network Solutions in Northern Colorado | Berthoud WiFi",
    }
    if title in title_map:
        title = title_map[title]
        soup.title.string = title

    ensure_meta(soup, name="robots", content="index, follow, max-image-preview:large, max-snippet:-1, max-video-preview:-1")
    ensure_meta(soup, name="theme-color", content=INK)
    ensure_meta(soup, prop="og:site_name", content="Berthoud WiFi")
    ensure_meta(soup, prop="og:title", content=title)
    ensure_meta(soup, prop="og:description", content=description)
    ensure_meta(soup, prop="og:type", content="article" if any(part in path.parts for part in ("news", "guides")) and path.name != "index.html" else "website")
    ensure_meta(soup, prop="og:url", content=canonical_url)
    ensure_meta(soup, prop="og:image", content=f"{SITE_URL}{SOCIAL_IMAGE_PATH}")
    ensure_meta(soup, prop="og:image:width", content="1200")
    ensure_meta(soup, prop="og:image:height", content="630")
    ensure_meta(soup, prop="og:image:type", content="image/png")
    ensure_meta(soup, prop="og:image:alt", content="Berthoud WiFi professional UniFi systems in Northern Colorado")
    ensure_meta(soup, name="twitter:card", content="summary_large_image")
    ensure_meta(soup, name="twitter:title", content=title)
    ensure_meta(soup, name="twitter:description", content=description)
    ensure_meta(soup, name="twitter:image", content=f"{SITE_URL}{SOCIAL_IMAGE_PATH}")
    ensure_meta(soup, name="twitter:image:alt", content="Berthoud WiFi professional UniFi systems in Northern Colorado")

    for script in soup.find_all("script", type="application/ld+json"):
        try:
            data = json.loads(script.string or script.get_text())
            enrich_schema(data)
            script.string = json.dumps(data, separators=(",", ":"), ensure_ascii=False)
        except Exception:
            continue

    relative = path.relative_to(ROOT).as_posix()
    if relative == "index.html":
        add_homepage_faq_schema(soup)
        add_website_schema(soup)
    if relative == "contact.html":
        update_contact_page(soup)

    replace_copy(soup)
    update_navigation(soup)
    update_footer(soup)
    apply_image_attributes(soup, mapping)

    # Remove old portrait logo references from markup.
    for img in soup.find_all("img"):
        src = img.get("src", "")
        if src.endswith("/berthoud-wifi-logo.png"):
            img["src"] = LOGO_PATH

    path.write_text("<!doctype html>\n" + str(soup.html), encoding="utf-8")


def write_brand_css() -> None:
    css = r'''/* Berthoud WiFi v17 design system: editorial, local, and conversion-focused. */
:root{
  --ink:#16233B;
  --body-text:#5B6472;
  --accent-blue:#1958C4;
  --accent-clay:#BC5B2E;
  --accent-clay-soft:#FDF3ED;
  --bg-white:#FFFFFF;
  --bg-tint:#F4F6F9;
  --border:#E7E9EE;
  --photo-placeholder:#E1E6EC;
  --text:var(--ink);
  --muted:var(--body-text);
  --accent:var(--accent-blue);
  --accent-2:var(--accent-blue);
  --line:var(--border);
  --panel:#fff;
  --panel-2:#fff;
  --radius:10px;
  --shadow:none;
}
html{background:var(--bg-white)}
body{font-family:Inter,ui-sans-serif,system-ui,-apple-system,BlinkMacSystemFont,"Segoe UI",sans-serif;background:var(--bg-white);color:var(--ink);font-weight:400}
p,li,.lead,.prose p,.prose li,.article-content p,.article-content li,.authority-content p,.authority-content li{color:var(--body-text)}
h1,h2{font-family:Fraunces,Georgia,serif;font-weight:700;color:var(--ink);letter-spacing:-.025em}
h3,h4,h5,h6,.card h3,.home-service-card h3,.project-photo-card h3,.resource-card h3{font-family:Inter,ui-sans-serif,sans-serif;font-weight:500;color:var(--ink);letter-spacing:-.01em}
a{transition:color .18s ease,border-color .18s ease,background-color .18s ease,box-shadow .18s ease,transform .18s ease}
.eyebrow{font-family:Inter,sans-serif;font-size:11px;font-weight:600;letter-spacing:.04em;color:var(--accent-blue);text-transform:uppercase}
.site-header{background:rgba(255,255,255,.97);border-bottom:1px solid var(--border);box-shadow:0 2px 12px rgba(22,35,59,.04)}
.site-header .brand,.site-header .nav-links a,.nav-dropdown-toggle{color:var(--ink)}
.site-header .brand{font-weight:600}
.site-header .brand img{border-radius:50%;box-shadow:none}
.site-header .nav-links a:hover,.nav-dropdown-toggle:hover,.nav-dropdown a:hover{color:var(--accent-blue)!important}
.site-header .nav-links{gap:12px}
.nav-phone{gap:7px;color:var(--ink)!important;font-weight:600!important}
.nav-phone span{color:var(--accent-blue);font-size:.95rem}
.nav-dropdown{border:1px solid var(--border);border-radius:10px;box-shadow:0 14px 35px rgba(22,35,59,.10)}
.nav-dropdown a:hover{background:var(--bg-tint)}
.btn{border-radius:7px;font-family:Inter,sans-serif;font-weight:500;text-transform:none;box-shadow:none;padding:11px 17px}
.btn-primary,.site-header .nav-links .btn-primary,.site-header .nav-links .btn-primary:visited{background:var(--accent-clay)!important;color:#fff!important;border-color:var(--accent-clay)!important;box-shadow:none!important}
.btn-primary:hover,.site-header .nav-links .btn-primary:hover{background:#A94F28!important;transform:translateY(-1px);filter:none}
.btn-secondary{background:#fff;color:var(--ink);border:1px solid #C7CDD6}
.btn-secondary:hover{border-color:var(--ink);background:var(--bg-tint)}
.link-arrow{color:var(--accent-clay)!important;font-weight:500}
.link-arrow:hover{color:#934521!important}
.section{background:var(--bg-white)}
.section-dark{background:var(--bg-tint);border-top:1px solid var(--border);border-bottom:1px solid var(--border)}
.card,.sidebar-card,.quote-card,.home-service-card,.project-photo-card,.resource-card,.featured-post,.editorial-card,.process-step,.fact,.toc-card{background:#fff!important;border:1px solid var(--border)!important;border-radius:10px!important;box-shadow:none!important}
.card:hover,.home-service-card:hover,.project-photo-card:hover,.resource-card:hover,.editorial-card:hover{box-shadow:0 10px 24px rgba(22,35,59,.07)!important;transform:translateY(-1px)}
.home-service-card,.project-photo-card,.news-card,.featured-post,.editorial-card{overflow:hidden}
.home-service-card h3,.project-photo-card h3{font-weight:500}
.photo-frame,.service-image,.local-section img,.local-photo,.article-hero-image,.authority-hero img,.inner-hero-photo{border-radius:10px!important;border:1px solid var(--border)!important;box-shadow:none!important;background:var(--photo-placeholder)}
.photo-frame img,.home-service-card img,.project-photo-card img,.news-card img,.featured-post img,.editorial-card img{background:var(--photo-placeholder)}
img{height:auto}
.photo-frame img,.home-service-card img,.project-photo-card img,.local-section img,.authority-hero img,.news-card img,.editorial-card img,.featured-post img{object-fit:cover}
.checklist li:before,.sidebar-card li::before{color:var(--accent-blue)!important;background:transparent}
.city-list a{border-radius:7px;background:#fff;border:1px solid var(--border);color:var(--body-text);font-weight:500}
.city-list a:hover{color:var(--accent-blue);border-color:rgba(25,88,196,.35)}
.faq details{background:#fff;border:1px solid var(--border);border-radius:10px;box-shadow:none}
.faq summary{font-weight:500;color:var(--ink)}
.cta,.content-cta{background:var(--bg-tint);border:1px solid var(--border);border-radius:10px;color:var(--ink);box-shadow:none}
.home-hero::before{background:linear-gradient(90deg,rgba(255,255,255,.99) 0%,rgba(255,255,255,.93) 42%,rgba(255,255,255,.52) 72%,rgba(255,255,255,.18) 100%),url("https://images.unsplash.com/photo-1497366754035-f200968a6e72?auto=format&fit=crop&w=1800&q=82") center/cover no-repeat}
.home-hero h1{font-family:Fraunces,Georgia,serif;font-weight:700;color:var(--ink)}
.home-hero .lead{color:var(--body-text)}
.home-proof div{background:rgba(255,255,255,.94);border:1px solid var(--border);border-radius:8px;box-shadow:none;backdrop-filter:blur(5px)}
.home-proof strong{color:var(--ink);font-weight:600}
.home-proof span{color:var(--body-text)}
.icon,.icon-png{background:rgba(25,88,196,.08);color:var(--accent-blue)}
.post-meta{color:var(--accent-blue)}
.note{border-left-color:var(--accent-blue);background:rgba(25,88,196,.06)}
.local-copy{background:var(--bg-tint);border:1px solid var(--border)}
.form-field input,.form-field select,.form-field textarea{background:#fff!important;color:var(--ink)!important;border:1px solid var(--border)!important;border-radius:7px}
.form-field input:focus,.form-field select:focus,.form-field textarea:focus{outline:2px solid rgba(25,88,196,.22);border-color:var(--accent-blue)!important}
.check-grid label:hover{border-color:rgba(25,88,196,.35)!important;background:rgba(25,88,196,.04)!important;color:var(--ink)!important}
.direct-contact{margin-top:28px;padding:22px;background:var(--bg-tint);border:1px solid var(--border);border-radius:10px}
.direct-contact h2{font-size:1.55rem;margin-bottom:12px}
.direct-contact p{margin:7px 0}
.direct-contact a{color:var(--accent-blue);font-weight:500;text-decoration:none}
.site-footer{margin-top:0;padding:48px 0 28px;background:var(--ink);color:#A9B4C4}
.site-footer .brand,.site-footer strong,.site-footer a{color:#fff}
.site-footer p{color:#A9B4C4}
.site-footer .brand img{background:#fff;border-radius:50%}
.footer-contact{display:grid;gap:8px;margin-top:17px}
.footer-contact>a{display:inline-flex;align-items:center;gap:8px;width:max-content;text-decoration:none}
.footer-contact>a span{color:var(--accent-blue)}
.footer-social{display:flex;gap:14px;margin-top:3px}
.footer-social a{color:#DCE3EC;text-decoration:none}
.footer-social a:hover{color:#fff}
@media(max-width:1080px){.nav-phone{order:20}.site-header .nav-links .btn{order:21}}
@media(max-width:700px){.home-hero h1{font-size:clamp(2.45rem,12vw,3.6rem)}.site-footer{padding-top:38px}}
'''
    target = ROOT / "assets" / "css" / "brand-refresh.css"
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(css, encoding="utf-8")


def update_headers() -> None:
    path = ROOT / "_headers"
    if not path.exists():
        return
    text = path.read_text(encoding="utf-8")
    csp = (
        "  Content-Security-Policy: default-src 'self'; "
        "img-src 'self' data: https:; "
        "style-src 'self' 'unsafe-inline' https://fonts.googleapis.com; "
        "script-src 'self' 'unsafe-inline' https://www.googletagmanager.com https://www.google-analytics.com; "
        "font-src 'self' data: https://fonts.gstatic.com; "
        "connect-src 'self' https://www.google-analytics.com https://region1.google-analytics.com; "
        "frame-ancestors 'self'; base-uri 'self'; form-action 'self' mailto:;"
    )
    if "Content-Security-Policy:" in text:
        text = re.sub(r"^\s*Content-Security-Policy:.*$", csp, text, flags=re.MULTILINE)
    else:
        text = text.rstrip() + "\n" + csp + "\n"
    path.write_text(text, encoding="utf-8")


def update_manifest() -> None:
    path = ROOT / "manifest.webmanifest"
    if not path.exists():
        return
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except Exception:
        return
    data["name"] = "Berthoud WiFi"
    data["short_name"] = "Berthoud WiFi"
    data["theme_color"] = INK
    data["background_color"] = "#FFFFFF"
    data["icons"] = [
        {"src": "/favicon.png?v=17", "sizes": "256x256", "type": "image/png"},
        {"src": "/apple-touch-icon.png?v=17", "sizes": "180x180", "type": "image/png"},
    ]
    path.write_text(json.dumps(data, indent=2) + "\n", encoding="utf-8")


def update_sitemap() -> None:
    path = ROOT / "sitemap.xml"
    if not path.exists():
        return
    text = path.read_text(encoding="utf-8")
    text = re.sub(r"<lastmod>\d{4}-\d{2}-\d{2}</lastmod>", f"<lastmod>{TODAY}</lastmod>", text)
    path.write_text(text, encoding="utf-8")


def main() -> None:
    print("Generating flat logo and social card…")
    make_logo()
    make_social_card()
    print("Optimizing photography…")
    mapping = optimize_images()
    update_css_image_urls(mapping)
    write_brand_css()
    print("Updating HTML…")
    for html in ROOT.rglob("*.html"):
        if any(part.startswith(".") for part in html.relative_to(ROOT).parts):
            continue
        update_html(html, mapping)
    update_headers()
    update_manifest()
    update_sitemap()
    print(f"Updated {len(list(ROOT.rglob('*.html')))} HTML files and {len(mapping)} image references.")


if __name__ == "__main__":
    main()
