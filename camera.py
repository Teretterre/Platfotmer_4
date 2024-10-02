import pygame
import const

class Camera:
    def __init__(self, width, height):
        self.camera = pygame.Rect(0, 0, width, height)
        self.width = width
        self.height = height

    def update(self, target):
        X = - target.rect.centerx + self.width // 2

        if target.rect.centery < 30:
            Y = - target.rect.centery + self.height // 2
        else:
            Y = self.height - const.SCREEN_HEIGHT

        self.camera = pygame.Rect(X, Y, self.width, self.height)

    def apply(self, sprite):
        return sprite.rect.move(self.camera.topleft)
