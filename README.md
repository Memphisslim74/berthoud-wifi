# Berthoud WiFi v2

Expanded Northern Colorado UniFi service site with a Git-backed news CMS.

## Cloudflare Pages
- Build command: `npm run build`
- Output directory: `dist`
- Production branch: `main`

## CMS
The `.pages.yml` file configures Pages CMS. Sign in with GitHub, select this repository, and edit **The Connected Front Range** posts.

## Branding
All custom artwork is PNG. No SVG artwork or decorative animation is used.


## Resend contact forms

Every customer-facing page includes a contact form that submits to the Cloudflare Pages Function at:

`/functions/api/contact.js`

Configure these variables in **Cloudflare Pages → Settings → Variables and Secrets**:

- `RESEND_API_KEY` — add this as an encrypted secret.
- `CONTACT_FROM_EMAIL` — example: `Berthoud WiFi <forms@berthoudwifi.com>`
- `CONTACT_TO_EMAIL` — example: `hello@berthoudwifi.com`

Do not place the Resend API key in JavaScript, HTML, GitHub, or `.pages.yml`.

Before using `forms@berthoudwifi.com`, verify `berthoudwifi.com` in Resend and add the DNS records Resend provides.

The form includes:
- server-side validation
- HTML escaping
- a honeypot spam field
- Reply-To set to the visitor's email
- browser success and error messages


## Branded email workflow

Every successful form submission now sends two branded Resend emails:

1. **Lead notification to Berthoud WiFi**
   - Branded header and logo
   - Contact and project summary
   - Services, budget, timeline, city, and property type
   - Project details
   - Reply and call buttons

2. **Automatic confirmation to the customer**
   - Branded confirmation
   - Copy of their submitted contact and project details
   - A short “What happens next” section
   - Email and service buttons

Successful submissions redirect to `/thank-you`, which records the GA4 lead events and provides a dedicated conversion destination. The thank-you page is intentionally excluded from search indexing and the XML sitemap.

Recommended Cloudflare variables:

- `CONTACT_FROM_EMAIL=Berthoud WiFi <forms@berthoudwifi.com>`
- `CONTACT_TO_EMAIL=hello@berthoudwifi.com`
- `RESEND_API_KEY` as an encrypted secret

The sender domain must be verified in Resend.
