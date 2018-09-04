import requests
import json
import helper
from flask import Flask, render_template
app = Flask(__name__)
    
@app.route("/")
def getHome():
    url = ('https://newsapi.org/v2/top-headlines?country=id&apiKey=8ac2f8a40a47434b90fe31f15fd35ee0')
    response = requests.get(url)
    raw = json.dumps(response.json())
    datas = json.loads(raw)
    return render_template('index.html',posts = datas["articles"],convert_time=helper.format_datetime)

if __name__ == '__main__':
    app.run(debug=True)