import sqlite3
con = sqlite3.connect("./test.db")
cur = con.cursor()
cur.execute("CREATE TABLE PhoneBook(Name text, PhoneNum text);")
cur.execute("INSERT INTO PhoneBook VALUES('Derick', '010-1234-5678');")
cur.execute("SELECT * FROM PhoneBook;")
print(cur.fetchall())
