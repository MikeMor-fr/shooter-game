import pygame
from player import Player


# Créer une seconde classe représentant notre jeu
class Game:
    def __init__(self):
        # Generer le jouer
        self.player = Player()
        self.pressed = {}
