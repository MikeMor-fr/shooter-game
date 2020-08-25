import pygame
pygame.init()

# Generer la fenetre du jeu
pygame.display.set_caption('Commet Fall Game')
screen = pygame.display.set_mode((1080, 720))

# importer l'arriere plan du jeu
background = pygame.image.load('assets/bg.jpg')

running = True

# Boucle tant que cette condition est vrai
while running:

    # appliquer l'arriere plan
    screen.blit(background, (0,-200))

    # mise à jour de l'ecran
    pygame.display.flip()

    # si le joueur ferme la fenetre
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()