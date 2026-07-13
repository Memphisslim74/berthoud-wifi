const forms = document.querySelectorAll("[data-contact-form]");

const TURNSTILE_SCRIPT_ID = "cloudflare-turnstile-api";
const TURNSTILE_SCRIPT_URL =
  "https://challenges.cloudflare.com/turnstile/v0/api.js?render=explicit";

let turnstileScriptPromise;

function loadTurnstileScript() {
  if (window.turnstile) return Promise.resolve(window.turnstile);
  if (turnstileScriptPromise) return turnstileScriptPromise;

  turnstileScriptPromise = new Promise((resolve, reject) => {
    const existing = document.getElementById(TURNSTILE_SCRIPT_ID);
    if (existing) {
      existing.addEventListener("load", () => resolve(window.turnstile), {
        once: true,
      });
      existing.addEventListener(
        "error",
        () => reject(new Error("The security check could not be loaded.")),
        { once: true },
      );
      return;
    }

    const script = document.createElement("script");
    script.id = TURNSTILE_SCRIPT_ID;
    script.src = TURNSTILE_SCRIPT_URL;
    script.async = true;
    script.defer = true;
    script.addEventListener("load", () => resolve(window.turnstile), {
      once: true,
    });
    script.addEventListener(
      "error",
      () => reject(new Error("The security check could not be loaded.")),
      { once: true },
    );
    document.head.appendChild(script);
  });

  return turnstileScriptPromise;
}

function createTurnstileField(form) {
  const existing = form.querySelector("[data-turnstile-field]");
  if (existing) return existing;

  const actions = form.querySelector(".form-actions");
  if (!actions) return null;

  const field = document.createElement("div");
  field.className = "form-field full turnstile-field";
  field.dataset.turnstileField = "";
  field.hidden = true;
  field.innerHTML = `
    <div class="turnstile-widget" data-turnstile-container></div>
    <p class="turnstile-note">Protected by Cloudflare Turnstile.</p>
  `;
  actions.before(field);
  return field;
}

async function initializeTurnstile(form, submitButton, statusBox, state) {
  const field = createTurnstileField(form);
  if (!field) return;

  let config;
  try {
    const response = await fetch("/api/turnstile-config", {
      headers: { Accept: "application/json" },
      cache: "no-store",
    });
    if (!response.ok) throw new Error("Security configuration unavailable.");
    config = await response.json();
  } catch (error) {
    console.error("Turnstile configuration error:", error);
    state.failed = true;
    submitButton.disabled = true;
    field.hidden = false;
    field.classList.add("is-error");
    field.querySelector("[data-turnstile-container]").textContent =
      "The security check is temporarily unavailable. Please call 720-209-3130 or email hello@berthoudwifi.com.";
    statusBox.textContent = "The form security check could not load.";
    statusBox.className = "form-status is-error";
    return;
  }

  if (!config.enabled || !config.siteKey) {
    field.remove();
    return;
  }

  state.enabled = true;
  field.hidden = false;
  submitButton.disabled = true;

  try {
    const turnstile = await loadTurnstileScript();
    if (!turnstile || typeof turnstile.render !== "function") {
      throw new Error("The security check could not be initialized.");
    }

    const container = field.querySelector("[data-turnstile-container]");
    state.widgetId = turnstile.render(container, {
      sitekey: config.siteKey,
      theme: "light",
      size: "flexible",
      action: "contact",
      callback(token) {
        state.token = token;
        state.failed = false;
        submitButton.disabled = false;
        if (statusBox.classList.contains("is-error")) {
          statusBox.textContent = "";
          statusBox.className = "form-status";
        }
      },
      "expired-callback"() {
        state.token = "";
        submitButton.disabled = true;
        statusBox.textContent = "The security check expired. Please complete it again.";
        statusBox.className = "form-status is-error";
      },
      "error-callback"() {
        state.token = "";
        state.failed = true;
        submitButton.disabled = true;
        statusBox.textContent =
          "The security check could not be completed. Please refresh and try again.";
        statusBox.className = "form-status is-error";
      },
    });
  } catch (error) {
    console.error("Turnstile loading error:", error);
    state.failed = true;
    submitButton.disabled = true;
    field.classList.add("is-error");
    field.querySelector("[data-turnstile-container]").textContent =
      "The security check is temporarily unavailable. Please call 720-209-3130 or email hello@berthoudwifi.com.";
    statusBox.textContent = "The form security check could not load.";
    statusBox.className = "form-status is-error";
  }
}

function resetTurnstile(state, submitButton) {
  if (!state.enabled || state.widgetId === null || !window.turnstile) return;
  state.token = "";
  submitButton.disabled = true;
  window.turnstile.reset(state.widgetId);
}

forms.forEach((form) => {
  const statusBox = form.querySelector("[data-form-status]");
  const submitButton = form.querySelector('button[type="submit"]');

  if (!statusBox || !submitButton) return;

  const turnstileState = {
    enabled: false,
    failed: false,
    token: "",
    widgetId: null,
    ready: null,
  };

  turnstileState.ready = initializeTurnstile(
    form,
    submitButton,
    statusBox,
    turnstileState,
  );

  form.addEventListener("submit", async (event) => {
    event.preventDefault();
    await turnstileState.ready;

    if (turnstileState.failed) {
      statusBox.textContent =
        "The security check is unavailable. Please refresh the page or contact us directly.";
      statusBox.className = "form-status is-error";
      return;
    }

    if (turnstileState.enabled && !turnstileState.token) {
      statusBox.textContent = "Please complete the security check before sending.";
      statusBox.className = "form-status is-error";
      return;
    }

    statusBox.textContent = "Sending your request…";
    statusBox.className = "form-status is-sending";
    submitButton.disabled = true;

    const formData = new FormData(form);
    const payload = {};

    for (const [key, value] of formData.entries()) {
      if (key === "cf-turnstile-response") continue;
      if (key === "services") {
        if (!Array.isArray(payload.services)) payload.services = [];
        payload.services.push(value);
      } else {
        payload[key] = value;
      }
    }

    if (turnstileState.enabled) {
      payload.turnstileToken = turnstileState.token;
    }

    try {
      const response = await fetch("/api/contact", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(payload),
      });

      const result = await response.json();

      if (!response.ok || !result.ok) {
        throw new Error(result.message || "Unable to send your request.");
      }

      statusBox.textContent = result.message;
      statusBox.className = "form-status is-success";
      form.reset();
    } catch (error) {
      statusBox.textContent =
        error.message || "Unable to send your request. Please try again.";
      statusBox.className = "form-status is-error";
    } finally {
      if (turnstileState.enabled) {
        resetTurnstile(turnstileState, submitButton);
      } else {
        submitButton.disabled = false;
      }
    }
  });
});
