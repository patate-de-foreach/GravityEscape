import json
import time

import pygame
from hud import Hud
from audio_manager import AudioManager
from mapManager import *
from ennemiFactory import *
import game_state
import defeated_window
from power_ups_factory import *
from player import *


class Level(game_state.Game_State):
    def __init__(self, num_lvl, screen, clock):
        super().__init__()
        self.screen = screen
        self.num_lvl = num_lvl
        screen_width, screen_height = self.screen.get_size()
        self.clock = clock
        self.player = Player(
            screen_width / 2,
            100,
            self.screen,
            self.charger_controller_type(),
            self.clock,
        )
        self.death_timer = 0
        self.start_run = time.perf_counter()
        self.end_run = 0.0
        # Récupère les infos du level depuis un fichier Json
        self.get_level_config("level_config.json")
        self.level_graphic_resource = pygame.image.load(
            self.level_graphic_resource_path
        )

        AudioManager().play_bgm(
            self.battle_music, loop=-1, introName=self.battle_music_intro
        )

        self.map_manager = MapManager(
            self.tiles_size,
            [self.level_graphic_resource],
            self.csv_path,
            self.level_background_path,
        )
        self.enemy_factory = EnemyFactory(
            self.screen,
            self.player,
            self.nbr_ennemis,
            self.tps_min_spawn,
            self.tps_max_spawn,
            self.clock,
        )
        self.power_up_factory = Power_ups_factory(self.screen, 600, "HEAL")

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
        self.battle_music = level_config["battle_bgm"]
        self.battle_music_intro = level_config["battle_bgm_intro"]

    def run(self):
        # Remise à zero de l'affichage
        self.screen.fill("black")
        self.map_manager.draw_map(self.screen)
        self.player.update()
        self.player.show()

        self.power_up_factory.update(self.player)
        self.power_up_factory.show()

        self.enemy_factory.create_enemy()  # Crée un ennemi à chaque frame
        self.enemy_factory.update_enemies()
        self.check_life()

        if self.enemy_factory.state == "FINISH":
            # OUVRIR LES PORTES
            pass

    def check_life(self):
        if self.player.is_dead:
            if self.end_run == 0.0:
                self.end_run = time.perf_counter()
            if self.death_timer < 100:
                self.death_timer += 1
            else:
                Hud(self.screen, self.player).display_end_score(
                    str(self.end_run - self.start_run)
                )
                self.save_score(
                    "score.txt", str(self.end_run - self.start_run).split(".", 1)[0]
                )
                self.menu_dead()
        else:
            Hud(self.screen, self.player).display_live_score(self.start_run)
            self.enemy_factory.draw_enemies()
            Hud(self.screen, self.player).display_life_bar()

    def menu_dead(self):
        pygame.display.set_caption("GravityEscape - Defeated")

        self.redirect = "defeated"
        self.is_finished = True

    def save_score(self, filename, score):
        try:
            with open(filename, "a") as file:
                file.write(score + "\n")
            print(f"Score sauvegardé dans {filename}")
        except IOError as e:
            print(f"Erreur lors de la sauvegarde du score : {e}")

    def charger_controller_type(self, nom_fichier="setting.json"):
        try:
            # Ouvrir le fichier JSON en lecture
            with open(nom_fichier, "r") as fichier_json:
                # Charger les données JSON depuis le fichier
                data = json.load(fichier_json)

                # Vérifier si l'option 'controller_type' existe dans les données
                if "controller_type" in data:
                    return data["controller_type"]
                else:
                    print(
                        "L'option 'controller_type' n'a pas été trouvée dans le fichier JSON."
                    )
                    return None
        except FileNotFoundError:
            print(f"Le fichier {nom_fichier} n'a pas été trouvé.")
            return None
        except json.JSONDecodeError:
            print(f"Erreur de décodage JSON dans le fichier {nom_fichier}.")
        return None
