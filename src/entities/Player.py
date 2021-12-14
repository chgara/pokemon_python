from src.entities.Entity import Entity
from src.utils.Entity_Loader import Entity_Loader
from src.utils.Player_Loader import Player_Loader


class Player(Entity):
    """
    """

    def __init__(self):
        path: str = 'src/assets/entities/player/main.json'
        self.entity_loader = self.get_Entity_Loader(path)
        super().__init__(path, self.entity_loader.coordinates[0],
                         self.entity_loader.coordinates[1])

    def get_Entity_Loader(self, pathToInfo) -> Player_Loader:
        """
        Get the entity loader
        :return Entity_Loader:
        """
        return Player_Loader(pathToInfo)

    def update(self):
        pass
