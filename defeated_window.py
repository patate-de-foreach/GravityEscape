import pygame, sys
from buttons import Button

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
    
    def update(self):
        self.screen.blit(self.BackGround, (0,0))

        mouse_pos = pygame.mouse.get_pos()

        self.replay = Button(
            image=pygame.image.load("assets/graphics/menubuttons/play2.png"),
            pos=(400, 600),
            input="",
            font=self.get_font(75),
            color="#ffffff",
            hover_color="red",
            scale=8,
        )

        self.home = Button(
            image=pygame.image.load("assets/graphics/menubuttons/Home.png"),
            pos=(700, 600),
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
           print("replay")
        if self.replay.checkinput(mouse_pos):
           print("home")