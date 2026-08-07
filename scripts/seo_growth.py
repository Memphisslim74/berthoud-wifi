#!/usr/bin/env python3
"""Ongoing SEO growth tasks for Berthoud WiFi.

Runs after the legacy refresh scripts so canonical URLs, internal links, sitemap
entries, priority-page metadata, analytics events, and scheduled articles end in
one consistent state.
"""

from __future__ import annotations

import json
import re
from datetime import datetime
from pathlib import Path
from urllib.parse import urlsplit, urlunsplit
from zoneinfo import ZoneInfo

from bs4 import BeautifulSoup

ROOT = Path(__file__).resolve().parents[1]
SITE_URL = "https://berthoudwifi.com"
BASELINE_LASTMOD = "2026-08-07"
DENVER = ZoneInfo("America/Denver")
TODAY = datetime.now(DENVER).date().isoformat()

POSTS = [
    {
        "slug": "professional-wifi-installation-cost-northern-colorado",
        "date": "2026-08-07",
        "title": "How Much Does Professional WiFi Installation Cost in Northern Colorado?",
        "description": "What drives the cost of professional WiFi installation in Northern Colorado, from access points and cabling to barns, offices, cameras, and UniFi equipment.",
        "image": "/assets/images/actual/business-consultation.webp",
        "image_alt": "Planning a professional WiFi and network installation",
        "category": "Planning & cost",
        "body": r'''
<p>When someone asks what professional WiFi installation costs, the most accurate answer is that the price follows the property and the problem. A single weak room in a newer home is a very different project from a multi-story house with a detached garage, a shop, outdoor cameras, or an office full of employees.</p>
<p>The useful question is not just “How much is an access point?” It is “What will it take to make the network dependable where people and devices actually use it?” A professional design accounts for coverage, cabling, switching, power, internet service, device count, building materials, and how the network may grow.</p>
<h2>The biggest factors that affect WiFi installation cost</h2>
<p><strong>Property size and construction.</strong> Square footage matters, but walls and layout often matter more. Stone, concrete, metal, radiant barriers, ductwork, and multiple floors can reduce signal strength. A long ranch-style home can need a different design than a compact two-story home of the same size.</p>
<p><strong>Access point count and placement.</strong> Better WiFi usually comes from placing the right number of wired access points in useful locations rather than buying the most powerful router available. A site survey and a look at the floor plan help determine whether the project needs one additional access point or several.</p>
<p><strong>Cabling and backhaul.</strong> Ethernet is often the best backhaul inside a home or office. Fiber can make sense between buildings or in locations where electrical isolation and distance matter. Existing Cat6 or Cat6A may be reusable, while older or poorly terminated cable may need to be repaired or replaced.</p>
<p><strong>Switching, gateway, and power.</strong> A UniFi installation may include a gateway, PoE switching, rack equipment, patch panels, UPS protection, and network configuration. If the existing equipment is still appropriate, it does not automatically need to be replaced.</p>
<p><strong>Special coverage areas.</strong> Garages, patios, barns, shops, acreage, gates, cameras, and detached offices can add design requirements. Those areas may need outdoor access points, a point-to-point bridge, buried fiber, or a separate switch.</p>
<h2>Why a cheap extender can become the expensive option</h2>
<p>Consumer extenders are inexpensive because they are easy to add, but they can repeat an already weak wireless signal and create inconsistent roaming. That can lead to years of buying another router, another mesh node, or another extender without fixing placement or backhaul.</p>
<p>If the goal is simply one stronger room, a small change may be enough. If the goal is property-wide coverage, cameras, smart-home devices, work-from-home reliability, or business operations, it usually makes more sense to design the network as a system.</p>
<h2>Home installations and business installations are scoped differently</h2>
<p>A home project may prioritize video calls, streaming, gaming, smart-home devices, outdoor coverage, and clean equipment placement. A business project may also require guest WiFi, VLANs, security cameras, VoIP, point-of-sale systems, printers, door access, traffic separation, and easier troubleshooting.</p>
<p>That is why Berthoud WiFi does not publish a one-size-fits-all package price. The goal is to avoid selling equipment that does not solve the actual problem. A quote should identify the work, the equipment, the cabling, and what the finished network is expected to support.</p>
<h2>What should be included in a professional WiFi quote?</h2>
<ul>
<li>Coverage goals and problem areas.</li>
<li>Recommended access point locations.</li>
<li>Required Ethernet, fiber, or wireless bridge work.</li>
<li>Gateway, switching, PoE, and rack requirements.</li>
<li>Configuration for primary, guest, and device networks where needed.</li>
<li>Testing, labeling, and final documentation.</li>
<li>Options for future cameras, access control, or additional buildings.</li>
</ul>
<p>For a closer look at the process, see <a href="/installations">what to expect from an installation</a> and our <a href="/services/unifi-network-installation">UniFi network installation service</a>.</p>
<h2>Start with the problem, not the shopping list</h2>
<p>If your internet plan is fast but the house still has dead zones, or if a business network has grown into a mix of routers and switches, the fastest way to get an accurate cost is to scope the property first. Berthoud WiFi serves Berthoud, Loveland, Fort Collins, Longmont, and surrounding Northern Colorado communities.</p>
<p>Tell us what is not working, where you need coverage, and what devices or buildings need to connect. We can recommend a practical design and provide a project-specific quote.</p>
''',
    },
    {
        "slug": "business-wifi-installation-loveland-co",
        "date": "2026-08-09",
        "title": "Business WiFi Installation in Loveland, CO: What a Professional Network Should Include",
        "description": "A practical guide to business WiFi and office network installation in Loveland, Colorado, including access points, VLANs, PoE, cameras, cabling, and guest networks.",
        "image": "/assets/images/actual/connected-business.webp",
        "image_alt": "Connected small business network environment",
        "category": "Loveland business networks",
        "body": r'''
<p>A business can have fast internet service and still have a network that feels slow, unreliable, or difficult to manage. The internet circuit is only one part of the system. Access point placement, switching, cabling, network segmentation, interference, and the number of connected devices all affect how the network performs.</p>
<p>For businesses in Loveland, a professional WiFi installation should be designed around how the space actually operates. An office, retail shop, warehouse, restaurant, clinic, church, and production space may all need different coverage and security choices.</p>
<h2>Start with coverage and capacity</h2>
<p>A single consumer router may work in a small office, but it becomes a bottleneck when employees, guests, phones, cameras, printers, TVs, point-of-sale devices, and smart equipment all depend on it. A professional design uses multiple access points where needed and plans channel use so those access points work together instead of competing with each other.</p>
<p>Access points should be placed for the people and devices using the network. Mounting everything near the internet modem because that is where the cable enters the building is convenient, but it is rarely the best coverage plan.</p>
<h2>Use wired backhaul wherever practical</h2>
<p>Business access points perform best when they have a dependable wired path back to the network. Cat6 or Cat6A is common inside buildings, while fiber can be useful for longer runs, electrical isolation, or building-to-building links. PoE switching can provide both network connectivity and power to access points, cameras, phones, and other supported equipment.</p>
<p>If the business already has structured cabling, it should be tested before assuming it needs replacement. Reusing good infrastructure can reduce cost while still allowing the network electronics to be modernized.</p>
<h2>Separate employees, guests, and devices</h2>
<p>Business WiFi should not put every device on one flat network. Guest users generally should not have access to printers, cameras, business systems, or management interfaces. IoT devices and security equipment may also belong on separate networks depending on the environment.</p>
<p>UniFi makes it possible to manage multiple SSIDs, VLANs, firewall rules, guest policies, and wired networks from one platform. The right design depends on the business, but segmentation can improve both security and troubleshooting.</p>
<h2>Plan for the systems that depend on the network</h2>
<p>WiFi is often only the visible part of the project. A Loveland business may also depend on:</p>
<ul>
<li>VoIP phones and video conferencing.</li>
<li>Security cameras and local recording.</li>
<li>Door access and intercom systems.</li>
<li>Point-of-sale terminals and payment devices.</li>
<li>Cloud applications and file transfers.</li>
<li>Guest WiFi for customers or visitors.</li>
<li>Outdoor areas, shops, or detached buildings.</li>
</ul>
<p>Those systems should influence switch capacity, PoE budget, UPS sizing, VLAN design, and the number of available Ethernet ports.</p>
<h2>What a professional installation should leave behind</h2>
<p>A finished network should be easier to understand than the one it replaced. Equipment should be mounted cleanly, cables should be labeled, network names should be intentional, firmware should be current, and the system should be tested from the areas where people actually work.</p>
<p>For growing businesses, it is also worth leaving room for additional access points, cameras, switches, or faster internet service so the next change does not require starting over.</p>
<h2>Local business WiFi help in Loveland</h2>
<p>Berthoud WiFi provides <a href="/services/small-business-infrastructure">small business network infrastructure</a>, <a href="/services/unifi-network-installation">UniFi installation</a>, <a href="/services/fiber-structured-cabling">fiber and structured cabling</a>, and <a href="/services/unifi-protect-security">UniFi Protect camera systems</a> across Northern Colorado.</p>
<p>If you are planning an office network installation in Loveland or trying to fix unreliable business WiFi, start with the <a href="/cities/loveland">Loveland service page</a> or request a site-specific quote. We can work from the systems you already have when they still make sense and recommend upgrades where they will actually improve reliability.</p>
''',
    },
    {
        "slug": "fast-internet-bad-wifi-dead-zones-northern-colorado",
        "date": "2026-08-11",
        "title": "Why Fast Internet Still Has Bad WiFi: Fixing Dead Zones in Northern Colorado Homes",
        "description": "Why a fast internet plan can still produce weak WiFi, dead zones, buffering, and unreliable video calls in Berthoud, Loveland, and Northern Colorado homes.",
        "image": "/assets/images/actual/home-laptop.webp",
        "image_alt": "Laptop connected to a home WiFi network",
        "category": "Home WiFi",
        "body": r'''
<p>Paying for gigabit internet does not guarantee gigabit WiFi in every room. Your internet provider is responsible for getting service to the modem or gateway. From there, your home network has to distribute that connection through walls, floors, furniture, appliances, and sometimes several thousand square feet of living space.</p>
<p>That is why a speed test beside the router can look excellent while a bedroom, basement, garage, patio, or home office struggles to stay connected.</p>
<h2>Internet speed and WiFi coverage are different problems</h2>
<p>Your internet plan determines the maximum capacity available to the property. WiFi determines how devices reach that connection wirelessly. If the WiFi signal is weak, congested, or poorly placed, buying a faster internet tier may not change the experience in the problem area.</p>
<p>A good troubleshooting process tests both sides. First verify what the internet connection can deliver over a wired connection. Then measure wireless performance and signal quality in the places that matter.</p>
<h2>Common causes of dead zones in Northern Colorado homes</h2>
<p><strong>Router placement.</strong> Internet equipment is often installed where the provider can reach it easily, not where wireless coverage will be best. A router in a basement utility room or at one end of a long house has to push signal through the entire structure.</p>
<p><strong>Building materials.</strong> Concrete, brick, stone, metal ductwork, radiant barriers, mirrors, and dense tile can absorb or reflect radio signals. Even ordinary walls reduce signal as distance increases.</p>
<p><strong>Too few access points.</strong> One router cannot cover every floor plan well. Larger homes often perform better with multiple access points placed closer to the devices they serve.</p>
<p><strong>Wireless backhaul.</strong> Mesh systems can be convenient, but each mesh node still needs a strong path back to the network. A node placed in a dead zone cannot magically create a good upstream connection. Wired access points generally provide more predictable performance.</p>
<p><strong>Interference and channel congestion.</strong> Neighboring WiFi networks and other radio sources can compete for airtime. This matters in subdivisions, apartments, townhomes, and dense neighborhoods.</p>
<h2>Why adding more transmit power is not always the answer</h2>
<p>WiFi is a two-way conversation. An access point may be able to transmit farther than a phone or laptop can reliably answer. Turning power up can also make roaming worse because a device may hold onto a distant access point instead of moving to a closer one.</p>
<p>Good design usually focuses on access point location, channel planning, sensible power levels, and reliable backhaul rather than trying to make one radio cover the entire property.</p>
<h2>When wired access points beat mesh</h2>
<p>If Ethernet is available or can be installed cleanly, wired access points give each access point a direct connection back to the network. That avoids spending wireless airtime repeating traffic between mesh nodes.</p>
<p>Mesh can still be useful where cabling is impractical, but it should be designed around strong node-to-node connections. See our guide to <a href="/guides/mesh-vs-wired-access-points">mesh versus wired access points</a> for a deeper comparison.</p>
<h2>What about basements, garages, patios, and outbuildings?</h2>
<p>Those areas are common trouble spots because they are farther from the router or separated by heavier construction. A garage may need a dedicated access point. An outdoor living area may benefit from an outdoor-rated AP. A detached shop or barn may need a <a href="/services/building-to-building-connectivity">wireless bridge or fiber connection</a> before WiFi is added inside that building.</p>
<h2>A better way to troubleshoot bad WiFi</h2>
<ul>
<li>Test the internet connection over Ethernet.</li>
<li>Measure WiFi in the actual problem rooms.</li>
<li>Identify where the existing access point or mesh nodes are located.</li>
<li>Check whether wired Ethernet is already available.</li>
<li>Look for building materials and layout issues.</li>
<li>Design coverage around devices and usage rather than around the modem location.</li>
</ul>
<p>Berthoud WiFi provides <a href="/services/home-network-improvements">home network improvements</a> and UniFi WiFi installation throughout Berthoud, Loveland, Fort Collins, Longmont, and nearby Northern Colorado communities. If your wired speed is good but the WiFi experience is not, the network inside the property is the right place to start.</p>
''',
    },
    {
        "slug": "wifi-house-barn-shop-detached-garage-colorado",
        "date": "2026-08-13",
        "title": "How to Get WiFi to a Barn, Shop, Detached Garage, or Outbuilding in Colorado",
        "description": "Compare fiber, Ethernet, point-to-point wireless bridges, and outdoor WiFi for connecting barns, shops, detached garages, and outbuildings in Colorado.",
        "image": "/assets/images/actual/outdoor-ap.webp",
        "image_alt": "Outdoor wireless access point for property-wide coverage",
        "category": "Rural property connectivity",
        "body": r'''
<p>Getting reliable WiFi to a detached building is not usually solved by aiming the house router at the backyard. A barn, workshop, detached garage, gate, studio, or office needs a dependable connection back to the main network first. Once that connection exists, an access point inside or outside the remote building can provide normal WiFi coverage.</p>
<p>For Northern Colorado properties, the best connection is usually one of three options: fiber, Ethernet, or a point-to-point wireless bridge. The right choice depends on distance, trenching, line of sight, electrical conditions, bandwidth needs, and how permanent the installation should be.</p>
<h2>Option 1: Fiber between buildings</h2>
<p>Fiber is often the strongest long-term choice when trenching is practical. It can cover long distances at high speed and does not conduct electricity between buildings. That electrical isolation is useful when separate structures have different grounding conditions or are exposed to lightning and outdoor electrical events.</p>
<p>A typical design runs outdoor-rated or conduit-protected fiber between network equipment at each building. The remote building can then have a PoE switch, one or more access points, cameras, and wired devices.</p>
<h2>Option 2: Ethernet between buildings</h2>
<p>Copper Ethernet can work for shorter links when installed correctly and within distance limits. It is familiar and economical, but it does create an electrical connection between structures. Outdoor runs need appropriate cable, surge protection, grounding considerations, and physical protection.</p>
<p>For a detached garage close to the house, Ethernet may be perfectly reasonable. For a more distant barn or shop, fiber is often worth considering.</p>
<h2>Option 3: Point-to-point wireless bridge</h2>
<p>A wireless bridge uses dedicated radios mounted on the two buildings to create a network link through the air. It is different from a WiFi extender. The bridge is focused on carrying traffic between two known points, while a separate access point provides WiFi to phones, laptops, cameras, or other devices at the remote building.</p>
<p>Wireless bridges can be a great option when trenching would be disruptive or expensive. They work best with good line of sight and careful mounting. Trees, terrain, metal structures, and future construction should be considered before choosing radio locations.</p>
<h2>Do not confuse the building link with the WiFi inside the building</h2>
<p>Once the barn or shop is connected, it still needs local coverage. A metal-sided building can be especially difficult for a signal coming from outside. Installing an access point inside the structure usually provides a much better experience than trying to blast WiFi through the wall.</p>
<p>Large shops may need more than one access point. Outdoor yards, arenas, patios, or parking areas may need outdoor-rated equipment mounted for those spaces.</p>
<h2>What else can use the connection?</h2>
<p>A properly connected outbuilding can support much more than phones and laptops:</p>
<ul>
<li>UniFi Protect security cameras.</li>
<li>Door access, intercoms, and gate equipment.</li>
<li>Computers, TVs, printers, and shop equipment.</li>
<li>Smart thermostats, sensors, and automation.</li>
<li>VoIP phones and video calls.</li>
<li>Additional outdoor WiFi coverage.</li>
</ul>
<p>That is why it helps to plan the switch and PoE capacity at the same time as the building link.</p>
<h2>Fiber or wireless bridge: which should you choose?</h2>
<p>If a trench is already open for utilities or new construction, fiber is often an easy long-term choice. If the buildings have clear line of sight and digging would be difficult, a wireless bridge can deliver strong performance without disturbing the property. Ethernet can make sense for shorter, protected runs where the electrical considerations are acceptable.</p>
<p>Our <a href="/news/fiber-vs-wireless-bridge-outbuildings">fiber versus wireless bridge guide</a> compares those choices in more detail.</p>
<h2>Connecting Northern Colorado properties</h2>
<p>Berthoud WiFi works with homes, acreage, shops, barns, detached garages, offices, and other multi-building properties. We can design the <a href="/solutions/barn-shop-wifi">barn or shop WiFi</a>, <a href="/services/building-to-building-connectivity">building-to-building connection</a>, switching, and access points as one system rather than treating each problem separately.</p>
<p>If you are trying to extend a network beyond the main building, tell us the approximate distance, whether the buildings have line of sight, and what needs to work at the remote location. That is enough to start narrowing down the right approach.</p>
''',
    },
]

