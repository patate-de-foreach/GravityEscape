import pygame
from buttons import Button
import game_state


class Settings(game_state.Game_State):
    def __init__(self, screen):
            super().__init__()
            SCREEN_WIDTH, SCREEN_HEIGHT = pygame.display.get_surface().get_size()
            self.BackGround = pygame.image.load(
            "assets/graphics/background/settings_back.jpg"
            )
            self.screen = screen

            self.sound_state = True


    def get_font(self, size):
            return pygame.font.Font("assets/font/BrokenRobot.ttf", size)


    def run(self):
         self.draw_settings()


     # Affichage du menu settings
    def draw_settings(self):
        # image + boutton Son -ON
        self.screen.blit(self.BackGround, (0, 0))

        mouse_pos = pygame.mouse.get_pos()

        if self.sound_state == True:
             
            self.sound = Button(
                image=pygame.image.load("assets/graphics/menubuttons/sound.png"),
                pos=(512, 400),
                input="",
                font=self.get_font(75),
                color="#ffffff",
                hover_color="red",
                scale=8,
            )
        else:
             
            self.sound = Button(
                image=pygame.image.load("assets/graphics/menubuttons/nosound.png"),
                pos=(512, 400),
                input="",
                font=self.get_font(75),
                color="#ffffff",
                hover_color="red",
                scale=8,
            )

        self.back = Button(
                image=pygame.image.load("assets/graphics/menubuttons/goback.png"),
                pos=(100, 100),
                input="",
                font=self.get_font(75),
                color="#ffffff",
                hover_color="red",
                scale=3,
            )
        
        self.title = Button(
                image=pygame.image.load("assets/graphics/background/settings_typo.png"),
                pos=(512, 150),
                input="",
                font=self.get_font(75),
                color="#ffffff",
                hover_color="red",
                scale=1,
            )

        for button in [self.sound, self.back, self.title]:
            button.ColorChange(mouse_pos)
            button.update(self.screen)

        pygame.display.update()


    def mouseClicked(self):
        mouse_pos = pygame.mouse.get_pos()
        
        if self.sound.checkinput(mouse_pos):
            if self.sound_state == True:
                 self.sound_state = False
            else:
                 self.sound_state = True
        if self.back.checkinput(mouse_pos):
            self.redirect = "main_menu"
            self.is_finished = True
        

        
