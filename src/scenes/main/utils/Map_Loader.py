import json
import pygame
import itertools
from src.lib import config


class Entities_Map_Loader:
    location: str
    x_position: int
    y_position: int

    def __init__(self, location: str, x_position: int, y_position: int):
        self.location = location
        self.x_position = x_position
        self.y_position = y_position


class Map_Loader_Component:
    type: str
    size: tuple[int, int]
    image: str

    def __init__(self, type: str, size: tuple[int, int], image: str):
        self.type = type
        self.size = size
        self.image = image


class Map_Loader:
    map_info_file: str
    entities: list[Entities_Map_Loader] = []
    components: dict[str, Map_Loader_Component] = {}
    map: list[list[str]] = []
    height: int
    width: int

    def __init__(self, map_info_file: str):
        self.map_info_file = map_info_file

        # Loading propeties
        with open(map_info_file, 'r') as f:
            map_data = json.load(f)

            # Loading the map and the tile size
            self.map = self.get_map(map_data['map'])

            # Loading the components
            self.components = self.get_map_components(
                map_data['components'])

            # Loading the Entities
            self.entities = self.get_entities(map_data['entities'])

        self.width, self.height = self.get_map_measures()
        # Checking the map
        self.check_map()

    def get_map(self, path) -> list[list[str]]:
        """
        Loads a map from a text file.
        :param path: The path to the map file.
        :return: The map as a list of lists.
        """
        map: list[list[str]] = []
        with open(path, 'r') as map_file:
            lines_list: list[str] = map_file.read().split('\n')
            for line in lines_list:
                if line != '':
                    map.append(line.split(' '))
        return map

    def get_map_components(self, components: list) -> dict[str, Map_Loader_Component]:
        """
        Returns the components stored in a dictionary.
        !!!!!Important!!!!!
        The key of the dictionary is the type of the component.
        :return: The map and the npcs.
        """
        result: dict[str, Map_Loader_Component] = {}
        for component in components:
            type: str = component['type']
            size: tuple[int, int] = (
                component['size'][0]*config.SCALE, component['size'][1]*config.SCALE)
            image: str = component['image']
            result[type] = Map_Loader_Component(type, size, image)
        return result

    def get_map_measures(self) -> tuple[int, int]:
        """
        Returns the measures of the map.
        :return: The width and the height of the map.
        """
        def get_line_measure(line: list[str]) -> int:
            measure = 0
            for tile in line:
                # This is because the transposing of the map
                if(tile != None):
                    measure += self.components[tile].size[0]
            return measure

        def get_max_line_measure(map: list[list[str]]) -> int:
            max_measure = 0
            for line in map:
                new_measure = get_line_measure(line)
                if new_measure > max_measure:
                    max_measure = new_measure
            return max_measure

        width: int = 0
        width += get_max_line_measure(self.map)

        # Todo the same with the height we have to transpose the array
        height: int = 0
        transposed_map = list(itertools.zip_longest(*self.map))
        height += get_max_line_measure(transposed_map)
        return width, height

    def check_map(self,) -> None:
        """
        Checks if the map is valid.
        :return: None
        """
        result = True
        for line in self.map:
            for tile in line:
                if tile not in self.components:
                    result = False
        if not result:
            raise Exception(f"The map is not valid. {self.map_info_file}")

    def get_entities(self, entities) -> list[Entities_Map_Loader]:
        """
        Returns the entities stored in a list.
        :return: The entities.
        """
        result: list[Entities_Map_Loader] = []
        for entity in entities:
            location: str = entity['location']
            x_position: int = entity['coordinates']['x']
            y_position: int = entity['coordinates']['y']
            result.append(Entities_Map_Loader(
                location, x_position, y_position))
        return result

    def get_map_component_image(self, component_type: str):
        """
        Returns the image of a component.
        And scale it to the tile size.
        :param component_type: The type of the component.
        :return: The image of the component.
        """
        image = pygame.image.load(self.components[component_type].image)
        width = self.components[component_type].size[0]
        height = self.components[component_type].size[1]
        return pygame.transform.scale(image, (width, height))

    def render_map(self, screen, camera: tuple[int, int]) -> None:
        """
        Renders the map.
        :param screen: The screen to render the map on.
        :param camera: The camera of the map.
        :return: None
        """
        y_position = 0
        for line in self.map:
            x_position = 0
            for tile in line:
                size = self.components[tile].size
                image = self.get_map_component_image(tile)
                rect = image.get_rect()
                rect.x = x_position * size[0] - camera[0]
                rect.y = y_position * size[1] - camera[1]
                screen.blit(image, rect)

                x_position += 1

            y_position += 1