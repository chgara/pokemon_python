import json
from src.scenes.main.utils.Entity_Loader import Entity_Loader


class Player_Loader(Entity_Loader):
    map: str
    coordinates: tuple[int, int]

    def __init__(self, pathToInfo: str):
        super().__init__(pathToInfo)

        # Load the map from the json pathToInfo
        with open(pathToInfo, 'r') as f:
            data = json.load(f)
            self.map = data['map']
            self.coordinates = (data['coordinates'][0], data['coordinates'][1])
