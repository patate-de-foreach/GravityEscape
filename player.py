import pygame
import math
from player_controls import *
from sprite_animator import SpriteAnimator
from audio_manager import AudioManager


class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, fenetre, playerControlType, clock):
        pygame.sprite.Sprite.__init__(self)
        self.screen = fenetre
        self.clock = clock
        self.player_control = Player_Controls(playerControlType)
        self.action_dictionnary = {
            "GRAVITY_UP": {
                "left": self.go_left,
                "right": self.go_right,
                "jump": self.jump,
                "gravity_down": "GRAVITY_DOWN",
                "gravity_left": "GRAVITY_LEFT",
                "gravity_right": "GRAVITY_RIGHT",
            },
            "GRAVITY_DOWN": {
                "left": self.go_left,
                "right": self.go_right,
                "jump": self.jump,
                "gravity_up": "GRAVITY_UP",
                "gravity_left": "GRAVITY_LEFT",
                "gravity_right": "GRAVITY_RIGHT",
            },
            "GRAVITY_LEFT": {
                "up": self.go_up,
                "down": self.go_down,
                "jump": self.jump,
                "gravity_down": "GRAVITY_DOWN",
                "gravity_up": "GRAVITY_UP",
                "gravity_right": "GRAVITY_RIGHT",
            },
            "GRAVITY_RIGHT": {
                "up": self.go_up,
                "down": self.go_down,
                "jump": self.jump,
                "gravity_down": "GRAVITY_DOWN",
                "gravity_up": "GRAVITY_UP",
                "gravity_left": "GRAVITY_LEFT",
            },
        }

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.acceleration = pygame.Vector2(0, 0)
        self.friction = 0.1

        self.GRAVITY_STRENGHT = 2.8
        self.jump_force = 60
        self.speed = 2
        self.GRAVITY_DIRECTION = "GRAVITY_DOWN"  # anciennement GRAVITY_SIDE
        self.health = 10
        self.hit_box_radius = 16
        self.max_speed = 1
        self.max_force = 0.2  # Force d'acceleration

        self.original_surface = pygame.image.load(
            "assets/graphics/entities/hero/idle/idle1.png"
        ).convert_alpha()
        self.rotated_surface = pygame.image.load(
            "assets/graphics/entities/hero/idle/idle1.png"
        ).convert_alpha()
        self.player_rect = self.rotated_surface.get_rect(
            midbottom=(self.position.x, self.position.y)
        )

    def update(self):
        # Convertit les touches appuyées par le joueur en actions
        self.velocity += self.acceleration
        self.position += self.velocity
        self.player_rect.x = self.position.x
        self.player_rect.y = self.position.y
        self.acceleration = pygame.Vector2(0, 0)
        self.velocity -= self.velocity * self.friction
        self.apply_gravity()
        self.check_collisions()
        self.convert_control_into_action(self.player_control.get_control_pressed())

    def convert_control_into_action(self, actionSet):
        for action in actionSet:
            if "gravity" in action:
                try:
                    gravity_direction = self.action_dictionnary[self.GRAVITY_DIRECTION][
                        action
                    ]
                    if gravity_direction:
                        self.set_gravity(gravity_direction)
                except Exception as error:
                    pass
            else:
                try:
                    function_action = self.action_dictionnary[self.GRAVITY_DIRECTION][
                        action
                    ]
                    if function_action:
                        function_action()
                except:
                    pass

    def go_up(self):
        self.apply_force((0, -self.speed))

    def go_down(self):
        self.apply_force((0, self.speed))

    def go_left(self):
        self.apply_force((-self.speed, 0))

    def go_right(self):
        self.apply_force((self.speed, 0))

    def jump(self):
        if self.on_floor == True:
            if self.GRAVITY_DIRECTION == "GRAVITY_UP":
                self.apply_force((0, self.jump_force))
            elif self.GRAVITY_DIRECTION == "GRAVITY_DOWN":
                self.apply_force((0, -self.jump_force))
            elif self.GRAVITY_DIRECTION == "GRAVITY_LEFT":
                self.apply_force((self.jump_force, 0))
            elif self.GRAVITY_DIRECTION == "GRAVITY_RIGHT":
                self.apply_force((-self.jump_force, 0))

    def apply_gravity(self):
        # GRAVITY DOWN
        if self.GRAVITY_DIRECTION == "GRAVITY_DOWN":
            self.apply_force((0, self.GRAVITY_STRENGHT))
        # GRAVITY UP
        if self.GRAVITY_DIRECTION == "GRAVITY_UP":
            self.apply_force((0, -self.GRAVITY_STRENGHT))
        # GRAVITY LEFT
        if self.GRAVITY_DIRECTION == "GRAVITY_LEFT":
            self.apply_force((-self.GRAVITY_STRENGHT, 0))
        # GRAVITY RIGHT
        if self.GRAVITY_DIRECTION == "GRAVITY_RIGHT":
            self.apply_force((self.GRAVITY_STRENGHT, 0))

    def show(self):
        self.player_rect.x = self.position.x
        self.player_rect.y = self.position.y
        self.screen.blit(self.rotated_surface, self.player_rect)

    def changeSprite(self, spritePath):
        self.sprite_sheet = pygame.image.load(spritePath)
        self.sprite_animator = SpriteAnimator(
            self.sprite_sheet,
            num_frames=4,
            frame_width=36,
            frame_height=78,
            frame_duration=1000,
        )

    def apply_force(self, force):
        self.acceleration += force

    def check_collisions(self):
        screen_width, screen_height = self.screen.get_size()
        self.on_floor = False
        # Collision mur droite
        if self.position.x + self.player_rect.width > screen_width - 64:
            self.position.x = screen_width - 64 - self.player_rect.width
            if self.GRAVITY_DIRECTION == "GRAVITY_RIGHT":
                self.on_floor = True
        # Collision mur gauche
        if self.position.x < 64:
            self.position.x = 64
            if self.GRAVITY_DIRECTION == "GRAVITY_LEFT":
                self.on_floor = True
        # Collision sol
        if self.position.y + self.player_rect.height > screen_height - 64:
            self.position.y = screen_height - 64 - self.player_rect.height
            if self.GRAVITY_DIRECTION == "GRAVITY_DOWN":
                self.on_floor = True
        # Collision plafond
        if self.position.y < 64:
            self.position.y = 64
            if self.GRAVITY_DIRECTION == "GRAVITY_UP":
                self.on_floor = True

    def set_gravity(self, gravity_direction):
        self.GRAVITY_DIRECTION = gravity_direction
        self.flipSprite()
        AudioManager().player_sounds["gravity"].play()

    def flipSprite(self):
        if self.GRAVITY_DIRECTION == "GRAVITY_DOWN":
            self.rotated_surface = self.original_surface
            self.player_rect = self.rotated_surface.get_rect(
                midbottom=(self.position.x, self.position.y)
            )
        if self.GRAVITY_DIRECTION == "GRAVITY_LEFT":
            self.rotated_surface = pygame.transform.rotate(self.original_surface, -90)
            self.player_rect = self.rotated_surface.get_rect(
                midleft=(self.position.x, self.position.y)
            )
        if self.GRAVITY_DIRECTION == "GRAVITY_UP":
            self.rotated_surface = pygame.transform.rotate(self.original_surface, 180)
            self.player_rect = self.rotated_surface.get_rect(
                midtop=(self.position.x, self.position.y)
            )
        if self.GRAVITY_DIRECTION == "GRAVITY_RIGHT":
            self.rotated_surface = pygame.transform.rotate(self.original_surface, 90)
            self.player_rect = self.rotated_surface.get_rect(
                midright=(self.position.x, self.position.y)
            )
