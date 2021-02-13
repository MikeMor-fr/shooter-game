import pygame
import random
import animation


# créer la classe monstre
class Monster(animation.AnimateSprite):
    def __init__(self, game, name, size, offset=0):
        super().__init__(name, size)
        self.health = 100
        self.max_health = 100
        self.attack = 0.3
        self.rect = self.image.get_rect()
        self.rect.x = 1000 + random.randint(0, 300)
        self.rect.y = 540 - offset
        self.game = game
        self.start_animation()
        self.loot_amount = 1

    def set_speed(self, speed):
        self.default_speed = speed
        self.velocity = random.randint(1, 3)

    def set_loot_amount(self, amount):
        self.loot_amount = amount

    def damage(self, amount):
        # Infliger les degats
        self.health -= amount

        # verifier si les pdv son >= 0
        if self.health <= 0:
            # Reapparaitre comme un nouveau monstre
            self.rect.x = 1000 + random.randint(0, 300)
            self.health = self.max_health
            self.velocity = random.randint(1, self.default_speed)

            # ajouter le nombre de points
            self.game.add_score(self.loot_amount)

            # si la barre d'evenement est chargée au max
            if self.game.comet_event.is_full_loaded():
                # retirer du jeu
                self.game.all_monsters.remove(self)

                # appem de la methode pour essayer de declancher la pluie de comete
                self.game.comet_event.attempt_fall()

    def update_animation(self):
        self.animate(loop=True)

    def update_health_bar(self, surface):
        # definir une couleur pour jauge de vie (vert clair)
        bar_color = (111, 210, 46)

        # definir une couleur pour l'arriere plan de la jauge de vie
        back_bar_color = (60, 63, 60)

        # definir la position de la jauge, largeur et épaisseur
        bar_position = [self.rect.x + 10, self.rect.y - 20, self.health, 5]

        # definir la position de l'arriere plan de jauge de vie
        back_bar_position = [bar_position[0], bar_position[1], self.max_health, bar_position[-1]]

        # dessin de bar de vie
        pygame.draw.rect(surface, back_bar_color, back_bar_position)
        pygame.draw.rect(surface, bar_color, bar_position)

    def forward(self):
        # le deplacement que si pas de collision
        if not self.game.check_collision(self, self.game.all_players):
            self.rect.x -= self.velocity
        # si le monstre est en collision
        else:
            # infliger des degats
            self.game.player.damage(self.attack)


# definir une classe pour la momie
class Mummy(Monster):
    def __init__(self, game):
        super().__init__(game, 'mummy', (130, 130))
        self.set_speed(3)
        self.set_loot_amount(1)


# definir une classe pour l'alien
class Alien(Monster):
    def __init__(self, game):
        super().__init__(game, 'alien', (300, 300), 130)
        self.health = 250
        self.max_health = 250
        self.attack = 0.8
        self.set_speed(1)
        self.set_loot_amount(10)
