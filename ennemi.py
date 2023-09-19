import pygame
import math
import random

from utils import *

class Ennemi:
    def __init__(self, x, y, fenetre):
        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.acceleration = pygame.Vector2(0, 0)
        self.screen = fenetre


        self.image = pygame.Surface((16,16))
        self.rect = self.image.get_rect(topleft = self.position)

        self.dist_target = 50
        self.stop_radius = 150
        self.arrival_radius = 50
        self.health = 10
        self.hit_box_radius = 16
        self.max_speed = 4
        self.max_force = 0.25  # Force d'acceleration

    def update(self):
        self.velocity += self.acceleration
        self.position += self.velocity
        self.acceleration = pygame.Vector2(0, 0)

    def show(self):
        pygame.draw.rect(self.screen, (255, 0, 0), pygame.Rect(int(self.position.x), int(self.position.y), self.hit_box_radius, self.hit_box_radius))


        velocity_line_end = self.position + self.velocity * 10  # Visualisation de la velocité
        acceleration_line_end = self.position + self.acceleration * 10  # Visualisation de la velocité

        #pygame.draw.line(self.screen, (255, 0, 0), (int(self.position.x), int(self.position.y)), (int(velocity_line_end.x), int(velocity_line_end.y)))
        #pygame.draw.line(self.screen, (0, 255, 0), (int(self.position.x), int(self.position.y)), (int(acceleration_line_end.x), int(acceleration_line_end.y)))

        angle = math.degrees(self.velocity.as_polar()[1])
        rotated_triangle = pygame.transform.rotate(pygame.Surface((self.hit_box_radius*2, self.hit_box_radius*2), pygame.SRCALPHA), -angle)
        self.screen.blit(rotated_triangle, (self.position.x - self.hit_box_radius, self.position.y - self.hit_box_radius))

    def get_hitbox(self):
        return pygame.Rect(self.position.x, self.position.y, self.hit_box_radius, self.hit_box_radius)

    def apply_force(self, force):
        self.acceleration += force

    # Fuit la cible
    def flee(self, target):
        desired = target - self.position
        desired.scale_to_length(self.max_speed)
        steering = desired - self.velocity
        steering.scale_to_length(self.max_force)
        self.apply_force(steering)

    # Fonce sur la cible
    def seek(self, target):
        # Si la distance entre l'ennemi et la target et inférieur à DIST_TARGET alors arreter de seek
        if(dist(self.position.x, self.position.y, target.position.x, target.position.y) > 50):

            desired = target.position - self.position

            if abs(desired.x) + abs(desired.y) <= 20:
                print("Captured !!!")
                target.pos = pygame.Vector2(random.randint(0, pygame.display.get_surface().get_width()), random.randint(0, pygame.display.get_surface().get_height()))

            desired.scale_to_length(self.max_speed)
            steering = desired - self.velocity
            if (steering.length() > 1):
                steering.scale_to_length(self.max_force)
            self.apply_force(steering)

    def arrive(self, target):
        desired = pygame.Vector2(target.position.x - self.position.x, target.position.y - self.position.y)
        distance = math.sqrt(desired.x**2 + desired.y**2)

        if distance < self.dist_target:
            # L'agent est proche de la cible, ralentir progressivement
            desired_length = self.max_speed * (distance / self.dist_target)
        else:
            desired_length = self.max_speed

        desired.x = (desired.x / distance) * desired_length
        desired.y = (desired.y / distance) * desired_length

        steering = pygame.Vector2(desired.x - self.velocity.x, desired.y - self.velocity.y)
        self.apply_force(steering)

    def arrive_and_stop(self, target):
        desired = pygame.Vector2(target.position.x - self.position.x, target.position.y - self.position.y)
        distance = math.sqrt(desired.x**2 + desired.y**2)

        if distance < self.stop_radius:
            # L'agent est suffisamment proche pour s'arrêter
            desired.x = 0
            desired.y = 0
        elif distance < self.arrival_radius:
            # L'agent est proche de la cible, ralentir progressivement
            desired_length = self.max_speed * (distance / self.arrival_radius)
            desired.x = (desired.x / distance) * desired_length
            desired.y = (desired.y / distance) * desired_length
        else:
            desired_length = self.max_speed
            desired.x = (desired.x / distance) * desired_length
            desired.y = (desired.y / distance) * desired_length

        steering = pygame.Vector2(desired.x - self.velocity.x, desired.y - self.velocity.y)
        self.apply_force(steering)

    def avoid_collision(self, other_enemy):
        # Calculez la direction de l'autre ennemi par rapport à cet ennemi
        direction = pygame.Vector2(self.position.x - other_enemy.position.x, self.position.y - other_enemy.position.y)
        direction_length = direction.length()
        
        if direction_length < self.hit_box_radius * 2:  # Si les ennemis se chevauchent
            # Calculez une force de répulsion pour les éloigner l'un de l'autre
            repulsion_force = direction.normalize() * (self.max_force * 2)
            self.apply_force(repulsion_force)