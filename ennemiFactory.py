import random

from ennemi import *

class EnemyFactory:
    def __init__(self, screen, target):
        self.screen = screen
        self.target = target
        self.enemies = []
        self.max_enemies = 10

    def create_enemy(self):
        if len(self.enemies)<self.max_enemies:
            side = random.choice(['top', 'bottom', 'left', 'right'])
            if side == 'top':
                x = random.randint(0, self.screen.get_width())
                y = 0
            elif side == 'bottom':
                x = random.randint(0, self.screen.get_width())
                y = self.screen.get_height()
            elif side == 'left':
                x = 0
                y = random.randint(0, self.screen.get_height())
            elif side == 'right':
                x = self.screen.get_width()
                y = random.randint(0, self.screen.get_height())
            enemy = Ennemi(x, y, self.screen)
            self.enemies.append(enemy)

    def update_enemies(self):
        for enemy in self.enemies:
            enemy.arrive_and_stop(self.target)
            enemy.update()
            enemy.show()
            
            # Si l'ennemi sort de l'écran, le supprimer
            if not self.screen.get_rect().collidepoint(enemy.position):
                self.enemies.remove(enemy)

            # Vérifiez s'il y a une collision entre l'ennemi et la cible
            if enemy.get_hitbox().colliderect(self.target.get_hitbox()):
                print("Collision avec la cible !")

        # Détectez les collisions entre les ennemis
        self.detect_enemy_collisions()
    
    def draw_enemies(self):
        for enemy in self.enemies:
            enemy.show()

    def get_enemy_count(self):
        return len(self.enemies)
    
    def detect_enemy_collisions(self):
        for i, enemy1 in enumerate(self.enemies):
            for j, enemy2 in enumerate(self.enemies):
                if i != j:  # Évitez de vérifier une collision avec le même ennemi
                    if enemy1.get_hitbox().colliderect(enemy2.get_hitbox()):
                        enemy1.avoid_collision(enemy2)
                        enemy2.avoid_collision(enemy1)