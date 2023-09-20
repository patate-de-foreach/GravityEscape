import pygame
import start

pygame.init()
screen = pygame.display.set_mode((1024, 768))

#Starting page start du jeu
start_game = start.Start(screen)
start_game.strating()
