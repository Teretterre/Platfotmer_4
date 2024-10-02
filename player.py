import pygame
import const

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        # Загрузка и масштабирование картинок
        self.walk_r_imgs = [
            pygame.transform.scale(pygame.image.load("img/player_r_1.png"), [const.PLAYER_WIDTH, const.PLAYER_HEIGHT]),
            pygame.transform.scale(pygame.image.load("img/player_r_2.png"), [const.PLAYER_WIDTH, const.PLAYER_HEIGHT]),
            pygame.transform.scale(pygame.image.load("img/player_r_3.png"), [const.PLAYER_WIDTH, const.PLAYER_HEIGHT]),
            pygame.transform.scale(pygame.image.load("img/player_r_4.png"), [const.PLAYER_WIDTH, const.PLAYER_HEIGHT])
        ]
        self.walk_l_imgs = [
            pygame.transform.scale(pygame.image.load("img/player_L_1.png"), [const.PLAYER_WIDTH, const.PLAYER_HEIGHT]),
            pygame.transform.scale(pygame.image.load("img/player_L_2.png"), [const.PLAYER_WIDTH, const.PLAYER_HEIGHT]),
            pygame.transform.scale(pygame.image.load("img/player_L_3.png"), [const.PLAYER_WIDTH, const.PLAYER_HEIGHT])
        ]
        self.current_img = 0
        self.image = self.walk_r_imgs[self.current_img]
        self.rect = self.image.get_rect()
        self.rect.topleft = [x, y]
        self.velocity_y = 0
        self.velocity_x = 0
        self.on_ground = False

    def update(self):
        keys = pygame.key.get_pressed()
        self.velocity_x = 0
        if keys[pygame.K_LEFT]:
            self.current_img += 0.1
            self.velocity_x -= const.PLAYER_SPEED
        if keys[pygame.K_RIGHT]:
            self.current_img += 0.1
            self.velocity_x += const.PLAYER_SPEED
        if keys[pygame.K_SPACE] and self.on_ground:
            self.velocity_y = -const.JUMP_STRENGTH
            self.on_ground = False

        self.velocity_y += const.GRAVITY

        if self.rect.bottom > const.SCREEN_HEIGHT - 30:
            self.velocity_y = 0
            self.rect.bottom = const.SCREEN_HEIGHT - 30
            self.on_ground = True

        if self.current_img > 3:
            self.current_img = 0

        if self.velocity_x > 0:
            self.image = self.walk_r_imgs[int(self.current_img)]
        elif self.velocity_x < 0:
            self.image = self.walk_l_imgs[int(self.current_img)]


    def check_collision(self, platforms):
        # Проверка горизонтальных колизий
        self.rect.x += self.velocity_x
        collisions = pygame.sprite.spritecollide(self, platforms, False)
        for platform in collisions:
            if self.velocity_x > 0:
                self.rect.right = platform.rect.left
            elif self.velocity_x < 0:
                self.rect.left = platform.rect.right

        # Проверка вертикальных колизий
        self.rect.y += self.velocity_y
        collisions = pygame.sprite.spritecollide(self, platforms, False)
        for platform in collisions:
            if self.velocity_y > 0:
                self.rect.bottom = platform.rect.top
                self.on_ground = True
            elif self.velocity_y < 0:
                self.rect.top = platform.rect.bottom
            self.velocity_y = 0