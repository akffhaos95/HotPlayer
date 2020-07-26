import pandas as pd
import matplotlib as mlp
import matplotlib.pyplot as plt
import seaborn as sns

subway_total = pd.read_csv("C:/Users/a0104/OneDrive/문서/Python Scripts/HotPlayer/static/data/subway.csv", encoding="cp949")

# subway: basic dataframe for each subway line. 

up_total = subway_total[subway_total['승하'] == '승차']
up_total = up_total.groupby(['역명']).sum()

down_total = subway_total[subway_total['승하'] == '하차']
down_total = down_total.groupby(['역명']).sum()

up_total_아침 = up_total.loc[:,["06~07","07~08","08~09"]]
up_total_오전 = up_total.loc[:,["09~10","10~11"]]
up_total_점심 = up_total.loc[:,["11~12","12~13","13~14"]]
up_total_오후 = up_total.loc[:,["14~15","15~16","16~17"]]
up_total_저녁 = up_total.loc[:,["17~18","18~19","19~20"]]
up_total_밤 =  up_total.loc[:,["20~21","21~22","22~23","23~24"]]

down_total_아침 = down_total.loc[:,["06~07","07~08","08~09"]]
down_total_오전 = down_total.loc[:,["09~10","10~11"]]
down_total_점심 = down_total.loc[:,["11~12","12~13","13~14"]]
down_total_오후 = down_total.loc[:,["14~15","15~16","16~17"]]
down_total_저녁 = down_total.loc[:,["17~18","18~19","19~20"]]
down_total_밤 =  down_total.loc[:,["20~21","21~22","22~23","23~24"]]


up_total_아침['sum']=up_total_아침.apply(lambda row: (row[0]+row[1]+row[2]),axis=1)
up_total_오전['sum']=up_total_오전.apply(lambda row: (row[0]+row[1]),axis=1)
up_total_점심['sum']=up_total_점심.apply(lambda row: (row[0]+row[1]+row[2]),axis=1)
up_total_오후['sum']=up_total_오후.apply(lambda row: (row[0]+row[1]+row[2]),axis=1)
up_total_저녁['sum']=up_total_저녁.apply(lambda row: (row[0]+row[1]+row[2]),axis=1)
up_total_밤['sum']=up_total_밤.apply(lambda row: (row[0]+row[1]+row[2]+row[3]),axis=1)

down_total_아침['sum'] = down_total_아침.apply(lambda row: (row[0]+row[1]+row[2]),axis=1)
down_total_오전['sum'] = down_total_오전.apply(lambda row: (row[0]+row[1]),axis=1)
down_total_점심['sum'] = down_total_점심.apply(lambda row: (row[0]+row[1]+row[2]),axis=1)
down_total_오후['sum'] = down_total_오후.apply(lambda row: (row[0]+row[1]+row[2]),axis=1)
down_total_저녁['sum'] = down_total_저녁.apply(lambda row: (row[0]+row[1]+row[2]),axis=1)
down_total_밤['sum'] =  down_total_밤.apply(lambda row: (row[0]+row[1]+row[2]+row[3]),axis=1)

up_total_아침_head = up_total_아침.sort_values(by = ['sum'],  axis=0, ascending=False).head(12)
up_total_오전_head = up_total_아침.sort_values(by = ['sum'],  axis=0, ascending=False).head(12)
up_total_점심_head = up_total_아침.sort_values(by = ['sum'],  axis=0, ascending=False).head(12)
up_total_오후_head = up_total_아침.sort_values(by = ['sum'],  axis=0, ascending=False).head(12)
up_total_저녁_head = up_total_아침.sort_values(by = ['sum'],  axis=0, ascending=False).head(12)
up_total_밤_head = up_total_점심.sort_values(by = ['sum'],  axis=0, ascending=False).head(12)

down_total_아침_head = up_total_아침.sort_values(by = ['sum'],  axis=0, ascending=False).head(12)
down_total_오전_head = up_total_아침.sort_values(by = ['sum'],  axis=0, ascending=False).head(12)
down_total_점심_head = up_total_아침.sort_values(by = ['sum'],  axis=0, ascending=False).head(12)
down_total_오후_head = up_total_아침.sort_values(by = ['sum'],  axis=0, ascending=False).head(12)
down_total_저녁_head = up_total_아침.sort_values(by = ['sum'],  axis=0, ascending=False).head(12)
down_total_밤_head = up_total_점심.sort_values(by = ['sum'],  axis=0, ascending=False).head(12)

up_total_아침_head.to_json('up_total_아침_head.json', orient='table')
up_total_오전_head.to_json('up_total_오전_head.json', orient='table')
up_total_점심_head.to_json('up_total_점심_head.json', orient='table')
up_total_오후_head.to_json('up_total_오후_head.json', orient='table')
up_total_저녁_head.to_json('up_total_저녁_head.json', orient='table')
up_total_밤_head.to_json('up_total_밤_head.json', orient='table')

down_total_아침_head.to_json('down_total_아침_head.json', orient='table')
down_total_오전_head.to_json('down_total_오전_head.json', orient='table')
down_total_점심_head.to_json('down_total_점심_head.json', orient='table')
down_total_오후_head.to_json('down_total_오후_head.json', orient='table')
down_total_저녁_head.to_json('down_total_저녁_head.json', orient='table')
down_total_밤_head.to_json('down_total_밤_head.json', orient='table')