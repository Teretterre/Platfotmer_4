import pygame
import json
from platform import Platform


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

    def load_data(self, json_file):
        with open(json_file, 'r') as file:
            data = json.load(file)
        return data

    def create_objects(self):
        data = self.level_data
        self.level = data["level"]
        self.player_size = data["level_size"]
        self.player_start = data["player-start"]

        for plat in data["platforms"]:
            self.platforms.append(Platform(plat["x"], plat["y"], plat["width"], plat["heightc x"]))