PRIORITY_META = {
    "comparisons/unifi-vs-orbi.html": (
        "UniFi vs Orbi for Large Homes: Which WiFi System Is Better? | Berthoud WiFi",
        "Compare UniFi and Netgear Orbi for large homes, wired backhaul, roaming, management, expansion, and professional WiFi installation.",
    ),
    "comparisons/unifi-protect-vs-arlo.html": (
        "UniFi Protect vs Arlo: Local Recording, Cameras & Costs Compared | Berthoud WiFi",
        "Compare UniFi Protect and Arlo cameras for local recording, subscriptions, PoE, video retention, remote access, and whole-property security.",
    ),
    "cities/berthoud.html": (
        "UniFi & WiFi Installation in Berthoud, CO | Berthoud WiFi",
        "Local UniFi installation, home WiFi, business networks, cameras, fiber, and property connectivity in Berthoud, Colorado.",
    ),
    "cities/loveland.html": (
        "Business WiFi & UniFi Installation in Loveland, CO | Berthoud WiFi",
        "Professional business WiFi, office network installation, UniFi systems, cameras, cabling, and home WiFi service in Loveland, Colorado.",
    ),
    "cities/fort-collins.html": (
        "UniFi & Business WiFi Installation in Fort Collins, CO | Berthoud WiFi",
        "Professional UniFi installation, business WiFi, home networking, cameras, and structured cabling in Fort Collins, Colorado.",
    ),
}


