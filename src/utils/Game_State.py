from enum import Enum


class Game_State(Enum):
    NONE = 0
    RUNNING = 1
    ENDED = 2
    PAUSED = 3
