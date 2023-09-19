import pygame
import math
import random
from utils import *
from sprite_animator import *
from ennemi import *

class Drone(Ennemi):
    def __init__(self, x, y, fenetre):
        super().__init__(x, y, fenetre)
        
        self.anim = {
            "death":"assets/graphics/drones/1/Death.png",
            "idle":"assets/graphics/drones/1/Idle.png",
            "scan":"assets/graphics/drones/1/Scan.png",
            "walk_scan":"assets/graphics/drones/1/Walk_scan.png",
            "walk":"assets/graphics/drones/1/Walk.png",
        }

        self.changeSprite(self.anim["walk"])
        

        self.clock = pygame.time.Clock()

    # Vous pouvez ajouter des méthodes spécifiques à la classe Drone ici
    def show(self):
        dt = self.clock.tick(60)
        self.sprite_animator.update(dt)
        current_frame = self.sprite_animator.get_current_frame()

        self.screen.blit(current_frame, (self.position.x, self.position.y))
    # Si vous avez des attributs ou des méthodes spécifiques à la classe Drone,
    # assurez-vous de les définir ici.
    def changeSprite(self, spritePath):
        self.sprite_sheet = pygame.image.load(spritePath)  # Chargez votre feuille de sprites
        self.sprite_animator = SpriteAnimator(self.sprite_sheet, num_frames=4, frame_width=48, frame_height=48, frame_duration=200)

