import pygame, sys
import start

class Loading:
    def __init__(self, screen):
        SCREEN_WIDTH, SCREEN_HEIGHT = pygame.display.get_surface().get_size()
        self.logo = pygame.image.load("assets/logo.png")
        self.screen = screen
        self.clock = pygame.time.Clock()


    # fonction qqui affiche la page avant la page d'accuil
    def starting(self):
        #une clock pour que au bout d'un moment cette page disparaisse et affiche la page principale
        clock = pygame.time.Clock()
        pygame.time.set_timer(pygame.USEREVENT, 200)
        pygame.display.set_caption("GravityEscape")

        start_game = start.Start(self.screen)
        
        self.screen.fill('black')
        counter = 10
        while True:

            # affiche le logo
            self.screen.blit(self.logo, (310,190))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit
                    sys.exit()
                if event.type == pygame.USEREVENT: 
                    #Ici au bout du temps il affiche la page d'accueil
                    counter -= 1
                    if counter > 0:
                        pass
                    else:
                        #Affiche la page d'accueil
                        start_game.Start_page()

            
            pygame.display.flip()
            clock.tick(60)
              
            pygame.display.update()

        

