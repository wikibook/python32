# -*- coding: cp949 -*-
import sqlite3

con = sqlite3.connect(":memory:")

with open('script.txt') as f:	# script.txt에서 SQL 구문을 읽음
	SQLScript = f.read()

cur = con.cursor()
cur.executescript(SQLScript)
