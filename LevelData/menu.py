from importlib.metadata import files

import pygame
import os
import json

class Menu:
    def __init__(self, screen):
        self.screen = screen
        self.font = pygame.font.Font(None, 36)
        self.levels = self.get_levels
        self.selected_level = 0

    def get_levels(self):
        levels = []
        for file in os.listdir("LevelData/"):
            if file.endwith('.json'):
                levels.append(file)
        return sorted(levels)
    def update(self):
        for event in pygame.KEYDOWN:
            if event.key == pygame.K_UP():
                self.selected_level = (self.selected_level - 1) % len(self.levels)
            elif event.key == pygame.K_DOWN:
                self.selected_level = (self.selected_level + 1) % len(self.levels)
            elif event.key == pygame.K_KP_ENTER:
                return self.levels[self.selected_level]
        return None