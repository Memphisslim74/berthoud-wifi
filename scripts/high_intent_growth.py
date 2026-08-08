#!/usr/bin/env python3
"""Generate Berthoud WiFi's high-intent service and builder landing pages."""

from __future__ import annotations

import json
from pathlib import Path

from bs4 import BeautifulSoup

ROOT = Path(__file__).resolve().parents[1]
SITE_URL = "https://berthoudwifi.com"

BUSINESS = {
    "@type": "LocalBusiness",
    "name": "Berthoud WiFi",
    "url": f"{SITE_URL}/",
    "@id": f"{SITE_URL}/#business",
    "telephone": "+17202093130",
    "email": "hello@berthoudwifi.com",
    "logo": f"{SITE_URL}/assets/images/berthoud-wifi-logo-flat.png",
    "image": f"{SITE_URL}/assets/images/berthoud-wifi-social-card.png",
    "sameAs": [
        "https://www.facebook.com/profile.php?id=61591527285692",
        "https://www.linkedin.com/company/berthoud-wifi/",
    ],
}

AREA = [
    "Berthoud", "Loveland", "Fort Collins", "Longmont", "Erie", "Boulder",
    "Windsor", "Johnstown", "Timnath", "Mead", "Frederick", "Firestone",
    "Wellington", "Greeley",
]


