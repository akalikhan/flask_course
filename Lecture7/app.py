from flask import Flask, request
from flask_restful import Resource, Api, reqparse
from flask_jwt import JWT, jwt_required, current_identity
from auth_conf import authenticate, identity
from user import UserResource
from item import Item, ItemCollection
import table

app = Flask(__name__)
app.secret_key = "Alpachino"
api = Api(app)

jwt = JWT(app, authenticate, identity)


api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemCollection, '/items')
api.add_resource(UserResource, '/register')

if __name__ == "__main__":
    app.run(port=8080, debug=True)