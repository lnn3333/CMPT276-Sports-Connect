// menu bar
const elemToggleFunc = function (elem) { elem.classList.toggle("active"); }
//navbar

const navbar = document.querySelector("[data-nav]");
const navOpenBtn = document.querySelector("[data-nav-open-btn]");
const navCloseBtn = document.querySelector("[data-nav-close-btn]");
const overlay = document.querySelector("[data-overlay]");

const navElemArr = [navOpenBtn, navCloseBtn, overlay];

for (let i = 0; i < navElemArr.length; i++) {

  navElemArr[i].addEventListener("click", function () {
    elemToggleFunc(navbar);
    elemToggleFunc(overlay);
    elemToggleFunc(document.body);
  })

}

// Live score
// JavaScript code to simulate live score updates


//js for news
document.addEventListener('DOMContentLoaded', function() {
  fetch('/nba-news')
      .then(response => response.json())
      .then(data => {
          const newsContainer = document.getElementById('news-container');
          let newsHtml = data.map(article => {
              return `
                  <div class="article">
                      <h3>${article.title}</h3>
                      <p>${article.summary}</p>
                      <!-- 其他内容 -->
                  </div>
              `;
          }).join('');
          newsContainer.innerHTML = newsHtml;
      })
      .catch(error => console.error('Error:', error));
});

