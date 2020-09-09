import pygame
pygame.init()

# Create the player class
class Player(pygame.sprite.Sprite):
  def __init__(self):
    super().__init__()
    self.health = 100
    self.max_health = 100

    self.attack = 10
    self.velocity = 5

    self.image = pygame.image.load('assets/player.png')
    self.rect = self.image.get_rect()


# Generer la fenetre du jeu
pygame.display.set_caption('Commet Fall Game')
screen = pygame.display.set_mode((1080, 720))

# importer l'arriere plan du jeu
background = pygame.image.load('assets/bg.jpg')

# Load the Player
player = Player()

running = True

# Boucle tant que cette condition est vrai
while running:

  # appliquer l'arriere plan
  screen.blit(background, (0, -200))

  # Add player image
  screen.blit(player.image, player.rect)    

  # mise à jour de l'ecran
  pygame.display.flip()

  # si le joueur ferme la fenetre
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
      pygame.quit()
