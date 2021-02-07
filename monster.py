import pygame
import random


# créer la classe monstre
class Monster(pygame.sprite.Sprite):
    def __init__(self, game):
        super().__init__()
        self.health = 100
        self.max_health = 100
        self.attack = 5
        self.image = pygame.image.load("assets/mummy.png")
        self.rect = self.image.get_rect()
        self.rect.x = 1000 + random.randint(0, 300)
        self.rect.y = 540

        self.velocity = random.randint(1, 5)

        self.game = game

    def damage(self, amount):
        # Infliger les degats
        self.health -= amount

        # verifier si les pdv son >= 0
        if self.health <= 0:
            # Reapparaitre comme un nouveau monstre
            self.rect.x = 1000 + random.randint(0, 300)
            self.health = self.max_health
            self.velocity = random.randint(1, 5)

    def update_health_bar(self, surface):
        # definir une couleur pour jauge de vie (vert clair)
        bar_color = (111, 210, 46)

        # definir une couleur pour l'arriere plan de la jauge de vie
        back_bar_color = (60, 63, 60)

        # definir la position de la jauge, largeur et épaisseur
        bar_position = [self.rect.x + 10, self.rect.y - 20, self.health, 5]

        # definir la position de l'arriere plan de jauge de vie
        back_bar_position = [self.rect.x + 10, self.rect.y - 20, self.max_health, 5]

        # dessin de bar de vie
        pygame.draw.rect(surface, back_bar_color, back_bar_position)
        pygame.draw.rect(surface, bar_color, bar_position)


    def forward(self):
        # le deplacement que si pas de collision
        if not self.game.check_collision(self, self.game.all_players):
            self.rect.x -= self.velocity
