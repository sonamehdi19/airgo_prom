const hamburger = document.querySelector(".nav__hamburger");
const navList = document.querySelector(".nav__list");

hamburger.addEventListener("click", function () {
  navList.classList.toggle("nav--active");
});
