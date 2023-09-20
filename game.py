import pygame, sys

import game, player, ennemi, ennemiFactory, obstacle, level, mapManager, start


class Game:
    def __init__(self, screen):
        SCREEN_WIDTH, SCREEN_HEIGHT = pygame.display.get_surface().get_size()
        self.clock = pygame.time.Clock()
        self.Player = player.Player(
            SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, screen, "CLAVIER", self.clock
        )

        # Initialisation constructeur des game_state
        self.main_menu = start.Start(screen)
        self.level1 = level.Level(1, screen, self.Player, self.clock)

        # Début du jeu state initial
        self.set_state("main_menu")

    def eventHandler(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

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

            # Vérifie si l'état est terminée
            self.update()
            pygame.display.update()
            self.clock.tick(60)

    def set_state(self, new_state):
        self.current_state = new_state
        self.current_state_object = self.get_current_state_object()

    def get_current_state_object(self):
        if self.current_state == "main_menu":
            return self.main_menu
        elif self.current_state == "level1":
            return self.level1