PAGES = [
    {
        "path": "services/home-ethernet-installation.html",
        "title": "Home Ethernet Installation in Northern Colorado | Berthoud WiFi",
        "description": "Professional Cat6 Ethernet installation, wall jacks, access-point wiring, home-office cabling, testing, and clean retrofits across Northern Colorado.",
        "eyebrow": "Residential Network Cabling",
        "h1": "Home Ethernet Installation in Northern Colorado",
        "lead": "Clean Cat6 and Cat6A wiring for finished homes, remodels, home offices, access points, cameras, TVs, and new construction.",
        "image": "/assets/images/actual/fiber-ethernet.webp",
        "image_alt": "Professional home Ethernet cabling and structured network installation",
        "intro": "Hardwired Ethernet gives access points, offices, cameras, televisions, and other fixed devices a dependable connection without using limited wireless airtime.",
        "facts": [
            ("Common cable", "Cat6 or Cat6A selected for the pathway, distance, and long-term plan."),
            ("Finished homes", "Routes are planned around accessible attics, basements, crawlspaces, and existing pathways."),
            ("New construction", "Drops, conduit, access points, cameras, and the central rack are planned before drywall."),
            ("Handoff", "Runs are terminated, tested, labeled, and documented."),
        ],
        "sections": [
            ("Ethernet for existing homes", "A finished-home retrofit starts with the least disruptive practical route. We review attic, basement, crawlspace, closet, exterior, and existing low-voltage pathways before recommending cable locations. The goal is a clean installation with minimal drywall impact—not exposed cable stapled through living spaces."),
            ("Cat6 wiring for home offices and entertainment", "Hardwired wall jacks can stabilize video calls, large uploads, gaming, streaming, media equipment, printers, and desktop computers. Ethernet also reduces the number of fixed devices competing for WiFi airtime."),
            ("Wired backhaul for whole-home WiFi", "Professional access points work best with a reliable wired connection. We can install ceiling or wall locations based on coverage, terminate the cabling at a patch panel or switch, and coordinate the Ethernet work with a whole-home UniFi design."),
            ("PoE cabling for cameras, doorbells, and smart-home devices", "A single Ethernet run can carry both data and power to supported access points, cameras, intercoms, and other PoE equipment. Planning those runs together creates a cleaner system and makes future expansion easier."),
            ("New builds, additions, and remodels", "Open walls are the best opportunity to install structured cabling, spare pathways, fiber, and conduit. We work from plans, coordinate with builders and electricians, label each run, and keep the central network location serviceable."),
            ("Testing, labeling, and network-rack cleanup", "Every completed run is terminated and tested. Patch panels, labels, cable management, switching, and UPS protection can be included so the finished system is understandable and supportable."),
        ],
        "faqs": [
            ("Can you install Ethernet in an existing finished home?", "Yes. Feasibility depends on access, wall construction, floor plan, and the route between rooms and the network location. We review the property before recommending the cleanest practical path."),
            ("Should I use Cat6 or Cat6A?", "Cat6 is an excellent fit for many homes. Cat6A may make sense for specific higher-speed, longer-term, or interference-sensitive plans, but it is thicker and needs more pathway space."),
            ("Can you add Ethernet wall jacks for a home office?", "Yes. Home offices, televisions, gaming systems, access points, cameras, and other fixed devices are common retrofit projects."),
            ("Do you test and label the cable runs?", "Yes. Completed runs are terminated, tested, labeled, and tied back to an organized network location."),
            ("Can Ethernet improve my WiFi?", "Yes. Wired backhaul lets access points use their radios for client devices instead of repeating traffic wirelessly."),
        ],
        "related": [
            ("Whole-home WiFi installation", "/services/home-network-improvements"),
            ("Fiber and structured cabling", "/services/fiber-structured-cabling"),
            ("New-construction pre-wire", "/builders/custom-home-low-voltage-prewire"),
            ("Security camera installation", "/services/security-cameras"),
        ],
        "cta_title": "Get a home Ethernet installation quote",
        "cta_copy": "Tell us which rooms or devices need wired connections, where the internet equipment is located, and whether the home has attic, basement, or crawlspace access.",
    },
    {
        "path": "builders/custom-home-low-voltage-prewire.html",
        "title": "Custom Home Low-Voltage Pre-Wire | Northern Colorado",
        "description": "Network, WiFi, security camera, fiber, and low-voltage pre-wiring for Northern Colorado custom homes, builders, architects, and luxury residential projects.",
        "eyebrow": "For Custom Builders & Homeowners",
        "h1": "Network, WiFi and Security Pre-Wiring for Custom Homes",
        "lead": "A design-first low-voltage partner for custom builders who want reliable technology infrastructure planned before insulation and drywall.",
        "image": "/assets/images/projects/new-construction-ap.webp",
        "image_alt": "Wireless access point location prepared during custom-home construction",
        "intro": "The best time to solve home networking, camera coverage, and future technology needs is while the walls are open. Berthoud WiFi coordinates the plan, rough-in, trim-out, testing, and final network handoff.",
        "facts": [
            ("Experience", "Owners with a combined 30+ years in networking and infrastructure."),
            ("Project scale", "Technology and infrastructure programs up to $2 million."),
            ("Coordination", "Plan review, site walks, rough-in, trim-out, labeling, testing, and documentation."),
            ("One partner", "Ethernet, WiFi, cameras, fiber, racks, exterior coverage, gates, and outbuildings."),
        ],
        "sections": [
            ("Plan review before the rough-in", "We review floor plans, elevations, room use, internet entry, mechanical spaces, outdoor living areas, gates, detached structures, and the technology systems expected at turnover. That produces a coordinated low-voltage plan instead of a last-minute list of wall jacks."),
            ("WiFi access-point placement based on coverage", "Access points are located for the finished home—not simply centered in a hallway because the ceiling is open. The plan considers floor layout, ceiling height, building materials, outdoor areas, equipment density, and wired backhaul."),
            ("Structured cabling, fiber, and conduit", "Cat6 or Cat6A runs support offices, televisions, access points, cameras, doorbells, intercoms, and other fixed devices. Fiber and conduit can preserve options for long pathways, detached buildings, gates, service changes, and technology that does not exist yet."),
            ("Security-camera and entry pre-wire", "Camera views are planned around entrances, driveways, garages, yards, gates, equipment areas, and identification distance. Cable locations account for soffits, stone, lighting, landscaping, and how each camera will actually be serviced."),
            ("Central rack and equipment-room design", "A maintainable home network needs adequate wall space, ventilation, power, UPS protection, patch panels, switching, internet equipment, storage, and a clear labeling standard. We help keep that infrastructure out of cramped cabinets and unsuitable utility corners."),
            ("Rough-in, trim-out, testing, and documentation", "We coordinate around the construction schedule, protect and label cabling, return for termination and equipment installation, test the completed runs, and provide a clean handoff. Builders receive a technology partner who can answer field questions before they become change orders."),
            ("Built for high-expectation homes", "Our background includes homes, businesses, film studios, large facilities, exterior networks, camera systems, and multi-building properties. That experience translates into residential infrastructure designed to be stable, serviceable, and ready for what the owner expects on move-in day."),
        ],
        "faqs": [
            ("When should a builder involve Berthoud WiFi?", "Ideally during design development or before electrical and low-voltage rough-in. Earlier involvement creates more options and reduces late changes."),
            ("Do you work from architectural plans?", "Yes. We can review plans, create a technology scope, participate in a site walk, and coordinate locations with the builder, electrician, and other trades."),
            ("Can you handle both rough-in and final network installation?", "Yes. The project can include planning, cabling, trim-out, rack work, WiFi, cameras, configuration, testing, documentation, and owner orientation."),
            ("Do you only install UniFi?", "UniFi is our preferred platform for many integrated network and camera projects, but cabling and pathway recommendations are based on the home and long-term requirements."),
            ("Can plans be sent with the inquiry?", "Submit the builder form below with a secure plan link, or reply to the branded confirmation email with the plan set and project documents."),
        ],
        "related": [
            ("Home Ethernet installation", "/services/home-ethernet-installation"),
            ("New-construction networking guide", "/solutions/new-construction-networking"),
            ("Security camera installation", "/services/security-cameras"),
            ("Fiber and structured cabling", "/services/fiber-structured-cabling"),
        ],
        "cta_title": "Send us your plans",
        "cta_copy": "Share the project location, square footage, current phase, target drywall date, and a secure link to the plan set. You can also reply to the confirmation email with attachments.",
    },
    {
        "path": "services/outdoor-wifi.html",
        "title": "Outdoor WiFi Installation in Northern Colorado | Berthoud WiFi",
        "description": "Professional outdoor WiFi for patios, pools, acreage, barns, detached garages, venues, shops, and multi-building Northern Colorado properties.",
        "eyebrow": "Property-Wide Connectivity",
        "h1": "Outdoor WiFi Installation in Northern Colorado",
        "lead": "Reliable coverage for patios, pools, yards, acreage, work areas, venues, barns, shops, and detached buildings.",
        "image": "/assets/images/projects/outdoor-bridge-install.webp",
        "image_alt": "Berthoud WiFi installing outdoor connectivity equipment",
        "intro": "Outdoor coverage needs weather-rated equipment, reliable backhaul, appropriate mounting, and testing from the places where people and devices actually connect.",
        "facts": [
            ("Home projects", "Patios, pools, yards, fire pits, gates, driveways, and outdoor offices."),
            ("Rural projects", "Acreage, barns, shops, arenas, detached garages, and equipment areas."),
            ("Business projects", "Restaurant patios, venues, commercial yards, parking, and exterior work areas."),
            ("Backhaul", "Ethernet, fiber, or a dedicated point-to-point wireless bridge."),
        ],
        "sections": [
            ("Outdoor WiFi for patios, pools, and larger homes", "An indoor router often loses much of its signal through exterior walls, low-emissivity glass, stone, metal, and distance. Outdoor-rated access points can be mounted for the living area while preserving clean roaming back into the home network."),
            ("WiFi for acreage, barns, shops, and detached garages", "A remote building needs a dependable link back to the main network before local WiFi is added. We compare fiber, protected Ethernet, and point-to-point bridges, then install access points where the remote space actually needs coverage."),
            ("Point-to-point wireless bridge installation", "A bridge is a focused building-to-building connection, not a consumer extender. Proper line of sight, mounting, alignment, power, surge considerations, and capacity planning make the difference between a temporary signal and a reliable link."),
            ("Outdoor WiFi for restaurants, venues, and work areas", "Commercial outdoor coverage may support guests, staff, point-of-sale devices, cameras, scanners, tablets, and events. Network separation, client capacity, placement, and operational support are included in the design."),
            ("Weather, mounting, and cable protection", "Outdoor equipment is selected and installed around exposure, temperature, water paths, sunlight, wind, lightning risk, service access, and the structure available for mounting."),
            ("Real-world coverage testing", "We test from representative seating, work, gate, parking, and property locations. Radio settings are adjusted for stable roaming and useful coverage rather than judged only from directly below the access point."),
        ],
        "faqs": [
            ("Can you extend WiFi to a detached garage or barn?", "Yes. The project may use fiber, Ethernet, or a dedicated wireless bridge for the building link, plus an access point inside or outside the remote structure."),
            ("Can outdoor WiFi cover a pool or large backyard?", "Yes. Coverage depends on size, terrain, construction, foliage, mounting options, and where devices are used."),
            ("Is an outdoor access point different from a WiFi extender?", "Yes. A weather-rated access point with dependable backhaul provides a planned part of the network instead of repeating a weak indoor signal."),
            ("Can cameras use the same outdoor network?", "Yes, when bandwidth, PoE switching, storage, and network separation are included in the design."),
        ],
        "related": [
            ("Building-to-building connectivity", "/services/building-to-building-connectivity"),
            ("Barn and shop WiFi", "/solutions/barn-shop-wifi"),
            ("Security camera installation", "/services/security-cameras"),
            ("Fiber and structured cabling", "/services/fiber-structured-cabling"),
        ],
        "cta_title": "Plan outdoor coverage for your property",
        "cta_copy": "Tell us which outdoor areas or buildings need service, the approximate distances, and what devices must connect.",
    },
    {
        "path": "services/security-cameras.html",
        "title": "Security Camera Installation in Northern Colorado | Berthoud WiFi",
        "description": "Professional wired PoE security camera installation for homes, businesses, driveways, gates, barns, shops, and Northern Colorado properties.",
        "eyebrow": "Wired PoE Camera Systems",
        "h1": "Home and Business Security Camera Installation",
        "lead": "Professional camera planning, PoE cabling, local recording, mounting, remote viewing, and coverage for the areas that matter.",
        "image": "/assets/images/projects/completed-outdoor-device.webp",
        "image_alt": "Completed outdoor security and network device installation",
        "intro": "A useful camera system begins with the event you need to capture. Entrances, driveways, gates, parking, work areas, barns, and yards require different views, lenses, mounting, and lighting decisions.",
        "facts": [
            ("Residential", "Entrances, doorbells, driveways, garages, yards, gates, barns, and acreage."),
            ("Commercial", "Offices, shops, parking, inventory, cash areas, entrances, and exterior operations."),
            ("Infrastructure", "PoE cabling, switching, local recorders, UPS protection, storage, and remote access."),
            ("Platform", "UniFi Protect systems without the typical consumer-camera monthly cloud subscription."),
        ],
        "sections": [
            ("Home security camera installation", "Residential projects can cover doors, packages, vehicles, driveways, yards, garages, gates, barns, and detached buildings. Camera positions are chosen for usable identification and context—not simply the widest possible view."),
            ("Wired PoE cameras and clean cabling", "PoE cameras receive power and data over structured Ethernet. We plan cable routes, mounting, drip loops, penetrations, switching capacity, surge considerations, and service access for a cleaner and more dependable installation than battery-only cameras."),
            ("Local recording without typical monthly cloud fees", "UniFi Protect stores footage on a local recorder you control while still supporting secure remote viewing. Storage is sized around camera count, resolution, frame rate, detection settings, and the number of retention days required."),
            ("Driveway, gate, barn, and acreage cameras", "Long approaches and rural properties often need more than a camera mounted on the house. We can combine fiber, wireless bridges, remote PoE switches, exterior WiFi, and carefully selected cameras to cover gates, shops, barns, equipment, and separate structures."),
            ("Business security camera installation", "Commercial designs consider entrances, parking, public areas, work zones, inventory, employee safety, cash handling, and who needs access to footage. Camera traffic, recorders, switching, VLANs, and UPS protection are planned with the rest of the network."),
            ("Remote viewing, alerts, and handoff", "The finished system is configured for appropriate users, detections, notification zones, remote viewing, and retention. We walk through normal use so finding an event does not require learning the system during an incident."),
        ],
        "faqs": [
            ("Do you install home security cameras?", "Yes. We install wired camera systems for homes, driveways, garages, yards, gates, barns, and larger properties."),
            ("Can I use cameras without a monthly fee?", "UniFi Protect records locally and does not require the typical per-camera cloud-storage subscription. Internet access is still useful for remote viewing and alerts."),
            ("Can you install cameras on a detached shop or gate?", "Yes. Remote areas may need fiber, a wireless bridge, a PoE switch, power coordination, or a camera selected for the distance and lighting."),
            ("How much footage can the system keep?", "Retention depends on camera count, resolution, frame rate, detections, and storage capacity. We size the recorder around the desired retention window and future expansion."),
            ("Do you install Ring, Arlo, or other battery cameras?", "Our primary focus is professionally wired PoE systems and UniFi Protect. We can explain when that approach is a better fit than consumer battery cameras."),
        ],
        "related": [
            ("UniFi Protect camera systems", "/services/unifi-protect-security"),
            ("Home Ethernet installation", "/services/home-ethernet-installation"),
            ("Outdoor WiFi installation", "/services/outdoor-wifi"),
            ("Custom-home pre-wire", "/builders/custom-home-low-voltage-prewire"),
        ],
        "cta_title": "Get a security camera installation quote",
        "cta_copy": "Tell us which entrances, vehicles, buildings, gates, or work areas need coverage and whether any cabling or cameras already exist.",
    },
]


