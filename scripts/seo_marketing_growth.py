#!/usr/bin/env python3
"""Publish the SEO/organic-marketing content cluster and keep site navigation discoverable."""

from __future__ import annotations

import html
import json
from pathlib import Path

from bs4 import BeautifulSoup

ROOT = Path(__file__).resolve().parents[1]
TODAY = "2026-09-08"
SITE = "https://berthoudwifi.com"

ARTICLES = [
    {
        "slug": "local-seo-northern-colorado-small-business",
        "title": "Local SEO for Northern Colorado Small Businesses: What Actually Moves Visibility",
        "description": "A practical local SEO guide for Berthoud, Loveland, Fort Collins, Longmont, Greeley, and Northern Colorado businesses focused on search visibility and qualified leads.",
        "eyebrow": "Local SEO",
        "image": "/assets/images/actual/business-consultation.webp",
        "body": """
<p>Local SEO is not a single setting and it is not just a Google Business Profile. It is the combined signal created by your website, business profile, service pages, reviews, citations, technical health, internal links, and the way your content matches what people in your market are actually searching for.</p>
<p>For a Northern Colorado business, the goal is not to rank for every broad keyword. The goal is to become a strong answer for the searches that are most likely to turn into a call, form submission, appointment, or visit.</p>
<h2>Start with the searches closest to revenue</h2>
<p>A useful local SEO plan begins by separating informational searches from commercial searches. Someone searching for “what is local SEO” is learning. Someone searching for “local SEO services Loveland CO” is much closer to hiring. Both can matter, but the service page should be built around the second type of intent.</p>
<p>We look for the combination of service, location, problem, and buying stage. That usually creates a smaller but much more valuable keyword set than chasing national search volume.</p>
<h2>Make the website explain exactly what you do and where you do it</h2>
<p>Search engines need a clear relationship between the business, the services, and the communities served. That means strong service pages, useful location context, descriptive page titles and headings, crawlable internal links, and content that gives a visitor enough information to decide whether the company is a fit.</p>
<p>Thin city pages that repeat the same paragraph with a different town name are not a strong strategy. A useful location page should contain real local context, the services relevant to that market, common customer problems, proof, FAQs, and links to deeper resources.</p>
<h2>Google Business Profile should match the website</h2>
<p>The profile and website should reinforce each other. Business categories, services, descriptions, landing-page links, hours, photos, reviews, and contact information should be accurate and consistent. The website should then give Google and the customer more detail than the profile can hold.</p>
<h2>Reviews help, but they are not the whole strategy</h2>
<p>Reviews can improve trust and local prominence, but they do not fix a weak website, incorrect categories, indexing problems, or pages that never target the service being searched. A healthy program works on all of those pieces together.</p>
<h2>Measure impressions before you only measure rankings</h2>
<p>Google Search Console is one of the most useful places to see whether the strategy is beginning to work. Growing impressions for the right service queries can show that Google is starting to understand the site before the page reaches a top position. From there, clicks, calls, forms, and qualified leads tell us whether the visibility is useful.</p>
<h2>Local SEO across Northern Colorado</h2>
<p>Berthoud, Loveland, Fort Collins, Longmont, Greeley, Erie, Boulder, and nearby communities have overlapping markets but different local competition. The best structure depends on the business, how far customers realistically travel, and which services are profitable enough to support dedicated pages and content.</p>
<p>If your site already receives impressions but very little traffic, or traffic without leads, the next move is usually an audit of page intent, technical health, local relevance, and conversion paths—not simply publishing more generic articles.</p>
""",
    },
    {
        "slug": "google-business-profile-optimization-northern-colorado",
        "title": "Google Business Profile Optimization: A Practical Checklist for Local Businesses",
        "description": "A practical Google Business Profile optimization checklist covering categories, services, reviews, photos, landing pages, tracking, and local SEO for Northern Colorado businesses.",
        "eyebrow": "Google Business Profile",
        "image": "/assets/images/actual/connected-business.webp",
        "body": """
<p>Your Google Business Profile is often the first version of your business a local customer sees. It can appear before the website, especially for service searches with strong local intent. That makes the profile important, but optimization should be accurate rather than stuffed with keywords.</p>
<h2>Choose the primary category carefully</h2>
<p>The primary category is one of the strongest signals describing what the business is. Pick the category that best represents the primary service, then add relevant secondary categories only when they describe real services the business provides.</p>
<h2>Complete the services and business information</h2>
<p>Hours, phone number, website, service area, business description, services, appointment links, and other available fields should be kept current. Inconsistency between the profile and website creates confusion for both people and search systems.</p>
<h2>Link to the best landing page</h2>
<p>The website link should send a visitor to the page that best answers the search. For many businesses that is the homepage. For specific profile features or campaigns, a focused service page can be more useful. The destination should be fast, mobile-friendly, and immediately explain the service and next step.</p>
<h2>Use real photos</h2>
<p>Current photos of the team, work, building, equipment, projects, or customer environment provide proof that generic stock photography cannot. They also help customers understand what to expect before they call.</p>
<h2>Build a repeatable review process</h2>
<p>Ask real customers for honest reviews after successful work. Do not offer incentives for positive reviews or manufacture review patterns. A steady, legitimate review process is more useful than a sudden spike that does not reflect normal customer activity.</p>
<h2>Respond to reviews like a business owner</h2>
<p>Responses should be short, useful, and human. Thank the customer, acknowledge the specific work when appropriate, and handle complaints professionally. The goal is not to write SEO copy inside every response.</p>
<h2>Track what the profile is producing</h2>
<p>Profile performance should be reviewed alongside Search Console and Analytics. Calls, website visits, direction requests, messages, and search visibility help show which services and locations are creating real demand.</p>
<h2>Keep the profile connected to the larger SEO plan</h2>
<p>A strong profile cannot fully compensate for a weak website. The best results usually come when the business profile, service pages, local content, reviews, technical SEO, and conversion tracking all support the same services and markets.</p>
""",
    },
    {
        "slug": "technical-seo-audit-small-business",
        "title": "Technical SEO Audit for a Small Business Website: What We Check First",
        "description": "A practical technical SEO audit checklist for small business websites covering indexing, canonicals, sitemaps, page speed, mobile usability, internal links, schema, and tracking.",
        "eyebrow": "Technical SEO",
        "image": "/assets/images/actual/fiber-rack.webp",
        "body": """
<p>Before adding more content, a small business website should be able to be crawled, indexed, understood, and used easily on a phone. A technical SEO audit is the process of finding the issues that prevent that from happening.</p>
<h2>Can search engines crawl the important pages?</h2>
<p>We start with robots directives, HTTP status codes, redirects, navigation, JavaScript dependencies, and internal links. Important service pages should not depend on obscure paths that neither users nor crawlers can easily reach.</p>
<h2>Are the right pages indexed?</h2>
<p>Search Console indexing reports, site searches, XML sitemaps, canonical tags, and page-level directives help show whether Google is indexing the pages you want and ignoring duplicates or low-value URLs.</p>
<h2>Do canonicals and redirects agree?</h2>
<p>A site can accidentally send conflicting signals when the canonical points to one URL while internal links and redirects point somewhere else. We normalize the preferred URL structure and remove unnecessary chains where practical.</p>
<h2>Is the site fast enough on mobile?</h2>
<p>Page speed is not the only ranking factor, but slow pages lose users and make every acquisition channel work harder. We look at image weight, render-blocking resources, third-party scripts, layout shift, caching, and the elements that affect Core Web Vitals.</p>
<h2>Can every page explain its purpose?</h2>
<p>Titles, headings, body copy, structured data, image alt text, and internal links should make the page topic obvious. A technically perfect page that never clearly describes the service still has a relevance problem.</p>
<h2>Are internal links helping important pages?</h2>
<p>Internal links show relationships between services, locations, guides, comparisons, and articles. They also help visitors move from an informational article into a commercial service page when they are ready.</p>
<h2>Is structured data accurate?</h2>
<p>Schema markup can clarify business information, services, articles, FAQs, and site structure. It should match visible content and should never claim awards, reviews, locations, or business details that are not true.</p>
<h2>Is measurement installed correctly?</h2>
<p>An SEO program needs enough measurement to distinguish visibility from business outcomes. Search Console, Analytics, form events, phone clicks, and other conversion events should be checked before judging whether the work is generating value.</p>
<p>A good technical audit ends with a prioritized list. Critical crawl and indexing issues come before cosmetic improvements, and high-intent pages usually come before low-value pages with little search opportunity.</p>
""",
    },
    {
        "slug": "organic-content-strategy-local-business",
        "title": "Organic Content Strategy for Local Businesses: Build Content That Can Produce Leads",
        "description": "How local businesses can build an organic content strategy around service intent, buyer questions, local searches, comparisons, internal links, and measurable lead generation.",
        "eyebrow": "Organic Content Strategy",
        "image": "/assets/images/actual/home-laptop.webp",
        "body": """
<p>Publishing a blog every week does not automatically create organic growth. A useful content strategy starts with the questions, comparisons, problems, and searches that happen before a customer contacts the business.</p>
<h2>Build the commercial pages first</h2>
<p>The core service pages should be strong before the blog becomes the priority. Those pages explain what you sell, who it is for, where you provide it, and what a customer should do next. Supporting content should strengthen those pages rather than compete with them.</p>
<h2>Use articles to answer the questions around the purchase</h2>
<p>Good supporting topics include cost, timelines, comparisons, mistakes, preparation, maintenance, equipment choices, local considerations, and signs that a customer needs the service. These searches often happen while someone is evaluating options.</p>
<h2>Choose topics from evidence, not a generic content calendar</h2>
<p>Search Console queries, customer emails, sales questions, competitor gaps, Google Business Profile activity, internal site search, and actual conversations can reveal stronger topics than a list of generic “SEO blog ideas.”</p>
<h2>Connect every article to a next step</h2>
<p>An article should link naturally to the relevant service page, location page, guide, or contact path. Internal linking is useful for search engines, but it is just as important for the person who has finished reading and wants to understand what to do next.</p>
<h2>Do not create dozens of thin location pages</h2>
<p>Local content should earn its existence. A city page is useful when the business genuinely serves that market and can provide unique local context. Repeating the same article or page with different city names creates a poor experience and usually adds little value.</p>
<h2>Refresh content when the market changes</h2>
<p>Pricing, technology, regulations, product capabilities, and search behavior change. Strong articles should be reviewed and updated when the underlying information changes rather than treated as one-time publishing tasks.</p>
<h2>Measure the content by more than traffic</h2>
<p>Traffic is useful, but impressions, qualified clicks, assisted conversions, form submissions, phone calls, and the search terms bringing visitors to the page are more actionable. Some of the best local content may never produce huge traffic because the audience is intentionally narrow.</p>
<p>The purpose of organic content is to build useful search visibility over time. That means fewer filler posts, stronger service pages, better internal linking, and content that helps a real buyer make a decision.</p>
""",
    },
]


