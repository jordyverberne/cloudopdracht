import os
from flask import Flask, redirect, url_for, request, render_template, jsonify
from pymongo import MongoClient
from bson import json_util
import json

app = Flask(__name__)

client = MongoClient('mongodb://db:27017')
db = client.MAF
collection = db.sporters



@app.route('/')
def todo():
    cursor = collection.find({"email":"jordyverberne@gmail.com"})
    naam = "{}".format(cursor[0]['voornaam']+ ' '+ cursor[0]['achternaam'])
    return jsonify (naam)


    #naam = collection.find_one({"voornaam":"Jordy"})
    #find = collection.find()
    #json_projects = []
    #for i in find:
	#json_projects.append(i)
    #json_projects = json.dumps(json_projects, default=json_util.default) 
    #return json_projects

#@app.route('/new', methods=['POST'])
#def new():
#
    #item_doc = {
        #'name': request.form['name'],
        #'description': request.form['description']
    #}
    #db.tododb.insert_one(item_doc)
#
    #return redirect(url_for('todo'))

if __name__ == "__main__":
    app.run(debug=True, ssl_context='adhoc', host='0.0.0.0', port=5001)
