import pygame


class Hud:
    def __init__(self, screen, player):
        self.screen = screen
        self.player = player

    def dysplay_life_bar(self):
        test_barre = pygame.image.load('assets/graphics/barres_de_vie/bdv' + str(self.player.health) + '.png').convert_alpha()
        self.screen.blit(test_barre, (10, 10))
        print(self.player.health)
