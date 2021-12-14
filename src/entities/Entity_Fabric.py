import json
from src.entities.Entity import Entity
from src.entities.NPC import NPC
from src.entities.Structure import Structure


class Entity_Fabric:
    accected_types: list[str] = ['npc', 'structure']
    entity: Entity
    location: str

    def __init__(self, location: str, x_position, y_position):
        self.location = location
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
        else:
            return NPC(location, x_position, y_position)
