#!/usr/bin/env python

from flask import Flask
from flask import request
from flask import json
from flask import jsonify

app = Flask(__name__)

@app.route("/", methods=["GET"])
def hello():
    print repr(request)
    print dir(request)
    print "HTTP Method: %s " % request.method

    resp = jsonify(hello="world", version="0.0.1")
    return resp

if __name__ == '__main__':
    app.run(debug=True)


# python .. decorator .