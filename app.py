from flask import Flask, render_template, json, url_for, jsonify, Markup
from redis import Redis
import os
import csv
import folium
import make_data

app = Flask(__name__)
redis = Redis(host='localhost', port=6379)

#메인 페이지  
@app.route("/")
def home():
    redis.incr('hits')
    return render_template("index.html", data=redis.get('hits').decode("utf-8"))

#주말, 평일 정보 페이지
@app.route("/subway")
def subway():
    day = ['days', 'ends']
    return render_template("subway.html", day = day)

@app.route("/subwayDay/<day>")
def subwayDay(day = 'days'):
    label, time, score = make_data.ret_day(day)
    analysis = "json_url"
    return jsonify({'label': label, 'time': time[1:], 'score': score, 'analysis': analysis})

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
    label, time, score = make_data.ret_subway(up_down, line, time)
    analysis = "json_url"
    return jsonify({'label': label, 'time': time, 'score': score, 'analysis': analysis})

#카페 정보 페이지
@app.route("/cafe")
def cafe():
    cafe = ['스타벅스', '이디야', '투썸플레이스', '설빙', '핸즈커피', '엔제리너스', '파스쿠찌', '탐앤탐스']
    return render_template('cafe.html', cafe = cafe)

#카페 정보 맵 iframe
@app.route("/cafeMap/<query>")
def cafeMapQuery(query = '탐앤탐스'):
    print("tyest")
    return make_data.ret_map(query)
    
#히트맵 정보 페이지
@app.route("/heat")
def heat():
    line = ['total', 'line1', 'line2', 'line3']
    return render_template('heat.html', line = line)

#히트맵 정보
@app.route("/heatMap/<query>")
def heatMap(query = "line1"):
    station, heat, brand = make_data.make_heat(query)
    return jsonify({'station': station, 'heat': heat, 'brand': brand})

if __name__=="__main__":
    app.run(debug=True, host="0.0.0.0")
