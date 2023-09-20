import pygame, sys
from buttons import Button

class Mainmenu():
    def __init__(self,screen):
        # on prends la largeur de la fenêtre
        SCREEN_WIDTH, SCREEN_HEIGHT = pygame.display.get_surface().get_size()
        self.settings_back = pygame.image.load("assets/graphics/background/settings_back.jpg")

        #on prends la longeur de la fenêtre
        
        # on prends la fenêtre
        self.screen = screen
        #on prends la surface de la fenêtre
        self.surface = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.SRCALPHA)

        # etat du jeu ( en pause ou non)
        self.game_paused = False
        #etat du menu : main ou settings 
        self.menu_state = "main"
        #etat du son ( activer / desactiver)
        self.sound_state = True

        self.mouse_pos = pygame.mouse.get_pos()


    #Affichage du menu main
    def draw_pause_menu(self):
 
        #image + boutton RESUME
        resume = Button(image = pygame.image.load("assets/graphics/menubuttons/resume.png"), pos=(512,400),
                        input= "", font= Button.get_font(self,size=75), color="#ffffff", hover_color = "red", scale=11)
        
        for button in [resume]:
            button.ColorChange(self.mouse_pos)
            button.update(self.screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if resume.checkinput(self.mouse_pos):
                    self.settings()


            pygame.display.update()

        #image + boutton HOME
        # home_img = pygame.image.load("assets/graphics/menubuttons/Home.png").convert_alpha()
        # self.home_button = buttons.Button(self.screen_width/2+30, self.screen_height/2+48, home_img, 6)

        #image + boutton Settings
        # setting_img = pygame.image.load("assets/graphics/menubuttons/settings.png").convert_alpha()
        # self.settings_button = buttons.Button(self.screen_width/2-150, self.screen_height/2+50, setting_img, 6)

        
    #Affichage du menu settings
    def draw_settings(self):
        state_sound = True

        self.screen.blit(self.settings_back, (0,0))
        
        #image + boutton Son -ON
        
        sound = Button(image = pygame.image.load("assets/graphics/menubuttons/sound.png"), pos=(512,400),
            input= "", font= Button.get_font(self,size=75), color="#ffffff", hover_color = "red", scale=8)
            
        nosound = Button(image = pygame.image.load("assets/graphics/menubuttons/nosound.png"), pos=(512,400),
            input= "", font= Button.get_font(self,size=75), color="#ffffff", hover_color = "red", scale=8)
        
        title = Button(image = pygame.image.load("assets/graphics/background/settings_typo.png"), pos=(530,125),
            input= "", font= Button.get_font(self,size=75), color="#ffffff", hover_color = "red", scale=0.8)
        
        back = Button(image = pygame.image.load("assets/graphics/menubuttons/goback.png"), pos=(100,125),
            input= "", font= Button.get_font(self,size=75), color="#ffffff", hover_color = "red", scale=3)
            
        for button in [sound, nosound, title, back]:
            button.ColorChange(self.mouse_pos)
            button.update(self.screen)


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                # if state_sound == True:
                #     if sound.checkinput(self.mouse_pos):
                #         state_sound = False
                # else:
                #     if nosound.checkinput(self.mouse_pos):
                #         state_sound = True
                if back.checkinput(self.mouse_pos):
                    pass
                


            pygame.display.update()
        # #image + boutton Son -OFF
        # nosound_img = pygame.image.load("assets/graphics/menubuttons/nosound.png").convert_alpha()
        # self.nosound_button = buttons.Button(self.screen_width/2-60, self.screen_height/3+10, nosound_img, 6)

        # #image + boutton RETOUR
        # back_img = pygame.image.load("assets/graphics/menubuttons/goback.png").convert_alpha()
        # self.back_button = buttons.Button(self.screen_width/2-450, self.screen_height/3-150, back_img, 5)
        pass




    # def draw_text(text, font, text_col, x, y, screen):
    #     img = font.render(text, True, text_col)
    #     screen.blit(img, (x,y))

    
    #Actualisation des etats du menu
    def update_menu(self):
        #si le jeu est en pause : dessiner le menu principal (main)
        if self.game_paused == False:
            self.draw_pause_menu()

            # si letat du menu est main dessiner les boutons respectifs
            if self.menu_state == "main":
                if self.resume_button.draw(self.screen):
                    self.game_paused = False
                if self.home_button.draw(self.screen):
                    pass
                if self.settings_button.draw(self.screen):
                    self.menu_state = "settings"
            
            # sinon letat settings et donc dessiner les boutons respectifs
            if self.menu_state == "settings":
                self.draw_settings()
                if self.sound_state == True:
                    if self.sound_button.draw(self.screen):
                        self.sound_state = False
                else:
                    if self.nosound_button.draw(self.screen):
                        self.sound_state = True
                
                if self.back_button.draw(self.screen):
                    self.menu_state = "main"
    