const searchBarArea = document.getElementById("searchBarArea")
const postsArea = document.getElementById("postsArea");
const inputBox = document.getElementById("searchInput")

inputBox.onkeyup = () => {
  const query = inputBox.value.toLowerCase();

  if (query === ""){
    for (let i = 0; i < postsArea.children.length; i++) {
      postsArea.children[i].style.display = "block";
    }
  }
  else{
    for (let i = 0; i < postsArea.children.length; i++) {
      const curBlogTitle = postsArea.children[i].children[0].children[0];

      if (curBlogTitle.textContent.toLowerCase().includes(query) === false){
        curBlogTitle.parentElement.parentElement.style.display = "none";
      }
      else{
        curBlogTitle.parentElement.parentElement.style.display = "block";
      }
    }
  }
}


//elmnt.textContent