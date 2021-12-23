import pygame
from Player import Player
import random

WIDTH = 800
HEIGHT = 600
FPS = 30
# Задаем цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
background_image = pygame.image.load('images/background 800x600.jpg')
# pacman = pygame.image.load("images/pacman.png")
# Создаем игру и окно
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("My Game")
clock = pygame.time.Clock()
player = Player()
# Цикл игры
running = True
while running:

    # Держим цикл на правильной скорости
    clock.tick(FPS)
    screen.blit(background_image, (0, 0))

    player.move(screen)
    player.draw(screen)

    # Ввод процесса (события)
    for event in pygame.event.get():
        # check for closing window
        if event.type == pygame.QUIT:
            running = False
    pygame.display.flip()   # отрисовка
pygame.quit()
