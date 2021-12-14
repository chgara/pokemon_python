import pygame
from src.lib import config
from src.lib.Game_State import Game_State
from src.lib.Game_Sceene import Game_Sceene
from src.scenes.main.entities.Player import Player
from src.scenes.main.entities.Entity import Entity
from src.scenes.main.entities.Entity_Fabric import Entity_Fabric
from src.scenes.main.utils.Map_Loader import Entities_Map_Loader, Map_Loader


class Game(Game_Sceene):
    """
    The main game class.
    All the game logic is here.
    :screen: The screen to render the game on.
    """
    objects: list[Entity]
    player: Player
    map: Map_Loader
    camera: tuple[int, int]

    def __init__(self, screen: pygame.Surface, change_game_state, change_game_scene):
        super().__init__(screen, change_game_state, change_game_scene)
        self.objects = []
        self.camera = (0, 0)

    def set_up(self) -> None:
        """
        Sets up the game.
        :return: None
        """
        # Add the player to the game
        self.player: Player = Player()
        self.objects.append(self.player)

        # Load the map and the entities
        self.map = Map_Loader(self.player.entity_loader.map)
        self.load_entities_from_map(self.map.entities)

        # Set the game state to running
        self.change_game_state(Game_State.RUNNING)

    def update(self) -> None:
        """
        Updates the game logic.
        :return: None
        """
        self.screen.fill(config.Colors.black)

        # Handle events
        self.handle_events()

        # Update the camera position
        self.determine_camera()

        # Update the entities
        self.update_entities()

        self.map.render_map(self.screen, self.camera)
        for object in self.objects:
            if not isinstance(object, Entity):
                raise TypeError("Objects must be of type Entity")
            object.render(self.screen, self.camera)

    # Using the observer entities
    def update_entities(self,) -> None:
        """
        Updates the entities state
        :return: None
        """
        for object in self.objects:
            new_objects = [] + self.objects
            new_objects.remove(object)
            object.update_entitie_state(new_objects)

    def load_entities_from_map(self, entities: list[Entities_Map_Loader]) -> None:
        """
        Loads the entities from the map.
        :return: None
        """
        for entity in entities:
            location: str = entity.location
            x_position: int = entity.x_position
            y_position: int = entity.y_position
            new_entity: Entity = Entity_Fabric(
                location, x_position, y_position).entity
            self.objects.append(new_entity)

    def determine_camera(self):
        """
        Determines the camera position.
        :return: None
        """
        max_x_position: int = round(
            self.map.width - config.Resolution[0])
        max_y_position: int = round(
            self.map.height - config.Resolution[1])

        x_position = self.player.x_position - config.Resolution[0] // 2
        y_position = self.player.y_position - config.Resolution[1] // 2

        if x_position <= max_x_position and x_position >= 0:
            self.camera = (x_position, self.camera[1])
        elif x_position < 0:
            self.camera = (0, self.camera[1])
        elif x_position > max_x_position:
            self.camera = (max_x_position, self.camera[1])

        if y_position <= max_y_position and y_position >= 0:
            self.camera = (self.camera[0], y_position)
        elif y_position < 0:
            self.camera = (self.camera[0], 0)
        elif y_position > max_y_position:
            self.camera = (self.camera[0], max_y_position)

    def handle_events(self):
        """
        Handles all events.
        :return: None
        """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.change_game_state(Game_State.ENDED)
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.change_game_state(Game_State.ENDED)
            keys = pygame.key.get_pressed()
            if keys[pygame.K_w]:
                self.player.move('up')
            if keys[pygame.K_s]:
                self.player.move('down')
            if keys[pygame.K_d]:
                self.player.move('right')
            if keys[pygame.K_a]:
                self.player.move('left')
