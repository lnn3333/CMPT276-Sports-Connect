from flask import Flask, jsonify
import requests

app = Flask(__name__)

@app.route('/nba-games')
def nba_games():
    # 这里的URL和参数需要根据您要获取的具体数据进行修改
    api_url = "https://api.sportradar.com/nba/{access_level}/v7/{language_code}/games/{year}/{month}/{day}/schedule.{format}"
    api_key = "wm4wf3terhkcn7rkz457jm89"  # 替换为您的NBA API密钥
    params = {
        "access_level": "trial",  # 或者 "production"，取决于您的密钥类型
        "language_code": "en",
        "year": "2022",
        "month": "01",
        "day": "22",
        "format": "json",
        "api_key": api_key
    }
    response = requests.get(api_url, params=params)
    if response.ok:
        return jsonify(response.json())
    else:
        return jsonify({"error": "Failed to fetch NBA data"}), response.status_code

if __name__ == "__main__":
    app.run(debug=True)
