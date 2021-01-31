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

    # recuperer les pojectiles du joueur
    for projectile in game.player.all_projectiles:
        projectile.move()

    # recuperer les monstres
    for monster in game.all_monsters:
        monster.forward()

    # appliquer l'ensemble des images du groupe projectile
    game.player.all_projectiles.draw(screen)

    # appliquer l'ensemble des images du groupe monstre
    game.all_monsters.draw(screen)

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

            # detecter si space est enclenchée
            if event.key == pygame.K_SPACE:
                game.player.launch_projectile()

        elif event.type == pygame.KEYUP:
            game.pressed[event.key] = False
