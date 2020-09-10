import sqlite3

conn = sqlite3.connect('data.db')
cur = conn.cursor()

create_items = 'CREATE TABLE IF NOT EXISTS items (name TEXT, price REAL)'
cur.execute(create_items)

create_users = 'CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, username TEXT, password TEXT)'
cur.execute(create_users)

conn.commit()

conn.close()