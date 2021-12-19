import json
import pygame
from src.lib import config
from src.lib.Game_Save import Game_Save
from src.utils.save_utils import read_save
from src.lib.Game_State import Game_State
from src.lib.Game_Sceene import Game_Sceene, Game_Sceenes
from src.scenes.menu.components.Menu_Save import Menu_Save
from src.scenes.menu.components.New_Save import New_Save


class Menu(Game_Sceene):
    path_to_save_file = config.SAVES_PATH
    menu_saves: list[Menu_Save] = []
    new_save: New_Save

    def __init__(self, screen: pygame.Surface, change_game_state, change_game_scene) -> None:
        super().__init__(screen, config.Music.menu, change_game_state, change_game_scene)

    def set_up(self) -> None:
        """
        Sets up the menu.
        Reads the state of the game from the file and sets the game state accordingly.
        """
        # Start playing the music
        self.bg_music.play()

        saves: list[Game_Save] = self.load_saves()
        for save in saves:
            self.menu_saves.append(Menu_Save(save, self.load))

        self.new_save = New_Save(self.load)

    def update(self) -> None:
        """
        Updates the menu.
        """
        self.screen.fill(config.Colors.purple)
        self.handle_events()

        # Render the components
        self.render_head_text()
        self.render_saves()
        self.new_save.render(self.screen)

    def handle_events(self) -> None:
        """
        Handles the events of the menu.
        """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.change_game_state(Game_State.ENDED)
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.change_game_state(Game_State.ENDED)

            # If there is a click check if is in a button
            elif event.type == pygame.MOUSEBUTTONDOWN:
                click_position: tuple[int, int] = pygame.mouse.get_pos()
                self.new_save.update_click(click_position)
                for menu_save in self.menu_saves:
                    menu_save.update_click(click_position)

    def render_head_text(self) -> None:
        """
        Renders the text of the head of the menu.
        """
        font = pygame.font.Font(config.FONT_PATH2, config.FONT_SIZE*3)
        text = font.render("Pokemon", True, config.Colors.white)
        text_rect = text.get_rect()
        text_rect.center = (
            config.Resolution[0]//2, round(Menu_Save.padding*1.5))
        self.screen.blit(text, text_rect)

    def render_saves(self) -> None:
        """
        Renders the saves.
        """
        for i in range(len(self.menu_saves)):
            position: tuple[int, int] = (
                100*config.SCALE, 110*(i+1)*config.SCALE)
            self.menu_saves[i].render(self.screen, position)

    def load(self, game_save: Game_Save) -> None:
        """
        Loads the game.
        """
        if not isinstance(game_save, Game_Save):
            raise TypeError("game_save must be of type Game_Save")
        path_to_player_info = config.PLAYER_PATH
        with open(path_to_player_info, 'r+') as file:
            data = json.load(file)
            data['coordinates'] = game_save.player_coordinates
            data['map'] = game_save.map
            data['actual_save'] = game_save.name
            file.seek(0)
            json.dump(data, file)
            file.truncate()
        self.change_game_scene(Game_Sceenes.GAME)

    def load_saves(self) -> list[Game_Save]:
        """
        Returns a list of all the saves.
        """
        result: list[Game_Save] = []
        with open(self.path_to_save_file, "r") as file:
            data = json.load(file)
            names: list[str] = list(data.keys())
            for save_name in names:
                save: Game_Save = read_save(save_name)
                result.append(save)
        return result
