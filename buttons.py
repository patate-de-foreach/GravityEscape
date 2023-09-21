import pygame

class Button():
    def __init__(self, image, pos, scale):
        self.image = pygame.transform.scale(image,(int(image.get_width() * scale), int(image.get_height() * scale)))        
        self.x = pos[0]
        self.y = pos[1]

        self.rect = self.image.get_rect(center=(self.x, self.y))

    def update(self, screen):
        screen.blit(self.image, self.rect)

    def checkinput(self, pos):
        if pos[0] in range(self.rect.left, self.rect.right) and pos[1] in range(self.rect.top, self.rect.bottom):
            return True
        return False
    


        