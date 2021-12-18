import json
from src.lib import config
from src.scenes.menu.lib.Game_Save import Game_Save


def read_save(save_name: str) -> Game_Save:
    """
    Reads the save with the name 'save_name' and returns a Game_Save object.
    """
    with open(config.SAVES_PATH, "r") as file:
        data = json.load(file)
        coordinates = (data[save_name]["player_coordinates"]
                       [0], data[save_name]["player_coordinates"][1])
        map = data[save_name]["map"]
        time = data[save_name]["time"]
        return Game_Save(save_name, time, coordinates, map)


def create_new_save(new_name: str) -> Game_Save:
    """
    Creates a new save with the name 'new_name'.
    """
    # Create the new save whitout rewrtiing other thata in the json
    with open(config.SAVES_PATH, "r") as file:
        data = json.load(file)
    data[new_name] = {"player_coordinates": [0, 0],
                      "map": config.DEFAULT_MAP,
                      "time": 0}
    with open(config.SAVES_PATH, "w") as file:
        json.dump(data, file)
    return read_save(new_name)


def write_save():
    pass
