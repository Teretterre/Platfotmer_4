import  pygame
import  const

class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y, direction):
        super().__init__()
        self.bullet_r_imgs = [
            pygame.transform.scale(pygame.image.load("img/bullet_1.png.png"), [const.BULLET_WIDTH, const.BULLET_HEIGHT]),
            pygame.transform.scale(pygame.image.load("img/bullet_2.png.png"), [const.BULLET_WIDTH, const.BULLET_HEIGHT]),
            pygame.transform.scale(pygame.image.load("img/bullet_3.png.png"), [const.BULLET_WIDTH, const.BULLET_HEIGHT])
        ]
        self.bullet_l_imgs = [
            pygame.transform.scale(pygame.image.load("img/bullet_1L.png.png"),[const.BULLET_WIDTH, const.BULLET_HEIGHT]),
            pygame.transform.scale(pygame.image.load("img/bullet_2L.png.png"),[const.BULLET_WIDTH, const.BULLET_HEIGHT]),
            pygame.transform.scale(pygame.image.load("img/bullet_3L.png.png"), [const.BULLET_WIDTH, const.BULLET_HEIGHT])
        ]
        self.current_img = 0
        if direction > 0:
            self.image = self.bullet_r_imgs[self.current_img]
        else:
            self.image = self.bullet_l_imgs[self.current_img]
        self.rect = self.image.get_rect()
        self.rect.center = [x, y]
        self.velocity = const.BULLET_SPEED * direction
        self.direction = direction
        self.animation_speed = 0.2
        self.start_x = x

    def update(self):
        self.rect.x += self.velocity
        self.current_img += self.animation_speed

        if self.current_img > len(self.bullet_r_imgs):
            self.current_img = 0

        if self.velocity > 0:
            self.image = self.bullet_r_imgs[int(self.current_img)]
        elif self.velocity < 0:
            self.image = self.bullet_r_imgs[int(self.current_img)]

        if self.rect.x - self.start_x > const.SCREEN_WIDTH // 2:
            self.kill()