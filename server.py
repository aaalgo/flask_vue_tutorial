#!/usr/bin/env python3
import json
from flask import Flask, jsonify, request, redirect

HOST = '0.0.0.0'
PORT = 8888

app = Flask(__name__)

@app.route('/')
def index ():
    return redirect("/static/index.html", code=302)


@app.route('/simple/')
def simple ():
    return "<html><body><h1>Hello, world!</h1></body></html>"

@app.route('/api/hello/')
def hello ():
    out = {
            'text': 'Hello from Flask! (Flask is Working!)',
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
    f = request.files['file']
    content = f.read()
    # The file can be saved by
    # f.save("path")
    # https://tedboy.github.io/flask/generated/generated/werkzeug.FileStorage.html
    out = {
            'result': len(content)
          }
    return jsonify(out)

if __name__ == '__main__':
    app.run(host=HOST, port=PORT)


