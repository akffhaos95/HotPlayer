sub_star = {'station': '','star':[]}
sub_star_list=[]

for i in range(len(station_df)):
    sub_star['station']=[station_df['name'][i], station_df['y'][i],station_df['x'][i]]
    y, x = sub_star['station'][1], sub_star['station'][2]
    
    query="스타벅스"
    url = "https://dapi.kakao.com/v2/local/search/keyword.json?y={}&x={}&radius=1000&query={}".format(y, x, query)
    headers = {'Authorization' : 'KakaoAK {0}'.format(key)}
    res = requests.get(url, headers=headers).json()
    for j in res['documents']:
        if j['place_name'] not in name:
            sub_star['star'].append([j['place_name'], j['y'], j['x']])
    sub_star_list.append({'station':sub_star['station'],'star':sub_star['star']})
    sub_star['star']=[]

dic = {'station' : '','star' : []}
color = [['mediumturquoise', 'mediumpurple', 'crimson'],
        ['blue', 'purple', 'red'],
        ['steelblue', 'indigo', 'crimson']]
sg = [[],[],[]]

for i in range(0, len(sub_star_list)):
    dic['station'] = sub_star_list[i]['station']
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
    for i in range(0,len(sg[k])):
        folium.Circle([sg[k][i]['station'][1], sg[k][i]['station'][2]], radius=1000,
                       popup=sg[k][i]['station'][0], color=color[0][k],fill_color=color[2][k]).add_to(m)
        #marker
        for j in range(len(sg[k][i]['star'][0])):
            x = sg[k][i]['star'][0][j][2]
            y = sg[k][i]['star'][0][j][1]
            name = str(sg[k][i]['star'][0][j][0])
            folium.Marker([y,x],popup=name, icon=folium.Icon(color=color[1][k],icon="flag")).add_to(m)

m.save('index.html')
m
#위도 경도
#6371*acos(cos(radians(lat좌표값))*cos(radians(slLat))*cos(radians(slLng)-radians(lng좌표값))+sin(radians(lat좌표값))*sin(radians(slLat)))
# from scipy.spatial import distance

# a = round(distance.euclidean((126.97843, 37.56668), (127.02758, 37.49794)),5)
# print(a*100)
