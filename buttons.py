import pygame

class Button():
    def __init__(self, image, pos, input, font, color, hover_color, scale):
        self.image = pygame.transform.scale(image,(int(image.get_width() * scale), int(image.get_height() * scale)))        
        self.x = pos[0]
        self.y = pos[1]
        self.font = font
        self.color, self.hover_color = color, hover_color
        self.input = input

        self.txt = self.font.render(self.input, True, self.color)

        if self.image is None:
            self.image = self.txt
        self.rect = self.image.get_rect(center=(self.x, self.y))
        self.txt_rect = self.txt.get_rect(center=(self.x, self.y))

    def __update__(self, screen):
        if self.image is not None:
            screen.blit(self.image, self.rect)
        screen.blit(self.txt, self.txt_rect)

    def __checkinput__(self, pos):
        if pos[0] in range(self.rect.left, self.rect.right) and pos[1] in range(self.rect.top, self.rect.bottom):
            return True
        return False
    
    def __ColorChange__(self, position):
        if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
            self.txt = self.font.render(self.input, True , self.hover_color)
        else:
            self.txt = self.font.render(self.input, True, self.color)



        