window.onscroll = function () {
  scrollFunction();
};

function scrollFunction() {
  if (document.body.scrollTop > 10 || document.documentElement.scrollTop > 10) {
    document.getElementById("navbar").classList.remove("navbar-transparent");
    document.getElementById("navbar").classList.add("navbar-colored");
  } else {
    document.getElementById("navbar").classList.remove("navbar-colored");
    document.getElementById("navbar").classList.add("navbar-transparent");
  }
}

//acvtive Navbar
var currentUrl = window.location.pathname;

window.addEventListener("load", function () {
  var navbarItems = document.querySelectorAll(".navbar-nav .nav-item");

  navbarItems.forEach(function (link) {
    if (link.getAttribute("href") === currentUrl) {
      // Nếu URL trùng khớp, thêm lớp active vào liên kết đó
      link.classList.add("active");
      link.classList.remove("disabled");
    } else {
      // Nếu không, loại bỏ lớp active nếu có
      link.classList.remove("active");
      link.classList.add("disabled");
    }
  });
});

fetch("/component/navbar.html")
  .then((response) => response.text())
  .then((data) => (document.getElementById("nav").innerHTML = data));
