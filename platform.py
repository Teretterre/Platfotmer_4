from pydoc_data.topics import topics
from sys import platform
import img

import pygame
import const

class Platform(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height):
        super().__init__()
        self.image = pygame.image.load("img/platform.png")
        self.image = pygame.transform.scale(self.image, [self.image.get_width(), self.image.get_height()])
        self.image = self.scale_image(self.image, 80)
        self.rect = self.image.get_rect()
        self.rect.topleft = [x, y]
        self.width = width
        self.height = height

    def update(self):
        platform_surface = pygame.Surface((self.width, self.height))
        for x in range(0, self.width, self.image.get_width()):
            y = 0
            platform_surface.blit(self.image, (x, y))

        self.image = platform_surface
        self.rect = self.image.get_rect(topleft=self.rect.topleft)


    def scale_image(self, img, max_width):
        orig_w = img.get_width()
        orig_h = img.get_height()
        ratio = orig_w / orig_h
        new_w = max_width
        new_h = new_w / ratio
        return pygame.transform.scale(img, (new_w, new_h))