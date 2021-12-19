import json
from src.lib import config
from src.lib.Game_Save import Game_Save


def read_save(save_name: str) -> Game_Save:
    """
    Reads the save with the name 'save_name' and returns a Game_Save object.
    :param save_name: The name of the save to read.
    :return: A Game_Save object.
    """
    with open(config.SAVES_PATH, "r") as file:
        data = json.load(file)
        coordinates = (data[save_name]["player_coordinates"]
                       [0], data[save_name]["player_coordinates"][1])
        map = data[save_name]["map"]
        time = data[save_name]["time"]
        return Game_Save(save_name, time, coordinates, map, save_name)


def create_new_save(new_name: str) -> Game_Save:
    """
    Creates a new save with the name 'new_name'.
    :param new_name: The name of the new save.
    :return: A Game_Save object.
    """
    # Create the new save whitout rewrtiing other thata in the json
    with open(config.SAVES_PATH, "r") as file:
        data = json.load(file)
    data[new_name] = {"player_coordinates": [425, 500],
                      "map": config.DEFAULT_MAP,
                      "time": 0}
    with open(config.SAVES_PATH, "w") as file:
        json.dump(data, file)
    return read_save(new_name)


def write_save(coordinates: tuple[int, int]):
    """
    Writes the current Game_Save object to the json file.
    """
    # Read map and play name from players json
    map = ''
    play_name = ''
    with open(config.PLAYER_PATH, 'r') as file:
        data = json.load(file)
        map = data["map"]
        play_name = data["actual_save"]

    # Write the info to the json file
    with open(config.SAVES_PATH, "r") as file:
        data = json.load(file)
        data[play_name] = {"player_coordinates": [coordinates[0], coordinates[1]],
                           "map": map,
                           "time": 0}
    with open(config.SAVES_PATH, "w") as file:
        json.dump(data, file)
