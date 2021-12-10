import pygame
from typing import Union
from threading import Timer
from abc import ABC, abstractmethod
from src.utils.Entity_Loader import Entity_Loader, Sprite_coords


class Entity(ABC):
    rect: pygame.Rect
    image: pygame.Surface
    position: list[int] = [0, 0]
    last_image: tuple[str, int] = ("", 0)
    entity_loader: Entity_Loader

    def __init__(self, pathToInfo: str,):
        self.entity_loader = Entity_Loader(pathToInfo)
        # Load the defaul image
        self.image = self.entity_loader.load_default_image()
        # Updating the entity position
        [x_position, y_position] = self.entity_loader.entity_coords
        self.update_position(x_position, y_position)

    @abstractmethod
    def update(self) -> None:
        """
        Updates the logic of the entity
        It is intended to be overrided by the child classes
        :return None:
        """
        pass

    def update_position(self, x_position: int, y_position: int) -> None:
        """
        Update position of the entity
        :param x_position: x position of the entity
        :param y_position: y position of the entity
        :return None:
        """
        # Update position of the entity
        self.position[0] += x_position
        self.position[1] += y_position

        self.rect = self.image.get_rect()
        self.rect.x = self.position[0]
        self.rect.y = self.position[1]

    def animate_player_image_to(self, d: str) -> None:
        """
        Animate the entity to the new direction
        :param d: direction to animate the entity
        :return None:
        """
        # Gettting the new coords for the image
        coords = self.entity_loader.get_image_coords(d)
        if self.last_image[0] != d:
            if len(coords) == 0:
                return
            # Update the last image
            self.last_image = (d, 0)
        else:
            # Update the last image if its posible
            if len(coords) > self.last_image[1] + 1:
                self.last_image = (d, self.last_image[1] + 1)
            else:
                self.last_image = (d, 0)

        # Load the new image
        new_image = self.entity_loader.get_image(
            coords[self.last_image[1]])
        # Update the entity image
        self.image = new_image

    def move(self, move_to: str, factor: int = 5) -> None:
        # If the provided movement is not valid raise an error
        if move_to not in self.entity_loader.valid_moves:
            raise ValueError("Invalid direction")

        # If the movement is valid update the position of the entity
        if move_to == "up":
            self.update_position(0, -1*factor)
        elif move_to == "down":
            self.update_position(0, 1*factor)
        elif move_to == "left":
            self.update_position(-1*factor, 0)
        elif move_to == "right":
            self.update_position(1*factor, 0)

        # Animate the entity to the new direction
        self.animate_player_image_to(move_to)

    def move_with_animation(self, move_to: str, times: int, seconds_delay: float = 0.1) -> None:
        for i in range(times):
            Timer(seconds_delay * i, self.move, (move_to,)).start()

    def render(self, screen) -> None:
        """
        Render the entity on the screen
        :param screen: screen where the entity will be rendered
        :return None:
        """
        # Render the entity on the screen
        self.update()
        screen.blit(self.image, self.rect)
