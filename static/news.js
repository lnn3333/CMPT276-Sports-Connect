document.addEventListener('DOMContentLoaded', function() {
    loadNews();
});

function loadNews() {
    fetch('/sports-news')
        .then(response => response.json())
        .then(data => {
            const newsContainer = document.getElementById('news-container');
            let newsHtml = data.map(article => {
                return `
                    <div class="news-article">
                        <h3>${article.title}</h3>
                        <p>${article.description}</p>
                        <a href="${article.url}" target="_blank">Read more</a>
                    </div>
                `;
            }).join('');
            newsContainer.innerHTML = newsHtml;
        })
        .catch(error => console.error('Error loading news:', error));
}
