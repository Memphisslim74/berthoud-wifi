const json = (data, status = 200) =>
  new Response(JSON.stringify(data), {
    status,
    headers: {
      "Content-Type": "application/json; charset=utf-8",
      "Cache-Control": "no-store",
    },
  });

export function onRequestGet({ env }) {
  const siteKey = String(env.TURNSTILE_SITE_KEY || "").trim();
  const secretConfigured = Boolean(
    String(env.TURNSTILE_SECRET_KEY || "").trim(),
  );

  return json({
    enabled: Boolean(siteKey && secretConfigured),
    siteKey: siteKey || null,
  });
}

export function onRequest() {
  return json({ ok: false, message: "Method not allowed." }, 405);
}
