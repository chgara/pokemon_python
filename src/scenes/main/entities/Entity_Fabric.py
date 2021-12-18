import json
from src.scenes.main.entities.npcs.NPC import NPC
from src.scenes.main.entities.Entity import Entity
from src.scenes.main.entities.player.Player import Player
from src.scenes.main.entities.npcs.Random_NPC import Random_NPC
from src.scenes.main.entities.structures.Structure import Structure
from src.scenes.main.entities.structures.Colidable_Structure import Colidable_Structure


class Entity_Fabric:
    accected_types: list[str] = ['npc', 'random-npc',
                                 'structure', 'colidable-structure']
    entity: Entity
    location: str

    def __init__(self, location: str, x_position, y_position, player: Player):
        self.location = location
        self.player = player
        type: str = self.load_type_from_file(location)

        # Check that the provided type is valid
        self.check_is_valid_type(type)

        # Create the entity
        self.entity = self.create_entity(location, x_position, y_position)

    def load_type_from_file(self, location) -> str:
        """
        Loads the type of the entity from the json file
        :param location: the location of the json file
        :return: the type of the entity
        """
        with open(location) as json_file:
            data = json.load(json_file)
            return data['type']

    def check_is_valid_type(self, type: str) -> None:
        """
        Checks if the type is valid
        :param type: the type to check
        :return: True if the type is valid, False otherwise
        """
        if not type in self.accected_types:
            raise ValueError(
                f'The type {type} is not valid in file {self.location}')

    def create_entity(self, location: str, x_position, y_position) -> Entity:
        """
        Creates an entity based on the type
        :param location: the location of the json file
        :param x_position: the x position of the entity
        :param y_position: the y position of the entity
        :return: the entity
        """
        type: str = self.load_type_from_file(location)
        if type == 'structure':
            return Structure(location, x_position, y_position)
        elif type == 'colidable-structure':
            return Colidable_Structure(location, x_position, y_position)
        elif type == 'npc':
            return NPC(location, x_position, y_position, self.player)
        elif type == 'random-npc':
            return Random_NPC(location, x_position, y_position, self.player)
        else:
            raise ValueError(
                f'The type {type} is not valid in file {self.location}')
