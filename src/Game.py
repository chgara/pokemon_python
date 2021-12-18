import pygame
from typing import Type
from src.scenes.main.main import Game
from src.scenes.menu.main import Menu
from src.lib import config
from src.lib.Game_State import Game_State
from src.lib.Game_Sceene import Game_Sceene, Game_Sceenes


class Game_Context:
    """
    The main game class.
    All the game logic is here.
    :screen: The screen to render the game on.
    """
    game_state: Game_State
    game_scenes: dict[Game_Sceenes, Type[Game_Sceene]] = {
        Game_Sceenes.GAME: Game,
        Game_Sceenes.MENU: Menu,
    }
    selected_scene: Game_Sceene

    def __init__(self, screen):
        self.screen = screen
        self.game_state = Game_State.RUNNING
        # Init the menu
        self.selected_scene = self.game_scenes[Game_Sceenes.MENU](
            self.screen, self.change_game_state, self.change_game_scene)

    def set_up(self) -> None:
        """
        Sets up the game.
        :return: None
        """
        # Set the game state to running
        self.selected_scene.set_up()

    def update(self) -> None:
        """
        Updates the game logic.
        :return: None
        """
        self.selected_scene.update()

    def change_game_state(self, new_state: Game_State) -> None:
        """
        Changes the game state.
        :param new_state: The new game state.
        :return: None
        """
        if new_state not in [Game_State.RUNNING, Game_State.PAUSED, Game_State.PAUSED]:
            raise ValueError("Invalid game state")
        self.game_state = new_state

    def change_game_scene(self, new_scene: Game_Sceenes) -> None:
        """
        Changes the game scene.
        To simply change the game scene to other simply pass a new scene.
        :param new_scene: The new game scene.
        :return: None
        """
        # First we need to stop all the sounds
        pygame.mixer.fadeout(100)
        pygame.mixer.stop()
        self.selected_scene = self.game_scenes[new_scene](
            self.screen, self.change_game_state, self.change_game_scene)
        self.set_up()
