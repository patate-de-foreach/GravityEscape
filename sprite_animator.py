import pygame

class SpriteAnimator:
    def __init__(self, sprite_sheet, num_frames, frame_width, frame_height, frame_duration):
        
        self.sprite_sheet = sprite_sheet
        self.num_frames = num_frames
        self.frame_width = frame_width
        self.frame_height = frame_height
        self.frame_duration = frame_duration

        self.frames = []  # Une liste pour stocker les images individuelles
        self.current_frame = 0
        self.frame_timer = 0

        self.load_frames()

    def load_frames(self):
        # Divise la feuille de sprites en images individuelles
        for i in range(self.num_frames):
            frame = self.sprite_sheet.subsurface((i * self.frame_width, 0, self.frame_width, self.frame_height))
            self.frames.append(frame)

    def update(self, dt):
        # Met à jour le frame actuel de l'animation
        self.frame_timer += dt.get_time()
        if self.frame_timer >= self.frame_duration:
            self.frame_timer = 0
            self.current_frame = (self.current_frame + 1) % self.num_frames

    def get_current_frame(self):
        # Renvoie le frame actuel
        return self.frames[self.current_frame]

    def reset(self):
        # Réinitialise l'animation au premier frame
        self.current_frame = 0
        self.frame_timer = 0

