#Resource /items
#GET /items 




#Resource /item/<string:name>
#GET /item/<string:name>
#POST /item/<string:name>
#PUT /item/<string:name>
#DELETE /item/<string:name>

'''
Product structure
{
    "name" : "Item Name",
    "price": 99.99
}
'''

from flask import Flask, request
from flask_restful import Resource, Api, reqparse

app = Flask(__name__)

api = Api(app)
#DB
items = []

#resource Item /item/<string:name>
class Item(Resource):
    
    parser = reqparse.RequestParser()
    parser.add_argument('price', type=float, required=True, help='This field cannot be blank')

    def get(self, name):
        item = next(filter(lambda x: x['name'] == name, items), None)
        if item:
            return {"item": item}, 200
        return {"Error": "Item not found"}, 404
    
    def post(self, name):
        if next(filter(lambda x: x['name'] == name, items), None):
            return {'Error' : 'Item with name {} exists'.format(name)}, 400
        
        data = Item.parser.parse_args()
        item = {'name': name, 'price': data['price']}
        items.append(item)

        return item, 201

    def put(self, name):
        item = next(filter(lambda x: x['name'] == name, items), None)
        if item:
            data = Item.parser.parse_args()
            item.update(data)
            return {"item": item}, 200
        
        return {'Error' : 'Item with name {} not found'.format(name)}, 404

    def delete(self, name):
        global items
        start_len = len(items)
        items = list(filter(lambda x: x['name'] != name, items))
        if len(items) < start_len:
            return {'Message' : 'Item deleted'}, 202
        return {'Error' : 'Item not found'}, 404

#resource Items /items
class ItemCollection(Resource):
    def get(self):
        return {"items": items}, 200

api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemCollection, '/items')

if __name__ == "__main__":
    app.run(port=8080, debug=True)