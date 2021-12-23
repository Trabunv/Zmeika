import pygame


class Player:
    def __init__(self, screen):
        self.image = pygame.image.load("images\link.png")
        alpha = 0.5
        self.image = pygame.transform.scale(self.image, (self.image.get_width()*alpha, self.image.get_height()*alpha))
        # self.image.set_colorkey((255, 255, 255))
        self.speed = 15
        self.cropxIndex = 0
        self.cropy = 0
        self.imWidth = 120*alpha
        self.imHeight = 130*alpha
        self.x = screen.get_width()/2 - self.imWidth/2
        self.y = screen.get_height()/2 - self.imHeight/2

    def getXY(self):
        return self.x, self.y, self.imWidth, self.imHeight

    def move(self, screen):
        """ Метод движения персонажа
            На вход нужно подать на вход объект класса pygame.Screen()
        """
        if pygame.key.get_pressed()[pygame.K_LEFT] and self.x > 0:
            self.x -= self.speed
            self.cropy = 5 * self.imHeight
            self.cropxIndex = (self.cropxIndex + 1) % 10

        elif pygame.key.get_pressed()[pygame.K_RIGHT] and self.x < screen.get_width() - self.imWidth:
            self.x += self.speed
            self.cropy = 7 * self.imHeight
            self.cropxIndex = (self.cropxIndex + 1) % 10

        elif pygame.key.get_pressed()[pygame.K_UP] and self.y > 0:
            self.y -= self.speed
            self.cropy = 6 * self.imHeight
            self.cropxIndex = (self.cropxIndex + 1) % 10

        elif pygame.key.get_pressed()[pygame.K_DOWN] and self.y < screen.get_height() - self.imHeight:
            self.y += self.speed
            self.cropy = 4 * self.imHeight
            self.cropxIndex = (self.cropxIndex + 1) % 10
        else:
            self.cropy = 0 * self.imHeight
            self.cropxIndex = 0

    def draw(self, screen):
        """Отрисовка персонажа"""
        self.rect = screen.blit(self.image,
                                (self.x, self.y),
                                (self.cropxIndex * self.imWidth, self.cropy, self.imWidth, self.imHeight))