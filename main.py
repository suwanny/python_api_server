#!/usr/bin/env python

import sys
import os.path

lib_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'lib')
sys.path.append(lib_dir)

from flask import Flask
from flask import request
from flask import json
from flask import jsonify
from flask import render_template

from controller.main_controller import MainController

app         = Flask(__name__)
controller  = MainController()


@app.route('/')
def index():
  print "path: %s" % lib_dir
  return render_template('index.html', name="Dude")

@app.route("/hello", methods=["GET"])
def hello():
  data = controller.hello(request)
  return jsonify(data)

@app.route("/get", methods=["GET"])
def get():
  args = request.args.get("params").split(",")
  def u2ascii(s): return s.encode("ascii", "ignore")
  args = map(u2ascii, args)
  print args
  def print_args(x,y,z): return "%s, %s, %s" % (x,y,z)
  return print_args(*args)

if __name__ == '__main__':
  app.run(host="0.0.0.0", debug=True)

