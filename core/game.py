import pygame
from core.player import Player
from core.ai import AI
from core.map import GameMap

def main():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    clock = pygame.time.Clock()

    # Initialize game entities
    player = Player()
    allies = [AI(), AI()]  # Two allied AI tanks
    game_map = GameMap()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        # Update game state, player, allies, and map here
        # Render game graphics
        pygame.display.flip()
        clock.tick(60)
        
    pygame.quit()

if __name__ == '__main__':
    main()