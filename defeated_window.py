import pygame
from buttons import Button
from player import *

import game_state


class Defeated(game_state.Game_State):
    def __init__(self, screen):
        super().__init__()
        SCREEN_WIDTH, SCREEN_HEIGHT = pygame.display.get_surface().get_size()
        self.BackGround = pygame.image.load(
            "assets/graphics/background/defeated_screen.jpg"
        )
        self.surface = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.SRCALPHA)
        self.screen = screen
        # AudioManager().play_bgm("main_menu", introName="main_menu_intro", loop=-1)

    def run(self):
        self.update()

    def update(self):
        self.screen.blit(self.BackGround, (0, 0))
        self.display_end_score(self.get_last_line("score.txt"))

        self.replay = Button(
            image=pygame.image.load("assets/graphics/menubuttons/playagain.png"),
            pos=(350, 600),
            scale=8,
        )

        self.home = Button(
            image=pygame.image.load("assets/graphics/menubuttons/Home.png"),
            pos=(650, 600),
            scale=8,
        )

        for button in [self.replay, self.home]:
            button.update(self.screen)

        pygame.display.update()

    def mouseClicked(self):
        mouse_pos = pygame.mouse.get_pos()
        if self.replay.checkinput(mouse_pos):
            self.redirect = "level1"
            AudioManager().play_bgm("battle", loop=-1, introName="battle_intro")
            self.is_finished = True
        if self.home.checkinput(mouse_pos):
            self.redirect = "main_menu"
            AudioManager().play_bgm("main_menu", loop=-1, introName="main_menu_intro")
            self.is_finished = True

    def get_last_line(self, filename):
        try:
            with open(filename, "r") as file:
                lines = file.readlines()
                if lines:
                    last_line = lines[
                        -1
                    ].strip()  # Supprime les espaces et les sauts de ligne
                    return last_line
                else:
                    return None  # Le fichier est vide
        except IOError as e:
            print(f"Erreur lors de la lecture du fichier : {e}")
            return None  # Une erreur s'est produite lors de la lecture du fichier

    def display_end_score(self, score):
        self.police = pygame.font.Font("assets/font/BrokenRobot.ttf", 40)
        self.SCREEN_WIDTH, self.SCREEN_HEIGHT = pygame.display.get_surface().get_size()

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
