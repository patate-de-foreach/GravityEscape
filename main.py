import pygame, sys, math

import player, ennemi, ennemiFactory, obstacle, level, mapManager, main_menu

pygame.init()
screen_width = 1024
screen_height = 768
surface = pygame.Surface((screen_width, screen_height), pygame.SRCALPHA)

#Variable pour détécter si le jeu est en pause ou pas defaut : False
pause = False

screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()

PlayerRobot = player.Player(screen_width/2,screen_height/2,screen)
Ennemi1 = ennemi.Ennemi(0,0,screen)
enemy_factory = ennemiFactory.EnemyFactory(screen, PlayerRobot)


#Ajout du main_menu.py avec le width et le heigh , screen et surface en parametre
MainMenuManager = main_menu.Mainmenu(screen_width,screen_height, screen, surface)
# level1 = level.Level(screen,64)
#level1.updateLevel()

image2 = pygame.image.load("assets/graphics/[64x64] Dungeon Bricks Plain.png")
image1 = pygame.image.load("assets/graphics/[64x64] Dungeon Bricks Shadow.png")

my_map_manager = mapManager.MapManager(tile_size=(64, 64), images=[image1, image2], map_csv='assets/levels/battle room 1/battle room 1.csv')



run = True

while True:

    
    my_map_manager.draw_map(screen)  # Où 'screen' est la surface Pygame sur laquelle vous voulez dessiner la carte
    
    # #level1.showLevel()

    # si le jeu est en pause mettre a jour le menu 
    if pause == True:
        MainMenuManager.update_menu()
    

    PlayerRobot.update()
    PlayerRobot.show()

    #PlayerRobot.position.x,PlayerRobot.position.y = pygame.mouse.get_pos()

    

    enemy_factory.create_enemy()  # Crée un ennemi à chaque frame (vous pouvez ajuster cela)
    

    enemy_factory.update_enemies()
    enemy_factory.draw_enemies()

    # gestion des evènements
    for event in pygame.event.get():
        # detection de la touche echap : mettre pause ou enlever pause
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                    if pause == False:
                        pause = True
                    else:
                        pause = False
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()
    clock.tick(60)