import pygame


class Button:
    def __init__(self, x=0, y=0, width=0, height=0):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.button = pygame.Rect(self.x, self.y, self.width, self.height)

    def set_pos(self, x, y):
        self.x = x
        self.y = y

    def set_size(self, width, height):
        self.width = width
        self.height = height

    def is_pressed(self):
        x, y = pygame.mouse.get_pos()
        for i in pg.event.get():
            if i.type == pg.QUIT:
                sys.exit()
            if i.type == pg.MOUSEBUTTONDOWN:
                if (i.button == 0
                    and (x >= self.x and x <= self.x + self.width)
                and (y >= self.y and y <= self.y + self.height)):
                    return True
        return False

