class Colors:
    black: str = '#000000'
    white: str = '#ffffff'
    red: str = '#ff0000'
    green: str = '#00ff00'
    blue: str = '#0000ff'


FPS: int = 24
SCALE: int = 1
IMAGES_PATH = 'src/assets/imgs/'

PLAYER_PATH: str = 'src/assets/entities/player/main.json'

# class Resolution:
#     MEDIUM: tuple[int, int] = (1280, 960)
#     HIGH: tuple[int, int] = (1875, 975)
#     LOW: tuple[int, int] = (640, 480)

Resolution = (640*SCALE, 480*SCALE)
