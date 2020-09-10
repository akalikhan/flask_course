from flask import Flask, jsonify, request

app = Flask(__name__)

stores = [
    {
        'name'  : 'FirstStore',
        'items' : [
            {
                'name'  : 'FirstItem', 
                'price' : 500
            }
        ]
    }
]

@app.route('/stores', methods = ['GET'])
def get_stores():
    return jsonify(stores), 200

@app.route('/store', methods = ['POST'])
def create_store():
    new_store = {
        'name'  : request.get_json()['name'],
        'items' : []
    }
    stores.append(new_store)
    return new_store, 201

@app.route('/store/<string:name>', methods = ['GET'])
def get_store_by_name(name):
    for store in stores:
        if store['name'] == name:
            return jsonify(store), 200

    return {'Error': 'Store not found'}, 404

@app.route('/store/<string:name>', methods = ['DELETE'])
def delete_store(name):
    for store in stores:
        if store['name'] == name:
            stores.pop(stores.index(store))
            return {"Message": "Store deleted"}, 202

    return {'Error': 'Store not found'}, 404
    

@app.route('/store/<string:name>', methods = ['PUT'])
def update_store(name):
    for store in stores:
        if store['name'] == name:
            store['items'] = request.get_json()['items']
            return jsonify(store), 201

    return {'Error': 'Store not found'}, 404

if __name__ == "__main__":
    app.run(port=800, debug=True)