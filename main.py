import pygame
from Player import Player
from Background import Background
from Button import Button
from Item import Item
from func import *
import sys
import random

WIDTH = 720  # Ширина экрана
HEIGHT = 720 # Высота экрана
FPS = 30 # Задача ФПС
# Создаем игру и окно
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("zmeika")
clock = pygame.time.Clock()

background = Background()

pygame.font.init()
font1 = pygame.font.Font('fonts\\Evil Empire.ttf', 30)

tittle_screen_is_on = True # Задаем значения логических переменных для ращличных экранов
settings_screen_is_on = False
running = True

# Задаем значения для кнопок и задника:
play_button = Button((WIDTH - 300) / 2, (HEIGHT) * 0.15, 300, 75, 'Play', (200, 50, 155))
settings_button = Button((WIDTH - 300) / 2, (HEIGHT) * 0.3, 300, 75, 'Settings', (200, 50, 155))
play_button.set_font('fonts\\Evil Empire.ttf')
settings_button.set_font('fonts\\Evil Empire.ttf')
background.set_image('images\\background 1080x720.jpg')

# Цикл  первого экрана
while tittle_screen_is_on:
    clock.tick(FPS)
    background.draw(screen)
    play_button.draw(screen)
    settings_button.draw(screen)

    for event in pygame.event.get():
        # check for closing window
        if event.type == pygame.QUIT: # Выход из игры
            tittle_screen_is_on = False
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                if play_button.is_hovered():  # Нажата кнопка играть
                    tittle_screen_is_on = False
                elif settings_button.is_hovered():  # Нажата кнопка настройки
                    settings_screen_is_on = True
                    back_button = Button(WIDTH * 0.05, HEIGHT * 0.15, 100, 50, 'Back', (200, 50, 155))
                    res_button1 = Button((WIDTH - 300) / 2, HEIGHT * 0.15, 300, 75, 'Resolution: 720x720',
                                         (200, 50, 155))
                    res_button2 = Button((WIDTH - 300) / 2, HEIGHT * 0.3, 300, 75, 'Resolution: 1080x720',
                                         (200, 50, 155))
                    back_button.set_font('fonts\\Evil Empire.ttf')
                    res_button1.set_font('fonts\\Evil Empire.ttf', 30)
                    res_button2.set_font('fonts\\Evil Empire.ttf', 30)

                    while settings_screen_is_on: # экран настроек
                        clock.tick(FPS)
                        background.draw(screen)
                        back_button.draw(screen)
                        res_button1.draw(screen)
                        res_button2.draw(screen)

                        for event1 in pygame.event.get():
                            # check for closing window
                            if event1.type == pygame.QUIT: # выход из игры
                                tittle_screen_is_on = False
                                settings_screen_is_on = False
                                running = False
                            if event1.type == pygame.MOUSEBUTTONDOWN:
                                if event1.button == 1:
                                    if back_button.is_hovered():  # Нажата кнопка назад
                                        settings_screen_is_on = False
                                    elif res_button1.is_hovered(): # Изменить разрешение на №1
                                        WIDTH = 720
                                        HEIGHT = 720
                                        screen = pygame.display.set_mode((WIDTH, HEIGHT))
                                        play_button.set_pos((WIDTH - 300) / 2, HEIGHT * 0.15)
                                        settings_button.set_pos((WIDTH - 300) / 2, HEIGHT * 0.3)
                                        back_button.set_pos(WIDTH * 0.05, HEIGHT * 0.15)
                                        res_button1.set_pos((WIDTH - 300) / 2, HEIGHT * 0.15)
                                        res_button2.set_pos((WIDTH - 300) / 2, HEIGHT * 0.3)
                                    elif res_button2.is_hovered(): # Изменить разрешение на №2
                                        WIDTH = 1080
                                        HEIGHT = 720
                                        screen = pygame.display.set_mode((WIDTH, HEIGHT))
                                        play_button.set_pos((WIDTH - 300) / 2, HEIGHT * 0.15)
                                        settings_button.set_pos((WIDTH - 300) / 2, HEIGHT * 0.3)
                                        back_button.set_pos(WIDTH * 0.05, HEIGHT * 0.15)
                                        res_button1.set_pos((WIDTH - 300) / 2, HEIGHT * 0.15)
                                        res_button2.set_pos((WIDTH - 300) / 2, HEIGHT * 0.3)

                        pygame.display.flip()  # отрисовка
    pygame.display.flip()  # отрисовка

background.set_map()
player = Player(screen)
apple = Item()
apple.place_item(screen)
countApples = 0
# Цикл игры
while running:
    # Держим цикл на правильной скорости
    clock.tick(FPS)
    background.draw(screen)

    apple.draw(screen)
    player.move(screen)

    if isAinsideB(player.get_pos(), apple.get_pos()):  # если игрок коснулся яблока
        apple.place_item(screen)
        countApples += 1
        player.grow()

    player.draw(screen)

    textsurface = font1.render('Apples: ' + str(countApples), False, (225, 0, 225))  # Вывод количества яблок
    screen.blit(textsurface, ((screen.get_width() - textsurface.get_width()) / 2, 0))

    # Ввод процесса (события)
    for event in pygame.event.get():
        # check for closing window
        if event.type == pygame.QUIT: # Выход из игры
            running = False
        if event.type == pygame.KEYDOWN and event.key == 27: # нажата на кнопку ескейп -> пауза
            pause = True
            while pause: # экран паузы
                background.draw(screen)
                apple.draw(screen)
                player.draw(screen)
                textsurface = font1.render('Apples: ' + str(countApples), False,
                                            (225, 0, 225))
                screen.blit(textsurface, ((screen.get_width() - textsurface.get_width()) / 2, 0))
                font2 = pygame.font.Font('fonts\\Evil Empire.ttf', 50)
                surf = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA, 16)
                surf.set_alpha(100)
                # surf = surf.convert_alpha()
                surf.fill((50, 50, 50))
                screen.blit(surf, (0, 0))
                textsurface1 = font2.render('Pause', False,
                                              (225, 155, 225))
                screen.blit(textsurface1,
                            ((screen.get_width() - textsurface1.get_width()) / 2, screen.get_height() * 0.3))
                pygame.display.flip()
                for event1 in pygame.event.get():
                    # check for closing window
                    if event1.type == pygame.QUIT: # Выход из игры
                        running = False
                        pause = False
                    if event1.type == pygame.KEYDOWN and event1.key == 27: #обратно в игру
                        pause = False
    pygame.display.flip()  # отрисовка
pygame.quit()
