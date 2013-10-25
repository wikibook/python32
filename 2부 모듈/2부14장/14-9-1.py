# -*- coding: cp949 -*-
class Point(object):   
    def __init__(self, x, y):
        self.x, self.y = x, y

    def __repr__(self):             # Point 객체의 내용 출력     
        return "Point(%f, %f)" % (self.x, self.y)

import sqlite3
def PointAdapter(point):                # 클래스 객체에서 SQLite3 입력 가능한 자료형으로 변환      
    return "%f:%f" % (point.x, point.y)

def PointConverter(s):                  # SQLite3에서 조회한 결과를 클래스 객체로 변환 
    x, y = list(map(float, s.decode().split(":")))
    return Point(x, y)

sqlite3.register_adapter(Point, PointAdapter)          # 클래스 이름과 변환 함수 등록
sqlite3.register_converter("point", PointConverter)    # SQL 구문에서 사용할 자료형 이름과 변환함수 등록

p = Point(4, -3.2)           # 입력할 데이터(파이썬 클래스 객체)
p2 = Point(-1.4, 6.2)

# 암묵적으로 선언된 자료형으로 조회하도록 설정  
con = sqlite3.connect(":memory:", detect_types=sqlite3.PARSE_DECLTYPES)
cur = con.cursor()
cur.execute("create table test(p point)")             # point 자료형을 이용하여 테이블 생성

cur.execute("insert into test values (?)", (p, ))     # point 레코드 입력
cur.execute("insert into test(p) values (?)", (p2,))

cur.execute("select p from test")    # 테이블 조회 
print([r[0] for r in cur])           
cur.close()
con.close()
