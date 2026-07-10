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

The homepage and `/contact.html` submit to the Cloudflare Pages Function at:

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
