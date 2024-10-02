import pygame
import const

class Health:
    def __init__(self, total_hp=3):
        self.total_hp = total_hp
        self.hp = total_hp

    def lose_hp(self):
        self.hp -= 1

    def add_hp(self):
        self.hp += 1

    def reset_hp(self):
        self.hp = self.total_hp

    def draw(self, surface):
        for i in range(self.hp):
            pygame.draw.circle(surface, const.GREEN, [30 * i + 30, 30], 15)
