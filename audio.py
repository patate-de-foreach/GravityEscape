from pygame import mixer


class Audio:
    def __init__(self, sound_path):
        self.mixer = mixer.init()
        self.load = mixer.music.load(sound_path)
        self.volume = mixer.music.set_volume(1)
        self.play = mixer.music.play(loops=-1)