def clean_route(route: str) -> str:
    if not route:
        return route
    if route == "/index.html":
        return "/"
    route = re.sub(r"/index\.html$", "/", route)
    route = re.sub(r"\.html$", "", route)
    return route or "/"


def clean_url(value: str) -> str:
    if not value or value.startswith(("mailto:", "tel:", "javascript:", "data:")):
        return value
    if value.startswith("#"):
        return value
    if value.startswith("/"):
        parts = urlsplit(value)
        return urlunsplit(("", "", clean_route(parts.path), parts.query, parts.fragment))
    if value.startswith(("http://", "https://")):
        parts = urlsplit(value)
        if parts.netloc.lower() in {"berthoudwifi.com", "www.berthoudwifi.com"}:
            return urlunsplit(("https", "berthoudwifi.com", clean_route(parts.path), parts.query, parts.fragment))
    return value


def route_for_file(path: Path) -> str:
    rel = path.relative_to(ROOT).as_posix()
    if rel == "index.html":
        return "/"
    if rel.endswith("/index.html"):
        return "/" + rel[: -len("index.html")]
    return "/" + rel[:-5] if rel.endswith(".html") else "/" + rel


def set_meta(soup: BeautifulSoup, title: str, description: str) -> None:
    if soup.title:
        soup.title.string = title
    else:
        tag = soup.new_tag("title")
        tag.string = title
        soup.head.append(tag)
    desc = soup.head.find("meta", attrs={"name": "description"})
    if desc is None:
        desc = soup.new_tag("meta", attrs={"name": "description"})
        soup.head.append(desc)
    desc["content"] = description
    for prop in ("og:title",):
        tag = soup.head.find("meta", attrs={"property": prop})
        if tag:
            tag["content"] = title
    for prop in ("og:description",):
        tag = soup.head.find("meta", attrs={"property": prop})
        if tag:
            tag["content"] = description
    for name in ("twitter:title",):
        tag = soup.head.find("meta", attrs={"name": name})
        if tag:
            tag["content"] = title
    for name in ("twitter:description",):
        tag = soup.head.find("meta", attrs={"name": name})
        if tag:
            tag["content"] = description


