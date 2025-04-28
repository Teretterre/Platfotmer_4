import pygame
import const
from button import Button
class EndScreen:
    def __init__(self, status):
        self.status = status #win или lose
        self.font = pygame.font.Font("fonts/PixelifySans-VariableFont_wght.ttf", 36)
        self.font_text = pygame.font.Font("fonts/PixelifySans-VariableFont_wght.ttf", 72)
        self.output = None
        def button_menu_action():
            self.output = 'return_menu'

        self.button_menu = Button(200, 200, 100, 50, 'в меню', 30, const.RED, const.GREEN, const.BLUE, button_menu_action)

    def update(self, event):
        self.button_menu.update(event)
        return self.output
        #if event.type == pygame.KEYDOWN:
        #    if event.key == pygame.K_UP:
        #        self.selected_level = (self.selected_level - 1) % len(self.levels)
        #    elif event.key == pygame.K_DOWN:
        #        self.selected_level = (self.selected_level + 1) % len(self.levels)
        #    elif event.key == pygame.K_SPACE:
        #        print(self.levels[self.selected_level])
        #        return self.levels[self.selected_level]
        #return None


    def render(self, screen):
        screen.fill((0, 0, 0))
        self.button_menu.render(screen)
        if self.status == 'win':
            text = self.font_text.render(const.WIN, True, (255, 255, 255))
        else:
            text = self.font_text.render(const.LOSE, True, (255, 255, 255))
        screen.blit(text, (180, 50))
