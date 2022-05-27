// const [btnSend, btnCarry] = document.querySelectorAll(".add__buttons button");
// const [formCarry, formSend] = document.querySelectorAll(".add-post form");

// btnSend.addEventListener("click", function () {
//   document
//     .querySelectorAll(".add__buttons button")
//     .forEach((el) => el.classList.toggle("active"));
//   formSend.style.display = "flex";
//   formCarry.style.display = "none";
// });

// btnCarry.addEventListener("click", function () {
//   document
//     .querySelectorAll(".add__buttons button")
//     .forEach((el) => el.classList.toggle("active"));
//   formCarry.style.display = "flex";
//   formSend.style.display = "none";
// });

const overlay = document.querySelector(".overlay");
const btnAdd = document.querySelector(".btn-post");
const addModal = document.querySelector(".add-post");

overlay.addEventListener("click", function () {
  addModal.classList.add("hidden");
  overlay.classList.add("hidden");
});

btnAdd.addEventListener("click", function () {
  addModal.classList.remove("hidden");
  overlay.classList.remove("hidden");
});

document.querySelectorAll(".add-post form button").forEach((el) => {
  el.addEventListener("click", function () {
    if (validation.isValid(`.${el.parentElement.classList[0]}`)) {
      addModal.classList.add("hidden");
      overlay.classList.add("hidden");
    }
  });
});
