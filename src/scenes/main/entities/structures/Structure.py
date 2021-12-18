from src.scenes.main.entities.Entity import Entity
from src.scenes.main.utils.Entity_Loader import Entity_Loader


class Structure(Entity):

    def __init__(self, path_to_entity, x_position, y_position):
        super().__init__(path_to_entity, x_position, y_position)

    def get_Entity_Loader(self, pathToInfo) -> Entity_Loader:
        return Entity_Loader(pathToInfo)

    def on_collision(self, entity: 'Entity') -> None:
        """
        Implement this method in the child class
        if you want to do something when the player collides with the structure
        :param entity: The entity that collided with the structure
        :return: None
        """
        pass

    def update(self) -> None:
        pass

    def animate_player_image_to(self, d: str) -> None:
        pass

    def move(self, move_to: str, factor: int) -> None:
        pass

    def move_with_animation(self, move_to: str, times: int, seconds_delay: float) -> None:
        pass
