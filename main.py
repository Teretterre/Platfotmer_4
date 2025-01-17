from random import random
import random
import pygame
from level import Level
from Bullet import Bullet
from my_platform import Platform
from player import Player
from camera import Camera
from enemy import Enemy
from health import Health
from gameObject import GameObject
from Bullet import Bullet
import const
from background import draw_back_gradient, Cloud



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
    l1 = Level('LevelData/lvl_1.json')
    Boxes = [GameObject(400, const.SCREEN_HEIGHT - 600, object_type='box')]




    camera = Camera(const.SCREEN_WIDTH, const.SCREEN_HEIGHT)

    all_sprites = pygame.sprite.Group()
    for plat in platforms:
        all_sprites.add(plat)
    all_sprites.add(player)
    enemys_sprites = pygame.sprite.Group()
    for ene in enemys:
        enemys_sprites.add(ene)
    for obj in Boxes:
        all_sprites.add(Boxes)
    for bull in player.bullets:
        all_sprites.add(bull)

    cloud_spites = pygame.sprite.Group()
    for i in range(20):
        cloud = Cloud(random.randint(0, const.LEVEL_LENGTH), random.randint(40,200), random.randint(100,200), 50)
        cloud_spites.add(cloud)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        for bull in player.bullets:
            all_sprites.add(bull)

        # Обновление всех спрайтов
        all_sprites.update()
        enemys_sprites.update()
        camera.update(player)
        cloud_spites.update()

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
                sprite.check_collision(enemys_sprites, all_sprites)

        # Рендеринг
        draw_back_gradient(screen, (135, 180, 200), (0, 191, 255))
        for sprite in all_sprites:
            screen.blit(sprite.image, camera.apply(sprite))
        for sprite in enemys_sprites:
            screen.blit(sprite.image, camera.apply(sprite))
        for sprite in cloud_spites:
            screen.blit(sprite.image, camera.apply(sprite))

        hp.draw(screen)
        pygame.display.flip()

        clock.tick(const.FPS)

    pygame.quit()

if __name__ == "__main__":
    main()