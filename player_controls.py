import pygame

import player

class Player_Controls:
    
    def __init__(self, controllerType):
        self.controller_type = controllerType
        if self.controller_type == "MANETTE":
            # Initialisation des manettes
            pygame.joystick.init()
            # Vérifier le nombre de manettes connectées
            self.joystick_count = pygame.joystick.get_count()
            self.joystick = None  # On initialise la manette à None pour le moment
            if self.joystick_count > 0:
                # Sélectionne la première manette disponible
                self.joystick = pygame.joystick.Joystick(0)
                self.joystick.init()  # Initialisez la manette sélectionnée
                self.joystick_dead_zone = 0.8
        elif self.controller_type == "CLAVIER":
            self.keysMap = {
                'left' : pygame.K_q,
                'right' : pygame.K_d,
                'up' : pygame.K_z,
                'down' : pygame.K_s,
                'jump' : pygame.K_SPACE,
                'gravity_down' : pygame.K_DOWN,
                'gravity_right' : pygame.K_RIGHT,
                'gravity_up' : pygame.K_UP,
                'gravity_left' : pygame.K_LEFT,
            }
            


    def get_control_pressed(self):
        if self.controller_type == "CLAVIER":
            return_keys = []
            
            keys = pygame.key.get_pressed()
            
            for key,value in self.keysMap.items():
                if keys[value]:
                    return_keys.append(key)


            return return_keys
        elif self.controller_type == "MANETTE" and self.joystick != None:
            return_buttons = []

            if self.joystick.get_axis(0)>self.joystick_dead_zone:
                return_buttons.append("right")
            if self.joystick.get_axis(0)<-self.joystick_dead_zone:
                return_buttons.append("left")
            if self.joystick.get_axis(1)>self.joystick_dead_zone:
                return_buttons.append("down")
            if self.joystick.get_axis(1)<-self.joystick_dead_zone:
                return_buttons.append("up")
            if self.joystick.get_button(0):
                return_buttons.append("jump")
            if self.joystick.get_axis(3)>self.joystick_dead_zone:
                return_buttons.append("gravity_right")
            if self.joystick.get_axis(3)<-self.joystick_dead_zone:
                return_buttons.append("gravity_left")
            if self.joystick.get_axis(4)>self.joystick_dead_zone:
                return_buttons.append("gravity_down")
            if self.joystick.get_axis(4)<-self.joystick_dead_zone:
                return_buttons.append("gravity_up")


            
            
            return return_buttons
        else:
            return []
    