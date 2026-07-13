const json = (data, status = 200) =>
  new Response(JSON.stringify(data), {
    status,
    headers: {
      "Content-Type": "application/json; charset=utf-8",
      "Cache-Control": "no-store",
    },
  });

const clean = (value, max = 2048) =>
  String(value ?? "").replace(/\0/g, "").trim().slice(0, max);

async function validateTurnstile(secret, token, remoteIp) {
  const formData = new FormData();
  formData.append("secret", secret);
  formData.append("response", token);
  if (remoteIp) formData.append("remoteip", remoteIp);

  try {
    const response = await fetch(
      "https://challenges.cloudflare.com/turnstile/v0/siteverify",
      {
        method: "POST",
        body: formData,
      },
    );

    if (!response.ok) {
      return { success: false, "error-codes": ["siteverify-http-error"] };
    }

    return await response.json();
  } catch (error) {
    console.error("Turnstile validation request failed:", error);
    return { success: false, "error-codes": ["internal-error"] };
  }
}

export async function onRequest(context) {
  const { request, env } = context;
  const url = new URL(request.url);

  if (url.pathname !== "/api/contact" || request.method !== "POST") {
    return context.next();
  }

  const siteKey = clean(env.TURNSTILE_SITE_KEY, 500);
  const secret = clean(env.TURNSTILE_SECRET_KEY, 500);

  // The form remains operational until both Turnstile environment variables
  // have been configured in Cloudflare Pages.
  if (!siteKey || !secret) {
    return context.next();
  }

  let body;
  try {
    body = await request.clone().json();
  } catch {
    return json({ ok: false, message: "Invalid form submission." }, 400);
  }

  // Preserve the existing honeypot behavior and avoid giving bots useful feedback.
  if (clean(body.company_website, 200)) {
    return context.next();
  }

  const token = clean(
    body.turnstileToken || body["cf-turnstile-response"],
    2048,
  );

  if (!token) {
    return json(
      {
        ok: false,
        message: "Please complete the security check before sending.",
      },
      400,
    );
  }

  const remoteIp =
    request.headers.get("CF-Connecting-IP") ||
    request.headers.get("X-Forwarded-For") ||
    "";
  const result = await validateTurnstile(secret, token, remoteIp);

  if (!result.success || result.action !== "contact") {
    console.warn("Turnstile rejected contact submission:", {
      hostname: result.hostname,
      action: result.action,
      errors: result["error-codes"],
    });
    return json(
      {
        ok: false,
        message:
          "The security check could not be verified. Please try again.",
      },
      400,
    );
  }

  return context.next();
}
