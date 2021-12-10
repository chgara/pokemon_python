import json
from src.utils.Entity_Loader import Entity_Loader


class Player_Loader(Entity_Loader):
    map: str

    def __init__(self, pathToInfo: str):
        super().__init__(pathToInfo)

        # Load the map from the json pathToInfo
        with open(pathToInfo, 'r') as f:
            data = json.load(f)
            self.map = data['map']
