import fs from 'fs';
import path from 'path';

const root = process.cwd();
const dist = path.join(root, 'dist');

if (fs.existsSync(dist)) fs.rmSync(dist, { recursive: true, force: true });
fs.mkdirSync(dist, { recursive: true });

const skip = new Set(['dist', 'node_modules', '.git', 'scripts']);
for (const entry of fs.readdirSync(root, { withFileTypes: true })) {
  if (skip.has(entry.name)) continue;
  fs.cpSync(path.join(root, entry.name), path.join(dist, entry.name), { recursive: true });
}

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
      .replaceAll(
        /href="\/assets\/css\/brand-refresh\.css\?v=\d+"/g,
        'href="/assets/css/brand-refresh.css?v=21"',
      )
      .replace(
        /src="\/assets\/js\/site\.js(?:\?v=\d+)?"/g,
        'src="/assets/js/site.js?v=21"',
      );
    if (versioned !== html) fs.writeFileSync(entryPath, versioned);
  }
}

versionSharedAssets(dist);
console.log('Berthoud WiFi site copied to dist with v21 shared assets');
