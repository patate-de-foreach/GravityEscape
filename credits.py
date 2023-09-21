import pygame

class Credits:
    def __init__(self, screen):
        SCREEN_WIDTH, SCREEN_HEIGHT = pygame.display.get_surface().get_size()
        # Image de fond
        fond = pygame.image.load("assets/graphics/background/GravityRobot.png")
        self.x = SCREEN_WIDTH // 2
        self.y = SCREEN_HEIGHT
        self.fond = pygame.transform.scale(fond, (self.x, self.y))
        self.surface = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.SRCALPHA)
        self.screen = screen

        # Vitesse de défilement du texte (ajustez selon vos besoins)
        self.vitesse_scroll = 1.6

        # Couleurs
        self.blanc = (255, 255, 255)
        self.noir = (0, 0, 0)
        self.clock = pygame.time.Clock()

        # Police et texte
        self.police = pygame.font.Font("assets/font/BrokenRobot.ttf", 40)
        self.texte = [
            "---Gravity Escape---",
            "                    ",
            "      CREDITS       ",
            "                    ",
            "Par Patate de Foreach",
            "                    ",
            "                    ",
            "  --DEVELOPPEURS--  ",
            "                    ",
            "      -Hugo-        ",
            "                    ",
            "                    ",
            "      -Alexy-       ",
            "                    ",
            "                    ",
            "      -Maxime-      ",
            "                    ",
            "                    ",
            "      -Diego-       ",
            "                    ",
            "                    ",
            "                    ",
            "    --MUSIQUES--    ",
            "                    ",
            "      -Hugo-        ",
            "                    ",
            "                    ",
            "                    ",
            "     --ASSETS--     ",
            "                    ",
            "      Pris sur      ",
            "       Itch.io      ",
            "                    ",
            "                    ",
            "                    ",
            "                    ",
            "                    ",
            "                    ",
            "      MERCI !!!     ",
            "                    ",
            "                    ",

        ]






    def afficher_texte(self):
        self.screen.blit(self.fond, (0, 0))
        y_pos = self.y
        for ligne in self.texte:
            texte_surface = self.police.render(ligne, True, self.noir)
            texte_rect = texte_surface.get_rect(center=(self.x+250, y_pos))
            self.screen.blit(texte_surface, texte_rect)
            y_pos += 50  # Espacement entre les lignes de texte


    def main(self):
        global y

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        running = False

            self.y -= self.vitesse_scroll
            if self.y < -len(self.texte) * 30:
                self.vitesse_scroll = 0


            self.screen.fill(self.blanc)
            self.afficher_texte()
            pygame.display.flip()
            self.clock.tick(60)

        

