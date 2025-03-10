# core/utils/player.py

import pygame
from core.entities.base_tank import BaseTank

class Player(BaseTank):
    """
    Player-controlled tank.
    Inherits from BaseTank and adds keyboard controls.
    """
    def handle_input(self, keys, dt):
        # Movement speed for a simple approach
        move_speed = self.speed * dt

        if keys[pygame.K_UP]:
            self.rect.y -= move_speed
        if keys[pygame.K_DOWN]:
            self.rect.y += move_speed
        if keys[pygame.K_LEFT]:
            self.rect.x -= move_speed
        if keys[pygame.K_RIGHT]:
            self.rect.x += move_speed
