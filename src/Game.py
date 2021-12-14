import pygame
from typing import Type
from src.scenes.main.main import Game
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
    game_scenes: dict[Game_Sceenes, Type[Game]] = {
        Game_Sceenes.GAME: Game,
    }
    selected_scene: Game

    def __init__(self, screen):
        self.screen = screen
        self.selected_scene = Game(
            self.screen, self.change_game_state, self.change_game_scene)
        self.game_state = Game_State.RUNNING

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
        self.game_state = new_state

    def change_game_scene(self, new_scene: Game_Sceenes) -> None:
        """
        Changes the game scene.
        To simply change the game scene to other simply pass a new scene.
        :param new_scene: The new game scene.
        :return: None
        """
        self.selected_scene = self.game_scenes[new_scene](
            self.screen, self.change_game_state, self.change_game_scene)
        self.set_up()
