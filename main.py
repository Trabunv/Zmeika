""" To utilize this version user need to make some changes in the goto lib files:
This can be fixed by changing line 54 to return code.replace(co_code=codestring)
This is the return value of the _make_code function.
After that, go to line 175 and change it to read return _make_code(code, buf.tobytes())
This will fix this module to work with
"""
import pygame
from Player import Player
from Background import Background
from Button import Button
from Item import Item
from func import *
import sys
import random
from goto import with_goto


@with_goto
def main():
    WIDTH = 720  # Ширина экрана
    HEIGHT = 720  # Высота экрана
    FPS = 25  # Задача ФПС
    VOLUME = 50

    # Создаем игру и окно
    pygame.init()
    pygame.mixer.init()
    pygame.display.set_caption("zmeika")
    clock = pygame.time.Clock()

    # Создаем музыку и звуки
    pygame.mixer.music.load('music\\music.mp3')
    pygame.mixer.music.play(-1)
    pygame.mixer.music.set_volume(VOLUME / 100)

    # Начальный экран
    label .title_screen

    # задаем параметры начального экрана
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    background = Background()
    pygame.font.init()
    font1 = pygame.font.Font('fonts\\Evil Empire.ttf', 30)

    # Задаем значения для кнопок и задника:
    play_button = Button((WIDTH - 300) / 2, HEIGHT * 0.15, 300, 75, 'Play', (200, 50, 155))
    settings_button = Button((WIDTH - 300) / 2, HEIGHT * 0.3, 300, 75, 'Settings', (200, 50, 155))
    play_button.set_font('fonts\\Evil Empire.ttf')
    settings_button.set_font('fonts\\Evil Empire.ttf')
    background.set_image('images\\background 1080x720.jpg')

    # Цикл  первого экрана
    tittle_screen_is_on = True
    while tittle_screen_is_on:
        clock.tick(FPS)
        background.draw(screen)
        play_button.draw(screen)
        settings_button.draw(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # Выход из игры
                goto.end
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if play_button.is_hovered():  # Нажата кнопка играть
                        goto .game
                    elif settings_button.is_hovered():  # Нажата кнопка настройки
                        goto .settings

        pygame.display.flip()  # отрисовка

    # Экран настроек
    label .settings

    # Задаем кнопки и их текстовые значения:
    back_button = Button(WIDTH * 0.05,
                         HEIGHT * 0.15,
                         100,
                         50,
                         'Back',
                         (200, 50, 155))

    res_button1 = Button((WIDTH - 300) / 2,
                         HEIGHT * 0.15,
                         300,
                         75,
                         'Resolution: 720x720',
                         (200, 50, 155))

    res_button2 = Button((WIDTH - 300) / 2,
                         HEIGHT * 0.3,
                         300,
                         75,
                         'Resolution: 1080x720',
                         (200, 50, 155))

    vol_button = Button((WIDTH - 300) / 2,
                        HEIGHT * 0.45,
                        300,
                        75,
                        'Volume: {}'.format(str(VOLUME)),
                        (200, 50, 155))

    back_button.set_font('fonts\\Evil Empire.ttf')
    res_button1.set_font('fonts\\Evil Empire.ttf', 30)
    res_button2.set_font('fonts\\Evil Empire.ttf', 30)
    vol_button.set_font('fonts\\Evil Empire.ttf', 30)

    settings_screen_is_on = True
    while settings_screen_is_on:  # экран настроек
        clock.tick(FPS)
        background.draw(screen)
        back_button.draw(screen)
        res_button1.draw(screen)
        res_button2.draw(screen)
        vol_button.draw(screen)

        for event1 in pygame.event.get():
            if event1.type == pygame.QUIT:  # выход из игры
                goto .end

            if event1.type == pygame.MOUSEBUTTONDOWN:
                if event1.button == 1:
                    if back_button.is_hovered():  # Нажата кнопка назад
                        goto .title_screen

                    elif res_button1.is_hovered():  # Изменить разрешение на №1
                        WIDTH = 720
                        HEIGHT = 720
                        screen = pygame.display.set_mode((WIDTH, HEIGHT))
                        play_button.set_pos((WIDTH - 300) / 2, HEIGHT * 0.15)
                        settings_button.set_pos((WIDTH - 300) / 2, HEIGHT * 0.3)
                        back_button.set_pos(WIDTH * 0.05, HEIGHT * 0.15)
                        res_button1.set_pos((WIDTH - 300) / 2, HEIGHT * 0.15)
                        res_button2.set_pos((WIDTH - 300) / 2, HEIGHT * 0.3)
                        vol_button.set_pos((WIDTH - 300) / 2, HEIGHT * 0.45)
                        vol_button.set_selected(False)

                    elif res_button2.is_hovered():  # Изменить разрешение на №2
                        WIDTH = 1080
                        HEIGHT = 720
                        screen = pygame.display.set_mode((WIDTH, HEIGHT))
                        play_button.set_pos((WIDTH - 300) / 2, HEIGHT * 0.15)
                        settings_button.set_pos((WIDTH - 300) / 2, HEIGHT * 0.3)
                        back_button.set_pos(WIDTH * 0.05, HEIGHT * 0.15)
                        res_button1.set_pos((WIDTH - 300) / 2, HEIGHT * 0.15)
                        res_button2.set_pos((WIDTH - 300) / 2, HEIGHT * 0.3)
                        vol_button.set_pos((WIDTH - 300) / 2, HEIGHT * 0.45)
                        vol_button.set_selected(False)

                    elif vol_button.is_hovered():
                        vol_button.set_selected(True)

            if event1.type == pygame.KEYDOWN:
                if event1.key == 1073741904 and vol_button.get_selected(): # Уменьшение громкости
                    if VOLUME > 0:
                        VOLUME -= 10

                    pygame.mixer.music.set_volume(VOLUME / 100)

                if event1.key == 1073741903 and vol_button.get_selected(): # Увеличение громкости
                    VOLUME += 10
                    pygame.mixer.music.set_volume(VOLUME / 100)

                vol_button.set_text('Volume: {}'.format(str(VOLUME)))

        pygame.display.flip()  # отрисовка

    # Игра
    label .game

    running = True
    background.set_map()
    player = Player(screen)
    player.set_screen_height(background.get_map_height())
    player.set_screen_width(background.get_map_width())
    apple = Item()
    apple.place_item(background.get_len(), background.get_size(), screen)
    apple_counter = 0

    action = pygame.mixer.Sound('sound\\action3.flac')
    action.set_volume(0.3)

    # Цикл игры
    while running:
        # Держим цикл на правильной скорости
        clock.tick(FPS)
        background.draw(screen)
        background.draw_map(screen)

        apple.draw(screen)
        if player.move(screen) and player.snake_collision():
            goto .game_over

        if isAinsideB(player.get_pos(), apple.get_pos()):  # если игрок коснулся яблока
            action.play()
            apple.place_item(background.get_len(), background.get_size(), screen)
            apple_counter += 1
            player.grow()

        player.draw_polygon(screen)

        text_surface = font1.render('Score: {}'.format(str(apple_counter)), False, (225, 0, 225)) # Вывод количества яблок
        screen.blit(text_surface, ((screen.get_width() - text_surface.get_width()) / 2, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT: # Выход из игры
                goto .end

            if event.type == pygame.KEYDOWN and event.key == 27: # нажата на кнопку ескейп -> пауза
                goto .pause

        # Продолжение игры
        label .play

        if running:
            pygame.display.flip()  # отрисовка

    # Экран паузы
    label .pause

    pause = True
    while pause:
        clock.tick(FPS)
        background.draw(screen)
        background.draw_map(screen)
        apple.draw(screen)
        player.draw_polygon(screen)

        text_surface = font1.render('Score: {}'.format(str(apple_counter)), False,
                                    (225, 0, 225))
        screen.blit(text_surface,
                    ((screen.get_width() - text_surface.get_width()) / 2, 0))

        font2 = pygame.font.Font('fonts\\Evil Empire.ttf', 50)
        surf = pygame.Surface((WIDTH, HEIGHT),
                              pygame.SRCALPHA,
                              16)
        surf.set_alpha(100)
        surf.fill((50, 50, 50))
        screen.blit(surf, (0, 0))
        text_surface1 = font2.render('Pause',
                                     False,
                                     (225, 155, 225))

        screen.blit(text_surface1,
                    ((screen.get_width() - text_surface1.get_width()) / 2,
                     screen.get_height() * 0.3))

        for event1 in pygame.event.get():
            if event1.type == pygame.QUIT:  # Выход из игры
                goto .end
            if event1.type == pygame.KEYDOWN and event1.key == 27:  # обратно в игру
                goto .play

        pygame.display.flip()

    # Экран проиграша
    label .game_over

    retry_button = Button((WIDTH - 300) / 2,
                          HEIGHT * 0.43,
                          300,
                          75,
                          'Retry',
                          (200, 50, 155))

    main_button = Button((WIDTH - 300) / 2,
                         HEIGHT * 0.57,
                         300,
                         75,
                         'Main menu',
                         (200, 50, 155))

    retry_button.set_font('fonts\\Evil Empire.ttf')
    main_button.set_font('fonts\\Evil Empire.ttf')

    game_over = True
    while game_over:
        clock.tick(FPS)
        background.draw(screen)
        surf = pygame.Surface((WIDTH, HEIGHT),
                              pygame.SRCALPHA,
                              16)
        surf.set_alpha(100)

        surf.fill((80, 80, 80))
        screen.blit(surf, (0, 0))
        retry_button.draw(screen)
        main_button.draw(screen)

        font2 = pygame.font.Font('fonts\\Evil Empire.ttf', 60)

        text_surface1 = font2.render('Game over',
                                     False,
                                     (225, 155, 225))

        screen.blit(text_surface1,
                    ((screen.get_width() - text_surface1.get_width()) / 2, screen.get_height() * 0.1))

        text_surface = font2.render('Score: {}'.format(str(apple_counter)),
                                    False,
                                    (225, 155, 225))

        screen.blit(text_surface,
                    ((screen.get_width() - text_surface.get_width()) / 2, screen.get_height() * 0.2))

        pygame.display.flip()
        for event1 in pygame.event.get():
            if event1.type == pygame.QUIT: # Выход из игры
                goto .end
            if event1.type == pygame.MOUSEBUTTONDOWN:
                if event1.button == 1:
                    if retry_button.is_hovered(): # Нажата кнопка играть
                        goto .game
                    elif main_button.is_hovered(): # Нажата кнопка настройки
                        goto .title_screen

        pygame.display.flip()
    # Выход из игры
    label .end
    pygame.quit()
    sys.exit()


main()
