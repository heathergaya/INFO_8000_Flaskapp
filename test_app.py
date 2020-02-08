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
  db = g._database = sqlite3.connect(DATABASE)
    return jsonify({"I connected"})
