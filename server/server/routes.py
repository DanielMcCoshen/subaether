from server import app
from flask import request, render_template, make_response
from flask_api import status
import os
import json


@app.route("/", methods=["GET"])
def home():
    return render_template("home.html", categories=app.config["CATEGORIES"]), status.HTTP_200_OK


@app.route("/categories/<category>", methods=["GET"])
def list_category(category):
    recepies = []
    for recepie in os.listdir(f"{app.config['RECEPIE_PATH']}/{category}/"):
        recepies.append(os.path.splitext(recepie)[0])
    return render_template("category.html", category=category, recepies=recepies), status.HTTP_200_OK


@app.route("/recepies/<recepie>", methods=["GET"])
def show_recepie(recepie):
    with open(f"{app.config['RECEPIE_PATH']}/all_recepies/{recepie}.json") as recepie_file:
        recepie_json = json.loads(recepie_file.read())
        return render_template("recepie.html", name=recepie, json=recepie_json), status.HTTP_200_OK