def set_meta(soup: BeautifulSoup, page: dict) -> None:
    soup.title.string = page["title"]
    for selector, value in [
        ('meta[name="description"]', page["description"]),
        ('meta[property="og:title"]', page["title"]),
        ('meta[property="og:description"]', page["description"]),
        ('meta[name="twitter:title"]', page["title"]),
        ('meta[name="twitter:description"]', page["description"]),
    ]:
        tag = soup.select_one(selector)
        if tag:
            tag["content"] = value


def service_schema(page: dict) -> list[dict]:
    return [
        {
            "@context": "https://schema.org",
            "@type": "Service",
            "name": page["h1"],
            "url": f"{SITE_URL}/{page['path'][:-5]}",
            "description": page["description"],
            "provider": BUSINESS,
            "areaServed": AREA,
        },
        {
            "@context": "https://schema.org",
            "@type": "FAQPage",
            "mainEntity": [
                {
                    "@type": "Question",
                    "name": question,
                    "acceptedAnswer": {"@type": "Answer", "text": answer},
                }
                for question, answer in page["faqs"]
            ],
        },
    ]


def render_page(page: dict) -> None:
    template = ROOT / "solutions" / "barn-shop-wifi.html"
    soup = BeautifulSoup(template.read_text(encoding="utf-8"), "lxml")
    set_meta(soup, page)

    route = "/" + page["path"][:-5]
    canonical = soup.select_one('link[rel="canonical"]')
    canonical["href"] = SITE_URL + route
    og_url = soup.select_one('meta[property="og:url"]')
    if og_url:
        og_url["content"] = SITE_URL + route

    for old in soup.find_all("script", type="application/ld+json"):
        old.decompose()
    schema = soup.new_tag("script", type="application/ld+json")
    schema.string = json.dumps(service_schema(page), separators=(",", ":"))
    soup.head.append(schema)

    section_html = "".join(
        f'<section id="section-{index}"><h2>{title}</h2><p>{copy}</p></section>'
        for index, (title, copy) in enumerate(page["sections"], start=1)
    )
    facts_html = "".join(
        f'<div class="fact"><strong>{title}</strong><span>{copy}</span></div>'
        for title, copy in page["facts"]
    )
    faq_html = "".join(
        f'<details><summary>{question}</summary><p>{answer}</p></details>'
        for question, answer in page["faqs"]
    )
    related_html = "".join(
        f'<a href="{href}">{label}</a>' for label, href in page["related"]
    )
    toc_html = "".join(
        f'<a href="#section-{index}">{title}</a>'
        for index, (title, _) in enumerate(page["sections"], start=1)
    )
    crumb_root = "Builder Services" if page["path"].startswith("builders/") else "Services"
    crumb_link = "/services/"

    main_html = f'''
<section class="authority-hero"><div class="container authority-hero-grid"><div>
<div class="breadcrumb"><a href="/">Home</a> / <a href="{crumb_link}">{crumb_root}</a> / {page['h1']}</div>
<span class="eyebrow">{page['eyebrow']}</span><h1>{page['h1']}</h1><p class="lead">{page['lead']}</p>
<div class="hero-actions"><a class="btn btn-primary" href="#contact">{page['cta_title']}</a><a class="btn btn-secondary" href="tel:+17202093130">Call 720-209-3130</a></div></div>
<img src="{page['image']}" alt="{page['image_alt']}" width="1800" height="1273" loading="eager" fetchpriority="high" decoding="async"/></div></section>
<section class="section"><div class="container authority-shell"><article class="authority-content">
<p class="intro">{page['intro']}</p><div class="fact-grid">{facts_html}</div>{section_html}
<div class="local-copy"><h2>Serving Northern Colorado</h2><p>Based in Berthoud and serving Loveland, Fort Collins, Longmont, Erie, Boulder, Windsor, Timnath, Johnstown, and nearby communities.</p></div>
<h2>Frequently asked questions</h2><div class="faq">{faq_html}</div>
<h2>Related services and planning resources</h2><div class="related-links">{related_html}</div>
<div class="content-cta"><h2>{page['cta_title']}</h2><p>{page['cta_copy']}</p><a class="btn btn-primary" href="#contact">Start your project</a></div>
</article><aside class="toc"><div class="toc-card"><h3>On this page</h3>{toc_html}</div>
<div class="toc-card"><h3>Why Berthoud WiFi</h3><p>Combined 30+ years of networking and infrastructure experience, clean installation, practical design, and local support.</p></div></aside></div></section>
'''
    main = soup.find("main")
    main.clear()
    for node in list(BeautifulSoup(main_html, "html.parser").contents):
        main.append(node)

    out = ROOT / page["path"]
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text("<!doctype html>\n" + str(soup.html), encoding="utf-8")


