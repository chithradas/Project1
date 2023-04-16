import sqlite3

def create_db():
    con = sqlite3.connect(database=r'ims.db')
    cur = con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS employee(eid INTEGER PRIMARY KEY AUTOINCREMENT, name text, email text, gender text, contact text, dob text, doj text, pass text, utype text, address text, salary text)")
    con.commit()

    cur.execute(
        "CREATE TABLE IF NOT EXISTS supplier(invoice INTEGER PRIMARY KEY AUTOINCREMENT, name text,contact text, desc text)")
    con.commit()

    cur.execute(
        "CREATE TABLE IF NOT EXISTS products (proId INTEGER PRIMARY KEY AUTOINCREMENT, name text, catId text)")
    con.commit()

    cur.execute(
        "CREATE TABLE IF NOT EXISTS category(catId INTEGER PRIMARY KEY AUTOINCREMENT, name text)")
    con.commit()

    cur.execute(
        "CREATE TABLE IF NOT EXISTS buy(invoice, product_name, catId, quantity, sup_id)")
    con.commit()

    cur.execute(
        "CREATE TABLE IF NOT EXISTS sale (invoice, product_name, catId, quantity, Emp_id)")
    con.commit()






create_db()
