import pygame
from game import Game
pygame.init()

# Generer la fenetre du jeu
pygame.display.set_caption('Commet Fall Game')
screen = pygame.display.set_mode((1080, 720))

# importer l'arriere plan du jeu
background = pygame.image.load('assets/bg.jpg')

# Charger le jeu
game = Game()

running = True

# Boucle tant que cette condition est vrai
while running:

    # appliquer l'arriere plan
    screen.blit(background, (0, -200))

    # Add player image
    screen.blit(game.player.image, game.player.rect)

    # Verifier si le joueur souhaite aller à gauche ou droite
    if game.pressed.get(pygame.K_RIGHT) and game.player.rect.x + game.player.rect.width < screen.get_width():
        game.player.move_right()
    elif game.pressed.get(pygame.K_LEFT) and game.player.rect.x > 0:
        game.player.move_left()


    # mise à jour de l'ecran
    pygame.display.flip()

    # si le joueur ferme la fenetre
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()

        # detecter lache une touche du clavier
        elif event.type == pygame.KEYDOWN:
            game.pressed[event.key] = True
        elif event.type == pygame.KEYUP:
            game.pressed[event.key] = False
