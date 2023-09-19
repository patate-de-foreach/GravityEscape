import pygame

import player

class Player_Controls:
    
    def __init__(self, controllerType):
        if controllerType == "MANETTE":
            # Initialisation des manettes
            pygame.joystick.init()
            # Vérifier le nombre de manettes connectées
            num_manette = pygame.joystick.get_count()
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
            pass


    def get_control_pressed(self):
        return_keys = []
        
        keys = pygame.key.get_pressed()
        
        for key,value in self.keysMap.items():
            if keys[value]:
                return_keys.append(key)


        return return_keys


    def remap_keys(self):
        pass