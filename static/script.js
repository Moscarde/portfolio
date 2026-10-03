// Menu Mobile Toggle
const menuMobile = document.querySelector(".menu-mobile");
const body = document.querySelector("body");

const setMenu = (open) => {
    body.classList.toggle("menu-nav-active", open);
    menuMobile.setAttribute("aria-expanded", String(open));
    menuMobile.setAttribute("aria-label", open ? "Fechar menu" : "Abrir menu");
};

menuMobile.addEventListener("click", () => {
    setMenu(!body.classList.contains("menu-nav-active"));
});

// Close Menu on Link Click
document.querySelectorAll(".nav-link").forEach((link) => {
    link.addEventListener("click", () => setMenu(false));
});

// Scroll Animations
const animatedItems = document.querySelectorAll("[data-anime]");

if ("IntersectionObserver" in window) {
    const observer = new IntersectionObserver((entries) => {
        entries.forEach((entry) => {
            if (entry.isIntersecting) {
                entry.target.classList.add("animate");
                observer.unobserve(entry.target);
            }
        });
    }, { rootMargin: "0px 0px -10% 0px" });

    animatedItems.forEach((item) => observer.observe(item));
} else {
    animatedItems.forEach((item) => item.classList.add("animate"));
}

// Spinner on Form Submit
const form = document.querySelector(".contact-form");
const btnEnviar = document.querySelector("#btn-send");
const btnEnviarSpinner = document.querySelector("#btn-send-spinner");

form.addEventListener("submit", () => {
    btnEnviar.style.display = "none";
    btnEnviarSpinner.style.display = "inline-flex";
});

// Flash Alert
const flashAlert = document.querySelector("#flash-alert");

if (flashAlert) {
    flashAlert.querySelector(".flash-close").addEventListener("click", () => flashAlert.remove());
    setTimeout(() => flashAlert.remove(), 5000);
}

// Navbar Active Link on Scroll
const navLinks = document.querySelectorAll(".nav-link");

const setActiveLink = () => {
    const scrollPosition = window.scrollY + window.innerHeight / 3;

    navLinks.forEach((link) => {
        const section = document.querySelector(link.getAttribute("href"));
        if (!section) return;

        const sectionTop = section.offsetTop;
        const sectionBottom = sectionTop + section.offsetHeight;
        link.classList.toggle("active", scrollPosition >= sectionTop && scrollPosition < sectionBottom);
    });
};

window.addEventListener("scroll", setActiveLink, { passive: true });
document.addEventListener("DOMContentLoaded", setActiveLink);
