import pygame

class Histoire:
    def __init__(self, screen):
        # Obtenir la taille de la surface de l'écran
        SCREEN_WIDTH, SCREEN_HEIGHT = pygame.display.get_surface().get_size()
        
        # Chargement de l'image de fond
        fond = pygame.image.load("assets/graphics/touches/touches.png")

        self.x = SCREEN_WIDTH // 2  # Position x du texte
        self.y = SCREEN_HEIGHT  # Position y initiale du texte
        self.fond = pygame.transform.scale(fond, (self.x, self.y))  # Mise à l'échelle de l'image de fond
        self.surface = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.SRCALPHA)  # Création d'une surface transparente pour le texte
        self.screen = screen

        # Vitesse de défilement du texte (ajustez selon vos besoins)
        self.vitesse_scroll = 1.3

        # Couleurs
        self.blanc = (255, 255, 255)
        self.noir = (0, 0, 0)
        self.clock = pygame.time.Clock()

        # Police et texte de l'histoire
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
            "                   ",
            "                   ",
            "                   ",
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
            "Jetté dans une pièce,",
            "son but est de survivre",
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
        self.screen.blit(self.fond, (0, 0))  # Affichage de l'image de fond
        y_pos = self.y  # Position verticale initiale du texte
        for ligne in self.texte:
            texte_surface = self.police.render(ligne, True, self.noir)  # Rendu du texte avec la police et la couleur
            texte_rect = texte_surface.get_rect(center=(self.x + 250, y_pos))  # Positionnement du texte au centre
            self.screen.blit(texte_surface, texte_rect)  # Affichage du texte à l'écran
            y_pos += 50  # Espacement vertical entre les lignes de texte

    def main(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        running = False

            self.y -= self.vitesse_scroll  # Déplacement vertical du texte vers le haut
            if self.y < -len(self.texte) * 45:  # Arrêt du défilement une fois que tous les crédits sont passés
                self.vitesse_scroll = 0

            self.screen.fill(self.blanc)  # Remplissage de l'écran avec la couleur blanche
            self.afficher_texte()  # Affichage du texte
            pygame.display.flip()  # Mise à jour de l'affichage
            self.clock.tick(60)  # Limite de rafraîchissement à 60 images par seconde
