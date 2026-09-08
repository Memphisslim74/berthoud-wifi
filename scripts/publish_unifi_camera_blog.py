from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
NEWS_INDEX = ROOT / "news" / "index.html"
SITEMAP = ROOT / "sitemap.xml"
SLUG = "why-unifi-cameras-strong-security-system"

card = '''<article class="editorial-card" data-seo-post="why-unifi-cameras-strong-security-system">
<img alt="UniFi Protect security cameras for homes and businesses" decoding="async" loading="lazy" src="/assets/images/services/protect-security.webp"/>
<div class="editorial-card-content"><p class="post-meta">UniFi Protect cameras</p>
<h3>Why UniFi Cameras Are One of the Best Security Systems for Homes and Businesses</h3><p>Why UniFi Protect is a strong choice for Northern Colorado homes and businesses that want local recording, smart detections, wired PoE reliability, privacy, and room to grow.</p>
<a class="link-arrow" href="/news/why-unifi-cameras-strong-security-system">Read article →</a></div></article>'''

index = NEWS_INDEX.read_text(encoding="utf-8")
if f'data-seo-post="{SLUG}"' not in index:
    marker = '<div class="editorial-list">'
    if marker not in index:
        raise SystemExit("Could not find editorial-list insertion point in news/index.html")
    index = index.replace(marker, marker + card, 1)
    NEWS_INDEX.write_text(index, encoding="utf-8")

sitemap = SITEMAP.read_text(encoding="utf-8")
url = f"https://berthoudwifi.com/news/{SLUG}"
entry = f'  <url><loc>{url}</loc><lastmod>2026-09-08</lastmod></url>'
pattern = rf'  <url><loc>{re.escape(url)}</loc><lastmod>[^<]+</lastmod></url>'
if re.search(pattern, sitemap):
    sitemap = re.sub(pattern, entry, sitemap)
else:
    marker = '  <url><loc>https://berthoudwifi.com/news/security-camera-installation-cost-northern-colorado</loc>'
    pos = sitemap.find(marker)
    if pos >= 0:
        line_end = sitemap.find("\n", pos)
        sitemap = sitemap[:line_end + 1] + entry + "\n" + sitemap[line_end + 1:]
    else:
        sitemap = sitemap.replace("</urlset>", entry + "\n</urlset>")
SITEMAP.write_text(sitemap, encoding="utf-8")

print("UniFi camera article references are present in news index and sitemap")
