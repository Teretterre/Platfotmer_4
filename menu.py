from importlib.metadata import files

import pygame
import os
import json
import const

class Menu:
    def __init__(self):
        self.font = pygame.font.Font("fonts/PixelifySans-VariableFont_wght.ttf", 36)
        self.font_name = pygame.font.Font("fonts/PixelifySans-VariableFont_wght.ttf", 72)
        self.levels = self.get_levels()
        self.selected_level = 0

    def get_levels(self):
        levels = []
        for file in os.listdir("LevelData/"):
            if file.endswith('.json'):
                levels.append(file)
        return sorted(levels)
    def update(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                self.selected_level = (self.selected_level - 1) % len(self.levels)
            elif event.key == pygame.K_DOWN:
                self.selected_level = (self.selected_level + 1) % len(self.levels)
            elif event.key == pygame.K_SPACE:
                print(self.levels[self.selected_level])
                return self.levels[self.selected_level]
        return None


    def render(self, screen):
        screen.fill((0, 0, 0))
        start_y = 240


        for i, level in enumerate(self.levels):
            if i == self.selected_level:
                color = (255, 0, 0)
            else:
                color = (255, 255, 255)

            level_txt = self.font.render(level.replace('.json', ''), True, color)

            screen.blit(level_txt, (const.SCREEN_WIDTH // 2 - level_txt.get_width() // 2, start_y + i * 50))
        name = self.font_name.render(const.NAME, True, (255, 255, 255))
        screen.blit(name, (180, 50))
