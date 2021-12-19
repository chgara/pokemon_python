import pygame
from src.lib import config
from src.scenes.main.entities.Entity import Entity
from src.scenes.main.entities.player.Player import Player
from src.scenes.main.utils.NPC_Loader import NPC_Loader


class NPC(Entity):
    is_in_dialog: bool = False
    dialog_cooldown: int = 1000
    last_dialog_time: int

    def __init__(self, path_to_entity, x_position, y_position, player: Player):
        super().__init__(path_to_entity, x_position, y_position)
        self.player = player
        self.entity_loader = self.get_Entity_Loader(path_to_entity)
        self.last_dialog_time = pygame.time.get_ticks()

    def get_Entity_Loader(self, pathToInfo) -> NPC_Loader:
        return NPC_Loader(pathToInfo)

    def update(self) -> None:
        pass

    def on_collision(self, entity: 'Entity') -> None:
        now = pygame.time.get_ticks()
        if now - self.last_dialog_time > self.dialog_cooldown:
            self.last_dialog_time = now
            self.is_in_dialog = not self.is_in_dialog

    def render_dialog(self, screen, camera: tuple[int, int]) -> None:
        """
        Renders the dialog box for the NPC
        :param screen: The screen to render the dialog box on
        :param camera: The camera to render the dialog box at
        :return: None
        """

        if self.entity_loader.dialog == "":
            return
        if not self.is_in_dialog:
            return

        # Render the dialog box
        rect = pygame.Rect(
            0, 0, config.Resolution[0], config.Resolution[1] // 4)
        rect.bottom = config.Resolution[1]

        # Draw the border and the rect above all the other stuff
        pygame.draw.rect(screen, config.Colors.white, rect)
        pygame.draw.rect(screen, config.Colors.purple, rect, 4)

        # Render the text
        font = pygame.font.Font(config.FONT_PATH, config.FONT_SIZE)
        text = self.entity_loader.dialog
        text = text.split('\n')
        for i, line in enumerate(text):
            d = font.render(line, True, config.Colors.black)
            text_rect = d.get_rect()
            text_rect.topleft = (rect.left + 10*config.SCALE, rect.top +
                                 10*config.SCALE + i * text_rect.height)
            screen.blit(d, text_rect)
