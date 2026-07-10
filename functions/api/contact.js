const json = (data, status = 200) =>
  new Response(JSON.stringify(data), {
    status,
    headers: {
      "Content-Type": "application/json; charset=utf-8",
      "Cache-Control": "no-store",
    },
  });

const clean = (value, max = 2000) =>
  String(value ?? "")
    .replace(/\0/g, "")
    .trim()
    .slice(0, max);

const escapeHtml = (value) =>
  clean(value, 5000).replace(/[&<>"']/g, (char) => ({
    "&": "&amp;",
    "<": "&lt;",
    ">": "&gt;",
    '"': "&quot;",
    "'": "&#039;",
  })[char]);

const isEmail = (value) =>
  /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(value);

export async function onRequestPost(context) {
  const { request, env } = context;

  if (!env.RESEND_API_KEY) {
    console.error("RESEND_API_KEY is not configured.");
    return json({ ok: false, message: "The contact form is not configured yet." }, 500);
  }

  let body;
  try {
    body = await request.json();
  } catch {
    return json({ ok: false, message: "Invalid form submission." }, 400);
  }

  // Honeypot field. Real visitors never fill this in.
  if (clean(body.company_website, 200)) {
    return json({ ok: true, message: "Thank you." });
  }

  const name = clean(body.name, 100);
  const email = clean(body.email, 200);
  const phone = clean(body.phone, 50);
  const city = clean(body.city, 100);
  const service = clean(body.service, 150);
  const propertyType = clean(body.property_type, 100);
  const message = clean(body.message, 5000);

  if (!name || !email || !message) {
    return json({
      ok: false,
      message: "Please provide your name, email address, and project details.",
    }, 400);
  }

  if (!isEmail(email)) {
    return json({ ok: false, message: "Please enter a valid email address." }, 400);
  }

  const fromEmail = env.CONTACT_FROM_EMAIL || "Berthoud WiFi <forms@berthoudwifi.com>";
  const toEmail = env.CONTACT_TO_EMAIL || "hello@berthoudwifi.com";

  const subjectCity = city ? ` in ${city}` : "";
  const subject = `New Berthoud WiFi request${subjectCity}: ${service || "General inquiry"}`;

  const html = `
    <div style="font-family:Arial,sans-serif;max-width:680px;margin:auto;color:#102033">
      <h1 style="font-size:24px">New Berthoud WiFi request</h1>
      <table style="border-collapse:collapse;width:100%">
        <tr><td style="padding:8px;border-bottom:1px solid #ddd"><strong>Name</strong></td><td style="padding:8px;border-bottom:1px solid #ddd">${escapeHtml(name)}</td></tr>
        <tr><td style="padding:8px;border-bottom:1px solid #ddd"><strong>Email</strong></td><td style="padding:8px;border-bottom:1px solid #ddd">${escapeHtml(email)}</td></tr>
        <tr><td style="padding:8px;border-bottom:1px solid #ddd"><strong>Phone</strong></td><td style="padding:8px;border-bottom:1px solid #ddd">${escapeHtml(phone || "Not provided")}</td></tr>
        <tr><td style="padding:8px;border-bottom:1px solid #ddd"><strong>City</strong></td><td style="padding:8px;border-bottom:1px solid #ddd">${escapeHtml(city || "Not provided")}</td></tr>
        <tr><td style="padding:8px;border-bottom:1px solid #ddd"><strong>Property</strong></td><td style="padding:8px;border-bottom:1px solid #ddd">${escapeHtml(propertyType || "Not provided")}</td></tr>
        <tr><td style="padding:8px;border-bottom:1px solid #ddd"><strong>Service</strong></td><td style="padding:8px;border-bottom:1px solid #ddd">${escapeHtml(service || "General inquiry")}</td></tr>
      </table>
      <h2 style="font-size:18px;margin-top:24px">Project details</h2>
      <div style="white-space:pre-wrap;background:#f5f7fa;padding:16px;border-radius:10px">${escapeHtml(message)}</div>
      <p style="color:#667085;margin-top:22px">Submitted from berthoudwifi.com</p>
    </div>
  `;

  const text = [
    "New Berthoud WiFi request",
    `Name: ${name}`,
    `Email: ${email}`,
    `Phone: ${phone || "Not provided"}`,
    `City: ${city || "Not provided"}`,
    `Property: ${propertyType || "Not provided"}`,
    `Service: ${service || "General inquiry"}`,
    "",
    "Project details:",
    message,
  ].join("\n");

  const response = await fetch("https://api.resend.com/emails", {
    method: "POST",
    headers: {
      Authorization: `Bearer ${env.RESEND_API_KEY}`,
      "Content-Type": "application/json",
    },
    body: JSON.stringify({
      from: fromEmail,
      to: [toEmail],
      reply_to: email,
      subject,
      html,
      text,
    }),
  });

  const result = await response.json().catch(() => ({}));

  if (!response.ok) {
    console.error("Resend API error:", response.status, result);
    return json({
      ok: false,
      message: "We could not send your request. Please try again shortly.",
    }, 502);
  }

  return json({
    ok: true,
    message: "Thanks — your request has been sent. We’ll be in touch soon.",
    id: result.id,
  });
}

export function onRequestGet() {
  return json({ ok: false, message: "Method not allowed." }, 405);
}
