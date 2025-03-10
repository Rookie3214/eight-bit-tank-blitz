# game.py

import pygame
import sys
from core.utils.constants import (SCREEN_WIDTH, SCREEN_HEIGHT, FPS, MENU_STATE, GAMEPLAY_STATE)
from core.ui.menu import MenuManager
from core.utils.game_map import GameMap
from core.utils.player import Player

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Eight-Bit Tank Blitz")
    clock = pygame.time.Clock()

    # Menu Manager
    menu_manager = MenuManager(screen)

    # Create a simple map
    game_map = GameMap()
    # Hard-coded player for now
    player = Player(100, 100)

    current_state = MENU_STATE

    running = True
    while running:
        dt = clock.get_time() / 1000.0  # delta time in seconds

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                running = False

            # Forward events to menu if we are in menu states
            if current_state != GAMEPLAY_STATE:
                menu_manager.handle_event(event)

        # State machine logic
        if menu_manager.state != GAMEPLAY_STATE:
            current_state = menu_manager.state
        else:
            current_state = GAMEPLAY_STATE

        # Update
        if current_state == MENU_STATE:
            menu_manager.update()
        elif current_state == GAMEPLAY_STATE:
            # Gameplay update
            keys = pygame.key.get_pressed()
            player.handle_input(keys, dt)
            # Collision check with map obstacles
            if game_map.check_collision(player.rect):
                # Very simple collision resolution: revert the movement
                # For a real game, you'd track old positions or do finer collision checks
                if keys[pygame.K_UP]:
                    player.rect.y += player.speed * dt
                if keys[pygame.K_DOWN]:
                    player.rect.y -= player.speed * dt
                if keys[pygame.K_LEFT]:
                    player.rect.x += player.speed * dt
                if keys[pygame.K_RIGHT]:
                    player.rect.x -= player.speed * dt
        else:
            # We are in some other menu state (nation_selector, campaign, tank_selection, ready)
            menu_manager.update()

        # Draw
        screen.fill((0, 0, 0))  # black background
        if current_state == GAMEPLAY_STATE:
            game_map.draw(screen)
            player.draw(screen)
        else:
            menu_manager.draw()

        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
