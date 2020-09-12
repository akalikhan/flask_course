import sqlite3

class ItemModel:
    __tablename__ = 'items'

    def __init__(self, title, amount, price, _id = None):
        self.title = title
        self.amount = amount
        self.price = price
        self.id = _id

    @classmethod
    def search_by_id(cls, _id):
        conn = sqlite3.connect('data.db')
        cur = conn.cursor()

        select_query = "SELECT * FROM {} WHERE id=?".format(cls.__tablename__)
        row = cur.execute(select_query, (_id, )).fetchone()

        conn.close()

        if row:
            return {'title' : row[1], 'amount' : row[2], 'price' : row[3]}

    def json(self):
        return {"title" : self.title, "amount" : self.amount, "price" : self.price}
    
    def insert(self):
        conn = sqlite3.connect('data.db')
        cur = conn.cursor()

        insert_query = "INSERT INTO {} VALUES(?,?,?,?)".format(self.__tablename__)
        cur.execute(insert_query, (self.id, self.title, self.amount, self.price))

        conn.commit()
        conn.close()

    def update(self):
        conn = sqlite3.connect('data.db')
        cur = conn.cursor()

        update_query = "UPDATE {} SET title=?, amount=?, price=? WHERE id=?".format(self.__tablename__)
        print(update_query)
        cur.execute(update_query, (self.title, self.amount, self.price, self.id))

        conn.commit()
        conn.close()
    
    def delete(self):
        conn = sqlite3.connect('data.db')
        cur = conn.cursor()

        delete_query = "DELETE FROM {} WHERE id=?".format(self.__tablename__)
        cur.execute(delete_query, (self.id, ))

        conn.commit()
        conn.close()

    @classmethod
    def get_all(cls):
        conn = sqlite3.connect('data.db')
        cur = conn.cursor()

        select_query = "SELECT * FROM {}".format(cls.__tablename__)

        items = []

        for line in cur.execute(select_query):
            items.append({"title" : line[1], "amount" : line[2], "price" : line[3]})
        
        conn.close()

        return items