def nav_html() -> str:
    return """<header class=\"site-header\"><div class=\"container nav\"><a class=\"brand\" href=\"/\"><img alt=\"Berthoud WiFi\" height=\"160\" width=\"160\" src=\"/assets/images/berthoud-wifi-logo-160.webp?v=23\"/><span>Berthoud WiFi</span></a><button aria-expanded=\"false\" aria-label=\"Open navigation\" class=\"menu-btn\">Menu</button><nav aria-label=\"Primary\" class=\"nav-links\"><a href=\"/\">Home</a><a href=\"/services/\">Services</a><div class=\"nav-item\"><button aria-expanded=\"false\" class=\"nav-dropdown-toggle\" type=\"button\">Solutions</button><div class=\"nav-dropdown\"><a href=\"/services/home-network-improvements\">Home WiFi</a><a href=\"/services/home-ethernet-installation\">Home Ethernet</a><a href=\"/services/small-business-infrastructure\">Business WiFi</a><a href=\"/services/unifi-protect-security\">Cameras</a><a href=\"/services/unifi-access-entry\">Door Access</a><a href=\"/services/fiber-structured-cabling\">Fiber &amp; Cabling</a><a href=\"/builders/custom-home-low-voltage-prewire\">Custom Home Pre-Wire</a><a href=\"/cybersecurity-consulting/\">Cybersecurity Consulting</a><a href=\"/seo-services/\">SEO &amp; Organic Marketing</a><a href=\"/solutions/\">View all solutions</a></div></div><a href=\"/news/\">Articles</a><a href=\"/guides/\">Guides</a><a href=\"/#areas\">Service Areas</a><a href=\"/cybersecurity-consulting/\">Cyber Consulting</a><a href=\"/about\">About</a><a aria-label=\"Call Berthoud WiFi at 720-209-3130\" class=\"nav-phone\" href=\"tel:+17202093130\"><span aria-hidden=\"true\">☎</span>720-209-3130</a><a class=\"btn btn-primary\" href=\"/contact\">Get a quote</a></nav></div></header>"""


