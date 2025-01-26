import pygame
import json
import random
from my_platform import Platform
from enemy import Enemy
from gameObject import GameObject
from player import Player
from  health import Health
from camera import Camera
import const
from background import Cloud
from Bullet import Bullet

class Level:
    def __init__(self, json_file):
        self.level = None
        self.level_size = None
        self.player = None
        self.platforms = []
        self.objects = []
        self.enemys = []
        self.level_data = self.load_data(json_file)
        self.hp = Health()
        self.camera = Camera(const.SCREEN_WIDTH, const.SCREEN_HEIGHT)
        self.all_sprites = pygame.sprite.Group()
        self.enemys_sprites = pygame.sprite.Group()
        self.cloud_spites = []

        self.create_objects()

    def load_data(self, json_file):
        with open(json_file, 'r') as file:
            data = json.load(file)
        return data

    def create_objects(self):
        data = self.level_data
        self.level = data["level"]
        self.level_size = data["level_size"]
        self.player = Player(data["player-start"]['x'], data["player-start"]['y'])

        for plat in data["platforms"]:
            self.platforms.append(Platform(plat["x"], plat["y"], plat["width"], plat["height"]))

        for enemy in data["enemys"]:
            self.enemys.append(Enemy(enemy["x"], enemy["y"], enemy["move_distance"], enemy["speed"]))

        for obj in data["objects"]:
            self.objects.append(GameObject(obj["x"], obj["y"], obj["width"], obj["height"], obj["type"]))



        for plat in self.platforms:
            self.all_sprites.add(plat)

        for obj in self.objects:
            self.all_sprites.add(obj)

        self.all_sprites.add(self.player)

        for ene in self.enemys:
            self.enemys_sprites.add(ene)

        for i in range(20):
            cloud = Cloud(random.randint(0, const.LEVEL_LENGTH), random.randint(40, 200), random.randint(100, 200), 50)
            self.cloud_spites.add(cloud)


    def update(self):

        for bull in self.player.bullets:
            self.all_sprites.add(bull)

        # Обновление всех спрайтов
        self.all_sprites.update()
        self.enemys_sprites.update()
        self.camera.update(self.player)
        self.cloud_spites.update()

        # Проверка коллизий
        self.player.check_collision(self.platforms, self.objects)
        enemy_collisions = pygame.sprite.spritecollide(self.player, self.enemys_sprites, True)

        if enemy_collisions:
            self.hp.lose_hp()
            if self.hp.hp == 0:
                print("ВЫВОД ОКНА ПРОИГРЫША")
        for obj in self.objects:
            obj.collide_player(self.player)

        for sprite in self.all_sprites:
            if isinstance(sprite, Bullet):
                sprite.check_collision(self.enemys_sprites, self.all_sprites)

    def render(self, screen):
        # Рендеринг
        self.draw_back_gradient(screen, (135, 180, 200), (0, 191, 255))
        for sprite in self.all_sprites:
            screen.blit(sprite.image, self.camera.apply(sprite))
        for sprite in self.enemys_sprites:
            screen.blit(sprite.image, self.camera.apply(sprite))
        for sprite in self.cloud_spites:
            screen.blit(sprite.image, self.camera.apply(sprite))

        self.hp.draw(screen)