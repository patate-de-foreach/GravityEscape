import pygame, sys
import player, ennemi, ennemiFactory

pygame.init()
screen_width = 1024
screen_height = 768
screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()

PlayerRobot = player.Player(screen_width/2,screen_height/2,screen)
Ennemi1 = ennemi.Ennemi(0,0,screen)

enemy_factory = ennemiFactory.EnemyFactory(screen, PlayerRobot)

while True:
    screen.fill('black')


    

    PlayerRobot.update()
    PlayerRobot.show()

    

    PlayerRobot.position.x,PlayerRobot.position.y = pygame.mouse.get_pos()

    

    enemy_factory.create_enemy()  # Crée un ennemi à chaque frame (vous pouvez ajuster cela)
    

    enemy_factory.update_enemies()
    enemy_factory.draw_enemies()

    # gestion des evènements
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    
    pygame.display.update()
    clock.tick(60)