import time
import pygame


class Hud:
    def __init__(self, screen, player):
        self.screen = screen
        self.player = player
        self.police = pygame.font.Font("assets/font/BrokenRobot.ttf", 40)
        self.SCREEN_WIDTH, self.SCREEN_HEIGHT = pygame.display.get_surface().get_size()

    def display_life_bar(self):
        if self.player.health >= 0:
            test_barre = pygame.image.load(
                "assets/graphics/barres_de_vie/bdv" + str(self.player.health) + ".png"
            ).convert_alpha()
            self.screen.blit(
                pygame.transform.scale(
                    test_barre,
                    (
                        int(test_barre.get_width() * 1.9),
                        int(test_barre.get_height() * 1.9),
                    ),
                ),
                (860, 725),
            )

    def display_live_score(self, start_run):
        in_progress_run = time.perf_counter()
        live_score_text = f"Score : {in_progress_run - start_run}".split(".", 1)[0]
        live_score_text_surface = self.police.render(
            live_score_text, True, (255, 255, 255)
        )
        live_score_text_rect = live_score_text_surface.get_rect(
            bottomleft=((self.SCREEN_WIDTH // 2) - 440, (self.SCREEN_HEIGHT // 2) + 370)
        )
        self.screen.blit(live_score_text_surface, live_score_text_rect)

    def display_end_score(self, score):
        text_display = "Votre score :"
        text_display_surface = self.police.render(text_display, True, (255, 255, 255))
        text_display_rect = text_display_surface.get_rect(
            center=(self.SCREEN_WIDTH // 2, (self.SCREEN_HEIGHT // 2) - 250)
        )
        self.screen.blit(text_display_surface, text_display_rect)

        text_score = str(score).split(".", 1)[0]
        text_score_surface = self.police.render(text_score, True, (255, 255, 255))
        text_score_rect = text_score_surface.get_rect(
            center=(self.SCREEN_WIDTH // 2, (self.SCREEN_HEIGHT // 2) - 200)
        )
        self.screen.blit(text_score_surface, text_score_rect)
