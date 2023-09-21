import pygame
import game

pygame.init()
screen = pygame.display.set_mode((1024, 768))


gravity_escape = game.Game(screen)
gravity_escape.run()
