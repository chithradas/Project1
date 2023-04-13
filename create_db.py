import sqlite3
def create_db():
    con=sq1ite3.connect(database=r'ims. db')
    cur = con. cursor()
    cur.excute("Create TABLE IF NOT EXISTS employee(eid INTEGER PRIMARY KEY AUTOINCREMENT")


create_db()