import pygame
import math
import random

class Player:
    def __init__(self, x, y, fenetre):
        self.position = pygame.Vector2(x, y)
        
        self.velocity = pygame.Vector2(0, 0)
        self.acceleration = pygame.Vector2(0, 0)
        self.screen = fenetre

        self.health = 10
        self.hit_box_radius = 16
        self.maxSpeed = 4
        self.maxForce = 0.25 # Force d'acceleration

    def update(self):
        # La Vélocité est la dérivée de l'acceleration
        self.velocity += self.acceleration
        # La Position est la dérivée de la vélocité
        self.position += self.velocity
        # Mise à zéro de l'accélération
        self.acceleration = pygame.Vector2(0, 0)
        
        
    def get_hitbox(self):
        return pygame.Rect(self.position.x, self.position.y, self.hit_box_radius, self.hit_box_radius)

    def show(self):
        # pygame.draw.circle(self.creen, (255, 255, 255), (int(self.position.x), int(self.position.y)), self.hitBoxRadius)
        pygame.draw.rect(self.screen, (255, 255, 255), pygame.Rect(int(self.position.x), int(self.position.y), self.hit_box_radius, self.hit_box_radius))

        velocityLineEnd = self.position + self.velocity * 10 # Visualisation de la velocité
        accelerationLineEnd = self.position + self.acceleration * 10 # Visualisation de la velocité

        pygame.draw.line(self.screen, (255, 0, 0), (int(self.position.x), int(self.position.y)), (int(velocityLineEnd.x), int(velocityLineEnd.y)))
        pygame.draw.line(self.screen, (0, 255, 0), (int(self.position.x), int(self.position.y)), (int(accelerationLineEnd.x), int(accelerationLineEnd.y)))

        angle = math.degrees(self.velocity.as_polar()[1])
        rotated_triangle = pygame.transform.rotate(pygame.Surface((self.hit_box_radius*2, self.hit_box_radius*2), pygame.SRCALPHA), -angle)
        self.screen.blit(rotated_triangle, (self.position.x - self.hit_box_radius, self.position.y - self.hit_box_radius))

    def apply_force(self, force):
        self.acceleration += force