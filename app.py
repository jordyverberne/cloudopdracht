#Geschreven door Jordy Verberne
from flask import Flask, render_template, request, make_response, jsonify
from authomatic.adapters import WerkzeugAdapter
from authomatic import Authomatic
import authomatic
import logging
import pymongo
import os
import pprint
from pymongo import MongoClient
import time
from config import CONFIG
from flask_restful import reqparse, abort, Api, Resource
from bson.json_util import dumps

parser = reqparse.RequestParser()
parser.add_argument('kaartid')
client = MongoClient("mongodb://mongodb:27017")
db = client.MAF
collection = db.sporters
# Instantiate Authomatic.
authomatic = Authomatic(CONFIG, 'P@ssword', report_errors=False)
parser.add_argument('kaartid')

app = Flask(__name__, template_folder='.')
app.config["MONGO_URI"] = "mongodb://mongodb:27017"
api = Api(app)
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login/<provider_name>/', methods=['GET', 'POST'])
def login(provider_name):
    # We need response object for the WerkzeugAdapter.
    response = make_response()
    # Log the user in, pass it the adapter and the provider name.
    result = authomatic.login(WerkzeugAdapter(request, response), provider_name)

    # If there is no LoginResult object, the login procedure is still pending.
    
    if result:
        if result.user:
            # We need to update the user to get more info.
            result.user.update()

        cursor = collection.find({"email":result.user.email})
	naam = "{}".format(cursor[0]['voornaam']+ ' '+ cursor[0]['achternaam'])
        email = cursor[0]['email']
        kaart = cursor[0]['kaartID']
        checkin = cursor[0]['checkin']
        checkout = cursor[0]['checkout']
        timespend = []
        for a,b in zip(checkin,checkout):
            timespend.append(b-a)

        # The rest happens inside the template.
        return render_template('login.html',email=email, result=result,naam=naam, timespend=timespend,kaart=kaart)

    # Don't forget to return the response.
    return response


class query(Resource):
    @app.route('/query/<kaartid>/', methods=['GET'])#, 'PUT'])
    def get(kaartid):#, kaartid):
	cursor = collection.find({"kaartID":kaartid})
	return dumps(cursor[0])


class checkInOut(Resource):
    @app.route('/checkinout', methods=['PUT'])
    def put():
        args = parser.parse_args()
	kaartid=args['kaartid']
	tijd = int(time.time())
	cursor = collection.find({"kaartID":kaartid})
	if len(cursor[0]['checkin']) == len(cursor[0]['checkout']):
	    collection.update({"kaartID":kaartid}, {'$push':{'checkin':tijd}})
	elif len(cursor[0]['checkin']) > len(cursor[0]['checkout']):
	    collection.update({"kaartID":kaartid}, {'$push':{'checkout':tijd}})
        return jsonify({'status': 'ok'})



if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port='5000', ssl_context='adhoc')
