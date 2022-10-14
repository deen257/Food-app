from flask import Flask , request, jsonify, render_template
from flask_cors import CORS 
import os
from collections import Mapping

app = Flask(__name__)



@app.route("/")
def index():
    return render_template("index.html")

