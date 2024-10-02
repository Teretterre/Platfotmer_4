import pygame
import const

class Platform(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height):
        super().__init__()
        self.image = pygame.image.load("img/platform.png")
        self.image = pygame.transform.scale(self.image, [width, height])
        self.rect = self.image.get_rect()
        self.rect.topleft = [x, y]

    def update(self):
        pass
