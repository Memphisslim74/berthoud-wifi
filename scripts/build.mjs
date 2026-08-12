import fs from 'fs';
import path from 'path';

const root = process.cwd();
const dist = path.join(root, 'dist');
const assetVersion = 23;

if (fs.existsSync(dist)) fs.rmSync(dist, { recursive: true, force: true });
fs.mkdirSync(dist, { recursive: true });

const skip = new Set(['dist', 'node_modules', '.git', 'scripts']);
for (const entry of fs.readdirSync(root, { withFileTypes: true })) {
  if (skip.has(entry.name)) continue;
  fs.cpSync(path.join(root, entry.name), path.join(dist, entry.name), { recursive: true });
}

// Ship one shared stylesheet. The source homepage inlines this same file so its
// first paint does not wait for a second mobile network round trip.
const cssDirectory = path.join(dist, 'assets', 'css');
let combinedCss = [
  fs.readFileSync(path.join(root, 'assets', 'css', 'styles.css'), 'utf8'),
  fs.readFileSync(path.join(root, 'assets', 'css', 'brand-refresh.css'), 'utf8'),
].join('\n');
combinedCss = combinedCss.replace(
  /https:\/\/images\.unsplash\.com\/photo-1497366754035-f200968a6e72[^\")]+/g,
  '/assets/images/hero-office-v22-1600.webp',
);
if (!combinedCss.includes('/assets/fonts/inter-latin.woff2')) {
  combinedCss = `@font-face{font-family:Inter;font-style:normal;font-weight:400 600;font-display:swap;src:url("/assets/fonts/inter-latin.woff2") format("woff2")}\n@font-face{font-family:Fraunces;font-style:normal;font-weight:600 700;font-display:swap;src:url("/assets/fonts/fraunces-latin.woff2") format("woff2")}\n${combinedCss}`;
}
fs.writeFileSync(path.join(cssDirectory, 'site.css'), combinedCss);

function versionSharedAssets(directory) {
  for (const entry of fs.readdirSync(directory, { withFileTypes: true })) {
    const entryPath = path.join(directory, entry.name);
    if (entry.isDirectory()) {
      versionSharedAssets(entryPath);
      continue;
    }
    if (!entry.name.endsWith('.html')) continue;

    const html = fs.readFileSync(entryPath, 'utf8');
    const versioned = html
      .replace(/<link href="https:\/\/fonts\.googleapis\.com" rel="preconnect"\/>/g, '')
      .replace(/<link crossorigin="anonymous" href="https:\/\/fonts\.gstatic\.com" rel="preconnect"\/>/g, '')
      .replace(/<link href="https:\/\/fonts\.googleapis\.com\/css2\?[^\"]+" rel="stylesheet"\/>/g, '')
      .replace(/<link href="https:\/\/challenges\.cloudflare\.com" rel="preconnect"\/>/g, '')
      .replace(
        /<link href="\/assets\/css\/styles\.css(?:\?v=\d+)?" rel="stylesheet"\/>/g,
        `<link as="font" crossorigin href="/assets/fonts/fraunces-latin.woff2" rel="preload" type="font/woff2"/><link href="/assets/css/site.css?v=${assetVersion}" rel="stylesheet"/>`,
      )
      .replace(/<link href="\/assets\/css\/brand-refresh\.css(?:\?v=\d+)?" rel="stylesheet"\/>/g, '')
      .replace(
        /<link as="image" fetchpriority="high" href="https:\/\/images\.unsplash\.com\/photo-1497366754035-f200968a6e72[^\"]*" rel="preload"\/>/g,
        '<link as="image" fetchpriority="high" href="/assets/images/hero-office-v22-800.webp" media="(max-width: 700px)" rel="preload" type="image/webp"/><link as="image" fetchpriority="high" href="/assets/images/hero-office-v22-1600.webp" media="(min-width: 701px)" rel="preload" type="image/webp"/>',
      )
      .replace(
        /src="\/assets\/js\/site\.js(?:\?v=\d+)?"/g,
        `src="/assets/js/site.js?v=${assetVersion}"`,
      )
      .replace(
        /src="\/assets\/js\/contact-form\.js(?:\?v=\d+)?"/g,
        `src="/assets/js/contact-form.js?v=${assetVersion}"`,
      );
    if (versioned !== html) fs.writeFileSync(entryPath, versioned);
  }
}

versionSharedAssets(dist);
console.log(`Berthoud WiFi site copied to dist with v${assetVersion} performance assets`);
