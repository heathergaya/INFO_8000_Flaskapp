from flask import Flask, escape, request, jsonify
import sqlite3
from flask import g

DATABASE = 'birdinfo.db'

app = Flask(__name__)

@app.route('/')
def hello():
    name = request.args.get("name", "World")
    response = {"name":name + "Hello"}
    return jsonify(response)



@app.route('/getdata/')
def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return jsonify(db)
