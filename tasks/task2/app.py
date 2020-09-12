from flask import Flask, request
from flask_restful import Resource, Api, reqparse

app = Flask(__name__)
api = Api(app)

coef = [0,0,0]

class Grab(Resource):
    def post(self):
        data = request.get_json()
        coef[0] = data['A']
        coef[1] = data['B']
        coef[2] = data['C']
        return {"Message" : "Coeficients created"}, 200

class Solve(Resource):
    def get(self):
        D = coef[1]*coef[1] - 4 * coef[0] * coef[2]
        
        if coef[0] == 0:
            if coef[1] == 0:
                n = 0
            else:
                n = 1
        else:
            if D < 0:
                n = 0
            elif D == 0:
                n = 1
            else: 
                n = 2

        return {
            "A" : coef[0],
            "B" : coef[1],
            "C" : coef[2],
            "Nroots": n
        }, 200
        

api.add_resource(Grab, '/grab')
api.add_resource(Solve, '/solve')

if __name__ == "__main__":
    app.run(port=8080, debug=True)