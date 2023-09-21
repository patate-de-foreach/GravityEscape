from utils import import_folder

class Explosion:
    def __init__(self, screen, position):
        self.screen = screen
        self.load_explosion()
        self.frame_index = 0.0
        self.animation_speed = 0.15
        self.position = position
        self.explosion_finished = False

    # charge l'explosion
    def load_explosion(self):
        explosion_fx_path = "assets/graphics/effects"
        self.explosion_anim = import_folder(explosion_fx_path)

    def animate(self):
        self.frame_index += self.animation_speed
        frame = int(self.frame_index)
        if frame>len(self.explosion_anim)-1:
            self.explosion_finished = True
        else:
            self.screen.blit(self.explosion_anim[frame], (self.position.x - 100, self.position.y - 100))
