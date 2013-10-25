# -*- coding: cp949 -*-
class Average:
    def __init__(self):
        self.sum = 0          # sum, cnt의 초기화
        self.cnt = 0

    def step(self, value):
        self.sum += value     # 입력된 값을 sum에 더하고, 카운트(cnt)를 증가 
        self.cnt += 1

    def finalize(self):
        return self.sum / self.cnt    # 평균을 반환

import sqlite3
con = sqlite3.connect(":memory:")
cur = con.cursor()

cur.execute("CREATE TABLE User(Name text, Age int);")
list = (('Tom', '16'),
 ('DSP', '33'),
('Derick', '25'))
cur.executemany("INSERT INTO User VALUES(?, ?);", list)   

con.create_aggregate("avg", 1, Average)        # Average 클래스를 사용자 정의 집계함수로 등록

cur.execute("SELECT avg(Age) FROM User")       # 질의시 생성한 사용자 정의 집계 함수를 사용
print(cur.fetchone()[0])                       # 출력 결과: 24.6666666667 
