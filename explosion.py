from utils import import_folder


class Explosion:
    def __init__(self):
        self.load_explosion_fx()

    def load_explosion_fx(self):
        explosion_fx_path = "assets/graphics/effects"
        self.explosion_anim = []
        self.explosion_anim = import_folder(explosion_fx_path)
