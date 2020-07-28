import pandas as pd
import json
import os

SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
heat_url = os.path.join(SITE_ROOT, 'static', 'data/heat_line1.json')   
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
    brand.append(test[0])
    heat.append(test[1:])