def clean_jsonld(value):
    if isinstance(value, dict):
        return {k: clean_jsonld(v) for k, v in value.items()}
    if isinstance(value, list):
        return [clean_jsonld(v) for v in value]
    if isinstance(value, str):
        return clean_url(value)
    return value


def normalize_html(path: Path) -> None:
    soup = BeautifulSoup(path.read_text(encoding="utf-8"), "lxml")
    if not soup.head:
        return

    rel = path.relative_to(ROOT).as_posix()
    if rel in PRIORITY_META:
        set_meta(soup, *PRIORITY_META[rel])

    canonical_url = SITE_URL + route_for_file(path)
    canonical = soup.head.find("link", rel="canonical")
    if canonical is None:
        canonical = soup.new_tag("link", rel="canonical")
        soup.head.append(canonical)
    canonical["href"] = canonical_url

    og_url = soup.head.find("meta", attrs={"property": "og:url"})
    if og_url:
        og_url["content"] = canonical_url

    for tag in soup.find_all(href=True):
        tag["href"] = clean_url(tag["href"])

    for script in soup.find_all("script", type="application/ld+json"):
        try:
            data = json.loads(script.string or script.get_text())
        except Exception:
            continue
        script.string = json.dumps(clean_jsonld(data), separators=(",", ":"), ensure_ascii=False)

    path.write_text("<!doctype html>\n" + str(soup.html), encoding="utf-8")


