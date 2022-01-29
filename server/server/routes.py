from crypt import methods
from urllib import response
from server import app
from flask import request, jsonify
from flask_api import status
from .game_object import game_object
from random import randrange


objects = []


@app.route("/", methods=["GET"])
def home():
    return """ <br><tt>
███████╗██╗   ██╗██████╗  █████╗ ███████╗████████╗██╗  ██╗███████╗██████╗  <br>
██╔════╝██║   ██║██╔══██╗██╔══██╗██╔════╝╚══██╔══╝██║  ██║██╔════╝██╔══██╗ <br>
███████╗██║   ██║██████╔╝███████║█████╗     ██║   ███████║█████╗  ██████╔╝ <br>
╚════██║██║   ██║██╔══██╗██╔══██║██╔══╝     ██║   ██╔══██║██╔══╝  ██╔══██╗ <br>
███████║╚██████╔╝██████╔╝██║  ██║███████╗   ██║   ██║  ██║███████╗██║  ██║ <br>
╚══════╝ ╚═════╝ ╚═════╝ ╚═╝  ╚═╝╚══════╝   ╚═╝   ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝ <br>
</tt>""".replace(" ", "&nbsp;"), status.HTTP_200_OK


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

    return jsonify({
            "id": player_id,
            "pos": {
                "x": new_player.pos["x"],
                "y": new_player.pos["y"]
            },
            "aether": new_player.aether,
            "destroyed": new_player.destroyed,
            "type": new_player.type
        }), status.HTTP_200_OK


@app.route("/object", methods=["POST"])
def spawn_object():
    request_json = request.json
    new_object = game_object(
        {
            "x": request_json["pos"]["x"],
            "y": request_json["pos"]["y"]
        },
        request_json["aether"],
        request_json["type"]
    )
    objects.append(new_object)
    return jsonify({
        "id": objects.index(new_object)
        }), status.HTTP_200_OK


@app.route("/object", methods=["GET"])
def get_objects():
    response_json = []
    for entity in objects:
        response_json.append({
            "id": objects.index(entity),
            "pos": {
                "x": entity.pos["x"],
                "y": entity.pos["y"]
            },
            "aether": entity.aether,
            "destroyed": entity.destroyed,
            "type": entity.type
        })
    return jsonify(response_json), status.HTTP_200_OK


@app.route("/object", methods=["PUT"])
def batch_update_objects():
    found = False
    miss = False

    request_json = request.json
    for updated_object in request_json:
        local_object = None
        try:
            local_object = objects[updated_object["id"]]
        except IndexError:
            miss = True
            continue
        found = True

        if "destroyed" in updated_object and updated_object["destroyed"] is True:
            local_object.destroy()
        if "pos" in updated_object:
            local_object.pos = {
                "x": updated_object["pos"]["x"],
                "y": updated_object["pos"]["y"]
            }
        if "aether" in updated_object:
            local_object.aether = updated_object["aether"]

    if found and not miss:
        return "OK", status.HTTP_200_OK
    elif found and miss:
        return "Some IDs not found", status.HTTP_207_MULTI_STATUS
    elif miss and not found:
        return "Invalid IDs", status.HTTP_404_NOT_FOUND
