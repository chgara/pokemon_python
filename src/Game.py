import pygame
from src.utils import config
from src.entities.Player import Player
from src.entities.NPC import NPC
from src.entities.Entity import Entity
from src.utils.Game_State import Game_State


class Game:
    """
    The main game class.
    All the game logic is here.
    :screen: The screen to render the game on.
    """
    objects: list
    game_state: Game_State
    player: Player

    def __init__(self, screen):
        self.screen = screen
        self.objects = []
        self.game_state = Game_State.NONE

    def set_up(self) -> None:
        self.player: Player = Player()
        npc: NPC = NPC('src/assets/entities/npcs/buisnessman/main.json')
        self.objects.append(self.player)
        self.objects.append(npc)
        self.game_state = Game_State.RUNNING

    def update(self) -> None:
        self.screen.fill(config.Colors.black)
        self.handle_events()
        for object in self.objects:
            if not isinstance(object, Entity):
                raise TypeError("Objects must be of type Entity")
            object.render(self.screen)

    def handle_events(self):
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
