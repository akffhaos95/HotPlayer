from flask import Flask, render_template, json, url_for, jsonify, Markup
import os
import csv
import folium
from random import sample
#from redis import Redis

app = Flask(__name__)
#redis = Redis(host='redis', port=6379)

#메인 페이지  
@app.route("/")
def home():
    #redis.incr('hits')
    return render_template("index.html")

#지하철 정보 페이지
@app.route("/list")
def list():
    up_down = ['up', 'down']
    list = ['total', 'one', 'two', 'thr']
    time = ['아침', '오전', '점심', '오후', '저녁', '밤']
    return render_template("list.html", up_down = up_down, list = list, time = time)

#지하철 정보
@app.route("/subwayTime/<up_down>/<line>/<time>")
def subwayTime(up_down = 'up', line = 'total', time = '아침'):
    SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
    json_url = os.path.join(SITE_ROOT, 'static', 'data/'+up_down+'_'+line+'_'+time+'_head.json')
    data = json.load(open(json_url))
    label, time, score = [], [], []
    lab = data['schema']['fields']
    for i in lab:
        time.append(i['name'])
    for i in data['data']:
        label.append(i['역명'])
        tmp = []
        for j in range(1, len(lab)):
            tmp.append(i[time[j]])
        score.append(tmp)
    analysis = json_url
    return jsonify({'label': label, 'time': time, 'score': score, 'analysis': analysis})

#카페 정보 페이지
@app.route("/cafe")
def cafe():
    return render_template('cafescore.html')

@app.route("/cafeMap/<station>/<cafe>")
def cafeMap(station = '', cafe = ''):
    SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
    csv_url = os.path.join(SITE_ROOT, 'static', 'data/cafe.csv')
    start_coords = (35.8394, 128.757)
    folium_map = folium.Map(location=start_coords, zoom_start=14)
    with open(csv_url, 'r', encoding='utf-8') as f:
        cafe_list = csv.reader(f)
        for i in cafe_list:
            if i[4] == cafe:
                folium.Marker([i[3],i[2]], popup=i[1], icon=folium.Icon(color='orange')).add_to(folium_map)
    return folium_map._repr_html_()
    
if __name__=="__main__":
    app.run(debug=True, host="0.0.0.0")
