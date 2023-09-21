from explosion import *

class ExplosionManager:
    def __init__(self):
        self.explosions = []

    def add_explosion(self, screen, position):
        explosion = Explosion(screen, position)
        self.explosions.append(explosion)

    def animate_explosions(self):
        for explosion in self.explosions:
            if not explosion.explosion_finished:
                explosion.animate()
            else:
                self.explosions.remove(explosion)