const json = (data, status = 200) =>
  new Response(JSON.stringify(data), {
    status,
    headers: {
      "Content-Type": "application/json; charset=utf-8",
      "Cache-Control": "no-store",
    },
  });

const clean = (value, max = 2000) =>
  String(value ?? "").replace(/\0/g, "").trim().slice(0, max);

const escapeHtml = (value) =>
  clean(value, 10000).replace(/[&<>"']/g, (char) => ({
    "&": "&amp;",
    "<": "&lt;",
    ">": "&gt;",
    '"': "&quot;",
    "'": "&#039;",
  })[char]);

const isEmail = (value) => /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(value);

const formatServices = (services) => {
  if (Array.isArray(services)) return services.map((s) => clean(s, 100)).filter(Boolean);
  if (!services) return [];
  return String(services).split(",").map((s) => clean(s, 100)).filter(Boolean);
};

const emailShell = ({ eyebrow, title, intro, content, footerNote }) => `
<!doctype html>
<html>
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width,initial-scale=1">
</head>
<body style="margin:0;background:#07111e;padding:24px;font-family:Arial,Helvetica,sans-serif;color:#102033">
  <table role="presentation" width="100%" cellspacing="0" cellpadding="0" border="0">
    <tr>
      <td align="center">
        <table role="presentation" width="100%" cellspacing="0" cellpadding="0" border="0" style="max-width:680px;background:#ffffff;border-radius:22px;overflow:hidden;box-shadow:0 18px 50px rgba(0,0,0,.25)">
          <tr>
            <td style="background:linear-gradient(135deg,#07111e,#0e2a48);padding:28px 32px;text-align:center">
              <img src="https://berthoudwifi.com/assets/images/berthoud-wifi-logo.png" width="110" alt="Berthoud WiFi" style="display:block;margin:0 auto 12px;border-radius:50%">
              <div style="font-size:24px;line-height:1.2;font-weight:800;color:#ffffff;letter-spacing:.4px">BERTHOUD WIFI</div>
              <div style="margin-top:6px;color:#65c7ff;font-size:13px;font-weight:700;letter-spacing:.9px">UNIFI-FIRST SOLUTIONS • NORTHERN COLORADO</div>
            </td>
          </tr>
          <tr>
            <td style="padding:34px 34px 12px">
              <div style="font-size:12px;font-weight:800;color:#1597ff;letter-spacing:1.4px;text-transform:uppercase">${eyebrow}</div>
              <h1 style="margin:10px 0 12px;font-size:30px;line-height:1.15;color:#0b1725">${title}</h1>
              <p style="margin:0;color:#53657a;font-size:16px;line-height:1.65">${intro}</p>
            </td>
          </tr>
          <tr>
            <td style="padding:12px 34px 34px">${content}</td>
          </tr>
          <tr>
            <td style="background:#eef5fb;padding:22px 34px;text-align:center;color:#60758a;font-size:13px;line-height:1.6">
              ${footerNote}<br>
              <a href="https://berthoudwifi.com" style="color:#0875d2;font-weight:700;text-decoration:none">berthoudwifi.com</a>
            </td>
          </tr>
        </table>
      </td>
    </tr>
  </table>
</body>
</html>`;

const infoRow = (label, value) => `
<tr>
  <td style="padding:11px 12px;border-bottom:1px solid #e6edf4;color:#6b7d90;font-size:13px;font-weight:700;width:34%">${label}</td>
  <td style="padding:11px 12px;border-bottom:1px solid #e6edf4;color:#142235;font-size:14px">${value}</td>
</tr>`;

