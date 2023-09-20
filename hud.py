import pygame


class Hud:
    def __init__(self, screen, player):
        self.screen = screen
        self.player = player

    def dysplay_life_bar(self):
        test_barre = pygame.image.load('assets/graphics/barres_de_vie/bdv' + str(self.player.health) + '.png').convert_alpha()
        self.screen.blit(pygame.transform.scale(test_barre, (int(test_barre.get_width() * 1.9), int(test_barre.get_height() * 1.9))), (860, 725))
        print(self.player.health)
