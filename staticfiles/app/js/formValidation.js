validation.rules["required"] = {
  message: "Boş qoyula bilməz",
  method: (el) => {
    return el.value !== "";
  },
};

validation.rules["email"] = {
  message: "Yanlış poçt ünvanı",
  method: (el) => {
    return (
      el.value === "" ||
      /^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/.test(
        el.value
      )
    );
  },
};

validation.rules["repeat"] = {
  message: "Şifrə və təkrar şifrə eyni olmalıdır",
  method: (el) => {
    return (
      el.value === "" || el.value === document.querySelector("#password").value
    );
  },
};

validation.rules["phone"] = {
  message: "Yanlış əlaqə nömrəsi",
  method: (el) => {
    return (
      el.value === "" ||
      /^[+]*[(]{0,1}[0-9]{1,3}[)]{0,1}[-\s\./0-9]*$/g.test(el.value)
    );
  },
};

validation.rules["password"] = {
  message:
    "Şifrə 8 simvol uzunluğunda və ən az 1 rəqəm, 1 böyük hərf, 1 kiçik hərf, 1 xüsusi simvoldan ibarət olmalıdır",
  method: (el) => {
    return (
      el.value === "" ||
      /^(?!.*\s)(?=.*[A-Z])(?=.*[a-z])(?=.*[0-9])(?=.*[~`!@#$%^&*()--+={}[\]|\\:;"'<>,.?/_₹]).{10,16}$/.test(
        el.value
      )
    );
  },
};

validation.init(".sign-up");
validation.init(".add__carrier");
validation.init(".add__sender");

const buttonSignUp = document.querySelector(".sign-up button");
if (buttonSignUp) {
  buttonSignUp.style.pointerEvents = "none";
}
const inputs = document.querySelectorAll(".sign-up input");

inputs?.forEach((el) => {
  el.addEventListener("input", function () {
    if (validation.isValid(".sign-up")) {
      buttonSignUp.style.pointerEvents = "all";
    }
  });
});

// buttonSignUp?.addEventListener("click", function (e) {
//   e.preventDefault();
//   if (validation.isValid(".sign-up")) {
//     let data = {};
//     document
//       .querySelectorAll(".sign-up input")
//       .forEach((el) => (data[el.id] = el.value));
//     document
//       .querySelectorAll(".sign-up input")
//       .forEach((el) => (el.value = ""));
//     console.log(data);
//   }
// });
