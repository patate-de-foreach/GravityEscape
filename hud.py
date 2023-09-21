import time
import pygame

class Hud:
    def __init__(self, screen, player):
        self.screen = screen
        self.player = player
        self.police = pygame.font.Font("assets/font/BrokenRobot.ttf", 40)
        self.SCREEN_WIDTH, self.SCREEN_HEIGHT = pygame.display.get_surface().get_size()

    def dysplay_life_bar(self):
        if self.player.health >= 0:
            test_barre = pygame.image.load('assets/graphics/barres_de_vie/bdv' + str(self.player.health) + '.png').convert_alpha()
            self.screen.blit(pygame.transform.scale(test_barre, (int(test_barre.get_width() * 1.9), int(test_barre.get_height() * 1.9))), (860, 725))

    def dysplay_live_score(self, start_run):
        in_progress_run = time.perf_counter()
        text_live_score = "Score : " + str(in_progress_run - start_run)
        text_live_score_surface = self.police.render(text_live_score[0:len(text_live_score) - 13], True, (255, 255, 255))
        text_live_score_rect = text_live_score_surface.get_rect(
            bottomleft=((self.SCREEN_WIDTH // 2) - 440, (self.SCREEN_HEIGHT // 2) + 370))
        self.screen.blit(text_live_score_surface, text_live_score_rect)

    def dysplay_end_score(self, score):
        text_dysplay = "Votre score :"
        text_dysplay_surface = self.police.render(text_dysplay, True, (255, 255, 255))
        text_dysplay_rect = text_dysplay_surface.get_rect(
            center=(self.SCREEN_WIDTH // 2, (self.SCREEN_HEIGHT // 2) - 250))
        self.screen.blit(text_dysplay_surface, text_dysplay_rect)

        text_score = str(score)
        text_score_surface = self.police.render(text_score[0:len(text_score) - 11], True, (255, 255, 255))
        text_score_rect = text_score_surface.get_rect(center=(self.SCREEN_WIDTH // 2, (self.SCREEN_HEIGHT // 2) - 200))
        self.screen.blit(text_score_surface, text_score_rect)