# -*- coding: cp949 -*-
import sqlite3
con = sqlite3.connect(":memory:")
cur = con.cursor()

cur.execute("CREATE TABLE PhoneBook(Name text, Age integer);")
list = (('Tom', 24),('Derick',30), ('Peter',53), ('Jane',29))
cur.executemany("INSERT INTO PhoneBook VALUES(?, ?);", list)

cur.execute("SELECT length(Name), upper(Name), lower(Name) FROM PhoneBook")    # 문자열 길이, 대문자, 소문자
print("== length(), upper(), lower() ==")
print([r for r in cur])

cur.execute("SELECT max(Age), min(Age), sum(Age) FROM PhoneBook")     # 최대값, 최소값, 총합
print("== max(), min(), sum() ==")
print([r for r in cur])

cur.execute("SELECT count(*), random(*) FROM PhoneBook")              # 레코드 갯수, 임의의 값
print("== count(*), random(*) ==")
print([r for r in cur])
