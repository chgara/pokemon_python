from src.scenes.main.entities.Entity import Entity
from src.scenes.main.entities.structures.Structure import Structure


class Colidable_Structure(Structure):
    def __init__(self, path_to_entity, x_position, y_position):
        super().__init__(path_to_entity, x_position, y_position)

    def on_collision(self, entity: 'Entity') -> None:
        """
        Executed when the structure collides with another entity.
        """
        self.on_collision_with_player()

    def on_collision_with_player(self) -> None:
        """
        Executed when the player collides with the structure.
        """
        print("Structure collision with player")
