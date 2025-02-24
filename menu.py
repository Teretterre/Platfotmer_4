from importlib.metadata import files

import pygame
import os
import json
import const

class Menu:
    def __init__(self, screen):
        self.screen = screen
        self.font = pygame.font.Font(None, 36)
        self.levels = self.get_levels()
        self.selected_level = 0

    def get_levels(self):
        levels = []
        for file in os.listdir("LevelData/"):
            if file.endswith('.json'):
                levels.append(file)
        return sorted(levels)
    def update(self):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.selected_level = (self.selected_level - 1) % len(self.levels)
                    print(self.selected_level)
                elif event.key == pygame.K_DOWN:
                    self.selected_level = (self.selected_level + 1) % len(self.levels)
                    print(self.selected_level)
                elif event.key == pygame.K_KP_ENTER:
                    return self.levels[self.selected_level]
            return None
    def render(self):
        self.screen.fill((0, 0, 0))
        start_y = 100

        for i, level in enumerate(self.levels):
            if i == self.selected_level:
                color = (255, 0, 0)
            else:
                color = (255, 255, 255)

            level_txt = self.font.render(level.replace('.json', ''), True, color)

            self.screen.blit(level_txt, (const.SCREEN_WIDTH // 2 - level_txt.get_width() // 2, start_y + i * 50))
