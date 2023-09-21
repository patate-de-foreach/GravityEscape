import pygame
import math
from player_controls import *
from sprite_animator import SpriteAnimator
from audio_manager import AudioManager
from utils import import_folder


class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, fenetre, playerControlType, clock):
        pygame.sprite.Sprite.__init__(self)
        self.screen = fenetre
        self.clock = clock


        self.import_player_assets()
        self.frame_index = 0
        self.animation_speed = 0.15
        # self.image = self.animations['idle'][self.frame_index]
        self.original_surface = self.animations['idle'][self.frame_index]
        self.rotated_surface = self.animations['idle'][self.frame_index]

        self.anim_state = 'idle'
        self.anim_orientation = 'unchanged'

        self.player_control = Player_Controls(playerControlType)
        self.action_dictionnary = {
            "GRAVITY_UP": {
                "attack": self.trigger_attack,
                "left": self.go_left,
                "right": self.go_right,
                "jump": self.jump,
                "gravity_down": "GRAVITY_DOWN",
                "gravity_left": "GRAVITY_LEFT",
                "gravity_right": "GRAVITY_RIGHT",
            },
            "GRAVITY_DOWN": {
                "attack": self.trigger_attack,
                "left": self.go_left,
                "right": self.go_right,
                "jump": self.jump,
                "gravity_up": "GRAVITY_UP",
                "gravity_left": "GRAVITY_LEFT",
                "gravity_right": "GRAVITY_RIGHT",
            },
            "GRAVITY_LEFT": {
                "attack": self.trigger_attack,
                "up": self.go_up,
                "down": self.go_down,
                "jump": self.jump,
                "gravity_down": "GRAVITY_DOWN",
                "gravity_up": "GRAVITY_UP",
                "gravity_right": "GRAVITY_RIGHT",
            },
            "GRAVITY_RIGHT": {
                "attack": self.trigger_attack,
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

        
        self.attack_cooldown = 50
        self.current_cooldown_attack = 0
        self.attack_damage = 1
        self.attack_range = 80
        self.is_attacking = False
        self.GRAVITY_STRENGHT = 2.8
        self.jump_force = 60
        self.speed = 2
        self.GRAVITY_DIRECTION = "GRAVITY_DOWN"  # anciennement GRAVITY_SIDE
        self.health = 10
        self.hit_box_radius = 16
        self.max_speed = 1
        self.max_force = 0.2  # Force d'acceleration
        self.player_rect = self.rotated_surface.get_rect(
            midbottom=(self.position.x, self.position.y)
        )
    
    def import_player_assets(self):
        animation_path = "assets/graphics/entities/hero"
        self.animations = {
            'attack':[],
            'death':[],
            'hurt':[],
            'idle':[],
            'init':[],
            'walk':[]
        }
        for animation in self.animations.keys():
            full_path = animation_path + '/' + animation
            self.animations[animation] = import_folder(full_path)
            # self.flipped_animations[animation] = import_folder(full_path)

    #fait défiler les frames d'animation (change le contenu de original surface)
    def animate(self):
        animation = self.animations[self.anim_state]

        self.frame_index += self.animation_speed
        if self.frame_index >= len(animation):
            self.frame_index = 0
        self.image = self.flipSprite(animation[int(self.frame_index)])
    
    def set_anim_state(self, state):
        self.anim_state = state
        

    def update(self):
        # self.image = self.rotated_surface
        # Convertit les touches appuyées par le joueur en actions
        self.velocity += self.acceleration
        self.position += self.velocity
        self.player_rect.x = self.position.x
        self.player_rect.y = self.position.y
        self.acceleration = pygame.Vector2(0, 0)
        self.velocity -= self.velocity * self.friction
        self.apply_gravity()
        self.check_collisions()
        self.cooldown_attack()
        self.convert_control_into_action(self.player_control.get_control_pressed())
        self.animate()

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
                    action_function = self.action_dictionnary[self.GRAVITY_DIRECTION][
                        action
                    ]
                    if action_function:
                        action_function()
                except:
                    pass

    def cooldown_attack(self):
        if self.is_attacking == True:
            self.current_cooldown_attack -= 1
        if self.current_cooldown_attack <= 0:
            self.current_cooldown_attack = 0
            self.is_attacking = False
        
    def go_up(self):
        if self.on_floor:
            self.set_anim_state('walk')
            if self.GRAVITY_DIRECTION == 'GRAVITY_LEFT':
                self.anim_orientation = 'flipped'
            elif self.GRAVITY_DIRECTION == 'GRAVITY_RIGHT':
                self.anim_orientation = 'unchanged'
        self.apply_force((0, -self.speed))
        

    def go_down(self):
        if self.on_floor:
            self.set_anim_state('walk')
            if self.GRAVITY_DIRECTION == 'GRAVITY_LEFT':
                self.anim_orientation = 'unchanged'
            elif self.GRAVITY_DIRECTION == 'GRAVITY_RIGHT':
                self.anim_orientation = 'flipped'
        self.apply_force((0, self.speed))

    def go_left(self):
        if self.on_floor:
            self.set_anim_state('walk')
            if self.GRAVITY_DIRECTION == 'GRAVITY_DOWN':
                self.anim_orientation = 'flipped'
            elif self.GRAVITY_DIRECTION == 'GRAVITY_UP':
                self.anim_orientation = 'unchanged'
        self.apply_force((-self.speed, 0))

    def go_right(self):
        if self.on_floor:
            self.set_anim_state('walk')
            if self.GRAVITY_DIRECTION == 'GRAVITY_DOWN':
                self.anim_orientation = 'unchanged'
            elif self.GRAVITY_DIRECTION == 'GRAVITY_UP':
                self.anim_orientation = 'flipped'
        self.apply_force((self.speed, 0))

    def trigger_attack(self):
        if self.is_attacking == False and self.current_cooldown_attack == 0:
            self.is_attacking = True
            self.current_cooldown_attack = self.attack_cooldown

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
        self.screen.blit(self.image, self.player_rect)

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
        
        AudioManager().player_sounds["gravity"].play()

    def flipSprite(self, sprite):
        if self.anim_orientation == 'flipped':
            sprite = pygame.transform.flip(sprite, flip_x=True, flip_y=False)
        if self.GRAVITY_DIRECTION == "GRAVITY_DOWN":
            self.player_rect = sprite.get_rect(
                midbottom=(self.position.x, self.position.y)
            )
        if self.GRAVITY_DIRECTION == "GRAVITY_LEFT":
            sprite = pygame.transform.rotate(sprite, -90)
            self.player_rect = self.rotated_surface.get_rect(
                midleft=(self.position.x, self.position.y)
            )
        if self.GRAVITY_DIRECTION == "GRAVITY_UP":
            sprite = pygame.transform.rotate(sprite, 180)
            self.player_rect = self.rotated_surface.get_rect(
                midtop=(self.position.x, self.position.y)
            )
        if self.GRAVITY_DIRECTION == "GRAVITY_RIGHT":
            sprite = pygame.transform.rotate(sprite, 90)
            self.player_rect = self.rotated_surface.get_rect(
                midright=(self.position.x, self.position.y)
            )
        return sprite
