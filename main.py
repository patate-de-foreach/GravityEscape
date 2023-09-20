import pygame, sys, math

import player, ennemi, ennemiFactory, obstacle, level, mapManager, main_menu
from buttons import Button
import game

pygame.init()
screen_width = 1024
screen_height = 768
BackGround = pygame.image.load("assets/graphics/background/Start_Background.png")

surface = pygame.Surface((screen_width, screen_height), pygame.SRCALPHA)

#Variable pour détécter si le jeu est en pause ou pas defaut : False
pause = False

screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()

PlayerRobot = player.Player(screen_width/2,screen_height/2,screen, "CLAVIER")
Ennemi1 = ennemi.Ennemi(0,0,screen)

enemy_factory = ennemiFactory.EnemyFactory(screen, PlayerRobot)


#Ajout du main_menu.py avec le width et le heigh , screen et surface en parametre
MainMenuManager = main_menu.Mainmenu(screen_width,screen_height, screen, surface)
# level1 = level.Level(screen,64)
#level1.updateLevel()

image2 = pygame.image.load("assets/graphics/[64x64] Dungeon Bricks Plain.png")
image1 = pygame.image.load("assets/graphics/[64x64] Dungeon Bricks Shadow.png")

my_map_manager = mapManager.MapManager(tile_size=(64, 64), images=[image1, image2], map_csv='assets/levels/battle room 1/battle room 1.csv')

def get_font(size):
    return pygame.font.Font("assets/font/BrokenRobot.ttf", size)

def Play():
     pygame.display.set_caption("GravityEscape - In-Game")

     while True:    
        screen.blit()
        my_map_manager.draw_map(screen)  # Où 'screen' est la surface Pygame sur laquelle vous voulez dessiner la carte
        PlayerRobot.update()
        PlayerRobot.show()
        enemy_factory.create_enemy()  # Crée un ennemi à chaque frame (vous pouvez ajuster cela)
        enemy_factory.update_enemies()
        enemy_factory.draw_enemies()

def Start_page():
    pygame.display.set_caption("GravityEscape - Menu")

    while True:

        screen.blit(BackGround, (0,0))

        mouse_pos = pygame.mouse.get_pos()

        title = Button(image = pygame.image.load("assets/title.png"), pos=(530,125),
                      input= "", font=get_font(75), color="#ffffff", hover_color = "red", scale=1.5)


        play = Button(image = pygame.image.load("assets/graphics/menubuttons/play2.png"), pos=(512,400),
                      input= "", font=get_font(75), color="#ffffff", hover_color = "red", scale=12)
        
        settings = Button(image = pygame.image.load("assets/graphics/menubuttons/settings.png"), pos=(100,700),
                      input = "", font=get_font(75), color="#ffffff", hover_color = "red", scale=4)
        
        credits = Button(image = pygame.image.load("assets/graphics/menubuttons/credits.png"), pos=(512,700),
                      input = "", font=get_font(75), color="#ffffff", hover_color = "red", scale=4)
        
        exit = Button(image = pygame.image.load("assets/graphics/menubuttons/exit.png"), pos=(924,700),
                      input = "", font=get_font(75), color="#ffffff", hover_color = "red", scale=4)

      

        for button in [play,settings,exit,credits, title]:
            button.__ColorChange__(mouse_pos)
            button.__update__(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if play.__checkinput__(mouse_pos):
                    Play()
                if settings.__checkinput__(mouse_pos):
                    settings()
                if credits.__checkinput__(mouse_pos):
                    credits()
                if title.__checkinput__(mouse_pos):
                    easterEgg()
                if exit.__checkinput__(mouse_pos):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()


def easterEgg():
    pass



Start_page()
# run = True

# while True:

#     # #level1.showLevel()

#     # si le jeu est en pause mettre a jour le menu 
#     if pause == True:
#         MainMenuManager.update_menu()
    

    

#     #PlayerRobot.position.x,PlayerRobot.position.y = pygame.mouse.get_pos()

    


#     # gestion des evènements
#     for event in pygame.event.get():
#         # detection de la touche echap : mettre pause ou enlever pause
#         if event.type == pygame.KEYDOWN:
#             if event.key == pygame.K_ESCAPE:
#                     if pause == False:
#                         pause = True
#                     else:
#                         pause = False
#         if event.type == pygame.QUIT:
#             pygame.quit()
#             sys.exit()

#     pygame.display.update()
#     clock.tick(60)
import game

pygame.init()
screen = pygame.display.set_mode((1024, 768))
gravity_escape = game.Game(screen)


gravity_escape.run()
