import pygame
import json
from src.lib import config


class Sprite_coords:
    """
    Class that stores the info of an entity position.
    It stores the position and the image corresponding to the position.
    """
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
    This class is used to load and entity from its corresponding json file
    It updates the entity properties with the json file ones.

    Atributes:
        name: the name of the entity
        color_to_be_erased: the color to be erased from the image
        image_path: the path to the image

        scale:
            The scale to be applied to the image

        valid_moves:
            The moves that we can use in an entity because not all the entities
            have the sprites to move in the specified direction.

        sprite_sheet:
            The image that contains all the sprites of the entity

        pathToInfo:
            The path to the json file that contains the information of the entity
    """
    name: str
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
            self.color_to_be_erased = data['color_to_be_erased']
            self.image_path = data['img']
            self.scale = data['scale']
            self.valid_moves = data['valid_moves']

        # Load the image of the entity
        self.sprite_sheet = pygame.image.load(self.image_path).convert()

    def get_image(self, coords: Sprite_coords) -> pygame.Surface:
        """
        The image of the entity stored in the json file
        :param coords: the coordinates of the sprite type (Sprite_coords)
        :return: a pygame.image
        """

        # Gettting the meassures of the image
        width = coords.width
        height = coords.height

        # Setting the image
        image = self.sprite_sheet.subsurface(
            coords.x, coords.y, coords.width, coords.height)
        # Scaling the image
        image = pygame.transform.scale(
            image, (int(width)*self.scale*config.SCALE, int(height)*self.scale*config.SCALE))

        # Erase the color
        image.set_colorkey(pygame.Color(self.color_to_be_erased))
        return image

    def get_image_coords(self, propety: str) -> list[Sprite_coords]:
        """
        Returns a list of the coordinates of the sprites of the entity
        These list contain the animation images of the entity with the specified position
        :param propety: the property of the entity
        :return: a list of the coordinates of the sprites of the entity
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
        """
        All the entities have a default image and this method returns it
        :return: a pygame.Surface
        """
        img: Sprite_coords = self.get_image_coords('down')[
            0]
        image = self.get_image(img)
        return image
