let activeNavItem = document.getElementById("homeLink");
let activePage = document.getElementById("homePage");

function switchActive(currentLink, currentPage) {
  activeNavItem.classList.remove('active');
  activeNavItem = document.getElementById(currentLink);
  activeNavItem.classList.add('active');
  activePage.style.display = "none";
  activePage = document.getElementById(currentPage);
  activePage.style.display = "flex";
}