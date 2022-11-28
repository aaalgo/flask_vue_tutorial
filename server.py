#!/usr/bin/env python3
import json
from flask import Flask, jsonify, request

HOST = '0.0.0.0'
PORT = 8888

app = Flask(__name__)

@app.route('/')
def index ():
    return "Hello, world!"

@app.route('/simple/')
def simple ():
    return "<html><body><h1>Hello, world!</h1></body></html>"

@app.route('/api/hello/')
def hello ():
    out = {
            'text': 'Hello from Flask!',
            'value': 1000
            }
    return jsonify(out)

@app.route('/api/strlen/', methods=['POST'])
def strlen ():
    inp = request.get_json()
    print(inp)
    out = {
            'result': len(inp['input'])
            }
    return jsonify(out)

@app.route('/api/upload/', methods=['POST'])
def upload ():
    #print(request.form['files'])
    print(request.files)
    out = {
            'result': 'xxx'
            }
    return jsonify(out)

if __name__ == '__main__':
    app.run(host=HOST, port=PORT)


