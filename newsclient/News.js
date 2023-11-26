import React, { useState, useEffect } from 'react';

function News() {
  const [data, setData] = useState([{}]);

  useEffect(() => {
    fetch("/nba-articles").then(
      res => res.json()
    ).then(
      data => {
        setData(data);
        console.log(data);
      }
    );
  }, []);

  return (
    <div>
      {data.map((article, index) => (
        <div key={index} className="article">
          <h3>{article.title}</h3>
          <p>{article.summary}</p>
          {/* 如果有更多字段，也可以在这里显示 */}
        </div>
      ))}
    </div>
  );
}

export default News;
