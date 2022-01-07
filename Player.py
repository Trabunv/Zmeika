import pygame
from func import *


class Player(object):
    """Класс игрока, определяет положение, движение, отрисовку и другие параметры связанные с игроком"""
    def __init__(self, screen):
        self.image = pygame.image.load("images\\ball.png")
        alpha = 0.0234375
        self.image = pygame.transform.scale(self.image,
                                            (self.image.get_width()*alpha, self.image.get_height()*alpha))

        self.rect = 0
        self.speed = 30
        self.length = 1
        self.cropIndex = 0
        self.cropy = 0
        self.imWidth = 1280*alpha
        self.imHeight = 1280*alpha
        self.x = screen.get_width()/2
        self.y = screen.get_height()/2
        self.pos_arr = [(self.x, self.y)]
        self.current_movement = 'still'
        self.screen_width = 660
        self.screen_height = 660

    def set_screen_width(self, width):
        self.screen_width = width

    def set_screen_height(self, height):
        self.screen_height = height

    def get_pos(self):
        return self.x, self.y, self.imWidth, self.imHeight

    def get_pos_arr(self):
        return self.pos_arr

    def snake_moving(self):
        self.pos_arr.append((self.x, self.y))
        self.pos_arr.pop(0)

    def move(self, screen):
        """ Метод движения персонажа
            На вход нужно подать на вход объект класса pygame.Screen()
        """
        if ((pygame.key.get_pressed()[pygame.K_RIGHT]
             or pygame.key.get_pressed()[pygame.K_d])
                and self.current_movement != 'left'):
            self.current_movement = 'right'

        if ((pygame.key.get_pressed()[pygame.K_LEFT]
             or pygame.key.get_pressed()[pygame.K_a])
                and self.current_movement != 'right'):
            self.current_movement = 'left'

        if ((pygame.key.get_pressed()[pygame.K_UP]
             or pygame.key.get_pressed()[pygame.K_w])
                and self.current_movement != 'down'):
            self.current_movement = 'up'

        if ((pygame.key.get_pressed()[pygame.K_DOWN]
             or pygame.key.get_pressed()[pygame.K_s])
                and self.current_movement != 'up'):
            self.current_movement = 'down'

        if ((self.current_movement == 'left')
                and self.x > (screen.get_width() - self.screen_width)/2):
            self.x -= self.speed
            self.cropy = 5 * self.imHeight
            self.cropIndex = (self.cropIndex + 1) % 10
            self.snake_moving()
            return True

        if ((self.current_movement == 'right')
                and self.x < (screen.get_width() + self.screen_width)/2 - self.imWidth
                and self.current_movement != 'left'):
            self.x += self.speed
            self.cropy = 7 * self.imHeight
            self.cropIndex = (self.cropIndex + 1) % 10
            self.snake_moving()
            return True

        if ((self.current_movement == 'up')
                and self.y > (screen.get_height() - self.screen_height)/2
                and self.current_movement != 'down'):
            self.y -= self.speed
            self.cropy = 6 * self.imHeight
            self.cropIndex = (self.cropIndex + 1) % 10
            self.snake_moving()
            return True

        if ((self.current_movement == 'down')
                and self.y < (screen.get_height() + self.screen_height)/2 - self.imHeight
                and self.current_movement != 'up'):
            self.y += self.speed
            self.cropy = 4 * self.imHeight
            self.cropIndex = (self.cropIndex + 1) % 10
            self.snake_moving()
            return True

        else:
            self.cropy = 0 * self.imHeight
            self.cropIndex = 0
            return False

    def draw(self, screen):
        """Отрисовка персонажа"""
        for i in range(len(self.pos_arr)-1, -1, -1):
            self.rect = screen.blit(
                self.image,
                (self.pos_arr[i][0], self.pos_arr[i][1]),
                (0, 0, self.imWidth, self.imHeight)
            )

    def draw_polygon(self, screen):
        for i in range(len(self.pos_arr)-1, -1, -1):
            r = 200 + (5 * i) if 200 + (5 * i) <= 240 else 240
            g = 125 + (5 * i) if 125 + (5 * i) <= 240 else 240
            b = 25 + (5 * i) if 25 + (5 * i) <= 230 else 230
            self.image = pygame.draw.circle(
                screen,
                (r, g, b),
                (self.pos_arr[i][0]+15, self.pos_arr[i][1]+15),
                15
            )

    def grow(self):
        self.length += 1
        self.pos_arr.append((self.x, self.y))

    def snake_collision(self):
        x0 = self.pos_arr[-1][0]
        y0 = self.pos_arr[-1][1]
        w = 30
        h = 30
        arr1 = (x0, y0, w, h)
        for i in range(len(self.pos_arr)-1):
            x = self.pos_arr[i][0]
            y = self.pos_arr[i][1]
            arr2 = (x, y, w, h)
            if isAinsideB(arr1, arr2):
                return True
        return False
