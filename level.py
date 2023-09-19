import json

import pygame

from mapManager import *
from ennemiFactory import * 


class Level:
    def __init__(self, num_lvl, screen, mapManager, enemmiFactory):
        self.screen = screen
        self.mapManager = mapManager
        self.ennemiFactory = enemmiFactory
        with open('names' + num_lvl + ".csv", newline='') as csvfile:
            self.csv = csv.DictReader(csvfile)
        self.tiles = pygame.image.load('names' + num_lvl + '.png')
        self.obstacle = json.load('names' + num_lvl + '.json')

