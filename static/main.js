let btn = document.querySelector(".shazam-content");
let input = document.querySelector(".form-control");

btn.addEventListener("click", function () {
  if (btn.nextElementSibling.classList[2] == "d-none") {
    input.click()
  }
});

input.addEventListener("change", function () {
  btn.nextElementSibling.nextElementSibling.textContent = ""
  document.querySelector(".submit-form").click()
  btn.parentElement.style.gap = "3rem";
  btn.nextElementSibling.classList.remove("d-none");
  document.querySelector(".shazam-content").style.marginTop = "10%"
})