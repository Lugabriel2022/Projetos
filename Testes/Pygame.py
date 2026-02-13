import pygame
import sys

class App():
    def __init__(self, W, H):
        pygame.init()
        self.tela = pygame.display.set_mode(W, H)
    