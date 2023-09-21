import power_up
import pygame

class Heal_power_up(power_up.Power_up):
    def __init__(self, screen,position, healing_amount):
        super().__init__(screen, position, "HEAL")
        self.healing_amount = healing_amount
        self.image = pygame.image.load("assets/graphics/power_ups/healing_power_up.png")

    def show(self):
        self.screen.blit(self.image, (self.position.x, self.position.y))

    def apply_effect(self, player):
        player.heal(self.healing_amount)
