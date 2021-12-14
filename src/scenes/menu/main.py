import pygame
from src.lib import config
from src.lib.Game_State import Game_State


class Menu:
    game_state: Game_State
    screen: pygame.Surface

    def __init__(self, screen):
        self.screen = screen
        self.game_state = Game_State.RUNNING

    def set_up(self) -> None:
        """
        Load the data to show in the menu.
        :return: None
        """

    def update(self) -> None:
        """
        Updates the menu.
        :return: None
        """
        self.screen.fill(config.Colors.blue)
        self.handle_events()
        # render de menu

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
