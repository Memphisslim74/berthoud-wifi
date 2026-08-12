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
BASELINE_LASTMOD = "2026-08-08"
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

POSTS.extend([
    {
        "slug": "home-ethernet-installation-cost-northern-colorado",
        "date": "2026-08-08",
        "title": "How Much Does Home Ethernet Installation Cost in Northern Colorado?",
        "description": "A practical 2026 guide to home Ethernet installation cost, including price per drop, finished-home labor, Cat6, patch panels, testing, and new construction.",
        "image": "/assets/images/actual/fiber-ethernet.webp",
        "image_alt": "Professional Cat6 Ethernet and structured cabling installation",
        "category": "Home Ethernet cost",
        "body": r'''
<p>Home Ethernet installation can range from a simple office wall jack to a complete structured wiring system serving access points, cameras, televisions, workstations, and a central network rack. The largest cost factor is usually not the cable itself. It is the labor required to create a clean path through the home.</p>
<p>Published 2026 pricing guides vary widely: <a href="https://www.angi.com/articles/ethernet-installation-cost.htm" rel="noopener noreferrer">Angi reports a broad $400 to $3,500 range for many home projects</a>, while other professional cabling guides commonly use roughly $100 to $250 per straightforward drop as an early budgeting range. Northern Colorado homes with finished basements, multiple floors, vaulted ceilings, fire blocking, stone, or limited attic access can cost more. An onsite scope is the only reliable way to price a retrofit.</p>
<h2>What changes the cost per Ethernet drop?</h2>
<ul><li>Whether walls are open or finished.</li><li>Attic, basement, and crawlspace access.</li><li>The distance and difficulty of each cable route.</li><li>Cat6 versus Cat6A and pathway size.</li><li>Exterior, masonry, or fire-rated penetrations.</li><li>Patch panels, wall plates, racks, switches, and UPS equipment.</li><li>Testing, labeling, documentation, and drywall repair requirements.</li></ul>
<h2>Finished-home retrofit versus new construction</h2>
<p>New construction is generally more efficient because cable routes are visible and multiple drops can be installed together before insulation and drywall. Finished homes require more planning and careful fishing. A low-looking price that excludes termination, testing, wall plates, patch-panel work, or cleanup is not directly comparable with a complete installation.</p>
<h2>How many locations should be included?</h2>
<p>Start with wired access points, home offices, televisions, gaming areas, cameras, doorbells, and the network rack. In new construction, spare drops and conduit are inexpensive compared with opening walls later. In an existing home, focus first on the locations that will materially improve reliability.</p>
<h2>What should a professional quote include?</h2>
<p>A useful quote should identify cable type, approximate routes, termination points, testing standard, labels, wall plates, patch-panel work, equipment exclusions, and any expected access or repair work. Berthoud WiFi provides <a href="/services/home-ethernet-installation">home Ethernet installation</a> and <a href="/builders/custom-home-low-voltage-prewire">custom-home pre-wire planning</a> across Northern Colorado. Send the rooms, device types, network location, and a few property details for a project-specific estimate.</p>
''',
    },
    {
        "slug": "how-many-ethernet-drops-new-custom-home",
        "date": "2026-08-16",
        "title": "How Many Ethernet Drops Should a New Custom Home Have?",
        "description": "Plan Ethernet drops for a new custom home, including access points, offices, televisions, cameras, doorbells, outdoor areas, racks, and future conduit.",
        "image": "/assets/images/projects/new-construction-ap.webp",
        "image_alt": "New custom-home access point location planned before drywall",
        "category": "Custom-home planning",
        "body": r'''
<p>There is no universal Ethernet-drop count for a custom home. A better plan starts with rooms, devices, coverage, and future pathways. A modest home may need a dozen carefully chosen runs. A larger custom home with cameras, multiple offices, outdoor living, and detached structures may need several dozen.</p>
<h2>Count systems, not just rooms</h2>
<p>Include wired WiFi access points, workstations, televisions, gaming areas, printers, cameras, doorbells, intercoms, touch panels, audio equipment, gates, garages, and outbuildings. Many of those locations use PoE, so the central switch and power budget matter as much as the cable count.</p>
<h2>Use at least two cables at important media and office locations</h2>
<p>Two or more runs create flexibility for a computer, phone, television, streaming device, small switch, or future equipment. Dedicated wired access points and cameras should normally have their own home runs to the network location.</p>
<h2>Do not forget ceilings and exterior areas</h2>
<p>Ceiling access-point locations are far easier to wire before drywall. Patios, pools, driveways, gates, soffits, garages, and shops should be included in the same property-wide plan.</p>
<h2>Add conduit where the future is uncertain</h2>
<p>Conduit can be more valuable than guessing at every future cable. Consider pathways from the service entrance to the rack, from the rack to attic or crawlspace areas, and toward gates or detached buildings.</p>
<p>Berthoud WiFi reviews plans with builders and homeowners through our <a href="/builders/custom-home-low-voltage-prewire">custom-home low-voltage pre-wire service</a>. The result is a labeled plan tied to the home’s actual technology goals.</p>
''',
    },
    {
        "slug": "security-camera-installation-cost-northern-colorado",
        "date": "2026-08-23",
        "title": "Security Camera Installation Cost in Northern Colorado",
        "description": "What affects the cost of professional wired security camera installation, including camera count, PoE cabling, recorder storage, mounting, gates, and local recording.",
        "image": "/assets/images/projects/completed-outdoor-device.webp",
        "image_alt": "Completed professional outdoor security camera installation",
        "category": "Camera installation cost",
        "body": r'''
<p>Security-camera installation cost depends on more than the number of cameras. A complete wired system may include camera planning, Ethernet cabling, PoE switching, mounting, a recorder, storage, UPS protection, configuration, and remote access.</p>
<p><a href="https://www.homeadvisor.com/cost/safety-and-security/security-camera-installation-cost/" rel="noopener noreferrer">HomeAdvisor's 2026 national guide places many professional home installations between about $593 and $2,040</a>, with larger or more complex systems extending beyond that range. Northern Colorado projects with long driveways, gates, barns, detached shops, high mounting locations, masonry, or difficult cable routes need a property-specific design.</p>
<h2>The largest cost drivers</h2>
<ul><li>Number and type of cameras.</li><li>New PoE cabling versus reusable cabling.</li><li>Mounting height, exterior access, and surface type.</li><li>Recorder model and desired footage retention.</li><li>Remote buildings, gates, fiber, or wireless bridges.</li><li>Night identification distance and specialty lenses.</li><li>Switching, UPS protection, configuration, and user setup.</li></ul>
<h2>Equipment-only pricing is not an installation quote</h2>
<p>A box of cameras does not account for coverage gaps, cable pathways, power, storage, weatherproofing, or whether a face and license plate will be useful at the required distance. Compare proposals by scope and expected result, not camera count alone.</p>
<h2>Local recording changes the long-term cost</h2>
<p>UniFi Protect records locally and avoids the typical per-camera cloud-storage subscription. The upfront recorder and storage cost should be compared with years of monthly fees, as well as the desired retention period.</p>
<p>See our <a href="/services/security-cameras">home and business security-camera installation service</a> or send the property, important views, and existing equipment for a tailored quote.</p>
''',
    },
    {
        "slug": "custom-home-low-voltage-prewire-checklist",
        "date": "2026-08-30",
        "title": "The Custom-Home Low-Voltage Pre-Wire Checklist",
        "description": "A builder-ready checklist for Ethernet, WiFi, cameras, fiber, conduit, gates, outdoor living, racks, power, testing, and documentation before drywall.",
        "image": "/assets/images/projects/jack-install-prep.webp",
        "image_alt": "Installer preparing equipment during a low-voltage project",
        "category": "Builder checklist",
        "body": r'''
<p>Low-voltage planning should happen before insulation and drywall, while cable routes and framing are visible. Use this checklist during plan review and the pre-wire walk.</p>
<h2>Service entrance and central rack</h2>
<ul><li>Confirm internet and utility entry locations.</li><li>Select a rack location with wall space, ventilation, service access, and adequate power.</li><li>Plan patch panels, gateway, PoE switches, recorder, storage, and UPS capacity.</li><li>Add conduit from the service entrance and toward accessible attic or crawlspace areas.</li></ul>
<h2>WiFi and wired devices</h2>
<ul><li>Place ceiling access points from a coverage plan.</li><li>Wire offices, media areas, televisions, gaming locations, and fixed equipment.</li><li>Consider two or more drops at important work and entertainment locations.</li><li>Include garages, patios, pools, outdoor kitchens, and guest spaces.</li></ul>
<h2>Security and property systems</h2>
<ul><li>Plan camera views for entrances, driveways, yards, gates, garages, and equipment areas.</li><li>Pre-wire doorbells, intercoms, access control, and gate locations.</li><li>Plan fiber or conduit to detached buildings and long exterior pathways.</li></ul>
<h2>Closeout requirements</h2>
<ul><li>Protect and label every cable during construction.</li><li>Photograph routes before drywall.</li><li>Terminate, test, and document completed runs.</li><li>Allow for final WiFi tuning and owner orientation after the home is furnished.</li></ul>
<p>Our <a href="/builders/custom-home-low-voltage-prewire">custom-home pre-wire service</a> gives Northern Colorado builders one partner for plan review, rough-in, trim-out, network installation, cameras, testing, and handoff.</p>
''',
    },
    {
        "slug": "wifi-access-point-placement-before-drywall",
        "date": "2026-09-06",
        "title": "Where Should WiFi Access Points Go Before Drywall?",
        "description": "How to place wired WiFi access points in a new home before drywall, including floor plans, building materials, ceiling locations, outdoor spaces, and coverage testing.",
        "image": "/assets/images/actual/ceiling-ap.webp",
        "image_alt": "Ceiling-mounted WiFi access point in a professionally designed network",
        "category": "New-construction WiFi",
        "body": r'''
<p>Access-point locations should be chosen from the finished floor plan, not simply spaced at equal distances or placed wherever the cable installer has easy access. Walls, floors, stone, metal, ductwork, cabinetry, ceiling height, and room use all change coverage.</p>
<h2>Start with where people and devices will be</h2>
<p>Prioritize offices, bedrooms, living spaces, media rooms, garages, patios, pools, and other areas where reliable service matters. Then account for device density and the construction between those spaces and the proposed access point.</p>
<h2>Ceiling placement is usually cleaner and more predictable</h2>
<p>Many professional access points are designed for ceiling or high-wall mounting. Avoid hiding them in metal cabinets, mechanical rooms, or crowded utility closets. A visually discreet location is useful only if it still serves the intended coverage area.</p>
<h2>Plan wired backhaul and switch capacity</h2>
<p>Each access point should have a home-run Ethernet cable to the network location. Verify cable category, route length, PoE requirements, and whether the planned switch supports the access point’s speed.</p>
<h2>Include outdoor and detached areas early</h2>
<p>Exterior living areas may need outdoor-rated access points. Detached garages, shops, and gates may need fiber, conduit, or a point-to-point bridge before local WiFi can be added.</p>
<p>Berthoud WiFi reviews access-point placement as part of <a href="/builders/custom-home-low-voltage-prewire">custom-home technology planning</a> and completes final tuning after the home is occupied.</p>
''',
    },
    {
        "slug": "prewire-new-home-security-cameras",
        "date": "2026-09-13",
        "title": "How to Pre-Wire a New Home for Security Cameras",
        "description": "Plan PoE security camera cabling before drywall, including driveway, entry, gate, garage, yard, recorder, lighting, mounting, and future camera locations.",
        "image": "/assets/images/projects/new-construction-ap.webp",
        "image_alt": "Low-voltage location prepared during new-home construction",
        "category": "Camera pre-wire",
        "body": r'''
<p>Camera pre-wire is most effective when it begins with the views the homeowner will need, not a fixed number of generic soffit locations. A camera should either identify, observe, or provide context for a specific area.</p>
<h2>Map the important events</h2>
<p>Walk through arrivals, packages, vehicles, visitors, backyard access, garages, gates, equipment, and detached structures. Decide where identification matters and where a wider overview is enough.</p>
<h2>Coordinate mounting with exterior finishes</h2>
<p>Stone, stucco, siding, soffits, lighting, gutters, rooflines, and landscaping affect the final field of view and service access. Cable locations should leave room for a proper mount and weather-protected termination.</p>
<h2>Run home-run Cat6 to the network location</h2>
<p>PoE camera cabling should terminate at the planned rack or recorder location. Confirm PoE switch capacity, UPS protection, ventilation, recorder storage, and an internet path for remote viewing.</p>
<h2>Plan for gates and detached buildings</h2>
<p>Long distances may need fiber, a wireless bridge, local power, and a remote PoE switch. Conduit installed during site work can preserve options for future cameras, intercoms, and access control.</p>
<h2>Photograph and label before drywall</h2>
<p>Document each route and leave clear labels at both ends. Spare cable or conduit at likely future locations can be a small investment compared with reopening finished walls.</p>
<p>Berthoud WiFi combines <a href="/services/security-cameras">camera installation</a> with <a href="/builders/custom-home-low-voltage-prewire">builder pre-wire coordination</a> so the network, storage, and property links are planned together.</p>
''',
    },
    {
        "slug": "electrician-or-low-voltage-installer-home-ethernet",
        "date": "2026-09-20",
        "title": "Electrician or Low-Voltage Installer: Who Should Run Home Ethernet?",
        "description": "Compare electricians and low-voltage network installers for home Ethernet, Cat6, access points, cameras, patch panels, testing, racks, and new-construction pre-wire.",
        "image": "/assets/images/projects/jack-rack-install.webp",
        "image_alt": "Low-voltage network installer working inside a structured rack",
        "category": "Choosing an installer",
        "body": r'''
<p>Some electricians install excellent low-voltage cabling, and some focus primarily on line-voltage power. The title matters less than the scope, experience, testing, and final handoff. Ethernet is not difficult because the voltage is high; it is difficult because routing, termination, performance, and network design all have to be correct.</p>
<h2>Ask what the installer will deliver</h2>
<ul><li>Appropriate Cat6 or Cat6A cable and pathways.</li><li>Correct separation from power and respect for bend radius.</li><li>Wall plates, keystones, patch panels, and service loops.</li><li>Labels at both ends of every run.</li><li>Testing results and correction of failed runs.</li><li>A rack and switch plan that supports access points, cameras, and PoE.</li></ul>
<h2>Network design and cable installation are connected</h2>
<p>A cable can pass a basic test and still terminate in the wrong place for WiFi coverage, camera identification, or the equipment rack. A network-focused low-voltage installer can coordinate device placement, switching, PoE budgets, internet service, VLANs, and the final configuration.</p>
<h2>Use the right trade for the right work</h2>
<p>Electricians remain essential for outlets, dedicated circuits, grounding, and other line-voltage requirements. Low-voltage installers focus on data cabling and network systems. Well-run projects coordinate both trades instead of assuming one scope replaces the other.</p>
<p>Berthoud WiFi provides <a href="/services/home-ethernet-installation">home Ethernet installation</a>, testing, rack work, WiFi, and camera integration across Northern Colorado.</p>
''',
    },
    {
        "slug": "outdoor-wifi-patios-pools-large-colorado-properties",
        "date": "2026-09-27",
        "title": "Outdoor WiFi for Patios, Pools and Larger Colorado Properties",
        "description": "Plan reliable outdoor WiFi for patios, pools, acreage, barns, shops, detached garages, gates, venues, and larger Northern Colorado properties.",
        "image": "/assets/images/projects/outdoor-bridge-install.webp",
        "image_alt": "Professional outdoor WiFi and wireless bridge installation",
        "category": "Outdoor WiFi",
        "body": r'''
<p>Outdoor WiFi is often treated as an afterthought: place a mesh node by a window and hope the signal reaches the patio. That approach struggles with exterior walls, low-emissivity glass, distance, weather, trees, terrain, and detached structures.</p>
<h2>Start with the outdoor use area</h2>
<p>Map where phones, speakers, televisions, cameras, tablets, point-of-sale devices, or work equipment will connect. A pool deck, outdoor kitchen, gate, arena, parking area, and acreage property have different coverage patterns.</p>
<h2>Choose dependable backhaul</h2>
<p>Ethernet is preferred when practical. Fiber can serve long or electrically separate pathways. A point-to-point wireless bridge can connect buildings where trenching is not practical and good line of sight is available.</p>
<h2>Use weather-rated equipment and protected cabling</h2>
<p>Outdoor access points must be mounted for exposure, water paths, sunlight, wind, temperature, and serviceability. Cable type, penetrations, drip loops, surge considerations, and PoE power are part of the installation.</p>
<h2>Do not ask one access point to cover everything</h2>
<p>Large properties may need separate zones for the home, yard, barn, shop, gate, or event area. Sensible power levels and placement create better roaming than a single radio turned up to maximum.</p>
<h2>Test in the places that matter</h2>
<p>Final testing should happen at seating, work, parking, gate, and remote-building locations—not only beside the access point. See our <a href="/services/outdoor-wifi">outdoor WiFi installation service</a> for patios, pools, businesses, acreage, and multi-building properties.</p>
''',
    },
])

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

