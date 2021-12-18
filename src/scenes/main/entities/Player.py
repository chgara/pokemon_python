from src.lib import config
from src.lib.Game_Sound import Game_Sound
from src.scenes.main.entities.Entity import Entity
from src.scenes.main.utils.Entity_Loader import Entity_Loader
from src.scenes.main.utils.Player_Loader import Player_Loader


class Player(Entity):
    """
    """

    def __init__(self):
        path = config.PLAYER_PATH
        self.entity_loader = self.get_Entity_Loader(path)
        super().__init__(path, self.entity_loader.coordinates[0],
                         self.entity_loader.coordinates[1])

    def get_Entity_Loader(self, pathToInfo) -> Player_Loader:
        """
        Get the entity loader
        :return Entity_Loader:
        """
        return Player_Loader(pathToInfo)

    def on_collision(self, entity: 'Entity') -> None:
        return super().on_collision(entity)

    def update(self):

        # If the player collides with something then play the sound
        # if self.check_collision(self.x_position, self.y_position):
        #     collision_sound: Game_Sound = Game_Sound(
        #         config.Sounds.collision, sound_volume=0.7)
        #     collision_sound.play()
        #     print("sound")
        pass
