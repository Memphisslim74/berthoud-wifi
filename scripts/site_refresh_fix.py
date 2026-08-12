#!/usr/bin/env python3
"""Post-processing fixes for the generated Berthoud WiFi refresh."""

import json
import re
from pathlib import Path

from bs4 import BeautifulSoup

ROOT = Path(__file__).resolve().parents[1]
HERO_IMAGES = (
    ("/assets/images/hero-office-v22-800.webp", "(max-width: 700px)"),
    ("/assets/images/hero-office-v22-1600.webp", "(min-width: 701px)"),
)
BRAND_CSS = "/assets/css/brand-refresh.css?v=22"
SITE_JS = "/assets/js/site.js?v=22"
LOGO_PATH = "/assets/images/berthoud-wifi-logo.webp?v=21"

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
.sitewide-contact{padding:64px 0;background:var(--bg-tint);border-top:1px solid var(--border)}
.sitewide-contact-grid{display:grid;grid-template-columns:minmax(240px,.72fr) minmax(0,1.28fr);gap:48px;align-items:start}
.sitewide-contact-copy{padding-top:8px}
.sitewide-contact-copy h2{margin:10px 0 14px;font-size:clamp(2rem,4vw,3rem)}
.sitewide-contact-copy p{max-width:46ch;margin:0 0 20px}
.sitewide-contact-direct{display:grid;gap:8px}
.sitewide-contact-direct a{width:max-content;color:var(--accent-blue);font-weight:600;text-decoration:none}
.compact-contact-form{padding:24px}
.compact-contact-form textarea{min-height:118px}
.thank-you-card{max-width:820px;margin:0 auto;padding:clamp(28px,5vw,54px);text-align:center}
.thank-you-card h1{margin:10px 0 16px}
.thank-you-next{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:14px;margin:30px 0;text-align:left}
.thank-you-step{padding:18px;background:var(--bg-tint);border:1px solid var(--border);border-radius:10px}
.thank-you-step strong{display:block;margin-bottom:7px;color:var(--ink)}
.thank-you-step p{margin:0;font-size:.92rem}
@media(max-width:700px){
  .cta>.btn,.content-cta>.btn{width:100%;max-width:280px;align-self:flex-start}
  .form-actions .btn{width:100%;max-width:none}
  .sitewide-contact{padding:46px 0}
  .sitewide-contact-grid{grid-template-columns:1fr;gap:28px}
  .thank-you-next{grid-template-columns:1fr}
}

/* v21 professional navigation and approved full-detail logo. */
@media(min-width:1441px){
  .site-header .container.nav{
    width:min(1540px,calc(100% - 44px));
    max-width:1540px;
    min-height:148px;
    gap:clamp(22px,2.2vw,38px);
  }
  .site-header .brand{
    gap:16px;
    flex:0 0 auto;
  }
  .site-header .brand img{
    width:128px;
    height:128px;
    flex-basis:128px;
    object-fit:contain;
    border-radius:0;
  }
  .site-header .brand span{
    font-size:1.14rem;
    font-weight:650;
    letter-spacing:-.02em;
  }
  .site-header .nav-links{
    flex:1;
    justify-content:flex-end;
    gap:clamp(13px,1.15vw,21px);
  }
  .site-header .nav-links > a,
  .site-header .nav-links > .nav-item > button{
    min-height:48px;
    font-size:.94rem;
    font-weight:650;
    letter-spacing:-.01em;
  }
  .site-header .nav-phone{
    min-height:46px;
    margin-left:3px;
    padding:0 15px!important;
    border:1px solid var(--border);
    border-radius:7px;
    background:var(--bg-tint);
  }
  .site-header .nav-links .btn{
    min-height:46px;
    padding:13px 21px;
    margin-left:0;
    font-weight:650;
  }
}

