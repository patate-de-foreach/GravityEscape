import json
import pygame
from hud import Hud
from audio_manager import AudioManager
from mapManager import *
from ennemiFactory import *
import game_state


class Level(game_state.Game_State):
    def __init__(self, num_lvl, screen, player, clock):
        super().__init__()
        self.screen = screen
        self.num_lvl = num_lvl
        self.player = player
        self.clock = clock
        self.death_timer = 0
        # Récupère les infos du level depuis un fichier Json
        self.get_level_config("level_config.json")
        self.level_graphic_resource = pygame.image.load(
            self.level_graphic_resource_path
        )

        AudioManager().play_bgm(self.background_music, loop=-1)

        self.map_manager = MapManager(
            self.tiles_size,
            [self.level_graphic_resource],
            self.csv_path,
            self.level_background_path,
        )
        self.enemy_factory = EnemyFactory(
            self.screen,
            player,
            self.nbr_ennemis,
            self.tps_min_spawn,
            self.tps_max_spawn,
            self.clock,
        )

    def get_level_config(self, configPath):
        with open(configPath) as json_file:
            self.config_json = json.load(json_file)
        level_config = self.config_json["level" + str(self.num_lvl)]

        self.level = level_config["num_level"]
        self.csv_path = level_config["csv_path"]
        self.level_graphic_resource_path = level_config["resource_path"]
        self.level_background_path = level_config["background_path"]
        self.open_door_id = level_config["open_door"]
        self.closed_door_id = level_config["closed_door"]
        self.nbr_ennemis = level_config["nbr_ennemis"]
        self.tps_min_spawn = level_config["tps_min_spawn"]
        self.tps_max_spawn = level_config["tps_max_spawn"]
        self.tiles_size = level_config["tiles_size"]
        self.background_music = level_config["roaming_bgm"]
        self.battle_music = level_config["battle_bgm"]
        self.battle_music_intro = level_config["battle_bgm_intro"]

    def run(self):
        # Remise à zero de l'affichage
        self.screen.fill("black")
        self.map_manager.draw_map(self.screen)
        self.player.update()
        self.player.show()
        self.enemy_factory.create_enemy()  # Crée un ennemi à chaque frame

        self.enemy_factory.update_enemies()
        self.check_life()
        print(self.player.is_dead)
        print(self.death_timer)

        if self.enemy_factory.state == "FINISH":
            # OUVRIR LES PORTES
            pass

    def check_life(self):
        if self.player.is_dead:
            if self.death_timer < 80:
                self.death_timer += 1
            else:
                image = pygame.image.load(
                    "assets/graphics/background/defeated_screen.jpg"
                )
                self.screen.blit(image, (0, 0))
                # play game over music
        else:
            self.enemy_factory.draw_enemies()
            Hud(self.screen, self.player).dysplay_life_bar()
