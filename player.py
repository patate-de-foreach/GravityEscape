import pygame
from player_controls import *
from audio_manager import AudioManager
from utils import import_folder


class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, fenetre, playerControlType, clock):
        pygame.sprite.Sprite.__init__(self)
        self.screen = fenetre
        self.clock = clock

        # animation
        self.import_player_assets()
        self.frame_index = 0
        self.animation_speed = 0.15
        self.rotated_surface = self.animations["idle"][self.frame_index]

        self.anim_state = "idle"
        self.anim_orientation = "unchanged"
        self.is_walking = False
        self.is_dead = False

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

        self.player_rect = self.rotated_surface.get_rect(
            midbottom=(self.position.x, self.position.y)
        )

        self.attack_cooldown = 35
        self.current_cooldown_attack = 0
        self.attack_damage = 10
        self.attack_range = 80

        self.is_attacking = False

        self.friction = 0.1
        self.GRAVITY_STRENGHT = 2.6
        self.jump_force = 35
        self.speed = 1.3
        self.max_speed = 0.5
        self.max_force = 0.1  # Force d'acceleration

        self.GRAVITY_DIRECTION = "GRAVITY_DOWN"  # anciennement GRAVITY_SIDE
        self.max_health = 10
        self.health = self.max_health

        self.hit_box_radius = 16

    def import_player_assets(self):
        animation_path = "assets/graphics/entities/hero"
        self.animations = {
            "attack": [],
            "death": [],
            "hurt": [],
            "idle": [],
            "walk": [],
        }
        for animation in self.animations.keys():
            full_path = animation_path + "/" + animation
            self.animations[animation] = import_folder(full_path)

    # fait défiler les frames d'animation
    def animate(self):
        if (
            not self.is_walking
            and self.anim_state != "attack"
            and self.anim_state != "death"
            and self.anim_state != "hurt"
        ):
            self.anim_state = "idle"
        animation = self.animations[self.anim_state]

        if self.anim_state == "death" and self.frame_index == 0:
            AudioManager().play_bgm("game_over", loop=-1, introName="game_over_intro")

        if self.frame_index > len(animation) - 1:
            if self.anim_state == "death":
                self.is_dead = True
                self.frame_index = len(animation) - 1
            else:
                self.frame_index = 0
                if self.anim_state == "attack" or self.anim_state == "hurt":
                    self.frame_index = len(animation) - 1
                    self.anim_state = "idle"
                    self.animation_speed = 0.15

        else:
            self.frame_index += self.animation_speed

        self.image = self.flipSprite(animation[int(self.frame_index)])

    def update(self):
        self.check_hp()
        # Convertit les touches appuyées par le joueur en actions
        self.is_walking = False
        self.velocity += self.acceleration
        self.position += self.velocity
        self.player_rect.x = self.position.x
        self.player_rect.y = self.position.y
        self.acceleration = pygame.Vector2(0, 0)
        self.velocity -= self.velocity * self.friction
        self.apply_gravity()
        self.cooldown_attack()
        self.convert_control_into_action(self.player_control.get_control_pressed())
        self.animate()
        self.check_collisions()

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
        if self.anim_state != "death":
            if self.on_floor:
                if self.anim_state != "attack" and self.anim_state != "hurt":
                    self.anim_state = "walk"
                if self.GRAVITY_DIRECTION == "GRAVITY_LEFT":
                    self.anim_orientation = "flipped"
                elif self.GRAVITY_DIRECTION == "GRAVITY_RIGHT":
                    self.anim_orientation = "unchanged"
                self.apply_force((0, -self.speed))
                self.is_walking = True

    def go_down(self):
        if self.anim_state != "death":
            if self.on_floor:
                if self.anim_state != "attack" and self.anim_state != "hurt":
                    self.anim_state = "walk"
            if self.GRAVITY_DIRECTION == "GRAVITY_LEFT":
                self.anim_orientation = "unchanged"
            elif self.GRAVITY_DIRECTION == "GRAVITY_RIGHT":
                self.anim_orientation = "flipped"
            self.apply_force((0, self.speed))
            self.is_walking = True

    def go_left(self):
        if self.anim_state != "death":
            if self.on_floor:
                if self.anim_state != "attack" and self.anim_state != "hurt":
                    self.anim_state = "walk"
            if self.GRAVITY_DIRECTION == "GRAVITY_DOWN":
                self.anim_orientation = "flipped"
            elif self.GRAVITY_DIRECTION == "GRAVITY_UP":
                self.anim_orientation = "unchanged"
            self.apply_force((-self.speed, 0))
            self.is_walking = True

    def go_right(self):
        if self.anim_state != "death":
            if self.on_floor:
                if self.anim_state != "attack" and self.anim_state != "hurt":
                    self.anim_state = "walk"
            if self.GRAVITY_DIRECTION == "GRAVITY_DOWN":
                self.anim_orientation = "unchanged"
            elif self.GRAVITY_DIRECTION == "GRAVITY_UP":
                self.anim_orientation = "flipped"
            self.apply_force((self.speed, 0))
            self.is_walking = True

    def trigger_attack(self):
        if self.anim_state != "death":
            if self.is_attacking == False and self.current_cooldown_attack == 0:
                self.is_attacking = True
                self.current_cooldown_attack = self.attack_cooldown
                AudioManager().player_sounds["attack"].play()
                self.anim_state = "attack"
                self.animation_speed = 0.13
                self.frame_index = 0

    def jump(self):
        if self.anim_state != "death":
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

    def apply_force(self, force):
        self.acceleration += force

    def check_collisions(self):
        screen_width, screen_height = self.screen.get_size()
        self.on_floor = False
        # Collision mur droite
        if self.GRAVITY_DIRECTION == "GRAVITY_RIGHT":
            if self.position.x + self.player_rect.height > screen_width - 64:
                self.position.x = screen_width - 64 - self.player_rect.height
                self.on_floor = True
        else:
            if self.position.x + self.player_rect.width > screen_width - 64:
                self.position.x = screen_width - 64 - self.player_rect.width

        # Collision mur gauche
        if self.GRAVITY_DIRECTION == "GRAVITY_LEFT":
            if self.position.x < 64:
                self.position.x = 64
                self.on_floor = True
        else:
            if self.position.x < 64:
                self.position.x = 64

        # Collision sol
        if self.GRAVITY_DIRECTION == "GRAVITY_DOWN":
            if self.position.y + self.player_rect.height > screen_height - 64:
                self.position.y = screen_height - 64 - self.player_rect.height
                self.on_floor = True
        else:
            if self.position.y + self.player_rect.width > screen_height - 64:
                self.position.y = screen_height - 64 - self.player_rect.width

        # Collision plafond
        if self.GRAVITY_DIRECTION == "GRAVITY_UP":
            if self.position.y < 64:
                self.position.y = 64
                self.on_floor = True
        else:
            if self.position.y < 64:
                self.position.y = 64

    def receive_damage(self, damage):
        if self.anim_state != "death":
            self.health -= damage
            self.anim_state = "hurt"
            self.animation_speed = 0.1
            self.frame_index = 0
            AudioManager().player_sounds["hurt"].play()

    def check_hp(self):
        if self.health <= 0 and self.anim_state != "death":
            self.health = 0
            self.frame_index = 0
            self.animation_speed = 0.1
            self.anim_state = "death"

    def set_gravity(self, gravity_direction):
        if self.anim_state != "death":
            self.GRAVITY_DIRECTION = gravity_direction
            AudioManager().player_sounds["gravity"].play()

    def flipSprite(self, sprite):
        if self.anim_orientation == "flipped":
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

    def heal(self, healing_amount):
        self.health += healing_amount
        # Vérification que la vie du personnage ne soit pas trop élever
        if self.health > self.max_health:
            self.health = self.max_health
