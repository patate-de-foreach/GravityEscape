import json
import pygame

from audio import Audio
from mapManager import *
from ennemiFactory import * 

class Level:

    def __init__(self, num_lvl, screen, player, clock):
        self.screen = screen
        self.num_lvl = num_lvl
        self.player = player
        self.clock = clock
        
        # Récupère les infos du level depuis un fichier Json
        self.get_level_config("level_config.json")
        self.level_graphic_resource = pygame.image.load(self.level_graphic_resource_path)
        self.map_manager = MapManager(self.tiles_size,[self.level_graphic_resource],self.csv_path)
        self.enemy_factory = EnemyFactory(self.screen, player, self.nbr_ennemis ,self.tps_min_spawn, self.tps_max_spawn, self.clock)
        

    def get_level_config(self,configPath):
        with open(configPath) as json_file:
            self.config_json = json.load(json_file)

        self.level = self.config_json['level' + str(self.num_lvl)]['num_level']
        self.csv_path = self.config_json['level' + str(self.num_lvl)]['csv_path']
        self.level_graphic_resource_path = self.config_json['level' + str(self.num_lvl)]['resource_path']
        self.obstacles_ids = self.config_json['level' + str(self.num_lvl)]['obstacle_list']
        self.open_door_id = self.config_json['level' + str(self.num_lvl)]['open_door']
        self.closed_door_id = self.config_json['level' + str(self.num_lvl)]['closed_door']
        self.nbr_ennemis = self.config_json['level' + str(self.num_lvl)]['nbr_ennemis']
        self.tps_min_spawn = self.config_json['level' + str(self.num_lvl)]['tps_min_spawn']
        self.tps_max_spawn = self.config_json['level' + str(self.num_lvl)]['tps_max_spawn']
        self.tiles_size = self.config_json['level' + str(self.num_lvl)]['tiles_size']
        self.background_music = Audio(self.config_json['level' + str(self.num_lvl)]['music_path']).play

    def update_level(self):
        # Remise à zero de l'affichage
        self.screen.fill('black')

        background_surface = pygame.image.load('assets/graphics/background/awesomeCavePixelArt.png').convert()
        background_surface.set_alpha(120)
        self.screen.blit(background_surface,(0,0))
        self.map_manager.draw_map(self.screen)  # Où 'screen' est la surface Pygame sur laquelle vous voulez dessiner la carte

        self.player.update()
        self.player.show()

        self.enemy_factory.create_enemy()  # Crée un ennemi à chaque frame (vous pouvez ajuster cela)
        
        self.enemy_factory.update_enemies()
        self.enemy_factory.draw_enemies()

        