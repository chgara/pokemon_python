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

    The game structure is as follows:
    - Game_Context -> Class that holds all the game logic.
        - Game_Sceene -> Abstract class that ensurs that the childs have some common methods.
            - Game -> The main game scene.
            - Menu -> The main menu scene.

    Atributes:
    - screen: The screen of the game.
    - game_state: The current game state and is of the type Game_State (An Enum containing possible values)
    - game_scenes:
        The possible game scenes and is a dictionary with the scene as the key and the class as the value.
        The scene that is the key is of the type Game_Sceenes (An Enum containing possible values)
    - selected_scene: The current game scene and is of the type (Game_Sceene)

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

        ######## Initilize the menu scene ########
        self.selected_scene = self.game_scenes[Game_Sceenes.MENU](
            self.screen, self.change_game_state, self.change_game_scene)

    def set_up(self) -> None:
        """
        It actually sets up the scene method 'set_up'
        :return: None
        """
        # Set the game state to running
        self.selected_scene.set_up()

    def update(self) -> None:
        """
        Runns the 'update' method of the current game scene.
        """
        self.selected_scene.update()

    def change_game_state(self, new_state: Game_State) -> None:
        """
        Changes the game state to the provided state.
        :param new_state: The new game state that is a Game_State enum propety.
        :return: None
        """
        # Eval if the provided state is valid
        if new_state not in [Game_State.RUNNING, Game_State.PAUSED, Game_State.ENDED]:
            raise ValueError("Invalid game state")
        self.game_state = new_state

    def change_game_scene(self, new_scene: Game_Sceenes) -> None:
        """
        Changes the game scene.
        To simply change the game scene to other simply pass a new scene.
        :param new_scene: The new game scene and is of type Game_Sceenes (An Enum containing possible values)
        :return: None
        """
        # First we need to stop all the sounds
        pygame.mixer.fadeout(100)
        pygame.mixer.stop()

        # Create the new scene and set it as the current scene
        self.selected_scene = self.game_scenes[new_scene](
            self.screen, self.change_game_state, self.change_game_scene)
        # Set up the scene
        self.set_up()
