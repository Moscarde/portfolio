// Menu Mobile Toggle
const menuMobile = document.querySelector(".menu-mobile");
const body = document.querySelector("body");

menuMobile.addEventListener("click", () => {
    menuMobile.classList.toggle("bi-x");
    menuMobile.classList.toggle("bi-list");
    body.classList.toggle("menu-nav-active");
});

// Close Menu on Link Click
const navItems = document.querySelectorAll(".nav-item");

navItems.forEach((item) => {
    item.addEventListener("click", () => {
        if (body.classList.contains("menu-nav-active")) {
            body.classList.remove("menu-nav-active");
            menuMobile.classList.replace("bi-x", "bi-list");
        }
    });
});

// Scroll Animations
const animatedItems = document.querySelectorAll("[data-anime]");

const handleScrollAnimations = () => {
    const windowTop = window.pageYOffset + window.innerHeight * 0.90;

    animatedItems.forEach((element) => {
        element.classList.toggle("animate", windowTop > element.offsetTop);
    });
};

handleScrollAnimations();
window.addEventListener("scroll", handleScrollAnimations);

// Spinner on Button Click
const btnEnviar = document.querySelector("#btn-send");
const btnEnviarSpinner = document.querySelector("#btn-send-spinner");

btnEnviar.addEventListener("click", () => {
    btnEnviarSpinner.style.display = "block";
    btnEnviar.style.display = "none";

    setTimeout(() => {
        const flashAlert = document.querySelector("#flash-alert");
        if (flashAlert) {
            flashAlert.style.display = "none";
        }
    }, 5000);
});

// Navbar Active Link on Scroll
const navLinks = document.querySelectorAll(".nav-link");

const setActiveLink = () => {
    const scrollPosition = window.pageYOffset + window.innerHeight / 2;

    navLinks.forEach(link => {
        const section = document.querySelector(link.getAttribute("href"));

        if (section) {
            const sectionTop = section.offsetTop;
            const sectionBottom = sectionTop + section.offsetHeight;

            if (scrollPosition >= sectionTop && scrollPosition < sectionBottom) {
                link.classList.add("active");
            } else {
                link.classList.remove("active");
            }
        }
    });
};

window.addEventListener("scroll", setActiveLink);
document.addEventListener("DOMContentLoaded", setActiveLink);

navLinks.forEach(link => {
    link.addEventListener("click", (e) => {
        e.preventDefault();
        const target = document.querySelector(link.getAttribute("href"));
        window.scrollTo({
            top: target.offsetTop - 50,
            behavior: "smooth"
        });
    });
});


