fetch("/nba-news").then(
    res => res.json()
).then(
    data => {
        const newsContainer = document.getElementById('news-container');
        let newsHtml = data.map(article => {
            return `<div class="article">
                        <h3>${article.title}</h3>
                        <p>${article.summary}</p>
                    </div>`;
        }).join('');
        newsContainer.innerHTML = newsHtml;
    }
).catch(
    error => console.error('Error:', error)
);
