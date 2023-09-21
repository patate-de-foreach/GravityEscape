import pygame

class Button():
    def __init__(self, image, pos, scale):
        # prends l'image du bouton et la rescale selon la variable scale
        self.image = pygame.transform.scale(image,(int(image.get_width() * scale), int(image.get_height() * scale)))        
        # prends la hauteur et la largeur
        self.x = pos[0]
        self.y = pos[1]

        # prends le rect de l'image et prends le centre selon x et y
        self.rect = self.image.get_rect(center=(self.x, self.y))

    # fonction qui actualise l'ecran et l'image
    def update(self, screen):
        screen.blit(self.image, self.rect)

    def checkinput(self, pos):
        if pos[0] in range(self.rect.left, self.rect.right) and pos[1] in range(self.rect.top, self.rect.bottom):
            return True
        return False
    


        