@media(max-width:1440px){
  .site-header .container.nav{
    min-height:102px;
  }
  .site-header .brand img{
    width:88px;
    height:88px;
    flex-basis:88px;
    object-fit:contain;
    border-radius:0;
  }
  .site-header .brand span{
    font-size:1.02rem;
    font-weight:600;
  }
  .site-header .nav-phone{
    margin-left:0;
    padding-left:10px!important;
    border-left:0;
    background:transparent;
  }
  .site-header .menu-btn{
    display:inline-flex;
    align-items:center;
    justify-content:center;
    min-height:44px;
    padding:10px 15px;
    color:var(--ink);
    background:#fff;
    border:1px solid var(--border);
    font-weight:650;
  }
  .site-header .nav-links{
    display:none;
    position:absolute;
    top:108px;
    left:20px;
    right:20px;
    flex-direction:column;
    align-items:stretch;
    gap:2px;
    padding:14px;
    background:#fff;
    border:1px solid var(--border);
    border-radius:10px;
    box-shadow:0 22px 55px rgba(22,35,59,.16);
  }
  .site-header .nav-links.is-open,
  .site-header .nav-links.open{display:flex}
  .site-header .nav-links > a,
  .site-header .nav-links > .nav-item > button{
    width:100%;
    min-height:46px;
    justify-content:flex-start;
    padding:12px 13px;
    font-size:1rem;
    font-weight:600;
  }
  .site-header .nav-links .btn{
    width:100%;
    max-width:none;
    justify-content:center;
    margin-top:8px;
  }
  .nav-item{
    display:block;
    padding-bottom:0;
    margin-bottom:0;
  }
  .nav-dropdown-toggle::after{margin-left:auto}
  .nav-dropdown{
    position:static;
    transform:none;
    min-width:0;
    margin:0 0 6px 10px;
    padding:4px;
    background:var(--bg-tint);
    border:0;
    border-radius:8px;
    box-shadow:none;
  }
  .nav-dropdown::before{display:none}
  .nav-item:hover .nav-dropdown{display:none}
  .nav-item.is-open .nav-dropdown{display:grid}
}

@media(max-width:520px){
  .site-header .container.nav{
    min-height:84px;
  }
  .site-header .brand img{
    width:70px;
    height:70px;
    flex-basis:70px;
  }
  .site-header .brand span{font-size:1rem}
  .site-header .nav-links{
    top:90px;
  }
}

