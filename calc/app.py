# Put your app in here.
from flask import Flask, request
from operations import *

app = Flask(__name__)


@app.route('/add')
def addRoute():
    a = request.args["a"]
    b = request.args["b"]
    c = add(int(a),int(b))
    return str(c)

@app.route('/sub')
def subRoute():
    a = request.args["a"]
    b = request.args["b"]
    c = sub(int(a),int(b))
    return str(c)

@app.route('/mult')
def multRoute():
    a = request.args["a"]
    b = request.args["b"]
    c = mult(int(a),int(b))
    return str(c)

@app.route('/div')
def divRoute():
    a = request.args["a"]
    b = request.args["b"]
    c = div(int(a),int(b))
    return str(c)