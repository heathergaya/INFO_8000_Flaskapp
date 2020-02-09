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

@app.route('/', methods=['GET'])
def home():
    return "<h1>This is the home page for a fake bird database </h1><p>Oh boy birds!</p></p>Typing /testy after the web address gives you the practice page from class </p>"


@app.route('/testy')
def hello():
    name = request.args.get("name", "World")
    response = {"name":name + " Hello"}
    return jsonify(response)



@app.route('/viewtable', methods=['GET'])
def hello2():
    myquery = request.args.get("myquery")
    #data = query_db(myquery)
    return jsonify(myquery)
