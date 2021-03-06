from flask import Flask, request
from flask_restful import Resource, Api, reqparse
from flask_jwt import JWT, jwt_required, current_identity
from secure.auth_conf import authenticate, identity
from resources.user import UserResource
from resources.item import ItemResource, ItemCollectionResource


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:////data.db'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

@app.before_first_request
def db_scheme_generator():
    print("Before first request!")


app.secret_key = "Alpachino"
api = Api(app)

jwt = JWT(app, authenticate, identity)


api.add_resource(ItemResource, '/item/<string:name>')
api.add_resource(ItemCollectionResource, '/items')
api.add_resource(UserResource, '/register')

if __name__ == "__main__":
    app.run(port=8080, debug=True)