def footer_html() -> str:
    return """<footer class=\"site-footer\"><div class=\"container footer-grid\" data-nosnippet><div><a class=\"brand\" href=\"/\"><img alt=\"Berthoud WiFi\" height=\"160\" width=\"160\" src=\"/assets/images/berthoud-wifi-logo-160.webp?v=23\"/><span>Berthoud WiFi</span></a><p>UniFi-first networking, cybersecurity consulting, and practical digital growth support across Northern Colorado.</p><div class=\"footer-contact\"><a href=\"tel:+17202093130\">720-209-3130</a><a href=\"mailto:hello@berthoudwifi.com\">hello@berthoudwifi.com</a></div></div><div class=\"footer-links\"><strong>Services</strong><a href=\"/services/home-network-improvements\">Home Networks</a><a href=\"/services/small-business-infrastructure\">Small Business</a><a href=\"/cybersecurity-consulting/\">Cybersecurity Consulting</a><a href=\"/seo-services/\">SEO &amp; Organic Marketing</a></div><div class=\"footer-links\"><strong>Explore</strong><a href=\"/news/\">Articles</a><a href=\"/guides/\">Guides</a><a href=\"/cities/berthoud\">Berthoud</a><a href=\"/cities/loveland\">Loveland</a><a href=\"/cities/fort-collins\">Fort Collins</a></div></div><div class=\"container\"><p>© <span data-year></span> Berthoud WiFi. All rights reserved.</p></div></footer>"""


