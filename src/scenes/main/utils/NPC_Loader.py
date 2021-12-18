import json
import warnings
from src.scenes.main.utils.Entity_Loader import Entity_Loader


class NPC_Loader(Entity_Loader):
    dialog: str

    def __init__(self, pathToInfo: str):
        super().__init__(pathToInfo)

        # Load the map from the json pathToInfo
        with open(pathToInfo, 'r') as f:
            data = json.load(f)
            # Verify that the dialog exists
            if 'dialog' in data:
                self.dialog = data['dialog']
            else:
                self.dialog = ''
                warnings.warn(f'No dialog found for NPC {self.name}')
