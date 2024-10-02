import pygame
import const

class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y, move_distance=100, speed=2):
        super().__init__()
        self.image = pygame.Surface([40, 40])
        self.image.fill(const.GREEN)
        self.rect = self.image.get_rect()
        self.rect.topleft = [x, y]
        self.speed = speed
        self.start_x = x
        self.end_x = x + move_distance
        self.direciton = 1

    def update(self):
        self.rect.x += self.speed * self.direciton
        if self.rect.x >= self.end_x:
            self.direciton = -1
        elif self.rect.x <= self.start_x:
            self.direciton = 1