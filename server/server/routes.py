from curses.panel import new_panel
import imp
from operator import indexOf
from server import app
from flask import request
from flask_api import status
from .game_object import game_object
from random import randrange
import os
import json


objects = []


@app.route("/", methods=["GET"])
def home():
    return """
███████╗██╗   ██╗██████╗  █████╗ ███████╗████████╗██╗  ██╗███████╗██████╗  <br>
██╔════╝██║   ██║██╔══██╗██╔══██╗██╔════╝╚══██╔══╝██║  ██║██╔════╝██╔══██╗ <br>
███████╗██║   ██║██████╔╝███████║█████╗     ██║   ███████║█████╗  ██████╔╝ <br>
╚════██║██║   ██║██╔══██╗██╔══██║██╔══╝     ██║   ██╔══██║██╔══╝  ██╔══██╗ <br>
███████║╚██████╔╝██████╔╝██║  ██║███████╗   ██║   ██║  ██║███████╗██║  ██║ <br>
╚══════╝ ╚═════╝ ╚═════╝ ╚═╝  ╚═╝╚══════╝   ╚═╝   ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝ <br>
""", status.HTTP_200_OK


@app.route("/register", methods=["POST"])
def register():
    new_player = game_object(
        {
            "x": randrange(app.config['SPAWN_AREA']["x"]),
            "y": randrange(app.config['SPAWN_AREA']["y"])
        },
        False,
        game_object.PLAYER
    )
    objects.append(new_player)
    player_id = objects.index(new_player)
    print(f"Registering Player. ID: {player_id}")

    json_str = json.dumps({
            "id": player_id,
            "pos": {
                "x": new_player.pos["x"],
                "y": new_player.pos["y"]
            },
            "aether": new_player.aether,
            "destroyed": new_player.destroyed,
            "type": new_player.type
        }
    )

    return json_str, status.HTTP_200_OK


@app.route("/object", methods=["POST"])
def spawn_object():
    return "", status.HTTP_200_OK
