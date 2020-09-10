import sqlite3

conn = sqlite3.connect('data.db')
cur = conn.cursor()

create_table = 'CREATE TABLE IF NOT EXISTS users (id INTEGER, login TEXT, password TEXT)';

cur.execute(create_table);

insert_user = 'INSERT INTO users VALUES (?,?,?)'
user = [1, "Alex", "itvizion"]

cur.execute(insert_user, (user[0], user[1], user[2]))

conn.commit()

select_all = "SELECT * FROM users"

for row in cur.execute(select_all):
    print(row)