SITEWIDE_CONTACT_HTML = r'''
<section id="contact" class="sitewide-contact" aria-labelledby="sitewide-contact-title">
  <div class="container sitewide-contact-grid">
    <div class="sitewide-contact-copy">
      <span class="eyebrow">Start a conversation</span>
      <h2 id="sitewide-contact-title">Tell us what needs to work better.</h2>
      <p>Share the property, the problem areas, and what you need the network to support. We will review the details and follow up with practical next steps.</p>
      <div class="sitewide-contact-direct" data-nosnippet="">
        <a href="tel:+17202093130">Call 720-209-3130</a>
        <a href="mailto:hello@berthoudwifi.com">hello@berthoudwifi.com</a>
      </div>
    </div>
    <form class="contact-form quote-card compact-contact-form" data-contact-form novalidate>
      <div class="honeypot" aria-hidden="true" hidden style="display:none!important">
        <label for="sitewide-company-website">Leave this field empty</label>
        <input id="sitewide-company-website" name="company_website" type="text" tabindex="-1" autocomplete="off">
      </div>
      <div class="form-field">
        <label for="sitewide-name">Name *</label>
        <input id="sitewide-name" name="name" type="text" autocomplete="name" required>
      </div>
      <div class="form-field">
        <label for="sitewide-email">Email *</label>
        <input id="sitewide-email" name="email" type="email" autocomplete="email" required>
      </div>
      <div class="form-field">
        <label for="sitewide-phone">Phone</label>
        <input id="sitewide-phone" name="phone" type="tel" autocomplete="tel">
      </div>
      <div class="form-field">
        <label for="sitewide-city">City</label>
        <input id="sitewide-city" name="city" type="text" autocomplete="address-level2" placeholder="Berthoud, Loveland, Fort Collins…">
      </div>
      <div class="form-field full">
        <label for="sitewide-service">What do you need help with?</label>
        <select id="sitewide-service" name="services">
          <option value="">Select a service</option>
          <option>Home WiFi improvements</option>
          <option>Home Ethernet installation</option>
          <option>New-construction or builder pre-wire</option>
          <option>UniFi network installation</option>
          <option>Small business infrastructure</option>
          <option>UniFi Protect cameras</option>
          <option>Door access or intercom</option>
          <option>Fiber or structured cabling</option>
          <option>Building-to-building connection</option>
          <option>Outdoor or rural connectivity</option>
          <option>Network troubleshooting</option>
          <option>Not sure yet</option>
        </select>
      </div>
      <div class="form-field full">
        <label for="sitewide-message">How can we help? *</label>
        <textarea id="sitewide-message" name="message" required placeholder="What is not working, where do you need coverage, and what equipment do you already have?"></textarea>
      </div>
      <div class="form-actions">
        <button class="btn btn-primary" type="submit">Send Request</button>
        <p class="form-status" data-form-status aria-live="polite"></p>
      </div>
    </form>
  </div>
</section>
'''


