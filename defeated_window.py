import pygame, sys
from buttons import Button
from hud import Hud
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


    def get_font(self, size):
        return pygame.font.Font("assets/font/BrokenRobot.ttf", size)
    
    def run(self):
        self.update()


    def update(self):
        self.screen.blit(self.BackGround, (0,0))
        self.display_end_score(self.get_last_line("score.txt"))
        mouse_pos = pygame.mouse.get_pos()

        self.replay = Button(
            image=pygame.image.load("assets/graphics/menubuttons/playagain.png"),
            pos=(350, 600),
            input="",
            font=self.get_font(75),
            color="#ffffff",
            hover_color="red",
            scale=8,
        )

        self.home = Button(
            image=pygame.image.load("assets/graphics/menubuttons/Home.png"),
            pos=(650, 600),
            input="",
            font=self.get_font(75),
            color="#ffffff",
            hover_color="red",
            scale=8,
        )

        for button in [self.replay, self.home]:
            button.ColorChange(mouse_pos)
            button.update(self.screen)

        pygame.display.update()

        
    def mouseClicked(self):
        mouse_pos = pygame.mouse.get_pos()
        if self.replay.checkinput(mouse_pos):
            self.redirect = "level1"
            self.is_finished = True
        if self.home.checkinput(mouse_pos):
            self.redirect = "main_menu"
            self.is_finished = True
        
    def get_last_line(self,filename):
        try:
            with open(filename, 'r') as file:
                lines = file.readlines()
                if lines:
                    last_line = lines[-1].strip()  # Supprime les espaces et les sauts de ligne
                    return last_line
                else:
                    return None  # Le fichier est vide
        except IOError as e:
            print(f"Erreur lors de la lecture du fichier : {e}")
            return None  # Une erreur s'est produite lors de la lecture du fichier

    def display_end_score(self,score):
        self.police = pygame.font.Font("assets/font/BrokenRobot.ttf", 40)
        self.SCREEN_WIDTH, self.SCREEN_HEIGHT = pygame.display.get_surface().get_size()
        
        text_dysplay = "Votre score :"
        text_dysplay_surface = self.police.render(text_dysplay, True, (255, 255, 255))
        text_dysplay_rect = text_dysplay_surface.get_rect(
            center=(self.SCREEN_WIDTH // 2, (self.SCREEN_HEIGHT // 2) - 250))
        self.screen.blit(text_dysplay_surface, text_dysplay_rect)

        text_score = str(score)
        text_score_surface = self.police.render(text_score[0:len(text_score) - 11], True, (255, 255, 255))
        text_score_rect = text_score_surface.get_rect(center=(self.SCREEN_WIDTH // 2, (self.SCREEN_HEIGHT // 2) - 200))
        self.screen.blit(text_score_surface, text_score_rect)