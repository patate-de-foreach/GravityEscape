import pygame, sys
from audio_manager import AudioManager

from buttons import Button
import game_state, credits, histoire


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

        self.type = True


        AudioManager().play_bgm("main_menu", introName="main_menu_intro", loop=-1)

    # fonction qui apelle le jeu
    def Play(self):
        pygame.display.set_caption("GravityEscape - Histoire")

        hisoire = histoire.Histoire(self.screen)
        hisoire.main()

        self.redirect = "level1"
        self.is_finished = True

    def Settings(self):
        pygame.display.set_caption("GravityEscape - Settings")

        self.redirect = "settings"
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
        if pygame.display.get_caption != "GravityEscape - Menu":
            pygame.display.set_caption("GravityEscape - Menu")

        self.screen.blit(self.BackGround, (0, 0))

        # création des boutons
        self.title = Button(
            image=pygame.image.load("assets/title.png"),
            pos=(530, 125),
            scale=1.5,
        )

        self.play = Button(
            image=pygame.image.load("assets/graphics/menubuttons/play.png"),
            pos=(512, 400),
            scale=12,
        )

        self.settings = Button(
            image=pygame.image.load("assets/graphics/menubuttons/settings.png"),
            pos=(100, 700),
            scale=4,
        )

        self.credits = Button(
            image=pygame.image.load("assets/graphics/menubuttons/credits.png"),
            pos=(512, 700),
            scale=4,
        )


        if self.type == True:
            self.type_gameplay = Button(
                image=pygame.image.load("assets/graphics/menubuttons/Bouton_souris.png"),
                pos=(512, 575),
                scale=5,
            )
        else:
            self.type_gameplay = Button(
                image=pygame.image.load("assets/graphics/menubuttons/Bouton_Manette.png"),
                pos=(512, 575),
                scale=5,
            )

        self.credits = Button(
            image=pygame.image.load("assets/graphics/menubuttons/credits.png"),
            pos=(512, 700),
            scale=4,
        )

        self.exit = Button(
            image=pygame.image.load("assets/graphics/menubuttons/exit.png"),
            pos=(924, 700),
            scale=4,
        )

        # detecte les changement si il y a un texte au lieu d'une image
        for button in [self.play, self.settings, self.exit, self.credits, self.title, self.type_gameplay]:
            button.update(self.screen)

        pygame.display.update()

    def mouseClicked(self):
        mouse_pos = pygame.mouse.get_pos()
        if self.play.checkinput(mouse_pos):
            self.Play()
        if self.settings.checkinput(mouse_pos):
            self.Settings()
        if self.credits.checkinput(mouse_pos):
            self.Credits()
        if self.type_gameplay.checkinput(mouse_pos):
            if self.type == True:
                 self.type = False
            else:
                 self.type = True
        if self.title.checkinput(mouse_pos):
            self.easterEgg()
        if self.exit.checkinput(mouse_pos):
            pygame.quit()
            sys.exit()

    def easterEgg(self):
        pass
