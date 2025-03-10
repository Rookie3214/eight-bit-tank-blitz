# core/entities/base_tank.py

import pygame
from core.utils.constants import BLUE

class BaseTank:
    """
    Base class for all tanks (player or AI).
    """
    def __init__(self, x, y, width=40, height=40, speed=150, health=100, damage=10):
        # Position and size
        self.rect = pygame.Rect(x, y, width, height)

        # Basic stats
        self.speed = speed
        self.health = health
        self.damage = damage

        # For rendering
        self.color = BLUE  # Simple color placeholder

    def update(self, dt):
        """
        Update logic each frame.
        For base tank, there's no default behavior.
        """
        pass

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.rect)

    def take_damage(self, amount):
        self.health -= amount
        if self.health < 0:
            self.health = 0

    def is_destroyed(self):
        return self.health <= 0
