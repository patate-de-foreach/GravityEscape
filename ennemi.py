import pygame
import math
import random

class Ennemi:
    def __init__(self, x, y, fenetre):
        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.acceleration = pygame.Vector2(0, 0)
        self.screen = fenetre

        self.distTarget = 50
        self.health = 10
        self.hitBoxRadius = 16
        self.maxSpeed = 4
        self.maxForce = 0.25 # Force d'acceleration

    def update(self):
        self.velocity += self.acceleration
        self.position += self.velocity
        self.acceleration = pygame.Vector2(0, 0)

    def show(self):
        # pygame.draw.circle(self.creen, (255, 255, 255), (int(self.position.x), int(self.position.y)), self.hitBoxRadius)
        pygame.draw.rect(self.screen, (255, 255, 255), pygame.Rect(int(self.position.x), int(self.position.y), self.hitBoxRadius, self.hitBoxRadius))

        velocityLineEnd = self.position + self.velocity * 10 # Visualisation de la velocité
        accelerationLineEnd = self.position + self.acceleration * 10 # Visualisation de la velocité

        pygame.draw.line(self.creen, (255, 0, 0), (int(self.position.x), int(self.position.y)), (int(velocityLineEnd.x), int(velocityLineEnd.y)))
        pygame.draw.line(self.creen, (0, 255, 0), (int(self.position.x), int(self.position.y)), (int(accelerationLineEnd.x), int(accelerationLineEnd.y)))

        angle = math.degrees(self.velocity.as_polar()[1])
        rotated_triangle = pygame.transform.rotate(pygame.Surface((self.hitBoxRadius*2, self.hitBoxRadius*2), pygame.SRCALPHA), -angle)
        self.creen.blit(rotated_triangle, (self.position.x - self.hitBoxRadius, self.position.y - self.hitBoxRadius))

    def apply_force(self, force):
        self.acceleration += force

    # Fuit la cible
    def flee(self, target):
        desired = target - self.position
        desired.scale_to_length(self.maxSpeed)
        steering = desired - self.velocity
        steering.scale_to_length(self.maxForce)
        self.apply_force(steering)

    # Fonce sur la cible
    def seek(self, target):
        # Si la distance entre l'ennemi et la target et inférieur à DIST_TARGET alors arreter de seek

        desired = target.pos - self.position
        '''
        if abs(desired.x) + abs(desired.y) <= 20:
            print("Captured !!!")
            target.pos = pygame.Vector2(random.randint(0, pygame.display.get_surface().get_width()), random.randint(0, pygame.display.get_surface().get_height()))
        '''
        desired.scale_to_length(self.maxSpeed)
        steering = desired - self.velocity
        steering.scale_to_length(self.maxForce)
        self.apply_force(steering)
