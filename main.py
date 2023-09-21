import pygame
# import loading
import start

pygame.init()
screen = pygame.display.set_mode((1024, 768))
# loading page du jeu
# loading_page = loading.Loading(screen)
# loading_page.starting()
startgame = start.Start(screen)
startgame.Start_page()
