import pygame
from src.lib import config
from src.Game import Game_Context
from src.lib.Game_State import Game_State


class Main:
    game: Game_Context
    screen = pygame.display.set_mode((0, 0))
    clock: pygame.time.Clock

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode(config.Resolution)
        self.clock = pygame.time.Clock()
        self.set_up()

    def set_up(self):
        pygame.display.set_caption("Pokemon")
        self.game: Game_Context = Game_Context(self.screen)
        self.game.set_up()

    def execute(self):
        while self.game.game_state == Game_State.RUNNING:
            self.clock.tick(config.FPS)
            self.game.update()
            pygame.display.flip()


def main():
    main: Main = Main()
    main.execute()


if __name__ == '__main__':
    main()
