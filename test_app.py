from flask import Flask, escape, request, jsonify
import sqlite3
from flask import g

DATABASE = '/home/heather_e_gaya/INFO_8000_Flaskapp/birdinfo.db'

app = Flask(__name__)

@app.route('/')
def hello():
    name = request.args.get("name", "World")
    response = {"name":name + " Hello"}
    return jsonify(response)



@app.route('/testconnect/')
def get_db():
    db = getattr(g, '_database', None)
     name = request.args.get("name", "World")
    response = {"name":name + " Hello"}
    if db is None:
        database_file = current_app.config['DATABASE']
        db = g._database = sqlite3.connect(database_file)
        db.row_factory = sqlite3.Row
    return jsonify(response)
