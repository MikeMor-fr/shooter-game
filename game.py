import pygame
from player import Player
from monster import Mummy, Alien
from comet_event import CometFallEvent
from sounds import SoundManager


# Créer une seconde classe représentant notre jeu
class Game:
    def __init__(self):
        # Generer le jouer
        self.all_players = pygame.sprite.Group()
        self.player = Player(self)
        self.all_players.add(self.player)

        # Definir si le jeu a commence
        self.is_playing = False

        # groupe de monstre
        self.all_monsters = pygame.sprite.Group()
        self.pressed = {}

        # generer l'evenement comet
        self.comet_event = CometFallEvent(self)
        
        # mettre le score a zero
        self.font = pygame.font.SysFont('monospace', 25, True)
        self.score = 0

        # gerer le son
        self.sound_manager = SoundManager()

    def start(self):
        self.is_playing = True
        self.spawn_monster(Mummy)
        self.spawn_monster(Mummy)
        self.spawn_monster(Alien)

    def game_over(self):
        self.all_monsters = pygame.sprite.Group()
        self.comet_event.all_comets = pygame.sprite.Group()
        self.player.health = self.player.max_health
        self.comet_event.reset_percent()
        self.is_playing = False
        self.score = 0
        self.sound_manager.play('game_over')

    def add_score(self, score=1):
        self.score += score

    def update(self, screen):
        # afficher le score:
        score_text = self.font.render(f'Score: {self.score}', 1, (0, 0, 0))
        screen.blit(score_text, (20, 20))
        
        # Add player image
        screen.blit(self.player.image, self.player.rect)

        # actualiser la barre de vie du joueur
        self.player.update_health_bar(screen)

        # actualiser l'animation du joueur
        self.player.update_animation()

        # actualiser la barre d'evenement du jeu
        self.comet_event.update_bar(screen)

        # recuperer les pojectiles du joueur
        for projectile in self.player.all_projectiles:
            projectile.move()

        # recuperer les monstres
        for monster in self.all_monsters:
            monster.forward()
            monster.update_health_bar(screen)
            monster.update_animation()

        # recuperer les commettes du jeu
        for comet in self.comet_event.all_comets:
            comet.fall()

        # appliquer l'ensemble des images du groupe projectile
        self.player.all_projectiles.draw(screen)

        # appliquer l'ensemble des images du groupe monstre
        self.all_monsters.draw(screen)

        # appliquer l'ensemble des images du groupe comet
        self.comet_event.all_comets.draw(screen)

        # Verifier si le joueur souhaite aller à gauche ou droite
        if self.pressed.get(pygame.K_RIGHT) and self.player.rect.x + self.player.rect.width < screen.get_width():
            self.player.move_right()
        elif self.pressed.get(pygame.K_LEFT) and self.player.rect.x > 0:
            self.player.move_left()

    def check_collision(self, sprite, group):
        return pygame.sprite.spritecollide(sprite, group, False, pygame.sprite.collide_mask)

    def spawn_monster(self, monster_class_name):
        self.all_monsters.add(monster_class_name.__call__(self))
