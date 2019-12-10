#!/usr/bin/python3

import json
import random

from flask import Flask
from flask import render_template
from flask import request
# import werkzeug

app = Flask(__name__)


@app.route("/")
@app.route("/index")
def home():
    return '''<a href="poems">Random Poem</a>
    <p>
        <a href="poemuploader">Upload a Poem</a>'''


@app.route("/poems")
def randpoem():
    # randomly select a poem
    return random.choice(list(pythonpoems.values()))


@app.route("/poems/<pn>")
def send(pn):
    if pythonpoems.get(pn):
        return pythonpoems.get(pn)
    else:
        return "the key does not exist"


@app.route("/poemuploader", methods=["GET", "POST"])
def poemuploader():
    if request.method == "POST":
        f = request.files["file"]
        f = f.read().decode()  # read the new poem out of the uploaded file
        highestkey = pythonpoems.keys()
        f = pythonpoems[str(int(sorted(highestkey)[-1]) + 1)]
        with open("poem.json", "w") as npj:
            json.dump(pythonpoems, npj)
        return "New poem has been added to the database"

    if request.method == "GET":
        return render_template("upload.html")


if __name__ == '__main__':
    with open("poem.json") as pj:
        pythonpoems = json.load(pj)  # convert poems.json data to pythonic structure
    app.run(port=5210)
