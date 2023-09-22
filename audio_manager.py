from pygame import mixer


class AudioManager:
    def __init__(self):
        self.bgm_level = 0.4
        self.sfx_level = 0.8
        self.init_player_sfx()
        self.init_mixer()

    def init_player_sfx(self):
        self.gravity = mixer.Sound("assets/audio/sfx/gravity.mp3")
        self.attack = mixer.Sound("assets/audio/sfx/attack_sound.mp3")
        self.hurt = mixer.Sound("assets/audio/sfx/hurt_sound.mp3")
        self.player_sounds = {
            "gravity": self.gravity,
            "attack": self.attack,
            "hurt": self.hurt,
        }
        for player_sound in self.player_sounds.values():
            player_sound.set_volume(self.sfx_level)

    def init_mixer(self):
        mixer.init()
        mixer.music.set_volume(self.bgm_level)
        self.bgm_paths = {
            "credits": "assets/audio/bgm/credits.mp3",
            "main_menu": "assets/audio/bgm/main_menu.mp3",
            "main_menu_intro": "assets/audio/bgm/main_menu_intro.mp3",
            "game_over": "assets/audio/bgm/game_over.mp3",
            "game_over_intro": "assets/audio/bgm/game_over_intro.mp3",
            "battle_intro": "assets/audio/bgm/battle_intro.mp3",
            "battle": "assets/audio/bgm/battle.mp3",
        }

    ## Change la musique jouée
    # si loop = -1, la musique tourne en boucle
    # si une intro est donnée, joue l'intro et enchaine avec la musique
    def play_bgm(self, bgmName, loop=0, introName=""):
        if introName != "":
            mixer.music.load(self.bgm_paths[introName])
            mixer.music.queue(self.bgm_paths[bgmName], loops=loop)
            mixer.music.play()
        else:
            mixer.music.load(self.bgm_paths[bgmName])
            mixer.music.play(loops=loop)

    ## Arrête la musique en cours avec une option fadeout paramétrable
    def stop_bgm(self, fadeout=False, fadeout_time=1):
        if fadeout:
            mixer.music.fadeout(fadeout_time)
        else:
            mixer.music.stop()
