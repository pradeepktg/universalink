from flask import Flask,url_for,send_from_directory, json
import json

app = Flask(__name__)
@app.route('/')
@app.route("/.well-known")
def index():
    return "<h1>Welcome to Universal Link - iOS<h1>"

@app.route("/.well-known/<path:filename>", methods=['GET','POST'])
def wellknown(filename):
    return send_from_directory(directory=app.root_path + '/well-known/',
                                                      filename=filename,
                                                      mimetype='application/json')
