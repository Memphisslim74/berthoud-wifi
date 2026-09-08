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
    } else if (href === "/seo-services/" || href === "/seo-services") {
      trackEvent("seo_services_click", { link_url: href, link_text: link.textContent.trim() });
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

function closeNavigationFromLink(link) {
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
}

document.querySelectorAll(".nav-links a").forEach((link) => {
  link.addEventListener("click", () => closeNavigationFromLink(link));
});

function addSeoNavigationLink() {
  document.querySelectorAll(".nav-dropdown").forEach((dropdown) => {
    if (dropdown.querySelector('a[href="/seo-services/"]')) return;

    const link = document.createElement("a");
    link.href = "/seo-services/";
    link.textContent = "SEO & Organic Marketing";

    const viewAll = Array.from(dropdown.querySelectorAll("a")).find((item) =>
      /view all solutions/i.test(item.textContent || "")
    );
    if (viewAll) dropdown.insertBefore(link, viewAll);
    else dropdown.appendChild(link);

    link.addEventListener("click", () => closeNavigationFromLink(link));
  });
}

function addSeoServiceOptions() {
  document.querySelectorAll('select[name="services"]').forEach((select) => {
    const alreadyPresent = Array.from(select.options).some((option) =>
      /seo|organic marketing/i.test(option.textContent || "")
    );
    if (alreadyPresent) return;

    const option = document.createElement("option");
    option.value = "SEO & organic marketing";
    option.textContent = "SEO & organic marketing";

    const notSure = Array.from(select.options).find((item) => /not sure/i.test(item.textContent || ""));
    if (notSure) select.insertBefore(option, notSure);
    else select.appendChild(option);
  });
}

function loadSeoStyles() {
  if (document.querySelector('link[data-seo-services-css]')) return;
  const link = document.createElement("link");
  link.rel = "stylesheet";
  link.href = "/assets/css/seo-services.css?v=1";
  link.dataset.seoServicesCss = "";
  document.head.appendChild(link);
}

function createHomepageSeoCompanion() {
  const isHome = window.location.pathname === "/" || window.location.pathname === "/index.html";
  if (!isHome) return;

  const hero = document.querySelector(".home-hero");
  const container = hero?.querySelector(":scope > .container");
  const copy = hero?.querySelector(".home-hero-copy");
  if (!hero || !container || !copy || container.querySelector(".home-seo-companion")) return;

  loadSeoStyles();
  hero.classList.add("has-seo-companion");

  if (!copy.querySelector(".home-seo-pill")) {
    const pill = document.createElement("a");
    pill.className = "home-seo-pill";
    pill.href = "/seo-services/";
    pill.textContent = "Local SEO & organic marketing for Northern Colorado businesses";
    const actions = copy.querySelector(".hero-actions");
    if (actions) actions.insertAdjacentElement("afterend", pill);
    else copy.appendChild(pill);
  }

  const companion = document.createElement("aside");
  companion.className = "home-seo-companion";
  companion.setAttribute("aria-label", "SEO and organic marketing preview");
  companion.innerHTML = `
    <div class="seo-tour-wrap" data-seo-tour>
      <span class="seo-tour-label">New: SEO & organic growth</span>
      <div class="seo-tour">
        <div class="seo-tour-stage">
          <article class="seo-tour-card" data-seo-slide>
            <div class="seo-screen-head"><div><span class="seo-screen-kicker">Search Visibility</span><strong>See what Google already knows about your site</strong></div><span class="seo-screen-step">01</span></div>
            <div class="seo-screen-body"><p class="seo-screen-copy">Technical SEO, Search Console, indexing, page structure, and real search opportunities.</p><div class="seo-metric-grid"><div class="seo-metric"><span>Visibility</span><strong>+38%</strong><em>Trend</em></div><div class="seo-metric"><span>Health</span><strong>92</strong><em>Score</em></div><div class="seo-metric"><span>Leads</span><strong>+17%</strong><em>Organic</em></div></div><div class="seo-panel"><div class="seo-panel-title"><span>Organic growth</span><span>90 days</span></div><div class="seo-chart" aria-hidden="true"><i style="height:22%"></i><i style="height:28%"></i><i style="height:34%"></i><i style="height:43%"></i><i style="height:52%"></i><i style="height:64%"></i><i style="height:77%"></i><i style="height:91%"></i></div></div></div>
          </article>
          <article class="seo-tour-card" data-seo-slide>
            <div class="seo-screen-head"><div><span class="seo-screen-kicker">Local SEO</span><strong>Compete where your customers are searching</strong></div><span class="seo-screen-step">02</span></div>
            <div class="seo-screen-body"><p class="seo-screen-copy">Google Business Profile, service-area relevance, local pages, reviews, and search intent.</p><div class="seo-locations"><div class="seo-location"><strong>Berthoud</strong><span>Strong local relevance</span><div class="seo-progress"><i style="width:92%"></i></div></div><div class="seo-location"><strong>Loveland</strong><span>Growth opportunity</span><div class="seo-progress"><i style="width:72%"></i></div></div><div class="seo-location"><strong>Fort Collins</strong><span>Growth opportunity</span><div class="seo-progress"><i style="width:61%"></i></div></div><div class="seo-location"><strong>Longmont</strong><span>Growth opportunity</span><div class="seo-progress"><i style="width:55%"></i></div></div></div></div>
          </article>
          <article class="seo-tour-card" data-seo-slide>
            <div class="seo-screen-head"><div><span class="seo-screen-kicker">Organic Content</span><strong>Build pages that answer real buying questions</strong></div><span class="seo-screen-step">03</span></div>
            <div class="seo-screen-body"><p class="seo-screen-copy">Service pages, comparisons, guides, and articles built around the searches closest to revenue.</p><div class="seo-panel"><div class="seo-panel-title"><span>Content roadmap</span><span>Intent</span></div><div class="seo-content-row"><div><strong>Primary service page</strong><span>Commercial</span></div><span class="seo-status">Optimize</span></div><div class="seo-content-row"><div><strong>Local landing page</strong><span>Local</span></div><span class="seo-status">Build</span></div><div class="seo-content-row"><div><strong>Buyer comparison</strong><span>Decision</span></div><span class="seo-status">Publish</span></div></div></div>
          </article>
        </div>
        <div class="seo-tour-controls"><button class="seo-tour-btn" data-seo-prev type="button" aria-label="Previous SEO preview">‹</button><div class="seo-tour-dots" data-seo-dots></div><span class="seo-tour-status" data-seo-status aria-live="polite"></span><button class="seo-tour-btn" data-seo-next type="button" aria-label="Next SEO preview">›</button></div>
      </div>
      <a class="home-seo-companion-cta" href="/seo-services/">Explore SEO & organic marketing →</a>
    </div>`;
  container.appendChild(companion);
}

function initSeoTour(root) {
  if (!root || root.dataset.seoTourReady === "true") return;
  const slides = Array.from(root.querySelectorAll("[data-seo-slide]"));
  const prev = root.querySelector("[data-seo-prev]");
  const next = root.querySelector("[data-seo-next]");
  const dots = root.querySelector("[data-seo-dots]");
  const status = root.querySelector("[data-seo-status]");
  if (!slides.length || !prev || !next) return;

  root.dataset.seoTourReady = "true";
  let index = 0;

  const dotButtons = slides.map((_, slideIndex) => {
    const dot = document.createElement("button");
    dot.type = "button";
    dot.className = "seo-tour-dot";
    dot.setAttribute("aria-label", `Show SEO process screen ${slideIndex + 1}`);
    dot.addEventListener("click", () => {
      index = slideIndex;
      render();
    });
    dots?.appendChild(dot);
    return dot;
  });

  function cyclicDistance(from, to) {
    return (to - from + slides.length) % slides.length;
  }

  function render() {
    slides.forEach((slide, slideIndex) => {
      slide.classList.remove("is-active", "is-next-1", "is-next-2", "is-prev", "is-hidden");
      const distance = cyclicDistance(index, slideIndex);
      if (distance === 0) slide.classList.add("is-active");
      else if (distance === 1) slide.classList.add("is-next-1");
      else if (distance === 2) slide.classList.add("is-next-2");
      else if (distance === slides.length - 1) slide.classList.add("is-prev");
      else slide.classList.add("is-hidden");
      slide.setAttribute("aria-hidden", String(distance !== 0));
    });

    dotButtons.forEach((dot, dotIndex) => {
      dot.classList.toggle("is-active", dotIndex === index);
      dot.setAttribute("aria-current", dotIndex === index ? "true" : "false");
    });

    if (status) status.textContent = `${index + 1} of ${slides.length}`;
  }

  prev.addEventListener("click", () => {
    index = (index - 1 + slides.length) % slides.length;
    render();
  });
  next.addEventListener("click", () => {
    index = (index + 1) % slides.length;
    render();
  });

  root.addEventListener("keydown", (event) => {
    if (event.target.closest("input,textarea,select")) return;
    if (event.key === "ArrowLeft") {
      event.preventDefault();
      prev.click();
    }
    if (event.key === "ArrowRight") {
      event.preventDefault();
      next.click();
    }
  });

  let pointerStartX = null;
  root.addEventListener("pointerdown", (event) => {
    if (event.pointerType === "mouse") return;
    pointerStartX = event.clientX;
  });
  root.addEventListener("pointerup", (event) => {
    if (pointerStartX === null) return;
    const delta = event.clientX - pointerStartX;
    pointerStartX = null;
    if (Math.abs(delta) < 45) return;
    if (delta < 0) next.click();
    else prev.click();
  });

  render();
}

addSeoNavigationLink();
addSeoServiceOptions();
createHomepageSeoCompanion();
document.querySelectorAll("[data-seo-tour]").forEach(initSeoTour);
