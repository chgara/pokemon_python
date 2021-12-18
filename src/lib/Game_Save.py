class Game_Save:
    """
    This is the main save class.
    It contains all the propeties that a save can have.

    Attributes:
        name (str): The name of the save.
        time (int): The time that the player has been playing.
        player_coordinates (tuple[int, int]): The coordinates of the player.
        map (str): The map that the player is on.

    :param name: The name of the save.
    :param time: The time that the player has been playing.
    :param player_coordinates: The coordinates of the player.
    :param map: The map that the player is on.
    """
    player_coordinates: tuple[int, int]
    name: str
    map: str
    # The time in seconds
    time: int

    def __init__(self, name: str, time: int,
                 player_coordinates: tuple[int, int],
                 map: str):
        self.player_coordinates = player_coordinates
        self.map = map
        self.name = name
        self.time = time
