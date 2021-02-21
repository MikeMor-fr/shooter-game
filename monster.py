import pygame
import random
import animation


# créer la classe monstre
class Monster(animation.AnimateSprite):
    def __init__(self, game):
        super().__init__('mummy')
        self.health = 100
        self.max_health = 100
        self.attack = 0.3
        self.rect = self.image.get_rect()
        self.rect.x = 1000 + random.randint(0, 300)
        self.rect.y = 540
        self.velocity = 0.05 * random.randint(1, 5)
        self.game = game
        self.start_animation()

    def damage(self, amount):
        # Infliger les degats
        self.health -= amount

        # verifier si les pdv son >= 0
        if self.health <= 0:
            # Reapparaitre comme un nouveau monstre
            self.rect.x = 1000 + random.randint(0, 300)
            self.health = self.max_health
            self.velocity = random.randint(1, 5)

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
