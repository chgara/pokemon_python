from src.entities.Entity import Entity
from src.utils.Entity_Loader import Entity_Loader
from src.utils.Player_Loader import Player_Loader


class Player(Entity):
    """
    Player class
    !!!!!!!!!!!!!!!!!!!!!!!!!IMPORTANT!!!!!!!!!!!!!!!!!!!!!!!!!!
    !!!!!The name of the entity is where assets are stored!!!!!!
    !!!!!!!!!!!!!!!!!!!!!!!!!IMPORTANT!!!!!!!!!!!!!!!!!!!!!!!!!!
    :param name: name of the entity
    :param x_position: x position of the entity
    :param y_position: y position of the entity
    """

    def __init__(self):
        super().__init__('src/assets/entities/player/main.json', 0, 0)

    def get_Entity_Loader(self, pathToInfo) -> Entity_Loader:
        """
        Get the entity loader
        :return Entity_Loader:
        """
        return Player_Loader(pathToInfo)

    def update(self):
        pass