async function sendResend(env, payload) {
  const response = await fetch("https://api.resend.com/emails", {
    method: "POST",
    headers: {
      Authorization: `Bearer ${env.RESEND_API_KEY}`,
      "Content-Type": "application/json",
    },
    body: JSON.stringify(payload),
  });

  const result = await response.json().catch(() => ({}));
  if (!response.ok) {
    console.error("Resend API error:", response.status, result);
    throw new Error(result.message || "Resend rejected the email.");
  }
  return result;
}

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

  if (clean(body.company_website, 200)) {
    return json({ ok: true, message: "Thank you." });
  }

  const name = clean(body.name, 100);
  const email = clean(body.email, 200);
  const phone = clean(body.phone, 50);
  const city = clean(body.city, 100);
  const propertyType = clean(body.property_type, 100);
  const budget = clean(body.budget, 100);
  const timeline = clean(body.timeline, 100);
  const message = clean(body.message, 5000);
  const services = formatServices(body.services);

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
  const serviceSummary = services.length ? services.join(", ") : "General inquiry";
  const submittedAt = new Date().toLocaleString("en-US", {
    timeZone: "America/Denver",
    dateStyle: "medium",
    timeStyle: "short",
  });

  const adminContent = `
    <table role="presentation" width="100%" cellspacing="0" cellpadding="0" border="0" style="border:1px solid #e3ebf3;border-radius:14px;overflow:hidden">
      ${infoRow("Name", escapeHtml(name))}
      ${infoRow("Email", `<a href="mailto:${escapeHtml(email)}" style="color:#0875d2;text-decoration:none">${escapeHtml(email)}</a>`)}
      ${infoRow("Phone", phone ? `<a href="tel:${escapeHtml(phone)}" style="color:#0875d2;text-decoration:none">${escapeHtml(phone)}</a>` : "Not provided")}
      ${infoRow("City", escapeHtml(city || "Not provided"))}
      ${infoRow("Property", escapeHtml(propertyType || "Not provided"))}
      ${infoRow("Services", escapeHtml(serviceSummary))}
      ${infoRow("Budget", escapeHtml(budget || "Not provided"))}
      ${infoRow("Timeline", escapeHtml(timeline || "Not provided"))}
      ${infoRow("Received", escapeHtml(submittedAt))}
    </table>

    <div style="margin-top:22px;background:#f5f8fb;border-radius:14px;padding:18px">
      <div style="font-size:12px;font-weight:800;color:#1597ff;letter-spacing:1px;text-transform:uppercase;margin-bottom:8px">Project details</div>
      <div style="white-space:pre-wrap;color:#24384d;font-size:15px;line-height:1.65">${escapeHtml(message)}</div>
    </div>

    <div style="margin-top:24px;text-align:center">
      <a href="mailto:${escapeHtml(email)}?subject=${encodeURIComponent("Re: Your Berthoud WiFi request")}" style="display:inline-block;background:#1597ff;color:white;text-decoration:none;font-weight:800;padding:13px 20px;border-radius:999px;margin:4px">Reply to Customer</a>
      ${phone ? `<a href="tel:${escapeHtml(phone)}" style="display:inline-block;background:#0b1725;color:white;text-decoration:none;font-weight:800;padding:13px 20px;border-radius:999px;margin:4px">Call Customer</a>` : ""}
    </div>`;

  const customerRows = `
    <table role="presentation" width="100%" cellspacing="0" cellpadding="0" border="0" style="border:1px solid #e3ebf3;border-radius:14px;overflow:hidden">
      ${infoRow("City", escapeHtml(city || "Not provided"))}
      ${infoRow("Property", escapeHtml(propertyType || "Not provided"))}
      ${infoRow("Services", escapeHtml(serviceSummary))}
      ${infoRow("Budget", escapeHtml(budget || "Not provided"))}
      ${infoRow("Timeline", escapeHtml(timeline || "Not provided"))}
    </table>

    <div style="margin-top:22px;background:#f5f8fb;border-radius:14px;padding:18px">
      <div style="font-size:12px;font-weight:800;color:#1597ff;letter-spacing:1px;text-transform:uppercase;margin-bottom:8px">Your project details</div>
      <div style="white-space:pre-wrap;color:#24384d;font-size:15px;line-height:1.65">${escapeHtml(message)}</div>
    </div>

    <div style="margin-top:24px;text-align:center">
      <a href="mailto:${escapeHtml(toEmail)}" style="display:inline-block;background:#1597ff;color:white;text-decoration:none;font-weight:800;padding:13px 20px;border-radius:999px;margin:4px">Email Berthoud WiFi</a>
      <a href="https://berthoudwifi.com/services/index.html" style="display:inline-block;background:#0b1725;color:white;text-decoration:none;font-weight:800;padding:13px 20px;border-radius:999px;margin:4px">View Services</a>
    </div>`;

  const adminHtml = emailShell({
    eyebrow: "New Lead Received",
    title: `New request from ${escapeHtml(name)}`,
    intro: "A new project request was submitted through berthoudwifi.com.",
    content: adminContent,
    footerNote: "This lead was submitted through the Berthoud WiFi website.",
  });

  const customerHtml = emailShell({
    eyebrow: "Request Confirmed",
    title: `Thanks, ${escapeHtml(name)}.`,
    intro: "We received your request and will review the details shortly. Here is a copy of what you submitted.",
    content: customerRows,
    footerNote: "Berthoud WiFi • Strong connections. Local support.",
  });

  const adminText = [
    "NEW BERTHOUD WIFI LEAD",
    `Name: ${name}`,
    `Email: ${email}`,
    `Phone: ${phone || "Not provided"}`,
    `City: ${city || "Not provided"}`,
    `Property: ${propertyType || "Not provided"}`,
    `Services: ${serviceSummary}`,
    `Budget: ${budget || "Not provided"}`,
    `Timeline: ${timeline || "Not provided"}`,
    `Received: ${submittedAt}`,
    "",
    "Project details:",
    message,
  ].join("\n");

  const customerText = [
    `Thanks, ${name}.`,
    "We received your Berthoud WiFi request and will review it shortly.",
    "",
    `City: ${city || "Not provided"}`,
    `Property: ${propertyType || "Not provided"}`,
    `Services: ${serviceSummary}`,
    `Budget: ${budget || "Not provided"}`,
    `Timeline: ${timeline || "Not provided"}`,
    "",
    "Your project details:",
    message,
    "",
    "Berthoud WiFi",
    "https://berthoudwifi.com",
  ].join("\n");

  try {
    const adminResult = await sendResend(env, {
      from: fromEmail,
      to: [toEmail],
      reply_to: email,
      subject: `New Berthoud WiFi lead: ${name}${city ? ` — ${city}` : ""}`,
      html: adminHtml,
      text: adminText,
    });

    let confirmationSent = true;
    try {
      await sendResend(env, {
        from: fromEmail,
        to: [email],
        reply_to: toEmail,
        subject: "We received your Berthoud WiFi request",
        html: customerHtml,
        text: customerText,
      });
    } catch (confirmationError) {
      confirmationSent = false;
      console.error("Customer confirmation failed:", confirmationError);
    }

    return json({
      ok: true,
      message: confirmationSent
        ? "Thanks — your request has been sent. A confirmation email is on its way."
        : "Thanks — your request has been sent. We’ll be in touch soon.",
      id: adminResult.id,
    });
  } catch (error) {
    console.error("Contact form delivery failed:", error);
    return json({
      ok: false,
      message: "We could not send your request. Please try again shortly.",
    }, 502);
  }
}

export function onRequestGet() {
  return json({ ok: false, message: "Method not allowed." }, 405);
}
