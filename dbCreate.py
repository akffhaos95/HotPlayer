import pymysql
connect = pymysql.connect(host = 'localhost',
                            user = 'root',
                            password = 'qwer1234',
                            db = 'test',
                            charset = 'utf8mb4',
                            cursorclass = pymysql.cursors.DictCursor)

try:
    with connect.cursor() as cursor:
        sql = '''
            drop table if exists users;
            '''
        cursor.execute(sql)
        connect.commit()

    with connect.cursor() as cursor:
        sql = '''
            create table if not exists users(
                userid varchar(20) primary key,
                userpw varchar(20) not null,
                username varchar(20) not null,
                userage int,
                usermail varchar(20),
                useradd varchar(50),
                usergender varchar(20),
                usertel varchar(20))DEFAULT CHARSET=utf8;;
            '''
        cursor.execute(sql)
        connect.commit()

    with connect.cursor() as cursor:
        sql = '''
                insert into users values('gilldong1', 
                                            '1234', '길동',
                                            33, 'gildong1@gmail.com', 
                                            '부산시 남구',
                                            'male',
                                            '010-2314-3479')'''
        cursor.execute(sql)
        connect.commit()

    with connect.cursor() as cursor:
        sql = '''
                select * from users;
                '''
        cursor.execute(sql)
        result = cursor.fetchall()
        print(result)

finally:
    connect.close()