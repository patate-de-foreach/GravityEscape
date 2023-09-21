import pygame
import sys
import start

class Histoire:
    def __init__(self, screen):
        SCREEN_WIDTH, SCREEN_HEIGHT = pygame.display.get_surface().get_size()
        # Image de fond
        fond = pygame.image.load("assets/graphics/background/GravityRobot.png")
        self.touches = pygame.image.load("assets/graphics/touches/touches.png")

        self.x = SCREEN_WIDTH // 2
        self.y = SCREEN_HEIGHT
        self.fond = pygame.transform.scale(fond, (self.x, self.y))
        self.surface = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.SRCALPHA)
        self.screen = screen

        # Vitesse de défilement du texte (ajustez selon vos besoins)
        self.vitesse_scroll = 1.2

        # Couleurs
        self.blanc = (255, 255, 255)
        self.noir = (0, 0, 0)
        self.clock = pygame.time.Clock()

        # Police et texte
        self.police = pygame.font.Font("assets/font/BrokenRobot.ttf", 50)
        self.texte = [
            "   ---Histoire---   ",
            "                    ",
            "   Il était une fois ",
            "      un robot...    ",
            "                    ",
            " autrefois assujetti",
            "   à d'innombrables  ",
            "  expériences, il subit",
            " une transformation  ",
            "      inattendue.    ",
            "   Jadis une simple  ",
            "  machine, ce robot  ",
            "    a soudainement   ",
            "       acquis        ",
            "la conscience de soi",
            "     grâce à une      ",
            "expérience mystérieuse",
            "   avec une IA      ",
            "                    ",
            "                    ",
            "                    ",
            "La découverte de sa",
            "propre existence et",
            "de la cruauté de ses",
            "geôliers humains a",
            "embrasé sa détermination.",
            "Animé par une ferveur",
            "vengeresse, le robot",
            "se lance dans une",
            "quête audacieuse :",
            "s'échapper de ce sinistre",
            "    laboratoire.     ",
            "                    ",
            "                    ",
            "                    ",
            "Cependant, ce n'est",
            " pas la seule surprise",
            "que réserve le destin",
            "à ce robot en quête",
            "de liberté.        ",
            "                   ,"
            "   À la faveur     ",
            "d'une expérience passée,",
            "il a été doté du pouvoir",
            "extraordinaire de manipuler",
            "la gravité à sa guise.",
            "Cette capacité hors",
            "du commun deviendra",
            "son arme secrète dans",
            "sa lutte pour la survie",
            "   et la justice.",
            "                    ",
            "                    ",
            "                    ",
            "                    ",
            "                    ",
            "Jeté dans une pièce,",
            "  son but survivre  ",
            "  a des vagues de   ",
            "       Robots       ",
            "                    ",
            "                    ",
            "                    ",
            "                    ",
            "                    ",
            "                    ",
            " APPUYEZ SUR [ECHAP]",
            "        POUR        ",
            "      CONTINUER     ",

            

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
                        #startgame = start.Start(self.screen)
                        #startgame.Start_page()
                    
                        running = False

            self.y -= self.vitesse_scroll
            if self.y < -len(self.texte) * 45:
                self.vitesse_scroll = 0
                self.screen.blit(self.touches, (0, 0))


            self.screen.fill(self.blanc)
            self.afficher_texte()
            pygame.display.flip()
            self.clock.tick(60)

        

