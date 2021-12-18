class Game_Save:
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
