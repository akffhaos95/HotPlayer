sub_star, sub_star_lists, key = {'station': '','star':[]}, [], ""

for i in range(0,len(station_df)):
    sub_star['station']=[station_df['name'][i],station_df['y'][i],station_df['x'][i]]
    y=sub_star['station'][1]
    x=sub_star['station'][2]
    
    query="스타벅스"
    url = "https://dapi.kakao.com/v2/local/search/keyword.json?y={}&x={}&radius=1000&query={}".format(y,x,query)
    headers = {'Authorization': 'KakaoAK {0}'.format(key)}
    res = requests.get(url, headers=headers).json()
    for j in res['documents']:
        if j['place_name'] not in name:
            sub_star['star'].append([j['place_name'],j['y'],j['x']])
    sub_star_list.append({'station':sub_star['station'],'star':sub_star['star']})
    sub_star['star']=[]

#그룹 나누기 (6개 이상/4개이상/1개이상)
dic = {'station': '','star':[]}
firstg = []
secondg = []
thirdg = []

for i in range(0,len(sub_star_list)):
    if len(sub_star_list[i]['star']) >= 6:
        dic['station']=sub_star_list[i]['station']
        dic['star'].append(sub_star_list[i]['star'])
        firstg.append(dic)
        dic={'station': '','star':[]}
    elif len(sub_star_list[i]['star']) >= 4:
        dic['station']=sub_star_list[i]['station']
        dic['star'].append(sub_star_list[i]['star'])
        secondg.append(dic)
        dic={'station': '','star':[]}
    elif len(sub_star_list[i]['star']) >= 1:
        dic['station']=sub_star_list[i]['station']
        dic['star'].append(sub_star_list[i]['star'])
        thirdg.append(dic)
        dic={'station': '','star':[]}

#Circle - station 
#그룹별 지도 써클 및 마커 표시

#첫번째 그룹
color = [['mediumturquoise', 'mediumpurple', 'crimson'],
        ['blue', 'purple', 'red'],
        ['']

for j in range(3):
    m = folium.Map(location=[station_df['y'][0], station_df['x'][0]], zoom_start=12)
    for i in range(0,len(thirdg)):
        folium.Circle([thirdg[i]['station'][1], thirdg[i]['station'][2]], radius=1000, 
                            popup = thirdg[i]['station'][0], color = color[0][i],
                            fill_color = 'steelblue').add_to(m)
        #marker
        for j in range(len(thirdg[i]['star'][0])):
            x = thirdg[i]['star'][0][j][2]
            y = thirdg[i]['star'][0][j][1]
            name = str(thirdg[i]['star'][0][j][0])
            folium.Marker([y,x],popup=name, icon=folium.Icon(color = color2[1][i], icon="flag")).add_to(m)

    
for i in range(0,len(secondg)):
    folium.Circle([secondg[i]['station'][1], secondg[i]['station'][2]], radius=1000, 
                        popup=secondg[i]['station'][0], color='mediumpurple',
                        fill_color='indigo').add_to(m)
    #marker
    for j in range(len(secondg[i]['star'][0])):
        x = secondg[i]['star'][0][j][2]
        y = secondg[i]['star'][0][j][1]
        name = str(secondg[i]['star'][0][j][0])
        folium.Marker([y,x],popup=name,
                     icon=folium.Icon(color='purple',icon="flag")).add_to(m)
        
for i in range(0,len(firstg)):
    folium.Circle([firstg[i]['station'][1], firstg[i]['station'][2]], radius=1000, 
                        popup=firstg[i]['station'][0], color='crimson',
                        fill_color='crimson').add_to(m)
    #marker
    for j in range(len(firstg[i]['star'][0])):
        x = firstg[i]['star'][0][j][2]
        y = firstg[i]['star'][0][j][1]
        name = str(firstg[i]['star'][0][j][0])
        folium.Marker([y,x],popup=name,
                     icon=folium.Icon(color='red',icon="flag")).add_to(m)
        
m.save('index.html')
m