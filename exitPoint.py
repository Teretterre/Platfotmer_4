import pygame
import const
from const import BLACK


class ExitPoint(pygame.sprite.Sprite):
    def __init__(self, x, y, width=50, height=50):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(const.RED)
        self.rect = self.image.get_rect()
        self.rect.topleft = [x, y]

    def update(self, player):
        return self.rect.colliderect(player.rect)
