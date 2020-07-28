from scipy.spatial import distance
from flask import Flask, json
import os
import folium
import numpy as np
import pandas as pd

def ret_subway(up_down, line, time):
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
    return label, time, score

def ret_day(day):
    SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
    json_url = os.path.join(SITE_ROOT, 'static', 'data/'+day+'_head.json')
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
    print(label)
    print(time)
    print(score)
    return label, time, score

def ret_map(query):
    SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
    subway_url = os.path.join(SITE_ROOT, 'static', 'data/station.csv')    
    station_df = pd.read_csv(subway_url, index_col=0)

    cafe_url = os.path.join(SITE_ROOT, 'static', 'data/cafe.csv')    
    cafe_df = pd.read_csv(cafe_url, index_col=0)
    cafe_df.columns = ["name", "x", "y", 'brand']

    cafe_df = cafe_df[cafe_df['brand'] == query]

    sub_star = {'station': '','star':[]}
    sub_star_list, x1, y1 = [], [], []
    color = [['mediumturquoise', 'mediumpurple', 'crimson'],
            ['blue', 'purple', 'red'],
            ['steelblue', 'indigo', 'crimson']]

    for i in range(len(station_df)):
        sub_star['station']=[station_df['name'][i], station_df['y'][i], station_df['x'][i]]
        y, x = sub_star['station'][1], sub_star['station'][2]

        for _, row in cafe_df.iterrows():
            if (round(distance.euclidean((x, y), (row['x'], row['y'])),5)*1000) < 10:
                sub_star['star'].append([row['name'],row['y'],row['x']])
        sub_star_list.append({'station':sub_star['station'],'star':sub_star['star']})
        sub_star['star']=[]
        
    dic = {'station': '','star':[]}
    sg = [[], [], []]

    for i in range(len(sub_star_list)):
        dic['station']=sub_star_list[i]['station']
        dic['star'].append(sub_star_list[i]['star'])        
        if len(sub_star_list[i]['star']) >= 6:
            sg[2].append(dic)
        elif len(sub_star_list[i]['star']) >= 4:
            sg[1].append(dic)
        elif len(sub_star_list[i]['star']) >= 1:
            sg[0].append(dic)
        dic={'station': '','star':[]}

    m = folium.Map(location=[station_df['y'][0], station_df['x'][0]], zoom_start=12)

    for k in range(len(sg)):
        for i in range(len(sg[k])):
            folium.Circle([sg[k][i]['station'][1], sg[k][i]['station'][2]], radius=1000,
                        popup=sg[k][i]['station'][0], color=color[0][k],fill_color=color[2][k]).add_to(m)
            for j in range(len(sg[k][i]['star'][0])):
                x = sg[k][i]['star'][0][j][2]
                y = sg[k][i]['star'][0][j][1]
                name = str(sg[k][i]['star'][0][j][0])
                folium.Marker([y,x],popup=name, icon=folium.Icon(color=color[1][k],icon="flag")).add_to(m)
    return m._repr_html_()

def ret_heat(query):
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
    return station, heat, brand