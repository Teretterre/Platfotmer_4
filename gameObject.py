#ящик , камень
import pygame
import const
from const import BLACK


class GameObject(pygame.sprite.Sprite):
    def __init__(self, x, y, width=50, height=50, object_type='rock'):
        super().__init__()
        self.object_type = object_type
        self.image = pygame.Surface([width, height])
        if self.object_type == 'rock':
            self.image.fill(BLACK)
        elif self.object_type == 'box':
            self.image.fill(const.BROWN)
        self.rect = self.image.get_rect()
        self.rect.topleft = [x, y]
        self.velocity_y = 0
        self.velocity_x = 0


    def gravity(self):
        self.velocity_y += const.GRAVITY
        self.rect.y += self.velocity_y
        if self.rect.bottom > const.SCREEN_HEIGHT - 30:
            self.velocity_y = 0
            self.rect.bottom = const.SCREEN_HEIGHT - 30

    def move(self, dx):
        if self.object_type == 'box':
            self.rect.x += dx

    def collide_player(self, player):
        if self.rect.colliderect(player.rect):
            if player.velocity_x != 0:
                self.move(player.velocity_x)


    def update(self):
        self.gravity()

