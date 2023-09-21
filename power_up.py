import pygame

class Power_up():
    def __init__(self,screen,position, type):
        self.screen = screen
        self.type = type
        self.position = position
        self.largeur = self.hauteur = 32
        self.power_up_rect =  self.power_up_rect = pygame.Rect(position.x, position.y, self.largeur, self.hauteur)
    
    def show(self):
        pass

    def apply_effect(self):
        pass