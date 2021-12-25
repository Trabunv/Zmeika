import pygame
import numpy as np


class Item:
    def __init__(self):
        self.image = pygame.image.load("images\\apple.png")
        self.rect = 0
        self.x = 0
        self.y = 0

    def place_item(self, screen):
        self.x = np.random.randint(0, screen.get_width()-self.image.get_width(), size=1)[0]
        self.y = np.random.randint(0, screen.get_height()-self.image.get_height(), size=1)[0]

    def get_pos(self):
        self.image = pygame.transform.scale(self.image, (50, 50))
        return self.x, self.y, self.image.get_width(), self.image.get_height()

    def draw(self, screen):
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = screen.blit(self.image, (self.x, self.y))