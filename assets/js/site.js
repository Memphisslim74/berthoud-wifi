
const menuButton = document.querySelector('.menu-btn');
const navLinks = document.querySelector('.nav-links');
if (menuButton && navLinks) {
  menuButton.addEventListener('click', () => navLinks.classList.toggle('open'));
}
document.querySelectorAll('[data-year]').forEach(el => {
  el.textContent = new Date().getFullYear();
});

document.querySelectorAll(".menu-btn").forEach((button) => {
  button.addEventListener("click", () => {
    const nav = button.parentElement?.querySelector(".nav-links");
    if (!nav) return;
    const open = nav.classList.toggle("is-open");
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
        openItem.querySelector(".nav-dropdown-toggle")?.setAttribute("aria-expanded", "false");
      }
    });

    const open = item.classList.toggle("is-open");
    button.setAttribute("aria-expanded", String(open));
  });
});

document.addEventListener("click", (event) => {
  if (!event.target.closest(".nav-item")) {
    document.querySelectorAll(".nav-item.is-open").forEach((item) => {
      item.classList.remove("is-open");
      item.querySelector(".nav-dropdown-toggle")?.setAttribute("aria-expanded", "false");
    });
  }
});

document.querySelectorAll(".nav-links a").forEach((link) => {
  link.addEventListener("click", () => {
    const nav = link.closest(".nav-links");
    const menuButton = nav?.parentElement?.querySelector(".menu-btn");

    nav?.classList.remove("is-open");
    menuButton?.setAttribute("aria-expanded", "false");

    document.querySelectorAll(".nav-item.is-open").forEach((item) => {
      item.classList.remove("is-open");
      item.querySelector(".nav-dropdown-toggle")?.setAttribute("aria-expanded", "false");
    });
  });
});
