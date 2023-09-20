import pygame
import csv


class MapManager:
    def __init__(self, tile_size, images, map_csv, obstacles_ids, background_path):
        # Gestion tuiles
        self.tuiles = []  # Tuiles à afficher
        self.obstacles_ids = obstacles_ids
        self.tiles_obstacles = []
        self.background_path = background_path

        if background_path != "":
            self.background_surface = pygame.image.load(self.background_path).convert()
            self.background_surface.set_alpha(120)
        for image in images:
            self.cut_image_into_tiles(image, tile_size)
        # Gestion map
        self.map_data = []  # Données de la carte
        self.load_map_data(map_csv)

    # Découpe dans l'images des tuiles
    def cut_image_into_tiles(self, image, tile_size):
        largeur_tuile = hauteur_tuile = tile_size
        largeur_image = image.get_width()
        hauteur_image = image.get_height()
        nombre_tuiles_largeur = largeur_image // largeur_tuile
        nombre_tuiles_hauteur = hauteur_image // hauteur_tuile

        tuiles_decoupees = []

        for y in range(nombre_tuiles_hauteur):
            for x in range(nombre_tuiles_largeur):
                tuile = image.subsurface(
                    pygame.Rect(
                        x * largeur_tuile,
                        y * hauteur_tuile,
                        largeur_tuile,
                        hauteur_tuile,
                    )
                )
                tuiles_decoupees.append(tuile)

        self.tuiles += tuiles_decoupees

    # Lecture du csv de la map
    def load_map_data(self, file_path):
        self.map_data = []
        with open(file_path, "r") as csv_file:
            csv_reader = csv.reader(csv_file)
            for row in csv_reader:
                self.map_data.append(row)

    # Affichage de la map
    def draw_map(self, screen):
        if self.background_path != "":
            screen.blit(self.background_surface, (0, 0))

        tile_width, tile_height = (
            self.tuiles[0].get_width(),
            self.tuiles[0].get_height(),
        )

        for y, row in enumerate(self.map_data):
            for x, tile_index in enumerate(row):
                if tile_index != "-1":  # Vérifie si la case n'est pas vide (-1)
                    tile_index = int(tile_index)
                    tile_to_draw = self.tuiles[tile_index]
                    screen.blit(tile_to_draw, (x * tile_width, y * tile_height))
