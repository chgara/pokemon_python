import pygame
import json
from src.utils import config


class Sprite_coords:
    x: int
    y: int
    width: int
    height: int

    def __init__(self, json_object):
        self.x = json_object['x']
        self.y = json_object['y']
        self.width = json_object['w']
        self.height = json_object['h']


class Entity_Loader:
    """
    The following methods are used to get the information of the entity
    :param pathToInfo the path to the json file
    """
    name: str
    entity_coords: list[int]
    color_to_be_erased: str
    image_path: str
    scale: float
    valid_moves: list[str]

    def __init__(self, pathToInfo):
        self.pathToInfo = pathToInfo

        # Setting the properties
        with open(self.pathToInfo) as json_file:
            data = json.load(json_file)
            self.name = data['name']
            self.entity_coords = data['coordinates']
            self.color_to_be_erased = data['color_to_be_erased']
            self.image_path = data['img']
            self.scale = data['scale']
            self.valid_moves = data['valid_moves']

        self.sprite_sheet = pygame.image.load(self.image_path).convert()

    def get_image(self, coords: Sprite_coords) -> pygame.Surface:
        """
        The image of the entity stored in the json file
        :param coords: the coordinates of the sprite
        :return: a pygame.image
        """

        # Gettting the meassures of the image
        width = coords.width
        height = coords.height

        # Setting the image
        image = self.sprite_sheet.subsurface(
            coords.x, coords.y, coords.width, coords.height)
        image = pygame.transform.scale(
            image, (int(width)*self.scale, int(height)*self.scale))

        # Erase the color
        image.set_colorkey(pygame.Color(self.color_to_be_erased))
        return image

    def get_image_coords(self, propety: str) -> list[Sprite_coords]:
        """
        The back image of the entity stored in the json file
        :return: a list of coordinates for the sprite
        """
        with open(self.pathToInfo) as json_file:
            data = json.load(json_file)
            # Eval if the property exists
            if propety in data:
                datalist: list = data[propety]
                result: list[Sprite_coords] = []
                for d in datalist:
                    result.append(Sprite_coords(d))
                return result
            else:
                return []

    def load_default_image(self) -> pygame.Surface:
        # Load the image of the entity
        img: Sprite_coords = self.get_image_coords('down')[
            0]
        image = self.get_image(img)
        return image
