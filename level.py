import pygame
import json
import csv

import mapManager, ennemiFactory


class Level:
    def __init__(self, screen):
        self.screen = screen

        
        self.mapManager = mapManager.MapManager()

        self.ennemiFactory = ennemiFactory.EnemyFactory() 

        self.obstacles = self.extract_json()


    
    def extract_json(self, json_path):
        json.load(json_path)
        