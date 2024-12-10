import pygame
import random
import const
import camera

def draw_back_gradient(screen, start_color, end_color):
    widht, height = screen.get_size()
    for y in range(height):
        r = start_color[0] + (end_color[0] - start_color[0]) * y // height
        g = start_color[1] + (end_color[1] - start_color[1]) * y // height
        b = start_color[2] + (end_color[2] - start_color[2]) * y // height
        pygame.draw.line(screen, (r, g, b), (0, y), (widht, y))



class Cloud(pygame.sprite.Sprite):
    def __init__(self, x, y, widht, height):
        super().__init__()
        self.image = pygame.image.load(random.choice(['img/cloud1.png', 'img/cloud2.png', 'img/cloud3.png', 'img/cloud4.png'])).convert_alpha()
        self.image = pygame.transform.scale(self.image, (widht, height))
        self.image.set_alpha(128)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = random.uniform(const.CLOUD_SPEED_START, const.CLOUD_SPEED_END)


    def update(self):
        self.rect.x += self.speed
        if self.rect.left > const.LEVEL_LENGTH:
            self.rect.x = 0 - self.rect.width
            self.rect.y = random.randint(50, 150)
