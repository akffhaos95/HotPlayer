from flask import Flask, render_template, json, url_for, jsonify, Markup
from random import sample
from redis import Redis
import os
import csv
import folium
import make_map

app = Flask(__name__)
redis = Redis(host='localhost', port=6379)

#메인 페이지  
@app.route("/")
def home():
    redis.incr('hits')
    return render_template("index.html", data=redis.get('hits').decode("utf-8"))

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

@app.route("/cafeMap/<query>")
def cafeMapQuery(query = '탐앤탐스'):
    return make_map.ret_map(query)
    
@app.route("/heat")
def head():
    return render_template('heat.html')

@app.route("/heatMap/<query>")
def heatMap(query = "line1"):
    SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
    heat_url = os.path.join(SITE_ROOT, 'static', 'data/heat_'+query+'.json')   
    data = json.load(open(heat_url))

    station, heat, brand = [], [], []
    lab = data['schema']['fields']
    for i in lab:
        station.append(i['name'])
    station = station[1:]

    for i in data['data']:
        tmp = []
        for _, k in i.items():
            tmp.append(k)
        brand.append(tmp[0])
        heat.append(tmp[1:])
    return jsonify({'station': station, 'heat': heat, 'brand': brand})

if __name__=="__main__":
    app.run(debug=True, host="0.0.0.0")