def article_schema(post: dict) -> dict:
    url = f"{SITE_URL}/news/{post['slug']}"
    image = post["image"] if post["image"].startswith("http") else SITE_URL + post["image"]
    return {
        "@context": "https://schema.org",
        "@type": "Article",
        "headline": post["title"],
        "description": post["description"],
        "datePublished": post["date"],
        "dateModified": post["date"],
        "author": {"@type": "Person", "name": "Steve Smith"},
        "publisher": {"@id": f"{SITE_URL}/#business"},
        "mainEntityOfPage": url,
        "image": image,
    }


def render_article(post: dict) -> Path:
    template_path = ROOT / "news" / "why-wifi-extenders-fail-large-properties.html"
    soup = BeautifulSoup(template_path.read_text(encoding="utf-8"), "lxml")
    set_meta(soup, post["title"] + " | Berthoud WiFi", post["description"])

    main = soup.find("main")
    if main is None:
        raise RuntimeError("News article template is missing <main>.")
    main.clear()
    main.append(BeautifulSoup(
        f'''<section class="page-hero"><div class="container post-body">
<div class="breadcrumb"><a href="/">Home</a> / <a href="/news/">The Connected Front Range</a></div>
<span class="eyebrow">{post['category']}</span><h1>{post['title']}</h1>
<p class="lead">{post['description']}</p><p class="post-meta">{datetime.strptime(post['date'], '%Y-%m-%d').strftime('%B %-d, %Y')} · Steve Smith</p>
</div></section>''', "html.parser"))
    body = BeautifulSoup(
        f'''<section class="section"><div class="container post-body">
<img class="article-hero-image" src="{post['image']}" alt="{post['image_alt']}" decoding="async" loading="eager" fetchpriority="high"/>
{post['body']}
<div class="content-cta"><div><h2>Need help with your network?</h2><p>Tell us about the property, the problem areas, and what you need the network to support.</p></div><a class="btn btn-primary" href="/contact">Get a quote</a></div>
</div></section>''', "html.parser")
    main.append(body)

    for script in list(soup.find_all("script", type="application/ld+json")):
        text = script.string or script.get_text()
        if '"Article"' in text:
            script.decompose()
    schema = soup.new_tag("script", type="application/ld+json")
    schema.string = json.dumps(article_schema(post), separators=(",", ":"), ensure_ascii=False)
    soup.head.append(schema)

    out = ROOT / "news" / f"{post['slug']}.html"
    out.write_text("<!doctype html>\n" + str(soup.html), encoding="utf-8")
    return out


