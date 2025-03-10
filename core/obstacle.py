# core/utils/obstacle.py

import pygame
from core.utils.constants import GRAY

class Obstacle:
    """
    Simple rectangle obstacle.
    """
    def __init__(self, x, y, width, height):
        self.rect = pygame.Rect(x, y, width, height)

    def draw(self, surface):
        pygame.draw.rect(surface, GRAY, self.rect)