def clean_route(route: str) -> str:
    if not route:
        return route
    if route == "/index.html":
        return "/"
    route = re.sub(r"/index\.html$", "/", route)
    route = re.sub(r"\.html$", "", route)
    return route or "/"


def customize_builder_contact(section: BeautifulSoup) -> None:
    title = section.select_one("#sitewide-contact-title")
    intro = section.select_one(".sitewide-contact-copy > p")
    button = section.select_one('button[type="submit"]')
    if title:
        title.string = "Send us your custom-home plans."
    if intro:
        intro.string = (
            "Share the project schedule and a secure plan link. You can also reply "
            "to the branded confirmation email with plan attachments."
        )
    if button:
        button.string = "Send Builder Request"

    service = section.select_one('select[name="services"]')
    anchor = service.find_parent("div") if service else None
    if anchor is None:
        return
    fields = BeautifulSoup(
        r'''
<div class="form-field"><label for="builder-company">Builder or company</label><input id="builder-company" name="company" type="text" autocomplete="organization"></div>
<div class="form-field"><label for="builder-size">Estimated square footage</label><input id="builder-size" name="project_size" type="text" inputmode="numeric" placeholder="For example, 6,500 sq. ft."></div>
<div class="form-field"><label for="builder-phase">Current construction phase</label><select id="builder-phase" name="construction_phase"><option value="">Select a phase</option><option>Planning or design</option><option>Permitting</option><option>Foundation or framing</option><option>Ready for low-voltage rough-in</option><option>Insulation or drywall approaching</option><option>Trim-out or finish stage</option><option>Existing home or remodel</option></select></div>
<div class="form-field"><label for="builder-drywall">Target drywall date</label><input id="builder-drywall" name="drywall_date" type="date"></div>
<div class="form-field full"><label for="builder-plans">Secure floor-plan link</label><input id="builder-plans" name="plans_link" type="url" inputmode="url" placeholder="Google Drive, Dropbox, OneDrive, or project portal"><small>Optional. You may also reply to your confirmation email with attachments.</small></div>
''',
        "html.parser",
    )
    for node in list(fields.contents):
        anchor.insert_before(node)


