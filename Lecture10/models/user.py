import sqlite3

class UserModel:

    __tablename__ = 'users'

    def __init__(self, _id, username, password):
        self.id = _id
        self.username = username
        self.password = password

    @classmethod
    def search_username(cls, username):
        conn = sqlite3.connect('data.db')
        cur = conn.cursor()

        select_query = "SELECT * FROM {} WHERE username=?".format(cls.__tablename__)
        row = cur.execute(select_query, (username, )).fetchone()
        if row:
            user = cls(row[0], row[1], row[2])
        else:
            user = None
        
        conn.close()
        return user


    @classmethod
    def search_id(cls, _id):
        conn = sqlite3.connect('data.db')
        cur = conn.cursor()

        select_query = "SELECT * FROM {} WHERE id=?".format(cls.__tablename__)
        row = cur.execute(select_query, (_id, )).fetchone()
        if row:
            user = cls(row[0], row[1], row[2])
        else:
            user = None
        
        conn.close()
        return user

    def insert(self):
        conn = sqlite3.connect('data.db')
        cur = conn.cursor()

        insert_query = "INSERT INTO {} VALUES(NULL, ?, ?)".format(self.__tablename__)
        cur.execute(insert_query, (self.username, self.password))

        conn.commit()
        conn.close()