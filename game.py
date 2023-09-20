import pygame,sys

import game, player, ennemi, ennemiFactory, obstacle, level, mapManager

class Game:
    def __init__(self, screen):
        
        SCREEN_WIDTH, SCREEN_HEIGHT = pygame.display.get_surface().get_size()
        self.clock = pygame.time.Clock()
        self.Player = player.Player(SCREEN_WIDTH/2,SCREEN_HEIGHT/2,screen, "CLAVIER", self.clock)
        self.initial_state = level.Level(1,screen,self.Player, self.clock)
    
    def eventHandler(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

    def update(self):
        self.initial_state.update_level()

    def run(self):
        while True:
            self.eventHandler()
            self.update()
            pygame.display.update()
            self.clock.tick(60)