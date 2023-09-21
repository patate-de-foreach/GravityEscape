import pygame
import sys

import level
import player
import start
import defeated_window


class Game:
    def __init__(self, screen):
        SCREEN_WIDTH, SCREEN_HEIGHT = pygame.display.get_surface().get_size()
        self.screen = screen
        self.clock = pygame.time.Clock()
        self.Player = player.Player(
            SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, screen, "CLAVIER", self.clock
        )

        # Initialisation à None des game_states
        self.main_menu = None
        self.level1 = None
        self.defeated = None

        # Début du jeu state initial
        self.set_state("main_menu")

    def eventHandler(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.current_state_object != None:
                    self.current_state_object.mouseClicked()

    def update(self):
        # Va chercher le current_state et display sa fonction de run
        if (
            self.current_state_object != None
            and self.current_state_object.is_finished == True
        ):
            self.set_state(self.current_state_object.redirect)

    def run(self):
        while True:
            self.eventHandler()  # event fermeture fenetre
            self.current_state_object = self.get_current_state_object()

            # Lance la boucle principale de l'état en cours
            self.current_state_object.run()

            # Vérifie si l'état est terminé
            self.update()
            pygame.display.update()
            self.clock.tick(60)

    def set_state(self, new_state):
        self.current_state = new_state
        self.current_state_object = self.get_current_state_object()

    # Retourne le game_state actuel.
    # S'il n'est pas initialisé, l'initialise
    def get_current_state_object(self):
        if self.current_state == "main_menu":
            if self.main_menu == None:
                self.main_menu = start.Start(self.screen)
            return self.main_menu
        elif self.current_state == "level1":
            if self.level1 == None:
                self.level1 = level.Level(1, self.screen, self.Player, self.clock)
            return self.level1
        elif self.current_state == "defeated":
            if self.defeated == None:
                self.defeated = defeated_window.Defeated(self.screen)
            return self.defeated
