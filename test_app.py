from flask import Flask, escape, request, jsonify
import sqlite3
from flask import g

app = Flask(__name__)

DATABASE = '/home/heather_e_gaya/INFO_8000_Flaskapp/birdinfo.db'

def connect_db():
    return sqlite3.connect(DATABASE)

@app.before_request
def before_request():
    g.db = connect_db()

@app.teardown_request
def teardown_request(exception):
    if hasattr(g, 'db'):
        g.db.close()

def query_db(query, args=(), one=False):
    cur = g.db.execute(query, args)
    rv = [dict((cur.description[idx][0], value)
               for idx, value in enumerate(row)) for row in cur.fetchall()]
    return (rv[0] if rv else None) if one else rv

@app.route('/')
def hello():
    name = request.args.get("name", "World")
    response = {"name":name + " Hello"}
    return jsonify(response)



@app.route('/viewtable/', methods=['GET'])
def hello2():
    data = query_db("SELECT * FROM ?")
    return jsonify(data)