def add_service_cards() -> None:
    path = ROOT / "services" / "index.html"
    soup = BeautifulSoup(path.read_text(encoding="utf-8"), "lxml")
    grid = soup.select_one(".service-index")
    if not grid:
        return
    cards = [
        ("home-ethernet-installation", "Home Ethernet Installation", "Cat6 and Cat6A wall jacks, access-point backhaul, home offices, cameras, testing, and clean residential retrofits.", "/services/home-ethernet-installation", "/assets/images/actual/fiber-ethernet-480.webp"),
        ("custom-home-prewire", "Custom Home Pre-Wire", "A builder-focused partner for network, WiFi, camera, fiber, conduit, rack, rough-in, trim-out, and final handoff.", "/builders/custom-home-low-voltage-prewire", "/assets/images/projects/new-construction-ap-480.webp"),
    ]
    for key, title, copy, href, image in cards:
        if grid.select_one(f'[data-growth-card="{key}"]'):
            continue
        card = BeautifulSoup(
            f'<article class="card service-feature" data-growth-card="{key}"><img src="{image}" alt="{title}" width="480" height="480" loading="lazy" decoding="async"/><h3>{title}</h3><p>{copy}</p><a class="link-arrow" href="{href}">Explore service →</a></article>',
            "html.parser",
        ).article
        grid.append(card)
    path.write_text("<!doctype html>\n" + str(soup.html), encoding="utf-8")


