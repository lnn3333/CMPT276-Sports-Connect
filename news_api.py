# -*- coding: utf-8 -*-
from flask import Flask, jsonify
import requests

app = Flask(__name__)

@app.route('/nba-articles')
def get_nba_articles():
    url = "https://nba-latest-news.p.rapidapi.com/articles"
    headers = {
        'X-RapidAPI-Key': '您的RapidAPI密钥',
        'X-RapidAPI-Host': 'nba-latest-news.p.rapidapi.com'
    }
    response = requests.get(url, headers=headers)
    if response.ok:
        return jsonify(response.json())
    else:
        return jsonify({"error": "请求失败"}), response.status_code

if __name__ == "__main__":
    app.run(debug=True)
