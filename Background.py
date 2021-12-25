import pygame
import numpy as np

class Background:
    def __init__(self):
        self.image = pygame.image.load("images\link.png")
        self.image = pygame.transform.scale(self.image,
                                            (self.image.get_width(), self.image.get_height()))
        self.length = 25
        self.width = 30
        self.height = 30
        self.map = np.ones((self.length, self.length))

    def get_width(self):
        return self.width

    def get_height(self):
        return self.height

    def get_length(self):
        return self.length

    def setmap(self):
        for y in range(len(self.map)):
            for x in range(len(self.map[0])):
                if (x == max(range(len(self.map[0])))-1
                        or x == min(range(len(self.map[0])))
                        or y == max(range(len(self.map)))-1
                        or y == min(range(len(self.map)))
                ):
                    self.map[y][x] = 0.4
                elif (x*y) % 5 == 3:
                    self.map[y][x] = 0.8
                elif (x*y*2) % 7 == 3:
                    self.map[y][x] = 1.1

    def draw(self, screen):
        for y in range(len(self.map)):
            for x in range(len(self.map[0])):
                surf = pygame.Surface((200, 150))
                surf.fill((7*y*self.map[y][x], 4*x*self.map[y][x], 155*self.map[y][x]))
                self.rect = screen.blit(surf,
                                        (x * self.width, y * self.height),
                                        (0, 0, self.width, self.height))
