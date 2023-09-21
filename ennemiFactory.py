import random

from ennemi import *
from drone import *
from enums.level_state_ENUM import *
import utils


class EnemyFactory:
    def __init__(
        self, screen, target, max_enemies, minRespawnTime, maxRespawnTime, clock
    ):
        self.state = level_state_ENUM.RUNNING

        self.minRespawnTime = minRespawnTime * 100
        self.maxRespawnTime = maxRespawnTime * 100

        self.last_spawn_time = 0  # Temps du dernier spawn
        self.spawn_delay = random.randint(self.minRespawnTime, self.maxRespawnTime)

        self.clock = clock
        self.screen = screen
        self.target = target
        self.enemies = []
        self.max_enemies = max_enemies

    def create_enemy(self):
        current_time = pygame.time.get_ticks()
        if current_time - self.last_spawn_time >= self.spawn_delay:
            side = random.choice(["top", "bottom", "left", "right"])
            if side == "top":
                x = random.randint(0, self.screen.get_width())
                y = 0
            elif side == "bottom":
                x = random.randint(0, self.screen.get_width())
                y = self.screen.get_height()
            elif side == "left":
                x = 0
                y = random.randint(0, self.screen.get_height())
            elif side == "right":
                x = self.screen.get_width()
                y = random.randint(0, self.screen.get_height())

            enemy = Drone(x, y, self.screen, self.clock)
            self.enemies.append(enemy)

            # Mettre à jour le temps du dernier spawn et le délai de spawn
            self.last_spawn_time = current_time
            self.minRespawnTime = int(self.minRespawnTime * 0.95)
            self.maxRespawnTime = int(self.maxRespawnTime * 0.95)
            self.spawn_delay = random.randint(self.minRespawnTime, self.maxRespawnTime)
            # print(self.minRespawnTime, self.maxRespawnTime)

    def update_enemies(self):
        if len(self.enemies) <= 0 and self.max_enemies:
            self.state = self.state = level_state_ENUM.FINISHED
        for enemy in self.enemies:
            if enemy.attack_behavior == "KAMIKAZE":
                enemy.seek(self.target)
            else:
                enemy.arrive_and_stop(self.target)
            enemy.update()
            enemy.show()

            # Si l'ennemi sort de l'écran, le supprimer
            if not self.screen.get_rect().collidepoint(enemy.position):
                self.enemies.remove(enemy)

            if enemy.current_health <= 0:
                self.enemies.remove(enemy)

            dist_enemy_target = utils.dist(
                self.target.position.x,
                self.target.position.y,
                enemy.position.x,
                enemy.position.y,
            )

            if (
                dist_enemy_target <= self.target.attack_range
                and self.target.is_attacking
            ):
                enemy.current_health -= self.target.attack_damage

            if utils.approx(dist_enemy_target, enemy.stop_radius, 10):
                enemy.shot(self.target)

            # Vérifiez s'il y a une collision entre l'ennemi et la cible
            if enemy.get_hitbox().colliderect(self.target.player_rect):
                enemy.kamikaze(self.target)

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
