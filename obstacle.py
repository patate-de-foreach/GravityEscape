import pygame


class Obstacle:
    def __init__(self, x1, y1, x2, y2, fenetre):
        self.position1 = pygame.Vector2(x1, y1)
        self.position2 = pygame.Vector2(x2,y2)
        
        #self.image = pygame.Surface((16,16))
        #self.rect = self.image.get_rect(topleft = self.position)

        self.screen = fenetre


    def get_hitbox(self):
        return pygame.Rect(self.position.x, self.position.y, self.hit_box_radius, self.hit_box_radius)

    def show(self):
        pygame.draw.line(self.screen, (255, 255, 0), (int(self.position1.x), int(self.position1.y)), (int(self.position2.x), int(self.position2.y)))
        
