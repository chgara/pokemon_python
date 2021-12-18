from threading import Timer
import pygame
from src.lib import config
from src.lib.Game_Save import Game_Save
from src.utils.save_utils import create_new_save


class New_Save:
    padding: int = 40 * config.SCALE
    is_expanded: bool
    btn: pygame.Rect
    btn_positon: tuple[int, int] = (0, 0)
    bg_rect: pygame.Rect
    input_times: int = 0

    def __init__(self, load):
        self.is_expanded = False
        x_pos = config.Resolution[0] - round(self.padding * 1.5)
        y_pos = config.Resolution[1] - round(self.padding * 1.5)
        self.btn_positon = (x_pos, y_pos)
        self.load = load

    def update_click(self, position: tuple[int, int]) -> None:
        """
        Update the menu item when clicked
        :param position: tuple[int, int]
        """
        # if the mouse is in the rect
        if self.btn.collidepoint(position):
            self.is_expanded = not self.is_expanded

    def ask_for_name(self) -> None:
        """
        Ask the user for a name for the save
        :return: str
        """
        name = input("Enter a name for your save: ")
        new_save: Game_Save = create_new_save(name)
        self.load(new_save)

    def render_btn(self, screen: pygame.Surface) -> None:
        """
        Given a screen, render the background of the menu save item
        :param screen: pygame.Surface
        """
        self.btn = pygame.Rect(self.btn_positon[0], self.btn_positon[1],
                               self.padding, self.padding)
        pygame.draw.rect(screen, config.Colors.white, self.btn)

        # draw a purple border around the rect
        pygame.draw.rect(screen, config.Colors.red, self.btn, 2)

        # draw the text + in the middle of the rect
        font = pygame.font.Font(config.FONT_PATH2, config.FONT_SIZE*2)
        text = font.render("+", True, config.Colors.purple)
        text_rect = text.get_rect()
        text_rect.center = (self.btn.centerx, self.btn.centery+5*config.SCALE)
        screen.blit(text, text_rect)

    def render_bg(self, screen: pygame.Surface) -> None:
        """
        Given a screen, render the background of the menu save item
        :param screen: pygame.Surface
        """
        self.bg_rect = pygame.Rect(0, 0, config.Resolution[0],
                                   config.Resolution[1])
        pygame.draw.rect(screen, config.Colors.purple, self.bg_rect)

    def render_input(self, screen: pygame.Surface) -> None:
        """
        Render the input box on the middle of the screen
        :param screen: pygame.Surface
        """
        # create the text
        font = pygame.font.Font(config.FONT_PATH, round(config.FONT_SIZE*1.5))
        text = font.render("Enter a name for your save:",
                           True, config.Colors.white)
        text_rect = text.get_rect()
        text_rect.topleft = (self.padding, self.padding)
        screen.blit(text, text_rect)

        # Help text
        font = pygame.font.Font(config.FONT_PATH2, config.FONT_SIZE)
        text = font.render("At the moment enter the input in the console :)",
                           True, config.Colors.white)
        text_rect = text.get_rect()
        text_rect.center = (config.Resolution[0]//2, config.Resolution[1]//2)
        screen.blit(text, text_rect)

        if self.input_times < 1:
            self.input_times += 1
            Timer(5, self.ask_for_name).start()

    def render(self, screen: pygame.Surface) -> None:
        if self.is_expanded:
            self.render_bg(screen)
            self.render_input(screen)
            self.render_btn(screen)
        else:
            self.render_btn(screen)
