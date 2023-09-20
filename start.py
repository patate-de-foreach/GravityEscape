import pygame, sys
import game

from buttons import Button
import game_state

class Start(game_state.Game_State):
    def __init__(self, screen):
        super().__init__()
        SCREEN_WIDTH, SCREEN_HEIGHT = pygame.display.get_surface().get_size()
        self.BackGround = pygame.image.load("assets/graphics/background/Start_Background.png")
        self.logo = pygame.image.load("assets/logo.png")
        self.surface = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.SRCALPHA)
        self.screen = screen
        self.clock = pygame.time.Clock()

    #récupere la font choisi et l'applique au txt demandé
    def get_font(self,size):
        return pygame.font.Font("assets/font/BrokenRobot.ttf", size)

    # fonction qui apelle le jeu
    def Play(self):
        pygame.display.set_caption("GravityEscape - In-Game")
        self.redirect = "level1"
        self.is_finished = True
        

    # fonction qqui affiche la page avant la page d'accuil
    def run(self):
        #une clock pour que au bout d'un moment cette page disparaisse et affiche la page principale
        clock = pygame.time.Clock()
        pygame.time.set_timer(pygame.USEREVENT, 200)

        pygame.display.set_caption("GravityEscape")

        self.screen.fill('black')
        counter = 10
        
        self.Start_page()
        '''
        while self.logo_run:
            
            # affiche le logo
            self.screen.blit(self.logo, (310,190))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit
                    sys.exit()
                if event.type == pygame.USEREVENT: 
                    counter -= 1
                    if counter > 0:
                        pass
                    else:
                        self.logo_run = False
                        self.Start_page()
        '''
        pygame.display.flip()
        clock.tick(60)
            
        pygame.display.update()


    # affiche la page d'accueil
    def Start_page(self):
        

        pygame.display.set_caption("GravityEscape - Menu")

        

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

