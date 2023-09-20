from pygame import mixer


class Audio:
    def __init__(self, soung_path):
        self.mixer = mixer.init()
        self.load = mixer.music.load(soung_path)
        self.volume = mixer.music.set_volume(1)
        self.play = mixer.music.play(loops=-1)


