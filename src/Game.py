import pygame
from src.utils import config
from src.entities.NPC import NPC
from src.entities.Player import Player
from src.entities.Entity import Entity
from src.utils.Game_State import Game_State
from src.utils.Map_Loader import Map_Loader, NPC_Map_Loader


class Game:
    """
    The main game class.
    All the game logic is here.
    :screen: The screen to render the game on.
    """
    objects: list
    game_state: Game_State
    player: Player
    screen: pygame.Surface
    map: Map_Loader

    def __init__(self, screen):
        self.screen = screen
        self.objects = []
        self.game_state = Game_State.NONE

    def set_up(self) -> None:
        """
        Sets up the game.
        :return: None
        """
        # Create the player and the NPC
        # Add the player and the NPC to the game
        self.player: Player = Player()
        self.objects.append(self.player)

        # Load the map and the NPCs
        self.map = Map_Loader(self.player.entity_loader.map)
        self.load_npcs_from_map(self.map.npcs)

        # Set the game state to running
        self.game_state = Game_State.RUNNING

    def update(self) -> None:
        """
        Updates the game logic.
        :return: None
        """
        self.screen.fill(config.Colors.black)
        self.map.render_map(self.screen)
        self.handle_events()
        for object in self.objects:
            if not isinstance(object, Entity):
                raise TypeError("Objects must be of type Entity")
            object.render(self.screen)

    def load_npcs_from_map(self, npcs: list[NPC_Map_Loader]) -> None:
        """
        Loads all the NPCs from the map.
        :return: None
        """
        for npc in npcs:
            location: str = npc.location
            x_position: int = npc.x_position
            y_position: int = npc.y_position
            self.objects.append(NPC(location, x_position, y_position))

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