def ensure_growth_navigation(soup: BeautifulSoup) -> None:
    dropdown = soup.select_one(".nav-dropdown")
    if dropdown and not dropdown.select_one('a[href="/services/home-ethernet-installation"]'):
        first = dropdown.find("a")
        ethernet = soup.new_tag("a", href="/services/home-ethernet-installation")
        ethernet.string = "Home Ethernet"
        if first:
            first.insert_after(ethernet)
        else:
            dropdown.append(ethernet)
    if dropdown and not dropdown.select_one('a[href="/builders/custom-home-low-voltage-prewire"]'):
        builder = soup.new_tag("a", href="/builders/custom-home-low-voltage-prewire")
        builder.string = "Custom Home Pre-Wire"
        dropdown.append(builder)

    footer_services = None
    for block in soup.select(".footer-links"):
        heading = block.find("strong")
        if heading and heading.get_text(" ", strip=True) == "Services":
            footer_services = block
            break
    if footer_services and not footer_services.select_one('a[href="/services/home-ethernet-installation"]'):
        link = soup.new_tag("a", href="/services/home-ethernet-installation")
        link.string = "Home Ethernet"
        footer_services.append(link)
    if footer_services and not footer_services.select_one('a[href="/builders/custom-home-low-voltage-prewire"]'):
        link = soup.new_tag("a", href="/builders/custom-home-low-voltage-prewire")
        link.string = "Builder Pre-Wire"
        footer_services.append(link)


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


