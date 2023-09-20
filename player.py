import pygame
import math
from player_controls import *
from sprite_animator import SpriteAnimator

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, fenetre, playerControlType, clock):
        pygame.sprite.Sprite.__init__(self)
        self.screen = fenetre
        self.clock = clock
        # self.changeSprite(self.anim["idle"])
        self.player_control = Player_Controls(playerControlType)
        self.action_dictionnary = {
            "GRAVITY_UP":{
                "left" : self.go_left,
                "right" : self.go_right,
                "jump" : self.jump,
                "gravity_down" : "GRAVITY_DOWN",
                "gravity_left" : "GRAVITY_LEFT", 
                "gravity_right" : "GRAVITY_RIGHT",
            },
            "GRAVITY_DOWN":{
                "left" : self.go_left,
                "right" : self.go_right,
                "jump" : self.jump,
                "gravity_up" : "GRAVITY_UP",
                "gravity_left" : "GRAVITY_LEFT", 
                "gravity_right" : "GRAVITY_RIGHT",
            },
            "GRAVITY_LEFT":{
                "up": self.go_up,
                "down" : self.go_down,
                "jump" : self.jump,
                "gravity_down" : "GRAVITY_DOWN",
                "gravity_up" : "GRAVITY_UP",
                "gravity_right" : "GRAVITY_RIGHT",
            },
            "GRAVITY_RIGHT":{
                "up": self.go_up,
                "down" : self.go_down,
                "jump" : self.jump,
                "gravity_down" : "GRAVITY_DOWN",
                "gravity_up" : "GRAVITY_UP",
                "gravity_left" : "GRAVITY_LEFT", 
            }
        }
        

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.acceleration = pygame.Vector2(0, 0)
        self.friction = 0.1
       
        self.GRAVITY_STRENGHT = 2.8
        self.jump_force = 60
        self.speed = 2
        self.GRAVITY_SIDE = "GRAVITY_DOWN"  # anciennement GRAVITY_SIDE
        self.health = 10
        self.hit_box_radius = 16
        self.maxSpeed = 1
        self.maxForce = 0.2 # Force d'acceleration

    def update(self):
        # Convertit les touches appuyées par le joueur en actions
        self.velocity += self.acceleration
        self.position += self.velocity
        self.acceleration = pygame.Vector2(0, 0)
        self.velocity -= self.velocity * self.friction
        self.apply_gravity()
        self.convert_control_into_action(self.player_control.get_control_pressed())

    def convert_control_into_action(self, actionSet):
        print(actionSet)
        for action in actionSet:
            if "gravity" in action:
                try:
                    gravity_direction = self.action_dictionnary[self.GRAVITY_SIDE][action]
                    if gravity_direction:
                        self.set_gravity(gravity_direction)
                except:
                    pass
            else:
                try:
                    function_action = self.action_dictionnary[self.GRAVITY_SIDE][action]
                    if function_action:
                        function_action()
                except:
                    pass


    def go_up(self):
        self.apply_force((0,-self.speed))

    def go_down(self):
        self.apply_force((0,self.speed))

    def go_left(self):
        self.apply_force((-self.speed,0))

    def go_right(self):
        self.apply_force((self.speed,0))

    def jump(self):
        if self.on_floor == True:
            if self.GRAVITY_SIDE == "GRAVITY_UP":
                self.apply_force((0,self.jump_force))
            elif self.GRAVITY_SIDE == "GRAVITY_DOWN":
                self.apply_force((0,-self.jump_force))
            elif self.GRAVITY_SIDE == "GRAVITY_LEFT":
                self.apply_force((self.jump_force,0))
            elif self.GRAVITY_SIDE == "GRAVITY_RIGHT":
                self.apply_force((-self.jump_force,0))
        
    def apply_gravity(self):
        if self.GRAVITY_SIDE == "GRAVITY_DOWN":
            # GRAVITY DOWN
            if self.position.y <= 640 :
                self.apply_force((0,self.GRAVITY_STRENGHT))
                self.on_floor = False
            else:
                self.on_floor = True
                self.position.y = 640
        # GRAVITY UP
        if self.GRAVITY_SIDE == "GRAVITY_UP":
            # GRAVITY UP
            if self.position.y >= 120 :
                self.apply_force((0,-self.GRAVITY_STRENGHT))
                self.on_floor = False
            else:
                self.on_floor = True
                self.position.y = 120
        # GRAVITY LEFT
        if self.GRAVITY_SIDE == "GRAVITY_LEFT":
            # GRAVITY LEFT
            if self.position.x >= 124 :
                self.apply_force((-self.GRAVITY_STRENGHT,0))
                self.on_floor = False
            else:
                self.on_floor = True
                self.position.x = 120
        # GRAVITY RIGHT
        if self.GRAVITY_SIDE == "GRAVITY_RIGHT":
            # GRAVITY RIGHT
            if self.position.x <= 890 :
                self.apply_force((self.GRAVITY_STRENGHT,0))
                self.on_floor = False
            else:
                self.on_floor = True
                self.position.x = 890
        
    def get_hitbox(self):
        return pygame.Rect(self.position.x, self.position.y, self.hit_box_radius, self.hit_box_radius)

    def show(self):
        # pygame.draw.circle(self.creen, (255, 255, 255), (int(self.position.x), int(self.position.y)), self.hitBoxRadius)
        # Ancienne gestion par rectangle
        # pygame.draw.rect(self.screen, (255, 255, 255), pygame.Rect(int(self.position.x), int(self.position.y), self.hit_box_radius, self.hit_box_radius))
        #gestion du sprite
        # dt = self.clock.tick(60)
        # self.sprite_animator.update(dt)
        # current_frame = self.sprite_animator.get_current_frame()
        player_surface = pygame.image.load("assets/graphics/entities/hero/idle/idle1.png").convert_alpha()
        player_rect = player_surface.get_rect(midbottom = (self.position.x,self.position.y))
        self.screen.blit(player_surface, player_rect)

    def changeSprite(self, spritePath):
        self.sprite_sheet = pygame.image.load(spritePath)
        self.sprite_animator = SpriteAnimator(self.sprite_sheet, num_frames=4, frame_width=36, frame_height=78, frame_duration=1000)

    def apply_force(self, force):
        self.acceleration += force

    def avoid_collision(self, obstacle):

        # Calculez la direction de l'autre ennemi par rapport à cet ennemi
        direction = pygame.Vector2(self.position.x - obstacle.position.x, self.position.y - obstacle.position.y)
        direction_length = direction.length()

        if direction_length < self.hit_box_radius * 2:  # Si les ennemis se chevauchent
            # Calculez une force de répulsion pour les éloigner l'un de l'autre
            repulsion_force = direction.normalize() * (self.max_force * 2)

            self.apply_force(repulsion_force)

    def set_gravity(self, gravity_direction):
        self.GRAVITY_SIDE = gravity_direction
        self.flipSprite()

    def flipSprite():
        pass

