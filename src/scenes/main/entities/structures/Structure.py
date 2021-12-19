from src.scenes.main.entities.Entity import Entity
from src.lib.Game_Sceene import Game_Sceenes
from src.scenes.main.utils.Entity_Loader import Entity_Loader


class Structure(Entity):

    def __init__(self, path_to_entity, x_position, y_position, change_game_scene):
        super().__init__(path_to_entity, x_position, y_position)
        self.change_game_scene = change_game_scene

    def get_Entity_Loader(self, pathToInfo) -> Entity_Loader:
        return Entity_Loader(pathToInfo)

    def on_collision(self, entity: 'Entity') -> None:
        """
        Executed when the structure collides with another entity.
        """
        self.on_collision_with_player()

    def on_collision_with_player(self) -> None:
        """
        Executed when the player collides with the structure.
        """
        self.change_game_scene(Game_Sceenes.MENU)

    def update(self) -> None:
        pass

    def animate_player_image_to(self, d: str) -> None:
        pass

    def move(self, move_to: str, factor: int) -> None:
        pass

    def move_with_animation(self, move_to: str, times: int, seconds_delay: float) -> None:
        pass
