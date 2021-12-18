import pygame
from enum import Enum
from abc import ABC, abstractmethod
from src.lib.Game_Sound import Game_Sound
from src.lib.Game_State import Game_State


class Game_Sceene(ABC):
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
        Updates the game sceene
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
    GAME = 'GAME'
    MENU = 'MENU'
    BATTLE = 'BATTLE'
    PAUSED = 'PAUSED'