def update_news_index(published: list[dict]) -> None:
    path = ROOT / "news" / "index.html"
    soup = BeautifulSoup(path.read_text(encoding="utf-8"), "lxml")
    listing = soup.select_one(".editorial-list")
    if listing is None:
        return

    for old in list(listing.select("[data-seo-post]")):
        old.decompose()

    for post in reversed(published):
        card = BeautifulSoup(
            f'''<article class="editorial-card" data-seo-post="{post['slug']}">
<img src="{post['image']}" alt="{post['image_alt']}" decoding="async" loading="lazy"/>
<div class="editorial-card-content"><p class="post-meta">{post['category']}</p>
<h3>{post['title']}</h3><p>{post['description']}</p>
<a class="link-arrow" href="/news/{post['slug']}">Read article →</a></div></article>''',
            "html.parser",
        )
        listing.insert(0, card)

    path.write_text("<!doctype html>\n" + str(soup.html), encoding="utf-8")


def update_sitemap(published: list[dict]) -> None:
    post_dates = {f"news/{p['slug']}.html": p["date"] for p in published}
    urls = []
    for path in ROOT.rglob("*.html"):
        rel = path.relative_to(ROOT).as_posix()
        if any(part in {"dist", "node_modules"} or part.startswith(".") for part in path.relative_to(ROOT).parts):
            continue
        route = route_for_file(path)
        lastmod = post_dates.get(rel, BASELINE_LASTMOD)
        urls.append((route, lastmod))

    unique = {}
    for route, lastmod in urls:
        unique[route] = max(lastmod, unique.get(route, "0000-00-00"))

    lines = ['<?xml version="1.0" encoding="UTF-8"?>', '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
    for route in sorted(unique, key=lambda x: (x != "/", x)):
        lines.append(f"  <url><loc>{SITE_URL}{route}</loc><lastmod>{unique[route]}</lastmod></url>")
    lines.append("</urlset>")
    (ROOT / "sitemap.xml").write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    published = [post for post in POSTS if post["date"] <= TODAY]
    print(f"SEO growth run for {TODAY}: {len(published)} scheduled posts are live.")

    for post in published:
        render_article(post)
    update_news_index(published)

    for path in ROOT.rglob("*.html"):
        if any(part in {"dist", "node_modules"} or part.startswith(".") for part in path.relative_to(ROOT).parts):
            continue
        normalize_html(path)

    update_sitemap(published)


if __name__ == "__main__":
    main()
