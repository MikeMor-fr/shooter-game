import pygame


# créer la classe monstre
class Monster(pygame.sprite.Sprite):
    def __init__(self, game):
        super().__init__()
        self.health = 100
        self.max_health = 100
        self.attack = 5
        self.image = pygame.image.load("assets/mummy.png")
        self.rect = self.image.get_rect()
        self.rect.x = 1000
        self.rect.y = 540

        self.velocity = 0.1

        self.game = game

    def forward(self):
        # le deplacement que si pas de collision
        if not self.game.check_collision(self, self.game.all_players):
            self.rect.x -= self.velocity