def article_page(item: dict[str, str]) -> str:
    url = f"{SITE}/news/{item['slug']}"
    schema = json.dumps({
        "@context": "https://schema.org",
        "@type": "Article",
        "headline": item["title"],
        "description": item["description"],
        "datePublished": TODAY,
        "dateModified": TODAY,
        "author": {"@type": "Person", "name": "Steve Smith"},
        "publisher": {"@id": f"{SITE}/#business"},
        "mainEntityOfPage": url,
        "image": f"{SITE}{item['image']}",
    }, separators=(",", ":"))
    return f'''<!doctype html>
<html lang="en-US"><head><meta charset="utf-8"/><meta content="width=device-width,initial-scale=1" name="viewport"/><title>{html.escape(item['title'])} | Berthoud WiFi</title><meta name="description" content="{html.escape(item['description'], quote=True)}"/><link rel="canonical" href="{url}"/><link href="/favicon.png?v=17" rel="icon" type="image/png"/><meta name="robots" content="index, follow, max-image-preview:large, max-snippet:-1, max-video-preview:-1"/><meta property="og:site_name" content="Berthoud WiFi"/><meta property="og:title" content="{html.escape(item['title'], quote=True)}"/><meta property="og:description" content="{html.escape(item['description'], quote=True)}"/><meta property="og:type" content="article"/><meta property="og:url" content="{url}"/><meta property="og:image" content="{SITE}{item['image']}"/><meta name="twitter:card" content="summary_large_image"/><script type="application/ld+json">{schema}</script><script async src="https://www.googletagmanager.com/gtag/js?id=G-3VV539JDCW"></script><script>window.dataLayer=window.dataLayer||[];function gtag(){{dataLayer.push(arguments)}}gtag('js',new Date());gtag('config','G-3VV539JDCW');</script><link href="/assets/css/site.css?v=23" rel="stylesheet"/></head><body>{nav_html()}<main><section class="page-hero"><div class="container post-body"><div class="breadcrumb"><a href="/">Home</a> / <a href="/news/">Articles</a></div><span class="eyebrow">{html.escape(item['eyebrow'])}</span><h1>{html.escape(item['title'])}</h1><p class="lead">{html.escape(item['description'])}</p><p class="post-meta">September 8, 2026 · Steve Smith</p></div></section><section class="section"><div class="container post-body"><img class="article-hero-image" src="{item['image']}" alt="{html.escape(item['eyebrow'])} strategy and consulting" loading="eager" fetchpriority="high"/>{item['body']}<h2>Need a clearer organic-growth plan?</h2><p>Berthoud WiFi provides <a href="/seo-services/">local SEO, technical SEO, and organic marketing services</a> for businesses that want a practical plan built around search data, website structure, and qualified leads.</p><div class="content-cta"><div><h2>Start with the site you already have.</h2><p>We can review the current website, Search Console data, local presence, and the pages already getting impressions before recommending what to build next.</p></div><a class="btn btn-primary" href="/seo-services/#seo-contact">Talk about SEO</a></div></div></section></main>{footer_html()}<script defer src="/assets/js/site.js?v=22"></script></body></html>'''


