import pygame
from src.utils import config
from src.entities.Player import Player
from src.entities.Entity import Entity
from src.entities.Entity_Fabric import Entity_Fabric
from src.utils.Game_State import Game_State
from src.utils.Map_Loader import Entities_Map_Loader, Map_Loader


class Menu:
    """
    """
    objects: list[Entity]
    game_state: Game_State
    player: Player
    screen: pygame.Surface
    map: Map_Loader
    camera: tuple[int, int]

    def __init__(self, screen):
        self.screen = screen
        self.objects = []
        self.game_state = Game_State.NONE
        # self.camera = (0, 0)

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
        self.game_state = Game_State.RUNNING

    def update(self) -> None:
        """
        Updates the game logic.
        :return: None
        """
        self.screen.fill(config.Colors.bl)

        # Handle events
        self.handle_events()
        for object in self.objects:
            if not isinstance(object, Entity):
                raise TypeError("Objects must be of type Entity")
            object.render(self.screen, self.camera)

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
                self.game_state = Game_State.ENDED
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.game_state = Game_State.ENDED
            keys = pygame.key.get_pressed()
            if keys[pygame.K_w]:
                self.player.move('up')
            if keys[pygame.K_s]:
                self.player.move('down')
            if keys[pygame.K_d]:
                self.player.move('right')
            if keys[pygame.K_a]:
                self.player.move('left')
