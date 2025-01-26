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
from background import draw_back_gradient, Cloud



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
    l1 = Level('LevelData/lvl_1.json')

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        l1.update()

        l1.render(screen)

        pygame.display.flip()
        clock.tick(const.FPS)

    pygame.quit()

if __name__ == "__main__":
    main()