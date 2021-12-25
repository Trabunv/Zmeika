import pygame


class Player:
    def __init__(self, screen):
        self.image = pygame.image.load("images\link.png")
        alpha = 0.5
        self.image = pygame.transform.scale(self.image, (self.image.get_width()*alpha, self.image.get_height()*alpha))
        self.rect = 0
        self.speed = 15
        self.length = 1
        self.cropIndex = 0
        self.cropy = 0
        self.imWidth = 120*alpha
        self.imHeight = 130*alpha
        self.x = screen.get_width()/2 - self.imWidth/2
        self.y = screen.get_height()/2 - self.imHeight/2
        self.pos_arr = [(self.x, self.y)]

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
        if pygame.key.get_pressed()[pygame.K_LEFT] and self.x > 0:
            self.x -= self.speed
            self.cropy = 5 * self.imHeight
            self.cropIndex = (self.cropIndex + 1) % 10
            self.snake_moving()

        elif pygame.key.get_pressed()[pygame.K_RIGHT] and self.x < screen.get_width() - self.imWidth:
            self.x += self.speed
            self.cropy = 7 * self.imHeight
            self.cropIndex = (self.cropIndex + 1) % 10
            self.snake_moving()

        elif pygame.key.get_pressed()[pygame.K_UP] and self.y > 0:
            self.y -= self.speed
            self.cropy = 6 * self.imHeight
            self.cropIndex = (self.cropIndex + 1) % 10
            self.snake_moving()

        elif pygame.key.get_pressed()[pygame.K_DOWN] and self.y < screen.get_height() - self.imHeight:
            self.y += self.speed
            self.cropy = 4 * self.imHeight
            self.cropIndex = (self.cropIndex + 1) % 10
            self.snake_moving()
        else:
            self.cropy = 0 * self.imHeight
            self.cropIndex = 0
            # self.snake_moving()

    def draw(self, screen):
        """Отрисовка персонажа"""
        for i in range(len(self.pos_arr)-1, -1, -1):
            self.rect = screen.blit(self.image,
                                    (self.pos_arr[i][0], self.pos_arr[i][1]),
                                    (self.cropIndex * self.imWidth, self.cropy, self.imWidth, self.imHeight)
                                    )

    def grow(self):
        self.length += 1
        self.pos_arr.append((self.x, self.y))
