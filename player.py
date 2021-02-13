import pygame
from projectile import Projectile
import animation


# Create the player class
class Player(animation.AnimateSprite):
    def __init__(self, game):
        super().__init__('player')
        self.health = 100
        self.max_health = 100
        self.attack = 10
        self.velocity = 2
        self.rect = self.image.get_rect()
        self.rect.x = 400
        self.rect.y = 500
        self.all_projectiles = pygame.sprite.Group()
        self.game = game

    def damage(self, amount):
        if self.health - amount > amount:
            self.health -= amount
        else:
            self.game.game_over()

    def launch_projectile(self):
        self.all_projectiles.add(Projectile(self))
        # demarrer l'animation du lancer
        self.start_animation()

    def move_right(self):
        # si le jouer n'est pas en collision
        if not self.game.check_collision(self, self.game.all_monsters):
            self.rect.x += self.velocity

    def move_left(self):
        self.rect.x -= self.velocity

    def update_animation(self):
        self.animate()

    def update_health_bar(self, surface):
        # definir une couleur pour jauge de vie (vert clair)
        bar_color = (111, 210, 46)

        # definir une couleur pour l'arriere plan de la jauge de vie
        back_bar_color = (60, 63, 60)

        # definir la position de la jauge, largeur et épaisseur
        bar_position = [self.rect.x + 50, self.rect.y + 20, self.health, 7]

        # definir la position de l'arriere plan de jauge de vie
        back_bar_position = [bar_position[0], bar_position[1], self.max_health, bar_position[-1]]

        # dessin de bar de vie
        pygame.draw.rect(surface, back_bar_color, back_bar_position)
        pygame.draw.rect(surface, bar_color, bar_position)
