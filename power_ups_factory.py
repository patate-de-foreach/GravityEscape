from utils import *
from heal_power_up import *
from random import *

class Power_ups_factory():
    def __init__(self, screen,respawn_time, type):
        self.screen = screen
        self.power_ups_list = []
        self.respawn_time = respawn_time
        self.respawn_counter = 0
        self.type = type

    def update(self, player):
        self.check_if_captured(player)
        self.respawn_counter += 1
        # Ajouter un delai sur lequel faire spawn un power up
        if self.respawn_counter >= self.respawn_time:
            self.respawn_counter = 0
            #créé un nouveau powerup
            if self.type == "HEAL":
                new_power_up = Heal_power_up(self.screen,pygame.Vector2(randint(64, 1024-64-32),randint(64, 768-64-32)),healing_amount = 5)
            #l'ajouter a la liste
            self.power_ups_list.append(new_power_up)



    def show(self):
        for power_up in self.power_ups_list:
            power_up.show()

    def check_if_captured(self, player):
        for power_up in self.power_ups_list:
            if player.player_rect.colliderect(power_up.power_up_rect):
                power_up.apply_effect(player)
                self.power_ups_list.remove(power_up)