def publish_articles() -> None:
    news = ROOT / "news"
    news.mkdir(exist_ok=True)
    for item in ARTICLES:
        (news / f"{item['slug']}.html").write_text(article_page(item), encoding="utf-8")


def patch_navigation() -> None:
    for path in ROOT.rglob("*.html"):
        soup = BeautifulSoup(path.read_text(encoding="utf-8"), "lxml")
        changed = False
        nav = soup.select_one(".site-header .nav-links")
        if nav:
            direct_links = nav.find_all("a", recursive=False)
            if not any((a.get("href") or "").rstrip("/") == "/news" for a in direct_links):
                link = soup.new_tag("a", href="/news/")
                link.string = "Articles"
                guide = next((a for a in direct_links if (a.get("href") or "").rstrip("/") == "/guides"), None)
                if guide:
                    guide.insert_before(link)
                else:
                    nav.append(link)
                changed = True
            else:
                for a in direct_links:
                    if (a.get("href") or "").rstrip("/") == "/news" and a.get_text(strip=True) != "Articles":
                        a.string = "Articles"
                        changed = True
            dropdown = nav.select_one(".nav-dropdown")
            if dropdown and not dropdown.select_one('a[href="/seo-services/"]'):
                link = soup.new_tag("a", href="/seo-services/")
                link.string = "SEO & Organic Marketing"
                view_all = next((a for a in dropdown.find_all("a", recursive=False) if "view all" in a.get_text(" ", strip=True).lower()), None)
                if view_all:
                    view_all.insert_before(link)
                else:
                    dropdown.append(link)
                changed = True
        for select in soup.select('select[name="services"]'):
            if not any("seo" in option.get_text(" ", strip=True).lower() for option in select.find_all("option")):
                option = soup.new_tag("option")
                option.string = "SEO & organic marketing"
                not_sure = next((o for o in select.find_all("option") if "not sure" in o.get_text(" ", strip=True).lower()), None)
                if not_sure:
                    not_sure.insert_before(option)
                else:
                    select.append(option)
                changed = True
        if changed:
            path.write_text("<!doctype html>\n" + str(soup.html), encoding="utf-8")


def patch_news_index() -> None:
    path = ROOT / "news" / "index.html"
    if not path.exists():
        return
    soup = BeautifulSoup(path.read_text(encoding="utf-8"), "lxml")
    h1 = soup.select_one(".news-hero h1")
    eyebrow = soup.select_one(".news-hero .eyebrow")
    lead = soup.select_one(".news-hero .lead")
    if h1:
        h1.string = "Articles & Guides"
    if eyebrow:
        eyebrow.string = "The Connected Front Range"
    if lead:
        lead.string = "Practical Northern Colorado guidance on networking, cybersecurity, local SEO, organic marketing, cameras, fiber, and business technology."
    if soup.title:
        soup.title.string = "Articles & Guides | Berthoud WiFi"
    meta = soup.head.find("meta", attrs={"name": "description"})
    if meta:
        meta["content"] = "Berthoud WiFi articles and practical guides covering Northern Colorado networking, cybersecurity, local SEO, organic marketing, cameras, fiber, and business technology."
    editorial = soup.select_one(".editorial-list")
    if editorial:
        for item in reversed(ARTICLES):
            if editorial.select_one(f'[data-seo-post="{item["slug"]}"]'):
                continue
            card = BeautifulSoup(f'''<article class="editorial-card" data-seo-post="{item['slug']}"><img alt="{html.escape(item['eyebrow'])}" decoding="async" loading="lazy" src="{item['image']}"/><div class="editorial-card-content"><p class="post-meta">{html.escape(item['eyebrow'])}</p><h3>{html.escape(item['title'])}</h3><p>{html.escape(item['description'])}</p><a class="link-arrow" href="/news/{item['slug']}">Read article →</a></div></article>''', "html.parser")
            editorial.insert(0, card.article)
    path.write_text("<!doctype html>\n" + str(soup.html), encoding="utf-8")


