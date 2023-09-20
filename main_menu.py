import pygame
import buttons


class MainMenu:
    def __init__(self, width, height, window, surf):
        # on prend la largeur de la fenêtre
        self.screen_width = width
        # on prend la longeur de la fenêtre
        self.screen_height = height
        # on prend la fenêtre
        self.screen = window
        # on prend la surface de la fenêtre
        self.surface = surf

        # etat du jeu ( en pause ou non)
        self.game_paused = False
        # etat du menu : main ou settings
        self.menu_state = "main"
        # etat du son ( activé / desactivé)
        self.sound_state = True

    # Affichage du menu main
    def draw_pause_menu(self):
        # ajout du background noir avec transparence de 120 ( max: 255 / min: 0)
        self.screen.blit(self.surface, (0, 0))
        pygame.draw.rect(
            self.surface, (0, 0, 0, 120), [0, 0, self.screen_width, self.screen_height]
        )

        # image + boutton RESUME
        resume_img = pygame.image.load(
            "assets/graphics/menubuttons/resume.png"
        ).convert_alpha()
        self.resume_button = buttons.Button(
            self.screen_width / 2 - 100, self.screen_height / 3, resume_img, 8
        )

        # image + boutton HOME
        home_img = pygame.image.load(
            "assets/graphics/menubuttons/Home.png"
        ).convert_alpha()
        self.home_button = buttons.Button(
            self.screen_width / 2 + 30, self.screen_height / 2 + 48, home_img, 6
        )

        # image + boutton Settings
        setting_img = pygame.image.load(
            "assets/graphics/menubuttons/settings.png"
        ).convert_alpha()
        self.settings_button = buttons.Button(
            self.screen_width / 2 - 150, self.screen_height / 2 + 50, setting_img, 6
        )

    # Affichage du menu settings
    def draw_settings(self):
        # image + boutton Son -ON
        sound_img = pygame.image.load(
            "assets/graphics/menubuttons/sound.png"
        ).convert_alpha()
        self.sound_button = buttons.Button(
            self.screen_width / 2 - 60, self.screen_height / 3 + 10, sound_img, 6
        )

        # image + boutton Son -OFF
        nosound_img = pygame.image.load(
            "assets/graphics/menubuttons/nosound.png"
        ).convert_alpha()
        self.nosound_button = buttons.Button(
            self.screen_width / 2 - 60, self.screen_height / 3 + 10, nosound_img, 6
        )

        # image + boutton RETOUR
        back_img = pygame.image.load(
            "assets/graphics/menubuttons/goback.png"
        ).convert_alpha()
        self.back_button = buttons.Button(
            self.screen_width / 2 - 450, self.screen_height / 3 - 150, back_img, 5
        )

    # def draw_text(text, font, text_col, x, y, screen):
    #     img = font.render(text, True, text_col)
    #     screen.blit(img, (x,y))

    # Actualisation des etats du menu
    def update_menu(self):
        # si le jeu est en pause : dessiner le menu principal (main)
        if self.game_paused == False:
            self.draw_pause_menu()

            # si letat du menu est main, dessiner les boutons respectifs
            if self.menu_state == "main":
                if self.resume_button.draw(self.screen):
                    self.game_paused = False
                if self.home_button.draw(self.screen):
                    pass
                if self.settings_button.draw(self.screen):
                    self.menu_state = "settings"

            # sinon l'etat settings et donc, dessiner les boutons respectifs
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
