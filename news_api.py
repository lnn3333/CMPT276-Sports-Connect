import http.client
import json

from datetime import datetime
from flask import url_for
import pytz

conn = http.client.HTTPSConnection("nba-latest-news.p.rapidapi.com")

headers = {
    'X-RapidAPI-Key': "c3c71e434emsh40b6a9607764354p1c4421jsn9494467b16fc",
    'X-RapidAPI-Host': "nba-latest-news.p.rapidapi.com"
}

conn.request("GET", "/articles", headers=headers)

res = conn.getresponse()
data = res.read()

decodedData=data.decode("utf-8")
conn.close()

newsJSON = json.loads(decodedData)

#store JSON data
with open ("newsData.json","w") as file:
    json.dump(newsJSON,file,indent=4)

def readNews():
    with open("newsData.json","r") as reading:
        news = json.load(reading)
    return news

newsImageMap = {
    "slam":"/newsArticleImages/slam.png",
    "espn":"/newsArticleImages/espn.png",
    "bleacher_report":"/newsArticleImages/br.png",
    "nba":"/newsArticleImages/nba.png",
}

newsArticles = set()

def getNews(news):
    for article in news:
        name = article['title']
        link = article['url']
        source = article['source']
        imagePath = url_for('static',filename=newsImageMap.get(source,newsImageMap["nba"]))
        newsArticles.add((name,link,source,imagePath))
    return newsArticles
        