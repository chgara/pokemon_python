import pygame
from src.lib import config
from src.lib.Game_State import Game_State
from src.lib.Game_Sceene import Game_Sceene
from src.utils.save_utils import write_save
from src.scenes.main.entities.npcs.NPC import NPC
from src.scenes.main.entities.Entity import Entity
from src.scenes.main.entities.player.Player import Player
from src.scenes.main.entities.Entity_Fabric import Entity_Fabric
from src.scenes.main.utils.Map_Loader import Entities_Map_Loader, Map_Loader


class Game(Game_Sceene):
    """
    This is the main part of the game.

    Atributes:
        (To view some atributes not explainded here plese refer to Game_Sceen class)

        objects:
            A list of all objects that should be rendered on the screen. All objects must be of type Entity to ensure
            that the game is rendered correctly.

        map:
            The map that the game is played on.
            Is of type (Map_Loader) and it manages all the map related things.

        player:
            The player that the game is played on.
            Is of type (Player) and it manages all the player related things.

        camera:
            The camera position.
    """
    objects: list[Entity]
    player: Player
    map: Map_Loader
    camera: tuple[int, int]

    def __init__(self, screen: pygame.Surface, change_game_state, change_game_scene):
        super().__init__(screen, config.Music.game, change_game_state, change_game_scene)
        self.objects = []
        self.camera = (0, 0)

    def set_up(self) -> None:
        """
        Sets up the main game sceene
        """
        # Start the music
        self.bg_music.play()

        # Add the player to the game
        self.player: Player = Player()
        self.objects.append(self.player)

        # Load the map and the entities
        self.map = Map_Loader(self.player.entity_loader.map)
        # TODO: load music from map
        self.load_entities_from_map(self.map.entities)

#       # Set the game state to running
#       self.change_game_state(Game_State.RUNNING)

    def update(self) -> None:
        """
        Updates the game logic.
        """
        self.screen.fill(config.Colors.black)

        # Handle events
        self.handle_events()

        # Update the camera position
        self.determine_camera()

        # Update the entities
        self.update_entities()

        # If dev mode is on, get new map files
        if config.DEV_MODE:
            print(self.player.x_position, self.player.y_position)
            self.map = Map_Loader(self.player.entity_loader.map)

        self.map.render_map(self.screen, self.camera)
        for object in self.objects:
            if not isinstance(object, Entity):
                raise TypeError("Objects must be of type Entity")

            # Due to performance this is necesary
            if object.is_entitie_in_camera(self.camera):
                object.render(self.screen, self.camera)

        self.render_npcs_dialog()

    def render_npcs_dialog(self):
        """
        Renders the dialog of the npcs
        """
        for entity in self.objects:
            if isinstance(entity, NPC):
                entity.render_dialog(self.screen, self.camera)

    def clean_dialog(self):
        """
        Cleans the dialog of the npcs
        """
        for entity in self.objects:
            if isinstance(entity, NPC):
                entity.is_in_dialog = False

    # Using the observer entities
    def update_entities(self,) -> None:
        """
        Using the observer pattern we update the entities state
        that all the entities/observers are observing.
        """
        for object in self.objects:
            new_objects = [] + self.objects
            new_objects.remove(object)
            object.update_entitie_state(new_objects)

    def load_entities_from_map(self, entities: list[Entities_Map_Loader]) -> None:
        """
        Loads the entities from the map.
        """
        for entity in entities:
            location: str = entity.location
            x_position: int = entity.x_position
            y_position: int = entity.y_position
            new_entity: Entity = Entity_Fabric(
                location, x_position, y_position, self.player, self.change_game_scene).entity
            self.objects.append(new_entity)

    def determine_camera(self):
        """
        Determines the camera position.
        It does in the following way:
            - Camera put player on the center of the screen always except when:
                - Player is on the edge of the screen
                - Player is on the edge of the map
        """
        max_x_position: int = round(
            self.map.width - config.Resolution[0])
        max_y_position: int = round(
            self.map.height - config.Resolution[1])

        x_position = self.player.x_position - config.Resolution[0] // 2
        y_position = self.player.y_position - config.Resolution[1] // 2

        if x_position <= max_x_position and x_position >= 0:
            self.camera = (x_position, self.camera[1])
        elif x_position < 0:
            self.camera = (0, self.camera[1])
        elif x_position > max_x_position:
            self.camera = (max_x_position, self.camera[1])

        if y_position <= max_y_position and y_position >= 0:
            self.camera = (self.camera[0], y_position)
        elif y_position < 0:
            self.camera = (self.camera[0], 0)
        elif y_position > max_y_position:
            self.camera = (self.camera[0], max_y_position)

    def handle_events(self):
        """
        Handles all events.
        """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.change_game_state(Game_State.ENDED)
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE and config.DEV_MODE:
                    self.change_game_state(Game_State.ENDED)
                # If CRTL s is presed we will save the actual play
                elif event.key == pygame.K_m:
                    mods = pygame.key.get_mods()
                    if mods & pygame.KMOD_CTRL:
                        write_save((self.player.x_position,
                                   self.player.y_position))
            keys = pygame.key.get_pressed()
            if keys[pygame.K_w]:
                self.player.move('up')
            if keys[pygame.K_s]:
                self.player.move('down')
            if keys[pygame.K_d]:
                self.player.move('right')
            if keys[pygame.K_a]:
                self.player.move('left')
            if keys[pygame.K_c]:
                self.clean_dialog()
            if keys[pygame.K_i] and config.DEV_MODE:
                input()