def ensure_contact_experience(soup: BeautifulSoup, rel: str) -> None:
    for duplicate in list(soup.select(".sitewide-contact")):
        duplicate.decompose()

    for existing in soup.select('[id="contact"]'):
        existing["id"] = "project-cta"

    has_form = rel == "contact.html"
    if rel not in {"contact.html", "thank-you.html"}:
        section = BeautifulSoup(SITEWIDE_CONTACT_HTML, "html.parser").find("section")
        if rel == "builders/custom-home-low-voltage-prewire.html":
            customize_builder_contact(section)
        footer = soup.select_one(".site-footer")
        if footer:
            footer.insert_before(section)
        elif soup.body:
            soup.body.append(section)
        has_form = True

    scripts = soup.find_all("script", src="/assets/js/contact-form.js")
    if has_form:
        if not scripts and soup.body:
            script = soup.new_tag("script", src="/assets/js/contact-form.js")
            script["defer"] = ""
            soup.body.append(script)
        for duplicate in scripts[1:]:
            duplicate.decompose()

    else:
        for script in scripts:
            script.decompose()


def set_thank_you_indexing(soup: BeautifulSoup, rel: str) -> None:
    if rel != "thank-you.html":
        return
    robots = soup.head.find("meta", attrs={"name": "robots"})
    if robots is None:
        robots = soup.new_tag("meta", attrs={"name": "robots"})
        soup.head.append(robots)
    robots["content"] = "noindex, nofollow"


