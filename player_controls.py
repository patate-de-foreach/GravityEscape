import pygame

import player

class Player_Controls:
    
    def __init__(self, controllerType):
        if controllerType == "MANETTE":
            # Initialisation des manettes
            pygame.joystick.init()
            # Vérifier le nombre de manettes connectées
            self.joystick_count = pygame.joystick.get_count()
            self.joystick = None  # On initialise la manette à None pour le moment
            if self.joystick_count > 0:
                # Sélectionnez la première manette disponible
                self.joystick = pygame.joystick.Joystick(0)
                self.joystick.init()  # Initialisez la manette sélectionnée
        elif controllerType == "CLAVIER":
            self.keysMap = {
                'left' : pygame.K_q,
                'right' : pygame.K_d,
                'up' : pygame.K_z,
                'down' : pygame.K_s,
                'jump' : pygame.K_SPACE,
                'gravity_down' : pygame.K_1,
                'gravity_right' : pygame.K_2,
                'gravity_up' : pygame.K_3,
                'gravity_left' : pygame.K_4,
            }
            


    def get_control_pressed(self):
        return_keys = []
        
        keys = pygame.key.get_pressed()
        
        for key,value in self.keysMap.items():
            if keys[value]:
                return_keys.append(key)


        return return_keys


    