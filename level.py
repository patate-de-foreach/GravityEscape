import json
import pygame
from mapManager import *
from ennemiFactory import * 

class Level:
    def __init__(self, num_lvl, screen):
        self.screen = screen
        self.num_lvl = num_lvl
        # self.mapManager = MapManager()
        # self.enemyFactory = EnemyFactory()
        # self.tiles = pygame.image.load('names' + str(num_lvl) + '.png')
        with open('testConfig.json') as json_file:
            self.obstacle = json.load(json_file)

        self.level = self.obstacle['levels' + str(self.num_lvl)]['num_level']
        self.csv_path = self.obstacle['levels' + str(self.num_lvl)]['csv_path']
        self.list_obstacle = self.obstacle['levels' + str(self.num_lvl)]['list_obstacle']
        self.opened_door = self.obstacle['levels' + str(self.num_lvl)]['opened_door']
        self.closed_door = self.obstacle['levels' + str(self.num_lvl)]['closed_door']
        self.nbr_enemi = self.obstacle['levels' + str(self.num_lvl)]['nbr_enemi']
        self.tps_min_spawn = self.obstacle['levels' + str(self.num_lvl)]['tps_min_spawn']
        self.tps_max_spawn = self.obstacle['levels' + str(self.num_lvl)]['tps_max_spawn']
        self.tiles_size = self.obstacle['levels' + str(self.num_lvl)]['tiles_size']