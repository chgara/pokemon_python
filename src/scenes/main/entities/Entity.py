import pygame
from typing import Union
from threading import Timer
from src.lib import config
from abc import ABC, abstractmethod
from src.scenes.main.utils.Entity_Loader import Entity_Loader


class Entity(ABC):
    image: pygame.Surface
    x_position: int = 0
    y_position: int = 0
    last_image: tuple[str, int] = ("", 0)
    entity_loader: Entity_Loader
    external_entitys: list['Entity'] = []

    def __init__(self, pathToInfo: str, x_position: int, y_position: int):
        self.entity_loader = self.get_Entity_Loader(pathToInfo)
        # Load the defaul image
        self.image = self.entity_loader.load_default_image()
        self.rect = self.image.get_rect()
        # Updating the entity position
        self.update_position(x_position, y_position)

    @abstractmethod
    def update(self) -> None:
        """
        Updates the logic of the entity
        It is intended to be overrided by the child classes
        :return None:
        """
        pass

    @abstractmethod
    # With these we ensure that the childs will have its own loader with it
    # own entity info loaded. To make these I have used the STRATEGY pattern
    def get_Entity_Loader(self, pathToInfo) -> Entity_Loader:
        """
        Get the entity loader
        :return Entity_Loader:
        """
        pass

    @abstractmethod
    def on_collision(self, entity: 'Entity') -> None:
        """
        On collision with another entity execute this method
        :param entity: entity that collided with the entity
        :return None:
        """
        pass

    def update_rect(self, camera: tuple[int, int]) -> None:
        """
        Update the rect of the entity
        :param camera: camera position
        :return None:
        """
        self.rect = self.image.get_rect()
        self.rect.x = self.x_position - camera[0]
        self.rect.y = self.y_position - camera[1]

    def update_position(self, x_position: int, y_position: int) -> None:
        """
        Update position of the entity
        :param x_position: x position of the entity
        :param y_position: y position of the entity
        :return None:
        """
        # Check that the entity has not colided in previous movement
        if self.check_collision(x_position, y_position):
            return

        # Update position of the entity
        self.x_position += x_position * config.SCALE
        self.y_position += y_position * config.SCALE

    def check_collision(self, x_movement: int, y_movement: int, entity: Union['Entity', None] = None) -> bool:
        """
        Check if the entity has colided with another entity
        :param entity: entity to check
        :return bool:
        """
        rect = self.rect
        rect.x += x_movement
        rect.y += y_movement
        if entity is None:
            for entity in self.external_entitys:
                if rect.colliderect(entity.rect):
                    return True
        else:
            if rect.colliderect(entity.rect):
                return True
        return False

    def update_entitie_state(self, entities: list['Entity']) -> None:
        """
        Update the entities
        :param entities: list of entities
        :return None:
        """
        self.external_entitys = entities

    def is_entitie_in_camera(self, camera: tuple[int, int]) -> bool:
        """
        Check if the entity is in the camera
        :param camera: camera position
        :return bool:
        """
        # Ensure that thhe entity's rect is updated
        self.update_rect(camera)

        def check_if_in_camera(x: int, y: int) -> bool:
            """
            Check if the entity is in the camera
            :param x: x position of the entity
            :param y: y position of the entity
            :return bool:
            """
            x = x + camera[0]
            y = y + camera[1]
            if x > camera[0] and x < camera[0] + config.Resolution[0]:
                if y > camera[1] and y < camera[1] + config.Resolution[1]:
                    return True
            return False

        bottom_right = check_if_in_camera(
            self.rect.topleft[0], self.rect.topleft[1])
        bottom_left = check_if_in_camera(
            self.rect.bottomleft[0], self.rect.bottomleft[1])
        top_right = check_if_in_camera(
            self.rect.topright[0], self.rect.topright[1])
        top_left = check_if_in_camera(
            self.rect.bottomright[0], self.rect.bottomright[1])

        return bottom_right or bottom_left or top_right or top_left

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

    def move(self, move_to: str, factor: int = 3) -> None:
        # If the provided movement is not valid raise an error
        if move_to not in self.entity_loader.valid_moves:
            raise ValueError("Invalid direction")

        factor = factor
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

    def render(self, screen, camera: tuple[int, int]) -> None:
        """
        Render the entity on the screen
        :param screen: screen where the entity will be rendered
        :return None:
        """
        # Render the entity on the screen
        self.update()
        screen.blit(self.image, self.rect)

        if config.DEV_MODE:
            # Render the entity rect on the screen
            pygame.draw.rect(screen, (255, 0, 0), self.rect, 4)
