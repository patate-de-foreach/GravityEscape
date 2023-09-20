import pygame, sys
import game

from buttons import Button

class Start:
    def __init__(self, screen):
        SCREEN_WIDTH, SCREEN_HEIGHT = pygame.display.get_surface().get_size()
        self.BackGround = pygame.image.load("assets/graphics/background/Start_Background.png")
        self.surface = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.SRCALPHA)
        self.screen = screen

    #récupere la font choisi et l'applique au txt demandé
    def get_font(self,size):
        return pygame.font.Font("assets/font/BrokenRobot.ttf", size)

    # fonction qui apelle le jeu
    def Play(self):
        pygame.display.set_caption("GravityEscape - In-Game")

        while True:    
            gravity_escape = game.Game(self.screen)
            gravity_escape.run()


    # affiche la page d'accueil
    def Start_page(self):
        pygame.display.set_caption("GravityEscape - Menu")

        while True:

            self.screen.blit(self.BackGround, (0,0))

            mouse_pos = pygame.mouse.get_pos()

            # création des boutons
            title = Button(image = pygame.image.load("assets/title.png"), pos=(530,125),
                        input= "", font= self.get_font(75), color="#ffffff", hover_color = "red", scale=1.5)


            play = Button(image = pygame.image.load("assets/graphics/menubuttons/play2.png"), pos=(512,400),
                        input= "", font= self.get_font(75), color="#ffffff", hover_color = "red", scale=12)
            
            settings = Button(image = pygame.image.load("assets/graphics/menubuttons/settings.png"), pos=(100,700),
                        input = "", font= self.get_font(75), color="#ffffff", hover_color = "red", scale=4)
            
            credits = Button(image = pygame.image.load("assets/graphics/menubuttons/credits.png"), pos=(512,700),
                        input = "", font= self.get_font(75), color="#ffffff", hover_color = "red", scale=4)
            
            exit = Button(image = pygame.image.load("assets/graphics/menubuttons/exit.png"), pos=(924,700),
                        input = "", font= self.get_font(75), color="#ffffff", hover_color = "red", scale=4)

        
            # detecte les changement si il y a un texte au lieu d'une image
            for button in [play,settings,exit,credits, title]:
                button.ColorChange(mouse_pos)
                button.update(self.screen)

            # detecte les clicks de souris et choisi quelle bouton est cliquer et lance la fonction demandé
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if play.checkinput(mouse_pos):
                        self.Play()
                    if settings.checkinput(mouse_pos):
                        self.settings()
                    if credits.checkinput(mouse_pos):
                        self.credits()
                    if title.checkinput(mouse_pos):
                        self.easterEgg()
                    if exit.checkinput(mouse_pos):
                        pygame.quit()
                        sys.exit()

            pygame.display.update()


    def easterEgg():
        pass
