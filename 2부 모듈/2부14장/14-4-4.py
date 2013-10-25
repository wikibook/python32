import sqlite3
con = sqlite3.connect("./commit.db")
cur = con.cursor()
cur.execute("SELECT * FROM PhoneBook;")
print(cur.fetchall())
