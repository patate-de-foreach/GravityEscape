import pygame
from level import Level
from game_state import Game_State


class LevelManager(Game_State):
    def __init__(self, clock, screen, player):
        super().__init__()
        self.clock = clock
        self.current_level_num = 2
        self.screen = screen
        self.player = player

        # redirect l'état level1, level2, etc

    def set_current_level(self, num_level):
        self.set_current_level = num_level

    def init_level(self):
        return Level(self.current_level, self.screen, self.Player, self.clock)

    def run(self):
        self.init_level()

    # créer méthode "set level to run" qui attribue le numéro du level
    # dans run(), initie le level associé à la variable d'instance "num_level"