def normalize_html(path: Path) -> None:
    soup = BeautifulSoup(path.read_text(encoding="utf-8"), "lxml")
    if not soup.head:
        return

    rel = path.relative_to(ROOT).as_posix()
    if rel in PRIORITY_META:
        set_meta(soup, *PRIORITY_META[rel])

    ensure_contact_experience(soup, rel)
    ensure_growth_navigation(soup)
    set_thank_you_indexing(soup, rel)

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
    for path in sorted(ROOT.rglob("*.html")):
        rel = path.relative_to(ROOT).as_posix()
        if any(part in {"dist", "node_modules"} or part.startswith(".") for part in path.relative_to(ROOT).parts):
            continue
        if rel == "thank-you.html":
            continue
        route = route_for_file(path)
        page_dates = {
            "services/home-ethernet-installation.html": "2026-08-08",
            "builders/custom-home-low-voltage-prewire.html": "2026-08-08",
            "services/outdoor-wifi.html": "2026-08-08",
            "services/security-cameras.html": "2026-08-08",
            "cities/timnath.html": "2026-08-08",
            "cities/windsor.html": "2026-08-08",
            "cities/johnstown.html": "2026-08-08",
            "cybersecurity-consulting/index.html": "2026-08-11",
        }
        lastmod = post_dates.get(rel, page_dates.get(rel, BASELINE_LASTMOD))
        urls.append((route, lastmod))

    unique = {}
    for route, lastmod in urls:
        unique[route] = max(lastmod, unique.get(route, "0000-00-00"))

    lines = ['<?xml version="1.0" encoding="UTF-8"?>', '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
    for route in sorted(unique, key=lambda x: (x != "/", x)):
        lines.append(f"  <url><loc>{SITE_URL}{route}</loc><lastmod>{unique[route]}</lastmod></url>")
    lines.append("</urlset>")
    (ROOT / "sitemap.xml").write_text("\n".join(lines) + "\n", encoding="utf-8")


def ensure_security_headers() -> None:
    """Keep Turnstile allowed after the legacy refresh rewrites _headers."""
    (ROOT / "_headers").write_text(
        "/*\n"
        "  X-Content-Type-Options: nosniff\n"
        "  Referrer-Policy: strict-origin-when-cross-origin\n"
        "  Permissions-Policy: geolocation=(), microphone=(), camera=()\n"
        "  X-Frame-Options: SAMEORIGIN\n"
        "  Content-Security-Policy: default-src 'self'; img-src 'self' data: https:; "
        "style-src 'self' 'unsafe-inline'; script-src 'self' "
        "'unsafe-inline' https://www.googletagmanager.com https://www.google-analytics.com "
        "https://challenges.cloudflare.com; font-src 'self' data:; "
        "connect-src 'self' https://www.google-analytics.com https://region1.google-analytics.com; "
        "frame-src https://challenges.cloudflare.com; frame-ancestors 'self'; base-uri 'self'; "
        "form-action 'self' mailto:;\n"
        "\n"
        "/robots.txt\n"
        "  Cache-Control: public, max-age=3600\n"
        "  Content-Type: text/plain; charset=utf-8\n"
        "\n"
        "/llms.txt\n"
        "  Cache-Control: public, max-age=3600\n"
        "  Content-Type: text/plain; charset=utf-8\n"
        "\n"
        "/assets/fonts/*\n"
        "  Cache-Control: public, max-age=31536000, immutable\n"
        "\n"
        "/assets/images/hero-office-v22-*\n"
        "  Cache-Control: public, max-age=31536000, immutable\n"
        "\n"
        "/assets/images/berthoud-wifi-logo-160.webp\n"
        "  Cache-Control: public, max-age=31536000, immutable\n",
        encoding="utf-8",
    )


def main() -> None:
    published = [post for post in POSTS if post["date"] <= TODAY]
    print(f"SEO growth run for {TODAY}: {len(published)} scheduled posts are live.")

    for post in published:
        render_article(post)
    update_news_index(published)

    for path in sorted(ROOT.rglob("*.html")):
        if any(part in {"dist", "node_modules"} or part.startswith(".") for part in path.relative_to(ROOT).parts):
            continue
        normalize_html(path)

    update_sitemap(published)
    ensure_security_headers()


if __name__ == "__main__":
    main()
