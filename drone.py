import pygame
import math
import random
from utils import *
from sprite_animator import *
from ennemi import *


class Drone(Ennemi):
    def __init__(self, x, y, fenetre, clock):
        Ennemi.__init__(self, x, y, fenetre, clock)

        self.anim = {
            "death": "assets/graphics/entities/enemies/drones/1/Death.png",
            "idle": "assets/graphics/entities/enemies/drones/1/Idle.png",
            "scan": "assets/graphics/entities/enemies/drones/1/Scan.png",
            "walk_scan": "assets/graphics/entities/enemies/drones/1/Walk_scan.png",
            "walk": "assets/graphics/entities/enemies/drones/1/Walk.png",
        }

        self.changeSprite(self.anim["walk"])

    def show(self):
        dt = self.clock
        self.sprite_animator.update(dt)
        current_frame = self.sprite_animator.get_current_frame()
        self.screen.blit(current_frame, (self.position.x, self.position.y))
        self.draw_life_bar(self.position.x, self.position.y)

    def changeSprite(self, spritePath):
        self.sprite_sheet = pygame.image.load(spritePath)
        self.sprite_animator = SpriteAnimator(
            self.sprite_sheet,
            num_frames=4,
            frame_width=48,
            frame_height=48,
            frame_duration=1000,
        )
