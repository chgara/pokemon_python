import random
import pygame
from src.scenes.main.entities.Entity import Entity
from src.scenes.main.utils.Entity_Loader import Entity_Loader


class NPC(Entity):
    last: int
    cooldown: int

    def __init__(self, path_to_entity, x_position, y_position):
        super().__init__(path_to_entity, x_position, y_position)
        self.last = pygame.time.get_ticks()
        self.cooldown: int = self.random_cooldown()

    def get_Entity_Loader(self, pathToInfo) -> Entity_Loader:
        return Entity_Loader(pathToInfo)

    def update(self) -> None:
        now = pygame.time.get_ticks()
        move_to: str = self.random_move()
        if now - self.last > self.cooldown:
            self.last = now
            self.cooldown = self.random_cooldown()
            self.move_with_animation(move_to, 5)

    def on_collision(self, entity: 'Entity') -> None:
        return super().on_collision(entity)

    def random_cooldown(self) -> int:
        posible_cooldowns: list[int] = [1500, 2000, 3000, 4000]
        selected_cooldown: int = random.choice(posible_cooldowns)
        return selected_cooldown

    def random_move(self) -> str:
        posible_movements: list[str] = ['up', 'down', 'left', 'right']
        selected_movement: str = random.choice(posible_movements)
        return selected_movement


# super().__init__('src/assets/entities/npcs/buisnessman/main.json')
# super().__init__('src/assets/entities/npcs/childmary/main.json')
# super().__init__('src/assets/entities/npcs/athletemike/main.json')
