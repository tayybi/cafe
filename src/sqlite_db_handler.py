import sqlite3
def create_db_tables():
    #openning database creat DB if not exist
    connection = sqlite3.connect('data/db_london_cafy.db')

    #table creating
    connection.execute('''CREATE TABLE IF NOT EXISTS courier
    (id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    phone TEXT NOT NULL);''')
    connection.execute('''CREATE TABLE IF NOT EXISTS product
    (id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    price FLOAT NOT NULL);''')
    connection.close()

def insert_into_courior(name,phone):
    conn = sqlite3.connect('data/db_london_cafy.db')
    conn.execute(f'''INSERT INTO courier (name,price)
      VALUES ({name},{phone})''');
    conn.close

def insert_into_product(name, price):
    conn = sqlite3.connect('data/db_london_cafy.db')
    conn.execute(f'''INSERT INTO courier (name,price)
      VALUES ({name},{price})''');
    conn.close

create_db_tables()