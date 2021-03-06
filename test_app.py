from flask import Flask, escape, request, jsonify, make_response
import sqlite3
from flask import g
from flask_httpauth import HTTPBasicAuth


app = Flask(__name__)

auth = HTTPBasicAuth()

USER_DATA = {
    "admin": "yaybirds"
}

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
    return "<h1>This is the home page for a fake bird database </h1><p>Oh boy birds!</p></p>Typing /viewtable?myquery= allows you to view database </p></p>Typing /addstuff?info= after allows information entry into database </p>"


@app.route('/testy')
def hello():
    name = request.args.get("name", "World")
    response = {"name":name + " Hello"}
    return jsonify(response)


@app.route('/viewtable', methods=['GET'])
def tableview():
    myquery = request.args.get("myquery")
    data = query_db(myquery)
    return jsonify(data)

#can't put without "login" 
@auth.verify_password
def verify(username, password):
    if not (username and password):
        return False
    return USER_DATA.get(username) == password

@auth.login_required
@app.route('/addstuff', methods=['PUT', 'GET'])
def addinfo():
    stuff = request.args.get("info")
    g.db.execute(stuff)
    g.db.commit()
    return "<p>The data was entered. Check /viewtable?myquery= to see changes in database </p>"
