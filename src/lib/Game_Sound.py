import pygame


class Game_Sound:
    should_sound_infinite: bool
    sound_path: str
    sound_volume: float
    sound: pygame.mixer.Sound

    def __init__(self, sound_path: str, sound_volume: float = 0.5, should_sound_infinite: bool = False):
        self.should_sound_infinite = should_sound_infinite
        self.sound_path = sound_path
        self.sound_volume = sound_volume
        self.sound = pygame.mixer.Sound(self.sound_path)
        self.sound.set_volume(self.sound_volume)

    def play(self):
        if self.should_sound_infinite:
            self.sound.play(-1)
        else:
            self.sound.play()

    def stop(self):
        self.sound.stop()
