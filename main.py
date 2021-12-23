import pygame
from Player import Player
from Background import Background
import random

WIDTH = 720
HEIGHT = 720
FPS = 30
# Задаем цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
# pacman = pygame.image.load("images/pacman.png")
# Создаем игру и окно
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("My Game")
clock = pygame.time.Clock()
background = Background()
background.setmap()
player = Player(screen)
# Цикл игры
running = True
while running:

    # Держим цикл на правильной скорости
    clock.tick(FPS)
    background.draw(screen)

    player.move(screen)
    player.draw(screen)

    # Ввод процесса (события)
    for event in pygame.event.get():
        # check for closing window
        if event.type == pygame.QUIT:
            running = False
    pygame.display.flip()   # отрисовка
pygame.quit()
