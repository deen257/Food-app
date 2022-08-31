from flask import Flask , request, jsonify, render_template
from flask_cors import CORS 
import os
from collections import Mapping

app = Flask(__name__)
CORS(app)



@app.after_request
def after_request(response):
    response.headers.add("Access-Control-Allow-Headers", 'Content-Type, Authorization')
    response.headers.add("Access-Control-Allow-Headers", "GET,POST,DELETE,PATCH,OPTIONS")
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response 

@app.route("/")
def index():
    return render_template("index.html")

