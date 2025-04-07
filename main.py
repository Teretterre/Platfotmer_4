from random import random
import random
import pygame
from level import Level
from Bullet import Bullet
from my_platform import Platform
from player import Player
from camera import Camera
from enemy import Enemy
from health import Health
from gameObject import GameObject
from Bullet import Bullet
import const
from menu import Menu
from background import draw_back_gradient, Cloud
import os


# Инициализация Pygame
pygame.init()

# Создание окна
screen = pygame.display.set_mode((const.SCREEN_WIDTH, const.SCREEN_HEIGHT))
pygame.display.set_caption("Platformer Game")
clock = pygame.time.Clock()




# перезапуск игры
def reset_game(hp):
    hp.reset_hp()
    main()

# Игровой цикл
def main():
    level = None
    screen_now = 'menu'
    menu = Menu()
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if screen_now == 'menu':
                name_file = menu.update(event)
                if name_file != None:
                    screen_now = 'lvl'
                    level = Level(os.path.join("LevelData/" + str(name_file)))
        if screen_now == 'menu':
            menu.render(screen)
        elif screen_now == 'lvl':
            level.update()
            level.render(screen)



        pygame.display.flip()
        clock.tick(const.FPS)

    pygame.quit()

if __name__ == "__main__":
    main()