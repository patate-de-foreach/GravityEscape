import pygame, sys
import game
from audio_manager import AudioManager

from buttons import Button
import game_state
import credits


# naming : conflit avec "main_menu"
class Start(game_state.Game_State):
    def __init__(self, screen):
        super().__init__()
        SCREEN_WIDTH, SCREEN_HEIGHT = pygame.display.get_surface().get_size()
        self.BackGround = pygame.image.load(
            "assets/graphics/background/Start_Background.png"
        )
        self.logo = pygame.image.load("assets/logo.png")
        self.surface = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.SRCALPHA)
        self.screen = screen
        self.clock = pygame.time.Clock()
        AudioManager().play_bgm("main_menu", introName="main_menu_intro", loop=-1)

    # récupere la font choisi et l'applique au txt demandé
    def get_font(self, size):
        return pygame.font.Font("assets/font/BrokenRobot.ttf", size)

    # fonction qui apelle le jeu
    def Play(self):
        pygame.display.set_caption("GravityEscape - In-Game")
        self.redirect = "level1"
        self.is_finished = True

    def Credits(self):
        pygame.display.set_caption("GravityEscape - Crédits")

        credit = credits.Credits(self.screen)
        credit.main()
    # fonction qqui affiche la page avant la page d'accuil
    def run(self):
        
        pygame.display.set_caption("GravityEscape")
        
        self.Start_page()
        
       
    # affiche la page d'accueil
    def Start_page(self):
        pygame.display.set_caption("GravityEscape - Menu")

        self.screen.blit(self.BackGround, (0, 0))

        mouse_pos = pygame.mouse.get_pos()

        # création des boutons
        self.title = Button(
            image=pygame.image.load("assets/title.png"),
            pos=(530, 125),
            input="",
            font=self.get_font(75),
            color="#ffffff",
            hover_color="red",
            scale=1.5,
        )

        self.play = Button(
            image=pygame.image.load("assets/graphics/menubuttons/play2.png"),
            pos=(512, 400),
            input="",
            font=self.get_font(75),
            color="#ffffff",
            hover_color="red",
            scale=12,
        )

        self.settings = Button(
            image=pygame.image.load("assets/graphics/menubuttons/settings.png"),
            pos=(100, 700),
            input="",
            font=self.get_font(75),
            color="#ffffff",
            hover_color="red",
            scale=4,
        )

        self.credits = Button(
            image=pygame.image.load("assets/graphics/menubuttons/credits.png"),
            pos=(512, 700),
            input="",
            font=self.get_font(75),
            color="#ffffff",
            hover_color="red",
            scale=4,
        )

        self.exit = Button(
            image=pygame.image.load("assets/graphics/menubuttons/exit.png"),
            pos=(924, 700),
            input="",
            font=self.get_font(75),
            color="#ffffff",
            hover_color="red",
            scale=4,
        )

        # detecte les changement si il y a un texte au lieu d'une image
        for button in [self.play, self.settings, self.exit, self.credits, self.title]:
            button.ColorChange(mouse_pos)
            button.update(self.screen)

        # detecte les clicks de souris et choisi quelle bouton est cliquer et lance la fonction demandé
        '''
        for event in pygame.event.get():
            print(event.type == pygame.MOUSEBUTTONDOWN)
            if event.type == pygame.QUIT:
                pygame.quit
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
        '''  

        pygame.display.update()


    def mouseClicked(self):
        mouse_pos = pygame.mouse.get_pos()
        if self.play.checkinput(mouse_pos):
            self.Play()
        if self.settings.checkinput(mouse_pos):
            self.settings()
        if self.credits.checkinput(mouse_pos):
            self.Credits()
        if self.title.checkinput(mouse_pos):
            self.easterEgg()
        if self.exit.checkinput(mouse_pos):
            pygame.quit()
            sys.exit()
    

     
    def easterEgg(self):
        pass
