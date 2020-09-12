from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
from models.item import ItemModel
import sqlite3

#resource Item /item/<string:name>
class ItemResource(Resource):

    parser = reqparse.RequestParser()
    parser.add_argument('price', type=float, required=True, help='This field cannot be blank')

    def get(self, name):
        item = ItemModel.search_name(name)
        if item:
            return {"item": item}, 200
        return {"Error": "Item not found"}, 404
    
    @jwt_required()
    def post(self, name):
        if ItemModel.search_name(name):
            return {'Error' : 'Item with name {} exists'.format(name)}, 400
        
        data = ItemResource.parser.parse_args()

        item = ItemModel(name, data['price'])
        item.insert()

        return item.json(), 201

    @jwt_required()
    def put(self, name):
        if ItemModel.search_name(name):
            data = ItemResource.parser.parse_args()
    
            updated_item = ItemModel(name, data['price'])
            updated_item.update()

            return updated_item.json(), 200
        
        return {'Error' : 'Item with name {} not found'.format(name)}, 404

    @jwt_required()
    def delete(self, name):
        if ItemModel.search_name(name):
        
            item_to_delete = ItemModel(name, None)
            item_to_delete.delete()

            return {'Message' : 'Item deleted'}, 202
        
        return {'Error' : 'Item not found'}, 404

#resource Items /items
class ItemCollectionResource(Resource):
    def get(self):
        items = ItemModel.get_all()
        return {"items": items}, 200
