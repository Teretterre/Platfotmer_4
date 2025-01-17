import pygame
import json
from my_platform import Platform
from enemy import Enemy
from gameObject import GameObject
from player import Player
from  health import Health
from camera import Camera
import const


class Level:
    def __init__(self, json_file):
        self.level = None
        self.player_size = None
        self.player_start = None
        self.platforms = []
        self.objects = []
        self.enemys = []
        self.level_data = self.load_data(json_file)
        self.create_objects()
        self.hp = []
        self.camera = []

    def load_data(self, json_file):
        with open(json_file, 'r') as file:
            data = json.load(file)
        return data

    def create_objects(self):
        data = self.level_data
        self.level = data["level"]
        self.player_size = data["level_size"]
        self.hp =
        self.player_start = Player(data["player-start"]['x'], data["player-start"]['y'])

        for plat in data["platforms"]:
            self.platforms.append(Platform(plat["x"], plat["y"], plat["width"], plat["height"]))
        for enemy in data["enemys"]:
            self.enemys.append(Enemy(enemy["x"], enemy["y"], enemy["move_distance"], enemy["speed"]))
        for obj in data["objects"]:
            self.objects.append(GameObject(obj["x"], obj["y"], obj["width"], obj["height"], obj["type"]))