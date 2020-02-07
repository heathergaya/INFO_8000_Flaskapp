from flask import Flask, escape, request, jsonify

app = Flask(__name__)

@app.route('/')
def hello():
    name = request.args.get("name", "World")
    response = {"name":name}
    return jsonify(response)
