from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
import sqlite3

#resource Item /item/<string:name>
class Auto(Resource):
    
    __tablename__ = 'cars'
    parser = reqparse.RequestParser()
    parser.add_argument('handler', type=str, required=True, help='This field cannot be blank')
    parser.add_argument('stock', type=str, required=True, help='This field cannot be blank')
    parser.add_argument('distance', type=int, required=True, help='This field cannot be blank')
    parser.add_argument('max_speed', type=int, required=True, help='This field cannot be blank')

    @classmethod
    def search_mark(cls, mark):
        conn = sqlite3.connect('data.db')
        cur = conn.cursor()

        select_query = "SELECT * FROM {} WHERE mark=?".format(cls.__tablename__)
        row = cur.execute(select_query, (mark, )).fetchone()

        conn.close()

        if row:
            return {'max_speed' : row[1], 'distance' : row[2], 'handler' : row[3], 'stock' : row[4]}

    @jwt_required()
    def get(self, mark):
        car = Auto.search_mark(mark)
        if car:
            return car, 200
        return {"Error": "Auto with that mark not found"}, 404
    
    @jwt_required()
    def post(self, mark):
        if Auto.search_mark(mark):
            return {'Error' : 'Auto with that mark exists'}, 400
        
        data = Auto.parser.parse_args()
        car = {'max_speed': data['max_speed'], 'distance' : data['distance'], 'handler': data['handler'], 'stock' : data['stock']}
        
        conn = sqlite3.connect('data.db')
        cur = conn.cursor()

        insert_query = "INSERT INTO {} VALUES(?,?,?,?,?)".format(self.__tablename__)
        cur.execute(insert_query, (mark, car['max_speed'], car['distance'], car['handler'], car['stock']))

        conn.commit()
        conn.close()

        return {"Message" : "Auto created"}, 201

    @jwt_required()
    def put(self, mark):
        if Auto.search_mark(mark):
            data = Auto.parser.parse_args()
            
            conn = sqlite3.connect('data.db')
            cur = conn.cursor()

            update_query = "UPDATE {} SET max_speed=? and distance=? and handler=? and stock=? WHERE mark=?".format(self.__tablename__)
            cur.execute(update_query, (data['max_speed'], data['distance'], data['handler'], data['stock'], mark))

            conn.commit()
            conn.close()


            return {"Message" : "Auto updated"}, 200
        
        return {'Error' : 'Auto with that mark not found'}, 404

    @jwt_required()
    def delete(self, mark):
        if Auto.search_mark(mark):
        
            conn = sqlite3.connect('data.db')
            cur = conn.cursor()

            delete_query = "DELETE FROM {} WHERE mark=?".format(self.__tablename__)
            cur.execute(delete_query, (mark, ))

            conn.commit()
            conn.close()

            return {'Message' : 'Auto deleted'}, 202
        
        return {'Error' : 'Auto with that mark not found'}, 404

class Stock(Resource):
    __tablename__ = 'cars'

    @jwt_required()
    def get(self):
        conn = sqlite3.connect('data.db')
        cur = conn.cursor()
        print("hi")
        select_query = "SELECT * FROM {}".format(self.__tablename__)

        cars = []
        count = 0

        for line in cur.execute(select_query):
            count += 1
            cars.append({"mark" : line[0], "max_speed" : line[1], "distance" : line[2], "handler" : line[3], "stock" : line[4]})
        
        conn.close()

        if count:
            return cars, 200
        else:
            return {"Error": "No one autos found in database"}, 400