def patch_seo_page() -> None:
    path = ROOT / "seo-services" / "index.html"
    if not path.exists():
        return
    text = path.read_text(encoding="utf-8")
    replacements = {
        "<span>Indexed pages</span><strong>84</strong><em>Healthy</em>": "<span>Indexing</span><strong>Review</strong><em>Coverage</em>",
        "<span>SEO health</span><strong>91%</strong><em>+18 pts</em>": "<span>Site health</span><strong>Audit</strong><em>Technical</em>",
        "<span>Issues found</span><strong>12</strong><em>Prioritized</em>": "<span>Priorities</span><strong>Roadmap</strong><em>Ordered</em>",
        "<span>Search opportunities</span><span>Current</span>": "<span>Search opportunities</span><span>Intent</span>",
        '<span class="seo-rank">#18</span>': '<span class="seo-rank">Service</span>',
        '<span class="seo-rank">#24</span>': '<span class="seo-rank">Local</span>',
        '<span class="seo-rank">#31</span>': '<span class="seo-rank">Profile</span>',
        '<span class="seo-rank">#27</span>': '<span class="seo-rank">Audit</span>',
    }
    for old, new in replacements.items():
        text = text.replace(old, new)
    soup = BeautifulSoup(text, "lxml")
    tour = soup.select_one(".seo-tour-wrap")
    if tour and not tour.select_one(".seo-demo-note"):
        note = soup.new_tag("p")
        note["class"] = ["seo-demo-note"]
        note.string = "The interface below demonstrates the process. Client reporting uses real Search Console, Analytics, Business Profile, and website data."
        label = tour.select_one(".seo-tour-label")
        if label:
            label.insert_after(note)
        else:
            tour.insert(0, note)
    if not soup.select_one(".seo-resource-links"):
        target = soup.select_one("#seo-contact") or soup.select_one(".sitewide-contact")
        if target:
            section = BeautifulSoup('<section class="section section-dark seo-resource-links"><div class="container"><div class="section-head"><span class="eyebrow">SEO Resources</span><h2>See how the pieces fit together.</h2><p class="lead">These guides explain the same practical process we use when reviewing search visibility and organic growth opportunities.</p></div><div class="resource-grid"></div></div></section>', "html.parser").section
            grid = section.select_one(".resource-grid")
            for item in ARTICLES:
                card = BeautifulSoup(f'<article class="resource-card"><h3>{html.escape(item["title"])}</h3><p>{html.escape(item["description"])}</p><a class="link-arrow" href="/news/{item["slug"]}">Read article →</a></article>', "html.parser").article
                grid.append(card)
            target.insert_before(section)
    path.write_text("<!doctype html>\n" + str(soup.html), encoding="utf-8")


def patch_site_js() -> None:
    path = ROOT / "assets" / "js" / "site.js"
    if not path.exists():
        return
    text = path.read_text(encoding="utf-8")
    text = text.replace('<span>Visibility</span><strong>+38%</strong><em>Trend</em>', '<span>Search data</span><strong>GSC</strong><em>Queries</em>')
    text = text.replace('<span>Health</span><strong>92</strong><em>Score</em>', '<span>Indexing</span><strong>Audit</strong><em>Pages</em>')
    text = text.replace('<span>Leads</span><strong>+17%</strong><em>Organic</em>', '<span>Local SEO</span><strong>GBP</strong><em>Maps</em>')
    path.write_text(text, encoding="utf-8")


def patch_sitemap() -> None:
    path = ROOT / "sitemap.xml"
    if not path.exists():
        return
    text = path.read_text(encoding="utf-8")
    additions = []
    for item in ARTICLES:
        url = f"{SITE}/news/{item['slug']}"
        if url not in text:
            additions.append(f"  <url><loc>{url}</loc><lastmod>{TODAY}</lastmod></url>")
    if additions:
        text = text.replace("</urlset>", "\n".join(additions) + "\n</urlset>")
    text = text.replace("<url><loc>https://berthoudwifi.com/</loc><lastmod>2026-08-08</lastmod></url>", f"<url><loc>https://berthoudwifi.com/</loc><lastmod>{TODAY}</lastmod></url>")
    text = text.replace("<url><loc>https://berthoudwifi.com/news/</loc><lastmod>2026-08-08</lastmod></url>", f"<url><loc>https://berthoudwifi.com/news/</loc><lastmod>{TODAY}</lastmod></url>")
    path.write_text(text, encoding="utf-8")


def main() -> None:
    publish_articles()
    patch_navigation()
    patch_news_index()
    patch_seo_page()
    patch_site_js()
    patch_sitemap()
    # Run navigation once more so newly generated and modified pages are consistent.
    patch_navigation()


if __name__ == "__main__":
    main()
