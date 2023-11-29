# -*- coding: utf-8 -*-
from flask import Flask, jsonify
import requests

app = Flask(__name__)

@app.route('/nba-articles')
def get_nba_articles():
    url = "https://nba-latest-news.p.rapidapi.com/articles"
    headers = {
        'X-RapidAPI-Key': 'c3c71e434emsh40b6a9607764354p1c4421jsn9494467b16fc',
        'X-RapidAPI-Host': 'nba-latest-news.p.rapidapi.com'
    }
    response = requests.get(url, headers=headers)
    if response.ok:
        return jsonify(response.json())
    else:
        return jsonify({"error": "请求失败"}), response.status_code

if __name__ == "__main__":
    app.run(debug=True)
