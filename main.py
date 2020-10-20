from flask import Flask, request
from flask_restful import Resource, Api
from sqlalchemy import create_engine
from json import dumps
from flask_jsonpify import jsonify

from Blotter import Blotter

app = Flask(__name__)
CORS(app)
api = Api(app)
blotter = Blotter()

class PlaceOrder(Resource):
    def post(self):
        """
        post api to place an order
        """
        contents = request.get_json(force=True)
        for content in contents:
            trader = content['trader']
            date = content['date']
            ticker = content['ticker']
            side = content['side']
            contract = content['contract']
            position = content['position']
            if ticker != "":
                blotter.insertOrder(trader, date, ticker, side, contract, position)
                
        #return jsonify(result)

# get api         
class GetPosition(Resource):
    def get(self):
        """
        get api to get current position
        """
        result = blotter.getPosition()
        response = jsonify(result)
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response
    
#@app.route('/recommend', methods=['POST'])

api.add_resource(PlaceOrder, '/placeOrder') # Route_3
api.add_resource(GetPosition, '/getPosition') # Route_3

if __name__ == '__main__':
     app.run(port='5002')
