// Keep every page on the same visual release, including after an edge-cache hit.
document
  .querySelectorAll('link[rel="stylesheet"][href^="/assets/css/brand-refresh.css"]')
  .forEach((link) => {
    link.href = "/assets/css/brand-refresh.css?v=21";
  });

function trackEvent(name, parameters = {}) {
  if (typeof window.gtag !== "function") return;
  window.gtag("event", name, {
    page_location: window.location.href,
    ...parameters,
  });
}

document.querySelectorAll("[data-year]").forEach((element) => {
  element.textContent = new Date().getFullYear();
});

document.querySelectorAll(".menu-btn").forEach((button) => {
  button.addEventListener("click", () => {
    const nav = button.parentElement?.querySelector(".nav-links");
    if (!nav) return;

    const open = nav.classList.toggle("is-open");
    nav.classList.toggle("open", open);
    button.setAttribute("aria-expanded", String(open));
  });
});

document.querySelectorAll(".nav-dropdown-toggle").forEach((button) => {
  button.addEventListener("click", (event) => {
    event.stopPropagation();
    const item = button.closest(".nav-item");
    if (!item) return;

    document.querySelectorAll(".nav-item.is-open").forEach((openItem) => {
      if (openItem !== item) {
        openItem.classList.remove("is-open");
        openItem
          .querySelector(".nav-dropdown-toggle")
          ?.setAttribute("aria-expanded", "false");
      }
    });

    const open = item.classList.toggle("is-open");
    button.setAttribute("aria-expanded", String(open));
  });
});

document.addEventListener("click", (event) => {
  const link = event.target.closest("a[href]");
  if (link) {
    const href = link.getAttribute("href") || "";
    if (href.startsWith("tel:")) {
      trackEvent("phone_click", { link_url: href });
    } else if (href.startsWith("mailto:")) {
      trackEvent("email_click", { link_url: href });
    } else if (
      (href === "/contact" || href === "/contact/" || href.endsWith("/contact.html")) &&
      link.classList.contains("btn")
    ) {
      trackEvent("quote_cta_click", { link_url: href, link_text: link.textContent.trim() });
    }
  }

  if (!event.target.closest(".nav-item")) {
    document.querySelectorAll(".nav-item.is-open").forEach((item) => {
      item.classList.remove("is-open");
      item
        .querySelector(".nav-dropdown-toggle")
        ?.setAttribute("aria-expanded", "false");
    });
  }
});

document.querySelectorAll(".nav-links a").forEach((link) => {
  link.addEventListener("click", () => {
    const nav = link.closest(".nav-links");
    const menuButton = nav?.parentElement?.querySelector(".menu-btn");

    nav?.classList.remove("is-open", "open");
    menuButton?.setAttribute("aria-expanded", "false");

    document.querySelectorAll(".nav-item.is-open").forEach((item) => {
      item.classList.remove("is-open");
      item
        .querySelector(".nav-dropdown-toggle")
        ?.setAttribute("aria-expanded", "false");
    });
  });
});
