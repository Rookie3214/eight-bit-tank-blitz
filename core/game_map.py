# core/utils/game_map.py

import pygame
from core.utils.obstacle import Obstacle

class GameMap:
    """
    Loads and stores map data, obstacles, spawn points, etc.
    """
    def __init__(self, map_data=None):
        self.obstacles = []
        if map_data:
            self.load_map_data(map_data)

    def load_map_data(self, map_data):
        # Example obstacle in the center
        self.obstacles.append(Obstacle(350, 250, 100, 100))

    def draw(self, surface):
        for obs in self.obstacles:
            obs.draw(surface)

    def check_collision(self, rect):
        for obs in self.obstacles:
            if obs.rect.colliderect(rect):
                return True
        return False
