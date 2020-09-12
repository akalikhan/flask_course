from flask_restful import Resource, reqparse
from models.item import ItemModel

class ItemResource(Resource):

    parser = reqparse.RequestParser()
    parser.add_argument('title', type=str, required=True, help='This field cannot be blank')
    parser.add_argument('amount', type=int, required=True, help='This field cannot be blank')
    parser.add_argument('price', type=float, required=True, help='This field cannot be blank')

    def get(self, _id):
        item = ItemModel.search_by_id(_id)
        if item:
            return item, 200
        return {"Error": "Item with that id not found"}, 404
    
    def post(self, _id):
        if ItemModel.search_by_id(_id):
            return {'Error' : 'Item with that id already exists'}, 400
        
        data = ItemResource.parser.parse_args()

        ItemModel(data['title'], data['amount'], data['price'], _id).insert()

        return {"Message" : "Item created"}, 201

    def put(self, _id):
        if ItemModel.search_by_id(_id):
            data = ItemResource.parser.parse_args()
    
            updated_item = ItemModel(data['title'], data['amount'], data['price'], _id)
            updated_item.update()

            return updated_item.json(), 202
        
        return {'Error' : 'Item with that id not found'}, 404

    def delete(self, _id):
        if ItemModel.search_by_id(_id):
        
            item_to_delete = ItemModel(None, None, None, _id)
            item_to_delete.delete()

            return {'Message' : 'Item deleted'}, 202
        
        return {'Error' : 'Item with that id not found'}, 404


class ItemCollectionResource(Resource):
    def get(self):
        items = ItemModel.get_all()
        if len(items):
            return {"items": items}, 200
        else:
            return {"Error" : "No one items found in store back"}, 403