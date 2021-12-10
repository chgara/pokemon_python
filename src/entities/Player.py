from src.entities.Entity import Entity


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
        super().__init__('src/assets/entities/player/main.json')

    def update(self):
        pass
