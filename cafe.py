import requests, pandas as pd, pymysql

class Database():
    def create_conn(self):
        conn = pymysql.connect(
            host="localhost", 
            user="root", 
            password="qwer1234", 
            db="test",
            charset="utf8",
            cursorclass=pymysql.cursors.DictCursor
        )
        return conn
    def create_table(self):
        conn = self.create_conn()
        c = conn.cursor()
        sql = '''
            CREATE TABLE if not exists CAFE(
            ID INTEGER NOT NULL AUTO_INCREMENT PRIMARY KEY,
            NAME TEXT,
            X FLOAT,
            Y FLOAT,
            BRAND TEXT
            )DEFAULT CHARSET=utf8
        '''
        c.execute(sql)
        conn.commit()
        c.close()
    def insert_books(self, item):
        conn = self.create_conn()
        c = conn.cursor()
        sql = 'INSERT INTO CAFE (NAME, X, Y, BRAND) VALUES(%s,%s,%s,%s)'
        c.execute(sql, item)
        conn.commit()
        c.close()
        conn.close()
   
def get_station_location(query, key):
    name, x, y = [], [], []
    for page in range(1,7):
        url = "https://dapi.kakao.com/v2/local/search/keyword.json?query={}&category_group_code=SW8&page={}".format(query, page)
        headers = {'Authorization': 'KakaoAK {0}'.format(key)}
        res = requests.get(url, headers=headers)
        res = res.json()
        res = res['documents']
        for i in res:
            if i['place_name'] not in name:
                name.append(i['place_name'])
                x.append(i['x'])
                y.append(i['y'])
    return name, x, y

def get_cafe_location(query, lng, loc, radius, key):
    name, x, y = [], [], []
    url = "https://dapi.kakao.com/v2/local/search/keyword.json?y={}&x={}&radius={}&query={}&category_group_code=CE7".format(loc, lng, radius, query)
    headers = {'Authorization': 'KakaoAK {0}'.format(key)}
    res = requests.get(url, headers=headers).json()
    for i in res['documents']:
        name.append(i['place_name'])
        x.append(i['x'])
        y.append(i['y'])
    return name, x, y

if __name__ == "__main__":
    db = Database()
    #테이블 생성
    db.create_table()
    #데이터 삽입하기    
    name, x, y = [], [], []

    key = "f3ff022cb1217ebafbcdb6e7ef9d026f"
    
    cafe_list = ['스타벅스', '이디야', '투썸플레이스', '설빙', '탐앤탐스', '핸즈커피', '엔제리너스','파스쿠찌'] 
    subway_list = ['대구 1호선', '대구 2호선', '대구 3호선','경산'] 
    radius = 1000

    for i in subway_list:
        name1, x1, y1 = get_station_location(i, key)
        name += name1
        x += x1
        y += y1
    for query in cafe_list:
        cafe_name, cafe_x, cafe_y = [], [], []
        for i in range(len(name)):
            cafe_name1, cafe_x1, cafe_y1 = get_cafe_location(query, x[i], y[i], radius,key)
            for i in range(len(cafe_name1)):
                if cafe_name1[i] not in cafe_name:
                    cafe_name.append(cafe_name1[i])
                    cafe_x.append(cafe_x1[i])
                    cafe_y.append(cafe_y1[i])
        for i in range(len(cafe_name)):
            cafe = [cafe_name[i], cafe_x[i], cafe_y[i], query]
            db.insert_books(cafe)
            print("insert", cafe)