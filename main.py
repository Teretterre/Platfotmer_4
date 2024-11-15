import pygame

from Bullet import Bullet
from platform import Platform
from player import Player
from camera import Camera
from enemy import Enemy
from health import Health
from gameObject import GameObject
from Bullet import Bullet
import const

# Инициализация Pygame
pygame.init()

# Создание окна
screen = pygame.display.set_mode((const.SCREEN_WIDTH, const.SCREEN_HEIGHT))
pygame.display.set_caption("Platformer Game")
clock = pygame.time.Clock()

# перезапуск игры
def reset_game(hp):
    hp.reset_hp()
    main()

# Игровой цикл
def main():
    player = Player(500, const.SCREEN_HEIGHT - 100)

    platforms = [
        Platform(0, const.SCREEN_HEIGHT - 30, const.LEVEL_LENGTH, 30),
        Platform(400, 500, 150, 20),
        Platform(600, 400, 150, 20),
        Platform(900, 300, 150, 20),
        Platform(1300, 450, 150, 20),
        Platform(1600, 350, 150, 20),
        Platform(2000, 300, 150, 20),
        Platform(2500, 450, 150, 20),
        Platform(3000, 500, 150, 20),
        Platform(3200, 400, 150, 20),
        Platform(3400, 300, 150, 20),
        Platform(3700, 200, 150, 20),
        Platform(3900, 100, 150, 20),
    ]
    enemys = [
        Enemy(700, const.SCREEN_HEIGHT - 70, 50, 1),
        Enemy(1000, const.SCREEN_HEIGHT - 70, 150),
        Enemy(1500, const.SCREEN_HEIGHT - 70, 30, 1)
    ]

    Boxes = [GameObject(400, const.SCREEN_HEIGHT - 600, object_type='box')]

    hp = Health()

    camera = Camera(const.SCREEN_WIDTH, const.SCREEN_HEIGHT)

    all_sprites = pygame.sprite.Group()
    for plat in platforms:
        all_sprites.add(plat)
    all_sprites.add(player)
    enemys_sprites = pygame.sprite.Group()
    for ene in enemys:
        enemys_sprites.add(ene)
    for obj in Boxes:
        enemys_sprites.add(Boxes)
    for bull in player.bullets:
        all_sprites.add(bull)


    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Обновление всех спрайтов
        all_sprites.update()
        enemys_sprites.update()
        camera.update(player)

        # Проверка коллизий
        player.check_collision(platforms, Boxes)
        enemy_collisions = pygame.sprite.spritecollide(player, enemys_sprites, True)

        if enemy_collisions:
            hp.lose_hp()
            if hp.hp == 0:
                reset_game(hp)
        for obj in Boxes:
            obj.collide_player(player)

        for sprite in all_sprites:
            if isinstance(sprite, Bullet) :
                sprite.check_collision(enemys, all_sprites)

        # Рендеринг
        screen.fill(const.WHITE)
        for sprite in all_sprites:
            screen.blit(sprite.image, camera.apply(sprite))
        for sprite in enemys_sprites:
            screen.blit(sprite.image, camera.apply(sprite))
        hp.draw(screen)
        pygame.display.flip()

        clock.tick(const.FPS)

    pygame.quit()

if __name__ == "__main__":
    main()