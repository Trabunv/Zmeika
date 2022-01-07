import pygame
import numpy as np


class Item(object):
    """Класс, определяющий положение, размер, цвет, текст и поведение  объектов игры"""
    def __init__(self):
        self.image = pygame.image.load("images\\apple.png")
        self.rect = 0
        self.x = 0
        self.y = 0
        self.length = 0
        self.size = [0, 0]

    def place_item(self, length, size, screen):
        self.length = length
        self.size = size
        self.x = np.random.randint(-(length - 2)*(size[0])/2,
                                   (length - 5)*(size[0])/2,
                                   size=1)[0] + screen.get_width() / 2
        self.y = np.random.randint(-(length - 2)*(size[1])/2,
                                   (length - 5)*(size[1])/2,
                                   size=1)[0] + screen.get_height() / 2

    def get_pos(self):
        self.image = pygame.transform.scale(self.image, (50, 50))
        return self.x, self.y, self.image.get_width(), self.image.get_height()

    def draw(self, screen):
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = screen.blit(self.image,
                                (self.x, self.y)
                                )