.cyber-outcome-grid,.cyber-service-grid,.cyber-proof-grid{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:18px}
.cyber-outcome,.cyber-service,.cyber-proof{padding:24px;background:#fff;border:1px solid var(--border);border-radius:10px}
.cyber-outcome strong{display:block;margin-bottom:8px;color:var(--ink);font-size:1.08rem}
.cyber-service h3,.cyber-proof h3{margin-top:0}
.cyber-step{display:grid;grid-template-columns:52px minmax(0,1fr);gap:16px;align-items:start;padding:20px 0;border-bottom:1px solid var(--border)}
.cyber-step:last-child{border-bottom:0}
.cyber-step-number{display:grid;place-items:center;width:44px;height:44px;border-radius:50%;background:rgba(25,88,196,.09);color:var(--accent-blue);font-weight:700}
.cyber-boundary{padding:20px;border-left:4px solid var(--accent-blue);background:var(--bg-tint);border-radius:0 10px 10px 0}
@media(max-width:900px){.cyber-outcome-grid,.cyber-service-grid,.cyber-proof-grid{grid-template-columns:1fr}}
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


def ensure_consulting_navigation(soup: BeautifulSoup) -> None:
    for brand in soup.select(".site-header .brand img, .site-footer .brand img"):
        brand["src"] = LOGO_PATH
        brand["alt"] = "Berthoud WiFi"
        brand["width"] = "768"
        brand["height"] = "768"

    nav = soup.select_one(".site-header .nav-links")
    existing_top_level = nav.find(
        "a",
        href=lambda value: value and value.startswith("/cybersecurity-consulting"),
        recursive=False,
    ) if nav else None
    if nav and not existing_top_level:
        consulting = soup.new_tag("a", href="/cybersecurity-consulting/")
        consulting.string = "Cyber Consulting"
        about = nav.find("a", href=lambda value: value and value.startswith("/about"))
        if about:
            about.insert_before(consulting)
        else:
            phone = nav.select_one(".nav-phone")
            phone.insert_before(consulting) if phone else nav.append(consulting)

    for dropdown in soup.select(".nav-dropdown"):
        if dropdown.select_one('a[href^="/cybersecurity-consulting"]'):
            continue
        link = soup.new_tag("a", href="/cybersecurity-consulting/")
        link.string = "Cybersecurity Consulting"
        dropdown.append(link)

    for footer in soup.select(".site-footer"):
        if footer.select_one('a[href^="/cybersecurity-consulting"]'):
            continue
        columns = footer.select(".footer-links")
        target = columns[0] if columns else None
        if target:
            link = soup.new_tag("a", href="/cybersecurity-consulting/")
            link.string = "Cybersecurity Consulting"
            target.append(link)


def ensure_consulting_form_option(soup: BeautifulSoup) -> None:
    for select in soup.select('select[name="services"]'):
        if any("Cybersecurity" in option.get_text() for option in select.find_all("option")):
            continue
        option = soup.new_tag("option")
        option.string = "Cybersecurity risk consulting"
        first = select.find("option")
        first.insert_after(option) if first else select.append(option)

    for picker in soup.select(".service-picker .check-grid"):
        if picker.select_one('input[value="Cybersecurity risk consulting"]'):
            continue
        label = soup.new_tag("label")
        checkbox = soup.new_tag(
            "input",
            attrs={
                "name": "services",
                "type": "checkbox",
                "value": "Cybersecurity risk consulting",
            },
        )
        label.append(checkbox)
        label.append(" Cybersecurity risk consulting")
        picker.insert(0, label)


def fix_html(path: Path) -> None:
    soup = BeautifulSoup(path.read_text(encoding="utf-8"), "lxml")
    if not soup.head:
        return

    ensure_consulting_navigation(soup)
    ensure_consulting_form_option(soup)

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

    brand_stylesheets = soup.head.find_all(
        "link",
        rel="stylesheet",
        href=lambda value: value and value.startswith("/assets/css/brand-refresh.css"),
    )
    if brand_stylesheets:
        brand_stylesheets[0]["href"] = BRAND_CSS
        for duplicate in brand_stylesheets[1:]:
            duplicate.decompose()
    else:
        soup.head.append(soup.new_tag("link", rel="stylesheet", href=BRAND_CSS))

    site_scripts = soup.find_all(
        "script",
        src=lambda value: value and value.startswith("/assets/js/site.js"),
    )
    if site_scripts:
        site_scripts[0]["src"] = SITE_JS
        for duplicate in site_scripts[1:]:
            duplicate.decompose()

    gtag_loaders = soup.find_all(
        "script", src=lambda value: value and "googletagmanager.com/gtag/js" in value
    )
    for duplicate in gtag_loaders[1:]:
        duplicate.decompose()

    for link in list(soup.head.find_all("link", href=True)):
        href = link.get("href", "")
        if href.startswith("https://fonts.googleapis.com") or href == "https://fonts.gstatic.com":
            link.decompose()
        elif href == "https://challenges.cloudflare.com" and "preconnect" in link.get("rel", []):
            link.decompose()

    dedupe_jsonld(soup)
    relative = path.relative_to(ROOT).as_posix()

    if relative == "index.html":
        for preload in list(soup.head.find_all("link", rel="preload")):
            href = preload.get("href", "")
            if "photo-1497366754035" in href or "hero-office-v22" in href:
                preload.decompose()
        for href, media in HERO_IMAGES:
            preload = soup.new_tag("link", rel="preload", href=href)
            preload["as"] = "image"
            preload["type"] = "image/webp"
            preload["media"] = media
            preload["fetchpriority"] = "high"
            soup.head.append(preload)

    for img in soup.select(".site-header .brand img"):
        img["loading"] = "eager"
        img["fetchpriority"] = "low"
    for img in soup.select(".site-footer .brand img"):
        img["loading"] = "lazy"
        img.attrs.pop("fetchpriority", None)

    if not soup.select_one("[data-contact-form]"):
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
    text = re.sub(
        r"/\* Berthoud WiFi v\d+ design system:",
        "/* Berthoud WiFi v22 design system:",
        text,
        count=1,
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
        "style-src 'self' 'unsafe-inline'; "
        "script-src 'self' 'unsafe-inline' https://www.googletagmanager.com "
        "https://www.google-analytics.com https://challenges.cloudflare.com; "
        "font-src 'self' data:; "
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
        parts = html.relative_to(ROOT).parts
        if any(part in {"dist", "node_modules"} or part.startswith(".") for part in parts):
            continue
        fix_html(html)


if __name__ == "__main__":
    main()
