from flask import Flask, request
from flask_restful import Api
from resources.item import ItemResource, ItemCollectionResource

app = Flask(__name__)
api = Api(app)

api.add_resource(ItemResource, '/api/v1/item/<string:_id>')
api.add_resource(ItemCollectionResource, '/api/v1/items')

if __name__ == "__main__":
    app.run(port=8080, debug=True)