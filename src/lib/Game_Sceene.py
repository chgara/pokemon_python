import pygame
from enum import Enum
from abc import ABC, abstractmethod
from src.lib.Game_Sound import Game_Sound
from src.lib.Game_State import Game_State


class Game_Sceene(ABC):
    """
    Abstract class for all game sceenes.
    It ensures that all the sceenes have a update method an a set_up method.
    And also it ensures that all the sceenes have the method change_game_state and change_game_scene

    Atributes:
        screen:
            The screen where the sceene will be drawn

        change_game_state:
            Function that changes the game state (Game_State)
            To view how it works please go to Game_Context class.

        change_game_scene:
            Function that changes the game scene (Game_Sceene)
            To view how it works please go to Game_Context class.

        bg_music:
            The background music of the sceene (Game_Sound)
            To view how it works please go to Game_Sound class.
    """
    screen: pygame.Surface
    bg_music: Game_Sound

    def __init__(self, screen: pygame.Surface, music_path: str, change_game_state, change_game_scene):
        self.screen = screen
        self.change_game_state = change_game_state
        self.change_game_scene = change_game_scene

        # All the scenes should have a background music
        self.bg_music = Game_Sound(
            music_path, sound_volume=0.3, should_sound_infinite=True)

    @abstractmethod
    def set_up(self) -> None:
        """
        Sets up the game sceene
        """
        pass

    # You should render the game sceene here
    @abstractmethod
    def update(self) -> None:
        """
        Updates the game sceene logic
        """
        pass

    def handle_events(self):
        """
        Handles mouse and keyboard events
        """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.change_game_state(Game_State.ENDED)
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.change_game_state(Game_State.ENDED)


class Game_Sceenes(Enum):
    """
    Enum for all the possible game sceenes
    """
    GAME = 'GAME'
    MENU = 'MENU'
    BATTLE = 'BATTLE'
    PAUSED = 'PAUSED'
