# core/ui/menu.py

import pygame
from core.utils.constants import (WHITE, BLACK, MENU_STATE, NATION_SELECTOR_STATE,
                                  CAMPAIGN_STATE, TANK_SELECTION_STATE, READY_STATE,
                                  GAMEPLAY_STATE, MENU_OPTIONS, NATION_OPTIONS,
                                  GERMANY_LEVELS, SOVIET_LEVELS)

class MenuManager:
    """
    Handles UI flow: main menu, nation selection, campaign map, tank selection, ready screen.
    """
    def __init__(self, screen):
        self.screen = screen
        self.font = pygame.font.SysFont("Arial", 24)
        self.state = MENU_STATE

        # Tracking user choices
        self.selected_nation = None
        self.selected_level = None
        self.selected_tank = None

        # Simple placeholders for button rectangles
        self.menu_buttons = []
        self.nation_buttons = []
        self.level_buttons = []
        self.ready_button = None

        # Initialize menus
        self._init_menu_buttons()
        self._init_nation_buttons()

    def _init_menu_buttons(self):
        # Suppose we only have one button: "Story"
        x, y, w, h = 300, 200, 200, 50
        self.menu_buttons.append((pygame.Rect(x, y, w, h), MENU_OPTIONS[0]))

    def _init_nation_buttons(self):
        # Two buttons for Germany and Soviet Union
        x, y, w, h = 300, 200, 200, 50
        self.nation_buttons.append((pygame.Rect(x, y, w, h), NATION_OPTIONS[0]))  # Germany
        self.nation_buttons.append((pygame.Rect(x, y+70, w, h), NATION_OPTIONS[1]))  # Soviet Union

    def handle_event(self, event):
        """
        Process menu interactions.
        """
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            mouse_pos = event.pos

            if self.state == MENU_STATE:
                for rect, text in self.menu_buttons:
                    if rect.collidepoint(mouse_pos):
                        if text == "Story":
                            self.state = NATION_SELECTOR_STATE

            elif self.state == NATION_SELECTOR_STATE:
                for rect, text in self.nation_buttons:
                    if rect.collidepoint(mouse_pos):
                        self.selected_nation = text
                        self.state = CAMPAIGN_STATE

            elif self.state == CAMPAIGN_STATE:
                # Check which level was clicked
                for rect, text in self.level_buttons:
                    if rect.collidepoint(mouse_pos):
                        self.selected_level = text
                        self.state = TANK_SELECTION_STATE

            elif self.state == TANK_SELECTION_STATE:
                # In a real game, you would have multiple tank options
                # For now, let's assume clicking anywhere just picks a default tank
                self.selected_tank = "Default Tank"
                self.state = READY_STATE

            elif self.state == READY_STATE:
                if self.ready_button and self.ready_button.collidepoint(mouse_pos):
                    self.state = GAMEPLAY_STATE

    def update(self):
        """
        Update menu elements (e.g., dynamic unlocking).
        """
        if self.state == CAMPAIGN_STATE:
            # Show levels based on selected nation
            if self.selected_nation == "Germany":
                levels = GERMANY_LEVELS
            else:
                levels = SOVIET_LEVELS

            self.level_buttons = []
            x, y, w, h = 200, 150, 400, 40
            offset = 50
            for lvl in levels:
                rect = pygame.Rect(x, y, w, h)
                self.level_buttons.append((rect, lvl))
                y += offset

        elif self.state == READY_STATE:
            # Create a single "Start" button
            self.ready_button = pygame.Rect(300, 400, 200, 50)

    def draw(self):
        """
        Draw menu elements depending on current state.
        """
        if self.state == MENU_STATE:
            self._draw_main_menu()
        elif self.state == NATION_SELECTOR_STATE:
            self._draw_nation_selector()
        elif self.state == CAMPAIGN_STATE:
            self._draw_campaign_map()
        elif self.state == TANK_SELECTION_STATE:
            self._draw_tank_selection()
        elif self.state == READY_STATE:
            self._draw_ready_screen()

    def _draw_main_menu(self):
        for rect, text in self.menu_buttons:
            pygame.draw.rect(self.screen, WHITE, rect)
            label = self.font.render(text, True, BLACK)
            self.screen.blit(label, (rect.x + 10, rect.y + 10))

    def _draw_nation_selector(self):
        for rect, text in self.nation_buttons:
            pygame.draw.rect(self.screen, WHITE, rect)
            label = self.font.render(text, True, BLACK)
            self.screen.blit(label, (rect.x + 10, rect.y + 10))

    def _draw_campaign_map(self):
        label = self.font.render("Select a Level:", True, WHITE)
        self.screen.blit(label, (50, 50))
        for rect, text in self.level_buttons:
            pygame.draw.rect(self.screen, WHITE, rect)
            lvl_label = self.font.render(text, True, BLACK)
            self.screen.blit(lvl_label, (rect.x + 10, rect.y + 5))

    def _draw_tank_selection(self):
        label = self.font.render("Select a Tank (click anywhere for default):", True, WHITE)
        self.screen.blit(label, (50, 50))

    def _draw_ready_screen(self):
        label = self.font.render(f"Ready Screen: {self.selected_nation}, {self.selected_level}, {self.selected_tank}", True, WHITE)
        self.screen.blit(label, (50, 50))
        if self.ready_button:
            pygame.draw.rect(self.screen, WHITE, self.ready_button)
            start_label = self.font.render("Start Battle", True, BLACK)
            self.screen.blit(start_label, (self.ready_button.x + 10, self.ready_button.y + 10))
