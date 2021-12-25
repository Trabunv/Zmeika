import pygame
from Player import Player
from Background import Background
from Item import Item
from func import *
import random

WIDTH = 720
HEIGHT = 720
FPS = 30
# Создаем игру и окно
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("My Game")
clock = pygame.time.Clock()

background = Background()
background.setmap()
player = Player(screen)

pygame.font.init()
myfont = pygame.font.SysFont('Times New Roman', 30)

apple = Item()
apple.place_item(screen)
countApples = 0
# Цикл игры
running = True
while running:
    # Держим цикл на правильной скорости
    clock.tick(FPS)
    background.draw(screen)

    apple.draw(screen)
    player.move(screen)

    if isAinsideB(player.get_pos(), apple.get_pos()): #если игрок коснулся яблока
        apple.place_item(screen)
        countApples += 1
        player.grow()

    player.draw(screen)

    textsurface = myfont.render('Apples: ' + str(countApples), False, (150, 85, 155)) # Вывод количества яблок
    screen.blit(textsurface, (screen.get_width()/2 - 50, 0))

    # Ввод процесса (события)
    for event in pygame.event.get():
        # check for closing window
        if event.type == pygame.QUIT:
            running = False
    pygame.display.flip()   # отрисовка
pygame.quit()
