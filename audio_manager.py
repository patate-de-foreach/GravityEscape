from pygame import mixer


class AudioManager:
    def __init__(self):
        self.bgm_level = 0.4
        self.sfx_level = 0.8
        self.init_player_sfx()
        self.init_mixer()

    def init_player_sfx(self):
        self.gravity = mixer.Sound("assets/audio/sfx/gravity.mp3")
        self.player_sounds = {"gravity": self.gravity}
        for player_sound in self.player_sounds.values():
            player_sound.set_volume(self.sfx_level)

    def init_mixer(self):
        mixer.init()
        mixer.music.set_volume(self.bgm_level)
        self.bgm_paths = {"roaming": "assets/audio/bgm/roaming.mp3"}

    ## Change la musique jouée
    # si loop = -1, la musique tourne en boucle
    # si une intro est donnée, joue l'intro et enchaine avec la musique
    def play_bgm(self, bgmName, loop=0, introName=""):
        if introName != "":
            mixer.music.load(self.bgm_paths[introName])
            mixer.music.queue(self.bgm_paths[bgmName], loops=loop)
        else:
            mixer.music.load(self.bgm_paths[bgmName])
            mixer.music.play(loops=loop)

    ## Arrête la musique en cours avec une option fadeout paramétrable
    def stop_bgm(self, fadeout=False, fadeout_time=1):
        if fadeout:
            mixer.music.fadeout(fadeout_time)
        else:
            mixer.music.stop()