def strengthen_city_pages() -> None:
    city_copy = {
        "timnath": ("Custom-home networking in Timnath", "Timnath's newer and custom homes are an ideal fit for builder-coordinated low-voltage planning. We can review plans before drywall, locate wired access points, pre-wire cameras and outdoor areas, and design the central rack for a clean move-in handoff."),
        "windsor": ("New-construction and acreage infrastructure in Windsor", "Windsor projects often combine larger homes, outdoor living areas, detached structures, cameras, and home offices. We coordinate Ethernet, WiFi, fiber, camera, gate, and rack planning so those systems work as one property-wide design."),
        "johnstown": ("Pre-wire planning for growing Johnstown", "For new homes, additions, and remodels in Johnstown, we plan Cat6 or Cat6A, ceiling access points, camera views, office connections, exterior coverage, and the network location before insulation and drywall close the pathways."),
    }
    for city, (heading, copy) in city_copy.items():
        path = ROOT / "cities" / f"{city}.html"
        soup = BeautifulSoup(path.read_text(encoding="utf-8"), "lxml")
        article = soup.select_one(".authority-content")
        if not article or article.select_one("[data-builder-city]"):
            continue
        marker = article.find("h2", string=lambda value: value and "Services available" in value)
        section = BeautifulSoup(
            f'<section data-builder-city="{city}"><h2>{heading}</h2><p>{copy}</p><p><a href="/builders/custom-home-low-voltage-prewire">Explore custom-home low-voltage pre-wire services</a> or <a href="/services/home-ethernet-installation">home Ethernet installation</a>.</p></section>',
            "html.parser",
        ).section
        if marker:
            marker.insert_before(section)
        else:
            article.append(section)
        path.write_text("<!doctype html>\n" + str(soup.html), encoding="utf-8")


def main() -> None:
    for page in PAGES:
        render_page(page)
    add_service_cards()
    strengthen_city_pages()
    print(f"Generated {len(PAGES)} high-intent landing pages and local updates.")


if __name__ == "__main__":
    main()
