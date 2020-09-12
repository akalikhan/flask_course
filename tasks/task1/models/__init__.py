import sqlite3

conn = sqlite3.connect('data.db')
cur = conn.cursor()

create_items = 'CREATE TABLE IF NOT EXISTS items (id INTEGER, title TEXT, amount INTEGER, price REAL)'
cur.execute(create_items)

conn.commit()

conn.close()