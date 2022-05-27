const btnSignIn = document.querySelector("#sign-in-btn");
const btnSignUp = document.querySelector("#sign-up-btn");
const main = document.querySelector("main");

btnSignUp.addEventListener("click", () => {
  main.classList.add("sign-up-mode");
});

btnSignIn.addEventListener("click", () => {
  main.classList.remove("sign-up-mode");
});
