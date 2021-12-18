import pygame
from src.lib import config
from src.lib.Game_Save import Game_Save


class Menu_Save:
    game_save: Game_Save
    width: int = 440 * config.SCALE
    height: int = 100 * config.SCALE
    padding: int = 40 * config.SCALE
    bg_rect: pygame.Rect

    def __init__(self, save: Game_Save, load):
        self.game_save = save
        self.load = load

    def update_click(self, position: tuple[int, int]) -> None:
        """
        Update the menu item when clicked
        :param position: tuple[int, int]
        """
        # if the mouse is in the rect
        if self.bg_rect.collidepoint(position):
            self.load(self.game_save)

    def render_save_name(self, position: tuple[int, int], screen: pygame.Surface) -> None:
        font = pygame.font.Font(config.FONT_PATH, config.FONT_SIZE)
        text = font.render(f'Save:   {self.game_save.name}',
                           True, config.Colors.blue)
        text_rect = text.get_rect()
        # set the text in the drawed rect with a little padding
        text_rect.topleft = (position[0] + self.padding,
                             position[1] + round(self.padding / 1.75))
        screen.blit(text, text_rect)

    def render_time_played(self, position: tuple[int, int], screen: pygame.Surface) -> None:
        font = pygame.font.Font(config.FONT_PATH, config.FONT_SIZE)
        text = font.render(
            f'Time played:   {self.game_save.time}', True, config.Colors.blue)
        text_rect = text.get_rect()
        # set the text in the drawed rect with a little padding
        text_rect.topleft = (position[0] + self.padding,
                             round(position[1] + self.padding // 2 +
                                   self.padding / 1.75 + config.FONT_SIZE))
        screen.blit(text, text_rect)

    def render_bg(self, screen: pygame.Surface, position: tuple[int, int]) -> None:
        """
        Given a screen, render the background of the menu save item
        :param screen: pygame.Surface
        """
        # draw a withe rect startting on the provided position
        # save the rect in the class
        self.bg_rect = pygame.Rect(position[0], position[1],
                                   self.width, self.height)
        # draw the rect
        pygame.draw.rect(screen, config.Colors.white, self.bg_rect)

        # draw a green border around the rect
        pygame.draw.rect(screen, config.Colors.green,
                         (position[0], position[1], self.width, self.height), 2)

    def render(self, screen: pygame.Surface, position: tuple[int, int]) -> None:
        self.render_bg(screen, position)
        self.render_save_name(position, screen)
        self.render_time_played(position, screen)
