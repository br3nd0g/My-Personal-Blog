let postsObj;

jsonString = jsonFromFlask;
const postArea = document.getElementById("postsArea");
postsObj = JSON.parse(jsonString)

for(let post of postsObj.posts) {

  var htmlString = `
  <div class="postBox">
    <div class="postHeader">
      <h1 class="blogTitle">${post.title}</h1>
      <h1 class="blogDate">${post.date}</h1>
    </div>
    <br>
    <p class="blogText">${post.text}</p>
  </div>`;
  
  postArea.insertAdjacentHTML('afterbegin', htmlString)
}